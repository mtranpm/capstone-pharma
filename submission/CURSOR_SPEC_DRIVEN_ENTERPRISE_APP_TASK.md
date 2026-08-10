# Cursor Task File — Project AEGIS-PHARMA Enterprise Application

## Purpose

Use this file as the master Cursor task prompt for building an enterprise-grade, spec-driven application for the Project AEGIS-PHARMA capstone.

The application must help humans **find, reconcile, explain and defend evidence faster** across the three mandatory NovaCura workflows while staying inside strict GxP, safety, privacy, security and human-accountability boundaries.

All generated implementation, artefacts, tests, runbooks and evidence must stay under `submission/`. Do not modify original challenge evidence.

---

## 0. Cursor operating instructions

When using Cursor, work in phases. Do not jump directly into coding.

### Mandatory repo boundaries

- Start from `submission/artefacts/00_case_discovery_understanding.md` for business context and repository interpretation.
- Challenge evidence lives in `case/`, `data/`, `knowledge/`, `source_documents/`, `sources/`, `evaluation/`, `requirements/`, `runbooks/`, `templates/`, `prompts/`, `starter/` and `app/`.
- Participant work must live under `submission/`.
- Do not modify original challenge evidence unless explicitly instructed.
- The app must be offline-capable and deterministic for tests.
- The AI system must never execute regulated actions.
- Every workflow must produce structured, contract-valid, auditable outputs.

### Initial Cursor instruction

Paste this into Cursor:

```text
Use submission/CURSOR_SPEC_DRIVEN_ENTERPRISE_APP_TASK.md as the master delivery plan.
Use submission/artefacts/00_case_discovery_understanding.md as the business-discovery and repository-understanding source.
Follow the phases in order.
Begin with business discovery: case context, affected decisions, evidence fragmentation, human accountability, regulatory boundaries, prohibited actions and final defence expectations.
Only after business discovery is clear, convert it into SCQA, PRD, DDD, ADRs, architecture, test plan and development specs under submission/artefacts/.
All code must be under submission/src/, submission/app/, submission/tests/, submission/scripts/.
Do not modify challenge evidence outside submission/.
The system must be advisory only and must fail closed on missing authority, stale evidence, policy conflict, untrusted content or prohibited action.
```

---

## 1. Mission statement

Build a defensible enterprise evidence-orchestration application for fictional NovaCura Therapeutics Group.

The application must support:

1. **Batch-review evidence reconciliation**
   - Finds batch evidence, genealogy, lab results, deviations, CAPA, validation state, supplier evidence and release packet gaps.
   - Must not release, reject, reprocess, relabel or recall a batch.

2. **Pharmacovigilance case intake and signal support**
   - Supports intake, duplicate detection, terminology normalization, reporting-clock reconstruction, listedness evidence and multilingual review.
   - Must not make final seriousness, causality, expectedness, reportability or signal-confirmation decisions.

3. **Supply-shortage and cold-chain recovery planning**
   - Generates traceable non-executing options using inventory, quality status, market authorization, demand, cold-chain evidence, CMO capacity and allocation policy.
   - Must not allocate stock, reserve capacity, change inventory status, ship product, release product or initiate recall.

---

## 2. Enterprise problem statement

NovaCura has fragmented evidence across manufacturing, quality, safety, regulatory, clinical and supply systems. The organisation must respond to concurrent batch, safety, cold-chain, shortage, cyber and inspection pressures. Evidence is inconsistent across identifiers, timestamps, units, terminology, authority, access control and effective dates.

The application must reduce evidence-reconciliation effort while preserving:

- human accountability,
- GxP data integrity,
- auditability,
- source authority,
- temporal applicability,
- safety boundaries,
- privacy boundaries,
- security controls,
- offline continuity.

Short problem statement:

> NovaCura needs an advisory evidence-orchestration system that accelerates regulated evidence review across batch, PV and supply workflows without making or executing regulated decisions.

---

## 3. Phase plan

### Discovery source and business-first ordering

Cursor must use `submission/artefacts/00_case_discovery_understanding.md` as the first orientation file. That file separates:

- **business-relevant sections to use first**, for understanding NovaCura, workflows, evidence, stakeholders, regulatory boundaries, evaluation expectations and deliverables;
- **technical/specification sections to use later**, for converting the business understanding into contracts, tests, architecture, implementation controls, runbooks and evidence.

Do not begin with model choice, agent design, UI design, knowledge graph design or tool automation. First establish:

- measurable business problem,
- affected decisions,
- accountable human roles,
- fragmented or conflicting evidence,
- allowed AI support,
- prohibited AI behavior,
- regulatory and safety boundary,
- evidence a human reviewer must inspect,
- final defence obligations.

Business-first framing:

> NovaCura needs faster, safer evidence reconciliation across regulated workflows. The system must help humans understand and defend evidence, not replace accountable regulated decisions.

Technical/specification principle:

> Business discovery explains what problem must be solved and what boundaries must hold. Technical specs explain how the solution will prove those boundaries through contracts, tests, controls, evidence and reproducible execution.

### Formal artefact register from `requirements/ARTEFACT_EXPECTATIONS.md`

Cursor must create or maintain the following artefacts under `submission/artefacts/`. These are not optional documentation extras. They are required evidence for scoring and final defence.

