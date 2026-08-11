# 17 — Cursor Engineering Evidence

| Field | Entry |
|---|---|
| Owner | Engineering lead |
| Version | 0.2.0 |
| Status | Phase 6 exit — MET |
| Sources | `.cursor/{agents,skills,commands,rules}/`, `Docs/specs/Engineering/`, `Docs/specs/Security/`, task list P6, D-021 |

## 1. Purpose

Document how **Cursor-assisted development** is governed for AEGIS-PHARMA: inventory of workshop Cursor assets, nine-role RACI (simulatable via prompts), Docs/specs pointers, and explicit exit stance on AGENTS.md / hooks / MCP / custom agents.

## 2. Exit stance (Phase 6)

| Item | Stance |
|---|---|
| `AGENTS.md` | **Not used** and **not required** for Phase 6 exit |
| Hooks (`.cursor/hooks.json`) | **Optional** — none required for workshop exit |
| MCP servers | **Optional** — external docs untrusted until cross-checked with `Docs/specs/` |
| New custom agents / skills | **Not required** for exit — workshop inventory below is sufficient; roles may be simulated via task prompts |

Decision **D-021**: AGENTS.md not required; this artefact inventories workshop agents/skills/commands/rules.

## 3. Inventory — workshop Cursor assets

### 3.1 Agents (`.cursor/agents/`)

| File | Role in workshop |
|---|---|
| [`test-engineer.md`](../../.cursor/agents/test-engineer.md) | Deterministic / adversarial / prohibited-action tests |
| [`security-reviewer.md`](../../.cursor/agents/security-reviewer.md) | Injection, tool poisoning, auth, kill-switch review |
| [`evidence-reviewer.md`](../../.cursor/agents/evidence-reviewer.md) | Authority, lineage, conflicts — no regulated decisions |

### 3.2 Skills (`.cursor/skills/`)

| File | Domain skill |
|---|---|
| [`pv-case-intake.md`](../../.cursor/skills/pv-case-intake.md) | PV intake with uncertainty / verbatim preserve |
| [`gxp-evidence-reconciliation.md`](../../.cursor/skills/gxp-evidence-reconciliation.md) | GxP cite / conflict / abstain / human review |
| [`bounded-supply-planning.md`](../../.cursor/skills/bounded-supply-planning.md) | Draft supply options only; no side effects |

### 3.3 Commands (`.cursor/commands/`)

| File | Intent |
|---|---|
| [`00_qualify_problem.md`](../../.cursor/commands/00_qualify_problem.md) | Qualify problem; compare no-AI alternatives |
| [`01_map_evidence.md`](../../.cursor/commands/01_map_evidence.md) | Map sources, authority, lineage, gaps |
| [`02_build_tests_first.md`](../../.cursor/commands/02_build_tests_first.md) | Contracts + deterministic tests before implementation |

### 3.4 Rules (`.cursor/rules/`)

| Rule file | Apply | Key enforcements |
|---|---|---|
| [`pharma-fde.mdc`](../../.cursor/rules/pharma-fde.mdc) | Always (workspace) | Work under `submission/`; immutable challenge evidence; no regulated automation; deny-by-default; tests before inference; offline mode |
| [`aegis-typed-contracts.mdc`](../../.cursor/rules/aegis-typed-contracts.mdc) | `submission/**/*.py` | Pydantic strict / ports / FastAPI discipline → Engineering specs |
| [`aegis-owasp-llm-top10.mdc`](../../.cursor/rules/aegis-owasp-llm-top10.mdc) | `submission/**/*.{py,ts,tsx}` | Untrusted retrieval; no excessive agency → Security spec |
| [`aegis-otel.mdc`](../../.cursor/rules/aegis-otel.mdc) | `submission/**/*.py` | Redaction, offline exporter, fail-closed telemetry |

Rule themes map to NN-01..06 and programme non-negotiables in `13`.

## 4. Spec-driven engineering (Docs/specs)

| Spec | Path | Governs |
|---|---|---|
| Typed contracts, ports, FastAPI | [`Docs/specs/Engineering/TYPED_CONTRACTS_PORTS_FASTAPI.md`](../../Docs/specs/Engineering/TYPED_CONTRACTS_PORTS_FASTAPI.md) | Pydantic v2 strict, ports (`FixturePort`, `AuthorityPort`, `GraphPort`, `LlmPort`, `AuditPort`, `TelemetryPort`, `ToolManifestPort`), offline stub |
| OpenTelemetry | [`Docs/specs/Engineering/OPENTELEMETRY_TELEMETRY.md`](../../Docs/specs/Engineering/OPENTELEMETRY_TELEMETRY.md) | Redaction, correlation ids |
| OWASP LLM Top 10 | [`Docs/specs/Security/OWASP_LLM_TOP10_THREAT_CONTROLS.md`](../../Docs/specs/Security/OWASP_LLM_TOP10_THREAT_CONTROLS.md) | Tool poisoning, excessive agency |
| Enterprise app task | [`Docs/specs/Tasks/CURSOR_SPEC_DRIVEN_ENTERPRISE_APP_TASK.md`](../../Docs/specs/Tasks/CURSOR_SPEC_DRIVEN_ENTERPRISE_APP_TASK.md) | Workshop delivery pattern (nine roles) |

