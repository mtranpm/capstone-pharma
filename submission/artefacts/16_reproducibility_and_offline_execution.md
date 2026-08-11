# 16 — Reproducibility & Offline Execution

| Field | Entry |
|---|---|
| Owner | Platform / QA evidence lead |
| Version / date | 1.0.0 / 2026-08-10 |
| Status | Phase 5 — clean-room recipe locked |
| Sources | ADR-004, `11`, `17`, NN-06, PUB-10, `evaluation/PUBLIC_FIXTURE_INDEX.csv` |

---

## 1. Objectives

1. **Deterministic evaluation** — same inputs → same contract-valid outputs (rules path; LLM stubbed).
2. **Offline continuity** — no network, no Neo4j, no cloud LLM required for workshop defence.
3. **Reproducible evidence** — hashes for fixtures, catalog version, adapter modes, packet JSON.

Aligned to [`SCQA.md`](SCQA.md) Answer: *offline-capable* orchestration.

---

## 2. Clean-room execution recipe

| Step | Action | Evidence |
|---|---|---|
| 1 | Clone repo; work only under `submission/` for mutable deliverables | Git commit hash in run manifest |
| 2 | Python 3.11+ venv; `pip install -e submission/` (or project `pyproject` as documented in task list) | Lockfile / hash **pending** full lock commit |
| 3 | Set offline env (see §3) | Env snapshot in audit (no secrets) |
| 4 | Run contract tests: `pytest submission/tests/contracts/` | JUnit/xml **pending** CI run |
| 5 | Run CLI workflow per PUB fixture id | stdout + emitted packet under `submission/evidence/` **when created** |
| 6 | Run eval graders per `32` | Grader report JSON **pending** Phase 7–9 |

**Do not** mutate challenge CSVs under immutable evidence policy; copy outputs to `submission/evidence/` only.

---

## 3. Environment profile: `AEGIS_OFFLINE=1`

| Variable (conceptual) | Offline value | Effect |
|---|---|---|
| `AEGIS_OFFLINE` | `1` | Force stub adapters in `composition.py` |
| `AEGIS_LLM_ENABLED` | `0` | `OfflineLlmStub` / rules-only |
| `AEGIS_GRAPH_MODE` | `memory` | `InMemoryGraphStub` |
| `AEGIS_TELEMETRY` | `console` | No OTLP exporter required |
| `NEO4J_URI` | unset | Neo4j adapter not loaded |

Live profile (demo only): explicit flags + network allow-list + budget caps (`20`, `33`).

---

## 4. Adapter parity matrix

| Port | Offline adapter | Live adapter | Parity test |
|---|---|---|---|
| `FixturePort` | CSV loader | HTTP read client (future) | Golden row counts per batch id |
| `GraphPort` | `InMemoryGraphStub` | `graph_neo4j.py` | `test_port_adapter_fakes.py` shape equality |
| `LlmPort` | Stub (empty or fixed) | Gateway | Schema validation only in offline |
| `AuthorityPort` | `knowledge_catalog.csv` | ECM API (future) | Trust state mapping |
| `AuditPort` | File/console emit | Archive API | Event schema version |

On parity failure → **block release** (`11` §6).

---

## 5. Reproducibility manifest (per run)

Each run SHOULD emit:

```json
{
  "run_id": "uuid",
  "idempotency_key": "client-supplied",
  "git_sha": "pending-local",
  "fixture_index_version": "PUBLIC_FIXTURE_INDEX.csv row hash pending",
  "knowledge_catalog_version": "from catalog metadata",
  "adapters": { "graph": "in_memory_stub", "llm": "offline" },
  "packet_sha256": "of canonical JSON",
  "timestamp_utc": "ISO-8601 with precision preserved"
}
```

Store under `submission/evidence/runs/<run_id>/manifest.json` when evidence folder exists.

---

## 6. CI / workshop gates

| Gate | Command / check | Status |
|---|---|---|
| G-REP-01 | Contract pytest offline | **Pending** recorded run |
| G-REP-02 | CLI batch packet for PUB-01 class | **Pending** |
| G-REP-03 | AI-disabled path same as stub default | Design locked |
| G-REP-04 | No network in offline job | CI config **pending** |

---

## 7. Failure modes

| Condition | Behaviour |
|---|---|
| Missing fixture file | Fail closed; abstain reason `FIXTURE_NOT_FOUND` |
| Catalog row untrusted for cited claim | NN-04; strip or abstain |
| Graph stub empty for focus id | Return empty subgraph + warning; do not invent nodes |
| LLM enabled but unreachable | Degrade to rules-only if policy allows; else abstain (`21`) |

---

## 8. Traceability

| REQ | Section |
|---|---|
| NN-06 | §2–§5 |
| XC-02 | §7 |
| BAT-01 | §2 step 5 |

*Implementation: `submission/src/aegis/cli.py`, `composition.py`, `adapters/graph_memory.py`.*