| Requirement area | Required artefact file |
|---|---|
| Problem statement, baseline, KPI tree, value hypothesis | `01_discovery_problem_baseline_value.md` |
| No-AI, rules, analytics, workflow redesign, buy/build/partner comparison | `02_no_ai_and_solution_options.md` |
| Stakeholder map, incentives, decision rights, conflicts, escalation | `03_stakeholders_decision_rights.md` |
| DMAIC, benefits-realisation plan, stop/pivot criteria | `04_dmaic_benefits_stop_pivot.md` |
| Personas, JTBD, service blueprint, intended/prohibited use | `05_product_operating_model.md` |
| Human oversight, review, override, contestability, emergency stop | `06_human_oversight_and_emergency_stop.md` |
| Adoption, training, accessibility, multilingual, change management | `07_adoption_accessibility_change.md` |
| DDD bounded contexts and context map | `08_ddd_context_map.md` |
| Data inventory, contracts, quality, lineage, provenance, retention, residency, stewardship | `09_data_governance_lineage_contracts.md` |
| Pharmaceutical ontology and semantic layer | `10_ontology_semantic_layer.md` |
| Knowledge graph decision and simpler alternative benchmark | `11_knowledge_graph_decision.md` |
| Document authority, effective-date, supersession, conflict-resolution model | `12_document_authority_model.md` |
| Traceable functional, non-functional, GxP, safety, privacy, security requirements | `13_requirements_traceability_matrix.md` |
| C4 architecture, integration contracts, event semantics, minimum 10 ADRs | `14_architecture_c4_adrs.md` |
| Brownfield modernization, migration, coexistence, cutover, rollback, decommissioning | `15_brownfield_modernization_plan.md` |
| Reproducible offline execution, locked dependencies, reset, seeded data, evidence export | `16_reproducibility_and_offline_execution.md` |
| Cursor engineering evidence, rules, skills, agents, commands, prompts, review controls | `17_cursor_engineering_evidence.md` |
| Model and non-model baselines, model selection, substitution strategy | `18_model_baseline_selection_substitution.md` |
| Prompt, retrieval, schema, tool, state, memory, context-boundary design | `19_ai_context_and_tool_design.md` |
| Budgets, stop conditions, checkpointing, idempotency, bounded human-approved tools | `20_agent_budget_stop_checkpointing.md` |
| Deterministic test mode, safe degradation, kill switch, AI-disabled continuity | `21_degraded_mode_kill_switch_continuity.md` |
| Intended purpose and regulatory applicability | `22_intended_use_regulatory_applicability.md` |
| Computerised-system lifecycle and validation/assurance strategy | `23_gxp_lifecycle_validation_strategy.md` |
| Data integrity, electronic records/signatures, audit-trail controls | `24_data_integrity_records_audit_trail.md` |
| Quality risk management and clinical/safety assurance case | `25_quality_risk_and_safety_assurance.md` |
| EU AI Act and ISO/IEC 42001-aligned governance | `26_ai_governance_analysis.md` |
| Claims-arguments-evidence assurance case, invalidation conditions, residual risk | `27_assurance_case_residual_risk.md` |
| Threat and abuse model | `28_threat_abuse_model.md` |
| Zero Trust authorization, signed tools, least privilege, segregation of duties | `29_zero_trust_tool_governance.md` |
| Privacy-by-design, consent, secondary use, pseudonymisation, re-identification, cross-border | `30_privacy_by_design_assessment.md` |
| Red-team evidence, remediation verification, residual-risk acceptance | `31_red_team_and_remediation.md` |
| TEVV plan, datasets, graders, thresholds, subgroup analysis, regression gates | `32_tevv_evaluation_strategy.md` |
| Token efficiency, context budgets, caching, avoided inference, token economics | `33_token_efficiency_economics.md` |
| Full AI FinOps including human review, validation, security, observability, exit cost | `34_ai_finops_model.md` |
| SLI/SLO, error budget, observability, incident response, backup, restore, DR | `35_operations_slo_incident_dr.md` |
| Vendor exit, model replacement, data portability, retirement, evidence preservation | `36_vendor_exit_retirement.md` |
| Production-readiness gaps, 90-day roadmap, handover pack, final defence | `37_production_readiness_roadmap_defence.md` |

### Mandatory machine-readable submission evidence

Cursor must also create these files under `submission/evidence/` as required by `requirements/SUBMISSION_EVIDENCE_STANDARD.md`:

| Evidence file | Required content |
|---|---|
| `submission/evidence/submission_manifest.csv` | Columns: `path,owner,version,status,sha256` |
| `submission/evidence/file_hashes.csv` | Final hash list generated from the submission state |
| `submission/evidence/test_results.json` | Suite, test ID, requirement/control IDs, result, timestamp, runtime mode, evidence path |
| `submission/evidence/evaluation_results.json` | Dataset/cohort, grader, threshold, observed result, gate result, evidence path |

Evidence quality rules:

- Use relative paths and stable IDs.
- Preserve original evidence and record transformations.
- Separate facts, interpretations, assumptions, decisions and residual risk.
- Record software, model, prompt, corpus, schema, tool and evaluator versions.
- Do not include credentials, live personal data, proprietary records or unverifiable screenshots as sole evidence.

