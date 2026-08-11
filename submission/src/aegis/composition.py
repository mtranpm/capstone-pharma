from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from aegis.adapters.audit import InMemoryAuditAdapter
from aegis.adapters.authority import StaticAuthorityAdapter
from aegis.adapters.fixture_loader import FileFixtureAdapter
from aegis.adapters.graph_memory import InMemoryGraphStub
from aegis.adapters.tool_manifest import FileToolManifestAdapter
from aegis.telemetry.console import ConsoleTelemetryAdapter


def repo_root() -> Path:
    # submission/src/aegis/composition.py -> parents: aegis, src, submission, repo
    return Path(__file__).resolve().parents[3]


@dataclass
class AppContainer:
    fixtures: FileFixtureAdapter
    authority: StaticAuthorityAdapter
    graph: object
    audit: InMemoryAuditAdapter
    telemetry: ConsoleTelemetryAdapter
    tools: FileToolManifestAdapter


def build_container(*, use_neo4j: bool | None = None) -> AppContainer:
    root = repo_root()
    fixtures_dir = root / "evaluation" / "public_fixtures"
    if use_neo4j is None:
        use_neo4j = os.environ.get("AEGIS_USE_NEO4J", "").lower() in {"1", "true", "yes"}

    if use_neo4j:
        from aegis.adapters.graph_neo4j import Neo4jGraphAdapter

        graph: object = Neo4jGraphAdapter(
            uri=os.environ.get("NEO4J_URI", "bolt://localhost:7687"),
            user=os.environ.get("NEO4J_USER", "neo4j"),
            password=os.environ.get("NEO4J_PASSWORD", ""),
        )
    else:
        graph = InMemoryGraphStub()

    return AppContainer(
        fixtures=FileFixtureAdapter(fixtures_dir),
        authority=StaticAuthorityAdapter(),
        graph=graph,
        audit=InMemoryAuditAdapter(),
        telemetry=ConsoleTelemetryAdapter(),
        tools=FileToolManifestAdapter(),
    )
