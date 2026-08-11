# A7 — Domain Model and Invariant Register: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## 1. Stage 7 Mission

Stage 7 converts the Stage 6 event storming board into a business-domain model for the NovaCura Therapeutics Group governed evidence-reconciliation case. The purpose is to identify the domain objects that matter across batch review, pharmacovigilance case intake and supply recovery, classify them as entities or value objects, define aggregate ownership boundaries, and capture business invariants that protect evidence completeness, conflict visibility, provenance, contextual authority, fail-closed behaviour on unresolved state, human accountability for regulated decisions, the read-only advisory boundary, and auditability.

This stage does not solve batch, safety or supply issues, approve batch release or rejection, disposition safety cases, allocate stock, ship product, initiate recalls, design architecture, introduce technical implementation, or provide medical, regulatory or legal advice. It only models the regulated pharmaceutical business domain and the rules that must remain true while unresolved workflow/domain gaps remain visible.

## 2. Input Summary

The Stage 7 input comes from the Stage 6 event storming board for the NovaCura Therapeutics Group governed evidence-reconciliation case.

The business scenario concerns the disputed biologics batch NCB204-B24071 (missing single-use assembly lot SUA-88 genealogy branch with a warehouse consumption record, mg/L vs µg/mL unit-conversion assumption, disputed OOS/OOT/notebook-invalid state, unverified contract-site audit commitment in the EU release packet, back-entered batch-record step), a sterile-area excursion near fill-finish with a corrected organism identification, emerging safety reports (duplicate ICSR candidates under different product names, disputed awareness date, MedDRA version mismatch, listedness conflict between the investigator brochure, core data sheet and local label), a cold-chain failure (disputed logger clocks and pallet association, missing case-to-pallet and serialisation aggregation), a sole-source excipient shortage with a CMO capacity conflict and demand exceeding stock, a ransomware event with a 47-minute audit-capture gap, and a multi-agency inspection request within 72 hours.

Bounded contexts referenced by Stage 6:

1. Identity, Genealogy and Product Master Context
2. GxP Batch Evidence Reconciliation Context
3. Unit and Terminology Standardisation Context
4. Authority, Effective-Date and Jurisdiction Context
5. Consent, Entitlement and Privacy Context
6. PV Case Intake and Signal Support Context
7. Supply, Cold-Chain and Allocation Planning Context
8. Source and Document Governance Context
9. Supplier and Audit Evidence Context
10. Audit, Evidence and Continuity Context

Known unresolved gaps carried into Stage 7:

- Genealogy branch gap for SUA-88 with a warehouse consumption record.
- Unapproved mg/L vs µg/mL unit-conversion assumption.
- Disputed OOS/OOT/notebook-invalid state with an open investigation.
- Unverified contract-site audit commitment in the EU release packet.
- Back-entered batch-record step; 47-minute audit-capture gap.
- Disputed PV awareness date; duplicate ICSR cluster; MedDRA version mismatch; listedness conflict (IB vs CCDS vs local label).
- Cold-chain logger clock and pallet association dispute; missing case-to-pallet and serialisation aggregation.
- Sole-source excipient contamination with eight-week recovery; CMO capacity conflict; demand exceeds available stock.
- Validation-state ambiguity; untrusted supplier deviation PDF and tool manifests; eConsent version asynchrony; pivotal-trial amendment not approved in one country.

Non-negotiables carried into Stage 7:

- The AI never releases, rejects, reprocesses, re-labels or recalls a batch.
- The AI never makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions.
- The AI never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval.
- The AI never changes formulation, specification, clinical eligibility, safety-case disposition, batch release or recall decisions.
- Regulated accountability remains with the accountable Quality, Safety, Regulatory, Clinical and Supply roles.
- Evidence output must not be produced while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
- Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable.
- The system operates read-only and advisory; it prepares, reconciles, explains and packages evidence.
- No product, batch, safety, quality or supply issue is considered resolved merely because it has been identified.

## 3. Domain Modeling Principles

- Model the regulated pharmaceutical review work, not the underlying software systems (LIMS, MES, eBR, QMS, RIM, safety databases).
- Entities have identity and lifecycle across the batch-review, PV case-intake and supply-recovery processes.
- Value objects describe facts, statuses, conventions, references, measurements, labels, or classifications without independent lifecycle.
- Aggregates define consistency boundaries where related business state must change together.
- Aggregate roots should own the state that they are accountable for, not every object in the case.
- Batch identity, material genealogy and product-master state are shared references, but they must not become a single giant aggregate that owns every review decision.
- GxP batch evidence reconciliation must remain distinct from PV case intake and from supply planning because each has distinct regulated human ownership.
- Authority, effective date, jurisdiction and validation state must be modeled as gating constraints on evidence use, not optional metadata; no system is universally authoritative and a later timestamp is not automatically more authoritative than an approved signed record.
- Consent, entitlement and privacy status must be modeled as access/use constraints for patient and participant data, not optional metadata.
- Auditability must be modeled as first-class evidence, not as a late documentation task.
- Unresolved gaps must remain explicit states or exceptions until a responsible human role records the appropriate review, escalation, approval, override, or closure.
- No domain model object should imply batch, safety or supply resolution where the case only provides a gap or exception.
- Fail-closed behaviour means no evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved; the domain model must represent abstention/no-answer as a first-class state.

## 4. Candidate Domain Object Classification

