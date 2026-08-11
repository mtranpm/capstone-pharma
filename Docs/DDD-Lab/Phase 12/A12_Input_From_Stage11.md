# A12 Input From Stage 11 — NovaCura Therapeutics Group

## Source Artifact

Stage 11 — Human Decision Ownership Matrix

## Purpose of This Input

This file is the compact handoff from Stage 11 to Stage 12. It should be attached as the primary input for creating the Stage 12 Evidence and Audit Model.

Stage 12 must convert the human decision ownership model into an evidence and audit design. It must not resolve any batch, safety, quality or supply issue, approve batch release, QP certification, PV dispositions, allocation, shipment or recall, or bypass consent, entitlement, privacy or auditability constraints.

---

## 1. Decision Ownership Summary

```text
Batch-release readiness closure is responsible to Quality release reviewer and accountable to Quality release reviewer; EU QP certification follows as a separate gate.
QP certification is owned by the EU Qualified Person.
Batch release/rejection/reprocess/re-label/recall is owned by EU QP / Quality release reviewer with Quality/Regulatory roles for recall.
OOS/OOT disposition is owned by the laboratory analyst / OOS owner.
Unit-conversion acceptance (mg/L vs µg/mL) is owned by the laboratory / interface owner with Quality acceptance.
Batch identity/genealogy resolution (SUA-88) is owned by the identity / genealogy / master-data owner.
Environmental-excursion disposition is owned by the Quality / Manufacturing owner.
Deviation/CAPA/change-control closure is owned by the Quality / Manufacturing owner.
Supplier-audit verification and commitment closure is owned by the supplier-quality / quality reviewer.
Release-packet completeness acceptance is owned by the Quality release reviewer.
Final PV seriousness, causality, expectedness, reportability determinations are owned by the PV medical/safety reviewer.
Signal confirmation is owned by signal management; duplicate confirmation by the PV reviewer; awareness-date acceptance by PV case-intake staff / PV reviewer; listedness determination by PV medical reviewer / Regulatory Affairs; MedDRA terminology by the safety coder / terminology owner.
Cold-chain excursion disposition is owned by the logistics / cold-chain accountable owner with Quality input.
Serialisation aggregation resolution is owned by the serialisation owner.
Allocation recommendation sign-off and allocation approval are owned by the Supply Chain VP / authorised Quality owner.
Excipient-supply continuity and CMO capacity decisions are owned by procurement / Supply Chain planner with Supply Chain VP accountability.
Recall consideration is owned by Quality / Regulatory accountable roles.
Label/IB/CCDS alignment, IDMP identity and submission/commitment decisions are owned by Regulatory Affairs (with PV medical reviewer for listedness alignment).
Consent, entitlement, privacy and access exception decisions are owned by the Data Protection Officer / privacy owner.
The 72-hour inspection-evidence package sign-off and inspection response are owned by Regulatory Affairs / Quality accountable roles.
Evidence and audit completeness are owned by the relevant decision owner plus the audit/evidence owner to be assigned.
```

---

## 2. Human Approval Gates

```text
Batch-review readiness cannot be treated as complete without Quality release reviewer approval.
QP certification requires EU QP approval.
Batch release/rejection/reprocess/re-label/recall requires explicit human approval.
OOS/OOT disposition requires laboratory analyst / OOS owner disposition.
Unit-conversion acceptance requires laboratory/interface owner approval with Quality acceptance.
Supplier-audit commitment closure requires supplier-quality verification.
PV seriousness/causality/expectedness/reportability and signal confirmation require PV reviewer / signal management determination.
Duplicate confirmation, awareness-date acceptance and listedness determination require accountable PV review.
Allocation approval, capacity reservation, inventory-status change, shipment and recall require explicit authorised human approval.
Cold-chain excursion disposition requires logistics / cold-chain owner with Quality input.
Consent, entitlement and privacy exceptions require authorized owner and reason.
Overrides require authorized owner, reason, evidence, and timestamp.
Inspection-evidence package sign-off and inspection response require accountable Regulatory/Quality approval.
```

---

## 3. Batch and Quality Ownership

```text
Genealogy resolution, unit acceptance, OOS/OOT disposition, excursion disposition, deviation/CAPA/change-control closure, supplier verification, release-packet acceptance, readiness closure, QP certification and batch disposition all have named or to-be-assigned human owners.
No batch or quality issue is resolved in Stage 11.
```

---

## 4. Pharmacovigilance Ownership

```text
Duplicate candidates, awareness date, MedDRA version, listedness, seriousness/causality/reportability and signal confirmation all have named or to-be-assigned PV human owners.
No safety issue is resolved in Stage 11.
```

---

## 5. Supply, Cold-Chain and Allocation Ownership

```text
Cold-chain disposition, aggregation resolution, excipient-supply continuity, CMO capacity, allocation recommendation/approval and recall consideration all have named or to-be-assigned human owners.
No allocation or recall is approved in Stage 11.
```

---

## 6. Regulatory, Consent and Inspection Ownership

```text
Label/IB/CCDS alignment, IDMP identity, submission/commitment, consent/entitlement/privacy and inspection packaging/response all have named or to-be-assigned human owners.
No consent, entitlement or privacy boundary is overridden in Stage 11.
```

---

## 7. Escalation and Override Ownership

```text
Escalations require named owner, trigger, evidence, action, outcome, and closure decision.
Overrides require authorized owner, reason, evidence, timestamp, and downstream impact record.
Escalations must not close until action and outcome are recorded.
```

---

## 8. Audit Obligations

```text
Product/batch/case/shipment/participant data access and boundary checks must be logged.
Reconciliation packages, drafts, evidence-gap lists, readiness packages, options and evidence packages must be logged.
Human review requests, edits, approvals, rejections and overrides must be logged.
Batch and quality handling, PV handling, supply/cold-chain handling, regulatory/consent handling, escalation handling and closure must be logged.
The 47-minute audit-capture gap and AI-off continuity state must remain visible.
Case closure must be linked to evidence completeness.
```

---

## 9. Forbidden Ownership Patterns That Stage 12 Must Prevent Through Evidence and Audit Design

```text
Support role owns batch disposition or QP certification.
Support role makes final PV determinations or confirms signals.
Support role confirms duplicates, sets the reporting clock, or picks a listedness winner.
Support role disposes OOS/OOT, excursions or cold-chain events.
Support role approves allocation, reserves capacity, changes inventory status, ships product or initiates a recall.
Support role overrides consent, entitlement or privacy boundary.
Support role authorizes overrides without authorized owner and reason.
Support role closes cases or escalations without human outcome documentation.
Case is closed while unresolved gaps are hidden or unaudited.
```

---

## 10. Open Questions Carried Into Stage 12

```text
Who is the named EU QP, OOS owner, identity/genealogy owner, PV reviewer, signal owner, logistics owner, serialisation owner and inspection package signatory?
Who approves the mg/L vs µg/mL conversion, and which Quality role co-signs?
Who determines listedness per jurisdiction, and which approved versions apply?
Who approves allocation, and what constraint/compassionate-use rationale is required?
Who owns consent, entitlement and privacy checks?
Who can authorize overrides and what reason format is required?
Who confirms evidence and audit completeness before closure, including the 47-minute audit-capture gap?
```

---

## 11. Stage 12 Work Instruction

Use this handoff to create the Stage 12 Evidence and Audit Model. The Stage 12 artifact must define what evidence must be captured, where audit events are needed, which decisions require traceability, what must block release, disposition, allocation, shipment, recall or closure, and what audit gaps remain open.

Do not resolve batch, safety, quality, regulatory, clinical or supply issues. Identify evidence and audit needs only.
