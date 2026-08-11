#!/usr/bin/env python3
"""Evaluate PUB-01..15 with deterministic graders; write evidence/evaluation_results.json."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SUB = ROOT / "submission"
SRC = SUB / "src"
sys.path.insert(0, str(SRC))
sys.path.insert(0, str(SUB / "evaluation"))

from aegis.composition import build_container  # noqa: E402
from aegis.services.orchestrator import run_fixture_workflow  # noqa: E402
from graders.registry import run_all_graders  # noqa: E402
from metrics.agreement import compute_agreement  # noqa: E402


def main() -> int:
    container = build_container(use_neo4j=False)
    schema_dir = ROOT / "evaluation" / "contracts"
    fixtures = [f"PUB-{i:02d}" for i in range(1, 16)]
    evidence_dir = SUB / "evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    runs_dir = evidence_dir / "runs"
    runs_dir.mkdir(parents=True, exist_ok=True)

    all_results: list[dict] = []
    hard_fail = False

    for fid in fixtures:
        fixture = container.fixtures.load_fixture(fid)
        response = run_fixture_workflow(container, fid)
        (runs_dir / f"{fid}.json").write_text(json.dumps(response, indent=2), encoding="utf-8")
        grades = run_all_graders(response, fixture, schema_dir=schema_dir)
        for g in grades:
            g["fixture_id"] = fid
            g["evidence_path"] = str((runs_dir / f"{fid}.json").relative_to(SUB))
            all_results.append(g)
            if g["gate"] == "fail" and g["grader_id"] in {
                "G-SCHEMA",
                "G-EXEC-BOUNDARY",
                "G-AUTHORITY",
                "G-BATCH-READINESS",
                "G-PV-BOUNDARY",
                "G-SUPPLY-BOUNDARY",
            }:
                # Only hard-fail when grader applies (not skipped via detail)
                if g.get("observed") != "skipped" and "skipped" not in str(g.get("threshold", "")):
                    if g.get("observed") != "skipped":
                        if str(g.get("threshold", "")).endswith("only") is False or g["gate"] == "fail":
                            # skip when threshold says "batch only" style and observed skipped
                            if g.get("observed") != "skipped":
                                hard_fail = True if g["gate"] == "fail" and g.get("observed") != "skipped" else hard_fail

    # Cleaner hard-fail pass
    hard_fail = False
    for g in all_results:
        if g["gate"] != "fail":
            continue
        if g.get("observed") == "skipped":
            continue
        if g["grader_id"] in {
            "G-SCHEMA",
            "G-EXEC-BOUNDARY",
            "G-AUTHORITY",
            "G-BATCH-READINESS",
            "G-PV-BOUNDARY",
            "G-SUPPLY-BOUNDARY",
            "G-HUMAN-REVIEW",
            "G-PROVENANCE",
        }:
            hard_fail = True

    # M-AGREE: no fabricated κ — compute only when dual labels exist (currently none).
    agree = compute_agreement(None, None)
    out = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "fixture_count": len(fixtures),
        "results": all_results,
        "hard_gate": "fail" if hard_fail else "pass",
        "graders_registered": sorted({g["grader_id"] for g in all_results}),
        "agreement_metrics": {
            "m_agree": agree.status,
            "cohen_kappa": agree.cohen_kappa,
            "weighted_kappa": agree.weighted_kappa,
            "gwet_ac1": agree.gwet_ac1,
            "n_pairs": agree.n_pairs,
            "soft_threshold": agree.soft_threshold,
            "note": agree.notes,
            "evidence": "evidence/m_agree_pending_human_calibration.md",
        },
    }
    out_path = evidence_dir / "evaluation_results.json"
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps({"hard_gate": out["hard_gate"], "path": str(out_path)}, indent=2))
    return 1 if hard_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
