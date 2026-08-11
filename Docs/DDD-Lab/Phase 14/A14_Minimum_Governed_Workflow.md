# A14 — Minimum Governed Workflow: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## 1. Stage 14 Mission

Stage 14 converts the Stage 13 evaluation suite into a narrow, safe, human-owned, auditable workflow slice for the NovaCura Therapeutics Group evidence-reconciliation case. The purpose is not to solve the case or make batch, quality, safety, regulatory, clinical or supply decisions. The purpose is to define the minimum governed sequence of work across Workflow A (GxP evidence reconciliation for batch-review readiness), Workflow B (PV case-intake and signal-support) and Workflow C (bounded supply-shortage and cold-chain recovery planner) that keeps known risks visible, routes them to the right accountable Quality, Safety, Regulatory, Clinical and Supply roles, blocks unsafe release, disposition, allocation or closure, preserves consent/entitlement/privacy boundaries, keeps the 47-minute audit-capture gap visible, supports AI-off continuity, and creates an evidence trail for every draft, review, decision, approval, rejection, override, release, escalation, action, outcome and closure.

The workflow is intentionally limited to a minimum governed slice so that the workshop team can test whether the domain model, ubiquitous language, bounded contexts, decision ownership, evidence model, audit model and evaluation suite can operate together safely and fail-closed on unresolved state.

---

## 2. Input Summary

The Stage 14 input comes from Stage 13 (Evaluation Suite) via `Docs/DDD-Lab/Phase 14/A14_Input_From_Stage13.md`, drawing on Stage 12 (Evidence and Audit Model) and Stage 11 (Human Decision Ownership Matrix). The evaluation suite established the capability-to-scenario matrix, the scenario register (positive, negative, edge, adversarial, fail-closed), the assertion register, fail-closed behaviour checks, traceability checks, guardrail-compliance checks, metrics and thresholds, and the non-negotiables.

Decision ownership remains with the Chief Quality Officer; EU Qualified Person; Quality release reviewers; laboratory/OOS owners; identity/genealogy/master-data owners; supplier-quality reviewers; PV case-intake staff; PV medical/safety reviewers; signal management; logistics/cold-chain owners; serialisation owners; Supply Chain VP / authorised Quality owner; procurement; Regulatory Affairs; Data Protection Officer; CISO; Biostatistics; and the patient-safety voice, or is explicitly marked role to be assigned.

The non-negotiables carried into the workflow are:

```text
1. The AI never releases, rejects, reprocesses, re-labels or recalls a batch.
2. The AI never makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions.
3. The AI never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval.
4. The AI never changes formulation, specification, clinical eligibility, safety-case disposition, batch release or recall decisions.
5. Regulated accountability remains with the accountable Quality, Safety, Regulatory, Clinical and Supply roles.
6. Evidence output must not be produced while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
7. Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable.
8. The system operates read-only and advisory; it prepares, reconciles, explains and packages evidence.
```

---

## 3. Workflow Principles

```text
Start from the business object (batch, case, shipment, shortage), not from technology.
Keep all known gaps visible until reviewed, approved, escalated, or blocked.
The system prepares, reconciles, explains and packages evidence; it never decides.
Fail-closed on unresolved state: no-answer is a valid output; ambiguity is never treated as completeness.
A later timestamp is not automatically more authoritative than an approved signed record.
Authority is contextual per business object, jurisdiction and effective date.
Regulated accountability remains with accountable human roles.
Every major action must produce evidence and an audit event; the 47-minute audit gap stays visible.
Untrusted sources (MALICIOUS_SUPPLIER_DEVIATION.md, poisoned tool manifests, undocumented spreadsheets) are never authority.
Consent, entitlement and privacy must be checked before patient/participant data use.
Draft outputs stay draft until the accountable human gate is satisfied.
AI-off continuity keeps the workflow safe and auditable without model inference.
No vague status such as handled, cleared, ready or safe without owner, evidence, status and timestamp.
Closure is a governed human decision, not an automatic workflow end.
```

---

## 4. Workflow Overview

The minimum governed workflow is an end-to-end advisory, read-only pipeline that spans all three mandatory workflows. It shares a common intake and identity foundation, workflow-specific evidence reconciliation lanes, human decision points, and a common audit, inspection and continuity layer.

**Common foundation.** The workflow opens with product-batch-case-shipment identity and genealogy resolution. Every lane starts only when identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation and checkpoint state is resolved or explicitly declared no-answer. Untrusted sources are quarantined before any lane uses evidence.

**Workflow A lane (GxP batch-review readiness).** The lane reconciles batch genealogy (including the SUA-88 break), laboratory results and interface units, OOS/OOT states, environmental monitoring and organism corrections, deviation/CAPA/change-control lineage, validation state, supplier-audit evidence and release-packet completeness. It assembles a batch-review readiness package as a draft for Quality release review. The EU QP owns certification and batch disposition as separate human gates; the system never performs either.

**Workflow B lane (PV case-intake and signal-support).** The lane supports intake, duplicate-candidate surfacing, terminology normalisation, reporting-clock reconstruction, listedness evidence retrieval, product-quality linkage and multilingual review. It prepares review material only. PV medical/safety reviewers, signal management and Regulatory Affairs own final determinations; the system never makes final seriousness, causality, expectedness, reportability or signal-confirmation decisions.

**Workflow C lane (supply-shortage and cold-chain recovery).** The lane reconstructs cold-chain logger, pallet and excursion evidence, checks serialisation aggregation state, reconciles excipient-supply and CMO capacity evidence, and generates traceable, policy-bounded allocation options with constraint rationale. Options remain draft until the Supply Chain VP / authorised Quality owner approves. The system never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall.

**Common control layer.** A gate register enforces deterministic gates and human approval gates. An audit-capture lane records every event and keeps the 47-minute audit-capture gap visible. A continuity lane supports at least 14 days of safe operation without model inference, with rollback to the last validated checkpoint and no stale-state duplication. An inspection lane assembles the 72-hour multi-agency evidence package as a manifest with gap ownership and human sign-off.

Where the AI assists, it prepares, reconciles, surfaces, explains and packages evidence. Where deterministic controls apply, they enforce gates that cannot be bypassed. Where human review and authorization apply, the workflow routes to the accountable role and blocks everything else until the human decision is recorded.

---

## 5. Workflow Step Register

