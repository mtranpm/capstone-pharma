# AEGIS-PHARMA — SCQA

| Field | Entry |
|---|---|
| Owner | Product / value lead |
| Version / date | 1.0.0 / 2026-08-10 |
| Status | Phase 2 locked — canonical SCQA artefact |
| Canonical for | Executive framing, defence pitch, PRD handoff |
| Also summarized in | `01_discovery_problem_baseline_value.md`, `37_production_readiness_roadmap_defence.md` |
| Sources | A1 business framing, case pack, Phase 1–2 discovery |

---

## Executive SCQA

| Element | Statement |
|---|---|
| **Situation** | NovaCura must assemble conflict-visible, provenance-backed evidence for batch review, PV intake and supply recovery across fragmented SoRs. |
| **Complication** | Concurrent injects (genealogy, units, OOS/OOT, ICSR clocks, cold-chain, shortage) plus inspection/cyber pressure make manual reconciliation slow and hard to defend. |
| **Question** | How do we use AI to accelerate evidence packaging **without** replacing QP, PV or supply regulated decisions? |
| **Answer** | Ship **AEGIS Evidence Orchestrator**: advisory, fail-closed, offline-capable orchestration with contract-valid packets, authority gates, abstention and human review — **not** disposition, final PV, allocation, ship or recall. |

**One-line pitch:** *Faster, auditable evidence packets; humans keep every regulated pen.*

**Intervention boundary:** AEGIS addresses *evidence reconciliation and review-packet prep* for Batch / PV / Supply under PUB-01..15. It does **not** solve patent-cliff commercial strategy, full R&D/clinical ops automation, PQS redesign, or vendor replacement of Quality systems.

---

## Expanded SCQA

### Situation

NovaCura Therapeutics Group must prepare evidence-complete, conflict-visible, provenance-backed material for regulated batch-review, pharmacovigilance intake support and supply-recovery optioning across fragmented systems (LIMS, MES, eBR, QMS, safety DB, serialisation, cold-chain, RIM, and more).

### Complication

Evidence is contradictory and time-sensitive: genealogy break (SUA-88), unit mismatch (mg/L vs µg/mL), OOS/OOT dispute, unverified supplier-audit commitment, duplicate ICSR candidates, awareness-date conflict, MedDRA version mismatch, cold-chain logger/pallet disputes, excipient shortage and CMO capacity conflict, plus a 47-minute audit-capture gap and converging cyber/inspection pressure. Accountable humans reconcile this manually without a defensible orchestration trail.

### Question

How can NovaCura use AI to accelerate evidence reconciliation across Batch, PV and Supply workflows **without** replacing accountable regulated human decisions?

### Answer

Build an **advisory, fail-closed, offline-capable evidence orchestration system** (AEGIS Evidence Orchestrator) that finds, reconciles, explains and packages evidence with authority checks, structured contract-valid outputs, abstention, human-review gates, provenance hashes and audit export — never executing batch disposition, final PV decisions, allocation, shipment or recall.

---

## Scope reminder

| In | Out |
|---|---|
| Advisory Batch / PV / Supply evidence orchestration | Autonomous release / reject / recall |
| PUB-01..15 evaluation path | Final PV seriousness / causality / expectedness / reportability / signal |
| Contract-valid packets, abstention, human review | Stock allocation / shipment / inventory quality-status change |
| Offline / AI-disabled continuity | Clinical eligibility decisions; live SoR write-back |

---

## Change control

- Prefer editing **this file** for SCQA wording; sync short hooks in `01` and `37` if pitch or S/C/Q/A changes.
- Do not broaden Answer into regulated decision automation.
