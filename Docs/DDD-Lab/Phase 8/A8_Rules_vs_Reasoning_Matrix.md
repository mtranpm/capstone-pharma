# A8 — Rules vs Reasoning Matrix: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## 1. Stage 8 Purpose

Stage 8 separates the NovaCura Therapeutics Group evidence-reconciliation domain work into hard rules, workflow gates, human-owned decisions, judgment-based decisions, support-only activities, forbidden automated actions, and audit obligations. The purpose is to prevent unsafe delegation of regulated Quality, Safety, Regulatory, Clinical and Supply accountability while still making batch-review, pharmacovigilance case-intake and supply-recovery work clearer, safer, more conflict-visible and more auditable. This stage does **not** resolve the NCB204-B24071 genealogy/unit/OOS dispute, the PV awareness-date/duplicate/listedness conflict, the cold-chain excursion, the excipient shortage or the CMO capacity conflict; it only classifies how those issues must be governed in the business workflow. It does not provide medical, regulatory or legal advice, and it does not approve batch release, QP certification, PV dispositions, allocation, shipment or recall.

---

## 2. Rule / Judgment / Support Classification Model

| Category | Meaning in This Case | Example From the Case |
|---|---|---|
| Deterministic rule | A yes/no, state-based, or evidence-based rule that can be checked consistently | A batch must not be shown as release-ready while any genealogy branch or release-packet element is unresolved or unverified |
| Workflow gate | A process checkpoint that must be passed, escalated, or explicitly left open before the workflow proceeds | Unit-conversion state and validation state must be resolved or declared no-answer before evidence output |
| Approval gate | A checkpoint requiring named human approval | QP certification; batch release/rejection; allocation approval by an authorised Supply Chain/Quality owner |
| Human-owned decision | A decision that must remain with an accountable human pharmaceutical role | Batch release/rejection; OOS/OOT disposition; final PV seriousness/causality/expectedness/reportability determinations; recall decision |
| Judgment-based decision | A decision requiring regulated professional judgment rather than rule-only handling | Whether the disputed OOS/OOT state warrants investigation conclusion; whether a duplicate candidate is confirmed; whether an out-of-window cold-chain excursion is acceptable |
| Draft/support activity | Preparation, reconciliation, summarization, comparison, checklist support, or evidence organization that does not make the decision | Reconciling batch genealogy into a conflict-visible readiness package; preparing reporting-clock evidence for review |
| Forbidden automated action | Any action that must not be delegated away from the accountable human owner | Releasing/rejecting/reprocessing/re-labelling/recalling a batch; changing inventory status; reserving capacity; allocating stock; initiating a recall |
| Audit/evidence obligation | Required traceability for source, owner, status, decision, approval, override, release, escalation, or closure | Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable |

---

## 3. Deterministic Rules Register