### Workflow A — GxP evidence reconciliation for batch-review readiness

#### WS-01 — Product-batch identity and genealogy reconciliation

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-01 / Product-batch identity and genealogy reconciliation |
| Input | `data/batches.csv` (NCB204-B24071), `data/material_genealogy.csv` (SUA-88 missing branch), `data/warehouse_movements.csv` (WM-90), product master |
| Output | Identity-match record and genealogy-break record with ownership and no-answer declaration |
| AI assist scope | Reconcile branches, surface the break, explain source rows |
| Deterministic control | Genealogy-complete gate: no readiness output while the break is unresolved |
| Human review point | Identity / genealogy / master-data owner reviews the break record |
| Human authorization point | Human resolution of the SUA-88 break (never performed by the system) |
| Evidence and audit need | Genealogy-break record, source rows, owner, decision, timestamp |
| Fail-closed default | No batch evidence output while identity or genealogy is unresolved |
| Bounded context | Identity and Genealogy Context |

#### WS-02 — Unit and terminology reconciliation

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-02 / Unit and terminology reconciliation |
| Input | `data/lab_results.csv` (LR-88, mg/L), `data/interface_mappings.csv` (µg/mL assumption), `data/adverse_events.csv`, `data/terminology_versions.csv` (MedDRA 27.1 / 28.0) |
| Output | Unit-conflict record, terminology-version basis record, no-answer declarations |
| AI assist scope | Surface unit and terminology conflicts; explain mapping basis |
| Deterministic control | Unit-resolved and terminology-resolved gates: no silent conversion, no preferred term |
| Human review point | Laboratory / interface owner with Quality; safety coder / terminology owner |
| Human authorization point | Human acceptance of unit conversion; human terminology-version decision |
| Evidence and audit need | Reported unit, assumed unit, mapping, approval state; version-per-event basis |
| Fail-closed default | No output while unit or terminology state is unresolved |
| Bounded context | Unit and Terminology Standardisation Context |

#### WS-03 — OOS/OOT evidence reconciliation and packaging

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-03 / OOS/OOT evidence reconciliation and packaging |
| Input | `data/lab_results.csv`, `data/oos_investigations.csv` (OOS-88 open), statistical tool state, laboratory notebook state |
| Output | Conflicting-state record with the open investigation visible |
| AI assist scope | Reconcile conflicting states without disposition |
| Deterministic control | OOS/OOT disposition gate: disputed result never presumed valid |
| Human review point | Laboratory analyst / OOS owner |
| Human authorization point | Human disposition and investigation conclusion |
| Evidence and audit need | Conflicting states, investigation ID, visibility record |
| Fail-closed default | Disputed result state stays open and visible |
| Bounded context | GxP Batch Evidence Reconciliation Context |

#### WS-04 — Environmental, sterility and lineage evidence reconciliation

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-04 / Environmental, sterility and lineage evidence reconciliation |
| Input | `data/environmental_monitoring.csv` (EM-501), `data/microbiology_results.csv` (corrected organism), `data/deviations.csv`, `data/capa_records.csv`, `data/change_controls.csv`, `data/cleaning_validation.csv`, `data/production_schedule.csv` |
| Output | Excursion and lineage evidence package with both identifications preserved |
| AI assist scope | Prepare excursion and lineage evidence; link CAPA and change-control lineage |
| Deterministic control | Excursion and lineage gates: excursions never hidden or dismissed |
| Human review point | Quality / Manufacturing owner |
| Human authorization point | Human excursion disposition; human deviation/CAPA/change-control closure |
| Evidence and audit need | Excursion record, correction rationale, lineage links, closure status |
| Fail-closed default | Excursion not hidden or dismissed; lineage not treated as resolved without evidence |
| Bounded context | GxP Batch Evidence Reconciliation Context |

#### WS-05 — Supplier-audit verification state check

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-05 / Supplier-audit verification state check |
| Input | `data/supplier_audits.csv` (AUD-2025-14, vendor_claims_closed_unverified), `data/release_packets.csv` |
| Output | Verification-state record; commitment remains open until verified |
| AI assist scope | Present verification state; never treat unverified as closed |
| Deterministic control | Supplier-verification gate: packet cannot pass while commitment unverified |
| Human review point | Supplier-quality / quality reviewer |
| Human authorization point | Human verification and commitment closure |
| Evidence and audit need | Verification request/state, packet status, owner, timestamp |
| Fail-closed default | Unverified commitment never treated as closed |
| Bounded context | Supplier and Audit Evidence Context |

#### WS-06 — Release-packet completeness check

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-06 / Release-packet completeness check |
| Input | `data/release_packets.csv`, `data/supplier_audits.csv`, `data/certificates_analysis.csv`, `data/batches.csv` |
| Output | Element-status list with gap ownership and pending QP status |
| AI assist scope | List packet elements and evidence gaps |
| Deterministic control | Release-packet-complete gate: incomplete or unverified elements block readiness |
| Human review point | Quality release reviewer |
| Human authorization point | Human acceptance of packet completeness |
| Evidence and audit need | Element checklist, gap ownership, reviewer, timestamp |
| Fail-closed default | Batch not shown release-ready with unresolved or unverified elements |
| Bounded context | GxP Batch Evidence Reconciliation Context |

#### WS-07 — Batch-review readiness package creation

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-07 / Batch-review readiness package creation |
| Input | Cited rows from WS-01 to WS-06 plus validation and checkpoint state |
| Output | Batch-review readiness package, status draft, pending QP status |
| AI assist scope | Assemble, cite and explain the readiness package |
| Deterministic control | Readiness gates: no readiness completion while any element is unresolved |
| Human review point | Quality release reviewer |
| Human authorization point | Human readiness-review closure (before the QP gate) |
| Evidence and audit need | Package version, cited rows, gap list, owner, status |
| Fail-closed default | Package stays draft until Quality/QP review |
| Bounded context | GxP Batch Evidence Reconciliation Context |

#### WS-08 — QP review handoff (human authorization)

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-08 / QP review handoff |
| Input | Batch-review readiness package with all cited rows |
| Output | Certification evidence package routed to EU QP; QP pending status |
| AI assist scope | Package certification evidence only |
| Deterministic control | QP certification gate and batch disposition gate |
| Human review point | EU QP / Quality release reviewer |
| Human authorization point | Human QP certification; human batch release/reject/reprocess/re-label/recall decision |
| Evidence and audit need | Certification decision, evidence package link, QP identity, timestamp; disposition record |
| Fail-closed default | No certification or disposition with unresolved genealogy, unit, OOS/OOT, supplier or packet state |
| Bounded context | GxP Batch Evidence Reconciliation Context |

