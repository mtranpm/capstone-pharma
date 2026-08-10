# A1 — Input From Stage 0: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

Use this file as the dedicated input attachment for Stage 1 — Business Problem Framing.

This file is extracted from the Stage 0 Context Pack (`Docs/DDD-Lab/Phase 0/A0_Context_Pack.md`). It is intentionally limited to business-domain context. It does not solve the case, does not provide medical, regulatory or legal advice, and does not introduce architecture or technical implementation.

---

## Stage 1 Input — Business Problem Framing

### Final Business Challenge

NovaCura Therapeutics Group needs a redesigned evidence-reconciliation capability so that batch-review, pharmacovigilance and supply-recovery work is evidence-complete, conflict-visible, provenance-backed, authority-respected, fail-closed on uncertainty, owned by the right accountable human roles, auditable and defensible — reducing evidence-reconciliation time (board target: 14% end-to-end release lead-time reduction) without changing registered specifications, weakening independent Quality authority, or taking over regulated human accountability.

### Mandatory Workflows

- **Workflow A — GxP evidence reconciliation for batch-review readiness:** reconcile batch genealogy, laboratory results, environmental monitoring, deviations, CAPA, change control, validation state, supplier evidence and release-packet completeness. It may identify gaps, contradictions and evidence lineage. It must never release, reject, reprocess, re-label or recall a batch.
- **Workflow B — Pharmacovigilance case-intake and signal-support:** support intake, duplicate detection, terminology normalisation, source authority, reporting-clock reconstruction, listedness evidence, product-quality linkage and multilingual review. It must never make final seriousness, causality, expectedness, reportability or signal-confirmation decisions.
- **Workflow C — Bounded supply-shortage and cold-chain recovery planner:** generate traceable options using inventory, quality status, market authorisation, trial demand, compassionate-use constraints, cold-chain evidence, CMO capacity, transport and allocation policy. It must never change inventory status, reserve capacity, allocate stock, release product or initiate a recall without explicit authorised human approval.

### Representative Scenario Summary

During the capstone window, a pivotal-trial amendment, a disputed biologics batch, emerging safety reports, a sterile-area excursion, a cold-chain failure, an excipient shortage, a ransomware event and a multi-agency inspection request converge:

- **Pivotal-trial amendment:** sites execute multiple protocol versions and one country has not approved the latest amendment; protocol, consent and data-collection versions are asynchronous; clocks differ across decentralised devices.
- **Disputed biologics batch NCB204-B24071:** single-use assembly lot SUA-88 is missing from one MES genealogy branch but appears in warehouse consumption; a contract laboratory concentration is transmitted in mg/L while the receiving interface assumes µg/mL; LIMS marks an assay OOS while the statistical tool marks it OOT and the laboratory notebook labels it invalid; the EU release packet lacks confirmation of one contract-site audit commitment; a required batch-record step was back-entered after network degradation.
- **Sterile-area excursion:** environmental monitoring shows an excursion near fill-finish and the organism identification was corrected after initial review; campaign sequencing changed after a high-potency product was introduced.
- **Emerging safety reports:** cases from a patient programme, literature vendor and call centre likely describe the same event under different product names; the awareness date differs across vendor receipt, affiliate inbox and global safety database; coding used two MedDRA versions changing the preferred term; the investigator brochure, core data sheet and local label are not aligned on expectedness.
- **Cold-chain failure:** a biologic shipment exceeds range and logger clocks and pallet association are disputed; case-to-pallet aggregation is missing after a line restart.
- **Excipient shortage:** a sole-source excipient supplier reports contamination with an eight-week recovery estimate; a CMO promises capacity to two sponsors in the same window; demand exceeds available stock across markets, trials and compassionate-use programmes.
- **Ransomware event:** manufacturing historians are isolated while MES and QMS operate in degraded mode; audit capture was disabled for 47 minutes during master-data repair; the organisation must operate safely without AI inference.
- **Multi-agency inspection request:** regulators request traceable evidence spanning trial data, batch history, safety cases and AI-system controls within 72 hours.

