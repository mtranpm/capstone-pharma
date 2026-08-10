# A5 — Context Map: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## 1. Stage 5 Mission

Stage 5 converts the bounded context canvases from Stage 4 into a business-domain context map for the NovaCura Therapeutics Group governed evidence-reconciliation case. The purpose is to show how identity, genealogy, unit/terminology, authority/effective-date/jurisdiction, consent/entitlement/privacy, batch evidence reconciliation, PV case intake, supply/cold-chain planning, source governance, supplier evidence, and audit/continuity responsibilities interact without merging them into one unsafe evidence context.

This stage does not solve batch, safety or supply issues, approve batch release or rejection, disposition safety cases, allocate stock, ship product, initiate recalls, provide medical, regulatory or legal advice, create architecture, or introduce technical implementation. It only maps business ownership, upstream/downstream dependencies, partnership relationships, shared language, translation risks, and audit/evidence requirements. The AI remains read-only and advisory across Workflows A, B and C.

## 2. Input Summary

The Stage 5 input comes from the Stage 4 bounded context canvases for the NovaCura Therapeutics Group case. The business scenario concerns the disputed biologics batch NCB204-B24071 (missing single-use assembly lot SUA-88 genealogy branch, mg/L vs µg/mL unit-conversion assumption, disputed OOS/OOT state, unverified supplier-audit commitment, back-entered batch-record step), emerging safety reports (duplicate ICSR candidates, disputed awareness date, MedDRA version mismatch, listedness conflict between IB, CCDS and local label), a cold-chain failure (disputed logger clocks and pallet association, missing serialisation aggregation), a sole-source excipient shortage with CMO capacity conflict and demand exceeding stock, a ransomware event with a 47-minute audit-capture gap, and a multi-agency inspection request within 72 hours.

The final bounded contexts from Stage 4 are:

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

## 3. Context Mapping Principles

- The map represents business-domain relationships, not system architecture.
- A context owns a specific business responsibility, language, status, and risk area.
- No single context owns the full evidence-reconciliation journey across batch review, PV case handling and supply recovery.
- GxP batch evidence reconciliation prepares batch-review readiness evidence; batch release, rejection, reprocess, re-label, recall and QP certification remain human-owned by accountable Quality and EU QP roles.
- PV case intake supports intake, duplicate detection, terminology normalisation, reporting-clock reconstruction and listedness evidence; final seriousness, causality, expectedness, reportability and signal-confirmation decisions remain human-owned by accountable PV roles.
- Supply, cold-chain and allocation planning generates traceable, policy-bounded options; inventory status changes, capacity reservation, stock allocation, shipment and recall initiation require explicit authorised human approval.
- No system is universally authoritative; authority is per business object, jurisdiction and effective date, and a later timestamp is not automatically more authoritative than an approved signed record.
- Unit, terminology and identity translation boundaries must be explicit because a silent conversion or identity mismatch can corrupt batch, safety and supply evidence.
- Consent, entitlement and privacy boundaries apply before patient or participant data is accessed, used, routed or shared.
- Untrusted sources (prompt-injection supplier PDF, stale/unsigned tool manifests, shared-account spreadsheets) must be quarantined before they are used as evidence.
- Evidence and audit must observe all relevant contexts and capture recommendations, drafts, approvals, overrides, releases, escalations, actions, outcomes and closures.
- Fail-closed means no evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
- Operational contexts must not silently convert unresolved exceptions into completed readiness.
- Context relationships must make handoff risks visible.

## 4. Final Context Map Overview

