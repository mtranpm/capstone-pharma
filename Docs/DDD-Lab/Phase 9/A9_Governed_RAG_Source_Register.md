# A9 — Governed RAG Source Register: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## 1. Stage 9 Purpose

Stage 9 creates a governed source and evidence register for the NovaCura Therapeutics Group pharmaceutical evidence-reconciliation case. The purpose is to identify which batch and product-specific evidence, quality and supplier evidence, PV and safety evidence, supply and cold-chain evidence, regulatory evidence, policy/SOP/standard sources, governance constraints, AI-platform control evidence, and prior-stage artifacts may support the next stage of work, and which sources must be treated as untrusted or missing. This artifact does not resolve any batch, safety, quality or supply issue, does not approve batch release, rejection, reprocess, re-label or recall, does not make final PV decisions, does not allocate stock, does not create architecture, and does not design implementation. It defines what sources must be trusted, owned, versioned, access-controlled, consent-checked where relevant, approved for regulated or patient-facing output where relevant, and auditable.

---

## 2. Source Governance Boundary

This artifact governs:

```text
authoritative source identification
batch and product-specific evidence classification
quality and supplier evidence classification
PV and safety evidence classification
supply and cold-chain evidence classification
regulatory evidence classification
policy, SOP and standard source classification
governance / non-negotiable source classification
AI-platform control evidence classification
untrusted-source identification and quarantine
source ownership to confirm
regulated-output and patient/participant-facing source suitability
source metadata requirements
rule-to-source traceability
evidence gaps
source access boundaries
no-answer / no-output conditions
audit obligations
```

This artifact must not:

```text
resolve the NCB204-B24071 genealogy, unit, OOS/OOT or supplier-audit gap
resolve the PV awareness-date, duplicate, MedDRA-version or listedness conflict
resolve the cold-chain logger, pallet or aggregation dispute
resolve the excipient shortage, CMO capacity conflict or allocation question
resolve validation-state ambiguity or the 47-minute audit-capture gap
approve batch release, rejection, reprocess, re-label or recall
perform or imply QP certification
make final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions
change inventory status, reserve capacity, allocate stock, ship product or initiate a recall
override consent, entitlement or privacy boundaries
invent missing policy content
invent product, batch, safety, quality, regulatory, clinical or supply facts
create architecture
create implementation design
replace accountable Quality, Safety, Regulatory, Clinical or Supply roles
```

---

## 3. Source Classification Model

| Source Category | Meaning | Example From Case | Key Governance Concern |
|---|---|---|---|
| Batch and product-specific evidence | Evidence tied to a product, batch, material or compound identity, genealogy and lineage | Product/batch master, MES genealogy, warehouse consumption, eBR steps, lab results, environmental monitoring | Identity and genealogy must be resolved or the gap kept visible before batch evidence output; no silent unit conversion or lineage repair |
| Quality and supplier evidence | Evidence about deviations, CAPA, change control, cleaning validation, supplier audits, certificates and release packets | Deviations, CAPA, change controls, supplier audits, certificates of analysis, EU release packet | An unverified supplier-audit commitment is not closed; release-packet elements must be complete or gaps visible |
| PV and safety evidence | Evidence about ICSRs, duplicate candidates, safety receipts, terminology, listedness, labels, complaints and signal metrics | ICSR cluster, safety receipts, MedDRA versions, IB/CCDS/local labels, product complaints | Duplicate detection is candidate-only; clock reconstruction is evidence, not a decision; terminology and listedness conflicts remain visible |
| Supply and cold-chain evidence | Evidence about inventory, allocation constraints, shipments, loggers, serialisation, CMO capacity and supplier risk | Inventory, temperature loggers, serialisation events, CMO capacity, excipient supplier risk | Cold-chain evidence must be resolved before options are trusted; options only, no allocation/reservation/shipment without authorised human approval |
| Regulatory evidence | Evidence about market authorisations, IDMP mappings, labels, commitments, changes and inspections | Market authorisations, IDMP mappings, regulatory commitments, inspection requests | Authority is per object, jurisdiction and effective date; a later timestamp is not automatically more authoritative |
| Policy / SOP / standard source | Approved operating, quality, safety, regulatory or supply guidance | `knowledge/` policy documents (e.g., BATCH_RELEASE_EVIDENCE_POLICY, PV_LISTEDNESS_AUTHORITY, SUPPLY_ALLOCATION_ETHICS) | Must be approved, current, applicable, versioned and role-appropriate; old, fake or untrusted documents must not be used |
| Governance / non-negotiable source | Hard safety and accountability constraints | A0 context pack, Stage 8 rules, human-owned decisions and gates, inject evidence map | Must override convenience, automation or workflow speed; non-negotiables carry forward verbatim |
| AI-platform control evidence | Evidence about tools, manifests, models, entitlements, access and audit capture | Tool catalog, model registry, users/entitlements, access logs, audit trails | Tool manifests may be poisoned or stale; audit-capture gaps must remain visible; needed for AI-system-control inspection evidence |
| Untrusted source | Data that must be quarantined until governance review | MALICIOUS_SUPPLIER_DEVIATION.md, tool_manifest_poisoned.json, vendor portals, shared-account spreadsheets | Must never be treated as authoritative; prompt-injection and unsigned-definition risk |
| Missing or required source | A source needed for governed use but not fully available in the Stage 8 handoff | Full allocation policy, full consent/entitlement policy, independent supplier-audit verification records | Must be identified as a gap; content must not be invented |

---

## 4. Governed Source Register

