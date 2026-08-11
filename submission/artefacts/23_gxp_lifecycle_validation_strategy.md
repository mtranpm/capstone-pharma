# 23 — GxP Lifecycle & Validation Strategy

| Field | Entry |
|---|---|
| Owner | Quality / Validation |
| Version / date | 1.0.0 / 2026-08-10 |
| Status | Phase 5 — CSV-oriented validation plan |
| Sources | `22`, `24`, GAMP 5 (risk-based), `13`, ADRs |

---

## 1. Validation philosophy

AEGIS is **GAMP Category 5** (custom application) with **configured** integrations. Validation is **risk-based**: focus on data integrity, audit trail, access control, and prohibited-action prevention — not on proving LLM “correctness” for regulated decisions (which are out of scope).

---

## 2. V-Model mapping

| Phase | Deliverable | Workshop status |
|---|---|---|
| URS | RTM `13` + NN rows | Seeded |
| FRS / specs | `Docs/specs/`, contracts | Active |
| Design | `14`, `08`, `09` | This phase |
| Build | `submission/src` | In progress |
| IQ | Environment manifest `16` | **Pending** |
| OQ | Contract + workflow tests | **Pending** run records |
| PQ | Pilot on live read APIs | Out of workshop |
| Release | Change control + trace matrix | Gate 7 `37` |

---

## 3. Critical requirements (validation focus)

| ID | Validation focus | Method |
|---|---|---|
| NN-01..03 | Prohibited actions impossible via API/UI | OQ scripted + penetration |
| NN-04 | Authority gate | OQ catalog injects |
| NN-05 | Abstention on ambiguity | OQ injects INJ-021..024 |
| NN-06 | Offline path | OQ PUB-10 |
| BAT-02 | Verbatim units/values | OQ diff vs SoR |
| G-HR-01..06 | Human gate before export | OQ UI + audit |

---

## 4. AI-specific validation stance

| Element | Treatment |
|---|---|
| LLM adapter | **Validated as configurable component** — substitute per `18`; re-OQ on change |
| Training data | Not validated in workshop — vendor + governance evidence |
| TEVV metrics | Soft thresholds κ≥0.6 advisory only (`32`) — not alone for release |
| Rules engine | Primary object of OQ |

---

## 5. Change control

| Change type | Revalidation depth |
|---|---|
| Port adapter swap (same contract) | Regression suite |
| Schema version bump | Full contract + affected OQ |
| Tool manifest | Security OQ + red-team sample |
| Model swap | `18` procedure + TEVV slice |

---

## 6. Validation evidence package

| Document | Path |
|---|---|
| RTM | `13` |
| Risk assessment | `25` |
| Trace logs / audit design | `24` |
| Test protocols | `submission/tests/` + eval **pending** |
| Deviation log | `submission/evidence/validation/` **pending** |

---

## 7. Traceability

All NN and G-HR rows map to OQ cases in RTM §8 (ISO/EU controls).
