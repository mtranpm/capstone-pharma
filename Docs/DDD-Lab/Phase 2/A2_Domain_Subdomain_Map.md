# A2 — Domain and Subdomain Map: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

This artifact is the Stage 2 output. It is business-domain only: it maps the domain and subdomains, it does not solve the case, does not provide medical, regulatory or legal advice, does not resolve any product, batch, compound, safety, quality or supply conflict, and does not introduce architecture or technical implementation.

## 1. Stage 2 Mission

Stage 2 identifies the main business domain represented by the case and separates it into core, supporting and generic/reusable areas, so that later stages can define ubiquitous language, bounded contexts and ownership without merging regulated review work into unsafe single contexts. It maps known gaps to the subdomains that must own or coordinate them, and it carries forward every non-negotiable.

## 2. Input Summary

NovaCura Therapeutics Group cannot reliably and quickly assemble evidence-complete, conflict-visible, provenance-backed, authority-respected material for regulated batch-review, pharmacovigilance and supply-recovery decisions, because its enterprise systems fragment identifiers, timestamps, terminology, access controls and authority hierarchies. The required work is confined to three advisory workflows: GxP evidence reconciliation for batch-review readiness (Workflow A), pharmacovigilance case-intake and signal-support (Workflow B), and bounded supply-shortage and cold-chain recovery planning (Workflow C). The AI support must remain read-only and advisory, and regulated decisions must remain with accountable Quality, Safety, Regulatory, Clinical and Supply roles.

## 3. Main Business Domain

The main business domain is **governed evidence reconciliation and review support for regulated pharmaceutical workflows**.

It is the main domain because the case is fundamentally about the work of preparing, validating, reconciling, explaining, packaging and defending evidence so that accountable humans can perform batch review, pharmacovigilance case handling and supply recovery. The value of the organisation in this case is created by completing that review and release work with trustworthy evidence under a 14% lead-time reduction target, while every regulated decision remains human-owned. Systems, records and AI capabilities are support for this domain, not the domain itself.

## 4. Core Subdomains

### GxP evidence reconciliation for batch-review readiness (Workflow A)

- **Business purpose:** assemble evidence-complete, conflict-visible, provenance-backed material so accountable Quality roles and the EU Qualified Person can assess batch-review readiness for release decisions.
- **Key responsibilities:** reconcile batch genealogy, laboratory results, environmental monitoring, deviations, CAPA, change control, validation state, supplier evidence and release-packet completeness; surface gaps, contradictions and evidence lineage; flag unresolved identity, genealogy, unit, OOS/OOT, audit and validation issues.
- **Key risks if weak or missing:** unreconciled genealogy breaks (e.g., missing SUA-88 branch), unit-conversion defects (mg/L vs µg/mL), disputed OOS/OOT states, unverified supplier-audit commitments and back-entered records can block QP certification, delay release, or hide evidence problems under inspection.

### Pharmacovigilance case-intake and signal-support (Workflow B)

- **Business purpose:** support intake, duplicate detection, terminology normalisation, source authority, reporting-clock reconstruction, listedness evidence, product-quality linkage and multilingual review so PV staff can manage cases and signals safely and consistently.
- **Key responsibilities:** surface duplicate ICSR candidates, reconstruct reporting clocks from receipts, normalise MedDRA terminology, align listedness sources, link product-quality complaints to cases, and prepare multilingual review material.
- **Key risks if weak or missing:** duplicate cases, disputed awareness dates, MedDRA version mismatch and listedness conflicts can distort reporting-clock compliance, signal grouping and benefit-risk assessment; the workflow must never make final seriousness, causality, expectedness, reportability or signal-confirmation decisions.

### Bounded supply-shortage and cold-chain recovery planning (Workflow C)

- **Business purpose:** generate traceable, policy-bounded options for resolving supply shortages and cold-chain failures using inventory, quality status, market authorisation, trial demand, compassionate-use constraints, cold-chain evidence, CMO capacity, transport and allocation policy.
- **Key responsibilities:** reconstruct cold-chain evidence (logger clocks, pallet association, aggregation), surface allocation constraints and competing demand, evaluate CMO and excipient-supply options, and prepare options for human approval.
- **Key risks if weak or missing:** unresolved logger clocks or aggregation gaps, constrained allocation with compassionate-use obligations, and sole-source excipient shortages can cause stock-outs, mis-allocation, or unwarranted recall consideration; the workflow must never change inventory status, reserve capacity, allocate stock, ship product or initiate a recall without explicit authorised human approval.

