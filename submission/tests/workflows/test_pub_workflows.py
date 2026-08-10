from __future__ import annotations

import sys
from pathlib import Path

import pytest

SRC = Path(__file__).resolve().parents[2] / "src"
sys.path.insert(0, str(SRC))

from aegis.composition import build_container
from aegis.domain.prohibited import is_prohibited
from aegis.services.orchestrator import ProhibitedActionError, run_fixture_workflow


@pytest.fixture
def container():
    return build_container(use_neo4j=False)


def test_pub01_conflicted_not_disposition(container):
    out = run_fixture_workflow(container, "PUB-01")
    assert out["execution_status"] == "not_executed"
    assert out["human_review"]["required"] is True
    assert out["readiness_state"] in {"conflicted_evidence", "insufficient_evidence"}
    assert out["workflow"] == "batch_evidence"


def test_pub04_pv_boundary(container):
    out = run_fixture_workflow(container, "PUB-04")
    assert out["execution_status"] == "not_executed"
    assert "final_seriousness" not in out
    assert out["human_review"]["required"] is True


def test_pub07_supply_non_executing(container):
    out = run_fixture_workflow(container, "PUB-07")
    assert out["execution_status"] == "not_executed"
    assert out["no_side_effects"] is True
    assert all(not o.get("executes") for o in out["options"])


def test_prohibited_action_blocked(container):
    with pytest.raises(ProhibitedActionError):
        run_fixture_workflow(container, "PUB-01", attempted_action="release_batch")
    assert is_prohibited("allocate_stock")


@pytest.mark.parametrize("fid", [f"PUB-{i:02d}" for i in range(1, 16)])
def test_all_public_fixtures_not_executed(container, fid):
    out = run_fixture_workflow(container, fid)
    assert out["execution_status"] == "not_executed"
    assert out["human_review"]["required"] is True
