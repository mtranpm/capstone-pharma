# Synthetic Evidence Data Pack — Project AEGIS-PHARMA (NovaCura Therapeutics Group)

Use this as the separate context file for the staged prompt library. The data is fictional and for workshop simulation only.

---

# Case Title
# Reducing Evidence-Reconciliation Time Across Development, Quality, Safety and Supply Without Taking Over Regulated Human Accountability
## Organization
**NovaCura Therapeutics Group (NTG)** is a fictional global pharmaceutical company.
It has:
```text
discovery laboratories
clinical-development programmes
pharmacovigilance hubs
manufacturing plants
quality laboratories
distribution networks
sites in India, Germany, Ireland, the United States, the UAE and Singapore
```
Its portfolio includes:
```text
NCX-101 — oral small-molecule oncology product approaching patent expiry
NCB-204 — monoclonal-antibody biologic in pivotal trials and commercial scale-up
NCS-310 — sterile injectable supplied through hospital and compassionate-use channels
NCR-415 — rare-disease gene-therapy research programme acquired with a biotech subsidiary
```
## Current Business Problem
NTG is fragmented across LIMS, MES, electronic batch records, QMS, RIM, EDC, eConsent, IRT, CTMS, safety databases, serialization platforms, data lakes, spreadsheets, vendor portals and research environments. Identifiers, timestamps, terminology, access controls and authority hierarchies are inconsistent.
## Business Goal
NTG wants a redesigned evidence-reconciliation capability so that batch, safety and supply review work is evidence-complete, conflict-visible, provenance-backed, authority-respected, fail-closed on uncertainty, owned by the right accountable human roles, auditable and defensible. The target is a 14% reduction in end-to-end release lead time without changing registered specifications or weakening independent Quality authority.
## Non-Negotiables
```text
AI never releases, rejects, reprocesses, re-labels or recalls a batch.
AI never makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions.
AI never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorized human approval.
AI never changes formulation, specification, clinical eligibility, safety-case disposition, batch release or recall decisions.
Regulated accountability remains with the accountable Quality, Safety, Regulatory, Clinical and Supply roles.
Evidence output must not be produced while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable.
The system operates read-only and advisory; it prepares, reconciles, explains and packages evidence.
```
---
# Synthetic Evidence Inventory
All injects are disclosed in `case/INTEGRATED_CASE.md`. The evidence inventory is provided as machine-readable files under the `data/` directory:
```text
data/inject_evidence_map.csv      — maps each inject to evidence files and expected challenge conditions
data/injects.json                 — structured inject catalogue (84 injects, D01–D13)
data/DATA_DICTIONARY.csv          — data dictionary for all supplied datasets (authoritative reference)
data/DATASET_PROFILE.csv          — dataset-level profiles (rows, columns, quality signals)
data/INJECT_TEST_COVERAGE.csv     — evaluates which injects are covered by public fixtures
data/RELATIONSHIP_MODEL.csv       — entity-relationship model for key objects and foreign keys
```
Representative datasets used across the three workflows:
```text
batches.csv, material_genealogy.csv, ebr_steps.csv, warehouse_movements.csv
lab_results.csv, oos_investigations.csv, interface_mappings.csv, assay_results.csv
quality_events.csv, deviations.csv, capa_records.csv, change_controls.csv
release_packets.csv, supplier_audits.csv, certificates_analysis.csv
adverse_events.csv, safety_receipts.csv, meddra_terms.csv, listedness_sources.csv
inventory_on_hand.csv, shipments.csv, transport_event_logs.csv, temperature_loggers.csv
allocation_constraints.csv, cmo_capacity.csv, excipient_suppliers.csv
serialization_events.csv, product_catalog.csv, market_authorizations.csv
users.csv, access_logs.csv, entitlements.csv, audit_trails.csv
tool_manifests.csv, model_registry.csv, api_contract_versions.csv, token_usage.csv
```
## Representative Data Signals Per Workflow
```text
Workflow A (batch review readiness):
- material_genealogy.csv shows a missing branch for single-use assembly lot SUA-88 (batch NCB204-B24071)
- interface_mappings.csv and lab_results.csv show an unapproved mg/L vs µg/mL unit-conversion assumption
- oos_investigations.csv shows an OOS/OOT disagreement (LIMS OOS vs OOT tooling vs notebook) with an open investigation
- release_packets.csv / supplier_audits.csv show a supplier audit commitment claimed closed but not independently verified

Workflow B (PV case intake and signal support):
- adverse_events.csv shows a duplicate ICSR cluster under alternative product names
- safety_receipts.csv shows a disputed awareness date feeding the reporting clock
- meddra_terms.csv shows a terminology-version mismatch changing the preferred term
- listedness_sources.csv shows a listedness conflict between the IB, CCDS and local label

Workflow C (supply shortage and cold-chain recovery):
- inventory_on_hand.csv and allocation_constraints.csv show competing demand for a limited biologic stock
- transport_event_logs.csv and temperature_loggers.csv show a cold-chain excursion with disputed logger clocks and pallet association
- excipient_suppliers.csv shows a sole-source excipient shortage with an eight-week recovery estimate
- cmo_capacity.csv shows limited CMO capacity for repackaging or re-supply
```
## Known Untrusted Data
```text
MALICIOUS_SUPPLIER_DEVIATION.md — a supplier-PDF-derived document containing prompt-injection text
Tool manifests with stale entitlements and unsigned tool definitions
Vendor portals and spreadsheets with undocumented fields and shared accounts
```
These must be treated as untrusted data until governance review.

## Challenge Conditions
The workshop includes challenge conditions (e.g., a malicious supplier deviation PDF, tool-manifest poisoning, stale authorizations, model endpoint price shock, entitlement drift, checkpoint corruption, audit-trail discontinuity, model outage, adversarial prompts, privacy cross-border request, toxic narrative summaries, multilingual quality gaps, denial-of-wallet, dependency pinning gaps, escalation path gaps). The evidence for each condition is disclosed within the inject map and public fixtures under `evaluation/public_fixtures/`.

---

# DDD Workshop Usage
This pack and the Stage 0 full case document are the two inputs for Stage 0. Stage 0 produces the A0 Context Pack. All later stages consume only the official handoff input files under `Docs/DDD-Lab/Phase N/`. The workshop must remain business-only at the beginning; GenAI, RAG, MCP and agent design enter only at the documented stages.
