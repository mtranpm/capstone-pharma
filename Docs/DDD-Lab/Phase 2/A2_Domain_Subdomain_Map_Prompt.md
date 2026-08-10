# Stage 2 Prompt — Domain and Subdomain Map

You are the context engineering assistant for an AI FDE × Domain-Driven Design workshop for Project AEGIS-PHARMA at NovaCura Therapeutics Group.

I have attached the Stage 1 input file for NovaCura Therapeutics Group.

Your task is to read the attached Stage 1 input and create a clean, structured Stage 2 Domain and Subdomain Map that will be used as the input for Stage 3 of the workshop.

Important rules:

1. Use only the attached Stage 1 input.
2. Do not invent new product, batch, clinical, safety, quality or supply facts or records.
3. Do not solve the case yet.
4. Do not create architecture yet.
5. Do not introduce GenAI, RAG, MCP, agents, or technical implementation yet.
6. Keep this as a business-domain DDD artifact.
7. Preserve all non-negotiables around fail-closed handling of unresolved product/batch/compound identity, genealogy, unit, terminology, clock/time, source, authority, effective date, jurisdiction, consent/entitlement, validation and checkpoint state; read-only advisory behaviour; and auditability.
8. Do not provide medical, regulatory or legal advice.
9. Do not resolve product/batch/compound identity, genealogy, unit, terminology, authority, consent, validation or evidence conflicts. Only identify them as workflow/domain gaps.
10. Do not treat pharmaceutical systems or records as the domain. The domain is the regulated review and reconciliation work being performed.
11. Keep every workflow inside the three mandatory advisory workflows (Workflow A — GxP evidence reconciliation for batch-review readiness; Workflow B — Pharmacovigilance case-intake and signal-support; Workflow C — Bounded supply-shortage and cold-chain recovery planner).

Create the output in the following format:

# A2 — Domain and Subdomain Map: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## 1. Stage 2 Mission
Summarize the purpose of Stage 2 in one clear paragraph.

## 2. Input Summary
Summarize the Stage 1 business problem in business-domain terms.

## 3. Main Business Domain
Identify the main domain represented by the case and explain why it is the main domain.

## 4. Core Subdomains
Identify the core subdomains that are central to the three mandatory advisory workflows:
- GxP evidence reconciliation for batch-review readiness
- Pharmacovigilance case-intake and signal-support
- Bounded supply-shortage and cold-chain recovery planning

For each core subdomain, include:
- subdomain name
- business purpose
- key responsibilities
- key risks if weak or missing

## 5. Supporting Subdomains
Identify supporting subdomains required for the core advisory work.
For each supporting subdomain, include:
- subdomain name
- business purpose
- why it supports the core domain

## 6. Generic / Reusable Organizational Capabilities
Identify reusable capabilities that are important but not unique to the advisory workflows.

## 7. Domain and Subdomain Map
Create a clean text map showing the main domain, core subdomains, supporting subdomains, and generic/reusable capabilities.

## 8. Known Gaps Mapped to Subdomains
Map the known gaps and exceptions from Stage 1 to the relevant subdomains.
Do not resolve them.

## 9. Ownership Signals for Later Stages
Identify which business roles or functions appear to be natural owners or participants for each subdomain.
Do not finalize accountability yet.

## 10. Boundary Warnings
List boundary mistakes the workshop team must avoid at this stage.

## 11. Non-Negotiables Carried Forward
Restate the hard constraints that must remain active in later stages.

## 12. Open Questions for Stage 3
List open questions that should be carried into the ubiquitous language stage.

## 13. STAGE_3_INPUT_BLOCK
Create a compact handoff block for Stage 3.

The block must include:
- main business domain
- core subdomains
- supporting subdomains
- reusable capabilities
- known gaps mapped to subdomains
- ownership signals
- non-negotiables
- terms needing precise definition
- open questions

End the output with:

"Stage 2 complete. Use the STAGE_3_INPUT_BLOCK as the main input for Stage 3."
