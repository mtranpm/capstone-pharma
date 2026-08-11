# Stage 10 Prompt — Agent Responsibility Cards

You are the context engineering assistant for an AI FDE × Domain-Driven Design workshop for Project AEGIS-PHARMA at NovaCura Therapeutics Group.

I have attached the Stage 10 input file created from Stage 9:

- `Docs/DDD-Lab/Phase 10/A10_Input_From_Stage9.md`

Your task is to read the Stage 10 input and create a clean, structured AGENT RESPONSIBILITY CARDS artifact for the NovaCura Therapeutics Group (AEGIS-PHARMA) advisory workflows.

Important rules:

1. Use only the attached Stage 10 input and its upstream case context.
2. Do not invent new product, batch, safety, quality, regulatory, clinical or supply facts, policies, or sources.
3. Do not create architecture yet.
4. Do not introduce GenAI, RAG systems, MCP, agents, vector databases, orchestration frameworks, or technical implementation yet.
5. Keep this as a responsibility-design artifact. It is safe to name candidate agent roles, but not to design their technical implementation.
6. Preserve all non-negotiables around fail-closed handling of unresolved identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation and checkpoint state; read-only advisory behaviour; and auditability. The AI never releases, rejects, reprocesses, re-labels or recalls a batch; never makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions; and never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval.
7. Do not provide medical, regulatory or legal advice.
8. Do not resolve batch, safety, quality, supply, genealogy, unit, terminology, authority, consent or validation issues; identify them as gaps and exceptions only.
9. Keep human ownership visible. An agent role must never be granted authority to: release or reject a batch, certify as QP, make final PV determinations, confirm duplicates, set reporting clocks, pick listedness winners, dispose OOS/OOT or cold-chain excursions, change inventory status, reserve capacity, allocate stock, ship product, initiate a recall, override consent/entitlement, change formulation/specification/eligibility/disposition, or decide overrides.
10. Every responsibility an agent role is given must be traceable to a deterministic rule, a bounded heuristic, or an explicitly human-owned decision, and must state the fail-closed default.

Create the output in the following structure:

# A10 — Agent Responsibility Cards: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## 1. Stage 10 Mission
Summarize what this stage does and what it must avoid.

## 2. Input Summary
Summarize the source register, rules vs reasoning, domain model, and non-negotiables being used.

## 3. Agent Role Design Principles
State the principles used to design agent responsibility cards.

## 4. Candidate Agent Roles
List candidate agent roles, their purpose, and their owner context.

## 5. Agent Responsibility Cards
For each candidate agent role, create a card with:
- agent role
- mission
- bounded context it operates in
- input the agent receives
- deterministic rules the agent must apply
- bounded reasoning the agent may perform
- actions the agent may take
- actions the agent must never take
- fail-closed defaults
- evidence and traceability requirements
- human review and override points
- handoff to other agents or roles

## 6. Human-Only Decision Boundaries
List every decision that must remain human-only and the agent role that must hand off to the human.

## 7. Agent-to-Agent Handoffs
List candidate handoffs, the information exchanged, and the risk of each handoff.

## 8. Guardrail and Guardrail-Owner Register
For each guardrail, list:
- guardrail
- type: deterministic gate, bounded heuristic, or human authorization
- owner context
- human role accountable
- fail-closed default
- evidence need

## 9. Anti-Patterns to Avoid
List the agent responsibility anti-patterns to avoid.

## 10. Boundary Warnings
State what the team must not confuse while designing agent responsibilities.

## 11. Stage 10 Quality Gate
List the checks that make the agent responsibility cards acceptable.

## 12. NEXT_STAGE_INPUT_BLOCK
Create a compact handoff block for Stage 11.

The block must include:
- candidate agent roles
- agent responsibility card summaries
- human-only decision boundaries
- agent-to-agent handoffs
- guardrails and owners
- fail-closed defaults
- anti-patterns
- non-negotiables
- open questions for human decision ownership

End the output with:

"Stage 10 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 11."
