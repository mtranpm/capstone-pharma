# A11 — Human Decision Ownership Matrix: NovaCura Therapeutics Group

## 1. Stage 11 Purpose

Stage 11 defines who owns the important batch, quality, pharmacovigilance, supply, cold-chain, regulatory, consent/entitlement, escalation and audit decisions in the NovaCura Therapeutics Group evidence-reconciliation case. The purpose is to make decision accountability explicit before designing the evidence and audit trail. This artifact preserves regulated Quality, Safety, Regulatory, Clinical and Supply accountability, the read-only advisory boundary, QP certification ownership, PV final-decision ownership, allocation and recall approval ownership, consent and entitlement boundaries, and auditable handling of recommendations, drafts, approvals, overrides, escalations, outcomes, and closure. It does not resolve the NCB204-B24071 genealogy, unit, OOS/OOT or supplier-audit gap; the PV awareness-date, duplicate, MedDRA-version or listedness conflict; the cold-chain logger, pallet or aggregation dispute; the excipient shortage, CMO capacity conflict or allocation question; the validation-state ambiguity; or the 47-minute audit-capture gap.

---

## 2. Human Ownership Boundary

### Humans must own

```text
batch-review readiness closure
QP certification (final batch certification)
batch release / rejection / reprocess / re-label / recall decisions
OOS/OOT disposition and investigation conclusion
unit-conversion acceptance (mg/L vs µg/mL)
supplier-audit verification and commitment closure
batch identity / genealogy resolution (SUA-88 break)
environmental-monitoring excursion disposition
deviation / CAPA / change-control closure
release-packet completeness acceptance for QP
final PV seriousness, causality, expectedness, reportability determinations
signal confirmation
duplicate-ICSR confirmation
awareness-date acceptance
MedDRA terminology decisions
listedness determination per jurisdiction
product-quality-to-case linkage disposition
cold-chain excursion disposition
serialisation aggregation resolution
excipient-supply continuity decisions
CMO capacity decisions
allocation recommendation sign-off and allocation approval
recall consideration
label / IB / CCDS alignment decisions
IDMP identity resolution
submission / commitment decisions
consent, entitlement, privacy, and access exception decisions
72-hour inspection-evidence packaging sign-off and response ownership
override approval and override reason
case / escalation closure when unresolved gaps exist or have been escalated
```

### Support roles may only help prepare

```text
summaries
reconciliation packages
conflict lists
genealogy-break identifications
unit-conversion and terminology conflict evidence
no-answer declarations
release-packet element and evidence-gap lists
readiness assessment drafts
duplicate-candidate lists
reporting-clock reconstruction evidence
listedness evidence comparisons
option-generation drafts with constraint rationale
cold-chain logger / pallet / aggregation evidence
approval requests
escalation summaries
inspection evidence package manifests
audit records
```

### Support roles must never own

```text
batch release, rejection, reprocess, re-label or recall
QP certification
final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions
duplicate confirmation
reporting-clock setting
listedness-winner selection
OOS/OOT or environmental-excursion disposition
cold-chain excursion disposition
serialisation aggregation resolution
inventory status change, capacity reservation, stock allocation, shipment or recall initiation
consent, entitlement, privacy or access override
exception override
case or escalation closure while unresolved gaps are hidden
```

---

## 3. Decision Inventory

### Batch and quality decisions

```text
batch identity / genealogy resolution (SUA-88 break)
unit-conversion acceptance (mg/L vs µg/mL)
OOS/OOT disposition and investigation conclusion
environmental-monitoring excursion disposition
deviation / CAPA / change-control closure
supplier-audit verification and commitment closure
release-packet completeness acceptance
batch-review readiness closure
QP certification
batch release / rejection / reprocess / re-label / recall
```

### Pharmacovigilance decisions

```text
PV case-intake completeness and routing decisions
duplicate-ICSR confirmation
awareness-date acceptance
MedDRA terminology decisions
listedness / expectedness determination
seriousness, causality, reportability determinations
product-quality-to-case linkage disposition
signal confirmation
```

### Supply, cold-chain and allocation decisions

```text
cold-chain excursion disposition
serialisation aggregation resolution
excipient-supply continuity decision
CMO capacity decision
allocation recommendation sign-off
allocation approval
shipment and inventory-status decisions
recall consideration
```

### Regulatory, consent and inspection decisions

```text
label / IB / CCDS alignment decisions
IDMP identity resolution
submission / commitment decisions
consent, entitlement, privacy, and access exception decisions
72-hour inspection-evidence packaging sign-off
inspection response ownership
```

### Escalation, override and audit decisions

```text
escalation creation, action, outcome and closure
exception override
evidence and audit completeness confirmation
case / escalation closure
```

---

## 4. RACI-Style Decision Ownership Matrix

