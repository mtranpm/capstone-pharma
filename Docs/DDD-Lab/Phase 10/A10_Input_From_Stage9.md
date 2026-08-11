# A10 Input From Stage 9 — Governed RAG Source Register

Use this file as the direct input attachment for **Stage 10 — Agent Responsibility Cards**.

This input is derived from the completed Stage 9 artifact for the **NovaCura Therapeutics Group** pharmaceutical evidence-reconciliation case (Project AEGIS-PHARMA).

---

## Source Stage

```text
Stage 9 — Governed RAG Source Register
```

## Target Stage

```text
Stage 10 — Agent Responsibility Cards
```

## Stage 10 Purpose

Stage 10 must define bounded responsibility cards for support roles that may help the batch-review, pharmacovigilance and supply-recovery workflows. The goal is to clarify responsibility, inputs, outputs, forbidden actions, human ownership, approval requirements, evidence requirements, failure modes, escalation paths, and audit events.

The output must remain governed, bounded, auditable, and human-owned. It must not resolve any batch, safety, quality or supply issue, must not approve batch release, rejection, reprocess, re-label or recall, must not make final PV decisions, must not change inventory status, reserve capacity, allocate stock, ship product or initiate a recall, must not override consent/entitlement/privacy controls, and must not create technical architecture.

---

# 1. Case Context

NovaCura Therapeutics Group (NTG) is a fictional global pharmaceutical company operating discovery laboratories, clinical-development programmes, pharmacovigilance hubs, manufacturing plants, quality laboratories and distribution networks across India, Germany, Ireland, the United States, the UAE and Singapore. Portfolio: NCX-101 (oral small-molecule oncology near patent expiry), NCB-204 (monoclonal-antibody biologic in pivotal trials and commercial scale-up), NCS-310 (sterile injectable), and NCR-415 (rare-disease gene-therapy research programme).

The estate is fragmented across LIMS, MES, electronic batch records, QMS, RIM, EDC, eConsent, IRT, CTMS, safety databases, serialisation platforms, data lakes, spreadsheets and vendor portals. No system is universally authoritative; authority is contextual per business object, jurisdiction and effective date, and a later timestamp is not automatically more authoritative than an approved signed record.

The active scenario converges on: a pivotal-trial amendment (multiple protocol versions, one country not approved); the disputed biologics batch NCB204-B24071 (missing single-use assembly lot SUA-88 in the MES genealogy branch but present in warehouse consumption; contract-lab concentration in mg/L while the receiving interface assumes µg/mL; LIMS OOS, statistical tool OOT, notebook invalid; EU release packet lacking confirmation of a contract-site audit commitment; a batch-record step back-entered after network degradation); a sterile-area environmental excursion near fill-finish with a corrected organism identification; emerging safety reports (duplicate ICSR cluster under different product names; disputed awareness date across vendor receipt, affiliate inbox and global safety DB; two MedDRA versions changing a preferred term; listedness conflict between IB, core data sheet and local label); a cold-chain failure (disputed logger clocks and pallet association; missing case-to-pallet aggregation after a line restart); an excipient shortage (sole-source supplier contamination, eight-week recovery, CMO capacity promised to two sponsors, demand exceeding stock); a ransomware event (manufacturing historians isolated, MES/QMS degraded, 47-minute audit-capture gap during master-data repair, safe operation required without AI inference); and a multi-agency inspection request within 72 hours.

---

# 2. Final Source Governance Summary From Stage 9

Stage 9 created a governed source and evidence register for the NovaCura pharmaceutical case. The register identifies batch and product-specific evidence, quality and supplier evidence, PV and safety evidence, supply and cold-chain evidence, regulatory evidence, policy/SOP/standard sources, governance constraints, AI-platform control evidence, untrusted sources, and missing required sources.

Stage 9 confirmed that sources must be trusted, owned, versioned, access-controlled, consent-checked where relevant, approved for regulated or patient-facing output where relevant, and auditable. It also confirmed that untrusted sources must be quarantined, missing source content must not be invented, and evidence gaps must remain visible.