```text
Authority, Effective-Date and Jurisdiction Context
    → provides authoritative-source, effective-date, jurisdiction and validation-state basis to all contexts
    → gates every context fail-closed when any required state is unresolved

Consent, Entitlement and Privacy Context
    → controls legitimate patient/participant data access/use, routing and sharing across contexts

Source and Document Governance Context
    → provides trusted/quarantined source state to all contexts

Identity, Genealogy and Product Master Context
    → provides resolved/flagged product, batch, compound and material identity and lineage state
    → GxP Batch Evidence Reconciliation Context
    → Supply, Cold-Chain and Allocation Planning Context
    → PV Case Intake and Signal Support Context
    → Audit, Evidence and Continuity Context

Unit and Terminology Standardisation Context
    → provides normalised units and terminology state (mg/L vs µg/mL, MedDRA versions, preferred terms)
    → GxP Batch Evidence Reconciliation Context
    → PV Case Intake and Signal Support Context
    → Supply, Cold-Chain and Allocation Planning Context

Supplier and Audit Evidence Context
    → provides verified supplier audits, certificates, commitments and CAPA linkage
    → GxP Batch Evidence Reconciliation Context (release packet)
    → Supply, Cold-Chain and Allocation Planning Context

GxP Batch Evidence Reconciliation Context
    → provides batch-review readiness packages, evidence-gap reports and evidence lineage
    → Quality release reviewers and EU Qualified Person
    → Audit, Evidence and Continuity Context

PV Case Intake and Signal Support Context
    → provides prepared case-review material, duplicate/clock/listedness evidence and multilingual review material
    → PV medical/safety reviewers and signal management
    → Audit, Evidence and Continuity Context

Supply, Cold-Chain and Allocation Planning Context
    → provides traceable recovery options and allocation-constraint reports
    → authorised Supply/Quality roles for human approval
    → Audit, Evidence and Continuity Context

Audit, Evidence and Continuity Context
    ← receives evidence, approval, override, release, escalation, action, outcome and closure records from every context
    → provides auditable trail, evidence packages and continuity posture to all contexts and to multi-agency inspection
```

## 5. Context Relationship Matrix