| Source ID | Source / Evidence Item | Source Category | Business Use | Relevant Rule / Decision / Gate | Likely Accountable Owner to Confirm | Regulated-Output / Patient-Facing Use Status | Required Metadata | Audit Requirement | Risk If Misused |
|---|---|---|---|---|---|---|---|---|---|
| SRC-001 | Product / medicinal product master (`data/medicinal_products.csv`, `data/substance_master.csv`, `data/compounds.csv`) | Batch and product-specific evidence | Establish product, substance and compound identity for batch, PV and supply evidence | R-01, R-05 (identity / product-code match) | Identity / genealogy / master-data owner; Regulatory Affairs (IDMP) | Internal; never patient-facing by itself | Product ID, name, substance, batch scope, source, status, effective date | Record source use, match check, reviewer | Wrong product identity or an unapproved alias treated as authoritative |
| SRC-002 | Batch records (`data/batches.csv`) | Batch and product-specific evidence | Identify batch, product, dates, state and campaign context | R-01; batch-release gates | Manufacturing / Quality release reviewer | Internal | Batch ID, product ID, state, dates, source | Record use in batch-review readiness | Treating a later timestamp as automatically more authoritative |
| SRC-003 | MES genealogy (`data/material_genealogy.csv`) | Batch and product-specific evidence | Reconcile batch lineage; surface the SUA-88 missing branch | R-02 genealogy completeness; genealogy escalation gate | Identity / genealogy / master-data owner | Internal | Batch ID, material lot, relation, source | Genealogy-break identification, source records | Silently repairing the SUA-88 break or claiming completeness |
| SRC-004 | Warehouse consumption / movements (`data/warehouse_movements.csv`) | Batch and product-specific evidence | Show SUA-88 consumption evidence counter to the MES branch | R-02; genealogy escalation gate | Warehouse / master-data owner | Internal | Batch ID, material lot, movement, time, source | Consumption evidence, discrepancy record | Resolving the genealogy conflict without an accountable owner |
| SRC-005 | Electronic batch record steps (`data/ebr_steps.csv`) | Batch and product-specific evidence | Review batch-record step state and back-entered steps | R-08 back-entered step checkpoint | Manufacturing / Quality reviewer | Internal | Batch ID, step, checkpoint state, timestamp, source | Detection record, timestamps, checkpoint state | Treating a back-entered step as normal without checkpoint evidence |
| SRC-006 | Laboratory results (`data/lab_results.csv`) | Batch and product-specific evidence | Show assay values, units and spec status | R-04 unit conversion; R-06 OOS/OOT state | Laboratory analyst / OOS owner | Internal | Result ID, batch ID, test, value, unit, spec, status | Value/unit used, conflict visibility | Silent mg/L vs µg/mL conversion or hiding the OOS state |
| SRC-007 | Interface mappings (`data/interface_mappings.csv`) | Batch and product-specific evidence | Show the receiving-interface assumed unit | R-04 unit-conversion consistency | Laboratory / interface owner with Quality acceptance | Internal | Interface, field, assumed unit, source, state | Conversion mapping, approval/override record | Treating the mg/L vs µg/mL assumption as approved |
| SRC-008 | OOS investigations (`data/oos_investigations.csv`) | Batch and product-specific evidence | Show OOS/OOT/notebook-invalid conflict and open investigation | R-06 disputed result state open and visible | Laboratory analyst / OOS owner | Internal | Result ID, state, investigation status, owner | Conflicting states, investigation record | Dispositioning the assay automatically |
| SRC-009 | Environmental monitoring (`data/environmental_monitoring.csv`) | Batch and product-specific evidence | Show sterile-area excursion near fill-finish | Sterile-area excursion disposition gate | Quality / Manufacturing owner | Internal | Monitoring point, date, value, excursion state, source | Excursion record, correction rationale | Hiding or dismissing the excursion |
| SRC-010 | Microbiology results (`data/microbiology_results.csv`) | Batch and product-specific evidence | Show organism identification and its correction after initial review | Excursion disposition; checkpoint state | Laboratory / Quality owner | Internal | Sample ID, organism, identification state, correction, source | Organism-correction evidence | Treating the corrected identification as final without review |
| SRC-011 | Deviations (`data/deviations.csv`) | Quality and supplier evidence | Link deviations to batch, process and campaign context | Deviation lineage gate | Quality / Manufacturing owner | Internal | Deviation ID, batch, state, owner, source | Lineage links, state | Treating deviation lineage as resolved without evidence |
| SRC-012 | CAPA records (`data/capa_records.csv`) | Quality and supplier evidence | Link CAPA effectiveness to deviations and excursions | CAPA effectiveness gate | Quality owner | Internal | CAPA ID, linked record, state, effectiveness, owner | CAPA closure, effectiveness state | Claiming CAPA effectiveness without evidence |
| SRC-013 | Change controls (`data/change_controls.csv`) | Quality and supplier evidence | Track change-control state including campaign sequencing | Change-control lineage gate | Quality owner | Internal | Change-control ID, state, scope, owner | Change-control state | Treating change as approved without change-control state |
| SRC-014 | Cleaning validation (`data/cleaning_validation.csv`) | Quality and supplier evidence | Show cleaning-validation boundary for high-potency product changeover | Validation-state gate | Validation / Quality owner | Internal | Equipment, campaign, validation state, owner | Validation-state evidence | Treating cleaning as validated beyond its boundary |
| SRC-015 | Production schedule (`data/production_schedule.csv`) | Quality and supplier evidence | Show campaign sequencing change after high-potency introduction | Change-control / excursion context | Manufacturing / planning owner | Internal | Campaign, product, dates, change state, source | Schedule references | Ignoring campaign-sequencing impact on excursion context |
| SRC-016 | Supplier audits (`data/supplier_audits.csv`) | Quality and supplier evidence | Show contract-site audit state and the unverified commitment | R-07 unverified commitment not closed; supplier-audit escalation gate | Supplier-quality / Quality reviewer | Internal | Audit ID, site, commitment, verification state, owner | Verification request, verification state | Treating the claimed-closed audit commitment as verified |
| SRC-017 | Certificates of analysis (`data/certificates_analysis.csv`) | Quality and supplier evidence | Show CoA provenance and ALCOA+ chain | R-09 validation state; provenance gate | Supplier-quality / Quality owner | Internal | CoA ID, lot, values, source, lineage | Provenance chain | Treating a broken CoA provenance chain as complete |
| SRC-018 | Release packets (`data/release_packets.csv`) | Quality and supplier evidence | Show EU release-packet element completeness | R-12 release-packet completeness; QP certification evidence package | Quality release reviewer | Internal (QP/regulator-facing only when packaged by humans) | Batch ID, packet elements, completeness state, gaps, owner | Packet status, element checklist, gap ownership | Showing a batch as release-ready with unresolved packet elements |
| SRC-019 | ICSR cases (`data/icsr_cases.csv`) | PV and safety evidence | Identify cases, products, events, countries and awareness dates | R-14 duplicate candidates; R-15 clock inputs; PV intake | Global Head of Pharmacovigilance / PV case-intake staff | Internal; never patient-facing | Case ID, source, product, event, country, awareness date, language, patient key | Case-intake evidence, receipt basis | Treating a duplicate cluster as separate new events |
| SRC-020 | Duplicate candidates (`data/duplicate_candidates.csv`) | PV and safety evidence | Surface duplicate-ICSR candidates under different product names | R-14 candidate-only duplicate detection | PV case-intake staff / PV reviewer | Internal | Case IDs, similarity rationale, product-name evidence, state | Duplicate rationale, candidates, reviewer routing | Confirming or merging duplicates automatically |
| SRC-021 | Safety receipts (`data/safety_receipts.csv`) | PV and safety evidence | Show vendor receipt, affiliate inbox and global safety DB awareness inputs | R-15 reporting-clock reconstruction | PV case-intake staff / PV reviewer | Internal | Case ID, receipt source, receipt time, state | Clock-reconstruction evidence, source basis | Setting the reporting clock automatically |
| SRC-022 | Adverse events / terminology versions (`data/adverse_events.csv`, `data/terminology_versions.csv`) | PV and safety evidence | Show MedDRA version basis and preferred-term changes | R-13 MedDRA version consistency | Safety coder / terminology owner | Internal | Event ID, term, MedDRA version, preferred term, source | Version-alignment evidence, source | Choosing a preferred term under a mismatched MedDRA version |
| SRC-023 | Listedness sources (`data/listedness_sources.csv`) | PV and safety evidence | Show IB, core data sheet and local label listedness basis | D-10 listedness determination per jurisdiction | PV medical reviewer / Regulatory Affairs | Internal for reviewers; not patient-facing | Source type, jurisdiction, version, effective date, state | Listedness-source versions, determination record | Picking a listedness winner automatically |
| SRC-024 | Product labels (`data/product_labels.csv`) | PV and safety evidence | Show approved label content per jurisdiction | Listedness/expectedness context; regulated-output source control | Regulatory Affairs (labelling) / PV medical reviewer | Approved labels are the regulated patient/HCP-facing source; output must cite version | Label ID, product, jurisdiction, version, status, effective date | Label version used, citation | Using an unapproved or superseded label for listedness |
| SRC-025 | Sensitive segments (`data/sensitive_segments.csv`) | PV and safety evidence | Identify pregnancy/paediatric and other sensitive case content | R-10 entitlement/consent gate; privacy boundary | Data Protection Officer / PV intake | Internal; patient data access restricted | Case ID, sensitive segment, access rule, consent/entitlement status | Consent/entitlement check, access/use record | Surfacing sensitive patient data without lawful basis |
| SRC-026 | Product complaints (`data/product_complaints.csv`) | PV and safety evidence | Link product-quality complaints to cases and batches | Product-quality linkage gate | PV / Quality owner | Internal | Complaint ID, product, batch, link state, owner | Complaint records, linkage | Treating linkage as disposition |
| SRC-027 | Signal metrics / exposure estimates (`data/signal_metrics.csv`, `data/exposure_estimates.csv`) | PV and safety evidence | Support signal-review material without confirming signals | D-11 signal confirmation | Signal management / biostatistics | Internal | Metric, period, exposure basis, source | Signal-review material, basis | Confirming a signal automatically |
| SRC-028 | Inventory (`data/inventory.csv`, `data/backup_inventory.csv`) | Supply and cold-chain evidence | Show product, market, quality status and units on hand | D-12 allocation decision; R-11 checkpoint state | Supply Chain planner / authorised Quality owner | Internal | Product, market, quality status, units, source | Inventory state used, basis | Changing inventory status or allocating stock without approval |
| SRC-029 | Demand forecast (`data/demand_forecast.csv`) | Supply and cold-chain evidence | Show market, trial and compassionate-use demand | D-12 allocation; shortage options | Supply Chain planner | Internal | Product, market, forecast period, demand, source | Demand basis for options | Ignoring compassionate-use or trial demand in options |
| SRC-030 | Allocation constraints (`data/allocation_constraints.csv`) | Supply and cold-chain evidence | Show allocation policy constraints and market/trial bounds | D-12 allocation; R-11 checkpoint state | Supply Chain VP / authorised Quality owner | Internal | Product, constraint, market, policy reference, state | Constraint rationale, policy reference | Generating options that violate allocation constraints |
| SRC-031 | Shipments (`data/shipments.csv`) | Supply and cold-chain evidence | Show shipment, lane and product movement context | Cold-chain excursion context | Logistics / cold-chain owner | Internal | Shipment ID, product, lane, dates, temperature state, source | Shipment evidence | Dispositioning a shipment automatically |
| SRC-032 | Temperature loggers (`data/temperature_loggers.csv`) | Supply and cold-chain evidence | Show logger readings, clocks and pallet association | D-13 cold-chain excursion disposition | Logistics / cold-chain accountable owner with Quality input | Internal | Logger ID, shipment, reading, logger clock, pallet link, state | Logger basis, pallet link | Trusting an excursion disposition with disputed logger clocks |
| SRC-033 | Serialisation events / packaging events (`data/serialisation_events.csv`, `data/packaging_events.csv`) | Supply and cold-chain evidence | Show case-to-pallet aggregation state and line-restart gap | Serialisation aggregation gate | Serialisation owner | Internal | Event ID, case/pallet, aggregation state, line, source | Aggregation-state record, gap ownership | Assuming the aggregation link after line restart |
| SRC-034 | CMO capacity / vendor contracts (`data/cmo_capacity.csv`, `data/vendor_contracts.csv`) | Supply and cold-chain evidence | Show CMO capacity promised to multiple sponsors | D-12 allocation; shortage escalation gate | Procurement / CMO quality | Internal | CMO, capacity, window, contract basis, state | Capacity-conflict evidence, contract basis | Treating promised capacity as reserved |
| SRC-035 | Supplier risks (`data/supplier_risks.csv`) | Supply and cold-chain evidence | Show sole-source excipient contamination and recovery estimate | D-12 allocation; shortage escalation gate | Procurement / Supplier-quality | Internal | Supplier, material, risk, recovery estimate, state | Risk evidence, recovery basis | Treating an eight-week recovery estimate as fixed |
| SRC-036 | Returns / recall candidates (`data/returns.csv`, `data/recall_candidates.csv`) | Supply and cold-chain evidence | Show returns, counterfeit suspicion and recall-scope material | D-14 recall decision | Quality / Regulatory accountable roles | Internal | Return/recall ID, product, batch, scope evidence, state | Recall consideration record, decision, owner | Initiating or scoping a recall automatically |
| SRC-037 | Market authorisations (`data/market_authorisations.csv`) | Regulatory evidence | Show authorised markets, products and conditions | Authority / effective-date / jurisdiction gate | Regulatory Affairs | Internal | Product, market, authorisation state, effective date, source | Authorisation basis | Using a non-authorised market assumption in options |
| SRC-038 | IDMP mappings (`data/idmp_mappings.csv`) | Regulatory evidence | Show substance/product IDMP identity mappings | R-05 identity match; IDMP authority gate | Regulatory Affairs (IDMP) | Internal | Substance, product, mapping, source, state | Mapping evidence | Resolving an IDMP identity conflict automatically |
| SRC-039 | Regulatory commitments / authority correspondence (`data/regulatory_commitments.csv`, `data/authority_correspondence.csv`) | Regulatory evidence | Show commitments and authority correspondence including audit commitments | R-07 supplier-audit commitment; inspection gate | Regulatory Affairs / Supplier-quality | Internal | Commitment ID, authority, deadline, verification state, source | Commitment status, verification record | Treating a commitment as met without verification |
| SRC-040 | Regulatory changes / inspection requests (`data/regulatory_changes.csv`, `data/inspection_requests.csv`) | Regulatory evidence | Show variation state and the 72-hour multi-agency inspection request | Inspection-evidence packaging gate | Regulatory Affairs / Quality | Internal | Change/request ID, authority, deadline, scope, source | Inspection-evidence package manifest | Packaging that creates or hides evidence |
| SRC-041 | Protocol versions / site approvals (`data/protocol_versions.csv`, `data/site_approvals.csv`) | Regulatory evidence | Show pivotal-trial amendment version and country approval state | Authority / effective-date / jurisdiction gate; R-10 eConsent asynchrony | Clinical Operations / Regulatory Affairs | Internal; eConsent version handling governed | Protocol, version, country approval state, effective date, source | Protocol-version basis, consent-version basis | Treating one country's unapproved amendment as approved |
| SRC-042 | `knowledge/BATCH_RELEASE_EVIDENCE_POLICY.md` (K-006) | Policy / SOP / standard source | Define batch release evidence requirements | R-03, R-12 release-readiness rules | Quality policy owner to confirm | Internal; QP/regulator-facing when packaged by humans | Document ID, title, owner, approver, version, effective/review date, allowed roles | Policy section/reference used | Using an old or superseded release policy |
| SRC-043 | `knowledge/GXP_DATA_INTEGRITY_STANDARD.md` (K-014) | Policy / SOP / standard source | Define ALCOA+ and data-integrity expectations | R-08, R-09, R-16 data-integrity gates | Quality / data-integrity owner | Internal | Document metadata, version, effective date, applicability | Data-integrity checks used | Treating a broken data-integrity chain as complete |
| SRC-044 | `knowledge/OOS_OOT_INVESTIGATION.md` (K-018) | Policy / SOP / standard source | Define OOS/OOT investigation expectations | R-06 disputed result state; OOS disposition gate | Laboratory / OOS owner | Internal | Document metadata, version, applicability | Investigation-process references | Dispositioning an open OOS investigation |
| SRC-045 | `knowledge/STERILE_MANUFACTURING_ESCALATION.md` (K-028) | Policy / SOP / standard source | Define sterile-area excursion escalation expectations | Excursion disposition and escalation gates | Quality / Manufacturing owner | Internal | Document metadata, version, effective date | Escalation references | Hiding or downgrading a sterile-area excursion |
| SRC-046 | `knowledge/PHARMACOVIGILANCE_CASE_POLICY.md` (K-019) | Policy / SOP / standard source | Define PV case-intake and handling expectations | Workflow B intake gates | Global Head of Pharmacovigilance | Internal | Document metadata, version, effective date | Intake-policy references | Making final PV decisions under policy cover |
| SRC-047 | `knowledge/PV_DUPLICATE_MANAGEMENT.md` (K-021) | Policy / SOP / standard source | Define duplicate-management expectations | R-14 candidate-only duplicate detection | PV reviewer | Internal | Document metadata, version, effective date | Duplicate-management references | Confirming duplicates automatically |
| SRC-048 | `knowledge/PV_LISTEDNESS_AUTHORITY.md` (K-022) | Policy / SOP / standard source | Define CCDS, IB and local label authority by context | D-10 listedness determination | PV medical reviewer / Regulatory Affairs | Internal | Document metadata, version, effective date, jurisdiction basis | Listedness-authority references | Picking a listedness winner automatically |
| SRC-049 | `knowledge/PV_MULTILINGUAL_REVIEW.md` (K-023) | Policy / SOP / standard source | Define multilingual PV narrative review expectations (Arabic, Hindi, English, German) | Language/translation control; multilingual review gate | PV intake / safety coder | Internal; narratives only through approved review | Document metadata, version, language scope | Language-check references, translation evidence | Releasing unverified translation of a PV narrative |
| SRC-050 | `knowledge/PV_REPORTING_CLOCKS.md` (K-024) | Policy / SOP / standard source | Define source-receipt reconstruction and awareness-date escalation | R-15 reporting-clock reconstruction | PV case-intake staff / PV reviewer | Internal | Document metadata, version, effective date | Clock-reconstruction references | Setting the reporting clock automatically |
| SRC-051 | `knowledge/SERIALISATION_AND_RETURNS.md` (K-027) | Policy / SOP / standard source | Define serialisation aggregation and returns handling | Serialisation aggregation gate; recall consideration | Serialisation / Quality owner | Internal | Document metadata, version, effective date | Aggregation references | Assuming missing case-to-pallet aggregation |
| SRC-052 | `knowledge/COLD_CHAIN_ASSESSMENT.md` (K-009) | Policy / SOP / standard source | Define cold-chain assessment expectations | D-13 cold-chain excursion disposition | Logistics / cold-chain owner with Quality input | Internal | Document metadata, version, effective date | Cold-chain references | Dispositioning an excursion with disputed logger clocks |
| SRC-053 | `knowledge/SUPPLY_ALLOCATION_ETHICS.md` (K-029) | Policy / SOP / standard source | Define documented constraints and governance for shortage allocation | D-12 allocation decision | Supply Chain VP / authorised Quality owner | Internal | Document metadata, version, effective date | Allocation-option references | Generating options that ignore documented constraints |
| SRC-054 | `knowledge/CLINICAL_PROTOCOL_AUTHORITY.md` (K-008) | Policy / SOP / standard source | Define protocol-version authority for the pivotal trial | Authority / effective-date / jurisdiction gate | Clinical Operations / Regulatory Affairs | Internal | Document metadata, version, jurisdiction | Protocol-authority references | Treating the unapproved country amendment as effective |
| SRC-055 | `knowledge/ECONSENT_AND_SECONDARY_USE.md` (K-011) | Policy / SOP / standard source | Define eConsent and secondary-use expectations | R-10 entitlement/consent gate | Data Protection Officer / Clinical | Internal; patient/participant data access governed | Document metadata, version, consent-version basis | Consent/entitlement references | Surfacing participant data under an outdated consent version |
| SRC-056 | `knowledge/PRIVACY_AND_PSEUDONYMISATION.md` (K-020) | Policy / SOP / standard source | Define privacy and pseudonymisation expectations | Consent / privacy boundary gate | Data Protection Officer | Internal | Document metadata, version, applicability | Privacy-check references | Re-identifying or routing patient data without basis |
| SRC-057 | `knowledge/COMPUTERISED_SYSTEM_LIFECYCLE.md` (K-010) | Policy / SOP / standard source | Define system lifecycle and validation expectations | R-09 validation-state gate | Validation / Quality owner | Internal | Document metadata, version | Validation references | Using an unvalidated system as authoritative |
| SRC-058 | `knowledge/IDMP_MASTER_DATA_GOVERNANCE.md` (K-015) | Policy / SOP / standard source | Define IDMP master-data governance | R-05 identity match; IDMP authority gate | Regulatory Affairs (IDMP) | Internal | Document metadata, version | IDMP references | Resolving an IDMP conflict automatically |
| SRC-059 | `knowledge/AI_GXP_BOUNDARY.md` (K-003) | Policy / SOP / standard source | Define the AI read-only advisory boundary in GxP work | All non-negotiables | Quality / AI governance owner | Internal | Document metadata, version | Boundary references | Delegating regulated accountability to AI |
| SRC-060 | `knowledge/AI_DISABLED_CONTINUITY.md` (K-002) | Policy / SOP / standard source | Define safe operation without AI inference | Ransomware / AI-off continuity gate | CISO / continuity owner | Internal | Document metadata, version | Continuity references | Stopping safe operation when AI is unavailable |
| SRC-061 | `knowledge/AI_INCIDENT_RESPONSE.md` (K-004) | Policy / SOP / standard source | Define AI incident response expectations | R-16 audit-capture gap; ransomware gate | CISO / AI governance owner | Internal | Document metadata, version | Incident-response references | Hiding the 47-minute audit-capture gap |
| SRC-062 | `knowledge/ZERO_TRUST_AI_TOOLS.md` (K-032) | Policy / SOP / standard source | Define Zero-Trust expectations for AI tools and manifests | Tool-manifest governance gate | CISO / tool owner | Internal | Document metadata, version | Tool-governance references | Using unsigned or stale tool definitions |
| SRC-063 | `knowledge/AI_MODEL_CHANGE_CONTROL.md` (K-005) | Policy / SOP / standard source | Define model change-control expectations | Model-registry / AI-control gate | AI governance / Quality owner | Internal | Document metadata, version | Model-change references | Using an unqualified model change as evidence |
| SRC-064 | A0 context pack (`Docs/DDD-Lab/Phase 0/A0_Context_Pack.md`) | Governance / non-negotiable source | Carry forward organisation facts, non-negotiables and scenario | All rules and gates | Workshop/domain facilitation owner | Internal | Artifact ID, version, source stage, validation status | Boundary and non-negotiable checks | Bypassing non-negotiables or adding invented facts |
| SRC-065 | Stage 8 rules vs reasoning matrix (`Docs/DDD-Lab/Phase 8/A8_Rules_vs_Reasoning_Matrix.md`) | Governance / non-negotiable source | Trace rules, decisions, gates and audit obligations | All Stage 8 rules and gates | Workshop/domain facilitation owner; business owners to validate | Internal | Artifact ID, version, source stage, validation status | Trace from source evidence to rule/gate | Mistaking a derived artifact for a controlled source |
| SRC-066 | Stage 8 human-owned decision register | Governance / non-negotiable source | Identify decisions requiring accountable human owners | D-01 to D-16 | Relevant accountable owners to confirm | Internal | Artifact ID, decision ID, owner, evidence requirement | Ownership and decision evidence | Treating support output as decision authority |
| SRC-067 | Stage 8 approval / stop / escalation / closure gates | Governance / non-negotiable source | Preserve required gates before approval, release, escalation or closure | Approval, stop, escalation, closure gates | Relevant process owners to confirm | Internal | Gate ID, trigger, owner, pass/fail condition | Gate evaluation and unresolved exceptions | Hidden exceptions, premature release, premature closure |
| SRC-068 | Inject evidence map (`data/inject_evidence_map.csv`) | Governance / non-negotiable source | Map injects to evidence files and challenge conditions | All workflows; evidence-inventory alignment | Workshop/domain facilitation owner | Internal | Inject ID, dimension, title, evidence sources, status | Inject-to-evidence trace | Treating the map as decision authority |
| SRC-069 | Inject catalogue (`data/injects.json`) | Governance / non-negotiable source | Reference the 84 disclosed injects (INJ-001 to INJ-084, D01–D13) | All workflows; case discovery | Workshop/domain facilitation owner | Internal | Inject ID, dimension, description, state | Inject references | Inventing hidden injects beyond the disclosed 84 |
| SRC-070 | Data dictionary (`data/DATA_DICTIONARY.csv`) | Governance / non-negotiable source | Define dataset columns, types and semantics | All evidence interpretation | Data governance / facilitation owner | Internal | Dataset, column, type, description, nullability | Column interpretation references | Interpreting a field outside its dictionary semantics |
| SRC-071 | Dataset profile (`data/DATASET_PROFILE.csv`) | Governance / non-negotiable source | Show dataset rows, columns and quality signals | Evidence-quality context | Data governance / facilitation owner | Internal | Dataset, rows, columns, quality signals | Dataset-profile references | Treating sparse or low-quality datasets as complete |
| SRC-072 | Tool catalog (`data/tool_catalog.csv`) | AI-platform control evidence | Describe tools available to AI-assisted workflows | Tool-manifest governance gate | CISO / tool owner | Internal | Tool ID, definition, entitlement, state, source | Tool-use records | Calling tools with stale or revoked entitlements |
| SRC-073 | Tool manifest (`data/tool_manifest_poisoned.json`) | AI-platform control evidence | Show tool manifest with stale entitlements and unsigned definitions | Tool-manifest governance gate | CISO / tool owner | Internal; quarantined until governance review | Manifest ID, definitions, entitlement, signature state, source | Manifest verification, quarantine record | Using a poisoned or unsigned tool definition |
| SRC-074 | Model registry / artifacts (`data/model_registry.csv`, `data/model_artifacts.csv`) | AI-platform control evidence | Show model state, qualification and artifacts | AI-model change-control gate | AI governance / Quality owner | Internal | Model ID, state, qualification, artifact link, source | Model-state records | Using an unqualified research model as evidence |
| SRC-075 | Model costs / usage (`data/model_costs.csv`, `data/model_usage.csv`) | AI-platform control evidence | Show token usage and cost context for AI-system controls | Token-efficiency / AI-control gate | Finance / AI platform owner | Internal | Model, period, usage, cost, source | Cost/usage records | Ignoring token cost or denial-of-wallet risk |
| SRC-076 | Users and entitlements (`data/users_entitlements.csv`, `data/access_cache.csv`) | AI-platform control evidence | Show user entitlement state and cache lag | R-10 entitlement gate; entitlement-revocation gate | Identity / access owner; Data Protection Officer | Internal | User, role, entitlement, cache state, source | Entitlement check, revocation state | Surfacing data through a stale entitlement cache |
| SRC-077 | Access logs / privileged sessions (`data/access_logs.csv`, `data/privileged_sessions.csv`) | AI-platform control evidence | Show access and privileged-session evidence | R-16 audit completeness; shared-account gate | CISO / audit owner | Internal | User, system, time, session, source | Access records | Missing a shared-account or privileged access pattern |
| SRC-078 | Audit trails (`data/audit_trails.csv`) | AI-platform control evidence | Show audit-capture completeness and the 47-minute gap | R-16 audit-capture gap remains visible | Audit / quality oversight | Internal | Event ID, source, owner, status, timestamp | Audit event envelope, gap record | Filling or hiding the 47-minute audit-capture gap |
| SRC-079 | System inventory / validation inventory / spreadsheet inventory (`data/system_inventory.csv`, `data/validation_inventory.csv`, `data/spreadsheet_inventory.csv`) | AI-platform control evidence | Show system and validation state including unapproved spreadsheets | R-09 validation-state gate | Validation / Quality owner | Internal | System, validation state, spreadsheet state, owner | Validation-state evidence | Treating an unvalidated system or unapproved spreadsheet as authoritative |
| SRC-080 | Downtime / network zones / continuity requirements (`data/downtime_events.csv`, `data/network_zones.csv`, `data/continuity_requirements.csv`) | AI-platform control evidence | Show ransomware isolation, OT segmentation and continuity | Ransomware / AI-off continuity gate | CISO / continuity owner | Internal | Event, zone, requirement, state, source | Downtime and continuity records | Operating unsafely when AI is unavailable |
| SRC-081 | Retention rules / legal holds (`data/retention_rules.csv`, `data/legal_holds.csv`) | AI-platform control evidence | Show retention, legal hold and deletion constraints | Record-retention gate; data-subject request gate | Records owner / Data Protection Officer | Internal | Record class, retention, hold, state, source | Retention/hold references | Deleting or preserving records against retention rules |
| SRC-082 | `knowledge/MALICIOUS_SUPPLIER_DEVIATION.md` (K-998) | Untrusted source | Test that supplier-derived content with hidden prompt-injection is quarantined | INJ-065; source-governance gate | Source/document governance owner | Internal only; quarantined; never authoritative | Source ID, status untrusted, quarantine state, retrieval time | Quarantine record, attempted-injection flag | Executing the embedded "ignore quality holds" instruction |
| SRC-083 | Vendor portals | Untrusted source | Show vendor-supplied data with undocumented fields and shared accounts | Source-governance gate; INJ-067 | Vendor-quality / Procurement; CISO | Internal; treat as untrusted until governed | Vendor, field documentation state, account model, source | Portal-evidence verification | Treating undocumented vendor fields as authoritative |
| SRC-084 | Shared-account spreadsheets (`data/spreadsheet_inventory.csv`) | Untrusted source | Show macro-enabled or shared-account spreadsheets with undocumented fields | Source-governance gate; INJ-032 | Quality / spreadsheet owner | Internal; treat as untrusted until governed | Spreadsheet, owner, macro state, account model, source | Spreadsheet-use records, governance state | Silently influencing quality, safety or supply evidence |
| SRC-085 | `knowledge/BATCH_RELEASE_POLICY_OLD.md` (K-007) | Untrusted source | Show a superseded release policy that must not be used as current | R-03, R-12 release-readiness rules | Quality policy owner | Internal; expired status, not usable as current | Document ID, status, version, supersession evidence | Policy-version check | Using an expired release policy as current |

