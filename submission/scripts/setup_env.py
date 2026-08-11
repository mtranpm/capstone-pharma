#!/usr/bin/env python3
"""Print setup checklist / verify offline path (no secrets written)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

SUB = Path(__file__).resolve().parents[1]
SRC = SUB / "src"


def main() -> int:
    sys.path.insert(0, str(SRC))
    from aegis.composition import build_container

    c = build_container(use_neo4j=False)
    print(
        json.dumps(
            {
                "status": "ok",
                "graph": type(c.graph).__name__,
                "hint": "pip install -r submission/requirements.txt; see runbooks/SETUP.md",
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
