# A7 Input From Stage 6 — Domain Model and Invariant Register Handoff

This file contains the Stage 6 → Stage 7 handoff input extracted from the completed event storming board for the NovaCura Therapeutics Group (Project AEGIS-PHARMA) governed evidence-reconciliation case. Use this as the primary attachment/input for Stage 7.

Do not use this stage to solve batch, safety or supply issues, approve batch release or rejection, disposition safety cases, allocate stock, ship product, initiate recalls, design architecture, introduce GenAI, define agents, create technical implementation, or provide medical, regulatory or legal advice. Stage 7 is only for business-domain modeling: entities, value objects, aggregates, ownership boundaries, and invariants.

## STAGE_7_INPUT_BLOCK

```text
Stage 7 Input — Domain Model and Invariant Register

Final Event Timeline:
1. Batch review opened for NCB204-B24071
2. Batch identity and product-master state checked
3. Genealogy check requested
4. Genealogy branch gap detected (SUA-88)
5. Warehouse consumption record found for SUA-88
6. Unit-conversion conflict detected (mg/L vs µg/mL)
7. Unit-conversion state declared unresolved (no-answer)
8. OOS/OOT state disagreement surfaced
9. Sterile-area excursion near fill-finish detected
10. Organism identification corrected after initial review
11. Supplier-audit commitment verification requested
12. Supplier-audit commitment found unverified
13. Back-entered batch-record step detected
14. Release packet marked evidence-incomplete
15. Batch-review readiness assessed with unresolved gaps
16. QP certification decision pending
17. PV case intake opened
18. Consent/entitlement check requested for participant data use
19. ICSR duplicate cluster identified
20. Awareness-date dispute surfaced
21. MedDRA preferred-term conflict surfaced
22. Listedness conflict surfaced (IB vs CCDS vs local label)
23. Reporting-clock evidence prepared for review
24. Multilingual review requested
25. Case-review material prepared for accountable PV review
26. Cold-chain excursion detected (logger clock/pallet disputed)
27. Case-to-pallet aggregation gap detected
28. Serialisation aggregation gap detected
29. Excipient shortage surfaced
30. CMO capacity conflict surfaced
31. Allocation constraint check completed
32. Allocation option proposed (awaiting human approval)
33. Human approval requested for allocation option
34. Validation state found ambiguous
35. Master-data repair window opened
36. Audit record captured
37. Audit-capture gap detected (47 minutes)
38. AI-off continuity mode activated
39. Inspection evidence request received (72h)
40. Evidence package assembled for inspection
41. Escalation created for unresolved evidence state
42. No-answer (abstention) declared where required state unresolved
43. Human approval recorded
44. Human override recorded

Major Commands / Activities:
- Open batch review
- Verify batch and product identity
- Request lineage check
- Detect missing lineage branch
- Search warehouse consumption records
- Compare reported vs assumed units
- Abstain on unresolved unit state
- Surface conflicting result states
- Report environmental excursion
- Correct organism identification
- Request commitment verification
- Check commitment verification state
- Detect back-entered record
- Assess release-packet completeness
- Assess batch-review readiness
- Prepare evidence for QP certification
- Open PV case intake
- Validate consent and entitlement
- Detect duplicate candidates
- Reconstruct reporting clock
- Align terminology versions
- Compare listedness sources
- Request multilingual review
- Prepare case-review material
- Detect temperature excursion
- Detect aggregation gap
- Check aggregation hierarchy
- Surface shortage
- Surface capacity conflict
- Check allocation constraints
- Generate traceable options
- Request authorised approval
- Check validation state
- Open repair window
- Capture audit event envelope
- Detect audit-capture gap
- Activate AI-off operation
- Receive multi-agency request
- Assemble evidence package
- Escalate unresolved state
- Abstain on unresolved state
- Record human approval
- Record human override

Actors and Human Owners:
- Chief Quality Officer
- EU Qualified Person
- Quality release reviewer
- Manufacturing / sterile-fill participant
- Laboratory analyst / OOS owner
- Microbiology / laboratory reviewer
- Identity / genealogy / master-data owner
- Supplier-quality / procurement
- Global Head of Pharmacovigilance
- PV case-intake staff
- PV medical / safety reviewer
- Signal management
- Clinical Operations
- Regulatory Affairs (RIM, submissions, labelling, IDMP)
- Supply Chain planner / logistics / cold-chain
- Serialisation / aggregation participant
- CMO and supplier-quality
- Data Protection Officer / privacy owner
- CISO / IT operations
- Audit / quality oversight
- Biostatistics
- Patient-safety voice

Bounded Contexts Referenced by Events:
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

Policies and Rules Used by the Event Storm:
- AI never releases, rejects, reprocesses, re-labels or recalls a batch.
- AI never makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions.
- AI never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval.
- AI never changes formulation, specification, clinical eligibility, safety-case disposition, batch-release or recall decisions.
- Regulated accountability remains with the accountable Quality, Safety, Regulatory, Clinical and Supply roles.
- No evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
- Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable.
- The system operates read-only and advisory; it prepares, reconciles, explains and packages evidence.
- No product, batch, safety, quality or supply issue is considered resolved merely because it has been identified.
- Batch-review readiness is not release approval or QP certification.
- PV intake supports review; it never sets the clock or the disposition.
- Allocation options are advisory until explicit authorised human approval.
- Authority is per business object, jurisdiction and effective date; later timestamps are not automatically authoritative.
- Untrusted sources and ambiguous validation states remain quarantined or unresolved.
- The organisation must operate safely with or without AI.

Known Exceptions and Unresolved Gaps:
- Genealogy branch gap for SUA-88 with a warehouse consumption record.
- Unapproved mg/L vs µg/mL unit-conversion assumption.
- Disputed OOS/OOT/notebook-invalid state with an open investigation.
- Unverified contract-site audit commitment in the EU release packet.
- Back-entered batch-record step; 47-minute audit-capture gap.
- Disputed PV awareness date; duplicate ICSR cluster; MedDRA version mismatch; listedness conflict (IB vs CCDS vs local label).
- Cold-chain logger clock and pallet association dispute; missing case-to-pallet and serialisation aggregation.
- Sole-source excipient contamination with eight-week recovery; CMO capacity conflict; demand exceeds available stock.
- Validation-state ambiguity; untrusted supplier deviation PDF and tool manifests; eConsent version asynchrony; pivotal-trial amendment not approved in one country.

Audit / Evidence Requirements:
- Identity and lineage evidence, genealogy-break identification and ownership must be traceable.
- Unit-conversion conflict and no-answer declarations must be recorded with mapping and source.
- OOS/OOT/invalid dispute evidence and open investigation ownership must be recorded.
- Supplier-audit verification state and release-packet completeness must be recorded.
- Batch-review readiness assessment, evidence-gap ownership and QP pending status must be recorded.
- PV intake, duplicate rationale, clock reconstruction, MedDRA version, listedness sources and reviewer routing must be recorded.
- Cold-chain logger basis, pallet association, aggregation state, shortage, capacity conflict and constraint rationale must be recorded.
- Approval requests, human approvals, human overrides, escalations, actions, outcomes and closures must be auditable.
- The audit event envelope must be captured for every workflow event; the 47-minute audit-capture gap remains visible.
- AI-off continuity activation, repair-window operation and the 72-hour inspection evidence package must be recorded.

Candidate Domain Objects Visible From Events:
- BatchReview
- BatchReviewReadiness
- ReleasePacket
- BatchRecordStep
- Genealogy
- GenealogyBreak
- MaterialLot (SUA-88)
- WarehouseConsumptionRecord
- UnitConversionAssumption
- LaboratoryResult
- OOSState
- OOTState
- EnvironmentalMonitoringExcursion
- OrganismIdentificationCorrection
- SupplierAuditCommitment
- ReleasePacketCompleteness
- QPCertificationDecision
- ICSRCase
- DuplicateICSRCandidate
- AwarenessDate
- ReportingClock
- MedDRATerminologyState
- PreferredTerm
- ListednessEvidence
- ExpectednessEvidence
- CaseReviewMaterial
- TemperatureLoggerRecord
- ColdChainExcursion
- AggregationHierarchy
- SerialisationAggregation
- ExcipientShortage
- CMOCapacity
- AllocationConstraint
- AllocationOption
- ApprovalRequest
- ApprovalRecord
- OverrideRecord
- ValidationState
- AuditRecord
- AuditCaptureGap
- ContinuityState
- InspectionRequest
- EvidencePackage
- EscalationRecord
- AbstentionRecord

Open Questions for Stage 7:
- Which objects are entities versus value objects?
- Which object should act as the main aggregate root for batch-review readiness, PV case intake, and supply recovery respectively?
- Which object owns evidence status and which owns checkpoint state?
- Which object owns the authority/effective-date basis and how is it passed between contexts?
- Which object owns the audit event envelope?
- Which invariants prevent evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved?
- Which invariants prevent batch release/rejection, QP certification, PV dispositions, allocation, shipment and recall events from being advisory or automated?
- Which invariants prevent silent unit conversion, silent genealogy repair, and silent listedness selection?
- Which invariants keep the audit-capture gap and unresolved exceptions visible?
```

Stage 6 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 7.
