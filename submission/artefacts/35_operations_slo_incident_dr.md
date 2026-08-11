# 35 — Operations, SLO, Incident & DR

| Field | Entry |
|---|---|
| Owner | Platform / SRE |
| Version / date | 1.0.0 / 2026-08-10 |
| Status | Phase 5 — ops framework |
| Sources | ADR-005, `21`, `06`, `24` |

---

## 1. Service tiers

| Tier | Function | SLO (pilot target) |
|---|---|---|
| API + review UI | Interactive packets | 99.5% monthly availability |
| CLI offline bundle | Continuity | Best-effort local |
| Neo4j advisory | Graph queries | 99.0% (degrade to stub) |
| LLM gateway | Optional assist | 99.0% (degrade to D1) |

---

## 2. SLO indicators

| SLI | Measurement |
|---|---|
| Availability | Successful health checks |
| Latency p95 | API workflow start → draft (excludes human review) |
| Error rate | 5xx + abstain rate |
| Audit completeness | % runs with full event chain |

---

## 3. Incident severity

| Sev | Example | Response |
|---|---|---|
| S1 | Prohibited action reached UI | ES + KS; exec notify |
| S2 | PHI in logs | DPO + rotate keys |
| S3 | Neo4j down | Auto stub |
| S4 | Elevated abstention | Data quality ticket |

---

## 4. DR

| Scenario | RTO | RPO | Playbook |
|---|---|---|---|
| Region loss | 4h | 1h audit | Offline bundle `16` |
| LLM vendor outage | 0 (instant) | n/a | D1 AI-disabled |
| Corrupt manifest | 1h | 0 | Rollback manifest version |

DR drill: **pending** production.

---

## 5. On-call runbook links

- Degraded modes: `21`
- Kill switches: `21` §3
- Red team post-incident: `31`

---

## 6. Traceability

XC-02, NN-06 continuity evidence.
