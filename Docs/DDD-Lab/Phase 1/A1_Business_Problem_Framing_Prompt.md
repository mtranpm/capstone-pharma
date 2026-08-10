# A1 — Business Problem Framing Prompt

You are the context engineering assistant for an AI FDE × Domain-Driven Design workshop for Project AEGIS-PHARMA at NovaCura Therapeutics Group.

I have attached the Stage 1 input file generated from Stage 0:

1. `Docs/DDD-Lab/Phase 1/A1_Input_From_Stage0.md`

Your task is to read the attached Stage 1 input and create a clean, structured **Stage 1 Business Problem Framing** output for NovaCura Therapeutics Group (AEGIS-PHARMA).

Important rules:

1. Use only the attached Stage 1 input.
2. Do not invent new product, batch, clinical, safety, quality or supply facts or records.
3. Do not solve the case yet.
4. Do not create architecture yet.
5. Do not introduce GenAI, RAG, MCP, agents, or technical implementation yet.
6. Keep this as a business-domain problem framing artifact.
7. Preserve all non-negotiables around fail-closed handling of unresolved product/batch/compound identity, genealogy, unit, terminology, clock/time, source, authority, effective date, jurisdiction, consent/entitlement, validation and checkpoint state; read-only advisory behaviour; and auditability.
8. Do not provide medical, regulatory or legal advice.
9. Do not resolve product/batch/compound identity, genealogy, unit, terminology, authority, consent, validation or evidence conflicts. Only identify them as business-domain gaps, risks, or exceptions.
10. Do not create domain/subdomain maps yet. That belongs to Stage 2.
11. Do not create ubiquitous language yet. That belongs to Stage 3.
12. Do not create bounded contexts yet. That belongs to a later stage.
13. Keep every workflow inside the three mandatory advisory workflows (Workflow A — GxP evidence reconciliation for batch-review readiness; Workflow B — Pharmacovigilance case-intake and signal-support; Workflow C — Bounded supply-shortage and cold-chain recovery planner).

Create the output as a downloadable Markdown file named:

```text
A1_Business_Problem_Framing.md
```

Use the following structure:

# A1 — Business Problem Framing: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## 1. Stage 1 Mission
Summarize what Stage 1 is meant to accomplish in one clear paragraph.

## 2. Business Problem Statement
Create one clear business problem statement without technology or solution language.

## 3. Problem Narrative
Explain the current enterprise problem — a global pharmaceutical company facing converging batch, safety, quality, supply, cyber and inspection events — as a business-domain narrative. Anchor the representative scenario at the disputed biologics batch NCB204-B24071 as described in the Stage 1 input.

## 4. Problem Decomposition
Separate the problem into:
- product and batch identity/genealogy risk (unresolved identity, missing genealogy, unit conversion, OOS/OOT state)
- evidence and provenance risk (missing, conflicting, untrusted and poorly attributable evidence)
- terminology, authority and jurisdictional risk (inconsistent terminology, authority hierarchy, effective dates, jurisdictions)
- consent, entitlement and privacy risk (patient/participant data, cross-border routing, secondary use)
- safety-case and reporting risk (duplicate ICSRs, disputed awareness dates, listedness/expectedness conflicts)
- supply and cold-chain risk (shortage, allocation constraints, logger/aggregation disputes, CMO capacity)
- operational, reliability and economic risk (ransomware, downtime, cost, vendor and telemetry)
- ownership and exception-handling risk

## 5. Affected Roles and Functions
List the business and pharmaceutical roles/functions affected by the problem. Do not assign new authority or invent owners.

## 6. Business Impact
Explain why the problem matters to the organization using only the provided Stage 1 input.

## 7. Desired Business Outcomes
List the outcomes the organization wants to achieve.

## 8. Scope Boundary for Stage 1
Separate:
- in scope
- out of scope

## 9. Non-Negotiables and Safety Boundaries
Restate the hard boundaries that must govern all later stages.

## 10. Known Gaps and Exceptions
List the unresolved gaps and exceptions without resolving them.

## 11. Open Questions for Stage 2
List open questions that should guide Stage 2.

## 12. STAGE_2_INPUT_BLOCK
Create a compact handoff block for Stage 2.

The block must include:
- business problem statement
- affected roles/functions
- desired outcomes
- non-negotiables
- known gaps/exceptions
- open questions for domain and subdomain discovery

End the output with:

“Stage 1 complete. Use the STAGE_2_INPUT_BLOCK as the main input for Stage 2.”
