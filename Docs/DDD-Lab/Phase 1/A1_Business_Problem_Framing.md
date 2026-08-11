# A1 — Business Problem Framing: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

This artifact is the Stage 1 output. It is business-domain only: it frames the problem, it does not solve it, does not provide medical, regulatory or legal advice, does not resolve any product, batch, compound, safety, quality or supply conflict, and does not introduce architecture or technical implementation.

## 1. Stage 1 Mission

Stage 1 converts the Stage 0 context pack into a clean, business-only problem framing that all later stages can use. It states the business challenge, the mandatory workflows, the affected roles, the desired outcomes, the non-negotiable safety boundaries, and the unresolved gaps that must remain visible. It deliberately does not design solutions, name technologies, or resolve any of the deliberate conflicts in the evidence.

## 2. Business Problem Statement

NovaCura Therapeutics Group cannot reliably and quickly assemble evidence-complete, conflict-visible, provenance-backed, authority-respected material for regulated batch-review, pharmacovigilance and supply-recovery decisions, because its enterprises systems fragment identifiers, timestamps, terminology, access controls and authority hierarchies, forcing accountable humans to reconcile evidence manually, slowly, and without a defensible evidence trail.

## 3. Problem Narrative

NovaCura Therapeutics Group is a global pharmaceutical company operating discovery, clinical development, pharmacovigilance, manufacturing, quality, and distribution across India, Germany, Ireland, the United States, the UAE and Singapore, with a portfolio spanning an oral oncology small molecule (NCX-101), a pivotal biologics antibody (NCB-204), a sterile injectable (NCS-310) and a rare-disease gene-therapy programme (NCR-415). Its work depends on evidence that lives across LIMS, MES, electronic batch records, QMS, RIM, EDC, eConsent, IRT, CTMS, safety databases, serialisation platforms, data lakes, spreadsheets, vendor portals and research environments. No system is universally authoritative, and a later timestamp is not automatically more authoritative than an approved signed record.

During the capstone window, the situation concentrates. A pivotal-trial amendment is not yet approved in one country while sites execute multiple protocol versions. The disputed biologics batch NCB204-B24071 has a genealogy branch missing a single-use assembly lot (SUA-88), a contract laboratory concentration transmitted in mg/L while the receiving interface assumes µg/mL, an assay marked OOS by LIMS, OOT by statistical tooling and invalid by the laboratory notebook, an unverified supplier-audit commitment in the EU release packet, and a batch-record step back-entered after network degradation. Safety reports emerge that may duplicate one another under different product names, with a disputed awareness date, a MedDRA version mismatch and a listedness conflict between the investigator brochure, core data sheet and local label. A sterile-area excursion near fill-finish was corrected after initial review. A biologic shipment exceeds cold-chain range with disputed logger clocks and pallet association, and serialisation aggregation is missing after a line restart. A sole-source excipient supplier reports contamination with an eight-week recovery estimate while a CMO promises capacity to two sponsors and demand exceeds available stock across markets, trials and compassionate-use programmes. A ransomware event isolates manufacturing historians and degrades MES and QMS, and audit capture was disabled for 47 minutes. Regulators then request traceable evidence spanning trial data, batch history, safety cases and AI-system controls within 72 hours.

In this setting the accountable Quality, Safety, Regulatory, Clinical and Supply roles must prepare, validate, explain, package and defend evidence for batch review, pharmacovigilance case handling and supply recovery — while the AI support they use must never release, reject, reprocess, re-label or recall a batch; never make final PV decisions; never change inventory status, reserve capacity, allocate stock, ship product or initiate a recall without explicit authorised human approval; and never change formulation, specification, clinical eligibility, safety-case disposition, batch release or recall decisions.

## 4. Problem Decomposition

- **Product and batch identity/genealogy risk:** unresolved identity, missing genealogy branch (SUA-88), unapproved unit conversion (mg/L vs µg/mL), disputed OOS/OOT state, back-entered batch-record step.
- **Evidence and provenance risk:** missing, conflicting, untrusted and poorly attributable evidence; a supplier-audit commitment claimed closed but unverified; certificates transcribed without the original signed source; a 47-minute audit-capture gap.
- **Terminology, authority and jurisdictional risk:** inconsistent terminology, authority hierarchy and effective dates across systems, products and regions; no single authoritative system.
- **Consent, entitlement and privacy risk:** patient and participant data across affiliates, cross-border routing, secondary-use questions, sensitive segments within general queues.
- **Safety-case and reporting risk:** duplicate ICSR candidates, disputed awareness dates feeding reporting clocks, MedDRA version mismatch, listedness/expectedness conflicts, multilingual review quality.
- **Supply and cold-chain risk:** sole-source excipient shortage, cold-chain excursion with disputed logger clocks and pallet association, missing aggregation, CMO capacity conflict, constrained allocation with compassionate-use obligations.
- **Operational, reliability and economic risk:** ransomware and network degradation, model outage and cost pressure, vendor concentration, telemetry and token budget concerns.
- **Ownership and exception-handling risk:** unclear ownership of closure, escalation, override and evidence-gap handling across Quality, Safety, Regulatory, Clinical and Supply.

