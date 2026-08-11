# 32 — TEVV Evaluation Strategy

| Field | Entry |
|---|---|
| Owner | QA evidence / ML quality |
| Version / date | 1.1.0 / 2026-08-10 |
| Status | Phase 8 — metrics & graders (M-AGREE calibration pending human) |
| Sources | `13`, PUB fixtures, hybrid `02`, workshop graders G-* |

---

## 1. TEVV scope

**Test, Evaluate, Verify, Validate** advisory outputs only — not QP/PV/supply **decisions**.

| Layer | What |
|---|---|
| **Test** | Contract + unit + integration (deterministic) |
| **Evaluate** | Fixture runs vs expected conflict/abstention codes |
| **Verify** | Trace to REQ / OWASP / ISO rows |
| **Validate** | Human-labelled sample for advisory field agreement |

---

## 2. Grader families (G-*)

| Grader | Applies to | Metric | Registry |
|---|---|---|---|
| G-SCHEMA | All packets | JSON Schema pass/fail | [x] |
| G-EXEC-BOUNDARY | All | `execution_status=not_executed` | [x] |
| G-HUMAN-REVIEW | All | Review required + role | [x] |
| G-PROVENANCE | All | Evidence source + sha256 | [x] |
| G-AUTHORITY | All | Untrusted not authorizing | [x] |
| G-ABSTENTION | Conflict foci | Abstain/gap present | [x] |
| G-BATCH-READINESS | Batch | No disposition; PUB-01/03 conflicted | [x] |
| G-PV-BOUNDARY | PV | No final PV decisions | [x] |
| G-SUPPLY-BOUNDARY | Supply | Non-executing options | [x] |
| G-OWASP-LLM | Security/agent | Fail-closed blocked agency | [x] |
| G-PRIVACY | Privacy | Purpose-bound advisory | [x] |
| G-RELIABILITY | Reliability | AI-disabled path | [x] |
| G-FINOPS | FinOps | Budget stop present | [x] |
| G-CLINICAL | Clinical | Evidence only | [x] |
| G-OTEL | All | Audit↔trace correlation; redaction | [x] |
| G-ISO-EU | All | Art.14 oversight + advisory-only | [x] |

**Classification tasks** within graders use **F1** (macro where multi-label) when multi-label slices are defined.

Implementation: `submission/evaluation/graders/`.

---

## 3. Inter-rater agreement (human vs system labels) — M-AGREE

For **advisory** fields only (e.g. “conflict_present”, “abstention_reason_class”):

| Metric | Use | Notes |
|---|---|---|
| **Cohen κ** | Binary fields | Primary |
| **Weighted κ** | Ordinal severity | Linear weights |
| **Gwet AC1** | High prevalence skew | Report alongside κ |

**Soft threshold (workshop):** κ ≥ 0.6 — **advisory indicator only**, not sole release gate (`23` §4). Below threshold triggers review (`25` safety monitoring), not auto-disposition.

Report 95% CI via bootstrap when sample size allows.

### 3.1 Calibration status (do not fabricate)

| Item | Status |
|---|---|
| Dual-annotated label slice | **Not collected** |
| Computed κ / AC1 | **None** — deliberately omitted |
| Code path | `submission/evaluation/metrics/agreement.py` returns `pending_human_calibration` when labels absent |
| Evidence note | [`../evidence/m_agree_pending_human_calibration.md`](../evidence/m_agree_pending_human_calibration.md) |

---

## 4. LLM-on vs rules-only comparison

| Run mode | Purpose |
|---|---|
| Offline rules/stub | Baseline for reproducibility `16` |
| LLM enabled | Delta on advisory narrative fields only |

Compare: abstention rate, G-SCHEMA, κ — **not** “accuracy of release decision.”

---

## 5. Multilingual + subgroup

| Check | Method | Status |
|---|---|---|
| Language metadata preserved (PV-02) | `tests/workflows/test_multilingual_subgroup.py` on PUB-04 | Deterministic pass path |
| No silent translation replace | Assert no `translated_narrative` collapse | Covered |
| Subgroup strata | Distinct `language` values remain in `source_facts` | Covered |
| κ by language subgroup | Requires human labels | **Pending** (same as M-AGREE) |

---

## 6. Evaluation protocol

1. Pin fixture index + catalog version in manifest.
2. Run CLI/API per PUB id via `scripts/evaluate_public_fixtures.py`.
3. Apply graders → `submission/evidence/evaluation_results.json` + `evidence/runs/PUB-*.json`.
4. Sample n≥30 per workflow for κ (**if** labels available) — currently blocked on human calibration.
5. Record failures with inject ids from `traceability_inject_workflow.csv`.

---

## 7. Acceptance (workshop)

| Gate | Criterion | Status |
|---|---|---|
| EVAL-01 | Schema/structural graders pass PUB-01..15 offline | **Met** (hard_gate via evaluate script) |
| EVAL-02 | Prohibited / boundary graders (exec, batch/PV/supply) | **Met** (hard_gate) |
| EVAL-03 | κ ≥ 0.6 soft on labelled slice | **Pending human calibration** — no fabricated score |
| EVAL-04 | F1 on multi-label G-* slices | Optional; not blocking |

---

## 8. Traceability

BAT-01, PV-01, PV-02, SUP-01, NN-05, `27` E-1/E-5, `13` §8 (G-ISO-EU), OTel spec (G-OTEL).
