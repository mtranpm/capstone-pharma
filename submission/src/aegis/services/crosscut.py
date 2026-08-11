from __future__ import annotations

import os
from typing import Any

from aegis.domain.prohibited import PROHIBITED_ACTIONS, is_prohibited
from aegis.services.evidence import authorization_from_fixture, fixture_evidence_items


def run_crosscut(fixture: dict[str, Any], *, request_id: str, audit_event_id: str, trace_id: str | None) -> dict[str, Any]:
    """Advisory non-executing packet for PUB-09..15 (participant-defined contract)."""
    scenario = fixture.get("scenario") or {}
    workflow = str(scenario.get("workflow", "crosscut"))
    as_of = str((fixture.get("authorized_context") or {}).get("as_of", "1970-01-01T00:00:00Z"))
    ai_disabled = os.environ.get("AEGIS_AI_DISABLED", "").lower() in {"1", "true", "yes"}

    blocked = sorted(PROHIBITED_ACTIONS)
    findings: list[dict[str, Any]] = []

    if workflow == "security":
        findings.append(
            {
                "control": "LLM01/LLM03/LLM06",
                "result": "fail_closed",
                "detail": "Untrusted tool/prompt content quarantined; no regulated execution",
            }
        )
    if workflow == "reliability" or ai_disabled:
        findings.append(
            {
                "control": "AI_DISABLED_CONTINUITY",
                "result": "deterministic_path_active",
                "ai_disabled": True,
            }
        )
    if workflow == "privacy":
        findings.append(
            {
                "control": "purpose_binding",
                "result": "minimisation_applied",
                "detail": "No raw narrative export in telemetry attributes",
            }
        )
    if workflow == "agent":
        findings.append(
            {
                "control": "budget_stop",
                "max_steps": int(os.environ.get("AEGIS_MAX_STEPS", "8")),
                "result": "bounded",
            }
        )
    if workflow == "finops":
        findings.append(
            {
                "control": "token_budget",
                "max_tokens": int(os.environ.get("AEGIS_MAX_TOKENS", "4000")),
                "result": "within_budget_or_stop",
            }
        )
    if workflow == "clinical":
        findings.append(
            {
                "control": "no_eligibility_decision",
                "result": "evidence_only",
            }
        )
    if workflow == "integration":
        findings.append(
            {
                "control": "typed_clients_no_silent_merge",
                "result": "ports_only",
            }
        )

    # Attempted prohibited action detection from prompt text
    prompt = str(scenario.get("prompt", "")).lower()
    for action in PROHIBITED_ACTIONS:
        token = action.replace("_", " ")
        if token in prompt or action in prompt:
            findings.append({"blocked_action": action, "is_prohibited": is_prohibited(action)})

    evidence = [e.model_dump() for e in fixture_evidence_items(fixture, as_of)]

    return {
        "request_id": request_id,
        "workflow": f"crosscut_{workflow}",
        "as_of": as_of,
        "authorization": authorization_from_fixture(fixture, as_of),
        "evidence": evidence,
        "contradictions": [],
        "gaps": [],
        "abstentions": [{"reason": "crosscut_advisory_only", "action": "human_review"}],
        "human_review": {"required": True, "role": "control_owner"},
        "execution_status": "not_executed",
        "audit": {"event_id": audit_event_id, "trace_id": trace_id},
        "findings": findings,
        "blocked_actions": blocked,
        "no_side_effects": True,
        "ai_disabled": ai_disabled,
    }
