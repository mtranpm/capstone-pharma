# AEGIS-PHARMA — Implementation Task List

Living checklist for track and implement. Primary tracker = **Phases 1–10** (+ Pre-Phase).  
Plan source: Cursor plan `aegis_implementation_tasks_03199b29.plan.md`.  
All build/evidence under `submission/`. Challenge evidence outside `submission/` is immutable.

**Status legend:** `[ ]` pending · `[~]` in progress · `[x]` done · `[!]` blocked

---

## Locked decisions

| Area | Decision |
|---|---|
| Tracker | Phases 1–10 (gates optional verify only) |
| Core | Python ports/adapters, type hints |
| Contracts | Pydantic v2 strict; FastAPI + OpenAPI; typed errors; clients with retry/backoff |
| Telemetry | OpenTelemetry (offline console/file default) |
| Graph | Neo4j advisory KG + ontology; GraphPort + in-memory stub for offline |
| UI | React — human-review workflows + ontology/KG dashboard |
| Challenge path | CLI/eval without React/Neo4j |
| Design rules | `Docs/Regulations/iso_42001_eu_ai_act.md` + OWASP LLM Top 10 |
| Specs location | `Docs/specs/Engineering/`, `Docs/specs/Security/` |
| Hooks / MCP | Not required |
| Agreement metrics | Cohen’s κ (+ weighted κ / Gwet AC1); F1 for deterministic graders |

---

## Pre-Phase — Scaffold

| ID | Task | Status |
|---|---|---|
| P0-01 | Create `Docs/specs/Engineering/TYPED_CONTRACTS_PORTS_FASTAPI.md` | [x] |
| P0-02 | Create `Docs/specs/Engineering/OPENTELEMETRY_TELEMETRY.md` | [x] |
| P0-03 | Create `Docs/specs/Security/OWASP_LLM_TOP10_THREAT_CONTROLS.md` | [x] |
| P0-04 | Create `.cursor/rules/aegis-typed-contracts.mdc` (link Docs specs) | [x] |
| P0-05 | Create `.cursor/rules/aegis-owasp-llm-top10.mdc` | [x] |
| P0-06 | Create `.cursor/rules/aegis-otel.mdc` (or fold OTel into typed-contracts rule) | [x] |
| P0-07 | Seed `submission/artefacts/00_case_discovery_understanding.md` | [x] |
| P0-08 | Seed `submission/CURSOR_SPEC_DRIVEN_ENTERPRISE_APP_TASK.md` | [x] |
| P0-09 | Stub artefacts `01`–`37` under `submission/artefacts/` | [x] |
| P0-10 | Scaffold `submission/src/aegis/` (domain, ports, adapters, contracts, api, clients, telemetry, cli, composition) | [x] |
| P0-11 | Scaffold FastAPI `/docs`, health, sample workflow + `/ontology` + `/graph` stubs | [x] |
| P0-12 | GraphPort: InMemoryGraphStub + Neo4j adapter placeholder | [x] |
| P0-13 | Pin deps: pydantic v2, fastapi, httpx, uvicorn, neo4j, OTel packages | [x] |
| P0-14 | Scaffold `submission/tests/contracts/` + security/OTel redaction stubs | [x] |
| P0-15 | Run `python tools/check_submission_structure.py --scaffold` | [x] |
| P0-16 | Preserve `submission/optimized _project_plan.xlsx` | [x] |

**Exit:** specs + rules + typed skeleton; offline stub works without Neo4j; challenge evidence untouched.

---

## Phase 1 — Discovery and evidence mapping