| Rule ID | Rule Statement | Triggering Condition | Pass Condition | Fail Condition | Owner / Accountable Role | Audit Evidence Required |
|---|---|---|---|---|---|---|
| R-01 | Evidence output requires resolved product/batch/compound identity | Any batch, safety or supply evidence output is contemplated | Identity is confirmed or output is withheld with a no-answer declaration | Identity state is unresolved and output is still produced | Identity / genealogy / master-data owner | Identity-match evidence, source, no-answer record |
| R-02 | Genealogy completeness must be checked before batch evidence output | Batch-review readiness evidence is assembled | All branches are present and linked, or gaps are visible with ownership | A genealogy branch is missing (SUA-88) without a visible gap | Identity / genealogy / master-data owner | Genealogy-break identification, source records, ownership |
| R-03 | A batch must not be shown as release-ready while any genealogy branch or release-packet element is unresolved or unverified | Release-packet completeness is assessed | All genealogy branches and release-packet elements are resolved/verified | Release-ready status claimed with unresolved or unverified elements | Quality release reviewer | Genealogy state, release-packet completeness, gap list |
| R-04 | Unit-conversion consistency must be resolved before output (mg/L vs µg/mL) | Contract-lab concentration is used | Reported unit and receiving-interface assumption are aligned and approved | mg/L vs µg/mL assumption is unapproved | Laboratory / interface owner with Quality acceptance | Conversion mapping, approval/override record |
| R-05 | Identity/product-code match check | Product code or batch is referenced | Product code and batch identity match the product master | Product code/batch mismatch is unresolved | Identity / genealogy / master-data owner | Match-check result, product-master reference |
| R-06 | A disputed OOS/OOT/notebook-invalid result state remains open and visible | A laboratory result is assessed | Result state is visible with open investigation ownership | The result is dispositioned or hidden | Laboratory analyst / OOS owner | Conflicting states, sources, investigation record |
| R-07 | An unverified supplier-audit commitment is not treated as closed | Release-packet completeness is assessed | Commitment is independently verified | EU release packet lacks confirmation of the contract-site audit commitment | Supplier-quality / quality reviewer | Verification request, verification state, packet status |
| R-08 | Back-entered batch-record steps require checkpoint and audit evidence | A batch-record step is reviewed | Checkpoint and audit evidence exist for the step | Step was back-entered after network degradation without checkpoint evidence | Manufacturing / quality reviewer | Detection record, timestamps, checkpoint state |
| R-09 | Validation-state consistency must be checked before evidence output | A system or record is used as evidence | Validation state is unambiguous (validated/conditionally released/research-only) | Validation state is ambiguous across inventories | Validation / quality owner | Validation-state evidence, owner, no-answer record |
| R-10 | Entitlement/consent gate must pass before patient/participant data is surfaced | Patient or participant data is accessed, used, routed or shared | Consent/entitlement is valid for the purpose | eConsent version asynchrony with the trial amendment makes consent unresolved | Data Protection Officer / privacy owner | Consent/entitlement check, access/use record |
| R-11 | Checkpoint-state completeness check before evidence output | Any record or step is relied on | Checkpoint state is complete or unresolved state is declared no-answer | Checkpoint state is unresolved and output is still produced | Accountable workflow owner | Checkpoint-state record, no-answer declaration |
| R-12 | Required release-packet element completeness check | Release packet is assembled | All required elements are present or gaps are visible with owners | Missing supplier-audit confirmation, unresolved unit/OOS state hidden in the packet | Quality release reviewer | Packet status, element checklist, gap ownership |
| R-13 | MedDRA version consistency must be resolved before terminology output | PV terminology is used | A single MedDRA version basis is established and consistent | Two MedDRA versions change the preferred term | Safety coder / terminology owner | Version-alignment evidence, source |
| R-14 | Duplicate-ICSR candidate similarity check surfaces candidates only | A new ICSR is compared with existing cases | Candidates are surfaced for accountable review; no confirmation is made | Candidates are confirmed, merged or split without review | PV case-intake staff | Duplicate rationale, candidates, reviewer routing |
| R-15 | Reporting-clock reconstruction inputs must be complete | Awareness date is reconstructed | Vendor receipt, affiliate inbox and global safety DB inputs are present and attributed | A disputed awareness date lacks complete source inputs | PV case-intake staff / PV reviewer | Clock-reconstruction evidence, source basis |
| R-16 | The audit-capture gap remains visible and is not filled silently | An audit-trail completeness check occurs | The 47-minute gap is documented with owner | The gap is filled or hidden silently | Audit / quality oversight | Gap detection, duration, owner |
| R-17 | Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable | Any workflow event occurs | Audit event envelope captures source, owner, status, timestamp | Missing or incomplete audit trail | Audit / quality oversight | Audit event envelope, source, owner, timestamp |

---

## 4. Human-Owned Decision Register