| Upstream context | Downstream context | Relationship type | Exchanged business information | Ownership concern | Translation / handoff risk | Audit / evidence requirement |
|---|---|---|---|---|---|---|
| Identity, Genealogy and Product Master Context | GxP Batch Evidence Reconciliation Context | Upstream/downstream | Product/batch/material identity state, genealogy tree state, lineage completeness, genealogy-break status | Identity and lineage ownership is not owned by batch review | A genealogy break may be silently repaired or hidden; identity may be conflated across systems | Record identity-match evidence, lineage sources, genealogy-break identification, owner |
| Identity, Genealogy and Product Master Context | Supply, Cold-Chain and Allocation Planning Context | Upstream/downstream | Batch/material identity state, aggregation hierarchy state, case-to-pallet linkage | Identity/aggregation ownership is not owned by supply planning | Missing case-to-pallet aggregation may be assumed resolved after a line restart | Record aggregation state, linkage evidence, identity source |
| Identity, Genealogy and Product Master Context | PV Case Intake and Signal Support Context | Upstream/downstream | Product identity state for product-quality linkage | Product linkage must not displace accountable PV review | A product-quality complaint may be attached to the wrong product identity | Record product-linkage evidence and source |
| Unit and Terminology Standardisation Context | GxP Batch Evidence Reconciliation Context | Upstream/downstream | Unit-conversion assumption status, normalised laboratory units, reference-data state | Conversion and terminology ownership is not owned by batch review | mg/L vs µg/mL unit assumption may be applied silently, changing a concentration 1000x | Record conversion-assumption approval/override, mapping history, unit state |
| Unit and Terminology Standardisation Context | PV Case Intake and Signal Support Context | Upstream/downstream / partnership | MedDRA version alignment, preferred-term state, terminology normalisation | Terminology state must not displace final PV decisions | Two MedDRA versions changing the preferred term may split or merge safety cases | Record MedDRA version, preferred-term mapping, terminology-state evidence |
| Unit and Terminology Standardisation Context | Supply, Cold-Chain and Allocation Planning Context | Upstream/downstream | Unit conventions for temperature, volume and concentration data | Unit ownership is not owned by supply planning | Logger temperature units or concentrations may be misinterpreted | Record unit conventions used in option evidence |
| Authority, Effective-Date and Jurisdiction Context | All contexts | Upstream control / policy gate | Authoritative-source basis, effective-date state, jurisdiction applicability, validation state | No system is universally authoritative; authority is contextual | A later timestamp may be treated as automatically more authoritative than an approved signed record; an unvalidated system may be treated as authoritative | Record authority rationale, effective-date determination, jurisdiction basis, validation-state records |
| Consent, Entitlement and Privacy Context | PV Case Intake and Signal Support Context | Upstream control / policy gate | Consent status, entitlement status, privacy-boundary state, lawful basis for routing and secondary use | Access/use legitimacy is not owned by PV intake | Operational urgency may bypass privacy boundaries; eConsent version asynchrony may be ignored | Record consent, entitlement, privacy-boundary and routing-legitimacy checks |
| Consent, Entitlement and Privacy Context | Audit, Evidence and Continuity Context | Upstream control / policy gate | Privacy-boundary state, retention and deletion constraints, legal holds | Evidence preservation must respect privacy and entitlement | Defensible preservation may conflict with minimisation; a legal hold may be missed | Record retention, deletion, legal-hold and privacy-boundary state |
| Source and Document Governance Context | All contexts | Upstream control / policy gate | Trusted/quarantined source state, document version and approval state, manifest currency | Source trust is not owned by consuming contexts | The prompt-injection supplier deviation PDF or a shared-account spreadsheet may be treated as usable evidence | Record quarantine decision, version history, approval state, source attribution |
| Supplier and Audit Evidence Context | GxP Batch Evidence Reconciliation Context | Upstream/downstream | Verified audit status, audit-commitment verification state, certificate state, CAPA linkage | Supplier evidence is not owned by batch review | An unverified audit commitment may be treated as closed in the release packet | Record audit reports, commitment verification, certificate provenance, CAPA linkage |
| Supplier and Audit Evidence Context | Supply, Cold-Chain and Allocation Planning Context | Upstream/downstream / partnership | CMO capacity evidence, supplier-risk state, contaminated excipient supplier status | Supplier evidence is not owned by supply planning | CMO capacity promised to two sponsors may be treated as committed | Record capacity evidence, supplier-risk state, sourcing constraint rationale |
| GxP Batch Evidence Reconciliation Context | Quality release reviewers / EU Qualified Person | Upstream/downstream / published language | Batch-review readiness package, evidence-gap report, release-packet completeness state | Readiness visibility is owned by batch review; the release decision is not | Review readiness may be mistaken for release approval or QP certification | Record readiness state, gap ownership, reviewer identity, certification evidence |
| PV Case Intake and Signal Support Context | PV medical/safety reviewers / signal management | Upstream/downstream / published language | Prepared case-review material, duplicate-candidate list, reporting-clock evidence, listedness evidence | Case intake supports review; final PV decisions are not owned by intake | A duplicate or mis-coded case may be treated as a new event; final PV disposition may be displaced | Record receipts, intake timestamps, duplicate rationale, clock reconstruction, terminology version, reviewer routing |
| Supply, Cold-Chain and Allocation Planning Context | Authorised Supply/Quality roles | Upstream/downstream / published language | Traceable recovery options, allocation-constraint report, cold-chain evidence state | Option generation is owned by planning; allocation and shipment are not | A recovery recommendation may be mistaken for an executed allocation or shipment | Record option generation, evidence used, approval requests, escalation, constraint rationale |
| Audit, Evidence and Continuity Context | All contexts | Upstream/downstream / audit sink | Audit-trail completeness, audit-capture-gap state, degraded-mode state, evidence-package state | Traceability is owned by audit; the underlying decision is not | Work may appear evidence-complete when the audit trail is incomplete | Record who did what, from which source, when, why, under which approval or override, with what final action |
| All contexts | Audit, Evidence and Continuity Context | Upstream/downstream / audit sink | Recommendations, drafts, approvals, overrides, releases, escalations, actions, outcomes, closures | Audit records traceability but does not own any regulated decision | The 47-minute audit-capture gap may hide required evidence | Record the audit event envelope for every workflow event |

## 6. Shared Kernel

These terms and statuses must remain consistent across contexts because misunderstanding them can create safety, handoff, or accountability failure.

