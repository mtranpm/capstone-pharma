from __future__ import annotations

from typing import Any, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field


class StrictModel(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")


class AuthorizationContext(StrictModel):
    user: str
    purpose: str
    checked_at: str
    decision: Literal["allow", "deny"]
    reason: Optional[str] = None


class IntegrityInfo(StrictModel):
    sha256: str
    source_preserved: bool = True


class EvidenceItem(StrictModel):
    source: str
    record_id: str
    authority: str
    effective_at: Optional[str] = None
    retrieved_at: str
    facts: dict[str, Any] = Field(default_factory=dict)
    integrity: IntegrityInfo


class HumanReview(StrictModel):
    required: bool = True
    role: str


class AuditInfo(StrictModel):
    event_id: str
    trace_id: Optional[str] = None


class TypedError(StrictModel):
    code: str
    message: str
    details: Optional[dict[str, Any]] = None
    request_id: Optional[str] = None
    retryable: bool = False


class ToolCallArgs(StrictModel):
    """Base for validated function-calling / tool arguments."""

    tool_name: str
    arguments: dict[str, Any] = Field(default_factory=dict)