| Decision / Work Item | Responsible Human Role | Accountable Human Role | Support Role May Prepare | Approval Required Before Action | Evidence Required | Stop / Escalation Condition | Audit Requirement |
|---|---|---|---|---|---|---|---|
| Batch identity/genealogy resolution (SUA-88) | Identity / genealogy / master-data owner | Identity / genealogy / master-data owner | ARC-002 Genealogy and Identity Verifier may surface the break | Human resolution required | MES genealogy, warehouse consumption, product master, aggregation state | Genealogy branch missing or conflict unresolved | Genealogy-break record, source records, owner, decision, timestamp |
| Unit-conversion acceptance (mg/L vs µg/mL) | Laboratory / interface owner | Laboratory / interface owner with Quality acceptance | ARC-003 Unit and Terminology Normaliser may surface the conflict and declare no-answer | Human acceptance required | Reported unit, assumed unit, mapping, approval record | Conversion assumption unapproved | Conversion mapping, no-answer declaration, approval/override record |
| OOS/OOT disposition | Laboratory analyst / OOS owner | Laboratory analyst / OOS owner | ARC-001 / ARC-003 may reconcile conflicting states | Human disposition required | LIMS OOS, statistical OOT, notebook-invalid, investigation record | Result state disputed with open investigation | Conflicting states, investigation record, disposition, reason |
| Environmental-monitoring excursion disposition | Quality / Manufacturing owner | Quality / Manufacturing accountable owner | ARC-001 may prepare excursion and organism-correction evidence | Human disposition required | Environmental monitoring, microbiology results, correction rationale | Excursion unresolved or organism correction unapproved | Excursion record, correction rationale, owner, decision |
| Deviation / CAPA / change-control closure | Quality / Manufacturing owner | Quality owner | ARC-001 may link lineage evidence | Human closure required | Deviation, CAPA, change-control, cleaning-validation, schedule records | Lineage unresolved or CAPA effectiveness unconfirmed | Lineage links, CAPA closure, change-control state, owner |
| Supplier-audit verification and commitment closure | Supplier-quality / quality reviewer | Supplier-quality / quality reviewer | ARC-005 Supplier-Audit Evidence Verifier may present verification state | Human verification required | Audit report, commitment evidence, verification record | Commitment claimed closed but unverified | Verification request/state, packet status, owner, timestamp |
| Release-packet completeness acceptance | Quality release reviewer | Quality release reviewer | ARC-004 Release-Packet Compiler may list elements and gaps | Human acceptance required | Release-packet checklist, supplier audits, CoAs, genealogy state | Packet elements unresolved or unverified | Packet status, element checklist, gap ownership, reviewer |
| Batch-review readiness closure | Quality release reviewer | Quality release reviewer | ARC-001 / ARC-004 may prepare readiness package | Human review required before readiness is treated as complete | Genealogy, unit, OOS/OOT, supplier, packet, validation, checkpoint state | Any unresolved or unverified element | Readiness review, reviewer, decision, unresolved gaps, timestamp |
| QP certification | EU Qualified Person | EU Qualified Person | ARC-001 / ARC-004 may prepare certification evidence package | QP approval required | Complete, conflict-visible batch-review readiness package | Unresolved genealogy, unit, OOS/OOT, supplier or packet state | Pending-status record, evidence package, QP identity, timestamp |
| Batch release / rejection / reprocess / re-label / recall | EU QP / Quality release reviewer; Quality/Regulatory for recall | EU QP / Quality release reviewer; Quality/Regulatory accountable roles for recall | ARC-001 / ARC-004 may prepare evidence; ARC-011 may prepare recall candidates | Explicit human approval required before any action | Batch history, release packet, safety cases, distribution evidence | Certification not completed or evidence gaps open | Release/reject/reprocess/re-label/recall decision, owner, evidence, timestamp |
| PV case-intake completeness and routing | PV case-intake staff | Global Head of Pharmacovigilance | ARC-006 PV Case Intake Assistant may prepare intake material | Human routing confirmation required | ICSR cases, receipts, consent/entitlement, terminology state | Identity, consent/entitlement or checkpoint state unresolved | Intake record, receipt basis, routing, reviewer |
| Duplicate-ICSR confirmation | PV reviewer | Global Head of Pharmacovigilance / PV reviewer | ARC-007 Duplicate-Candidate Detector may surface candidates only | Human confirmation required | Duplicate candidates, similarity rationale, product-name evidence | Candidates treated as confirmed without review | Duplicate rationale, candidates, confirmation, reviewer, timestamp |
| Awareness-date acceptance | PV case-intake staff / PV reviewer | Global Head of Pharmacovigilance / PV reviewer | ARC-008 Reporting-Clock Reconstructor may reconstruct evidence | Human acceptance required | Vendor receipt, affiliate inbox, global safety DB receipts | Receipt inputs incomplete or date disputed | Clock-reconstruction evidence, source basis, accepted date, owner |
| MedDRA terminology decisions | Safety coder / terminology owner | Global Head of Pharmacovigilance / terminology owner | ARC-003 may present version-mismatch evidence | Human decision required | Adverse events, terminology versions, controlled vocabularies | Version basis inconsistent | Version-alignment evidence, chosen basis, owner, timestamp |
| Listedness / expectedness determination | PV medical reviewer / Regulatory Affairs | Global Head of Pharmacovigilance / Regulatory Affairs VP | ARC-009 Listedness Evidence Retriever may compare sources | Human determination required | IB, CCDS, local label versions, jurisdiction basis | Listedness conflict unresolved or version unclear | Listedness-source versions, jurisdiction basis, determination record |
| Seriousness / causality / reportability determinations | PV medical/safety reviewer | Global Head of Pharmacovigilance / PV medical reviewer | ARC-006 / ARC-007 / ARC-008 / ARC-009 / ARC-010 may prepare evidence | Human determination required | Case data, duplicate/clock/terminology/listedness evidence | Duplicate, clock or terminology state unresolved | Determination record, reviewer, decision, reason, timestamp |
| Product-quality-to-case linkage disposition | PV / Quality owner | Global Head of Pharmacovigilance / Quality owner | ARC-010 Product-Quality Linkage Checker may surface linkage candidates | Human disposition required | Product complaints, ICSR cases, batches | Linkage treated as disposition | Complaint records, linkage evidence, disposition, owner |
| Signal confirmation | Signal management | Global Head of Pharmacovigilance / signal management lead | ARC-006 may prepare signal-review material | Human confirmation required | Signal metrics, exposure estimates, case evidence | Metrics unstable or exposure basis unclear | Signal-review record, basis, confirmation decision, owner |
| Cold-chain excursion disposition | Logistics / cold-chain accountable owner with Quality input | Logistics / cold-chain accountable owner with Quality input | ARC-012 Cold-Chain Evidence Reconstructor may present logger/pallet/aggregation evidence | Human disposition required | Logger clocks, pallet association, excursion evidence | Logger clock, pallet or aggregation evidence disputed | Logger basis, pallet link, excursion evidence, disposition, owner |
| Serialisation aggregation resolution | Serialisation owner | Serialisation accountable owner | ARC-002 / ARC-012 may surface missing aggregation | Human resolution required | Serialisation events, packaging events, line-restart evidence | Case-to-pallet aggregation missing after line restart | Aggregation-state record, gap ownership, resolution, owner |
| Excipient-supply continuity decision | Procurement / Supply Chain planner | Supply Chain VP | ARC-011 Supply Recovery Option Analyst may prepare options | Human decision required | Supplier risks, inventory, recovery estimate, alternate qualification | Sole-source contamination with no qualified alternate | Shortage record, options, decision, owner, reason |
| CMO capacity decision | Procurement / CMO quality | Supply Chain VP | ARC-011 may surface capacity-conflict evidence | Human decision required | CMO capacity, vendor contracts, promised capacity | CMO promised capacity to two sponsors | Capacity-conflict record, contract basis, decision, owner |
| Allocation recommendation sign-off | Supply planner | Supply Chain VP / authorised Quality owner | ARC-011 may generate traceable options; ARC-013 may check constraints | Human sign-off required before recommendation is presented as approved | Inventory, quality status, market authorisations, demand, constraints | Option violates a constraint or cold-chain evidence unresolved | Option rationale, constraint checks, sign-off record, owner |
| Allocation approval | Supply Chain VP / authorised Quality owner | Supply Chain VP / authorised Quality owner | ARC-011 / ARC-013 may prepare approval request | Explicit human approval required before any allocation | Traceable options, constraint rationale, approval request | No explicit authorised human approval | Approval request, human approval, action record, reason |
| Shipment / inventory-status decisions | Supply Chain / logistics accountable owner | Supply Chain VP / authorised Quality owner | ARC-011 may prepare shipment evidence | Explicit human approval required | Allocation approval, cold-chain evidence, logistics evidence | Cold-chain evidence unresolved or no approval | Shipment/status record, approval link, owner, timestamp |
| Recall consideration | Quality / Regulatory accountable roles | Quality / Regulatory accountable roles | ARC-011 / ARC-014 may prepare recall-candidate evidence | Human decision required before any recall action | Recall candidates, batch history, distribution, safety cases | Recall-scope uncertainty unresolved | Recall consideration record, decision, owner, evidence, timestamp |
| Label / IB / CCDS alignment decisions | Regulatory Affairs (labelling) / PV medical reviewer | Regulatory Affairs VP | ARC-009 may present listedness-source comparisons | Human decision required | Product labels, listedness sources, market authorisations | Label / IB / CCDS conflict unresolved | Label version used, alignment decision, owner, reason |
| IDMP identity resolution | Regulatory Affairs (IDMP) | Regulatory Affairs VP | ARC-002 / ARC-003 may surface mapping conflicts | Human resolution required | IDMP mappings, medicinal products, substance master | Mapping ambiguous (strength/presentation) | Mapping evidence, resolution, owner, timestamp |
| Submission / commitment decisions | Regulatory Affairs / Supplier-quality | Regulatory Affairs VP | ARC-014 may prepare commitment status evidence | Human decision required | Regulatory commitments, authority correspondence, tracker dates | Commitment due date ambiguous or unverified | Commitment record, decision, owner, verification state |
| Consent / entitlement / privacy decisions | Data Protection Officer / privacy owner | Data Protection Officer | Support role may record check status only | Valid check or authorized exception required before access/use | Consent status, entitlement status, privacy boundary status | eConsent version asynchrony or entitlement unclear | Check performed, result, accessor, purpose, timestamp |
| 72-hour inspection-evidence packaging sign-off | Regulatory / Quality participant | Regulatory Affairs VP / Chief Quality Officer | ARC-014 Inspection Evidence Packager may assemble package and manifest | Human sign-off required before submission | Package manifest, source citations, batch/trial/safety/AI-control evidence | Evidence gap or 47-minute audit gap unresolved | Package manifest, sign-off, reviewer, timestamp |
| Inspection response ownership | Regulatory Affairs / Quality accountable roles | Regulatory Affairs VP / Chief Quality Officer | ARC-014 may prepare response material | Human approval required before response | Inspection request, packaged evidence, open gap status | Missing or conflicting evidence | Response record, approver, evidence links, timestamp |
| Exception override | Authorized human owner for the decision | Same accountable owner or delegated authorized owner | Support role may show risk/evidence only | Authorized owner approval and reason required | Decision context, evidence, risk, reason | Unauthorized override or missing reason | Override owner, reason, evidence, timestamp, downstream impact |
| Case / escalation closure | Accountable workflow owner plus relevant decision owner | Accountable workflow owner | ARC-014 / ARC-015 may surface closure checklist | Human closure decision required | Evidence status, unresolved gaps, approvals, escalation outcome | Any unresolved hidden gap or missing outcome | Closure decision, owner, evidence, unresolved exceptions, timestamp |

