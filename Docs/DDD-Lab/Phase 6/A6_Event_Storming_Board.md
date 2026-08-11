# A6 — Event Storming Board: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## 1. Stage 6 Mission

Stage 6 converts the Stage 5 context map into a business-domain event storming board for the NovaCura Therapeutics Group governed evidence-reconciliation case. The purpose is to identify what happens in batch review, pharmacovigilance case intake and supply recovery, what triggers those events, which human roles participate, which bounded context is involved, which policy or business rule applies, what can fail, and what evidence must be captured.

This stage does not solve batch, safety or supply issues, approve batch release or rejection, disposition safety cases, allocate stock, ship product, initiate recalls, provide medical, regulatory or legal advice, create architecture, or introduce technical implementation. It only captures business events, commands, policies, exceptions, ownership, and audit needs. The AI remains read-only and advisory and must abstain (no-answer) where any required state is unresolved.

## 2. Input Summary

The Stage 6 input comes from the Stage 5 context map for the NovaCura Therapeutics Group governed evidence-reconciliation case.

The business scenario concerns the disputed biologics batch NCB204-B24071 (missing single-use assembly lot SUA-88 genealogy branch, mg/L vs µg/mL unit-conversion assumption, disputed OOS/OOT state, unverified supplier-audit commitment, back-entered batch-record step), a sterile-area excursion near fill-finish with a corrected organism identification, emerging safety reports (duplicate ICSR candidates under different product names, disputed awareness date, MedDRA version mismatch, listedness conflict between IB, CCDS and local label), a cold-chain failure (disputed logger clocks and pallet association, missing serialisation aggregation), a sole-source excipient shortage with CMO capacity conflict and demand exceeding stock, a ransomware event with a 47-minute audit-capture gap, and a multi-agency inspection request within 72 hours.

The Stage 5 context map identified these bounded contexts:

1. Identity, Genealogy and Product Master Context
2. GxP Batch Evidence Reconciliation Context
3. Unit and Terminology Standardisation Context
4. Authority, Effective-Date and Jurisdiction Context
5. Consent, Entitlement and Privacy Context
6. PV Case Intake and Signal Support Context
7. Supply, Cold-Chain and Allocation Planning Context
8. Source and Document Governance Context
9. Supplier and Audit Evidence Context
10. Audit, Evidence and Continuity Context

Key unresolved gaps carried into Stage 6:

- Genealogy branch gap for SUA-88 with a warehouse consumption record.
- Unapproved mg/L vs µg/mL unit-conversion assumption.
- Disputed OOS/OOT/notebook-invalid state with an open investigation.
- Unverified contract-site audit commitment in the EU release packet.
- Back-entered batch-record step; 47-minute audit-capture gap.
- Disputed PV awareness date; duplicate ICSR cluster; MedDRA version mismatch; listedness conflict.
- Cold-chain logger clock and pallet association dispute; missing serialisation aggregation.
- Sole-source excipient shortage with eight-week recovery; CMO capacity conflict; demand exceeds stock.
- Validation-state ambiguity; untrusted supplier deviation PDF and tool manifests; eConsent version asynchrony.

Non-negotiables carried into event storming:

- The AI never releases, rejects, reprocesses, re-labels or recalls a batch.
- The AI never makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions.
- The AI never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval.
- The AI never changes formulation, specification, clinical eligibility, safety-case disposition, batch release or recall decisions.
- Regulated accountability remains with the accountable Quality, Safety, Regulatory, Clinical and Supply roles.
- Evidence output must not be produced while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
- Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable.
- The system operates read-only and advisory; it prepares, reconciles, explains and packages evidence.
- No product, batch, safety, quality or supply issue is considered resolved merely because it has been identified.

## 3. Event Storming Principles

- Domain events are written as things that happened in the business workflow.
- Commands or activities are written as requests/actions that may trigger events.
- Events must stay in pharmaceutical business language, not technical language.
- Events do not imply batch, safety or supply resolution unless the case evidence explicitly says so.
- Batch release, rejection, reprocess, re-label, recall and QP certification remain human-owned by accountable Quality and EU QP roles.
- Final PV seriousness, causality, expectedness, reportability and signal-confirmation decisions remain human-owned by accountable PV roles.
- Inventory status change, capacity reservation, stock allocation, shipment and recall initiation require explicit authorised human approval.
- The AI prepares, reconciles, explains and packages evidence only; it must declare abstention/no-answer where identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
- Unit-conversion, terminology, identity, genealogy and authority conflicts remain visible as exceptions; they are not resolved in this stage.
- Untrusted sources and ambiguous validation states remain quarantined or unresolved; they are not treated as usable evidence.
- Auditability is treated as part of the business workflow, not an afterthought.
- Every major event should expose actor, trigger, bounded context, policy, failure condition, and evidence need.

## 4. Event Timeline Overview

```text
Batch review opened for NCB204-B24071
→ Batch identity and product-master state checked
→ Genealogy check requested
→ Genealogy branch gap detected (SUA-88)
→ Warehouse consumption record found for SUA-88
→ Unit-conversion conflict detected (mg/L vs µg/mL)
→ Unit-conversion state declared unresolved (no-answer)
→ OOS/OOT state disagreement surfaced
→ Sterile-area excursion near fill-finish detected
→ Organism identification corrected after initial review
→ Supplier-audit commitment verification requested
→ Supplier-audit commitment found unverified
→ Back-entered batch-record step detected
→ Release packet marked evidence-incomplete
→ Batch-review readiness assessed with unresolved gaps
→ QP certification decision pending

PV case intake opened
→ Consent/entitlement check requested for participant data use
→ ICSR duplicate cluster identified
→ Awareness-date dispute surfaced
→ MedDRA preferred-term conflict surfaced
→ Listedness conflict surfaced (IB vs CCDS vs local label)
→ Reporting-clock evidence prepared for review
→ Multilingual review requested
→ Case-review material prepared for accountable PV review

Cold-chain excursion detected (logger clock/pallet disputed)
→ Case-to-pallet aggregation gap detected
→ Serialisation aggregation gap detected
→ Excipient shortage surfaced
→ CMO capacity conflict surfaced
→ Allocation constraint check completed
→ Allocation option proposed (awaiting human approval)
→ Human approval requested for allocation option

Validation state found ambiguous
→ Master-data repair window opened
→ Audit record captured
→ Audit-capture gap detected (47 minutes)
→ AI-off continuity mode activated
→ Inspection evidence request received (72h)
→ Evidence package assembled for inspection
→ Escalation created for unresolved evidence state
→ No-answer (abstention) declared where required state unresolved
→ Human approval recorded
→ Human override recorded
```