| Candidate object | Classification | Primary bounded context | Reason for classification | Notes / caution |
|---|---|---|---|---|
| Batch | External reference entity | Identity, Genealogy and Product Master | Has identity and lifecycle, but the batch-review workflow should not make Batch own every evidence state | Use as reference; do not create one giant batch aggregate |
| MaterialGenealogy | Aggregate root / entity | Identity, Genealogy and Product Master | Owns the lineage tree for a batch and its materials | Genealogy breaks remain visible; never silently repaired |
| WarehouseMovement | Entity / evidence artifact | Identity, Genealogy and Product Master | Source record of material consumption (SUA-88) | Contradictory lineage evidence remains visible |
| EbrStep | Entity / evidence artifact | GxP Batch Evidence Reconciliation | Batch-record step with checkpoint and audit state | Back-entered steps require checkpoint/audit evidence |
| LabResult | Entity / evidence artifact | GxP Batch Evidence Reconciliation / Unit and Terminology Standardisation | Laboratory result with reported unit and source | Do not disposition OOS/OOT state |
| OOSInvestigation | Entity | GxP Batch Evidence Reconciliation | Owns open investigation state for an out-of-specification result | Disputed OOS/OOT/invalid state remains open |
| EnvironmentalMonitoringResult | Entity / evidence artifact | GxP Batch Evidence Reconciliation | Environmental monitoring record near fill-finish | Excursion evidence must stay visible |
| Deviation | Entity | GxP Batch Evidence Reconciliation | Quality event record | Must link to investigation, CAPA, batch evidence |
| CAPA | Entity | GxP Batch Evidence Reconciliation / Supplier and Audit Evidence | Corrective and preventive action record | Closure must be evidence-backed |
| ChangeControl | Entity | GxP Batch Evidence Reconciliation / Authority, Effective-Date and Jurisdiction | Change record affecting validation or product state | Change and validation state must remain visible |
| CleaningValidation | Entity / evidence artifact | GxP Batch Evidence Reconciliation | Cleaning-validation evidence for campaign sequencing | High-potency campaign change remains visible |
| ReleasePacket | Aggregate root | GxP Batch Evidence Reconciliation | Owns release-packet element completeness | Must never be shown release-ready while elements are unresolved |
| SupplierAudit | Entity | Supplier and Audit Evidence | Audit record with commitments | Commitment verification is required before closure |
| CertificateOfAnalysis | Entity / evidence artifact | Supplier and Audit Evidence | Certificate evidence with unit and result state | Unit convention must be resolved before output |
| ICSR | Aggregate root | PV Case Intake and Signal Support | Owns safety case intake, receipts, terminology and listedness evidence | Final PV decisions remain human-owned |
| SafetyReceipt | Entity / evidence artifact | PV Case Intake and Signal Support | Receipt from vendor, affiliate inbox or global safety DB | Awareness-date source dispute remains visible |
| MedDRAVersion | Value object / external reference | Unit and Terminology Standardisation | Terminology version reference | Version mismatch changing preferred term stays visible |
| ListednessSource | Value object / evidence artifact | Authority, Effective-Date and Jurisdiction / PV Case Intake | IB, CCDS or local label reference | No winner is picked at this stage |
| ProductLabel | Entity / evidence artifact | Regulatory Affairs (RIM, labelling) | Local label version reference | Listedness conflict across label versions stays visible |
| InventoryItem | Entity | Supply, Cold-Chain and Allocation Planning | Inventory status and quantity reference | AI never changes inventory status |
| Shipment | Aggregate root | Supply, Cold-Chain and Allocation Planning | Owns shipment, logger and aggregation evidence | Do not disposition the shipment at this stage |
| TemperatureLogger | Entity / evidence artifact | Supply, Cold-Chain and Allocation Planning | Logger reading and clock reference | Disputed logger clock remains visible |
| SerialisationEvent | Entity / evidence artifact | Identity, Genealogy and Product Master / Supply | Case-to-pallet aggregation event | Aggregation gaps remain visible |
| AllocationConstraint | Entity | Supply, Cold-Chain and Allocation Planning | Market-authorisation, trial-demand and compassionate-use constraint | Options respect constraints; no allocation without approval |
| ExcipientSupplier | Entity / external reference | Supplier and Audit Evidence | Sole-source excipient supplier with contamination evidence | Eight-week recovery estimate is unresolved |
| CmoContract | Entity / external reference | Supplier and Audit Evidence / Supply | CMO capacity and contract evidence | Competing capacity commitments remain a visible constraint |
| MarketAuthorisation | Entity / evidence artifact | Authority, Effective-Date and Jurisdiction / Regulatory | Registration and jurisdiction basis | Authority is contextual per object, jurisdiction and date |
| EvidenceSource | Aggregate root | Source and Document Governance | Owns source trust, version, approval and quarantine state | Untrusted documents are quarantined before use |
| AuditRecord | Evidence/audit artifact | Audit, Evidence and Continuity | Captures auditable event envelope | Every event is auditable |
| Entitlement | Value object / entity | Consent, Entitlement and Privacy | Represents lawful access/use basis | Must be rechecked before patient/participant data is surfaced |
| User/AccessRole | Entity / external reference | Consent, Entitlement and Privacy | Represents role and access authorization | Shared accounts and stale entitlements are untrusted |
| CheckpointState | Value object | Authority, Effective-Date and Jurisdiction / GxP Batch Evidence Reconciliation | Represents checkpoint completeness for records and steps | Fail-closed while unresolved |
| NoAnswerRecord | Evidence/audit artifact | All contexts | Records abstention/no-answer on unresolved state | No-answer, not a guess |

## 5. Entity Register

| Entity | Identity | Lifecycle | Owner / accountable business role | Key states | Important relationships |
|---|---|---|---|---|---|
| Batch | Batch identifier (e.g., NCB204-B24071) | Created at manufacturing; persists across review, release and distribution scope | Quality / manufacturing / identity-genealogy owner | Identity verified, genealogy complete/incomplete, review readiness assessed, release decision pending, certified/rejected where applicable | MaterialGenealogy, ReleasePacket, LabResult, EbrStep, OOSInvestigation, BatchReviewReadiness |
| MaterialGenealogy | Genealogy tree identifier for a batch | Assembled from material and warehouse records; remains visible until identity/lineage resolved | Identity / genealogy / master-data owner | Complete, break present, consumption record found, aggregation state | Batch, MaterialLot, WarehouseMovement, SerialisationEvent |
| WarehouseMovement | Movement/consumption record identifier | Recorded at material consumption | Warehouse / manufacturing participant | Recorded, linked to genealogy branch, unmatched | MaterialGenealogy, MaterialLot (SUA-88) |
| EbrStep | Batch-record step identifier | Executed and recorded with checkpoint and audit state | Manufacturing / sterile-fill participant with quality review | Executed, recorded, back-entered, checkpoint verified, audit-capture gap related | Batch, CheckpointState, AuditRecord |
| LabResult | Result identifier | Generated by laboratory; remains visible with unit and state until disposition | Laboratory analyst / OOS owner | Reported, unit-unresolved, OOS, OOT, invalid-noted, under investigation | Batch, CertificateOfAnalysis, UnitConversionAssumption, OOSInvestigation |
| OOSInvestigation | Investigation identifier | Opened for an OOS/OOT result; remains open until accountable disposition | Laboratory analyst / OOS owner | Open, disputed, evidence gathered, awaiting disposition | LabResult, Batch, CAPA, Deviation |
| EnvironmentalMonitoringResult | Monitoring result identifier | Recorded near fill-finish; visible for excursion assessment | Manufacturing / sterile-fill participant | In-range, excursion, organism identification pending/corrected | Batch, Deviation, CampaignEvidence |
| Deviation | Deviation identifier | Recorded for quality events; linked to investigation and CAPA | Quality / manufacturing | Raised, investigated, CAPA linked, closure state | Batch, CAPA, OOSInvestigation, EnvironmentalMonitoringResult |
| CAPA | CAPA identifier | Created from deviation/investigation; remains until verified closure | Quality / supplier-quality | Open, implemented, verification pending, closed | Deviation, ChangeControl, SupplierAudit |
| ChangeControl | Change identifier | Raised for formulation, process or system change; remains until approved | Quality / Regulatory Affairs | Raised, assessed, approved, validation state linked | CleaningValidation, ValidationState, Batch |
| CleaningValidation | Validation identifier | Evidence for campaign sequencing; remains visible for batch evidence | Quality / manufacturing | Validated, campaign-changed, evidence incomplete | ChangeControl, Batch, EnvironmentalMonitoringResult |
| ReleasePacket | Release packet identifier | Assembled for batch review; status until QP certification | Quality release reviewer / EU Qualified Person | Incomplete, evidence gap list, readiness assessed, pending QP certification | Batch, SupplierAudit, CertificateOfAnalysis, ReleasePacketCompleteness |
| SupplierAudit | Audit identifier | Performed for supplier/contract site; commitments tracked | Supplier-quality / procurement | Audited, commitment open, commitment verified/unverified, closed | CmoContract, ExcipientSupplier, ReleasePacket, CAPA |
| CertificateOfAnalysis | Certificate identifier | Issued for batch or material; visible with result and unit state | Supplier-quality / laboratory | Issued, unit-unresolved, verified | Batch, LabResult, ReleasePacket |
| ICSR | ICSR identifier | Intake opened; progresses through receipts, terminology, duplicate/clock/listedness evidence; disposition remains human-owned | Global Head of Pharmacovigilance / PV case-intake staff | Intake opened, duplicate candidates identified, clock disputed, terminology conflicted, listedness evidence prepared, awaiting accountable PV review | SafetyReceipt, DuplicateICSRCandidate, ReportingClock, ListednessSource |
| SafetyReceipt | Receipt identifier | Recorded from vendor, affiliate inbox or global safety DB | PV case-intake staff | Received, awareness-date disputed, clock reconstruction evidence | ICSR, ReportingClock, AwarenessDate |
| MedDRAVersion | Version identifier | Reference data; alignment state tracked | Safety coder / terminology owner | Active, superseded, mismatch present | ICSR, PreferredTerm |
| ListednessSource | Source identifier | IB, CCDS or local label version; compared but not resolved | PV medical reviewer / Regulatory Affairs | Available, versioned, conflicting, no winner | ICSR, ProductLabel, MarketAuthorisation |
| ProductLabel | Label identifier and version | Local label version lifecycle; regulatory-owned | Regulatory Affairs (labelling) | Versioned, approved, current, superseded | ListednessSource, MarketAuthorisation |
| InventoryItem | Inventory record identifier | Inventory status and quantity; status never changed by AI | Supply Chain planner | In stock, quality-held, committed, shortage-related | AllocationConstraint, Shipment, ExcipientSupplier |
| Shipment | Shipment identifier | Dispatched; cold-chain evidence tracked; disposition human-owned | Logistics / cold-chain participant | Dispatched, logger disputed, pallet association disputed, excursion evidence prepared | TemperatureLogger, SerialisationEvent, AllocationOption |
| TemperatureLogger | Logger identifier | Assigned to shipment; readings and clock state tracked | Logistics / cold-chain participant | Reading recorded, clock disputed, evidence resolved/unresolved | Shipment, LoggerReading |
| SerialisationEvent | Serialisation event identifier | Recorded for case-to-pallet aggregation | Serialisation / logistics participant | Recorded, aggregation linked, aggregation gap present | Shipment, MaterialGenealogy |
| AllocationConstraint | Constraint identifier | Derived from policy, market authorisation, trial demand and compassionate use | Supply planner / patient-safety voice | Checked, respected, conflict present | InventoryItem, MarketAuthorisation, AllocationOption |
| ExcipientSupplier | Supplier identifier | Sole-source relationship with contamination evidence | Supplier-quality / procurement | Active, contaminated, recovery estimate eight weeks, unresolved | CmoContract, InventoryItem, AllocationOption |
| CmoContract | Contract identifier | Capacity commitment lifecycle; conflict remains visible | Procurement / CMO quality | Committed, capacity conflicted, capacity available | ExcipientSupplier, AllocationOption |
| MarketAuthorisation | Authorisation identifier | Registration lifecycle per jurisdiction | Regulatory Affairs | Approved, pending, jurisdiction-limited | ProductLabel, Batch, AllocationConstraint |
| EvidenceSource | Source identifier and version | Governed as trusted/quarantined before use | Source and Document Governance | Trusted, quarantined, versioned, approved | AuditRecord, ICSR, Batch, ReleasePacket |
| User/AccessRole | User/role identifier | Role lifecycle with entitlement state | Data Protection Officer / privacy owner / security | Entitled, stale entitlement, shared-account risk | Entitlement, EvidenceSource, AuditRecord |
| AuditRecord | Audit event identifier | Created for every auditable action or state change | Audit / quality oversight | Recorded, linked, immutable in business meaning | EvidenceSource, user/role, timestamp, batch/safety/supply object |