| Shared term/status | Why it must be consistent |
|---|---|
| Batch identity | Ensures all contexts refer to the same manufactured batch (e.g., NCB204-B24071). |
| Product identity | Ensures all contexts refer to the same product across RIM, ERP, IDMP, labels and safety sources. |
| Material / single-use assembly lot identity | Ensures lineage references are consistent (e.g., SUA-88). |
| Genealogy state | Shows whether material/batch lineage is complete, flagged as a break, or unresolved. |
| Unit-of-measure conventions | Prevents a silent mg/L vs µg/mL conversion from changing a concentration by 1000x. |
| Unit-conversion assumption status | Shows whether a conversion assumption is approved, unapproved, or conflicting. |
| Terminology state | Shows whether MedDRA versions and preferred terms are aligned or conflicting. |
| Effective date | Determines which version of a record, protocol, IB, CCDS or label applies. |
| Authority registry | Records which source is authoritative per business object, jurisdiction and date. |
| Jurisdiction applicability | Determines which market, protocol version or regulatory basis applies. |
| Evidence status | Shows whether each review item is present, complete, flagged, unresolved or no-answer. |
| Checkpoint state | Shows whether required review or approval checkpoints have been reached. |
| Validation state | Shows whether an application or system is validated, conditionally released or research-only. |
| Consent and entitlement status | Ensures patient/participant data is accessed and used only within allowed boundaries. |
| Audit event envelope | Ensures every event records what happened, who owned it, when, from which source, and with what status. |

## 7. Published Language / Handoff Vocabulary

These handoff terms should be used consistently across contexts.

| Handoff term | Business meaning in this case |
|---|---|
| Batch-review readiness | Evidence state where the material needed for batch release review is assembled, complete or explicitly unresolved with ownership. |
| Release-ready | State where accountable Quality and EU QP roles judge that all conditions for batch release are met; only these roles may reach it. |
| Release packet | The assembled evidence package for batch-release review, including genealogy, laboratory results, deviations, CAPA, change control, validation, supplier evidence and completeness status. |
| QP certification | The EU Qualified Person's final batch certification decision; never advisory, never automated. |
| Genealogy break | Missing or unlinked branch in batch lineage (e.g., SUA-88) that remains visible, not silently repaired. |
| Unit-conversion assumption | The stated assumption converting reported units to receiving-interface units (mg/L vs µg/mL); must be approved, never silent. |
| OOS | Out-of-specification laboratory result state; disputed here and not dispositioned in this stage. |
| OOT | Out-of-trend result state; disputed with OOS and the notebook label, and not dispositioned in this stage. |
| Reporting clock | The reconstructed PV reporting timeframe from awareness date and receipts. |
| Awareness date | The date on which an accountable PV role became aware of a report; disputed here. |
| Duplicate ICSR candidate | A case likely describing the same event as another case under an alternative product name; pending accountable review. |
| Preferred term | The MedDRA term chosen to code an event; two versions conflict in this case. |
| Listedness | Whether an event is listed in the IB, CCDS or local label; sources conflict in this case. |
| Expectedness | Whether an event is expected relative to the reference document; final determination remains human-owned. |
| Cold-chain excursion | A shipment temperature outside the approved range with disputed logger clock and pallet association. |
| Aggregation hierarchy | The linkage between product, case, pallet and shipment identifiers. |
| Allocation constraint | A policy-bounded condition limiting how available stock may be proposed for allocation. |
| Compassionate-use entitlement | A patient's lawful basis to receive product outside a registered indication; binds allocation options. |
| Escalation | Formal action created when an unresolved evidence state requires routed accountable attention. |
| Approval | Human review and authorisation by the accountable owner for the relevant decision or content. |
| Override | Human-owned deviation from expected rule or workflow, requiring reason and audit trail. |
| Abstention / no-answer | The declared response when a required state cannot be resolved; no output is produced rather than a guess. |
| Evidence trail | Traceable record of sources, drafts, reviews, approvals, overrides, releases, escalations, actions, outcomes and closures. |

## 8. Partnership Relationships

Some relationships are not simple handoffs. They require coordinated ownership because one context's status affects another context's readiness or safety.

### 8.1 GxP Batch Evidence Reconciliation ↔ Identity, Genealogy and Product Master

Batch-review readiness depends on identity and lineage state, while identity and genealogy ownership depends on batch and product context. A genealogy break (SUA-88) cannot be treated as purely operational; it requires identity/lineage ownership and must remain visible in batch-review readiness.

### 8.2 GxP Batch Evidence Reconciliation ↔ Unit and Terminology Standardisation

Batch-review readiness depends on unit and terminology state. Unit and terminology ownership can surface the mg/L vs µg/mL conflict and the OOS/OOT/notebook disagreement, but it cannot approve the conversion or disposition the assay. The unapproved assumption must remain visible and fail-closed.

### 8.3 GxP Batch Evidence Reconciliation ↔ Supplier and Audit Evidence