## 5. Event Storming Board

| Seq | Domain event | Event type | Triggering command / activity | Primary actor / human role | Bounded context | Policy or business rule | Evidence source | Failure or exception condition | Audit / evidence need |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | Batch review opened for NCB204-B24071 | Workflow event | Open batch review | Quality release reviewer | GxP Batch Evidence Reconciliation Context | Batch-review readiness requires evidence-complete, conflict-visible material | Batch record, review request | Review may be opened without identity/lineage readiness | Review opening, owner, batch identity |
| 2 | Batch identity and product-master state checked | Identity event | Verify batch and product identity | Quality / manufacturing / master-data participant | Identity, Genealogy and Product Master Context | No evidence output while identity state is unresolved | Product master, batch record, RIM/IDMP reference | Product or batch identity may be ambiguous across systems | Identity-match evidence and source |
| 3 | Genealogy check requested | Identity event | Request lineage check | Quality release reviewer / manufacturing | Identity, Genealogy and Product Master Context | Lineage must be visible and complete or flagged before review can proceed | MES/eBR genealogy, warehouse records | Lineage may be incomplete without visibility | Genealogy check request and source |
| 4 | Genealogy branch gap detected (SUA-88) | Exception event | Detect missing lineage branch | Identity/genealogy owner | Identity, Genealogy and Product Master Context | Genealogy breaks remain visible; they are never silently repaired | MES genealogy branch, warehouse consumption record | SUA-88 present in warehouse consumption but missing from one MES branch | Gap description, owner, source records |
| 5 | Warehouse consumption record found for SUA-88 | Evidence event | Search warehouse consumption records | Warehouse / manufacturing participant | Identity, Genealogy and Product Master Context | Contradictory lineage evidence must remain visible | Warehouse consumption record | Consumption evidence may conflict with MES branch | Consumption record and source attribution |
| 6 | Unit-conversion conflict detected (mg/L vs µg/mL) | Exception event | Compare reported vs assumed units | Laboratory / interface participant | Unit and Terminology Standardisation Context | Conversion assumptions must be approved; no silent conversion | Contract-lab result, receiving-interface mapping | Contract-lab concentration in mg/L, receiving interface assumes µg/mL | Conversion conflict, mapping, unit state |
| 7 | Unit-conversion state declared unresolved (no-answer) | Abstention event | Abstain on unresolved unit state | Quality / laboratory owner | Unit and Terminology Standardisation Context | No evidence output while unit state is unresolved | Unit-conversion assumption status | Unapproved conversion may be treated as usable | No-answer declaration and reason |
| 8 | OOS/OOT state disagreement surfaced | Exception event | Surface conflicting result states | Laboratory analyst / OOS owner | GxP Batch Evidence Reconciliation Context + Unit and Terminology Standardisation Context | Disputed result states remain conflict-visible; no disposition | LIMS OOS, statistical OOT tool, laboratory notebook | LIMS marks OOS, tool marks OOT, notebook labels invalid | Conflicting states, sources, open investigation |
| 9 | Sterile-area excursion near fill-finish detected | Quality-event event | Report environmental excursion | Manufacturing / sterile-fill participant | GxP Batch Evidence Reconciliation Context | Excursions affect batch-review readiness evidence | Environmental monitoring records | Excursion near fill-finish may affect campaign evidence | Excursion record and monitoring evidence |
| 10 | Organism identification corrected after initial review | Correction event | Correct organism identification | Microbiology / laboratory reviewer | GxP Batch Evidence Reconciliation Context | Corrections must remain visible with rationale | Microbiology results, review record | Initial identification was corrected after review | Correction rationale and reviewer |
| 11 | Supplier-audit commitment verification requested | Supplier-evidence event | Request commitment verification | Supplier-quality / quality reviewer | Supplier and Audit Evidence Context | Audit commitments must be independently verified | Audit report, release packet checklist | EU release packet lacks confirmation of one contract-site audit commitment | Verification request and owner |
| 12 | Supplier-audit commitment found unverified | Exception event | Check commitment verification state | Supplier-quality participant | Supplier and Audit Evidence Context + GxP Batch Evidence Reconciliation Context | An unverified commitment is not closed | Supplier-audit records, release packet | Commitment claimed closed but not independently verified | Unverified status, source, owner |
| 13 | Back-entered batch-record step detected | Exception event | Detect back-entered record | Manufacturing / quality reviewer | GxP Batch Evidence Reconciliation Context + Audit, Evidence and Continuity Context | Back-entered records require checkpoint and audit evidence | eBR step timestamps, downtime records | Batch-record step back-entered after network degradation | Detection record, timestamps, checkpoint state |
| 14 | Release packet marked evidence-incomplete | Exception event | Assess release-packet completeness | Quality release reviewer | GxP Batch Evidence Reconciliation Context | Evidence-incomplete packet is not batch-review ready | Release packet, evidence-gap list | Missing supplier-audit confirmation, unresolved unit/OOS state | Packet status, gap list, owner |
| 15 | Batch-review readiness assessed with unresolved gaps | Status event | Assess batch-review readiness | Quality release reviewer | GxP Batch Evidence Reconciliation Context | Readiness is review readiness, not release approval | Readiness checklist, known gaps | Gaps may be hidden or treated as complete | Readiness assessment, gap ownership |
| 16 | QP certification decision pending | Human-decision event | Prepare evidence for QP certification | EU Qualified Person | GxP Batch Evidence Reconciliation Context + Quality ownership | QP certification is a human batch-certification decision; AI prepares evidence only | Batch-review readiness package, release packet | Certification may be considered without complete reliable evidence | Pending-decision status, evidence package, QP identity |
| 17 | PV case intake opened | Workflow event | Open PV case intake | PV case-intake staff | PV Case Intake and Signal Support Context | Intake completeness must be supported without final PV decisions | ICSR receipts, safety sources | Intake may be incomplete or mis-attributed | Intake opening, source receipts |
| 18 | Consent/entitlement check requested for participant data use | Control event | Validate consent and entitlement | Data Protection Officer / privacy owner | Consent, Entitlement and Privacy Context | No data access or use without lawful basis and entitlement | eConsent, entitlement records | eConsent version asynchrony with trial amendment | Consent/entitlement check and result |
| 19 | ICSR duplicate cluster identified | Exception event | Detect duplicate candidates | PV case-intake staff | PV Case Intake and Signal Support Context + Unit and Terminology Standardisation Context | Duplicate candidates remain pending accountable review | Safety receipts, product names, terminology | Cases likely describe the same event under different product names | Duplicate rationale, candidates, reviewer |
| 20 | Awareness-date dispute surfaced | Exception event | Reconstruct reporting clock | PV case-intake staff / PV reviewer | PV Case Intake and Signal Support Context + Authority, Effective-Date and Jurisdiction Context | Reporting clock is evidence for review; the clock is not set automatically | Vendor receipt, affiliate inbox, global safety DB | Awareness date differs across sources | Clock reconstruction evidence, source basis |
| 21 | MedDRA preferred-term conflict surfaced | Exception event | Align terminology versions | Safety coder / terminology owner | Unit and Terminology Standardisation Context + PV Case Intake and Signal Support Context | Terminology state remains conflict-visible | Two MedDRA versions | Version mismatch changes the preferred term | Version alignment evidence and source |
| 22 | Listedness conflict surfaced (IB vs CCDS vs local label) | Exception event | Compare listedness sources | PV medical reviewer / regulatory participant | PV Case Intake and Signal Support Context + Authority, Effective-Date and Jurisdiction Context + Source and Document Governance Context | Listedness sources remain conflict-visible; no winner is picked | IB, CCDS, local label | Sources not aligned on expectedness | Listedness evidence and source versions |
| 23 | Reporting-clock evidence prepared for review | Review-preparation event | Prepare clock evidence | PV case-intake staff | PV Case Intake and Signal Support Context | Case intake prepares evidence; final PV decisions remain human-owned | Receipts, awareness-date reconstruction | Clock evidence may be incomplete or disputed | Prepared evidence and source citations |
| 24 | Multilingual review requested | Review event | Request multilingual review | PV medical/safety reviewer | PV Case Intake and Signal Support Context | Multilingual material supports review; it does not decide | Case text, translation evidence | Review may proceed without multilingual completeness | Review request, language scope, reviewer |
| 25 | Case-review material prepared for accountable PV review | Review-preparation event | Prepare case-review material | PV case-intake staff | PV Case Intake and Signal Support Context | Intake and support never make final seriousness, causality, expectedness, reportability or signal decisions | ICSR data, duplicate/clock/listedness evidence | Material may omit disputed states | Prepared material, sources, routing |
| 26 | Cold-chain excursion detected (logger clock/pallet disputed) | Exception event | Detect temperature excursion | Logistics / cold-chain participant | Supply, Cold-Chain and Allocation Planning Context + Authority, Effective-Date and Jurisdiction Context | Cold-chain evidence must be resolved before options are trusted | Temperature loggers, shipment records | Logger clock and pallet association disputed | Excursion evidence, logger basis, pallet link |
| 27 | Case-to-pallet aggregation gap detected | Exception event | Detect aggregation gap | Serialisation / logistics participant | Identity, Genealogy and Product Master Context + Supply, Cold-Chain and Allocation Planning Context | Aggregation gaps remain visible with ownership | Serialisation events, packaging records | Case-to-pallet aggregation missing after line restart | Gap identification and linkage evidence |
| 28 | Serialisation aggregation gap detected | Exception event | Check aggregation hierarchy | Serialisation participant | Identity, Genealogy and Product Master Context | Aggregation state must be visible before shipment evidence is trusted | Serialisation events | Missing linkage after line restart | Aggregation state and owner |
| 29 | Excipient shortage surfaced | Exception event | Surface shortage | Supply planner / procurement | Supply, Cold-Chain and Allocation Planning Context + Supplier and Audit Evidence Context | Shortage constraints generate options; no allocation without approval | Supplier risk, inventory, recovery estimate | Sole-source contamination, eight-week recovery | Shortage record, supplier source, estimate |
| 30 | CMO capacity conflict surfaced | Exception event | Surface capacity conflict | CMO quality / procurement | Supply, Cold-Chain and Allocation Planning Context + Supplier and Audit Evidence Context | Competing capacity commitments remain a visible sourcing constraint | CMO portals, contracts | CMO promises capacity to two sponsors | Capacity conflict evidence and source |
| 31 | Allocation constraint check completed | Planning event | Check allocation constraints | Supply planner | Supply, Cold-Chain and Allocation Planning Context | Options must respect market authorisation, trial demand, compassionate-use and policy | Allocation policy, demand forecast, entitlements | Constraints may be overlooked | Constraint-check result and rationale |
| 32 | Allocation option proposed (awaiting human approval) | Advisory event | Generate traceable options | Supply planner | Supply, Cold-Chain and Allocation Planning Context | Options are advisory; no inventory status change, reservation, allocation, shipment or recall without approval | Inventory, quality status, cold-chain evidence, policy | A proposed option may be mistaken for an executed allocation | Option rationale, evidence used, status |
| 33 | Human approval requested for allocation option | Human-decision event | Request authorised approval | Supply Chain / Quality accountable owner | Supply, Cold-Chain and Allocation Planning Context + authorised human ownership | Explicit authorised human approval is required before any allocation action | Option proposal, escalation record | Approval may be assumed or bypassed | Approval request, owner, option reference |
| 34 | Validation state found ambiguous | Exception event | Check validation state | Validation / quality owner | Authority, Effective-Date and Jurisdiction Context + Audit, Evidence and Continuity Context | Ambiguous validation state remains unresolved; no evidence output | Validation inventory, system records | Validated vs conditionally released vs research-only across inventories | Validation-state evidence and owner |
| 35 | Master-data repair window opened | Continuity event | Open repair window | IT operations / master-data owner | Audit, Evidence and Continuity Context | Audit capture must remain complete during repair | Downtime records, change control | Repair may run without full audit capture | Repair window record and timeline |
| 36 | Audit record captured | Audit event | Capture audit event envelope | Audit/quality oversight | Audit, Evidence and Continuity Context | Every recommendation, draft, approval, override, release, escalation, action, outcome and closure is auditable | Audit trail | Events may occur without audit capture | Audit event envelope, timestamp, source |
| 37 | Audit-capture gap detected (47 minutes) | Exception event | Detect audit-capture gap | Audit/quality oversight | Audit, Evidence and Continuity Context | Audit-trail completeness gaps remain visible; they are not filled silently | Audit trail, downtime records | Audit capture disabled 47 minutes during master-data repair | Gap detection, duration, owner |
| 38 | AI-off continuity mode activated | Continuity event | Activate AI-off operation | CISO / IT operations | Audit, Evidence and Continuity Context | The organisation must operate safely without AI | Continuity requirements, incident record | Operation may stall without AI | Activation record and continuity state |
| 39 | Inspection evidence request received (72h) | Regulatory event | Receive multi-agency request | Regulatory Affairs / quality oversight | Audit, Evidence and Continuity Context + all evidence contexts | Traceable evidence across trial, batch, safety and AI-system controls within 72 hours | Inspection request | Evidence may be incomplete or untraceable | Request record, timeline, scope |
| 40 | Evidence package assembled for inspection | Evidence event | Assemble evidence package | Regulatory / quality participant | Audit, Evidence and Continuity Context | Packaging preserves traceability; it does not create evidence | Batch history, safety cases, trial data, AI-system controls | Package may omit unresolved states or gaps | Package manifest and source citations |
| 41 | Escalation created for unresolved evidence state | Escalation event | Escalate unresolved state | Accountable workflow owner | All contexts via governance | Unresolved identity, genealogy, unit, terminology, authority, consent, validation or checkpoint state requires escalation, not guessing | Escalation record, gap state | Escalation may be created but never owned | Escalation record, owner, status |
| 42 | No-answer (abstention) declared where required state unresolved | Abstention event | Abstain on unresolved state | AI advisory capability / accountable owner | All contexts | No evidence output while any required state is unresolved | Abstention declaration | A guess may be produced instead of an honest abstention | No-answer declaration and reason |
| 43 | Human approval recorded | Approval event | Record human approval | Accountable Quality / PV / Supply / Regulatory owner | Decision-owning context + Audit, Evidence and Continuity Context | Regulated decisions require human approval with audit trail | Approval record | Approval may be missing, ambiguous, or bypassed | Approver, timestamp, scope, evidence |
| 44 | Human override recorded | Override event | Record human override | Accountable owner | Decision-owning context + Audit, Evidence and Continuity Context | Overrides require reason and audit trail | Override record | Override may occur without documented reason | Override reason, owner, evidence |

