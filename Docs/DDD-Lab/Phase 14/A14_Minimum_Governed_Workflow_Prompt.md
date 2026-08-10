# Stage 14 Prompt — Minimum Governed Workflow

You are the context engineering assistant for an AI FDE × Domain-Driven Design workshop for Project AEGIS-PHARMA at NovaCura Therapeutics Group.

I have attached the Stage 14 input file created from Stage 13:

- `Docs/DDD-Lab/Phase 14/A14_Input_From_Stage13.md`

Your task is to read the Stage 14 input and create a clean, structured MINIMUM GOVERNED WORKFLOW for the NovaCura Therapeutics Group (AEGIS-PHARMA) advisory workflows.

Important rules:

1. Use only the attached Stage 14 input and its upstream case context.
2. Do not invent new product, batch, compound, clinical, safety, quality or supply facts, policies, or sources.
3. Do not create architecture yet.
4. Do not introduce GenAI, RAG systems, MCP, agents, vector databases, or technical implementation yet.
5. Keep this as a business-process and governance artifact that stays implementable.
6. Preserve all non-negotiables around fail-closed handling of unresolved identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation and checkpoint state; read-only advisory behaviour; and auditability.
7. Do not provide medical, regulatory or legal advice.
8. Do not resolve identity, genealogy, unit, terminology, authority, OOS/OOT, supplier, PV, cold-chain, shortage, capacity or allocation issues.
9. Every step in the workflow must stay within the three advisory workflows and must never release, reject, reprocess, re-label or recall a batch; never make final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions; and never change inventory status, reserve capacity, allocate stock, ship product or initiate a recall without explicit authorised human approval.
10. The workflow must show where AI can assist (prepare, reconcile, surface, explain, package) and where deterministic controls and human review must take over.

Create the output in the following structure:

# A14 — Minimum Governed Workflow: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## 1. Stage 14 Mission
Summarize what this stage does and what it must avoid.

## 2. Input Summary
Summarize the evaluation suite, human decision ownership, and non-negotiables being used.

## 3. Workflow Principles
State the principles used to design the minimum governed workflow.

## 4. Workflow Overview
Describe the end-to-end advisory workflow in business terms.

## 5. Workflow Step Register
For each step, include:
- step ID
- step name
- input
- output
- AI assist scope
- deterministic control
- human review point
- human authorization point
- evidence and audit need
- fail-closed default
- bounded context

## 6. Control and Gate Register
List each control and gate with:
- gate ID
- gate name
- trigger
- requirement to pass
- fail-closed default
- accountable role
- bounded context

## 7. AI Assist vs Deterministic vs Human Responsibility Map
Map each workflow step to AI assist, deterministic control, or human responsibility.

## 8. Read-Only Boundary Declaration
State explicitly the read-only boundary of the advisory workflows.

## 9. Human Decision Points
List the human decision points that must never be bypassed.

## 10. Evidence and Audit Trail
Describe the evidence and audit trail each workflow run must produce.

## 11. Rollback and AI-Off Behaviour
Describe the rollback and AI-off behaviour for the workflow.

## 12. Anti-Patterns to Avoid
List the workflow anti-patterns to avoid.

## 13. Boundary Warnings
State what the team must not confuse while designing the workflow.

## 14. Stage 14 Quality Gate
List the checks that make the minimum governed workflow acceptable.

## 15. NEXT_STAGE_INPUT_BLOCK
Create a compact handoff block for the final synthesis stage.

The block must include:
- workflow overview summary
- step register summary
- control and gate register summary
- AI assist vs deterministic vs human responsibility map
- read-only boundary declaration
- human decision points
- evidence and audit trail summary
- rollback and AI-off behaviour
- non-negotiables
- open questions for final synthesis

End the output with:

“Stage 14 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for the final synthesis.”
