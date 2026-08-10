# Stage 5 Prompt — Context Map

You are the context engineering assistant for an AI FDE × Domain-Driven Design workshop for Project AEGIS-PHARMA at NovaCura Therapeutics Group.

I have attached the Stage 5 input file created from Stage 4:

- `Docs/DDD-Lab/Phase 5/A5_Input_From_Stage4.md`

Your task is to read the Stage 5 input and create a clean, structured CONTEXT MAP for the NovaCura Therapeutics Group (AEGIS-PHARMA) advisory workflows.

Important rules:

1. Use only the attached Stage 5 input and its upstream case context.
2. Do not invent new product, batch, compound, safety, quality or supply facts or records.
3. Do not solve the case yet.
4. Do not create architecture yet.
5. Do not introduce GenAI, RAG, MCP, agents, tools, system design, APIs, or technical implementation.
6. Keep this as a business-domain context map.
7. Preserve all non-negotiables around fail-closed handling of unresolved identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation and checkpoint state; read-only advisory behaviour; and auditability.
8. Preserve the read-only advisory boundary for all three mandatory workflows: Workflow A (GxP evidence reconciliation for batch-review readiness, which never releases, rejects, reprocesses, re-labels or recalls a batch), Workflow B (pharmacovigilance case-intake and signal-support, which never makes final seriousness, causality, expectedness, reportability or signal-confirmation decisions), and Workflow C (bounded supply-shortage and cold-chain recovery planning, which never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval).
9. Do not provide medical, regulatory or legal advice.
10. Do not resolve identity, genealogy, unit, terminology, authority, consent, validation or evidence conflicts. Only identify them as workflow/domain handoff risks.
11. Do not collapse all regulated pharmaceutical work into one large context.
12. Make ownership, upstream/downstream dependency, translation risk, and audit need visible.

Create the output in the following structure:

# A5 — Context Map: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## 1. Stage 5 Mission
Summarize what this stage does and what it must avoid.

## 2. Input Summary
Summarize the bounded contexts and the business scenario being mapped.

## 3. Context Mapping Principles
State the business-domain rules used to create the context map.

## 4. Final Context Map Overview
Show the final context map as a clear business-domain map using plain text.

## 5. Context Relationship Matrix
For each important context relationship, include:
- upstream context
- downstream context
- relationship type
- exchanged business information
- ownership concern
- translation or handoff risk
- audit/evidence requirement

Use DDD relationship language where useful, such as:
- upstream/downstream
- partnership
- shared kernel
- published language
- anti-corruption boundary

## 6. Shared Kernel
List shared terms/statuses that must remain consistent across contexts.

## 7. Published Language / Handoff Vocabulary
List the key handoff terms that contexts must use consistently.

## 8. Partnership Relationships
Identify relationships that require joint ownership or coordinated decision flow.

## 9. Anti-Corruption and Translation Risks
Identify places where one context’s language could distort another context’s meaning — for example laboratory unit-conversion interfaces (mg/L vs µg/mL), MedDRA version translation across PV systems, product identity translation across RIM/ERP/IDMP, MES-to-warehouse genealogy handoffs, temperature-logger clock versus UTC reconciliation for cold-chain, and untrusted supplier PDF text extraction.

## 10. Known Gaps Mapped to Context Relationships
Map visible unresolved gaps to the context relationship where the gap appears.

## 11. Boundary Warnings
State what the team must not confuse or merge.

## 12. Stage 5 Quality Gate
List the checks that make the context map acceptable.

## 13. NEXT_STAGE_INPUT_BLOCK
Create a compact handoff block for Stage 6.

The block must include:
- final context list
- final context map summary
- key relationships
- shared kernel
- published language / handoff vocabulary
- known handoff risks
- non-negotiables
- candidate business events for event storming
- open questions

End the output with:

"Stage 5 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 6."

Write the completed artifact to `Docs/DDD-Lab/Phase 5/A5_Context_Map.md`.
