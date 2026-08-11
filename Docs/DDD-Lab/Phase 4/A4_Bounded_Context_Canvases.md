# A4 — Bounded Context Canvases: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## 1. Stage 4 Mission

Stage 4 converts the Stage 3 ubiquitous language into clear bounded context canvases for the NovaCura Therapeutics Group evidence-reconciliation case. The purpose is to make business ownership visible across the batch-review, pharmacovigilance and supply-recovery workflows, to separate identity, batch, unit/terminology, authority, consent, PV, supply, source-governance, supplier-evidence and audit responsibilities, and to prevent a single overloaded evidence context from hiding safety-critical boundaries.

This stage remains business-domain only. It does not solve batch, safety or supply issues, does not approve batch release or rejection, does not disposition safety cases, does not allocate stock, ship product or initiate recalls, does not provide medical, regulatory or legal advice, and does not create architecture or technical implementation.

## 2. Input Summary

The Stage 4 input comes from the Stage 3 glossary for **governed evidence reconciliation and review support for regulated pharmaceutical workflows**. The scenario concerns the disputed biologics batch NCB204-B24071 (missing SUA-88 genealogy branch, mg/L vs µg/mL unit assumption, disputed OOS/OOT state, unverified supplier-audit commitment, back-entered batch-record step), emerging safety reports (duplicate ICSR candidates, disputed awareness date, MedDRA version mismatch, listedness conflict), a cold-chain failure (disputed logger clocks and pallet association, missing aggregation), a sole-source excipient shortage with CMO capacity conflict, a ransomware event with a 47-minute audit-capture gap, and a multi-agency inspection request.

The core business concern is that batch, safety and supply review work must be evidence-complete, conflict-visible, provenance-backed, authority-respected and fail-closed on uncertainty, while preserving human accountability for regulated decisions, the read-only advisory boundary, consent/entitlement/privacy boundaries, and complete auditability across Workflows A, B and C.

## 3. Bounded Context Design Principles

- A bounded context represents a distinct area of regulated pharmaceutical review work, not a software system.
- Each context must own a clear portion of language, information, statuses, risks, and business responsibility.
- No context should own the entire evidence-reconciliation journey.
- Regulated decision accountability must not be diluted across advisory contexts.
- Batch release, rejection, reprocess, re-label and recall decisions remain inside accountable Quality and EU QP ownership.
- Final PV seriousness, causality, expectedness, reportability and signal-confirmation decisions remain inside accountable PV review ownership.
- Inventory status changes, capacity reservation, stock allocation, shipment and recall initiation remain inside authorised human ownership.
- Consent, entitlement and privacy boundaries must apply across all contexts that access or use patient or participant data.
- Authority must remain contextual per business object, jurisdiction and effective date; no system is universally authoritative.
- Evidence and audit must record what was reviewed, drafted, approved, overridden, released, escalated, executed or closed.
- Known gaps must be placed in the right business context but not resolved.
- Context boundaries should expose handoff risk, not hide it.
- Fail-closed behaviour means no evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.

## 4. Final Bounded Context List

| Bounded Context | One-line purpose |
|---|---|
| Identity, Genealogy and Product Master Context | Owns product, batch, compound and material identity, genealogy and lineage state, and product-master state used by every workflow. |
| GxP Batch Evidence Reconciliation Context | Assembles evidence-complete, conflict-visible material for batch-review readiness (Workflow A) without ever releasing, rejecting, reprocessing, re-labelling or recalling a batch. |
| Unit and Terminology Standardisation Context | Owns unit-conversion assumptions and terminology/reference-data state (mg/L vs µg/mL, MedDRA versions and preferred terms). |
| Authority, Effective-Date and Jurisdiction Context | Owns which source is authoritative per business object, jurisdiction and effective date, including validation state. |
| Consent, Entitlement and Privacy Context | Owns lawful access and use of patient and participant data across consent, entitlement and privacy boundaries. |
| PV Case Intake and Signal Support Context | Supports intake, duplicate detection, terminology normalisation, reporting-clock reconstruction, listedness evidence and multilingual review (Workflow B) without making final PV decisions. |
| Supply, Cold-Chain and Allocation Planning Context | Generates traceable, policy-bounded supply-shortage and cold-chain recovery options (Workflow C) without executing allocation, shipment, reservation or recall. |
| Source and Document Governance Context | Owns versioned, approved, audit-trailed source governance and quarantine of untrusted documents and manifests. |
| Supplier and Audit Evidence Context | Owns verified supplier audits, certificates, commitments and CAPA linkage needed for release-packet completeness. |
| Audit, Evidence and Continuity Context | Owns auditability, evidence packaging, the audit-capture gap and safe operation with or without AI during incidents and inspections. |

