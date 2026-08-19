# Ontology & Knowledge Graph — Pictorial View

| Field | Entry |
|---|---|
| Owner | Architecture / data lead |
| Version / date | 1.0.0 / 2026-08-16 |
| Purpose | Executive / defence pictorial of AEGIS ontology + advisory KG |
| Code source | [`graph_memory.py`](../../src/aegis/adapters/graph_memory.py), [`graph_neo4j.py`](../../src/aegis/adapters/graph_neo4j.py), [`load_graph.py`](../../scripts/load_graph.py) |
| Design source | [`10_ontology_semantic_layer.md`](../10_ontology_semantic_layer.md), [`11_knowledge_graph_decision.md`](../11_knowledge_graph_decision.md) |

**Headline:** Five ontology classes. Advisory graph only. CSV / fixtures remain the system of record.

**How to use:** Paste Mermaid into slides, or render in Markdown preview / Mermaid Live.

---

## 1. Ontology classes (hardcoded)

```mermaid
flowchart TB
  Batch[Batch]
  Product[Product]
  SafetyCase[SafetyCase]
  Shipment[Shipment]
  KnowledgeDocument[KnowledgeDocument]
```

| Class | Meaning (semantic layer) |
|---|---|
| **Batch** | Manufactured batch / lot under review |
| **Product** | Medicinal product identity |
| **SafetyCase** | ICSR / safety case aggregate |
| **Shipment** | Cold-chain / logistics unit |
| **KnowledgeDocument** | Controlled policy / SOP / labeled knowledge |

---

## 2. Ontology relationships (class level)

### 2.1 What the in-memory stub exposes via `list_ontology()`

```mermaid
flowchart LR
  Batch -->|HAS_GENEALOGY| Batch
  Batch -->|SUPPORTED_BY| KnowledgeDocument
```

| Relationship | From | To | Meaning |
|---|---|---|---|
| `HAS_GENEALOGY` | Batch | Batch | Parent / child or lineage link between batches or lots |
| `SUPPORTED_BY` | Batch | KnowledgeDocument | Batch evidence supported by a governed document |

### 2.2 Full advisory ontology used for Neo4j seed / empty-seed UI

```mermaid
flowchart LR
  Batch -->|HAS_GENEALOGY| Batch
  Batch -->|OF_PRODUCT| Product
  Batch -->|SUPPORTED_BY| KnowledgeDocument
  SafetyCase -->|RELATED_CASE| SafetyCase
  Shipment((Shipment))
```

| Relationship | From | To | Meaning |
|---|---|---|---|
| `HAS_GENEALOGY` | Batch | Batch | Lineage / genealogy edge |
| `OF_PRODUCT` | Batch | Product | Batch belongs to product |
| `SUPPORTED_BY` | Batch | KnowledgeDocument | Document supports batch evidence |
| `RELATED_CASE` | SafetyCase | SafetyCase | Possible duplicate / linked safety cases |

`Shipment` is a class in the ontology; no class-level edge is hardcoded for it in the seed plan (instances may still appear in a fuller projection later).

---

## 3. Ontology as one picture (recommended slide)

```mermaid
flowchart TB
  subgraph ontology [AEGIS advisory ontology]
    Product[Product]
    Batch[Batch]
    SafetyCase[SafetyCase]
    Shipment[Shipment]
    KnowledgeDocument[KnowledgeDocument]
  end
  Batch -->|OF_PRODUCT| Product
  Batch -->|HAS_GENEALOGY| Batch
  Batch -->|SUPPORTED_BY| KnowledgeDocument
  SafetyCase -->|RELATED_CASE| SafetyCase
```

**Talk track:** Ontology answers *what kinds of things exist* and *how they may relate*. It does not decide release, PV finals, or allocation.

---

## 4. Knowledge graph — how it sits in the architecture

```mermaid
flowchart LR
  SoR[CSV fixtures and SoR facts]
  Ont[Ontology classes and relationships]
  Stub[InMemoryGraphStub]
  Neo[Neo4j optional]
  API["GET /v1/ontology and /v1/graph"]
  UI[Review UI dashboard]
  SoR -.->|authoritative| Packets[Workflow packets]
  Ont --> Stub
  Ont --> Neo
  Stub -->|default offline| API
  Neo -->|AEGIS_USE_NEO4J=1| API
  API --> UI
  Stub -.->|advisory only| Packets
  Neo -.->|advisory only| Packets
```

| Rule | Meaning |
|---|---|
| Advisory | Every graph response includes `advisory: true` |
| SoR wins | On conflict, prefer CSV / fixture values; rebuild graph |
| No write-back | Graph does not update MES / LIMS / QMS / PV DB |
| Offline first | Default adapter is the in-memory stub |

---

## 5. Knowledge graph — sample instance projection (seed)

Illustrative instance graph seeded for demo explainability (not a full SoR dump):

```mermaid
flowchart LR
  P[Product instance]
  B[Batch instance]
  B -->|OF_PRODUCT| P
```

In code the seed uses one product and one batch node linked by `OF_PRODUCT`. Genealogy and document links are available as **relationship types** even when sample instance edges for those types are not populated in the stub.

```mermaid
flowchart TB
  subgraph instances [Advisory instance layer]
    B[Batch]
    P[Product]
    D[KnowledgeDocument]
    S[SafetyCase]
    H[Shipment]
  end
  B -->|OF_PRODUCT| P
  B -.->|HAS_GENEALOGY possible| B
  B -.->|SUPPORTED_BY possible| D
  S -.->|RELATED_CASE possible| S
```

Solid = seeded sample edge. Dashed = ontology allows the relationship; instance may be empty until loaded.

---

## 6. Stub vs Neo4j (same ontology, different store)

```mermaid
flowchart TB
  Port[GraphPort]
  Port --> Stub[InMemoryGraphStub]
  Port --> Neo[Neo4jGraphAdapter]
  Stub --> Ont1[Hardcoded classes + 2 ontology rels]
  Stub --> Inst1[Sample Batch to Product edge]
  Neo --> Ont2[OntologyClass nodes + ONTOLOGY_REL]
  Neo --> Inst2[Seeded Product Batch and OF_PRODUCT]
```

| | In-memory stub | Neo4j |
|---|---|---|
| Library | None (dicts) | `neo4j` Python driver + Neo4j 5 |
| Ontology API | Hardcoded dict | Cypher over `:OntologyClass` |
| Default | Yes | Only if `AEGIS_USE_NEO4J=1` |
| Mode flag | `in_memory_stub` | `neo4j` / `neo4j_empty_seed_view` / `neo4j_unavailable` |

---

## 7. One-slide leave-behind

```text
                    Product
                       ^
                       | OF_PRODUCT
                       |
    HAS_GENEALOGY   Batch ----SUPPORTED_BY----> KnowledgeDocument
         |  ^
         +--+

    SafetyCase ----RELATED_CASE----> SafetyCase

    Shipment   (class present; no hardcoded class-level edge)
```

**Libraries:** no RDF/OWL; optional Neo4j only.  
**Use:** explainability and UI ontology panel — not regulated decisions.
