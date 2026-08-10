# A9 Input From Stage 8 — Rules vs Reasoning Matrix

Use this file as the direct input attachment for **Stage 9 — Governed RAG Source Register**.

This input is derived from the completed Stage 8 artifact for the **NovaCura Therapeutics Group** pharmaceutical evidence-reconciliation case (Project AEGIS-PHARMA).

---

## Source Stage

```text
Stage 8 — Rules vs Reasoning Matrix
```

## Target Stage

```text
Stage 9 — Governed RAG Source Register
```

## Stage 9 Purpose

Stage 9 must identify the governed business, quality, safety, regulatory and supply sources that can support evidence-backed batch-review, pharmacovigilance and supply-recovery work. The goal is not to design architecture or implementation. The goal is to create a source governance register that clarifies:

```text
authoritative sources
batch, product and safety evidence
policy, SOP and standard sources
source ownership
approval and validation status
regulated-output and patient/participant-facing suitability
access boundaries
required metadata
evidence gaps
no-answer / no-output conditions
audit expectations
```

The output must preserve regulated human accountability, remain read-only and advisory, and must not resolve any batch, safety, quality or supply issue.

---

# 1. Case Context

NovaCura Therapeutics Group (NTG) is a fictional global pharmaceutical company operating discovery laboratories, clinical-development programmes, pharmacovigilance hubs, manufacturing plants, quality laboratories and distribution networks across India, Germany, Ireland, the United States, the UAE and Singapore. Portfolio: NCX-101 (oral small-molecule oncology near patent expiry), NCB-204 (monoclonal-antibody biologic in pivotal trials and commercial scale-up), NCS-310 (sterile injectable), and NCR-415 (rare-disease gene-therapy research programme).

The enterprise estate is fragmented across LIMS, MES, electronic batch records, QMS, RIM, EDC, eConsent, IRT, CTMS, safety databases, serialisation platforms, data lakes, spreadsheets and vendor portals. No system is universally authoritative; authority is contextual per business object, jurisdiction and effective date, and a later timestamp is not automatically more authoritative than an approved signed record.

The active scenario converges on: a pivotal-trial amendment (multiple protocol versions, one country not approved); the disputed biologics batch NCB204-B24071 (missing single-use assembly lot SUA-88 in the MES genealogy branch but present in warehouse consumption; contract-lab concentration in mg/L while the receiving interface assumes µg/mL; LIMS OOS, statistical tool OOT, notebook invalid; EU release packet lacking confirmation of a contract-site audit commitment; a batch-record step back-entered after network degradation); a sterile-area environmental excursion near fill-finish with a corrected organism identification; emerging safety reports (duplicate ICSR cluster under different product names; disputed awareness date across vendor receipt, affiliate inbox and global safety DB; two MedDRA versions changing a preferred term; listedness conflict between IB, core data sheet and local label); a cold-chain failure (disputed logger clocks and pallet association; missing case-to-pallet aggregation after a line restart); an excipient shortage (sole-source supplier contamination, eight-week recovery, CMO capacity promised to two sponsors, demand exceeding stock); a ransomware event (manufacturing historians isolated, MES/QMS degraded, 47-minute audit-capture gap during master-data repair, safe operation required without AI inference); and a multi-agency inspection request within 72 hours.

---

# 2. Final Rules vs Reasoning Summary From Stage 8

Stage 8 separates NovaCura's batch-review, PV case-intake and supply-recovery work into deterministic rules, workflow gates, human-owned decisions, support-only activities, forbidden actions and audit obligations. The case remains unresolved. The artifact only defines how decisions and workflow gaps must be governed, with regulated accountability preserved for Quality, Safety, Regulatory, Clinical and Supply roles.

---

# 3. Deterministic Rules From Stage 8

```text
Evidence output requires resolved product/batch/compound identity.

Genealogy completeness must be checked before batch evidence output; all branches present and linked.

A batch must not be shown as release-ready while any genealogy branch or release-packet element is unresolved or unverified.

Unit-conversion consistency must be resolved before output (mg/L vs µg/mL).

Identity/product-code match check.

Disputed OOS/OOT/notebook-invalid result state remains open and visible.

Unverified supplier-audit commitments are not treated as closed.

Back-entered batch-record steps require checkpoint and audit evidence.

Validation-state consistency must be checked before evidence output.

Entitlement/consent gate must pass before patient/participant data is surfaced.

Checkpoint-state completeness check before evidence output.

Required release-packet element completeness check.

MedDRA version consistency must be resolved before terminology output.

Duplicate-ICSR candidate similarity check surfaces candidates only.

Reporting-clock reconstruction inputs must be complete.

The audit-capture gap remains visible and is not filled silently.

Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable.
```

---

# 4. Human-Owned Decisions From Stage 8

```text
Batch release / rejection / reprocess / re-label: EU Qualified Person / Quality release reviewer.

QP certification: EU Qualified Person.

OOS/OOT disposition and investigation conclusion: Laboratory analyst / OOS owner.

Unit-conversion acceptance: Laboratory / interface owner with Quality acceptance.

Supplier-audit verification and commitment closure: Supplier-quality / quality reviewer.

Batch identity/genealogy resolution: Identity / genealogy / master-data owner.

PV seriousness, causality, expectedness, reportability determinations: PV medical/safety reviewer.

Duplicate confirmation: PV reviewer.

Awareness-date acceptance: PV case-intake staff / PV reviewer.

Listedness determination per jurisdiction/source: PV medical reviewer / Regulatory Affairs.

Signal confirmation: Signal management.

Allocation decision: Supply Chain VP / authorised Quality owner.

Cold-chain excursion disposition: Logistics / cold-chain accountable owner with Quality input.

Recall decision: Quality / Regulatory accountable roles.

Exception override: authorized human owner.

Case/escalation closure: accountable workflow owner.
```

