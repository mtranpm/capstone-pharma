# OpenTelemetry Telemetry — Engineering Spec

**Spec ID:** `aegis-opentelemetry-telemetry`  
**Version:** `1.0.0`

## 1. Purpose

Instrument AEGIS CLI, FastAPI, workflow runs, authority checks, LLM/tool calls, graph queries, and graders with OpenTelemetry (OTel) while preserving offline operation and privacy.

## 2. Signals

| Signal | Use |
|---|---|
| Traces | One root span per workflow/API request; child spans for load, authority, reason, validate, export, graph, LLM |
| Metrics | Counters/histograms for requests, retries, tokens/steps, latency, grader pass/fail, budget stops |
| Logs | Correlate with `trace_id`; prefer structured fields |

## 3. Port & adapters

- Domain uses `TelemetryPort` only.
- Adapters: console/file exporter (default offline), optional OTLP exporter.
- Composition selects adapter via config/env; default must not require a remote collector.

## 4. Required span attributes (allow-list)

Allowed examples: `request_id`, `workflow`, `fixture_id`, `batch_id`/`case_id` (IDs only), `execution_status`, `human_review.required`, `authority.decision`, `retry.attempt`, `token.count`, `sha256` (hashes), `trace_id` linkage to audit `event_id`.

## 5. Forbidden attributes

Never put in spans/metrics/logs attributes:

- Raw adverse-event narratives, pregnancy/paediatric free text
- Secrets, API keys, passwords, connection strings
- Full prompts/system prompts
- Unredacted personal data beyond synthetic IDs already in fixtures

Redaction helpers must strip/deny unknown sensitive keys (`test_otel_redaction.py`).

## 6. Correlation

- Propagate W3C trace context on HTTP where applicable.
- Persist `trace_id` (and optionally `span_id`) on audit export records.
- Graders may assert presence of required spans and absence of forbidden keys (`G-OTEL`).

## 7. Offline continuity

- AI-disabled / CLI evaluation path still emits local telemetry (or no-op port) without network.
- Telemetry failure must not break advisory workflow success path (fail-open for telemetry, fail-closed for safety controls).

## 8. Related

- Artefact `35` SLOs/ops; FinOps graders `G-FINOPS`
- `Docs/specs/Engineering/TYPED_CONTRACTS_PORTS_FASTAPI.md`
