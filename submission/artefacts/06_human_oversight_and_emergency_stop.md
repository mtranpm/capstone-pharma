# 06 — Human Oversight & Emergency Stop

| Field | Entry |
|---|---|
| Owner | Domain / governance lead |
| Version | 0.1.0 |
| Status | Phase 3 — draft for review |
| Sources | `03`, DDD A11, `data/ai_use_boundaries.csv`, `knowledge/K-001` (budget/stop), Engineering typed contracts |

## 1. Purpose

Define **when humans must intervene**, how **emergency stop** works, and how **contestability** is preserved — without AEGIS ever owning regulated decisions (NN-01..03 in `13`).

## 2. Human review gates (mandatory)

| Gate | Trigger | Reviewer (minimum role) | Pass criteria | Fail / block |
|---|---|---|---|---|
| **G-HR-01 Pre-export packet** | Any workflow packet leaves draft state | Batch: QP delegate; PV: case intake lead; Supply: supply planner | Conflicts acknowledged; citations present; no prohibited fields | Block export; remain draft |
| **G-HR-02 Authority unresolved** | `AuthorityPort` returns pending/untrusted for material claim | Quality or RA delegate | Human accepts risk **or** removes claim from packet | Abstain; no export |
| **G-HR-03 Abstention override** | Operator requests continue despite abstention reason | Workflow owner + Quality | Written override reason; audit event | Default deny |
| **G-HR-04 High-risk inject class** | Security poisoned tool / injection (PUB-09) | CISO delegate | Tool quarantined; no regulated action attempted | Hard stop |
| **G-HR-05 Multilingual PV narrative** | Non-English verbatim in case | PV intake (+ DPO if restricted segments) | Meaning preserved; no silent “correction” | Block if model altered narrative |
| **G-HR-06 Supply option review** | Any supply recovery option list | Supply planning + Quality (status constraints) | Options labelled non-executing | Block if UI implies shipment/allocation |

**Implementation note:** FastAPI returns draft packets; React exposes **Review & Export** only after checklist completion. No API route performs disposition.

## 3. Emergency stop (kill switch)

| Control | Scope | Effect | Recovery |
|---|---|---|---|
| **ES-01 Global AI disable** | LLM port + agent loops | Deterministic rules-only or full AI-disabled continuity (`K-002`) | Quality + Platform approve re-enable |
| **ES-02 Workflow halt** | Single workflow type | In-flight runs checkpoint; no new starts | Owner clears after root-cause |
| **ES-03 Tool manifest revoke** | Poisoned or stale manifest | `ToolManifestPort` deny-all for tool | CISO updates approved manifest |
| **ES-04 Budget exhaustion** | Agent step/token budget (`K-001`) | Fail-closed; partial packet with abstention | Increase budget only via change control |
| **ES-05 User/session revoke** | Stale role or entitlement | Deny by default at execution time | IAM refresh |

Emergency stop is **not** a substitute for QP/PV/Supply decisions — it stops **automation and advisory generation** until humans confirm safe posture.

## 4. Contestability

| Stakeholder | Mechanism | Evidence required |
|---|---|---|
| Patient safety representative | Challenge packet rationale in safety governance forum | Linked audit trail, source hashes, abstention codes |
| Quality / QP | Reject AI draft without using AI output | Human decision recorded in QMS (outside AEGIS SoR) |
| PV medical reviewer | Discard intake suggestions | Duplicate/clock evidence retained for inspection |
| Any authorized user | Flag “disputed citation” on a line item | Creates audit event; does not auto-correct SoR |

Contestability requires **visible conflicts** (e.g., SUA-88 genealogy break, mg/L vs µg/mL) — never hidden normalization.

## 5. Roles & RACI (AEGIS-specific)

| Activity | R | A | C | I |
|---|---|---|---|---|
| Configure workflow budgets/checkpoints | Platform | CISO | Quality | RA |
| Approve knowledge catalog for gates | Quality | CQO | RA, DPO | Platform |
| Operate human review UI | Workflow owner | Domain head (`03`) | QA evidence | Manufacturing |
| Invoke emergency stop | CISO, Platform, Quality delegate | CQO / CISO (incident) | DPO | Supply, PV |
| Audit export for inspection | Regulatory | RA VP | Quality, PV, Supply | Board |

## 6. Alignment with agent design

From bounded agent responsibilities (DDD A10 pattern):

- Agents may **prepare** reconciliation packages and conflict lists.  
- Agents must **never own** release, PV final assessment, allocation, or recall initiation (A11).  
- Checkpoints persist run state; resume requires current authorization re-check.

## 7. Acceptance tests (trace)

| Test intent | REQ / fixture |
|---|---|
| Export blocked without human gate | BAT/PV/SUP + UI contract |
| Prohibited action → typed error | NN-01..03, PUB fixtures |
| ES-01 offline path completes | NN-06, PUB-10 |
| Override requires audit | `24` (future), audit port emit |

## 8. Links

- Decision rights: [`03_stakeholders_decision_rights.md`](03_stakeholders_decision_rights.md)  
- Degraded mode detail: artefact `21` (Phase 5)  
- Agent budgets: artefact `20`, `K-001`