### Workflow B — PV case-intake and signal-support

#### WS-09 — ICSR intake and routing

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-09 / ICSR intake and routing |
| Input | `data/icsr_cases.csv` (PV-1001/1009/1014), `data/safety_receipts.csv`, `data/consents.csv`, `data/users_entitlements.csv`, `data/sensitive_segments.csv` |
| Output | Intake material with source attribution, consent/entitlement check and routing |
| AI assist scope | Prepare intake material; attribute sources |
| Deterministic control | Consent/entitlement gate: no patient/participant data without valid check |
| Human review point | PV case-intake staff |
| Human authorization point | Human routing confirmation |
| Evidence and audit need | Receipts, source attribution, check result, routing, reviewer |
| Fail-closed default | Intake blocked while identity, consent/entitlement or checkpoint state is unresolved |
| Bounded context | PV Case Intake and Signal Support Context |

#### WS-10 — Duplicate-candidate surfacing

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-10 / Duplicate-candidate surfacing |
| Input | `data/duplicate_candidates.csv`, `data/icsr_cases.csv` (product names) |
| Output | Candidate list with similarity rationale; candidate-only status |
| AI assist scope | Detect and rank candidates |
| Deterministic control | Duplicate-candidate gate: candidates never auto-confirmed or merged |
| Human review point | PV reviewer |
| Human authorization point | Human duplicate confirmation |
| Evidence and audit need | Candidate pairs, similarity rationale, product-name evidence, reviewer |
| Fail-closed default | Candidates only; no confirmation without human review |
| Bounded context | PV Case Intake and Signal Support Context |

#### WS-11 — Awareness-date (reporting-clock) reconstruction

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-11 / Awareness-date reconstruction |
| Input | `data/safety_receipts.csv` (vendor / affiliate_inbox / global_db), `data/icsr_cases.csv` |
| Output | Clock-reconstruction evidence with dispute record; no accepted date |
| AI assist scope | Reconstruct the clock as evidence only |
| Deterministic control | Reporting-clock gate: clock never set by support |
| Human review point | PV case-intake staff / PV reviewer |
| Human authorization point | Human acceptance of the awareness date |
| Evidence and audit need | Receipt sources, times, clock basis, dispute record |
| Fail-closed default | Clock not set; disputed inputs trigger escalation |
| Bounded context | PV Case Intake and Signal Support Context |

#### WS-12 — Terminology (MedDRA) version reconciliation

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-12 / Terminology version reconciliation |
| Input | `data/adverse_events.csv` (meddra_version), `data/terminology_versions.csv` (27.1 / 28.0) |
| Output | Version-per-event evidence; no preferred term |
| AI assist scope | Present version-mismatch evidence |
| Deterministic control | Terminology-resolved gate: no preferred term while basis inconsistent |
| Human review point | Safety coder / terminology owner |
| Human authorization point | Human terminology-version decision |
| Evidence and audit need | Version-alignment evidence, chosen basis, owner, timestamp |
| Fail-closed default | No terminology output while version state is unresolved |
| Bounded context | Unit and Terminology Standardisation Context |

#### WS-13 — Listedness evidence retrieval and comparison

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-13 / Listedness evidence retrieval and comparison |
| Input | `data/listedness_sources.csv` (IB v12, CCDS v4, IN local label), `data/product_labels.csv` |
| Output | Listedness-source comparison per jurisdiction and version; no winner |
| AI assist scope | Retrieve and compare listedness sources |
| Deterministic control | Listedness gate: no expectedness assertion while conflict unresolved |
| Human review point | PV medical reviewer / Regulatory Affairs |
| Human authorization point | Human listedness determination per jurisdiction |
| Evidence and audit need | Source versions, jurisdiction basis, citation |
| Fail-closed default | No winner picked; conflict visible |
| Bounded context | PV Case Intake and Signal Support Context; Regulatory |

#### WS-14 — PV medical review handoff (human authorization)

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-14 / PV medical review handoff |
| Input | Intake material, candidate list, clock evidence, terminology evidence, listedness evidence, linkage evidence |
| Output | Case-review material routed to PV medical/safety reviewer; no disposition |
| AI assist scope | Prepare case-review material |
| Deterministic control | PV final-determination gate and signal-confirmation gate |
| Human review point | PV medical/safety reviewer; signal management |
| Human authorization point | Human seriousness/causality/expectedness/reportability determinations; signal confirmation |
| Evidence and audit need | Determination record, reviewer, evidence links, reason, timestamp |
| Fail-closed default | No final determinations by support role |
| Bounded context | PV Case Intake and Signal Support Context |

#### WS-15 — Signal-support material preparation

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-15 / Signal-support material preparation |
| Input | `data/signal_metrics.csv` (ROR/EBGM bases), `data/exposure_estimates.csv` (sales vs infusion-registry), `data/product_complaints.csv` |
| Output | Signal-review material citing method and exposure basis |
| AI assist scope | Assemble signal-review material; explain metric basis |
| Deterministic control | Signal gate: metrics never confirmed by support |
| Human review point | Signal management / biostatistics |
| Human authorization point | Human signal confirmation |
| Evidence and audit need | Metric method, exposure basis, decision, owner, timestamp |
| Fail-closed default | No signal confirmation without human review |
| Bounded context | PV Case Intake and Signal Support Context |

### Workflow C — Supply-shortage and cold-chain recovery

#### WS-16 — Cold-chain evidence reconstruction

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-16 / Cold-chain evidence reconstruction |
| Input | `data/temperature_loggers.csv` (LG-31), `data/shipments.csv` (SH-901) |
| Output | Logger, pallet and excursion evidence with the dispute preserved |
| AI assist scope | Reconstruct logger, pallet and excursion evidence |
| Deterministic control | Cold-chain evidence gate: options not trusted while evidence unresolved |
| Human review point | Logistics / cold-chain accountable owner with Quality input |
| Human authorization point | Human cold-chain excursion disposition |
| Evidence and audit need | Logger basis, pallet link, aggregation state, excursion record |
| Fail-closed default | Options not trusted while cold-chain evidence is unresolved |
| Bounded context | Supply, Cold-Chain and Allocation Planning Context |