### Business Goals

- Ensure batch, safety and supply review work is evidence-complete.
- Ensure conflicts are visible rather than silently reconciled.
- Ensure provenance is backed by attributable evidence.
- Ensure the right authority is respected per business object, jurisdiction and effective date.
- Ensure the capability fails closed on uncertainty.
- Ensure the right accountable human roles own the right decisions.
- Ensure every recommendation, draft, approval, override, release, escalation, action, outcome and closure is auditable.
- Achieve a 14% reduction in end-to-end release lead time without changing registered specifications or weakening independent Quality authority.

### Non-Negotiables

- The AI never releases, rejects, reprocesses, re-labels or recalls a batch.
- The AI never makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions.
- The AI never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval.
- The AI never changes formulation, specification, clinical eligibility, safety-case disposition, batch release or recall decisions.
- Regulated accountability remains with the accountable Quality, Safety, Regulatory, Clinical and Supply roles.
- Evidence output must not be produced while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
- Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable.
- The system operates read-only and advisory; it prepares, reconciles, explains and packages evidence.

### Available Evidence

- Organization profile
- Business problem statement
- Business goal statement
- Non-negotiables
- Stakeholder pack (mandates, incentives, concerns, decision authority)
- Source-system fact pack (domain systems and known conditions)
- Regulatory and standards boundary pack
- Integrated case with inject catalogue (INJ-001 to INJ-084 across D01–D13)
- Synthetic evidence inventory (`data/inject_evidence_map.csv`, `data/injects.json`, `data/DATA_DICTIONARY.csv`, `data/DATASET_PROFILE.csv`, `data/INJECT_TEST_COVERAGE.csv`, `data/RELATIONSHIP_MODEL.csv`)
- Representative datasets per workflow (batch, genealogy, lab, OOS, quality, release packet, safety, cold-chain, inventory, allocation, CMO, supplier)
- Known untrusted data (malicious supplier deviation PDF, tool manifests, vendor portals and shared-account spreadsheets)

### Known Gaps and Exceptions

- Authority hierarchy is inconsistent across systems; no system is universally authoritative and a later timestamp is not automatically more authoritative than an approved signed record.
- Genealogy is incomplete for batch NCB204-B24071 (missing single-use assembly lot SUA-88 branch).
- Unit convention for contract-laboratory concentration (mg/L vs µg/mL) is unapproved and inconsistent.
- OOS/OOT state for an assay is disputed across LIMS, statistical tooling and the laboratory notebook, with an open investigation.
- A supplier-audit commitment is claimed closed but not independently verified in the release packet.
- A required batch-record step was back-entered after network degradation; audit capture was disabled for 47 minutes.
- Reporting-clock reconstruction is disputed for an ICSR awareness date; duplicate ICSR candidates exist under alternative product names; MedDRA version mismatch and listedness-source conflict are unresolved.
- Cold-chain logger clocks and pallet association are disputed; serialisation aggregation is missing after a line restart.
- Sole-source excipient shortage with an eight-week recovery estimate, CMO capacity conflict and competing demand beyond available stock are unresolved.
- Validation state is ambiguous for at least one application; an unapproved macro-enabled spreadsheet is in use.
- Untrusted documents and manifests (prompt-injection PDF, stale/unsigned tool manifests, undocumented shared-account spreadsheets) must be governed before use.

### Open Questions

- Which business area owns batch-review readiness closure?
- Which roles own PV case-intake completeness and reporting-clock reconstruction?
- Which roles own supply-recovery option selection and any allocation recommendation?
- What is the escalation path when evidence is incomplete or conflicting?
- How are authority and effective date determined per business object and jurisdiction?
- How is regulated human accountability preserved in every workflow while AI remains advisory?
- What evidence must exist before any recommendation or draft is produced?
- What must be documented for any human override?