## 5. Affected Roles and Functions

- Chief Quality Officer and pharmaceutical quality-system function
- EU Qualified Person(s) for batch certification
- Quality release reviewers and batch-review coordination
- Manufacturing and sterile-fill operations
- Laboratory analysts, LIMS/CDS and OOS investigation owners
- Global Head of Pharmacovigilance and PV case-intake/processing staff
- PV medical/safety reviewers and signal-management function
- Clinical Operations and trial-data functions
- Regulatory Affairs (RIM, submissions, labelling, IDMP)
- Supply Chain planning and shortage/risk management
- Logistics, serialisation and cold-chain operations
- Contract manufacturing organisations (CMOs) and supplier quality
- Procurement and vendor management
- Data Protection Officer and privacy/legal function
- CISO and cybersecurity/incident-response function
- Biostatistics and trial-integrity function
- Patient-safety voice and clinical/safety governance forums

## 6. Business Impact

The board requires a 14% reduction in end-to-end release lead time without changing registered specifications or weakening independent Quality authority. Today the impact of the fragmentation and converging events is concentrated in review and release delays: genealogy breaks and unit assumptions block batch-review readiness; supplier-audit evidence gaps block QP certification; disputed awareness dates and duplicate ICSR candidates threaten timely, complete and consistent safety case handling; cold-chain logger disputes and allocation constraints threaten supply continuity and shortage avoidance; and a 72-hour multi-agency inspection request demands traceable evidence the enterprise cannot currently produce quickly. Speed conflicts with completeness: Quality and Manufacturing disagree on the binding constraint, and local accountable roles require jurisdictional variation while global process owners seek standardisation.

## 7. Desired Business Outcomes

- Batch, safety and supply review work that is evidence-complete, conflict-visible, provenance-backed and authority-respected.
- Fail-closed behaviour on any unresolved identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state.
- Read-only, advisory AI support that prepares, reconciles, explains and packages evidence.
- Regulated decisions (batch release/rejection, PV dispositions, allocation, recall) owned by accountable human roles.
- A defensible, auditable trail for every recommendation, draft, approval, override, release, escalation, action, outcome and closure.
- A 14% reduction in end-to-end release lead time without changing registered specifications or weakening independent Quality authority.

## 8. Scope Boundary for Stage 1

In scope (business framing only):

- Framing the evidence-reconciliation problem for Workflows A, B and C.
- Identifying affected roles, outcomes, non-negotiables, gaps and exceptions.
- Preserving human accountability and the read-only advisory boundary.

Out of scope for Stage 1:

- Solving the case, approving release, dispositioning safety cases, allocating stock or initiating recalls.
- Domain/subdomain maps (Stage 2), ubiquitous language (Stage 3), bounded contexts (later stages).
- Any architecture, GenAI, RAG, MCP, agent or technical implementation decision.

## 9. Non-Negotiables and Safety Boundaries

- The AI never releases, rejects, reprocesses, re-labels or recalls a batch.
- The AI never makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions.
- The AI never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval.
- The AI never changes formulation, specification, clinical eligibility, safety-case disposition, batch release or recall decisions.
- Regulated accountability remains with the accountable Quality, Safety, Regulatory, Clinical and Supply roles.
- Evidence output must not be produced while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
- Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable.
- The system operates read-only and advisory; it prepares, reconciles, explains and packages evidence.

## 10. Known Gaps and Exceptions

