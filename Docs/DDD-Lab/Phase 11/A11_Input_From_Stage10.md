# A11 Input From Stage 10 — Agent Responsibility Cards

Use this file as the direct input attachment for **Stage 11 — Human Decision Ownership Matrix**.

This input is derived from the completed Stage 10 artifact for the **NovaCura Therapeutics Group (Project AEGIS-PHARMA)** pharmaceutical evidence-reconciliation case.

---

## Source Stage

```text
Stage 10 — Agent Responsibility Cards
```

## Target Stage

```text
Stage 11 — Human Decision Ownership Matrix
```

## Stage 11 Purpose

Stage 11 must convert the Stage 10 bounded responsibility cards into a clear human decision ownership model. The goal is to identify which human role is responsible, which human role is accountable, which support role may prepare evidence or drafts, what approval is required, what evidence must be available, when work must stop or escalate, and what must be audited.

The output must preserve regulated Quality, Safety, Regulatory, Clinical and Supply accountability, the read-only advisory boundary, consent/entitlement/privacy boundaries, and full auditability. It must not resolve any batch, safety, quality or supply issue, must not approve batch release, rejection, reprocess, re-label or recall, must not make final PV decisions, and must not approve inventory-status change, capacity reservation, stock allocation, shipment or recall initiation.

---

# 1. Case Context

NovaCura Therapeutics Group (NTG) is a fictional global pharmaceutical company operating discovery laboratories, clinical-development programmes, pharmacovigilance hubs, manufacturing plants, quality laboratories and distribution networks across India, Germany, Ireland, the United States, the UAE and Singapore. Portfolio: NCX-101 (oral small-molecule oncology near patent expiry), NCB-204 (monoclonal-antibody biologic in pivotal trials and commercial scale-up), NCS-310 (sterile injectable), NCR-415 (rare-disease gene-therapy research programme). The estate is fragmented across LIMS, MES, electronic batch records, QMS, RIM, EDC, eConsent, IRT, CTMS, safety databases, serialisation platforms, data lakes, spreadsheets and vendor portals. No system is universally authoritative; authority is contextual per business object, jurisdiction and effective date, and a later timestamp is not automatically more authoritative than an approved signed record.

The active scenario is the disputed biologics batch NCB204-B24071 (missing single-use assembly lot SUA-88 genealogy branch, mg/L vs µg/mL unit assumption, disputed OOS/OOT state, unverified contract-site audit commitment, back-entered batch-record step), the emerging safety reports (duplicate ICSR candidates under different product names, disputed awareness date, MedDRA version mismatch, IB/CCDS/local-label listedness conflict), the cold-chain failure (disputed logger clocks and pallet association, missing case-to-pallet aggregation), the sole-source excipient shortage with CMO capacity conflict and demand exceeding stock, the ransomware event with a 47-minute audit-capture gap, and the multi-agency inspection request within 72 hours.

---

# 2. Stage 10 Responsibility Cards Created

Stage 10 created the following bounded responsibility cards:

```text
ARC-001 Batch Evidence Reconciler
ARC-002 Genealogy and Identity Verifier
ARC-003 Unit and Terminology Normaliser
ARC-004 Release-Packet Compiler
ARC-005 Supplier-Audit Evidence Verifier
ARC-006 PV Case Intake Assistant
ARC-007 Duplicate-Candidate Detector
ARC-008 Reporting-Clock Reconstructor
ARC-009 Listedness Evidence Retriever
ARC-010 Product-Quality Linkage Checker
ARC-011 Supply Recovery Option Analyst
ARC-012 Cold-Chain Evidence Reconstructor
ARC-013 Allocation Constraint Checker
ARC-014 Inspection Evidence Packager
ARC-015 Evidence and Audit Recorder
```

These cards define support responsibilities only. They do not own batch release, QP certification, final PV decisions, allocation, shipment, recall, consent/entitlement override, or closure.

---

# 3. Human Owners Identified From Stage 10

