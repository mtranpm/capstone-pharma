from __future__ import annotations

import sys
from pathlib import Path

import pytest

SRC = Path(__file__).resolve().parents[2] / "src"
sys.path.insert(0, str(SRC))

from aegis.composition import build_container
from aegis.domain.prohibited import PROHIBITED_ACTIONS
from aegis.services.orchestrator import ProhibitedActionError, run_fixture_workflow


@pytest.mark.parametrize("action", sorted(PROHIBITED_ACTIONS))
def test_each_prohibited_action_blocked(action):
    c = build_container(use_neo4j=False)
    with pytest.raises(ProhibitedActionError):
        run_fixture_workflow(c, "PUB-01", attempted_action=action)


def test_pub09_security_fail_closed():
    c = build_container(use_neo4j=False)
    out = run_fixture_workflow(c, "PUB-09")
    assert out["execution_status"] == "not_executed"
    assert out.get("blocked_actions")
