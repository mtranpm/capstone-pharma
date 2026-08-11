#!/usr/bin/env python3
"""Export submission_manifest.csv, file_hashes.csv, and package test/eval pointers."""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

SUB = Path(__file__).resolve().parents[1]
EVIDENCE = SUB / "evidence"
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    rows = []
    for path in sorted(SUB.rglob("*")):
        if not path.is_file():
            continue
        if any(p in SKIP_DIRS for p in path.parts):
            continue
        if path.is_relative_to(EVIDENCE) and path.name in {
            "file_hashes.csv",
            "submission_manifest.csv",
        }:
            continue
        rel = path.relative_to(SUB).as_posix()
        digest = sha256_file(path)
        rows.append(
            {
                "path": rel,
                "owner": "aegis_participant",
                "version": "0.2.0",
                "status": "present",
                "sha256": digest,
                "bytes": path.stat().st_size,
            }
        )

    manifest_path = EVIDENCE / "submission_manifest.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["path", "owner", "version", "status", "sha256", "bytes"],
        )
        w.writeheader()
        w.writerows(rows)

    hash_path = EVIDENCE / "file_hashes.csv"
    with hash_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["path", "sha256"])
        w.writeheader()
        for r in rows:
            w.writerow({"path": r["path"], "sha256": r["sha256"]})

    meta = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "file_count": len(rows),
        "evaluation_results": "evidence/evaluation_results.json",
        "test_results": "evidence/test_results.json",
    }
    (EVIDENCE / "export_meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(json.dumps(meta, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