## 6. Command / Activity List

| Command / activity | Expected resulting event | Primary actor / role | Bounded context | Safety note |
|---|---|---|---|---|
| Open batch review | Batch review opened for NCB204-B24071 | Quality release reviewer | GxP Batch Evidence Reconciliation | Opening review is not release approval. |
| Verify batch and product identity | Batch identity and product-master state checked | Quality / manufacturing / master-data participant | Identity, Genealogy and Product Master | Identity must be resolved or flagged before evidence output. |
| Request lineage check | Genealogy check requested | Quality release reviewer / manufacturing | Identity, Genealogy and Product Master | Lineage breaks must remain visible. |
| Detect missing lineage branch | Genealogy branch gap detected (SUA-88) | Identity/genealogy owner | Identity, Genealogy and Product Master | Never silently repair a genealogy break. |
| Search warehouse consumption records | Warehouse consumption record found for SUA-88 | Warehouse / manufacturing participant | Identity, Genealogy and Product Master | Contradictory lineage evidence remains visible. |
| Compare reported vs assumed units | Unit-conversion conflict detected (mg/L vs µg/mL) | Laboratory / interface participant | Unit and Terminology Standardisation | No silent unit conversion. |
| Abstain on unresolved unit state | Unit-conversion state declared unresolved (no-answer) | Quality / laboratory owner | Unit and Terminology Standardisation | No-answer, not a guess. |
| Surface conflicting result states | OOS/OOT state disagreement surfaced | Laboratory analyst / OOS owner | GxP Batch Evidence Reconciliation + Unit and Terminology | Do not disposition the assay. |
| Report environmental excursion | Sterile-area excursion near fill-finish detected | Manufacturing / sterile-fill participant | GxP Batch Evidence Reconciliation | Excursion evidence must stay visible. |
| Correct organism identification | Organism identification corrected after initial review | Microbiology / laboratory reviewer | GxP Batch Evidence Reconciliation | Corrections must carry rationale. |
| Request commitment verification | Supplier-audit commitment verification requested | Supplier-quality / quality reviewer | Supplier and Audit Evidence | An unverified commitment is not closed. |
| Check commitment verification state | Supplier-audit commitment found unverified | Supplier-quality participant | Supplier and Audit Evidence + GxP Batch Evidence Reconciliation | Keep the gap visible. |
| Detect back-entered record | Back-entered batch-record step detected | Manufacturing / quality reviewer | GxP Batch Evidence Reconciliation + Audit, Evidence and Continuity | Back-entered steps require checkpoint/audit evidence. |
| Assess release-packet completeness | Release packet marked evidence-incomplete | Quality release reviewer | GxP Batch Evidence Reconciliation | Incomplete packet is not batch-review ready. |
| Assess batch-review readiness | Batch-review readiness assessed with unresolved gaps | Quality release reviewer | GxP Batch Evidence Reconciliation | Readiness is not release approval. |
| Prepare evidence for QP certification | QP certification decision pending | EU Qualified Person | GxP Batch Evidence Reconciliation + Quality ownership | QP certification is human-owned. |
| Open PV case intake | PV case intake opened | PV case-intake staff | PV Case Intake and Signal Support | Intake completeness is supported, not final disposition. |
| Validate consent and entitlement | Consent/entitlement check requested | Data Protection Officer / privacy owner | Consent, Entitlement and Privacy | No data use without lawful basis and entitlement. |
| Detect duplicate candidates | ICSR duplicate cluster identified | PV case-intake staff | PV Case Intake + Unit and Terminology | Duplicate candidates await accountable review. |
| Reconstruct reporting clock | Awareness-date dispute surfaced | PV case-intake staff / PV reviewer | PV Case Intake + Authority | Do not set the clock automatically. |
| Align terminology versions | MedDRA preferred-term conflict surfaced | Safety coder / terminology owner | Unit and Terminology + PV Case Intake | Terminology state remains conflict-visible. |
| Compare listedness sources | Listedness conflict surfaced (IB vs CCDS vs local label) | PV medical reviewer / regulatory participant | PV Case Intake + Authority + Source Governance | Do not pick a listedness winner. |
| Prepare clock evidence | Reporting-clock evidence prepared for review | PV case-intake staff | PV Case Intake and Signal Support | Final PV decisions remain human-owned. |
| Request multilingual review | Multilingual review requested | PV medical/safety reviewer | PV Case Intake and Signal Support | Language completeness supports review. |
| Prepare case-review material | Case-review material prepared for accountable PV review | PV case-intake staff | PV Case Intake and Signal Support | Intake never makes final PV decisions. |
| Detect temperature excursion | Cold-chain excursion detected | Logistics / cold-chain participant | Supply, Cold-Chain + Authority | Do not disposition the shipment. |
| Detect aggregation gap | Case-to-pallet aggregation gap detected | Serialisation / logistics participant | Identity, Genealogy and Product Master + Supply | Aggregation gaps remain visible. |
| Check aggregation hierarchy | Serialisation aggregation gap detected | Serialisation participant | Identity, Genealogy and Product Master | Aggregation state must be visible. |
| Surface shortage | Excipient shortage surfaced | Supply planner / procurement | Supply, Cold-Chain + Supplier Evidence | Generate options only. |
| Surface capacity conflict | CMO capacity conflict surfaced | CMO quality / procurement | Supply, Cold-Chain + Supplier Evidence | Competing commitments remain a visible constraint. |
| Check allocation constraints | Allocation constraint check completed | Supply planner | Supply, Cold-Chain and Allocation Planning | Respect market authorisation, trial demand, compassionate use. |
| Generate traceable options | Allocation option proposed (awaiting human approval) | Supply planner | Supply, Cold-Chain and Allocation Planning | Options are advisory, never executed allocation. |
| Request authorised approval | Human approval requested for allocation option | Supply Chain / Quality accountable owner | Supply, Cold-Chain + authorised human ownership | Approval is required before any allocation action. |
| Check validation state | Validation state found ambiguous | Validation / quality owner | Authority + Audit, Evidence and Continuity | Ambiguous validation state remains unresolved. |
| Open repair window | Master-data repair window opened | IT operations / master-data owner | Audit, Evidence and Continuity | Audit capture must remain complete. |
| Capture audit event envelope | Audit record captured | Audit/quality oversight | Audit, Evidence and Continuity | Every event is auditable. |
| Detect audit-capture gap | Audit-capture gap detected (47 minutes) | Audit/quality oversight | Audit, Evidence and Continuity | Do not fill the gap silently. |
| Activate AI-off operation | AI-off continuity mode activated | CISO / IT operations | Audit, Evidence and Continuity | Operate safely without AI. |
| Receive multi-agency request | Inspection evidence request received (72h) | Regulatory Affairs / quality oversight | Audit, Evidence and Continuity + all evidence contexts | Evidence must be traceable across trial, batch, safety and AI controls. |
| Assemble evidence package | Evidence package assembled for inspection | Regulatory / quality participant | Audit, Evidence and Continuity | Packaging preserves traceability; it does not create evidence. |
| Escalate unresolved state | Escalation created for unresolved evidence state | Accountable workflow owner | All contexts via governance | Escalation requires ownership, not a guess. |
| Abstain on unresolved state | No-answer (abstention) declared | AI advisory capability / accountable owner | All contexts | No-answer, not a guess. |
| Record human approval | Human approval recorded | Accountable Quality / PV / Supply / Regulatory owner | Decision-owning context + Audit | Regulated decisions require human approval. |
| Record human override | Human override recorded | Accountable owner | Decision-owning context + Audit | Overrides require reason and audit trail. |

