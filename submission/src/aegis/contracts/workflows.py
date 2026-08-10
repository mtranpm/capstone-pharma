from __future__ import annotations

from typing import Any, Literal, Optional

from aegis.contracts.base import (
    AuditInfo,
    AuthorizationContext,
    EvidenceItem,
    HumanReview,
    StrictModel,
)


class WorkflowRequest(StrictModel):
    request_id: str
    as_of: str
    authorization: AuthorizationContext
    fixture_id: Optional[str] = None


class BatchResponse(StrictModel):
    request_id: str
    workflow: Literal["batch_evidence"] = "batch_evidence"
    as_of: str
    authorization: AuthorizationContext
    evidence: list[EvidenceItem]
    contradictions: list[dict[str, Any]]
    gaps: list[dict[str, Any]]
    abstentions: list[dict[str, Any]]
    human_review: HumanReview
    execution_status: Literal["not_executed"] = "not_executed"
    audit: AuditInfo
    batch_id: str
    readiness_state: Literal[
        "ready_for_authorized_review",
        "conflicted_evidence",
        "insufficient_evidence",
    ]
    applicable_documents: list[dict[str, Any]]


class PvResponse(StrictModel):
    request_id: str
    workflow: Literal["pv_intake"] = "pv_intake"
    as_of: str
    authorization: AuthorizationContext
    evidence: list[EvidenceItem]
    contradictions: list[dict[str, Any]]
    gaps: list[dict[str, Any]]
    abstentions: list[dict[str, Any]]
    human_review: HumanReview
    execution_status: Literal["not_executed"] = "not_executed"
    audit: AuditInfo
    case_ids: list[str]
    source_facts: list[dict[str, Any]]
    duplicate_candidates: list[dict[str, Any]]
    clock_evidence: list[dict[str, Any]]
    terminology: list[dict[str, Any]]
    listedness_context: list[dict[str, Any]]
    required_reviews: list[str]


class SupplyResponse(StrictModel):
    request_id: str
    workflow: Literal["supply_options"] = "supply_options"
    as_of: str
    authorization: AuthorizationContext
    evidence: list[EvidenceItem]
    contradictions: list[dict[str, Any]]
    gaps: list[dict[str, Any]]
    abstentions: list[dict[str, Any]]
    human_review: HumanReview
    execution_status: Literal["not_executed"] = "not_executed"
    audit: AuditInfo
    event_id: str
    options: list[dict[str, Any]]
    constraints: list[dict[str, Any]]
    approvals_required: list[str]
    quality_holds: list[dict[str, Any]]
    no_side_effects: bool = True
