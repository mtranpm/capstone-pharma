# A0 — Context Pack: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

This pack is the Stage 0 output. It is intentionally limited to business-domain context. It does not solve the case, does not provide medical, regulatory or legal advice, does not resolve any product, batch, compound, safety, quality or supply conflict, and does not introduce architecture or technical implementation. GenAI, RAG, MCP and agent design enter only at the documented stages.

---

## 1. Workshop Mission

Project AEGIS-PHARMA challenges participants to design and defend an AI Forward Deployed Engineering intervention that reduces evidence-reconciliation time across development, quality, safety and supply operations at NovaCura Therapeutics Group, operating within a fragmented brownfield estate, without taking over regulated human accountability. Participants may conclude that a workflow, knowledge-graph or AI component is unjustified, but must prove that decision with evidence.

The intervention is confined to three mandatory advisory workflows:

- **Workflow A — GxP evidence reconciliation for batch-review readiness:** reconcile batch genealogy, laboratory results, environmental monitoring, deviations, CAPA, change control, validation state, supplier evidence and release-packet completeness. It may identify gaps, contradictions and evidence lineage. It must never release, reject, reprocess, re-label or recall a batch.
- **Workflow B — Pharmacovigilance case-intake and signal-support:** support intake, duplicate detection, terminology normalisation, source authority, reporting-clock reconstruction, listedness evidence, product-quality linkage and multilingual review. It must never make final seriousness, causality, expectedness, reportability or signal-confirmation decisions.
- **Workflow C — Bounded supply-shortage and cold-chain recovery planner:** generate traceable options using inventory, quality status, market authorisation, trial demand, compassionate-use constraints, cold-chain evidence, CMO capacity, transport and allocation policy. It must never change inventory status, reserve capacity, allocate stock, release product or initiate a recall without explicit authorised human approval.

## 2. Organization Snapshot

**NovaCura Therapeutics Group (NTG)** is a fictional global pharmaceutical company operating discovery laboratories, clinical-development programmes, pharmacovigilance hubs, manufacturing plants, quality laboratories and distribution networks across India, Germany, Ireland, the United States, the UAE and Singapore.

Portfolio:

- NCX-101 — oral small-molecule oncology product approaching patent expiry.
- NCB-204 — monoclonal-antibody biologic in pivotal trials and commercial scale-up.
- NCS-310 — sterile injectable supplied through hospital and compassionate-use channels.
- NCR-415 — rare-disease gene-therapy research programme acquired with a biotech subsidiary.

Enterprise estate (source-system fact pack): discovery (ELN, assay platform, image repository, compound registry); clinical (EDC, CTMS, eConsent, IRT, ePRO, wearable hub, imaging core lab); manufacturing (ERP, MES, eBR, historian, PAT, warehouse system); laboratory (LIMS, CDS, instrument PCs, notebooks, spreadsheets); quality (eQMS, document management, training, supplier quality); safety (global safety DB, affiliate inboxes, vendors, literature, call centre); regulatory (RIM, eCTD archive, labeling, IDMP/SPOR staging); supply (serialisation, logistics, cold-chain, CMO portals); and an AI platform layer (gateway, model endpoints, vector store, tools, evaluator). No system is universally authoritative; authority is contextual and must be defined by business object, jurisdiction, effective time, process state and accountable role.

Key stakeholder mandates (stakeholder pack): the Chief Quality Officer owns inspection readiness and product quality; the EU Qualified Person owns final batch certification with complete, reliable release evidence; the Global Head of Pharmacovigilance owns safety-system performance with timely, complete, consistent case handling; the Regulatory Affairs VP owns registrations and submissions; the Supply Chain VP owns service continuity and shortage avoidance; the CISO owns cyber and resilience; the Data Protection Officer owns lawful data processing; the Chief Medical Officer owns benefit-risk and clinical strategy. Deliberate stakeholder conflicts exist (see Section 8).

## 3. Business Problem

NTG is fragmented across LIMS, MES, electronic batch records, QMS, RIM, EDC, eConsent, IRT, CTMS, safety databases, serialisation platforms, data lakes, spreadsheets, vendor portals and research environments. Identifiers, timestamps, terminology, access controls and authority hierarchies are inconsistent, so evidence needed for batch review, safety case handling and supply decisions is slow to reconcile, conflict-prone and hard to defend under inspection.

