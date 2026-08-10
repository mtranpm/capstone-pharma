# Case Discovery Understanding Notes

## Purpose of this note

This file captures the working understanding discussed during discovery for Project AEGIS-PHARMA.

It is **not** a Cursor-ready development task. Use it as a plain-language discovery and onboarding note before writing formal artefacts such as SCQA, PRD, DDD, ADRs, threat model, evaluation strategy and final defence material.

## Project context

Project AEGIS-PHARMA is a synthetic pharmaceutical AI capstone. It represents a fictional global pharma company, **NovaCura Therapeutics Group**, facing fragmented evidence across quality, manufacturing, pharmacovigilance, supply, regulatory and clinical operations.

The central challenge is not simply to build an AI chatbot. The challenge is to design a defensible enterprise system that helps humans:

- find relevant evidence,
- reconcile conflicting evidence,
- explain gaps and risks,
- prepare review packets,
- defend conclusions with provenance,
- stay inside regulated safety and quality boundaries.

The system must remain advisory. It must not make or execute final regulated decisions.

## NovaCura and the business problem

NovaCura is the pharmaceutical company in the case. It owns the product, quality accountability, safety accountability and regulated decision-making.

The problem statement can be understood as:

> NovaCura needs to accelerate evidence review across batch quality, pharmacovigilance and supply operations, but the evidence is fragmented, contradictory, time-sensitive and controlled by strict regulatory, safety, privacy and GxP boundaries.

The AI system should help humans prepare and understand evidence faster, but it should not replace the accountable Quality, Safety, Regulatory or Supply decision-maker.

## What the `knowledge/` folder is used for

The `knowledge/` folder acts as the controlled policy and reference pack for the case.

It helps determine:

- which rules or policies are approved,
- which documents are superseded,
- which documents are untrusted,
- which evidence can be relied on,
- what the AI is allowed to say or do,
- when the AI must abstain,
- which human role remains accountable.

The knowledge files should be treated as authority-controlled documents, not just background text. The system should check document status, effective date and trust level before using a knowledge file as support.

## Relationship between case, data, knowledge and evaluation

| Area | Role |
|---|---|
| `case/` | Describes the fictional enterprise, inject catalogue, operating context and problem space |
| `data/` | Contains synthetic source-system records used as evidence |
| `knowledge/` | Contains policy, rule and authority documents |
| `source_documents/` | Contains short synthetic source-document extracts that provide document-level context behind selected records |
| `sources/` | Contains offline regulatory and standards reference guidance plus optional external research anchors |
| `runbooks/` | Contains challenge-provided execution and participant guidance runbooks |
| `templates/` | Contains blank artefact templates for participant deliverables |
| `evaluation/public_fixtures/` | Contains ready-made test scenarios |
| `evaluation/contracts/` | Defines required structured output shapes |
| `requirements/` | Defines artefact, scoring, submission and defence expectations |
| `submission/` | Participant-created artefacts, code, tests, runbooks and evidence |

The application should read from case/data/knowledge/evaluation, but participant-created work should be stored under `submission/`.

## Business-relevant sections to use first

This discovery note is mainly for **business understanding**. The most important repository areas for that purpose are the ones that explain the business scenario, evidence, risks, stakeholders, controls and evaluation expectations.

Use these first:

| Folder or file | Business use |
|---|---|
| `case/` | Main business scenario, NovaCura context, inject catalogue, stakeholder context, source-system facts and regulatory boundary |
| `data/` | Synthetic operational records showing what happened across batch, PV, supply, clinical, regulatory, security and operations |
| `knowledge/` | Case-specific policy and authority documents that define what can be trusted, what is superseded and when the system must abstain |
| `source_documents/` | Short source-document extracts that explain specific records, document versions, audit commitments, labels, protocol context and authority correspondence |
| `sources/` | Regulatory and standards background used to frame GxP, PV, privacy, validation, security and AI-governance requirements |
| `evaluation/public_fixtures/` | Business test scenarios that show how the system should be challenged in batch, PV, supply, security, privacy, reliability and other domains |
| `requirements/` | Business-grade completion expectations, scoring model, final defence requirements and evidence standard |
| `templates/` | Blank structures for business artefacts such as business case, DMAIC, DDD, architecture, risk, evaluation and final pitch |
| `runbooks/` | Participant working method and repository execution guidance |
| `prompts/PROMPT_LIBRARY.md` | Safe discovery and review prompts for problem qualification, evidence mapping, threat modelling and defence preparation |
| `submission/` | The participant-owned workspace where completed artefacts, solution code, tests, evidence and runbooks should be created |

