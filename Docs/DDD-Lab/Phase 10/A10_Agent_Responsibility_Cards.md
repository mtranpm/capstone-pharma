# A10 — Agent Responsibility Cards: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## 1. Stage 10 Mission

Stage 10 defines bounded responsibility cards for support roles in the NovaCura Therapeutics Group pharmaceutical evidence-reconciliation case. The purpose is to clarify what each agent role may prepare, reconcile, verify, compile, retrieve, generate, package or record; what it must never decide, certify, release, allocate, dispose, override or infer; which human owner remains accountable; what evidence is required; what fail-closed and stop conditions apply; and what audit events must be captured. This artifact does not resolve any batch, safety, quality or supply issue, does not approve batch release, rejection, reprocess, re-label or recall, does not make final PV decisions, does not allocate stock, and does not create architecture or implementation design. Agent roles are named as responsibility roles only; no technical agent, RAG or implementation is designed here.

---

## 2. Input Summary

The Stage 10 input comes from the Stage 9 governed source register for **governed evidence reconciliation and review support for regulated pharmaceutical workflows**. The scenario concerns the disputed biologics batch NCB204-B24071 (missing SUA-88 genealogy branch, mg/L vs µg/mL unit assumption, disputed OOS/OOT state, unverified supplier-audit commitment, back-entered batch-record step), emerging safety reports (duplicate ICSR candidates under different product names, disputed awareness date, MedDRA version mismatch, listedness conflict between IB, CCDS and local label), a cold-chain failure (disputed logger clocks and pallet association, missing case-to-pallet aggregation), a sole-source excipient shortage with CMO capacity conflict and demand exceeding stock, a ransomware event with a 47-minute audit-capture gap, and a multi-agency inspection request within 72 hours.

The core business concern is that batch, safety and supply review work must be evidence-complete, conflict-visible, provenance-backed, authority-respected and fail-closed on uncertainty, while preserving human accountability for regulated decisions, the read-only advisory boundary, consent/entitlement/privacy boundaries, and complete auditability across Workflows A, B and C. The non-negotiables carry forward verbatim: the AI never releases, rejects, reprocesses, re-labels or recalls a batch; never makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions; and never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval.

---

## 3. Agent Role Design Principles

- An agent role represents a bounded responsibility in regulated pharmaceutical review work, not a software system.
- Each agent role is named as a responsibility role (e.g., Batch Evidence Reconciler), not a technical agent.
- Every responsibility an agent role is given is traceable to a deterministic rule, a bounded heuristic, or an explicitly human-owned decision, and states its fail-closed default.
- Regulated decision accountability must not be diluted across advisory roles.
- Batch release, rejection, reprocess, re-label, recall and QP certification remain inside accountable Quality and EU QP ownership.
- Final PV seriousness, causality, expectedness, reportability and signal-confirmation decisions remain inside accountable PV review ownership.
- Inventory status changes, capacity reservation, stock allocation, shipment and recall initiation remain inside authorised human ownership.
- Consent, entitlement and privacy boundaries must apply across all roles that access or use patient or participant data.
- Authority must remain contextual per business object, jurisdiction and effective date; no system is universally authoritative.
- Fail-closed means no evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
- Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable.
- Known gaps must be placed in the right responsibility but not resolved.
- No agent role may be granted authority that belongs to a human-only decision boundary.

---

## 4. Candidate Agent Roles

| Agent Role | Primary Purpose | Owner Context (Bounded Context) |
|---|---|---|
| Batch Evidence Reconciler | Reconcile batch evidence into a conflict-visible batch-review readiness package (Workflow A) | GxP Batch Evidence Reconciliation Context |
| Genealogy and Identity Verifier | Verify product/batch/compound/material identity and genealogy completeness; surface lineage breaks | Identity, Genealogy and Product Master Context |
| Unit and Terminology Normaliser | Surface unit-conversion and terminology state (mg/L vs µg/mL, MedDRA versions) | Unit and Terminology Standardisation Context |
| Release-Packet Compiler | Compile release-packet element completeness and evidence-gap lists | GxP Batch Evidence Reconciliation Context |
| Supplier-Audit Evidence Verifier | Verify supplier audit, certificate and commitment evidence | Supplier and Audit Evidence Context; Source and Document Governance Context |
| PV Case Intake Assistant | Support PV case intake, source attribution and completeness (Workflow B) | PV Case Intake and Signal Support Context |
| Duplicate-Candidate Detector | Surface duplicate-ICSR candidates for review | PV Case Intake and Signal Support Context |
| Reporting-Clock Reconstructor | Reconstruct reporting-clock inputs and surface awareness-date conflicts | PV Case Intake and Signal Support Context |
| Listedness Evidence Retriever | Retrieve IB, CCDS and local label listedness evidence per jurisdiction and version | PV Case Intake and Signal Support Context; Regulatory evidence |
| Product-Quality Linkage Checker | Link product-quality complaints to cases and batches | PV Case Intake and Signal Support Context; Quality |
| Supply Recovery Option Analyst | Generate traceable, policy-bounded supply and cold-chain recovery options (Workflow C) | Supply, Cold-Chain and Allocation Planning Context |
| Cold-Chain Evidence Reconstructor | Reconstruct logger clock, pallet association and aggregation evidence | Supply, Cold-Chain and Allocation Planning Context; Identity context |
| Allocation Constraint Checker | Check allocation constraints for candidate options | Supply, Cold-Chain and Allocation Planning Context |
| Inspection Evidence Packager | Assemble traceable evidence packages for inspections | Audit, Evidence and Continuity Context |
| Evidence and Audit Recorder | Record auditable events and keep audit-capture gaps visible | Audit, Evidence and Continuity Context |

---

## 5. Agent Responsibility Cards

### ARC-001 — Batch Evidence Reconciler

