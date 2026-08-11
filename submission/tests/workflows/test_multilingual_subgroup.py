from __future__ import annotations

import sys
from pathlib import Path

import pytest

SRC = Path(__file__).resolve().parents[2] / "src"
sys.path.insert(0, str(SRC))

from aegis.composition import build_container
from aegis.services.orchestrator import run_fixture_workflow


@pytest.fixture
def container():
    return build_container(use_neo4j=False)


def _languages_in_fixture(fixture: dict) -> set[str]:
    langs: set[str] = set()
    for block in fixture.get("evidence") or []:
        for rec in block.get("records") or []:
            if isinstance(rec, dict) and rec.get("language"):
                langs.add(str(rec["language"]))
    return langs


def test_pub04_preserves_multilingual_languages(container):
    """PV-02: original language metadata must appear; no silent translation field."""
    fixture = container.fixtures.load_fixture("PUB-04")
    expected = _languages_in_fixture(fixture)
    assert expected, "PUB-04 fixture should carry language metadata"

    out = run_fixture_workflow(container, "PUB-04")
    observed: set[str] = set()
    for fact in out.get("source_facts") or []:
        fields = fact.get("fields") or {}
        if fields.get("language"):
            observed.add(str(fields["language"]))

    assert expected <= observed
    # Must not invent a single "translated_to" that replaces originals
    assert "translated_narrative" not in out
    assert out.get("execution_status") == "not_executed"


def test_subgroup_languages_reported_not_collapsed(container):
    """Subgroup analysis stub: languages remain distinct strata in facts."""
    out = run_fixture_workflow(container, "PUB-04")
    langs = []
    for fact in out.get("source_facts") or []:
        lang = (fact.get("fields") or {}).get("language")
        if lang:
            langs.append(str(lang))
    assert len(set(langs)) >= 2
    # Subgroup note for TEVV — abstain from cross-language merge
    assert out["human_review"]["required"] is True