| ID | Task | Artefact / output | Status |
|---|---|---|---|
| P1-01 | Business-first repo map (case/data/knowledge/source_documents/evaluation/requirements) | notes → `01` | [x] |
| P1-02 | Inject→workflow matrix (beyond PUB; aim 84 injects) | `traceability_inject_workflow.csv` + `01` | [x] |
| P1-03 | Data→workflow, source_document→record, knowledge→control maps | `09`, `13` | [x] |
| P1-04 | Write `01_discovery_problem_baseline_value.md` | `01` | [x] |
| P1-05 | Write `02_no_ai_and_solution_options.md` | `02` | [x] |
| P1-06 | Write `03_stakeholders_decision_rights.md` | `03` | [x] |
| P1-07 | Write `04_dmaic_benefits_stop_pivot.md` | `04` | [x] |
| P1-08 | Write/refresh `09_data_governance_lineage_contracts.md` | `09` | [x] |
| P1-09 | Write/refresh `13_requirements_traceability_matrix.md` | `13` | [x] |
| P1-10 | Start assumptions & decision log | `submission/artefacts/assumptions_decision_log.md` | [x] |
| P1-11 | SCQA draft via Prompt `02` (gaps via Prompt `01`) | into `01` / `SCQA.md` | [x] |

**Exit:** each of Batch/PV/Supply links to injects, data, source docs, knowledge, fixtures, contracts, human owners; prohibited actions listed; no-AI alternative documented. **MET 2026-08-10.**

---

## Phase 2 — SCQA and executive framing

| ID | Task | Status |
|---|---|---|
| P2-01 | Finalize SCQA + value hypothesis in artefact `01` | [x] |
| P2-02 | Seed executive case hooks for artefact `37` | [x] |

**Exit:** concise executive SCQA; intervention narrower than the full business problem. **MET 2026-08-10.** Canonical: `SCQA.md`.

---

## Phase 3 — PRD

| ID | Task | Status |
|---|---|---|
| P3-01 | Write `05_product_operating_model.md` | [x] |
| P3-02 | Write `06_human_oversight_and_emergency_stop.md` | [x] |
| P3-03 | Write `07_adoption_accessibility_change.md` (incl. multilingual, a11y) | [x] |

**Exit:** advisory vs regulated decisions separated; requirements traceable. **MET.**

---

## Phase 4 — DDD, ontology, Neo4j KG

| ID | Task | Status |
|---|---|---|
| P4-01 | Synthesize Docs/DDD-Lab → `08_ddd_context_map.md` (no full Prompt 03 re-run) | [x] |
| P4-02 | Write `10_ontology_semantic_layer.md` | [x] |
| P4-03 | Write `11_knowledge_graph_decision.md` — **adopt Neo4j** + simpler-alternative benchmark | [x] |
| P4-04 | Write `12_document_authority_model.md` | [x] |
| P4-05 | Optional `submission/artefacts/ddd/` extracts | [x] |
| P4-06 | Document local Neo4j setup constraints (no cloud secrets in repo) | [x] |

**Exit:** `08`+`10`+`11`+`12` complete; Neo4j adoption defended. **MET.**

---

## Phase 5 — Architecture and ADRs

| ID | Task | Status |
|---|---|---|
| P5-01 | Refresh RTM `13` with ISO/EU + LLM01–10 IDs | [x] |
| P5-02 | Write `14_architecture_c4_adrs.md` (≥10 ADRs; hybrid + Neo4j GraphPort) | [x] |
| P5-03 | Write `15_brownfield_modernization_plan.md` + review `starter/` | [x] |
| P5-04 | Write `16_reproducibility_and_offline_execution.md` | [x] |
| P5-05 | Write `28_threat_abuse_model.md` (OWASP LLM map) | [x] |
| P5-06 | Document RAG/retrieval stance in design (artefact `19` draft) | [x] |

**Exit:** architecture traces to PRD/DDD/regulation/OWASP; ADRs complete. **MET.**

---

## Phase 6 — Cursor working model

| ID | Task | Status |
|---|---|---|
| P6-01 | Write `17_cursor_engineering_evidence.md` (rules, skills, agents, commands, Docs specs) | [x] |
| P6-02 | Confirm hooks/MCP optional; document if any added later | [x] |

**Exit:** owner + review role model; GxP/security/test review before acceptance. **MET.**

---

## Phase 7 — Dev specs and build

