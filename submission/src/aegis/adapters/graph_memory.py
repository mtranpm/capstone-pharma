from __future__ import annotations

from typing import Any, Optional


class InMemoryGraphStub:
    """Offline GraphPort for CLI/eval without Neo4j."""

    def __init__(self) -> None:
        self._ontology = {
            "classes": [
                {"id": "Batch", "label": "Batch"},
                {"id": "Product", "label": "Product"},
                {"id": "SafetyCase", "label": "Safety Case"},
                {"id": "Shipment", "label": "Shipment"},
                {"id": "KnowledgeDocument", "label": "Knowledge Document"},
            ],
            "relationships": [
                {"id": "HAS_GENEALOGY", "from": "Batch", "to": "Batch"},
                {"id": "SUPPORTED_BY", "from": "Batch", "to": "KnowledgeDocument"},
            ],
        }
        self._nodes = [
            {"id": "NCB204-B24071", "label": "Batch", "props": {"product_id": "NCB-204"}},
            {"id": "NCB-204", "label": "Product", "props": {}},
        ]
        self._edges = [
            {"from": "NCB204-B24071", "to": "NCB-204", "type": "OF_PRODUCT"},
        ]

    def list_ontology(self) -> dict[str, Any]:
        return dict(self._ontology)

    def query_subgraph(self, workflow: str, focus_id: Optional[str] = None) -> dict[str, Any]:
        nodes = self._nodes
        edges = self._edges
        if focus_id:
            nodes = [n for n in nodes if n["id"] == focus_id or focus_id in str(n.get("props"))]
        return {
            "workflow": workflow,
            "focus_id": focus_id,
            "nodes": nodes,
            "edges": edges,
            "mode": "in_memory_stub",
            "advisory": True,
        }
