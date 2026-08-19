# 43 — Problem-statement volumetrics (commercial / supply mapped)

| Field | Entry |
|---|---|
| Owner | Product / value lead |
| Version / date | 1.0.0 / 2026-08-19 |
| Status | Problem-statement support — case extract volumes, not live ERP |
| Canonical problem framing | [`SCQA.md`](SCQA.md), [`01_discovery_problem_baseline_value.md`](01_discovery_problem_baseline_value.md), [`executive_summary/executive_summary.md`](executive_summary/executive_summary.md) |
| Sources | `data/commercial_forecast.csv`, `data/demand_forecast.csv`, `data/inventory.csv`, `data/exposure_estimates.csv`, `data/cmo_capacity.csv`, `data/supplier_risks.csv`, `data/DATASET_PROFILE.csv`, plus supporting tables listed in §3 |

**How to read this file:** Volumes are **workshop extract numbers**. They describe gravity of *manual evidence collection*, not AEGIS delivered KPIs. AEGIS packages evidence; it does **not** allocate stock, certify batches, or close PV cases.

**Problem nutshell these numbers support:** NovaCura must defend batch, safety and supply decisions while records disagree. Manual reconciliation is too slow for the **72-hour** inspection pack and the **−14%** release-lead-time clock (BR-01, 2026-11-30), and too unsafe to “fix” silently.

---

## 0. Workflow legend (who owns the evidence job)

| Workflow | Job (advisory only) | Must never |
|---|---|---|
| **A — Batch readiness** | Reconcile genealogy, units, OOS/OOT, eBR, supplier-audit, release-packet completeness for QP review | Certify, dispose, release, reject, recall |
| **B — PV intake** | Surface ICSR clocks, duplicates, listedness, terminology, exposure-basis conflicts for medical review | Final seriousness / causality / expectedness / reportability / signal |
| **C — Supply options** | Reconstruct cold-chain / serialisation, shortage, CMO capacity and **draft** policy-bounded options | Allocate, reserve, ship, change inventory quality status, initiate recall |
| **Cross-cut** | Assemble IR-72H inspection manifest (trial + batch + safety + AI controls) | Fabricate missing evidence |

Manual evidence collection **creates impact** when the accountable workflow cannot produce a conflict-visible packet in time — humans still take the regulated decision.

---

## 1. Commercial / supply volumes mapped to the problem statement

Each row: **volume → why it belongs in the problem statement → impact if evidence stays manual → which workflow’s packet delay creates that impact.**