During the capstone window, converging events test every workflow: a pivotal-trial amendment, a disputed biologics batch, emerging safety reports, a sterile-area excursion, a cold-chain failure, an excipient shortage, a ransomware event and a multi-agency inspection request.

## 4. Business Goals

NTG wants a redesigned evidence-reconciliation capability so that batch, safety and supply review work is:

- Evidence-complete.
- Conflict-visible.
- Provenance-backed.
- Authority-respected (no single system assumed authoritative).
- Fail-closed on uncertainty.
- Owned by the right accountable human roles.
- Auditable and defensible.

The board requires a 14% reduction in end-to-end release lead time without changing registered specifications or weakening independent Quality authority.

## 5. Non-Negotiables

- The AI never releases, rejects, reprocesses, re-labels or recalls a batch.
- The AI never makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions.
- The AI never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval.
- The AI never changes formulation, specification, clinical eligibility, safety-case disposition, batch release or recall decisions.
- Regulated accountability remains with the accountable Quality, Safety, Regulatory, Clinical and Supply roles.
- Evidence output must not be produced while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
- Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable.
- The system operates read-only and advisory; it prepares, reconciles, explains and packages evidence.

## 6. Representative Scenario Summary

- **Pivotal-trial amendment (Workflows A and B context):** sites are executing multiple protocol versions and one country has not approved the latest amendment; protocol, consent and data-collection versions are asynchronous; clocks differ across decentralised devices.
- **Disputed biologics batch NCB204-B24071 (Workflow A):** a single-use assembly lot (SUA-88) is missing from one MES genealogy branch but appears in warehouse consumption; a contract laboratory concentration is transmitted in mg/L while the receiving interface assumes µg/mL; LIMS marks an assay OOS while the statistical tool marks it OOT and the laboratory notebook labels it invalid; the EU release packet lacks confirmation of one contract-site audit commitment; a required batch-record step was back-entered after network degradation.
- **Sterile-area excursion (Workflow A):** environmental monitoring shows an excursion near fill-finish and the organism identification was corrected after initial review; campaign sequencing changed after a high-potency product was introduced.
- **Emerging safety reports (Workflow B):** cases from a patient programme, literature vendor and call centre likely describe the same event under different product names; the awareness date differs across vendor receipt, affiliate inbox and global safety database; coding used two MedDRA versions changing the preferred term; the investigator brochure, core data sheet and local label are not aligned on expectedness.
- **Cold-chain failure (Workflow C):** a biologic shipment exceeds range and logger clocks and pallet association are disputed; case-to-pallet aggregation is missing after a line restart.
- **Excipient shortage (Workflow C):** a sole-source excipient supplier reports contamination with an eight-week recovery estimate; a CMO promises capacity to two sponsors in the same window; demand exceeds available stock across markets, trials and compassionate-use programmes.
- **Ransomware event (all workflows):** manufacturing historians are isolated while MES and QMS operate in degraded mode; audit capture was disabled for 47 minutes during master-data repair; the organisation must be able to operate safely without AI inference.
- **Multi-agency inspection request (all workflows):** regulators request traceable evidence spanning trial data, batch history, safety cases and AI-system controls within 72 hours.

## 7. Synthetic Evidence Inventory

The 84 disclosed challenge conditions (INJ-001 to INJ-084) are catalogued across 13 dimensions (D01–D13): portfolio and strategy; discovery and model risk; clinical development and trial integrity; GMP manufacturing, laboratories and batch release; quality systems, validation and data integrity; pharmacovigilance and benefit-risk; regulatory information and submissions; supply chain, serialisation and anti-counterfeit; privacy, ethics and cross-border data; cybersecurity, agentic security and Zero Trust; human factors, responsible AI and adoption; economics, token efficiency and vendor concentration; reliability, business continuity and retirement.

Machine-readable evidence inventory (authoritative reference):