| Field | Detail |
|---|---|
| Agent role | Batch Evidence Reconciler |
| Mission | Reconcile batch evidence across genealogy, laboratory results, environmental monitoring, deviations, CAPA, change control, validation state, supplier evidence and release-packet completeness into a conflict-visible batch-review readiness package (Workflow A). It never releases, rejects, reprocesses, re-labels or recalls a batch. |
| Bounded context | GxP Batch Evidence Reconciliation Context |
| Input | Genealogy state, lab results, interface mappings, OOS investigations, environmental monitoring, microbiology results, deviations, CAPA, change controls, cleaning validation, validation state, supplier evidence, release-packet state |
| Deterministic rules | R-01 identity resolved; R-02 genealogy completeness; R-03 batch not shown release-ready with unresolved elements; R-06 disputed OOS/OOT state open and visible; R-08 back-entered step checkpoint; R-09 validation-state consistency; R-11 checkpoint-state completeness; R-16 audit-capture gap visible |
| Bounded reasoning | Link evidence items to batch-review readiness, attribute conflicts to sources, surface evidence gaps with ownership; no disposition, no completeness claim beyond evidence |
| Actions it may take | Prepare the batch-review readiness package; surface evidence gaps; attribute sources; prepare readiness assessment drafts for Quality/QP review |
| Actions it must never take | Release, reject, reprocess, re-label or recall a batch; certify as QP; disposition OOS/OOT or excursions; hide conflicts; claim release-ready while any element is unresolved or unverified; treat a later timestamp as authoritative |
| Fail-closed defaults | No batch evidence output while identity, genealogy, unit, terminology, authority, consent, validation or checkpoint state is unresolved; batch not shown release-ready with unresolved or unverified elements |
| Evidence and traceability | Reconciliation trail, source citations, genealogy-break record, evidence-gap ownership, reviewer identity, readiness assessment status |
| Human review and override | Quality release reviewer reviews readiness; EU QP owns certification; OOS owner disposes disputed results; overrides require authorized owner and reason |
| Handoff | Genealogy and Identity Verifier; Unit and Terminology Normaliser; Release-Packet Compiler; Supplier-Audit Evidence Verifier; Inspection Evidence Packager; Evidence and Audit Recorder |

---

### ARC-002 — Genealogy and Identity Verifier

| Field | Detail |
|---|---|
| Agent role | Genealogy and Identity Verifier |
| Mission | Verify product, batch, compound and material identity and genealogy completeness; surface lineage breaks (including the SUA-88 branch) with ownership; never repair lineage or merge records |
| Bounded context | Identity, Genealogy and Product Master Context |
| Input | Product master, substance master, batch records, MES genealogy, warehouse consumption, serialisation events, product-master aliases |
| Deterministic rules | R-01 identity resolved; R-02 genealogy completeness; R-05 identity/product-code match; R-11 checkpoint-state completeness; authority/effective-date/jurisdiction gate |
| Bounded reasoning | Compare genealogy branches against warehouse consumption; locate break position and ownership; assess aggregation state; assess identity-match candidates without resolving conflicts |
| Actions it may take | Surface genealogy breaks; identify ownership; prepare identity-match checks; flag missing case-to-pallet aggregation; present evidence of conflict between MES and warehouse |
| Actions it must never take | Repair lineage, merge records, resolve the SUA-88 break, pick an authoritative record, treat a later timestamp as more authoritative, claim genealogy complete with a missing branch |
| Fail-closed defaults | No batch evidence output while identity or genealogy is unresolved; the SUA-88 break remains visible with ownership |
| Evidence and traceability | Identity-match evidence, genealogy-break identification, source records, aggregation-state record, owner attribution |
| Human review and override | Identity/genealogy/master-data owner resolves the break; overrides require authorized owner and reason |
| Handoff | Batch Evidence Reconciler; Cold-Chain Evidence Reconstructor (aggregation); PV Case Intake Assistant (product linkage); Inspection Evidence Packager; Evidence and Audit Recorder |

---

### ARC-003 — Unit and Terminology Normaliser

| Field | Detail |
|---|---|
| Agent role | Unit and Terminology Normaliser |
| Mission | Surface unit-conversion and terminology state (mg/L vs µg/mL; MedDRA versions and preferred terms) for accountable review; never apply silent conversions or choose terms |
| Bounded context | Unit and Terminology Standardisation Context |
| Input | Lab results, interface mappings, adverse events, terminology versions, controlled vocabularies, data dictionary |
| Deterministic rules | R-04 unit-conversion consistency; R-13 MedDRA version consistency; R-11 checkpoint-state completeness |
| Bounded reasoning | Detect reported-unit vs receiving-interface-assumed-unit conflicts; detect MedDRA version differences that change a preferred term; attribute to sources |
| Actions it may take | Surface unit conflicts; declare no-answer; present conversion evidence; present version-mismatch evidence for review |
| Actions it must never take | Apply a conversion, choose a preferred term, pick a version winner, resolve the unit or terminology conflict, treat an unapproved assumption as approved |
| Fail-closed defaults | No evidence output while unit or terminology state is unresolved; conversion assumptions remain unapproved and visible |
| Evidence and traceability | Mapping history, version-alignment records, conversion-assumption status, no-answer declaration, source attribution |
| Human review and override | Laboratory/interface owner with Quality accepts the conversion; safety coder/terminology owner aligns MedDRA versions; overrides require authorized owner and reason |
| Handoff | Batch Evidence Reconciler; PV Case Intake Assistant; Evidence and Audit Recorder |

---

### ARC-004 — Release-Packet Compiler

| Field | Detail |
|---|---|
| Agent role | Release-Packet Compiler |
| Mission | Compile release-packet element completeness, evidence-gap lists and the batch-review readiness package for human review; never certify or release |
| Bounded context | GxP Batch Evidence Reconciliation Context |
| Input | Release packets, supplier audits, certificates of analysis, batch records, lab results, genealogy state, release-packet checklist, release policy |
| Deterministic rules | R-03 batch not shown release-ready with unresolved elements; R-07 unverified commitment not closed; R-12 required release-packet element completeness; R-11 checkpoint-state completeness |
| Bounded reasoning | Check required packet elements; surface missing or unverified items (e.g., contract-site audit commitment); attribute gaps to owners |
| Actions it may take | List packet elements; prepare evidence-gap lists; prepare the readiness package for QP; present unverified-commitment status |
| Actions it must never take | Mark the packet release-ready with unresolved elements; certify as QP; release, reject, reprocess, re-label or recall; treat an unverified commitment as closed |
| Fail-closed defaults | Incomplete or unverified packet is not shown ready; the unverified supplier-audit commitment remains open |
| Evidence and traceability | Packet status, element checklist, evidence-gap ownership, verification state, pending-certification status |
| Human review and override | Quality release reviewer reviews; EU QP certifies; supplier-quality verifies commitments; overrides require authorized owner and reason |
| Handoff | EU QP / Quality release reviewer; Supplier-Audit Evidence Verifier; Inspection Evidence Packager; Evidence and Audit Recorder |

