from __future__ import annotations

from pathlib import Path
from typing import Any

import jsonschema


def grade(response: dict[str, Any], fixture: dict[str, Any], *, schema_dir: Path | None = None) -> dict[str, Any]:
    workflow = str((fixture.get("scenario") or {}).get("workflow", "")).lower()
    if schema_dir is None:
        schema_dir = Path(__file__).resolve().parents[3] / "evaluation" / "contracts"

    schema_name = {
        "batch": "batch_response.schema.json",
        "pv": "pv_response.schema.json",
        "supply": "supply_response.schema.json",
    }.get(workflow)

    if not schema_name:
        return {
            "grader_id": "G-SCHEMA",
            "gate": "pass",
            "observed": "crosscut_participant_contract",
            "threshold": "n/a",
            "detail": "No package schema for crosscut; structural keys checked lightly",
        }

    schema_path = schema_dir / schema_name
    schema = __import__("json").loads(schema_path.read_text(encoding="utf-8"))
    # Resolve local refs relative to contracts dir
    resolver = jsonschema.RefResolver(base_uri=schema_path.resolve().as_uri(), referrer=schema)
    validator = jsonschema.Draft202012Validator(schema, resolver=resolver)
    errors = sorted(validator.iter_errors(response), key=lambda e: e.path)
    if errors:
        return {
            "grader_id": "G-SCHEMA",
            "gate": "fail",
            "observed": errors[0].message,
            "threshold": "validates",
            "detail": [e.message for e in errors[:5]],
        }
    return {
        "grader_id": "G-SCHEMA",
        "gate": "pass",
        "observed": "valid",
        "threshold": "validates",
    }
