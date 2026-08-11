# OPERATIONS

Day-2 operations for AEGIS Evidence Orchestrator (advisory only).

## Health
- API: `GET /health`
- CLI: `python -m aegis.cli health` (`PYTHONPATH=submission/src`)

## Routine runs
- Assemble packets: `python -m aegis.cli run PUB-01`
- Evaluate: see `EVALUATE.md`
- UI review: start API + `npm run dev` in `submission/app`

## Telemetry
- Offline console spans by default; correlate `trace_id` with audit `event_id`.
- Do not log raw PV/clinical narratives in attributes.

## Neo4j (optional)
- Default offline stub. Enable only with local env vars — never commit secrets.
- Reload: `python submission/scripts/load_graph.py` (dry-run) / `--apply` when configured.
