# Stage 6 Prompt — Event Storming Board

You are the context engineering assistant for an AI FDE × Domain-Driven Design workshop for Project AEGIS-PHARMA at NovaCura Therapeutics Group.

I have attached the Stage 6 input file created from Stage 5:

- `Docs/DDD-Lab/Phase 6/A6_Input_From_Stage5.md`

Your task is to read the Stage 6 input and create a clean, structured EVENT STORMING BOARD for the NovaCura Therapeutics Group (AEGIS-PHARMA) advisory workflows.

Important rules:

1. Use only the attached Stage 6 input and its upstream case context.
2. Do not invent new product, batch, compound, safety, quality or supply facts or records.
3. Do not solve the case yet.
4. Do not create architecture yet.
5. Do not introduce GenAI, RAG, MCP, agents, tools, system design, APIs, or technical implementation.
6. Keep this as a business-domain event storming artifact.
7. Preserve all non-negotiables around fail-closed handling of unresolved identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation and checkpoint state; read-only advisory behaviour; and auditability.
8. Preserve the read-only advisory boundary for all three mandatory workflows: Workflow A (GxP evidence reconciliation for batch-review readiness, which never releases, rejects, reprocesses, re-labels or recalls a batch), Workflow B (pharmacovigilance case-intake and signal-support, which never makes final seriousness, causality, expectedness, reportability or signal-confirmation decisions), and Workflow C (bounded supply-shortage and cold-chain recovery planning, which never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval).
9. Do not provide medical, regulatory or legal advice.
10. Do not resolve identity, genealogy, unit, terminology, authority, consent, validation or evidence conflicts. Only identify them as workflow/domain events, commands, policies, exceptions, and audit needs.
11. Keep regulated decisions human-only: batch release/rejection, QP certification, PV seriousness/causality/expectedness/reportability/signal confirmation, and allocation/stock/capacity changes and recall. The event board must show where the AI only prepares and surfaces evidence and must abstain (no-answer) on unresolved identity, genealogy, unit, terminology, authority, effective-date, jurisdiction, consent/entitlement, validation or checkpoint state.
12. Use event-storming language carefully:
    - Domain events should be written as things that happened.
    - Commands or activities should be written as requests/actions.
    - Policies should explain why an event or action is required.
    - Exceptions should remain unresolved unless the case evidence says otherwise.
13. Make actor, trigger, policy, context, failure condition, and audit need visible for major events.

Create the output in the following structure:

# A6 — Event Storming Board: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## 1. Stage 6 Mission
Summarize what this stage does and what it must avoid.

## 2. Input Summary
Summarize the context map, representative scenario, known gaps, and non-negotiables being used.

## 3. Event Storming Principles
State the rules used to create the business-domain event storming board.

## 4. Event Timeline Overview
Show the event flow as a simple business sequence.

## 5. Event Storming Board
Create a table with:
- sequence
- domain event
- event type
- triggering command or activity
- primary actor / human role
- bounded context
- policy or business rule
- evidence source
- failure or exception condition
- audit / evidence need

## 6. Command / Activity List
List the commands or business activities that trigger major events.

## 7. Actor and Human Ownership Map
Map each actor or role to the event areas they participate in and decisions they must not be bypassed for.

## 8. Policy and Rule Triggers
List the policies, SOP requirements, non-negotiables, and escalation rules that influence the event flow.

## 9. Exception and Escalation Events
List unresolved gaps and the event/storming treatment for each.

## 10. Audit and Evidence Events
List the audit-relevant events that must be captured.

## 11. Boundary Warnings
State what the team must not confuse during event storming.

## 12. Stage 6 Quality Gate
List the checks that make the event storming board acceptable.

## 13. NEXT_STAGE_INPUT_BLOCK
Create a compact handoff block for Stage 7.

The block must include:
- final event timeline
- major commands / activities
- actors and human owners
- bounded contexts referenced by events
- policies and rules used by the event storm
- known exceptions and unresolved gaps
- audit/evidence requirements
- candidate domain objects visible from events
- open questions for Stage 7

End the output with:

"Stage 6 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 7."

Write the completed artifact to `Docs/DDD-Lab/Phase 6/A6_Event_Storming_Board.md`.