## 5. Bounded Context Canvases

### 5.1 Identity, Genealogy and Product Master Context

| Canvas field | Detail |
|---|---|
| Context name | Identity, Genealogy and Product Master Context |
| Business purpose | Own product, batch, compound and material identity, genealogy and lineage, and the product-master state needed by all workflows; surface identity and lineage breaks visibly without resolving them. |
| Primary participants | Quality, Manufacturing, Regulatory Affairs (IDMP/product master), IT/master-data owners, serialisation and genealogy owners. |
| Owned language | Product identity, batch identity, material identity, compound identity, genealogy, material/batch lineage, genealogy break, single-use assembly lot, consumption record, product master, aggregation hierarchy. |
| Owned information/statuses | Product/batch/material identity state, genealogy tree state, lineage completeness status, product-master state, aggregation state. |
| Decisions/statuses owned | Whether identity and lineage are resolved or complete for a batch or product; whether a genealogy break exists and remains visible with ownership. |
| Decisions not owned | Batch release, rejection, reprocess, re-label or recall; QP certification; PV dispositions; unit-conversion acceptance; terminology decisions; allocation, reservation or shipment. |
| Upstream inputs | Product master, batch records (MES/eBR), warehouse consumption records, serialisation events, supplier material data. |
| Downstream outputs | Resolved or flagged identity and lineage state for batch-review readiness, cold-chain aggregation, PV product linkage and inspection packaging. |
| Policies/rules it must respect | No evidence output while identity or genealogy is unresolved; authority is contextual, no system is universally authoritative; genealogy breaks are made visible, not silently repaired. |
| Known gaps/exceptions touching this context | Missing SUA-88 branch in MES genealogy for NCB204-B24071 while present in warehouse consumption; missing case-to-pallet aggregation after a line restart. |
| Audit/evidence needs | Identity-match evidence, lineage source records, genealogy-break identification, aggregation event linkage. |
| Safety risk if boundary is misunderstood | Batch review may be evaluated against incomplete lineage, or an identity mismatch may be hidden across systems. |

### 5.2 GxP Batch Evidence Reconciliation Context

