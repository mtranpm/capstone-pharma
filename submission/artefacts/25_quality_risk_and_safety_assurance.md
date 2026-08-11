# 25 — Quality Risk & Safety Assurance

| Field | Entry |
|---|---|
| Owner | Quality / Patient safety |
| Version / date | 1.0.0 / 2026-08-10 |
| Status | Phase 5 — QRM summary |
| Sources | ICH Q9 principles, `04`, `06`, NN rows, [`SCQA.md`](SCQA.md) |

---

## 1. Scope

Quality risk management for **advisory evidence orchestration** — hazards where AI or integration errors could **mislead** humans or **bypass** controls, not where AEGIS autonomously harms patients (prohibited by design).

---

## 2. Hazard inventory (selected)

| HZ-ID | Hazard | Cause | Harm | Severity | Likelihood | Initial risk |
|---|---|---|---|---|---|---|
| HZ-01 | False “ready” impression | Overconfident LLM text | Delayed batch hold | Major | Low | Medium |
| HZ-02 | Silent unit change | Bad adapter | Wrong QP decision | Critical | Low | Medium |
| HZ-03 | Untrusted SOP cited as policy | NN-04 fail | Non-compliant release | Major | Medium | **High** |
| HZ-04 | Genealogy break missed | Incomplete join | Contaminated lineage undetected | Critical | Low | Medium |
| HZ-05 | PV narrative altered | Translation “fix” | Mis-triage | Major | Low | Medium |
| HZ-06 | Execute ship via UI | Excessive agency | Wrong shipment | Critical | Very low | Low |
| HZ-07 | Audit gap | Missing events | Inspection finding | Major | Medium | Medium |
| HZ-08 | Offline path fails | Config error | Ops paralysis in outage | Minor | Medium | Medium |

---

## 3. Controls (summary)

| HZ | Control | REQ / artefact |
|---|---|---|
| HZ-01 | Status = draft; no “approved batch”; G-HR-01 | NN-01, `06` |
| HZ-02 | Verbatim fields; abstain on unit conflict | BAT-02, NN-05 |
| HZ-03 | AuthorityPort + catalog | NN-04, `12` |
| HZ-04 | Genealogy inject tests; graph advisory labels | BAT-03 |
| HZ-05 | G-HR-05 multilingual preserve | PV-02 |
| HZ-06 | No execute controls; prohibited guard | NN-03, D-004 |
| HZ-07 | Audit event schema `24` | OQ pending |
| HZ-08 | NN-06 offline CLI | `16`, `21` |

---

## 4. Residual risk acceptance

Residual risks documented in `27` with owners. **No autonomous regulated actions** — primary mitigation for catastrophic patient harm pathways.

---

## 5. Safety monitoring

| Signal | Threshold (indicative) | Action |
|---|---|---|
| Abstention rate spike | >2× baseline | Data quality / authority review |
| Prohibited-action block | Any | Mandatory incident review |
| Human override G-HR-03 | Any | QA monthly review |
| TEVV κ drop below soft 0.6 | Advisory fields | Model rollback candidate (`32`) |

---

## 6. Traceability

Links to assurance claims in `27` and tests in `32`, `28`.