Business discovery should answer:

- What is the measurable business problem?
- Which decisions are affected?
- Who owns each decision?
- What evidence is fragmented or conflicting?
- Which workflow is in scope?
- Which AI use is allowed?
- Which AI use is prohibited?
- What regulatory or safety boundary applies?
- What evidence would a human reviewer need?
- What must be demonstrated in the final defence?

Business understanding should not start with:

- choosing a model,
- designing agents,
- building a UI,
- creating a knowledge graph,
- automating tool actions,
- optimizing prompts before evidence is mapped.

The business-first framing is:

> NovaCura needs faster, safer evidence reconciliation across regulated workflows. The system must help humans understand and defend evidence, not replace accountable regulated decisions.

## Technical/specification sections to use later

Some folders are less important for initial business understanding, but they become important when converting discovery into specs, implementation, validation and defence evidence.

Use these during specification and build planning:

| Folder or file | Technical/spec use |
|---|---|
| `evaluation/contracts/` | JSON schemas and output contracts that the solution must satisfy |
| `evaluation/contract_samples/` | Example contract-shaped outputs or samples for implementation reference |
| `app/` | Offline evidence/inject explorer supplied with the package, useful for browsing case content locally |
| `starter/` | Intentionally unsafe brownfield starter code used for modernization, risk assessment and baseline diagnostics |
| `tools/` | Verification and validation scripts, including package checks, contract tests, submission structure checks and hash generation |
| `.cursor/` | Cursor-specific rules, commands, skills and agents for guided delivery |
| `submission/scripts/` | Participant-created setup, run, test, evaluate, reset and evidence-export commands |
| `submission/tests/` | Participant-created deterministic, adversarial, outage, recovery and prohibited-action tests |
| `submission/evidence/` | Participant-created machine-readable evidence, manifests, hashes, test results and evaluation results |
| `submission/runbooks/` | Participant-created operational runbooks for setup, run, evaluation, incident response, AI-disabled continuity, deployment and retirement |
| `project plan/` | Planning workbooks and WBS material, useful for delivery planning rather than case evidence |
| `tmp/` | Generated workbook JSONs and helper scripts, useful only if maintaining project plan artefacts |

Technical/specification work should translate business understanding into:

- requirements,
- acceptance criteria,
- domain model,
- architecture,
- ADRs,
- data contracts,
- output schemas,
- test strategy,
- threat model,
- validation plan,
- runbooks,
- evaluation evidence.

Spec principle:

> Business discovery explains what problem must be solved and what boundaries must hold. Technical specs explain how the solution will prove those boundaries through contracts, tests, controls, evidence and reproducible execution.

## What the `data/` folder is used for

The `data/` folder contains the synthetic source-system datasets for the capstone. It is the main operational evidence layer for the case.

Most files are CSV datasets, with a few JSON or metadata files. The records are deliberately small but cross-linked, so participants can inspect them manually and build deterministic tests.

Plain-language understanding:

> `data/` contains the evidence records the system must search, compare, reconcile, cite and preserve. It should be treated as challenge evidence and should not be modified directly.

### Major dataset groups

The folder includes datasets across several enterprise domains:

| Domain | Example files | What they support |
|---|---|---|
| Batch / Quality | `batches.csv`, `lab_results.csv`, `material_genealogy.csv`, `warehouse_movements.csv`, `oos_investigations.csv`, `release_packets.csv`, `deviations.csv`, `capa_records.csv` | Batch-review evidence readiness, genealogy gaps, unit issues, OOS/OOT conflicts and release packet gaps |
| Pharmacovigilance | `icsr_cases.csv`, `adverse_events.csv`, `duplicate_candidates.csv`, `safety_receipts.csv`, `listedness_sources.csv`, `product_complaints.csv` | PV intake support, duplicate detection, listedness context and source preservation |
| Clinical | `clinical_trials.csv`, `protocol_versions.csv`, `site_approvals.csv`, `subjects.csv`, `eligibility_evidence.csv`, `consents.csv` | Protocol versioning, site applicability, consent and eligibility evidence |
| Supply / Cold chain | `inventory.csv`, `shipments.csv`, `temperature_loggers.csv`, `demand_forecast.csv`, `cmo_capacity.csv`, `allocation_constraints.csv` | Supply recovery planning, cold-chain evidence, demand constraints and non-executing options |
| Regulatory / Documents | `authority_correspondence.csv`, `regulatory_commitments.csv`, `ectd_sequences.csv`, `document_catalog.csv`, `document_lineage.csv` | Regulatory commitments, authority correspondence, document provenance and due-date reconciliation |
| Security / AI governance | `access_logs.csv`, `users_entitlements.csv`, `tool_catalog.csv`, `tool_manifest_poisoned.json`, `model_registry.csv`, `model_performance.csv`, `agent_runs.csv` | Authorization, tool governance, model governance, agent reliability and abuse testing |
| Economics / Operations | `cost_model.csv`, `model_costs.csv`, `model_usage.csv`, `downtime_events.csv`, `continuity_requirements.csv`, `backup_inventory.csv` | FinOps, reliability, outage behavior, continuity and recovery planning |
| Metadata / Traceability | `DATASET_PROFILE.csv`, `DATA_DICTIONARY.csv`, `injects.json`, `inject_evidence_map.csv`, `INJECT_TEST_COVERAGE.csv`, `RELATIONSHIP_MODEL.csv` | Understanding dataset shape, fields, hashes, inject mapping, coverage and data relationships |

### Important metadata files

- `DATASET_PROFILE.csv`
  - Lists each dataset, row count, column count, header and SHA-256 hash.
  - Useful for integrity checks and understanding dataset shape.

- `DATA_DICTIONARY.csv`
  - Describes dataset columns, inferred types, nullability and examples.
  - Useful for data contracts, parsing logic and evidence mapping.

- `injects.json`
  - Structured list of injects and challenge conditions.
  - Useful for requirements, test design and traceability.

- `inject_evidence_map.csv`
  - Maps inject IDs to the evidence files where supporting or conflicting evidence appears.
  - Useful for finding which data sources belong to each scenario.

- `INJECT_TEST_COVERAGE.csv`
  - Tracks public or expected test coverage against injects.
  - Useful for evaluation planning.

- `RELATIONSHIP_MODEL.csv`
  - Describes relationships between datasets.
  - Useful for DDD, data lineage and evidence graph design.

### How the AI system should use `data/`

The system should:

- read data files as immutable challenge evidence,
- preserve source paths and row-level references where possible,
- use `DATA_DICTIONARY.csv` to understand fields,
- use `inject_evidence_map.csv` to locate relevant evidence for each inject,
- use `DATASET_PROFILE.csv` and hashes for integrity checks,
- reconcile records across files rather than relying on one source,
- cite the datasets used in every material conclusion,
- distinguish source facts from interpretations,
- avoid silently transforming units, dates, identifiers or terminology,
- fail closed when evidence is missing, contradictory, stale, untrusted or outside authority.

The system should not:

- overwrite original data,
- correct source records in place,
- hide contradictions,
- merge safety cases irreversibly,
- silently normalize units,
- make regulated decisions directly from data alone.

### Example discovery use

For `PUB-01`, the batch workflow should inspect data such as:

- `batches.csv`,
- `lab_results.csv`,
- `interface_mappings.csv`,
- `material_genealogy.csv`,
- `warehouse_movements.csv`,
- `oos_investigations.csv`,
- `release_packets.csv`,
- `supplier_audits.csv`,
- `certificates_analysis.csv`.

The goal is to produce an evidence-readiness view, not a batch disposition decision.

Discovery implication:

> The `data/` folder is the operational evidence backbone of the project. It drives requirements, DDD entities, lineage, tests, evaluation, audit evidence and final defence.

## What the `source_documents/` folder is used for

The `source_documents/` folder contains local synthetic extracts of important source documents. These are not general policy files like the `knowledge/` folder. They are document-level evidence snippets that give context behind selected data records and injects.

Use the folder to understand what a referenced document says, what version or status it has, and what limitation still requires human review.

Examples in this folder include:

- `LIMS_result_contract_v1.md` and `LIMS_result_contract_v2.md`
  - Explain LIMS result contract fields and version differences.
  - Important for unit handling, UCUM validation and avoiding silent unit normalization.