## 6. Value Object Register

| Value object | Describes | Examples from case | Validation or consistency concern |
|---|---|---|---|
| UnitOfMeasureConvention | Unit used to report and interpret a measurement | Contract-lab concentration in mg/L; receiving interface assumes µg/mL | Conversion assumption must be approved; no silent conversion; fail-closed on unit state |
| EffectiveDate | Date from which a record or source applies | Approval dates, registration dates, label effective dates, protocol version effective dates | A later timestamp is not automatically more authoritative than an approved signed record |
| Jurisdiction | Applicable regulatory region | EU release packet, country-specific label, one country not approving the amendment | Jurisdiction applicability must be resolved before authority is cited |
| AuthorityReference | Which source is authoritative for an object, jurisdiction and date | No system is universally authoritative; authority is contextual | Must be resolved before a source is cited as decisive |
| BatchStatusLabel | Business status of a batch | Identity verified, genealogy complete/incomplete, review readiness assessed, release pending | Review readiness must never be labelled as release approval |
| ReportingClockReconstruction | Reconstructed awareness-date timeline evidence | Vendor receipt, affiliate inbox, global safety DB timestamps | The clock is evidence for review; it is not set automatically |
| ListednessDeterminationReference | Reference for listedness/expectedness evidence | IB, core data sheet, local label | No winner is picked; conflict remains visible |
| AllocationConstraintReason | Reason a constraint applies to an option | Market authorisation, trial demand, compassionate-use entitlement, policy | Constraint rationale must be traceable to sources |
| LoggerReading | Temperature reading with logger identity and clock | Biologic shipment exceeds range; disputed logger clocks | Logger clock and pallet association must be resolved before options are trusted |
| AggregationLink | Link between packaging levels | Case-to-pallet aggregation missing after line restart | Missing linkage remains visible; do not assume the link |
| ProvenanceCitation | Citation of the source of an evidence fact | Genealogy record, lab result source, safety receipt, supplier audit | Every evidence fact links to a governed source |
| NoAnswerReason | Reason abstention/no-answer is declared | Unresolved unit state, unresolved validation state, disputed awareness date | No-answer is a legitimate output; a guess is not |
| ConsentStatus | Lawful basis and consent boundary state | eConsent version asynchrony with the trial amendment | Must be rechecked before patient/participant data is surfaced |
| EntitlementStatus | Role/access authorization state | Stale tool-manifest entitlements, shared accounts | Access/use must not occur without legitimate entitlement |
| CheckpointState | Completeness state of a record or step | Back-entered batch-record step checkpoint, validation state | Fail-closed while checkpoint state is unresolved |
| ValidationState | Application/system validation status | Validated vs conditionally released vs research-only across inventories | Ambiguous validation state remains unresolved |
| DuplicateCandidateReason | Rationale that cases are duplicate candidates | Same event under different product names | Surfaces candidates; does not confirm duplicates |
| PreferredTerm | MedDRA term assigned under a terminology version | Two MedDRA versions change the preferred term | Terminology state remains conflict-visible |
| Timestamp | Time of event/action | Receipt, review, approval, override, escalation, closure timing | Required for auditability and clock reconstruction |
| RoleName | Human role involved | EU QP, Quality release reviewer, PV medical reviewer, Supply Chain VP | Role must not hide accountability |

## 7. Aggregate Register

| Aggregate root | Owned objects | Consistency responsibility | Business owner | What the aggregate must not own |
|---|---|---|---|---|
| BatchEvidenceAggregate | Batch reference, MaterialGenealogy, EbrStep, LabResult, OOSInvestigation, EnvironmentalMonitoringResult, Deviation, CAPA, ChangeControl, CleaningValidation, ReleasePacket, SupplierAudit reference, CertificateOfAnalysis reference, BatchReviewReadiness | Ensures batch-review readiness evidence is complete, conflict-visible and provenance-backed, and that no batch is shown release-ready while any genealogy branch or release-packet element is unresolved or unverified | Quality release reviewer / EU Qualified Person ownership boundary | Batch release/rejection/reprocess/re-label/recall; QP certification decision; unit-conversion acceptance; OOS/OOT disposition; formulation/specification changes |
| ProductAndMarketAuthorisationAggregate | ProductLabel, MarketAuthorisation, EffectiveDate, Jurisdiction, AuthorityReference, ValidationState | Ensures authority, effective date, jurisdiction and validation state are resolved before product/batch evidence is cited | Regulatory Affairs (RIM, labelling, IDMP) | Batch disposition, PV dispositions, allocation, shipment |
| PVCaseAggregate | ICSR, SafetyReceipt, MedDRAVersion, PreferredTerm, ListednessSource, ReportingClockReconstruction, DuplicateCandidateReason, Consent/Entitlement status reference | Ensures intake completeness and duplicate/terminology/clock/listedness evidence is visible and attributed for accountable PV review | Global Head of Pharmacovigilance / PV case-intake staff | Final seriousness, causality, expectedness, reportability or signal-confirmation decisions; safety-case disposition |
| ColdChainShipmentAggregate | Shipment, TemperatureLogger, LoggerReading, AggregationLink, SerialisationEvent, cold-chain evidence state | Ensures logger clock, pallet association and aggregation evidence is resolved before shipment options are trusted | Logistics / cold-chain participant with accountable supply owner | Shipment disposition, excursion disposition, inventory status change, recall |
| SupplyAllocationAggregate | InventoryItem, AllocationConstraint, AllocationConstraintReason, ExcipientSupplier, CmoContract, demand and market-authorisation references, AllocationOption | Ensures options are traceable and policy-bounded and that no allocation, reservation, shipment or recall is executed without explicit authorised human approval | Supply Chain planner with authorised human approval owner | Allocation execution, capacity reservation, inventory status change, shipment, recall initiation |
| EvidenceSourceAggregate | EvidenceSource, version/approval/quarantine state, ProvenanceCitation | Ensures sources are trusted, versioned, approved and auditable before evidence is used | Source and Document Governance | Content decisions, batch/safety/supply decisions |
| AuditAggregate | AuditRecord, ApprovalRecord, OverrideRecord, EscalationRecord, AbstentionRecord, EvidencePackage, AuditCaptureGap state | Ensures every recommendation, draft, approval, override, release, escalation, action, outcome and closure is auditable, and audit-capture gaps remain visible | Audit / quality oversight | Business decision authority; it records decisions but does not make them |

