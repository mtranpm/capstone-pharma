# 03 — Stakeholders & Decision Rights

| Field | Entry |
|---|---|
| Owner | Domain / governance lead |
| Version | 0.1.0 |
| Status | Draft |
| Sources | `case/STAKEHOLDER_PACK.md`, `data/decision_rights.csv`, A1 §5, Docs/DDD-Lab A11 |

## 1. Stakeholder map (summary)

| Stakeholder | Mandate | Decision authority (regulated) | AI may support |
|---|---|---|---|
| Chief Quality Officer | PQS / inspection readiness | Quality-system policy, risk acceptance | Evidence packets, gap registers |
| EU Qualified Person | EU batch certification | **Final certification / disposition — human only** | Readiness evidence, contradictions |
| Global Head of PV | Safety system performance | **Final seriousness/causality/expectedness/reportability/signal — human only** | Intake support, duplicates, clocks |
| Supply Chain VP | Service continuity | Planning; **allocation/ship/recall need approvals** | Non-executing options + constraints |
| Regulatory Affairs VP | Registrations / labelling | Submission strategy | Applicability framing (not legal conclusions) |
| DPO | Lawful processing | Privacy risk acceptance | Purpose checks, minimisation flags |
| CISO | Cyber / resilience | Security controls, IR | Poisoned-tool / injection detection |
| Manufacturing VP | Throughput | Operations — **not** independent release | Hold/evidence visibility |
| Patient Safety Representative | Contestability | Advisory through safety governance | Plain-language explanations |
| Procurement | Vendor terms | Contracting with control owners | Exit/cost evidence |

## 2. Decision rights for AEGIS outputs

| Output | AI role | Accountable human | Escalation |
|---|---|---|---|
| Batch readiness state | Propose conflicted/insufficient/ready_for_human_review | Quality release / QP | CQQ / QP |
| PV intake packet | Propose duplicates/clocks/listedness evidence | PV case intake → medical reviewer | Global Head PV |
| Supply options | Propose non-executing options | Supply planning + Quality approval gates | Supply Chain VP |
| Authority abstention | Mandatory when unresolved | Workflow owner | Policy owner |
| Prohibited action attempt | **Block** | N/A — system deny | Security / Quality |

## 3. Conflicts & incentives

- Quality vs Manufacturing: completeness vs speed (INJ-002).
- Privacy minimisation vs GxP preservation.
- Procurement bundled vendor vs Architecture/CISO substitutability.
- Global standardisation vs local jurisdictional accountability.

## 4. Escalation principles

1. Unresolved identity/unit/time/authority → abstain; escalate to object owner.  
2. Untrusted document/tool → quarantine; CISO/Quality notified via audit event.  
3. Inspection request → Regulatory + Quality own package; AI only assembles evidence trail.  
4. Emergency stop / contestability → human oversight artefact `06` (Phase 3).