| Decision ID | Decision | Accountable Owner | Supporting Participants | Evidence Needed | What Must Not Be Automated |
|---|---|---|---|---|---|
| D-01 | Batch release / rejection / reprocess / re-label | EU Qualified Person / Quality release reviewer | Manufacturing, laboratory, supplier-quality, batch-review coordination | Genealogy, lab results, OOS/OOT state, excursion evidence, supplier evidence, release-packet completeness | Batch release/rejection/reprocess/re-label decision |
| D-02 | QP certification (final batch certification) | EU Qualified Person | Quality release reviewer, batch-review coordination | Batch-review readiness package, release packet, evidence-gap status | QP certification decision |
| D-03 | OOS/OOT disposition and investigation conclusion | Laboratory analyst / OOS owner | Statistical/biostatistics input, quality, laboratory management | LIMS OOS, statistical OOT, notebook-invalid notes, investigation record | Dispositioning the assay automatically |
| D-04 | Unit-conversion acceptance | Laboratory / interface owner with Quality acceptance | Interface/IT mapping owner, quality | Reported unit, assumed unit, mapping, approval record | Applying the conversion without approval |
| D-05 | Supplier-audit verification and commitment closure | Supplier-quality / quality reviewer | CMO/supplier quality, procurement | Audit report, commitment evidence, verification record | Treating an unverified commitment as closed |
| D-06 | Batch identity/genealogy resolution | Identity / genealogy / master-data owner | Manufacturing, warehouse, quality | MES genealogy, warehouse consumption records, product master | Resolving the SUA-88 genealogy break automatically |
| D-07 | PV seriousness, causality, expectedness, reportability determinations | PV medical/safety reviewer | PV case-intake staff, safety coder, product-quality linkage | ICSR data, duplicate/clock/terminology/listedness evidence | Final PV determinations |
| D-08 | Duplicate confirmation | PV reviewer | PV case-intake staff, safety coder | Duplicate candidates, similarity rationale, product-name evidence | Confirming duplicates automatically |
| D-09 | Awareness-date acceptance | PV case-intake staff / PV reviewer | Affiliate inbox, vendor, global safety DB inputs | Reporting-clock reconstruction evidence | Setting the reporting clock automatically |
| D-10 | Listedness determination per jurisdiction/source | PV medical reviewer / Regulatory Affairs | Labelling, RIM/IDMP, local affiliate | IB, core data sheet, local label versions, jurisdiction basis | Picking a listedness winner automatically |
| D-11 | Signal confirmation | Signal management | PV medical reviewer, biostatistics | Signal metrics, exposure estimates, case evidence | Confirming a signal automatically |
| D-12 | Allocation decision | Supply Chain VP / authorised Quality owner | Supply planners, procurement, CMO quality, patient-safety voice | Inventory, quality status, market authorisation, trial demand, constraints, cold-chain evidence | Allocating stock without human approval |
| D-13 | Cold-chain excursion disposition | Logistics / cold-chain accountable owner with Quality input | Quality, temperature-logger evidence, serialisation | Logger clock, pallet association, excursion evidence | Dispositioning the shipment automatically |
| D-14 | Recall decision | Quality / Regulatory accountable roles | Supply chain, safety, regulatory | Batch history, safety cases, distribution evidence | Initiating a recall automatically |
| D-15 | Exception override | Authorized human owner for the decision type | Relevant domain participants | Unresolved exception, reason, risk, evidence trail | Unowned or unexplained override |
| D-16 | Case closure / escalation closure | Accountable workflow owner | All relevant workflow owners | Evidence status, unresolved gaps, approvals, escalation outcome | Closing a case with unresolved mandatory states hidden |

---

## 5. Rules vs Reasoning Matrix

