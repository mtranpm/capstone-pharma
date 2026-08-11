# 33 — Token Efficiency Economics

| Field | Entry |
|---|---|
| Owner | Platform / FinOps |
| Version / date | 1.0.0 / 2026-08-10 |
| Status | Phase 5 — token discipline |
| Sources | XC-06, `20`, `19`, PUB-14 |

---

## 1. Goals

Minimize token spend while preserving **conflict-visible** evidence — never drop conflicts to save tokens.

---

## 2. Context economics

| Technique | Saving | Risk mitigated by |
|---|---|---|
| Workflow templates (fixed sections) | 20–40% vs free-form | Schema validation |
| SoR field projection (column allow-list) | High | BAT-02 verbatim still from source row |
| Graph summary caps | Medium | `advisory:true` + link to expand in UI |
| Retrieval top-k + deterministic tie-break | Medium | Hash verify `19` |
| Checkpoint reuse | Avoid re-send | `20` |

---

## 3. Measurement

| Metric | Source |
|---|---|
| Tokens in/out per run | LlmPort + audit |
| Cost per successful packet | FinOps model `34` |
| Tokens per abstention | Quality signal |
| Cache hit rate (if prompt cache) | Platform metrics |

Redacted aggregates only in dashboards — no PV text.

---

## 4. Policies

| Policy | Rule |
|---|---|
| Refuse start | If projected tokens > budget without override role |
| Truncation | Must set `context_truncated`; never truncate conflict register |
| Model routing | Cheaper model for formatting; stronger for complex PV **optional** |

---

## 5. Workshop baseline

Default **zero tokens** (offline stub). Demo profile documents assumed price sheet in `34`.

---

## 6. Traceability

XC-06, LLM10, `20` §2.