## 5. Supporting Subdomains

- **Identity, genealogy and product-master resolution:** resolves product, batch, compound and material identity and lineage. Supports the core domain because every workflow depends on correct identity and genealogy (e.g., batch NCB204-B24071 and single-use assembly lot SUA-88).
- **Unit, terminology and reference-data standardisation:** resolves units (mg/L vs µg/mL), MedDRA versions and reference data across systems. Supports the core domain because conflicting units and terminology corrupt batch, safety and supply evidence.
- **Authority, effective-date and jurisdiction management:** defines which system or record is authoritative for each business object, jurisdiction and effective time. Supports the core domain because no system is universally authoritative and later timestamps are not automatically more authoritative than approved signed records.
- **Consent, entitlement and privacy management:** governs lawful use of patient and participant data, cross-border routing and secondary use. Supports the core domain because PV case intake, trial data and patient-support data carry consent, entitlement and privacy obligations.
- **Source and document governance:** governs versioned, owned, approved and audit-trailed sources, including untrusted documents and manifests. Supports the core domain because evidence quality depends on source governance (e.g., the prompt-injection supplier deviation PDF must be quarantined).
- **Supplier and audit-evidence management:** manages supplier audits, certificates, commitments and CAPA linkage. Supports the core domain because release-packet completeness depends on verified supplier evidence.
- **Regulatory and inspection-readiness coordination:** prepares traceable evidence for submissions and multi-agency inspection requests. Supports the core domain because the 72-hour inspection request spans trial, batch, safety and AI-system evidence.
- **Quality-event and deviation lineage:** links deviations, CAPA, change control and environmental excursions into a coherent lineage. Supports the core domain because batch-review readiness depends on resolved or visible quality-event lineage.
- **Evidence and audit-trail management:** records what happened, who owned it, when, with what source and status. Supports the core domain because every workflow must be auditable and defensible.
- **Continuity, reliability and economy management:** keeps review work safe during ransomware, degraded mode, model outage and vendor-exit conditions. Supports the core domain because the organisation must operate safely with or without AI.

## 6. Generic / Reusable Organizational Capabilities

- Identity and access management (least privilege, current authorisation, revocation lag detection)
- Time and clock synchronisation
- Audit logging (immutable, complete, tamper-evident)
- Document and record management (versioning, retention, legal hold, deletion)
- Master data management (products, batches, suppliers, customers)
- Monitoring, alerting and telemetry (usage, cost, token budgets)
- Notification and escalation routing
- Reporting and evidence packaging (structured outputs, citations, no-answer paths)
- Validation and qualification state management (GxP-relevant components)
- Training and competency management for accountable roles

## 7. Domain and Subdomain Map

```text
MAIN DOMAIN: Governed evidence reconciliation and review support
             for regulated pharmaceutical workflows
  |
  |-- CORE SUBDOMAINS
  |     |-- GxP evidence reconciliation for batch-review readiness (Workflow A)
  |     |-- Pharmacovigilance case-intake and signal-support (Workflow B)
  |     `-- Bounded supply-shortage and cold-chain recovery planning (Workflow C)
  |
  |-- SUPPORTING SUBDOMAINS
  |     |-- Identity, genealogy and product-master resolution
  |     |-- Unit, terminology and reference-data standardisation
  |     |-- Authority, effective-date and jurisdiction management
  |     |-- Consent, entitlement and privacy management
  |     |-- Source and document governance
  |     |-- Supplier and audit-evidence management
  |     |-- Regulatory and inspection-readiness coordination
  |     |-- Quality-event and deviation lineage
  |     |-- Evidence and audit-trail management
  |     `-- Continuity, reliability and economy management
  |
  `-- GENERIC / REUSABLE CAPABILITIES
        |-- Identity and access management
        |-- Time and clock synchronisation
        |-- Audit logging
        |-- Document and record management
        |-- Master data management
        |-- Monitoring, alerting and telemetry
        |-- Notification and escalation routing
        |-- Reporting and evidence packaging
        |-- Validation and qualification state management
        `-- Training and competency management
```