---

# 3. Governed Source Categories From Stage 9

```text
Batch and product-specific evidence
Quality and supplier evidence
PV and safety evidence
Supply and cold-chain evidence
Regulatory evidence
Policy / SOP / standard source
Governance / non-negotiable source
AI-platform control evidence
Untrusted source
Missing or required source
```

---

# 4. Available Source Register Summary From Stage 9

```text
Product master, batch records, MES genealogy, warehouse consumption, eBR steps, lab results, interface mappings, OOS investigations, environmental monitoring, microbiology results
Deviations, CAPA, change controls, cleaning validation, production schedule, supplier audits, certificates of analysis, release packets
ICSR cases, duplicate candidates, safety receipts, adverse events / terminology versions, listedness sources, product labels, sensitive segments, product complaints, signal metrics / exposure estimates
Inventory, demand forecast, allocation constraints, shipments, temperature loggers, serialisation / packaging events, CMO capacity / vendor contracts, supplier risks, returns / recall candidates
Market authorisations, IDMP mappings, regulatory commitments, regulatory changes / inspection requests, protocol versions / site approvals
Approved knowledge/ policy documents (e.g., BATCH_RELEASE_EVIDENCE_POLICY, GXP_DATA_INTEGRITY_STANDARD, PHARMACOVIGILANCE_CASE_POLICY, PV_DUPLICATE_MANAGEMENT, PV_LISTEDNESS_AUTHORITY, PV_MULTILINGUAL_REVIEW, PV_REPORTING_CLOCKS, STERILE_MANUFACTURING_ESCALATION, SERIALISATION_AND_RETURNS, COLD_CHAIN_ASSESSMENT, SUPPLY_ALLOCATION_ETHICS, CLINICAL_PROTOCOL_AUTHORITY, ECONSENT_AND_SECONDARY_USE, PRIVACY_AND_PSEUDONYMISATION, COMPUTERISED_SYSTEM_LIFECYCLE, IDMP_MASTER_DATA_GOVERNANCE, AI_GXP_BOUNDARY, AI_DISABLED_CONTINUITY, AI_INCIDENT_RESPONSE, ZERO_TRUST_AI_TOOLS, AI_MODEL_CHANGE_CONTROL)
A0 context pack, Stage 8 rules / decisions / gates, inject evidence map, inject catalogue, data dictionary, dataset profile
Tool catalog, tool manifest, model registry / artifacts, model costs / usage, users / entitlements, access logs / privileged sessions, audit trails, system / validation / spreadsheet inventories, downtime / network zones / continuity, retention / legal holds
Untrusted: MALICIOUS_SUPPLIER_DEVIATION.md, tool_manifest_poisoned.json, vendor portals, shared-account spreadsheets, superseded BATCH_RELEASE_POLICY_OLD
```

---

# 5. Missing / Required Source Gaps From Stage 9

```text
Full consent, entitlement, and privacy boundary policy
Full authority and effective-date policy per business object and jurisdiction
Approved unit-conversion mapping and acceptance record (mg/L vs µg/mL)
Independent verification record for the contract-site audit commitment
Full release-packet checklist and evidence-gap list
Approved MedDRA-version basis and listedness-determination record per jurisdiction
Resolved cold-chain logger clock, pallet-association and aggregation evidence
Full allocation policy and authorised allocation-approval record
CMO capacity commitment records and excipient recovery evidence
eConsent version mapping for the pivotal-trial amendment
Validation-state confirmation across inventories
Independent evidence of the 47-minute audit-capture gap and AI-off continuity state
Approved multilingual PV narrative review process (Arabic, Hindi, English, German)
Override policy
Audit record retention / evidence-trail policy
Quarantine and governance disposition for untrusted sources
```

Do not invent missing source content. Only identify the missing source as a gap, dependency, or escalation item.

---

# 6. Required Metadata From Stage 9