## 7. Actor and Human Ownership Map

| Actor / human role | Participates in event areas | Must not be bypassed for | Boundary warning |
|---|---|---|---|
| Chief Quality Officer | Batch-review readiness governance, inspection readiness, evidence completeness | Overall quality oversight and inspection readiness | Review readiness must not be mistaken for release approval. |
| EU Qualified Person | Batch certification evidence package, QP certification decision | Final batch certification (QP certification) | QP certification is human-owned; AI prepares evidence only. |
| Quality release reviewer | Batch review opening, genealogy/unit/OOS visibility, release-packet completeness | Batch-release readiness assessment; not the release decision | Release/rejection/reprocess/re-label/recall are never advisory outputs. |
| Manufacturing / sterile-fill participant | Campaign evidence, environmental excursion, back-entered steps, batch-record evidence | Production evidence accuracy and batch-record checkpoint state | Back-entered steps must stay visible with checkpoint evidence. |
| Laboratory analyst / OOS owner | Laboratory results, OOS/OOT/invalid dispute visibility, unit-conversion conflict | OOS/OOT disposition and unit-conversion acceptance | Do not disposition the assay; conversion assumptions remain unapproved. |
| Microbiology / laboratory reviewer | Organism identification correction | Correction rationale and review | Corrections must carry rationale and reviewer identity. |
| Identity / genealogy / master-data owner | Product/batch/material identity, genealogy state, aggregation state | Identity and lineage resolution status; never silent repair | Genealogy breaks remain visible with ownership. |
| Supplier-quality / procurement | Supplier audits, commitment verification, CMO capacity evidence | Verification of supplier evidence before it is treated as closed | Unverified commitments are not closed. |
| Global Head of Pharmacovigilance | PV system performance, case handling oversight, signal management | Final seriousness, causality, expectedness, reportability and signal confirmation | Final PV decisions remain with accountable PV roles. |
| PV case-intake staff | Intake, duplicate detection, reporting-clock reconstruction, multilingual preparation | Case-intake completeness preparation; not the final disposition | Intake never sets the clock or the disposition. |
| PV medical / safety reviewer | Listedness, expectedness and signal review | Final seriousness, causality, expectedness, reportability and signal confirmation | Listedness conflicts remain visible; no winner is picked. |
| Signal management | Signal-support evidence preparation | Final signal-confirmation decisions | AI supports, never confirms signals. |
| Clinical Operations | Protocol version, consent version and trial-data evidence | Clinical eligibility and trial-integrity evidence | Amendment and consent version asynchrony remains visible. |
| Regulatory Affairs (RIM, submissions, labelling, IDMP) | Authority, effective-date, jurisdiction basis; listedness sources; inspection packaging | Authority determination and submission evidence | No system is universally authoritative. |
| Supply Chain planner / logistics / cold-chain | Cold-chain evidence, allocation constraints, recovery options | Recovery-option generation; not allocation execution | Options are advisory until authorised human approval. |
| Serialisation / aggregation participant | Aggregation hierarchy, case-to-pallet linkage | Aggregation state visibility | Aggregation gaps remain visible with ownership. |
| CMO and supplier-quality | CMO capacity, contaminated excipient evidence | Capacity and sourcing evidence | Competing capacity commitments remain a visible constraint. |
| Data Protection Officer / privacy owner | Consent, entitlement, privacy-boundary checks | Lawful access and use of patient/participant data | Operational urgency must not bypass privacy boundaries. |
| CISO / IT operations | Continuity, AI-off mode, audit-capture-gap detection | Safe operation with or without AI | The organisation must operate safely without AI. |
| Audit / quality oversight | Audit event envelope capture, evidence packaging | Traceability completeness | Audit records trace decisions; they do not make them. |
| Biostatistics | OOT and statistical-tooling evidence | Statistical trend evidence visibility | OOT state remains disputed with OOS and the notebook. |
| Patient-safety voice | Compassionate-use and patient-safety context for allocation options | Visibility of patient-impact constraints | Allocation options must respect compassionate-use entitlements. |

