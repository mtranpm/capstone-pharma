# 37 — Production Readiness Roadmap & Defence Package

| Field | Entry |
|---|---|
| Owner | Programme / defence lead |
| Version / date | 1.0.0 / 2026-08-10 |
| Status | Phase 5 — expanded defence narrative (evidence runs **pending**) |
| Sources | [`SCQA.md`](SCQA.md), `01`–`04`, `13`, `14`–`36`, workshop DoD |

---

## 1. Executive case hooks

### 1.1 Pitch (locked)

> **Faster, auditable evidence packets; humans keep every regulated pen.**

### 1.2 SCQA for slides / oral defence

**Canonical:** [`SCQA.md`](SCQA.md)

| | Hook |
|---|---|
| Situation | Fragmented SoRs force slow, hard-to-defend Batch / PV / Supply evidence assembly. |
| Complication | Concurrent injects (units, genealogy, OOS, ICSR clocks, cold-chain, shortage) + inspection pressure. |
| Question | Can AI accelerate packaging without replacing QP / PV / supply decisions? |
| Answer | AEGIS: advisory, fail-closed, offline-capable orchestration with contracts, abstention, human review. |

### 1.3 What we are *not* selling

- Autonomous release / PV final / ship / recall  
- Replacement of Quality independence or QP judgment  
- Neo4j or LLM as system of record (ADR-009, `11`)  
- Guaranteed board 14% lead-time cut — pressure context only (`04`, A-004)

### 1.4 Value claims & evidence pointers

| Claim | Evidence path | Status |
|---|---|---|
| Contract-valid advisory Batch/PV/Supply outputs | `evaluation/contracts/` + `submission/evidence/eval/` | **Pending** Phase 7–9 runs |
| Hybrid architecture (ports/FastAPI/React/GraphPort) | [`14_architecture_c4_adrs.md`](14_architecture_c4_adrs.md), `submission/src/aegis/` | **Documented**; OQ **pending** |
| Fail-closed prohibited actions | `domain/prohibited.py`, G-PROHIB, `28` T-LLM-05 | **Pending** green tests |
| Offline / AI-disabled continuity | [`16_reproducibility_and_offline_execution.md`](16_reproducibility_and_offline_execution.md), PUB-10 | **Pending** run manifest |
| Authority / untrusted-doc handling | [`12_document_authority_model.md`](12_document_authority_model.md), NN-04, G-AUTH | **Pending** eval |
| Human review gates | [`06_human_oversight_and_emergency_stop.md`](06_human_oversight_and_emergency_stop.md), ADR-006 | **Documented** |
| Traceability to injects & RTM | [`13_requirements_traceability_matrix.md`](13_requirements_traceability_matrix.md) §8, `traceability_inject_workflow.csv` | **Enriched** Phase 5 |
| Brownfield strangler (no big-bang SoR) | [`15_brownfield_modernization_plan.md`](15_brownfield_modernization_plan.md) | **Complete** (artefact) |
| Security OWASP LLM01–10 coverage | [`28_threat_abuse_model.md`](28_threat_abuse_model.md), red team [`31`](31_red_team_and_remediation.md) | Plan **complete**; RT **pending** |
| TEVV κ / F1 (soft κ≥0.6) | [`32_tevv_evaluation_strategy.md`](32_tevv_evaluation_strategy.md); [`../evidence/m_agree_pending_human_calibration.md`](../evidence/m_agree_pending_human_calibration.md) | Deterministic G-* **met**; κ **pending human calibration** (not fabricated) |
| Assurance & residual risk | [`27_assurance_case_residual_risk.md`](27_assurance_case_residual_risk.md) | Outline **complete** |
| GxP validation strategy | [`23_gxp_lifecycle_validation_strategy.md`](23_gxp_lifecycle_validation_strategy.md) | Plan **complete** |
| FinOps / token discipline | [`33`](33_token_efficiency_economics.md), [`34`](34_ai_finops_model.md) | Policy **complete** |
| Ops SLO / DR | [`35_operations_slo_incident_dr.md`](35_operations_slo_incident_dr.md) | Framework **complete** |
| Honest no-AI alternative | [`02_no_ai_and_solution_options.md`](02_no_ai_and_solution_options.md) | Seeded Phase 1 |

### 1.5 Stop / pivot lines for Q&A

- Disposition-like output → **stop** (STOP-01, `04`).  
- Untrusted knowledge authorizes → **pivot** to authority model (`12`, NN-04).  
- Offline path broken → **no-go** for defence (`16`, `21`).  
- κ below 0.6 → **investigate**, not auto-release (`32`).