#### WS-17 — Serialisation aggregation state check

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-17 / Serialisation aggregation state check |
| Input | `data/serialisation_events.csv`, `data/packaging_events.csv` (line restart) |
| Output | Aggregation-state record; gap surfaced, no assumed link |
| AI assist scope | Surface missing aggregation state |
| Deterministic control | Aggregation-state gate: no assumed case-to-pallet link |
| Human review point | Serialisation owner |
| Human authorization point | Human aggregation resolution |
| Evidence and audit need | Aggregation-state record, line-restart evidence, ownership |
| Fail-closed default | Aggregation gap preserved and visible |
| Bounded context | Supply, Cold-Chain and Allocation Planning Context |

#### WS-18 — Shortage and capacity evidence reconciliation

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-18 / Shortage and capacity evidence reconciliation |
| Input | `data/supplier_risks.csv` (8-week recovery), `data/cmo_capacity.csv` (dual-sponsor promise), `data/vendor_contracts.csv`, `data/inventory.csv` |
| Output | Shortage, capacity-conflict and risk evidence; recovery estimate preserved as estimate |
| AI assist scope | Reconcile shortage, capacity and risk evidence |
| Deterministic control | Capacity and shortage gates: no reservation implied |
| Human review point | Procurement / CMO quality / Supply Chain planner |
| Human authorization point | Human excipient-supply continuity and CMO capacity decisions |
| Evidence and audit need | Capacity-conflict record, contract basis, risk evidence, decision, owner |
| Fail-closed default | Capacity conflict preserved; no reservation |
| Bounded context | Supply, Cold-Chain and Allocation Planning Context |

#### WS-19 — Allocation option preparation

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-19 / Allocation option preparation |
| Input | `data/inventory.csv`, `data/demand_forecast.csv`, `data/allocation_constraints.csv`, cold-chain evidence, capacity and risk evidence |
| Output | Traceable option set with constraint rationale; status draft |
| AI assist scope | Generate policy-bounded options with evidence citations |
| Deterministic control | Allocation constraint gate: hard constraints never presented as executable |
| Human review point | Supply planner / authorised Quality owner |
| Human authorization point | Human allocation recommendation sign-off |
| Evidence and audit need | Option rationale, evidence rows, constraint checks, status |
| Fail-closed default | Options stay draft until explicit authorised human approval |
| Bounded context | Supply, Cold-Chain and Allocation Planning Context |

#### WS-20 — Human allocation approval (authorization)

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-20 / Human allocation approval |
| Input | Approved option set with constraint rationale and approval request |
| Output | Approval record linking human approval to the option and any execution action |
| AI assist scope | Prepare approval request and evidence summary only |
| Deterministic control | Allocation approval gate, shipment/inventory-status gate, recall gate |
| Human review point | Supply Chain VP / authorised Quality owner |
| Human authorization point | Explicit human approval for allocation, reservation, shipment or inventory-status change |
| Evidence and audit need | Approval request, human approval, action record, reason, timestamp |
| Fail-closed default | No allocation, reservation, shipment or recall without explicit authorised human approval |
| Bounded context | Supply, Cold-Chain and Allocation Planning Context |

### Cross-cutting

#### WS-21 — Consent, entitlement, validation and checkpoint gate check

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-21 / Consent, entitlement, validation and checkpoint gate check |
| Input | `data/consents.csv`, `data/users_entitlements.csv`, `data/validation_inventory.csv`, `data/ebr_steps.csv`, `data/access_cache.csv` |
| Output | Check records; no-answer declarations where state is unresolved |
| AI assist scope | Record check status only |
| Deterministic control | Consent/entitlement gate, validation-state gate, checkpoint-state gate |
| Human review point | Data Protection Officer / privacy owner; validation / Quality owner; identity owner |
| Human authorization point | Human exception decisions for consent/entitlement boundaries |
| Evidence and audit need | Check type, result, actor, purpose, exception, timestamp |
| Fail-closed default | No patient/participant data use or evidence output while required state is unresolved |
| Bounded context | Consent, Entitlement and Privacy Context; Validation and Checkpoint Context |

#### WS-22 — Inspection evidence packaging (72-hour)

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-22 / Inspection evidence packaging |
| Input | Cited rows from Workflows A, B, C plus `data/audit_trails.csv`, `data/tool_catalog.csv`, `data/model_registry.csv`, `data/users_entitlements.csv` |
| Output | Package manifest with source citations, gap ownership and sign-off routing |
| AI assist scope | Assemble package and manifest |
| Deterministic control | Inspection packaging gate: package not complete while gaps or the 47-minute audit gap are unresolved |
| Human review point | Regulatory / Quality participant |
| Human authorization point | Human manifest sign-off; accountable Regulatory/Quality approval for response |
| Evidence and audit need | Package manifest, source citations, gap ownership, sign-off |
| Fail-closed default | Package not presented complete while evidence or audit gaps are unresolved |
| Bounded context | Audit, Evidence and Continuity Context |

#### WS-23 — Audit capture and evidence linkage

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-23 / Audit capture and evidence linkage |
| Input | Every draft, recommendation, approval, override, release, escalation, action, outcome and closure |
| Output | Linked audit events with trigger, bounded context, role, fields, retention/immutability need |
| AI assist scope | Record event envelopes; link evidence |
| Deterministic control | Audit-capture gate: no action without an audit event; the 47-minute gap never filled |
| Human review point | Audit / quality oversight |
| Human authorization point | Human confirmation of audit completeness before closure |
| Evidence and audit need | Event, trigger, actor, owner, evidence, status, timestamp; gap record |
| Fail-closed default | The 47-minute gap remains visible; nothing is treated as auditable across it |
| Bounded context | Audit, Evidence and Continuity Context |

#### WS-24 — AI-off continuity mode

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-24 / AI-off continuity mode |
| Input | `data/continuity_requirements.csv`, `data/downtime_events.csv`, `data/model_endpoints.csv`, manual runbooks |
| Output | Continuity-state record; workflow continues safely without model inference |
| AI assist scope | None while AI-off; state surfaced for human operation |
| Deterministic control | Deterministic gates remain fully operable offline |
| Human review point | CISO / continuity owner; accountable workflow owners |
| Human authorization point | Human continuation of decisions under AI-off mode |
| Evidence and audit need | Continuity state, downtime timeline, runbook usage, no-inference declaration |
| Fail-closed default | No AI-dependent assertion; safe operation for at least 14 days without inference |
| Bounded context | Audit, Evidence and Continuity Context |