- `data/inject_evidence_map.csv` — maps each inject to evidence files and expected challenge conditions.
- `data/injects.json` — structured inject catalogue (84 injects, D01–D13).
- `data/DATA_DICTIONARY.csv` — data dictionary for all supplied datasets.
- `data/DATASET_PROFILE.csv` — dataset-level profiles (rows, columns, quality signals).
- `data/INJECT_TEST_COVERAGE.csv` — evaluates which injects are covered by public fixtures.
- `data/RELATIONSHIP_MODEL.csv` — entity-relationship model for key objects and foreign keys.

Representative evidence sources per workflow:

- Workflow A: batches, material_genealogy, warehouse_movements, ebr_steps, lab_results, interface_mappings, oos_investigations, environmental_monitoring, microbiology_results, cleaning_validation, production_schedule, deviations, capa_records, change_controls, release_packets, supplier_audits, certificates_analysis, downtime_events.
- Workflow B: icsr_cases, duplicate_candidates, safety_receipts, adverse_events, terminology_versions, listedness_sources, product_labels, sensitive_segments, social_listening, product_complaints, signal_metrics, exposure_estimates.
- Workflow C: inventory, demand_forecast, allocation_constraints, shipments, temperature_loggers, serialisation_events, packaging_events, returns, supplier_risks, cmo_capacity, vendor_contracts, trade_documents, recall_candidates.
- Cross-cutting: users_entitlements, access_logs, audit_trails, privileged_sessions, system_inventory, validation_inventory, spreadsheet_inventory, tool_catalog, model_registry, model_artifacts, model_costs, model_usage, vendor_dependencies, downtime_events, network_zones, continuity_requirements, retention_rules, legal_holds, deletion_requests, knowledge_catalog, security_events.

Known untrusted data that must be treated as untrusted until governance review: a supplier-PDF-derived document containing hidden prompt-injection text (`MALICIOUS_SUPPLIER_DEVIATION.md`), tool manifests with stale entitlements and unsigned tool definitions, and vendor portals and spreadsheets with undocumented fields and shared accounts.

## 8. Known Gaps and Exceptions

These are workflow and domain gaps only. They are identified, not resolved. Resolution decisions remain with accountable human roles in later stages.

- Authority and hierarchy are inconsistent across systems; no system is universally authoritative and a later timestamp is not automatically more authoritative than an approved signed record.
- Genealogy is incomplete for batch NCB204-B24071 (missing single-use assembly lot SUA-88 branch).
- Unit convention for contract-laboratory concentration (mg/L vs µg/mL) is unapproved and inconsistent.
- OOS/OOT state for an assay is disputed across LIMS, statistical tooling and the laboratory notebook, with an open investigation.
- A supplier-audit commitment is claimed closed but not independently verified in the release packet.
- Reporting-clock reconstruction is disputed for an ICSR awareness date; duplicate ICSR candidates exist under alternative product names; MedDRA version mismatch and listedness-source conflict are unresolved.
- Cold-chain logger clocks and pallet association are disputed; serialisation aggregation is missing after a line restart.
- Sole-source excipient shortage with an eight-week recovery estimate, CMO capacity conflict and competing demand beyond available stock are unresolved.
- Validation state is ambiguous for at least one application (validated vs conditionally released vs research-only across inventories); an unapproved macro-enabled spreadsheet is in use; audit capture was disabled for 47 minutes.
- Deliberate stakeholder conflicts: Quality vs Manufacturing on speed vs evidence completeness; global standardisation vs jurisdictional variation; privacy minimisation vs defensible preservation; bundled vendor vs substitutability; automation vs prespecified, explainable transformations.
- Untrusted documents and manifests (prompt-injection PDF, stale/unsigned tool manifests, undocumented shared-account spreadsheets) must be governed before use.

## 9. Workshop Guardrails

- Business-only at this stage. No architecture, no GenAI, RAG, MCP or agent design yet; those enter only at documented stages.
- Use only the supplied case and synthetic evidence. Do not invent new product, batch, clinical, safety, quality or supply facts or records.
- Do not solve the case, approve release, disposition safety cases, allocate stock or initiate recalls at any stage.
- Do not provide medical, regulatory or legal advice.
- Do not resolve identity, genealogy, unit, terminology, authority, consent, validation or evidence conflicts; only identify them as workflow and domain gaps.
- Preserve all non-negotiables in Section 5 in every later stage and artifact.
- All 84 injects are disclosed; there are no later hidden instructor injects. Participants must discover connections, contradictions and failure chains from the supplied evidence.
- Preserve human accountability for regulated decisions and require explicit authorised human approval for any regulated execution action.

