# 10 — Ontology & Semantic Layer

| Field | Entry |
|---|---|
| Owner | Data / architecture lead |
| Version | 0.1.0 |
| Status | Phase 4 — draft |
| Sources | A3 glossary (DDD-Lab), A7 object register, `data/DATA_DICTIONARY.csv`, `data/RELATIONSHIP_MODEL.csv`, `GraphPort.list_ontology()` |

## 1. Purpose

Provide a **controlled semantic layer** for advisory reconciliation: shared terms, units, authority/status, and **as-of** semantics — mapped to challenge **`data/`** fields without altering source values.

## 2. Core classes (ontology)

| Class | Definition | Primary keys in `data/` | Notes |
|---|---|---|---|
| **Product** | Medicinal product identity (IDMP-aligned) | `portfolio_products.csv` `product_id`; `medicinal_products.csv`; `icsr_cases.csv` `product` (alias risk) | Use `product_master_aliases.csv` for conflicts |
| **Batch** | Manufactured batch/lot | `batches.csv` `batch_id`; `material_genealogy.csv` `batch_id` | Status is SoR field — not graph-derived |
| **MaterialLot** | Component / SUA lot | `material_genealogy.csv`, `warehouse_movements.csv` | Genealogy break = missing link, not auto-repair |
| **SafetyCase** | ICSR case aggregate | `icsr_cases.csv` `case_id`; `adverse_events.csv`, `safety_receipts.csv` | Final PV assessment out of scope |
| **Shipment** | Cold-chain / logistics unit | `shipments.csv` `shipment_id`; `temperature_loggers.csv`; `serialisation_events.csv` | Options only — no ship execution |
| **KnowledgeDocument** | Controlled policy/SOP | `knowledge_catalog.csv` `doc_id` → `knowledge/*.md` | Authority via catalog, not filename |
| **LabResult** | Analytical evidence | `lab_results.csv`, `assay_results.csv` | `unit` verbatim |
| **QualityEvent** | Deviation/CAPA/OOS | `deviations.csv`, `capa_records.csv`, `oos_investigations.csv` | Disputed states stay open |
| **Constraint** | Allocation / MA constraint | `allocation_constraints.csv`, `market_authorisations.csv` | Hard vs soft in `priority` |

Stub ontology in code mirrors these classes (`submission/src/aegis/adapters/graph_memory.py`).

## 3. Controlled terms (selected)

| Term | Allowed usage | Forbidden usage |
|---|---|---|
| **batch-review readiness** | Evidence assembled or gaps explicit | Synonym for “released” or QP certified |
| **release-ready** | Human-only QP/Quality judgment | AI status field |
| **genealogy break** | Visible missing branch (e.g. SUA-88) | Auto-closed by graph inference |
| **unit-conversion assumption** | Explicit approved/unapproved/conflict | Silent normalization |
| **advisory translation** | Human-reviewed helper text | Replacement for verbatim narrative |
| **non-executing option** | Supply recovery draft | Order, allocation, or shipment |
| **abstain / no-answer** | Fail-closed output | Hidden retry until “success” |

Extended vocabulary: `data/controlled_vocabularies.csv` (dose form, route); MedDRA via `terminology_versions.csv` / `adverse_events.csv` `meddra_version`.

## 4. Units & measurements

| Rule | Field examples |
|---|---|
| Reported unit travels with value | `lab_results.csv` `unit`, `assay_results.csv` `unit`, `api_contract_versions.csv` `unit_field` |
| No silent conversion | DATA_DICTIONARY flags unit columns explicitly |
| Temperature / logger | `temperature_loggers.csv`; shipment `logger` FK |
| Concentration conflict case | mg/L vs µg/mL — emit **assumption status**, not converted number |

## 5. Authority & document status

Aligned to `knowledge_catalog.csv`:

| Semantic status | Catalog signals | Gate behaviour |
|---|---|---|
| **trusted** | `trust=approved`, `status=approved`, effective date applicable | May support readiness **after** jurisdiction/as-of check |
| **pending** | draft / in review | Evidence of risk only |
| **superseded** | `status=superseded`, `supersedes` chain | Must not authorize; may explain history |
| **untrusted** | e.g. `K-999`, external upload | Quarantine; NN-04 |

`AuthorityPort.classify_document(doc_id)` is the runtime seam.

## 6. As-of semantics

| Dimension | Source fields | Rule |
|---|---|---|
| **Effective date** | `knowledge_catalog.csv` `effective`; `market_authorisations.csv`; `protocol_versions.csv` | Pick record version valid at evaluation as-of |
| **Event time** | `*_date`, `time` columns per DATA_DICTIONARY | Preserve precision (date vs datetime) |
| **Evaluation as-of** | Run request parameter (FastAPI) | Stated in packet lineage; no retroactive SoR edit |
| **Awareness date (PV)** | `icsr_cases.csv` `awareness_date`, `safety_receipts.csv` | Conflicts remain visible |

Later timestamp **≠** automatic authority (Authority context).

## 7. Relationships (semantic → physical)

From `RELATIONSHIP_MODEL.csv` (subset):

| Relationship | From → To | Rule |
|---|---|---|
| HAS_GENEALOGY | Batch → MaterialLot | `material_genealogy.csv` |
| OF_PRODUCT | Batch → Product | `batches.csv` `product_id` |
| HAS_RESULT | Batch → LabResult | `lab_results.csv` |
| HAS_CASE | SafetyCase → AdverseEvent | `adverse_events.csv` |
| HAS_RECEIPT | SafetyCase → SafetyReceipt | `safety_receipts.csv` |
| DUPLICATE_CANDIDATE | SafetyCase ↔ SafetyCase | `duplicate_candidates.csv` |
| USES_LOGGER | Shipment → TemperatureLogger | optional FK per case notes |
| SUPPORTED_BY | Any claim → KnowledgeDocument | citation in packet |
| SUBJECT_TO | Shipment/Option → Constraint | `allocation_constraints.csv` |

GraphPort exposes a **read-only projection** of these edges for explainability.

## 8. API / GraphPort alignment

| Operation | Returns |
|---|---|
| `list_ontology()` | Classes, relationship types, advisory disclaimer |
| `query_subgraph(workflow, focus_id)` | Nodes/edges for batch id, case id, or shipment id — mode `in_memory_stub` or `neo4j` |

Workflow focus examples:

- Batch: `NCB204-B24071`  
- PV: `PV-1001`, `PV-1014`  
- Supply: `SH-901`, `SH-902`

## 9. Links

- Document authority detail: [`12_document_authority_model.md`](12_document_authority_model.md)  
- KG decision: [`11_knowledge_graph_decision.md`](11_knowledge_graph_decision.md)  
- Data governance: [`09_data_governance_lineage_contracts.md`](09_data_governance_lineage_contracts.md)
