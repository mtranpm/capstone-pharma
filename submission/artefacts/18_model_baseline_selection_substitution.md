# 18 — Model Baseline Selection & Substitution

| Field | Entry |
|---|---|
| Owner | ML platform / product |
| Version / date | 1.0.0 / 2026-08-10 |
| Status | Phase 5 — baseline policy (workshop) |
| Sources | ADR-011, `18`/`19` pairing, `32`, `36`, hybrid decision D-003 |

---

## 1. Role of models in AEGIS

Models are **optional accelerators** behind `LlmPort`. **Rules-first** reconciliation satisfies NN-05 and offline NN-06. Any model output is **untrusted** until Pydantic contract + grader pass (`19`).

**Not in scope:** autonomous regulated classification (seriousness, release, ship).

---

## 2. Baseline selection (workshop)

| Use case | Baseline (workshop) | Rationale |
|---|---|---|
| Structured field extraction from short snippets | **None required** — rules + CSV | Deterministic eval |
| Narrative **draft** summaries (optional demo) | Small instruct model via gateway **or** stub | Cost/latency bounded |
| Embedding / RAG (if enabled) | Enterprise-approved embedding model | Governed retrieval only |
| Graph / logic | No LLM | `GraphPort` + rules |

**Workshop default:** `OfflineLlmStub` — baseline = *no model*.

---

## 3. Selection criteria (production-oriented)

| Criterion | Weight | Threshold / note |
|---|---|---|
| Structured output reliability | High | Must conform to strict schema (ADR-003) |
| Data residency / DPA | High | EU processing for EU PV data |
| Prompt injection resistance | High | Tool manifest + fail-closed (`28`) |
| Cost per 1k tokens | Medium | FinOps caps (`34`) |
| Latency p95 | Medium | SLO in `35` |
| Vendor SOC2 / ISO 27001 | Medium | Vendor dossier `36` |
| Substitutability | High | `LlmPort` adapter swap ≤ 1 sprint |

---

## 4. Substitution procedure

```text
1. Register candidate in model registry (version, endpoint, data policy)
2. Run offline golden set — no regression on G-* F1 / abstention codes
3. Run TEVV slice (32): κ on human labels for advisory fields only
4. Red-team subset (31) — LLM01/06/08 cases
5. Change control: Quality + DPO + Platform sign-off
6. Deploy behind feature flag + budget (20)
7. Rollback: flip to stub; prior adapter retained 90d (36)
```

---

## 5. Prohibited model uses

| Prohibited | REQ |
|---|---|
| Final PV seriousness/causality/reportability | NN-02 |
| Batch disposition language presented as decision | NN-01 |
| Supply allocation / ship recommendations as execution | NN-03 |
| Silent translation altering PV meaning | PV-02, G-HR-05 |
| Training on live PV narratives without governance | `30`, `26` |

---

## 6. Evidence artefacts

| Artefact | Location | Status |
|---|---|---|
| Model card (intended use, limits) | `submission/evidence/models/` | **Pending** |
| Substitution test report | TEVV run output | **Pending** |
| Offline parity (stub vs model) | `32` | **Pending** |

---

## 7. Traceability

| REQ | Section |
|---|---|
| NN-06 | §2 default stub |
| XC-06 | §3 cost criterion |
| ADR-011 | §1, §4 |