| Canvas field | Detail |
|---|---|
| Context name | GxP Batch Evidence Reconciliation Context |
| Business purpose | Assemble evidence-complete, conflict-visible, provenance-backed material for batch-review readiness (Workflow A) by reconciling genealogy, laboratory results, environmental monitoring, deviations, CAPA, change control, validation state, supplier evidence and release-packet completeness. It never releases, rejects, reprocesses, re-labels or recalls a batch. |
| Primary participants | Quality release reviewers, EU Qualified Person, batch-review coordination, Manufacturing, Laboratory analysts and OOS owners, supplier-quality. |
| Owned language | Batch review, GxP evidence, laboratory result, OOS, OOT, environmental monitoring excursion, deviation, CAPA, change control, validation state, batch-record step, back-entered record, release packet, release-packet completeness, supplier evidence, QP-certification evidence. |
| Owned information/statuses | Evidence status per review item, release-packet completeness state, batch-review readiness state, unresolved evidence list, evidence lineage. |
| Decisions/statuses owned | Whether batch review is ready (batch-review readiness) from an evidence perspective and which evidence gaps remain; not the release decision. |
| Decisions not owned | Batch release, rejection, reprocess, re-label or recall; QP certification (the QP's decision); formulation or specification changes; PV or supply decisions. |
| Upstream inputs | Identity and lineage state, laboratory results, environmental monitoring, deviations, CAPA, change control, validation state, supplier/audit evidence, batch records. |
| Downstream outputs | Batch-review readiness package, evidence-gap report, evidence lineage for release packets, inspection evidence. |
| Policies/rules it must respect | AI never releases/rejects/reprocesses/re-labels/recalls a batch; fail-closed on unresolved identity, genealogy, unit, terminology, validation or checkpoint state; conflicts stay visible; everything auditable. |
| Known gaps/exceptions touching this context | SUA-88 genealogy break; mg/L vs µg/mL unit assumption; OOS/OOT/invalid dispute; unverified supplier-audit commitment in the EU release packet; back-entered batch-record step; 47-minute audit-capture gap. |
| Audit/evidence needs | Reconciliation trail, source citations, gap identification, evidence-gap ownership, reviewer identity. |
| Safety risk if boundary is misunderstood | Review readiness may be confused with release approval, or an unreconciled unit, OOS state or supplier-evidence gap may be hidden inside the packet. |

### 5.3 Unit and Terminology Standardisation Context

| Canvas field | Detail |
|---|---|
| Context name | Unit and Terminology Standardisation Context |
| Business purpose | Own units, terminology and reference data (mg/L vs µg/mL, MedDRA versions and preferred terms) so that batch, safety and supply evidence is interpretable consistently. |
| Primary participants | Quality, Laboratory, Regulatory Affairs, Safety (MedDRA), reference-data owners. |
| Owned language | Unit-conversion assumption, reported unit, receiving-interface assumed unit, terminology normalisation, MedDRA version, preferred term, reference data, terminology state. |
| Owned information/statuses | Unit-conversion assumption status, terminology mapping state, MedDRA version alignment, reference-data state. |
| Decisions/statuses owned | Whether units and terminology are aligned and approved; whether a conversion assumption is unapproved or conflicting; terminology-state status. |
| Decisions not owned | Batch release or rejection, PV seriousness/causality/expectedness/reportability/signal confirmation, allocation, formulation changes. |
| Upstream inputs | Interface mappings, laboratory results, MedDRA versions, regulatory reference data. |
| Downstream outputs | Normalised units and terminology for GxP batch evidence reconciliation, PV case intake and supply planning. |
| Policies/rules it must respect | No evidence output while unit or terminology state is unresolved; conversion assumptions must be approved; terminology changes remain conflict-visible. |
| Known gaps/exceptions touching this context | Unapproved mg/L vs µg/mL assumption; two MedDRA versions changing the preferred term for the same event. |
| Audit/evidence needs | Mapping history, version alignment records, conversion-assumption approval or override records. |
| Safety risk if boundary is misunderstood | A silent unit conversion can change a reported concentration by 1000x, and a terminology mismatch can split or merge safety cases. |

### 5.4 Authority, Effective-Date and Jurisdiction Context

| Canvas field | Detail |
|---|---|
| Context name | Authority, Effective-Date and Jurisdiction Context |
| Business purpose | Define which source or record is authoritative for each business object, jurisdiction and effective date; no system is universally authoritative and a later timestamp is not automatically more authoritative than an approved signed record. |
| Primary participants | Regulatory Affairs, Quality, Privacy/Legal, master-data governance, validation owners. |
| Owned language | Authority, authoritative source, effective date, jurisdiction, approval date, signed record, validation state, master-data repair, protocol version. |
| Owned information/statuses | Authority assignment per object/jurisdiction/date, effective-date state, jurisdiction applicability, validation state. |
| Decisions/statuses owned | Which record is authoritative for a given object, jurisdiction and date; whether effective dates, jurisdiction and validation state are resolved. |
| Decisions not owned | Batch release, rejection or certification, PV dispositions, allocation, shipment or recall, formulation changes. |
| Upstream inputs | Registrations, signed records, approvals, protocol versions, labels, validation inventories. |
| Downstream outputs | Authority, effective-date and jurisdiction basis for all contexts; fail-closed gating when unresolved. |
| Policies/rules it must respect | Authority is contextual; later timestamps are not automatically authoritative; no evidence while authority, effective date, jurisdiction or validation state is unresolved. |
| Known gaps/exceptions touching this context | Inconsistent authority hierarchy; validation-state ambiguity across inventories; pivotal-trial amendment with one country not approved. |
| Audit/evidence needs | Authority rationale, effective-date determination, jurisdiction basis, validation-state records. |
| Safety risk if boundary is misunderstood | The wrong record may be treated as binding, or an unvalidated system may be treated as authoritative. |

### 5.5 Consent, Entitlement and Privacy Context

| Canvas field | Detail |
|---|---|
| Context name | Consent, Entitlement and Privacy Context |
| Business purpose | Govern lawful access and use of patient and participant data across PV case intake, trial data and patient-support data, including cross-border routing, secondary use and sensitive segments. |
| Primary participants | Data Protection Officer, Legal, Clinical, Safety, privacy oversight. |
| Owned language | Consent, entitlement, privacy boundary, cross-border routing, secondary use, sensitive segment, lawful basis. |
| Owned information/statuses | Consent status, entitlement status, privacy-boundary state, routing legitimacy, retention and deletion constraints. |
| Decisions/statuses owned | Whether a role or process is entitled to access or use data under the relevant consent and privacy boundary. |
| Decisions not owned | Batch release, rejection or certification, PV dispositions, allocation, clinical eligibility, formulation changes. |
| Upstream inputs | eConsent, protocol consent versions, entitlement records, retention rules, legal holds. |
| Downstream outputs | Legitimate access/use status for PV intake, trial data, supply and inspection evidence. |
| Policies/rules it must respect | No evidence output while consent/entitlement is unresolved; privacy obligations respected; no secondary use without a lawful basis. |
| Known gaps/exceptions touching this context | eConsent version asynchrony with a pivotal-trial protocol amendment; cross-border routing of safety data; sensitive segments present in general queues. |
| Audit/evidence needs | Consent check, entitlement check, privacy-boundary check, access and use records. |
| Safety risk if boundary is misunderstood | Patient data may be accessed, used or routed without proper consent or entitlement, or legitimate evidence access may be blocked. |

### 5.6 PV Case Intake and Signal Support Context

| Canvas field | Detail |
|---|---|
| Context name | PV Case Intake and Signal Support Context |
| Business purpose | Support intake, duplicate detection, terminology normalisation, source authority, reporting-clock reconstruction, listedness evidence, product-quality linkage and multilingual review (Workflow B). It never makes final seriousness, causality, expectedness, reportability or signal-confirmation decisions. |
| Primary participants | Global Head of Pharmacovigilance, PV case-intake staff, PV medical/safety reviewers, signal management, product-quality linkage. |
| Owned language | ICSR, duplicate ICSR, awareness date, reporting clock, reporting-clock reconstruction, seriousness, causality, expectedness, listedness, investigator brochure (IB), core data sheet (CCDS), local label, preferred term, product-quality complaint, reportability, signal confirmation, case-intake completeness. |
| Owned information/statuses | Case-intake completeness, duplicate-candidate status, reporting-clock reconstruction state, terminology alignment, listedness-source evidence, multilingual review status. |
| Decisions/statuses owned | Whether intake is complete and whether duplicate, terminology, clock and listedness evidence is visible and attributed for accountable review; not the disposition. |
| Decisions not owned | Final seriousness, causality, expectedness, reportability or signal-confirmation decisions; safety-case disposition; clinical eligibility; batch or supply decisions. |
| Upstream inputs | Safety receipts (vendor, affiliate inbox, global safety DB), ICSR candidates, MedDRA versions, IB/CCDS/local labels, product-quality complaints, consent/entitlement status. |
| Downstream outputs | Prepared case-review material, reporting-clock evidence, listedness evidence, duplicate-candidate list, multilingual review material, inspection evidence. |
| Policies/rules it must respect | AI never makes final PV decisions; no evidence while terminology, authority, effective date or consent/entitlement state is unresolved; conflicts remain visible. |
| Known gaps/exceptions touching this context | Disputed awareness date; duplicate ICSR candidates under different product names; MedDRA version mismatch; listedness conflict between IB, CCDS and local label. |
| Audit/evidence needs | Receipts, intake timestamps, duplicate-detection rationale, clock reconstruction evidence, terminology version, listedness sources, reviewer routing. |
| Safety risk if boundary is misunderstood | A duplicate or mis-coded case may be treated as a new event, or a final PV decision may be displaced from accountable reviewers. |

### 5.7 Supply, Cold-Chain and Allocation Planning Context

| Canvas field | Detail |
|---|---|
| Context name | Supply, Cold-Chain and Allocation Planning Context |
| Business purpose | Generate traceable, policy-bounded options for supply-shortage and cold-chain recovery (Workflow C) using inventory, quality status, market authorisation, trial demand, compassionate-use constraints, cold-chain evidence, CMO capacity, transport and allocation policy. It never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval. |
| Primary participants | Supply Chain planning, logistics/serialisation/cold-chain, CMO and supplier-quality, Regulatory Affairs for market-authorisation constraints, Procurement. |
| Owned language | Inventory status, cold-chain excursion, temperature logger, logger clock, pallet association, serialisation aggregation, sole-source excipient, excipient shortage, recovery estimate, CMO capacity, CMO capacity conflict, allocation constraint, allocation policy, compassionate-use entitlement, market authorisation, trial demand, shipment. |
| Owned information/statuses | Inventory status visibility, cold-chain evidence state, allocation-option status, capacity-availability state, recovery-option status. |
| Decisions/statuses owned | Which recovery options are traceable and policy-bounded; whether cold-chain evidence is resolved; option recommendation status prepared for human approval. |
| Decisions not owned | Inventory status change, capacity reservation, stock allocation, shipment, recall initiation, batch release, formulation changes. |
| Upstream inputs | Inventory, quality status, market authorisation, demand forecast, cold-chain evidence, CMO capacity, allocation policy, identity/aggregation state. |
| Downstream outputs | Traceable recovery options, allocation-constraint report, escalation for authorised human approval, inspection evidence. |
| Policies/rules it must respect | No inventory status change, capacity reservation, allocation, shipment or recall without explicit authorised human approval; no evidence while identity, genealogy or cold-chain evidence is unresolved. |
| Known gaps/exceptions touching this context | Cold-chain logger clock and pallet association dispute; missing case-to-pallet aggregation; sole-source excipient contamination with eight-week recovery; CMO capacity conflict; demand exceeds available stock. |
| Audit/evidence needs | Option generation, evidence used for each option, approval requests, escalation records, constraint rationale. |
| Safety risk if boundary is misunderstood | A recovery recommendation may be mistaken for an executed allocation or shipment, or constrained allocation may ignore compassionate-use entitlements. |

### 5.8 Source and Document Governance Context

| Canvas field | Detail |
|---|---|
| Context name | Source and Document Governance Context |
| Business purpose | Govern versioned, owned, approved and audit-trailed sources, and quarantine untrusted documents and manifests (the prompt-injection supplier deviation PDF, stale/unsigned tool manifests, shared-account spreadsheets) before they are used as evidence. |
| Primary participants | Quality, Regulatory Affairs, Document management, IT/security. |
| Owned language | Source, source authority, document version, approved document, untrusted document, manifest, quarantine, transcription, signed original. |
| Owned information/statuses | Document version state, approval state, quarantine state, source trust state, manifest currency. |
| Decisions/statuses owned | Whether a document or source is trusted, versioned, approved and usable as evidence. |
| Decisions not owned | Batch release, rejection or certification, PV dispositions, allocation, content decisions. |
| Upstream inputs | Supplier PDFs, tool manifests, spreadsheets, certificates, vendor portals. |
| Downstream outputs | Trusted-source state to all contexts; quarantine notifications for untrusted documents. |
| Policies/rules it must respect | Untrusted sources are quarantined until governance review; evidence must be provenance-backed; no evidence while source state is unresolved. |
| Known gaps/exceptions touching this context | MALICIOUS_SUPPLIER_DEVIATION.pdf with hidden prompt-injection text; stale/unsigned tool manifests; shared-account spreadsheets with undocumented fields. |
| Audit/evidence needs | Quarantine record, version history, approval state, source attribution, manifest verification. |
| Safety risk if boundary is misunderstood | A poisoned document may be treated as evidence, or an unapproved spreadsheet may silently alter quality, safety or supply decisions. |

### 5.9 Supplier and Audit Evidence Context

| Canvas field | Detail |
|---|---|
| Context name | Supplier and Audit Evidence Context |
| Business purpose | Manage supplier audits, certificates, commitments and CAPA linkage so that release-packet completeness is supported by verified supplier evidence. |
| Primary participants | Supplier-quality, Procurement, Quality, CMO quality. |
| Owned language | Supplier audit, audit commitment, audit closure, certificate of analysis, certificate status, supplier evidence, CAPA linkage. |
| Owned information/statuses | Audit status, audit-commitment verification state, certificate state, supplier-evidence completeness. |
| Decisions/statuses owned | Whether supplier audit and commitment evidence is verified and complete; whether supplier CAPA linkage is visible. |
| Decisions not owned | Batch release, rejection or certification, allocation, formulation changes, recall. |
| Upstream inputs | Audit reports, commitments, certificates, CAPA records, CMO portals. |
| Downstream outputs | Verified supplier evidence to GxP batch evidence reconciliation (release packets) and supply planning. |
| Policies/rules it must respect | Audit commitments must be independently verified before they are treated as closed; no evidence while supplier-evidence state is unresolved. |
| Known gaps/exceptions touching this context | Contract-site audit commitment claimed closed but not independently verified in the EU release packet; CMO capacity conflict; contaminated sole-source excipient supplier. |
| Audit/evidence needs | Audit reports, commitment verification, certificate provenance, CAPA linkage records. |
| Safety risk if boundary is misunderstood | An unverified commitment may be treated as closed, hiding a gap in release-packet completeness. |

### 5.10 Audit, Evidence and Continuity Context

| Canvas field | Detail |
|---|---|
| Context name | Audit, Evidence and Continuity Context |
| Business purpose | Preserve traceability of every recommendation, draft, approval, override, release, escalation, action, outcome and closure; ensure the operation can run safely with or without AI (ransomware, degraded mode, model outage); and package evidence for inspection. |
| Primary participants | Audit/quality oversight, CISO, IT operations, finance/procurement, all accountable roles. |
| Owned language | Audit trail, audit-capture gap, auditability, recommendation, draft, approval, override, escalation, final action, evidence package, degraded mode, operate safely without AI, continuity requirement, master-data repair window. |
| Owned information/statuses | Audit-trail completeness, audit-capture-gap state, degraded-mode state, evidence-package state, continuity state. |
| Decisions/statuses owned | Whether required events are captured and auditable; whether the evidence package is traceable; continuity posture during incidents. |
| Decisions not owned | Batch release, rejection or certification, PV dispositions, allocation, shipment or recall. |
| Upstream inputs | Events from all contexts, security incidents, downtime records, retention and legal-hold records. |
| Downstream outputs | Auditable trail, evidence package for inspection (e.g., the 72-hour multi-agency request), audit-capture-gap reports. |
| Policies/rules it must respect | Everything auditable; the organisation must operate safely without AI; evidence output only when required states are resolved; the audit-capture gap remains visible. |
| Known gaps/exceptions touching this context | 47-minute audit-capture gap during master-data repair; ransomware isolation of manufacturing historians; degraded MES/QMS; validation-state ambiguity; unapproved macro-enabled spreadsheet. |
| Audit/evidence needs | This context owns the audit/evidence need itself: who did what, from what source, when, why, under which approval or override, and what final action resulted. |
| Safety risk if boundary is misunderstood | Work may appear evidence-complete when the audit trail is actually incomplete, or the organisation may stop operating safely when AI is unavailable. |

## 6. Known Gaps Mapped to Bounded Contexts

| Known gap or exception | Primary bounded context | Coordinating / dependent contexts | Stage 4 handling |
|---|---|---|---|
| Missing SUA-88 genealogy branch (present in warehouse consumption) | Identity, Genealogy and Product Master Context | GxP Batch Evidence Reconciliation Context; Supply, Cold-Chain and Allocation Planning Context | Identify as a genealogy break requiring identity/lineage ownership; do not repair the lineage. |
| mg/L vs µg/mL unit assumption | Unit and Terminology Standardisation Context | GxP Batch Evidence Reconciliation Context; PV Case Intake and Signal Support Context | Identify as an unapproved unit-conversion assumption; fail-closed on unit state. |
| OOS vs OOT vs invalid dispute | GxP Batch Evidence Reconciliation Context | Unit and Terminology Standardisation Context; Identity, Genealogy and Product Master Context | Identify as a disputed assay result state with open investigation ownership; do not disposition. |
| Unverified supplier-audit commitment | Supplier and Audit Evidence Context | GxP Batch Evidence Reconciliation Context (release packet) | Identify as supplier-evidence gap; commitment must be verified before treated as closed. |
| Back-entered batch-record step | GxP Batch Evidence Reconciliation Context | Audit, Evidence and Continuity Context | Identify as a back-entered record requiring checkpoint and audit evidence. |
| 47-minute audit-capture gap | Audit, Evidence and Continuity Context | GxP Batch Evidence Reconciliation Context; Authority, Effective-Date and Jurisdiction Context | Identify as an audit-trail completeness gap; keep visible, do not fill silently. |
| Disputed PV awareness date | PV Case Intake and Signal Support Context | Authority, Effective-Date and Jurisdiction Context; Audit, Evidence and Continuity Context | Identify as reporting-clock reconstruction dispute; do not set the clock. |
| Duplicate ICSR candidates | PV Case Intake and Signal Support Context | Unit and Terminology Standardisation Context | Identify as duplicate candidates pending accountable review. |
| MedDRA version mismatch | Unit and Terminology Standardisation Context | PV Case Intake and Signal Support Context | Identify as preferred-term conflict; terminology state unresolved. |
| Listedness conflict (IB/CCDS/local label) | PV Case Intake and Signal Support Context | Authority, Effective-Date and Jurisdiction Context; Source and Document Governance Context | Identify as listedness-source conflict; do not pick a winner. |
| Cold-chain logger/pallet dispute | Supply, Cold-Chain and Allocation Planning Context | Identity, Genealogy and Product Master Context; Authority, Effective-Date and Jurisdiction Context | Identify as disputed cold-chain evidence; do not disposition the shipment. |
| Missing case-to-pallet aggregation | Identity, Genealogy and Product Master Context | Supply, Cold-Chain and Allocation Planning Context | Identify as aggregation gap requiring evidence linkage. |
| Sole-source excipient shortage / CMO capacity conflict / demand exceeds stock | Supply, Cold-Chain and Allocation Planning Context | Supplier and Audit Evidence Context; Procurement | Identify as supply-shortage constraint; generate options only, no allocation without authorised human approval. |
| Validation-state ambiguity / unapproved spreadsheet | Authority, Effective-Date and Jurisdiction Context | Source and Document Governance Context; Audit, Evidence and Continuity Context | Identify as checkpoint and source-governance state unresolved. |
| Untrusted supplier PDF / tool manifests | Source and Document Governance Context | Consent, Entitlement and Privacy Context (where patient data involved); Audit, Evidence and Continuity Context | Identify as untrusted-source governance; quarantine before use. |
| Authority hierarchy inconsistent | Authority, Effective-Date and Jurisdiction Context | All contexts | Identify as contextual-authority gap; later timestamps not automatically authoritative. |
| Deliberate stakeholder conflicts | All contexts via governance | Audit, Evidence and Continuity Context | Identify as governance and continuity risks; do not resolve at this stage. |

## 7. Boundary Warnings

- Do not treat **GxP Batch Evidence Reconciliation Context** as owning batch release, rejection, reprocess, re-label, recall or QP certification; it owns review readiness only.
- Do not allow **Unit and Terminology Standardisation Context** to silently apply a conversion; unapproved conversion assumptions remain visible.
- Do not let **PV Case Intake and Signal Support Context** make final seriousness, causality, expectedness, reportability or signal-confirmation decisions.
- Do not treat **Supply, Cold-Chain and Allocation Planning Context** outputs as executed allocation, reservation, shipment or recall.
- Do not let **Identity, Genealogy and Product Master Context** silently resolve a genealogy break; breaks remain visible with ownership.
- Do not treat any system (LIMS, MES, safety DB) as universally authoritative; authority is per business object, jurisdiction and effective date.
- Do not allow **Source and Document Governance Context** to treat an untrusted document as usable before quarantine and governance review.
- Do not bypass **Consent, Entitlement and Privacy Context** when patient or participant data is accessed, used, routed or shared.
- Do not allow **Audit, Evidence and Continuity Context** to become an afterthought; auditability is required across recommendations, drafts, approvals, overrides, releases, escalations, actions, outcomes and closures, and the organisation must operate safely without AI.
- Do not merge all three workflows into one giant evidence context, because that hides accountability and safety boundaries.
- Do not produce evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.

## 8. Stage 4 Quality Gate

The Stage 4 bounded context canvases are acceptable only if:

- each context has a clear business purpose;
- each context owns distinct language and statuses;
- no context can execute a regulated decision it does not own;
- batch release, rejection, reprocess, re-label, recall and QP certification are never owned by an advisory context;
- final PV seriousness, causality, expectedness, reportability and signal-confirmation decisions are never owned by an advisory context;
- inventory status change, capacity reservation, stock allocation, shipment and recall initiation require explicit authorised human approval;
- AI remains read-only and advisory, preparing, reconciling, explaining and packaging evidence;
- fail-closed behaviour on unresolved identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation and checkpoint state is preserved;
- known genealogy, unit, OOS/OOT, supplier-evidence, PV, cold-chain, shortage, validation, source-governance and audit gaps are mapped but not resolved;
- consent, entitlement and privacy boundaries remain explicit;
- everything remains auditable and defensible under inspection;
- no context is overloaded to own the full evidence-reconciliation journey;
- cross-context handoffs and boundary risks are visible for Stage 5.

## 9. NEXT_STAGE_INPUT_BLOCK

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

Stage 4 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 5.