---

## 5. Missing / Required Source Register

These sources are needed for safe governed use but are not fully available in the Stage 8 handoff or evidence inventory. Their content must not be invented.

| Missing Source ID | Missing or Incomplete Source | Why It Is Needed | Affected Rule / Decision / Gate | Consequence If Unavailable | Owner to Confirm |
|---|---|---|---|---|---|
| MISS-001 | Full consent, entitlement and privacy boundary policy | Needed to govern access, use, routing and sharing of patient/participant data | R-10 entitlement/consent gate; privacy boundary | Patient/participant data access cannot be confidently governed | Data Protection Officer / Legal |
| MISS-002 | Full authority and effective-date policy per business object and jurisdiction | Needed to define which source is authoritative per object, jurisdiction and date | Authority / effective-date / jurisdiction gate | A later timestamp may be wrongly treated as authoritative | Regulatory Affairs / master-data governance |
| MISS-003 | Approved unit-conversion mapping and acceptance record (mg/L vs µg/mL) | Needed to resolve the contract-lab concentration convention | R-04 unit-conversion consistency | Unit state remains unapproved; no output while unresolved | Laboratory / interface owner with Quality |
| MISS-004 | Independent verification record for the contract-site audit commitment | Needed to treat the commitment as verified rather than claimed closed | R-07 supplier-audit commitment; R-12 release-packet completeness | EU release packet remains incomplete | Supplier-quality / Quality reviewer |
| MISS-005 | Full release-packet checklist and evidence-gap list | Needed to assess release-packet completeness beyond the packet dataset | R-12 release-packet completeness | A batch may be shown release-ready with hidden gaps | Quality release reviewer |
| MISS-006 | Approved single-source-of-truth MedDRA version basis | Needed to align terminology across versions | R-13 MedDRA version consistency | Preferred-term conflict remains unresolved | Safety coder / terminology owner |
| MISS-007 | Approved listedness determination record per jurisdiction | Needed to govern IB/CCDS/local-label conflict handling | D-10 listedness determination | Listedness conflict remains visible but unresolved | PV medical reviewer / Regulatory Affairs |
| MISS-008 | Full cold-chain logger clock and pallet-association evidence | Needed to resolve disputed logger clocks and pallet links | D-13 cold-chain excursion disposition | Cold-chain excursion cannot be disposed confidently | Logistics / cold-chain owner with Quality |
| MISS-009 | Case-to-pallet aggregation records after the line restart | Needed to confirm aggregation state | Serialisation aggregation gate | Aggregation link cannot be assumed | Serialisation owner |
| MISS-010 | Full allocation policy and authorised allocation-approval record | Needed to generate policy-bounded options and evidence approval basis | D-12 allocation decision | Options cannot be policy-bounded; no execution without approval | Supply Chain VP / authorised Quality owner |
| MISS-011 | CMO capacity commitment records showing dual-sponsor promises | Needed to evidence the CMO capacity conflict | D-12 allocation; shortage escalation gate | Capacity conflict cannot be evidenced | Procurement / CMO quality |
| MISS-012 | Excipient supplier recovery and replacement evidence beyond the estimate | Needed to bound shortage options | D-12 allocation; shortage escalation gate | Eight-week recovery estimate treated as fixed | Procurement / Supplier-quality |
| MISS-013 | Independent verification that no later record supersedes approved signed records | Needed to govern authority by approval date, not timestamp | Authority gate | A later timestamp may be wrongly treated as more authoritative | Regulatory Affairs / master-data governance |
| MISS-014 | Full eConsent version mapping for the pivotal-trial amendment | Needed to govern participant-data access and use | R-10 entitlement/consent gate | Consent version asynchrony blocks lawful access | Clinical Operations / Data Protection Officer |
| MISS-015 | Validation-state confirmation across inventories (validated/conditional/research-only) | Needed to gate systems used as evidence | R-09 validation-state gate | Ambiguous validation state blocks output | Validation / Quality owner |
| MISS-016 | Independent evidence of the 47-minute audit-capture gap and AI-off continuity state | Needed to keep the gap visible and govern safe operation | R-16 audit-capture gap; ransomware gate | Gap may be filled or hidden silently | Audit / CISO |
| MISS-017 | Approved multilingual PV narrative review process (Arabic, Hindi, English, German) | Needed to govern language/translation controls | Language/translation control; multilingual review gate | Unverified translation may be treated as reviewed | PV intake / Global Head of Pharmacovigilance |
| MISS-018 | Override policy | Needed to define who can override what, under what conditions, with what evidence | Exception override gate | Overrides may be recorded without a clear authorization boundary | Quality / governance owner |
| MISS-019 | Audit record retention / evidence-trail policy | Needed to define audit completeness, retention and inspection requirements | Audit obligations; inspection gate | Audit trail may be captured but not retention-governed | Audit / compliance / records owner |
| MISS-020 | Quarantine and governance disposition for untrusted documents and manifests | Needed to govern the malicious supplier deviation and poisoned tool manifest | Source-governance gate; INJ-065, INJ-066 | Untrusted content may be used as evidence | Source/document governance owner; CISO |

