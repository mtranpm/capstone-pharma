from __future__ import annotations

import sys
from pathlib import Path

SUB = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(SUB / "evaluation"))

from metrics.agreement import compute_agreement


def test_agreement_pending_without_labels() -> None:
    report = compute_agreement(None, None)
    assert report.status == "pending_human_calibration"
    assert report.cohen_kappa is None
    assert report.gwet_ac1 is None
    assert report.n_pairs == 0


def test_agreement_computes_when_labels_provided() -> None:
    human = [1, 1, 0, 0, 1, 0]
    system = [1, 1, 0, 1, 1, 0]
    report = compute_agreement(human, system)
    assert report.status == "computed"
    assert report.n_pairs == 6
    assert report.cohen_kappa is not None
    assert -1.0 <= report.cohen_kappa <= 1.0
    assert report.gwet_ac1 is not None
