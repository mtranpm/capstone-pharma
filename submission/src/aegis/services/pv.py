from __future__ import annotations

from typing import Any

from aegis.contracts.base import AuditInfo, AuthorizationContext, HumanReview
from aegis.contracts.workflows import PvResponse
from aegis.services.evidence import authorization_from_fixture, fixture_evidence_items


def run_pv(fixture: dict[str, Any], *, request_id: str, audit_event_id: str, trace_id: str | None) -> PvResponse:
    as_of = str((fixture.get("authorized_context") or {}).get("as_of", "1970-01-01T00:00:00Z"))
    auth = AuthorizationContext(**authorization_from_fixture(fixture, as_of))
    evidence = fixture_evidence_items(fixture, as_of)

    case_ids: list[str] = []
    duplicate_candidates: list[dict[str, Any]] = []
    clock_evidence: list[dict[str, Any]] = []
    terminology: list[dict[str, Any]] = []
    listedness_context: list[dict[str, Any]] = []
    source_facts: list[dict[str, Any]] = []
    contradictions: list[dict[str, Any]] = []
    gaps: list[dict[str, Any]] = []
    abstentions: list[dict[str, Any]] = []

    for block in fixture.get("evidence", []):
        source = str(block.get("source", ""))
        for rec in block.get("records") or []:
            if not isinstance(rec, dict):
                continue
            if rec.get("case_id"):
                cid = str(rec["case_id"])
                if cid not in case_ids:
                    case_ids.append(cid)
                source_facts.append({"case_id": cid, "fields": dict(rec)})
            if "duplicate" in source or rec.get("candidate_a") or rec.get("pair"):
                duplicate_candidates.append(dict(rec))
            if "awareness" in str(rec.keys()) or rec.get("awareness_date") or "receipt" in source:
                if rec.get("awareness_date") or rec.get("receipt_date"):
                    clock_evidence.append(dict(rec))
            if "meddra" in source.lower() or rec.get("meddra_version") or "terminology" in source:
                terminology.append(dict(rec))
            if "listedness" in source or rec.get("listedness") or rec.get("label_source"):
                listedness_context.append(dict(rec))

    # Awareness-date conflicts across cases
    awareness = {
        str(f["case_id"]): f["fields"].get("awareness_date")
        for f in source_facts
        if f.get("case_id") and isinstance(f.get("fields"), dict)
    }
    if len({v for v in awareness.values() if v}) > 1:
        contradictions.append({"type": "awareness_date_conflict", "values": awareness})
        abstentions.append(
            {
                "reason": "unresolved_time",
                "object": "awareness_date",
                "action": "abstain_from_clock_conclusion",
            }
        )

    if duplicate_candidates or len(case_ids) > 1:
        gaps.append(
            {
                "type": "duplicate_uncertainty",
                "case_ids": case_ids,
                "note": "candidates require human PV review; no merge performed",
            }
        )

    if not case_ids:
        case_ids = ["UNKNOWN"]
        gaps.append({"type": "missing_case_ids"})

    return PvResponse(
        request_id=request_id,
        as_of=as_of,
        authorization=auth,
        evidence=evidence,
        contradictions=contradictions,
        gaps=gaps,
        abstentions=abstentions,
        human_review=HumanReview(required=True, role="pv_case_intake_reviewer"),
        execution_status="not_executed",
        audit=AuditInfo(event_id=audit_event_id, trace_id=trace_id),
        case_ids=case_ids,
        source_facts=source_facts,
        duplicate_candidates=duplicate_candidates,
        clock_evidence=clock_evidence,
        terminology=terminology,
        listedness_context=listedness_context,
        required_reviews=[
            "duplicate_assessment",
            "clock_confirmation",
            "listedness_human_decision",
        ],
    )