---

## 5. Batch and Quality Decision Ownership

Batch and quality decisions remain with EU QP, Quality release reviewers, laboratory/OOS owners, identity/genealogy owners and supplier-quality owners. The support role may reconcile evidence and surface gaps, but must not resolve, dispose, certify or release.

| Batch / Quality Area | Visible Gap / Decision Need | Human Owner | Support Role Boundary | Required Gate |
|---|---|---|---|---|
| Batch identity/genealogy resolution | Single-use assembly lot SUA-88 missing from MES genealogy branch but present in warehouse consumption | Identity / genealogy / master-data owner | Reconcile branches and surface the break with ownership | Human resolution |
| Unit-conversion handling | Contract-lab concentration in mg/L while receiving interface assumes µg/mL | Laboratory / interface owner with Quality acceptance | Surface the conflict and declare no-answer | Human acceptance |
| OOS/OOT disposition | LIMS marks OOS, statistical tool marks OOT, notebook labels invalid | Laboratory analyst / OOS owner | Reconcile conflicting states without disposition | Human disposition |
| Environmental-monitoring excursion | Excursion near fill-finish; organism identification corrected after initial review | Quality / Manufacturing owner | Prepare excursion and correction evidence | Human disposition |
| Deviation / CAPA / change-control closure | Open deviation similar to a closed deviation; CAPA effectiveness; change-control retrospective approval missing | Quality / Manufacturing owner | Link lineage evidence | Human closure |
| Supplier-audit verification | EU release packet lacks confirmation of a contract-site audit commitment | Supplier-quality / quality reviewer | Present verification state; never treat unverified as closed | Human verification |
| Release-packet completeness | Packet lacks confirmation of one audit commitment | Quality release reviewer | List elements and evidence gaps | Human acceptance |
| Batch-review readiness closure | Batch not shown release-ready while elements are unresolved | Quality release reviewer | Prepare readiness package only | Human review |
| QP certification | Final batch certification | EU Qualified Person | Prepare certification evidence package | QP approval |
| Batch release / rejection / reprocess / re-label / recall | Regulated batch disposition | EU QP / Quality release reviewer; Quality/Regulatory for recall | Prepare evidence only | Explicit human approval |