---

## 2. Defence narrative (how artefacts compose)

```text
SCQA (why) → 05 operating model (who/how)
  → 14 ADRs + 08 DDD (what we built)
  → 13 RTM + contracts (requirements proof)
  → 16 offline recipe (reproducibility)
  → 06 + 20 human/agent bounds (oversight)
  → 28–31 security (trust boundaries)
  → 32 TEVV (measure advisory quality)
  → 27 assurance (residual risk acceptance)
  → evidence/ hashes (when runs exist)
```

**One-slide architecture:** C4 context + container in `14` §1–§2.  
**One-slide safety:** NN-01..03 + G-HR-01..06 + no execute UI (ADR-006).

---

## 3. Production readiness roadmap

| Horizon | Theme | Exit signal | Artefacts |
|---|---|---|---|
| **Now (workshop)** | Deterministic core + advisory workflows + doc package | Structure/RTM/ADRs complete; eval **pending** | `14`–`36`, `13` §8 |
| **Near (post-workshop)** | Green contract + PUB eval + red-team sample | EVAL-01..03 in `32`; evidence under `submission/evidence/` | `31`, `16` |
| **Pilot** | Read-only SoR APIs, one site | OQ per `23`; SLO `35` | `15` W1 |
| **Scale** | Optional Neo4j; enterprise LLM gateway | Parity tests; FinOps caps | `11`, `34` |
| **Later** | Vendor exit drills; full AIMS audit | `36`, `26` | Programme |
| **Never in scope** | MES/LIMS write-back; autonomous regulated acts | Explicit in `22`, `SCQA.md` | — |

---

## 4. Gate 7 defence checklist

| Item | Pointer | Done |
|---|---|---|
| Executive SCQA | [`SCQA.md`](SCQA.md) + §1 above | [x] |
| Architecture one-pager | [`14`](14_architecture_c4_adrs.md) | [x] doc |
| ADRs (≥10) | `14` ADR-001..012 | [x] |
| Human oversight / emergency stop | [`06`](06_human_oversight_and_emergency_stop.md) | [x] doc |
| Brownfield plan | [`15`](15_brownfield_modernization_plan.md) | [x] |
| RTM ISO/EU/LLM map | [`13`](13_requirements_traceability_matrix.md) §8 | [x] |
| TEVV strategy | [`32`](32_tevv_evaluation_strategy.md) | [x] doc |
| TEVV **results** | `submission/evidence/eval/` | [ ] **pending** |
| Clean-room reproducibility | [`16`](16_reproducibility_and_offline_execution.md) + CLI | [ ] **pending run** |
| Demo evidence hashes | `submission/evidence/runs/` | [ ] **pending** |
| Red team report | [`31`](31_red_team_and_remediation.md) | [ ] **pending** |
| Assurance / residual risk | [`27`](27_assurance_case_residual_risk.md) | [x] outline |
| Regulatory intended use | [`22`](22_intended_use_regulatory_applicability.md) | [x] |
| Cursor / engineering governance | [`17`](17_cursor_engineering_evidence.md) | [x] |

---

## 5. Oral defence flow (10–12 min suggested)

1. **SCQA** (30s) — `SCQA.md`  
2. **Boundary** (60s) — NN-01..03, what UI cannot do (`06`, ADR-006)  
3. **Architecture** (90s) — ports, offline default, GraphPort advisory (`14`, `11`)  
4. **Live or recorded demo** — CLI offline **when available**; disclose adapter modes  
5. **Evidence** — RTM §8, pending eval honesty  
6. **Security** — one LLM06 example from `28`  
7. **Close** — assurance claim C-1 with residual risks `27`

---

## 6. Evidence directory convention (target)

| Path | Content |
|---|---|
| `submission/evidence/runs/<run_id>/manifest.json` | Reproducibility `16` |
| `submission/evidence/runs/<run_id>/packet.json` | Workflow output |
| `submission/evidence/eval/<batch_id>/report.json` | Graders `32` |
| `submission/evidence/redteam/` | `31` findings |

*Do not overwrite challenge evidence outside `submission/` policy.*

---

## 7. Open items (honest status)

- Executable pytest + PUB fixture runs not yet recorded in this package version.  
- Legal classification of EU AI Act risk tier remains with RA/legal (`22`).  
- Production OQ/PQ out of workshop scope (`23`).

*Version bump to 1.0.0 reflects Phase 5 documentation completeness, not production go-live.*
