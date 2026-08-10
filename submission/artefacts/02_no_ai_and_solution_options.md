# 02 — No-AI and Solution Options Comparison

| Field | Entry |
|---|---|
| Owner | Product / value lead |
| Version | 0.1.0 |
| Status | Draft |
| Sources | `data/no_ai_baselines.csv`, INJ-003, A1 framing, `case/STAKEHOLDER_PACK.md` |

## 1. Options considered

| Option | Description | Pros | Cons |
|---|---|---|---|
| **A. No-AI process redesign** | SOP redesign, more reviewers, longer hold times, manual checklists | Clear accountability; no model risk | Does not meet board cycle-time target; unsustainable under converging injects |
| **B. Rules / deterministic reconciliation only** | Schemas, authority tables, unit/identity rules, no LLM | Offline, testable, fail-closed friendly | Weak on multilingual narrative and soft clustering; still needs UI/orchestration |
| **C. Analytics / dashboards only** | BI over CSVs without governed abstention | Fast visibility | Silent merges/unit conversion risk; weak provenance for inspection |
| **D. Buy/partner enterprise AI** | Vendor bundle | Speed to feature | Concentration, weak exit (Procurement vs CISO conflict), offline reproducibility hard |
| **E. Selected — advisory orchestration (hybrid)** | Deterministic core + optional LLM behind port; React review; Neo4j advisory KG | Matches non-negotiables; offline path; contract tests | Build effort; must resist over-automation |

## 2. Honest no-AI comparison

A pure no-AI path can preserve Quality independence but **fails the measurable board constraint** (14% lead-time reduction) under the documented concurrent Batch/PV/Supply/cyber/inspection pressures without unsustainable headcount. Therefore AI is justified **only** as advisory acceleration with fail-closed boundaries — not as decision replacement.

Evidence anchors: INJ-003 (`no_ai_baselines.csv`), INJ-006 (`ai_use_boundaries.csv`), stakeholder conflicts (Quality vs Manufacturing speed/completeness).

## 3. Selected intervention

**E — AEGIS Evidence Orchestrator:** rules/deterministic baseline first; LLM optional and swappable; prohibited actions blocked; human review mandatory for regulated decisions.

## 4. Stop / pivot criteria

| Condition | Action |
|---|---|
| System produces disposition-like outputs | Stop release; redesign / remove capability |
| Untrusted knowledge used as authority | Pivot to stronger authority gate; red-team |
| Offline/AI-disabled path unavailable | No-go for defence |
| No-AI checklist outperforms AI packets on fidelity | Pivot toward rules-only |
| Vendor lock-in without exit | Prefer build path (already selected) |
