# 05 — Product Operating Model

| Field | Entry |
|---|---|
| Owner | Product / value lead |
| Version | 0.1.0 |
| Status | Phase 3 — draft for review |
| Sources | `SCQA.md`, `01`–`04`, `03`, A1/A11, `data/ai_use_boundaries.csv` |

## 1. Product intent

**AEGIS Evidence Orchestrator** is the advisory product surface for NovaCura’s three locked workflows (Batch, PV, Supply). It packages conflict-visible, provenance-backed evidence for human review — aligned to the Answer in [`SCQA.md`](SCQA.md).

| Principle | Operating rule |
|---|---|
| Advisory-only | Outputs are drafts, checklists, and packets — never regulated decisions |
| Fail-closed | Unresolved identity, unit, time, terminology, jurisdiction, or authority → abstain |
| SoR read-only | Fixture CSVs and signed knowledge are sources; AEGIS does not write back to MES/LIMS/QMS/PV DB |
| Offline-capable | CLI + `InMemoryGraphStub` + AI-disabled path must complete PUB evaluation |

## 2. Personas & jobs-to-be-done (JTBD)

| Persona | Primary JTBD | Success signal | AEGIS touchpoints |
|---|---|---|---|
| **EU Qualified Person / Quality release reviewer** | Decide batch certification with complete, defensible evidence | Genealogy, OOS/OOT, supplier audit gaps visible before review meeting | Batch readiness packet, conflict register, authority citations |
| **PV case intake coordinator** | Triage incoming reports without losing clocks or duplicates | Duplicate candidates and awareness-date conflicts surfaced with sources | PV intake packet, multilingual narrative preserved |
| **PV medical reviewer** (downstream) | Final seriousness/causality/reportability | Receives prepared evidence — **not** AI final calls | Export for human systems only |
| **Supply planner** | Option cold-chain/shortage recovery under constraints | Non-executing options with constraint evidence | Supply options packet (no allocation controls) |
| **Quality release / supplier-quality** | Gate supplier evidence in release packet | Unverified audit commitments flagged | Batch + supplier cross-links |
| **Regulatory Affairs** | Inspection/submission packaging in 72h window | Traceable manifest, no silent merges | Audit export, document authority states |
| **CISO / platform** | Detect poisoned tools and maintain continuity | Blocked prohibited actions; degraded mode works | Security fixtures PUB-09, offline PUB-10 |
| **DPO** | Lawful purpose on retrieval | Minimised logs; purpose binding | Privacy flags on export |
| **Manufacturing VP** | Throughput visibility | Hold reasons visible — not bypass of Quality | Read-only batch status from SoR |
| **Patient safety representative** | Contestability & plain language | Can challenge packet rationale | Human oversight artefact `06` |

## 3. In scope / out of scope

| In scope (product) | Out of scope (explicit non-goals) |
|---|---|
| Batch / PV / Supply evidence orchestration for PUB-01..15 | Autonomous batch disposition, QP certification, release/reject/reprocess/recall |
| Contract-valid JSON packets + React human review UI | Final PV seriousness, causality, expectedness, reportability, signal confirmation |
| Authority gates, abstention, audit emit | Stock reservation, allocation, shipment, inventory quality-status change |
| Neo4j **advisory** graph via `GraphPort`; offline stub | Clinical eligibility decisions |
| Multilingual **preservation** (not silent translation that changes meaning) | Live SoR write-back or ERP execution |
| Change management & a11y baselines for review UI | Patent-cliff strategy, full PQS redesign, vendor replacement of Quality systems |

## 4. Operating cadence

| Cadence | Activity | Participants | Artefacts |
|---|---|---|---|
| **Per run** | Operator starts workflow with purpose, object id, idempotency key | Workflow owner | Audit event, packet draft |
| **Per packet** | Mandatory human review gate before export/share | Accountable role per `03` | Sign-off record (human), not AI |
| **Daily** (ops) | Monitor abstention rate, prohibited-action blocks, offline health | Platform + workflow owners | Telemetry dashboards (no raw PV narrative in spans) |
| **Weekly** | Inject/fixture regression + contract tests | QA evidence lead | `13`, evaluation graders |
| **Incident** | Emergency stop → AI-disabled continuity | CISO + Quality + Platform | `06`, `21` |
| **Release train** | Model/tool/catalog change via change control | Quality + RA + DPO | `07`, knowledge catalog version |

## 5. Advisory vs regulated decisions

| Decision class | AEGIS may | AEGIS must not | Accountable human |
|---|---|---|---|
| Evidence completeness / conflicts | Propose `ready_for_human_review`, `insufficient`, `conflicted` | Imply release-ready or QP certification | QP / Quality release |
| Unit / genealogy / authority | Flag gaps; cite verbatim SoR values | Silently convert units or repair genealogy | Lab / MDM / Quality |
| PV intake support | List duplicate candidates, clock reconstruction **evidence** | Set reporting clock or confirm duplicate | PV intake → medical reviewer |
| Supply recovery | Generate **options** with constraints cited | Execute allocation or ship | Supply planning + Quality gates |
| Knowledge use | Apply `AuthorityPort` / catalog trust | Treat untrusted/superseded as policy authority | Quality / RA |

Regulated pen stays with roles defined in [`03_stakeholders_decision_rights.md`](03_stakeholders_decision_rights.md) and DDD A11.

## 6. Workflow operating model (summary)

```text
Trigger (batch id / case id / shipment focus)
  → Authorize user + purpose + object
  → Load SoR fixtures (read-only) + authority classify
  → Reconcile (rules first; optional LLM behind port)
  → GraphPort advisory subgraph (never authoritative over SoR)
  → Human review gate (React)
  → Export audit + packet OR abstain with reason codes
```

## 7. Metrics (product, not compliance sign-off)

| Metric | Use | Guardrail |
|---|---|---|
| Time-to-review-packet | Board 14% pressure (`A-004`) | Must not reduce conflict visibility |
| Abstention rate | Quality of gates | Rising abstention preferred over silent wrong answers |
| Human review completion | Governance | 100% before external export |
| Offline pass rate | Continuity | Required for defence |
| Prohibited-action blocks | Safety | Expected under red-team |

## 8. Links

- Requirements: [`13_requirements_traceability_matrix.md`](13_requirements_traceability_matrix.md)  
- Data contracts: [`09_data_governance_lineage_contracts.md`](09_data_governance_lineage_contracts.md)  
- Human gates: [`06_human_oversight_and_emergency_stop.md`](06_human_oversight_and_emergency_stop.md)
