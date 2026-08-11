# 09 — Data Governance, Lineage & Contracts

| Field | Entry |
|---|---|
| Owner | Data / platform lead |
| Version | 0.1.0 |
| Status | Draft |
| Sources | `data/knowledge_catalog.csv`, `data/systems_of_record.csv`, Engineering typed-contracts spec, A1 §6–7 |

## 1. Systems of record vs derived

| Class | Examples | Rule |
|---|---|---|
| **System of record** | Fixture CSVs under `data/` (MES/LIMS/QMS/PV/ERP/WMS analogues), signed SOPs/specs in knowledge | Never silently overwrite; preserve verbatim fields |
| **Derived / advisory** | Neo4j KG, embeddings, LLM summaries, React views | Must cite sources; cannot outrank SoR / authority |
| **Not SoR** | Chat history, tool descriptions, untrusted uploads | Untrusted until verified |

## 2. Lineage requirements

Every material claim in an advisory packet must carry:

- `source_system` / document id  
- `authority_status` (trusted / untrusted / superseded / pending)  
- `effective_date` / `version` when applicable  
- `retrieved_at` / run id  
- unit + time precision as in source (no silent conversion)

## 3. Contract principles (implementation)

Aligned to `Docs/specs/Engineering/TYPED_CONTRACTS_PORTS_FASTAPI.md`:

- Pydantic v2 strict; `extra="forbid"`  
- Versioned request/response envelopes  
- Idempotency keys on mutating orchestration starts  
- Bounded steps / budgets  
- Ports for LLM, graph, clock, audit — adapters swappable  

## 4. Knowledge classes (from catalog)

| Class | Use in decisions | Default |
|---|---|---|
| Signed / effective controlled docs | May support readiness if applicable | Authority gate required |
| Draft / superseded / untrusted | Evidence of risk only | Must not authorize |
| Multilingual narrative | Intake support | Preserve original; no silent “fix” |

## 5. Privacy & retention (discovery level)

- Purpose binding at retrieval (DPO mandate).  
- Minimisation: do not log raw case narratives in OTel attributes.  
- Retention/deletion subject to GxP vs privacy conflict → escalate (no silent purge of audit).  
Detail in artefact `29` (Phase 3).

## 6. Fixture / inject data map

See `01_discovery_problem_baseline_value.md` §6 and `traceability_inject_workflow.csv`.
