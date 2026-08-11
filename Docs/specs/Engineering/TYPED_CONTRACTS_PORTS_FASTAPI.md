# Typed Contracts, Ports & FastAPI — Engineering Spec

**Spec ID:** `aegis-typed-contracts-ports-fastapi`  
**Version:** `1.0.0`  
**Applies to:** `submission/**/*.py`

## 1. Purpose

Define mandatory engineering standards for the AEGIS Evidence Orchestrator: type hints, Pydantic v2 strict models, swappable ports/adapters, FastAPI OpenAPI surface, typed clients with retries, and contract tests.

## 2. Type hints

- All public functions and methods must have parameter and return annotations.
- Prefer `Protocol` for ports; avoid untyped `Any` except at intentional boundaries (e.g. raw JSON before validation).
- Style should be mypy/pyright friendly (`from __future__ import annotations` allowed).

## 3. Pydantic v2 strict contracts

Use Pydantic v2 for:

- Workflow API request/response models (aligned with `evaluation/contracts/*.schema.json`)
- LLM I/O envelopes
- Tool / function-calling argument models
- Typed error models returned by API and application services

Required model config:

```python
from pydantic import BaseModel, ConfigDict

class StrictModel(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")
```

Rules:

- `extra="forbid"` on all external-facing models.
- Do not silently coerce units, identifiers, or timestamps.
- Validate tool/function-calling args with Pydantic **before** execution; on failure return a typed error (never a bare string as the sole contract).

## 4. Ports & adapters

Domain/application code depends on **ports** (`typing.Protocol`), not concrete SDKs.

Minimum ports:

| Port | Responsibility |
|---|---|
| `FixturePort` / data loader | Load public fixtures and CSV evidence (read-only) |
| `AuthorityPort` | Knowledge document status, effective date, trust |
| `GraphPort` | Ontology/KG queries (Neo4j or in-memory stub) |
| `LlmPort` | Optional inference; offline stub default |
| `AuditPort` | Persist audit/evidence export events |
| `TelemetryPort` | Traces/metrics/logs (OpenTelemetry) |
| `ToolManifestPort` | Approved vs poisoned tool manifest checks |

Composition root (`composition.py`) wires adapters. Domain must not import FastAPI, Neo4j driver, or OpenTelemetry SDK directly.

## 5. FastAPI service

- Expose OpenAPI at `/docs` and `/openapi.json`.
- Route handlers: parse → call application service → map typed errors.
- No business logic in routers beyond validation and error mapping.
- Health: `GET /health`.
- Workflow routes under `/v1/workflows/{batch|pv|supply}`.
- Ontology/graph under `/v1/ontology`, `/v1/graph` (parameterized, allow-listed queries only).

## 6. Typed clients

- HTTP clients (e.g. httpx) validate responses with the same Pydantic models.
- Retries: exponential backoff + jitter; bounded max attempts.
- Do not retry non-idempotent side effects (advisory APIs remain read/reconcile).
- Propagate correlation ids (`request_id`, `trace_id`) when present.

## 7. Typed errors

Canonical error model fields (minimum):

- `code` (stable string enum)
- `message` (safe for operators; no secrets)
- `details` (structured, optional)
- `request_id` (optional)
- `retryable` (bool)

Map validation failures, auth denials, prohibited actions, and abstentions to distinct codes.

## 8. Contract tests (pin)

Under `submission/tests/contracts/`:

- Pydantic models ↔ evaluation JSON Schema alignment
- OpenAPI request/response shapes
- Port fakes vs adapters for golden fixtures
- Tool-arg validation failures → typed errors
- Telemetry redaction (no PII/secrets in attributes)

## 9. Offline / challenge path

- CLI must run workflows and evaluation without React or Neo4j (use `InMemoryGraphStub`).
- Challenge `data/`, `knowledge/`, `evaluation/` remain read-only.

## 10. Related specs

- `Docs/specs/Engineering/OPENTELEMETRY_TELEMETRY.md`
- `Docs/specs/Security/OWASP_LLM_TOP10_THREAT_CONTROLS.md`
- `Docs/Regulations/iso_42001_eu_ai_act.md`