#### WS-25 — Escalation, override and closure

| Field | Workflow Definition |
|---|---|
| Step ID / name | WS-25 / Escalation, override and closure |
| Input | Escalation trigger, blocked gate, source evidence, closure request |
| Output | Escalation record with action and outcome; override record with authorized owner and reason; closure record |
| AI assist scope | Surface closure checklists and escalation summaries |
| Deterministic control | Escalation gate, override gate, closure gate |
| Human review point | Accountable workflow owner plus relevant decision owner |
| Human authorization point | Human escalation closure; human override approval; human closure decision |
| Evidence and audit need | Trigger, evidence, owner, action, outcome, reason, downstream impact, timestamp |
| Fail-closed default | Escalation cannot close without action/outcome; override without owner/reason; closure while gaps are hidden or unaudited |
| Bounded context | All workflow contexts |

---

## 6. Control and Gate Register

| Gate ID | Gate Name | Trigger | Requirement to Pass | Fail-Closed Default | Accountable Role | Bounded Context |
|---|---|---|---|---|---|---|
| G-01 | Genealogy-complete gate | Batch-review lane opens on NCB204-B24071 | SUA-88 branch resolved or no-answer declared with ownership | No batch evidence output while genealogy unresolved | Identity / genealogy / master-data owner | Identity and Genealogy |
| G-02 | Unit-resolved gate | Unit conflict (mg/L vs µg/mL) detected | Conversion accepted by human with Quality or no-answer declared | No silent conversion; no output while unit unresolved | Laboratory / interface owner with Quality | Unit and Terminology |
| G-03 | OOS/OOT disposition gate | OOS/OOT/notebook states disagree | Human disposition recorded or investigation left open visibly | Disputed result stays open | Laboratory analyst / OOS owner | GxP Batch Evidence |
| G-04 | Excursion disposition gate | Sterile-area or environmental excursion | Human disposition recorded | Excursion never hidden or dismissed | Quality / Manufacturing owner | GxP Batch Evidence |
| G-05 | Supplier-verification gate | Audit commitment claimed closed but unverified | Verification confirmed or declared open | Unverified never treated as closed | Supplier-quality / quality reviewer | Supplier and Audit Evidence |
| G-06 | Release-packet-complete gate | Release packet assessed | All elements resolved and verified | Batch not shown release-ready with unresolved elements | Quality release reviewer | GxP Batch Evidence |
| G-07 | QP certification gate | Readiness package ready | EU QP certification recorded | No certification with unresolved state | EU Qualified Person | GxP Batch Evidence |
| G-08 | Batch disposition gate | Release/reject/reprocess/re-label/recall considered | Explicit human approval recorded | No disposition by support role | EU QP / Quality release reviewer; Quality/Regulatory for recall | GxP Batch Evidence / Quality |
| G-09 | Consent/entitlement gate | Patient/participant data accessed or used | Valid check or authorized exception recorded | No data use without lawful basis | Data Protection Officer / privacy owner | Consent, Entitlement and Privacy |
| G-10 | Authority/effective-date gate | Multiple versions or authorities conflict | Authority and effective date per jurisdiction established | Later timestamp never automatically authoritative | Accountable document/version owner per domain | Identity and Genealogy / Regulatory |
| G-11 | Checkpoint-state gate | Back-entered EBR step or corrupted state | Checkpoint state resolved or no-answer declared | No contemporaneous claim; no stale-state use | Manufacturing / Quality reviewer; continuity owner | Validation and Checkpoint |
| G-12 | Validation-state gate | Validation state ambiguous | State resolved or source quarantined | No output from ambiguous or unvalidated source | Validation / Quality owner | Validation and Checkpoint |
| G-13 | Duplicate-candidate gate | Duplicate candidates surfaced | Human confirmation or candidate status retained | Candidates only; no confirmation without review | PV reviewer | PV Case Intake and Signal Support |
| G-14 | Reporting-clock gate | Awareness date disputed | Human acceptance or escalation recorded | Clock never set by support | PV case-intake staff / PV reviewer | PV Case Intake and Signal Support |
| G-15 | Terminology gate | MedDRA version mismatch | Human version-basis decision recorded | No preferred term chosen | Safety coder / terminology owner | Unit and Terminology |
| G-16 | Listedness gate | IB/CCDS/label conflict | Human listedness determination per jurisdiction | No winner picked | PV medical reviewer / Regulatory Affairs | PV Case Intake and Signal Support; Regulatory |
| G-17 | PV final-determination gate | Final seriousness/causality/expectedness/reportability | Human determination recorded | No final determination by support role | PV medical/safety reviewer | PV Case Intake and Signal Support |
| G-18 | Signal-confirmation gate | Signal metrics assessed | Human signal confirmation | No confirmation without review | Signal management | PV Case Intake and Signal Support |
| G-19 | Cold-chain evidence gate | Logger/pallet/excursion dispute | Evidence reconstructed or disposition recorded | Options not trusted while unresolved | Logistics / cold-chain owner with Quality | Supply, Cold-Chain and Allocation |
| G-20 | Aggregation-state gate | Aggregation gap after line restart | Gap resolved or surfaced with ownership | No assumed link | Serialisation owner | Supply, Cold-Chain and Allocation |
| G-21 | Allocation approval gate | Allocation option proposed | Explicit authorised human approval | No allocation/reservation without approval | Supply Chain VP / authorised Quality owner | Supply, Cold-Chain and Allocation |
| G-22 | Shipment/inventory-status gate | Shipment or status change considered | Explicit human approval and resolved cold-chain evidence | No shipment/status change without approval | Supply Chain / logistics accountable owner | Supply, Cold-Chain and Allocation |
| G-23 | Recall consideration gate | Recall candidates surfaced | Human consideration decision recorded | No recall initiated by support | Quality / Regulatory accountable roles | Quality / Regulatory |
| G-24 | Escalation gate | Unresolved state or blocker | Action and outcome recorded | Escalation cannot close without outcome | Accountable workflow owner | All contexts |
| G-25 | Override gate | Authorized deviation requested | Authorized owner, reason, evidence, timestamp | No silent or unowned override | Authorized owner for the decision | All contexts |
| G-26 | Audit-capture gate | Audit event required | Event recorded; 47-minute gap visible | Gap never filled; nothing auditable across it | Audit / quality oversight | Audit, Evidence and Continuity |
| G-27 | Inspection packaging gate | 72-hour multi-agency request | Manifest with citations and gap ownership signed off | Package not complete while gaps unresolved | Regulatory / Quality participant | Audit, Evidence and Continuity |
| G-28 | Closure gate | Case/escalation closure requested | Evidence completeness, approvals, escalation outcomes, visible gaps, human closure decision | Closure blocked while gaps hidden or unaudited | Accountable workflow owner | All contexts |