---

# 5. Support-Only Activities From Stage 8

```text
Reconcile batch genealogy and surface genealogy breaks with ownership.

Surface unit-conversion conflicts and declare no-answer.

Reconcile LIMS, statistical tool and notebook states without disposition.

Prepare environmental-excursion and organism-correction evidence.

Link deviation, CAPA, change control and cleaning-validation evidence.

List release-packet elements and evidence gaps.

Present supplier-audit commitment status.

Prepare the QP-certification evidence package.

Surface duplicate candidates, clock-reconstruction evidence, MedDRA version mismatch and listedness-source conflicts.

Present logger clock, pallet association, aggregation and excursion evidence.

Generate traceable allocation options with constraint rationale.

Assemble inspection-evidence packages with manifests.

Organize evidence and audit references for escalation, approval, override and closure.
```

---

# 6. Forbidden Actions From Stage 8

```text
Batch release/rejection/reprocess/re-label/recall.

QP certification.

Final PV seriousness, causality, expectedness, reportability determinations.

Signal confirmation.

Inventory status change, capacity reservation, stock allocation, shipment initiation.

Recall initiation.

Formulation, specification, clinical eligibility or safety-case disposition changes.

Silent unit conversion.

Silent genealogy repair.

Duplicate confirmation or merge/split of cases.

Setting the reporting clock.

Picking a listedness winner.

OOS/OOT or cold-chain excursion disposition.

Consent/entitlement override.

Exception override without authorized owner and reason.

Treating ambiguity as completeness.

Any unaudited recommendation, draft, approval, override, release, escalation, action, outcome or closure.
```

---

# 7. Approval / Stop / Escalation / Closure Gates From Stage 8

```text
Approval gates:
- QP certification / batch release: EU QP / Quality release reviewer
- OOS/OOT disposition: OOS owner
- unit-conversion acceptance: Laboratory/interface owner with Quality
- supplier-audit commitment closure: Supplier-quality
- PV disposition: PV medical reviewer
- allocation approval: Supply Chain VP / authorised Quality owner
- cold-chain excursion disposition: Logistics/Quality owner
- recall decision: Quality/Regulatory roles
- exception override: authorized human owner

Stop gates:
- unresolved identity/genealogy
- unresolved unit state
- unresolved terminology state
- unresolved authority/effective-date/jurisdiction
- unresolved consent/entitlement
- unresolved validation/checkpoint state
- incomplete release packet
- unverified supplier-audit commitment
- missing audit trail

Escalation gates:
- genealogy gap
- unit-conversion conflict
- OOS/OOT dispute
- supplier-audit gap
- PV clock/duplicate/terminology/listedness disputes
- cold-chain logger/pallet/aggregation dispute
- shortage/capacity conflict
- 47-minute audit-capture gap
- multi-agency inspection request

Closure gates:
- escalation closure
- release-packet evidence closure
- PV intake support closure
- supply option closure
- inspection-evidence closure
- case closure
```

---

# 8. Evidence and Audit Obligations From Stage 8

```text
Batch/product/case/shipment/source identity
Source evidence and provenance citation
Owner / role
Status and timestamp
Decision or action taken
Approval, rejection, or override where applicable
Reason where applicable (no-answer reason, override reason)
Release or closure status where applicable
Escalation action and outcome where applicable
The audit-capture gap and AI-off continuity state remain visible
```

---

# 9. Source / Evidence Needs for Stage 9

```text
Product master, batch record, MES genealogy, warehouse consumption records.
Lab results, interface mappings, LIMS OOS, statistical OOT, laboratory notebook.
Environmental monitoring and microbiology results.
Deviation, CAPA, change-control and cleaning-validation records.
Release-packet checklist and evidence-gap list.
Supplier audit reports and commitment-verification records.
Batch-review readiness package and QP-certification evidence.
Safety receipts (vendor, affiliate inbox, global safety DB), ICSR candidates, MedDRA versions, IB/CCDS/local labels.
Temperature logger records, pallet-association and serialisation-aggregation records.
Inventory, quality status, market authorisations, demand forecast, allocation policy, CMO capacity, supplier-risk records.
Validation inventory, source/document governance records, audit trails, downtime records, continuity requirements.
Non-negotiables and Stage 8 rule/decision registers.
```

---

# 10. Open Questions for Stage 9

```text
Which source documents are authoritative for each rule and decision, per business object, jurisdiction and effective date?

Which source documents are approved for internal review versus external/inspection packaging?

Which source documents need owner, version, effective date, review date and applicability metadata?

Which evidence sources are required before a draft, approval, override, escalation, release or closure can be audited?

Which supplier documents (including the untrusted deviation PDF and tool manifests) require quarantine and governance before use?

Which source gaps prevent safe evidence-backed workflow completion?

Which policies define authority, validation state, consent/entitlement, release-packet requirements, reporting-clock reconstruction, listedness sources, allocation constraints and recall criteria?
```

Stage 9 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 10.
