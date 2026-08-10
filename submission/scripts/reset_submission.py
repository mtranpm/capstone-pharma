#!/usr/bin/env python3
"""Reset generated evidence/runs (does not touch challenge package outside submission/)."""
from __future__ import annotations

import shutil
from pathlib import Path

EVIDENCE = Path(__file__).resolve().parents[1] / "evidence"
RUNS = EVIDENCE / "runs"


def main() -> int:
    if RUNS.exists():
        shutil.rmtree(RUNS)
    for name in (
        "evaluation_results.json",
        "test_results.json",
        "file_hashes.csv",
        "submission_manifest.csv",
        "export_meta.json",
    ):
        p = EVIDENCE / name
        if p.exists():
            p.unlink()
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    print("reset complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
