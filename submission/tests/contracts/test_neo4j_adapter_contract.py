from __future__ import annotations

import sys
from pathlib import Path

SRC = Path(__file__).resolve().parents[2] / "src"
sys.path.insert(0, str(SRC))

from aegis.adapters.graph_neo4j import ALLOWED_QUERIES, Neo4jGraphAdapter
from aegis.ports import GraphPort


def test_neo4j_adapter_is_graph_port() -> None:
    adapter = Neo4jGraphAdapter("bolt://localhost:7687", "neo4j", "")
    assert isinstance(adapter, GraphPort)


def test_allow_listed_queries_are_parameterized() -> None:
    assert "ontology_classes" in ALLOWED_QUERIES
    assert "subgraph_focus" in ALLOWED_QUERIES
    assert "$focus_id" in ALLOWED_QUERIES["subgraph_focus"]
    assert "$workflow" in ALLOWED_QUERIES["subgraph_workflow"]
    # Free-form client Cypher is not exposed — only fixed templates
    for cypher in ALLOWED_QUERIES.values():
        assert "RETURN" in cypher
        assert "LIMIT" in cypher


def test_list_ontology_degrades_without_server() -> None:
    adapter = Neo4jGraphAdapter("bolt://127.0.0.1:1", "neo4j", "invalid")
    ont = adapter.list_ontology()
    assert ont.get("advisory") is True
    assert ont.get("mode") in {"neo4j_unavailable", "neo4j_empty_seed_view", "neo4j"}