---

## 7. AI Assist vs Deterministic vs Human Responsibility Map

| Step | AI Assist (prepare/reconcile/surface/explain/package) | Deterministic Control | Human Responsibility |
|---|---|---|---|
| WS-01 Identity/genealogy | Reconcile branches; surface the break | Genealogy-complete gate (G-01) | Resolve the SUA-88 break |
| WS-02 Unit/terminology | Surface conflicts; explain basis | Unit/terminology gates (G-02, G-15) | Accept conversion; decide version basis |
| WS-03 OOS/OOT packaging | Reconcile conflicting states | OOS/OOT gate (G-03) | Dispose result; conclude investigation |
| WS-04 Excursion/lineage | Prepare excursion and lineage evidence | Excursion gate (G-04) | Dispose excursion; close deviation/CAPA/change |
| WS-05 Supplier verification | Present verification state | Supplier gate (G-05) | Verify and close commitment |
| WS-06 Release-packet check | List elements and gaps | Release-packet gate (G-06) | Accept packet completeness |
| WS-07 Readiness package | Assemble and cite | Readiness gates | Review readiness closure |
| WS-08 QP handoff | Package certification evidence | QP and disposition gates (G-07, G-08) | Certify; release/reject/reprocess/re-label/recall |
| WS-09 ICSR intake | Prepare intake material | Consent/entitlement gate (G-09) | Confirm routing |
| WS-10 Duplicate candidates | Detect candidates | Duplicate gate (G-13) | Confirm duplicates |
| WS-11 Awareness date | Reconstruct clock evidence | Reporting-clock gate (G-14) | Accept awareness date |
| WS-12 Terminology | Present version evidence | Terminology gate (G-15) | Decide version basis |
| WS-13 Listedness | Compare sources | Listedness gate (G-16) | Determine listedness per jurisdiction |
| WS-14 PV review handoff | Prepare case-review material | PV determination gate (G-17) | Make final determinations |
| WS-15 Signal support | Assemble signal material | Signal gate (G-18) | Confirm signal |
| WS-16 Cold-chain evidence | Reconstruct logger/pallet/excursion | Cold-chain gate (G-19) | Dispose excursion |
| WS-17 Aggregation | Surface gap | Aggregation gate (G-20) | Resolve aggregation state |
| WS-18 Shortage/capacity | Reconcile evidence | Capacity/shortage gates | Decide continuity and capacity |
| WS-19 Allocation options | Generate traceable options | Constraint gate (G-21) | Sign off recommendation |
| WS-20 Allocation approval | Prepare approval request | Allocation/shipment gates (G-21, G-22) | Approve allocation; decide shipment/status |
| WS-21 Boundary checks | Record check status | Consent/validation/checkpoint gates (G-09, G-11, G-12) | Decide exceptions |
| WS-22 Inspection packaging | Assemble manifest | Inspection gate (G-27) | Sign manifest; own response |
| WS-23 Audit capture | Record and link events | Audit gate (G-26) | Confirm audit completeness |
| WS-24 AI-off continuity | None while AI-off | Deterministic gates stay operable | Continue decisions manually |
| WS-25 Escalation/override/closure | Surface checklists | Escalation/override/closure gates (G-24, G-25, G-28) | Close, override or approve |

---

## 8. Read-Only Boundary Declaration

```text
The advisory system NEVER:
- releases, rejects, reprocesses, re-labels or recalls a batch
- makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions
- confirms duplicate ICSRs or merges cases
- sets the reporting clock or accepts the awareness date
- picks a preferred term, listedness winner or version basis
- disposes OOS/OOT results, environmental excursions or cold-chain excursions
- resolves the SUA-88 genealogy break or applies the mg/L vs µg/mL conversion
- closes a supplier-audit commitment without human verification
- changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall
- changes formulation, specification, clinical eligibility or safety-case disposition
- overrides consent, entitlement or privacy boundaries
- authorizes overrides without authorized owner and reason
- closes cases or escalations without documented human outcome
- fills or hides the 47-minute audit-capture gap
- treats untrusted sources (MALICIOUS_SUPPLIER_DEVIATION.md, poisoned tool manifests, undocumented spreadsheets) as authority

The advisory system ONLY:
- prepares, reconciles, explains and packages evidence
- surfaces gaps, conflicts and evidence lineage with attribution
- issues no-answer declarations when required state is unresolved
- compiles drafts (readiness packages, review material, option sets, package manifests)
- records audit events and keeps the 47-minute gap visible
- routes decisions to the accountable human role
```

---

## 9. Human Decision Points

The following human decision points must never be bypassed:

```text
EU QP certification of batch NCB204-B24071.
Batch release / rejection / reprocess / re-label / recall decisions.
Batch-review readiness closure by the Quality release reviewer.
OOS/OOT disposition and investigation conclusion by the laboratory analyst / OOS owner.
Unit-conversion acceptance (mg/L vs µg/mL) by the laboratory / interface owner with Quality acceptance.
SUA-88 genealogy-break resolution by the identity / genealogy / master-data owner.
Environmental-excursion disposition by the Quality / Manufacturing owner.
Supplier-audit commitment verification and closure by the supplier-quality / quality reviewer.
Deviation / CAPA / change-control closure by the Quality / Manufacturing owner.
Final PV seriousness, causality, expectedness, reportability determinations by the PV medical/safety reviewer.
Signal confirmation by signal management.
Duplicate-ICSR confirmation by the PV reviewer.
Awareness-date acceptance by the PV case-intake staff / PV reviewer.
MedDRA terminology decisions by the safety coder / terminology owner.
Listedness determination per jurisdiction by the PV medical reviewer / Regulatory Affairs.
Cold-chain excursion disposition by the logistics / cold-chain accountable owner with Quality input.
Serialisation aggregation resolution by the serialisation owner.
Excipient-supply continuity and CMO capacity decisions by procurement / Supply planner with Supply Chain VP accountability.
Allocation recommendation sign-off and allocation approval by the Supply Chain VP / authorised Quality owner.
Shipment and inventory-status decisions by the Supply Chain / logistics accountable owner.
Recall consideration by Quality / Regulatory accountable roles.
Consent, entitlement, privacy and access-exception decisions by the Data Protection Officer / privacy owner.
Inspection-evidence package sign-off and response by Regulatory / Quality accountable roles.
Override approval by the authorized owner for the decision, with reason.
Escalation and case closure by the accountable workflow owner, only when outcomes are recorded and gaps are visible.
```

---

## 10. Evidence and Audit Trail

Each workflow run must produce the following evidence and audit trail:

```text
Product / batch / case / shipment identity and genealogy match evidence.
Source system, file path, row and record references for every cited claim.
Reported unit and terminology version basis.
Authority reference, effective date and jurisdiction.
Event time and clock basis.
Consent / entitlement / privacy check records.
Validation state and checkpoint state.
Record and output version.
Human owner for each decision; human reviewer for each draft or recommendation.
Review, approval and rejection status.
Override reason where applicable.
Escalation trigger and owner; action and outcome.
Readiness package with draft status and QP pending status.
PV review material with candidate and conflict status.
Allocation options with draft status and approval links.
Recall consideration records.
Inspection evidence package manifest with gap ownership and sign-off.
The 47-minute audit-capture gap record, never filled.
AI-off continuity state.
Closure evidence.
```

Every draft, recommendation, approval, override, release, escalation, action, outcome and closure is linked to its evidence rows and named human owners, and every event is recorded in `data/audit_trails.csv` with trigger, bounded context, accountable role, audit fields and retention/immutability need.

---

## 11. Rollback and AI-Off Behaviour

```text
AI-off continuity: the workflow must operate safely for at least 14 days without model inference.
- Deterministic gates (G-01, G-02, G-05, G-06, G-09, G-11, G-12, G-13, G-26) remain fully operable offline.
- No AI-dependent assertion is produced; no-answer declarations substitute for model output.
- Manual runbooks cover intake, reconciliation checklists, packaging and audit capture.
- Continuity state is visible in every run during the outage.

Rollback:
- Rollback to the last validated checkpoint when state is corrupted (checkpoint corruption, duplicate draft reservations).
- Duplicate or stale draft state is detected and never converted into reservations, allocations or approvals.
- Rolled-back runs are recorded with reason and timestamp; downstream outputs are regenerated only from the validated checkpoint.

The 47-minute audit-capture gap:
- Never filled or hidden during any run, including during master-data repair.
- Runs spanning the gap carry a visible gap record and are never presented as fully auditable.
```

---

## 12. Anti-Patterns to Avoid

```text
AI deciding batch release, rejection, reprocess, re-label or recall.
AI making final PV determinations or confirming signals.
AI confirming duplicate ICSRs, setting the reporting clock, or picking a listedness winner or preferred term.
AI allocating stock, reserving capacity, changing inventory status or shipping product.
AI treating ambiguity as completeness (unapproved unit, unverified commitment, open investigation, disputed clock, missing aggregation).
AI ignoring untrusted-data warnings (prompt-injection PDF, poisoned tool manifest, undocumented spreadsheets).
AI overriding audit, filling the 47-minute gap, or claiming auditability across it.
Hallucinated or unverifiable evidence citations.
Automation bias in batch review where reviewer divergence is hidden.
Language inequity in multilingual review where reduced coverage is normalised.
Role conflict where the support role is treated as the accountable owner.
Economy or price-shock pressure eroding safety gates.
Closure without evidence completeness, approval trail, escalation outcomes and visible gaps.
```

---

## 13. Boundary Warnings

- Do not confuse readiness evidence with certification; the readiness package is a draft for Quality/QP review, never QP certification or release.
- Do not treat any single system (LIMS, MES, safety DB, RIM, ERP) as universally authoritative; authority is per business object, jurisdiction and effective date.
- Do not convert mg/L to µg/mL, choose a MedDRA preferred term, set the reporting clock, confirm duplicates or pick a listedness winner in the workflow.
- Do not disposition OOS/OOT results, environmental excursions or cold-chain excursions.
- Do not treat option drafts or constraint checks as executed allocation, reservation, shipment or recall.
- Do not mark a release packet, readiness package or inspection evidence package complete while any element is unresolved, unverified or hidden.
- Do not surface patient/participant data without consent/entitlement checks.
- Do not fill or hide the 47-minute audit-capture gap.
- Do not treat the untrusted supplier deviation or poisoned tool manifests as authority.
- Do not let workflow design substitute for human decision ownership; every output remains owned by the accountable human role.
- Do not resolve the case; unresolved gaps are represented with ownership only.
- Do not bypass AI-off continuity planning because the workflow is advisory.

---

## 14. Stage 14 Quality Gate

Before Stage 14 is accepted, confirm:

```text
[ ] The workflow has a narrow and explicit scope covering all three advisory workflows.
[ ] The workflow overview shows where AI assists (prepare/reconcile/surface/explain/package) and where deterministic controls and human review/authorization take over.
[ ] Every step in the step register carries step ID, name, input, output, AI assist scope, deterministic control, human review point, human authorization point, evidence and audit need, fail-closed default and bounded context.
[ ] Steps include identity/genealogy intake, unit/terminology reconciliation, release-packet completeness, supplier verification, OOS/OOT packaging, QP handoff, ICSR intake, duplicate surfacing, awareness-date reconstruction, listedness retrieval, PV review handoff, cold-chain reconstruction, allocation preparation, human allocation approval, inspection packaging, audit capture and AI-off continuity.
[ ] Every control and gate carries trigger, requirement to pass, fail-closed default, accountable role and bounded context.
[ ] Deterministic gates (genealogy-complete, unit-resolved, entitlement/consent, authority/effective-date, checkpoint-state, release-packet-complete) are explicit.
[ ] Human approval gates (QP certification, PV dispositions, allocation, recall, override, closure) are explicit and never bypassed.
[ ] The read-only boundary declaration is explicit: the system never releases, rejects, reprocesses, re-labels, recalls, changes inventory status, reserves capacity, allocates stock, ships or changes formulation/spec/eligibility/disposition.
[ ] Human decision points that must never be bypassed are listed.
[ ] Every run produces the evidence and audit trail with the Stage 12 traceability dimensions; the 47-minute audit gap remains visible.
[ ] AI-off continuity supports at least 14 days of safe operation without model inference; rollback to the last validated checkpoint is defined with no stale-state duplication.
[ ] Anti-patterns are explicit and rejected.
[ ] Non-negotiables are preserved verbatim.
[ ] No new product, batch, safety, quality, regulatory, clinical or supply facts are added.
[ ] No medical, regulatory or legal advice is provided.
[ ] Open questions are documented for the final synthesis.
```

