# 20 — Agent Budget, Stop & Checkpointing

| Field | Entry |
|---|---|
| Owner | Platform / agent lead |
| Version / date | 1.0.0 / 2026-08-10 |
| Status | Phase 5 — bounded agent orchestration |
| Sources | ADR-012, XC-05, `06`, `04` STOP table, PUB-13 |

---

## 1. Scope

Applies when multi-step **agent-style** orchestration uses `LlmPort` + tools. Rules-only CLI path uses **step budget = 1** (deterministic).

---

## 2. Budget dimensions

| Budget | Default (workshop) | Production target | On exceed |
|---|---|---|---|
| **Max tool calls** | 12 | 20 (role-adjusted) | Stop; checkpoint; abstain |
| **Max LLM turns** | 6 | 10 | Stop |
| **Max wall time** | 120 s | 300 s | Stop |
| **Max tokens (in+out)** | 32k | Policy per `33` | Stop or refuse start |
| **Max retrieval chunks** | 24 | 40 | Truncate with flag |

Budgets are **declared in run request** and validated at API gateway.

---

## 3. Stop conditions (hard)

| Code | Trigger | Action |
|---|---|---|
| STOP-BUDGET | Any budget exceeded | Halt agent loop |
| STOP-PROHIBITED | Guard detects NN-01..03 pattern | Halt + audit alert |
| STOP-TOOL | Unknown tool / schema fail | Halt |
| STOP-AUTH | AuthZ fail or stale session | Halt fail-closed |
| STOP-HUMAN | Emergency stop ES-01..05 (`06`) | Immediate AI-disabled |
| STOP-CONFIDENCE | Grader pre-check fail (optional) | Abstain |

Align programme **STOP-01** (`04`): disposition-like output → stop demo.

---

## 4. Checkpointing

| Checkpoint | Contents | Use |
|---|---|---|
| `CP-after-sor-load` | Fact snapshot ids | Resume without re-fetch |
| `CP-after-reconcile` | Conflict register hash | Audit replay |
| `CP-pre-llm` | Tool manifest version | Prove tool surface |
| `CP-pre-export` | Draft packet hash | Human gate G-HR-01 |

Checkpoints stored with run id; **no PHI in object storage keys**. Retention per `24`.

Idempotency: same `idempotency_key` + same inputs → return prior completed run if hash matches.

---

## 5. Human checkpoints (mandatory)

Agent automation **never** bypasses G-HR-01..06 (`06`, D-008). Checkpoints are machine aids; export requires human attestation in UI.

---

## 6. Observability

Spans: `agent.step`, `tool.call`, `budget.remaining` (aggregated only). No raw PV text in attributes (ADR-005).

---

## 7. Test IDs

| Test | Description | Status |
|---|---|---|
| T-BUD-01 | Exceed max tool calls → STOP-BUDGET | **Pending** |
| T-BUD-02 | Idempotent replay same key | **Pending** |
| T-BUD-03 | Prohibited tool denied pre-call | **Pending** |

---

## 8. Traceability

| REQ | Section |
|---|---|
| XC-05 | §2–§4 |
| NN-01..03 | §3 STOP-PROHIBITED |
