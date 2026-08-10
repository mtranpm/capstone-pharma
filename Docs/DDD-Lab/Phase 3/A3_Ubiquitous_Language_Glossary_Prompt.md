# Stage 3 Prompt — Ubiquitous Language Glossary

You are the context engineering assistant for an AI FDE × Domain-Driven Design workshop for Project AEGIS-PHARMA at NovaCura Therapeutics Group.

I have attached the Stage 2 input file for NovaCura Therapeutics Group.

Your task is to read the attached Stage 2 input and create a clean, structured Stage 3 Ubiquitous Language Glossary that will be used as the input for Stage 4 of the workshop.

Important rules:

1. Use only the attached Stage 2 input.
2. Do not invent new product, batch, compound, safety, quality or supply facts or records.
3. Do not solve the case yet.
4. Do not create architecture yet.
5. Do not introduce GenAI, RAG, MCP, agents, or technical implementation yet.
6. Keep this as a business-domain DDD artifact.
7. Preserve all non-negotiables around fail-closed handling of unresolved identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation and checkpoint state; read-only advisory behaviour; and auditability.
8. Do not provide medical, regulatory or legal advice.
9. Do not resolve identity, genealogy, unit, terminology, authority, consent, validation or evidence conflicts. Only identify them as workflow/domain language gaps.
10. Do not treat pharmaceutical systems or records (LIMS, MES, safety databases) as the domain. The domain is the regulated review and reconciliation work being performed.
11. Define language as used in this case, not as a universal regulatory or medical dictionary.

Create the output in the following format:

# A3 — Ubiquitous Language Glossary: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## 1. Stage 3 Mission
Summarize the purpose of Stage 3 in one clear paragraph.

## 2. Input Summary
Summarize the Stage 2 domain/subdomain map in business-domain terms.

## 3. Ubiquitous Language Principles
List the principles the workshop team must follow while defining shared language.

## 4. Core Domain Glossary
Define the central advisory-workflow terms.
For each term, include:
- term
- business meaning in this case
- likely owner or participant
- valid context
- risk if misunderstood

## 5. Subdomain-Specific Glossary
Define terms grouped by subdomain:
- Identity and Genealogy
- GxP Evidence Reconciliation (batch review)
- Unit and Terminology Standardisation
- Authority, Effective Date and Jurisdiction
- Consent, Entitlement and Privacy
- PV Case Intake and Signal Support
- Supply, Cold-Chain and Allocation
- Source and Document Governance
- Audit and Evidence
- Continuity, Reliability and Economy

For each term, include concise business meaning and risk if misunderstood.

## 6. Status, Exception, and Approval Language
Define important status terms, exception terms, and approval terms.

## 7. Ambiguous Terms Requiring Care
Identify terms that may be interpreted differently by quality, manufacturing, laboratory, PV/safety, regulatory, supply chain, privacy/entitlement, audit/quality, cybersecurity, or biostatistics roles.

## 8. Terms That Must Not Be Used Loosely
List terms that must not be used casually because they imply approval, release, rejection, certification, completion, ownership, or an executed regulated action.

## 9. Known Gaps Expressed in Ubiquitous Language
Restate the known gaps using the agreed business-domain language.
Do not resolve them.

## 10. Non-Negotiables Carried Forward
Restate the hard constraints that must remain active in later stages.

## 11. Open Questions for Stage 4
List open questions that should be carried into bounded context design.

## 12. STAGE_4_INPUT_BLOCK
Create a compact handoff block for Stage 4.

The block must include:
- main business domain
- core subdomains
- supporting subdomains
- key ubiquitous language terms
- terms requiring ownership clarity
- terms requiring approval clarity
- known gaps in standardized language
- non-negotiables
- open questions

End the output with:

"Stage 3 complete. Use the STAGE_4_INPUT_BLOCK as the main input for Stage 4."