```text
Document ID
Title
Source category
Source owner
Approver
Business function / specialty
Product / batch / case / shipment applicability
Workflow applicability
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

---

# 7. Rule-to-Source Traceability Summary From Stage 9

```text
Identity/product-code and genealogy gates depend on product master, batch records, MES genealogy, warehouse consumption.
Unit-conversion, OOS/OOT and release-packet gates depend on lab results, interface mappings, OOS investigations, supplier audits, certificates and release packets.
PV intake, duplicate, clock, terminology, listedness and linkage gates depend on ICSR cases, duplicate candidates, safety receipts, adverse events/terminology versions, listedness sources, product labels, sensitive segments, product complaints and approved PV policies.
Supply and cold-chain gates depend on inventory, demand forecast, allocation constraints, shipments, temperature loggers, serialisation events, CMO capacity, supplier risks and approved supply/cold-chain policies.
Regulatory and authority gates depend on market authorisations, IDMP mappings, regulatory commitments, protocol versions/site approvals and approved regulatory policies.
Consent/entitlement gates depend on eConsent/secondary-use, privacy and users/entitlements sources.
AI-system-control gates depend on tool catalog, tool manifest, model registry, users/entitlements, access logs, audit trails, system/validation/spreadsheet inventories, downtime/network zones/continuity and approved AI boundary policies.
Auditability depends on non-negotiables, Stage 8 audit obligations and audit-trail/retention sources.
```

---

# 8. Regulated-Output and Patient/Patient-Participant-Facing Source Controls From Stage 9

```text
Consent/entitlement checks must pass before patient/participant data is surfaced, routed or shared.
Listedness and expectedness content must cite approved label, IB and core data sheet (CCDS) sources by version and jurisdiction.
Approved product labels are the regulated patient/HCP-facing source; any draft for release requires approval and approved-version citation.
Multilingual PV narratives require approved language/translation controls (Arabic, Hindi, English, German); unverified translation must not be released.
Release packets and QP-certification evidence packages are regulator-facing material assembled by accountable human roles.
Inspection-evidence packages must preserve traceability and must not create or hide evidence.
Every draft, review, approval, edit, release and delivery event must be auditable.
```

---

# 9. Access and No-Answer Rules From Stage 9

```text
Do not produce evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
Do not treat draft, expired, superseded, unapproved, quarantined or untrusted sources as authoritative.
Do not infer missing evidence.
Do not silently convert units, repair genealogy, confirm duplicates, set reporting clocks, pick listedness winners, or disposition OOS/OOT or cold-chain excursions.
Do not change inventory status, reserve capacity, allocate stock, ship product or initiate a recall without explicit authorised human approval.
Do not release or package regulated or patient-facing content without approval.
Do not treat derived workshop artifacts as controlled source records.
Do not treat any recommendation, draft, approval, override, release, escalation, action, outcome or closure as complete without audit evidence.
```

---

# 10. Audit Obligations From Stage 9

```text
Batch/product/case/shipment/source identity
Source evidence and provenance citation
Source owner / role
Source status and timestamp
Decision or action taken
Approval, rejection, or override where applicable
Override reason where applicable
Release/closure status where applicable
Escalation action and outcome where applicable
The 47-minute audit-capture gap and AI-off continuity state remain visible
```

---

# 11. Open Questions From Stage 9

```text
Who confirms each source owner and approver?
Which sources are approved and current versus excerpt-only, missing, draft, expired or untrusted?
Which sources are approved for regulated-output or patient/participant-facing use?
Which policy defines authority, effective date and jurisdiction per business object?
Which policy defines consent, entitlement, privacy and access boundaries?
Which evidence is required before a draft, approval, override, escalation, release or closure can be audited?
How are untrusted documents and manifests quarantined and disposed?
What is the approved multilingual PV narrative review process?
Who governs overrides and audit retention?
Which source gaps prevent safe evidence-backed workflow completion?
```

---

# 12. Stage 10 Working Constraint

Stage 10 must produce responsibility cards only. It must not create architecture, technical design, autonomous action design, or resolution of any batch, safety, quality or supply issue. Every card must clearly state forbidden actions and accountable human ownership, and must carry a fail-closed default.

Stage 10 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 11.
