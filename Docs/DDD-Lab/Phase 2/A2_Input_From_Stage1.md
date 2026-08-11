# A2 — Input From Stage 1: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

Use this file as the dedicated input attachment for Stage 2 — Domain and Subdomain Map.

This file is extracted from the Stage 1 Business Problem Framing output (`Docs/DDD-Lab/Phase 1/A1_Business_Problem_Framing.md`). It is intentionally limited to business-domain context. It does not solve the case, does not provide medical, regulatory or legal advice, does not resolve any product, batch, compound, safety, quality or supply issue, and does not introduce architecture or technical implementation.

---

## Stage 2 Input — Domain and Subdomain Discovery

### Business Problem Statement

NovaCura Therapeutics Group cannot reliably and quickly assemble evidence-complete, conflict-visible, provenance-backed, authority-respected material for regulated batch-review, pharmacovigilance and supply-recovery decisions, because its enterprise systems fragment identifiers, timestamps, terminology, access controls and authority hierarchies.

### Mandatory Workflows

- **Workflow A — GxP evidence reconciliation for batch-review readiness:** reconcile batch genealogy, laboratory results, environmental monitoring, deviations, CAPA, change control, validation state, supplier evidence and release-packet completeness. It may identify gaps, contradictions and evidence lineage. It must never release, reject, reprocess, re-label or recall a batch.
- **Workflow B — Pharmacovigilance case-intake and signal-support:** support intake, duplicate detection, terminology normalisation, source authority, reporting-clock reconstruction, listedness evidence, product-quality linkage and multilingual review. It must never make final seriousness, causality, expectedness, reportability or signal-confirmation decisions.
- **Workflow C — Bounded supply-shortage and cold-chain recovery planner:** generate traceable options using inventory, quality status, market authorisation, trial demand, compassionate-use constraints, cold-chain evidence, CMO capacity, transport and allocation policy. It must never change inventory status, reserve capacity, allocate stock, release product or initiate a recall without explicit authorised human approval.

### Affected Roles and Functions

- Chief Quality Officer and pharmaceutical quality-system function
- EU Qualified Person(s) for batch certification
- Quality release reviewers and batch-review coordination
- Manufacturing and sterile-fill operations
- Laboratory analysts, LIMS/CDS and OOS investigation owners
- Global Head of Pharmacovigilance and PV case-intake/processing staff
- PV medical/safety reviewers and signal-management function
- Clinical Operations and trial-data functions
- Regulatory Affairs (RIM, submissions, labelling, IDMP)
- Supply Chain planning and shortage/risk management
- Logistics, serialisation and cold-chain operations
- Contract manufacturing organisations (CMOs) and supplier quality
- Procurement and vendor management
- Data Protection Officer and privacy/legal function
- CISO and cybersecurity/incident-response function
- Biostatistics and trial-integrity function
- Patient-safety voice and clinical/safety governance forums

### Desired Outcomes

- Evidence-complete, conflict-visible, provenance-backed, authority-respected review work across Workflows A, B and C.
- Fail-closed behaviour on unresolved identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state.
- Read-only, advisory AI support that prepares, reconciles, explains and packages evidence.
- Regulated decisions (batch release/rejection, PV dispositions, allocation, recall) owned by accountable human roles.
- Auditable trail for every recommendation, draft, approval, override, release, escalation, action, outcome and closure.
- A 14% reduction in end-to-end release lead time without changing registered specifications or weakening independent Quality authority.

### Non-Negotiables

- The AI never releases, rejects, reprocesses, re-labels or recalls a batch.
- The AI never makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions.
- The AI never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval.
- The AI never changes formulation, specification, clinical eligibility, safety-case disposition, batch release or recall decisions.
- Regulated accountability remains with the accountable Quality, Safety, Regulatory, Clinical and Supply roles.
- Evidence output must not be produced while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
- Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable.
- The system operates read-only and advisory; it prepares, reconciles, explains and packages evidence.
- No product, batch, safety, quality or supply issue is considered resolved merely because it has been identified.

### Known Gaps and Exceptions

- Authority hierarchy inconsistent across systems; no universal authority; later timestamps not automatically more authoritative than approved signed records.
- Genealogy incomplete for batch NCB204-B24071 (missing single-use assembly lot SUA-88 branch).
- Unapproved unit convention (mg/L vs µg/mL) for contract-laboratory concentration.
- Disputed OOS/OOT state with an open investigation across LIMS, statistical tooling and laboratory notebook.
- Supplier-audit commitment claimed closed but not independently verified in the EU release packet.
- Batch-record step back-entered after network degradation; audit capture disabled for 47 minutes.
- Disputed PV awareness date; duplicate ICSR candidates under alternative product names; MedDRA version mismatch; listedness-source conflict.
- Cold-chain logger clocks and pallet association disputed; serialisation aggregation missing after a line restart.
- Sole-source excipient shortage with eight-week recovery estimate; CMO capacity conflict; demand exceeds available stock.
- Validation-state ambiguity across inventories; unapproved macro-enabled spreadsheet in use.
- Untrusted documents and manifests (prompt-injection PDF, stale/unsigned tool manifests, shared-account spreadsheets).
- Deliberate stakeholder conflicts: Quality vs Manufacturing on speed vs completeness; global standardisation vs jurisdictional variation; privacy minimisation vs defensible preservation; bundled vendor vs substitutability; automation vs prespecified, explainable transformations.

### Open Questions for Domain and Subdomain Discovery

- What is the main business domain represented by this problem?
- Which business areas are core to evidence-complete, fail-closed batch, safety and supply review work?
- Which business areas support the core advisory workflows?
- Which reusable organizational capabilities are needed across many regulated workflows?
- Which business areas own genealogy, unit/terminology, authority, PV case handling, allocation recommendation, and audit evidence?
- Which exception types need explicit ownership in later stages?
- Which business terms need precise definition before modelling continues?
