# A5 — Input From Stage 4: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

Use this file as the dedicated input attachment for Stage 5 — Context Map.

This file is extracted from the Stage 4 Bounded Context Canvases output (the NEXT_STAGE_INPUT_BLOCK). It is intentionally limited to business-domain context. It does not solve the case, does not provide medical, regulatory or legal advice, does not resolve any product, batch, compound, safety, quality or supply conflict, and does not introduce architecture or technical implementation. Stage 5 is only for business-domain context mapping.

---

## STAGE_5_INPUT_BLOCK

```text
Stage 5 Input — Context Map

Final Bounded Context List:
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

Purpose of Each Context:
- Identity, Genealogy and Product Master Context: Owns product, batch, compound and material identity, genealogy/lineage state, and product-master state.
- GxP Batch Evidence Reconciliation Context: Assembles evidence for batch-review readiness (Workflow A); never releases/rejects/reprocesses/re-labels/recalls.
- Unit and Terminology Standardisation Context: Owns unit-conversion assumptions and terminology/reference-data state (mg/L vs µg/mL, MedDRA versions, preferred terms).
- Authority, Effective-Date and Jurisdiction Context: Owns which source is authoritative per business object, jurisdiction and effective date, including validation state.
- Consent, Entitlement and Privacy Context: Owns lawful access and use of patient and participant data across consent, entitlement and privacy boundaries.
- PV Case Intake and Signal Support Context: Supports intake, duplicate detection, reporting-clock reconstruction, listedness evidence and multilingual review (Workflow B); never final PV decisions.
- Supply, Cold-Chain and Allocation Planning Context: Generates traceable supply-shortage and cold-chain recovery options (Workflow C); never executes allocation, shipment, reservation or recall.
- Source and Document Governance Context: Owns versioned, approved, audit-trailed source governance and quarantine of untrusted documents.
- Supplier and Audit Evidence Context: Owns verified supplier audits, certificates, commitments and CAPA linkage for release-packet completeness.
- Audit, Evidence and Continuity Context: Owns auditability, evidence packaging, audit-capture gaps and safe operation with or without AI.

Key Upstream / Downstream Dependencies:
- Identity, Genealogy and Product Master Context feeds resolved/flagged identity and lineage state to GxP Batch Evidence Reconciliation, Supply/Cold-Chain and PV Case Intake.
- Unit and Terminology Standardisation Context feeds normalised units and terminology to GxP Batch Evidence Reconciliation, PV Case Intake and Supply.
- Authority, Effective-Date and Jurisdiction Context feeds the authoritative-source basis to all contexts and gates outputs fail-closed when unresolved.
- Consent, Entitlement and Privacy Context feeds legitimate access/use status to PV Case Intake, trial data handling and inspection evidence.
- Source and Document Governance Context feeds trusted/quarantined source state to all contexts.
- Supplier and Audit Evidence Context feeds verified supplier evidence to GxP Batch Evidence Reconciliation (release packets) and Supply.
- GxP Batch Evidence Reconciliation Context feeds batch-review readiness packages and evidence-gap reports to Quality/QP roles and Audit.
- PV Case Intake and Signal Support Context feeds prepared case-review material and duplicate/clock/listedness evidence to PV reviewers and Audit.
- Supply, Cold-Chain and Allocation Planning Context feeds traceable recovery options to accountable Supply/Quality roles for authorised human approval.
- Audit, Evidence and Continuity Context feeds auditable trail and evidence packages to all contexts and to multi-agency inspection.

Known Cross-Context Handoffs:
- Genealogy/identity state from Identity, Genealogy and Product Master Context to GxP Batch Evidence Reconciliation Context.
- Unit and terminology state from Unit and Terminology Standardisation Context to GxP Batch Evidence Reconciliation and PV Case Intake Contexts.
- Authoritative-source and effective-date basis from Authority, Effective-Date and Jurisdiction Context to all contexts.
- Consent/entitlement/privacy status from Consent, Entitlement and Privacy Context to PV Case Intake and Audit Contexts.
- Trusted/quarantined source state from Source and Document Governance Context to all contexts.
- Verified supplier evidence from Supplier and Audit Evidence Context to GxP Batch Evidence Reconciliation Context (release packet).
- Batch-review readiness package from GxP Batch Evidence Reconciliation Context to Quality/QP roles and Audit.
- Duplicate/clock/listedness evidence from PV Case Intake and Signal Support Context to PV reviewers and Audit.
- Recovery options and allocation constraints from Supply, Cold-Chain and Allocation Planning Context to authorised Supply/Quality roles.
- Evidence, approval, override, release, escalation, action, outcome and closure records from all contexts to Audit, Evidence and Continuity Context.

Safety-Critical Boundary Warnings:
- GxP Batch Evidence Reconciliation does not own batch release, rejection, reprocess, re-label, recall or QP certification.
- PV Case Intake and Signal Support does not own final seriousness, causality, expectedness, reportability or signal-confirmation decisions.
- Supply, Cold-Chain and Allocation Planning never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval.
- Unit and Terminology Standardisation must not silently apply a conversion.
- Identity, Genealogy and Product Master must not silently resolve a genealogy break.
- No system is universally authoritative; later timestamps are not automatically more authoritative than approved signed records.
- Source and Document Governance must quarantine untrusted documents before use.
- Consent, Entitlement and Privacy boundaries must be respected before patient or participant data is accessed, used, routed or shared.
- Audit, Evidence and Continuity must capture every recommendation, draft, approval, override, release, escalation, action, outcome and closure, and must operate safely without AI.
- No context may produce evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.

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

Open Questions for Context Mapping:
- Which context is upstream and which is downstream for each handoff?
- Which handoffs require shared language such as batch/product identity, readiness status, unit state, authority basis or checkpoint status?
- Which handoffs require explicit evidence capture?
- Which context owns escalation when a required evidence state cannot be resolved?
- Which context records approval versus which context performs the underlying review?
- Which cross-context translations could create safety risk?
- Which context boundaries require consent, entitlement or privacy checks before access or use?
- Which context relationships are partnership relationships rather than simple upstream/downstream relationships?
- How is fail-closed gating passed across context boundaries without hiding unresolved states?
```