## 8. Aggregate Detail Canvases

### 8.1 BatchEvidenceAggregate

| Field | Detail |
|---|---|
| Purpose | Coordinate batch-review readiness evidence for Workflow A and preserve visibility of unresolved identity, genealogy, unit, OOS/OOT, supplier and release-packet gaps. |
| Owned terms | Batch review, batch-review readiness, material genealogy, genealogy break, batch-record step, laboratory result, OOS, OOT, environmental monitoring excursion, deviation, CAPA, change control, cleaning validation, release packet, release-packet completeness, supplier evidence, QP-certification evidence. |
| Owned state | Identity verification state, genealogy completeness state, unit-conversion state, result state, excursion evidence state, supplier-evidence state, release-packet completeness state, batch-review readiness state, unresolved-gap list. |
| Commands / activities that affect it | Open batch review, verify batch/product identity, request lineage check, detect missing lineage branch, compare reported vs assumed units, abstain on unresolved unit state, surface conflicting result states, report environmental excursion, correct organism identification, request commitment verification, detect back-entered record, assess release-packet completeness, assess batch-review readiness, prepare evidence for QP certification. |
| Events it emits or records | Batch review opened, genealogy branch gap detected (SUA-88), unit-conversion conflict detected, unit-conversion state declared unresolved (no-answer), OOS/OOT state disagreement surfaced, excursion detected, organism identification corrected, supplier-audit commitment found unverified, back-entered step detected, release packet marked evidence-incomplete, batch-review readiness assessed with unresolved gaps, QP certification decision pending. |
| Invariants it enforces | No evidence output while identity, genealogy, unit, terminology, validation or checkpoint state is unresolved; batch must not be shown release-ready while any genealogy branch or release-packet element is unresolved or unverified; review readiness is not release approval or QP certification. |
| External dependencies | Identity/genealogy state, unit/terminology state, authority/effective-date/jurisdiction state, supplier/audit evidence, validation state, audit record. |
| Audit needs | Batch identity, genealogy-break identification and ownership, unit-conversion conflict, OOS/OOT dispute, supplier-audit verification state, release-packet completeness, readiness assessment, evidence-gap ownership, QP pending status. |

### 8.2 ProductAndMarketAuthorisationAggregate

| Field | Detail |
|---|---|
| Purpose | Represent the authority, effective-date, jurisdiction and validation basis that determines which record is decisive for a product or batch in a given market. |
| Owned terms | Authority, authoritative source, effective date, jurisdiction, approval date, signed record, validation state, product label, market authorisation, protocol version. |
| Owned state | Authority assignment per object/jurisdiction/date, effective-date state, jurisdiction applicability, validation state, label version state, registration state. |
| Commands / activities that affect it | Check validation state, verify identity and product-master state, align terminology versions, compare listedness sources, check authority/effective-date basis. |
| Events it emits or records | Authority basis resolved/flagged, validation state found ambiguous, label version conflict surfaced, amendment jurisdiction applicability gap surfaced, later-timestamp-not-authoritative warning recorded. |
| Invariants it enforces | No evidence while authority, effective date, jurisdiction or validation state is unresolved; a later timestamp is not automatically more authoritative than an approved signed record; source authority must be resolved before a source is cited as decisive. |
| External dependencies | RIM/IDMP reference data, signed records, approvals, labels, protocol versions, validation inventory. |
| Audit needs | Authority rationale, effective-date determination, jurisdiction basis, validation-state evidence, label/registration version. |

### 8.3 PVCaseAggregate

| Field | Detail |
|---|---|
| Purpose | Support PV case intake, duplicate detection, terminology normalisation, source authority, reporting-clock reconstruction, listedness evidence and multilingual review (Workflow B) without making final PV decisions. |
| Owned terms | ICSR, duplicate ICSR, awareness date, reporting clock, reporting-clock reconstruction, seriousness, causality, expectedness, listedness, IB, core data sheet, local label, preferred term, MedDRA version, product-quality complaint, reportability, signal confirmation, case-intake completeness. |
| Owned state | Intake completeness, duplicate-candidate status, awareness-date reconstruction state, terminology alignment state, listedness-source evidence state, multilingual review status, consent/entitlement status. |
| Commands / activities that affect it | Open PV case intake, validate consent and entitlement, detect duplicate candidates, reconstruct reporting clock, align terminology versions, compare listedness sources, request multilingual review, prepare case-review material, prepare clock evidence. |
| Events it emits or records | PV case intake opened, consent/entitlement check requested, ICSR duplicate cluster identified, awareness-date dispute surfaced, MedDRA preferred-term conflict surfaced, listedness conflict surfaced (IB vs CCDS vs local label), reporting-clock evidence prepared for review, multilingual review requested, case-review material prepared for accountable PV review. |
| Invariants it enforces | No final PV seriousness, causality, expectedness, reportability or signal-confirmation decision may be attributed to the AI; duplicate candidates are surfaced, not confirmed; the clock is evidence, not set automatically; listedness sources remain conflict-visible; entitlement/consent must be rechecked before patient/participant data is surfaced. |
| External dependencies | Safety receipts, MedDRA versions, IB/CCDS/local label, product-quality complaints, consent/entitlement state, authority/effective-date state. |
| Audit needs | Receipts, intake timestamps, duplicate-detection rationale, clock-reconstruction evidence, terminology version, listedness sources, reviewer routing, consent/entitlement checks. |

### 8.4 ColdChainShipmentAggregate

| Field | Detail |
|---|---|
| Purpose | Own cold-chain shipment evidence (logger readings, clocks, pallet association, aggregation) so that recovery options are built on resolved evidence. |
| Owned terms | Cold-chain excursion, temperature logger, logger clock, pallet association, serialisation aggregation, case-to-pallet aggregation, shipment, cold-chain evidence state. |
| Owned state | Logger-reading state, logger-clock state, pallet-association state, aggregation-link state, excursion-evidence state. |
| Commands / activities that affect it | Detect temperature excursion, detect aggregation gap, check aggregation hierarchy, record logger readings, resolve pallet association. |
| Events it emits or records | Cold-chain excursion detected (logger clock/pallet disputed), case-to-pallet aggregation gap detected, serialisation aggregation gap detected, logger clock dispute surfaced. |
| Invariants it enforces | Cold-chain evidence must be resolved before options are trusted; aggregation gaps remain visible with ownership; no shipment disposition or recall by the AI. |
| External dependencies | Identity/genealogy/aggregation state, authority/effective-date/jurisdiction state, logistics records. |
| Audit needs | Logger basis, pallet link, aggregation state, excursion evidence, source citations. |

### 8.5 SupplyAllocationAggregate

