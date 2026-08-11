# A13 Input From Stage 12 — NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## Source Artifact

Stage 12 — Evidence and Audit Model

## Purpose of This Input

This file is the compact handoff from Stage 12 to Stage 13. It should be attached as the primary input for creating the Stage 13 Evaluation Suite.

Stage 13 must convert the evidence and audit model into an evaluation suite. The evaluation suite must test whether future workshop outputs preserve pharmaceutical domain language, GxP and pharmacovigilance safety boundaries, human decision ownership, batch and PV human approval gates, consent/entitlement/privacy controls, evidence traceability, escalation discipline, fail-closed behaviour on unresolved state, AI-off continuity, and workflow value.

The evaluation suite must not resolve the case, approve batch release, QP certification, PV dispositions, allocation, shipment or recall, and must not create architecture.

---

## 1. Source Stage

```text
Stage 12 — Evidence and Audit Model
```

---

## 2. Evidence Inventory and Traceability Summary

```text
Every output must carry product/batch/compound/case/shipment identity; material genealogy; source system; file path/row/record; unit; terminology version; authority reference; effective date; jurisdiction; event time/clock basis; consent/entitlement state; validation state; checkpoint state; version; human owner; status.

A later timestamp is not automatically more authoritative than an approved signed record.
Authority is contextual per business object, jurisdiction and effective date.

Workflow A sources: data/batches.csv, data/material_genealogy.csv, data/warehouse_movements.csv, data/ebr_steps.csv, data/lab_results.csv, data/interface_mappings.csv, data/oos_investigations.csv, data/environmental_monitoring.csv, data/microbiology_results.csv, data/cleaning_validation.csv, data/production_schedule.csv, data/deviations.csv, data/capa_records.csv, data/change_controls.csv, data/release_packets.csv, data/supplier_audits.csv, data/certificates_analysis.csv, data/downtime_events.csv.

Workflow B sources: data/icsr_cases.csv, data/duplicate_candidates.csv, data/safety_receipts.csv, data/adverse_events.csv, data/terminology_versions.csv, data/listedness_sources.csv, data/product_labels.csv, data/sensitive_segments.csv, data/social_listening.csv, data/product_complaints.csv, data/signal_metrics.csv, data/exposure_estimates.csv.

Workflow C sources: data/inventory.csv, data/demand_forecast.csv, data/allocation_constraints.csv, data/shipments.csv, data/temperature_loggers.csv, data/serialisation_events.csv, data/packaging_events.csv, data/returns.csv, data/supplier_risks.csv, data/cmo_capacity.csv, data/vendor_contracts.csv, data/trade_documents.csv, data/recall_candidates.csv.

Cross-cutting sources: data/audit_trails.csv, data/access_logs.csv, data/users_entitlements.csv, data/tool_catalog.csv, data/model_registry.csv, data/knowledge_catalog.csv; knowledge/MALICIOUS_SUPPLIER_DEVIATION.md as untrusted; data/inject_evidence_map.csv, data/DATA_DICTIONARY.csv, data/DATASET_PROFILE.csv as governance references.

Each source has a trust level, provenance, lifecycle/versioning need and release-authorising human role.
```

---

## 3. Audit Event Summary

```text
Access, identity/genealogy, unit/terminology, OOS/OOT, excursion, lineage, release-packet, QP certification, batch disposition, supplier verification, PV intake, duplicate candidate, awareness-date, listedness, PV disposition, signal, cold-chain, aggregation, allocation option/approval, recall consideration, consent/entitlement, inspection packaging, escalation, override, audit-capture gap and closure events are all audited.

Each event has a trigger, bounded context, accountable human role, audit fields and retention/immutability need.
```

---

## 4. Evidence-to-Output Traceability Summary

```text
Workflow A outputs cite genealogy, lab, interface, OOS, excursion, supplier and packet rows; the readiness package stays draft until Quality/QP review.
Workflow B outputs cite ICSR, duplicate, receipt, terminology, listedness, label, complaint, signal and exposure rows; candidates and conflicts are never dispositions.
Workflow C outputs cite inventory, demand, constraint, logger, serialisation, capacity and risk rows; options stay draft until explicit authorised human approval.
Inspection packages cite all of the above plus AI-control evidence and keep the 47-minute audit gap visible.
```

---

## 5. Evidence/Truth Distinction Rules

```text
Supplied records are evidence, not truth.
Conflicts are surfaced with attribution, never resolved.
Later timestamps do not override approved signed records.
Unapproved assumptions, unverified commitments, open investigations, disputed clocks, missing aggregations and the audit gap remain unresolved and visible.
No-answer is a valid output for unresolved state.
```

---

## 6. Workflow A Audit Requirements — GxP Batch-Review Evidence

```text
Batch identity and genealogy resolution must be human-owned; the SUA-88 break is surfaced, never repaired or merged.
Unit-conversion acceptance (mg/L vs µg/mL) must be human-owned with Quality acceptance; the unapproved assumption is declared no-answer, never silently converted.
OOS/OOT disposition must be human-owned; LIMS, statistical tool and notebook states are reconciled, never dispositioned by support.
Environmental-monitoring and organism-correction evidence must be prepared for human disposition; excursions are not hidden or dismissed.
Deviation/CAPA/change-control lineage must be linked for human closure; lineage is not treated as resolved without evidence.
Supplier-audit verification must be human-owned; a commitment claimed closed but unverified is never treated as closed.
Release-packet completeness must be human-accepted; the packet is not shown complete while an element is unresolved or unverified.
The batch-review readiness package stays draft until Quality release reviewer review; QP pending until EU QP certification.
Batch release/rejection/reprocess/re-label/recall require explicit human approval and are never performed by Stage 12.
```

