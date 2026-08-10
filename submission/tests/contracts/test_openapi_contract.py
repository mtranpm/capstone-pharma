from __future__ import annotations

from fastapi.testclient import TestClient

from aegis.api.app import create_app
from aegis.composition import build_container
import aegis.api.app as app_module


def test_openapi_and_health() -> None:
    app_module._container = build_container(use_neo4j=False)
    client = TestClient(create_app())
    health = client.get("/health")
    assert health.status_code == 200
    assert health.json()["status"] == "ok"
    openapi = client.get("/openapi.json")
    assert openapi.status_code == 200
    body = openapi.json()
    assert "/health" in body["paths"]
    assert "/v1/ontology" in body["paths"]
    assert "/v1/graph" in body["paths"]


def test_ontology_and_graph_routes() -> None:
    app_module._container = build_container(use_neo4j=False)
    client = TestClient(create_app())
    ont = client.get("/v1/ontology")
    assert ont.status_code == 200
    assert "classes" in ont.json()
    g = client.get("/v1/graph", params={"workflow": "batch"})
    assert g.status_code == 200
    assert g.json()["advisory"] is True