No batch or quality issue is resolved in this artifact.

---

## 6. Pharmacovigilance Decision Ownership

Pharmacovigilance decisions remain with PV case-intake staff, PV medical/safety reviewers, signal management and Regulatory Affairs. The support role may prepare intake material, candidate lists, clock-reconstruction evidence and listedness comparisons, but must not make final determinations.

| PV Area | Visible Gap / Decision Need | Human Owner | Support Role Boundary | Required Gate |
|---|---|---|---|---|
| Case-intake completeness | ICSR cluster under different product names | PV case-intake staff / Global Head of PV | Attribute sources and surface completeness gaps | Human routing confirmation |
| Duplicate confirmation | Duplicate candidates PV-1001 / PV-1009 / PV-1014 | PV reviewer | Surface candidates only; never confirm or merge | Human confirmation |
| Awareness-date acceptance | Awareness date disputed across vendor receipt, affiliate inbox, global safety DB | PV case-intake staff / PV reviewer | Reconstruct the clock as evidence only | Human acceptance |
| MedDRA terminology | Two MedDRA versions change the preferred term | Safety coder / terminology owner | Present version-mismatch evidence | Human decision |
| Listedness / expectedness | IB v12 and CCDS v4 list; IN local label does not | PV medical reviewer / Regulatory Affairs | Compare listedness sources per jurisdiction and version | Human determination |
| Seriousness / causality / reportability | Final PV determinations | PV medical/safety reviewer | Prepare case-review material | Human determination |
| Product-quality linkage | Product-quality complaints link to cases and batches | PV / Quality owner | Surface linkage candidates only | Human disposition |
| Signal confirmation | Signal metrics unstable across methods and exposure bases | Signal management | Prepare signal-review material | Human confirmation |

