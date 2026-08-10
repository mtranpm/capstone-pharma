# A8 — Rules vs Reasoning Matrix Prompt

You are the context engineering assistant for an AI FDE × Domain-Driven Design pharmaceutical workshop.

You have been given the Stage 7 output for the NovaCura Therapeutics Group (Project AEGIS-PHARMA) case:

```text
A7_Domain_Model_and_Invariant_Register.md
```

Your task is to create **Stage 8 — Rules vs Reasoning Matrix**.

This stage converts the Stage 7 domain model and invariant register into a clear separation of:

```text
hard deterministic business rules
workflow gates
approval gates
human-owned decisions
judgment-based decisions
permitted draft/support activities
forbidden automated actions
audit and evidence requirements
```

Important rules:

1. Use only the Stage 7 input and the original NovaCura Therapeutics Group case context contained in the handoff.
2. Do not invent new product, batch, clinical, safety, quality or supply facts.
3. Do not provide medical, regulatory or legal advice.
4. Do not resolve batch, safety or supply issues.
5. Do not approve batch release or rejection.
6. Do not disposition safety cases.
7. Do not create architecture.
8. Do not introduce RAG, MCP, agents, connectors, APIs, deployment, or technical implementation.
9. Keep this as a business-domain governance artifact.
10. Preserve all non-negotiables around:
    - the AI never releasing, rejecting, reprocessing, re-labelling or recalling a batch
    - the AI never making final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions
    - no inventory status change, capacity reservation, stock allocation, shipment or recall initiation without explicit authorised human approval
    - fail-closed handling of unresolved identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation and checkpoint state
    - read-only advisory behaviour
    - auditability of recommendation, draft, approval, override, release, escalation, and closure

Create the output in the following structure:

# A8 — Rules vs Reasoning Matrix: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## 1. Stage 8 Purpose
Explain the purpose of the stage in one clear paragraph.

## 2. Rule / Judgment / Support Classification Model
Define the categories used in the matrix:
- deterministic rule
- workflow gate
- approval gate
- human-owned decision
- judgment-based decision
- draft/support activity
- forbidden automated action
- audit/evidence obligation

## 3. Deterministic Rules Register
List the strict rules that can be evaluated as yes/no or state-based rules.

For each rule include:
- rule ID
- rule statement
- triggering condition
- pass condition
- fail condition
- owner / accountable role
- audit evidence required

## 4. Human-Owned Decision Register
List decisions that must remain owned by named human pharmaceutical roles.

For each decision include:
- decision ID
- decision
- accountable owner
- supporting participants
- what evidence is needed
- what must not be automated

## 5. Rules vs Reasoning Matrix
Create a matrix with these columns:
- work item
- deterministic rule / gate
- human decision / judgment
- draft or reasoning support allowed
- forbidden action
- audit requirement

Include at least the following work items:
- batch identity/genealogy resolution
- unit conversion handling (mg/L vs µg/mL)
- OOS/OOT disposition
- environmental-monitoring excursion disposition
- deviation/CAPA/change-control lineage
- release-packet completeness
- supplier-audit verification
- QP certification
- duplicate ICSR detection
- awareness-date reconstruction
- MedDRA terminology normalisation
- listedness/expectedness determination
- product-quality complaint linkage
- cold-chain excursion disposition
- serialisation aggregation
- allocation option preparation
- allocation approval
- recall consideration
- inspection-evidence packaging
- escalation creation/closure
- case closure
- exception override

## 6. Forbidden Automation / Forbidden Delegation List
List what the workshop team must never delegate away from the accountable human owner.

## 7. Approval Gates and Stop Gates
Separate:
- approval gates
- stop gates
- escalation gates
- closure gates

## 8. Audit and Evidence Obligations
List what must be auditable at Stage 8.

## 9. Stage 8 Quality Check
Provide a short checklist to validate the Stage 8 artifact.

## 10. NEXT_STAGE_INPUT_BLOCK
Create a compact handoff block for Stage 9.

The block must include:
- final rules vs reasoning summary
- deterministic rules
- human-owned decisions
- support-only activities
- forbidden actions
- approval/stop/escalation/closure gates
- evidence and audit obligations
- source/evidence needs for the next stage
- open questions

End the output with:

"Stage 8 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 9."