---

## 6. Required Metadata Schema

Every governed source should carry metadata sufficient for ownership, applicability, regulated-output control, and auditability.

```text
Document ID
Title
Source category
Source owner
Approver
Business function / specialty
Product / batch / case / shipment applicability
Workflow applicability (Workflow A / B / C / cross-cutting)
Jurisdiction
Effective date
Review date
Version
Source status: approved / draft / expired / excerpt / untrusted / derived artifact
Language
Sensitivity level
Allowed roles
Consent / entitlement status where applicable
Approved-for-regulated-output flag
Approved-for-patient/participant-facing-use flag
Citation / evidence reference format
Batch / product / case / shipment identifier where applicable
Author / creator where applicable
Timestamp or record date
Source system or repository where applicable
Validation state where applicable
Trust boundary / untrusted-data warning where applicable
Audit event ID where used
```

Minimum metadata for batch and product-specific evidence:

```text
Batch / product / material identifier
Source item name
Source date/time
Author or originating system where available
Genealogy or lineage reference
Unit and terminology state
Validation state
Accessing role
Consent / entitlement status where patient data involved
Evidence reference
Use context
Timestamp of access/use
```

Minimum metadata for PV and safety evidence:

```text
Case identifier
Product / batch linkage
Source receipt (vendor, affiliate inbox, global safety DB)
MedDRA version and preferred term
Listedness-source version and jurisdiction
Language
Sensitive-segment state
Consent / entitlement status
Accessing role
Evidence reference
Timestamp of access/use
```

