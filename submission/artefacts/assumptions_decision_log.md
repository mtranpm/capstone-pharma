# Assumptions & Decision Log

Living log. Record assumptions explicitly; abstain in product behaviour when unresolved.  
Do not silently normalize regulated evidence.

| ID | Type | Statement | Basis | Status | Linked artefacts |
|---|---|---|---|---|---|
| A-001 | Assumption | Synthetic challenge CSVs under `data/` are sufficient for offline deterministic evaluation | Workshop design | Open | `01`, `09` |
| A-002 | Assumption | Knowledge catalog authority statuses are authoritative for gate decisions in this exercise | `knowledge_catalog.csv` | Open | `09`, `12` |
| A-003 | Interpretation | Narrowest viable intervention is advisory evidence orchestration (not full PQS automation) | A1 framing, INJ-003/006 | Accepted | `01`, `02` |
| D-001 | Decision | Hybrid Python ports/adapters + Pydantic v2 + FastAPI; React human review; Neo4j advisory KG with offline stub | Plan locked decisions | Accepted | Pre-Phase, `11` |
| D-002 | Decision | Specs live under `Docs/specs/`; Cursor rules link there | Plan | Accepted | Pre-Phase |
| D-003 | Decision | No-AI-only path rejected as sole solution; hybrid selected with stop/pivot | Options analysis | Accepted | `02`, `04` |
| D-004 | Decision | Prohibited actions are hard stops (NN-01..03); UI must not offer execute controls | Non-negotiables | Accepted | `01`, `03`, `13` |
| D-005 | Decision | Phase 1 inject register = 84 rows in `traceability_inject_workflow.csv` | `inject_evidence_map` / case data | Accepted | `01`, `13` |
| A-004 | Assumption | Board 14% lead-time target remains a pressure metric, not a license to weaken Quality independence | `board_requests.csv` | Open | `01`, `04` |
| G-001 | Gap | ISO/EU + LLM Top 10 IDs not yet fully mapped into RTM rows — **Superseded 2026-08-10:** mapping in `13` §8; executable test evidence still open | Phase 5 P5-01 | Closed (mapping) | `13` §8 |
| G-002 | Gap | Multilingual / a11y detail deferred to artefact `07` | Phase 3 | Open | `07` |
| G-003 | Gap | Brownfield starter review deferred to artefact `15` — **Superseded 2026-08-10:** `15` complete | Phase 5 | Closed | `15` |
| D-006 | Decision | Executive SCQA + value hypothesis locked in `01` v0.2.0; intervention = evidence packet prep only (narrower than enterprise problem); `37` seeded with defence hooks | Phase 2 exit | Accepted | `01`, `37` |
| D-007 | Decision | Canonical SCQA stored in separate file `submission/artefacts/SCQA.md`; `01`/`37` keep summaries and point to it | User request | Accepted | `SCQA.md` |
| D-008 | Decision | Mandatory human review gates (G-HR-01..06) before packet export; emergency stop ES-01..05 documented | Phase 3 `06`, A11, NN-01..03 | Accepted | `06`, `05`, `13` |
| D-009 | Decision | Neo4j adopted only as advisory `GraphPort` projection; CSV SoR remains authoritative; `InMemoryGraphStub` required for offline | Phase 4 `11`, Engineering spec §4 | Accepted | `11`, `16`, D-001 |
| D-010 | Decision | Document authority states (trusted/pending/superseded/untrusted) mapped to `knowledge_catalog.csv`; hash verification before cite | Phase 4 `12`, NN-04 | Accepted | `12`, `09`, `AuthorityPort` |
| D-011 | Decision | DDD submission synthesis uses five views (Batch/PV/Supply/Authority/Evidence) while retaining ten A4 context names for audit | Phase 4 `08`, A2/A4/A5/A7 | Accepted | `08`, `ddd/README.md` |
| D-012 | Decision | PV multilingual preserve + WCAG-oriented keyboard/no-color-only baseline for review UI | Phase 3 `07`, PV-02 | Accepted | `07`, `13` |
| D-013 | Decision | Phase 5 architecture locked in `14`: 12 ADRs (hybrid ports, GraphPort, Pydantic strict, offline default, OTel redaction, React review-only, tool manifest, fail-closed, no graph SoR, read-only SoR, LlmPort, idempotency/audit) | Phase 5 exit | Accepted | `14`, `13`, `17` |
| D-014 | Decision | Brownfield approach = strangler fig on ports; starter reviewed in `15`; no SoR write-back | `15`, ADR-010 | Accepted | `15`, `37` |
| D-015 | Decision | Governed retrieval only — no open RAG; retrieved content untrusted until authority/hash verify (`19`) | OWASP LLM01/04/08 | Accepted | `19`, `28`, NN-04 |
| D-016 | Decision | Agent runs bounded by tool/turn/token/time budgets with checkpoints (`20`); exceed → STOP-BUDGET | XC-05, PUB-13 | Accepted | `20`, `29` |
| D-017 | Decision | Degraded mode ladder D0–D5 + kill switches KS-AI/AGENT/GRAPH/EXPORT/REGION (`21`) | NN-06, XC-02 | Accepted | `21`, `35` |
| D-018 | Decision | TEVV uses Cohen κ, weighted κ, Gwet AC1 for advisory fields; F1 for G-* classification; κ≥0.6 soft threshold only (`32`) | Phase 5 QA | Accepted | `32`, `23`, `27` |
| D-019 | Decision | RTM `13` v0.2.0 adds §8 ISO 42001 / EU AI Act indicative / LLM01–10 crosswalk — closes ID mapping for G-001 | P5-01 | Accepted | `13`, `26`, `28` |
| D-020 | Decision | `37` defence package expanded to v1.0.0 narrative with evidence paths; eval/red-team runs explicitly pending | Phase 5 | Accepted | `37` |
| D-021 | Decision | AGENTS.md not required for Phase 6 exit; artefact `17` inventories workshop `.cursor` agents/skills/commands/rules; hooks/MCP optional; custom new agents/skills not required (roles may be simulated via prompts) | Phase 6 P6-01/P6-02 | Accepted | `17`, `00` task list |
| D-022 | Decision | Overnight Phases 3–10 build accepted: deterministic workflows + graders for PUB-01..15; React review UI scaffold; runbooks/scripts/evidence; `--final` structural PASS; eval `hard_gate=pass` (47 pytest) | User continue-rest request | Accepted | `00` task list, `evidence/` |
| D-023 | Decision | Register executable `G-OTEL` + `G-ISO-EU` graders (correlation/redaction; Art.14 oversight + advisory-only). Soft relative to hard safety set unless fail on required fields | Gap close 2026-08-10 | Accepted | `32`, `evaluation/graders/` |
| D-024 | Decision | M-AGREE remains `pending_human_calibration`; κ/AC1 **not fabricated**; code returns null metrics until dual labels exist; evidence note under `evidence/m_agree_pending_human_calibration.md` | Gap close; D-018 | Accepted | `32`, `metrics/agreement.py` |
| D-025 | Decision | Neo4j adapter upgraded beyond placeholder: allow-listed Cypher, seed_from_plan, degrade to `neo4j_unavailable`; offline default remains `InMemoryGraphStub` | Gap close P7-11 | Accepted | `graph_neo4j.py`, `load_graph.py`, `11` |
| D-026 | Decision | Multilingual/subgroup deterministic coverage via PUB-04 language preservation tests; κ-by-language still blocked on human labels (same as M-AGREE) | P8-08 close | Accepted | `test_multilingual_subgroup.py`, `32` §5 |
| A-005 | Assumption | Node.js may be absent on grader hosts; UI demo is optional and must not gate CLI/eval/`--final` | Workshop environments | Open (this host had Node — build verified; still optional for challenge path) | `SETUP.md`, P9 |
| D-027 | Decision | `npm install` + `vite build` verified 2026-08-10; `node_modules`/`dist` gitignored and not retained in tree after verify | Gap close P9 | Accepted | `app/.gitignore`, `SETUP.md` |

## Change rules

1. New assumption → new ID; never overwrite prior text (append supersession note).  
2. Decisions that change architecture or regulated boundary → update RTM + task list.  
3. If identity/unit/time/authority cannot be resolved in a run → product abstains; log here only if it changes programme assumptions.
