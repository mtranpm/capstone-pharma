# Stage 7 Prompt — Domain Model and Invariant Register

You are the context engineering assistant for an AI FDE × Domain-Driven Design workshop for Project AEGIS-PHARMA at NovaCura Therapeutics Group.

I have attached the Stage 7 input file created from Stage 6:

- `Docs/DDD-Lab/Phase 7/A7_Input_From_Stage6.md`

Your task is to read the Stage 7 input and create a clean, structured DOMAIN MODEL AND INVARIANT REGISTER for the NovaCura Therapeutics Group (AEGIS-PHARMA) advisory workflows.

Important rules:

1. Use only the attached Stage 7 input and its upstream case context.
2. Do not invent new product, batch, clinical, safety, quality or supply facts or records.
3. Do not solve the case yet.
4. Do not create architecture yet.
5. Do not introduce GenAI, RAG, MCP, agents, tools, system design, APIs, databases, or technical implementation.
6. Keep this as a business-domain DDD artifact.
7. Preserve all non-negotiables around fail-closed handling of unresolved identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation and checkpoint state; read-only advisory behaviour; and auditability.
8. Do not provide medical, regulatory or legal advice.
9. Do not resolve identity, genealogy, unit, terminology, authority, effective-date, jurisdiction, consent, validation, batch, safety or supply conflicts. Only model them as domain objects, states, gaps, exceptions, and invariants.
10. Use DDD language carefully:
    - Entities have identity and lifecycle.
    - Value objects describe attributes without independent identity.
    - Aggregates define consistency and ownership boundaries.
    - Invariants define rules that must always hold true in the business domain.
11. Keep human ownership visible for identity/genealogy resolution, unit/terminology acceptance, OOS/OOT disposition, supplier-evidence verification, QP certification, batch release/rejection, PV dispositions, allocation/recall decisions, consent/entitlement decisions, authority/approval, overrides, and closure.

Create the output in the following structure:

# A7 — Domain Model and Invariant Register: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## 1. Stage 7 Mission
Summarize what this stage does and what it must avoid.

## 2. Input Summary
Summarize the event storming input, representative scenario, contexts, known gaps, and non-negotiables being used.

## 3. Domain Modeling Principles
State the modeling rules used for entities, value objects, aggregates, invariants, ownership, unresolved exceptions, and auditability.

## 4. Candidate Domain Object Classification
Create a table with:
- candidate object
- classification: entity, value object, aggregate root, policy/rule, evidence/audit artifact, or external reference
- primary bounded context
- reason for classification
- notes / caution

## 5. Entity Register
List the main entities with:
- entity
- identity
- lifecycle
- owner / accountable business role
- key states
- important relationships

## 6. Value Object Register
List the main value objects with:
- value object
- describes
- examples from case
- validation or consistency concern

## 7. Aggregate Register
List the main aggregates with:
- aggregate root
- owned objects
- consistency responsibility
- business owner
- what the aggregate must not own

## 8. Aggregate Detail Canvases
For each major aggregate, provide a concise canvas:
- purpose
- owned terms
- owned state
- commands/activities that affect it
- events it emits or records
- invariants it enforces
- external dependencies
- audit needs

## 9. Invariant Register
Create a table with:
- invariant ID
- invariant statement
- aggregate / context
- source rule or case fact
- human owner
- failure risk if violated
- audit evidence required

Include invariants that enforce fail-closed behaviour, for example: an evidence output must not be produced while product/batch/compound identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved; a batch must not be shown as release-ready while any genealogy branch or release-packet element is unresolved or unverified; no final PV seriousness, causality, expectedness, reportability or signal-confirmation decision may be attributed to the AI; no allocation recommendation may be executed without explicit authorised human approval; no inventory status change, capacity reservation, stock allocation, shipment or recall initiation may be performed by the AI; source authority must be resolved before a source is cited as decisive; entitlement/consent must be rechecked before patient/participant data is surfaced; and every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable.

## 10. Unresolved Exceptions Captured as Domain State
Show how the known case gaps remain represented without being resolved (genealogy break for SUA-88, mg/L vs µg/mL unit assumption, OOS/OOT/invalid dispute, unverified supplier-audit commitment, back-entered batch-record step, 47-minute audit-capture gap, disputed awareness date, duplicate ICSR candidates, MedDRA version mismatch, listedness conflict, cold-chain logger/pallet dispute, missing aggregation, excipient shortage, CMO capacity conflict, validation-state ambiguity, untrusted documents, eConsent asynchrony, amendment not approved in one country).

## 11. Human Decision Ownership Preserved in the Model
Map decisions to human owners and state what the model must not allow to be bypassed.

## 12. Audit and Evidence Requirements
List what must be traceable across the domain model.

## 13. Boundary Warnings
State what the team must not confuse while modeling.

## 14. Stage 7 Quality Gate
List the checks that make the domain model and invariant register acceptable.

## 15. NEXT_STAGE_INPUT_BLOCK
Create a compact handoff block for Stage 8.

The block must include:
- final entities
- final value objects
- final aggregate roots
- key aggregate boundaries
- invariant register summary
- known unresolved exceptions as domain state
- human decision ownership rules
- audit/evidence requirements
- open questions for Stage 8

End the output with:

"Stage 7 complete. Use the NEXT_STAGE_INPUT_BLOCK as the main input for Stage 8."