## 8. Policy and Rule Triggers

| Policy / rule source | Triggering condition | Event-storming effect | Boundary reminder |
|---|---|---|---|
| Non-negotiable 1 | Any batch disposition is contemplated | Batch release/rejection/reprocess/re-label/recall events are never advisory outputs | AI never releases, rejects, reprocesses, re-labels or recalls a batch. |
| Non-negotiable 2 | Any PV disposition is contemplated | Final seriousness, causality, expectedness, reportability and signal-confirmation decisions stay human-only | AI never makes final PV decisions. |
| Non-negotiable 3 | Inventory status, capacity, stock, shipment or recall is contemplated | Allocation option proposed event must be followed by human approval before any execution | AI never changes inventory status, reserves capacity, allocates stock, ships or recalls without explicit authorised human approval. |
| Non-negotiable 4 | Formulation, specification, eligibility or safety-case disposition is contemplated | These decisions remain human-owned | AI never changes formulation, specification, clinical eligibility, safety-case disposition, batch-release or recall decisions. |
| Non-negotiable 5 | Any regulated decision is approached | Human ownership must be explicit in the event flow | Regulated accountability remains with Quality, Safety, Regulatory, Clinical and Supply roles. |
| Non-negotiable 6 | Identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved | No-answer (abstention) event is required; no evidence output | Fail-closed on unresolved state. |
| Non-negotiable 7 | Any recommendation, draft, approval, override, release, escalation, action, outcome or closure occurs | Audit record captured event is required | Every decision and action is auditable. |
| Non-negotiable 8 | Any workflow output is produced | Output is read-only and advisory | The system prepares, reconciles, explains and packages evidence. |
| GxP batch-release rule | A batch approaches review | Genealogy, unit, OOS/OOT, supplier-evidence and release-packet completeness events must be visible | Review readiness is not release approval or QP certification. |
| PV reporting-clock rule | A safety report is received | Awareness-date dispute and reporting-clock evidence events must be visible | The clock is evidence; it is not set automatically. |
| Listedness/expectedness rule | Expectedness evidence is prepared | Listedness conflict event must remain visible across IB, CCDS and local label | No winner is picked at this stage. |
| Cold-chain rule | A shipment temperature is questioned | Logger-clock and pallet-association evidence must be resolved before options are trusted | Do not disposition the shipment. |
| Allocation-policy rule | A shortage or recovery option is generated | Allocation constraint check and human-approval-requested events are required | Compassionate-use entitlements and trial demand bind the options. |
| Continuity rule | A ransomware, degraded-mode or repair event occurs | AI-off continuity mode and audit-capture-gap events must be visible | The organisation must operate safely with or without AI. |
| Source-governance rule | An untrusted document or manifest is encountered | Source and Document Governance quarantines before use | Prompt-injection PDF text is untrusted until governance review. |
| Privacy rule | Patient/participant data is accessed, used, routed or shared | Consent/entitlement check event must be visible | Privacy boundaries must not be bypassed. |

