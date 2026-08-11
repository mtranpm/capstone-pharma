from __future__ import annotations

from typing import Any, Optional

# Allow-listed Cypher templates only — no free-form client Cypher.
ALLOWED_QUERIES: dict[str, str] = {
    "ontology_classes": (
        "MATCH (c:OntologyClass) "
        "RETURN c.id AS id, c.label AS label ORDER BY c.id LIMIT 200"
    ),
    "ontology_rels": (
        "MATCH (a:OntologyClass)-[r:ONTOLOGY_REL]->(b:OntologyClass) "
        "RETURN a.id AS from_id, type(r) AS rel, r.id AS id, b.id AS to_id LIMIT 200"
    ),
    "subgraph_focus": (
        "MATCH (n) WHERE n.id = $focus_id "
        "OPTIONAL MATCH (n)-[r]-(m) "
        "RETURN n, collect(DISTINCT r) AS rels, collect(DISTINCT m) AS neighbours "
        "LIMIT 1"
    ),
    "subgraph_workflow": (
        "MATCH (n) WHERE coalesce(n.workflow, $workflow) = $workflow OR $workflow = 'all' "
        "RETURN n LIMIT 50"
    ),
}


class Neo4jGraphAdapter:
    """
    Neo4j GraphPort adapter — advisory projection only.

    Requires NEO4J_URI / NEO4J_USER / NEO4J_PASSWORD at runtime.
    Do not embed credentials in the repository.
    Offline/CLI eval must use InMemoryGraphStub via composition (AEGIS_USE_NEO4J unset).
    """

    def __init__(self, uri: str, user: str, password: str) -> None:
        self._uri = uri
        self._user = user
        self._password = password
        self._driver: Any = None

    def _ensure_driver(self) -> Any:
        if self._driver is None:
            from neo4j import GraphDatabase

            self._driver = GraphDatabase.driver(self._uri, auth=(self._user, self._password))
        return self._driver

    def close(self) -> None:
        if self._driver is not None:
            self._driver.close()
            self._driver = None

    def _unavailable(self, *, workflow: str = "", focus_id: Optional[str] = None, error: str) -> dict[str, Any]:
        return {
            "workflow": workflow,
            "focus_id": focus_id,
            "nodes": [],
            "edges": [],
            "mode": "neo4j_unavailable",
            "advisory": True,
            "error": error,
            "fallback": "Use InMemoryGraphStub (unset AEGIS_USE_NEO4J) for offline",
        }

    def list_ontology(self) -> dict[str, Any]:
        try:
            driver = self._ensure_driver()
            with driver.session() as session:
                classes = [
                    {"id": r["id"], "label": r["label"] or r["id"]}
                    for r in session.run(ALLOWED_QUERIES["ontology_classes"])
                    if r.get("id")
                ]
                relationships = [
                    {
                        "id": r["id"] or r["rel"],
                        "from": r["from_id"],
                        "to": r["to_id"],
                        "type": r["rel"],
                    }
                    for r in session.run(ALLOWED_QUERIES["ontology_rels"])
                    if r.get("from_id") and r.get("to_id")
                ]
            if not classes:
                # Empty DB — return seed plan shape so UI still renders
                return {
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
                        {"id": "OF_PRODUCT", "from": "Batch", "to": "Product"},
                        {"id": "RELATED_CASE", "from": "SafetyCase", "to": "SafetyCase"},
                    ],
                    "mode": "neo4j_empty_seed_view",
                    "advisory": True,
                    "note": "Run submission/scripts/load_graph.py --apply with AEGIS_USE_NEO4J=1",
                }
            return {
                "classes": classes,
                "relationships": relationships,
                "mode": "neo4j",
                "advisory": True,
            }
        except Exception as exc:  # noqa: BLE001 — degrade for UI; CLI offline uses stub
            return {
                "classes": [],
                "relationships": [],
                "mode": "neo4j_unavailable",
                "advisory": True,
                "error": str(exc),
                "note": "Unset AEGIS_USE_NEO4J to use InMemoryGraphStub",
            }

    def query_subgraph(self, workflow: str, focus_id: Optional[str] = None) -> dict[str, Any]:
        try:
            driver = self._ensure_driver()
            nodes: list[dict[str, Any]] = []
            edges: list[dict[str, Any]] = []
            with driver.session() as session:
                if focus_id:
                    record = session.run(ALLOWED_QUERIES["subgraph_focus"], focus_id=focus_id).single()
                    if record and record.get("n") is not None:
                        n = record["n"]
                        nodes.append(self._node_dict(n))
                        for m in record.get("neighbours") or []:
                            if m is not None:
                                nodes.append(self._node_dict(m))
                        for r in record.get("rels") or []:
                            if r is not None:
                                edges.append(self._edge_dict(r))
                else:
                    for r in session.run(ALLOWED_QUERIES["subgraph_workflow"], workflow=workflow):
                        nodes.append(self._node_dict(r["n"]))
            # Deduplicate nodes by id
            seen: set[str] = set()
            uniq_nodes = []
            for n in nodes:
                nid = str(n.get("id"))
                if nid in seen:
                    continue
                seen.add(nid)
                uniq_nodes.append(n)
            return {
                "workflow": workflow,
                "focus_id": focus_id,
                "nodes": uniq_nodes,
                "edges": edges,
                "mode": "neo4j",
                "advisory": True,
            }
        except Exception as exc:  # noqa: BLE001
            return self._unavailable(workflow=workflow, focus_id=focus_id, error=str(exc))

    def seed_from_plan(self, plan: dict[str, Any]) -> dict[str, Any]:
        """Merge advisory ontology + sample nodes from load_graph plan (idempotent)."""
        driver = self._ensure_driver()
        class_ids = list(plan.get("nodes") or [])
        rel_ids = list(plan.get("relationships") or [])
        with driver.session() as session:
            session.run(
                "CREATE CONSTRAINT ontology_class_id IF NOT EXISTS "
                "FOR (c:OntologyClass) REQUIRE c.id IS UNIQUE"
            )
            for cid in class_ids:
                session.run(
                    "MERGE (c:OntologyClass {id: $id}) SET c.label = $id, c.advisory = true",
                    id=cid,
                )
            # Ontology relationships (class-level)
            ontology_edges = [
                ("Batch", "HAS_GENEALOGY", "Batch"),
                ("Batch", "OF_PRODUCT", "Product"),
                ("Batch", "SUPPORTED_BY", "KnowledgeDocument"),
                ("SafetyCase", "RELATED_CASE", "SafetyCase"),
            ]
            for frm, rel, to in ontology_edges:
                if rel not in rel_ids and rel_ids:
                    continue
                session.run(
                    f"MATCH (a:OntologyClass {{id: $frm}}), (b:OntologyClass {{id: $to}}) "
                    f"MERGE (a)-[r:ONTOLOGY_REL {{id: $rel}}]->(b) "
                    f"SET r.advisory = true",
                    frm=frm,
                    to=to,
                    rel=rel,
                )
            # Sample instance nodes (advisory demo only — not SoR)
            session.run(
                "MERGE (p:Product {id: $id}) SET p.workflow = 'batch', p.advisory = true",
                id="NCB-204",
            )
            session.run(
                "MERGE (b:Batch {id: $id}) SET b.workflow = 'batch', b.product_id = $pid, b.advisory = true",
                id="NCB204-B24071",
                pid="NCB-204",
            )
            session.run(
                "MATCH (b:Batch {id: $bid}), (p:Product {id: $pid}) "
                "MERGE (b)-[r:OF_PRODUCT]->(p) SET r.advisory = true",
                bid="NCB204-B24071",
                pid="NCB-204",
            )
        return {
            "seeded_classes": class_ids,
            "seeded_relationships": rel_ids,
            "mode": "neo4j",
            "advisory": True,
            "applied": True,
        }

    @staticmethod
    def _node_dict(n: Any) -> dict[str, Any]:
        props = dict(n)
        nid = props.get("id") or getattr(n, "element_id", None)
        labels = list(getattr(n, "labels", []) or [])
        return {
            "id": str(nid),
            "label": labels[0] if labels else props.get("label", "Node"),
            "labels": labels,
            "props": {k: v for k, v in props.items() if k != "id"},
        }

    @staticmethod
    def _edge_dict(r: Any) -> dict[str, Any]:
        try:
            start = r.start_node
            end = r.end_node
            return {
                "from": str(dict(start).get("id") or start.element_id),
                "to": str(dict(end).get("id") or end.element_id),
                "type": r.type,
            }
        except Exception:  # noqa: BLE001
            return {"from": None, "to": None, "type": getattr(r, "type", "REL")}
