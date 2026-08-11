# 11 — Knowledge Graph Decision

| Field | Entry |
|---|---|
| Owner | Architecture lead |
| Version | 0.1.0 |
| Status | Phase 4 — **ADOPT** Neo4j (advisory) |
| Sources | D-001, `Docs/specs/Engineering/TYPED_CONTRACTS_PORTS_FASTAPI.md`, `data/RELATIONSHIP_MODEL.csv`, `04` pivot table |

## 1. Decision summary

| Option | Verdict | Rationale |
|---|---|---|
| **Neo4j via `GraphPort`** | **ADOPT** | Multi-hop genealogy, case linkage, shipment/logger paths are awkward in ad-hoc CSV joins; graph suits **explainability** |
| **CSV joins only** | Reject as sole strategy | Error-prone for 140+ tables; silent merge risk violates NN-05 / `09` |
| **Neo4j as SoR** | **Reject** | Challenge evidence remains CSV + knowledge files; graph is derived |
| **InMemoryGraphStub** | **ADOPT** (required) | Offline eval, CI, AI-disabled continuity (NN-06) |

Decision id: **D-001** (Pre-Phase); reaffirmed here with benchmark notes.

## 2. Benchmark: graph vs CSV joins (workshop)

| Scenario | CSV join approach | GraphPort approach | Observation |
|---|---|---|---|
| Batch `NCB204-B24071` + genealogy + lab | 4–6 keyed merges (`batches`, `material_genealogy`, `warehouse_movements`, `lab_results`) | Single `query_subgraph("batch", focus_id)` | Graph returns explicit path for UI “why linked” |
| PV duplicate cluster | Join `icsr_cases`, `duplicate_candidates`, `adverse_events` | Subgraph from case id | Easier to show parallel product aliases |
| Supply cold chain | `shipments` ⋈ `temperature_loggers` ⋈ `serialisation_events` (optional logger) | Subgraph from `shipment_id` | Models optional logger per RELATIONSHIP_MODEL note |
| Knowledge citation | N/A (document ids) | `SUPPORTED_BY` edges to `KnowledgeDocument` | Keeps policy citations out of fact tables |

**Performance (synthetic scale):** At workshop data volumes, both are fast; **correctness and audit narrative** favour graph. At production scale, Neo4j indexing on `batch_id`, `case_id`, `shipment_id` remains advisory cache — rebuild from SoR on schedule.

## 3. GraphPort rules (non-negotiable)

| Rule | Enforcement |
|---|---|
| **Advisory only** | Every response includes `advisory: true`; packets label graph-derived links |
| **Never SoR** | No graph write path to `data/`; load scripts are batch rebuild only |
| **Fail-closed** | If graph unavailable → stub or abstain; never invent nodes |
| **Allow-listed queries** | FastAPI `/v1/graph` — parameterized workflows only; no arbitrary Cypher from clients |
| **Parity** | Contract tests: stub vs Neo4j adapter return same shape for golden focus ids |
| **Provenance** | Audit emit includes `mode: in_memory_stub` or `neo4j` + query version |
| **Authority** | Graph cannot elevate `trust`; document status still from `AuthorityPort` |

Protocol (minimum):

```python
# submission/src/aegis/ports/__init__.py — GraphPort
def query_subgraph(workflow: str, focus_id: str | None = None) -> dict[str, Any]: ...
def list_ontology() -> dict[str, Any]: ...
```

## 4. Adapters

| Adapter | Role | Status |
|---|---|---|
| `InMemoryGraphStub` | Offline default in `composition.py` | Implemented |
| `graph_neo4j.py` | Neo4j driver behind same protocol | Placeholder / workshop hook |
| `load_graph.py` | Optional bulk load from RELATIONSHIP_MODEL | CLI helper; skip when offline |

Composition root selects adapter via env/config — domain never imports Neo4j driver.

## 5. Data flow

```text
data/*.csv (SoR fixtures, read-only)
    → fixture loaders (verbatim)
    → optional ETL → Neo4j (derived projection)
    → GraphPort.query_subgraph → application services
    → packet citations (secondary to SoR row ids)
```

If Neo4j drift detected vs CSV → **prefer CSV** for values; graph rebuild ticket.

## 6. Pivot / stop (from `04`)

| Condition | Action |
|---|---|
| Neo4j unavailable | Stay on `InMemoryGraphStub`; KG remains advisory |
| Operators treat graph as authority | Training + UI labelling; red-team |
| Stub/Neo4j shape mismatch | Block release until contract test fixed |

## 7. Requirements trace

| REQ | Link |
|---|---|
| XC-04 integration | Typed graph responses |
| NN-06 offline | Stub path |
| BAT-03 genealogy | Subgraph explains SUA-88 break visibility |

## 8. Links

- Ontology: [`10_ontology_semantic_layer.md`](10_ontology_semantic_layer.md)  
- Architecture ADRs: artefact `14` (Phase 5)  
- Implementation: `submission/src/aegis/adapters/graph_memory.py`, `graph_neo4j.py`
