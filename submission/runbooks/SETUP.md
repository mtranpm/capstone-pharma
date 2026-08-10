# SETUP

1. Python 3.11+ recommended. From repo root:
   - `pip install -r submission/requirements.txt`
2. Offline default: do **not** set `AEGIS_USE_NEO4J`. Graph uses `InMemoryGraphStub`.
3. Optional Neo4j (local only): Desktop/Docker; set `NEO4J_URI`, `NEO4J_USER`, `NEO4J_PASSWORD` via environment — **never commit secrets**.
   - Seed advisory projection: `AEGIS_USE_NEO4J=1 python submission/scripts/load_graph.py --apply`
   - Adapter degrades to `mode=neo4j_unavailable` if the server is down; CLI/eval stay on the in-memory stub.
4. Optional UI (`submission/app`):
   - Requires **Node.js 18+** and npm.
   - `cd submission/app; npm install; npm run build` (PowerShell) or `npm install && npm run build` (bash).
   - Verified on this host (2026-08-10): Node v24.18.0 / npm 11.16.0 — `npm install` + `vite build` succeeded. `node_modules/` is gitignored; reinstall before demo.
   - If Node/npm is not installed, challenge CLI/eval still pass without the React app.
5. OTel: console/file offline by default; OTLP optional later. `G-OTEL` checks audit↔trace correlation on packets (no collector required).
