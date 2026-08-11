# RUN

## API
`python submission/scripts/run_app.py`

## CLI (no UI/Neo4j required)
```text
python -m aegis.cli health
python -m aegis.cli run PUB-01
```
Set `PYTHONPATH=submission/src` (or run via module from that path).

## AI-disabled
`$env:AEGIS_AI_DISABLED="1"` then re-run CLI — deterministic path only.

## UI
Start API, then `npm run dev` in `submission/app`.
