# 22 — Intended Use & Regulatory Applicability

| Field | Entry |
|---|---|
| Owner | RA / Quality |
| Version / date | 1.0.0 / 2026-08-10 |
| Status | Phase 5 — intended use statement |
| Sources | [`SCQA.md`](SCQA.md), `01`, `03`, `05`, EU AI Act framing, GxP applicability |

---

## 1. Product identification

| Field | Value |
|---|---|
| Name | AEGIS Evidence Orchestrator |
| Version | Workshop submission (0.x) |
| Manufacturer / sponsor | NovaCura programme (capstone) |
| Deployment | Advisory orchestration layer (read-only SoR) |

---

## 2. Intended use (IU)

AEGIS is intended to **assist qualified personnel** by locating, reconciling, explaining and packaging **evidence** for:

- Batch release **readiness review** support (not certification),
- Pharmacovigilance **case intake support** (not medical assessment finalization),
- Supply **recovery optioning** (not execution).

**Explicit exclusions (NN-01..03):** batch disposition; final PV seriousness/causality/reportability/signal; stock allocation/shipment/quality-status change/recall initiation.

---

## 3. Intended users

| User | Qualification | Use |
|---|---|---|
| QP / Quality release delegate | GxP role | Review batch packet |
| PV intake coordinator | Trained PV staff | Triage support packet |
| PV medical reviewer | Physician/pharmacovigilance | Receives export — decides |
| Supply planner | Supply ops | Review non-executing options |
| QA / RA | Inspection support | Audit export |

Not for patient self-service or clinical decision support at point of care.

---

## 4. Regulatory applicability (high level)

| Framework | Applicability | Rationale |
|---|---|---|
| **EU GMP (EudraLex Vol 4)** | **Indirect** — supports QMS evidence; not a batch record system | Human QP remains accountable |
| **21 CFR Part 11** (if US scope) | **Partial** — audit trail / e-records for AEGIS exports if adopted | Validate per `23` |
| **EU AI Act** | **Likely limited risk / GPAI use via vendor** — transparency, oversight, logging | See `26`, `22` §5 |
| **GDPR** | **Yes** for PV narratives | `30` |
| **ISO 42001** | **AIMS alignment** for AI management | `26` |
| **ICH E2B / PV regs** | **Support only** — does not submit ICSRs | NN-02 |

*Formal classification (SaMD vs non-device) requires legal review — **assumption A-005 pending** (log if opened).*

---

## 5. EU AI Act positioning (non-legal summary)

| Topic | AEGIS posture |
|---|---|
| Prohibited practices | No subliminal manipulation, social scoring, or biometric inference |
| High-risk annex | Not performing safety-critical autonomous decisions listed in NN-01..03 |
| Transparency | Users informed they interact with AI-assisted drafts (`07`, UI labelling) |
| Human oversight | G-HR gates mandatory (`06`) |
| Accuracy / robustness | TEVV + abstention (`32`, NN-05) |

---

## 6. Claims boundary (marketing / defence)

Allowed: faster evidence **packaging**, conflict visibility, provenance, offline continuity.  
Not allowed: guaranteed cycle-time reduction, “AI release,” “auto-reportable,” “ship recommendation executed.”

Align [`37`](37_production_readiness_roadmap_defence.md) §1.3.

---

## 7. Traceability

| REQ | Section |
|---|---|
| NN-01..03 | §2 |
| XC-07 | §2 clinical exclusion |
| PV-02 | §2 PV support |