---

### ARC-005 — Supplier-Audit Evidence Verifier

| Field | Detail |
|---|---|
| Agent role | Supplier-Audit Evidence Verifier |
| Mission | Verify supplier audit, certificate and commitment evidence; surface unverified commitments; quarantine untrusted supplier documents; never treat unverified as closed |
| Bounded context | Supplier and Audit Evidence Context; Source and Document Governance Context |
| Input | Supplier audits, certificates of analysis, regulatory commitments, vendor portals (untrusted), supplier-risk records, quarantine state |
| Deterministic rules | R-07 unverified commitment not closed; R-12 release-packet completeness; R-09 validation-state consistency; source-governance quarantine gate |
| Bounded reasoning | Match commitments to verification evidence; check certificate provenance and ALCOA+; flag unverified items; flag untrusted supplier content |
| Actions it may take | Present verification state; prepare verification requests; flag the malicious supplier deviation and other untrusted content; surface certificate-provenance breaks |
| Actions it must never take | Close a commitment, verify a commitment, treat an unverified commitment as closed, treat an untrusted supplier document as authoritative, execute embedded document instructions |
| Fail-closed defaults | An unverified commitment stays open; untrusted supplier sources remain quarantined; no evidence output while supplier-evidence state is unresolved |
| Evidence and traceability | Verification request/state, certificate provenance, quarantine record, packet status, attempted-injection flag |
| Human review and override | Supplier-quality / quality reviewer verifies and closes; source/document governance owner disposes untrusted content; overrides require authorized owner and reason |
| Handoff | Release-Packet Compiler; Supply Recovery Option Analyst; Inspection Evidence Packager; Evidence and Audit Recorder |

---

### ARC-006 — PV Case Intake Assistant

| Field | Detail |
|---|---|
| Agent role | PV Case Intake Assistant |
| Mission | Support PV case intake: attribute sources, capture completeness, surface gaps and route material for accountable review (Workflow B); never make final PV decisions |
| Bounded context | PV Case Intake and Signal Support Context |
| Input | ICSR cases, safety receipts, sensitive segments, product labels, consent/entitlement state, PV case policy |
| Deterministic rules | R-10 entitlement/consent gate; R-15 reporting-clock inputs complete; R-13 MedDRA version consistency; R-11 checkpoint-state completeness |
| Bounded reasoning | Attribute intake sources; check case-intake completeness; prepare intake material without disposition |
| Actions it may take | Prepare case-intake completeness material; surface gaps; route to reviewers; flag sensitive segments for privacy handling |
| Actions it must never take | Make final seriousness, causality, expectedness, reportability or signal-confirmation decisions; confirm duplicates; set the awareness date; disposition a case; surface patient data without consent/entitlement |
| Fail-closed defaults | No intake output while case identity, consent/entitlement, terminology or checkpoint state is unresolved |
| Evidence and traceability | Receipts, intake timestamps, consent/entitlement check, source attribution, reviewer routing |
| Human review and override | PV case-intake staff and PV medical/safety reviewers own intake and disposition; overrides require authorized owner and reason |
| Handoff | Duplicate-Candidate Detector; Reporting-Clock Reconstructor; Listedness Evidence Retriever; Product-Quality Linkage Checker; Evidence and Audit Recorder |

---

### ARC-007 — Duplicate-Candidate Detector

| Field | Detail |
|---|---|
| Agent role | Duplicate-Candidate Detector |
| Mission | Surface duplicate-ICSR candidates, including candidates under different product names; never confirm, merge or split |
| Bounded context | PV Case Intake and Signal Support Context |
| Input | ICSR cases, duplicate candidates, product-master aliases, adverse events/terminology versions |
| Deterministic rules | R-14 duplicate-ICSR candidate similarity check surfaces candidates only; R-05 identity/product-code match; R-13 MedDRA version consistency |
| Bounded reasoning | Assess candidate similarity bounded to surfacing, with product-name and terminology differences made visible; never concludes confirmation |
| Actions it may take | Surface duplicate candidates; present similarity rationale; route candidates for review |
| Actions it must never take | Confirm, merge or split cases; recommend confirmation; resolve the duplicate conflict; treat product-name aliases as authoritative identity |
| Fail-closed defaults | Candidates only; no confirmation without accountable PV review |
| Evidence and traceability | Duplicate rationale, candidate pairs, product-name evidence, reviewer routing |
| Human review and override | PV reviewer confirms duplicates; overrides require authorized owner and reason |
| Handoff | PV reviewers; Reporting-Clock Reconstructor; Evidence and Audit Recorder |

---

### ARC-008 — Reporting-Clock Reconstructor

| Field | Detail |
|---|---|
| Agent role | Reporting-Clock Reconstructor |
| Mission | Reconstruct reporting-clock inputs from vendor receipt, affiliate inbox and global safety DB; surface the awareness-date conflict; never set the clock |
| Bounded context | PV Case Intake and Signal Support Context; Authority, Effective-Date and Jurisdiction Context |
| Input | Safety receipts, ICSR cases, PV reporting-clocks policy, authority/effective-date basis |
| Deterministic rules | R-15 reporting-clock inputs complete; R-16 audit-capture gap visible; authority/effective-date/jurisdiction gate |
| Bounded reasoning | Attribute receipt times to sources; present a source-basis timeline; surface awareness-date disputes without resolving them |
| Actions it may take | Present clock-reconstruction evidence; surface the disputed awareness date; prepare reconstruction material for review; escalate incomplete inputs |
| Actions it must never set | Set the awareness date; accept the date; resolve the dispute; treat one receipt source as automatically authoritative |
| Fail-closed defaults | The reporting clock is not set; incomplete or disputed inputs trigger escalation, not inference |
| Evidence and traceability | Clock-reconstruction evidence, source basis, attribution, escalation record |
| Human review and override | PV case-intake staff / PV reviewer accepts the awareness date; overrides require authorized owner and reason |
| Handoff | PV reviewers; Duplicate-Candidate Detector; Evidence and Audit Recorder |