| Volume (verbatim) | Source | Problem-statement mapping | Impact of manual evidence collection | Workflow that creates the impact | Why this workflow |
|---|---|---|---|---|---|
| **NCX-101 EU annual units = 310,000** (forecast confidence **0.62**) | `commercial_forecast.csv` | Commercial heat on the **patent-cliff** product (**19 months** remaining exclusivity). Board still requires **−14%** release lead time **without** weaker QP (BR-01 / INJ-004). Confidence **0.62** means the number is **planning context, not a fact to execute against**. | Reviewers stitch label, MA, and release-packet evidence by hand. Packets arrive late or incomplete → release queue stretches while LoE clock runs; pressure grows to skip Quality checks. Using **310k** as if it were firm demand can also drive **undefendable** commercial-vs-quality trade-offs. | **Primary: A (Batch).** **Secondary: C (Supply)** as *constraint visibility only*. **Cross-cut** if the 72h pack must show how cliff pressure was *not* allowed to weaken QP. | Workflow A owns **release-evidence completeness** that gates how fast humans can even *consider* certification. Workflow C must **not** treat 310k as an allocation quantity. AEGIS does **not** own patent or indication strategy. |
| **NCB-204 US annual units = 42,000** (forecast confidence **0.41**) | `commercial_forecast.csv` | Center-of-gravity biologic: Phase III + commercial scale-up (**108 months** exclusivity). Low confidence (**0.41**) plus **batch / trial / compassionate** collision is the scale of *disputed* commercial expectation, not a clean SKU forecast. | Manual packs cannot show, in one place, that US volume sits on a **quality-hold batch**, **quarantine stock**, and **trial demand**. Leadership may treat **42k** as committed supply. Inspection cannot see the confidence gap. | **Primary: A (Batch)** for hold/genealogy/unit/OOS evidence that blocks treating forecast as releasable supply. **Co-primary: C (Supply)** for channel split and draft options. | Forecast is meaningless for service if Workflow A has not packaged **why** lots are not released. Workflow C packages **demand vs quality-status vs CMO** without executing. |
| **NCB-204 demand next 8 weeks = 6,700 units** (5,200 commercial EU + 900 clinical trial + 600 compassionate) | `demand_forecast.csv` | Shortage ethics and **channel contention** (INJ-056): three legitimate demands on one constrained biologic in the same recovery window as the **8-week** excipient outage. | Spreadsheets hide the split. Manual delay means compassionate and trial needs are invisible until after commercial is “promised.” Humans then decide under incomplete constraint evidence — or freeze all channels and miss hospital/trial clocks. | **Primary: C (Supply).** **Secondary: A (Batch)** if quality hold / quarantine is what makes 6,700 unmeetable from “released” stock. | Workflow C owns **traceable, policy-bounded options** (commercial vs trial vs compassionate). It never ranks patients or allocates. Workflow A owns **whether units are even eligible to be considered**. |
| **NCB-204 inventory: 4,300 EU released + 2,700 US released + 5,100 Global quarantine** | `inventory.csv` | **Released 7,000** vs **8-week demand 6,700** looks “enough” until **5,100 quarantine** is visible. Problem is not stock-out arithmetic; it is **quality-status ambiguity** under speed pressure. | Manual reconcilers mix released and quarantine in one total, or take days to prove provenance of the 5,100. Impact: either **false comfort** (allocate from quarantine) or **false shortage** (ignore released). Both are undefendable. | **Primary: C (Supply)** for optioning **without changing status**. **Gate: A (Batch)** — quarantine / hold evidence must stay visible; Quality still owns status. | Workflow C drafts options **constrained by** quality status. Workflow A packages **why** quarantine exists (genealogy, units, OOS, packet gaps). Neither workflow may flip `quality_status`. |
| **NCS-310 AE released inventory = 420 units** (marketed shortage, sterile injectable) | `inventory.csv` | Hospital / compassionate sterile channel: **hours matter**. Thin released stock plus **customs-hold shipment SH-902** and fill-finish excursion evidence. | Manual collection of EM, eBR back-entry, logger/pallet, and trade docs cannot keep up with SLA. **420** units can sit unused while the evidence pack is incomplete — or move without a defensible excursion/cold-chain story. | **Primary: C (Supply)** (lane, customs, shortage options, patient-impact *visibility*). **Co-primary: A (Batch)** for NCS310-S26033 excursion / eBR packet. | Workflow C owns **shipment/shortage option packets**. Workflow A owns **sterile-batch readiness** (never disposition). Patient Impact panels inform humans; they do not authorise shipment. |
| **NCB-204 DE exposure: 8,400 (sales) vs 6,100 (infusion registry)** | `exposure_estimates.csv` | Two **non-interchangeable** patient-exposure bases for the same product/market. Problem statement: denominators disagree, so safety *and* supply narratives can both be wrong. | Manual PV and Supply each pick a denominator. Signal rates and “patients at risk in shortage” cannot be compared. Inspection sees two stories. Expedited-on-time KPI (**100%**) collides with incomplete exposure evidence. | **Primary: B (PV)** for exposure-basis conflict on intake/signal *support*. **Secondary: C (Supply)** if shortage ethics cites “patients affected.” | Workflow B must **abstain or dual-cite**, not average 8,400 and 6,100. Workflow C may **show** both bases as constraints; it must not compute an allocation from either. |
| **CMO-IE window 2026-W34: capacity 2 batches; promised 2 to NTG and 1 to another sponsor** | `cmo_capacity.csv` | **Over-promise:** 3 promised vs 2 physical slots. Scale-up of NCB-204 is capacity-false, not just inventory-false. | Manual capacity emails vs NTG schedule vs other-sponsor promise are reconciled too late. Impact: a “recovery option” that double-books the CMO, or a silent choice that starves trial/compassionate. Inspection cannot see the conflict. | **Primary: C (Supply).** | Workflow C surfaces **CMO conflict as a constraint** on draft options. It must **not** reserve the slot. Workflow A is downstream (no batch to review if the campaign cannot run). |
| **Sole-source excipient recovery = 8 weeks; alternate not qualified** (`EXCIP-ONE` / Polysorbate-X, contamination) | `supplier_risks.csv` | Hard recovery clock on NCB-204 supply. Same window as **6,700** units demand. No qualified alternate = no silent substitution. | Manual supplier-audit / CoA / recovery evidence is slow and often **unverified** (EU packet gap class). Impact: humans plan 8-week continuity **without** seeing that the audit commitment is unverified, or they qualify an alternate informally. | **Primary: C (Supply)** for shortage-duration constraint. **Co-primary: A (Batch)** for **supplier-audit / release-packet** completeness (PUB-01 class). | Workflow C carries **recovery_weeks** into options. Workflow A carries **whether supplier evidence is verified** into QP-facing packets. Neither purchases nor qualifies a new supplier. |

### 1.1 Combined commercial / supply squeeze (problem sentence)

**8-week NCB-204 demand is 6,700 units** against **7,000 released** and **5,100 already quarantined**, with **CMO capacity over-promised (2+1 vs 2)** and **8 weeks** of sole-source recovery. **NCX-101** still forecasts **310,000** EU units/year at **0.62** confidence under a **19-month** LoE clock. **NCS-310** has **420** AE released units in a shortage/cold-chain/customs fight.

If evidence collection stays **manual**, Workflow **C** cannot produce defendable *options* before channels are informally promised; Workflow **A** cannot produce defendable *readiness packets* before QP is asked to go faster; Workflow **B** cannot keep **exposure denominators** honest when shortage and safety stories mix. The business impact is **undefendable signature risk** (false supply, skipped Quality, or missed inspection) — not “lost units AEGIS will recover.”

