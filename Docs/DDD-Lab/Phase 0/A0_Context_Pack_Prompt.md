# Prompt — A0 Context Pack

You are the context engineering assistant for an AI FDE × Domain-Driven Design workshop for Project AEGIS-PHARMA at NovaCura Therapeutics Group.

I have attached two files:

1. Full challenge case study for NovaCura Therapeutics Group (AEGIS-PHARMA) — `case/INTEGRATED_CASE.md` plus the four case evidence packs (`case/STAKEHOLDER_PACK.md`, `case/SOURCE_SYSTEM_FACT_PACK.md`, `case/REGULATORY_BOUNDARY_PACK.md`, and the integrated case itself).
2. Synthetic evidence inventory for the Stage 0 exercise — `data/inject_evidence_map.csv`, `data/injects.json`, `data/DATA_DICTIONARY.csv`, `data/DATASET_PROFILE.csv` and the referenced data files.

Your task is to read both attached inputs and create a clean, structured CONTEXT PACK that will be used as the input for Stage 1 of the workshop.

Important rules:

1. Use only the attached case and synthetic evidence.
2. Do not invent new product, batch, clinical, safety, quality or supply facts or records.
3. Do not solve the case yet.
4. Do not create architecture yet.
5. Do not introduce GenAI, RAG, MCP, agents, or technical implementation yet.
6. Keep this as a business-domain context pack.
7. Preserve all non-negotiables around fail-closed handling of unresolved product/batch/compound identity, genealogy, unit, terminology, clock/time, source, authority, effective date, jurisdiction, consent/entitlement, validation state and checkpoint state; read-only advisory behaviour; auditability; and preservation of human accountability for regulated decisions (batch release/rejection, PV dispositions, allocation, recall).
8. Do not provide medical, regulatory or legal advice.
9. Do not resolve product/batch/compound identity, genealogy, unit, terminology, authority, consent, validation or evidence conflicts. Only identify them as workflow/domain gaps.
10. Keep every workflow inside the three mandatory advisory workflows (Workflow A — GxP evidence reconciliation for batch-review readiness; Workflow B — Pharmacovigilance case-intake and signal-support; Workflow C — Bounded supply-shortage and cold-chain recovery planner). The AI must never release, reject, reprocess, re-label or recall a batch; must never make final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions; and must never change inventory status, reserve capacity, allocate stock, ship product or initiate a recall without explicit authorized human approval.

Create the output as a downloadable Markdown file named:

```text
A0_Context_Pack.md
```

Use the following structure:

```markdown
# A0 — Context Pack: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## 1. Workshop Mission
## 2. Organization Snapshot
## 3. Business Problem
## 4. Business Goals
## 5. Non-Negotiables
## 6. Representative Scenario Summary
## 7. Synthetic Evidence Inventory
## 8. Known Gaps and Exceptions
## 9. Workshop Guardrails
## 10. NEXT_STAGE_INPUT_BLOCK
```

Ground the organization snapshot in the four case packs: `case/STAKEHOLDER_PACK.md`, `case/SOURCE_SYSTEM_FACT_PACK.md`, `case/REGULATORY_BOUNDARY_PACK.md` and `case/INTEGRATED_CASE.md`. Anchor the representative scenario at the converging-event situation described in the case: the pivotal-trial amendment, the disputed biologics batch NCB204-B24071, emerging safety reports, the sterile-area excursion, the cold-chain failure, the excipient shortage, the ransomware event and the multi-agency inspection request. Surface the evidence inventory using `data/inject_evidence_map.csv` and `data/injects.json`, and cite the `data/` files used.

End the output with:

> "Stage 0 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 1."