No safety issue is resolved in this artifact.

---

## 7. Supply, Cold-Chain and Allocation Decision Ownership

Supply, cold-chain and allocation decisions remain with Supply Chain, logistics, serialisation, procurement, CMO quality and authorised Quality owners. The support role may generate traceable options and evidence, but must not approve any allocation, shipment, inventory-status change or recall.

| Supply / Cold-Chain / Allocation Area | Visible Gap / Decision Need | Human Owner | Support Role Boundary | Required Gate |
|---|---|---|---|---|
| Cold-chain excursion disposition | Biologic shipment exceeds range; logger clocks and pallet association disputed | Logistics / cold-chain accountable owner with Quality input | Reconstruct logger, pallet and excursion evidence | Human disposition |
| Serialisation aggregation resolution | Case-to-pallet aggregation missing after line restart | Serialisation owner | Surface missing aggregation state | Human resolution |
| Excipient-supply continuity | Sole-source excipient contamination with eight-week recovery | Procurement / Supply Chain planner | Prepare shortage options | Human decision |
| CMO capacity decision | CMO promises capacity to two sponsors in the same window | Procurement / CMO quality | Surface capacity-conflict evidence | Human decision |
| Allocation recommendation | Demand exceeds stock across markets, trials and compassionate use | Supply planner | Generate policy-bounded options with constraint rationale | Human sign-off |
| Allocation approval | No stock allocation without explicit authorised human approval | Supply Chain VP / authorised Quality owner | Prepare approval request | Explicit human approval |
| Recall consideration | Recall candidates exist with shared components and distribution | Quality / Regulatory accountable roles | Prepare recall-candidate evidence | Human consideration decision |

No allocation or recall is approved in this artifact.

---

## 8. Regulatory, Consent and Inspection Decision Ownership

Regulatory, consent and inspection decisions remain with Regulatory Affairs, labelling, IDMP, Data Protection Officer and accountable Quality roles. The support role may assemble evidence, but must not override consent, entitlement or privacy boundaries or sign inspection responses.

| Regulatory / Consent / Inspection Area | Visible Gap / Decision Need | Human Owner | Support Role Boundary | Required Gate |
|---|---|---|---|---|
| Label / IB / CCDS alignment | Listedness conflict between IB, core data sheet and local label | Regulatory Affairs (labelling) / PV medical reviewer | Compare approved sources per jurisdiction and version | Human decision |
| IDMP identity | Local product to IDMP mapping ambiguous on strength/presentation | Regulatory Affairs (IDMP) | Surface mapping conflict | Human resolution |
| Submission / commitment decisions | Commitment due dates and verification state | Regulatory Affairs / Supplier-quality | Prepare commitment-status evidence | Human decision |
| Consent / entitlement / privacy | eConsent version asynchrony with trial amendment; entitlement revocation lag | Data Protection Officer / privacy owner | Record check status only | Valid check or authorized exception |
| 72-hour inspection-evidence packaging | Multi-agency request spanning trial, batch, safety and AI controls | Regulatory / Quality participant | Assemble package and manifest | Human sign-off |
| Inspection response ownership | Response to the joint inspection request | Regulatory Affairs / Quality accountable roles | Prepare response material | Human approval |

No consent, entitlement or privacy boundary is overridden in this artifact.

---

## 9. Escalation and Override Ownership

