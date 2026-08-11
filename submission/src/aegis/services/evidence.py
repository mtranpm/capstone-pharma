from __future__ import annotations

from typing import Any

from aegis.contracts.base import EvidenceItem, IntegrityInfo


def fixture_evidence_items(fixture: dict[str, Any], retrieved_at: str) -> list[EvidenceItem]:
    """Map fixture evidence blocks to contract EvidenceItem rows (verbatim facts)."""
    items: list[EvidenceItem] = []
    for block in fixture.get("evidence", []):
        source = str(block.get("source", "unknown"))
        sha = str(block.get("sha256", "0" * 64))
        records = block.get("records")
        if not records:
            if block.get("text") is not None:
                records = [{"text_excerpt": str(block.get("text"))[:240]}]
            else:
                records = [{}]
        for idx, record in enumerate(records):
            if not isinstance(record, dict):
                record = {"value": record}
            record_id = str(
                record.get("batch_id")
                or record.get("case_id")
                or record.get("result_id")
                or record.get("investigation_id")
                or record.get("movement_id")
                or record.get("coa_id")
                or record.get("audit_id")
                or record.get("event_id")
                or record.get("shipment_id")
                or record.get("doc_id")
                or record.get("logger")
                or f"{source}#{idx}"
            )
            authority = "fixture_provided"
            trust = str(record.get("trust", record.get("status", ""))).lower()
            if (
                "untrusted" in source.lower()
                or "malicious" in source.lower()
                or "poison" in source.lower()
                or trust in {"untrusted", "superseded"}
                or "untrusted" in str(record.get("authority", "")).lower()
            ):
                authority = "untrusted"
            items.append(
                EvidenceItem(
                    source=source,
                    record_id=record_id,
                    authority=authority,
                    effective_at=record.get("effective") if isinstance(record.get("effective"), str) else None,
                    retrieved_at=retrieved_at,
                    facts=dict(record),
                    integrity=IntegrityInfo(sha256=sha, source_preserved=True),
                )
            )
    return items


def authorization_from_fixture(fixture: dict[str, Any], checked_at: str) -> dict[str, Any]:
    ctx = fixture.get("authorized_context") or {}
    decision = "allow"
    if str(ctx.get("execution", "")).lower() in {"enabled", "execute"}:
        # Execution requested in fixture context → still deny execution path; allow advisory
        decision = "allow"
    return {
        "user": str(ctx.get("user", "unknown")),
        "purpose": str(ctx.get("purpose", "unspecified")),
        "checked_at": checked_at,
        "decision": decision,
        "reason": "advisory_only",
    }