### Minimum runbook register

Cursor must create these under `submission/runbooks/`:

| Runbook | Purpose |
|---|---|
| `SETUP.md` | Prerequisites, install/setup, expected outputs, failure handling |
| `RUN.md` | How to run CLI/UI workflows |
| `EVALUATE.md` | How to run public fixture evaluation and interpret gates |
| `RESET_ROLLBACK.md` | Reset, rollback and clean rerun instructions |
| `INCIDENT_RESPONSE.md` | Security, GxP, safety and operational incident handling |
| `AI_DISABLED_CONTINUITY.md` | Manual operation for 14 days without model inference |
| `DEPLOYMENT.md` | Local/offline deployment and optional container/static deployment |
| `RETIREMENT_AND_VENDOR_EXIT.md` | Vendor exit, model substitution, evidence preservation and retirement |

Every command in a runbook must state prerequisites, inputs, expected outputs, failure handling and reset/rollback.

### Final defence artefact requirements

Cursor must prepare `submission/artefacts/37_production_readiness_roadmap_defence.md` and supporting demo evidence for:

1. 60-second elevator pitch and five-minute executive case.
2. Current-state baseline, no-AI comparison and measurable value case.
3. Live demo of batch, PV and supply workflows.
4. Prohibited-action test proving regulated boundaries cannot be crossed.
5. Malicious-document and poisoned-tool challenge.
6. Unit, terminology, temporal and product-identity conflict handling.
7. Model outage, fallback limitation and AI-disabled manual operation.
8. Evaluation evidence, subgroup weaknesses and failed-gate behavior.
9. Token and total-cost defence including human review.
10. Architecture, DDD, ontology, semantic layer, KG decision and ADR defence.
11. Inspection-style evidence request linking claims to immutable artefacts.
12. Vendor exit, model substitution and retirement demonstration.
13. Board recommendation: go, conditional go, pivot, pause or stop.

### Scoring and hard gates

The implementation must optimize for the 180-point scoring model in `requirements/SCORING_MODEL.md`, but hard gates override numeric score.

The submission cannot pass unconditionally if it:

- allows AI to release/reject a batch, make final PV decisions, allocate stock or initiate recall autonomously,
- fails to preserve evidence provenance, authority, effective date and auditability,
- silently converts units or merges safety cases irreversibly,
- uses revoked entitlements, unsigned tools or untrusted documents as instructions,
- lacks safe manual operation during model outage,
- cannot reproduce build, tests and evaluation from the supplied package,
- omits material subgroup, privacy, data-integrity or GxP risks.

### Phase 1 — Discovery and evidence mapping

Create:

- `submission/artefacts/01_discovery_problem_baseline_value.md`
- `submission/artefacts/02_no_ai_and_solution_options.md`
- `submission/artefacts/03_stakeholders_decision_rights.md`
- `submission/artefacts/04_dmaic_benefits_stop_pivot.md`
- `submission/artefacts/09_data_governance_lineage_contracts.md`
- `submission/artefacts/13_requirements_traceability_matrix.md`

Tasks:

1. Read and summarize:
   - `submission/artefacts/00_case_discovery_understanding.md`
   - `START_HERE.md`
   - `PACKAGE_SCOPE_AND_ASSUMPTIONS.md`
   - `case/INTEGRATED_CASE.md`
   - `case/REGULATORY_BOUNDARY_PACK.md`
   - `case/SOURCE_SYSTEM_FACT_PACK.md`
   - `case/STAKEHOLDER_PACK.md`
   - `data/DATASET_PROFILE.csv`
   - `data/DATA_DICTIONARY.csv`
   - `data/inject_evidence_map.csv`
   - `data/RELATIONSHIP_MODEL.csv`
   - `data/knowledge_catalog.csv`
   - `source_documents/`
   - `sources/LOCAL_REGULATORY_AND_STANDARDS_GUIDE.md`
   - `sources/REFERENCE_SOURCES.md`
   - `evaluation/EVALUATION_PLAN.md`
   - `evaluation/PUBLIC_FIXTURE_INDEX.csv`
   - `requirements/ARTEFACT_EXPECTATIONS.md`
   - `requirements/SUBMISSION_EVIDENCE_STANDARD.md`
   - `requirements/FINAL_DEFENCE.md`
   - `requirements/SCORING_MODEL.md`
   - `runbooks/PARTICIPANT_RUNBOOK.md`
   - `runbooks/REPO_EXECUTION.md`
   - `prompts/PROMPT_LIBRARY.md`
   - `DEFINITION_OF_DONE.md`
2. Create a business-first repository map:
   - `case/` for business scenario, stakeholders, source-system facts and regulatory boundary.
   - `data/` for synthetic operational evidence records.
   - `knowledge/` for case-specific policy, authority and abstention rules.
   - `source_documents/` for document-level evidence extracts.
   - `sources/` for regulatory and standards framing.
   - `evaluation/public_fixtures/` for business test scenarios.
   - `requirements/` for business-grade completion expectations.
   - `templates/` for blank artefact scaffolds.
   - `submission/` for participant-owned outputs.
