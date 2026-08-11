#!/usr/bin/env python3
"""Project selected relationships into Neo4j (advisory). Offline: prints stub plan."""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))


def plan() -> dict:
    return {
        "mode": "advisory_projection",
        "nodes": ["Product", "Batch", "SafetyCase", "Shipment", "KnowledgeDocument"],
        "relationships": ["OF_PRODUCT", "HAS_GENEALOGY", "SUPPORTED_BY", "RELATED_CASE"],
        "rule": "Neo4j is derived/advisory; CSV/fixture evidence remains system of record",
        "cypher_policy": "allow_listed_parameterized_only",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Apply to Neo4j when configured")
    args = parser.parse_args()
    payload = plan()
    if not args.apply or os.environ.get("AEGIS_USE_NEO4J", "").lower() not in {"1", "true", "yes"}:
        payload["applied"] = False
        payload["note"] = "Dry-run / offline stub — set AEGIS_USE_NEO4J=1 and --apply to load"
        print(json.dumps(payload, indent=2))
        return 0

    from aegis.adapters.graph_neo4j import Neo4jGraphAdapter

    adapter = Neo4jGraphAdapter(
        uri=os.environ.get("NEO4J_URI", "bolt://localhost:7687"),
        user=os.environ.get("NEO4J_USER", "neo4j"),
        password=os.environ.get("NEO4J_PASSWORD", ""),
    )
    try:
        result = adapter.seed_from_plan(payload)
        payload.update(result)
        payload["applied"] = True
    except Exception as exc:  # noqa: BLE001
        payload["applied"] = False
        payload["error"] = str(exc)
        print(json.dumps(payload, indent=2))
        return 1
    finally:
        adapter.close()
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