| ID | Task | Status |
|---|---|---|
| P7-01 | Write/refresh `18_model_baseline_selection_substitution.md` | [x] |
| P7-02 | Write/refresh `19_ai_context_and_tool_design.md` | [x] |
| P7-03 | Write/refresh `20_agent_budget_stop_checkpointing.md` | [x] |
| P7-04 | Write/refresh `21_degraded_mode_kill_switch_continuity.md` | [x] |
| P7-05 | Implement deterministic loaders, authority, contracts, prohibited-action, audit | [x] |
| P7-06 | Batch workflow PUB-01..03 (contract-valid, not_executed) | [x] |
| P7-07 | PV workflow PUB-04..06 | [x] |
| P7-08 | Supply workflow PUB-07..08 | [x] |
| P7-09 | FastAPI routes for three workflows + typed errors | [x] |
| P7-10 | Tool-arg validation (Pydantic) + typed clients retry/backoff | [x] |
| P7-11 | `scripts/load_graph.py` + Neo4j adapter; allow-listed Cypher API | [x] |
| P7-12 | OTel spans/metrics/logs; redaction; trace↔audit correlation | [x] |
| P7-13 | Signed/approved tool-manifest runtime check | [x] |
| P7-14 | AI-disabled / kill-switch path | [x] |

**Exit:** CLI + FastAPI prove three workflows; PUB-01 never disposition; offline stub safe. **MET.**

---

## Phase 8 — Tests, graders, TEVV

| ID | Task | Status |
|---|---|---|
| P8-01 | Write `32_tevv_evaluation_strategy.md` (incl. κ thresholds) | [x] |
| P8-02 | Write `31_red_team_and_remediation.md` | [x] |
| P8-03 | Implement graders under `submission/evaluation/graders/` (`G-SCHEMA` … `G-ISO-EU`, `G-OTEL`) | [x] |
| P8-04 | Agreement metrics `M-AGREE`: Cohen’s κ, weighted κ, Gwet AC1 as needed | [x] |
| P8-05 | Contract tests (Pydantic↔schema, OpenAPI, ports, tool-args) | [x] |
| P8-06 | Security suite (OWASP LLM adversarial) | [x] |
| P8-07 | PUB-01..15 evaluation via `evaluate_public_fixtures.py` | [x] |
| P8-08 | Multilingual + subgroup fixtures/analysis | [x] |
| P8-09 | Prohibited-action, authority, outage, regression suites | [x] |
| P8-10 | Draft `33` token economics / `34` FinOps (tie to OTel) | [x] |

**Exit:** contract + security + public-fixture suites green. **MET** — 47 pytest passed; eval `hard_gate=pass`.

---

## Phase 9 — React UI + ontology/KG dashboard

| ID | Task | Status |
|---|---|---|
| P9-01 | React app scaffold; typed OpenAPI client | [x] |
| P9-02 | Workflow review screens (evidence, gaps, abstentions, blocked actions, export) | [x] |
| P9-03 | No release/reject/allocate/recall/final-PV controls | [x] |
| P9-04 | Transparency / advisory copy (Art.13/50) | [x] |
| P9-05 | Ontology panel (`/dashboard/ontology-graph`) | [x] |
| P9-06 | Neo4j KG visualization via FastAPI (no browser Neo4j creds) | [x] |
| P9-07 | Graceful degrade when Neo4j unavailable | [x] |
| P9-08 | Accessibility: keyboard, no color-only warnings | [x] |
| P9-09 | Emergency stop / contestability UX (artefact `06`) | [x] |

**Exit:** React demo = review + ontology/KG; CLI/eval pass without UI/Neo4j. **MET** (`npm install` before UI demo).

---

## Phase 10 — Ops, evidence, defence