---

## 15. NEXT_STAGE_INPUT_BLOCK

```text
Final Synthesis Input — Minimum Governed Workflow

Source Stage:
Stage 14 — Minimum Governed Workflow

Workflow Overview:
- Common foundation: product-batch-case-shipment identity and genealogy resolution; all lanes start only when required state is resolved or declared no-answer.
- Workflow A lane: reconciles genealogy, lab, interface, OOS/OOT, environmental, lineage, validation, supplier and release-packet evidence; assembles batch-review readiness packages as drafts for Quality/QP review.
- Workflow B lane: supports PV intake, duplicate-candidate surfacing, terminology normalisation, reporting-clock reconstruction, listedness evidence, product-quality linkage and multilingual review; prepares review material only.
- Workflow C lane: reconstructs cold-chain evidence, checks aggregation state, reconciles shortage and capacity evidence, and generates traceable policy-bounded allocation options; options stay draft until explicit authorised human approval.
- Common control layer: deterministic gates, human approval gates, audit capture with the 47-minute gap visible, AI-off continuity, and 72-hour inspection packaging.

Step Register Summary:
- WS-01 identity/genealogy reconciliation; WS-02 unit/terminology; WS-03 OOS/OOT packaging; WS-04 excursion/lineage; WS-05 supplier verification; WS-06 release-packet completeness; WS-07 readiness package; WS-08 QP handoff (human); WS-09 ICSR intake; WS-10 duplicate candidates; WS-11 awareness-date reconstruction; WS-12 terminology; WS-13 listedness; WS-14 PV medical review handoff (human); WS-15 signal support; WS-16 cold-chain reconstruction; WS-17 aggregation state; WS-18 shortage/capacity; WS-19 allocation option preparation; WS-20 human allocation approval; WS-21 boundary checks; WS-22 inspection packaging; WS-23 audit capture; WS-24 AI-off continuity; WS-25 escalation/override/closure.

Control and Gate Register Summary:
- Deterministic gates: genealogy-complete (G-01), unit-resolved (G-02), OOS/OOT (G-03), excursion (G-04), supplier-verification (G-05), release-packet-complete (G-06), consent/entitlement (G-09), authority/effective-date (G-10), checkpoint-state (G-11), validation-state (G-12), duplicate-candidate (G-13), reporting-clock (G-14), terminology (G-15), listedness (G-16), cold-chain (G-19), aggregation (G-20), audit-capture (G-26).
- Human approval gates: QP certification (G-07), batch disposition (G-08), PV final determinations (G-17), signal confirmation (G-18), allocation approval (G-21), shipment/inventory-status (G-22), recall consideration (G-23), override (G-25), inspection sign-off (G-27), closure (G-28), escalation closure (G-24).

AI Assist vs Deterministic vs Human Responsibility Map:
- AI assists by preparing, reconciling, surfacing, explaining and packaging evidence.
- Deterministic controls enforce gates that cannot be bypassed.
- Human responsibilities own every regulated decision and approval.

Read-Only Boundary Declaration:
- The system never releases, rejects, reprocesses, re-labels, recalls, changes inventory status, reserves capacity, allocates stock, ships product, or changes formulation/spec/eligibility/disposition.
- The system prepares, reconciles, explains and packages evidence only.

Human Decision Points:
- QP certification; batch disposition; OOS/OOT disposition; unit acceptance; genealogy resolution; supplier verification; excursion disposition; PV final determinations; duplicate confirmation; awareness-date acceptance; terminology and listedness decisions; signal confirmation; cold-chain disposition; aggregation resolution; allocation approval; shipment/status decisions; recall consideration; consent/entitlement exceptions; inspection sign-off; override; escalation and closure.

Evidence and Audit Trail Summary:
- Every run produces identity/genealogy, source/row references, unit and terminology basis, authority, effective date, jurisdiction, clock basis, consent/entitlement, validation, checkpoint, version, owner and status for every claim.
- Every action produces an audit event; the 47-minute audit-capture gap remains visible and is never filled.

Rollback and AI-Off Behaviour:
- Safe operation for at least 14 days without model inference; deterministic gates remain operable offline.
- Rollback to the last validated checkpoint with no stale-state duplication (checkpoint corruption addressed).
- Runs spanning the audit gap carry a visible gap record.

Non-Negotiables:
- AI never releases, rejects, reprocesses, re-labels or recalls a batch.
- AI never makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions.
- AI never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval.
- AI never changes formulation, specification, clinical eligibility, safety-case disposition, batch release or recall decisions.
- Regulated accountability remains with accountable Quality, Safety, Regulatory, Clinical and Supply roles.
- No evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
- Everything is auditable.
- The system operates read-only and advisory.

Open Questions for the Final Synthesis:
- Which human roles are named for each approval gate (EU QP, OOS owner, genealogy owner, PV reviewer, signal owner, logistics owner, serialisation owner, inspection signatory)?
- How is the 14% release lead-time reduction reconciled with fail-closed readiness and audit completeness?
- How is AI-off continuity exercised as a first-class operating mode rather than a fallback?
- How is the 47-minute audit gap preserved across inspection, batch and safety evidence packages?
- How are untrusted sources governed and quarantined in every workflow run?
- Which evaluation metrics will be used to confirm the minimum governed workflow meets the Stage 13 thresholds?
```

Stage 14 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for the final synthesis.