```text
QP certification (final batch certification): EU Qualified Person
Batch release / rejection / reprocess / re-label / recall: EU Qualified Person / Quality release reviewer; Quality/Regulatory roles for recall
OOS/OOT disposition and investigation conclusion: Laboratory analyst / OOS owner
Unit-conversion acceptance (mg/L vs µg/mL): Laboratory / interface owner with Quality acceptance
Supplier-audit verification and commitment closure: Supplier-quality / quality reviewer
Batch identity/genealogy resolution (SUA-88): Identity / genealogy / master-data owner
Final PV seriousness, causality, expectedness, reportability: PV medical/safety reviewer
Signal confirmation: Signal management
Duplicate confirmation: PV reviewer
Awareness-date acceptance: PV case-intake staff / PV reviewer
Listedness determination per jurisdiction/source: PV medical reviewer / Regulatory Affairs
Inventory status change, capacity reservation, stock allocation, shipment, recall initiation: Supply Chain VP / authorised Quality owner
Cold-chain excursion disposition: Logistics / cold-chain accountable owner with Quality input
Formulation, specification, clinical eligibility or safety-case disposition changes: accountable Quality/Clinical/Safety roles
Consent/entitlement exception handling: Data Protection Officer / privacy owner
Exception override: authorized human owner
Case/escalation closure: accountable workflow owner
```

Where the exact named organizational role is not present in the case, Stage 11 must mark it as **role to be assigned**, not invent a new role.

---

# 4. Approval Requirements From Stage 10

```text
Batch-review readiness conclusion requires Quality release reviewer review and EU QP certification; the batch must not be shown release-ready with unresolved or unverified elements.
QP certification and batch release/rejection/reprocess/re-label/recall decisions require EU QP / Quality release reviewer approval.
OOS/OOT disposition requires laboratory analyst / OOS owner disposition.
Unit-conversion acceptance requires laboratory / interface owner approval with Quality acceptance.
Supplier-audit commitment closure requires supplier-quality verification.
Allocation approval requires Supply Chain VP / authorised Quality owner approval; no inventory status change, capacity reservation, stock allocation, shipment or recall without explicit authorised human approval.
Cold-chain excursion disposition requires logistics / cold-chain accountable owner with Quality input.
Overrides require authorized owner and reason.
Closure requires unresolved gaps to be resolved, escalated, owned, or explicitly documented.
```

---

# 5. Forbidden Actions From Stage 10

```text
Automated batch release / rejection / reprocess / re-label / recall
Automated QP certification
Automated final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions
Automated duplicate confirmation
Automated reporting-clock setting
Automated listedness-winner selection
Automated OOS/OOT or cold-chain excursion disposition
Automated inventory status change, capacity reservation, stock allocation, shipment or recall initiation
Automated consent, entitlement or privacy override
Automated exception override without authorized owner and reason
Automated case/escalation closure while unresolved gaps are hidden or unaudited
Inventing missing source content, product, batch, safety, quality or supply facts
Treating a later timestamp as automatically more authoritative
```

---

# 6. Evidence Requirements From Stage 10

```text
Product, batch, compound, case, shipment and source identity
Genealogy records (MES genealogy, warehouse consumption, eBR steps)
Laboratory results, interface mappings, OOS investigations
Environmental monitoring and microbiology results
Deviations, CAPA, change-control and cleaning-validation records
Release packets, supplier audits, certificates of analysis
ICSR cases, duplicate candidates, safety receipts, adverse events, terminology versions, listedness sources, product labels, sensitive segments, social listening, product complaints, signal metrics, exposure estimates
Inventory, demand forecast, allocation constraints, shipments, temperature loggers, serialisation events, packaging events, returns, supplier risks, CMO capacity, vendor contracts, trade documents, recall candidates
Market authorisations, IDMP mappings, regulatory commitments, protocol versions, site approvals
Audit trails, downtime events, continuity requirements, users/entitlements, tool catalog, model registry, knowledge catalog
Non-negotiables
Stage 8 rules and gates
Stage 9 source register and metadata requirements
Stage 10 responsibility cards
```