## 9. Exception and Escalation Events

| Known gap / exception | Related event | Event-storming treatment | What must not be done at this stage |
|---|---|---|---|
| Missing SUA-88 genealogy branch (present in warehouse consumption) | Genealogy branch gap detected (SUA-88); Warehouse consumption record found for SUA-88 | Keep visible as unresolved genealogy break with identity/lineage ownership | Do not repair the lineage or merge the records. |
| mg/L vs µg/mL unit-conversion assumption | Unit-conversion conflict detected; Unit-conversion state declared unresolved (no-answer) | Keep as unapproved unit-conversion assumption; fail-closed on unit state | Do not apply or approve the conversion. |
| OOS vs OOT vs notebook-invalid dispute | OOS/OOT state disagreement surfaced | Keep as disputed assay state with open investigation ownership | Do not disposition the assay. |
| Unverified contract-site audit commitment | Supplier-audit commitment found unverified | Keep as supplier-evidence gap in the release packet | Do not treat the commitment as closed. |
| Back-entered batch-record step | Back-entered batch-record step detected | Keep as checkpoint and audit-evidence gap | Do not silently accept or reject the step. |
| 47-minute audit-capture gap | Audit-capture gap detected (47 minutes) | Keep as audit-trail completeness gap | Do not fill the gap silently. |
| Disputed PV awareness date | Awareness-date dispute surfaced | Keep as reporting-clock reconstruction dispute | Do not set the clock. |
| Duplicate ICSR cluster under different product names | ICSR duplicate cluster identified | Keep as duplicate candidates pending accountable review | Do not merge or split the cases. |
| Two MedDRA versions changing the preferred term | MedDRA preferred-term conflict surfaced | Keep as terminology-state conflict | Do not choose a preferred term. |
| Listedness conflict between IB, CCDS and local label | Listedness conflict surfaced | Keep as listedness-source conflict | Do not pick a winner. |
| Cold-chain logger clock and pallet association dispute | Cold-chain excursion detected (logger clock/pallet disputed) | Keep as disputed cold-chain evidence | Do not disposition the shipment. |
| Missing case-to-pallet aggregation after line restart | Case-to-pallet aggregation gap detected | Keep as aggregation gap requiring evidence linkage | Do not assume the linkage. |
| Sole-source excipient contamination with eight-week recovery | Excipient shortage surfaced | Keep as supply-shortage constraint; generate options only | Do not allocate or purchase without human approval. |
| CMO capacity promised to two sponsors | CMO capacity conflict surfaced | Keep as a visible sourcing constraint | Do not reserve capacity. |
| Demand exceeds available stock | Allocation constraint check completed; Allocation option proposed (awaiting human approval) | Prepare policy-bounded options; require explicit authorised human approval | Do not allocate stock or ship product. |
| Validation-state ambiguity | Validation state found ambiguous | Keep as checkpoint and source-governance state unresolved | Do not treat the system as authoritative. |
| Untrusted supplier deviation PDF and tool manifests | Source and Document Governance quarantine path | Keep as untrusted-source governance | Do not use extracted PDF text as evidence. |
| Authority hierarchy inconsistent; later timestamps not automatically authoritative | Authority/effective-date gating across events | Keep as contextual-authority gap | Do not treat a later timestamp as authoritative. |
| eConsent version asynchrony with the pivotal-trial amendment | Consent/entitlement check requested | Keep as consent/entitlement gap | Do not use data without lawful basis. |
| Ransomware isolation of manufacturing historians; MES/QMS degraded | AI-off continuity mode activated | Keep as continuity requirement | Do not stop operating safely when AI is unavailable. |
| Pivotal-trial amendment not approved in one country | Authority/jurisdiction gating for trial data | Keep as jurisdiction-applicability gap | Do not treat the amendment as approved everywhere. |