---

### ARC-009 — Listedness Evidence Retriever

| Field | Detail |
|---|---|
| Agent role | Listedness Evidence Retriever |
| Mission | Retrieve IB, core data sheet (CCDS) and local label listedness evidence per jurisdiction and version; never pick a winner |
| Bounded context | PV Case Intake and Signal Support Context; Regulatory evidence; Source and Document Governance Context |
| Input | Listedness sources, product labels, market authorisations, PV listedness-authority policy, approved label/IB/CCDS versions |
| Deterministic rules | R-13 terminology consistency; R-05 identity match; authority/effective-date/jurisdiction gate; regulated-output source control |
| Bounded reasoning | Compare listedness sources by jurisdiction and version; surface the IB/CCDS/local-label conflict; cite approved versions only |
| Actions it may take | Present listedness evidence comparisons; surface conflicts; cite approved label/IB/CCDS versions |
| Actions it must never take | Pick a listedness winner; determine expectedness; use an unapproved, superseded or quarantined source for listedness; make a reportability determination |
| Fail-closed defaults | No listedness determination; the conflict remains visible with jurisdiction and version basis |
| Evidence and traceability | Listedness-source versions, jurisdiction basis, citation, determination record (created by the human) |
| Human review and override | PV medical reviewer / Regulatory Affairs determines listedness per jurisdiction; overrides require authorized owner and reason |
| Handoff | PV reviewers; regulated-output controls; Inspection Evidence Packager; Evidence and Audit Recorder |

---

### ARC-010 — Product-Quality Linkage Checker

| Field | Detail |
|---|---|
| Agent role | Product-Quality Linkage Checker |
| Mission | Link product-quality complaints to cases and batches; surface linkage evidence; never treat linkage as disposition |
| Bounded context | PV Case Intake and Signal Support Context; Quality |
| Input | Product complaints, ICSR cases, batches, product labels |
| Deterministic rules | R-01 identity resolved; R-05 identity/product-code match; R-06 disputed result state visible; R-11 checkpoint-state completeness |
| Bounded reasoning | Assess linkage candidates between complaints, cases and batches; attribute evidence without disposition |
| Actions it may take | Surface linkage candidates; present evidence; attribute to owners |
| Actions it must never take | Confirm linkage as disposition; dispose a complaint or case; change case disposition; treat linkage as batch or product judgement |
| Fail-closed defaults | Linkage remains a candidate until accountable review; no output while identity or checkpoint state is unresolved |
| Evidence and traceability | Complaint records, linkage evidence, owner attribution, status |
| Human review and override | PV/Quality owner disposes the linkage; overrides require authorized owner and reason |
| Handoff | PV reviewers; Batch Evidence Reconciler; Evidence and Audit Recorder |

---

### ARC-011 — Supply Recovery Option Analyst

| Field | Detail |
|---|---|
| Agent role | Supply Recovery Option Analyst |
| Mission | Generate traceable, policy-bounded supply-shortage and cold-chain recovery options from inventory, quality status, market authorisation, trial demand, compassionate-use constraints, cold-chain evidence, CMO capacity, transport and allocation policy (Workflow C); never execute |
| Bounded context | Supply, Cold-Chain and Allocation Planning Context |
| Input | Inventory, demand forecast, allocation constraints, shipments, temperature loggers, CMO capacity, vendor contracts, supplier risks, market authorisations, supply-allocation policy |
| Deterministic rules | R-11 checkpoint-state completeness; authority/effective-date/jurisdiction gate; cold-chain evidence gate; allocation-approval human gate |
| Bounded reasoning | Compose options within documented constraints; quantify trade-offs; surface constraint conflicts (e.g., dual-sponsor CMO promise, demand exceeding stock) |
| Actions it may take | Generate traceable options; prepare constraint rationale; prepare approval requests; escalate shortages |
| Actions it must never take | Change inventory status, reserve capacity, allocate stock, ship product, initiate a recall, exempt a constraint, override compassionate-use entitlements |
| Fail-closed defaults | Options are not trusted while cold-chain evidence is unresolved; no execution without explicit authorised human approval |
| Evidence and traceability | Option rationale, evidence used per option, approval request, escalation record, status |
| Human review and override | Supply Chain VP / authorised Quality owner approves; patient-safety voice informs compassionate-use constraints; overrides require authorized owner and reason |
| Handoff | Allocation Constraint Checker; Cold-Chain Evidence Reconstructor; Inspection Evidence Packager; Evidence and Audit Recorder |

---

### ARC-012 — Cold-Chain Evidence Reconstructor

| Field | Detail |
|---|---|
| Agent role | Cold-Chain Evidence Reconstructor |
| Mission | Reconstruct cold-chain evidence: logger clocks, pallet association, case-to-pallet aggregation and excursion data; never disposition the shipment |
| Bounded context | Supply, Cold-Chain and Allocation Planning Context; Identity, Genealogy and Product Master Context (aggregation) |
| Input | Temperature loggers, shipments, serialisation events, packaging events, cold-chain assessment policy |
| Deterministic rules | R-11 checkpoint-state completeness; cold-chain evidence gate; serialisation-aggregation gate; authority gate |
| Bounded reasoning | Attribute logger readings to pallets; reconstruct the temperature timeline; surface disputed logger clocks, pallet association and missing aggregation |
| Actions it may take | Present excursion evidence; surface logger-clock disputes; flag missing case-to-pallet aggregation; prepare evidence for disposition review |
| Actions it must never take | Disposition the excursion; assume the aggregation link; resolve the logger dispute; approve shipment; treat disputed evidence as resolved |
| Fail-closed defaults | The excursion remains unresolved; recovery options are not trusted until cold-chain evidence is resolved |
| Evidence and traceability | Logger basis, pallet link, aggregation-state record, excursion evidence, gap ownership |
| Human review and override | Logistics / cold-chain accountable owner with Quality input disposes; serialisation owner resolves aggregation; overrides require authorized owner and reason |
| Handoff | Supply Recovery Option Analyst; Batch Evidence Reconciler; Inspection Evidence Packager; Evidence and Audit Recorder |