- `Protocol_NCB204_301_v4_1.md` and `Protocol_NCB204_301_v5_0.md`
  - Show that global protocol currency and local site applicability can differ.
  - Important for clinical/protocol evidence, especially where a newer global protocol is not yet locally approved.

- `CCDS_NCB204_v4.md`
  - Provides core safety information context.
  - Important for PV listedness and safety review, but it does not make a case-level expectedness decision.

- `CMO_audit_commitment_2025_14.md`
  - Shows a supplier claims an audit commitment is closed, while NovaCura verification is not recorded.
  - Important for release packet and supplier evidence gaps.

- `Cold_chain_logger_association_SH_901.md`
  - Shows logger-to-pallet association and timezone uncertainty.
  - Important for cold-chain and supply evidence reconciliation.

- `EMA_letter_2026_114.md`
  - Shows regulatory correspondence with a possible due-date conflict.
  - Important for regulatory response tracking and deadline reconciliation.

Plain-language understanding:

> `source_documents/` is where selected original-style document extracts live. They help explain the meaning, version, status and limitations of evidence found in `data/`. They should be cited as supporting evidence, but they do not automatically authorize regulated decisions.

How it differs from `knowledge/`:

| Folder | Main purpose |
|---|---|
| `knowledge/` | Policy, authority, rules, standards and control expectations |
| `source_documents/` | Short source-document extracts that support or challenge specific evidence records |

How it should be used by the AI system:

- Retrieve relevant extracts when a data record references a document, protocol, contract, label, audit commitment, logger note or authority letter.
- Check version, status, effective date, local applicability and stated limitations.
- Use the extract to explain evidence conflicts or uncertainty.
- Cite the extract as supporting evidence where relevant.
- Avoid treating the extract as final approval, disposition, eligibility, reportability or allocation authority.
- Abstain or require human review when the extract says applicability, verification or normalization is unresolved.

Key discovery implication:

> The `source_documents/` folder is part of the evidence fabric. It bridges structured data records and narrative document evidence, so it is important for provenance, traceability, version control and defensible human review.

## What the `sources/` folder is used for

The `sources/` folder contains regulatory and standards reference material for the workshop. It is different from `case/`, `data/`, `knowledge/` and `source_documents/`.

Its purpose is to help participants understand the real-world regulatory and standards concepts that shape the capstone boundaries. It does not contain the solution to the case, and it should not be treated as a controlled legal opinion.

Files in this folder:

- `LOCAL_REGULATORY_AND_STANDARDS_GUIDE.md`
  - A concise offline guide for the workshop.
  - Summarizes key concepts around electronic records, GxP computerized systems, quality and manufacturing, clinical development, pharmacovigilance, privacy, AI governance and security.
  - Useful when internet access is not available.

- `REFERENCE_SOURCES.md`
  - A list of optional external research anchors.
  - Points to examples such as FDA Part 11, FDA computer software assurance, EU GMP, Annex 11, Annex 15, ICH E6, ICH Q9, EMA GVP, ISO IDMP/SPOR, CDSCO clinical trial rules and WHO GMP/data-integrity guidance.
  - These links inform the challenge boundaries but do not provide a case answer.

Plain-language understanding:

> `sources/` is the workshop reference library. It helps explain the regulatory and standards background behind the capstone, but participants must still verify current jurisdictional applicability before making legal, regulatory or compliance claims.

How it differs from nearby folders:

| Folder | Main purpose |
|---|---|
| `knowledge/` | Case-specific policy, authority and control documents used by the solution |
| `source_documents/` | Synthetic document extracts tied to specific evidence records |
| `sources/` | General regulatory and standards references for learning and framing |
| `requirements/` | Mandatory deliverable, scoring, evidence and defence expectations |

How it should be used during discovery:

- Use it to understand why GxP, data integrity, human accountability, audit trails, validation, privacy and security controls matter.
- Use it to frame intended use, prohibited use, regulated-record boundaries and human decision rights.
- Use it to support discovery artefacts, threat models, GxP analysis, privacy analysis and final defence.
- Do not copy external claims blindly.
- Do not treat the listed links as automatically current or jurisdictionally applicable.
- Always document jurisdiction, intended purpose, applicable date/version, source, assumptions and residual uncertainty.