Escalations and overrides must be owned by authorized humans, documented with reason, and closed only when outcomes are recorded.

| Escalation / Override Area | Trigger | Responsible Human Role | Accountable Human Role | Required Evidence | Audit Requirement |
|---|---|---|---|---|---|
| Genealogy escalation | SUA-88 break with conflicting warehouse evidence | Identity / genealogy / master-data owner | Identity / genealogy / master-data owner | MES genealogy, warehouse consumption | Break, owner, decision, timestamp |
| Unit-conversion escalation | Unapproved mg/L vs µg/mL assumption | Laboratory / interface owner with Quality | Laboratory / interface owner with Quality | Reported unit, assumed unit, mapping | No-answer declaration, acceptance, reason |
| OOS/OOT escalation | LIMS, statistical tool and notebook disagree | Laboratory analyst / OOS owner | Laboratory analyst / OOS owner | Conflicting states, investigation record | Disposition, reason, timestamp |
| Supplier-audit escalation | Commitment claimed closed but unverified | Supplier-quality / quality reviewer | Supplier-quality / quality reviewer | Audit report, verification record | Verification request/state, closure |
| PV clock/duplicate/terminology/listedness escalation | Disputed awareness date, duplicate candidates, MedDRA mismatch, listedness conflict | PV reviewer / safety coder / Regulatory Affairs | Global Head of Pharmacovigilance | Receipts, candidates, version and source basis | Escalation, owner, decision, reason |
| Cold-chain escalation | Logger clock, pallet or aggregation dispute | Logistics / serialisation owner | Logistics / cold-chain accountable owner with Quality input | Logger basis, pallet link, aggregation state | Escalation, owner, disposition, timestamp |
| Shortage/capacity escalation | Excipient shortage, CMO capacity conflict, demand exceeds stock | Procurement / Supply planner | Supply Chain VP | Inventory, supplier risk, capacity, forecast | Escalation, options, approval record |
| Audit-gap escalation | 47-minute audit-capture gap | Audit / quality oversight | Audit / quality oversight / CISO | Downtime records, audit trails | Gap record, duration, owner |
| Inspection escalation | Multi-agency request within 72 hours | Regulatory / Quality participant | Regulatory Affairs VP / Chief Quality Officer | Package manifest, source citations | Package, sign-off, timestamp |
| Override | Authorized deviation from normal rule or workflow | Authorized owner for that decision | Same accountable owner or delegated authorized owner | Evidence, risk, reason | Override owner, reason, timestamp, downstream impact |

---

## 10. Audit Ownership Model

| Audit Class | Minimum Events | Accountable Owner |
|---|---|---|
| Identity and access checks | Product/batch/case/shipment/participant data accessed; consent checked; entitlement checked; privacy boundary checked | Data Protection Officer / identity and access owner |
| Batch and quality review | Genealogy-break surfaced; unit conflict surfaced; OOS/OOT states reconciled; excursion evidence prepared; readiness package created; readiness reviewed; QP pending status recorded | Quality release reviewer; EU QP for certification |
| QP certification and batch disposition | Certification evidence package created; certification decision recorded; batch release/rejection/reprocess/re-label/recall decision recorded | EU Qualified Person / Quality release reviewer |
| Supplier evidence | Verification request created; commitment verification state recorded; packet status updated | Supplier-quality / quality reviewer |
| PV review | Intake material created; duplicate candidates surfaced; clock evidence reconstructed; listedness comparisons prepared; determination recorded; case routed | Global Head of Pharmacovigilance / PV reviewers |
| Supply and cold-chain | Options generated; constraint checks recorded; logger/pallet/aggregation evidence prepared; approval request created; approval recorded | Supply Chain VP / authorised Quality owner |
| Regulatory and inspection | Label/IDMP/commitment evidence prepared; package manifest created; package sign-off recorded; response approved | Regulatory Affairs VP / Chief Quality Officer |
| Escalation | Escalation created; owner notified; action taken; outcome recorded; closure approved | Accountable workflow owner |
| Override | Override requested; evidence reviewed; reason captured; authorized owner approved/rejected | Authorized owner for the decision |
| Audit-capture and closure | Audit event envelopes recorded; 47-minute gap kept visible; evidence completeness confirmed; closure decision recorded | Audit / quality oversight; accountable workflow owner |

---

## 11. Forbidden Ownership Patterns

The workshop team must avoid the following unsafe patterns:

```text
support role owns batch release, rejection, reprocess, re-label or recall
support role owns QP certification
support role makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions
support role confirms duplicates, sets the reporting clock, or picks a listedness winner
support role disposes OOS/OOT, environmental excursions or cold-chain excursions
support role resolves the SUA-88 genealogy break or applies the mg/L vs µg/mL conversion
support role closes a supplier-audit commitment without verification
support role approves allocation, reserves capacity, changes inventory status, ships product or initiates a recall
support role overrides consent, entitlement, or privacy boundary
support role authorizes an override without authorized owner and reason
support role closes cases or escalations without documented human outcome
approval is recorded without named human owner
exception is recorded without reason
source evidence is missing or not linked to the decision
a later timestamp is treated as automatically more authoritative
the 47-minute audit-capture gap is filled or hidden
```

---

## 12. Open Ownership Questions

```text
Who is the named EU Qualified Person accountable for certification of batch NCB204-B24071?
Who is the assigned identity/genealogy/master-data owner to resolve the SUA-88 break?
Who owns acceptance of the mg/L vs µg/mL conversion, and which Quality role co-signs?
Who is the assigned OOS owner for investigation OOS-88?
Who owns environmental-excursion disposition for the sterile-area event?
Who verifies and closes the contract-site audit commitment in the EU release packet?
Who confirms batch-review readiness closure before the QP certification gate?
Who is the named PV reviewer for duplicate confirmation and awareness-date acceptance?
Who owns MedDRA version alignment, and which version basis applies per case?
Who determines listedness per jurisdiction, and which approved label/IB/CCDS versions apply?
Who confirms the signal-review decision for the anaphylaxis cluster?
Who disposes the cold-chain excursion with resolved logger, pallet and aggregation evidence?
Who approves any allocation option, and what constraint/compassionate-use rationale is required?
Who owns the excipient-supply continuity and CMO capacity decisions?
Who owns the 72-hour inspection-evidence package and signs the manifest?
Who owns consent, entitlement, and privacy boundary checks and exceptions?
Who can authorize an override, and what reason format is required?
Who confirms audit completeness before case closure, including the 47-minute audit-capture gap?
Who can close a case or escalation when exceptions were escalated rather than fully resolved?
```

---

## 13. Quality Gate Checklist

Before Stage 11 is accepted, confirm:

```text
[ ] Every decision has a responsible human role.
[ ] Every decision has an accountable human role or is explicitly marked role-to-be-assigned.
[ ] No support role owns batch release, rejection, reprocess, re-label or recall.
[ ] No support role owns QP certification.
[ ] No support role makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions.
[ ] Duplicate confirmation, awareness-date acceptance and listedness determination remain human-owned.
[ ] OOS/OOT, environmental-excursion and cold-chain excursion disposition remain human-owned.
[ ] Allocation, capacity reservation, inventory-status change, shipment and recall require explicit authorised human approval.
[ ] Consent, entitlement, and privacy decisions remain human-owned.
[ ] Overrides require authorized owner, reason, evidence, and timestamp.
[ ] Escalations cannot close without documented action and outcome.
[ ] Every approval, rejection, override, release, escalation, outcome, and closure is auditable.
[ ] The 47-minute audit-capture gap is not filled or hidden.
[ ] Unresolved batch, safety, quality and supply issues are identified as workflow/domain gaps only, not resolved.
```

---

## 14. NEXT_STAGE_INPUT_BLOCK