## 8. Known Gaps Mapped to Subdomains

- Incomplete genealogy for NCB204-B24071 (missing SUA-88 branch) → Identity, genealogy and product-master resolution; GxP evidence reconciliation (Workflow A).
- Unapproved mg/L vs µg/mL unit assumption → Unit, terminology and reference-data standardisation; GxP evidence reconciliation (Workflow A).
- Disputed OOS/OOT state with open investigation → Quality-event and deviation lineage; GxP evidence reconciliation (Workflow A).
- Unverified supplier-audit commitment in release packet → Supplier and audit-evidence management; GxP evidence reconciliation (Workflow A).
- Back-entered batch-record step; 47-minute audit-capture gap → Evidence and audit-trail management; GxP evidence reconciliation (Workflow A).
- Disputed PV awareness date; duplicate ICSR candidates; MedDRA version mismatch; listedness-source conflict → Pharmacovigilance case-intake and signal-support (Workflow B); Unit, terminology and reference-data standardisation; Authority, effective-date and jurisdiction management.
- Cold-chain logger clocks and pallet association disputed; missing serialisation aggregation → Bounded supply-shortage and cold-chain recovery planning (Workflow C); Identity, genealogy and product-master resolution.
- Sole-source excipient shortage; CMO capacity conflict; demand exceeds available stock → Bounded supply-shortage and cold-chain recovery planning (Workflow C); Supplier and audit-evidence management.
- Validation-state ambiguity; unapproved macro-enabled spreadsheet → Authority, effective-date and jurisdiction management; Validation state management capability.
- Untrusted prompt-injection PDF and tool manifests → Source and document governance; Consent, entitlement and privacy management (where patient data involved).
- Authority hierarchy inconsistent; later timestamps not automatically authoritative → Authority, effective-date and jurisdiction management.
- Deliberate stakeholder conflicts (speed vs completeness; standardisation vs jurisdictional variation; minimisation vs preservation; bundled vendor vs substitutability; automation vs prespecified analysis) → All core subdomains via governance; Continuity, reliability and economy management.

## 9. Ownership Signals for Later Stages

- GxP evidence reconciliation (Workflow A): Chief Quality Officer, EU Qualified Person, Quality release reviewers, Manufacturing, Laboratory/OOS owners, supplier-quality.
- PV case-intake and signal-support (Workflow B): Global Head of Pharmacovigilance, PV case-intake staff, PV medical reviewers, signal management.
- Bounded supply-shortage and cold-chain recovery (Workflow C): Supply Chain VP, supply planners, logistics/serialisation/cold-chain, CMO and supplier-quality, regulatory for market-authorisation constraints.
- Identity/genealogy/product-master: Quality, Manufacturing, Regulatory (IDMP), IT/master-data owners.
- Unit/terminology/reference data: Quality, Laboratory, Regulatory, Safety (MedDRA).
- Authority/effective-date/jurisdiction: Regulatory Affairs, Quality, Privacy/Legal.
- Consent/entitlement/privacy: Data Protection Officer, Legal, Clinical, Safety.
- Source and document governance: Quality, Regulatory, Document management.
- Supplier/audit evidence: Supplier-quality, Procurement, Quality.
- Regulatory/inspection-readiness: Regulatory Affairs, Quality, all evidence owners.
- Evidence/audit trail: Quality, Safety, Regulatory, IT/security, all accountable roles.
- Continuity/reliability/economy: CISO, IT operations, finance/procurement.
- Ownership is signalled, not finalised, at this stage.

## 10. Boundary Warnings

- Do not treat systems or records (LIMS, MES, safety DB) as the domain; the domain is the regulated review and reconciliation work.
- Do not merge all three workflows into one giant context; each has distinct decisions, owners and risks.
- Do not confuse supporting subdomains with core value-creation; the core is batch, safety and supply review readiness.
- Do not let a supporting subdomain (e.g., identity resolution) silently make a regulated decision.
- Do not treat authority as global; it is per business object, jurisdiction and effective date.
- Do not resolve any known gap at this stage; gaps remain visible and mapped, not fixed.

## 11. Non-Negotiables Carried Forward