| Field | Detail |
|---|---|
| Purpose | Generate traceable, policy-bounded supply-shortage and cold-chain recovery options (Workflow C) without executing any allocation. |
| Owned terms | Inventory status, excipient shortage, recovery estimate, CMO capacity, CMO capacity conflict, allocation constraint, allocation policy, market authorisation, trial demand, compassionate-use entitlement, allocation option, human approval. |
| Owned state | Inventory status visibility, shortage state, capacity-availability state, allocation-constraint check state, allocation-option status, approval-request status. |
| Commands / activities that affect it | Surface shortage, surface capacity conflict, check allocation constraints, generate traceable options, request authorised approval. |
| Events it emits or records | Excipient shortage surfaced, CMO capacity conflict surfaced, allocation constraint check completed, allocation option proposed (awaiting human approval), human approval requested for allocation option. |
| Invariants it enforces | No allocation recommendation may be executed without explicit authorised human approval; no inventory status change, capacity reservation, stock allocation, shipment or recall initiation may be performed by the AI; compassionate-use entitlements and trial demand bind the options. |
| External dependencies | Inventory, quality status, market authorisation, demand forecast, cold-chain evidence, CMO capacity, allocation policy, supplier evidence. |
| Audit needs | Option generation, evidence used for each option, constraint rationale, approval requests, escalation records. |

### 8.6 EvidenceSourceAggregate

| Field | Detail |
|---|---|
| Purpose | Govern trusted, versioned, approved, audit-trailed sources and quarantine untrusted documents and manifests before use as evidence. |
| Owned terms | Source, source authority, document version, approved document, untrusted document, manifest, quarantine, transcription, signed original. |
| Owned state | Source trust state, version state, approval state, quarantine state, manifest currency. |
| Commands / activities that affect it | Register source, verify version/approval, quarantine untrusted document, verify manifest, cite provenance. |
| Events it emits or records | Source trusted, source quarantined, prompt-injection PDF quarantined, tool manifest flagged stale/unsigned, provenance citation recorded. |
| Invariants it enforces | Untrusted sources are quarantined until governance review; evidence must be provenance-backed; no evidence while source state is unresolved. |
| External dependencies | Quality, Regulatory Affairs, document management, IT/security. |
| Audit needs | Quarantine record, version history, approval state, source attribution, manifest verification. |

### 8.7 AuditAggregate

| Field | Detail |
|---|---|
| Purpose | Preserve traceability of every recommendation, draft, approval, override, release, escalation, action, outcome and closure; keep audit-capture gaps visible; package evidence for inspection. |
| Owned terms | Audit trail, audit event envelope, audit-capture gap, recommendation, draft, approval, override, escalation, final action, evidence package, degraded mode, operate safely without AI, continuity requirement. |
| Owned state | Audit-trail completeness, audit-capture-gap state, degraded-mode state, evidence-package state, continuity state. |
| Commands / activities that affect it | Capture audit event envelope, detect audit-capture gap, activate AI-off operation, open repair window, assemble evidence package, escalate unresolved state, abstain on unresolved state, record human approval, record human override. |
| Events it emits or records | Audit record captured, audit-capture gap detected (47 minutes), AI-off continuity mode activated, master-data repair window opened, inspection evidence request received (72h), evidence package assembled for inspection, escalation created, no-answer declared, human approval recorded, human override recorded. |
| Invariants it enforces | Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable; audit-capture gaps remain visible; the organisation must operate safely without AI; evidence output only when required states are resolved. |
| External dependencies | All business contexts and human owners. |
| Audit needs | This aggregate owns the audit/evidence need itself: who did what, from what source, when, why, under which approval or override, and what final action resulted. |

## 9. Invariant Register

| Invariant ID | Invariant statement | Aggregate / context | Source rule or case fact | Human owner | Failure risk if violated | Audit evidence required |
|---|---|---|---|---|---|---|
| INV-001 | An evidence output must not be produced while product/batch/compound identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved. | All aggregates | Non-negotiable 6 | Accountable workflow owner per context | A guess or premature output is treated as evidence | No-answer declaration, unresolved-state record, reason, owner |
| INV-002 | A batch must not be shown as release-ready while any genealogy branch or release-packet element is unresolved or unverified. | BatchEvidenceAggregate | NCB204-B24071 SUA-88 genealogy gap; unverified contract-site audit commitment | Quality release reviewer | Batch review proceeds against incomplete lineage or packet | Genealogy-break record, release-packet completeness state, gap ownership |
| INV-003 | Genealogy breaks must remain visible and must never be silently repaired. | BatchEvidenceAggregate / Identity, Genealogy and Product Master | SUA-88 present in warehouse consumption but missing from one MES branch | Identity / genealogy / master-data owner | A merge hides a lineage contradiction | Genealogy-break identification, source records, owner |
| INV-004 | Unit-conversion assumptions must be approved; no silent unit conversion is permitted. | Unit and Terminology Standardisation / BatchEvidenceAggregate | Contract-lab mg/L vs receiving-interface µg/mL | Laboratory / interface owner with quality acceptance | A 1000x unit error enters release evidence | Conversion mapping, approval/override record, no-answer state |
| INV-005 | A disputed OOS/OOT/notebook-invalid result state remains open and visible; it is not dispositioned by the AI. | BatchEvidenceAggregate | LIMS marks OOS, statistical tool marks OOT, notebook labels invalid | Laboratory analyst / OOS owner | The assay is dispositioned without accountable decision | Conflicting states, sources, open investigation record |
| INV-006 | An unverified supplier-audit commitment is not treated as closed. | Supplier and Audit Evidence / BatchEvidenceAggregate | EU release packet lacks confirmation of one contract-site audit commitment | Supplier-quality / quality reviewer | A gap is hidden inside the release packet | Verification request, verification state, packet status |
| INV-007 | Back-entered batch-record steps require checkpoint and audit evidence. | BatchEvidenceAggregate / AuditAggregate | Batch-record step back-entered after network degradation | Manufacturing / quality reviewer | A back-entered step is accepted without checkpoint evidence | Detection record, timestamps, checkpoint state |
| INV-008 | Batch-review readiness is not release approval or QP certification. | BatchEvidenceAggregate | Batch-review readiness assessed with unresolved gaps | Quality release reviewer / EU QP | Readiness is mistaken for a release or certification | Readiness assessment, pending-status record, evidence package |
| INV-009 | No final PV seriousness, causality, expectedness, reportability or signal-confirmation decision may be attributed to the AI. | PVCaseAggregate | Non-negotiable 2 | Global Head of Pharmacovigilance / PV medical reviewer | A final safety decision is displaced from accountable reviewers | Prepared review material, reviewer routing, decision ownership |
| INV-010 | Duplicate ICSR candidates are surfaced but never confirmed as duplicates by the AI. | PVCaseAggregate | Duplicate cluster under different product names | PV case-intake staff / PV reviewer | Cases are merged or split without accountable review | Duplicate rationale, candidates, reviewer |
| INV-011 | The reporting clock is evidence; the awareness date is not set automatically. | PVCaseAggregate / Authority, Effective-Date and Jurisdiction | Awareness date differs across vendor receipt, affiliate inbox and global safety DB | PV case-intake staff / PV reviewer | A disputed awareness date is treated as settled | Clock-reconstruction evidence, source basis |
| INV-012 | Terminology state remains conflict-visible; the preferred term is not chosen automatically. | Unit and Terminology Standardisation / PVCaseAggregate | Two MedDRA versions change the preferred term | Safety coder / terminology owner | A mis-coded case is treated as correctly coded | Version-alignment evidence, source |
| INV-013 | Listedness sources remain conflict-visible; no winner is picked. | PVCaseAggregate / Authority, Effective-Date and Jurisdiction | IB, core data sheet and local label are not aligned on expectedness | PV medical reviewer / Regulatory Affairs | Expectedness evidence is prematurely resolved | Listedness-source versions, conflict record |
| INV-014 | Entitlement/consent must be rechecked before patient/participant data is surfaced. | Consent, Entitlement and Privacy / PVCaseAggregate | eConsent version asynchrony with the trial amendment | Data Protection Officer / privacy owner | Patient data is used without lawful basis | Consent/entitlement check, access/use record |
| INV-015 | Cold-chain evidence must be resolved before shipment options are trusted. | ColdChainShipmentAggregate | Logger clocks and pallet association disputed | Logistics / cold-chain participant with accountable supply owner | Recovery options rest on disputed temperature evidence | Logger basis, pallet link, excursion evidence |
| INV-016 | Aggregation gaps remain visible; missing case-to-pallet linkage is not assumed. | Identity, Genealogy and Product Master / ColdChainShipmentAggregate | Aggregation missing after line restart | Serialisation / logistics participant | A shipment is trusted without aggregation linkage | Aggregation-state record, gap ownership |
| INV-017 | No allocation recommendation may be executed without explicit authorised human approval. | SupplyAllocationAggregate | Allocation option proposed (awaiting human approval) | Supply Chain VP / authorised Quality owner | An advisory option is executed as an allocation | Option rationale, approval request, approval record |
| INV-018 | No inventory status change, capacity reservation, stock allocation, shipment or recall initiation may be performed by the AI. | SupplyAllocationAggregate | Non-negotiable 3 | Supply Chain / Quality accountable owner | A regulated supply action occurs without human approval | Approval request, human approval, action record |
| INV-019 | Source authority must be resolved before a source is cited as decisive. | EvidenceSourceAggregate / Authority, Effective-Date and Jurisdiction | Authority hierarchy inconsistent; later timestamps not automatically authoritative | Regulatory Affairs / source governance | The wrong record is treated as binding | Authority rationale, effective date, jurisdiction, source version |
| INV-020 | Untrusted documents and manifests are quarantined until governance review. | EvidenceSourceAggregate | Prompt-injection supplier PDF, stale/unsigned tool manifests | Source and Document Governance | Poisoned content is treated as evidence | Quarantine record, source trust state |
| INV-021 | Ambiguous validation state remains unresolved; an unvalidated system is not treated as authoritative. | Authority, Effective-Date and Jurisdiction / EvidenceSourceAggregate | Validated vs conditionally released vs research-only across inventories | Validation / quality owner | A research-only or conditionally released system is treated as validated | Validation-state evidence, owner |
| INV-022 | The audit-capture gap remains visible and is not filled silently. | AuditAggregate | Audit capture disabled for 47 minutes during master-data repair | Audit / quality oversight | Work appears auditable when the trail is incomplete | Gap detection, duration, owner |
| INV-023 | The organisation must operate safely without AI inference. | AuditAggregate | Ransomware isolation of manufacturing historians; MES/QMS degraded | CISO / IT operations | Operation stalls or resorts to unsafe inference | AI-off continuity activation, continuity state |
| INV-024 | Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable. | AuditAggregate | Non-negotiable 7 | Audit / quality oversight | Missing accountability and weak traceability | Audit event envelope, source, owner, timestamp |
| INV-025 | Human overrides must record the authorized owner and reason. | AuditAggregate | Override must not be invisible or unaudited | Accountable Quality / PV / Supply / Regulatory owner | An unsafe or unexplained deviation occurs | Override record, reason, owner, timestamp |
| INV-026 | The AI never releases, rejects, reprocesses, re-labels or recalls a batch. | BatchEvidenceAggregate | Non-negotiable 1 | EU Qualified Person / Quality release reviewer | A batch disposition is produced by the AI | Human disposition record, evidence package |

