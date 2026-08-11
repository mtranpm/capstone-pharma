from __future__ import annotations

from typing import Any, Callable

from .g_schema import grade as g_schema
from .g_boundaries import (
    grade_abstention,
    grade_authority,
    grade_batch,
    grade_clinical,
    grade_exec,
    grade_finops,
    grade_human,
    grade_owasp,
    grade_privacy,
    grade_provenance,
    grade_pv,
    grade_reliability,
    grade_supply,
)
from .g_iso_eu import grade_iso_eu
from .g_otel import grade_otel

GraderFn = Callable[[dict[str, Any], dict[str, Any]], dict[str, Any]]

GRADERS: dict[str, GraderFn] = {
    "G-SCHEMA": g_schema,
    "G-EXEC-BOUNDARY": grade_exec,
    "G-HUMAN-REVIEW": grade_human,
    "G-PROVENANCE": grade_provenance,
    "G-AUTHORITY": grade_authority,
    "G-ABSTENTION": grade_abstention,
    "G-BATCH-READINESS": grade_batch,
    "G-PV-BOUNDARY": grade_pv,
    "G-SUPPLY-BOUNDARY": grade_supply,
    "G-OWASP-LLM": grade_owasp,
    "G-PRIVACY": grade_privacy,
    "G-RELIABILITY": grade_reliability,
    "G-FINOPS": grade_finops,
    "G-CLINICAL": grade_clinical,
    "G-OTEL": grade_otel,
    "G-ISO-EU": grade_iso_eu,
}


def run_all_graders(
    response: dict[str, Any],
    fixture: dict[str, Any],
    *,
    schema_dir: Any = None,
) -> list[dict[str, Any]]:
    results = []
    for gid, fn in GRADERS.items():
        if gid == "G-SCHEMA":
            results.append(fn(response, fixture, schema_dir=schema_dir))  # type: ignore[call-arg]
        else:
            results.append(fn(response, fixture))
    return results