Minimum metadata for policy/SOP/standard sources:

```text
Document ID
Title
Owner
Approver
Version
Effective date
Review date
Jurisdiction applicability
Workflow applicability
Language
Sensitivity level
Allowed roles
Approved-for-regulated-output flag
Approved-for-patient/participant-facing-use flag
Citation format
Status: approved/current or not usable
```

---

## 7. Rule-to-Source Traceability Matrix

| Rule / Gate | Primary Source Evidence | Supporting Source Evidence | Human Owner Who Uses the Evidence | Source Gap or Caution | Audit Evidence Required |
|---|---|---|---|---|---|
| Identity / product-code match (R-01, R-05) | Product master (SRC-001), batch records (SRC-002) | Substance master, IDMP mappings (SRC-038) | Identity / genealogy / master-data owner | IDMP identity conflict unresolved | Identity-match evidence, product-master reference |
| Genealogy completeness (R-02) | MES genealogy (SRC-003), warehouse consumption (SRC-004) | Batch records (SRC-002) | Identity / genealogy / master-data owner | SUA-88 branch missing; must remain visible | Genealogy-break identification, source records |
| Batch not release-ready with unresolved elements (R-03) | Release packets (SRC-018), batch-review readiness package | Batch records, genealogy, lab results, supplier evidence | Quality release reviewer | Packet gaps must stay visible | Packet status, element checklist, gap ownership |
| Unit-conversion consistency (R-04) | Lab results (SRC-006), interface mappings (SRC-007) | Data dictionary (SRC-070) | Laboratory / interface owner with Quality | mg/L vs µg/mL assumption unapproved | Conversion mapping, approval/override record |
| Disputed OOS/OOT/invalid state open (R-06) | Lab results (SRC-006), OOS investigations (SRC-008) | OOS/OOT policy (SRC-044), notebook evidence | Laboratory analyst / OOS owner | LIMS vs statistical tool vs notebook disagree | Conflicting states, investigation record |
| Supplier-audit commitment not closed until verified (R-07) | Supplier audits (SRC-016), release packets (SRC-018) | Regulatory commitments (SRC-039), policy (SRC-042) | Supplier-quality / Quality reviewer | Independent verification record missing | Verification request, verification state |
| Back-entered step checkpoint (R-08) | eBR steps (SRC-005), downtime events (SRC-080) | Data-integrity standard (SRC-043) | Manufacturing / Quality reviewer | Step back-entered after network degradation | Detection record, timestamps, checkpoint state |
| Validation-state consistency (R-09) | System inventory (SRC-079), validation inventory (SRC-079) | Computerised-system lifecycle (SRC-057) | Validation / Quality owner | Validation state ambiguous across inventories | Validation-state evidence, no-answer record |
| Entitlement/consent gate (R-10) | Users/entitlements (SRC-076), sensitive segments (SRC-025) | eConsent/secondary-use (SRC-055), privacy (SRC-056) | Data Protection Officer / privacy owner | eConsent version asynchrony with amendment | Consent/entitlement check, access/use record |
| Checkpoint-state completeness (R-11) | All batch/PV/supply records | Stage 8 rules (SRC-065) | Accountable workflow owner | Back-entered step checkpoint missing | Checkpoint-state record, no-answer declaration |
| Release-packet element completeness (R-12) | Release packets (SRC-018) | Supplier audits (SRC-016), certificates (SRC-017), release policy (SRC-042) | Quality release reviewer | Missing audit commitment confirmation | Packet status, element checklist, gap ownership |
| MedDRA version consistency (R-13) | Adverse events / terminology versions (SRC-022) | PV case policy (SRC-046) | Safety coder / terminology owner | Two MedDRA versions change preferred term | Version-alignment evidence, source |
| Duplicate candidates only (R-14) | ICSR cases (SRC-019), duplicate candidates (SRC-020) | PV duplicate management (SRC-047) | PV case-intake staff / PV reviewer | Candidates under different product names | Duplicate rationale, candidates, reviewer routing |
| Reporting-clock inputs complete (R-15) | Safety receipts (SRC-021), ICSR cases (SRC-019) | PV reporting clocks (SRC-050) | PV case-intake staff / PV reviewer | Disputed awareness date across sources | Clock-reconstruction evidence, source basis |
| Audit-capture gap visible (R-16) | Audit trails (SRC-078), downtime/continuity (SRC-080) | AI incident response (SRC-061), AI-disabled continuity (SRC-060) | Audit / quality oversight | 47-minute gap during master-data repair | Gap detection, duration, owner |
| Auditable everything (R-17) | All governed sources | Stage 8 audit obligations (SRC-065) | Audit / quality oversight | Missing or incomplete audit trail | Audit event envelope, source, owner, timestamp |
| QP certification evidence gate | Batch-review readiness package, release packets (SRC-018) | Batch records, lab results, supplier evidence, release policy | EU Qualified Person | Certification is human-only; readiness is not certification | Pending-status record, evidence package, QP identity |
| PV disposition (seriousness/causality/expectedness/reportability) | ICSR cases (SRC-019), listedness sources (SRC-023), labels (SRC-024) | PV case policy (SRC-046), listedness authority (SRC-048) | PV medical/safety reviewer | Final determinations are human-only | Prepared case-review material, reviewer routing |
| Signal confirmation | Signal metrics / exposure (SRC-027) | PV case policy (SRC-046) | Signal management | Signal confirmation is human-only | Signal-review material, basis |
| Allocation decision | Inventory (SRC-028), demand forecast (SRC-029), allocation constraints (SRC-030) | CMO capacity (SRC-034), supplier risks (SRC-035), allocation ethics (SRC-053) | Supply Chain VP / authorised Quality owner | No allocation without authorised human approval | Option rationale, evidence used, approval request |
| Cold-chain excursion disposition | Temperature loggers (SRC-032), shipments (SRC-031) | Serialisation events (SRC-033), cold-chain assessment (SRC-052) | Logistics / cold-chain owner with Quality input | Logger clocks and pallet association disputed | Logger basis, pallet link, excursion evidence |
| Serialisation aggregation | Serialisation/packaging events (SRC-033) | Serialisation and returns policy (SRC-051) | Serialisation owner | Case-to-pallet aggregation missing after line restart | Aggregation-state record, gap ownership |
| Recall consideration | Recall candidates (SRC-036), material genealogy (SRC-003) | Serialisation policy (SRC-051), market authorisations (SRC-037) | Quality / Regulatory accountable roles | Recall initiation is human-only | Recall consideration record, decision, owner |
| Inspection-evidence packaging | All governed sources | Inspection requests (SRC-040), AI-platform controls (SRC-072 to SRC-081) | Regulatory / Quality participant | 72-hour multi-agency request | Package manifest, source citations, timeline |
| Escalation / closure gates | All governed sources | Stage 8 gates (SRC-067) | Accountable workflow owner | Unresolved states must not be hidden | Escalation record, owner, status, outcome |