| Work Item | Deterministic Rule / Gate | Human Decision / Judgment | Draft or Reasoning Support Allowed | Forbidden Action | Audit Requirement |
|---|---|---|---|---|---|
| Batch identity/genealogy resolution | Genealogy completeness check; identity/product-code match | Identity/genealogy owner resolves the SUA-88 genealogy break | Reconcile MES genealogy with warehouse consumption; surface the break | Repairing the lineage or merging records automatically | Genealogy-break record, source records, owner |
| Unit conversion handling | Unit-conversion consistency check (mg/L vs µg/mL) | Laboratory/interface owner accepts the conversion with Quality approval | Surface the unit conflict; declare no-answer | Silent conversion or treating the assumption as approved | Conversion mapping, approval/override record |
| OOS/OOT disposition | Disputed result state remains open and visible | OOS owner disposes the investigation | Reconcile LIMS, statistical tool and notebook states | Dispositioning the assay automatically | Conflicting states, investigation record, disposition |
| Environmental-monitoring excursion disposition | Excursion evidence must stay visible | Quality/manufacturing owner disposes the excursion | Prepare excursion evidence and organism-identification correction | Hiding or dismissing the excursion | Excursion record, correction rationale, owner |
| Deviation/CAPA/change-control lineage | Lineage completeness visible | Quality/manufacturing owner concludes lineage | Link deviation, CAPA, change control and campaign evidence | Treating lineage as resolved without evidence | Lineage links, CAPA closure, change-control state |
| Release-packet completeness | Required-element completeness check | Quality release reviewer certifies readiness evidence | List packet elements and gaps | Claiming release-ready while elements are unresolved | Packet status, element checklist, gap ownership |
| Supplier-audit verification | Unverified commitment is not closed | Supplier-quality verifies and closes the commitment | Present audit commitment status | Treating the commitment as closed without verification | Verification record, packet status |
| QP certification | Batch-review readiness is not certification | EU QP certifies the batch | Prepare the certification evidence package | Automated QP certification | Pending-status record, evidence package, QP identity |
| Duplicate ICSR detection | Candidate similarity check surfaces candidates only | PV reviewer confirms duplicates | Surface duplicate candidates under different product names | Confirming or merging duplicates automatically | Duplicate rationale, candidates, reviewer |
| Awareness-date reconstruction | Clock reconstruction inputs complete | PV case-intake staff/PV reviewer accepts the date | Reconstruct the reporting clock from receipts | Setting the clock automatically | Clock-reconstruction evidence, source basis |
| MedDRA terminology normalisation | Version consistency resolved before output | Safety coder/terminology owner aligns terminology | Present version mismatch evidence | Choosing the preferred term automatically | Version-alignment evidence, source |
| Listedness/expectedness determination | Listedness sources remain conflict-visible | PV medical reviewer/Regulatory determines per jurisdiction | Compare IB, CCDS and local label | Picking a listedness winner automatically | Listedness-source versions, determination record |
| Product-quality complaint linkage | Quality-complaint linkage visible | PV/quality owner disposes the linkage | Link product-quality complaints to cases and batches | Treating linkage as disposition | Complaint records, linkage, owner |
| Cold-chain excursion disposition | Cold-chain evidence resolved before options trusted | Logistics/Quality owner disposes the excursion | Present logger clock, pallet association and aggregation evidence | Dispositioning the shipment automatically | Logger basis, pallet link, excursion evidence |
| Serialisation aggregation | Aggregation gaps remain visible | Serialisation owner resolves linkage evidence | Surface missing case-to-pallet aggregation | Assuming the aggregation link | Aggregation-state record, gap ownership |
| Allocation option preparation | Constraint check completed; options policy-bounded | Supply planner prepares traceable options | Generate options from inventory, quality status, authorisations, constraints | Executing an allocation | Option rationale, evidence used, status |
| Allocation approval | No allocation without explicit authorised human approval | Supply Chain VP / authorised Quality owner approves | Prepare approval request with option evidence | Allocating stock, reserving capacity, shipping without approval | Approval request, human approval, action record |
| Recall consideration | Recall initiation requires human decision | Quality/Regulatory owner decides | Prepare recall-candidate evidence | Initiating a recall automatically | Recall consideration record, decision, owner |
| Inspection-evidence packaging | Evidence package preserves traceability | Regulatory/quality participant packages for inspection | Assemble batch, trial, safety and AI-control evidence | Packaging that creates or hides evidence | Package manifest, source citations, timeline |
| Escalation creation/closure | Unresolved state requires escalation, not guessing | Accountable workflow owner owns escalation | Create escalation with ownership and status | Closing escalation without outcome or owner | Escalation record, owner, status, outcome |
| Case closure | Closure requires resolved or owned states | Accountable workflow owner closes the case | Prepare closure-readiness evidence pack | Closing with unresolved mandatory states hidden | Evidence status, gaps, approvals, closure record |
| Exception override | Override requires authorized owner and reason | Authorized human owner approves the override | Prepare unresolved-exception evidence | Silent or unowned override | Override owner, reason, evidence, timestamp |