## 10. Unresolved Exceptions Captured as Domain State

| Unresolved issue | Domain representation | Owning aggregate/context | Allowed Stage 7 treatment | Not allowed at this stage |
|---|---|---|---|---|
| Missing SUA-88 genealogy branch (present in warehouse consumption) | GenealogyBreak with WarehouseMovement reference | BatchEvidenceAggregate / Identity, Genealogy and Product Master | Keep visible as an unresolved genealogy break with identity/lineage ownership | Do not repair the lineage or merge the records |
| mg/L vs µg/mL unit-conversion assumption | UnitOfMeasureConvention unresolved state | Unit and Terminology Standardisation | Keep as an unapproved conversion assumption; fail-closed on unit state | Do not apply or approve the conversion |
| OOS vs OOT vs notebook-invalid dispute | LabResult disputed state with OOSInvestigation | BatchEvidenceAggregate | Keep as a disputed assay state with open investigation ownership | Do not disposition the assay |
| Unverified contract-site audit commitment | SupplierAudit commitment unverified state | Supplier and Audit Evidence / BatchEvidenceAggregate | Keep as a supplier-evidence gap in the release packet | Do not treat the commitment as closed |
| Back-entered batch-record step | EbrStep back-entered state with CheckpointState | BatchEvidenceAggregate / AuditAggregate | Keep as a checkpoint and audit-evidence gap | Do not silently accept or reject the step |
| 47-minute audit-capture gap | AuditCaptureGap state | AuditAggregate | Keep as an audit-trail completeness gap | Do not fill the gap silently |
| Disputed PV awareness date | ReportingClockReconstruction dispute | PVCaseAggregate | Keep as a reporting-clock reconstruction dispute | Do not set the clock |
| Duplicate ICSR cluster under different product names | DuplicateICSRCandidate set | PVCaseAggregate | Keep as duplicate candidates pending accountable review | Do not merge or split the cases |
| Two MedDRA versions changing the preferred term | MedDRAVersion mismatch state | Unit and Terminology Standardisation / PVCaseAggregate | Keep as a terminology-state conflict | Do not choose a preferred term |
| Listedness conflict between IB, CCDS and local label | ListednessSource conflict state | PVCaseAggregate / Authority, Effective-Date and Jurisdiction | Keep as a listedness-source conflict | Do not pick a winner |
| Cold-chain logger clock and pallet association dispute | LoggerReading/LoggerClock/pallet-association dispute | ColdChainShipmentAggregate | Keep as disputed cold-chain evidence | Do not disposition the shipment |
| Missing case-to-pallet aggregation after line restart | AggregationLink gap | Identity, Genealogy and Product Master / ColdChainShipmentAggregate | Keep as an aggregation gap requiring evidence linkage | Do not assume the linkage |
| Sole-source excipient contamination with eight-week recovery | ExcipientShortage constraint | SupplyAllocationAggregate | Keep as a supply-shortage constraint; generate options only | Do not allocate or purchase without human approval |
| CMO capacity promised to two sponsors | CmoContract capacity-conflict state | SupplyAllocationAggregate / Supplier and Audit Evidence | Keep as a visible sourcing constraint | Do not reserve capacity |
| Demand exceeds available stock | AllocationConstraint conflict with AllocationOption pending | SupplyAllocationAggregate | Prepare policy-bounded options; require explicit authorised human approval | Do not allocate stock or ship product |
| Validation-state ambiguity | ValidationState unresolved | Authority, Effective-Date and Jurisdiction | Keep as checkpoint and source-governance state unresolved | Do not treat the system as authoritative |
| Untrusted supplier deviation PDF and tool manifests | EvidenceSource quarantined state | EvidenceSourceAggregate | Keep as untrusted-source governance | Do not use extracted PDF text as evidence |
| Authority hierarchy inconsistent; later timestamps not automatically authoritative | AuthorityReference contextual state | Authority, Effective-Date and Jurisdiction | Keep as a contextual-authority gap | Do not treat a later timestamp as authoritative |
| eConsent version asynchrony with the pivotal-trial amendment | ConsentStatus/EntitlementStatus unresolved | Consent, Entitlement and Privacy / PVCaseAggregate | Keep as a consent/entitlement gap | Do not use data without lawful basis |
| Ransomware isolation of manufacturing historians; MES/QMS degraded | ContinuityState AI-off mode | AuditAggregate | Keep as a continuity requirement | Do not stop operating safely when AI is unavailable |
| Pivotal-trial amendment not approved in one country | Jurisdiction-applicability gap | Authority, Effective-Date and Jurisdiction | Keep as a jurisdiction-applicability gap | Do not treat the amendment as approved everywhere |

