# A11 Prompt — Human Decision Ownership Matrix

You are the context engineering assistant for an AI FDE × Domain-Driven Design pharmaceutical workshop.

I have attached the Stage 10 handoff input for the NovaCura Therapeutics Group (Project AEGIS-PHARMA) evidence-reconciliation case.

Your task is to read the attached Stage 10 handoff and create a clean, structured **Stage 11 — Human Decision Ownership Matrix** artifact.

Important rules:

1. Use only the attached Stage 10 handoff and prior case context included in it.
2. Do not invent new product, batch, safety, quality, regulatory, clinical or supply facts.
3. Do not provide medical, regulatory or legal advice.
4. Do not resolve genealogy, unit, OOS/OOT, supplier-evidence, PV, cold-chain, shortage, validation, consent/entitlement, authority or audit issues.
5. Do not approve batch release, rejection, reprocess, re-label or recall.
6. Do not certify as EU Qualified Person.
7. Do not make final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions.
8. Do not confirm duplicates, set the reporting clock, or pick a listedness winner.
9. Do not dispose OOS/OOT results, environmental excursions or cold-chain excursions.
10. Do not approve inventory status changes, capacity reservation, stock allocation, shipment or recall initiation.
11. Do not override consent, entitlement, privacy, or access boundaries.
12. Do not create technical architecture.
13. Do not design implementation.
14. Keep the output focused on human decision ownership, responsibility, accountability, approval gates, escalation ownership, and auditability.
15. Every decision must identify a responsible human role and an accountable human role.
16. If the exact role is not specified in the case, mark it as **role to be assigned** rather than inventing a new role.
17. Batch and quality decisions remain owned by EU QP / Quality release reviewer / Quality owners; PV dispositions remain owned by PV reviewers; supply and allocation decisions remain owned by Supply Chain / authorised Quality owners.
18. Every approval, rejection, override, release, escalation, outcome, and closure must be auditable.

Create the output in the following structure:

# A11 — Human Decision Ownership Matrix: NovaCura Therapeutics Group

## 1. Stage 11 Purpose
Explain the purpose of this stage in one clear paragraph.

## 2. Human Ownership Boundary
State what humans must own and what support roles must never own.

## 3. Decision Inventory
List the major batch, quality, pharmacovigilance, supply, cold-chain, regulatory, consent/entitlement, escalation, and audit decisions in the case.

## 4. RACI-Style Decision Ownership Matrix
Create a matrix with these columns:
- Decision / Work Item
- Responsible Human Role
- Accountable Human Role
- Support Role May Prepare
- Approval Required Before Action
- Evidence Required
- Stop / Escalation Condition
- Audit Requirement

## 5. Batch and Quality Decision Ownership
Clarify ownership for batch genealogy resolution, unit-conversion handling, OOS/OOT disposition, environmental-monitoring excursion disposition, deviation/CAPA/change-control closure, supplier-audit verification, release-packet completeness, QP certification and batch release/rejection/reprocess/re-label/recall.
Do not resolve any quality issue.

## 6. Pharmacovigilance Decision Ownership
Clarify ownership for duplicate-ICSR confirmation, awareness-date acceptance, MedDRA terminology decisions, listedness/expectedness determination, seriousness/causality/reportability decisions, and signal confirmation.
Do not resolve any safety issue.

## 7. Supply, Cold-Chain and Allocation Decision Ownership
Clarify ownership for cold-chain excursion disposition, serialisation aggregation resolution, excipient-supply continuity, CMO capacity decisions, allocation recommendation and approval, and recall consideration.
Do not approve any allocation or recall.

## 8. Regulatory, Consent and Inspection Decision Ownership
Clarify ownership for label/IB/CCDS alignment decisions, IDMP identity, submission/commitment decisions, consent/entitlement/privacy decisions, and 72-hour inspection-evidence packaging and response ownership.
Do not override any consent, entitlement or privacy boundary.

## 9. Escalation and Override Ownership
Clarify who owns escalation, override reason, outcome documentation, and closure.

## 10. Audit Ownership Model
List the minimum audit events and the accountable owner for each audit class.

## 11. Forbidden Ownership Patterns
List unsafe ownership mistakes that the team must avoid.

## 12. Open Ownership Questions
List questions that must be answered before Stage 12 evidence and audit design.

## 13. Quality Gate Checklist
Create a checklist to verify that Stage 11 is safe, human-owned, and auditable.

## 14. NEXT_STAGE_INPUT_BLOCK
Create a compact handoff block for Stage 12.

The block must include:
- decision ownership summary
- human approval gates
- batch and quality ownership
- pharmacovigilance ownership
- supply, cold-chain and allocation ownership
- regulatory, consent and inspection ownership
- escalation/override ownership
- audit obligations
- forbidden ownership patterns
- open questions

End the output with:

"Stage 11 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 12."
