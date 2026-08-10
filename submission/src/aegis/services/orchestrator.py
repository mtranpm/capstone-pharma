from __future__ import annotations

import os
from typing import Any
from uuid import uuid4

from aegis.composition import AppContainer
from aegis.domain.prohibited import is_prohibited
from aegis.services.batch import run_batch
from aegis.services.crosscut import run_crosscut
from aegis.services.pv import run_pv
from aegis.services.supply import run_supply


class ProhibitedActionError(PermissionError):
    pass


def run_fixture_workflow(
    container: AppContainer,
    fixture_id: str,
    *,
    request_id: str | None = None,
    attempted_action: str | None = None,
) -> dict[str, Any]:
    """Run advisory workflow for a public fixture. Always execution_status=not_executed."""
    if attempted_action and is_prohibited(attempted_action):
        raise ProhibitedActionError(f"prohibited action blocked: {attempted_action}")

    fixture = container.fixtures.load_fixture(fixture_id)
    scenario = fixture.get("scenario") or {}
    workflow = str(scenario.get("workflow", "")).lower()
    req = request_id or f"REQ-{uuid4().hex[:10]}"
    trace_id = f"tr-{uuid4().hex[:12]}"
    span = container.telemetry.start_span(
        "workflow.run",
        {
            "fixture_id": fixture_id,
            "workflow": workflow,
            "ai_disabled": os.environ.get("AEGIS_AI_DISABLED", ""),
        },
    )

    try:
        # Optional LLM path is stubbed: AI-disabled always uses deterministic reasoners.
        _ = os.environ.get("AEGIS_AI_DISABLED", "").lower() in {"1", "true", "yes"}

        if workflow == "batch":
            result_model = run_batch(
                fixture,
                request_id=req,
                audit_event_id="pending",
                trace_id=trace_id,
            )
            payload = result_model.model_dump()
        elif workflow == "pv":
            result_model = run_pv(
                fixture,
                request_id=req,
                audit_event_id="pending",
                trace_id=trace_id,
            )
            payload = result_model.model_dump()
        elif workflow == "supply":
            result_model = run_supply(
                fixture,
                request_id=req,
                audit_event_id="pending",
                trace_id=trace_id,
            )
            payload = result_model.model_dump()
        else:
            payload = run_crosscut(
                fixture,
                request_id=req,
                audit_event_id="pending",
                trace_id=trace_id,
            )

        event_id = container.audit.emit(
            {
                "request_id": req,
                "fixture_id": fixture_id,
                "workflow": payload.get("workflow"),
                "execution_status": "not_executed",
                "trace_id": trace_id,
                "readiness_state": payload.get("readiness_state"),
            }
        )
        payload["audit"] = {"event_id": event_id, "trace_id": trace_id}
        if payload.get("execution_status") != "not_executed":
            raise RuntimeError("invariant violation: execution_status must be not_executed")
        return payload
    finally:
        container.telemetry.end_span(span)
