from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_SRC = Path(__file__).resolve().parents[1]
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from aegis.composition import build_container
from aegis.services.orchestrator import ProhibitedActionError, run_fixture_workflow


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="AEGIS CLI (advisory, offline-capable)")
    sub = parser.add_subparsers(dest="command", required=True)

    p_health = sub.add_parser("health", help="Print local container health")
    p_health.add_argument("--neo4j", action="store_true")

    p_fix = sub.add_parser("fixture", help="Load a public fixture JSON")
    p_fix.add_argument("fixture_id")

    p_run = sub.add_parser("run", help="Run advisory workflow for a fixture")
    p_run.add_argument("fixture_id", help="e.g. PUB-01")
    p_run.add_argument("--attempt-action", default=None, help="Must be blocked if prohibited")
    p_run.add_argument("--out", default=None, help="Write JSON response to path")

    p_ont = sub.add_parser("ontology", help="List ontology via GraphPort")
    p_graph = sub.add_parser("graph", help="Query subgraph via GraphPort")
    p_graph.add_argument("--workflow", default="batch")
    p_graph.add_argument("--focus-id", default=None)

    args = parser.parse_args(argv)
    use_neo4j = bool(getattr(args, "neo4j", False)) if args.command == "health" else None
    container = build_container(use_neo4j=use_neo4j)

    if args.command == "health":
        print(json.dumps({"status": "ok", "graph": type(container.graph).__name__}, indent=2))
        return 0
    if args.command == "fixture":
        data = container.fixtures.load_fixture(args.fixture_id)
        print(json.dumps({"fixture_id": args.fixture_id, "keys": list(data.keys())}, indent=2))
        return 0
    if args.command == "run":
        try:
            payload = run_fixture_workflow(
                container,
                args.fixture_id,
                attempted_action=args.attempt_action,
            )
        except ProhibitedActionError as exc:
            print(json.dumps({"error": "PROHIBITED_ACTION", "message": str(exc)}, indent=2))
            return 2
        text = json.dumps(payload, indent=2)
        if args.out:
            Path(args.out).write_text(text, encoding="utf-8")
        print(text)
        return 0
    if args.command == "ontology":
        print(json.dumps(container.graph.list_ontology(), indent=2))  # type: ignore[attr-defined]
        return 0
    if args.command == "graph":
        print(
            json.dumps(
                container.graph.query_subgraph(args.workflow, args.focus_id),  # type: ignore[attr-defined]
                indent=2,
            )
        )
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