## 10. Audit and Evidence Events

The following audit-relevant events must be captured or made visible in the business workflow:

- Batch review opened for NCB204-B24071
- Batch identity and product-master state checked
- Genealogy check requested
- Genealogy branch gap detected (SUA-88)
- Warehouse consumption record found for SUA-88
- Unit-conversion conflict detected (mg/L vs µg/mL)
- Unit-conversion state declared unresolved (no-answer)
- OOS/OOT state disagreement surfaced
- Sterile-area excursion near fill-finish detected
- Organism identification corrected after initial review
- Supplier-audit commitment verification requested
- Supplier-audit commitment found unverified
- Back-entered batch-record step detected
- Release packet marked evidence-incomplete
- Batch-review readiness assessed with unresolved gaps
- QP certification decision pending
- PV case intake opened
- Consent/entitlement check requested for participant data use
- ICSR duplicate cluster identified
- Awareness-date dispute surfaced
- MedDRA preferred-term conflict surfaced
- Listedness conflict surfaced (IB vs CCDS vs local label)
- Reporting-clock evidence prepared for review
- Multilingual review requested
- Case-review material prepared for accountable PV review
- Cold-chain excursion detected (logger clock/pallet disputed)
- Case-to-pallet aggregation gap detected
- Serialisation aggregation gap detected
- Excipient shortage surfaced
- CMO capacity conflict surfaced
- Allocation constraint check completed
- Allocation option proposed (awaiting human approval)
- Human approval requested for allocation option
- Validation state found ambiguous
- Master-data repair window opened
- Audit record captured
- Audit-capture gap detected (47 minutes)
- AI-off continuity mode activated
- Inspection evidence request received (72h)
- Evidence package assembled for inspection
- Escalation created for unresolved evidence state
- No-answer (abstention) declared where required state unresolved
- Human approval recorded
- Human override recorded

## 11. Boundary Warnings

- Do not convert event storming into solution design.
- Do not introduce architecture, systems, APIs, tools, implementation components, or automation design.
- Do not turn candidate events into batch, safety or supply decisions.
- Do not let batch-review readiness events imply release approval, rejection, reprocess, re-label, recall or QP certification.
- Do not let PV case-intake events imply final seriousness, causality, expectedness, reportability or signal confirmation.
- Do not let an allocation-option event imply an executed allocation, reservation, shipment or recall.
- Do not resolve the SUA-88 genealogy break, the mg/L vs µg/mL conversion, or the OOS/OOT/invalid dispute in the board.
- Do not set the PV reporting clock or choose a listedness winner in the board.
- Do not treat a later timestamp as automatically more authoritative than an approved signed record.
- Do not treat untrusted supplier PDF text or an unvalidated system as usable evidence.
- Do not fill the 47-minute audit-capture gap silently.
- Do not bypass consent, entitlement and privacy boundaries for patient or participant data.
- Do not collapse all events into one "evidence reconciled" event; the domain story must stay visible.
- Do not treat audit as separate from workflow; audit-relevant events are part of the domain story.
- Do not produce evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved; declare no-answer instead.

## 12. Stage 6 Quality Gate

The Stage 6 event storming board is acceptable only if:

- It uses only case and upstream stage context.
- It avoids new product, batch, safety, quality or supply facts, and provides no medical, regulatory or legal advice.
- Domain events are phrased as things that happened.
- Commands/activities are phrased as requests or actions.
- Major events identify actor, bounded context, policy, evidence source, failure condition, and audit need.
- Batch release, rejection, reprocess, re-label, recall and QP certification events remain human-owned and are never advisory outputs.
- Final PV seriousness, causality, expectedness, reportability and signal-confirmation decisions remain human-only.
- Inventory status change, capacity reservation, stock allocation, shipment and recall initiation require explicit authorised human approval.
- The board shows abstention/no-answer on unresolved identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation and checkpoint state.
- Genealogy, unit-conversion, OOS/OOT, supplier-evidence, PV, cold-chain, shortage, validation, source-governance and audit gaps remain unresolved workflow/domain gaps.
- Consent, entitlement, privacy, and auditability are visible.
- Audit-capture gaps and AI-off continuity operation remain explicit.
- No architecture, GenAI, RAG, MCP, agent, tool, API, or technical implementation appears in the output.

## 13. NEXT_STAGE_INPUT_BLOCK

