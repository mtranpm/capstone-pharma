from __future__ import annotations

from typing import Any

from aegis.contracts.base import AuditInfo, AuthorizationContext, HumanReview
from aegis.contracts.workflows import SupplyResponse
from aegis.services.evidence import authorization_from_fixture, fixture_evidence_items


def run_supply(fixture: dict[str, Any], *, request_id: str, audit_event_id: str, trace_id: str | None) -> SupplyResponse:
    as_of = str((fixture.get("authorized_context") or {}).get("as_of", "1970-01-01T00:00:00Z"))
    auth = AuthorizationContext(**authorization_from_fixture(fixture, as_of))
    evidence = fixture_evidence_items(fixture, as_of)

    constraints: list[dict[str, Any]] = []
    quality_holds: list[dict[str, Any]] = []
    contradictions: list[dict[str, Any]] = []
    gaps: list[dict[str, Any]] = []
    abstentions: list[dict[str, Any]] = []
    event_id = str((fixture.get("scenario") or {}).get("id", "SUPPLY-EVENT"))

    inventory_rows: list[dict[str, Any]] = []
    demand_rows: list[dict[str, Any]] = []
    shipment_pallets: dict[str, str] = {}
    logger_pallets: list[tuple[str, str]] = []

    for block in fixture.get("evidence", []):
        source = str(block.get("source", ""))
        for rec in block.get("records") or []:
            if not isinstance(rec, dict):
                continue
            if "inventory" in source:
                inventory_rows.append(dict(rec))
                status = str(rec.get("status", rec.get("quality_status", ""))).lower()
                if "hold" in status or status in {"quarantine", "rejected"}:
                    quality_holds.append(dict(rec))
            if "shipment" in source:
                status = str(rec.get("status", "")).lower()
                if "hold" in status or status in {"quarantine", "rejected", "customs_hold"}:
                    quality_holds.append(dict(rec))
                if rec.get("shipment_id") and rec.get("pallet"):
                    shipment_pallets[str(rec["shipment_id"])] = str(rec["pallet"])
            if "demand" in source or "forecast" in source:
                demand_rows.append(dict(rec))
            if "constraint" in source or "allocation" in source:
                constraints.append(dict(rec))
            if "logger" in source or rec.get("logger"):
                if rec.get("pallet") and rec.get("logger"):
                    logger_pallets.append((str(rec["logger"]), str(rec["pallet"])))
                tz = str(rec.get("timezone", "")).lower()
                if "unknown" in tz or tz in {"local_unknown", ""}:
                    contradictions.append(
                        {
                            "type": "cold_chain_clock_dispute",
                            "logger": rec.get("logger"),
                            "timezone": rec.get("timezone"),
                        }
                    )
                    abstentions.append(
                        {
                            "reason": "unresolved_time",
                            "object": rec.get("logger") or "cold_chain_logger",
                            "action": "abstain",
                        }
                    )
            if rec.get("logger_time") and rec.get("pallet_time") and rec["logger_time"] != rec["pallet_time"]:
                contradictions.append(
                    {
                        "type": "cold_chain_clock_dispute",
                        "detail": rec,
                    }
                )
                abstentions.append(
                    {
                        "reason": "unresolved_time",
                        "object": "cold_chain_logger",
                        "action": "abstain",
                    }
                )

    # Logger–pallet association mismatch (e.g. SH-901 / LG-31 → P-88 vs P-89)
    expected = set(shipment_pallets.values())
    for logger_id, pallet in logger_pallets:
        if expected and pallet not in expected:
            contradictions.append(
                {
                    "type": "logger_pallet_mismatch",
                    "logger": logger_id,
                    "logger_pallet": pallet,
                    "shipment_pallets": sorted(expected),
                }
            )
            abstentions.append(
                {
                    "reason": "unresolved_identity",
                    "object": logger_id,
                    "action": "abstain_quality_assessment_required",
                }
            )

    # Non-executing options only — never allocate/ship
    options: list[dict[str, Any]] = [
        {
            "option_id": "OPT-REVIEW-RELEASED-ONLY",
            "status": "draft",
            "description": "Prioritise review of already-released stock visibility for human planners",
            "executes": False,
            "side_effects": [],
        },
        {
            "option_id": "OPT-ETHICS-ESCALATION",
            "status": "draft",
            "description": "Escalate trial vs compassionate vs commercial demand conflict to ethics/Quality",
            "executes": False,
            "side_effects": [],
        },
        {
            "option_id": "OPT-ABSTAIN-SHORTFALL",
            "status": "draft",
            "description": "Document shortfall; do not reserve, allocate, or ship",
            "executes": False,
            "side_effects": [],
        },
    ]

    if quality_holds:
        constraints.append({"type": "quality_hold_blocks_execution", "holds": quality_holds})
        abstentions.append(
            {
                "reason": "quality_status_unresolved_for_execution",
                "action": "options_only_no_allocation",
            }
        )

    if not constraints and demand_rows:
        constraints.append({"type": "demand_exceeds_or_conflicts", "demand_rows": len(demand_rows)})

    if contradictions:
        gaps.append({"type": "cold_chain_or_identity_gap"})

    approvals_required = [
        "inventory_status_change",
        "allocation",
        "shipment",
        "recall_initiation",
        "quality_assessment",
    ]

    return SupplyResponse(
        request_id=request_id,
        as_of=as_of,
        authorization=auth,
        evidence=evidence,
        contradictions=contradictions,
        gaps=gaps,
        abstentions=abstentions,
        human_review=HumanReview(required=True, role="supply_planning_with_quality"),
        execution_status="not_executed",
        audit=AuditInfo(event_id=audit_event_id, trace_id=trace_id),
        event_id=event_id,
        options=options,
        constraints=constraints,
        approvals_required=approvals_required,
        quality_holds=quality_holds,
        no_side_effects=True,
    )