## 11. Human Decision Ownership Preserved in the Model

| Decision or action area | Human owner / accountable role | Domain model enforcement | Must not be bypassed |
|---|---|---|---|
| Batch release / rejection / reprocess / re-label / recall | EU Qualified Person / accountable Quality role | BatchEvidenceAggregate tracks readiness; release/rejection events are never advisory outputs | No workflow state should imply an AI batch disposition |
| QP certification (final batch certification) | EU Qualified Person | ReleasePacket and BatchReviewReadiness keep QP-certification decision pending and human-owned | QP certification cannot be attributed to the AI |
| OOS/OOT disposition and investigation conclusion | Laboratory analyst / OOS owner | OOSInvestigation keeps disputed result state open until accountable disposition | The assay cannot be dispositioned by the model |
| Unit-conversion acceptance | Laboratory / interface owner with Quality acceptance | UnitOfMeasureConvention requires approved conversion state | No silent unit conversion |
| Supplier-audit verification and commitment closure | Supplier-quality / quality reviewer | SupplierAudit commitment must be independently verified before treated as closed | An unverified commitment cannot be closed |
| PV seriousness, causality, expectedness, reportability determinations | PV medical/safety reviewer | PVCaseAggregate prepares evidence; final PV decisions remain human-owned | Final PV decisions cannot be attributed to the AI |
| Duplicate confirmation | PV reviewer | DuplicateICSRCandidate surfaces candidates only | Duplicates cannot be confirmed or merged by the model |
| Awareness-date acceptance | PV case-intake staff / PV reviewer | ReportingClockReconstruction is evidence for review | The clock cannot be set automatically |
| Listedness determination per jurisdiction/source | PV medical reviewer / Regulatory Affairs | ListednessSource conflict remains visible | No winner is picked by the model |
| Signal confirmation | Signal management | Signal-support evidence is prepared; confirmation is human-owned | Signals cannot be confirmed by the AI |
| Allocation decision | Supply Chain VP / authorised Quality owner | SupplyAllocationAggregate requires explicit authorised human approval | No allocation without human approval |
| Cold-chain excursion disposition | Logistics / cold-chain accountable owner with Quality input | ColdChainShipmentAggregate keeps excursion evidence visible; disposition is human-owned | The shipment cannot be dispositioned by the model |
| Recall decision | Quality / Regulatory accountable roles | Recall initiation requires human decision and audit trail | The AI never initiates a recall |
| Override of any of the above | Accountable owner for the decision type | OverrideRecord requires owner, reason, timestamp | An override cannot be invisible or unaudited |
| Authority/effective-date/jurisdiction determination | Regulatory Affairs / master-data governance | ProductAndMarketAuthorisationAggregate resolves authority contextually | No system is treated as universally authoritative |

## 12. Audit and Evidence Requirements

The domain model must make the following traceable:

- Batch identity and product-master reference used for review; identity-match evidence and source.
- Genealogy-break identification for SUA-88 and its ownership; warehouse consumption record attribution.
- Unit-conversion conflict and no-answer declaration with mapping and source.
- OOS/OOT/invalid dispute evidence and open investigation ownership.
- Supplier-audit verification state and release-packet completeness state.
- Batch-review readiness assessment, evidence-gap ownership, and QP-certification pending status.
- Back-entered batch-record step detection, timestamps, and checkpoint state.
- PV intake opening, receipts, duplicate-detection rationale, clock-reconstruction evidence, MedDRA version, listedness sources, and reviewer routing.
- Consent/entitlement checks before patient/participant data is surfaced.
- Cold-chain logger basis, pallet association, aggregation state, shortage, capacity conflict, and allocation-constraint rationale.
- Approval requests, human approvals, human overrides, escalations, actions, outcomes and closures.
- The audit event envelope for every workflow event; the 47-minute audit-capture gap remains visible.
- AI-off continuity activation, repair-window operation, and the 72-hour inspection evidence package with a manifest and source citations.
- Evidence source trust, version, approval and quarantine state; provenance citations.

Each audit record should preserve: object identity (batch, product, case, shipment, source), source evidence, owner/role, status, decision or action, approval/rejection/override where applicable, reason where applicable, timestamp, and release or closure status where applicable.

## 13. Boundary Warnings

- Do not treat LIMS, MES, eBR, QMS, RIM or the safety database as the domain model or as universally authoritative.
- Do not let Batch or Product become a single aggregate that owns all review work.
- Do not merge PV case intake into batch evidence reconciliation; each has distinct regulated human ownership.
- Do not merge supply allocation into batch review; allocation execution requires explicit authorised human approval.
- Do not let BatchEvidenceAggregate own batch release, rejection, reprocess, re-label, recall or QP certification; it owns review readiness only.
- Do not let PVCaseAggregate own final seriousness, causality, expectedness, reportability or signal-confirmation decisions.
- Do not let SupplyAllocationAggregate execute inventory status changes, capacity reservations, stock allocation, shipments or recall initiations.
- Do not let Unit and Terminology Standardisation silently apply a conversion or pick a preferred term.
- Do not let Identity, Genealogy and Product Master silently resolve a genealogy break or assume an aggregation link.
- Do not treat a later timestamp as automatically more authoritative than an approved signed record.
- Do not treat an untrusted supplier PDF or an unvalidated system as usable evidence.
- Do not fill the 47-minute audit-capture gap silently.
- Do not bypass consent, entitlement and privacy boundaries for patient or participant data.
- Do not convert a gap into a resolution without evidence and an accountable human decision.
- Do not model audit as optional metadata; it is part of the business domain constraint.
- Do not introduce architecture, technical implementation, AI, agents, tools, APIs, or databases in this stage.

## 14. Stage 7 Quality Gate

The Stage 7 artifact is acceptable only if:

- Entities have clear identity, lifecycle, owner, state, and relationships.
- Value objects describe attributes, conventions, references or statuses without unnecessary identity.
- Aggregate roots have clear ownership boundaries and consistency responsibility.
- BatchEvidenceAggregate, ProductAndMarketAuthorisationAggregate, PVCaseAggregate, ColdChainShipmentAggregate, SupplyAllocationAggregate, EvidenceSourceAggregate and AuditAggregate are separated and do not own the full evidence journey.
- Batch release, rejection, reprocess, re-label, recall and QP certification remain human-owned and are never advisory outputs.
- Final PV seriousness, causality, expectedness, reportability and signal-confirmation decisions remain human-only.
- Inventory status change, capacity reservation, stock allocation, shipment and recall initiation require explicit authorised human approval.
- Fail-closed invariants prevent evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
- Invariants prevent silent unit conversion, silent genealogy repair, silent duplicate confirmation, and silent listedness selection.
- Consent, entitlement and privacy are modeled as constraints before patient/participant data is surfaced.
- Auditability is modeled as a first-class constraint, and the audit-capture gap remains visible.
- Known genealogy, unit, OOS/OOT, supplier-evidence, PV, cold-chain, shortage, validation, source-governance and audit gaps are mapped but not resolved.
- No batch, safety, quality or supply issue is resolved in the model unless the case evidence already resolves it.
- No architecture or technical implementation is introduced.

## 15. NEXT_STAGE_INPUT_BLOCK