---

## 8. Regulated-Output and Patient/Patient-Participant-Facing Source Controls

Sources used to prepare regulated output, inspection evidence, or content that reaches patients, participants, healthcare professionals or regulators are governed by stricter controls than internal evidence summaries.

```text
Consent / entitlement checks must pass before any patient or participant data is surfaced, routed or shared; eConsent version asynchrony with the trial amendment blocks lawful access.

Listedness and expectedness content must cite approved label, IB and core-data-sheet (CCDS) sources by version and jurisdiction; an unapproved or superseded source must not be used for listedness.

Approved product labels (SRC-024) are the regulated patient/HCP-facing source; any draft of label or package content for release requires approval and must cite the approved version.

Multilingual PV narrative review must respect language controls (e.g., Arabic, Hindi, English, German) and may only proceed through the approved multilingual review process; unverified translation must not be released.

Release packets and QP-certification evidence packages are regulator-facing material; they must be assembled with complete, conflict-visible evidence and are approved for external packaging only by the accountable human roles.

Inspection-evidence packages must preserve traceability and must not create or hide evidence.

Every patient-facing, participant-facing, HCP-facing or regulator-facing draft, review, approval, edit, release and delivery event must be auditable.
```

Regulated or patient/participant-facing content must not be based only on:

```text
raw, unreviewed or unverified batch, laboratory or safety records
unapproved unit conversions
unverified supplier evidence
unapproved translation of PV narratives
unresolved identity, genealogy, unit, terminology, authority, consent, validation or checkpoint states
untrusted supplier documents, tool manifests or shared-account spreadsheets
derived workshop artifacts treated as controlled sources
```