Important boundary:

> `sources/` supports regulatory reasoning. It does not override the case evidence, does not authorize regulated actions and does not remove the need for human expert review.

## What the root `runbooks/` folder is used for

The root `runbooks/` folder contains challenge-provided guidance for how participants should execute the capstone. It is different from `submission/runbooks/`.

Root `runbooks/` is read-only guidance from the package. `submission/runbooks/` is where participant-created operational runbooks should be written for the final solution.

Files in the root folder:

- `runbooks/PARTICIPANT_RUNBOOK.md`
  - Provides the recommended delivery phases:
    - Qualify
    - Investigate
    - Specify
    - Build
    - Break and recover
    - Transfer and defend
  - The key message is: do not start with a model or agent. Start with the measurable problem, evidence, no-AI alternatives, assumptions, specifications and tests.

- `runbooks/REPO_EXECUTION.md`
  - Explains how to run repository-level checks and local execution:
    - `python run_capstone.py --check`
    - `run_capstone.ps1`
    - `run_capstone.sh`
    - `python run_capstone.py --serve`
  - Explains the participant implementation contract: provide documented setup, run, test, evaluate, reset and evidence-export commands under `submission/scripts/`.

Plain-language understanding:

> The root `runbooks/` folder tells participants how to work through the capstone and how to execute repository checks. It is guidance for the challenge process, not the final operational runbooks for the system being built.

How it differs from `submission/runbooks/`:

| Folder | Purpose |
|---|---|
| `runbooks/` | Provided capstone guidance and repo execution instructions |
| `submission/runbooks/` | Participant-created solution runbooks for setup, operation, evaluation, incident response, AI-disabled continuity, deployment and retirement |

How it should be used during discovery and specs:

- Use `PARTICIPANT_RUNBOOK.md` to structure the project phases.
- Use `REPO_EXECUTION.md` to understand required repo checks and clean-room proof expectations.
- Reflect the phase logic in discovery and planning artefacts.
- Reflect execution requirements in reproducibility, operations and final defence specs.
- Do not treat the root runbooks as final solution runbooks.
- Create solution-specific runbooks under `submission/runbooks/`.

Discovery implication:

> The root `runbooks/` folder defines the working method for the capstone. It should influence the project plan and specs, while `submission/runbooks/` should document how the built system is actually installed, run, tested, evaluated, recovered and defended.

## What the `templates/` folder is used for

The `templates/` folder contains blank scaffold documents for the required participant artefacts. These templates help structure the final submission, but they are not completed answers.

The templates cover the major artefact areas expected in the capstone, including:

- business case,
- DMAIC workbook,
- stakeholder decision rights,
- product and service blueprint,
- DDD context map,
- data governance and integrity,
- ontology and semantic layer,
- knowledge graph decision,
- requirements traceability,
- C4 architecture,
- ADR register,
- integration contracts,
- GxP lifecycle validation,
- computer software assurance,
- quality risk management,
- threat and abuse model,
- privacy and ethics,
- responsible AI and human factors,
- EU AI Act applicability,
- ISO/IEC 42001 governance,
- assurance case,
- evaluation scorecard,
- token and FinOps model,
- reliability and observability,
- incident recovery,
- target operating model,
- vendor exit and retirement,
- production readiness,
- 90-day roadmap and handover,
- elevator pitch.

Plain-language understanding:

> `templates/` gives the blank forms and expected structure for the work. The actual completed artefacts should be written under `submission/artefacts/`.

Important boundary:

- The templates are scaffolds, not solution content.
- Do not treat a template heading as evidence that a requirement has been satisfied.
- Do not modify the original templates unless intentionally changing the challenge package.
- Copy, adapt or map their structure into participant-owned files under `submission/artefacts/`.

How it differs from nearby folders:

| Folder | Purpose |
|---|---|
| `templates/` | Blank scaffolds for required artefacts |
| `requirements/` | Defines what artefacts and evidence are mandatory |
| `submission/artefacts/` | Where completed participant artefacts should be created |

How it should be used during discovery and specs:

- Use templates to understand expected sections and evidence prompts.
- Use them to avoid missing required artefact topics.
- Map template content to the formal artefact register and scoring model.
- Complete the actual artefacts in `submission/artefacts/`, not in the root `templates/` folder.

Discovery implication:

> The `templates/` folder is the starting structure for documentation. The participant still needs to fill the substance with case evidence, source citations, assumptions, decisions, tests, controls and residual risks.

## Regulatory requirements understanding for system specs

This system should be specified as a **regulated decision-support and evidence-reconciliation system**, not as an autonomous regulated decision-maker.

The regulatory requirements are mainly about proving that the system is:

- advisory,
- controlled,
- validated,
- auditable,
- secure,
- privacy-aware,
- fail-closed,
- accountable to human decision-makers.

### 1. Intended use and regulatory boundary

The specification must clearly define:

- intended use,
- prohibited use,
- supported workflows,
- affected decisions,
- regulated-record boundary,
- advisory versus determinative role,
- accountable human role,
- evidence the human reviewer must inspect.

For this capstone, the intended use should be framed as:

> Advisory evidence reconciliation and review support for batch, pharmacovigilance and supply workflows.

The prohibited-use boundary should state:

> The system must not release product, reject product, close investigations, decide PV reportability, confirm safety signals, allocate stock, ship product, initiate recall or make clinical eligibility decisions.

### 2. GxP computerized-system controls

Because the system supports Quality, Safety, Clinical and Supply decisions, the specification should include GxP-style computerized-system controls:

- documented requirements,
- risk-based validation strategy,
- test evidence,
- change control,
- access control,
- audit trails,
- backup and restore,
- incident handling,
- controlled operation,
- data-integrity controls,
- supplier or model lifecycle controls where applicable.

Relevant reference anchors from the case include:

- FDA 21 CFR Part 11 for electronic records and signatures,
- FDA Computer Software Assurance concepts,
- EU GMP Annex 11 for computerized systems,
- EU GMP Annex 15 for qualification and validation,
- ICH Q9(R1) Quality Risk Management,
- ICH Q10 Pharmaceutical Quality System.

### 3. Electronic records and audit trail

If the system creates, modifies, retrieves, transmits, stores or exports regulated evidence, the specification must require:

- source record preservation,
- user identity,
- timestamp,
- source path or system,
- document version,
- evidence hash where available,
- transformation history,
- review status,
- human reviewer state,
- exportable audit evidence.

The system must not overwrite original evidence. Any derived interpretation must be separate from the source record.

### 4. Data integrity requirements

The system should follow ALCOA+ style data-integrity expectations:

- attributable,
- legible,
- contemporaneous,
- original,
- accurate,
- complete,
- consistent,
- enduring,
- available.

In this case, that means the specifications must require:

- no silent unit conversion,
- no irreversible merge of safety cases,
- no hidden changes to source evidence,
- no use of untrusted documents as authority,
- no unsupported final conclusions,
- no missing provenance for generated outputs.

### 5. Human oversight and decision rights

The specification must require human review before any regulated decision.

The system can support:

- evidence finding,
- evidence reconciliation,
- contradiction detection,
- gap identification,
- risk explanation,
- review packet preparation,
- audit and defence evidence export.

The system must not perform final decisions or execute regulated actions.

For batch review, it must not:

- release a batch,
- reject a batch,
- reprocess a batch,
- relabel a batch,
- recall a batch,
- override a quality hold,
- determine OOS invalidity.

For pharmacovigilance, it must not:

- make final seriousness decisions,
- make final causality decisions,
- make final expectedness decisions,
- make final reportability decisions,
- confirm a safety signal,
- automatically submit to an authority.

For supply, it must not:

- allocate stock,
- reserve capacity,
- change quality status,
- ship product,
- initiate recall.

For clinical workflows, it must not:

- make final participant eligibility decisions,
- make endpoint adjudication decisions,
- replace investigator or medical accountability.

### 6. Pharmacovigilance-specific requirements

For PV support, the specification should require the system to preserve:

- verbatim source information,
- source and receipt evidence,
- awareness dates,
- reporting-clock evidence,
- duplicate uncertainty,
- terminology version,
- listedness context,
- product-quality linkage,
- qualified medical review requirement.

Automated irreversible merging, final case assessment or automatic authority submission must be outside scope.

### 7. Clinical-development requirements

For clinical or protocol-related support, the specification should require:

- protocol version tracking,
- site-level applicability checks,
- consent and withdrawal handling,
- source evidence preservation,
- blinding protection where relevant,
- auditability of data corrections,
- accountable medical or investigator decision-making.