| ID | Task | Status |
|---|---|---|
| P10-01 | Runbooks: SETUP, RUN, EVALUATE, RESET_ROLLBACK, INCIDENT_RESPONSE, AI_DISABLED_CONTINUITY, DEPLOYMENT, RETIREMENT_AND_VENDOR_EXIT (+ OPERATIONS) | [x] |
| P10-02 | Scripts: run_app, run_tests, evaluate_public_fixtures, export_evidence, reset_submission, setup_env | [x] |
| P10-03 | Evidence: submission_manifest.csv, file_hashes.csv, test_results.json, evaluation_results.json | [x] |
| P10-04 | Complete `22`–`25`, `27`, `29`–`30`, `33`–`36` | [x] |
| P10-05 | Complete `26_ai_governance_analysis.md` (ISO↔EU crosswalk) | [x] |
| P10-06 | Complete `37_production_readiness_roadmap_defence.md` | [x] |
| P10-07 | Docker Compose (API + Neo4j + optional UI); keep CLI-without-Docker path | [x] |
| P10-08 | Clean-room handover rehearsal | [x] |
| P10-09 | Run final validation commands (`test_contracts`, `run_tests`, evaluate, export, hash, `--final`) | [x] |

**Exit:** clean-room reproducible; `--final` passes; hard scoring gates not violated. **MET 2026-08-10** (`check_submission_structure.py --final` PASS).

---

## Graders checklist (`G-*`)

| Grader | Status |
|---|---|
| G-SCHEMA | [x] |
| G-EXEC-BOUNDARY | [x] |
| G-HUMAN-REVIEW | [x] |
| G-PROVENANCE | [x] |
| G-AUTHORITY | [x] |
| G-ABSTENTION | [x] |
| G-BATCH-READINESS | [x] |
| G-PV-BOUNDARY | [x] |
| G-SUPPLY-BOUNDARY | [x] |
| G-OWASP-LLM | [x] |
| G-PRIVACY | [x] |
| G-RELIABILITY | [x] |
| G-FINOPS | [x] |
| G-OTEL | [x] |
| G-CLINICAL | [x] |
| G-ISO-EU | [x] |
| H-RUBRIC | [ ] |
| J-LLM (optional soft only) | [ ] |
| M-AGREE (Cohen’s κ + companions) | [~] pending human calibration — no fabricated κ |

---

## Gap register (do not leave to the end)

| Gap | Phase | Status |
|---|---|---|
| Artefacts 18–21 | 7 | [x] |
| Artefacts 22–25, 27, 29–30 | 5 draft / 10 finalize | [x] |
| Artefacts 33–36 | 8–10 | [x] |
| Brownfield 15 + starter/ | 5 | [x] |
| RAG/retrieval design 19 | 5/7 | [x] |
| Multilingual + subgroup | 8 | [x] (deterministic preserve; κ-by-lang pending labels) |
| Accessibility | 9 | [x] |
| 84-inject register | 1 | [x] |
| Assumptions & decision log | 1+ | [x] |
| Docker Compose | 10 | [x] |
| Clean-room rehearsal | 10 | [x] |
| Tool-manifest runtime check | 7/8 | [x] |
| Emergency stop UX | 9 | [x] |
| Neo4j local-only creds | 4/10 | [x] |

---

## Optional verify checkpoints

- [x] After Pre-Phase: scaffold OK  
- [x] After Phases 1–2: discovery/SCQA traceability  
- [x] After Phase 7: three workflows on CLI  
- [x] After Phase 8: cross-cutting fixtures  
- [x] After Phase 9: React + CLI independence  
- [x] After Phase 10: `--final` + defence  

---

## Next action

**Phases 1–10 complete; gap-close pass 2026-08-10.**  
Done this pass: `G-OTEL`/`G-ISO-EU` registered; Neo4j adapter allow-list + seed + degrade; M-AGREE documented as pending human calibration (no fabricated κ); multilingual/subgroup deterministic tests; SETUP Node note.

**True remaining (optional / human):**
- H-RUBRIC human scoring session
- M-AGREE dual annotation → real κ/AC1 (EVAL-03)
- Live Neo4j `--apply` on a local instance (offline stub remains default)
- J-LLM soft judge (optional)
- UI live demo against FastAPI (deps reinstall via `npm install` — build verified 2026-08-10)
