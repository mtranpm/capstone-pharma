# Demo data overlays for AEGIS UI

| Field | Entry |
|---|---|
| Purpose | Rich, demo-ready UI datasets that **join** challenge `data/` and PUB fixtures |
| Rule | Do **not** overwrite `data/`, `evaluation/`, or `source_documents/` |
| Authority | Synthetic for UI storytelling; whenever a field conflicts with SoR CSV, **SoR wins** and UI must show the conflict |
| As-of | 2026-08-01T08:00:00Z (aligned to PUB authorized_context) |

## Join keys

| Demo file | Joins to challenge data |
|---|---|
| `live_cases.csv` | `batches.csv`, `icsr_cases.csv` / PUB PV ids, `shipments.csv`, `portfolio_products.csv` |
| `portfolio_pressure_board.csv` | `portfolio_products.csv`, `commercial_forecast.csv`, `demand_forecast.csv`, `board_requests.csv` |
| `twin_nodes.csv` / `twin_edges.csv` | `material_genealogy.csv`, `lab_results.csv`, `warehouse_movements.csv`, `temperature_loggers.csv`, `serialisation_events.csv` |
| `review_by_exception_queue.csv` | PUB-01 focus areas; `release_packets.csv`, `supplier_audits.csv` |
| `cross_impact_links.csv` | batch → shipment → inspection `IR-72H` |
| `obligation_register.csv` | artefact `26`, `ai_use_boundaries.csv`, `06` gates |
| `exclusivity_brief_outline.csv` | NCX-101 + INJ-004 |
| `patient_impact_sla.csv` | `demand_forecast.csv`, `allocation_constraints.csv`, NCS-310 / NCR-415 |
| `inspection_war_room_tasks.csv` | `inspection_requests.csv` (`IR-72H`) |

## Usage in app (future build)

Load challenge CSVs as system of record; load `submission/demo_data/*` as UI orchestration overlays (case state, twin layout, microcopy).
