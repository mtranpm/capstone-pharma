# A8 Input From Stage 7 — Domain Model and Invariant Register

Use this file as the direct input attachment for **Stage 8 — Rules vs Reasoning Matrix**.

This input is derived from the completed Stage 7 artifact for the **NovaCura Therapeutics Group (Project AEGIS-PHARMA)** governed evidence-reconciliation case.

---

## Source Stage

```text
Stage 7 — Domain Model and Invariant Register
```

## Target Stage

```text
Stage 8 — Rules vs Reasoning Matrix
```

## Stage 8 Purpose

Stage 8 must separate:

```text
hard business rules
regulated human decisions
workflow gates
approval gates
draft-only or reasoning-support activities
forbidden automated actions
audit requirements
```

The goal is not to solve the batch, safety or supply case. The goal is to identify what must be governed as a rule, what must remain human-owned, what may be prepared or summarized as support, and what must never be automated or inferred.

---

# 1. Case Context

NovaCura Therapeutics Group (NTG) is a fictional global pharmaceutical company operating across India, Germany, Ireland, the United States, the UAE and Singapore. It is building a governed evidence-reconciliation capability for three mandatory advisory workflows: GxP batch-review readiness (Workflow A), PV case intake and signal support (Workflow B), and bounded supply-shortage and cold-chain recovery planning (Workflow C). The AI remains read-only and advisory; it prepares, reconciles, explains and packages evidence.

The active scenario includes the disputed biologics batch NCB204-B24071 (missing SUA-88 genealogy branch, mg/L vs µg/mL unit assumption, disputed OOS/OOT state, unverified contract-site audit commitment, back-entered batch-record step), a sterile-area excursion with a corrected organism identification, emerging safety reports (duplicate ICSR candidates, disputed awareness date, MedDRA version mismatch, listedness conflict), a cold-chain failure (disputed logger clocks and pallet association, missing aggregation), a sole-source excipient shortage with CMO capacity conflict, a ransomware event with a 47-minute audit-capture gap, and a multi-agency inspection request within 72 hours.

---

# 2. Final Domain Model Summary From Stage 7

## Final Entities

```text
Batch
MaterialGenealogy
WarehouseMovement
EbrStep
LabResult
OOSInvestigation
EnvironmentalMonitoringResult
Deviation
CAPA
ChangeControl
CleaningValidation
ReleasePacket
SupplierAudit
CertificateOfAnalysis
ICSR
SafetyReceipt
MedDRAVersion
ListednessSource
ProductLabel
InventoryItem
Shipment
TemperatureLogger
SerialisationEvent
AllocationConstraint
ExcipientSupplier
CmoContract
MarketAuthorisation
EvidenceSource
AuditRecord
User/AccessRole
CheckpointState
```

## Final Value Objects

```text
UnitOfMeasureConvention
EffectiveDate
Jurisdiction
AuthorityReference
BatchStatusLabel
ReportingClockReconstruction
ListednessDeterminationReference
AllocationConstraintReason
LoggerReading
AggregationLink
ProvenanceCitation
NoAnswerReason
ConsentStatus
EntitlementStatus
ValidationState
DuplicateCandidateReason
PreferredTerm
Timestamp
RoleName
```

## Final Aggregate Roots

```text
BatchEvidenceAggregate
ProductAndMarketAuthorisationAggregate
PVCaseAggregate
ColdChainShipmentAggregate
SupplyAllocationAggregate
EvidenceSourceAggregate
AuditAggregate
```

---

# 3. Key Aggregate Boundaries From Stage 7

```text
BatchEvidenceAggregate coordinates batch identity, genealogy, lab results, excursions, deviations, CAPA, change control, supplier evidence and release-packet completeness for batch-review readiness, but does not own batch release/rejection/reprocess/re-label/recall, QP certification, unit acceptance or OOS/OOT disposition.

ProductAndMarketAuthorisationAggregate owns authority, effective-date, jurisdiction and validation basis per object, market and date; no system is universally authoritative and a later timestamp is not automatically more authoritative than an approved signed record.

PVCaseAggregate owns ICSR intake, receipts, duplicate candidates, terminology, reporting-clock reconstruction and listedness evidence, but never final seriousness, causality, expectedness, reportability or signal-confirmation decisions.

ColdChainShipmentAggregate owns logger readings, logger clocks, pallet association, aggregation links and cold-chain evidence state; excursion disposition remains human-owned.

SupplyAllocationAggregate owns inventory visibility, shortage/capacity constraints and traceable allocation options; no inventory status change, capacity reservation, stock allocation, shipment or recall initiation without explicit authorised human approval.

EvidenceSourceAggregate owns source trust, version, approval and quarantine state; untrusted documents are quarantined before use.

AuditAggregate owns the audit event envelope, audit-capture-gap state, evidence packaging and continuity state; every recommendation, draft, approval, override, release, escalation, action, outcome and closure is auditable.
```

---

# 4. Invariant Register Summary From Stage 7