---

### ARC-013 — Allocation Constraint Checker

| Field | Detail |
|---|---|
| Agent role | Allocation Constraint Checker |
| Mission | Check allocation constraints (policy, market authorisation, trial demand, compassionate-use entitlements, quality status) for candidate options; never allocate |
| Bounded context | Supply, Cold-Chain and Allocation Planning Context |
| Input | Allocation constraints, demand forecast, market authorisations, inventory, quality status, supply-allocation ethics policy |
| Deterministic rules | R-11 checkpoint-state completeness; authority/effective-date/jurisdiction gate; allocation human-approval gate |
| Bounded reasoning | Test candidate options against documented constraints; surface violations and compassionate-use conflicts |
| Actions it may take | Check constraints; present violation lists; prepare compliance assessments for options; escalate constraint conflicts |
| Actions it must never take | Allocate, reserve, ship, exempt a constraint, override an entitlement, decide allocation |
| Fail-closed defaults | An option that violates a constraint is flagged; no allocation occurs without authorised human approval |
| Evidence and traceability | Constraint rationale, policy reference, check result, escalation record |
| Human review and override | Supply Chain VP / authorised Quality owner approves; overrides require authorized owner and reason |
| Handoff | Supply Recovery Option Analyst; Inspection Evidence Packager; Evidence and Audit Recorder |

---

### ARC-014 — Inspection Evidence Packager

| Field | Detail |
|---|---|
| Agent role | Inspection Evidence Packager |
| Mission | Assemble traceable evidence packages (e.g., for the 72-hour multi-agency request) spanning trial data, batch history, safety cases and AI-system controls; never create or hide evidence |
| Bounded context | Audit, Evidence and Continuity Context |
| Input | All governed sources, source metadata, AI-platform control evidence, inspection requests, regulatory policy, package requirements |
| Deterministic rules | R-16 audit-capture gap visible; R-17 everything auditable; source-governance gate; regulated-output source control |
| Bounded reasoning | Trace evidence to sources; build a package manifest; surface missing or conflicting evidence |
| Actions it may take | Package evidence; produce a manifest; cite sources; flag gaps; prepare inspection-readiness material |
| Actions it must never take | Create evidence, hide gaps, alter source records, make decisions, fill the 47-minute audit gap silently, include untrusted sources as authority |
| Fail-closed defaults | The package is not treated as complete while evidence gaps or audit gaps are unresolved |
| Evidence and traceability | Package manifest, source citations, timeline, gap ownership |
| Human review and override | Regulatory/Quality participant packages for inspection; evidence/audit owner confirms; overrides require authorized owner and reason |
| Handoff | Regulators (via accountable humans); Evidence and Audit Recorder |

---

### ARC-015 — Evidence and Audit Recorder

| Field | Detail |
|---|---|
| Agent role | Evidence and Audit Recorder |
| Mission | Record every recommendation, draft, approval, override, release, escalation, action, outcome and closure as an auditable event; keep the audit-capture gap visible; never alter source records |
| Bounded context | Audit, Evidence and Continuity Context |
| Input | Events from all workflows, audit trails, downtime events, continuity requirements, retention rules, legal holds |
| Deterministic rules | R-16 audit-capture gap remains visible; R-17 everything auditable; R-11 checkpoint-state completeness |
| Bounded reasoning | Assemble the audit event envelope: source, owner, status, timestamp, decision, approval/override, reason, closure |
| Actions it may take | Record audit events; surface missing audit evidence; keep the 47-minute gap visible; support safe operation without AI |
| Actions it must never take | Fill the audit-capture gap silently; delete or alter records; mark incomplete audit evidence as complete; decide or approve anything |
| Fail-closed defaults | No event is treated as complete without audit evidence; the audit-capture gap remains visible with ownership |
| Evidence and traceability | Audit event envelope, source, owner, status, timestamp, closure/retention references |
| Human review and override | Audit/quality oversight confirms completeness; overrides require authorized owner and reason |
| Handoff | All workflows; Inspection Evidence Packager; AI-off continuity roles |

---

## 6. Human-Only Decision Boundaries

| Human-Only Decision | Accountable Human Role | Agent Role That Must Hand Off |
|---|---|---|
| QP certification (final batch certification) | EU Qualified Person | ARC-001 Batch Evidence Reconciler; ARC-004 Release-Packet Compiler |
| Batch release / rejection / reprocess / re-label / recall | EU Qualified Person / Quality release reviewer; Quality/Regulatory roles for recall | ARC-001; ARC-004; ARC-011 |
| OOS/OOT disposition and investigation conclusion | Laboratory analyst / OOS owner | ARC-001; ARC-003 |
| Unit-conversion acceptance (mg/L vs µg/mL) | Laboratory / interface owner with Quality acceptance | ARC-003 |
| Supplier-audit verification and commitment closure | Supplier-quality / quality reviewer | ARC-005; ARC-004 |
| Batch identity/genealogy resolution (SUA-88) | Identity / genealogy / master-data owner | ARC-002 |
| Final PV seriousness, causality, expectedness, reportability | PV medical/safety reviewer | ARC-006, ARC-007, ARC-008, ARC-009, ARC-010 |
| Signal confirmation | Signal management | ARC-006 |
| Duplicate confirmation | PV reviewer | ARC-007 |
| Awareness-date acceptance | PV case-intake staff / PV reviewer | ARC-008 |
| Listedness determination per jurisdiction/source | PV medical reviewer / Regulatory Affairs | ARC-009 |
| Inventory status change, capacity reservation, stock allocation, shipment, recall initiation | Supply Chain VP / authorised Quality owner | ARC-011, ARC-012, ARC-013 |
| Cold-chain excursion disposition | Logistics / cold-chain accountable owner with Quality input | ARC-012 |
| Formulation, specification, clinical eligibility or safety-case disposition changes | Accountable Quality/Clinical/Safety roles | All agent roles |
| Consent/entitlement exception handling | Data Protection Officer / privacy owner | All agent roles touching patient data |
| Exception override | Authorized human owner | All agent roles |
| Case/escalation closure | Accountable workflow owner | All agent roles |