```text
Stage 7 Input — Domain Model and Invariant Register

Final Event Timeline:
1. Batch review opened for NCB204-B24071
2. Batch identity and product-master state checked
3. Genealogy check requested
4. Genealogy branch gap detected (SUA-88)
5. Warehouse consumption record found for SUA-88
6. Unit-conversion conflict detected (mg/L vs µg/mL)
7. Unit-conversion state declared unresolved (no-answer)
8. OOS/OOT state disagreement surfaced
9. Sterile-area excursion near fill-finish detected
10. Organism identification corrected after initial review
11. Supplier-audit commitment verification requested
12. Supplier-audit commitment found unverified
13. Back-entered batch-record step detected
14. Release packet marked evidence-incomplete
15. Batch-review readiness assessed with unresolved gaps
16. QP certification decision pending
17. PV case intake opened
18. Consent/entitlement check requested for participant data use
19. ICSR duplicate cluster identified
20. Awareness-date dispute surfaced
21. MedDRA preferred-term conflict surfaced
22. Listedness conflict surfaced (IB vs CCDS vs local label)
23. Reporting-clock evidence prepared for review
24. Multilingual review requested
25. Case-review material prepared for accountable PV review
26. Cold-chain excursion detected (logger clock/pallet disputed)
27. Case-to-pallet aggregation gap detected
28. Serialisation aggregation gap detected
29. Excipient shortage surfaced
30. CMO capacity conflict surfaced
31. Allocation constraint check completed
32. Allocation option proposed (awaiting human approval)
33. Human approval requested for allocation option
34. Validation state found ambiguous
35. Master-data repair window opened
36. Audit record captured
37. Audit-capture gap detected (47 minutes)
38. AI-off continuity mode activated
39. Inspection evidence request received (72h)
40. Evidence package assembled for inspection
41. Escalation created for unresolved evidence state
42. No-answer (abstention) declared where required state unresolved
43. Human approval recorded
44. Human override recorded

Major Commands / Activities:
- Open batch review
- Verify batch and product identity
- Request lineage check
- Detect missing lineage branch
- Compare reported vs assumed units
- Abstain on unresolved unit state
- Surface conflicting result states
- Report environmental excursion
- Request commitment verification
- Check commitment verification state
- Detect back-entered record
- Assess release-packet completeness
- Assess batch-review readiness
- Prepare evidence for QP certification
- Open PV case intake
- Validate consent and entitlement
- Detect duplicate candidates
- Reconstruct reporting clock
- Align terminology versions
- Compare listedness sources
- Request multilingual review
- Prepare case-review material
- Detect temperature excursion
- Detect aggregation gap
- Surface shortage
- Surface capacity conflict
- Check allocation constraints
- Generate traceable options
- Request authorised approval
- Check validation state
- Capture audit event envelope
- Detect audit-capture gap
- Activate AI-off operation
- Receive multi-agency request
- Assemble evidence package
- Escalate unresolved state
- Abstain on unresolved state
- Record human approval
- Record human override

Actors and Human Owners:
- Chief Quality Officer
- EU Qualified Person
- Quality release reviewer
- Manufacturing / sterile-fill participant
- Laboratory analyst / OOS owner
- Microbiology / laboratory reviewer
- Identity / genealogy / master-data owner
- Supplier-quality / procurement
- Global Head of Pharmacovigilance
- PV case-intake staff
- PV medical / safety reviewer
- Signal management
- Clinical Operations
- Regulatory Affairs (RIM, submissions, labelling, IDMP)
- Supply Chain planner / logistics / cold-chain
- Serialisation / aggregation participant
- CMO and supplier-quality
- Data Protection Officer / privacy owner
- CISO / IT operations
- Audit / quality oversight
- Biostatistics
- Patient-safety voice

Bounded Contexts Referenced by Events:
- Identity, Genealogy and Product Master Context
- GxP Batch Evidence Reconciliation Context
- Unit and Terminology Standardisation Context
- Authority, Effective-Date and Jurisdiction Context
- Consent, Entitlement and Privacy Context
- PV Case Intake and Signal Support Context
- Supply, Cold-Chain and Allocation Planning Context
- Source and Document Governance Context
- Supplier and Audit Evidence Context
- Audit, Evidence and Continuity Context

Policies and Rules Used by the Event Storm:
- AI never releases, rejects, reprocesses, re-labels or recalls a batch.
- AI never makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions.
- AI never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval.
- AI never changes formulation, specification, clinical eligibility, safety-case disposition, batch-release or recall decisions.
- Regulated accountability remains with the accountable Quality, Safety, Regulatory, Clinical and Supply roles.
- No evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
- Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable.
- The system operates read-only and advisory; it prepares, reconciles, explains and packages evidence.
- No product, batch, safety, quality or supply issue is considered resolved merely because it has been identified.
- Batch-review readiness is not release approval or QP certification.
- PV intake supports review; it never sets the clock or the disposition.
- Allocation options are advisory until explicit authorised human approval.
- Authority is per business object, jurisdiction and effective date; later timestamps are not automatically authoritative.
- Untrusted sources and ambiguous validation states remain quarantined or unresolved.
- The organisation must operate safely with or without AI.

Known Exceptions and Unresolved Gaps:
- Genealogy branch gap for SUA-88 with a warehouse consumption record.
- Unapproved mg/L vs µg/mL unit-conversion assumption.
- Disputed OOS/OOT/notebook-invalid state with an open investigation.
- Unverified contract-site audit commitment in the EU release packet.
- Back-entered batch-record step; 47-minute audit-capture gap.
- Disputed PV awareness date; duplicate ICSR cluster; MedDRA version mismatch; listedness conflict (IB vs CCDS vs local label).
- Cold-chain logger clock and pallet association dispute; missing case-to-pallet and serialisation aggregation.
- Sole-source excipient contamination with eight-week recovery; CMO capacity conflict; demand exceeds available stock.
- Validation-state ambiguity; untrusted supplier deviation PDF and tool manifests; eConsent version asynchrony; pivotal-trial amendment not approved in one country.

Audit / Evidence Requirements:
- Identity and lineage evidence, genealogy-break identification and ownership must be traceable.
- Unit-conversion conflict and no-answer declarations must be recorded with mapping and source.
- OOS/OOT/invalid dispute evidence and open investigation ownership must be recorded.
- Supplier-audit verification state and release-packet completeness must be recorded.
- Batch-review readiness assessment, evidence-gap ownership and QP pending status must be recorded.
- PV intake, duplicate rationale, clock reconstruction, MedDRA version, listedness sources and reviewer routing must be recorded.
- Cold-chain logger basis, pallet association, aggregation state, shortage, capacity conflict and constraint rationale must be recorded.
- Approval requests, human approvals, human overrides, escalations, actions, outcomes and closures must be auditable.
- The audit event envelope must be captured for every workflow event; the 47-minute audit-capture gap remains visible.
- AI-off continuity activation, repair-window operation and the 72-hour inspection evidence package must be recorded.

Candidate Domain Objects Visible From Events:
- BatchReview
- BatchReviewReadiness
- ReleasePacket
- BatchRecordStep
- Genealogy
- GenealogyBreak
- MaterialLot (SUA-88)
- WarehouseConsumptionRecord
- UnitConversionAssumption
- LaboratoryResult
- OOSState
- OOTState
- EnvironmentalMonitoringExcursion
- OrganismIdentificationCorrection
- SupplierAuditCommitment
- ReleasePacketCompleteness
- QPCertificationDecision
- ICSRCase
- DuplicateICSRCandidate
- AwarenessDate
- ReportingClock
- MedDRATerminologyState
- PreferredTerm
- ListednessEvidence
- ExpectednessEvidence
- CaseReviewMaterial
- TemperatureLoggerRecord
- ColdChainExcursion
- AggregationHierarchy
- SerialisationAggregation
- ExcipientShortage
- CMOCapacity
- AllocationConstraint
- AllocationOption
- ApprovalRequest
- ApprovalRecord
- OverrideRecord
- ValidationState
- AuditRecord
- AuditCaptureGap
- ContinuityState
- InspectionRequest
- EvidencePackage
- EscalationRecord
- AbstentionRecord

Open Questions for Stage 7:
- Which objects are entities versus value objects?
- Which object should act as the main aggregate root for batch-review readiness, PV case intake, and supply recovery respectively?
- Which object owns evidence status and which owns checkpoint state?
- Which object owns the authority/effective-date basis and how is it passed between contexts?
- Which object owns the audit event envelope?
- Which invariants prevent evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved?
- Which invariants prevent batch release/rejection, QP certification, PV dispositions, allocation, shipment and recall events from being advisory or automated?
- Which invariants prevent silent unit conversion, silent genealogy repair, and silent listedness selection?
- Which invariants keep the audit-capture gap and unresolved exceptions visible?
```

Stage 6 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 7.
