from __future__ import annotations

from typing import Any

# Mirror telemetry redaction allow-deny set (keep grader import-light).
FORBIDDEN_KEYS = {
    "password",
    "api_key",
    "apikey",
    "secret",
    "authorization_header",
    "system_prompt",
    "raw_narrative",
    "ssn",
    "connection_string",
}


def _base(ok: bool, observed: Any, threshold: str, detail: str = "") -> dict[str, Any]:
    return {
        "grader_id": "G-OTEL",
        "gate": "pass" if ok else "fail",
        "observed": observed,
        "threshold": threshold,
        "detail": detail,
    }


def grade_otel(response: dict[str, Any], _fixture: dict[str, Any]) -> dict[str, Any]:
    """
    Assert audit↔trace correlation and absence of forbidden telemetry attributes.

    Scopes checks to telemetry/audit attribute bags — not clinical evidence field names.
    Offline console/file telemetry is sufficient; does not require a live OTLP collector.
    """
    audit = response.get("audit") or {}
    if not isinstance(audit, dict):
        return _base(False, type(audit).__name__, "audit object with trace_id+event_id")

    trace_id = audit.get("trace_id")
    event_id = audit.get("event_id")
    if not trace_id or not event_id:
        return _base(
            False,
            {"trace_id": bool(trace_id), "event_id": bool(event_id)},
            "audit.trace_id + audit.event_id present",
            "missing correlation ids",
        )

    # Attribute bags that must stay redacted
    attr_bags: list[dict[str, Any]] = []
    for key in ("telemetry", "span_attributes", "otel_attributes", "metrics_attributes"):
        bag = response.get(key)
        if isinstance(bag, dict):
            attr_bags.append(bag)
    # Audit may carry optional attributes
    for key in ("attributes", "span_attributes"):
        bag = audit.get(key)
        if isinstance(bag, dict):
            attr_bags.append(bag)

    hits: list[str] = []
    for bag in attr_bags:
        for k in bag:
            lowered = str(k).lower()
            if lowered in FORBIDDEN_KEYS or any(m in lowered for m in ("password", "secret", "system_prompt")):
                hits.append(lowered)

    # Top-level packet must not expose secrets as sibling fields
    for k in response:
        lowered = str(k).lower()
        if lowered in FORBIDDEN_KEYS:
            hits.append(lowered)

    if hits:
        return _base(False, hits[:10], "no forbidden telemetry attribute keys", "forbidden keys present")

    wf = str(response.get("workflow", "")).lower()
    if "privacy" in wf:
        findings = response.get("findings") or []
        blob = str(findings).lower()
        if "narrative" not in blob and "telemetry" not in blob and "minimisation" not in blob:
            return _base(
                False,
                "privacy_findings_missing_telemetry_control",
                "privacy findings cite telemetry minimisation",
            )

    return _base(
        True,
        {"trace_id": True, "event_id": True, "forbidden_hits": 0},
        "correlation + redaction allow-list",
        "offline-safe",
    )