- The AI never releases, rejects, reprocesses, re-labels or recalls a batch.
- The AI never makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions.
- The AI never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval.
- The AI never changes formulation, specification, clinical eligibility, safety-case disposition, batch release or recall decisions.
- Regulated accountability remains with the accountable Quality, Safety, Regulatory, Clinical and Supply roles.
- Evidence output must not be produced while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
- Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable.
- The system operates read-only and advisory; it prepares, reconciles, explains and packages evidence.

## 12. Open Questions for Stage 3

- What is the precise shared meaning of "evidence-complete", "conflict-visible", "authority-respected" and "fail-closed" across the workflows?
- What does "batch-review readiness" mean and when does it become "release-ready"?
- What is the precise meaning of "reporting clock" and "awareness date" for PV case intake?
- What does "listedness" and "expectedness" mean relative to IB, CCDS and local label?
- What does "allocation constraint" and "compassionate-use entitlement" mean in Workflow C?
- Which terms (e.g., OOS, OOT, genealogy, release packet, QP certification, entitlement) need precise definition before modelling continues?

## 13. STAGE_3_INPUT_BLOCK

> **Main business domain.** Governed evidence reconciliation and review support for regulated pharmaceutical workflows.
>
> **Core subdomains.** GxP evidence reconciliation for batch-review readiness (Workflow A); pharmacovigilance case-intake and signal-support (Workflow B); bounded supply-shortage and cold-chain recovery planning (Workflow C).
>
> **Supporting subdomains.** Identity, genealogy and product-master resolution; unit, terminology and reference-data standardisation; authority, effective-date and jurisdiction management; consent, entitlement and privacy management; source and document governance; supplier and audit-evidence management; regulatory and inspection-readiness coordination; quality-event and deviation lineage; evidence and audit-trail management; continuity, reliability and economy management.
>
> **Reusable capabilities.** Identity and access management; time and clock synchronisation; audit logging; document and record management; master data management; monitoring, alerting and telemetry; notification and escalation routing; reporting and evidence packaging; validation and qualification state management; training and competency management.
>
> **Known gaps mapped to subdomains.** Genealogy break (SUA-88), unit conversion (mg/L vs µg/mL), OOS/OOT dispute, unverified supplier-audit commitment, back-entered batch-record step and audit-capture gap → Workflow A subdomain (with identity/unit/lineage support). Disputed PV awareness date, duplicate ICSR candidates, MedDRA version mismatch, listedness conflict → Workflow B subdomain. Cold-chain logger/pallet dispute, missing aggregation, excipient shortage, CMO capacity conflict, constrained allocation → Workflow C subdomain. Validation-state ambiguity, untrusted PDF/manifests, authority-hierarchy inconsistency → supporting subdomains.
>
> **Ownership signals.** Quality/EU QP/Manufacturing/Laboratory/supplier-quality for Workflow A; Global Head of PV, case intake, medical reviewers, signal management for Workflow B; Supply Chain, logistics/serialisation/cold-chain, CMO/supplier-quality, regulatory for Workflow C; DPO/Legal for privacy; CISO for continuity/cyber; Regulatory Affairs for authority/jurisdiction and inspection readiness.
>
> **Non-negotiables.** AI never releases/rejects/reprocesses/re-labels/recalls a batch; never makes final PV decisions; never changes inventory status, reserves capacity, allocates stock, ships or initiates recall without explicit authorised human approval; never changes formulation, specification, clinical eligibility, safety-case disposition, batch-release or recall decisions; regulated accountability stays human; no evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved; everything auditable; read-only and advisory.
>
> **Terms needing precise definition.** Evidence-complete; conflict-visible; authority-respected; fail-closed; batch-review readiness; release-ready; OOS; OOT; genealogy; release packet; QP certification; reporting clock; awareness date; listedness; expectedness; duplicate ICSR; allocation constraint; compassionate-use entitlement; cold-chain excursion; aggregation; effective date; validation state.
>
> **Open questions.** What does each core workflow mean precisely in business language? Which terms are owned by which roles? Which terms imply approval, release, completion or an executed regulated action and must therefore never be used loosely?

> "Stage 2 complete. Use the STAGE_3_INPUT_BLOCK as the main input for Stage 3."