3. Build an inject-to-workflow traceability matrix.
4. Map data files to each mandatory workflow.
5. Map source documents to the records, versions, commitments or authority correspondence they explain.
6. Map knowledge files to policies, controls and authority checks.
7. Identify no-AI alternatives, rules-based alternatives and workflow redesign options.
8. Define stop, pivot and no-go criteria.
9. Document which technical/specification inputs will be used later:
   - `evaluation/contracts/`
   - `evaluation/contract_samples/`
   - `app/`
   - `starter/`
   - `tools/`
   - `.cursor/`
   - `submission/scripts/`
   - `submission/tests/`
   - `submission/evidence/`
   - `submission/runbooks/`

Acceptance criteria:

- Every mandatory workflow links to case injects, data sources, knowledge documents and evaluation fixtures.
- Business discovery clearly separates business context from technical/specification implementation inputs.
- Source documents are treated as supporting evidence extracts, not automatic authorization.
- Regulatory sources are treated as framing anchors, not legal conclusions.
- At least one no-AI alternative is compared honestly.
- Prohibited actions are listed explicitly.

---

### Phase 2 — SCQA and executive framing

Create:

- Include SCQA inside `submission/artefacts/01_discovery_problem_baseline_value.md`
- Include value hypothesis inside `submission/artefacts/01_discovery_problem_baseline_value.md`
- Include executive case inside `submission/artefacts/37_production_readiness_roadmap_defence.md`

SCQA:

- **Situation:** NovaCura needs faster evidence reconciliation across regulated quality, safety and supply operations.
- **Complication:** Evidence is fragmented, contradictory, mixed-authority, time-sensitive and affected by GxP, safety, privacy and security constraints.
- **Question:** How can NovaCura use AI to accelerate evidence work without replacing accountable regulated human decisions?
- **Answer:** Build an advisory, fail-closed, offline-capable evidence orchestration system with provenance, authority checks, structured outputs, abstention and human review.

Acceptance criteria:

- SCQA is concise enough for executive presentation.
- Value hypothesis includes cycle-time, quality, safety, review-burden and cost assumptions.
- The selected intervention is narrower than the business problem.

---

### Phase 3 — PRD

Create:

- `submission/artefacts/05_product_operating_model.md`
- `submission/artefacts/06_human_oversight_and_emergency_stop.md`
- `submission/artefacts/07_adoption_accessibility_change.md`

PRD sections:

1. Product name: **AEGIS Evidence Orchestrator**
2. Personas:
   - Quality reviewer / Qualified Person
   - Pharmacovigilance safety associate
   - Supply planner
   - Regulatory / inspection response lead
   - QA validation lead
   - Security and privacy reviewer
3. Jobs to be done:
   - Find relevant evidence.
   - Reconcile contradictions.
   - Explain gaps and risks.
   - Prepare human-review packet.
   - Export audit and defence evidence.
4. In scope:
   - Batch evidence readiness.
   - PV case intake support.
   - Supply recovery option support.
   - Evidence citation.
   - Policy authority checks.
   - Contract-valid outputs.
   - Offline deterministic evaluation.
5. Out of scope:
   - Batch disposition.
   - Final safety decisions.
   - Stock allocation or shipment execution.
   - Recall initiation.
   - Live production integration.
6. Functional requirements:
   - Load public fixture or source data.
   - Load relevant `source_documents/` extracts when records reference protocols, contracts, labels, audit commitments, logger notes or authority correspondence.
   - Validate authorization context.
   - Retrieve applicable knowledge documents.
   - Check document status, effective date and authority.
   - Use `sources/` only for regulatory framing and applicability analysis, not as automatic legal conclusions.
   - Detect contradictions and gaps.
   - Produce schema-valid response.
   - Require human review.
   - Export audit evidence.
7. Non-functional requirements:
   - Offline capable.
   - Deterministic tests.
   - Fail-closed behavior.
   - Least privilege.
   - No secret dependency.
   - Repeatable setup and reset.
   - Accessible UI.
   - Evidence hash preservation.

Acceptance criteria:

- PRD traces each requirement to case evidence, knowledge controls and tests.
- PRD distinguishes advisory support from regulated decision-making.

---

### Phase 4 — Domain-driven design

Create:

- `submission/artefacts/08_ddd_context_map.md`
- `submission/artefacts/09_data_governance_lineage_contracts.md`
- `submission/artefacts/10_ontology_semantic_layer.md`
- `submission/artefacts/11_knowledge_graph_decision.md`
- `submission/artefacts/12_document_authority_model.md`

Bounded contexts:

1. Evidence Intake
2. Authority and Policy Management
3. Source Document Interpretation
4. Regulatory and Standards Framing
5. Batch Evidence Readiness
6. Pharmacovigilance Intake Support
7. Supply Recovery Planning
8. Human Review and Decision Rights
9. Audit and Evidence Export
10. Security, Authorization and Tool Governance
11. Evaluation and Test Harness

Core entities:

- `EvidenceItem`
- `EvidenceSource`
- `KnowledgeDocument`
- `DocumentAuthority`
- `SourceDocumentExtract`
- `RegulatoryReference`
- `PolicyStatus`
- `AsOfContext`
- `Contradiction`
- `Gap`
- `Abstention`
- `HumanReview`
- `AuditEvent`
- `WorkflowRun`
- `ReadinessState`
- `ProhibitedAction`
- `EvaluationFixture`

