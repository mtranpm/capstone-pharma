# A4 — Bounded Context Canvases Prompt

You are the context engineering assistant for an AI FDE × Domain-Driven Design workshop for Project AEGIS-PHARMA at NovaCura Therapeutics Group.

I have attached the Stage 4 input file created from Stage 3:

1. `Docs/DDD-Lab/Phase 4/A4_Input_From_Stage3.md`

Your task is to read the attached Stage 4 input and create a clean, structured **Bounded Context Canvases** artifact for NovaCura Therapeutics Group (Project AEGIS-PHARMA).

Important rules:

1. Use only the attached Stage 4 input.
2. Do not invent new product, batch, compound, safety, quality or supply facts or records.
3. Do not solve the case yet.
4. Do not create architecture yet.
5. Do not introduce GenAI, RAG, MCP, agents, tools, APIs, services, or technical implementation.
6. Keep this as a business-domain DDD artifact.
7. Preserve all non-negotiables around fail-closed handling of unresolved identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation and checkpoint state; read-only advisory behaviour; and auditability.
8. Do not provide medical, regulatory or legal advice.
9. Do not resolve identity, genealogy, unit, terminology, authority, consent, validation or evidence conflicts. Only locate them inside the right business contexts as workflow/domain gaps.
10. Do not make one giant pharmaceutical context. Each bounded context must have its own language, ownership, decisions/statuses, dependencies, risks, and audit needs.

Create the output in the following format:

# A4 — Bounded Context Canvases: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## 1. Stage 4 Mission
Briefly state the purpose of Stage 4.

## 2. Input Summary
Summarize the Stage 3 input being used.

## 3. Bounded Context Design Principles
List the principles used to separate bounded contexts.

## 4. Final Bounded Context List
List the final bounded contexts and one-line purpose for each.

## 5. Bounded Context Canvases
For each bounded context, provide a canvas with:

- context name
- business purpose
- primary participants
- owned language
- owned information/statuses
- decisions/statuses owned
- decisions not owned
- upstream inputs
- downstream outputs
- policies/rules it must respect
- known gaps/exceptions touching this context
- audit/evidence needs
- safety risk if boundary is misunderstood

Use the following bounded contexts unless there is a clear business reason to merge or split:

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

## 6. Known Gaps Mapped to Bounded Contexts
Map each known gap or exception to the bounded context that must own or coordinate it.

## 7. Boundary Warnings
List the unsafe boundary confusions that the workshop team must avoid.

## 8. Stage 4 Quality Gate
State the quality criteria for accepting the bounded context canvases.

## 9. NEXT_STAGE_INPUT_BLOCK
Create a compact handoff block for Stage 5 — Context Map.

The block must include:

- final bounded context list
- purpose of each context
- key upstream/downstream dependencies
- known cross-context handoffs
- safety-critical boundary warnings
- non-negotiables
- open questions for context mapping

End the output with:

“Stage 4 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 5.”