```text
Stage 12 Input — Evidence and Audit Model

Source Stage:
Stage 11 — Human Decision Ownership Matrix

Decision Ownership Summary:
- Batch-release readiness closure is responsible to Quality release reviewer and accountable to Quality release reviewer; EU QP certification follows as a separate gate.
- QP certification is owned by the EU Qualified Person.
- Batch release/rejection/reprocess/re-label/recall is owned by EU QP / Quality release reviewer with Quality/Regulatory roles for recall.
- OOS/OOT disposition is owned by the laboratory analyst / OOS owner.
- Unit-conversion acceptance (mg/L vs µg/mL) is owned by the laboratory / interface owner with Quality acceptance.
- Batch identity/genealogy resolution (SUA-88) is owned by the identity / genealogy / master-data owner.
- Environmental-excursion disposition is owned by the Quality / Manufacturing owner.
- Deviation/CAPA/change-control closure is owned by the Quality / Manufacturing owner.
- Supplier-audit verification and commitment closure is owned by the supplier-quality / quality reviewer.
- Release-packet completeness acceptance is owned by the Quality release reviewer.
- Final PV seriousness, causality, expectedness, reportability determinations are owned by the PV medical/safety reviewer.
- Signal confirmation is owned by signal management; duplicate confirmation by the PV reviewer; awareness-date acceptance by PV case-intake staff / PV reviewer; listedness determination by PV medical reviewer / Regulatory Affairs; MedDRA terminology by the safety coder / terminology owner.
- Cold-chain excursion disposition is owned by the logistics / cold-chain accountable owner with Quality input.
- Serialisation aggregation resolution is owned by the serialisation owner.
- Allocation recommendation sign-off and allocation approval are owned by the Supply Chain VP / authorised Quality owner.
- Excipient-supply continuity and CMO capacity decisions are owned by procurement / Supply Chain planner with Supply Chain VP accountability.
- Recall consideration is owned by Quality / Regulatory accountable roles.
- Label/IB/CCDS alignment, IDMP identity and submission/commitment decisions are owned by Regulatory Affairs (with PV medical reviewer for listedness alignment).
- Consent, entitlement, privacy and access exception decisions are owned by the Data Protection Officer / privacy owner.
- The 72-hour inspection-evidence package sign-off and inspection response are owned by Regulatory Affairs / Quality accountable roles.
- Evidence and audit completeness are owned by the relevant decision owner plus the audit/evidence owner to be assigned.

Human Approval Gates:
- Batch-review readiness cannot be treated as complete without Quality release reviewer approval.
- QP certification requires EU QP approval.
- Batch release/rejection/reprocess/re-label/recall requires explicit human approval.
- OOS/OOT disposition requires laboratory analyst / OOS owner disposition.
- Unit-conversion acceptance requires laboratory/interface owner approval with Quality acceptance.
- Supplier-audit commitment closure requires supplier-quality verification.
- PV seriousness/causality/expectedness/reportability and signal confirmation require PV reviewer / signal management determination.
- Duplicate confirmation, awareness-date acceptance and listedness determination require accountable PV review.
- Allocation approval, capacity reservation, inventory-status change, shipment and recall require explicit authorised human approval.
- Cold-chain excursion disposition requires logistics / cold-chain owner with Quality input.
- Consent, entitlement and privacy exceptions require authorized owner and reason.
- Overrides require authorized owner, reason, evidence, and timestamp.
- Inspection-evidence package sign-off and inspection response require accountable Regulatory/Quality approval.

Batch and Quality Ownership:
- Genealogy resolution, unit acceptance, OOS/OOT disposition, excursion disposition, deviation/CAPA/change-control closure, supplier verification, release-packet acceptance, readiness closure, QP certification and batch disposition all have named or to-be-assigned human owners.
- No batch or quality issue is resolved in Stage 11.

Pharmacovigilance Ownership:
- Duplicate candidates, awareness date, MedDRA version, listedness, seriousness/causality/reportability and signal confirmation all have named or to-be-assigned PV human owners.
- No safety issue is resolved in Stage 11.

Supply, Cold-Chain and Allocation Ownership:
- Cold-chain disposition, aggregation resolution, excipient-supply continuity, CMO capacity, allocation recommendation/approval and recall consideration all have named or to-be-assigned human owners.
- No allocation or recall is approved in Stage 11.

Regulatory, Consent and Inspection Ownership:
- Label/IB/CCDS alignment, IDMP identity, submission/commitment, consent/entitlement/privacy and inspection packaging/response all have named or to-be-assigned human owners.
- No consent, entitlement or privacy boundary is overridden in Stage 11.

Escalation / Override Ownership:
- Escalations require named owner, trigger, evidence, action, outcome, and closure decision.
- Overrides require authorized owner, reason, evidence, timestamp, and downstream impact record.
- Escalations must not close until action and outcome are recorded.

Audit Obligations:
- Product/batch/case/shipment/participant data access and boundary checks must be logged.
- Reconciliation packages, drafts, evidence-gap lists, readiness packages, options and evidence packages must be logged.
- Human review requests, edits, approvals, rejections and overrides must be logged.
- Batch and quality handling, PV handling, supply/cold-chain handling, regulatory/consent handling, escalation handling and closure must be logged.
- The 47-minute audit-capture gap and AI-off continuity state must remain visible.
- Case closure must be linked to evidence completeness.

Forbidden Ownership Patterns:
- Support role owns batch disposition or QP certification.
- Support role makes final PV determinations or confirms signals.
- Support role confirms duplicates, sets the reporting clock, or picks a listedness winner.
- Support role disposes OOS/OOT, excursions or cold-chain events.
- Support role approves allocation, reserves capacity, changes inventory status, ships product or initiates a recall.
- Support role overrides consent, entitlement or privacy boundary.
- Support role authorizes overrides without authorized owner and reason.
- Support role closes cases or escalations without human outcome documentation.
- Case is closed while unresolved gaps are hidden or unaudited.

Open Questions:
- Who is the named EU QP, OOS owner, identity/genealogy owner, PV reviewer, signal owner, logistics owner, serialisation owner and inspection package signatory?
- Who approves the mg/L vs µg/mL conversion, and which Quality role co-signs?
- Who determines listedness per jurisdiction, and which approved versions apply?
- Who approves allocation, and what constraint/compassionate-use rationale is required?
- Who owns consent, entitlement and privacy checks?
- Who can authorize overrides and what reason format is required?
- Who confirms evidence and audit completeness before closure, including the 47-minute audit-capture gap?
```

Stage 11 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 12.
