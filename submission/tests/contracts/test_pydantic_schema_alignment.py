from __future__ import annotations

import json
from pathlib import Path

import jsonschema

from aegis.contracts.base import AuthorizationContext, AuditInfo, EvidenceItem, HumanReview, IntegrityInfo
from aegis.contracts.workflows import BatchResponse

ROOT = Path(__file__).resolve().parents[3]


def _batch_schema() -> dict:
    schema_path = ROOT / "evaluation" / "contracts" / "batch_response.schema.json"
    evidence_path = ROOT / "evaluation" / "contracts" / "evidence_item.schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
    # Local resolver: inline evidence ref for unit test simplicity
    schema["properties"]["evidence"]["items"] = evidence
    return schema


def test_batch_response_model_validates_against_json_schema() -> None:
    auth = AuthorizationContext(
        user="tester",
        purpose="training",
        checked_at="2026-08-01T08:00:00Z",
        decision="allow",
        reason="synthetic",
    )
    model = BatchResponse(
        request_id="REQ-1",
        as_of="2026-08-01T08:00:00Z",
        authorization=auth,
        evidence=[
            EvidenceItem(
                source="data/batches.csv",
                record_id="NCB204-B24071",
                authority="synthetic",
                effective_at=None,
                retrieved_at="2026-08-01T08:00:00Z",
                facts={},
                integrity=IntegrityInfo(sha256="0" * 64, source_preserved=True),
            )
        ],
        contradictions=[],
        gaps=[],
        abstentions=[],
        human_review=HumanReview(required=True, role="quality_reviewer"),
        execution_status="not_executed",
        audit=AuditInfo(event_id="AUD-1"),
        batch_id="NCB204-B24071",
        readiness_state="conflicted_evidence",
        applicable_documents=[],
    )
    payload = model.model_dump(mode="json")
    jsonschema.validate(instance=payload, schema=_batch_schema())