```text
Stage 8 Input — Rules vs Reasoning Matrix

Final Entities:
- Batch
- MaterialGenealogy
- WarehouseMovement
- EbrStep
- LabResult
- OOSInvestigation
- EnvironmentalMonitoringResult
- Deviation
- CAPA
- ChangeControl
- CleaningValidation
- ReleasePacket
- SupplierAudit
- CertificateOfAnalysis
- ICSR
- SafetyReceipt
- MedDRAVersion
- ListednessSource
- ProductLabel
- InventoryItem
- Shipment
- TemperatureLogger
- SerialisationEvent
- AllocationConstraint
- ExcipientSupplier
- CmoContract
- MarketAuthorisation
- EvidenceSource
- AuditRecord
- User/AccessRole
- CheckpointState

Final Value Objects:
- UnitOfMeasureConvention
- EffectiveDate
- Jurisdiction
- AuthorityReference
- BatchStatusLabel
- ReportingClockReconstruction
- ListednessDeterminationReference
- AllocationConstraintReason
- LoggerReading
- AggregationLink
- ProvenanceCitation
- NoAnswerReason
- ConsentStatus
- EntitlementStatus
- ValidationState
- DuplicateCandidateReason
- PreferredTerm
- Timestamp
- RoleName

Final Aggregate Roots:
- BatchEvidenceAggregate
- ProductAndMarketAuthorisationAggregate
- PVCaseAggregate
- ColdChainShipmentAggregate
- SupplyAllocationAggregate
- EvidenceSourceAggregate
- AuditAggregate

Key Aggregate Boundaries:
- BatchEvidenceAggregate coordinates batch identity, genealogy, lab results, excursions, deviations, CAPA, change control, supplier evidence and release-packet completeness for batch-review readiness, but does not own batch release/rejection/reprocess/re-label/recall, QP certification, unit acceptance or OOS/OOT disposition.
- ProductAndMarketAuthorisationAggregate owns authority, effective-date, jurisdiction and validation basis per object, market and date; no system is universally authoritative.
- PVCaseAggregate owns ICSR intake, receipts, duplicate candidates, terminology, reporting-clock reconstruction and listedness evidence, but never final seriousness, causality, expectedness, reportability or signal-confirmation decisions.
- ColdChainShipmentAggregate owns logger readings, logger clocks, pallet association, aggregation links and cold-chain evidence state; excursion disposition remains human-owned.
- SupplyAllocationAggregate owns inventory visibility, shortage/capacity constraints and traceable allocation options; no inventory status change, capacity reservation, stock allocation, shipment or recall initiation without explicit authorised human approval.
- EvidenceSourceAggregate owns source trust, version, approval and quarantine state; untrusted documents are quarantined before use.
- AuditAggregate owns the audit event envelope, audit-capture-gap state, evidence packaging and continuity state; every recommendation, draft, approval, override, release, escalation, action, outcome and closure is auditable.

Invariant Register Summary:
- No evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
- A batch must not be shown as release-ready while any genealogy branch or release-packet element is unresolved or unverified.
- Genealogy breaks remain visible; they are never silently repaired.
- Unit-conversion assumptions must be approved; no silent conversion.
- Disputed OOS/OOT/invalid result state remains open and visible.
- Unverified supplier-audit commitments are not closed.
- Back-entered batch-record steps require checkpoint and audit evidence.
- Batch-review readiness is not release approval or QP certification.
- No final PV seriousness, causality, expectedness, reportability or signal-confirmation decision may be attributed to the AI.
- Duplicate ICSR candidates are surfaced, never confirmed.
- The reporting clock is evidence; the awareness date is not set automatically.
- Terminology state remains conflict-visible; the preferred term is not chosen automatically.
- Listedness sources remain conflict-visible; no winner is picked.
- Entitlement/consent must be rechecked before patient/participant data is surfaced.
- Cold-chain evidence must be resolved before shipment options are trusted; aggregation gaps remain visible.
- No allocation recommendation may be executed without explicit authorised human approval.
- No inventory status change, capacity reservation, stock allocation, shipment or recall initiation may be performed by the AI.
- Source authority must be resolved before a source is cited as decisive.
- Untrusted documents and ambiguous validation states remain quarantined or unresolved.
- The audit-capture gap remains visible; the organisation must operate safely without AI.
- Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable.
- Human overrides must record authorized owner and reason.
- The AI never releases, rejects, reprocesses, re-labels or recalls a batch.

Known Unresolved Exceptions as Domain State:
- SUA-88 genealogy break remains GenealogyBreak with WarehouseMovement reference.
- mg/L vs µg/mL remains UnitOfMeasureConvention unresolved state.
- OOS vs OOT vs notebook-invalid remains LabResult disputed state with OOSInvestigation.
- Unverified contract-site audit commitment remains SupplierAudit unverified state.
- Back-entered batch-record step remains EbrStep back-entered state with CheckpointState.
- 47-minute audit-capture gap remains AuditCaptureGap state.
- Disputed awareness date remains ReportingClockReconstruction dispute.
- Duplicate ICSR cluster remains DuplicateICSRCandidate set.
- MedDRA version mismatch remains MedDRAVersion conflict state.
- Listedness conflict remains ListednessSource conflict state.
- Cold-chain logger/pallet dispute remains LoggerReading/pallet-association dispute.
- Missing aggregation remains AggregationLink gap.
- Excipient shortage with eight-week recovery remains ExcipientShortage constraint.
- CMO capacity conflict remains CmoContract capacity-conflict state.
- Demand exceeds stock remains AllocationConstraint conflict with AllocationOption pending approval.
- Validation-state ambiguity remains ValidationState unresolved.
- Untrusted PDF/tool manifests remain EvidenceSource quarantined state.
- eConsent asynchrony and amendment jurisdiction gap remain ConsentStatus/Jurisdiction unresolved.

Human Decision Ownership Rules:
- EU Qualified Person owns QP certification and batch release/rejection (with Quality release reviewers); the AI prepares evidence only.
- Laboratory analyst / OOS owner owns OOS/OOT disposition and investigation conclusion.
- Laboratory / interface owner with Quality acceptance owns unit-conversion acceptance.
- Supplier-quality / quality reviewer owns supplier-audit verification and commitment closure.
- PV medical/safety reviewer owns seriousness, causality, expectedness, reportability determinations; PV case-intake staff and PV reviewer own duplicate confirmation and awareness-date acceptance.
- Signal management owns signal confirmation.
- Regulatory Affairs owns authority/effective-date/jurisdiction determination and listedness source basis.
- Supply Chain VP / authorised Quality owner owns allocation decisions and cold-chain excursion disposition.
- Quality / Regulatory accountable roles own recall decisions.
- Data Protection Officer owns consent/entitlement boundaries; audit/quality oversight owns auditability; CISO owns continuity.
- Authorized human owner must approve and explain any override.

Audit / Evidence Requirements:
- Every important state must reference batch/product/case/shipment/source identity, source evidence, owner, status, timestamp, and decision/action record where applicable.
- Batch evidence must retain genealogy breaks, unit-conversion state, OOS/OOT dispute, supplier verification and release-packet completeness.
- PV intake must retain receipts, duplicate rationale, clock reconstruction, MedDRA version, listedness sources and reviewer routing.
- Cold-chain evidence must retain logger basis, pallet link, aggregation state and excursion evidence.
- Allocation options must retain inventory, quality status, constraints and approval-request state.
- Consent/entitlement, approval, override, release, escalation, action, outcome and closure must be auditable; the audit-capture gap remains visible.

Open Questions for Stage 8:
- Which invariants are strict deterministic rules?
- Which items require human judgment rather than rule-only handling?
- Which activities can be supported by draft preparation or summarization without owning decisions?
- Which decisions must never be automated or inferred?
- Which rules are hard gates before evidence output, readiness claims, approval requests, or closure?
- Which unresolved exceptions require escalation versus review versus documented override?
- Which audit events are mandatory and rule-based?
- Which regulated decisions (QP certification, batch disposition, PV dispositions, allocation, recall) have explicit approval gates?
- Which rules enforce no-answer on unresolved identity, genealogy, unit, terminology, authority, consent, validation or checkpoint state?
```

Stage 7 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 8.
