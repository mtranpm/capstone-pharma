# AEGIS — Executive Summary (portfolio-framed)

| Field | Entry |
|---|---|
| Owner | Product / value lead |
| Version / date | 1.0.0 / 2026-08-15 |
| Status | Leadership briefing — portfolio-first |
| Audience | CQO, EU QP, Global Head of PV, Supply VP, RA, CISO, DPO |
| Canonical pitch | [`../SCQA.md`](../SCQA.md) |
| Sources | `case/INTEGRATED_CASE.md`, `data/portfolio_products.csv`, `data/board_requests.csv`, `data/inspection_requests.csv`, `data/kpi_conflicts.csv`, `data/commercial_forecast.csv`, `evaluation/public_scenarios.json`, artefacts `01`, `02`, `15`, `22`, `37` |

**Headline:** Four products. Concurrent evidence failures. AEGIS packages; QP, PV, and Supply still sign.

**Pitch:** Faster, auditable evidence packets. Humans keep every regulated pen.

**How to read the numbers:** These are **case pressure clocks**, not AEGIS results. −14% is a board constraint, not a delivered cycle-time cut.

---

## 1. Problem statement

NovaCura Therapeutics Group cannot defend batch, safety, and supply decisions when each product’s records disagree. Evidence sits in LIMS, MES, QMS, safety, cold-chain, and spreadsheets. No system is universally authoritative. Accountable humans reconcile by hand — too slow for inspection, too unsafe to “fix” silently.

The estate clock applies to **every** product:

- **−14%** end-to-end release lead time by **2026-11-30**, with no specification change and no weaker Quality / QP authority (BR-01, INJ-001).
- **72 hours** to produce a joint inspection pack: trial + batch + safety + AI-system controls (IR-72H, INJ-050).
- **47 minutes** of audit capture disabled during master-data repair (INJ-029) — records in that window are not fully attributable.
- **6 markets** (India, Germany, Ireland, United States, UAE, Singapore). Sponsor NTG (DE); CMO Emerald Fill Finish (IE); acquired BioXen (US).
- Conflicting KPIs: Manufacturing **98%** schedule adherence vs Quality **96%** right-first-time vs Safety **100%** expedited-on-time vs Clinical database lock **2026-09-15**.

AEGIS does **not** solve patent-cliff commercial strategy, PQS redesign, or replacement of Quality systems. It packages evidence so humans can still decide under these clocks.

### 1.1 Portfolio and issues

#### NCB-204 — center of gravity

| | |
|---|---|
| What | Monoclonal-antibody biologic |
| Stage | Phase III and commercial scale-up |
| Exclusivity | **108 months** remaining |
| Market | Global |

Batch, PV, and Supply collide on this product.

- **Batch NCB204-B24071:** missing genealogy branch **SUA-88**; LIMS vs statistical tool vs laboratory notebook disagree (**OOS / OOT / invalid**); contract laboratory sent **mg/L** while the receiving interface assumed **µg/mL** (~**1000×** if treated as 1:1, unapproved); EU release packet lacks a verified supplier-audit commitment (PUB-01).
- **PV:** possible duplicate ICSRs (PV-1001 / PV-1009 / PV-1014) under product aliases; disputed awareness dates; listedness conflict across investigator brochure, CCDS, and local label (PUB-04, PUB-06).
- **Supply:** sole-source excipient contamination with an **8-week** recovery estimate; demand split across commercial markets, trial, and compassionate use; CMO capacity promised to two sponsors (PUB-07).

**AEGIS job:** batch readiness packet, PV intake evidence, draft shortage options. Never certify the batch, never close the safety case, never allocate stock.

#### NCS-310 — hospital and compassionate sterile

| | |
|---|---|
| What | Sterile injectable |
| Stage | Marketed, in shortage |
| Exclusivity | **44 months** remaining |
| Market | Global |
| Risk | Cold-chain and sterility |

- **Batch NCS310-S26033:** environmental-monitoring excursion near fill-finish; organism identification corrected after first review; required eBR step back-entered after network degradation (PUB-02).
- **Shipment SH-901:** temperature-logger clocks and pallet association disputed (PUB-08).

**AEGIS job:** surface environmental, complaint, and logger evidence with provenance. Quality still assesses the excursion; Supply still decides what moves.

#### NCX-101 — patent-cliff commercial

| | |
|---|---|
| What | Oral small-molecule oncology |
| Stage | Marketed |
| Exclusivity | **19 months** to loss of exclusivity |
| Market | US / EU |
| Forecast | **310,000** EU units/year; confidence **0.62** |
| Risk | Label divergence |

This product creates **enterprise heat**, not a single public-fixture batch break. Commercial pressure to go faster and cheaper (INJ-004) collides with the board rule: do not weaken the QP while cutting **14%** off release lead time.

