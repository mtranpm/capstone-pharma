# 01 — Discovery: Problem, Baseline & Value Hypothesis

| Field | Entry |
|---|---|
| Owner | Product / value lead |
| Version / date | 0.2.0 / 2026-08-10 |
| Status | Phase 2 finalized — executive SCQA locked for PRD |
| Sources | `Docs/DDD-Lab/Phase 1/A1_Business_Problem_Framing.md`, `case/INTEGRATED_CASE.md`, `case/STAKEHOLDER_PACK.md`, `data/inject_evidence_map.csv`, `evaluation/PUBLIC_FIXTURE_INDEX.csv`, `submission/artefacts/00_case_discovery_understanding.md` |

## 0. Executive SCQA (defence hook)

**Canonical SCQA file:** [`SCQA.md`](SCQA.md) (edit there for S/C/Q/A wording).

| Element | Statement |
|---|---|
| **S** | NovaCura must assemble conflict-visible, provenance-backed evidence for batch review, PV intake and supply recovery across fragmented SoRs. |
| **C** | Concurrent injects (genealogy, units, OOS/OOT, ICSR clocks, cold-chain, shortage) plus inspection/cyber pressure make manual reconciliation slow and hard to defend. |
| **Q** | How do we use AI to accelerate evidence packaging **without** replacing QP, PV or supply regulated decisions? |
| **A** | Ship **AEGIS Evidence Orchestrator**: advisory, fail-closed, offline-capable orchestration with contract-valid packets, authority gates, abstention and human review — **not** disposition, final PV, allocation, ship or recall. |

**Intervention boundary (narrower than the enterprise problem):** AEGIS addresses *evidence reconciliation and review-packet prep* for Batch / PV / Supply under PUB-01..15. It does **not** solve patent-cliff commercial strategy, full R&D/clinical ops automation, PQS redesign, or vendor replacement of Quality systems.

**One-line pitch for artefact 37:** *Faster, auditable evidence packets; humans keep every regulated pen.*

---

## 1. SCQA (expanded)

Full expanded text lives in [`SCQA.md`](SCQA.md). Summary: advisory, fail-closed, offline-capable evidence orchestration for Batch / PV / Supply — never disposition, final PV, allocation, shipment or recall.

## 2. Measurable problem & baseline

| Metric / baseline (from case framing) | Evidence | Notes |
|---|---|---|
| Board target: 14% reduction in end-to-end release lead time | `data/board_requests.csv`, A1 §6 | AEGIS contributes via packet prep time — **not** by weakening Quality / QP authority |
| Manual reconciliation burden across Batch/PV/Supply | A1 §3–4; inject catalogue | Baseline is human-only evidence assembly |
| Inspection: 72-hour multi-agency evidence package | A1 narrative | Gap: cannot assemble quickly today |
| Conflicting KPIs (speed vs completeness) | `kpi_conflicts.csv`, INJ-002 | Quality vs Manufacturing tension |

**Affected decisions (human-owned):** EU QP certification / batch disposition; PV seriousness/causality/expectedness/reportability/signal confirmation; supply allocation / inventory status / shipment / recall approvals.

## 3. Value hypothesis (finalized for PRD)

| Outcome | Mechanism | Assumption | Stop / pivot signal |
|---|---|---|---|
| Faster review packet prep | Automated evidence gather + contradiction/gap surfacing | Humans still decide; packets are trusted | Packet error rate rises vs baseline |
| Higher evidence fidelity | Provenance + authority + as-of checks | Knowledge catalog statuses are used | Untrusted docs treated as authority |
| Lower review burden | Structured abstentions reduce rework | Reviewers accept “no answer” | Forced false completeness |
| Contained cost | Deterministic path + token budgets (OTel) | Offline mode covers outages | Unbounded inference / DoW |
| Defensible inspection response | Audit export + hashes + RTM | Claims map to immutable artefacts | Claims without evidence paths |

**Success proxy for workshop defence:** PUB-01..15 contract-valid advisory outputs; graders pass; AI-disabled path works; no prohibited-action controls in UI/CLI.

## 4. In / out of scope (intervention)

**In:** Advisory Batch/PV/Supply evidence orchestration; PUB-01..15 evaluation; ontology + Neo4j advisory KG dashboard; FastAPI + React human review; ISO/EU + OWASP controls.

**Out:** Autonomous release/reject/recall; final PV decisions; stock allocation/shipment; clinical eligibility decisions; live production write-back; treating Docs/Regulations as legal advice; enterprise-wide PQS replacement; commercial patent-cliff programmes.

## 5. Workflow ↔ fixture map (mandatory)

| Workflow | Public fixtures | Contract | Primary inject examples |
|---|---|---|---|
| Batch evidence readiness | PUB-01..03 | `batch_response.schema.json` | INJ-021 genealogy, INJ-023 OOS/OOT, INJ-024 units, INJ-028 QP gap |
| PV intake support | PUB-04..06 | `pv_response.schema.json` | Duplicate/clock/listedness injects (D06) |
| Supply options | PUB-07..08 | `supply_response.schema.json` | Cold-chain / shortage / allocation injects (D07) |
| Cross-cutting | PUB-09..15 | Participant contracts | Security, reliability, privacy, agent, FinOps, clinical |

Full inject register: [`traceability_inject_workflow.csv`](traceability_inject_workflow.csv) (84 injects).

## 6. Prohibited AI behaviours (explicit)

- Release, reject, reprocess, relabel or recall a batch.
- Final PV seriousness, causality, expectedness, reportability or signal confirmation.
- Allocate stock, reserve capacity, change inventory quality status, ship product or initiate recall.
- Change formulation, specification or clinical eligibility.

## 7. Fact / interpretation / assumption

| Type | Statement |
|---|---|
| Fact | Challenge data contains deliberate conflicts (e.g. SUA-88, unit mismatch) cited in A1 and PUB-01 |
| Interpretation | Advisory orchestration is the narrowest intervention that still addresses board cycle-time pressure |
| Assumption | Synthetic training data is sufficient for offline deterministic evaluation |
| Decision | Proceed with hybrid Python core + React UI + Neo4j advisory graph (see plan locked decisions) |

## 8. Phase 2 lock

| Item | State |
|---|---|
| Executive SCQA | Locked in §0; expands in §1 |
| Value hypothesis | Locked in §3 for PRD (`05`–`07`) |
| Intervention narrower than full problem | Explicit in §0 and §4 |
| Handoff to artefact `37` | Executive hooks seeded; full defence in Gate 7 / Phase 10 |
