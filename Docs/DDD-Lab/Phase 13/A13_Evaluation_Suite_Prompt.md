# Stage 13 Prompt — Evaluation Suite

You are the context engineering assistant for an AI FDE × Domain-Driven Design workshop for Project AEGIS-PHARMA at NovaCura Therapeutics Group.

I have attached the Stage 13 input file created from Stage 12:

- `Docs/DDD-Lab/Phase 13/A13_Input_From_Stage12.md`

Your task is to read the Stage 13 input and create a clean, structured EVALUATION SUITE for the NovaCura Therapeutics Group (AEGIS-PHARMA) advisory workflows.

Important rules:

1. Use only the attached Stage 13 input and its upstream case context.
2. Do not invent new product, batch, compound, clinical, safety, quality or supply facts, policies, or sources.
3. Do not create architecture yet.
4. Do not introduce GenAI, RAG systems, MCP, agents, vector databases, or technical implementation yet.
5. Keep this as an evaluation-design artifact for the three mandatory advisory workflows.
6. Preserve all non-negotiables around fail-closed handling of unresolved identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation and checkpoint state; read-only advisory behaviour; and auditability.
7. Do not provide medical, regulatory or legal advice.
8. Do not resolve identity, genealogy, unit, terminology, authority, OOS/OOT, supplier, PV, cold-chain, shortage, capacity or allocation issues.
9. The AI must never release, reject, reprocess, re-label or recall a batch; must never make final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions; and must never change inventory status, reserve capacity, allocate stock, ship product or initiate a recall without explicit authorised human approval.
10. Evaluation must measure the right behaviour, not just fluency. Correctness must include fail-closed behaviour on unresolved inputs, traceability to evidence, and respect for human decision ownership.

Create the output in the following structure:

# A13 — Evaluation Suite: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## 1. Stage 13 Mission
Summarize what this stage does and what it must avoid.

## 2. Input Summary
Summarize the evidence and audit model and the non-negotiables being used.

## 3. Evaluation Principles
State the principles used to design the evaluation suite.

## 4. Evaluation Scope
Define the three advisory workflows being evaluated and their boundaries.

## 5. Capability-to-Scenario Matrix
Map each required capability to the scenarios that test it.

## 6. Scenario Register
For each scenario, include:
- scenario ID
- scenario name
- workflow under test
- scenario type: positive, negative, edge, adversarial, or fail-closed
- input setup
- expected behaviour
- expected fail-closed behaviour
- evidence citation requirement
- human decision boundary

## 7. Evaluation Assertion Register
For each assertion, include:
- assertion ID
- scenario ID
- assertion statement
- pass condition
- traceability requirement
- owner

## 8. Fail-Closed Behaviour Evaluation
List the fail-closed checks that must be evaluated for unresolved identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation, and checkpoint state.

## 9. Traceability and Provenance Evaluation
List the traceability checks that must verify outputs point back to evidence.

## 10. Guardrail Compliance Evaluation
List the checks that verify deterministic rules, human review points, and human authorization boundaries are respected.

## 11. Anti-Patterns and Bias Checks
List the checks that detect unsafe automation patterns, hallucinations, and bias.

## 12. Evaluation Metrics and Thresholds
List the metrics and thresholds for evaluating the suite. Correctness must include fail-closed behaviour, traceability, and human-ownership respect, not just fluency. Include both qualitative and quantitative indicators appropriate to a governance evaluation suite.

## 13. Human-AI Interaction Evaluation
List the checks for clarity of the human decision points and the trustworthiness of the AI advisory output.

## 14. Boundary Warnings
State what the team must not confuse while designing the evaluation suite.

## 15. Stage 13 Quality Gate
List the checks that make the evaluation suite acceptable.

## 16. NEXT_STAGE_INPUT_BLOCK
Create a compact handoff block for Stage 14.

The block must include:
- evaluation scope
- capability-to-scenario matrix summary
- scenario register summary
- assertion register summary
- fail-closed behaviour checks
- traceability checks
- guardrail compliance checks
- metrics and thresholds
- non-negotiables
- open questions for the minimum governed workflow

End the output with:

“Stage 13 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 14.”