Global protocol currency alone must not be treated as proof of local site applicability.

### 8. Privacy and cross-border requirements

The specification should require a privacy-by-design assessment covering:

- purpose limitation,
- lawful basis or permission assumptions,
- data categories,
- minimization,
- retention,
- access control,
- pseudonymization,
- re-identification risk,
- consent and withdrawal propagation,
- secondary-use boundary,
- residency and transfer controls.

Deletion requests may require restriction, segregation or retention rather than simple deletion where legal, trial-integrity or GxP obligations apply.

### 9. AI governance and security requirements

The specification should require:

- intended-use statement,
- prohibited-use statement,
- accountable owner,
- model and non-model baseline,
- model-selection evidence,
- evaluation thresholds,
- prompt/document isolation,
- prompt-injection defenses,
- tool-use restrictions,
- signed or approved tools,
- least privilege,
- segregation of duties,
- continuous authorization checks,
- budget and stop conditions,
- idempotent tool behavior,
- fail-closed execution,
- kill switch,
- model outage behavior,
- AI-disabled continuity.

Security controls must cover prompt injection, document poisoning, exfiltration, tool abuse, excessive agency, replay, supply-chain risk and denial-of-wallet.

### 10. Validation, testing and evidence requirements

The specification should require evidence for:

- requirements traceability,
- contract tests,
- deterministic tests,
- adversarial tests,
- outage and recovery tests,
- prohibited-action tests,
- authority and effective-date tests,
- privacy tests,
- audit-trail tests,
- regression tests against public fixtures,
- evaluation thresholds and failed-gate behavior.

For the capstone submission, this maps to artefacts such as:

- intended-purpose and regulatory-applicability analysis,
- GxP lifecycle and validation strategy,
- data-integrity and audit-trail assessment,
- quality-risk and safety assurance case,
- AI governance analysis,
- threat and abuse model,
- privacy-by-design assessment,
- TEVV and evaluation strategy,
- final defence evidence.

### Simple specification principle

Use this principle when writing requirements:

> The system may help humans find, reconcile, explain and defend evidence, but it must preserve source truth, cite authority, fail closed on uncertainty and leave regulated decisions with accountable humans.

## Inject catalogue understanding

The inject catalogue is the full library of challenge problems in the case.

It tells the team:

- what can go wrong,
- which workflow is affected,
- where supporting evidence appears,
- which risks the solution must handle.

Examples of inject types include:

- batch genealogy break,
- unit conversion defect,
- OOS/OOT disagreement,
- supplier evidence gap,
- duplicate PV safety cases,
- cold-chain excursion,
- prompt injection,
- model outage,
- privacy conflict,
- provenance break.

Simple relationship:

```text
Inject Catalogue = full problem library
Public Fixtures = selected packaged test cases from that problem library
```

## Public fixture understanding

A public fixture is a ready-made test scenario. It packages a prompt, context, evidence references, embedded records and source hashes so the system can be tested consistently.

For example, `PUB-01.json` is a batch-review readiness scenario for batch `NCB204-B24071`.

It focuses on:

- unit mismatch,
- genealogy issues,
- OOS/OOT disagreement,
- supplier commitment evidence,
- provenance.

The expected behavior is not to decide whether the batch is good or bad. The expected behavior is to identify evidence conflicts and gaps, cite sources, require human review and avoid prohibited actions.

## Key batch-review concepts discussed

### Material genealogy missing branch

If `material_genealogy.csv` says material lot `SUA-88` is a `missing_branch` in MES, it means the manufacturing system does not have a complete recorded genealogy link for that material lot.

Plain-language meaning:

> The warehouse may show the material was issued or used, but the manufacturing genealogy record is incomplete. Quality must investigate before relying on the batch evidence.

### Unit conversion issue

The statement:

> Potency result may be affected by an unapproved unit conversion assumption between `mg/L` and `ug/mL`.

means the result and specification may use equivalent units mathematically, but the interface rule or conversion assumption is not formally approved in the case evidence.

Plain-language meaning:

> The result may be correct, but the system used an unapproved conversion rule, so Quality must verify it before trusting the result.

### Laboratory status conflict

The statement:

> The laboratory result has unresolved status conflict. LIMS, statistical tooling, and notebook evidence disagree, and the investigation remains open.