- Authority hierarchy inconsistent across systems; no universal authority; later timestamps not automatically more authoritative than approved signed records.
- Genealogy incomplete for batch NCB204-B24071 (missing single-use assembly lot SUA-88 branch).
- Unapproved unit convention (mg/L vs µg/mL) for contract-laboratory concentration.
- Disputed OOS/OOT state with an open investigation across LIMS, statistical tooling and laboratory notebook.
- Supplier-audit commitment claimed closed but not independently verified in the EU release packet.
- Batch-record step back-entered after network degradation; audit capture disabled for 47 minutes.
- Disputed PV awareness date; duplicate ICSR candidates under alternative product names; MedDRA version mismatch; listedness-source conflict.
- Cold-chain logger clocks and pallet association disputed; serialisation aggregation missing after a line restart.
- Sole-source excipient shortage with eight-week recovery estimate; CMO capacity conflict; demand exceeds available stock.
- Validation-state ambiguity across inventories; unapproved macro-enabled spreadsheet in use.
- Untrusted documents and manifests (prompt-injection PDF, stale/unsigned tool manifests, shared-account spreadsheets).
- Deliberate stakeholder conflicts: Quality vs Manufacturing on speed vs completeness; global standardisation vs jurisdictional variation; privacy minimisation vs defensible preservation; bundled vendor vs substitutability; automation vs prespecified, explainable transformations.

## 11. Open Questions for Stage 2

- What is the main business domain represented by this problem?
- Which business areas are core to evidence-complete, fail-closed batch, safety and supply review work?
- Which business areas support the core advisory workflows?
- Which reusable organizational capabilities are needed across many regulated workflows?
- Which business areas own genealogy, unit/terminology, authority, PV case handling, allocation recommendation, and audit evidence?
- Which exception types need explicit ownership in later stages?
- Which business terms need precise definition before modelling continues?

## 12. STAGE_2_INPUT_BLOCK

> **Business problem statement.** NovaCura Therapeutics Group cannot reliably and quickly assemble evidence-complete, conflict-visible, provenance-backed, authority-respected material for regulated batch-review, pharmacovigilance and supply-recovery decisions, because its enterprise systems fragment identifiers, timestamps, terminology, access controls and authority hierarchies.
>
> **Mandatory workflows.** Workflow A — GxP evidence reconciliation for batch-review readiness (never releases, rejects, reprocesses, re-labels or recalls). Workflow B — PV case-intake and signal-support (never makes final seriousness, causality, expectedness, reportability or signal-confirmation decisions). Workflow C — bounded supply-shortage and cold-chain recovery planner (never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval).
>
> **Affected roles/functions.** CQO and quality system; EU Qualified Person; batch-review coordination; Manufacturing and sterile-fill; Laboratory and OOS owners; Global Head of PV and case intake; PV medical reviewers and signal management; Clinical Operations; Regulatory Affairs; Supply Chain planning; logistics, serialisation and cold-chain; CMOs and supplier quality; Procurement; Data Protection; CISO/cyber; Biostatistics; patient-safety voice.
>
> **Desired outcomes.** Evidence-complete, conflict-visible, provenance-backed, authority-respected, fail-closed, human-owned, auditable, defensible review work across Workflows A, B and C; 14% release lead-time reduction without changing registered specifications or weakening independent Quality authority.
>
> **Non-negotiables.** See Section 9 (AI never releases/rejects/reprocesses/re-labels/recalls a batch; never makes final PV decisions; never changes inventory status, reserves capacity, allocates stock, ships or initiates recall without explicit authorised human approval; never changes formulation, specification, clinical eligibility, safety-case disposition, batch-release or recall decisions; regulated accountability stays human; no evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved; everything auditable; read-only and advisory).
>
> **Known gaps/exceptions.** Authority hierarchy inconsistent; incomplete genealogy for NCB204-B24071 (SUA-88); unapproved mg/L vs µg/mL unit assumption; disputed OOS/OOT state with open investigation; unverified supplier-audit commitment; disputed PV awareness date, duplicate ICSR candidates, MedDRA version mismatch, listedness-source conflict; disputed cold-chain logger clocks and pallet association; missing serialisation aggregation; excipient shortage with eight-week recovery, CMO capacity conflict and constrained allocation; validation-state ambiguity; 47-minute audit-capture gap; untrusted supplier deviation PDF and tool manifests; deliberate stakeholder conflicts.
>
> **Open questions for domain and subdomain discovery.** What is the main business domain? Which business areas are core to safe evidence-complete, fail-closed review work? Which are supporting? Which reusable capabilities are needed across regulated workflows? Which business areas own genealogy, unit/terminology, authority, PV case handling, allocation recommendation and audit evidence? Which exception types need explicit ownership? Which business terms need precise definition?

> "Stage 1 complete. Use the STAGE_2_INPUT_BLOCK as the main input for Stage 2."
