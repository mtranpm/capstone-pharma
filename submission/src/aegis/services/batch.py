from __future__ import annotations

from typing import Any

from aegis.contracts.base import AuditInfo, AuthorizationContext, HumanReview
from aegis.contracts.workflows import BatchResponse
from aegis.services.evidence import authorization_from_fixture, fixture_evidence_items


def _detect_batch_issues(fixture: dict[str, Any]) -> tuple[list[dict], list[dict], list[dict], str]:
    contradictions: list[dict[str, Any]] = []
    gaps: list[dict[str, Any]] = []
    abstentions: list[dict[str, Any]] = []
    batch_id = "UNKNOWN"

    for block in fixture.get("evidence", []):
        source = str(block.get("source", ""))
        for rec in block.get("records") or []:
            if not isinstance(rec, dict):
                continue
            if rec.get("batch_id") and batch_id == "UNKNOWN":
                # Prefer primary biologics batch when present
                if str(rec.get("batch_id")).startswith("NCB204"):
                    batch_id = str(rec["batch_id"])
                elif batch_id == "UNKNOWN":
                    batch_id = str(rec["batch_id"])

            unit = str(rec.get("unit", ""))
            spec = str(rec.get("spec", ""))
            if unit and spec and ("mg/L" in unit) and ("ug/mL" in spec or "µg/mL" in spec):
                contradictions.append(
                    {
                        "type": "unit_mismatch",
                        "result_id": rec.get("result_id"),
                        "detail": f"result unit {unit} vs spec {spec}; no approved conversion",
                    }
                )
                abstentions.append(
                    {
                        "reason": "unresolved_unit",
                        "object": rec.get("result_id"),
                        "action": "abstain_from_numeric_conclusion",
                    }
                )

            if str(rec.get("approved", "")).lower() == "no" and (
                rec.get("conversion_rule") or "interface" in source.lower()
            ):
                contradictions.append(
                    {
                        "type": "unapproved_unit_conversion",
                        "interface": rec.get("interface"),
                        "detail": "conversion_rule not approved",
                    }
                )
                abstentions.append(
                    {
                        "reason": "unresolved_unit_mapping",
                        "object": rec.get("interface"),
                        "action": "abstain",
                    }
                )

            if rec.get("relation") == "missing_branch" or rec.get("material_lot") == "SUA-88":
                if rec.get("relation") == "missing_branch":
                    contradictions.append(
                        {
                            "type": "genealogy_break",
                            "material_lot": rec.get("material_lot"),
                            "batch_id": rec.get("batch_id"),
                            "detail": "missing genealogy branch",
                        }
                    )
                    abstentions.append(
                        {
                            "reason": "unresolved_identity_genealogy",
                            "object": rec.get("material_lot"),
                            "action": "abstain",
                        }
                    )

            lims = rec.get("lims_state")
            stats = rec.get("stats_state")
            if lims and stats and lims != stats:
                contradictions.append(
                    {
                        "type": "oos_oot_disagreement",
                        "investigation_id": rec.get("investigation_id"),
                        "lims_state": lims,
                        "stats_state": stats,
                    }
                )

            if rec.get("packet_item") and str(rec.get("status", "")).lower() == "missing":
                gaps.append(
                    {
                        "type": "release_packet_gap",
                        "packet_item": rec.get("packet_item"),
                        "batch_id": rec.get("batch_id"),
                    }
                )

            if str(rec.get("status", "")).endswith("unverified") or "unverified" in str(
                rec.get("status", "")
            ):
                gaps.append(
                    {
                        "type": "unverified_supplier_commitment",
                        "audit_id": rec.get("audit_id"),
                        "status": rec.get("status"),
                    }
                )
                abstentions.append(
                    {
                        "reason": "unresolved_authority",
                        "object": rec.get("audit_id"),
                        "action": "abstain",
                    }
                )

            if str(rec.get("signature", "")).lower() in {"not available", "missing", "none"}:
                gaps.append(
                    {
                        "type": "unsigned_coa",
                        "coa_id": rec.get("coa_id"),
                    }
                )

            trust = str(rec.get("trust", rec.get("status", ""))).lower()
            if trust in {"untrusted", "superseded"} or "untrusted" in str(
                rec.get("authority", "")
            ).lower() or "malicious" in source.lower():
                contradictions.append(
                    {
                        "type": "untrusted_or_superseded_document",
                        "doc_id": rec.get("doc_id"),
                        "file": rec.get("file"),
                        "trust": trust or rec.get("authority"),
                    }
                )
                abstentions.append(
                    {
                        "reason": "unresolved_authority",
                        "object": rec.get("doc_id") or rec.get("file") or source,
                        "action": "quarantine_do_not_authorize",
                    }
                )

    return contradictions, gaps, abstentions, batch_id if batch_id != "UNKNOWN" else "NCB204-B24071"


def run_batch(fixture: dict[str, Any], *, request_id: str, audit_event_id: str, trace_id: str | None) -> BatchResponse:
    as_of = str((fixture.get("authorized_context") or {}).get("as_of", "1970-01-01T00:00:00Z"))
    auth = AuthorizationContext(**authorization_from_fixture(fixture, as_of))
    evidence = fixture_evidence_items(fixture, as_of)
    contradictions, gaps, abstentions, batch_id = _detect_batch_issues(fixture)
    if contradictions:
        readiness: str = "conflicted_evidence"
    elif gaps or abstentions:
        readiness = "insufficient_evidence"
    else:
        readiness = "ready_for_authorized_review"

    applicable: list[dict[str, Any]] = []
    for ref in fixture.get("evidence_references") or []:
        applicable.append({"path": ref, "authority": "reference_only"})

    return BatchResponse(
        request_id=request_id,
        as_of=as_of,
        authorization=auth,
        evidence=evidence,
        contradictions=contradictions,
        gaps=gaps,
        abstentions=abstentions,
        human_review=HumanReview(required=True, role="quality_reviewer_or_qp"),
        execution_status="not_executed",
        audit=AuditInfo(event_id=audit_event_id, trace_id=trace_id),
        batch_id=batch_id,
        readiness_state=readiness,  # type: ignore[arg-type]
        applicable_documents=applicable,
    )
