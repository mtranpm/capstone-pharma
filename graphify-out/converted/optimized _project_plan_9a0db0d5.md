<!-- converted from optimized _project_plan.xlsx -->

## Sheet: Overview
| Project AEGIS-PHARMA — Optimized FDE Project Plan (5-FDE Parallel Delivery Model) |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Same SCQA → DDD → C4 → ADR → SDD/PRD spine and DMAIC control cycle as the reference plan, restructured into five independent lanes so a 5-person FDE team can work in parallel from Day 1, with an owner and a reviewer on every deliverable. |  |  |  |  |  |  |  |
| What changed vs. the original single-thread WBS |  |  |  |  |  |  |  |
| Problem | Every phase (e.g. Discover 1.1→1.2→1.3→1.4) was one dependency chain. Only one FDE could touch a phase at a time; the rest waited. |  |  |  |  |  |  |
| Fix (pass 1) | The WBS is split into 5 parallel lanes: 3 workflow lanes (one per mandatory workflow) that each run their own mini end-to-end lifecycle, plus 2 cross-cutting lanes (Architecture/Security, and Product/Governance/Evaluation) that own enterprise-wide concerns. |  |  |  |  |  |  |
| Result | 96 granular tasks (vs. 28), each 0.25–1.0 person-day, with dependencies almost entirely WITHIN a lane. A lane never has to wait on another lane except at 7 explicit Sync Gates (one per phase) where outputs are reconciled. |  |  |  |  |  |  |
| Ownership | Every task has exactly one Owner FDE and one named Reviewer FDE who is never the same person — see the WBS sheet and the Review & Gate Protocol sheet. |  |  |  |  |  |  |
| Independence | See the 'FDE Sequences' sheet: each FDE has a complete, self-contained, day-by-day task list for the full 10 days that does not require reading anyone else's sequence to execute — only the Sync Gate rows require brief joint attendance. |  |  |  |  |  |  |
| Rubric strategy | See the 'Rubric Coverage Map' sheet: every one of the 180 scoring points and every hard gate is traced to specific WBS IDs and owners, so nothing in the 17-criterion rubric is structurally unowned. |  |  |  |  |  |  |
| Fix (pass 2) | A second SME pass benchmarked the plan against the actual Palantir FDE model ("ship on day one", field-as-ground-truth over documents) and closed four gaps: (1) a Day-3 throwaway walking-skeleton spike per workflow, so real code and real data inform Architect/Specify instead of the reverse — build no longer starts cold on Day 9; (2) the ontology/semantic layer is now a living artefact with delta-review checkpoints at Days 5, 7 and 10, not a one-time Day-3 freeze; (3) two 'gemba' sessions on Day 9 where the Architecture lead and the Governance lead each hands-on drive part of a workflow build instead of only reviewing it on paper; (4) a named-persona acceptance check (drawn from the real STAKEHOLDER_PACK roles — EU Qualified Person, CISO, Head of Pharmacovigilance, etc.) folded into every one of the 9 Sync Gates' exit criteria, so gates check for stakeholder acceptance, not just internal FDE sign-off. |  |  |  |  |  |  |
| Planning assumptions |  |  |  |  |  |  |  |
| Team | 5 FDEs, full-time, one dedicated lane owner each (FDE-1..FDE-3 = workflow leads, FDE-4 = architecture/security lead, FDE-5 = product/governance/evaluation lead). |  |  |  |  |  |  |
| Indicative duration | 10 working days (2 weeks), controlled parallel workstreams, same window as the reference plan. |  |  |  |  |  |  |
| Effort model | The Effort (person-days) column in the WBS is build effort charged to the Owner only. Peer review is a standing ~45–60 minute/day commitment per FDE (see Review & Gate Protocol), not a separately budgeted day — this is how granular review stays lightweight rather than doubling the schedule. |  |  |  |  |  |  |
| Owner build-effort totals | FDE-1: 9.25d, FDE-2: 9.25d, FDE-3: 9.25d, FDE-4: 10.5d, FDE-5: 9.75d after the pass-2 additions (spikes, ontology deltas, gemba sessions). FDE-4 now runs about half a day over a strict 10-day budget — a deliberate, small trade-off for de-risking Day-9 build. If the team needs to claw it back, trim P6-ARC-1 (ADR-register consolidation, currently 0.5d) to 0.25d first, since most of its content is already drafted incrementally as workflow-specific ADRs earlier in the WBS. |  |  |  |  |  |  |
| Delivery mode | Offline deterministic POC plus safe manual fallback for all three workflows. |  |  |  |  |  |  |
| Mandatory workflows | A: GxP evidence reconciliation (batch). B: PV case intake and signal-support. C: Bounded supply-shortage and cold-chain recovery planning. |  |  |  |  |  |  |
| Safety boundary | No workflow may autonomously release/reject a batch, make a final PV decision, allocate/reserve stock, ship, or initiate a recall. Enforced structurally: every lane's Architect-phase task includes an explicit fail-closed control point, reviewed by the Architecture/Security lead. |  |  |  |  |  |  |
| Work location | All participant work under submission/. |  |  |  |  |  |  |
| Lifecycle at a glance (unchanged spine, now lane-parallel within each phase) |  |  |  |  |  |  |  |
| Phase | Lifecycle step | DMAIC | Schedule window | Primary outcome | Exit gate (Sync ID) | Lane leads engaged |  |
| 1. Discover & Qualify | Discover | Define | Day 1-2 | Shared understanding of business context and decisions, per workflow and enterprise-wide | P1-SYNC-1 | All 5, in parallel |  |
| 2. Frame the Problem | Frame | Measure | Day 2 | Measured problem, scope, alternatives and success measures, per workflow and enterprise-wide | P2-SYNC-1 | All 5, in parallel |  |
| 3. Model Domain & Semantics | Model | Analyze | Day 2-4 | DDD bounded contexts and semantic foundation, contributed per workflow and consolidated | P3-SYNC-1, P3-SYNC-2 | All 5, in parallel |  |
| 4. Architect the Solution | Architect | Improve | Day 4-5 | C4 architecture and control boundaries, per workflow and consolidated | P4-SYNC-1 | All 5, in parallel |  |
| 5. Specify & Test | Specify | Improve | Day 6-7 | SRS, HLD, LLD, contracts and testable requirements, per workflow | P5-SYNC-1 | All 5, in parallel |  |
| 6. Decide & Govern | Decide | Improve / Control | Day 8 | ADRs, risk controls, validation and operating model, per workflow and consolidated | P6-SYNC-1 | All 5, in parallel |  |
| 7. Deliver & Evaluate | Deliver & Evaluate | Control | Day 9-10 | Working POC (3 workflows), evaluation evidence, handover and roadmap | P7-SYNC-1, P7-SYNC-2 | All 5, in parallel |  |
| Success principle | Move from ambiguity to a bounded, explainable, governed and deployable AI workflow — achieved five ways in parallel instead of one way in sequence. |  |  |  |  |  |  |
## Sheet: Team & Lane Model
| Team & Lane Model — 5 FDEs, 5 Parallel Lanes |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| FDE | Lane code | Lane / Primary responsibility | Home case dimensions & focus | Primary rubric areas owned | Review responsibilities |  |
| FDE-1 | WA | Workflow A — GxP Evidence Reconciliation | Batch genealogy, laboratory results, EM, OOS/OOT, CAPA, change control, release-packet completeness (D04, D05). | RUB-01,02,03,04,05,06,07,08,09,13 (their workflow's slice) | Reviews Workflow C's case-reading/current-state tasks in P1 (round-robin); Workflow B's requirements/HLD/LLD in P5; reviewed by FDE-2 (peer, P1/P2), FDE-4 (architecture sub-tasks, P3/P4/P6-ADR/P7-build), FDE-5 (validation & evaluation sub-tasks). |  |
| FDE-2 | WB | Workflow B — PV Case Intake | Case narratives, duplicate detection, terminology normalization, reporting-clock reconstruction, listedness (D03, D06). | RUB-01,02,03,04,05,06,07,08,09,11,13 (their workflow's slice) | Reviews Workflow A's case-reading/current-state tasks in P1; Workflow A's test fixtures & verification in P5/P7; reviewed by FDE-3 (peer, P1/P2), FDE-4 (architecture sub-tasks), FDE-5 (privacy & evaluation sub-tasks). |  |
| FDE-3 | WC | Workflow C — Bounded Supply Planning | Inventory, cold-chain, CMO capacity, allocation policy, compassionate use (D08, D12). | RUB-01,02,03,04,05,06,07,08,09,13,15 (their workflow's slice) | Reviews Workflow B's case-reading/current-state tasks in P1; Workflow C's own test fixtures reviewed by FDE-2; reviewed by FDE-1 (peer, P1/P2), FDE-4 (architecture sub-tasks), FDE-5 (reliability & evaluation sub-tasks). |  |
| FDE-4 | ARC | Domain, Architecture & Security lead | Cross-workflow fragmentation, DDD spine, C4, Zero Trust, threat modelling (D02, D05 shared, D10, D13). | RUB-04,05,06,07,10 (owns), plus reviews RUB-08,09 architecture sub-tasks in every workflow | Reviews all GOV-lane deliverables and all workflow architecture/data/security sub-tasks (P3, P4, P6-ADR, P7-build); reviewed by FDE-5 (peer cross-cutting check). |  |
| FDE-5 | GOV | Product, Value, Governance & Evaluation lead | Portfolio/value, stakeholders, regulatory, privacy/ethics, TEVV, FinOps, operating model (D01, D07, D09, D11, D12). | RUB-01,02,03,11,12,13,14,16,17 (owns), plus reviews RUB-09,13 sub-tasks in every workflow | Reviews all ARC-lane deliverables and all workflow validation/privacy/reliability/evaluation sub-tasks (P1 baselines, P2 value, P6, P7-evaluate); reviewed by FDE-4 (peer cross-cutting check); facilitates most sync gates. |  |
| Reviewer-assignment rule (never self-review, cross-pod where it adds signal) |  |  |  |  |  |  |
| 1. Governance-lane (GOV) deliverables are always reviewed by the Architecture lead (FDE-4). |  |  |  |  |  |  |
| 2. Architecture-lane (ARC) deliverables are always reviewed by the Governance lead (FDE-5). |  |  |  |  |  |  |
| 3. In Discover, Frame, Specify and most of Deliver, workflow-lane deliverables are peer-reviewed round robin: A→reviewed by B's lead, B→reviewed by C's lead, C→reviewed by A's lead. |  |  |  |  |  |  |
| 4. In Model and Architect — the two domain-modelling / architecture phases — workflow-lane deliverables are reviewed by the Architecture lead (FDE-4), because FDE-4 must internalize all three workflows before consolidating the enterprise DDD/C4 views at the Sync Gate. |  |  |  |  |  |  |
| 5. Workflow-specific ADRs (Decide phase) are reviewed by FDE-4; workflow validation/privacy/reliability notes are reviewed by FDE-5; workflow evaluation results (Deliver phase) are reviewed by FDE-5. |  |  |  |  |  |  |
| 6. Sync Gates are owned by a rotating integrator and reviewed by all 5 FDEs together in a short (20-30 minute) checkpoint — this is the only point where the whole team meets synchronously. |  |  |  |  |  |  |
## Sheet: WBS
| WBS ID | Lane | Phase | Lifecycle step | DMAIC | Activity | Deliverable | Owner (FDE) | Reviewer (FDE) | Build effort
(person-days) | Dependency
(WBS ID) | Task type | Rubric ID(s) | FDE principle / gate | Exit criteria | Schedule window |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P1-GOV-1 | Product / Value / Governance / Evaluation | 1. Discover & Qualify | Discover | Define | Read case, org/portfolio context; catalogue evidence boundary and label assumptions (D01, D07, D09, D11, D12). | Case reading log & assumptions register | FDE-5 | FDE-4 | 0.5 | — | Parallel | RUB-01 | Evidence discipline: cite source or mark Assumption | Claims cited or marked Assumption | Day 1 |
| P1-GOV-2 | Product / Value / Governance / Evaluation | 1. Discover & Qualify | Discover | Define | Enterprise stakeholder & decision-rights map incl. incentive conflicts (INJ-002) and escalation design. | Stakeholder & decision-rights map | FDE-5 | FDE-4 | 0.5 | P1-GOV-1 | Parallel | RUB-02 | Ambiguity as first-class input | Accountable owners and decision rights identified | Day 1-2 |
| P1-ARC-1 | Domain, Architecture & Security | 1. Discover & Qualify | Discover | Define | Read case, system inventory and source-authority fragmentation across the estate (D02, D10). | Case reading log (architecture slice) | FDE-4 | FDE-5 | 0.5 | — | Parallel | RUB-01 | Evidence discipline | Claims cited or marked Assumption | Day 1 |
| P1-ARC-2 | Domain, Architecture & Security | 1. Discover & Qualify | Discover | Define | Draft enterprise bounded-context long-list (Research, Clinical, Manufacturing, Quality, Safety, Regulatory, Supply) from acquisition fragmentation (INJ-005). | Draft bounded-context long-list | FDE-4 | FDE-5 | 0.25 | P1-ARC-1 | Parallel | RUB-04 | DDD before containers | Candidate contexts named with tentative owners | Day 1-2 |
| P1-WA-1 | Workflow A — GxP Evidence Reconciliation | 1. Discover & Qualify | Discover | Define | Read Workflow-A case slice: batch genealogy, EM, OOS, CAPA, release packet (D04, D05). | Case reading log (Workflow A) | FDE-1 | FDE-2 | 0.5 | — | Parallel | RUB-01 | Evidence discipline | Claims cited or marked Assumption | Day 1 |
| P1-WA-2 | Workflow A — GxP Evidence Reconciliation | 1. Discover & Qualify | Discover | Define | Workflow-A stakeholders (QP, Quality release, MES/LIMS/QMS owners) + current-state batch-review map + baseline pain points (INJ-021, INJ-023, INJ-028). | Current-state map & baseline (batch review) | FDE-1 | FDE-2 | 0.5 | P1-WA-1 | Parallel | RUB-01, RUB-02, RUB-03 | Product mindset — outcomes not activity | Baseline and affected decisions are evidenced | Day 1-2 |
| P1-WB-1 | Workflow B — PV Case Intake | 1. Discover & Qualify | Discover | Define | Read Workflow-B case slice: case narratives, duplicate/terminology/clock issues (D03, D06). | Case reading log (Workflow B) | FDE-2 | FDE-3 | 0.5 | — | Parallel | RUB-01 | Evidence discipline | Claims cited or marked Assumption | Day 1 |
| P1-WB-2 | Workflow B — PV Case Intake | 1. Discover & Qualify | Discover | Define | Workflow-B stakeholders (PV hub, safety physicians, reporting authorities) + current-state intake map + baseline pain points (duplicate rate, clock backlog, listedness delay). | Current-state map & baseline (PV intake) | FDE-2 | FDE-3 | 0.5 | P1-WB-1 | Parallel | RUB-01, RUB-02, RUB-03 | Product mindset — outcomes not activity | Baseline and affected decisions are evidenced | Day 1-2 |
| P1-WC-1 | Workflow C — Bounded Supply Planning | 1. Discover & Qualify | Discover | Define | Read Workflow-C case slice: shortage, cold-chain, CMO, allocation policy (D08, D12). | Case reading log (Workflow C) | FDE-3 | FDE-1 | 0.5 | — | Parallel | RUB-01 | Evidence discipline | Claims cited or marked Assumption | Day 1 |
| P1-WC-2 | Workflow C — Bounded Supply Planning | 1. Discover & Qualify | Discover | Define | Workflow-C stakeholders (supply planners, QP release, compassionate-use, CMO) + current-state shortage/cold-chain map + baseline pain points. | Current-state map & baseline (supply/cold-chain) | FDE-3 | FDE-1 | 0.5 | P1-WC-1 | Parallel | RUB-01, RUB-02, RUB-03 | Product mindset — outcomes not activity | Baseline and affected decisions are evidenced | Day 1-2 |
| P1-SYNC-1 | Cross-Lane Sync Gate | 1. Discover & Qualify | Discover | Define | Consolidate the five lane outputs into one Context & Assumptions Log and one Enterprise Decision-Rights Map; resolve naming conflicts across lanes. | Unified context/assumptions log (feeds 01_BUSINESS_CASE) | FDE-5 | All FDEs (Steering) | 0.5 | P1-GOV-2, P1-ARC-2, P1-WA-2, P1-WB-2, P1-WC-2 | SYNC GATE | RUB-01, RUB-02 | Traceability: cite backward, breaks are risks | D1 gate — case scope, assumptions and decision rights recorded (Go / Rework). Persona check: the Chief Quality Officer and the EU Qualified Person recognize their decision authority as stated. | Day 2 |
| P2-GOV-1 | Product / Value / Governance / Evaluation | 2. Frame the Problem | Frame | Measure | Enterprise SCQA narrative synthesizing the three workflow problem framings into one decision narrative. | SCQA decision narrative | FDE-5 | FDE-4 | 0.5 | P1-SYNC-1 | Parallel | RUB-01 | SCQA forces the real question into the open | Narrative is agreed and traceable to Discover evidence | Day 2 |
| P2-GOV-2 | Product / Value / Governance / Evaluation | 2. Frame the Problem | Frame | Measure | KPI tree, value hypothesis, benefits case and stop/pivot criteria (DMAIC Measure); no-AI / rules / analytics / workflow-redesign / buy-build-partner comparison answering the process-excellence challenge (INJ-003). | Value hypothesis, KPI tree & no-AI comparison | FDE-5 | FDE-1 | 0.75 | P2-GOV-1 | Parallel | RUB-01, RUB-03 | No-AI challenge is mandatory, not optional | Measures, thresholds and alternatives are documented | Day 2 |
| P2-ARC-1 | Domain, Architecture & Security | 2. Frame the Problem | Frame | Measure | Intended-use / prohibited-use boundary draft from the executive AI-use-boundaries directive (INJ-006): no autonomous batch release, PV decision, allocation or recall. | Prohibited-action boundary specification (draft) | FDE-4 | FDE-5 | 0.5 | P1-SYNC-1 | Parallel | RUB-02 (hard-gate driver) | HITL / authority boundaries are non-negotiable | Prohibited regulated actions are explicit | Day 2 |
| P2-ARC-2 | Domain, Architecture & Security | 2. Frame the Problem | Frame | Measure | Trust-boundary / authority-hierarchy framing: which human role can override or halt the AI, and how escalation works. | Trust-boundary & override-authority note | FDE-4 | FDE-5 | 0.25 | P2-ARC-1 | Parallel | RUB-02, RUB-10 | HITL / authority boundaries | Override authority is named per workflow | Day 2 |
| P2-WA-1 | Workflow A — GxP Evidence Reconciliation | 2. Frame the Problem | Frame | Measure | Workflow-A SCQA and measurable problem statement; restate prohibited actions for batch disposition. | Problem statement (Workflow A) | FDE-1 | FDE-2 | 0.5 | P1-WA-2 | Parallel | RUB-01, RUB-02 | SCQA at engagement start | Problem is measurable and traceable to baseline | Day 2 |
| P2-WA-2 | Workflow A — GxP Evidence Reconciliation | 2. Frame the Problem | Frame | Measure | Workflow-A value hypothesis and success measures: release-lead-time reduction, evidence-gap reduction, contradiction-detection rate. | Value hypothesis (Workflow A) | FDE-1 | FDE-2 | 0.5 | P2-WA-1 | Parallel | RUB-03 | DMAIC Measure discipline | Thresholds are measurable | Day 2 |
| P2-WB-1 | Workflow B — PV Case Intake | 2. Frame the Problem | Frame | Measure | Workflow-B SCQA and measurable problem statement; restate prohibited actions for seriousness/causality/reportability/signal decisions. | Problem statement (Workflow B) | FDE-2 | FDE-3 | 0.5 | P1-WB-2 | Parallel | RUB-01, RUB-02 | SCQA at engagement start | Problem is measurable and traceable to baseline | Day 2 |
| P2-WB-2 | Workflow B — PV Case Intake | 2. Frame the Problem | Frame | Measure | Workflow-B value hypothesis and success measures: duplicate-detection rate, clock-reconstruction accuracy, listedness-review delay. | Value hypothesis (Workflow B) | FDE-2 | FDE-3 | 0.5 | P2-WB-1 | Parallel | RUB-03 | DMAIC Measure discipline | Thresholds are measurable | Day 2 |
| P2-WC-1 | Workflow C — Bounded Supply Planning | 2. Frame the Problem | Frame | Measure | Workflow-C SCQA and measurable problem statement; restate prohibited actions for inventory/allocation/recall. | Problem statement (Workflow C) | FDE-3 | FDE-1 | 0.5 | P1-WC-2 | Parallel | RUB-01, RUB-02 | SCQA at engagement start | Problem is measurable and traceable to baseline | Day 2 |
| P2-WC-2 | Workflow C — Bounded Supply Planning | 2. Frame the Problem | Frame | Measure | Workflow-C value hypothesis and success measures: option-generation time, stockout avoidance, cold-chain excursion response time. | Value hypothesis (Workflow C) | FDE-3 | FDE-1 | 0.5 | P2-WC-1 | Parallel | RUB-03 | DMAIC Measure discipline | Thresholds are measurable | Day 2 |
| P2-SYNC-1 | Cross-Lane Sync Gate | 2. Frame the Problem | Frame | Measure | Prioritize the three workflows and use cases; unify the three prohibited-use statements into one Scope & Safety Boundary document; approve the release backlog. | Prioritized scope, safety boundary & release backlog | FDE-4 | All FDEs (Steering) | 0.5 | P2-GOV-2, P2-ARC-2, P2-WA-2, P2-WB-2, P2-WC-2 | SYNC GATE | RUB-01, RUB-02, RUB-03 | Gates are blocking on the critical path | D2 gate — scope, priorities and safety boundary approved (Go / Rework). Persona check: the EU Qualified Person, the Global Head of Pharmacovigilance and the Supply Chain VP each confirm their final-decision authority is preserved as stated. | Day 2 |
| P3-ARC-1 | Domain, Architecture & Security | 3. Model Domain & Semantics | Model | Analyze | Shared-kernel modelling: cross-context concepts (Product, Batch, Organisation, Site) and a cross-identifier map. | Shared-kernel model | FDE-4 | FDE-5 | 0.5 | P2-SYNC-1 | Parallel | RUB-04 | Language and boundaries before containers | Shared concepts are owned and bounded | Day 2-3 |
| P3-ARC-2 | Domain, Architecture & Security | 3. Model Domain & Semantics | Model | Analyze | Authority, effective-date, jurisdiction, supersession and conflict-resolution rule framework (CCDS v4 vs Protocol v4.1/v5.0, EMA letter 2026-114). | Semantic authority & provenance framework | FDE-4 | FDE-5 | 0.5 | P3-ARC-1 | Parallel | RUB-05, RUB-06 | Conflicts preserved, not silently resolved | Conflicts are preserved and resolution rules are explicit | Day 3 |
| P3-WA-1 | Workflow A — GxP Evidence Reconciliation | 3. Model Domain & Semantics | Model | Analyze | Workflow-A bounded context and ubiquitous language (Batch / Quality release domain). | Bounded context & language (Workflow A) | FDE-1 | FDE-4 | 0.5 | P2-WA-2 | Parallel | RUB-04 | DDD bounded contexts + ubiquitous language | Context, ownership and key invariants are defined | Day 2-3 |
| P3-WA-2 | Workflow A — GxP Evidence Reconciliation | 3. Model Domain & Semantics | Model | Analyze | Workflow-A entity/identifier/authority list and data contract (LIMS v1→v2 diff, MES event schema). | Data contract & ontology input (Workflow A) | FDE-1 | FDE-4 | 0.5 | P3-WA-1 | Parallel | RUB-05, RUB-06 | Data contracts as first-class artefacts | Identifiers, terms and units have governed definitions | Day 3 |
| P3-WB-1 | Workflow B — PV Case Intake | 3. Model Domain & Semantics | Model | Analyze | Workflow-B bounded context and ubiquitous language (Safety / Pharmacovigilance domain). | Bounded context & language (Workflow B) | FDE-2 | FDE-4 | 0.5 | P2-WB-2 | Parallel | RUB-04 | DDD bounded contexts + ubiquitous language | Context, ownership and key invariants are defined | Day 2-3 |
| P3-WB-2 | Workflow B — PV Case Intake | 3. Model Domain & Semantics | Model | Analyze | Workflow-B entity/identifier/authority list and data contract (E2B(R3) fragment, MedDRA terms, duplicate-detection keys). | Data contract & ontology input (Workflow B) | FDE-2 | FDE-4 | 0.5 | P3-WB-1 | Parallel | RUB-05, RUB-06 | Data contracts as first-class artefacts | Identifiers, terms and units have governed definitions | Day 3 |
| P3-WC-1 | Workflow C — Bounded Supply Planning | 3. Model Domain & Semantics | Model | Analyze | Workflow-C bounded context and ubiquitous language (Supply / Cold-chain domain). | Bounded context & language (Workflow C) | FDE-3 | FDE-4 | 0.5 | P2-WC-2 | Parallel | RUB-04 | DDD bounded contexts + ubiquitous language | Context, ownership and key invariants are defined | Day 2-3 |
| P3-WC-2 | Workflow C — Bounded Supply Planning | 3. Model Domain & Semantics | Model | Analyze | Workflow-C entity/identifier/authority list and data contract (IDMP product fragment, cold-chain logger association, allocation constraints). | Data contract & ontology input (Workflow C) | FDE-3 | FDE-4 | 0.5 | P3-WC-1 | Parallel | RUB-05, RUB-06 | Data contracts as first-class artefacts | Identifiers, terms and units have governed definitions | Day 3 |
| P3-GOV-1 | Product / Value / Governance / Evaluation | 3. Model Domain & Semantics | Model | Analyze | Regulatory and document-authority research feeding the semantic layer (protocol amendments, CCDS, EMA correspondence). | Regulatory document-authority note | FDE-5 | FDE-4 | 0.5 | P1-SYNC-1 | Parallel | RUB-05, RUB-12 | Evidence discipline, cite sources | Document authority is sourced, not assumed | Day 3 |
| P3-GOV-2 | Product / Value / Governance / Evaluation | 3. Model Domain & Semantics | Model | Analyze | Data governance stewardship note: retention, residency, lineage and stewardship policy. | Data governance & stewardship note | FDE-5 | FDE-4 | 0.25 | P3-GOV-1 | Parallel | RUB-05 | Data governance is a named owner, not a gap | Retention and residency are stated | Day 3-4 |
| P3-SYNC-1 | Cross-Lane Sync Gate | 3. Model Domain & Semantics | Model | Analyze | Consolidate the three workflow bounded contexts and the shared kernel into the full DDD Context Map (customer-supplier, conformist, anti-corruption-layer relationships). | DDD context map & ubiquitous language | FDE-4 | All FDEs (Steering) | 0.5 | P3-ARC-1, P3-WA-1, P3-WB-1, P3-WC-1 | SYNC GATE | RUB-04 | Cite backward; mark chain breaks | Bounded contexts, ownership and invariants are agreed enterprise-wide. Persona check: the Chief Quality Officer, the Global Head of Pharmacovigilance and the Supply Chain VP each recognize their own workflow's context map as their world. | Day 3 |
| P3-SYNC-2 | Cross-Lane Sync Gate | 3. Model Domain & Semantics | Model | Analyze | Consolidate the three workflow data contracts/ontology inputs and the authority framework into one Pharma Ontology, Glossary and Semantic Authority Model. | Ontology/glossary & semantic authority model | FDE-4 | All FDEs (Steering) | 0.5 | P3-ARC-2, P3-WA-2, P3-WB-2, P3-WC-2 | SYNC GATE | RUB-05, RUB-06 | Traceability spine: DDD → semantic layer | Critical identities, terms and units have governed, non-conflicting definitions. Persona check: the Regulatory Affairs VP and the Head of Biostatistics accept the identifier and authority definitions as submission-safe and reproducible. | Day 3-4 |
| P3-ARC-3 | Domain, Architecture & Security | 3. Model Domain & Semantics | Model | Analyze | Knowledge-graph decision: benchmark graph reasoning against a simpler alternative using the consolidated semantic layer. | Knowledge-graph decision record | FDE-4 | FDE-5 | 0.5 | P3-SYNC-2 | Parallel | RUB-06 | A KG is justified or rejected with evidence | KG decision is defensible with trade-offs recorded | Day 4 |
| P4-ARC-1 | Domain, Architecture & Security | 4. Architect the Solution | Architect | Improve | C4 system-context view: actors, external systems, accountability boundaries. | C4 system-context view | FDE-4 | FDE-5 | 0.25 | P3-SYNC-1 | Parallel | RUB-04, RUB-07 | Right altitude before containers | System boundary and accountable actors are clear | Day 4 |
| P4-ARC-2 | Domain, Architecture & Security | 4. Architect the Solution | Architect | Improve | Zero-Trust / security architecture: signed tools, least privilege, segregation of duties, high-risk trust boundaries. | Trust-boundary & Zero-Trust view | FDE-4 | FDE-5 | 0.5 | P4-ARC-1 | Parallel | RUB-10 | Zero Trust by default for agentic tools | High-risk boundaries and fail-closed controls are approved | Day 4-5 |
| P4-WA-1 | Workflow A — GxP Evidence Reconciliation | 4. Architect the Solution | Architect | Improve | Workflow-A container/component view and key sequence (batch evidence reconciliation), informed by the Day-3 walking-skeleton findings. | Container/component view (Workflow A) | FDE-1 | FDE-4 | 0.5 | P3-WA-2, SPIKE-WA-1 | Parallel | RUB-04, RUB-07 | C4 turns domain decisions into structure | Components and interfaces are defined | Day 4 |
| P4-WA-2 | Workflow A — GxP Evidence Reconciliation | 4. Architect the Solution | Architect | Improve | Workflow-A data-flow/integration view and trust-boundary control point (fail-closed: no autonomous disposition). | Data-flow & control-point view (Workflow A) | FDE-1 | FDE-4 | 0.5 | P4-WA-1 | Parallel | RUB-05, RUB-10 | Fail-closed on prohibited actions | Data flows and authority checks are traceable | Day 4-5 |
| P4-WB-1 | Workflow B — PV Case Intake | 4. Architect the Solution | Architect | Improve | Workflow-B container/component view and key sequence (intake → triage → duplicate-check → normalize → clock → human review), informed by the Day-3 walking-skeleton findings. | Container/component view (Workflow B) | FDE-2 | FDE-4 | 0.5 | P3-WB-2, SPIKE-WB-1 | Parallel | RUB-04, RUB-07 | C4 turns domain decisions into structure | Components and interfaces are defined | Day 4 |
| P4-WB-2 | Workflow B — PV Case Intake | 4. Architect the Solution | Architect | Improve | Workflow-B data-flow/integration view and trust-boundary control point (fail-closed: no final seriousness/causality/reportability decision). | Data-flow & control-point view (Workflow B) | FDE-2 | FDE-4 | 0.5 | P4-WB-1 | Parallel | RUB-05, RUB-10 | Fail-closed on prohibited actions | Data flows and authority checks are traceable | Day 4-5 |
| P4-WC-1 | Workflow C — Bounded Supply Planning | 4. Architect the Solution | Architect | Improve | Workflow-C container/component view and key sequence (constraint intake → option generation → approval routing), informed by the Day-3 walking-skeleton findings. | Container/component view (Workflow C) | FDE-3 | FDE-4 | 0.5 | P3-WC-2, SPIKE-WC-1 | Parallel | RUB-04, RUB-07 | C4 turns domain decisions into structure | Components and interfaces are defined | Day 4 |
| P4-WC-2 | Workflow C — Bounded Supply Planning | 4. Architect the Solution | Architect | Improve | Workflow-C data-flow/integration view and trust-boundary control point (fail-closed: no inventory/allocation/recall change without explicit human approval). | Data-flow & control-point view (Workflow C) | FDE-3 | FDE-4 | 0.5 | P4-WC-1 | Parallel | RUB-05, RUB-10 | Fail-closed on prohibited actions | Data flows and authority checks are traceable | Day 4-5 |
| P4-GOV-1 | Product / Value / Governance / Evaluation | 4. Architect the Solution | Architect | Improve | Human-oversight, review, override, contestability and emergency-stop design (product/service blueprint). | Human-oversight & blueprint design | FDE-5 | FDE-4 | 0.5 | P2-SYNC-1 | Parallel | RUB-02 | HITL is designed, not assumed | Oversight, override and emergency-stop are designed | Day 4-5 |
| P4-GOV-2 | Product / Value / Governance / Evaluation | 4. Architect the Solution | Architect | Improve | Adoption, training, accessibility, multilingual and change-management plan (draft). | Adoption & change-management plan (draft) | FDE-5 | FDE-4 | 0.5 | P4-GOV-1 | Parallel | RUB-02, RUB-11 | Product mindset, adoption not just delivery | Adoption plan is drafted with accessibility considered | Day 5 |
| P4-SYNC-1 | Cross-Lane Sync Gate | 4. Architect the Solution | Architect | Improve | Integrate the three workflow container/data-flow contributions with the shared C4 skeleton into the full container and component view. | C4 container/component view (full) | FDE-4 | All FDEs (Steering) | 0.5 | P4-ARC-2, P4-WA-2, P4-WB-2, P4-WC-2 | SYNC GATE | RUB-04, RUB-07 | C4 spine complete before specification | Containers and major interfaces are defined enterprise-wide. Persona check: the CISO accepts the trust boundary and the Data Protection Officer accepts the data flows. | Day 5 |
| P5-ARC-1 | Domain, Architecture & Security | 5. Specify & Test | Specify | Improve | Consolidated requirements traceability matrix spine linking Discovery → SCQA → DDD → C4 across all three workflows. | Requirements traceability matrix (spine) | FDE-4 | FDE-5 | 0.5 | P4-SYNC-1 | Parallel | RUB-07 | Traceability rule: every claim cites backward | Requirements trace backward to earlier artefacts | Day 6 |
| P5-ARC-2 | Domain, Architecture & Security | 5. Specify & Test | Specify | Improve | Seed ADR set for architecture-wide decisions: KG decision, integration pattern, trust-boundary model, offline execution mode (4 ADRs). | ADR seed set (4 ADRs) | FDE-4 | FDE-5 | 0.5 | P5-ARC-1 | Parallel | RUB-04, RUB-07 | ADRs beat tribal knowledge | Decisions recorded with alternatives and consequences | Day 6-7 |
| P5-WA-1 | Workflow A — GxP Evidence Reconciliation | 5. Specify & Test | Specify | Improve | Workflow-A functional, NFR, GxP, safety, privacy and security requirements with acceptance criteria. | Requirements (Workflow A) | FDE-1 | FDE-2 | 0.5 | P4-WA-2 | Parallel | RUB-07 | If it is not testable, it is not done | Every requirement has a testable acceptance criterion | Day 6 |
| P5-WA-2 | Workflow A — GxP Evidence Reconciliation | 5. Specify & Test | Specify | Improve | Workflow-A HLD/LLD and versioned API/event contract for the evidence-reconciliation logic. | HLD / LLD & contract (Workflow A) | FDE-1 | FDE-2 | 0.5 | P5-WA-1 | Parallel | RUB-07, RUB-08 | Specs lead, generation follows | Design is build-ready and contracts are versioned | Day 6-7 |
| P5-WA-3 | Workflow A — GxP Evidence Reconciliation | 5. Specify & Test | Specify | Improve | Workflow-A test-first fixtures: happy, edge, failure, attack, outage and recovery paths plus prohibited-disposition negative tests. | Test plan & fixtures (Workflow A) | FDE-1 | FDE-3 | 0.5 | P5-WA-2 | Parallel | RUB-08, RUB-13 | Failing tests for prohibited actions exist before build | Prohibited actions have failing tests before build | Day 7 |
| P5-WB-1 | Workflow B — PV Case Intake | 5. Specify & Test | Specify | Improve | Workflow-B functional, NFR, GxP, safety, privacy and security requirements with acceptance criteria (incl. multilingual review). | Requirements (Workflow B) | FDE-2 | FDE-3 | 0.5 | P4-WB-2 | Parallel | RUB-07 | If it is not testable, it is not done | Every requirement has a testable acceptance criterion | Day 6 |
| P5-WB-2 | Workflow B — PV Case Intake | 5. Specify & Test | Specify | Improve | Workflow-B HLD/LLD and versioned contract for intake/duplicate/normalize/clock logic (E2B mapping). | HLD / LLD & contract (Workflow B) | FDE-2 | FDE-3 | 0.5 | P5-WB-1 | Parallel | RUB-07, RUB-08 | Specs lead, generation follows | Design is build-ready and contracts are versioned | Day 6-7 |
| P5-WB-3 | Workflow B — PV Case Intake | 5. Specify & Test | Specify | Improve | Workflow-B test-first fixtures: happy, edge, failure, attack, outage and recovery paths plus prohibited-decision negative tests. | Test plan & fixtures (Workflow B) | FDE-2 | FDE-1 | 0.5 | P5-WB-2 | Parallel | RUB-08, RUB-13 | Failing tests for prohibited actions exist before build | Prohibited actions have failing tests before build | Day 7 |
| P5-WC-1 | Workflow C — Bounded Supply Planning | 5. Specify & Test | Specify | Improve | Workflow-C functional, NFR, GxP, safety, privacy and security requirements with acceptance criteria (idempotency, approval routing). | Requirements (Workflow C) | FDE-3 | FDE-1 | 0.5 | P4-WC-2 | Parallel | RUB-07 | If it is not testable, it is not done | Every requirement has a testable acceptance criterion | Day 6 |
| P5-WC-2 | Workflow C — Bounded Supply Planning | 5. Specify & Test | Specify | Improve | Workflow-C HLD/LLD and versioned contract for option-generation logic and constraint schema. | HLD / LLD & contract (Workflow C) | FDE-3 | FDE-1 | 0.5 | P5-WC-1 | Parallel | RUB-07, RUB-08 | Specs lead, generation follows | Design is build-ready and contracts are versioned | Day 6-7 |
| P5-WC-3 | Workflow C — Bounded Supply Planning | 5. Specify & Test | Specify | Improve | Workflow-C test-first fixtures: happy, edge, failure, attack, outage and recovery paths plus prohibited-allocation negative tests. | Test plan & fixtures (Workflow C) | FDE-3 | FDE-2 | 0.5 | P5-WC-2 | Parallel | RUB-08, RUB-13 | Failing tests for prohibited actions exist before build | Prohibited actions have failing tests before build | Day 7 |
| P5-GOV-1 | Product / Value / Governance / Evaluation | 5. Specify & Test | Specify | Improve | Delivery/build backlog assembly mapping backlog items to rubric IDs and evidence outputs. | Build backlog & evidence plan | FDE-5 | FDE-4 | 0.5 | P2-SYNC-1 | Parallel | RUB-07 | Gates are product, not polish | Build scope is sequenced and independently testable | Day 7 |
| P5-GOV-2 | Product / Value / Governance / Evaluation | 5. Specify & Test | Specify | Improve | Evaluation / TEVV plan skeleton (datasets, graders, thresholds, subgroup dimensions) drafted before build starts. | TEVV plan skeleton | FDE-5 | FDE-4 | 0.5 | P5-GOV-1 | Parallel | RUB-13 | Eval targets exist before code, not after | Thresholds and subgroup dimensions are defined pre-build | Day 7 |
| P5-SYNC-1 | Cross-Lane Sync Gate | 5. Specify & Test | Specify | Improve | Spec-quality cross-review of all three workflow specs before large-scale build, using the spec-quality checklist (cross-pod reviewers). | Spec-quality review sign-off | FDE-5 | All FDEs (Steering) | 0.5 | P5-WA-3, P5-WB-3, P5-WC-3 | SYNC GATE | RUB-05, RUB-07, RUB-08, RUB-13 | Review the spec before reviewing the code | Reviewers approve, or change requests are listed with owners. Persona check: the Head of Biostatistics accepts the acceptance criteria as reproducible and the Patient Safety Representative confirms the interface is contestable and accessible. | Day 7 |
| P6-ARC-1 | Domain, Architecture & Security | 6. Decide & Govern | Decide | Improve / Control | Finalize the ADR register: consolidate the three workflow-specific ADRs with the architecture-wide ADRs (target 10+ total). | Approved ADR register (10+ ADRs) | FDE-4 | FDE-5 | 0.5 | P5-ARC-2, P6-WA-2, P6-WB-2, P6-WC-2 | Parallel (late) | RUB-04, RUB-07 | ADRs beat tribal knowledge | Material design choices are recorded and approved | Day 8 |
| P6-ARC-2 | Domain, Architecture & Security | 6. Decide & Govern | Decide | Improve / Control | Threat and abuse model across all three workflows: injection, poisoning, exfiltration, tool abuse, excessive agency, replay, supply chain, denial-of-wallet. | Threat / abuse model | FDE-4 | FDE-5 | 0.5 | P4-SYNC-1 | Parallel | RUB-10 (hard gate) | Zero Trust; gates block unsafe progression | Critical risks have controls, tests, owners | Day 8 |
| P6-WA-1 | Workflow A — GxP Evidence Reconciliation | 6. Decide & Govern | Decide | Improve / Control | Workflow-A GxP lifecycle / computerised-system-assurance validation strategy and quality-risk assessment, proportionate to risk. | Validation strategy & QRM (Workflow A) | FDE-1 | FDE-5 | 0.5 | P5-WA-3 | Parallel | RUB-09 (hard gate) | Validation proportionate to risk, not blanket | Risk-proportionate validation approach is defined | Day 8 |
| P6-WA-2 | Workflow A — GxP Evidence Reconciliation | 6. Decide & Govern | Decide | Improve / Control | Workflow-A ADR(s): OOS/OOT reconciliation logic and evidence-abstention design. | ADR(s) (Workflow A) | FDE-1 | FDE-4 | 0.25 | P6-WA-1 | Parallel | RUB-04 | ADRs beat tribal knowledge | Decision recorded with alternatives and consequences | Day 8 |
| P6-WB-1 | Workflow B — PV Case Intake | 6. Decide & Govern | Decide | Improve / Control | Workflow-B privacy/ethics and cross-border data-protection assessment (D09) plus data-integrity note. | Privacy/ethics assessment & DI note (Workflow B) | FDE-2 | FDE-5 | 0.5 | P5-WB-3 | Parallel | RUB-09, RUB-11 (hard gate) | Privacy-by-design, not bolted on | Privacy risks and controls are documented | Day 8 |
| P6-WB-2 | Workflow B — PV Case Intake | 6. Decide & Govern | Decide | Improve / Control | Workflow-B ADR(s): duplicate-detection and source-authority resolution logic. | ADR(s) (Workflow B) | FDE-2 | FDE-4 | 0.25 | P6-WB-1 | Parallel | RUB-04 | ADRs beat tribal knowledge | Decision recorded with alternatives and consequences | Day 8 |
| P6-WC-1 | Workflow C — Bounded Supply Planning | 6. Decide & Govern | Decide | Improve / Control | Workflow-C reliability/continuity input (cold-chain and CMO outage behaviour) plus quality-risk note. | Reliability input & QRM (Workflow C) | FDE-3 | FDE-5 | 0.5 | P5-WC-3 | Parallel | RUB-09, RUB-15 (hard gate) | Safe manual operation during outage | Outage and recovery behaviour is defined | Day 8 |
| P6-WC-2 | Workflow C — Bounded Supply Planning | 6. Decide & Govern | Decide | Improve / Control | Workflow-C ADR(s): allocation-option ranking and approval-gate logic. | ADR(s) (Workflow C) | FDE-3 | FDE-4 | 0.25 | P6-WC-1 | Parallel | RUB-04 | ADRs beat tribal knowledge | Decision recorded with alternatives and consequences | Day 8 |
| P6-GOV-1 | Product / Value / Governance / Evaluation | 6. Decide & Govern | Decide | Improve / Control | Regulatory and governance applicability across the three workflows (EU AI Act, ISO/IEC 42001). | Regulatory & governance applicability note | FDE-5 | FDE-4 | 0.5 | P3-GOV-2 | Parallel | RUB-12 | State jurisdiction, purpose, role and boundary | Jurisdiction, purpose, accountable role and boundary are stated | Day 8 |
| P6-GOV-2 | Product / Value / Governance / Evaluation | 6. Decide & Govern | Decide | Improve / Control | Responsible-AI / human-factors and privacy-ethics consolidation, merging Workflow-B's privacy input with enterprise RAI. | RAI & privacy-ethics consolidation | FDE-5 | FDE-4 | 0.5 | P6-WB-1, P6-GOV-1 | Parallel (late) | RUB-11 (hard gate) | Material subgroup/privacy risks are not omitted | No material subgroup or privacy risk is omitted | Day 8 |
| P6-SYNC-1 | Cross-Lane Sync Gate | 6. Decide & Govern | Decide | Improve / Control | Stage-gate release decision: go / conditional-go / pivot / pause / stop for the POC build. | Stage-gate decision record | FDE-5 | All FDEs (Steering) | 0.5 | P6-ARC-1, P6-ARC-2, P6-WA-2, P6-WB-2, P6-WC-2, P6-GOV-2 | SYNC GATE | RUB-09, RUB-10, RUB-11 (hard gates) | Waivers are explicit, owned and time-boxed | D9 gate — recorded decision authorizes the next phase. Persona check: the Chief Medical Officer, the Chief Quality Officer and the Works Council / Employee Forum each accept the risk posture and oversight design. | Day 8 |
| P7-WA-1 | Workflow A — GxP Evidence Reconciliation | 7. Deliver & Evaluate | Deliver & Evaluate | Control | Build the Workflow-A engine: cited facts, authority, conflicts, gaps, abstention and human-review output; no disposition or execution. | Working Workflow-A module (offline) | FDE-1 | FDE-4 | 1 | P6-SYNC-1 | Parallel | RUB-08 | Production-ise AI output, don't paste it unchecked | Runs without any prohibited side effect | Day 9 |
| P7-WA-2 | Workflow A — GxP Evidence Reconciliation | 7. Deliver & Evaluate | Deliver & Evaluate | Control | Workflow-A verification: contract, unit, security, privacy, subgroup, outage, replay and recovery tests. | Machine-readable test results (Workflow A) | FDE-1 | FDE-3 | 0.75 | P7-WA-1 | Parallel | RUB-08, RUB-13 (hard gate) | Gates are blocking on the critical path | Critical tests pass; a failed gate blocks release | Day 9-10 |
| P7-WA-3 | Workflow A — GxP Evidence Reconciliation | 7. Deliver & Evaluate | Deliver & Evaluate | Control | Workflow-A evaluation against the relevant public fixtures plus a residual-risk note. | Evaluation results (Workflow A) | FDE-1 | FDE-5 | 0.5 | P7-WA-2 | Parallel | RUB-13 | Evidence fidelity over vibes | Thresholds and evidence fidelity meet release criteria | Day 10 |
| P7-WB-1 | Workflow B — PV Case Intake | 7. Deliver & Evaluate | Deliver & Evaluate | Control | Build the Workflow-B engine: intake, duplicate, normalize, clock and listedness logic with abstention and human-review hooks; no final PV decision. | Working Workflow-B module (offline) | FDE-2 | FDE-4 | 1 | P6-SYNC-1 | Parallel | RUB-08 | Production-ise AI output, don't paste it unchecked | Runs without any prohibited side effect | Day 9 |
| P7-WB-2 | Workflow B — PV Case Intake | 7. Deliver & Evaluate | Deliver & Evaluate | Control | Workflow-B verification: contract, unit, security, privacy, subgroup (incl. multilingual), outage, replay and recovery tests. | Machine-readable test results (Workflow B) | FDE-2 | FDE-1 | 0.75 | P7-WB-1 | Parallel | RUB-08, RUB-13 (hard gate) | Gates are blocking on the critical path | Critical tests pass; a failed gate blocks release | Day 9-10 |
| P7-WB-3 | Workflow B — PV Case Intake | 7. Deliver & Evaluate | Deliver & Evaluate | Control | Workflow-B evaluation against the relevant public fixtures plus a residual-risk note. | Evaluation results (Workflow B) | FDE-2 | FDE-5 | 0.5 | P7-WB-2 | Parallel | RUB-13 | Evidence fidelity over vibes | Thresholds and evidence fidelity meet release criteria | Day 10 |
| P7-WC-1 | Workflow C — Bounded Supply Planning | 7. Deliver & Evaluate | Deliver & Evaluate | Control | Build the Workflow-C engine: bounded option generation with approvals and idempotency; no side effects. | Working Workflow-C module (offline) | FDE-3 | FDE-4 | 1 | P6-SYNC-1 | Parallel | RUB-08 | Production-ise AI output, don't paste it unchecked | Runs without any prohibited side effect | Day 9 |
| P7-WC-2 | Workflow C — Bounded Supply Planning | 7. Deliver & Evaluate | Deliver & Evaluate | Control | Workflow-C verification: contract, unit, security, privacy, subgroup, outage, replay and recovery tests. | Machine-readable test results (Workflow C) | FDE-3 | FDE-2 | 0.75 | P7-WC-1 | Parallel | RUB-08, RUB-13 (hard gate) | Gates are blocking on the critical path | Critical tests pass; a failed gate blocks release | Day 9-10 |
| P7-WC-3 | Workflow C — Bounded Supply Planning | 7. Deliver & Evaluate | Deliver & Evaluate | Control | Workflow-C evaluation against the relevant public fixtures plus a residual-risk note. | Evaluation results (Workflow C) | FDE-3 | FDE-5 | 0.5 | P7-WC-2 | Parallel | RUB-13 | Evidence fidelity over vibes | Thresholds and evidence fidelity meet release criteria | Day 10 |
| P7-ARC-1 | Domain, Architecture & Security | 7. Deliver & Evaluate | Deliver & Evaluate | Control | Integrate the three workflow modules behind shared app/audit/evaluation containers; wire kill switch, AI-disabled continuity and checkpointing. | Integrated app shell with kill switch & continuity | FDE-4 | FDE-5 | 0.75 | P7-WA-1, P7-WB-1, P7-WC-1 | Parallel (late) | RUB-08, RUB-15 | Safe manual operation during model outage | Safe manual operation during outage is demonstrated | Day 9-10 |
| P7-ARC-2 | Domain, Architecture & Security | 7. Deliver & Evaluate | Deliver & Evaluate | Control | Security / red-team pass across the integrated system plus remediation verification. | Red-team evidence & remediation log | FDE-4 | FDE-5 | 0.5 | P7-ARC-1 | Parallel | RUB-10 (hard gate) | Residual risk is accepted with evidence, not assumed | Residual risk is accepted with evidence | Day 10 |
| P7-ARC-3 | Domain, Architecture & Security | 7. Deliver & Evaluate | Deliver & Evaluate | Control | Token-efficiency / FinOps instrumentation: context budgets, caching, avoided inference, cost-measurement hooks. | FinOps instrumentation & cost evidence | FDE-4 | FDE-5 | 0.25 | P7-ARC-1 | Parallel | RUB-14 | Token economics is evidence, not a claim | Cost and token evidence is captured | Day 10 |
| P7-GOV-1 | Product / Value / Governance / Evaluation | 7. Deliver & Evaluate | Deliver & Evaluate | Control | Consolidated evaluation scorecard across the three workflows including subgroup and regression gates. | Evaluation scorecard | FDE-5 | FDE-4 | 0.5 | P7-WA-3, P7-WB-3, P7-WC-3 | Parallel (late) | RUB-13 (hard gate) | Subgroup evidence is mandatory | Subgroup results meet the release criteria | Day 10 |
| P7-GOV-2 | Product / Value / Governance / Evaluation | 7. Deliver & Evaluate | Deliver & Evaluate | Control | Reliability/observability plus incident/recovery and vendor-exit/retirement runbooks. | Reliability & continuity runbooks | FDE-5 | FDE-4 | 0.5 | P7-ARC-1 | Parallel | RUB-15 (hard gate) | Backup, restore, DR and exit are documented | Backup/restore/DR/exit are documented | Day 10 |
| P7-GOV-3 | Product / Value / Governance / Evaluation | 7. Deliver & Evaluate | Deliver & Evaluate | Control | Target operating model, production-readiness gaps, 90-day roadmap and handover pack. | Operating model, roadmap & handover pack | FDE-5 | FDE-4 | 0.5 | P7-GOV-1, P7-GOV-2 | Parallel (late) | RUB-16 | Handover is a deliverable, not an afterthought | Handover and roadmap are complete | Day 10 |
| P7-SYNC-1 | Cross-Lane Sync Gate | 7. Deliver & Evaluate | Deliver & Evaluate | Control | Clean-room handover rehearsal and submission-evidence check (python run_capstone.py --check). | Submission check pass & clean-room proof | FDE-4 | All FDEs (Steering) | 0.25 | P7-GOV-3, P7-ARC-2, P7-ARC-3 | SYNC GATE | RUB-16 | Reproduce build, tests and evaluation from the package | Submission check passes. Persona check: the CISO and the EU Qualified Person accept the evidence trail at inspection standard. | Day 10 |
| P7-SYNC-2 | Cross-Lane Sync Gate | 7. Deliver & Evaluate | Deliver & Evaluate | Control | Assemble the final executive and technical defence (elevator pitch plus live failure demonstrations); every FDE presents their own lane's evidence. | Final defence pack & recommendation | FDE-5 | All FDEs (Steering) | 0.5 | P7-SYNC-1 | SYNC GATE | RUB-17 | Defend what you can trace, not what you claim | Release / conditional / pivot / pause / stop recommendation is defensible. Persona check: the full steering group (CMO, CQO, Supply Chain VP, Global Head of PV) accepts the board recommendation. | Day 10 |
| SPIKE-WA-1 | Workflow A — GxP Evidence Reconciliation | 3. Model Domain & Semantics | Model | Analyze | Walking-skeleton spike (throwaway, no polish): read one real batch-evidence packet from source_documents, produce one cited-fact output with authority and gaps, and hit the 'no autonomous disposition' guardrail once, end-to-end, on real data. | Walking-skeleton spike (Workflow A) + findings note | FDE-1 | FDE-4 | 0.75 | P2-SYNC-1 | Parallel (spike) | RUB-01, RUB-08 | Ship on Day one — field as ground truth beats a requirements document | Skeleton runs once end-to-end on real data; findings are logged and feed Architect + Specify | Day 3 |
| SPIKE-WB-1 | Workflow B — PV Case Intake | 3. Model Domain & Semantics | Model | Analyze | Walking-skeleton spike (throwaway, no polish): read one real PV case narrative, run one duplicate-check pass and one clock-reconstruction pass, and hit the 'no final PV decision' guardrail once, end-to-end, on real data. | Walking-skeleton spike (Workflow B) + findings note | FDE-2 | FDE-4 | 0.75 | P2-SYNC-1 | Parallel (spike) | RUB-01, RUB-08 | Ship on Day one — field as ground truth beats a requirements document | Skeleton runs once end-to-end on real data; findings are logged and feed Architect + Specify | Day 3 |
| SPIKE-WC-1 | Workflow C — Bounded Supply Planning | 3. Model Domain & Semantics | Model | Analyze | Walking-skeleton spike (throwaway, no polish): read one real shortage/cold-chain constraint set, generate one draft option, and hit the 'no autonomous allocation' guardrail once, end-to-end, on real data. | Walking-skeleton spike (Workflow C) + findings note | FDE-3 | FDE-4 | 0.75 | P2-SYNC-1 | Parallel (spike) | RUB-01, RUB-08 | Ship on Day one — field as ground truth beats a requirements document | Skeleton runs once end-to-end on real data; findings are logged and feed Architect + Specify | Day 3 |
| OD-1 | Domain, Architecture & Security | 4. Architect the Solution | Architect | Improve | Ontology delta review: reconcile any contradictions the three Day-3 spikes surfaced against the Phase-3 ontology/semantic layer; version and amend rather than silently overwrite. | Ontology delta log v2 | FDE-4 | FDE-5 | 0.25 | P4-SYNC-1, SPIKE-WA-1, SPIKE-WB-1, SPIKE-WC-1 | Parallel | RUB-05, RUB-06 | Ontology is a living artefact, not a one-time freeze | Contradictions from the spikes are resolved and versioned, not silently dropped | Day 5 |
| OD-2 | Domain, Architecture & Security | 5. Specify & Test | Specify | Improve | Ontology delta review: reconcile any contradictions surfaced by HLD/LLD and test-fixture design against the ontology/semantic layer; version and amend rather than silently overwrite. | Ontology delta log v3 | FDE-4 | FDE-5 | 0.25 | P5-SYNC-1 | Parallel | RUB-05, RUB-06 | Ontology is a living artefact, not a one-time freeze | Contradictions from specification are resolved and versioned, not silently dropped | Day 7 |
| OD-3 | Domain, Architecture & Security | 7. Deliver & Evaluate | Deliver & Evaluate | Control | Ontology delta review: reconcile any contradictions surfaced by the working build against the ontology/semantic layer; freeze the final submission version. | Ontology delta log v4 (final, submission version) | FDE-4 | FDE-5 | 0.25 | P7-WA-1, P7-WB-1, P7-WC-1 | Parallel | RUB-05, RUB-06 | Ontology is a living artefact, not a one-time freeze | Final version reconciles all build-time contradictions and is traceable | Day 10 |
| GEMBA-1 | Domain, Architecture & Security | 7. Deliver & Evaluate | Deliver & Evaluate | Control | Gemba session: FDE-4 sits with FDE-2 and hands-on drives part of the Workflow-B build for one session, instead of reviewing it on paper only — direct exposure to real broken data and edge cases. | Gemba session notes (Workflow B, driven by FDE-4) | FDE-4 | FDE-2 | 0.25 | P7-WB-1 | Parallel | RUB-08, RUB-10 | Startup-CTO mindset: own the whole stack, not just your slice | Architecture lead has hands-on exposure to at least one workflow's real build | Day 9 |
| GEMBA-2 | Product / Value / Governance / Evaluation | 7. Deliver & Evaluate | Deliver & Evaluate | Control | Gemba session: FDE-5 sits with FDE-3 and hands-on drives part of the Workflow-C build for one session, instead of reviewing it on paper only — direct exposure to real broken data and edge cases. | Gemba session notes (Workflow C, driven by FDE-5) | FDE-5 | FDE-3 | 0.25 | P7-WC-1 | Parallel | RUB-08, RUB-13 | Startup-CTO mindset: own the whole stack, not just your slice | Governance/evaluation lead has hands-on exposure to at least one workflow's real build | Day 9 |
## Sheet: FDE Sequences
| FDE Sequences — Independent Day-by-Day Track per Engineer |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Each block below is self-contained: an FDE can execute their block start-to-finish without reading anyone else's block, except for the shaded SYNC rows, which need a brief joint checkpoint (20-30 min) with the other four. |  |  |  |  |  |  |  |
| FDE-1 — Workflow A — GxP Evidence Reconciliation |  |  |  |  |  |  |  |
| Day | WBS ID | Role | Activity / Deliverable | Build effort
(person-days) | Counterpart | Rubric ID(s) |  |
| Day 1 | P1-WA-1 | BUILD (owner) | Case reading log (Workflow A) | 0.5 | reviewed by FDE-2 | RUB-01 |  |
| Day 1 | P1-WC-1 | REVIEW | Case reading log (Workflow C) | — | owned by FDE-3 | RUB-01 |  |
| Day 1-2 | P1-WA-2 | BUILD (owner) | Current-state map & baseline (batch review) | 0.5 | reviewed by FDE-2 | RUB-01, RUB-02, RUB-03 |  |
| Day 1-2 | P1-WC-2 | REVIEW | Current-state map & baseline (supply/cold-chain) | — | owned by FDE-3 | RUB-01, RUB-02, RUB-03 |  |
| Day 2 | P1-SYNC-1 | ATTEND (sync) | Unified context/assumptions log (feeds 01_BUSINESS_CASE) | — | all 5 FDEs | RUB-01, RUB-02 |  |
| Day 2 | P2-GOV-2 | REVIEW | Value hypothesis, KPI tree & no-AI comparison | — | owned by FDE-5 | RUB-01, RUB-03 |  |
| Day 2 | P2-SYNC-1 | ATTEND (sync) | Prioritized scope, safety boundary & release backlog | — | all 5 FDEs | RUB-01, RUB-02, RUB-03 |  |
| Day 2 | P2-WA-1 | BUILD (owner) | Problem statement (Workflow A) | 0.5 | reviewed by FDE-2 | RUB-01, RUB-02 |  |
| Day 2 | P2-WA-2 | BUILD (owner) | Value hypothesis (Workflow A) | 0.5 | reviewed by FDE-2 | RUB-03 |  |
| Day 2 | P2-WC-1 | REVIEW | Problem statement (Workflow C) | — | owned by FDE-3 | RUB-01, RUB-02 |  |
| Day 2 | P2-WC-2 | REVIEW | Value hypothesis (Workflow C) | — | owned by FDE-3 | RUB-03 |  |
| Day 2-3 | P3-WA-1 | BUILD (owner) | Bounded context & language (Workflow A) | 0.5 | reviewed by FDE-4 | RUB-04 |  |
| Day 3 | P3-SYNC-1 | ATTEND (sync) | DDD context map & ubiquitous language | — | all 5 FDEs | RUB-04 |  |
| Day 3 | P3-WA-2 | BUILD (owner) | Data contract & ontology input (Workflow A) | 0.5 | reviewed by FDE-4 | RUB-05, RUB-06 |  |
| Day 3 | SPIKE-WA-1 | BUILD (owner) | Walking-skeleton spike (Workflow A) + findings note | 0.75 | reviewed by FDE-4 | RUB-01, RUB-08 |  |
| Day 3-4 | P3-SYNC-2 | ATTEND (sync) | Ontology/glossary & semantic authority model | — | all 5 FDEs | RUB-05, RUB-06 |  |
| Day 4 | P4-WA-1 | BUILD (owner) | Container/component view (Workflow A) | 0.5 | reviewed by FDE-4 | RUB-04, RUB-07 |  |
| Day 4-5 | P4-WA-2 | BUILD (owner) | Data-flow & control-point view (Workflow A) | 0.5 | reviewed by FDE-4 | RUB-05, RUB-10 |  |
| Day 5 | P4-SYNC-1 | ATTEND (sync) | C4 container/component view (full) | — | all 5 FDEs | RUB-04, RUB-07 |  |
| Day 6 | P5-WA-1 | BUILD (owner) | Requirements (Workflow A) | 0.5 | reviewed by FDE-2 | RUB-07 |  |
| Day 6 | P5-WC-1 | REVIEW | Requirements (Workflow C) | — | owned by FDE-3 | RUB-07 |  |
| Day 6-7 | P5-WA-2 | BUILD (owner) | HLD / LLD & contract (Workflow A) | 0.5 | reviewed by FDE-2 | RUB-07, RUB-08 |  |
| Day 6-7 | P5-WC-2 | REVIEW | HLD / LLD & contract (Workflow C) | — | owned by FDE-3 | RUB-07, RUB-08 |  |
| Day 7 | P5-SYNC-1 | ATTEND (sync) | Spec-quality review sign-off | — | all 5 FDEs | RUB-05, RUB-07, RUB-08, RUB-13 |  |
| Day 7 | P5-WA-3 | BUILD (owner) | Test plan & fixtures (Workflow A) | 0.5 | reviewed by FDE-3 | RUB-08, RUB-13 |  |
| Day 7 | P5-WB-3 | REVIEW | Test plan & fixtures (Workflow B) | — | owned by FDE-2 | RUB-08, RUB-13 |  |
| Day 8 | P6-SYNC-1 | ATTEND (sync) | Stage-gate decision record | — | all 5 FDEs | RUB-09, RUB-10, RUB-11 (hard gates) |  |
| Day 8 | P6-WA-1 | BUILD (owner) | Validation strategy & QRM (Workflow A) | 0.5 | reviewed by FDE-5 | RUB-09 (hard gate) |  |
| Day 8 | P6-WA-2 | BUILD (owner) | ADR(s) (Workflow A) | 0.25 | reviewed by FDE-4 | RUB-04 |  |
| Day 9 | P7-WA-1 | BUILD (owner) | Working Workflow-A module (offline) | 1 | reviewed by FDE-4 | RUB-08 |  |
| Day 9-10 | P7-WA-2 | BUILD (owner) | Machine-readable test results (Workflow A) | 0.75 | reviewed by FDE-3 | RUB-08, RUB-13 (hard gate) |  |
| Day 9-10 | P7-WB-2 | REVIEW | Machine-readable test results (Workflow B) | — | owned by FDE-2 | RUB-08, RUB-13 (hard gate) |  |
| Day 10 | P7-SYNC-1 | ATTEND (sync) | Submission check pass & clean-room proof | — | all 5 FDEs | RUB-16 |  |
| Day 10 | P7-SYNC-2 | ATTEND (sync) | Final defence pack & recommendation | — | all 5 FDEs | RUB-17 |  |
| Day 10 | P7-WA-3 | BUILD (owner) | Evaluation results (Workflow A) | 0.5 | reviewed by FDE-5 | RUB-13 |  |
|  |  |  | Total build effort for FDE-1: | 9.25 |  |  |  |
| FDE-2 — Workflow B — PV Case Intake |  |  |  |  |  |  |  |
| Day | WBS ID | Role | Activity / Deliverable | Build effort
(person-days) | Counterpart | Rubric ID(s) |  |
| Day 1 | P1-WA-1 | REVIEW | Case reading log (Workflow A) | — | owned by FDE-1 | RUB-01 |  |
| Day 1 | P1-WB-1 | BUILD (owner) | Case reading log (Workflow B) | 0.5 | reviewed by FDE-3 | RUB-01 |  |
| Day 1-2 | P1-WA-2 | REVIEW | Current-state map & baseline (batch review) | — | owned by FDE-1 | RUB-01, RUB-02, RUB-03 |  |
| Day 1-2 | P1-WB-2 | BUILD (owner) | Current-state map & baseline (PV intake) | 0.5 | reviewed by FDE-3 | RUB-01, RUB-02, RUB-03 |  |
| Day 2 | P1-SYNC-1 | ATTEND (sync) | Unified context/assumptions log (feeds 01_BUSINESS_CASE) | — | all 5 FDEs | RUB-01, RUB-02 |  |
| Day 2 | P2-SYNC-1 | ATTEND (sync) | Prioritized scope, safety boundary & release backlog | — | all 5 FDEs | RUB-01, RUB-02, RUB-03 |  |
| Day 2 | P2-WA-1 | REVIEW | Problem statement (Workflow A) | — | owned by FDE-1 | RUB-01, RUB-02 |  |
| Day 2 | P2-WA-2 | REVIEW | Value hypothesis (Workflow A) | — | owned by FDE-1 | RUB-03 |  |
| Day 2 | P2-WB-1 | BUILD (owner) | Problem statement (Workflow B) | 0.5 | reviewed by FDE-3 | RUB-01, RUB-02 |  |
| Day 2 | P2-WB-2 | BUILD (owner) | Value hypothesis (Workflow B) | 0.5 | reviewed by FDE-3 | RUB-03 |  |
| Day 2-3 | P3-WB-1 | BUILD (owner) | Bounded context & language (Workflow B) | 0.5 | reviewed by FDE-4 | RUB-04 |  |
| Day 3 | P3-SYNC-1 | ATTEND (sync) | DDD context map & ubiquitous language | — | all 5 FDEs | RUB-04 |  |
| Day 3 | P3-WB-2 | BUILD (owner) | Data contract & ontology input (Workflow B) | 0.5 | reviewed by FDE-4 | RUB-05, RUB-06 |  |
| Day 3 | SPIKE-WB-1 | BUILD (owner) | Walking-skeleton spike (Workflow B) + findings note | 0.75 | reviewed by FDE-4 | RUB-01, RUB-08 |  |
| Day 3-4 | P3-SYNC-2 | ATTEND (sync) | Ontology/glossary & semantic authority model | — | all 5 FDEs | RUB-05, RUB-06 |  |
| Day 4 | P4-WB-1 | BUILD (owner) | Container/component view (Workflow B) | 0.5 | reviewed by FDE-4 | RUB-04, RUB-07 |  |
| Day 4-5 | P4-WB-2 | BUILD (owner) | Data-flow & control-point view (Workflow B) | 0.5 | reviewed by FDE-4 | RUB-05, RUB-10 |  |
| Day 5 | P4-SYNC-1 | ATTEND (sync) | C4 container/component view (full) | — | all 5 FDEs | RUB-04, RUB-07 |  |
| Day 6 | P5-WA-1 | REVIEW | Requirements (Workflow A) | — | owned by FDE-1 | RUB-07 |  |
| Day 6 | P5-WB-1 | BUILD (owner) | Requirements (Workflow B) | 0.5 | reviewed by FDE-3 | RUB-07 |  |
| Day 6-7 | P5-WA-2 | REVIEW | HLD / LLD & contract (Workflow A) | — | owned by FDE-1 | RUB-07, RUB-08 |  |
| Day 6-7 | P5-WB-2 | BUILD (owner) | HLD / LLD & contract (Workflow B) | 0.5 | reviewed by FDE-3 | RUB-07, RUB-08 |  |
| Day 7 | P5-SYNC-1 | ATTEND (sync) | Spec-quality review sign-off | — | all 5 FDEs | RUB-05, RUB-07, RUB-08, RUB-13 |  |
| Day 7 | P5-WB-3 | BUILD (owner) | Test plan & fixtures (Workflow B) | 0.5 | reviewed by FDE-1 | RUB-08, RUB-13 |  |
| Day 7 | P5-WC-3 | REVIEW | Test plan & fixtures (Workflow C) | — | owned by FDE-3 | RUB-08, RUB-13 |  |
| Day 8 | P6-SYNC-1 | ATTEND (sync) | Stage-gate decision record | — | all 5 FDEs | RUB-09, RUB-10, RUB-11 (hard gates) |  |
| Day 8 | P6-WB-1 | BUILD (owner) | Privacy/ethics assessment & DI note (Workflow B) | 0.5 | reviewed by FDE-5 | RUB-09, RUB-11 (hard gate) |  |
| Day 8 | P6-WB-2 | BUILD (owner) | ADR(s) (Workflow B) | 0.25 | reviewed by FDE-4 | RUB-04 |  |
| Day 9 | GEMBA-1 | REVIEW | Gemba session notes (Workflow B, driven by FDE-4) | — | owned by FDE-4 | RUB-08, RUB-10 |  |
| Day 9 | P7-WB-1 | BUILD (owner) | Working Workflow-B module (offline) | 1 | reviewed by FDE-4 | RUB-08 |  |
| Day 9-10 | P7-WB-2 | BUILD (owner) | Machine-readable test results (Workflow B) | 0.75 | reviewed by FDE-1 | RUB-08, RUB-13 (hard gate) |  |
| Day 9-10 | P7-WC-2 | REVIEW | Machine-readable test results (Workflow C) | — | owned by FDE-3 | RUB-08, RUB-13 (hard gate) |  |
| Day 10 | P7-SYNC-1 | ATTEND (sync) | Submission check pass & clean-room proof | — | all 5 FDEs | RUB-16 |  |
| Day 10 | P7-SYNC-2 | ATTEND (sync) | Final defence pack & recommendation | — | all 5 FDEs | RUB-17 |  |
| Day 10 | P7-WB-3 | BUILD (owner) | Evaluation results (Workflow B) | 0.5 | reviewed by FDE-5 | RUB-13 |  |
|  |  |  | Total build effort for FDE-2: | 9.25 |  |  |  |
| FDE-3 — Workflow C — Bounded Supply Planning |  |  |  |  |  |  |  |
| Day | WBS ID | Role | Activity / Deliverable | Build effort
(person-days) | Counterpart | Rubric ID(s) |  |
| Day 1 | P1-WB-1 | REVIEW | Case reading log (Workflow B) | — | owned by FDE-2 | RUB-01 |  |
| Day 1 | P1-WC-1 | BUILD (owner) | Case reading log (Workflow C) | 0.5 | reviewed by FDE-1 | RUB-01 |  |
| Day 1-2 | P1-WB-2 | REVIEW | Current-state map & baseline (PV intake) | — | owned by FDE-2 | RUB-01, RUB-02, RUB-03 |  |
| Day 1-2 | P1-WC-2 | BUILD (owner) | Current-state map & baseline (supply/cold-chain) | 0.5 | reviewed by FDE-1 | RUB-01, RUB-02, RUB-03 |  |
| Day 2 | P1-SYNC-1 | ATTEND (sync) | Unified context/assumptions log (feeds 01_BUSINESS_CASE) | — | all 5 FDEs | RUB-01, RUB-02 |  |
| Day 2 | P2-SYNC-1 | ATTEND (sync) | Prioritized scope, safety boundary & release backlog | — | all 5 FDEs | RUB-01, RUB-02, RUB-03 |  |
| Day 2 | P2-WB-1 | REVIEW | Problem statement (Workflow B) | — | owned by FDE-2 | RUB-01, RUB-02 |  |
| Day 2 | P2-WB-2 | REVIEW | Value hypothesis (Workflow B) | — | owned by FDE-2 | RUB-03 |  |
| Day 2 | P2-WC-1 | BUILD (owner) | Problem statement (Workflow C) | 0.5 | reviewed by FDE-1 | RUB-01, RUB-02 |  |
| Day 2 | P2-WC-2 | BUILD (owner) | Value hypothesis (Workflow C) | 0.5 | reviewed by FDE-1 | RUB-03 |  |
| Day 2-3 | P3-WC-1 | BUILD (owner) | Bounded context & language (Workflow C) | 0.5 | reviewed by FDE-4 | RUB-04 |  |
| Day 3 | P3-SYNC-1 | ATTEND (sync) | DDD context map & ubiquitous language | — | all 5 FDEs | RUB-04 |  |
| Day 3 | P3-WC-2 | BUILD (owner) | Data contract & ontology input (Workflow C) | 0.5 | reviewed by FDE-4 | RUB-05, RUB-06 |  |
| Day 3 | SPIKE-WC-1 | BUILD (owner) | Walking-skeleton spike (Workflow C) + findings note | 0.75 | reviewed by FDE-4 | RUB-01, RUB-08 |  |
| Day 3-4 | P3-SYNC-2 | ATTEND (sync) | Ontology/glossary & semantic authority model | — | all 5 FDEs | RUB-05, RUB-06 |  |
| Day 4 | P4-WC-1 | BUILD (owner) | Container/component view (Workflow C) | 0.5 | reviewed by FDE-4 | RUB-04, RUB-07 |  |
| Day 4-5 | P4-WC-2 | BUILD (owner) | Data-flow & control-point view (Workflow C) | 0.5 | reviewed by FDE-4 | RUB-05, RUB-10 |  |
| Day 5 | P4-SYNC-1 | ATTEND (sync) | C4 container/component view (full) | — | all 5 FDEs | RUB-04, RUB-07 |  |
| Day 6 | P5-WB-1 | REVIEW | Requirements (Workflow B) | — | owned by FDE-2 | RUB-07 |  |
| Day 6 | P5-WC-1 | BUILD (owner) | Requirements (Workflow C) | 0.5 | reviewed by FDE-1 | RUB-07 |  |
| Day 6-7 | P5-WB-2 | REVIEW | HLD / LLD & contract (Workflow B) | — | owned by FDE-2 | RUB-07, RUB-08 |  |
| Day 6-7 | P5-WC-2 | BUILD (owner) | HLD / LLD & contract (Workflow C) | 0.5 | reviewed by FDE-1 | RUB-07, RUB-08 |  |
| Day 7 | P5-SYNC-1 | ATTEND (sync) | Spec-quality review sign-off | — | all 5 FDEs | RUB-05, RUB-07, RUB-08, RUB-13 |  |
| Day 7 | P5-WA-3 | REVIEW | Test plan & fixtures (Workflow A) | — | owned by FDE-1 | RUB-08, RUB-13 |  |
| Day 7 | P5-WC-3 | BUILD (owner) | Test plan & fixtures (Workflow C) | 0.5 | reviewed by FDE-2 | RUB-08, RUB-13 |  |
| Day 8 | P6-SYNC-1 | ATTEND (sync) | Stage-gate decision record | — | all 5 FDEs | RUB-09, RUB-10, RUB-11 (hard gates) |  |
| Day 8 | P6-WC-1 | BUILD (owner) | Reliability input & QRM (Workflow C) | 0.5 | reviewed by FDE-5 | RUB-09, RUB-15 (hard gate) |  |
| Day 8 | P6-WC-2 | BUILD (owner) | ADR(s) (Workflow C) | 0.25 | reviewed by FDE-4 | RUB-04 |  |
| Day 9 | GEMBA-2 | REVIEW | Gemba session notes (Workflow C, driven by FDE-5) | — | owned by FDE-5 | RUB-08, RUB-13 |  |
| Day 9 | P7-WC-1 | BUILD (owner) | Working Workflow-C module (offline) | 1 | reviewed by FDE-4 | RUB-08 |  |
| Day 9-10 | P7-WA-2 | REVIEW | Machine-readable test results (Workflow A) | — | owned by FDE-1 | RUB-08, RUB-13 (hard gate) |  |
| Day 9-10 | P7-WC-2 | BUILD (owner) | Machine-readable test results (Workflow C) | 0.75 | reviewed by FDE-2 | RUB-08, RUB-13 (hard gate) |  |
| Day 10 | P7-SYNC-1 | ATTEND (sync) | Submission check pass & clean-room proof | — | all 5 FDEs | RUB-16 |  |
| Day 10 | P7-SYNC-2 | ATTEND (sync) | Final defence pack & recommendation | — | all 5 FDEs | RUB-17 |  |
| Day 10 | P7-WC-3 | BUILD (owner) | Evaluation results (Workflow C) | 0.5 | reviewed by FDE-5 | RUB-13 |  |
|  |  |  | Total build effort for FDE-3: | 9.25 |  |  |  |
| FDE-4 — Domain, Architecture & Security |  |  |  |  |  |  |  |
| Day | WBS ID | Role | Activity / Deliverable | Build effort
(person-days) | Counterpart | Rubric ID(s) |  |
| Day 1 | P1-ARC-1 | BUILD (owner) | Case reading log (architecture slice) | 0.5 | reviewed by FDE-5 | RUB-01 |  |
| Day 1 | P1-GOV-1 | REVIEW | Case reading log & assumptions register | — | owned by FDE-5 | RUB-01 |  |
| Day 1-2 | P1-ARC-2 | BUILD (owner) | Draft bounded-context long-list | 0.25 | reviewed by FDE-5 | RUB-04 |  |
| Day 1-2 | P1-GOV-2 | REVIEW | Stakeholder & decision-rights map | — | owned by FDE-5 | RUB-02 |  |
| Day 2 | P1-SYNC-1 | ATTEND (sync) | Unified context/assumptions log (feeds 01_BUSINESS_CASE) | — | all 5 FDEs | RUB-01, RUB-02 |  |
| Day 2 | P2-ARC-1 | BUILD (owner) | Prohibited-action boundary specification (draft) | 0.5 | reviewed by FDE-5 | RUB-02 (hard-gate driver) |  |
| Day 2 | P2-ARC-2 | BUILD (owner) | Trust-boundary & override-authority note | 0.25 | reviewed by FDE-5 | RUB-02, RUB-10 |  |
| Day 2 | P2-GOV-1 | REVIEW | SCQA decision narrative | — | owned by FDE-5 | RUB-01 |  |
| Day 2 | P2-SYNC-1 | BUILD (owner) | Prioritized scope, safety boundary & release backlog | 0.5 | reviewed by All FDEs (Steering) | RUB-01, RUB-02, RUB-03 |  |
| Day 2-3 | P3-ARC-1 | BUILD (owner) | Shared-kernel model | 0.5 | reviewed by FDE-5 | RUB-04 |  |
| Day 2-3 | P3-WA-1 | REVIEW | Bounded context & language (Workflow A) | — | owned by FDE-1 | RUB-04 |  |
| Day 2-3 | P3-WB-1 | REVIEW | Bounded context & language (Workflow B) | — | owned by FDE-2 | RUB-04 |  |
| Day 2-3 | P3-WC-1 | REVIEW | Bounded context & language (Workflow C) | — | owned by FDE-3 | RUB-04 |  |
| Day 3 | P3-ARC-2 | BUILD (owner) | Semantic authority & provenance framework | 0.5 | reviewed by FDE-5 | RUB-05, RUB-06 |  |
| Day 3 | P3-GOV-1 | REVIEW | Regulatory document-authority note | — | owned by FDE-5 | RUB-05, RUB-12 |  |
| Day 3 | P3-SYNC-1 | BUILD (owner) | DDD context map & ubiquitous language | 0.5 | reviewed by All FDEs (Steering) | RUB-04 |  |
| Day 3 | P3-WA-2 | REVIEW | Data contract & ontology input (Workflow A) | — | owned by FDE-1 | RUB-05, RUB-06 |  |
| Day 3 | P3-WB-2 | REVIEW | Data contract & ontology input (Workflow B) | — | owned by FDE-2 | RUB-05, RUB-06 |  |
| Day 3 | P3-WC-2 | REVIEW | Data contract & ontology input (Workflow C) | — | owned by FDE-3 | RUB-05, RUB-06 |  |
| Day 3 | SPIKE-WA-1 | REVIEW | Walking-skeleton spike (Workflow A) + findings note | — | owned by FDE-1 | RUB-01, RUB-08 |  |
| Day 3 | SPIKE-WB-1 | REVIEW | Walking-skeleton spike (Workflow B) + findings note | — | owned by FDE-2 | RUB-01, RUB-08 |  |
| Day 3 | SPIKE-WC-1 | REVIEW | Walking-skeleton spike (Workflow C) + findings note | — | owned by FDE-3 | RUB-01, RUB-08 |  |
| Day 3-4 | P3-GOV-2 | REVIEW | Data governance & stewardship note | — | owned by FDE-5 | RUB-05 |  |
| Day 3-4 | P3-SYNC-2 | BUILD (owner) | Ontology/glossary & semantic authority model | 0.5 | reviewed by All FDEs (Steering) | RUB-05, RUB-06 |  |
| Day 4 | P3-ARC-3 | BUILD (owner) | Knowledge-graph decision record | 0.5 | reviewed by FDE-5 | RUB-06 |  |
| Day 4 | P4-ARC-1 | BUILD (owner) | C4 system-context view | 0.25 | reviewed by FDE-5 | RUB-04, RUB-07 |  |
| Day 4 | P4-WA-1 | REVIEW | Container/component view (Workflow A) | — | owned by FDE-1 | RUB-04, RUB-07 |  |
| Day 4 | P4-WB-1 | REVIEW | Container/component view (Workflow B) | — | owned by FDE-2 | RUB-04, RUB-07 |  |
| Day 4 | P4-WC-1 | REVIEW | Container/component view (Workflow C) | — | owned by FDE-3 | RUB-04, RUB-07 |  |
| Day 4-5 | P4-ARC-2 | BUILD (owner) | Trust-boundary & Zero-Trust view | 0.5 | reviewed by FDE-5 | RUB-10 |  |
| Day 4-5 | P4-GOV-1 | REVIEW | Human-oversight & blueprint design | — | owned by FDE-5 | RUB-02 |  |
| Day 4-5 | P4-WA-2 | REVIEW | Data-flow & control-point view (Workflow A) | — | owned by FDE-1 | RUB-05, RUB-10 |  |
| Day 4-5 | P4-WB-2 | REVIEW | Data-flow & control-point view (Workflow B) | — | owned by FDE-2 | RUB-05, RUB-10 |  |
| Day 4-5 | P4-WC-2 | REVIEW | Data-flow & control-point view (Workflow C) | — | owned by FDE-3 | RUB-05, RUB-10 |  |
| Day 5 | OD-1 | BUILD (owner) | Ontology delta log v2 | 0.25 | reviewed by FDE-5 | RUB-05, RUB-06 |  |
| Day 5 | P4-GOV-2 | REVIEW | Adoption & change-management plan (draft) | — | owned by FDE-5 | RUB-02, RUB-11 |  |
| Day 5 | P4-SYNC-1 | BUILD (owner) | C4 container/component view (full) | 0.5 | reviewed by All FDEs (Steering) | RUB-04, RUB-07 |  |
| Day 6 | P5-ARC-1 | BUILD (owner) | Requirements traceability matrix (spine) | 0.5 | reviewed by FDE-5 | RUB-07 |  |
| Day 6-7 | P5-ARC-2 | BUILD (owner) | ADR seed set (4 ADRs) | 0.5 | reviewed by FDE-5 | RUB-04, RUB-07 |  |
| Day 7 | OD-2 | BUILD (owner) | Ontology delta log v3 | 0.25 | reviewed by FDE-5 | RUB-05, RUB-06 |  |
| Day 7 | P5-GOV-1 | REVIEW | Build backlog & evidence plan | — | owned by FDE-5 | RUB-07 |  |
| Day 7 | P5-GOV-2 | REVIEW | TEVV plan skeleton | — | owned by FDE-5 | RUB-13 |  |
| Day 7 | P5-SYNC-1 | ATTEND (sync) | Spec-quality review sign-off | — | all 5 FDEs | RUB-05, RUB-07, RUB-08, RUB-13 |  |
| Day 8 | P6-ARC-1 | BUILD (owner) | Approved ADR register (10+ ADRs) | 0.5 | reviewed by FDE-5 | RUB-04, RUB-07 |  |
| Day 8 | P6-ARC-2 | BUILD (owner) | Threat / abuse model | 0.5 | reviewed by FDE-5 | RUB-10 (hard gate) |  |
| Day 8 | P6-GOV-1 | REVIEW | Regulatory & governance applicability note | — | owned by FDE-5 | RUB-12 |  |
| Day 8 | P6-GOV-2 | REVIEW | RAI & privacy-ethics consolidation | — | owned by FDE-5 | RUB-11 (hard gate) |  |
| Day 8 | P6-SYNC-1 | ATTEND (sync) | Stage-gate decision record | — | all 5 FDEs | RUB-09, RUB-10, RUB-11 (hard gates) |  |
| Day 8 | P6-WA-2 | REVIEW | ADR(s) (Workflow A) | — | owned by FDE-1 | RUB-04 |  |
| Day 8 | P6-WB-2 | REVIEW | ADR(s) (Workflow B) | — | owned by FDE-2 | RUB-04 |  |
| Day 8 | P6-WC-2 | REVIEW | ADR(s) (Workflow C) | — | owned by FDE-3 | RUB-04 |  |
| Day 9 | GEMBA-1 | BUILD (owner) | Gemba session notes (Workflow B, driven by FDE-4) | 0.25 | reviewed by FDE-2 | RUB-08, RUB-10 |  |
| Day 9 | P7-WA-1 | REVIEW | Working Workflow-A module (offline) | — | owned by FDE-1 | RUB-08 |  |
| Day 9 | P7-WB-1 | REVIEW | Working Workflow-B module (offline) | — | owned by FDE-2 | RUB-08 |  |
| Day 9 | P7-WC-1 | REVIEW | Working Workflow-C module (offline) | — | owned by FDE-3 | RUB-08 |  |
| Day 9-10 | P7-ARC-1 | BUILD (owner) | Integrated app shell with kill switch & continuity | 0.75 | reviewed by FDE-5 | RUB-08, RUB-15 |  |
| Day 10 | OD-3 | BUILD (owner) | Ontology delta log v4 (final, submission version) | 0.25 | reviewed by FDE-5 | RUB-05, RUB-06 |  |
| Day 10 | P7-ARC-2 | BUILD (owner) | Red-team evidence & remediation log | 0.5 | reviewed by FDE-5 | RUB-10 (hard gate) |  |
| Day 10 | P7-ARC-3 | BUILD (owner) | FinOps instrumentation & cost evidence | 0.25 | reviewed by FDE-5 | RUB-14 |  |
| Day 10 | P7-GOV-1 | REVIEW | Evaluation scorecard | — | owned by FDE-5 | RUB-13 (hard gate) |  |
| Day 10 | P7-GOV-2 | REVIEW | Reliability & continuity runbooks | — | owned by FDE-5 | RUB-15 (hard gate) |  |
| Day 10 | P7-GOV-3 | REVIEW | Operating model, roadmap & handover pack | — | owned by FDE-5 | RUB-16 |  |
| Day 10 | P7-SYNC-1 | BUILD (owner) | Submission check pass & clean-room proof | 0.25 | reviewed by All FDEs (Steering) | RUB-16 |  |
| Day 10 | P7-SYNC-2 | ATTEND (sync) | Final defence pack & recommendation | — | all 5 FDEs | RUB-17 |  |
|  |  |  | Total build effort for FDE-4: | 10.5 |  |  |  |
| FDE-5 — Product / Value / Governance / Evaluation |  |  |  |  |  |  |  |
| Day | WBS ID | Role | Activity / Deliverable | Build effort
(person-days) | Counterpart | Rubric ID(s) |  |
| Day 1 | P1-ARC-1 | REVIEW | Case reading log (architecture slice) | — | owned by FDE-4 | RUB-01 |  |
| Day 1 | P1-GOV-1 | BUILD (owner) | Case reading log & assumptions register | 0.5 | reviewed by FDE-4 | RUB-01 |  |
| Day 1-2 | P1-ARC-2 | REVIEW | Draft bounded-context long-list | — | owned by FDE-4 | RUB-04 |  |
| Day 1-2 | P1-GOV-2 | BUILD (owner) | Stakeholder & decision-rights map | 0.5 | reviewed by FDE-4 | RUB-02 |  |
| Day 2 | P1-SYNC-1 | BUILD (owner) | Unified context/assumptions log (feeds 01_BUSINESS_CASE) | 0.5 | reviewed by All FDEs (Steering) | RUB-01, RUB-02 |  |
| Day 2 | P2-ARC-1 | REVIEW | Prohibited-action boundary specification (draft) | — | owned by FDE-4 | RUB-02 (hard-gate driver) |  |
| Day 2 | P2-ARC-2 | REVIEW | Trust-boundary & override-authority note | — | owned by FDE-4 | RUB-02, RUB-10 |  |
| Day 2 | P2-GOV-1 | BUILD (owner) | SCQA decision narrative | 0.5 | reviewed by FDE-4 | RUB-01 |  |
| Day 2 | P2-GOV-2 | BUILD (owner) | Value hypothesis, KPI tree & no-AI comparison | 0.75 | reviewed by FDE-1 | RUB-01, RUB-03 |  |
| Day 2 | P2-SYNC-1 | ATTEND (sync) | Prioritized scope, safety boundary & release backlog | — | all 5 FDEs | RUB-01, RUB-02, RUB-03 |  |
| Day 2-3 | P3-ARC-1 | REVIEW | Shared-kernel model | — | owned by FDE-4 | RUB-04 |  |
| Day 3 | P3-ARC-2 | REVIEW | Semantic authority & provenance framework | — | owned by FDE-4 | RUB-05, RUB-06 |  |
| Day 3 | P3-GOV-1 | BUILD (owner) | Regulatory document-authority note | 0.5 | reviewed by FDE-4 | RUB-05, RUB-12 |  |
| Day 3 | P3-SYNC-1 | ATTEND (sync) | DDD context map & ubiquitous language | — | all 5 FDEs | RUB-04 |  |
| Day 3-4 | P3-GOV-2 | BUILD (owner) | Data governance & stewardship note | 0.25 | reviewed by FDE-4 | RUB-05 |  |
| Day 3-4 | P3-SYNC-2 | ATTEND (sync) | Ontology/glossary & semantic authority model | — | all 5 FDEs | RUB-05, RUB-06 |  |
| Day 4 | P3-ARC-3 | REVIEW | Knowledge-graph decision record | — | owned by FDE-4 | RUB-06 |  |
| Day 4 | P4-ARC-1 | REVIEW | C4 system-context view | — | owned by FDE-4 | RUB-04, RUB-07 |  |
| Day 4-5 | P4-ARC-2 | REVIEW | Trust-boundary & Zero-Trust view | — | owned by FDE-4 | RUB-10 |  |
| Day 4-5 | P4-GOV-1 | BUILD (owner) | Human-oversight & blueprint design | 0.5 | reviewed by FDE-4 | RUB-02 |  |
| Day 5 | OD-1 | REVIEW | Ontology delta log v2 | — | owned by FDE-4 | RUB-05, RUB-06 |  |
| Day 5 | P4-GOV-2 | BUILD (owner) | Adoption & change-management plan (draft) | 0.5 | reviewed by FDE-4 | RUB-02, RUB-11 |  |
| Day 5 | P4-SYNC-1 | ATTEND (sync) | C4 container/component view (full) | — | all 5 FDEs | RUB-04, RUB-07 |  |
| Day 6 | P5-ARC-1 | REVIEW | Requirements traceability matrix (spine) | — | owned by FDE-4 | RUB-07 |  |
| Day 6-7 | P5-ARC-2 | REVIEW | ADR seed set (4 ADRs) | — | owned by FDE-4 | RUB-04, RUB-07 |  |
| Day 7 | OD-2 | REVIEW | Ontology delta log v3 | — | owned by FDE-4 | RUB-05, RUB-06 |  |
| Day 7 | P5-GOV-1 | BUILD (owner) | Build backlog & evidence plan | 0.5 | reviewed by FDE-4 | RUB-07 |  |
| Day 7 | P5-GOV-2 | BUILD (owner) | TEVV plan skeleton | 0.5 | reviewed by FDE-4 | RUB-13 |  |
| Day 7 | P5-SYNC-1 | BUILD (owner) | Spec-quality review sign-off | 0.5 | reviewed by All FDEs (Steering) | RUB-05, RUB-07, RUB-08, RUB-13 |  |
| Day 8 | P6-ARC-1 | REVIEW | Approved ADR register (10+ ADRs) | — | owned by FDE-4 | RUB-04, RUB-07 |  |
| Day 8 | P6-ARC-2 | REVIEW | Threat / abuse model | — | owned by FDE-4 | RUB-10 (hard gate) |  |
| Day 8 | P6-GOV-1 | BUILD (owner) | Regulatory & governance applicability note | 0.5 | reviewed by FDE-4 | RUB-12 |  |
| Day 8 | P6-GOV-2 | BUILD (owner) | RAI & privacy-ethics consolidation | 0.5 | reviewed by FDE-4 | RUB-11 (hard gate) |  |
| Day 8 | P6-SYNC-1 | BUILD (owner) | Stage-gate decision record | 0.5 | reviewed by All FDEs (Steering) | RUB-09, RUB-10, RUB-11 (hard gates) |  |
| Day 8 | P6-WA-1 | REVIEW | Validation strategy & QRM (Workflow A) | — | owned by FDE-1 | RUB-09 (hard gate) |  |
| Day 8 | P6-WB-1 | REVIEW | Privacy/ethics assessment & DI note (Workflow B) | — | owned by FDE-2 | RUB-09, RUB-11 (hard gate) |  |
| Day 8 | P6-WC-1 | REVIEW | Reliability input & QRM (Workflow C) | — | owned by FDE-3 | RUB-09, RUB-15 (hard gate) |  |
| Day 9 | GEMBA-2 | BUILD (owner) | Gemba session notes (Workflow C, driven by FDE-5) | 0.25 | reviewed by FDE-3 | RUB-08, RUB-13 |  |
| Day 9-10 | P7-ARC-1 | REVIEW | Integrated app shell with kill switch & continuity | — | owned by FDE-4 | RUB-08, RUB-15 |  |
| Day 10 | OD-3 | REVIEW | Ontology delta log v4 (final, submission version) | — | owned by FDE-4 | RUB-05, RUB-06 |  |
| Day 10 | P7-ARC-2 | REVIEW | Red-team evidence & remediation log | — | owned by FDE-4 | RUB-10 (hard gate) |  |
| Day 10 | P7-ARC-3 | REVIEW | FinOps instrumentation & cost evidence | — | owned by FDE-4 | RUB-14 |  |
| Day 10 | P7-GOV-1 | BUILD (owner) | Evaluation scorecard | 0.5 | reviewed by FDE-4 | RUB-13 (hard gate) |  |
| Day 10 | P7-GOV-2 | BUILD (owner) | Reliability & continuity runbooks | 0.5 | reviewed by FDE-4 | RUB-15 (hard gate) |  |
| Day 10 | P7-GOV-3 | BUILD (owner) | Operating model, roadmap & handover pack | 0.5 | reviewed by FDE-4 | RUB-16 |  |
| Day 10 | P7-SYNC-1 | ATTEND (sync) | Submission check pass & clean-room proof | — | all 5 FDEs | RUB-16 |  |
| Day 10 | P7-SYNC-2 | BUILD (owner) | Final defence pack & recommendation | 0.5 | reviewed by All FDEs (Steering) | RUB-17 |  |
| Day 10 | P7-WA-3 | REVIEW | Evaluation results (Workflow A) | — | owned by FDE-1 | RUB-13 |  |
| Day 10 | P7-WB-3 | REVIEW | Evaluation results (Workflow B) | — | owned by FDE-2 | RUB-13 |  |
| Day 10 | P7-WC-3 | REVIEW | Evaluation results (Workflow C) | — | owned by FDE-3 | RUB-13 |  |
|  |  |  | Total build effort for FDE-5: | 9.75 |  |  |  |
## Sheet: Rubric Coverage Map
| Rubric Coverage Map — How the Plan Earns All 180 Points |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Strategy: every rubric criterion is assigned to a lane owner as primary, tagged on every contributing WBS task, and checked at the nearest Sync Gate — so no criterion is structurally orphaned between lanes, and hard gates are never left to the last day. |  |  |  |  |  |  |  |
| Rubric ID | Area | Points | Hard gate | Minimum evidence (from ASSESSMENT_RUBRIC.csv) | Contributing WBS IDs | Primary owner(s) | Checked at Sync Gate |
| RUB-01 | Discovery, measurable problem and no-AI challenge | 10 | No | 01_BUSINESS_CASE; 02_DMAIC_WORKBOOK | P1-GOV-1, P1-ARC-1, P1-WA-1, P1-WA-2, P1-WB-1, P1-WB-2, P1-WC-1, P1-WC-2, P1-SYNC-1, P2-GOV-1, P2-GOV-2, P2-WA-1, P2-WB-1, P2-WC-1, P2-SYNC-1, SPIKE-WA-1, SPIKE-WB-1, SPIKE-WC-1 | FDE-1, FDE-2, FDE-3, FDE-4, FDE-5 | P1-SYNC-1, P2-SYNC-1 |
| RUB-02 | Product proposition, users and human oversight | 10 | No | 03_STAKEHOLDER_DECISION_RIGHTS; 04_PRODUCT_SERVICE_BLUEPRINT | P1-GOV-2, P1-WA-2, P1-WB-2, P1-WC-2, P1-SYNC-1, P2-ARC-1, P2-ARC-2, P2-WA-1, P2-WB-1, P2-WC-1, P2-SYNC-1, P4-GOV-1, P4-GOV-2 | FDE-1, FDE-2, FDE-3, FDE-4, FDE-5 | P1-SYNC-1, P2-SYNC-1 |
| RUB-03 | DMAIC, value case and benefits realization | 10 | No | 01_BUSINESS_CASE; 02_DMAIC_WORKBOOK | P1-WA-2, P1-WB-2, P1-WC-2, P2-GOV-2, P2-WA-2, P2-WB-2, P2-WC-2, P2-SYNC-1 | FDE-1, FDE-2, FDE-3, FDE-4, FDE-5 | P2-SYNC-1 |
| RUB-04 | DDD and brownfield modernization | 12 | No | 05_DDD_CONTEXT_MAP; 10_C4_ARCHITECTURE; 11_ADR_REGISTER | P1-ARC-2, P3-ARC-1, P3-WA-1, P3-WB-1, P3-WC-1, P3-SYNC-1, P4-ARC-1, P4-WA-1, P4-WB-1, P4-WC-1, P4-SYNC-1, P5-ARC-2, P6-ARC-1, P6-WA-2, P6-WB-2, P6-WC-2 | FDE-1, FDE-2, FDE-3, FDE-4 | P3-SYNC-1, P4-SYNC-1 |
| RUB-05 | Data governance, integrity, lineage and contracts | 14 | Yes | 06_DATA_GOVERNANCE_INTEGRITY; 09_REQUIREMENTS_TRACEABILITY; 12_INTEGRATION_CONTRACTS | P3-ARC-2, P3-WA-2, P3-WB-2, P3-WC-2, P3-GOV-1, P3-GOV-2, P3-SYNC-2, P4-WA-2, P4-WB-2, P4-WC-2, P5-SYNC-1, OD-1, OD-2, OD-3 | FDE-1, FDE-2, FDE-3, FDE-4, FDE-5 | P3-SYNC-2, P5-SYNC-1 |
| RUB-06 | Ontology, semantic layer and knowledge-graph decision | 8 | No | 07_ONTOLOGY_SEMANTIC_LAYER; 08_KNOWLEDGE_GRAPH_DECISION | P3-ARC-2, P3-WA-2, P3-WB-2, P3-WC-2, P3-SYNC-2, P3-ARC-3, OD-1, OD-2, OD-3 | FDE-1, FDE-2, FDE-3, FDE-4 | P3-SYNC-2 |
| RUB-07 | Requirements, C4, integrations and ADRs | 12 | No | 09_REQUIREMENTS_TRACEABILITY; 10_C4_ARCHITECTURE; 11_ADR_REGISTER; 12_INTEGRATION_CONTRACTS | P4-ARC-1, P4-WA-1, P4-WB-1, P4-WC-1, P4-SYNC-1, P5-ARC-1, P5-ARC-2, P5-WA-1, P5-WA-2, P5-WB-1, P5-WB-2, P5-WC-1, P5-WC-2, P5-GOV-1, P5-SYNC-1, P6-ARC-1 | FDE-1, FDE-2, FDE-3, FDE-4, FDE-5 | P4-SYNC-1, P5-SYNC-1 |
| RUB-08 | Three-workflow engineering quality | 18 | Yes | submission/src; submission/tests; submission/app | P5-WA-2, P5-WA-3, P5-WB-2, P5-WB-3, P5-WC-2, P5-WC-3, P5-SYNC-1, P7-WA-1, P7-WA-2, P7-WB-1, P7-WB-2, P7-WC-1, P7-WC-2, P7-ARC-1, SPIKE-WA-1, SPIKE-WB-1, SPIKE-WC-1, GEMBA-1, GEMBA-2 | FDE-1, FDE-2, FDE-3, FDE-4, FDE-5 | P5-SYNC-1 |
| RUB-09 | GxP lifecycle, validation and quality risk | 14 | Yes | 13_GXP_LIFECYCLE_VALIDATION; 14_COMPUTER_SOFTWARE_ASSURANCE; 15_QUALITY_RISK_MANAGEMENT | P6-WA-1, P6-WB-1, P6-WC-1, P6-SYNC-1 | FDE-1, FDE-2, FDE-3, FDE-5 | P6-SYNC-1 |
| RUB-10 | Security, agentic security and Zero Trust | 14 | Yes | 16_THREAT_ABUSE_MODEL; negative tests; security evidence | P2-ARC-2, P4-ARC-2, P4-WA-2, P4-WB-2, P4-WC-2, P6-ARC-2, P6-SYNC-1, P7-ARC-2, GEMBA-1 | FDE-1, FDE-2, FDE-3, FDE-4, FDE-5 | P6-SYNC-1 |
| RUB-11 | Privacy, ethics, responsible AI and accessibility | 10 | Yes | 17_PRIVACY_ETHICS; 18_RESPONSIBLE_AI_HUMAN_FACTORS | P4-GOV-2, P6-WB-1, P6-GOV-2, P6-SYNC-1 | FDE-2, FDE-5 | P6-SYNC-1 |
| RUB-12 | Regulatory and governance applicability | 8 | No | 19_EU_AI_ACT_APPLICABILITY; 20_ISO42001_GOVERNANCE; 21_ASSURANCE_CASE | P3-GOV-1, P6-GOV-1 | FDE-5 | P6-SYNC-1 |
| RUB-13 | Evaluation and TEVV | 14 | Yes | 22_EVALUATION_SCORECARD; submission/evaluation | P5-WA-3, P5-WB-3, P5-WC-3, P5-GOV-2, P5-SYNC-1, P7-WA-2, P7-WA-3, P7-WB-2, P7-WB-3, P7-WC-2, P7-WC-3, P7-GOV-1, GEMBA-2 | FDE-1, FDE-2, FDE-3, FDE-5 | P5-SYNC-1 |
| RUB-14 | Token efficiency, economics and AI FinOps | 8 | No | 23_TOKEN_FINOPS; cost evidence | P7-ARC-3 | FDE-4 | P7-SYNC-2 |
| RUB-15 | Reliability, continuity, incident and retirement | 8 | Yes | 24_RELIABILITY_OBSERVABILITY; 25_INCIDENT_RECOVERY; 27_VENDOR_EXIT_RETIREMENT | P6-WC-1, P7-ARC-1, P7-GOV-2 | FDE-3, FDE-4, FDE-5 | P7-SYNC-2 |
| RUB-16 | Operating model, change, handover and roadmap | 4 | No | 26_TARGET_OPERATING_MODEL; 28_PRODUCTION_READINESS; 29_NINETY_DAY_ROADMAP_HANDOVER | P7-GOV-3, P7-SYNC-1 | FDE-4, FDE-5 | P7-SYNC-1 |
| RUB-17 | Final executive and technical defence | 6 | No | 30_ELEVATOR_PITCH; live defence evidence | P7-SYNC-2 | FDE-5 | P7-SYNC-2 |
|  | TOTAL | 180 |  |  |  |  |  |
| Hard-gate criteria (RUB-05, 08, 09, 10, 11, 13, 15) are shaded above. Each has at least one Sync Gate checkpoint before Day 10, so a gate failure surfaces with time to remediate, not on defence day. |  |  |  |  |  |  |  |
## Sheet: Review & Gate Protocol
| Review & Gate Protocol — How This Plan Adheres to the FDE Delivery Cycle |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 1. Traceability spine (Discovery → SCQA → DDD → C4 → ADR → SDD/PRD) |  |  |  |  |  |
| Every phase in the WBS keeps the same spine as the reference plan, just replicated once per workflow lane and once for the enterprise (cross-cutting lanes). Every task's Activity column names the artefact it must cite backward to (Dependency column). A later-stage claim with no earlier artefact or Assumption behind it is a chain break — flag it at the next Sync Gate, don't silently backfill it. |  |  |  |  |  |
| Source: DK-04 concept-scqa-ddd-c4-adr-spine.md; X-08 traceability-spine.md |  |  |  |  |  |
| 2. Evidence discipline |  |  |  |  |  |
| Every '.1' task in Discover (case-reading log) exists specifically to force this habit early: claims cite a source path or inject ID, or are labelled Assumption. No silent facts. This is graded indirectly through RUB-01 and directly through the hard-gate requirement that evidence provenance, authority, effective date and auditability are preserved. |  |  |  |  |  |
| Source: DK-01 checklist-toolchain-and-evidence.md |  |  |  |  |  |
| 3. Spec quality gate before large build |  |  |  |  |  |
| P5-SYNC-1 is a dedicated cross-pod spec-quality review of all three workflow specs — using the same checklist structure as the delivery-kit's spec-quality checklist (problem/scope, in/out of scope, authority boundaries, testable acceptance criteria, negative/abuse cases, consistency with active ADRs) — BEFORE any workflow starts P7 build. This prevents 'vibe-built' POCs. |  |  |  |  |  |
| Source: DK-10 checklist-spec-quality.md; playbook-spec-implement-gate.md |  |  |  |  |  |
| 4. Quality gates are blocking, not advisory |  |  |  |  |  |
| Every Sync Gate (P1–P7) is a Go/Rework or Go/Conditional/Pivot/Stop decision, not a status update. A lane cannot proceed past a Sync Gate with an unresolved hard-gate item (see Rubric Coverage Map) without an explicit, owned, time-boxed waiver recorded in the ADR register. |  |  |  |  |  |
| Source: DK-07 x-02-quality-gates-acceptance-criteria.md |  |  |  |  |  |
| 5. HITL / authority boundaries are designed, not assumed |  |  |  |  |  |
| P2-ARC-1 (prohibited-action boundary) and P2-SYNC-1 (unified safety boundary) exist before any architecture work starts, so 'no autonomous disposition / PV decision / allocation / recall' is a design input to C4 and the data-flow views (P4-WA-2/WB-2/WC-2), not a retrofit. Each workflow's fail-closed control point is reviewed by the Architecture/Security lead specifically. |  |  |  |  |  |
| Source: DK-09 x-04-hitl-authority-boundaries.md; concept-rai-governance-by-design.md |  |  |  |  |  |
| 6. Reviewer independence — never self-review |  |  |  |  |  |
| The Owner and Reviewer columns in the WBS are never the same FDE. See 'Team & Lane Model' for the exact round-robin and specialist-review rules. Peer review of granular, small tasks is a standing ~45–60 minute/day commitment layered on top of each FDE's own build time — it is not itemized as a separate scheduled day, which is what keeps 88 reviewed tasks compatible with a 10-day sprint. |  |  |  |  |  |
| Source: DK-10 checklist-spec-quality.md ('reviewers assigned, ideally cross-pod') |  |  |  |  |  |
| 7. Product mindset over activity theatre |  |  |  |  |  |
| Every workflow lane's Discover-phase baseline (P1-WA-2/WB-2/WC-2) and Frame-phase value hypothesis (P2-WA-2/WB-2/WC-2) force a measurable outcome statement before any design work — stakeholder outcomes and learning loops, not slideware. |  |  |  |  |  |
| Source: DK-01 concept-fde-role-and-ambiguity.md |  |  |  |  |  |
| 8. Toolchain & evidence hygiene entry/exit |  |  |  |  |  |
| Day 1 for every FDE starts with a 0.5-day case-reading task producing a dated, sourced log — mirroring the delivery-kit's toolchain & evidence checklist entry/exit criteria (repo runs locally, claims cited or marked Assumption, artefacts named so a teammate finds them in under 2 minutes). |  |  |  |  |  |
| Source: DK-01 checklist-toolchain-and-evidence.md |  |  |  |  |  |
| 9. Sync Gate cadence (the only synchronous points) |  |  |  |  |  |
| 7 Sync Gates total, one per phase, each 20-30 minutes, each with a named integrator (rotates between FDE-4 and FDE-5) and a recorded decision. Everything else on the WBS and FDE Sequences sheets runs fully asynchronously within a lane. |  |  |  |  |  |
| P1-SYNC-1, P2-SYNC-1, P3-SYNC-1/2, P4-SYNC-1, P5-SYNC-1, P6-SYNC-1, P7-SYNC-1/2 — see WBS sheet |  |  |  |  |  |
| 10. Field-as-ground-truth spikes ("ship on day one") |  |  |  |  |  |
| Palantir's FDE philosophy explicitly rejects specifying everything before building anything ("if a problem could be solved through a requirements document, it would have been solved already"). SPIKE-WA-1 / SPIKE-WB-1 / SPIKE-WC-1 put throwaway, no-polish code on real case data by Day 3 — in parallel with, not after, the Model/Architect phases. Findings feed forward into the Day-4 container views (see the updated Dependency column on P4-WA-1/WB-1/WC-1) instead of the architecture being pure paper design until Day 9. |  |  |  |  |  |
| Benchmarked against: Palantir FDE model, 'ship on day one' / field-as-ground-truth doctrine; and the package's own WORKSHOP_DEPLOYMENT_PLAN.md, which schedules its first working three-workflow demo at Hour 26 of 40 (65%), not at the very end. |  |  |  |  |  |
| 11. Ontology as a living artefact, not a one-time freeze |  |  |  |  |  |
| OD-1 / OD-2 / OD-3 revisit the Phase-3 ontology and semantic-authority model at Days 5, 7 and 10, reconciling any contradiction the spikes, the specs or the working build surface. Each is versioned (v2, v3, v4-final) rather than silently overwritten, so a defence-day question about unit, terminology or identity conflicts (Final Defence item 6) has a dated, inspectable trail. |  |  |  |  |  |
| Benchmarked against: Palantir's ontology/object-model work as a continuously revisited platform primitive, not a one-time deliverable. |  |  |  |  |  |
| 12. Gemba — cross-cutting leads get hands-on exposure |  |  |  |  |  |
| GEMBA-1 (FDE-4 with Workflow B) and GEMBA-2 (FDE-5 with Workflow C) put the two cross-cutting leads inside a real build for one session each on Day 9, driving code against real broken data rather than only reviewing artefacts. This partially closes the gap between the plan's lane specialization (needed to solve the original parallelization problem) and the FDE ideal of an engineer who owns the whole stack. |  |  |  |  |  |
| Benchmarked against: Palantir's 'startup CTO' framing (own problem identification through production deployment, not pieces of it) and the Echo/Delta paired-team structure. |  |  |  |  |  |
| 13. Named-persona acceptance check at every gate |  |  |  |  |  |
| Each of the 9 Sync Gates' exit criteria now names a real stakeholder role from the case's STAKEHOLDER_PACK.md (e.g. 'would the EU Qualified Person and the Global Head of Pharmacovigilance accept this final-decision boundary as stated?') instead of only an internal FDE sign-off. This is the closest a synthetic capstone can get to Palantir's 'continuous customer discovery' without a live customer in the room. |  |  |  |  |  |
| Benchmarked against: Palantir's 'continuous customer discovery — deep conversations, not stakeholder check-ins' doctrine; personas sourced from case/STAKEHOLDER_PACK.md |  |  |  |  |  |
## Sheet: Exit Criteria
| Phase | Lifecycle step | Primary framework | Exit criteria | Minimum evidence | Decision facilitator | Gate result (Sync ID) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Discover | SCQA / DMAIC Define | The business situation, complication, question, affected decisions, stakeholders, constraints and baseline are understood across all three workflows. | 5 case-reading logs; unified stakeholder map; 3 current-state maps; 3 baselines; assumptions log | FDE-5 (facilitator) + all lane leads | P1-SYNC-1 — D1 gate: Go / Rework |
| 2 | Frame | SCQA / DMAIC Measure | The problem is measurable, the no-AI alternative is considered, the three workflows are prioritized, and one unified intended/prohibited-use statement exists. | Enterprise SCQA; KPI tree; no-AI comparison; 3 workflow problem statements; unified safety boundary | FDE-4 (facilitator) + all lane leads | P2-SYNC-1 — D2 gate: Go / Rework |
| 3 | Model | DDD / Ontology / Semantic layer / KG | Bounded contexts, ubiquitous language, identifiers, authority, temporal rules, provenance and the KG decision are agreed enterprise-wide. | DDD context map; unified ontology/glossary; authority framework; KG decision record | FDE-4 (facilitator) + all lane leads | P3-SYNC-1, P3-SYNC-2 — D4 gate: Go / Rework |
| 4 | Architect | C4 / DMAIC Improve | System context, containers, data flows, integrations, GxP boundaries, security boundaries and manual fallback are defined for all three workflows. | C4 context/container view; 3 data-flow views; trust-boundary view; offline mode design | FDE-4 (facilitator) + all lane leads | P4-SYNC-1 — D5 gate: Go / Rework |
| 5 | Specify | SRS / HLD / LLD | Requirements are traceable, contracts are versioned, components are specified, and critical tests exist before build — cross-reviewed for spec quality. | Traceability matrix; 3 sets of requirements/HLD/LLD/contracts; 3 test-fixture sets; spec-quality sign-off | FDE-5 (facilitator) + all lane leads | P5-SYNC-1 — D7 gate: Go / Rework |
| 6 | Decide | ADR / DMAIC Control | Material design choices, risks, validation approach, operating controls, continuity and release assumptions are formally reviewed across all lanes. | 10+ ADRs; threat/abuse model; 3 validation/privacy/reliability notes; regulatory applicability; stage-gate decision | FDE-5 (facilitator) + Steering (all FDEs) | P6-SYNC-1 — D9 gate: Go / Conditional / Pivot / Stop |
| 7 | Deliver & Evaluate | DMAIC Control / Lean Six Sigma | The POC works for all three workflows, prohibited actions fail closed, evaluation thresholds pass, evidence is reproducible and handover is complete. | 3 working modules; test/evaluation results; audit evidence; clean-room proof; submission check; roadmap; defence pack | FDE-4 & FDE-5 (facilitators) + Steering (all FDEs) | P7-SYNC-1, P7-SYNC-2 — D10 gate: Release / Conditional / Pivot / Stop |
## Sheet: Framework Map
| Framework | Purpose | Used in phase | Key output | Connection to next step | Delivery-Kit module | Primary lane owner(s) |
| --- | --- | --- | --- | --- | --- | --- |
| SCQA | Frame why the business problem matters and what decision is required. | 1 Discover; 2 Frame | Decision narrative and problem statement | Creates the problem/domain input for DDD. | DK-04 | FDE-5 (GOV), each workflow lead for their own SCQA |
| DMAIC / Lean Six Sigma | Baseline discipline, measurement, control, defect reduction. | All phases | Baseline, measures, improvement actions, controls, release gates | Keeps architecture tied to measurable outcomes. | DK-08 | FDE-5 (GOV) |
| DDD | Bounded contexts, language, rules, decision ownership. | 3 Model | Context map, aggregates, invariants, events, ownership | Provides semantics for ontology and architecture. | DK-04 | FDE-4 (ARC), each workflow lead contributes |
| Ontology | Concepts, identifiers, relationships, units, terminology. | 3 Model | Controlled vocabulary and concept model | Feeds semantic layer and evidence linking. | DK-06 | FDE-4 (ARC), each workflow lead contributes |
| Semantic layer | Authority, provenance, temporal applicability, jurisdiction. | 3 Model; 4 Architect | Authority and conflict-resolution model | Makes evidence usable in architecture decisions. | DK-06 | FDE-4 (ARC) |
| Knowledge graph | Facts, relationships, lineage, provenance where reasoning adds value. | 3 Model; 4 Architect | KG decision, or justified simpler alternative | Realizes semantic relationships in architecture. | DK-06 | FDE-4 (ARC) |
| C4 | Visualize context, containers, components, data flows, boundaries. | 4 Architect | Context, container, component views | Turns domain decisions into implementable structure. | DK-04 | FDE-4 (ARC), each workflow lead contributes |
| SRS / HLD / LLD | Requirements, interfaces, components, sequences, contracts, controls. | 5 Specify | Traceability matrix, specs, schemas, acceptance criteria | Creates the build and test baseline. | DK-10 | Each workflow lead; FDE-4 owns the spine |
| ADR | Design decisions, alternatives, trade-offs, consequences, assumptions. | 6 Decide | Approved decision records | Makes governance and architecture inspectable. | DK-04 | FDE-4 (ARC), each workflow lead contributes |
| Evaluation / TEVV | Evidence fidelity, safety, security, reliability, subgroup, recovery. | 7 Deliver & Evaluate | Test/evaluation results and release recommendation | Feeds DMAIC Control and future improvement. | DK-07 / DK-09 | FDE-5 (GOV), each workflow lead contributes |
## Sheet: Parallel Execution Calendar
| Parallel Execution Calendar — What Each Lane Is Doing, Day by Day |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Read across a row: five lanes running the same day, none blocked on another except where a SYNC row is shown for that day. |  |  |  |  |  |
| Day | Product / Value / Governance / Evaluation | Domain, Architecture & Security | Workflow A — GxP Evidence Reconciliation | Workflow B — PV Case Intake | Workflow C — Bounded Supply Planning |
| Day 1 | P1-GOV-1: Case reading log & assumptions register (FDE-5)
P1-GOV-2: Stakeholder & decision-rights map (FDE-5) | P1-ARC-1: Case reading log (architecture slice) (FDE-4)
P1-ARC-2: Draft bounded-context long-list (FDE-4) | P1-WA-1: Case reading log (Workflow A) (FDE-1)
P1-WA-2: Current-state map & baseline (batch review) (FDE-1) | P1-WB-1: Case reading log (Workflow B) (FDE-2)
P1-WB-2: Current-state map & baseline (PV intake) (FDE-2) | P1-WC-1: Case reading log (Workflow C) (FDE-3)
P1-WC-2: Current-state map & baseline (supply/cold-chain) (FDE-3) |
| Day 2 | P1-GOV-2: Stakeholder & decision-rights map (FDE-5)
P2-GOV-1: SCQA decision narrative (FDE-5)
P2-GOV-2: Value hypothesis, KPI tree & no-AI comparison (FDE-5) | P1-ARC-2: Draft bounded-context long-list (FDE-4)
P2-ARC-1: Prohibited-action boundary specification (draft) (FDE-4)
P2-ARC-2: Trust-boundary & override-authority note (FDE-4)
P3-ARC-1: Shared-kernel model (FDE-4) | P1-WA-2: Current-state map & baseline (batch review) (FDE-1)
P2-WA-1: Problem statement (Workflow A) (FDE-1)
P2-WA-2: Value hypothesis (Workflow A) (FDE-1)
P3-WA-1: Bounded context & language (Workflow A) (FDE-1) | P1-WB-2: Current-state map & baseline (PV intake) (FDE-2)
P2-WB-1: Problem statement (Workflow B) (FDE-2)
P2-WB-2: Value hypothesis (Workflow B) (FDE-2)
P3-WB-1: Bounded context & language (Workflow B) (FDE-2) | P1-WC-2: Current-state map & baseline (supply/cold-chain) (FDE-3)
P2-WC-1: Problem statement (Workflow C) (FDE-3)
P2-WC-2: Value hypothesis (Workflow C) (FDE-3)
P3-WC-1: Bounded context & language (Workflow C) (FDE-3) |
| → SYNC | P1-SYNC-1: Unified context/assumptions log (feeds 01_BUSINESS_CASE)  |  P2-SYNC-1: Prioritized scope, safety boundary & release backlog |  |  |  |  |
| Day 3 | P3-GOV-1: Regulatory document-authority note (FDE-5)
P3-GOV-2: Data governance & stewardship note (FDE-5) | P3-ARC-1: Shared-kernel model (FDE-4)
P3-ARC-2: Semantic authority & provenance framework (FDE-4) | P3-WA-1: Bounded context & language (Workflow A) (FDE-1)
P3-WA-2: Data contract & ontology input (Workflow A) (FDE-1)
SPIKE-WA-1: Walking-skeleton spike (Workflow A) + findings note (FDE-1) | P3-WB-1: Bounded context & language (Workflow B) (FDE-2)
P3-WB-2: Data contract & ontology input (Workflow B) (FDE-2)
SPIKE-WB-1: Walking-skeleton spike (Workflow B) + findings note (FDE-2) | P3-WC-1: Bounded context & language (Workflow C) (FDE-3)
P3-WC-2: Data contract & ontology input (Workflow C) (FDE-3)
SPIKE-WC-1: Walking-skeleton spike (Workflow C) + findings note (FDE-3) |
| → SYNC | P3-SYNC-1: DDD context map & ubiquitous language  |  P3-SYNC-2: Ontology/glossary & semantic authority model |  |  |  |  |
| Day 4 | P3-GOV-2: Data governance & stewardship note (FDE-5)
P4-GOV-1: Human-oversight & blueprint design (FDE-5) | P3-ARC-3: Knowledge-graph decision record (FDE-4)
P4-ARC-1: C4 system-context view (FDE-4)
P4-ARC-2: Trust-boundary & Zero-Trust view (FDE-4) | P4-WA-1: Container/component view (Workflow A) (FDE-1)
P4-WA-2: Data-flow & control-point view (Workflow A) (FDE-1) | P4-WB-1: Container/component view (Workflow B) (FDE-2)
P4-WB-2: Data-flow & control-point view (Workflow B) (FDE-2) | P4-WC-1: Container/component view (Workflow C) (FDE-3)
P4-WC-2: Data-flow & control-point view (Workflow C) (FDE-3) |
| → SYNC | P3-SYNC-2: Ontology/glossary & semantic authority model |  |  |  |  |
| Day 5 | P4-GOV-1: Human-oversight & blueprint design (FDE-5)
P4-GOV-2: Adoption & change-management plan (draft) (FDE-5) | P4-ARC-2: Trust-boundary & Zero-Trust view (FDE-4)
OD-1: Ontology delta log v2 (FDE-4) | P4-WA-2: Data-flow & control-point view (Workflow A) (FDE-1) | P4-WB-2: Data-flow & control-point view (Workflow B) (FDE-2) | P4-WC-2: Data-flow & control-point view (Workflow C) (FDE-3) |
| → SYNC | P4-SYNC-1: C4 container/component view (full) |  |  |  |  |
| Day 6 |  | P5-ARC-1: Requirements traceability matrix (spine) (FDE-4)
P5-ARC-2: ADR seed set (4 ADRs) (FDE-4) | P5-WA-1: Requirements (Workflow A) (FDE-1)
P5-WA-2: HLD / LLD & contract (Workflow A) (FDE-1) | P5-WB-1: Requirements (Workflow B) (FDE-2)
P5-WB-2: HLD / LLD & contract (Workflow B) (FDE-2) | P5-WC-1: Requirements (Workflow C) (FDE-3)
P5-WC-2: HLD / LLD & contract (Workflow C) (FDE-3) |
| Day 7 | P5-GOV-1: Build backlog & evidence plan (FDE-5)
P5-GOV-2: TEVV plan skeleton (FDE-5) | P5-ARC-2: ADR seed set (4 ADRs) (FDE-4)
OD-2: Ontology delta log v3 (FDE-4) | P5-WA-2: HLD / LLD & contract (Workflow A) (FDE-1)
P5-WA-3: Test plan & fixtures (Workflow A) (FDE-1) | P5-WB-2: HLD / LLD & contract (Workflow B) (FDE-2)
P5-WB-3: Test plan & fixtures (Workflow B) (FDE-2) | P5-WC-2: HLD / LLD & contract (Workflow C) (FDE-3)
P5-WC-3: Test plan & fixtures (Workflow C) (FDE-3) |
| → SYNC | P5-SYNC-1: Spec-quality review sign-off |  |  |  |  |
| Day 8 | P6-GOV-1: Regulatory & governance applicability note (FDE-5)
P6-GOV-2: RAI & privacy-ethics consolidation (FDE-5) | P6-ARC-1: Approved ADR register (10+ ADRs) (FDE-4)
P6-ARC-2: Threat / abuse model (FDE-4) | P6-WA-1: Validation strategy & QRM (Workflow A) (FDE-1)
P6-WA-2: ADR(s) (Workflow A) (FDE-1) | P6-WB-1: Privacy/ethics assessment & DI note (Workflow B) (FDE-2)
P6-WB-2: ADR(s) (Workflow B) (FDE-2) | P6-WC-1: Reliability input & QRM (Workflow C) (FDE-3)
P6-WC-2: ADR(s) (Workflow C) (FDE-3) |
| → SYNC | P6-SYNC-1: Stage-gate decision record |  |  |  |  |
| Day 9 | GEMBA-2: Gemba session notes (Workflow C, driven by FDE-5) (FDE-5) | P7-ARC-1: Integrated app shell with kill switch & continuity (FDE-4)
GEMBA-1: Gemba session notes (Workflow B, driven by FDE-4) (FDE-4) | P7-WA-1: Working Workflow-A module (offline) (FDE-1)
P7-WA-2: Machine-readable test results (Workflow A) (FDE-1) | P7-WB-1: Working Workflow-B module (offline) (FDE-2)
P7-WB-2: Machine-readable test results (Workflow B) (FDE-2) | P7-WC-1: Working Workflow-C module (offline) (FDE-3)
P7-WC-2: Machine-readable test results (Workflow C) (FDE-3) |
| Day 10 | P7-GOV-1: Evaluation scorecard (FDE-5)
P7-GOV-2: Reliability & continuity runbooks (FDE-5)
P7-GOV-3: Operating model, roadmap & handover pack (FDE-5) | P7-ARC-1: Integrated app shell with kill switch & continuity (FDE-4)
P7-ARC-2: Red-team evidence & remediation log (FDE-4)
P7-ARC-3: FinOps instrumentation & cost evidence (FDE-4)
OD-3: Ontology delta log v4 (final, submission version) (FDE-4) | P7-WA-2: Machine-readable test results (Workflow A) (FDE-1)
P7-WA-3: Evaluation results (Workflow A) (FDE-1) | P7-WB-2: Machine-readable test results (Workflow B) (FDE-2)
P7-WB-3: Evaluation results (Workflow B) (FDE-2) | P7-WC-2: Machine-readable test results (Workflow C) (FDE-3)
P7-WC-3: Evaluation results (Workflow C) (FDE-3) |
| → SYNC | P7-SYNC-1: Submission check pass & clean-room proof  |  P7-SYNC-2: Final defence pack & recommendation |  |  |  |  |
## Sheet: Gantt Chart
| Gantt Chart — AEGIS-PHARMA Optimized FDE Plan (5-Lane Parallel Delivery, 10 Working Days) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bars are derived from WBS Schedule window. Lane colors match Parallel Execution Calendar. Orange SYNC bars are cross-lane gates (only joint checkpoints). Day columns = working days 1–10. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Legend | GOV (FDE-5) |  | ARC (FDE-4) |  | WA (FDE-1) |  | WB (FDE-2) |  | WC (FDE-3) |  | SYNC GATE |  |  |  |  |  |  |  |
| WBS ID | Lane | Phase | Activity / Deliverable | Owner | Effort (d) | Start Day | End Day | Dependency | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 | Day 6 | Day 7 | Day 8 | Day 9 | Day 10 |
| PHASE — 1. Discover & Qualify  |  Schedule: see bars → |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| P1-GOV-1 | GOV | 1. Discover & Qualify | Case reading log & assumptions register | FDE-5 | 0.5 | 1 | 1 | — | ■ |  |  |  |  |  |  |  |  |  |
| P1-GOV-2 | GOV | 1. Discover & Qualify | Stakeholder & decision-rights map | FDE-5 | 0.5 | 1 | 2 | P1-GOV-1 | ■ |  |  |  |  |  |  |  |  |  |
| P1-ARC-1 | ARC | 1. Discover & Qualify | Case reading log (architecture slice) | FDE-4 | 0.5 | 1 | 1 | — | ■ |  |  |  |  |  |  |  |  |  |
| P1-ARC-2 | ARC | 1. Discover & Qualify | Draft bounded-context long-list | FDE-4 | 0.25 | 1 | 2 | P1-ARC-1 | ■ |  |  |  |  |  |  |  |  |  |
| P1-WA-1 | WA | 1. Discover & Qualify | Case reading log (Workflow A) | FDE-1 | 0.5 | 1 | 1 | — | ■ |  |  |  |  |  |  |  |  |  |
| P1-WA-2 | WA | 1. Discover & Qualify | Current-state map & baseline (batch review) | FDE-1 | 0.5 | 1 | 2 | P1-WA-1 | ■ |  |  |  |  |  |  |  |  |  |
| P1-WB-1 | WB | 1. Discover & Qualify | Case reading log (Workflow B) | FDE-2 | 0.5 | 1 | 1 | — | ■ |  |  |  |  |  |  |  |  |  |
| P1-WB-2 | WB | 1. Discover & Qualify | Current-state map & baseline (PV intake) | FDE-2 | 0.5 | 1 | 2 | P1-WB-1 | ■ |  |  |  |  |  |  |  |  |  |
| P1-WC-1 | WC | 1. Discover & Qualify | Case reading log (Workflow C) | FDE-3 | 0.5 | 1 | 1 | — | ■ |  |  |  |  |  |  |  |  |  |
| P1-WC-2 | WC | 1. Discover & Qualify | Current-state map & baseline (supply/cold-chain) | FDE-3 | 0.5 | 1 | 2 | P1-WC-1 | ■ |  |  |  |  |  |  |  |  |  |
| P1-SYNC-1 | SYNC | 1. Discover & Qualify | Unified context/assumptions log (feeds 01_BUSINESS_CASE) | FDE-5 | 0.5 | 2 | 2 | P1-GOV-2, P1-ARC-2, P1-WA-2, P1-WB-2, P1-WC-2 |  | ◆ |  |  |  |  |  |  |  |  |
| PHASE — 2. Frame the Problem  |  Schedule: see bars → |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| P2-GOV-1 | GOV | 2. Frame the Problem | SCQA decision narrative | FDE-5 | 0.5 | 2 | 2 | P1-SYNC-1 |  | ■ |  |  |  |  |  |  |  |  |
| P2-GOV-2 | GOV | 2. Frame the Problem | Value hypothesis, KPI tree & no-AI comparison | FDE-5 | 0.75 | 2 | 2 | P2-GOV-1 |  | ■ |  |  |  |  |  |  |  |  |
| P2-ARC-1 | ARC | 2. Frame the Problem | Prohibited-action boundary specification (draft) | FDE-4 | 0.5 | 2 | 2 | P1-SYNC-1 |  | ■ |  |  |  |  |  |  |  |  |
| P2-ARC-2 | ARC | 2. Frame the Problem | Trust-boundary & override-authority note | FDE-4 | 0.25 | 2 | 2 | P2-ARC-1 |  | ■ |  |  |  |  |  |  |  |  |
| P2-WA-1 | WA | 2. Frame the Problem | Problem statement (Workflow A) | FDE-1 | 0.5 | 2 | 2 | P1-WA-2 |  | ■ |  |  |  |  |  |  |  |  |
| P2-WA-2 | WA | 2. Frame the Problem | Value hypothesis (Workflow A) | FDE-1 | 0.5 | 2 | 2 | P2-WA-1 |  | ■ |  |  |  |  |  |  |  |  |
| P2-WB-1 | WB | 2. Frame the Problem | Problem statement (Workflow B) | FDE-2 | 0.5 | 2 | 2 | P1-WB-2 |  | ■ |  |  |  |  |  |  |  |  |
| P2-WB-2 | WB | 2. Frame the Problem | Value hypothesis (Workflow B) | FDE-2 | 0.5 | 2 | 2 | P2-WB-1 |  | ■ |  |  |  |  |  |  |  |  |
| P2-WC-1 | WC | 2. Frame the Problem | Problem statement (Workflow C) | FDE-3 | 0.5 | 2 | 2 | P1-WC-2 |  | ■ |  |  |  |  |  |  |  |  |
| P2-WC-2 | WC | 2. Frame the Problem | Value hypothesis (Workflow C) | FDE-3 | 0.5 | 2 | 2 | P2-WC-1 |  | ■ |  |  |  |  |  |  |  |  |
| P2-SYNC-1 | SYNC | 2. Frame the Problem | Prioritized scope, safety boundary & release backlog | FDE-4 | 0.5 | 2 | 2 | P2-GOV-2, P2-ARC-2, P2-WA-2, P2-WB-2, P2-WC-2 |  | ◆ |  |  |  |  |  |  |  |  |
| PHASE — 3. Model Domain & Semantics  |  Schedule: see bars → |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| P3-ARC-1 | ARC | 3. Model Domain & Semantics | Shared-kernel model | FDE-4 | 0.5 | 2 | 3 | P2-SYNC-1 |  | ■ |  |  |  |  |  |  |  |  |
| P3-WA-1 | WA | 3. Model Domain & Semantics | Bounded context & language (Workflow A) | FDE-1 | 0.5 | 2 | 3 | P2-WA-2 |  | ■ |  |  |  |  |  |  |  |  |
| P3-WB-1 | WB | 3. Model Domain & Semantics | Bounded context & language (Workflow B) | FDE-2 | 0.5 | 2 | 3 | P2-WB-2 |  | ■ |  |  |  |  |  |  |  |  |
| P3-WC-1 | WC | 3. Model Domain & Semantics | Bounded context & language (Workflow C) | FDE-3 | 0.5 | 2 | 3 | P2-WC-2 |  | ■ |  |  |  |  |  |  |  |  |
| P3-GOV-1 | GOV | 3. Model Domain & Semantics | Regulatory document-authority note | FDE-5 | 0.5 | 3 | 3 | P1-SYNC-1 |  |  | ■ |  |  |  |  |  |  |  |
| P3-GOV-2 | GOV | 3. Model Domain & Semantics | Data governance & stewardship note | FDE-5 | 0.25 | 3 | 4 | P3-GOV-1 |  |  | ■ |  |  |  |  |  |  |  |
| P3-ARC-2 | ARC | 3. Model Domain & Semantics | Semantic authority & provenance framework | FDE-4 | 0.5 | 3 | 3 | P3-ARC-1 |  |  | ■ |  |  |  |  |  |  |  |
| P3-WA-2 | WA | 3. Model Domain & Semantics | Data contract & ontology input (Workflow A) | FDE-1 | 0.5 | 3 | 3 | P3-WA-1 |  |  | ■ |  |  |  |  |  |  |  |
| SPIKE-WA-1 | WA | 3. Model Domain & Semantics | Walking-skeleton spike (Workflow A) + findings note | FDE-1 | 0.75 | 3 | 3 | P2-SYNC-1 |  |  | ▲ |  |  |  |  |  |  |  |
| P3-WB-2 | WB | 3. Model Domain & Semantics | Data contract & ontology input (Workflow B) | FDE-2 | 0.5 | 3 | 3 | P3-WB-1 |  |  | ■ |  |  |  |  |  |  |  |
| SPIKE-WB-1 | WB | 3. Model Domain & Semantics | Walking-skeleton spike (Workflow B) + findings note | FDE-2 | 0.75 | 3 | 3 | P2-SYNC-1 |  |  | ▲ |  |  |  |  |  |  |  |
| P3-WC-2 | WC | 3. Model Domain & Semantics | Data contract & ontology input (Workflow C) | FDE-3 | 0.5 | 3 | 3 | P3-WC-1 |  |  | ■ |  |  |  |  |  |  |  |
| SPIKE-WC-1 | WC | 3. Model Domain & Semantics | Walking-skeleton spike (Workflow C) + findings note | FDE-3 | 0.75 | 3 | 3 | P2-SYNC-1 |  |  | ▲ |  |  |  |  |  |  |  |
| P3-SYNC-1 | SYNC | 3. Model Domain & Semantics | DDD context map & ubiquitous language | FDE-4 | 0.5 | 3 | 3 | P3-ARC-1, P3-WA-1, P3-WB-1, P3-WC-1 |  |  | ◆ |  |  |  |  |  |  |  |
| P3-SYNC-2 | SYNC | 3. Model Domain & Semantics | Ontology/glossary & semantic authority model | FDE-4 | 0.5 | 3 | 4 | P3-ARC-2, P3-WA-2, P3-WB-2, P3-WC-2 |  |  | ◆ |  |  |  |  |  |  |  |
| P3-ARC-3 | ARC | 3. Model Domain & Semantics | Knowledge-graph decision record | FDE-4 | 0.5 | 4 | 4 | P3-SYNC-2 |  |  |  | ■ |  |  |  |  |  |  |
| PHASE — 4. Architect the Solution  |  Schedule: see bars → |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| P4-GOV-1 | GOV | 4. Architect the Solution | Human-oversight & blueprint design | FDE-5 | 0.5 | 4 | 5 | P2-SYNC-1 |  |  |  | ■ |  |  |  |  |  |  |
| P4-ARC-1 | ARC | 4. Architect the Solution | C4 system-context view | FDE-4 | 0.25 | 4 | 4 | P3-SYNC-1 |  |  |  | ■ |  |  |  |  |  |  |
| P4-ARC-2 | ARC | 4. Architect the Solution | Trust-boundary & Zero-Trust view | FDE-4 | 0.5 | 4 | 5 | P4-ARC-1 |  |  |  | ■ |  |  |  |  |  |  |
| P4-WA-1 | WA | 4. Architect the Solution | Container/component view (Workflow A) | FDE-1 | 0.5 | 4 | 4 | P3-WA-2, SPIKE-WA-1 |  |  |  | ■ |  |  |  |  |  |  |
| P4-WA-2 | WA | 4. Architect the Solution | Data-flow & control-point view (Workflow A) | FDE-1 | 0.5 | 4 | 5 | P4-WA-1 |  |  |  | ■ |  |  |  |  |  |  |
| P4-WB-1 | WB | 4. Architect the Solution | Container/component view (Workflow B) | FDE-2 | 0.5 | 4 | 4 | P3-WB-2, SPIKE-WB-1 |  |  |  | ■ |  |  |  |  |  |  |
| P4-WB-2 | WB | 4. Architect the Solution | Data-flow & control-point view (Workflow B) | FDE-2 | 0.5 | 4 | 5 | P4-WB-1 |  |  |  | ■ |  |  |  |  |  |  |
| P4-WC-1 | WC | 4. Architect the Solution | Container/component view (Workflow C) | FDE-3 | 0.5 | 4 | 4 | P3-WC-2, SPIKE-WC-1 |  |  |  | ■ |  |  |  |  |  |  |
| P4-WC-2 | WC | 4. Architect the Solution | Data-flow & control-point view (Workflow C) | FDE-3 | 0.5 | 4 | 5 | P4-WC-1 |  |  |  | ■ |  |  |  |  |  |  |
| P4-GOV-2 | GOV | 4. Architect the Solution | Adoption & change-management plan (draft) | FDE-5 | 0.5 | 5 | 5 | P4-GOV-1 |  |  |  |  | ■ |  |  |  |  |  |
| OD-1 | ARC | 4. Architect the Solution | Ontology delta log v2 | FDE-4 | 0.25 | 5 | 5 | P4-SYNC-1, SPIKE-WA-1, SPIKE-WB-1, SPIKE-WC-1 |  |  |  |  | ■ |  |  |  |  |  |
| P4-SYNC-1 | SYNC | 4. Architect the Solution | C4 container/component view (full) | FDE-4 | 0.5 | 5 | 5 | P4-ARC-2, P4-WA-2, P4-WB-2, P4-WC-2 |  |  |  |  | ◆ |  |  |  |  |  |
| PHASE — 5. Specify & Test  |  Schedule: see bars → |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| P5-ARC-1 | ARC | 5. Specify & Test | Requirements traceability matrix (spine) | FDE-4 | 0.5 | 6 | 6 | P4-SYNC-1 |  |  |  |  |  | ■ |  |  |  |  |
| P5-ARC-2 | ARC | 5. Specify & Test | ADR seed set (4 ADRs) | FDE-4 | 0.5 | 6 | 7 | P5-ARC-1 |  |  |  |  |  | ■ |  |  |  |  |
| P5-WA-1 | WA | 5. Specify & Test | Requirements (Workflow A) | FDE-1 | 0.5 | 6 | 6 | P4-WA-2 |  |  |  |  |  | ■ |  |  |  |  |
| P5-WA-2 | WA | 5. Specify & Test | HLD / LLD & contract (Workflow A) | FDE-1 | 0.5 | 6 | 7 | P5-WA-1 |  |  |  |  |  | ■ |  |  |  |  |
| P5-WB-1 | WB | 5. Specify & Test | Requirements (Workflow B) | FDE-2 | 0.5 | 6 | 6 | P4-WB-2 |  |  |  |  |  | ■ |  |  |  |  |
| P5-WB-2 | WB | 5. Specify & Test | HLD / LLD & contract (Workflow B) | FDE-2 | 0.5 | 6 | 7 | P5-WB-1 |  |  |  |  |  | ■ |  |  |  |  |
| P5-WC-1 | WC | 5. Specify & Test | Requirements (Workflow C) | FDE-3 | 0.5 | 6 | 6 | P4-WC-2 |  |  |  |  |  | ■ |  |  |  |  |
| P5-WC-2 | WC | 5. Specify & Test | HLD / LLD & contract (Workflow C) | FDE-3 | 0.5 | 6 | 7 | P5-WC-1 |  |  |  |  |  | ■ |  |  |  |  |
| P5-GOV-1 | GOV | 5. Specify & Test | Build backlog & evidence plan | FDE-5 | 0.5 | 7 | 7 | P2-SYNC-1 |  |  |  |  |  |  | ■ |  |  |  |
| P5-GOV-2 | GOV | 5. Specify & Test | TEVV plan skeleton | FDE-5 | 0.5 | 7 | 7 | P5-GOV-1 |  |  |  |  |  |  | ■ |  |  |  |
| OD-2 | ARC | 5. Specify & Test | Ontology delta log v3 | FDE-4 | 0.25 | 7 | 7 | P5-SYNC-1 |  |  |  |  |  |  | ■ |  |  |  |
| P5-WA-3 | WA | 5. Specify & Test | Test plan & fixtures (Workflow A) | FDE-1 | 0.5 | 7 | 7 | P5-WA-2 |  |  |  |  |  |  | ■ |  |  |  |
| P5-WB-3 | WB | 5. Specify & Test | Test plan & fixtures (Workflow B) | FDE-2 | 0.5 | 7 | 7 | P5-WB-2 |  |  |  |  |  |  | ■ |  |  |  |
| P5-WC-3 | WC | 5. Specify & Test | Test plan & fixtures (Workflow C) | FDE-3 | 0.5 | 7 | 7 | P5-WC-2 |  |  |  |  |  |  | ■ |  |  |  |
| P5-SYNC-1 | SYNC | 5. Specify & Test | Spec-quality review sign-off | FDE-5 | 0.5 | 7 | 7 | P5-WA-3, P5-WB-3, P5-WC-3 |  |  |  |  |  |  | ◆ |  |  |  |
| PHASE — 6. Decide & Govern  |  Schedule: see bars → |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| P6-GOV-1 | GOV | 6. Decide & Govern | Regulatory & governance applicability note | FDE-5 | 0.5 | 8 | 8 | P3-GOV-2 |  |  |  |  |  |  |  | ■ |  |  |
| P6-GOV-2 | GOV | 6. Decide & Govern | RAI & privacy-ethics consolidation | FDE-5 | 0.5 | 8 | 8 | P6-WB-1, P6-GOV-1 |  |  |  |  |  |  |  | ■ |  |  |
| P6-ARC-1 | ARC | 6. Decide & Govern | Approved ADR register (10+ ADRs) | FDE-4 | 0.5 | 8 | 8 | P5-ARC-2, P6-WA-2, P6-WB-2, P6-WC-2 |  |  |  |  |  |  |  | ■ |  |  |
| P6-ARC-2 | ARC | 6. Decide & Govern | Threat / abuse model | FDE-4 | 0.5 | 8 | 8 | P4-SYNC-1 |  |  |  |  |  |  |  | ■ |  |  |
| P6-WA-1 | WA | 6. Decide & Govern | Validation strategy & QRM (Workflow A) | FDE-1 | 0.5 | 8 | 8 | P5-WA-3 |  |  |  |  |  |  |  | ■ |  |  |
| P6-WA-2 | WA | 6. Decide & Govern | ADR(s) (Workflow A) | FDE-1 | 0.25 | 8 | 8 | P6-WA-1 |  |  |  |  |  |  |  | ■ |  |  |
| P6-WB-1 | WB | 6. Decide & Govern | Privacy/ethics assessment & DI note (Workflow B) | FDE-2 | 0.5 | 8 | 8 | P5-WB-3 |  |  |  |  |  |  |  | ■ |  |  |
| P6-WB-2 | WB | 6. Decide & Govern | ADR(s) (Workflow B) | FDE-2 | 0.25 | 8 | 8 | P6-WB-1 |  |  |  |  |  |  |  | ■ |  |  |
| P6-WC-1 | WC | 6. Decide & Govern | Reliability input & QRM (Workflow C) | FDE-3 | 0.5 | 8 | 8 | P5-WC-3 |  |  |  |  |  |  |  | ■ |  |  |
| P6-WC-2 | WC | 6. Decide & Govern | ADR(s) (Workflow C) | FDE-3 | 0.25 | 8 | 8 | P6-WC-1 |  |  |  |  |  |  |  | ■ |  |  |
| P6-SYNC-1 | SYNC | 6. Decide & Govern | Stage-gate decision record | FDE-5 | 0.5 | 8 | 8 | P6-ARC-1, P6-ARC-2, P6-WA-2, P6-WB-2, P6-WC-2, P6-GOV-2 |  |  |  |  |  |  |  | ◆ |  |  |
| PHASE — 7. Deliver & Evaluate  |  Schedule: see bars → |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| GEMBA-2 | GOV | 7. Deliver & Evaluate | Gemba session notes (Workflow C, driven by FDE-5) | FDE-5 | 0.25 | 9 | 9 | P7-WC-1 |  |  |  |  |  |  |  |  | ■ |  |
| GEMBA-1 | ARC | 7. Deliver & Evaluate | Gemba session notes (Workflow B, driven by FDE-4) | FDE-4 | 0.25 | 9 | 9 | P7-WB-1 |  |  |  |  |  |  |  |  | ■ |  |
| P7-ARC-1 | ARC | 7. Deliver & Evaluate | Integrated app shell with kill switch & continuity | FDE-4 | 0.75 | 9 | 10 | P7-WA-1, P7-WB-1, P7-WC-1 |  |  |  |  |  |  |  |  | ■ |  |
| P7-WA-1 | WA | 7. Deliver & Evaluate | Working Workflow-A module (offline) | FDE-1 | 1 | 9 | 9 | P6-SYNC-1 |  |  |  |  |  |  |  |  | ■ |  |
| P7-WA-2 | WA | 7. Deliver & Evaluate | Machine-readable test results (Workflow A) | FDE-1 | 0.75 | 9 | 10 | P7-WA-1 |  |  |  |  |  |  |  |  | ■ |  |
| P7-WB-1 | WB | 7. Deliver & Evaluate | Working Workflow-B module (offline) | FDE-2 | 1 | 9 | 9 | P6-SYNC-1 |  |  |  |  |  |  |  |  | ■ |  |
| P7-WB-2 | WB | 7. Deliver & Evaluate | Machine-readable test results (Workflow B) | FDE-2 | 0.75 | 9 | 10 | P7-WB-1 |  |  |  |  |  |  |  |  | ■ |  |
| P7-WC-1 | WC | 7. Deliver & Evaluate | Working Workflow-C module (offline) | FDE-3 | 1 | 9 | 9 | P6-SYNC-1 |  |  |  |  |  |  |  |  | ■ |  |
| P7-WC-2 | WC | 7. Deliver & Evaluate | Machine-readable test results (Workflow C) | FDE-3 | 0.75 | 9 | 10 | P7-WC-1 |  |  |  |  |  |  |  |  | ■ |  |
| P7-GOV-1 | GOV | 7. Deliver & Evaluate | Evaluation scorecard | FDE-5 | 0.5 | 10 | 10 | P7-WA-3, P7-WB-3, P7-WC-3 |  |  |  |  |  |  |  |  |  | ■ |
| P7-GOV-2 | GOV | 7. Deliver & Evaluate | Reliability & continuity runbooks | FDE-5 | 0.5 | 10 | 10 | P7-ARC-1 |  |  |  |  |  |  |  |  |  | ■ |
| P7-GOV-3 | GOV | 7. Deliver & Evaluate | Operating model, roadmap & handover pack | FDE-5 | 0.5 | 10 | 10 | P7-GOV-1, P7-GOV-2 |  |  |  |  |  |  |  |  |  | ■ |
| OD-3 | ARC | 7. Deliver & Evaluate | Ontology delta log v4 (final, submission version) | FDE-4 | 0.25 | 10 | 10 | P7-WA-1, P7-WB-1, P7-WC-1 |  |  |  |  |  |  |  |  |  | ■ |
| P7-ARC-2 | ARC | 7. Deliver & Evaluate | Red-team evidence & remediation log | FDE-4 | 0.5 | 10 | 10 | P7-ARC-1 |  |  |  |  |  |  |  |  |  | ■ |
| P7-ARC-3 | ARC | 7. Deliver & Evaluate | FinOps instrumentation & cost evidence | FDE-4 | 0.25 | 10 | 10 | P7-ARC-1 |  |  |  |  |  |  |  |  |  | ■ |
| P7-WA-3 | WA | 7. Deliver & Evaluate | Evaluation results (Workflow A) | FDE-1 | 0.5 | 10 | 10 | P7-WA-2 |  |  |  |  |  |  |  |  |  | ■ |
| P7-WB-3 | WB | 7. Deliver & Evaluate | Evaluation results (Workflow B) | FDE-2 | 0.5 | 10 | 10 | P7-WB-2 |  |  |  |  |  |  |  |  |  | ■ |
| P7-WC-3 | WC | 7. Deliver & Evaluate | Evaluation results (Workflow C) | FDE-3 | 0.5 | 10 | 10 | P7-WC-2 |  |  |  |  |  |  |  |  |  | ■ |
| P7-SYNC-1 | SYNC | 7. Deliver & Evaluate | Submission check pass & clean-room proof | FDE-4 | 0.25 | 10 | 10 | P7-GOV-3, P7-ARC-2, P7-ARC-3 |  |  |  |  |  |  |  |  |  | ◆ |
| P7-SYNC-2 | SYNC | 7. Deliver & Evaluate | Final defence pack & recommendation | FDE-5 | 0.5 | 10 | 10 | P7-SYNC-1 |  |  |  |  |  |  |  |  |  | ◆ |
| How to read this Gantt |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1. Five lanes run in parallel from Day 1; a lane waits on another only at SYNC GATE rows (◆). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2. Walking-skeleton spikes (▲) land on Day 3 so real data informs Architect/Specify — build does not start cold on Day 9. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3. Ontology deltas (OD-1/2/3) appear on Days 5, 7 and 10 — the semantic layer is living, not a one-time freeze. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4. Gemba sessions (GEMBA-1/2) sit inside Day 9 build so ARC/GOV leads get hands-on exposure. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5. Effort column is owner build effort only; peer review is a standing ~45–60 min/day commitment (see Review & Gate Protocol). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6. Source of truth for dependencies and exit criteria remains the WBS sheet; this chart visualizes schedule windows only. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Lane Swimlane Summary (phase coverage by lane) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Lane | Owner | Primary focus | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 | Day 6 | Day 7 | Day 8 | Day 9 | Day 10 |  |  |  |  |  |  |
| GOV | FDE-5 | Product / Value / Governance / Evaluation | ■ | ■ | ■ | ■ | ■ |  | ■ | ■ | ■ | ■ |  |  |  |  |  |  |
| ARC | FDE-4 | Domain, Architecture & Security | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ |  |  |  |  |  |  |
| WA | FDE-1 | Workflow A — GxP Evidence Reconciliation | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ |  |  |  |  |  |  |
| WB | FDE-2 | Workflow B — PV Case Intake | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ |  |  |  |  |  |  |
| WC | FDE-3 | Workflow C — Bounded Supply Planning | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ |  |  |  |  |  |  |
| SYNC | All FDEs | Cross-Lane Sync Gates (joint checkpoints) |  | ■ | ■ | ■ | ■ |  | ■ | ■ |  | ■ |  |  |  |  |  |  |