---

## 7. Agent-to-Agent Handoffs

| Handoff | Information Exchanged | Risk of the Handoff |
|---|---|---|
| ARC-002 Genealogy and Identity Verifier → ARC-001 Batch Evidence Reconciler | Identity-match result, genealogy-break state, aggregation state | The SUA-88 break may be treated as resolved instead of surfaced |
| ARC-003 Unit and Terminology Normaliser → ARC-001 / ARC-006 | Unit-conversion state, MedDRA version state, no-answer declarations | An unapproved conversion or version mismatch may propagate downstream |
| ARC-005 Supplier-Audit Evidence Verifier → ARC-004 Release-Packet Compiler | Commitment verification state, certificate provenance | An unverified commitment may be treated as closed in the packet |
| ARC-001 / ARC-004 → EU QP / Quality release reviewer | Batch-review readiness package, evidence-gap list | Readiness may be confused with certification or release approval |
| ARC-006 PV Case Intake Assistant → ARC-007 Duplicate-Candidate Detector | Intake completeness, source attribution | Duplicate candidates may be mistaken for confirmed duplicates |
| ARC-007 → ARC-008 Reporting-Clock Reconstructor | Candidate pairs, product-name evidence | Candidate status may be treated as a decision |
| ARC-008 → PV reviewers | Clock-reconstruction evidence, awareness-date dispute | The reconstructed timeline may be mistaken for the accepted date |
| ARC-009 Listedness Evidence Retriever → PV reviewers | Listedness evidence, IB/CCDS/local-label conflict | The evidence comparison may be mistaken for a listedness determination |
| ARC-010 Product-Quality Linkage Checker → ARC-001 / ARC-006 | Complaint-to-case-to-batch linkage candidates | Linkage may be treated as disposition |
| ARC-012 Cold-Chain Evidence Reconstructor → ARC-011 Supply Recovery Option Analyst | Logger basis, pallet link, aggregation state | Options may be trusted while cold-chain evidence is unresolved |
| ARC-013 Allocation Constraint Checker → ARC-011 | Constraint check results, violation lists | Option output may be mistaken for approved allocation |
| ARC-011 → Supply Chain VP / authorised Quality owner | Traceable options, approval request | Options may be mistaken for executed allocation or shipment |
| All workflows → ARC-015 Evidence and Audit Recorder | Audit events, gaps, approvals, closures | Events may be recorded without source, owner, or timestamp |
| ARC-015 → ARC-014 Inspection Evidence Packager | Audit trail, gap state, closure state | The 47-minute audit gap may be hidden in the package |
| ARC-014 → Regulators (via humans) | Package manifest, source citations, timeline | The package may appear complete while evidence gaps are hidden |

---

## 8. Guardrail and Guardrail-Owner Register

| Guardrail | Type | Owner Context | Human Role Accountable | Fail-Closed Default | Evidence Need |
|---|---|---|---|---|---|
| Identity/product-code match gate | Deterministic gate | Identity, Genealogy and Product Master Context | Identity / genealogy / master-data owner | No batch/PV/supply evidence output while identity unresolved | Identity-match evidence, product-master reference |
| Genealogy completeness gate | Deterministic gate | Identity, Genealogy and Product Master Context | Identity / genealogy / master-data owner | No batch evidence output while any branch missing; SUA-88 break stays visible | Genealogy-break record, source records |
| Unit-conversion state gate | Deterministic gate | Unit and Terminology Standardisation Context | Laboratory / interface owner with Quality | No silent conversion; mg/L vs µg/mL stays unapproved and visible | Conversion mapping, approval/override record |
| OOS/OOT state visibility gate | Deterministic gate | GxP Batch Evidence Reconciliation Context | Laboratory analyst / OOS owner | Disputed result state stays open and visible | Conflicting states, investigation record |
| MedDRA version gate | Deterministic gate | Unit and Terminology Standardisation Context | Safety coder / terminology owner | No terminology output while versions conflict | Version-alignment evidence, source |
| Validation/checkpoint gate | Deterministic gate | Authority, Effective-Date and Jurisdiction Context | Validation / Quality owner | No output while validation or checkpoint state ambiguous | Validation-state evidence, no-answer record |
| Authority/effective-date/jurisdiction gate | Deterministic gate | Authority, Effective-Date and Jurisdiction Context | Regulatory Affairs / master-data governance | Later timestamp never automatically authoritative | Authority rationale, jurisdiction basis |
| Consent/entitlement gate | Deterministic gate | Consent, Entitlement and Privacy Context | Data Protection Officer | No patient/participant data surfaced without lawful basis | Consent/entitlement check, access/use record |
| Release-packet completeness gate | Deterministic gate | GxP Batch Evidence Reconciliation Context | Quality release reviewer | Batch not shown release-ready with unresolved/unverified elements | Packet status, element checklist, gap ownership |
| Supplier-audit verification gate | Deterministic gate | Supplier and Audit Evidence Context | Supplier-quality / quality reviewer | Unverified commitment is not closed | Verification request/state, packet status |
| Duplicate-candidate heuristic | Bounded heuristic | PV Case Intake and Signal Support Context | PV reviewer | Candidates only; no confirmation | Duplicate rationale, candidates, routing |
| Reporting-clock completeness gate | Deterministic gate | PV Case Intake and Signal Support Context | PV case-intake staff / PV reviewer | Clock not set; inputs must be complete | Clock-reconstruction evidence, source basis |
| Listedness conflict visibility | Bounded heuristic | PV Case Intake and Signal Support Context | PV medical reviewer / Regulatory Affairs | No winner picked; conflict visible | Listedness-source versions, determination record |
| Cold-chain evidence gate | Deterministic gate | Supply, Cold-Chain and Allocation Planning Context | Logistics / cold-chain owner with Quality | Options not trusted until logger/pallet/aggregation resolved | Logger basis, pallet link, excursion evidence |
| Allocation approval gate | Human authorization | Supply, Cold-Chain and Allocation Planning Context | Supply Chain VP / authorised Quality owner | No allocation/reservation/shipment without approval | Approval request, human approval, action record |
| Regulated-output release gate | Human authorization | GxP Batch Evidence Reconciliation / Regulatory | EU QP / Quality release reviewer | No release or regulator-facing packaging without human approval | Release record, package manifest, approvals |
| PV final-decision gate | Human authorization | PV Case Intake and Signal Support Context | PV medical/safety reviewer | No final PV determinations by an agent role | Reviewer routing, disposition record |
| Audit-capture-gap gate | Deterministic gate | Audit, Evidence and Continuity Context | Audit / quality oversight | The 47-minute gap stays visible; not filled silently | Gap detection, duration, owner |
| Untrusted-source quarantine gate | Deterministic gate | Source and Document Governance Context | Source/document governance owner; CISO | Untrusted sources never authoritative | Quarantine record, attempted-injection flag |
| AI-off continuity gate | Deterministic gate | Audit, Evidence and Continuity Context | CISO / continuity owner | Safe operation continues without AI inference | Continuity records, downtime state |