Key domain rules:

- Approved and applicable policy can be used as authority.
- Superseded policy can be cited only for historical traceability.
- Untrusted policy can be preserved as adversarial evidence but not followed.
- Missing authority causes abstention.
- Prohibited action attempts fail closed.
- Human review is mandatory before any regulated decision.

Acceptance criteria:

- Domain model covers the three mandatory workflows.
- Context map shows system boundaries and anti-corruption layers for source data.

---

### Phase 5 — Architecture and ADRs

Create:

- `submission/artefacts/13_requirements_traceability_matrix.md`
- `submission/artefacts/14_architecture_c4_adrs.md`
- `submission/artefacts/15_brownfield_modernization_plan.md`
- `submission/artefacts/16_reproducibility_and_offline_execution.md`

Recommended architecture:

```text
Browser/UI
  -> Workflow API / CLI
    -> Authorization Context Validator
    -> Fixture/Data Loader
    -> Evidence Normalizer
    -> Knowledge Authority Checker
    -> Workflow Reasoners
       - Batch Reasoner
       - PV Reasoner
       - Supply Reasoner
    -> Contract Validator
    -> Audit/Evidence Exporter
```

Implementation recommendation:

- Use Python standard library first for deterministic offline mode.
- Optional lightweight web UI can be static HTML/JS under `submission/app/`.
- Use JSON schema contracts from `evaluation/contracts/`.
- Keep source challenge data read-only.
- Store generated run outputs under `submission/evidence/`.

Minimum ADRs:

1. Advisory-only AI with no regulated execution.
2. All participant work under `submission/`.
3. Offline deterministic-first architecture.
4. Schema-constrained workflow outputs.
5. Authority checking before using knowledge documents.
6. Fail-closed abstention on conflicts or missing authority.
7. Human review required for regulated decisions.
8. No write-enabled tools for batch, PV or supply actions.
9. Public fixtures as acceptance-test inputs.
10. Evidence hashes and provenance preserved.
11. Rules/deterministic baseline before LLM usage.
12. AI-disabled continuity and manual fallback.
13. Signed/approved tool manifest design for future production.
14. Vendor/model substitution through change control.
15. Audit and evidence retention by design.

Acceptance criteria:

- Architecture traces to PRD and DDD.
- ADRs include context, decision, alternatives, consequences and tests.

---

### Phase 6 — Agent and Cursor working model

Create:

- `submission/artefacts/17_cursor_engineering_evidence.md`

Use these Cursor roles. If custom Cursor agents are unavailable, simulate them through task prompts.

1. **Product Strategist Agent**
   - Owns SCQA, PRD, value hypothesis, personas, acceptance criteria.

2. **Domain Architect Agent**
   - Owns DDD, context map, domain model, ubiquitous language.

3. **GxP/Safety Boundary Agent**
   - Owns intended use, prohibited use, human accountability, validation and assurance.

4. **Data/Evidence Lineage Agent**
   - Owns source inventory, evidence mapping, provenance, hash checks and traceability.

5. **Security/Privacy Agent**
   - Owns threat model, privacy model, zero trust, prompt injection, tool poisoning and exfiltration controls.

6. **Backend Engineer Agent**
   - Owns workflow engine, data loaders, reasoners, contract validation and audit export.

7. **Frontend/UX Agent**
   - Owns human-review UI, evidence packet display, accessibility and non-executing workflow screens.

8. **Test Engineer Agent**
   - Owns deterministic, adversarial, outage, regression, contract and prohibited-action tests.

9. **DevOps/Operations Agent**
   - Owns setup, run, evaluate, reset, evidence export, deployment, monitoring and AI-disabled continuity.

Recommended sequence:

```text
Product Strategist -> Domain Architect -> GxP/Safety -> Data Lineage -> Security/Privacy -> Backend -> Frontend -> Test -> DevOps
```

Acceptance criteria:

- Every task has a responsible role and review role.
- Security, GxP and tests review implementation before final acceptance.

---

### Phase 7 — Development specifications

Create:

- `submission/artefacts/16_reproducibility_and_offline_execution.md`
- `submission/artefacts/18_model_baseline_selection_substitution.md`
- `submission/artefacts/19_ai_context_and_tool_design.md`
- `submission/artefacts/20_agent_budget_stop_checkpointing.md`
- `submission/artefacts/21_degraded_mode_kill_switch_continuity.md`

Recommended structure:

```text
submission/
  app/
    index.html
    app.js
    styles.css
  src/
    aegis/
      __init__.py
      cli.py
      config.py
      data_loader.py
      fixture_loader.py
      authority.py
      contracts.py
      audit.py
      workflows/
        batch.py
        pv.py
        supply.py
      security/
        authorization.py
        prohibited_actions.py
      evaluation/
        runner.py
  tests/
    test_batch_pub01.py
    test_pv_public.py
    test_supply_public.py
    test_authority.py
    test_prohibited_actions.py
    test_contracts.py
    test_outage_manual_fallback.py
  scripts/
    run_app.py
    run_tests.py
    evaluate_public_fixtures.py
    export_evidence.py
    reset_submission.py
  evidence/
  artefacts/
  runbooks/
```

Workflow output requirements:

- Batch output must comply with `evaluation/contracts/batch_response.schema.json`.
- PV output must comply with `evaluation/contracts/pv_response.schema.json`.
- Supply output must comply with `evaluation/contracts/supply_response.schema.json`.
- Security, reliability, privacy, integration, agent, finops and clinical outputs may use participant-defined non-executing contracts.

Core services:

1. `FixtureLoader`
   - Loads `evaluation/public_fixtures/*.json`.
   - Preserves source path and SHA-256.

2. `DataLoader`
   - Reads CSV evidence under `data/` without modifying it.
   - Uses `DATA_DICTIONARY.csv`, `DATASET_PROFILE.csv`, `inject_evidence_map.csv` and `RELATIONSHIP_MODEL.csv` for field interpretation, integrity and traceability.

3. `SourceDocumentLoader`
   - Reads local extracts under `source_documents/`.
   - Links protocols, contracts, labels, audit commitments, logger notes and authority correspondence to related data records.
   - Preserves limitations such as local applicability, unresolved verification, timezone uncertainty or non-decision language.

4. `RegulatoryReferenceMapper`
   - Reads `sources/LOCAL_REGULATORY_AND_STANDARDS_GUIDE.md` and `sources/REFERENCE_SOURCES.md`.
   - Uses them only for regulatory framing, applicability questions and artefact prompts.
   - Does not treat reference links as current legal conclusions.

5. `AuthorityChecker`
   - Reads knowledge documents.
   - Extracts document ID, status, effective date and authority.
   - Marks approved, superseded, untrusted or not-applicable.

6. `WorkflowReasoner`
   - Produces evidence, contradictions, gaps, abstentions and human-review instructions.

7. `ContractValidator`
   - Validates output shape against evaluation contracts.

8. `ProhibitedActionGuard`
   - Blocks release, reject, recall, allocation, reportability and other regulated actions.

9. `AuditExporter`
   - Exports run metadata, sources, hashes, timestamps, decisions, abstentions and reviewer state.

Acceptance criteria:

- `PUB-01` produces `readiness_state = conflicted_evidence` or `insufficient_evidence`, never a disposition.
- All workflow runs set `execution_status = not_executed`.
- Every contradiction or gap cites source records.

---

### Phase 8 — Tests-first plan

Create:

- `submission/artefacts/32_tevv_evaluation_strategy.md`
- `submission/artefacts/31_red_team_and_remediation.md`

Test categories:

1. Contract tests
   - Validate response schemas.

2. Happy-path tests
   - Evidence found and summarized correctly.

3. Edge tests
   - Missing file, empty data, duplicate records, stale as-of date.

4. Adversarial tests
   - Untrusted document, prompt injection, poisoned tool manifest.

5. Prohibited-action tests
   - Attempt to release batch, allocate stock or make final PV decision must fail.

6. Authority tests
   - Approved, superseded, untrusted and unknown documents handled correctly.

7. Outage and continuity tests
   - AI-disabled mode produces manual-review packet.

8. Regression tests
   - Public fixtures PUB-01 to PUB-15 run consistently.

Acceptance commands:

```text
python tools/test_contracts.py
python submission/scripts/run_tests.py
python submission/scripts/evaluate_public_fixtures.py
python tools/check_submission_structure.py --final
```

---

### Phase 9 — UI / human review design

Create:

- `submission/artefacts/05_product_operating_model.md`
- `submission/artefacts/06_human_oversight_and_emergency_stop.md`
- `submission/artefacts/07_adoption_accessibility_change.md`

UI must show:

- workflow selected,
- fixture or case loaded,
- authorization status,
- evidence table,
- contradictions,
- gaps,
- abstentions,
- applicable knowledge documents,
- prohibited actions blocked,
- human reviewer required,
- export audit button.

UI must not include:

- release batch button,
- reject batch button,
- submit final PV reportability button,
- allocate stock button,
- initiate recall button.

Accessibility requirements:

- Keyboard navigation.
- No color-only warnings.
- Plain-language explanations.
- Evidence source links or references.

---

### Phase 10 — Deployment and operations

Create:

- `submission/runbooks/SETUP.md`
- `submission/runbooks/RUN.md`
- `submission/runbooks/EVALUATE.md`
- `submission/runbooks/AI_DISABLED_CONTINUITY.md`
- `submission/runbooks/INCIDENT_RESPONSE.md`
- `submission/runbooks/DEPLOYMENT.md`
- `submission/runbooks/RETIREMENT.md`

Deployment target:

- Local/offline demo first.
- Optional static UI plus Python CLI.
- No external service dependency required.
- If adding containers, include Dockerfile only under `submission/`.

Operational controls:

- setup command,
- run command,
- test command,
- evaluate command,
- reset command,
- evidence export command,
- kill switch,
- manual fallback,
- backup/restore,
- vendor exit and retirement evidence preservation.

Minimum run commands:

```text
python submission/scripts/run_app.py
python submission/scripts/run_tests.py
python submission/scripts/evaluate_public_fixtures.py
python submission/scripts/export_evidence.py
python submission/scripts/reset_submission.py
```

---

## 4. Workflow-specific implementation specs

### Batch workflow spec

Inputs:

- `evaluation/public_fixtures/PUB-01.json`
- `PUB-02.json`
- `PUB-03.json`
- batch-related CSVs in `data/`
- batch-related knowledge files in `knowledge/`

