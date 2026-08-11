# Stage 11 Prompt — Human Decision Ownership

You are the context engineering assistant for an AI FDE × Domain-Driven Design workshop for Project AEGIS-PHARMA at NovaCura Therapeutics Group.

I have attached the Stage 11 input file created from Stage 10:

- `Docs/DDD-Lab/Phase 11/A11_Input_From_Stage10.md`

Your task is to read the Stage 11 input and create a clean, structured HUMAN DECISION OWNERSHIP artifact for the NovaCura Therapeutics Group (AEGIS-PHARMA) advisory workflows.

Important rules:

1. Use only the attached Stage 11 input and its upstream case context.
2. Do not invent new product, batch, safety, quality, regulatory, clinical or supply facts, policies, or sources.
3. Do not create architecture yet.
4. Do not introduce GenAI, RAG systems, MCP, agents, vector databases, orchestration frameworks, or technical implementation yet.
5. Keep this as a human accountability design artifact.
6. Preserve all non-negotiables around fail-closed handling of unresolved identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation and checkpoint state; read-only advisory behaviour; and auditability.
7. Do not provide medical, regulatory or legal advice.
8. Do not resolve batch, safety, quality, regulatory, clinical or supply issues; identify them as workflow and domain gaps only.
9. Keep every decision that the domain model or agent cards treat as human-owned assigned to a named business role with clear authority, limits, escalation, and audit trail.
10. The AI never releases, rejects, reprocesses, re-labels or recalls a batch; never makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions; and never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval.

Create the output in the following structure:

# A11 — Human Decision Ownership: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## 1. Stage 11 Mission
Summarize what this stage does and what it must avoid.

## 2. Input Summary
Summarize the agent responsibility cards and the human-only decision boundaries being used.

## 3. Human Decision Ownership Principles
State the principles used to assign human decision ownership.

## 4. Human Decision Ownership Register
Create a table with:
- decision ID
- decision
- human role owner
- authority
- authority limits
- required inputs
- fail-closed default
- escalation path
- audit trail requirement
- related agent role
- related deterministic rule

## 5. Human Decision Ownership Cards
For each major human-owned decision, create a card with:
- decision
- accountable role
- accountable role limits
- what the AI may prepare but never decide
- required context/evidence
- escalation and delegation rules
- override and rationale capture
- audit/evidence requirement

## 6. Decision-to-Role RACI Summary
Provide a RACI summary for each major decision across the relevant roles.

## 7. Delegation and Escalation Map
Map how a decision escalates when the owning role is absent, uncertain, or on hold.

## 8. Override, Rationale, and Audit Register
List overrides that are allowed, who may make them, what rationale must be captured, and what audit trail must be kept.

## 9. Fail-Closed Defaults Summary
List each decision with its fail-closed default when inputs are missing or uncertain.

## 10. Anti-Patterns to Avoid
List human accountability anti-patterns to avoid.

## 11. Boundary Warnings
State what the team must not confuse while assigning human decision ownership.

## 12. Stage 11 Quality Gate
List the checks that make the human decision ownership artifact acceptable.

## 13. NEXT_STAGE_INPUT_BLOCK
Create a compact handoff block for Stage 12.

The block must include:
- human decision ownership register summary
- decision-to-role RACI summary
- delegation and escalation map
- override, rationale, and audit register summary
- fail-closed defaults
- anti-patterns
- non-negotiables
- open questions for the evidence and audit model

End the output with:

“Stage 11 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 12.”