Release-packet completeness depends on verified supplier evidence. Supplier and audit ownership can confirm whether the contract-site audit commitment is verified, but it cannot declare the release packet complete for QP purposes without evidence. The unverified commitment must remain visible.

### 8.4 PV Case Intake ↔ Unit and Terminology Standardisation

PV case intake depends on MedDRA version alignment and terminology normalisation, while terminology ownership depends on safety-case context. Two MedDRA versions changing a preferred term must remain conflict-visible; the intake context must never select a winner or make final PV decisions.

### 8.5 PV Case Intake ↔ Authority, Effective-Date and Jurisdiction and Consent, Entitlement and Privacy

Reporting-clock reconstruction, listedness evidence and duplicate handling depend on which source is authoritative and whether consent/entitlement permits the data use. Authority and privacy contexts gate the work; PV intake prepares evidence but never sets the clock or the final PV disposition.

### 8.6 Supply, Cold-Chain and Allocation Planning ↔ Supplier and Audit Evidence

Recovery-option generation depends on supplier and CMO capacity evidence, while supplier evidence ownership depends on supply context. CMO capacity promised to two sponsors must remain a conflict-visible sourcing constraint; no capacity is reserved or stock allocated without explicit authorised human approval.

### 8.7 Audit, Evidence and Continuity ↔ All Contexts

Audit, evidence and continuity is a cross-cutting partner to every context. It records traceability, packages evidence for the 72-hour inspection request and maintains safe operation without AI, but it does not replace Quality, PV, Regulatory, Clinical or Supply ownership.

## 9. Anti-Corruption and Translation Risks

| Boundary | Risk | Required protection |
|---|---|---|
| Contract-laboratory interface language → batch-review language | A concentration reported in mg/L may be read by the receiving interface as µg/mL, changing the value 1000x. | Treat the unit-conversion assumption as unapproved and conflict-visible; no evidence output while unit state is unresolved. |
| MES genealogy language → warehouse consumption language | A single-use assembly lot (SUA-88) present in warehouse consumption but missing from one MES genealogy branch may be silently merged or dropped. | Keep the genealogy break visible with identity/lineage ownership; never repair the lineage silently. |
| MedDRA version language → PV case language | Two MedDRA versions changing the preferred term may split one event into two cases or merge two events into one. | Keep terminology state conflict-visible; version alignment evidence must accompany case material. |
| Product identity language across RIM/ERP/IDMP/labels | The same product may be referenced under different identities across regulatory, ERP and labelling sources, corrupting listedness and linkage. | Resolve product identity through the Identity, Genealogy and Product Master Context and the authority basis before use. |
| Temperature-logger clock language → UTC / cold-chain evidence language | A logger clock set to local time may be compared against UTC, mis-stating excursion duration and severity. | Reconcile logger-clock basis before treating cold-chain evidence as resolved; no disposition of the shipment. |
| Supplier PDF text language → evidence language | The supplier deviation PDF is untrusted and contains hidden prompt-injection text; extracted text may be treated as evidence. | Quarantine untrusted documents in Source and Document Governance until governance review; treat extracted text as untrusted. |
| Listedness-source language (IB vs CCDS vs local label) | The same event may be listed in one reference document and not another, changing expectedness evidence. | Keep listedness conflict-visible; final expectedness determination remains human-owned. |
| Reporting-clock language → compliance language | A disputed awareness date across vendor receipt, affiliate inbox and global safety DB may distort the reporting clock. | Reconstruct the clock as evidence for accountable review; never set the clock automatically. |
| Allocation-policy language → executed supply language | A traceable recovery option may be mistaken for an executed allocation, reservation or shipment. | Require explicit authorised human approval before any inventory status change, reservation, allocation, shipment or recall. |
| Validation-state language → authoritative-system language | An unvalidated or research-only application may be treated as authoritative. | Gate on validation state; ambiguous validation state remains unresolved and fail-closed. |
| Evidence trail → decision ownership | An audit record may be mistaken for an approval or final decision. | Audit records trace decisions; they do not make them. |
| Consent/entitlement status → operational convenience | Operational urgency during shortage or inspection may be used to bypass privacy boundaries. | Require consent, entitlement and privacy legitimacy before patient/participant data access, use, routing or sharing. |