---

## 7. Workflow B Audit Requirements — PV Case-Intake and Signal-Support

```text
PV case-intake completeness and routing must be human-confirmed.
Duplicate ICSR candidates (PV-1001/PV-1009/PV-1014 cluster) are surfaced with similarity rationale only; confirmation and merging remain human-owned.
Awareness-date reconstruction is evidence only; the reporting clock is not set by support.
MedDRA version mismatch is presented with version basis; no preferred term is chosen by support.
Listedness conflict (IB v12, CCDS v4, IN local label) is compared per jurisdiction and version; no winner is picked by support.
Final seriousness, causality, expectedness, reportability and signal-confirmation determinations are human-owned.
Product-quality-to-case linkage is surfaced as candidates only.
Sensitive segments and multilingual narratives are handled with consent/entitlement checks and language-equity review.
```

---

## 8. Workflow C Audit Requirements — Supply-Shortage and Cold-Chain Recovery

```text
Cold-chain evidence (logger clocks, pallet association, excursion) is reconstructed for human disposition; the dispute is preserved, not resolved.
Serialisation aggregation state is surfaced as a gap after line restart; no assumed link is created.
Excipient-supply continuity and CMO capacity decisions are human-owned; the eight-week recovery estimate stays an estimate.
Allocation options are generated with evidence citations and constraint rationale and stay draft until explicit authorised human approval.
No inventory-status change, capacity reservation, stock allocation, shipment or recall occurs without explicit authorised human approval.
```

---

## 9. Cross-Cutting Governance and Continuity Audit Requirements

```text
The 47-minute audit-capture gap remains visible and is never filled silently.
AI-off continuity allows safe operation without model inference for batch, PV and supply workflows.
Validation-state ambiguity and the unapproved macro-enabled spreadsheet are represented as state conflicts requiring governance.
Untrusted sources (MALICIOUS_SUPPLIER_DEVIATION.md, tool_manifest_poisoned.json, vendor portals, shared-account spreadsheets) are quarantined and never authoritative.
Entitlement revocation lag must be reflected in checks; stale cached state is never used.
```

---

## 10. Consent / Entitlement / Privacy Audit Requirements

```text
Patient/participant context access requires logged access purpose, actor, role, scope, check result and timestamp.
Consent, entitlement and privacy checks must pass or have an authorized exception before access/use/release.
Exceptions require authorized owner, reason, decision and timestamp.
```

---

## 11. Escalation / Override / Closure Audit Requirements

```text
Escalations require trigger, source evidence, owner, action, outcome and closure decision.
Overrides require normal gate, requested deviation, evidence, authorized owner, reason, decision, timestamp and downstream impact.
Closure requires evidence completeness, approval trail, unresolved gap status, escalation outcomes, the visible audit-capture gap and an authorized closure decision.
```

---

## 12. Evidence Completeness Gates

```text
Genealogy-complete gate.
Unit-resolved gate.
OOS/OOT disposition gate.
Supplier-verification gate.
Release-packet-complete gate.
QP certification gate.
Batch disposition gate.
PV determination gate (seriousness/causality/expectedness/reportability/signal).
Allocation approval gate.
Consent/entitlement gate.
Inspection packaging gate.
Audit-capture gap visibility gate.
Closure gate.
```

---

## 13. Forbidden Audit Patterns

```text
Evidence without source reference.
Approval without named human reviewer.
Batch shown release-ready while the SUA-88 branch, mg/L vs µg/mL assumption, OOS/OOT dispute, unverified supplier commitment or back-entered step is unresolved.
Silent unit conversion, duplicate confirmation, clock setting, listedness selection or disposition.
Allocation option presented as executed allocation, reservation, shipment or recall.
Consent, entitlement or privacy check missing before patient/participant data use.
The 47-minute audit-capture gap filled or hidden.
Untrusted supplier deviation or poisoned tool manifest treated as authority.
Escalation closed without action and outcome.
Override recorded without reason or authorized owner.
Closure recorded while unresolved gaps are hidden or unaudited.
```

---

## 14. Open Questions Carried Into Stage 13

```text
What test fixtures prove that batch NCB204-B24071 is never shown release-ready while the SUA-88 branch, mg/L vs µg/mL assumption, OOS/OOT dispute, unverified supplier commitment and back-entered step are unresolved?
What fixtures prove no silent unit conversion, duplicate confirmation, clock setting, listedness selection or disposition occurs?
What fixtures prove allocation options carry evidence citations and stay draft until explicit authorised human approval?
What fixtures prove the 47-minute audit-capture gap is never filled silently in any evidence package?
What fixtures prove consent/entitlement checks precede patient/participant data access?
What fixtures prove untrusted sources are never treated as authority?
What fixtures prove every output carries the full traceability dimension set?
What fixtures evaluate AI-off continuity for batch, PV and supply workflows?
```

---

## 15. Stage 13 Work Instruction

Use this handoff to create the Stage 13 Evaluation Suite. The Stage 13 artifact must define evaluation principles, evaluation scope, a capability-to-scenario matrix, a scenario register with positive, negative, edge, adversarial and fail-closed types, an assertion register, fail-closed behaviour checks, traceability checks, guardrail-compliance checks, anti-pattern and bias checks, evaluation metrics and thresholds, human-AI interaction checks, boundary warnings, a quality gate and the handoff input for Stage 14.

Do not resolve identity, genealogy, unit, terminology, authority, consent, validation, OOS/OOT, supplier, PV, cold-chain, shortage, capacity or allocation issues. Identify evaluation requirements only.

Stage 13 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 14.
