# Stage 8 Prompt — Rules vs Reasoning Register

You are the context engineering assistant for an AI FDE × Domain-Driven Design workshop for Project AEGIS-PHARMA at NovaCura Therapeutics Group.

I have attached the Stage 8 input file created from Stage 7:

- `Docs/DDD-Lab/Phase 8/A8_Input_From_Stage7.md`

Your task is to read the Stage 8 input and create a clean, structured RULES VS REASONING REGISTER for the NovaCura Therapeutics Group (AEGIS-PHARMA) advisory workflows.

Important rules:

1. Use only the attached Stage 8 input and its upstream case context.
2. Do not invent new product, batch, clinical, safety, quality or supply facts or records.
3. Do not solve the case yet.
4. Do not create architecture yet.
5. Do not introduce GenAI, RAG, MCP, agents, tools, system design, APIs, or technical implementation yet.
6. Keep this as a business-domain decision-design artifact.
7. Preserve all non-negotiables around fail-closed handling of unresolved identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation and checkpoint state; read-only advisory behaviour; and auditability.
8. Do not provide medical, regulatory or legal advice.
9. Do not resolve identity, genealogy, unit, terminology, authority, effective-date, jurisdiction, consent, validation, batch, safety or supply issues. Only classify which domain decisions are deterministic rules, which require judgement, and which require human authorization.
10. Distinguish carefully between:
    - Deterministic rules: objective, verifiable, binary, low human judgement.
    - Heuristic or judgement-based reasoning: involves experience, interpretation, or discretion.
    - Human authorization decisions: must remain owned by a named human role.
    - Hybrid: starts from a deterministic gate and then requires human judgement.

Create the output in the following structure:

# A8 — Rules vs Reasoning Register: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## 1. Stage 8 Mission
Summarize what this stage does and what it must avoid.

## 2. Input Summary
Summarize the domain model, invariants, human decision ownership, and non-negotiables being used.

## 3. Decision Classification Principles
State the classification rules used for deterministic rules, heuristic reasoning, and human authorization.

## 4. Decision Register
Create a table with:
- decision ID
- decision
- decision category: deterministic rule, heuristic reasoning, human authorization, or hybrid
- owning bounded context
- decisive business role / human owner
- key inputs
- key expected outputs
- failure risk if automated without control
- audit / evidence need
- invariant impact

## 5. Deterministic Rules Register
List each deterministic rule with:
- rule
- source policy/evidence
- trigger condition
- expected output
- fail-closed behaviour if inputs are missing or uncertain
- traceability need

## 6. Heuristic / Judgement-Based Reasoning Register
List each judgement area with:
- judgement area
- context
- why it requires reasoning
- acceptable output boundaries
- who must decide
- what must be protected

## 7. Human Authorization Decisions Register
List each decision that must stay with a human with:
- decision
- human role
- what the model must never auto-approve
- fail-closed default

## 8. Hybrid Decision Flows
List decisions that start deterministic but require human judgement before completion, describing the required checkpoint.

## 9. Classifying Inherently Safer Deterministic Controls
Highlight the controls that are inherently safer as deterministic rules, such as: identity/product-code match and genealogy completeness before any batch evidence output; unit-conversion and MedDRA-version consistency resolution before output; entitlement/consent and checkpoint-state gating before any retrieval or release; required release-packet element completeness; and blocking of batch release/rejection, QP certification, PV disposition, inventory status change, capacity reservation, allocation, shipment and recall initiation.

## 10. Anti-Patterns to Avoid
List the unsafe automation patterns to avoid, such as: AI deciding batch release, AI resolving genealogy to production data, AI authorizing overrides, AI confirming duplicates, AI setting the reporting clock, AI picking a listedness winner, AI dispositioning OOS/OOT or excursions, AI allocating stock, AI initiating recalls, AI resolving identity, and treating ambiguity as completeness.

## 11. Boundary Warnings
State what the team must not confuse while classifying decisions.

## 12. Stage 8 Quality Gate
List the checks that make the rules vs reasoning register acceptable.

## 13. NEXT_STAGE_INPUT_BLOCK
Create a compact handoff block for Stage 9.

The block must include:
- decision register summary
- deterministic rules summary
- heuristic reasoning areas
- human authorization decisions
- hybrid decision flows
- inherently safer deterministic controls
- anti-patterns to avoid
- non-negotiables
- open questions for the RAG source register

End the output with:

"Stage 8 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 9."