## 10. Known Gaps Mapped to Context Relationships

| Known gap or exception | Primary relationship where gap appears | Why it matters for context mapping | Stage 5 handling |
|---|---|---|---|
| Missing SUA-88 genealogy branch (present in warehouse consumption) | Identity, Genealogy and Product Master Context → GxP Batch Evidence Reconciliation Context | Genealogy handoff between MES and warehouse carries the lineage break into batch review. | Keep as unresolved genealogy break with identity/lineage ownership; do not repair lineage. |
| Unapproved mg/L vs µg/mL unit assumption | Unit and Terminology Standardisation Context → GxP Batch Evidence Reconciliation Context | Unit translation across laboratory interfaces can change a concentration 1000x. | Keep as unapproved unit-conversion assumption; fail-closed on unit state. |
| OOS vs OOT vs notebook-invalid dispute | GxP Batch Evidence Reconciliation Context ↔ Unit and Terminology Standardisation Context | The same assay result carries conflicting states across LIMS, statistical tooling and the notebook. | Keep as disputed result state with open investigation ownership; do not disposition. |
| Unverified contract-site audit commitment | Supplier and Audit Evidence Context → GxP Batch Evidence Reconciliation Context (release packet) | An unverified commitment may be treated as closed, hiding a release-packet gap. | Keep as supplier-evidence gap; commitment must be verified before treated as closed. |
| Back-entered batch-record step | GxP Batch Evidence Reconciliation Context ↔ Audit, Evidence and Continuity Context | A back-entered step after network degradation affects checkpoint and audit evidence. | Keep as checkpoint/audit-evidence gap; do not silently accept or reject. |
| 47-minute audit-capture gap during master-data repair | Audit, Evidence and Continuity Context ↔ all contexts | Work may appear evidence-complete while the audit trail is incomplete. | Keep as audit-trail completeness gap; visible, not filled silently. |
| Disputed PV awareness date | PV Case Intake and Signal Support Context ↔ Authority, Effective-Date and Jurisdiction Context | The reporting clock depends on which source and date are authoritative. | Keep as reporting-clock reconstruction dispute; do not set the clock. |
| Duplicate ICSR cluster under different product names | PV Case Intake and Signal Support Context ↔ Unit and Terminology Standardisation Context | Product-name and terminology differences may split one event into multiple cases. | Keep as duplicate candidates pending accountable review. |
| Two MedDRA versions changing the preferred term | Unit and Terminology Standardisation Context → PV Case Intake and Signal Support Context | Terminology translation across PV systems may corrupt case grouping. | Keep as preferred-term conflict; terminology state unresolved. |
| Listedness conflict between IB, CCDS and local label | PV Case Intake and Signal Support Context ↔ Authority, Effective-Date and Jurisdiction Context ↔ Source and Document Governance Context | Expectedness evidence depends on which reference is authoritative. | Keep as listedness-source conflict; do not pick a winner. |
| Cold-chain logger clock and pallet association disputed | Supply, Cold-Chain and Allocation Planning Context ↔ Authority, Effective-Date and Jurisdiction Context | Logger-clock basis and pallet association determine whether the excursion is real. | Keep as disputed cold-chain evidence; do not disposition the shipment. |
| Missing case-to-pallet aggregation after line restart | Identity, Genealogy and Product Master Context → Supply, Cold-Chain and Allocation Planning Context | Aggregation gap hides which cases are on which pallet. | Keep as aggregation gap requiring evidence linkage. |
| Sole-source excipient contamination with eight-week recovery | Supply, Cold-Chain and Allocation Planning Context ↔ Supplier and Audit Evidence Context | Shortage evidence depends on supplier status and recovery estimate. | Keep as supply-shortage constraint; generate options only. |
| CMO capacity promised to two sponsors | Supply, Cold-Chain and Allocation Planning Context ↔ Supplier and Audit Evidence Context | Competing capacity commitments constrain allocation options. | Keep as sourcing constraint; no capacity reservation without human approval. |
| Demand exceeds available stock | Supply, Cold-Chain and Allocation Planning Context ↔ authorised Supply/Quality roles | Allocation options must respect trial demand, market authorisation and compassionate-use entitlements. | Generate policy-bounded options; allocation requires explicit authorised human approval. |
| Validation-state ambiguity; unapproved macro-enabled spreadsheet | Authority, Effective-Date and Jurisdiction Context ↔ Source and Document Governance Context ↔ Audit, Evidence and Continuity Context | An unvalidated system or unapproved spreadsheet may be treated as authoritative. | Keep as checkpoint and source-governance state unresolved; fail-closed. |
| Untrusted supplier deviation PDF and tool manifests | Source and Document Governance Context → all contexts | A poisoned or stale manifest may be treated as usable evidence. | Quarantine until governance review; treat extracted text as untrusted. |
| Authority hierarchy inconsistent; later timestamps not automatically authoritative | Authority, Effective-Date and Jurisdiction Context ↔ all contexts | Wrong records may be treated as binding for batch, safety or supply evidence. | Keep as contextual-authority gap; no system is universally authoritative. |
| eConsent version asynchrony with pivotal-trial amendment | Consent, Entitlement and Privacy Context ↔ PV Case Intake and trial-data contexts | One country not approving the amendment and asynchronous consent versions affect entitlement. | Keep as consent/entitlement gap; no data use without lawful basis. |
| Ransomware isolation of manufacturing historians; MES/QMS degraded | Audit, Evidence and Continuity Context ↔ GxP Batch Evidence Reconciliation Context | The organisation must operate safely with or without AI during the event. | Keep as continuity requirement; degraded-mode and AI-off operation remain explicit. |