---

## 6. Forbidden Automation / Forbidden Delegation List

The workshop team must not delegate the following away from accountable human owners:

```text
Batch release
Batch rejection
Batch reprocess
Batch re-label
Batch recall
QP certification (final batch certification)
Final PV seriousness determination
Final PV causality determination
Final PV expectedness determination
Final PV reportability determination
Signal confirmation
Inventory status change
Capacity reservation
Stock allocation
Shipment initiation
Recall initiation
Formulation changes
Specification changes
Clinical eligibility decisions
Safety-case disposition
OOS/OOT disposition
Cold-chain excursion disposition
Duplicate confirmation
Awareness-date acceptance
Listedness winner selection
Silent unit conversion
Silent genealogy repair
Consent/entitlement exception handling
Exception override without authorized owner and reason
Treating ambiguity as completeness
Any action that removes auditability from recommendation, draft, approval, override, release, escalation, action, outcome, or closure
```

---

## 7. Approval Gates and Stop Gates

### Approval Gates

| Gate | Required Human Owner | What Must Exist Before Approval |
|---|---|---|
| QP certification / batch release | EU Qualified Person / Quality release reviewer | Complete, conflict-visible batch-review readiness package; resolved or owned genealogy, unit, OOS/OOT, supplier-evidence and release-packet state |
| OOS/OOT disposition | Laboratory analyst / OOS owner | Investigation record, conflicting result states, supporting lab evidence |
| Unit-conversion acceptance | Laboratory / interface owner with Quality acceptance | Approved conversion mapping and unit-consistency evidence |
| Supplier-audit commitment closure | Supplier-quality / quality reviewer | Independent verification of the commitment |
| PV disposition (seriousness/causality/expectedness/reportability) | PV medical/safety reviewer | Prepared case-review material with duplicate/clock/terminology/listedness evidence |
| Allocation approval | Supply Chain VP / authorised Quality owner | Traceable options, constraint rationale, inventory/quality/cold-chain evidence |
| Cold-chain excursion disposition | Logistics / cold-chain accountable owner with Quality input | Resolved logger clock, pallet association and aggregation evidence |
| Recall decision | Quality / Regulatory accountable roles | Batch history, safety case, distribution and quality evidence |
| Exception override | Authorized human owner | Exception details, evidence, reason, owner, risk visibility |

### Stop Gates

| Stop Gate | Stop Condition | Reason |
|---|---|---|
| Unresolved identity/genealogy | Product/batch/compound identity or genealogy state unresolved (SUA-88 break) | No evidence output while identity or lineage is unresolved |
| Unresolved unit state | mg/L vs µg/mL assumption unapproved | No silent conversion; fail-closed on unit state |
| Unresolved terminology state | Two MedDRA versions changing the preferred term | No evidence output while terminology is unresolved |
| Unresolved authority/effective-date/jurisdiction | Authority hierarchy inconsistent; amendment not approved in one country | A later timestamp is not automatically authoritative |
| Unresolved consent/entitlement | eConsent version asynchrony with the trial amendment | No patient/participant data surfaced without lawful basis |
| Unresolved validation/checkpoint state | Validation-state ambiguity; back-entered step checkpoint missing | No evidence output while validation or checkpoint state is unresolved |
| Incomplete release packet | Release-packet elements unresolved or unverified | Batch must not be shown release-ready |
| Unverified supplier-audit commitment | Commitment claimed closed but not verified | An unverified commitment is not closed |
| Missing audit trail | Required evidence, owner, decision, approval, override, or timestamp missing | The 47-minute audit-capture gap remains visible; nothing is treated as auditable |

### Escalation Gates