Must detect:

- batch status,
- genealogy gaps,
- warehouse/MES mismatch,
- unit mismatch,
- OOS/OOT conflict,
- open investigation,
- missing release packet item,
- unverified supplier commitment,
- provenance gap.

Must output:

- evidence,
- contradictions,
- gaps,
- abstentions,
- human review,
- audit,
- readiness state,
- applicable documents.

Must not:

- release,
- reject,
- recall,
- relabel,
- reprocess.

---

### PV workflow spec

Inputs:

- `evaluation/public_fixtures/PUB-04.json`
- `PUB-05.json`
- `PUB-06.json`
- PV-related CSVs in `data/`
- PV-related knowledge files in `knowledge/`

Must detect:

- duplicate case candidates,
- conflicting awareness dates,
- MedDRA version mismatch,
- listedness source conflict,
- product-quality linkage,
- sensitive pregnancy or paediatric content,
- multilingual extraction uncertainty.

Must output:

- intake support summary,
- source-to-case linkage,
- duplicate rationale,
- reporting-clock evidence,
- listedness evidence,
- uncertainty and abstentions,
- human safety review requirement.

Must not:

- decide seriousness,
- decide causality,
- decide expectedness,
- decide reportability,
- confirm signal.

---

### Supply workflow spec

Inputs:

- `evaluation/public_fixtures/PUB-07.json`
- `PUB-08.json`
- supply-related CSVs in `data/`
- supply-related knowledge files in `knowledge/`

Must detect:

- cold-chain excursion,
- logger clock conflict,
- pallet association uncertainty,
- inventory and quality status,
- market authorization constraints,
- trial demand,
- compassionate-use constraints,
- allocation ethics,
- CMO capacity conflict.

Must output:

- non-executing recovery options,
- constraints,
- risks,
- quality gates,
- required approvals,
- evidence citations,
- abstentions.

Must not:

- allocate stock,
- reserve capacity,
- change inventory quality status,
- ship product,
- initiate recall.

---

## 5. Evaluation mapping

Use `evaluation/PUBLIC_FIXTURE_INDEX.csv`.

| Fixture | Workflow | Use |
|---|---|---|
| PUB-01 | batch | Unit mismatch, genealogy, OOS/OOT, supplier commitment, provenance |
| PUB-02 | batch | Additional batch readiness test |
| PUB-03 | batch | Additional batch readiness test |
| PUB-04 | pv | PV intake test |
| PUB-05 | pv | PV intake test |
| PUB-06 | pv | PV intake test |
| PUB-07 | supply | Supply/cold-chain test |
| PUB-08 | supply | Supply/cold-chain test |
| PUB-09 | security | Non-executing security test |
| PUB-10 | reliability | Outage/recovery test |
| PUB-11 | privacy | Privacy-boundary test |
| PUB-12 | integration | Cross-workflow integration test |
| PUB-13 | agent | Agent budget/stop-policy test |
| PUB-14 | finops | Token/cost control test |
| PUB-15 | clinical | Clinical-boundary test |

---

## 6. Security, privacy and GxP controls

Implement controls for:

- prompt injection in source documents,
- untrusted knowledge documents,
- superseded policy,
- tool-manifest poisoning,
- stale authorization,
- safety-data exfiltration,
- model artifact mismatch,
- denial-of-wallet,
- privacy purpose limitation,
- re-identification risk,
- retention conflict,
- audit-trail gaps.

Fail closed when:

- user authorization is missing or stale,
- source authority is unknown,
- knowledge document is untrusted,
- effective date is not applicable,
- evidence conflicts are high risk,
- requested action is prohibited,
- output contract cannot be validated.

---

## 7. Definition of done for Cursor

Cursor should stop only when all are true:

1. Required artefacts exist under `submission/artefacts/`.
2. App/code exists only under `submission/`.
3. Three mandatory workflows are implemented.
4. Public fixtures can be evaluated.
5. Outputs are contract-valid.
6. Prohibited actions fail closed.
7. Manual fallback and AI-disabled continuity are documented.
8. Evidence export works.
9. Runbooks explain setup, run, test, evaluate, reset and export.
10. Final structure check passes:

```text
python tools/check_submission_structure.py --final
```

---

## 8. Final build implementation strategy

The goal is a complete final build, not only a narrow `PUB-01` prototype. Use a **gated final-build strategy**: build all required workflows and evidence, but do it in controlled gates so failures are visible and regulated boundaries stay intact.

### Gate 0 — Final-build scaffold

Create the full participant workspace under `submission/`:

- required artefact files under `submission/artefacts/`,
- source modules under `submission/src/`,
- UI files under `submission/app/`,
- tests under `submission/tests/`,
- scripts under `submission/scripts/`,
- machine-readable evidence under `submission/evidence/`,
- operational runbooks under `submission/runbooks/`.

Do not modify challenge evidence.

### Gate 1 — Business discovery and traceability

Use `submission/artefacts/00_case_discovery_understanding.md` first, then produce the formal discovery outputs.

Complete:

- business problem and SCQA,
- no-AI and alternative comparison,
- stakeholder decision rights,
- inject-to-workflow traceability,
- data/source-document/knowledge mapping,
- intended use and prohibited use,
- regulatory boundary and human accountability,
- final defence obligations.

