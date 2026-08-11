# A3 — Input From Stage 2: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

Use this file as the dedicated input attachment for Stage 3 — Ubiquitous Language Glossary.

This file is extracted from the Stage 2 Domain and Subdomain Map output. It is intentionally limited to business-domain context. It does not solve the case, does not provide medical, regulatory or legal advice, does not resolve any product, batch, compound, safety, quality or supply issue, and does not introduce architecture or technical implementation.

---

## Stage 3 Input — Ubiquitous Language Glossary

### Main Business Domain

Governed evidence reconciliation and review support for regulated pharmaceutical workflows

### Reason for Main Domain Selection

NovaCura Therapeutics Group's work depends on preparing, validating, reconciling, explaining, packaging and defending evidence so that accountable Quality, Safety, Regulatory, Clinical and Supply roles can perform batch review, pharmacovigilance case handling and supply recovery under a 14% release lead-time reduction target. The domain is the regulated review and reconciliation work, not the systems (LIMS, MES, safety databases) that hold the evidence.

### Core Subdomains

- GxP Evidence Reconciliation for Batch-Review Readiness (Workflow A)
- Pharmacovigilance Case-Intake and Signal-Support (Workflow B)
- Bounded Supply-Shortage and Cold-Chain Recovery Planning (Workflow C)

### Supporting Subdomains

- Identity, Genealogy and Product-Master Resolution
- Unit, Terminology and Reference-Data Standardisation
- Authority, Effective-Date and Jurisdiction Management
- Consent, Entitlement and Privacy Management
- Source and Document Governance
- Supplier and Audit-Evidence Management
- Regulatory and Inspection-Readiness Coordination
- Quality-Event and Deviation Lineage
- Evidence and Audit-Trail Management
- Continuity, Reliability and Economy Management

### Generic / Reusable Organizational Capabilities

- Identity and access management
- Time and clock synchronisation
- Audit logging
- Document and record management
- Master data management
- Monitoring, alerting and telemetry
- Notification and escalation routing
- Reporting and evidence packaging
- Validation and qualification state management
- Training and competency management

### Known Gaps Mapped to Subdomains

- Missing single-use assembly lot SUA-88 genealogy branch for batch NCB204-B24071 → Identity, Genealogy and Product-Master Resolution; GxP Evidence Reconciliation (Workflow A)
- Unapproved mg/L vs µg/mL unit assumption → Unit, Terminology and Reference-Data Standardisation; GxP Evidence Reconciliation (Workflow A)
- Disputed OOS/OOT state with an open investigation → Quality-Event and Deviation Lineage; GxP Evidence Reconciliation (Workflow A)
- Unverified supplier-audit commitment in the EU release packet → Supplier and Audit-Evidence Management; GxP Evidence Reconciliation (Workflow A)
- Back-entered batch-record step and 47-minute audit-capture gap → Evidence and Audit-Trail Management; GxP Evidence Reconciliation (Workflow A)
- Disputed PV awareness date, duplicate ICSR candidates, MedDRA version mismatch, listedness conflict → Pharmacovigilance Case-Intake and Signal-Support (Workflow B); Unit, Terminology and Reference-Data Standardisation; Authority, Effective-Date and Jurisdiction Management
- Cold-chain logger clocks and pallet association disputed; missing serialisation aggregation → Bounded Supply-Shortage and Cold-Chain Recovery Planning (Workflow C); Identity, Genealogy and Product-Master Resolution
- Sole-source excipient shortage, CMO capacity conflict, demand exceeds available stock → Bounded Supply-Shortage and Cold-Chain Recovery Planning (Workflow C); Supplier and Audit-Evidence Management
- Validation-state ambiguity and unapproved macro-enabled spreadsheet → Authority, Effective-Date and Jurisdiction Management; Source and Document Governance
- Untrusted supplier deviation PDF and stale/unsigned tool manifests → Source and Document Governance; Consent, Entitlement and Privacy Management where patient data is involved
- Inconsistent authority hierarchy; later timestamps not automatically more authoritative than approved signed records → Authority, Effective-Date and Jurisdiction Management
- Deliberate stakeholder conflicts (speed vs completeness; standardisation vs jurisdictional variation; minimisation vs preservation; bundled vendor vs substitutability; automation vs prespecified analysis) → All core subdomains via governance; Continuity, Reliability and Economy Management

### Ownership Signals

These are early ownership signals only. Final accountability must be defined in later stages.

- GxP Evidence Reconciliation (Workflow A) → Chief Quality Officer, EU Qualified Person, Quality release reviewers, Manufacturing, Laboratory/OOS owners, supplier-quality
- Pharmacovigilance Case-Intake and Signal-Support (Workflow B) → Global Head of Pharmacovigilance, PV case-intake staff, PV medical/safety reviewers, signal management
- Bounded Supply-Shortage and Cold-Chain Recovery Planning (Workflow C) → Supply Chain planning, logistics/serialisation/cold-chain, CMO and supplier-quality, Regulatory Affairs for market-authorisation constraints
- Identity, Genealogy and Product-Master Resolution → Quality, Manufacturing, Regulatory Affairs (IDMP), IT/master-data owners
- Unit, Terminology and Reference-Data Standardisation → Quality, Laboratory, Regulatory Affairs, Safety (MedDRA)
- Authority, Effective-Date and Jurisdiction Management → Regulatory Affairs, Quality, Privacy/Legal
- Consent, Entitlement and Privacy Management → Data Protection Officer, Legal, Clinical, Safety
- Source and Document Governance → Quality, Regulatory Affairs, Document management
- Supplier and Audit-Evidence Management → Supplier-quality, Procurement, Quality
- Regulatory and Inspection-Readiness Coordination → Regulatory Affairs, Quality, all evidence owners
- Evidence and Audit-Trail Management → Quality, Safety, Regulatory Affairs, IT/security, all accountable roles
- Continuity, Reliability and Economy Management → CISO, IT operations, finance/procurement

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

### Terms Needing Precise Definition

- Evidence-complete
- Conflict-visible
- Authority-respected
- Fail-closed
- Batch-review readiness
- Release-ready
- Release packet
- QP certification
- Genealogy
- Material/batch lineage
- OOS
- OOT
- Unit-conversion assumption
- Environmental monitoring excursion
- Deviation
- CAPA
- Change control
- Validation state
- Reporting clock
- Awareness date
- Duplicate ICSR
- MedDRA version
- Preferred term
- Listedness
- Expectedness
- Investigator brochure
- Core data sheet (CCDS)
- Local label
- Product-quality complaint
- Cold-chain excursion
- Temperature logger
- Pallet association
- Serialisation aggregation
- Sole-source excipient
- CMO capacity
- Allocation constraint
- Compassionate-use entitlement
- Market authorisation
- Effective date
- Jurisdiction
- Entitlement
- Consent
- Checkpoint state
- Provenance
- Audit trail
- Read-only advisory
- Abstention / no-answer

### Open Questions for Stage 3

- Which terms mean different things to Quality, Manufacturing, Laboratory, Pharmacovigilance, Regulatory, Supply, Privacy and Cybersecurity roles?
- Which terms need a clear owner or participant?
- Which terms represent a decision, status, event, document, task or exception?
- Which terms imply approval, release, completion, certification, allocation, shipment or an executed regulated action and are therefore unsafe if used loosely?
- Which terms require evidence or approval before they can be used in batch, safety or supply review material?

Stage 3 complete. Use the STAGE_4_INPUT_BLOCK as the main input for Stage 4.