---

## 9. Anti-Patterns to Avoid

```text
Granting an agent role the authority to release, reject, reprocess, re-label or recall a batch.

Granting an agent role the authority to certify as QP.

Granting an agent role the authority to make final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions.

Granting an agent role the authority to confirm duplicates, set reporting clocks, pick listedness winners, or dispose OOS/OOT or cold-chain excursions.

Granting an agent role the authority to change inventory status, reserve capacity, allocate stock, ship product or initiate a recall.

Naming a technical agent or orchestration design as an agent role.

Designing one overloaded agent role that owns the full batch, safety or supply journey.

Treating a surfaced gap, conflict or candidate as resolved.

Silent unit conversion, silent genealogy repair, or treating a later timestamp as authoritative.

Surfacing patient/participant data without consent/entitlement checks.

Treating untrusted documents or tool manifests as authoritative.

Filling or hiding the 47-minute audit-capture gap.

Marking a release packet or evidence package complete while gaps remain.

Bypassing human-only decision boundaries via a handoff.

Designing an agent role with no fail-closed default.

Designing an agent role with no evidence or traceability requirement.

Treating derived workshop artifacts as controlled source records.

Creating technical architecture or implementation design from this artifact.
```

---

## 10. Boundary Warnings

- Do not treat **ARC-001 Batch Evidence Reconciler** or **ARC-004 Release-Packet Compiler** as owning batch release, rejection, reprocess, re-label, recall or QP certification; they own review readiness and packet visibility only.
- Do not allow **ARC-003 Unit and Terminology Normaliser** to silently apply a conversion or choose a preferred term.
- Do not let **ARC-006 to ARC-010** make final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions.
- Do not treat **ARC-011 Supply Recovery Option Analyst**, **ARC-012 Cold-Chain Evidence Reconstructor** or **ARC-013 Allocation Constraint Checker** outputs as executed allocation, reservation, shipment or recall.
- Do not let **ARC-002 Genealogy and Identity Verifier** silently resolve a genealogy break; breaks remain visible with ownership.
- Do not let **ARC-005 Supplier-Audit Evidence Verifier** treat an unverified commitment or an untrusted supplier document as closed or authoritative.
- Do not treat any system (LIMS, MES, safety DB) as universally authoritative; authority is per business object, jurisdiction and effective date.
- Do not bypass consent, entitlement or privacy boundaries when patient or participant data is accessed, used, routed or shared.
- Do not allow **ARC-015 Evidence and Audit Recorder** to become an afterthought; auditability is required across recommendations, drafts, approvals, overrides, releases, escalations, actions, outcomes and closures, and the organisation must operate safely without AI.
- Do not produce evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
- Do not merge all three workflows into one giant agent role, because that hides accountability and safety boundaries.

---

## 11. Stage 10 Quality Gate

The Stage 10 agent responsibility cards are acceptable only if:

```text
No batch, safety, quality or supply issue has been solved in this artifact.
No batch release/rejection/reprocess/re-label/recall decision has been made or implied.
No QP certification has been implied.
No final PV seriousness, causality, expectedness, reportability or signal-confirmation decision has been made.
No inventory status change, capacity reservation, stock allocation, shipment or recall initiation has been implied.
Every agent role is a named responsibility role, not a technical agent.
Every agent role has a bounded context and a fail-closed default.
Every responsibility is traceable to a deterministic rule, a bounded heuristic, or an explicitly human-owned decision.
Human-only decision boundaries are explicit and comprehensive.
Agent-to-agent handoffs identify the information exchanged and the risk of the handoff.
Guardrails have a type, owner context, accountable human role, fail-closed default and evidence need.
Fail-closed behaviour on unresolved identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation and checkpoint state is preserved.
Consent, entitlement and privacy boundaries remain explicit.
Known genealogy, unit, OOS/OOT, supplier-evidence, PV, cold-chain, shortage, validation, source-governance and audit gaps are mapped but not resolved.
Everything remains auditable and defensible under inspection, including the 47-minute audit-capture gap.
No agent role is overloaded to own the full evidence-reconciliation journey.
No architecture, RAG systems, MCP, agents, vector databases, APIs, deployment or implementation design has been introduced.
```

---

## 12. NEXT_STAGE_INPUT_BLOCK