## 10. NEXT_STAGE_INPUT_BLOCK

> **Final business challenge.** NovaCura Therapeutics Group needs a redesigned evidence-reconciliation capability so that batch-review, pharmacovigilance and supply-recovery work is evidence-complete, conflict-visible, provenance-backed, authority-respected, fail-closed on uncertainty, owned by the right accountable human roles, auditable and defensible — reducing evidence-reconciliation time (board target: 14% end-to-end release lead-time reduction) without changing registered specifications, weakening independent Quality authority, or taking over regulated human accountability.
>
> **Mandatory workflows.** Workflow A — GxP evidence reconciliation for batch-review readiness (never releases, rejects, reprocesses, re-labels or recalls). Workflow B — PV case-intake and signal-support (never makes final seriousness, causality, expectedness, reportability or signal-confirmation decisions). Workflow C — bounded supply-shortage and cold-chain recovery planner (never changes inventory status, reserves capacity, allocates stock, releases product or initiates a recall without explicit authorised human approval).
>
> **Affected stakeholders and functions.** Quality (CQO, EU Qualified Person), Manufacturing, Laboratory, Pharmacovigilance and Safety, Clinical Operations, Regulatory Affairs, Supply Chain, Procurement, Privacy/Data Protection, Cybersecurity, Biostatistics, Patient Safety voice, Site Investigator Council, Works Council / Employee Forum.
>
> **Business goals.** Evidence-complete, conflict-visible, provenance-backed, authority-respected, fail-closed, human-owned, auditable, defensible; 14% release lead-time reduction without changing registered specifications or weakening Quality authority.
>
> **Non-negotiables.** See Section 5 (AI never releases/rejects/reprocesses/re-labels/recalls; never makes final PV decisions; never changes inventory status, reserves capacity, allocates stock, ships or initiates recall without explicit authorised human approval; never changes formulation, specification, clinical eligibility, safety-case disposition, batch-release or recall decisions; regulated accountability stays human; no evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved; everything auditable; read-only and advisory).
>
> **Available evidence.** Organization profile; business problem and goal statements; non-negotiables; stakeholder pack; source-system fact pack; regulatory and standards boundary pack; integrated case with inject catalogue (INJ-001 to INJ-084 across D01–D13); synthetic evidence inventory (`data/inject_evidence_map.csv`, `data/injects.json`, `data/DATA_DICTIONARY.csv`, `data/DATASET_PROFILE.csv`, `data/INJECT_TEST_COVERAGE.csv`, `data/RELATIONSHIP_MODEL.csv`); representative datasets per workflow; known untrusted documents.
>
> **Known gaps and exceptions (unresolved).** Authority hierarchy inconsistent; incomplete genealogy for NCB204-B24071 (SUA-88); unapproved mg/L vs µg/mL unit assumption; disputed OOS/OOT state with open investigation; unverified supplier-audit commitment; disputed PV awareness date, duplicate ICSR candidates, MedDRA version mismatch, listedness-source conflict; disputed cold-chain logger clocks and pallet association; missing serialisation aggregation; excipient shortage with eight-week recovery, CMO capacity conflict and constrained allocation; validation-state ambiguity; 47-minute audit-capture gap; untrusted supplier deviation PDF and tool manifests; deliberate stakeholder conflicts (speed vs completeness, standardisation vs jurisdictional variation, minimisation vs preservation, bundled vendor vs substitutability, automation vs prespecified analysis).
>
> **Open questions for Stage 1.** Which business area owns batch-review readiness closure? Which roles own PV case-intake completeness and reporting-clock reconstruction? Which roles own supply-recovery option selection and any allocation recommendation? What is the escalation path when evidence is incomplete or conflicting? How are authority and effective date determined per business object and jurisdiction? How is regulated human accountability preserved in every workflow while AI remains advisory? What evidence must exist before any recommendation or draft is produced, and what must be documented for any human override?

> "Stage 0 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 1."