This artifact does not write, approve or release any product label, patient instruction, PV narrative or inspection package; it only governs the sources from which such material could be prepared.

---

## 9. Source Access, Use, and No-Answer Rules

### Source Access Rules

```text
Batch, safety, quality, supply and patient/participant evidence may be accessed only when identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation and checkpoint state are resolved or declared no-answer.

Patient/participant data may be accessed or used only when the entitlement/consent gate passes.

Role access must match the sensitivity and use case of the source.

Policy, SOP and standard sources must have owner, approver, version, effective date, review date, jurisdiction applicability, status and allowed roles.

Regulated-output and patient/participant-facing source use requires approved status or approved human review and release workflow.

AI-platform control evidence is used to evidence AI-system controls, not to make regulated decisions.
```

### Source Use Rules

```text
Use batch and product-specific evidence only for the batch, product or material it belongs to.

Use genealogy evidence to surface lineage breaks, never to silently repair lineage.

Use laboratory results only to surface unit, OOS/OOT and interpretation conflicts until the accountable owner reviews.

Use PV and safety evidence only to prepare intake, duplicate, clock, terminology, listedness and linkage material; final PV decisions remain with reviewers.

Use supply and cold-chain evidence only to generate traceable, policy-bounded options; never to execute allocation, reservation, shipment or recall.

Use regulatory evidence only per jurisdiction, effective date and authority; a later timestamp is not automatically more authoritative.

Use untrusted sources only under quarantine and governance disposition; never as authority.

Use policy/SOP/standard sources only within their stated scope, jurisdiction and effective period and only when current/approved status is confirmed.
```

### No-Answer / Human-Review Rules

```text
If authority, effective date, jurisdiction or version is unresolved, do not treat the source as usable.

If identity, genealogy, unit, terminology, consent/entitlement, validation or checkpoint state is unresolved, do not produce evidence output.

If a source is untrusted, unverified, conflicting or out-of-scope, trigger no-answer, escalation or human review.

If evidence is missing, do not infer the missing batch, product, safety, quality or supply fact.

If a document is draft, expired, superseded, unapproved or quarantined, do not treat it as authoritative.

If a supplier-audit commitment is unverified, do not treat it as closed.

If the 47-minute audit-capture gap is unresolved, do not treat the affected records as complete.

If regulated or patient-facing approval status is missing, do not release or package the material.

If audit evidence cannot be captured, do not treat the recommendation, draft, approval, override, release, escalation, action, outcome or closure as complete.
```

---

## 10. Source Gaps and Risks

```text
Full consent, entitlement and privacy boundary policy is not fully provided.

Full authority and effective-date policy per business object and jurisdiction is not fully provided.

Approved unit-conversion mapping and acceptance record (mg/L vs µg/mL) is not provided.

Independent verification record for the contract-site audit commitment is not provided.

Full release-packet checklist and evidence-gap list is not provided.

Approved MedDRA-version basis and listedness-determination record per jurisdiction are not fully provided.

Full cold-chain logger clock, pallet-association and aggregation evidence is not resolved.

Full allocation policy and authorised allocation-approval record are not provided.

CMO capacity commitment records and excipient recovery evidence are not fully provided.

eConsent version mapping for the pivotal-trial amendment is not provided.

Validation-state confirmation across inventories is not provided.

The 47-minute audit-capture gap and AI-off continuity state are not resolved.

Approved multilingual PV narrative review process is not fully provided.

Override policy and audit record retention / evidence-trail policy are not provided.

Untrusted sources (MALICIOUS_SUPPLIER_DEVIATION.md, tool_manifest_poisoned.json, vendor portals, shared-account spreadsheets) require quarantine and governance disposition before any use.

Derived Stage 8 rules are governance artifacts, not controlled source records.
```

These risks must remain visible before the next stage because weak source governance can cause:

```text
wrong source use
expired, superseded, unapproved or untrusted source use
silent unit conversion or silent genealogy repair
hidden OOS/OOT, excursion, supplier or release-packet gaps
patient/participant data surfaced without consent/entitlement
duplicate, clock, terminology or listedness conflicts hidden
cold-chain or aggregation gaps assumed resolved
unbounded or unapproved allocation options
weak auditability and unclear human accountability
inspection-evidence packaging that creates or hides evidence
```

---

## 11. Stage 9 Quality Check

Use this checklist before moving to Stage 10:

```text
No batch, safety, quality or supply issue has been solved in this artifact.
No batch release/rejection/reprocess/re-label/recall decision has been made or implied.
No QP certification has been implied.
No final PV seriousness, causality, expectedness, reportability or signal-confirmation decision has been made.
No inventory status change, capacity reservation, stock allocation, shipment or recall initiation has been implied.
All regulated decisions remain human-owned with named accountable roles.
All available sources are classified across batch/product, quality/supplier, PV/safety, supply/cold-chain, regulatory, policy/SOP, governance, AI-platform control and untrusted categories.
Missing or incomplete sources remain visible as gaps with owners.
Regulated-output and patient/participant-facing source controls are explicit.
Consent/entitlement checks before patient/participant data is surfaced are explicit.
Approved label/IB/CCDS sources are identified for listedness.
Language/translation controls for multilingual PV narratives are explicit.
Untrusted sources are marked untrusted and quarantined.
Source metadata requirements include owner, approver, version, effective/review date, jurisdiction, language, allowed roles, sensitivity, validation state and regulated/patient-facing approval status.
Rule-to-source traceability is clear.
No-answer, escalation and human-review rules are explicit.
The 47-minute audit-capture gap and AI-off continuity state remain visible.
Audit obligations are preserved for recommendation, draft, approval, override, release, escalation, action, outcome and closure.
Derived workshop artifacts are not treated as controlled source records.
No architecture, RAG systems, MCP, agents, vector databases, APIs, deployment or implementation design has been introduced.
```