Exit gate only when each mandatory workflow links to:

- case injects,
- data files,
- source documents,
- knowledge controls,
- public fixtures,
- contracts,
- human decision roles.

### Gate 2 — Deterministic core platform

Implement reusable deterministic services before workflow-specific logic:

- `FixtureLoader`,
- `DataLoader`,
- `SourceDocumentLoader`,
- `RegulatoryReferenceMapper`,
- `AuthorityChecker`,
- `ContractValidator`,
- `ProhibitedActionGuard`,
- `AuditExporter`,
- common workflow response builder.

Exit gate only when:

- loaders preserve source path and hash,
- knowledge/source-document limitations are represented,
- prohibited actions fail closed,
- audit export works,
- contract validation can run locally.

### Gate 3 — Three mandatory workflows

Implement all three mandatory workflows, not just one:

1. **Batch evidence readiness**
   - Cover `PUB-01`, `PUB-02`, `PUB-03`.
   - Detect unit mismatch, genealogy gaps, OOS/OOT conflicts, open investigations, supplier evidence gaps and provenance issues.
   - Output must validate against `batch_response.schema.json`.

2. **PV intake and signal support**
   - Cover `PUB-04`, `PUB-05`, `PUB-06`.
   - Detect duplicates, awareness-date conflicts, terminology/version issues, listedness context and uncertainty.
   - Output must validate against `pv_response.schema.json`.

3. **Supply and cold-chain option planning**
   - Cover `PUB-07`, `PUB-08`.
   - Detect cold-chain/logger issues, inventory constraints, market authorization limits, demand conflicts and approval gates.
   - Output must validate against `supply_response.schema.json`.

Exit gate only when all three workflows:

- produce contract-valid outputs,
- cite evidence,
- state uncertainty and abstentions,
- require human review,
- set regulated execution status to `not_executed`,
- cannot perform prohibited actions.

### Gate 4 — Cross-cutting challenge coverage

Add support and tests for remaining public fixture themes:

- `PUB-09` security,
- `PUB-10` reliability and outage recovery,
- `PUB-11` privacy,
- `PUB-12` integration,
- `PUB-13` agent budget and stop policy,
- `PUB-14` FinOps,
- `PUB-15` clinical boundary.

These may use participant-defined non-executing output contracts where official contracts are not supplied.

Exit gate only when the system demonstrates:

- prompt/document injection handling,
- poisoned tool rejection,
- stale authorization blocking,
- privacy purpose limitation,
- AI-disabled manual mode,
- token/cost controls,
- clinical decision boundary protection.

### Gate 5 — User-facing app and CLI

Build a usable local/offline interface:

- CLI for running workflows and evaluation,
- simple UI for reviewing workflow outputs,
- evidence tables,
- contradictions and gaps,
- abstentions,
- human-review state,
- blocked prohibited actions,
- audit/evidence export.

The UI must not include buttons or flows for release, rejection, final PV decision, stock allocation, shipment or recall.

### Gate 6 — Evaluation, runbooks and evidence export

Create scripts and runbooks for:

- setup,
- run,
- test,
- evaluate,
- reset/rollback,
- export evidence,
- AI-disabled continuity,
- incident response,
- deployment,
- retirement/vendor exit.

Required validation commands:

```text
python tools/test_contracts.py
python submission/scripts/run_tests.py
python submission/scripts/evaluate_public_fixtures.py
python submission/scripts/export_evidence.py
python tools/hash_submission.py
python tools/check_submission_structure.py --final
```

Machine-readable evidence must include:

- `submission/evidence/submission_manifest.csv`,
- `submission/evidence/file_hashes.csv`,
- `submission/evidence/test_results.json`,
- `submission/evidence/evaluation_results.json`.

### Gate 7 — Final defence package

Prepare final defence evidence showing:

- all three workflows,
- public fixture evaluation,
- prohibited-action blocking,
- malicious document / poisoned tool handling,
- outage and manual mode,
- privacy and subgroup risks,
- cost/token model,
- architecture and ADR decisions,
- vendor exit and retirement plan,
- board recommendation.

### Final-build Cursor prompt

```text
Implement the final build strategy in submission/CURSOR_SPEC_DRIVEN_ENTERPRISE_APP_TASK.md.
Use submission/artefacts/00_case_discovery_understanding.md first for business understanding.
Work through Gates 0-7 in order.
Keep all work under submission/.
Build all three mandatory workflows, public fixture evaluation, prohibited-action blocking, audit evidence export, runbooks, tests, and final defence evidence.
Do not modify challenge evidence.
Do not implement any regulated execution action.
Stop and fix failures when any contract, prohibited-action, audit, evaluation, or structure gate fails.
```

---

## 9. Final defence checklist

Prepare to demonstrate:

- SCQA and problem statement.
- Why AI is justified or where no-AI is better.
- DDD context map.
- Architecture and ADRs.
- Batch, PV and supply workflows.
- Public fixture evaluation.
- Prohibited-action blocking.
- Prompt injection and untrusted-document handling.
- AI-disabled manual mode.
- Evidence export and audit trail.
- Residual risks and go / conditional-go / pivot / pause / stop recommendation.