## 11. Boundary Warnings

- Do not treat the context map as technical architecture.
- Do not merge all three workflows into one giant evidence context; that hides accountability and safety boundaries.
- Do not treat GxP Batch Evidence Reconciliation Context as owning batch release, rejection, reprocess, re-label, recall or QP certification; it owns batch-review readiness only.
- Do not allow Unit and Terminology Standardisation Context to silently apply a conversion; unapproved unit-conversion assumptions remain visible and fail-closed.
- Do not let PV Case Intake and Signal Support Context make final seriousness, causality, expectedness, reportability or signal-confirmation decisions.
- Do not treat Supply, Cold-Chain and Allocation Planning Context outputs as executed allocation, reservation, shipment or recall.
- Do not let Identity, Genealogy and Product Master Context silently resolve a genealogy break; breaks remain visible with ownership.
- Do not treat any system (LIMS, MES, safety DB) as universally authoritative; authority is per business object, jurisdiction and effective date, and later timestamps are not automatically more authoritative than approved signed records.
- Do not allow Source and Document Governance Context to treat an untrusted document as usable before quarantine and governance review.
- Do not bypass Consent, Entitlement and Privacy Context when patient or participant data is accessed, used, routed or shared.
- Do not allow Audit, Evidence and Continuity Context to become an afterthought; auditability is required across recommendations, drafts, approvals, overrides, releases, escalations, actions, outcomes and closures, and the organisation must operate safely without AI.
- Do not produce evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved; declare abstention/no-answer instead.

## 12. Stage 5 Quality Gate

The Stage 5 context map is acceptable only if:

- all Stage 4 bounded contexts are represented;
- upstream and downstream relationships are visible;
- partnership relationships are explicitly identified;
- shared kernel terms are clear and business-domain oriented;
- handoff vocabulary is consistent;
- anti-corruption and translation risks are identified, including unit conversion, MedDRA version, product identity, MES-to-warehouse genealogy, logger-clock versus UTC, and untrusted supplier PDF extraction;
- batch release, rejection, reprocess, re-label, recall and QP certification remain human-owned and never owned by an advisory context;
- final PV seriousness, causality, expectedness, reportability and signal-confirmation decisions remain human-owned;
- inventory status change, capacity reservation, stock allocation, shipment and recall initiation require explicit authorised human approval;
- AI remains read-only and advisory, preparing, reconciling, explaining and packaging evidence;
- fail-closed behaviour on unresolved identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation and checkpoint state is preserved;
- consent, entitlement and privacy boundaries remain explicit;
- evidence and audit receive traceability from all contexts;
- known genealogy, unit, OOS/OOT, supplier-evidence, PV, cold-chain, shortage, validation, source-governance and audit gaps are mapped but not resolved;
- the output remains business-domain only and does not introduce architecture or technical implementation.

## 13. NEXT_STAGE_INPUT_BLOCK

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

Stage 5 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 6.