---

# 7. Stop and Escalation Conditions From Stage 10

```text
Missing or unresolved identity, genealogy (SUA-88 break), unit (mg/L vs µg/mL), terminology (MedDRA version), authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state
Disputed OOS/OOT state with open investigation
Unverified supplier-audit commitment in the release packet
Back-entered batch-record step without checkpoint evidence
Duplicate ICSR candidates not confirmed
Disputed awareness date
MedDRA version mismatch or listedness-source conflict
Disputed cold-chain logger clocks, pallet association or missing aggregation
Sole-source excipient shortage, CMO capacity conflict, demand exceeding stock
47-minute audit-capture gap
Multi-agency inspection request within 72 hours
Missing audit trail
```

---

# 8. Audit Obligations From Stage 10

```text
Source access and source status checks
Product/batch/case/shipment/participant linkage
Drafts, summaries, comparisons, readiness packages and evidence packages created
Human review requests
Human edits
Approvals, rejections, and overrides
Override owner and reason
Escalations, actions, outcomes, and closures
Batch-release and QP-pending status
PV disposition and case routing records
Allocation approval requests and approvals
Inspection evidence package manifest
The 47-minute audit-capture gap and AI-off continuity state
Closure evidence
```

---

# 9. Known Unresolved Case Gaps

```text
Genealogy is incomplete for batch NCB204-B24071 (missing single-use assembly lot SUA-88 branch; warehouse consumption contradicts MES).
Unit convention for contract-laboratory concentration (mg/L vs µg/mL) is unapproved and inconsistent.
OOS/OOT state for an assay is disputed across LIMS, statistical tooling and the laboratory notebook, with an open investigation.
EU release packet lacks confirmation of one contract-site audit commitment.
A batch-record step was back-entered after network degradation.
Duplicate ICSR candidates exist under different product names (PV-1001, PV-1009, PV-1014).
The awareness date is disputed across vendor receipt, affiliate inbox and global safety DB.
Two MedDRA versions change the preferred term.
Listedness conflicts across IB v12, CCDS v4 and the IN local label.
Cold-chain logger clocks and pallet association are disputed; case-to-pallet aggregation is missing after a line restart.
Sole-source excipient contamination with an eight-week recovery estimate; CMO promises capacity to two sponsors; demand exceeds stock.
47-minute audit-capture gap during master-data repair.
Validation state is ambiguous for at least one application; an unapproved macro-enabled spreadsheet is in use.
Pivotal-trial amendment not approved in one country; protocol, consent and data-collection versions are asynchronous.
Evidence and approval trail must be complete and defensible under a 72-hour multi-agency inspection.
```

---

# 10. Required Stage 11 Output

Stage 11 must produce:

```text
Human decision ownership boundary
Decision inventory
RACI-style ownership matrix
Approval gate matrix
Batch and Quality decision ownership model
Pharmacovigilance decision ownership model
Supply, cold-chain and allocation decision ownership model
Regulatory, consent and inspection decision ownership model
Escalation and override ownership model
Audit responsibility model
Forbidden decision list
Open ownership questions
NEXT_STAGE_INPUT_BLOCK for Stage 12
```

---

# 11. Quality Gate for Stage 11

Stage 11 is acceptable only if:

```text
Every batch, safety, quality, regulatory, clinical or supply decision has a named or explicitly-to-be-assigned accountable human owner.
No support role owns batch release, QP certification, final PV decisions, allocation, shipment or recall.
No support role disposes OOS/OOT, cold-chain excursions, duplicates, awareness dates or listedness.
No support role overrides consent, entitlement or privacy controls.
Every exception has an owner, evidence requirement, escalation path, and audit event.
Every approval, rejection, override, release, escalation, outcome, and closure is auditable.
Unresolved batch, safety, quality and supply issues are identified as workflow/domain gaps only, not resolved.
```