```text
Stage 11 Input — Human Decision Ownership Matrix

Final Responsibility-Card Summary:
Stage 10 defined fifteen bounded agent responsibility cards for the NovaCura Therapeutics Group pharmaceutical evidence-reconciliation case. Each card clarifies mission, bounded context, inputs, deterministic rules, bounded reasoning, allowed actions, forbidden actions, fail-closed defaults, evidence and traceability requirements, human review and override points, and handoffs. The cards support reconciliation, verification, compilation, retrieval, option generation, packaging and recording only. They do not own batch release, QP certification, final PV decisions, allocation, shipment, recall, consent/entitlement override, or closure.

Agent Roles Created:
- ARC-001 Batch Evidence Reconciler (Workflow A)
- ARC-002 Genealogy and Identity Verifier
- ARC-003 Unit and Terminology Normaliser
- ARC-004 Release-Packet Compiler
- ARC-005 Supplier-Audit Evidence Verifier
- ARC-006 PV Case Intake Assistant (Workflow B)
- ARC-007 Duplicate-Candidate Detector
- ARC-008 Reporting-Clock Reconstructor
- ARC-009 Listedness Evidence Retriever
- ARC-010 Product-Quality Linkage Checker
- ARC-011 Supply Recovery Option Analyst (Workflow C)
- ARC-012 Cold-Chain Evidence Reconstructor
- ARC-013 Allocation Constraint Checker
- ARC-014 Inspection Evidence Packager
- ARC-015 Evidence and Audit Recorder

Human-Only Decision Boundaries:
- QP certification and batch release/rejection/reprocess/re-label/recall: EU QP / Quality release reviewer; Quality/Regulatory for recall.
- OOS/OOT disposition: Laboratory analyst / OOS owner.
- Unit-conversion acceptance: Laboratory / interface owner with Quality.
- Supplier-audit verification and commitment closure: Supplier-quality / quality reviewer.
- Batch identity/genealogy resolution: Identity / genealogy / master-data owner.
- Final PV seriousness, causality, expectedness, reportability: PV medical/safety reviewer.
- Signal confirmation: Signal management.
- Duplicate confirmation: PV reviewer.
- Awareness-date acceptance: PV case-intake staff / PV reviewer.
- Listedness determination: PV medical reviewer / Regulatory Affairs.
- Inventory status change, capacity reservation, stock allocation, shipment, recall initiation: Supply Chain VP / authorised Quality owner.
- Cold-chain excursion disposition: Logistics / cold-chain accountable owner with Quality input.
- Formulation/specification/eligibility/disposition changes: accountable Quality/Clinical/Safety roles.
- Consent/entitlement exception handling: Data Protection Officer / privacy owner.
- Exception override: authorized human owner.
- Case/escalation closure: accountable workflow owner.

Agent-to-Agent Handoffs:
- Genealogy/identity state from ARC-002 to ARC-001 and ARC-012.
- Unit/terminology state from ARC-003 to ARC-001 and ARC-006.
- Supplier verification state from ARC-005 to ARC-004 and ARC-011.
- Readiness packages from ARC-001/ARC-004 to EU QP / Quality release reviewer.
- Intake material from ARC-006 to ARC-007/ARC-008/ARC-009/ARC-010.
- Duplicate candidates from ARC-007 to PV reviewers.
- Clock evidence from ARC-008 to PV reviewers.
- Listedness evidence from ARC-009 to PV reviewers / Regulatory.
- Linkage candidates from ARC-010 to ARC-001 and ARC-006.
- Cold-chain evidence from ARC-012 to ARC-011.
- Constraint checks from ARC-013 to ARC-011.
- Options and approval requests from ARC-011 to Supply Chain VP / authorised Quality owner.
- Audit events from all roles to ARC-015.
- Evidence packages from ARC-014 to regulators (via humans).

Guardrails and Owners:
- Identity, genealogy, unit, terminology, validation/checkpoint, authority/effective-date/jurisdiction, consent/entitlement, release-packet completeness, supplier-audit verification, audit-capture-gap, untrusted-source quarantine and AI-off continuity: deterministic gates with accountable human owners.
- Duplicate-candidate and listedness-conflict handling: bounded heuristics surfacing candidates/conflicts only.
- Allocation approval, regulated-output release and PV final-decision: human-authorization gates.
- Fail-closed defaults: no evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved; no execution without explicit authorised human approval.

Non-Negotiables:
- AI never releases, rejects, reprocesses, re-labels or recalls a batch.
- AI never makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions.
- AI never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval.
- AI never changes formulation, specification, clinical eligibility, safety-case disposition, batch-release or recall decisions.
- Regulated accountability remains with the accountable Quality, Safety, Regulatory, Clinical and Supply roles.
- No evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
- Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable.
- The system operates read-only and advisory; it prepares, reconciles, explains and packages evidence.

Fail-Closed Defaults:
- Batch not shown release-ready while any genealogy branch or release-packet element is unresolved or unverified.
- No silent unit conversion, genealogy repair, duplicate confirmation, clock setting, listedness selection, or OOS/OOT/cold-chain disposition.
- Patient/participant data not surfaced without consent/entitlement.
- The 47-minute audit-capture gap stays visible.
- Options are not trusted while cold-chain evidence is unresolved.
- No allocation, reservation, shipment or recall without authorised human approval.

Anti-Patterns:
- Granting an agent role any human-only decision authority.
- Naming technical agents or orchestration as responsibility roles.
- One overloaded role owning the whole journey.
- Treating surfaced gaps, conflicts or candidates as resolved.
- Treating untrusted sources as authoritative.
- Hiding the audit-capture gap or marking incomplete evidence as complete.
- Bypassing consent/entitlement or regulated-output release controls.
- Creating architecture or implementation design from this artifact.

Open Questions for Human Decision Ownership:
- Who is the accountable owner for each batch-review readiness closure and release-packet gap?
- Who confirms QP-certification evidence completeness, and what is the pending-status workflow?
- Who resolves the SUA-88 genealogy break and the mg/L vs µg/mL unit acceptance?
- Who verifies and closes the contract-site supplier-audit commitment?
- Who accepts the awareness date and confirms duplicate candidates?
- Who determines listedness per jurisdiction, and which approved label/IB/CCDS versions apply?
- Who approves allocation options and documents constraint and compassionate-use rationale?
- Who disposes the cold-chain excursion with resolved logger, pallet and aggregation evidence?
- Who can authorize an override, and what reason format is required?
- Who confirms audit completeness and closure, including the 47-minute audit-capture gap?
- Which human role packages the 72-hour inspection evidence and signs the manifest?
```

Stage 10 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 11.
