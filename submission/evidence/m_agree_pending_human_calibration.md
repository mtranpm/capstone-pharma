# M-AGREE — Pending human calibration

| Field | Entry |
|---|---|
| Status | `pending_human_calibration` |
| Date | 2026-08-10 |
| Soft threshold | κ ≥ 0.6 (advisory indicator only — **not** a safety hard gate) |
| Metrics when labels exist | Cohen’s κ, linear weighted κ (ordinal), Gwet AC1 |
| Implementation | `submission/evaluation/metrics/agreement.py` |
| Wired into | `scripts/evaluate_public_fixtures.py` → `evidence/evaluation_results.json` |

## What is intentionally not claimed

- **No fabricated κ / AC1 numbers.** Dual-annotated human vs system labels for advisory fields (e.g. `conflict_present`, `abstention_reason_class`) have not been collected for this workshop slice.
- EVAL-03 in artefact `32` remains **Pending** until a labelled sample (target n≥30 per workflow) is available.
- Safety gates continue to use deterministic G-* graders only (`G-SCHEMA`, `G-EXEC-BOUNDARY`, boundaries, etc.).

## How to close (human step)

1. Sample advisory packets from PUB / inject register.
2. Two qualified reviewers label agreed fields independently.
3. Export paired labels (CSV/JSON) and pass to `compute_agreement(human, system)`.
4. Record κ / AC1 + 95% CI bootstrap in `evaluation_results.json`; update artefact `32` EVAL-03.
5. If κ < 0.6 → investigate per `25` / `27` RR-04 — do **not** auto-release or change disposition behaviour.