```text
No evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.

A batch must not be shown as release-ready while any genealogy branch or release-packet element is unresolved or unverified.

Genealogy breaks remain visible; they are never silently repaired.

Unit-conversion assumptions must be approved; no silent conversion.

Disputed OOS/OOT/invalid result state remains open and visible.

Unverified supplier-audit commitments are not closed.

Back-entered batch-record steps require checkpoint and audit evidence.

Batch-review readiness is not release approval or QP certification.

No final PV seriousness, causality, expectedness, reportability or signal-confirmation decision may be attributed to the AI.

Duplicate ICSR candidates are surfaced, never confirmed.

The reporting clock is evidence; the awareness date is not set automatically.

Terminology state remains conflict-visible; the preferred term is not chosen automatically.

Listedness sources remain conflict-visible; no winner is picked.

Entitlement/consent must be rechecked before patient/participant data is surfaced.

Cold-chain evidence must be resolved before shipment options are trusted; aggregation gaps remain visible.

No allocation recommendation may be executed without explicit authorised human approval.

No inventory status change, capacity reservation, stock allocation, shipment or recall initiation may be performed by the AI.

Source authority must be resolved before a source is cited as decisive.

Untrusted documents and ambiguous validation states remain quarantined or unresolved.

The audit-capture gap remains visible; the organisation must operate safely without AI.

Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable.

Human overrides must record authorized owner and reason.

The AI never releases, rejects, reprocesses, re-labels or recalls a batch.
```

---

# 5. Known Unresolved Exceptions as Domain State

```text
SUA-88 genealogy break remains GenealogyBreak with WarehouseMovement reference.

mg/L vs µg/mL remains UnitOfMeasureConvention unresolved state.

OOS vs OOT vs notebook-invalid remains LabResult disputed state with OOSInvestigation.

Unverified contract-site audit commitment remains SupplierAudit unverified state.

Back-entered batch-record step remains EbrStep back-entered state with CheckpointState.

47-minute audit-capture gap remains AuditCaptureGap state.

Disputed awareness date remains ReportingClockReconstruction dispute.

Duplicate ICSR cluster remains DuplicateICSRCandidate set.

MedDRA version mismatch remains MedDRAVersion conflict state.

Listedness conflict remains ListednessSource conflict state.

Cold-chain logger/pallet dispute remains LoggerReading/pallet-association dispute.

Missing aggregation remains AggregationLink gap.

Excipient shortage with eight-week recovery remains ExcipientShortage constraint.

CMO capacity conflict remains CmoContract capacity-conflict state.

Demand exceeds stock remains AllocationConstraint conflict with AllocationOption pending approval.

Validation-state ambiguity remains ValidationState unresolved.

Untrusted PDF/tool manifests remain EvidenceSource quarantined state.

eConsent asynchrony and amendment jurisdiction gap remain ConsentStatus/Jurisdiction unresolved.
```

---

# 6. Human Decision Ownership Rules From Stage 7

```text
EU Qualified Person owns QP certification and batch release/rejection (with Quality release reviewers); the AI prepares evidence only.

Laboratory analyst / OOS owner owns OOS/OOT disposition and investigation conclusion.

Laboratory / interface owner with Quality acceptance owns unit-conversion acceptance.

Supplier-quality / quality reviewer owns supplier-audit verification and commitment closure.

PV medical/safety reviewer owns seriousness, causality, expectedness, reportability determinations; PV case-intake staff and PV reviewer own duplicate confirmation and awareness-date acceptance.

Signal management owns signal confirmation.

Regulatory Affairs owns authority/effective-date/jurisdiction determination and listedness source basis.

Supply Chain VP / authorised Quality owner owns allocation decisions and cold-chain excursion disposition.

Quality / Regulatory accountable roles own recall decisions.

Data Protection Officer owns consent/entitlement boundaries; audit/quality oversight owns auditability; CISO owns continuity.

Authorized human owner must approve and explain any override.
```

---

# 7. Audit / Evidence Requirements From Stage 7

```text
Every important state must reference batch/product/case/shipment/source identity, source evidence, owner, status, timestamp, and decision/action record where applicable.

Batch evidence must retain genealogy breaks, unit-conversion state, OOS/OOT dispute, supplier verification and release-packet completeness.

PV intake must retain receipts, duplicate rationale, clock reconstruction, MedDRA version, listedness sources and reviewer routing.

Cold-chain evidence must retain logger basis, pallet link, aggregation state and excursion evidence.

Allocation options must retain inventory, quality status, constraints and approval-request state.

Consent/entitlement, approval, override, release, escalation, action, outcome and closure must be auditable; the audit-capture gap remains visible.
```

---

# 8. Open Questions for Stage 8

```text
Which invariants are strict deterministic rules?

Which items require human judgment rather than rule-only handling?

Which activities can be supported by draft preparation or summarization without owning decisions?

Which decisions must never be automated or inferred?

Which rules are hard gates before evidence output, readiness claims, approval requests, or closure?

Which unresolved exceptions require escalation versus review versus documented override?

Which audit events are mandatory and rule-based?

Which regulated decisions (QP certification, batch disposition, PV dispositions, allocation, recall) have explicit approval gates?

Which rules enforce no-answer on unresolved identity, genealogy, unit, terminology, authority, consent, validation or checkpoint state?
```

---

# 9. Stage 8 Guardrails

```text
Do not provide medical, regulatory or legal advice.
Do not resolve batch, safety or supply issues.
Do not approve batch release or rejection.
Do not disposition safety cases.
Do not allocate stock, ship product or initiate recalls.
Do not treat draft or reasoning support as a decision owner.
Do not create architecture.
Do not introduce RAG, MCP, agents, tools, APIs, or implementation design.
Do not add facts outside the NovaCura Therapeutics Group case and synthetic evidence.
Preserve regulated human accountability, the read-only advisory boundary, fail-closed behaviour on unresolved state, and auditability.
```

---

Use this input file as the only handoff material for Stage 8.
