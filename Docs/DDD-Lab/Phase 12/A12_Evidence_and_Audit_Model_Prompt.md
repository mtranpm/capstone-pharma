# Stage 12 Prompt — Evidence and Audit Model

You are the context engineering assistant for an AI FDE × Domain-Driven Design workshop for Project AEGIS-PHARMA at NovaCura Therapeutics Group.

I have attached the Stage 12 input file created from Stage 11:

- `Docs/DDD-Lab/Phase 12/A12_Input_From_Stage11.md`

Your task is to read the Stage 12 input and create a clean, structured EVIDENCE AND AUDIT MODEL for the NovaCura Therapeutics Group (AEGIS-PHARMA) advisory workflows.

Important rules:

1. Use only the attached Stage 12 input and the provided, evidence-inventory data files:
   - `data/inject_evidence_map.csv`
   - `data/injects.json`
   - `data/DATA_DICTIONARY.csv`
   - `data/DATASET_PROFILE.csv`
2. Do not invent new product, batch, safety, quality, regulatory, clinical or supply facts, policies, or sources.
3. Do not create architecture yet.
4. Do not introduce GenAI, RAG systems, MCP, agents, vector databases, or technical implementation yet.
5. Keep this as a business and governance artifact describing what must be evidenced, what must be audited, and what traceability must hold across the advisory workflows.
6. Preserve all non-negotiables around fail-closed handling of unresolved identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation and checkpoint state; read-only advisory behaviour; and auditability.
7. Do not provide medical, regulatory or legal advice.
8. Do not resolve batch, safety, quality, regulatory, clinical or supply issues; identify them as evidence and audit gaps only.
9. Cite the `data/inject_evidence_map.csv` rows and the referenced `data/` files you use.
10. Every important output must remain traceable to product/batch/compound identity, material genealogy, source system, file path/row/record, unit, terminology version, authority reference, effective date, jurisdiction, event time/clock basis, consent/entitlement state, validation state, checkpoint state, version, human owner and status as applicable.
11. Treat supplied records as evidence, not truth.
12. The AI never releases, rejects, reprocesses, re-labels or recalls a batch; never makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions; and never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval.

Create the output in the following structure:

# A12 — Evidence and Audit Model: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## 1. Stage 12 Mission
Summarize what this stage does and what it must avoid.

## 2. Input Summary
Summarize the human decision ownership input and the evidence inventory being used.

## 3. Evidence and Audit Principles
State the principles used to model evidence and audit requirements.

## 4. Evidence Tracing Model
Define the traceability dimensions that must accompany every important output, citing the evidence map and file paths you rely on.

## 5. Evidence Source Register
List each evidence source used by the advisory workflows with:
- source
- evidence map citation
- file path
- trust level
- provenance
- lifecycle/versioning need
- who may authorise release

## 6. Audit Event Register
List each audit-relevant event with:
- event
- trigger
- bounded context
- accountable role
- audit fields required
- retention/immutability need

## 7. Evidence-to-Output Traceability
Show how a workflow output must point back to its underlying evidence rows and files.

## 8. Audit Requirement Register
List the audit requirements for each stage of the workflow with:
- workflow stage
- required audit records
- required evidence
- accountable role
- fail-closed default

## 9. Evidence/Truth Distinction Rules
State the rules for treating supplied records as evidence, not truth, and for marking uncertainty.

## 10. Unknowns, Uncertainties, and Suppressed Records
List how missing or conflicting evidence must be represented without being resolved.

## 11. Boundary Warnings
State what the team must not confuse while modeling evidence and audit.

## 12. Stage 12 Quality Gate
List the checks that make the evidence and audit model acceptable.

## 13. NEXT_STAGE_INPUT_BLOCK
Create a compact handoff block for Stage 13.

The block must include:
- traceability dimensions
- evidence source register summary
- audit event register summary
- evidence-to-output traceability summary
- evidence/truth distinction rules
- unknowns and suppressed records
- non-negotiables
- open questions for the evaluation suite

End the output with:

“Stage 12 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 13.”