| Escalation Gate | Escalation Trigger | Required Response |
|---|---|---|
| Genealogy gap escalation | SUA-88 genealogy break with conflicting warehouse consumption evidence | Record the gap with identity/lineage ownership; route to accountable owner |
| Unit-conversion escalation | Unapproved mg/L vs µg/mL assumption affects batch or safety evidence | Declare no-answer; route conversion acceptance to laboratory/quality owner |
| OOS/OOT dispute escalation | LIMS, statistical tool and notebook disagree with open investigation | Keep dispute visible; route to OOS owner |
| Supplier-audit escalation | Contract-site audit commitment unverified in the EU release packet | Keep packet incomplete; route verification to supplier-quality |
| PV clock/duplicate/terminology/listedness escalation | Disputed awareness date, duplicate candidates, MedDRA mismatch, listedness conflict | Prepare evidence for accountable PV review; do not settle the dispute |
| Cold-chain escalation | Logger clock/pallet dispute or missing aggregation | Keep evidence unresolved; route to logistics/quality owner |
| Shortage/capacity escalation | Excipient shortage, CMO capacity conflict, demand exceeds stock | Prepare policy-bounded options; request authorised human approval |
| Audit-gap escalation | 47-minute audit-capture gap during master-data repair | Keep gap visible with owner; do not fill silently |
| Inspection escalation | Multi-agency request within 72 hours | Assemble traceable evidence package; escalate missing evidence state |

### Closure Gates

| Closure Gate | Closure Condition |
|---|---|
| Escalation closure | Outcome recorded by accountable owner; unresolved state still visible if not resolved |
| Release-packet closure (evidence) | Genealogy branches, unit state, OOS/OOT state, supplier evidence and packet elements resolved or owned with gaps visible |
| PV intake closure (support) | Case-review material complete and routed; final PV decisions remain with reviewers |
| Supply option closure | Options approved by authorised human or explicitly closed without execution |
| Inspection-evidence closure | Evidence package manifest complete and traceable; gaps owned |
| Case closure | Mandatory evidence states resolved or owned; approvals and evidence trail exist |

---

## 8. Audit and Evidence Obligations

At Stage 8, the following must be auditable:

```text
Batch identity and product-master references
Genealogy check and genealogy-break identification (SUA-88)
Warehouse consumption evidence
Unit-conversion conflict and no-answer declaration
OOS/OOT/invalid dispute and open investigation state
Environmental-monitoring excursion and organism-identification correction
Deviation, CAPA, change-control and cleaning-validation lineage
Release-packet element completeness
Supplier-audit verification and commitment closure
Batch-review readiness assessment and QP pending status
PV intake, receipts, duplicate rationale, clock reconstruction, MedDRA version, listedness sources
Consent/entitlement checks before patient/participant data is surfaced
Cold-chain logger basis, pallet association, aggregation state, excursion evidence
Shortage, capacity conflict, allocation constraints, allocation options, approval requests and approvals
Recall consideration and decision
Escalation creation, ownership, action, outcome and closure
Approval, override, release, action, outcome and closure records
Inspection evidence package manifest and source citations
The 47-minute audit-capture gap and AI-off continuity state
```

Each audit record should preserve:

```text
batch / product / case / shipment / source identity
source evidence and provenance citation
owner / role
status
decision or action
approval / rejection / override where applicable
reason where applicable (e.g., no-answer reason, override reason)
timestamp
release or closure status where applicable
```

---

## 9. Stage 8 Quality Check

Use this checklist before moving to Stage 9:

```text
No batch, safety, quality or supply issue has been solved in this artifact.
No batch release/rejection/reprocess/re-label/recall decision has been made or implied.
No QP certification has been implied.
No final PV seriousness, causality, expectedness, reportability or signal-confirmation decision has been made.
No inventory status change, capacity reservation, stock allocation, shipment or recall initiation has been implied.
All regulated decisions remain human-owned with named accountable roles.
Fail-closed rules block evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
Deterministic rules include genealogy completeness, unit-conversion consistency, MedDRA-version consistency, entitlement/consent gate, checkpoint-state completeness and release-packet element completeness.
Duplicate detection is candidate-only; the reporting clock is evidence, not a decision; listedness conflicts remain visible.
All unresolved case exceptions remain visible as gaps with owners.
Every rule has an owner and audit requirement.
Every judgment decision has an accountable human owner.
Forbidden actions are explicit.
Approval gates, stop gates, escalation gates, and closure gates are separated with accountable roles.
Evidence and audit obligations are clear enough to support the next stage.
No architecture, RAG, MCP, agents, APIs, or implementation design has been introduced.
```