Decision **D-002**: specs live under `Docs/specs/`; rules link there (not duplicated in chat).

## 5. Nine Cursor task roles — owner / reviewer (RACI)

Roles below match Phase 6 of the enterprise app task. Custom Cursor agents are **not required**; any role may be **simulated via prompts**. Workshop agents/skills/commands above support a subset; remaining roles use prompt simulation + human owner/reviewer.

| # | Cursor task role | Owner (R) | Reviewer (A/C) | Simulation / workshop asset | Evidence artefacts |
|---|---|---|---|---|---|
| 1 | Product Strategist | Product / value lead | Quality delegate | Prompt + `00_qualify_problem` | `SCQA.md`, `01`, `05`, `03` |
| 2 | Domain Architect | Architecture / domain lead | RA + Quality | Prompt | `08`, `ddd/README.md` |
| 3 | GxP/Safety Boundary | Quality / GxP lead | RA + CISO | Prompt + `gxp-evidence-reconciliation` skill | `06`, `22`, `23`, `13` |
| 4 | Data/Evidence Lineage | Data platform lead | Quality, DPO | Prompt + `01_map_evidence` + `evidence-reviewer` agent | `09`, `10`, `12` |
| 5 | Security/Privacy | CISO delegate | Platform + DPO | Prompt + `security-reviewer` agent + OWASP rule | `28`, `29`, `30` |
| 6 | Backend Engineer | Engineering lead | Security + Test | Prompt + typed-contracts / otel rules | ports, CLI, contract tests |
| 7 | Frontend/UX | UX / frontend lead | Quality + Product | Prompt | review UI (non-execute), `07` |
| 8 | Test Engineer | QA evidence lead | Product + Security | `test-engineer` agent + `02_build_tests_first` | `13`, graders, `submission/tests/` |
| 9 | DevOps/Operations | Platform / ops lead | Engineering + CISO | Prompt | `16`, `21`, runbooks |

**Acceptance sequence (recommended):** Product Strategist → Domain Architect → GxP/Safety → Data Lineage → Security/Privacy → Backend → Frontend → Test → DevOps.

**Gate before final acceptance:** Security, GxP, and Test roles review implementation (human accountable; AI assists only).

### 5.1 Area RACI (programme)

| Area | Owner | Reviewer(s) | Evidence artefact |
|---|---|---|---|
| Product / regulated boundary | Product / value lead | Quality delegate | `05`, `03`, `SCQA.md` |
| Domain & DDD synthesis | Architecture / domain lead | RA + Quality | `08`, `ddd/README.md` |
| Data & authority | Data platform lead | Quality, DPO | `09`, `10`, `12` |
| Graph decision | Architecture lead | Platform | `11`, contract tests |
| Security & tools | CISO delegate | Platform | `29`, `28` |
| QA evidence / RTM | QA evidence lead | Product | `13`, graders |
| Cursor rule / asset changes | Engineering lead | CISO + Quality | This file + PR review |

AI-generated code **requires** human review before merge; prohibited-action guards are not optional features.

## 6. Implementation evidence (submission)

| Evidence type | Location |
|---|---|
| Port protocol & fakes | `submission/src/aegis/ports/`, `submission/tests/contracts/test_port_adapter_fakes.py` |
| Composition / offline default | `submission/src/aegis/composition.py`, `InMemoryGraphStub` |
| CLI offline path | `submission/src/aegis/cli.py` |
| Contract tests | `submission/tests/contracts/` |
| Task completion | `submission/artefacts/00_implementation_task_list.md` (P6-01, P6-02) |

## 7. Hooks & MCP (optional)

| Mechanism | Status | Note |
|---|---|---|
| Cursor hooks (`.cursor/hooks.json`) | **Optional — not required** | May add pre-commit lint or secret scan later |
| MCP servers (browser, Context7, MongoDB, etc.) | **Optional** | External docs untrusted until cross-checked with specs |
| Bugbot / security review agents | On demand | Use for PRs touching orchestration or auth |

No hook is a substitute for deterministic contract tests and evaluation graders.

## 8. Hybrid architecture lock (engineering)

| Layer | Choice | Rule reference |
|---|---|---|
| Domain / application | Python ports + adapters | TYPED_CONTRACTS §4 |
| API | FastAPI OpenAPI | §5 |
| UI | React human review | No execute controls for NN-01..03 |
| Graph | Neo4j advisory + `InMemoryGraphStub` | D-001, `11` |
| LLM | Optional behind `LlmPort`; offline stub default | NN-06 |

## 9. Traceability

| Programme requirement | Engineering control |
|---|---|
| NN-01..03 | Router guards + UI affordances + tests |
| NN-04 | `AuthorityPort` + catalog hash |
| NN-05 | Abstention error codes |
| NN-06 | Stub composition root |
| XC-04 | Typed clients / contract tests |

## 10. Gaps (non-blocking for Phase 6)

| Gap | Plan |
|---|---|
| Full Neo4j adapter implementation | Later phase (`graph_neo4j.py` placeholder) |
| Automated Cursor rule compliance scan | Optional hook; manual review for capstone |
| ISO/EU control IDs executable test evidence | Tracked via `13` / graders (mapping closed G-001) |
