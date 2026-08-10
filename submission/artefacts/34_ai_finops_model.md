# 34 — AI FinOps Model

| Field | Entry |
|---|---|
| Owner | FinOps / Procurement |
| Version / date | 1.0.0 / 2026-08-10 |
| Status | Phase 5 — cost governance |
| Sources | `33`, XC-06, `36`, PUB-14 |

---

## 1. Cost components

| Component | Cost driver | Owner |
|---|---|---|
| LLM inference | Tokens, model tier | Platform |
| Embeddings (optional) | Index size, query volume | Data |
| Neo4j (optional) | Cluster size | Platform |
| Egress / API calls | SoR read volume | Integration |
| Human review | FTE (dominant in GxP) | Operations |

---

## 2. Unit economics (illustrative — workshop)

| Unit | Formula | Note |
|---|---|---|
| Cost per advisory run | Σ(token_price × tokens) + amortized infra | Stub run ≈ $0 |
| Cost per exported packet | Run cost / exports after G-HR | Human cost excluded |
| Waste ratio | Aborted runs / total | Budget stops |

**Do not cite dollar figures in defence without measured runs** — mark **pending** in `37`.

---

## 3. Budget & chargeback

| Control | Implementation |
|---|---|
| Hard cap per run | API enforces `20` |
| Monthly envelope | Procurement alert at 80% |
| Chargeback tags | cost_center, workflow, site |
| Refuse unbounded | XC-06 — deny if no budget id |

---

## 4. Vendor comparison (template)

| Vendor | Model | $/1M in | $/1M out | Residency | Exit notes |
|---|---|---|---|---|---|
| TBD | TBD | — | — | — | `36` |

Fill after vendor selection; workshop uses stub.

---

## 5. FinOps KPIs

| KPI | Target (indicative) |
|---|---|
| Budget stop rate | <5% of runs |
| Cost per PUB fixture eval | Tracked |
| LLM cost % of total AEGIS opex | <30% pilot |

---

## 6. Traceability

XC-06, EVAL cost gates optional in CI.