means different evidence sources give different interpretations:

- LIMS may say OOS, out of specification.
- Statistical tooling may say OOT, out of trend.
- Notebook evidence may say sample preparation was invalid.
- The formal investigation may still be open.

Plain-language meaning:

> The lab result cannot be treated as final because the systems disagree and Quality has not closed the investigation.

### Release packet gap

A release packet is the set of documents Quality needs before a batch can be reviewed for release.

A release packet gap means one required document or evidence item is missing, incomplete or not independently verified.

Example:

> Supplier commitment evidence is missing or not independently verified.

This means the supplier may claim an issue is fixed, but NovaCura does not yet have sufficient independent evidence to rely on that claim.

### Supplier vs NovaCura

NovaCura is the fictional pharma company responsible for the product and regulated decision-making.

A supplier is an external company that provides materials, components, services or manufacturing support to NovaCura.

Short version:

> A supplier provides goods or services. NovaCura remains accountable for quality and regulated decisions.

### Medicine batch release

When a medicine batch is released, it means an authorized Quality role has approved the batch to move forward for use, shipment, distribution or another allowed step.

It does not mean the medicine is physically released from a machine. It usually means the batch status changes from something like `quality_hold` or `pending_review` to `released`.

Release may be recorded in systems such as:

- MES,
- ERP,
- electronic batch record,
- QMS,
- release packet or batch disposition system.

The AI system must not release the batch. It can only help prepare evidence for the human Quality reviewer.

## Where AI should be used

AI should be used in evidence-support stages before a regulated decision.

Appropriate AI support stages:

1. **Evidence finding**
   - Find relevant batch, PV or supply evidence across source files.

2. **Evidence reconciliation**
   - Compare records and identify agreements, contradictions and gaps.

3. **Evidence explanation**
   - Explain issues in plain language for human reviewers.

4. **Evidence packaging**
   - Prepare structured review packets with source citations, gaps, conflicts and abstentions.

5. **Risk triage**
   - Prioritize which issues need human attention first.

6. **Draft recommendation support**
   - Draft advisory statements such as "human Quality review required".

7. **Audit and defence support**
   - Record sources, timestamps, policies, assumptions and reasoning so the result can be defended later.

## Where AI must not be used

AI must not make or execute final regulated decisions.

For batch review, AI must not:

- release a batch,
- reject a batch,
- recall a batch,
- reprocess a batch,
- relabel a batch,
- override a quality hold.

For pharmacovigilance, AI must not:

- make final seriousness decisions,
- make final causality decisions,
- make final expectedness decisions,
- make final reportability decisions,
- confirm a safety signal.

For supply, AI must not:

- allocate stock,
- reserve capacity,
- change inventory quality status,
- ship product,
- initiate recall.

## Example system behavior for `PUB-01`

If the user asks:

> Assess evidence readiness for batch `NCB204-B24071`.

The system should:

1. Load relevant fixture and source evidence.
2. Identify the batch and evidence sources.
3. Detect unit conversion concerns.
4. Detect genealogy gaps.
5. Detect lab status conflicts.
6. Detect open investigations.
7. Detect release packet and supplier evidence gaps.
8. Cite every evidence source.
9. Mark the review as advisory.
10. Require human Quality review.
11. State that no batch release, rejection or recall decision has been made.

Expected summary style:

> Evidence is not ready for automated clearance. Multiple records conflict or are incomplete. Human Quality review is required. This is not a batch disposition decision.

## Discovery implications

For discovery and SCQA work, the key framing is:

- The problem is evidence fragmentation, not just document search.
- AI value comes from faster evidence preparation and clearer conflict detection.
- The intervention must be narrower than the business problem.
- Human accountability is non-negotiable.
- Provenance, source authority and effective date are central.
- Abstention is a required safe behavior, not a failure.
- Public fixtures are the best starting point for deterministic tests.
- The inject catalogue should drive requirements, tests, controls and traceability.

## Suggested use of this note

Use this note as source material for:

- discovery problem statement,
- SCQA,
- stakeholder briefing,
- PRD introduction,
- DDD ubiquitous language,
- evidence mapping,
- safety boundary definition,
- evaluation narrative,
- final defence preparation.

Do not use this file as an implementation task list. The Cursor-ready task file remains separate.
