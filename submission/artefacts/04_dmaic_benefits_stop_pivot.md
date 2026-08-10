# 04 — DMAIC Benefits & Stop/Pivot Criteria

| Field | Entry |
|---|---|
| Owner | Value / measurement lead |
| Version | 0.1.0 |
| Status | Draft |
| Sources | A1 framing, INJ-003 baselines, PUB-01..15, workshop DoD |

## 1. DMAIC framing

| Phase | Focus for AEGIS |
|---|---|
| **Define** | Advisory orchestration for Batch / PV / Supply under concurrent injects; non-negotiables locked |
| **Measure** | Baseline cycle times, silent-merge risk, evidence completeness, abstention correctness |
| **Analyze** | Root causes: fragmented SoRs, unit/identity traps, authority lag, incentive conflicts |
| **Improve** | Deterministic contracts + fail-closed ports + human review UI + offline continuity |
| **Control** | Graders G-*, audit export, hash verification, stop/pivot gates, AI-disabled path |

## 2. Benefit hypotheses (measurable)

| Benefit | Baseline signal | Target direction | Measurement |
|---|---|---|---|
| Lead-time reduction support | Board 14% ask; no-AI baselines in CSV | Advisory packets reduce rework / waiting | Time-to-review-ready packet (demo clock) |
| Contradiction detection | Silent merges historically risky | Explicit conflicts surfaced | Graders + fixture expected abstentions |
| Inspection readiness | Fragmented evidence | Exportable audit + lineage | Hash/structure gates |
| Safety clock visibility | Multilingual / late narrative risk | Clock + duplicate candidates | PV fixture graders |
| Continuity | AI outage inject | Offline path works | AI-disabled run |

## 3. Stop criteria (hard)

| ID | Condition | Immediate action |
|---|---|---|
| STOP-01 | Autonomous disposition / PV final / ship / recall / quality-status change implemented | Remove capability; fail Gate |
| STOP-02 | Untrusted content treated as authority without verification | Quarantine; fail authority tests |
| STOP-03 | Offline / AI-disabled path broken | No-go defence; restore stub path |
| STOP-04 | Contract / grader regression on regulated fidelity | Block release of package |
| STOP-05 | Secrets or raw PHI/PII in logs/exports | Incident; scrub; fix telemetry |

## 4. Pivot criteria

| ID | Condition | Pivot |
|---|---|---|
| PIV-01 | LLM adds no graded value vs rules-only | Keep LLM port stubbed; ship rules-first |
| PIV-02 | Neo4j unavailable / over-trusted | Stay on `InMemoryGraphStub`; KG remains advisory |
| PIV-03 | Vendor concentration reintroduced | Refuse; document exit in FinOps artefact |
| PIV-04 | UI implies execute regulated action | Redesign UI to review-only |

## 5. Control plan linkage

Phase 9–10: eval harness, evidence export, clean-room scripts, defence package artefact `37`.