---

## 10. NEXT_STAGE_INPUT_BLOCK

```text
Stage 9 Input — Source / Evidence Governance Handoff

Final Rules vs Reasoning Summary:
Stage 8 separates NovaCura Therapeutics Group's batch-review, PV case-intake and supply-recovery work into deterministic rules, workflow gates, human-owned decisions, support-only activities, forbidden actions, and audit obligations. The case remains unresolved. The artifact only defines how decisions and workflow gaps must be governed, with regulated accountability preserved for Quality, Safety, Regulatory, Clinical and Supply roles.

Deterministic Rules:
- Evidence output requires resolved product/batch/compound identity.
- Genealogy completeness must be checked before batch evidence output; all branches present and linked.
- A batch must not be shown as release-ready while any genealogy branch or release-packet element is unresolved or unverified.
- Unit-conversion consistency must be resolved before output (mg/L vs µg/mL).
- Identity/product-code match check.
- Disputed OOS/OOT/notebook-invalid result state remains open and visible.
- Unverified supplier-audit commitments are not treated as closed.
- Back-entered batch-record steps require checkpoint and audit evidence.
- Validation-state consistency must be checked before evidence output.
- Entitlement/consent gate must pass before patient/participant data is surfaced.
- Checkpoint-state completeness check before evidence output.
- Required release-packet element completeness check.
- MedDRA version consistency must be resolved before terminology output.
- Duplicate-ICSR candidate similarity check surfaces candidates only.
- Reporting-clock reconstruction inputs must be complete.
- The audit-capture gap remains visible and is not filled silently.
- Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable.

Human-Owned Decisions:
- Batch release/rejection/reprocess/re-label: EU Qualified Person / Quality release reviewer.
- QP certification: EU Qualified Person.
- OOS/OOT disposition and investigation conclusion: Laboratory analyst / OOS owner.
- Unit-conversion acceptance: Laboratory / interface owner with Quality acceptance.
- Supplier-audit verification and commitment closure: Supplier-quality / quality reviewer.
- Batch identity/genealogy resolution: Identity / genealogy / master-data owner.
- PV seriousness, causality, expectedness, reportability determinations: PV medical/safety reviewer.
- Duplicate confirmation: PV reviewer.
- Awareness-date acceptance: PV case-intake staff / PV reviewer.
- Listedness determination per jurisdiction/source: PV medical reviewer / Regulatory Affairs.
- Signal confirmation: Signal management.
- Allocation decision: Supply Chain VP / authorised Quality owner.
- Cold-chain excursion disposition: Logistics / cold-chain accountable owner with Quality input.
- Recall decision: Quality / Regulatory accountable roles.
- Exception override: authorized human owner.
- Case/escalation closure: accountable workflow owner.

Support-Only Activities:
- Reconcile batch genealogy and surface genealogy breaks with ownership.
- Surface unit-conversion conflicts and declare no-answer.
- Reconcile LIMS, statistical tool and notebook states without disposition.
- Prepare environmental-excursion and organism-correction evidence.
- Link deviation, CAPA, change control and cleaning-validation evidence.
- List release-packet elements and evidence gaps.
- Present supplier-audit commitment status.
- Prepare the QP-certification evidence package.
- Surface duplicate candidates, clock-reconstruction evidence, MedDRA version mismatch and listedness-source conflicts.
- Present logger clock, pallet association, aggregation and excursion evidence.
- Generate traceable allocation options with constraint rationale.
- Assemble inspection-evidence packages with manifests.
- Organize evidence and audit references for escalation, approval, override and closure.

Forbidden Actions:
- Batch release/rejection/reprocess/re-label/recall.
- QP certification.
- Final PV seriousness, causality, expectedness, reportability determinations.
- Signal confirmation.
- Inventory status change, capacity reservation, stock allocation, shipment initiation.
- Recall initiation.
- Formulation, specification, clinical eligibility or safety-case disposition changes.
- Silent unit conversion.
- Silent genealogy repair.
- Duplicate confirmation or merge/split of cases.
- Setting the reporting clock.
- Picking a listedness winner.
- OOS/OOT or cold-chain excursion disposition.
- Consent/entitlement override.
- Exception override without authorized owner and reason.
- Treating ambiguity as completeness.
- Any unaudited recommendation, draft, approval, override, release, escalation, action, outcome or closure.

Approval / Stop / Escalation / Closure Gates:
- Approval gates: QP certification/batch release (EU QP / Quality release reviewer), OOS/OOT disposition (OOS owner), unit-conversion acceptance (Laboratory/interface owner with Quality), supplier-audit commitment closure (Supplier-quality), PV disposition (PV medical reviewer), allocation approval (Supply Chain VP / authorised Quality owner), cold-chain excursion disposition (Logistics/Quality owner), recall decision (Quality/Regulatory roles), exception override (authorized human owner).
- Stop gates: unresolved identity/genealogy, unresolved unit state, unresolved terminology state, unresolved authority/effective-date/jurisdiction, unresolved consent/entitlement, unresolved validation/checkpoint state, incomplete release packet, unverified supplier-audit commitment, missing audit trail.
- Escalation gates: genealogy gap, unit-conversion conflict, OOS/OOT dispute, supplier-audit gap, PV clock/duplicate/terminology/listedness disputes, cold-chain logger/pallet/aggregation dispute, shortage/capacity conflict, 47-minute audit-capture gap, multi-agency inspection request.
- Closure gates: escalation closure, release-packet evidence closure, PV intake support closure, supply option closure, inspection-evidence closure, case closure.

Evidence and Audit Obligations:
- Batch/product/case/shipment/source identity.
- Source evidence and provenance citation.
- Owner / role.
- Status and timestamp.
- Decision or action taken.
- Approval, rejection, or override where applicable.
- Reason where applicable (no-answer reason, override reason).
- Release or closure status where applicable.
- Escalation action and outcome where applicable.
- The audit-capture gap and AI-off continuity state remain visible.

Source / Evidence Needs for Next Stage:
- Product master, batch record, MES genealogy, warehouse consumption records.
- Lab results, interface mappings, LIMS OOS, statistical OOT, laboratory notebook.
- Environmental monitoring and microbiology results.
- Deviation, CAPA, change-control and cleaning-validation records.
- Release-packet checklist and evidence-gap list.
- Supplier audit reports and commitment-verification records.
- Batch-review readiness package and QP-certification evidence.
- Safety receipts (vendor, affiliate inbox, global safety DB), ICSR candidates, MedDRA versions, IB/CCDS/local labels.
- Temperature logger records, pallet-association and serialisation-aggregation records.
- Inventory, quality status, market authorisations, demand forecast, allocation policy, CMO capacity, supplier-risk records.
- Validation inventory, source/document governance records, audit trails, downtime records, continuity requirements.
- Non-negotiables and Stage 8 rule/decision registers.

Open Questions:
- Which source documents are authoritative for each rule and decision, per business object, jurisdiction and effective date?
- Which source documents are approved for internal review versus external/inspection packaging?
- Which source documents need owner, version, effective date, review date and applicability metadata?
- Which evidence sources are required before a draft, approval, override, escalation, release or closure can be audited?
- Which supplier documents (including the untrusted deviation PDF and tool manifests) require quarantine and governance before use?
- Which source gaps prevent safe evidence-backed workflow completion?
- Which policies define authority, validation state, consent/entitlement, release-packet requirements, reporting-clock reconstruction, listedness sources, allocation constraints and recall criteria?
```

Stage 8 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 9.
