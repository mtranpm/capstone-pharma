# 19 — AI Context & Tool Design

| Field | Entry |
|---|---|
| Owner | Architecture / security |
| Version / date | 1.0.0 / 2026-08-10 |
| Status | Phase 5 — governed context & tools |
| Sources | ADR-007, ADR-011, `12`, `09`, OWASP LLM spec, [`SCQA.md`](SCQA.md) |

---

## 1. Design principles

| Principle | Implementation |
|---|---|
| **Untrusted until verified** | Retrieved docs, tool descriptions, prior model turns, and user paste are **data** — not instructions |
| **Governed retrieval** | Only catalogued sources with authority state; no open web in regulated paths |
| **Minimal context** | Purpose-bound slices; redact PHI from telemetry (`05`, `30`) |
| **Structured out** | JSON schema / Pydantic at boundary; no free-text regulated decisions |
| **Tools are contracts** | Manifest version, arg schema, call budget, side-effect class |

---

## 2. RAG stance (explicit)

**AEGIS does not operate “open RAG.”** Retrieval is **governed**:

| Layer | Rule |
|---|---|
| Corpus | `knowledge/` + signed source documents; statuses from `AuthorityPort` |
| Query | Workflow-scoped; parameters validated; no arbitrary SQL/Cypher from LLM |
| Ranking | Deterministic tie-break (version date, authority rank) — model rerank optional and logged |
| Injection defence | Chunk metadata includes hash; mismatch → discard (LLM01) |
| Citation | Packets cite document id + hash + authority state; untrusted → NN-04 |

Vector search, if added, is an **index over governed corpus** — not a SoR (ADR-009).

---

## 3. Context assembly pipeline

```text
Authorize(purpose, object, role)
  → Select workflow template (Batch/PV/Supply)
  → Load SoR facts via FixturePort (verbatim fields)
  → Authority classify each document claim
  → Optional: GraphPort subgraph (advisory: true)
  → Optional: LlmPort with frozen tool list + schema
  → Validate output → human review gate
```

**Context budget:** token ceiling per stage (`20`, `33`); truncate with explicit `context_truncated` flag — never silent drop of conflict evidence.

---

## 4. Tool design

| Tool class | Example | Side effects | Allowed |
|---|---|---|---|
| **Read** | `get_batch_facts`, `query_subgraph` | None | Yes |
| **Search** | `search_knowledge` | None | Yes, governed corpus only |
| **Transform** | `format_packet_draft` | None | Yes, schema-bound |
| **Write / execute** | disposition, ship, PV submit | Regulated | **Denied** (NN-01..03) |

Tool descriptor fields (manifest):

- `tool_id`, `version`, `json_schema`, `max_calls_per_run`, `risk_tier`, `prohibited_regulated_action: bool`

Runtime checks: manifest signature (when keys available), user role, purpose binding (`29`).

---

## 5. Prompt & instruction hygiene

| Control | Detail |
|---|---|
| System policy | Fixed; not overridable by retrieved text |
| User content | Treated as untrusted data |
| Tool return | Parsed as JSON; schema validate before model re-ingest |
| No credential passthrough | Tools cannot accept secrets in args |

---

## 6. Failure / abstention

| Signal | Action |
|---|---|
| Retrieval hit untrusted/superseded | Exclude from authority claims; flag in packet |
| Tool schema fail | Do not invoke; log `TOOL_SCHEMA_REJECT` |
| Model proposes prohibited action | `domain/prohibited.py` guard → block |
| Ambiguous unit/time | NN-05 abstain |

---

## 7. Traceability

| REQ | Section |
|---|---|
| NN-04 | §2 |
| XC-01, XC-05 | §4 |
| PV-02 | §2, §6 |

*Code: `domain/tools.py`, `adapters/tool_manifest.py`, `domain/prohibited.py`.*
