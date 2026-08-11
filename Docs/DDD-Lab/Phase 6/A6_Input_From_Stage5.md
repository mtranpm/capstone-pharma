# A6 — Input From Stage 5: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

Use this file as the dedicated input attachment for Stage 6 — Event Storming Board.

This file is extracted from the Stage 5 Context Map output (the NEXT_STAGE_INPUT_BLOCK). It is intentionally limited to business-domain context. It does not solve the case, does not provide medical, regulatory or legal advice, does not resolve any product, batch, compound, safety, quality or supply conflict, and does not introduce architecture or technical implementation. Stage 6 is only for business-domain event storming.

---

## STAGE_6_INPUT_BLOCK

```text
Stage 6 Input — Event Storming Board

Final Context List:
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

Final Context Map Summary:
- Authority, Effective-Date and Jurisdiction Context provides the authoritative-source, effective-date, jurisdiction and validation-state basis to all contexts and gates outputs fail-closed when unresolved.
- Consent, Entitlement and Privacy Context controls legitimate patient/participant data access, use, routing and sharing.
- Source and Document Governance Context provides trusted/quarantined source state to all contexts.
- Identity, Genealogy and Product Master Context provides resolved/flagged product, batch, compound and material identity and lineage state.
- Unit and Terminology Standardisation Context provides normalised units and terminology state (mg/L vs µg/mL, MedDRA versions, preferred terms).
- Supplier and Audit Evidence Context provides verified supplier audits, certificates, commitments and CAPA linkage.
- GxP Batch Evidence Reconciliation Context provides batch-review readiness packages and evidence-gap reports for Quality/QP roles (Workflow A).
- PV Case Intake and Signal Support Context provides prepared case-review material and duplicate/clock/listedness evidence for PV reviewers (Workflow B).
- Supply, Cold-Chain and Allocation Planning Context provides traceable recovery options and allocation-constraint reports for authorised human approval (Workflow C).
- Audit, Evidence and Continuity Context receives traceability from all contexts and packages evidence for inspection.

Key Relationships:
- Authority, Effective-Date and Jurisdiction → all contexts: authoritative-source, effective-date and validation gating.
- Consent, Entitlement and Privacy → PV Case Intake and trial-data contexts: access/use legitimacy.
- Source and Document Governance → all contexts: trusted/quarantined source state.
- Identity, Genealogy and Product Master → GxP Batch Evidence Reconciliation, Supply/Cold-Chain, PV Case Intake: identity and lineage state.
- Unit and Terminology Standardisation → GxP Batch Evidence Reconciliation, PV Case Intake, Supply: units and terminology.
- Supplier and Audit Evidence → GxP Batch Evidence Reconciliation (release packet), Supply: verified supplier evidence.
- GxP Batch Evidence Reconciliation → Quality/QP roles: batch-review readiness package.
- PV Case Intake and Signal Support → PV reviewers: prepared case material.
- Supply, Cold-Chain and Allocation Planning → authorised Supply/Quality roles: recovery options for human approval.
- All contexts → Audit, Evidence and Continuity: evidence, approval, override, release, escalation, action, outcome and closure records.

Shared Kernel:
- Batch identity
- Product identity
- Material / single-use assembly lot identity
- Genealogy state
- Unit-of-measure conventions
- Unit-conversion assumption status
- Terminology state
- Effective date
- Authority registry
- Jurisdiction applicability
- Evidence status
- Checkpoint state
- Validation state
- Consent and entitlement status
- Audit event envelope

Published Language / Handoff Vocabulary:
- Batch-review readiness
- Release-ready
- Release packet
- QP certification
- Genealogy break
- Unit-conversion assumption
- OOS
- OOT
- Reporting clock
- Awareness date
- Duplicate ICSR candidate
- Preferred term
- Listedness
- Expectedness
- Cold-chain excursion
- Aggregation hierarchy
- Allocation constraint
- Compassionate-use entitlement
- Escalation
- Approval
- Override
- Abstention / no-answer
- Evidence trail

Known Handoff Risks:
- MES-to-warehouse genealogy handoff carries the SUA-88 lineage break into batch review.
- Laboratory unit-conversion interface can silently change mg/L to µg/mL (1000x).
- Two MedDRA versions changing the preferred term can split or merge safety cases.
- Product identity translation across RIM/ERP/IDMP/labels can corrupt listedness and linkage.
- Temperature-logger clock versus UTC can mis-state cold-chain excursion duration.
- Supplier PDF text extraction is untrusted (prompt-injection risk) until governance review.
- Listedness conflict between IB, CCDS and local label remains unresolved.
- Disputed awareness date can distort the PV reporting clock.
- Recovery options can be mistaken for executed allocation, reservation or shipment.
- Unvalidated or research-only systems can be mistaken for authoritative sources.
- The 47-minute audit-capture gap can hide required evidence.
- Consent/entitlement asynchrony with the pivotal-trial amendment can block lawful data use.

Non-Negotiables:
- AI never releases, rejects, reprocesses, re-labels or recalls a batch.
- AI never makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions.
- AI never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval.
- AI never changes formulation, specification, clinical eligibility, safety-case disposition, batch-release or recall decisions.
- Regulated accountability remains with the accountable Quality, Safety, Regulatory, Clinical and Supply roles.
- No evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
- Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable.
- The system operates read-only and advisory; it prepares, reconciles, explains and packages evidence.
- No product, batch, safety, quality or supply issue is considered resolved merely because it has been identified.

Candidate Business Events for Event Storming:
- Batch NCB204-B24071 review opened
- Genealogy branch gap detected (SUA-88)
- Unit-conversion conflict detected (mg/L vs µg/mL)
- OOS/OOT state disagreement surfaced
- Sterile-area excursion detected near fill-finish
- Organism identification corrected after initial review
- Supplier-audit commitment found unverified
- Back-entered batch-record step detected
- Release packet marked evidence-incomplete
- QP certification decision pending
- ICSR duplicate cluster identified
- Awareness-date dispute surfaced
- MedDRA preferred-term conflict surfaced
- Listedness conflict surfaced (IB vs CCDS vs local label)
- Cold-chain excursion detected (logger clock/pallet disputed)
- Serialisation aggregation gap detected
- Excipient shortage surfaced
- CMO capacity conflict surfaced
- Allocation constraint check completed
- Allocation option proposed (awaiting human approval)
- Inspection evidence request received (72h)
- AI-off continuity mode activated
- Audit record captured

Open Questions for Event Storming:
- Which business event starts batch-review readiness work for a batch?
- Which event records a genealogy break and its owner?
- Which event records that an unresolved unit, terminology, authority or validation state blocks evidence output?
- Which event triggers abstention/no-answer rather than a guess?
- Which event marks the release packet evidence-incomplete versus evidence-complete?
- Which event requests human review or approval, and which event records the human decision?
- Which event escalates an unresolved evidence state to accountable ownership?
- Which event records an override and its reason?
- Which event captures the audit event envelope for every workflow event?
- Which events remain human-owned for batch release/rejection, QP certification, PV dispositions, allocation and recall?
```
