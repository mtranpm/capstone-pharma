from __future__ import annotations

from aegis.adapters.graph_memory import InMemoryGraphStub
from aegis.composition import build_container
from aegis.ports import FixturePort, GraphPort


def test_in_memory_graph_satisfies_port() -> None:
    graph = InMemoryGraphStub()
    assert isinstance(graph, GraphPort)
    ont = graph.list_ontology()
    assert "classes" in ont
    sub = graph.query_subgraph("batch", "NCB204-B24071")
    assert sub["mode"] == "in_memory_stub"
    assert sub["advisory"] is True


def test_container_uses_stub_by_default() -> None:
    c = build_container(use_neo4j=False)
    assert isinstance(c.fixtures, FixturePort)
    assert isinstance(c.graph, GraphPort)