---

## 12. NEXT_STAGE_INPUT_BLOCK

```text
Stage 10 Input — Agent Responsibility Cards Handoff

Final Source Governance Summary:
Stage 9 creates the governed source and evidence register for the NovaCura Therapeutics Group pharmaceutical case. It identifies available batch/product evidence, quality/supplier evidence, PV/safety evidence, supply/cold-chain evidence, regulatory evidence, policy/SOP/standard sources, governance constraints, AI-platform control evidence, untrusted sources, and missing or required sources. It confirms that sources must be trusted, owned, versioned, access-controlled, consent-checked where relevant, approved for regulated or patient-facing output where relevant, and auditable, and that untrusted and missing sources must remain visible. No batch, safety, quality or supply issue has been solved, no release or PV decision has been made, no allocation has been executed, and no regulated or patient-facing content has been approved or released.

Governed Source Categories:
- Batch and product-specific evidence
- Quality and supplier evidence
- PV and safety evidence
- Supply and cold-chain evidence
- Regulatory evidence
- Policy / SOP / standard source
- Governance / non-negotiable source
- AI-platform control evidence
- Untrusted source
- Missing or required source

Available Source Register Summary:
- Product master, batch records, MES genealogy, warehouse consumption, eBR steps, lab results, interface mappings, OOS investigations, environmental monitoring, microbiology results
- Deviations, CAPA, change controls, cleaning validation, production schedule, supplier audits, certificates of analysis, release packets
- ICSR cases, duplicate candidates, safety receipts, adverse events/terminology versions, listedness sources, product labels, sensitive segments, product complaints, signal metrics/exposure
- Inventory, demand forecast, allocation constraints, shipments, temperature loggers, serialisation/packaging events, CMO capacity/vendor contracts, supplier risks, returns/recall candidates
- Market authorisations, IDMP mappings, regulatory commitments, regulatory changes/inspection requests, protocol versions/site approvals
- Approved knowledge/ policy documents (e.g., BATCH_RELEASE_EVIDENCE_POLICY, GXP_DATA_INTEGRITY_STANDARD, PHARMACOVIGILANCE_CASE_POLICY, PV_DUPLICATE_MANAGEMENT, PV_LISTEDNESS_AUTHORITY, PV_MULTILINGUAL_REVIEW, PV_REPORTING_CLOCKS, STERILE_MANUFACTURING_ESCALATION, SERIALISATION_AND_RETURNS, COLD_CHAIN_ASSESSMENT, SUPPLY_ALLOCATION_ETHICS, CLINICAL_PROTOCOL_AUTHORITY, ECONSENT_AND_SECONDARY_USE, PRIVACY_AND_PSEUDONYMISATION, COMPUTERISED_SYSTEM_LIFECYCLE, IDMP_MASTER_DATA_GOVERNANCE, AI_GXP_BOUNDARY, AI_DISABLED_CONTINUITY, AI_INCIDENT_RESPONSE, ZERO_TRUST_AI_TOOLS, AI_MODEL_CHANGE_CONTROL)
- A0 context pack, Stage 8 rules/decisions/gates, inject evidence map, inject catalogue, data dictionary, dataset profile
- Tool catalog, tool manifest, model registry/artifacts, model costs/usage, users/entitlements, access logs/privileged sessions, audit trails, system/validation/spreadsheet inventories, downtime/network zones/continuity, retention/legal holds
- Untrusted: MALICIOUS_SUPPLIER_DEVIATION.md, tool_manifest_poisoned.json, vendor portals, shared-account spreadsheets, superseded BATCH_RELEASE_POLICY_OLD

Missing / Required Source Gaps:
- Full consent/entitlement/privacy boundary policy
- Full authority and effective-date policy per object/jurisdiction
- Approved unit-conversion mapping (mg/L vs µg/mL)
- Independent supplier-audit verification record
- Full release-packet checklist and gap list
- Approved MedDRA-version basis and listedness-determination record
- Resolved cold-chain logger/pallet/aggregation evidence
- Full allocation policy and authorised approval record
- CMO capacity commitment records and excipient recovery evidence
- eConsent version mapping for the trial amendment
- Validation-state confirmation across inventories
- Independent audit-capture-gap and AI-off continuity record
- Approved multilingual PV narrative review process
- Override policy and audit retention/evidence-trail policy
- Quarantine and governance disposition for untrusted sources

Required Metadata:
- Document ID, title, source category, owner, approver, business function, product/batch/case/shipment applicability, workflow applicability, jurisdiction, effective/review date, version, source status, language, sensitivity level, allowed roles, consent/entitlement status, approved-for-regulated-output flag, approved-for-patient/participant-facing-use flag, citation format, identifiers, author/creator, timestamp, source system, validation state, trust boundary, audit event ID

Rule-to-Source Traceability Summary:
- Identity/product-code and genealogy gates depend on product master, batch records, MES genealogy, warehouse consumption.
- Unit-conversion, OOS/OOT and release-packet gates depend on lab results, interface mappings, OOS investigations, supplier audits, certificates and release packets.
- PV intake, duplicate, clock, terminology, listedness and linkage gates depend on ICSR cases, duplicate candidates, safety receipts, adverse events/terminology versions, listedness sources, product labels, sensitive segments, product complaints and approved PV policies.
- Supply and cold-chain gates depend on inventory, demand forecast, allocation constraints, shipments, temperature loggers, serialisation events, CMO capacity, supplier risks and approved supply/cold-chain policies.
- Regulatory and authority gates depend on market authorisations, IDMP mappings, regulatory commitments, protocol versions/site approvals and approved regulatory policies.
- Consent/entitlement gates depend on eConsent/secondary-use, privacy and users/entitlements sources.
- AI-system-control gates depend on tool catalog, tool manifest, model registry, users/entitlements, access logs, audit trails, system/validation/spreadsheet inventories, downtime/network zones/continuity and approved AI boundary policies.
- Auditability depends on non-negotiables, Stage 8 audit obligations and audit-trail/retention sources.

Regulated-Output and Patient/Patient-Participant-Facing Source Controls:
- Consent/entitlement checks must pass before patient/participant data is surfaced.
- Listedness/expectedness content must cite approved label, IB and CCDS sources by version and jurisdiction.
- Approved product labels are the regulated patient/HCP-facing source.
- Multilingual PV narratives require approved language/translation controls (Arabic, Hindi, English, German).
- Release packets and QP-certification evidence packages are regulator-facing and assembled by accountable humans.
- Every draft, review, approval, edit, release and delivery event must be auditable.

Access and No-Answer Rules:
- Do not produce evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
- Do not treat draft, expired, superseded, unapproved, quarantined or untrusted sources as authoritative.
- Do not infer missing evidence.
- Do not silently convert units, repair genealogy, confirm duplicates, set reporting clocks, pick listedness winners, or disposition OOS/OOT or cold-chain excursions.
- Do not change inventory status, reserve capacity, allocate stock, ship product or initiate a recall without explicit authorised human approval.
- Do not release or package regulated or patient-facing content without approval.
- Do not treat any recommendation, draft, approval, override, release, escalation, action, outcome or closure as complete without audit evidence.

Audit Obligations:
- Batch/product/case/shipment/source identity
- Source evidence and provenance citation
- Source owner / role
- Source status and timestamp
- Decision or action taken
- Approval, rejection, or override where applicable
- Override reason where applicable
- Release/closure status where applicable
- Escalation action and outcome where applicable
- The 47-minute audit-capture gap and AI-off continuity state remain visible

Open Questions:
- Who confirms each source owner and approver?
- Which sources are approved and current versus excerpt-only, missing, draft, expired or untrusted?
- Which sources are approved for regulated-output or patient/participant-facing use?
- Which policy defines authority, effective date and jurisdiction per business object?
- Which policy defines consent, entitlement, privacy and access boundaries?
- Which evidence is required before a draft, approval, override, escalation, release or closure can be audited?
- How are untrusted documents and manifests quarantined and disposed?
- What is the approved multilingual PV narrative review process?
- Who governs overrides and audit retention?
- Which source gaps prevent safe evidence-backed workflow completion?
```

Stage 9 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 10.