**AEGIS job:** keep release evidence inspectable while the cliff clock runs. AEGIS does **not** own patent or indication strategy.

#### NCR-415 — acquired gene therapy

| | |
|---|---|
| What | Rare-disease gene-therapy research |
| Stage | Research (acquired with BioXen) |
| Exclusivity | **144 months** remaining |
| Market | EU / US |
| Risk | Genomic privacy; incompatible identifiers |

- Consent, deletion, and legal-hold obligations can conflict with trial-integrity retention (PUB-11 class).
- Protocol-version authority must be established without making eligibility decisions (PUB-15 class).

**AEGIS job:** purpose, consent, and document-authority packets. Never decide clinical eligibility.

---

## 2. Current status

Workshop wave **W0** is built and evaluated locally. AEGIS is a hexagonal advisory layer (FastAPI + React + deterministic reasoners) with an AI-disabled path and no execute controls in the UI.

| Fact | Status |
|---|---|
| Public fixtures PUB-01..15 | **15/15** evaluated (evidence dated 2026-08-14) |
| Deterministic tests | **54** passed |
| Grader fails recorded | **0** |
| Human agreement κ | **Not claimed** — dual labels not collected |
| Live systems of record | **Not connected** |
| GxP OQ / PQ | **Not done** |
| EU AI Act classification | **Pending** RA / legal |

This is a defensible workshop intervention, not a production go-live.

---

## 3. Proposed solution (now)

Ship **AEGIS Evidence Orchestrator** as a **read-only advisory layer** on the brownfield estate. Rules first; optional LLM behind a port and switchable off; knowledge graph advisory only — never the system of record.

| Workflow | Provides | Does not provide |
|---|---|---|
| Batch | Readiness packet: citations, conflicts, gaps, abstentions | QP certification; release / reject / reprocess / relabel / recall |
| PV | Intake support: duplicates, clocks, listedness **evidence** | Final seriousness, causality, expectedness, reportability, signal |
| Supply | Ranked **draft** options with constraints | Reservation, allocation, shipment, inventory status change, recall |

Unresolved identity, unit, time, terminology, or authority → **fail closed**. Human review gate before export. Every run stays `execution_status = not_executed`.

---

## 4. Future solution

Strangle the evidence-assembly problem. Do not replace LIMS, MES, QMS, or the safety database.

| Wave | When | What changes | Exit |
|---|---|---|---|
| W0 Workshop | Now | Fixtures, contracts, offline CLI/API, review UI | PUB path green (in hand) |
| W1 Pilot | 8–12 weeks | One batch site; read-only SoR API; production human-review gates | OQ on one site (NCB-204 / NCS-310 evidence) |
| W2 PV | +8 weeks | Intake support in the safety workflow; multilingual preserve | DPO sign-off on logs |
| W3 Supply | +8 weeks | Shortage / cold-chain options in planning UI | No TMS / WMS write |
| W4 Scale | Parallel | Optional Neo4j; enterprise LLM gateway; FinOps caps | Parity tests + kill-switch to stub |

Later: vendor-exit drill and ISO 42001 AIMS audit. **Never:** MES / LIMS write-back or autonomous regulated acts.

---

## 5. Boundaries

AEGIS **must not**:

- Release, reject, reprocess, relabel, or recall a batch.
- Make final PV seriousness, causality, expectedness, reportability, or signal decisions.
- Reserve capacity, allocate stock, ship product, change inventory quality status, or initiate a recall.
- Decide clinical eligibility or change formulation / specification.
- Write back to MES, LIMS, QMS, or the PV database.
- Treat untrusted or superseded documents as policy.
- Silently convert units or repair genealogy.

**15** prohibited actions are blocked in code. **6** human-review gates sit in front of export. Emergency stop and AI-off continuity are required. If the system emits a disposition-like output: **stop**.

Pens stay with **QP / Quality**, **PV medical**, and **Supply + Quality**.

---

## Ask

**Conditional go** to package evidence on these four products.

Not a go for autonomous Quality, PV, or allocation.

---

## Number glossary (speaker notes)

| Number | Meaning | Not |
|---|---|---|
| −14% | Board release-lead-time target by 2026-11-30 | An AEGIS result |
| 72 h | Inspection pack deadline (trial, batch, safety, AI controls) | System latency SLO |
| 47 min | Audit logging was off — evidence hole | A planned maintenance window we accept |
| ~1000× | mg/L vs µg/mL if treated 1:1 | A conversion AEGIS should apply |
| 8 weeks | Sole-source excipient recovery (NCB-204 supply) | A reservation AEGIS may place |
| 19 / 108 / 44 / 144 months | Remaining exclusivity by product | A commercial forecast AEGIS owns |
| 310k / 0.62 | NCX-101 EU volume and forecast confidence | A demand number to allocate against |
| 15/15, 54, κ pending | Workshop evaluation status | Production validation |