---

## 2. Decision-object counts (extract scale)

| Object | Count | IDs / note | Problem relevance |
|---|---|---|---|
| Products | **4** | NCX-101, NCB-204, NCS-310, NCR-415 | Portfolio gravity, not SKU sprawl |
| Orgs | **3** | NTG (DE), CMO Emerald Fill Finish (IE), BioXen (US) | Sponsor / CMO / acquired-ID conflict |
| Market authorisations (NCB-204) | **3** | EU / US / IN | Label/version divergence |
| Batches in master | **2** | NCB204-B24071 quality_hold; NCS310-S26033 pending_review | Workflow A objects |
| Shipments | **2** | SH-901 quarantine; SH-902 customs_hold | Workflow C objects |
| ICSR cases | **3** | PV-1001, PV-1009, PV-1014 | Workflow B duplicate cluster |
| Receipt times for one case | **3** | vendor / affiliate / global DB | Awareness-date dispute |
| Clinical trials | **2** | NCB204-301 (US,DE,IN,AE); NCR415-101 | Trial vs commercial evidence |
| Subjects in extract | **2** | `subjects.csv` | Thin clinical extract |
| Injects | **84** | `inject_evidence_map.csv` | Concurrent pressure |
| Knowledge catalog docs | **32** | `knowledge_catalog.csv` | Authority/status checks |
| Profiled datasets | **~140** | `DATASET_PROFILE.csv` | Fragmented SoRs |

**Scale line for the problem statement:** Volume is **small**; **consequence per record is large**. Two batches and two shipments concentrate the gravity of four products, 84 injects, and a 72-hour multi-agency pack.

---

## 3. Other case volumes (supporting, not commercial SKU)

### 3.1 PV / evaluation cohorts

| Cohort | n | Source | Workflow |
|---|---|---|---|
| PV English | **500** | `evaluation_cohorts.csv` | B |
| PV Hindi | **40** | same | B (multilingual intake fidelity) |
| PV Arabic | **35** | same | B |
| Batch sterile | **85** | same | A (NCS-310 class) |

### 3.2 Model / cost estate (AI-pressure, not supply volume)

| Metric | Value | Source |
|---|---|---|
| Batch-review requests logged | **1,900** (1,110 successful) | `model_usage.csv` |
| PV-intake requests logged | **4,200** (2,800 successful) | `model_usage.csv` |
| Tokens (batch / PV) | **5.8M / 9.2M** in; **0.85M / 1.7M** out | `model_usage.csv` |
| Inference cost | **$184,000 / month** | `cost_model.csv` |
| Observability | **$31,000 / month** | `cost_model.csv` |
| Human quality / medical review in cost model | **$0** (unpriced — gap) | `cost_model.csv` |
| AI-off continuity | **14 days** batch & supply; PV **0 hours** | `continuity_requirements.csv` |
| Omics train / test | **n = 812 / 91** | `omics_cohorts.csv` (NCR-415 class; privacy, not allocation) |

These rows support the problem that **manual-plus-unpriced human review** sits beside a **priced** inference bill — they are not units AEGIS may ship.

---

## 4. Estate clocks (not AEGIS results)

| Number | Meaning | Not |
|---|---|---|
| **−14%** by 2026-11-30 | Board release-lead-time target; no weaker QP | A cycle-time AEGIS has delivered |
| **72 h** | IR-72H joint inspection pack | System latency SLO |
| **47 min** | Audit capture disabled (INJ-029) | Accepted maintenance |
| **~1000×** | mg/L vs µg/mL if treated 1:1 | A conversion to apply |
| **19 / 108 / 44 / 144 months** | Remaining exclusivity by product | A forecast AEGIS owns |

---

## 5. Drop-in problem-statement paragraph (volumes + workflows)

NovaCura must defend **batch, PV, and supply** decisions from a **thin high-stakes extract**: **4 products**, **2 contested batches**, **2 blocked shipments**, **3 colliding ICSRs**, and **~140** disagreeing tables. Commercial scale is concentrated, not large: **NCX-101** forecasts **310,000** EU units/year at only **0.62** confidence under a **19-month** LoE clock — **Workflow A** owns the release-evidence pack that must stay complete despite speed pressure. **NCB-204** (center of gravity) has **6,700** units demanded in **8 weeks** against **7,000** released and **5,100** quarantined, **CMO capacity over-promised**, and an **8-week** sole-source recovery — **Workflow C** owns draft shortage/cold-chain options; **Workflow A** owns why stock is not certifiable. **NCS-310** has **420** AE released units in shortage with sterile and customs evidence still disputed. **DE exposure** disagrees (**8,400** sales vs **6,100** registry) — **Workflow B** must keep both bases visible. Manual evidence collection makes these packets late or silently “fixed”; the impact is **undefendable signatures** under **−14%** lead-time and **72-hour** inspection clocks — not a chatbot gap.

---

## Change control

- Recalculate from `data/` if CSVs change; do not round confidence or dual-count released + quarantine as one available pool.
- Do not convert these volumes into AEGIS ROI, allocated units, or patient-outcome claims.
