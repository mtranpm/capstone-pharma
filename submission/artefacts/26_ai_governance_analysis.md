# 26 — AI Governance Analysis

| Field | Entry |
|---|---|
| Owner | AI governance / Quality |
| Version / date | 1.0.0 / 2026-08-10 |
| Status | Phase 5 — ISO 42001 ↔ EU AI Act crosswalk |
| Sources | ISO/IEC 42001:2023 (AIMS), EU AI Act (2024/1689) high-level, `22`, `13` §8 |

---

## 1. Governance scope

AIMS applies to **management** of AI used in AEGIS (optional LLM, retrieval, agents) — not to replacing NovaCura’s entire QMS.

---

## 2. ISO 42001 ↔ programme controls (selected)

| ISO 42001 theme | Control intent | AEGIS artefact / REQ |
|---|---|---|
| 4 Context | Advisory boundary | `22`, `SCQA.md` |
| 5 Leadership | Human accountability | `03`, `06` |
| 6 Planning | Risk treatment | `25`, `27` |
| 7 Support | Competence, data | `07`, `09` |
| 8 Operation | Lifecycle, vendors | `18`, `36` |
| 9 Performance eval | TEVV, audits | `32`, `23` |
| 10 Improvement | Incidents, CAPA | `31`, `35` |

---

## 3. EU AI Act crosswalk (high level, non-legal)

| EU AI Act topic | ISO 42001 bridge | AEGIS implementation |
|---|---|---|
| Risk management (Art. 9) | Clause 6 | `25`, `27` |
| Data governance (Art. 10) | Clause 7 + 8.2 | `09`, `30`, governed RAG `19` |
| Technical documentation (Annex IV) | Operation controls | `14`, `22`, specs |
| Record-keeping (Art. 12) | Performance + logs | `24`, ADR-005 |
| Transparency (Art. 13) | Communication | UI labelling `07` |
| Human oversight (Art. 14) | Operational planning | G-HR `06` |
| Accuracy/robustness (Art. 15) | Performance evaluation | `32`, abstention NN-05 |
| Cybersecurity (Art. 15) | Security controls | `28`, `29` |

**Classification note:** Intended use (`22`) targets **decision support without autonomous regulated acts** — likely outside highest-risk medical device pathways, but **DPO/RA legal confirmation required**.

---

## 4. AI system inventory

| Component | AI? | Risk tier | Owner |
|---|---|---|---|
| Rules reconciliation | No | Low | Engineering |
| LlmPort (optional) | Yes | Medium | ML platform |
| Embedding index (optional) | Yes | Medium | Data platform |
| Neo4j graph | No (deterministic load) | Low | Platform |
| Tool-using agent | Yes | Medium–High | Platform + CISO |

---

## 5. Residual governance risks

| R-ID | Risk | Mitigation | Owner |
|---|---|---|---|
| R-GOV-01 | Users trust draft as decision | Training, UI, κ monitoring | Product |
| R-GOV-02 | Model vendor policy drift | `36` exit, contract clauses | Procurement |
| R-GOV-03 | Shadow IT LLM paste | Block in prod UI; DLP | CISO |
| R-GOV-04 | Incomplete AIMS docs | Phase 10 evidence pack `37` | Quality |
| R-GOV-05 | Cross-border PV data to US model | Residency gates `30` | DPO |

---

## 6. Traceability

Closes gap **G-001** partially via RTM §8 control IDs.
