# A4 — Input From Stage 3: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

Use this file as the dedicated input attachment for **Stage 4 — Bounded Context Canvases**.

This file is extracted from the Stage 3 Ubiquitous Language Glossary output. It is intentionally limited to business-domain context. It does not solve the case, does not provide medical, regulatory or legal advice, does not resolve any product, batch, compound, safety, quality or supply issue, and does not create architecture or technical implementation.

---

## Stage 4 Input — Bounded Context Canvases

### Main Business Domain

**Governed evidence reconciliation and review support for regulated pharmaceutical workflows**

### Stage 4 Mission

Convert the Stage 3 ubiquitous language into clear bounded context canvases. Each bounded context must describe a distinct area of regulated pharmaceutical review work, its owned language, key business decisions or statuses, participants, dependencies, risks, and audit needs. The goal is to prevent one large, unclear evidence-reconciliation process and instead make business ownership visible across identity, batch-review, unit/terminology, authority, consent, PV, supply, source-governance, supplier-evidence and audit boundaries.

### Core Subdomains From Stage 2

- GxP Evidence Reconciliation for Batch-Review Readiness (Workflow A)
- Pharmacovigilance Case-Intake and Signal-Support (Workflow B)
- Bounded Supply-Shortage and Cold-Chain Recovery Planning (Workflow C)

### Supporting Subdomains From Stage 2

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

### Key Ubiquitous Language Terms To Preserve

- Governed evidence reconciliation and review support
- Evidence-complete
- Conflict-visible
- Provenance-backed
- Authority-respected
- Fail-closed
- Read-only advisory
- Batch-review readiness
- Release-ready
- Abstention / no-answer
- Genealogy
- Material/batch lineage
- Genealogy break
- OOS / OOT / invalid
- Release packet
- Release-packet completeness
- QP certification
- Unit-conversion assumption
- MedDRA version
- Preferred term
- Authority
- Effective date
- Jurisdiction
- Validation state
- Consent
- Entitlement
- Privacy boundary
- ICSR
- Duplicate ICSR
- Awareness date
- Reporting clock
- Reporting-clock reconstruction
- Listedness
- Expectedness
- Investigator brochure
- Core data sheet (CCDS)
- Local label
- Product-quality complaint
- Inventory status
- Cold-chain excursion
- Temperature logger
- Pallet association
- Serialisation aggregation
- Sole-source excipient
- CMO capacity
- Allocation constraint
- Compassionate-use entitlement
- Market authorisation
- Untrusted document
- Quarantine
- Audit trail
- Audit-capture gap
- Recommendation
- Draft
- Approval
- Override
- Escalation
- Final action
- Degraded mode
- Operate safely without AI

### Candidate Bounded Contexts To Test

The following candidates should be evaluated and refined. They are not technical services and must remain business-domain boundaries.

- Identity, Genealogy and Product Master Context
- GxP Batch Evidence Reconciliation Context
- Unit and Terminology Standardisation Context
- Authority, Effective-Date and Jurisdiction Context
- Consent, Entitlement and Privacy Context
- PV Case Intake and Signal Support Context
- Supply, Cold-Chain and Allocation Planning Context
- Source and Document Governance Context
- Supplier and Audit Evidence Context
- Audit, Evidence and Continuity Context

### Known Gaps / Exceptions To Carry Into Stage 4

- Missing single-use assembly lot SUA-88 branch in MES genealogy for batch NCB204-B24071 (present in warehouse consumption).
- Contract-laboratory concentration transmitted in mg/L while the receiving interface assumes µg/mL.
- Assay marked OOS by LIMS, OOT by statistical tooling and invalid by the laboratory notebook; open investigation.
- EU release packet lacks confirmation of a contract-site audit commitment.
- Batch-record step back-entered after network degradation.
- Audit capture disabled for 47 minutes during master-data repair.
- Disputed PV awareness date across vendor receipt, affiliate inbox and global safety database.
- Duplicate ICSR candidates under different product names.
- Two MedDRA versions changing the preferred term.
- Listedness conflict between investigator brochure, core data sheet and local label.
- Biologic shipment exceeds cold-chain range with disputed logger clocks and pallet association.
- Case-to-pallet serialisation aggregation missing after a line restart.
- Sole-source excipient contamination with eight-week recovery; CMO promises capacity to two sponsors; demand exceeds available stock.
- Validation-state ambiguity across inventories; unapproved macro-enabled spreadsheet in use.
- Untrusted supplier deviation PDF (hidden prompt-injection text) and stale/unsigned tool manifests.
- Deliberate stakeholder conflicts (speed vs completeness; standardisation vs jurisdictional variation; minimisation vs preservation; bundled vendor vs substitutability; automation vs prespecified analysis).

### Non-Negotiables To Preserve

- The AI never releases, rejects, reprocesses, re-labels or recalls a batch.
- The AI never makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions.
- The AI never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval.
- The AI never changes formulation, specification, clinical eligibility, safety-case disposition, batch release or recall decisions.
- Regulated accountability remains with the accountable Quality, Safety, Regulatory, Clinical and Supply roles.
- Evidence output must not be produced while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
- Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable.
- The system operates read-only and advisory; it prepares, reconciles, explains and packages evidence.
- No product, batch, safety, quality or supply issue is considered resolved merely because it has been identified.

### Ownership Signals From Stage 3

These are ownership signals only. Stage 4 should clarify context-level ownership without assigning final regulated decisions outside accountable human roles.

- Batch review and readiness involves the Chief Quality Officer, EU Qualified Person, quality release reviewers, manufacturing and laboratory/OOS owners.
- PV case intake and signal support involves the Global Head of Pharmacovigilance, case-intake staff, PV medical/safety reviewers and signal management.
- Supply-shortage and cold-chain recovery involves supply planning, logistics/serialisation/cold-chain, CMO/supplier quality and regulatory for market-authorisation constraints.
- Identity/genealogy/product master involves Quality, Manufacturing, Regulatory Affairs (IDMP) and IT/master-data owners.
- Unit/terminology/reference data involves Quality, Laboratory, Regulatory Affairs and Safety (MedDRA).
- Authority/effective-date/jurisdiction involves Regulatory Affairs, Quality and Privacy/Legal.
- Consent/entitlement/privacy involves the Data Protection Officer, Legal, Clinical and Safety.
- Source and document governance involves Quality, Regulatory Affairs and document management.
- Supplier and audit evidence involves supplier-quality, Procurement and Quality.
- Audit and continuity involves Quality, Safety, Regulatory Affairs, IT/security, CISO and finance/procurement.

### Open Questions for Stage 4

- Which contexts own decisions and statuses, and which only contribute evidence?
- Which terms belong inside one context and should not be overloaded elsewhere?
- Which context owns each known gap or exception?
- Which context is responsible for escalation when a required state (identity, unit, terminology, authority, validation, checkpoint) is unresolved?
- Which contexts can package evidence for inspection, and which never execute a regulated action?
- Which context records evidence, approvals, overrides and final actions?
- Which contexts need access to consent, entitlement and privacy status?
- Which boundaries are safety-critical because misunderstanding them could affect batch release/rejection, QP certification, PV dispositions, allocation, shipment or recall?

---

Stage 4 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 5.
