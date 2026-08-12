# 41 — Workflow 2 (PV) & Workflow 3 (Supply) UI Specs  
## Wired to Control Centre, Twins, Portfolio & Obligations

| Field | Entry |
|---|---|
| Owner | Product / UX demo lead |
| Version / date | 1.1.0 / 2026-08-12 |
| Status | **Ready to freeze** — demo depth & Control Centre rules locked; build only after explicit go |
| Depends on | `39_persona_to_workflow_e2e_flows.md`, `40_demo_ui_feature_catalogue.md` v1.1, Workflow 1 UI agreements, `submission/demo_data/*` |
| Login | Demo persona picker |
| Default home | Control Centre for **all** personas (role-filtered) |
| Comments | Append-only on conflicts, tasks, twin nodes, packets |
| Shared shell | Same areas as artefact `40` (War Room / What-if deferred in v1) |
| PV live depth (locked) | Priya → Aisha + Laura → Markus (+ optional Amira) |
| Supply live depth (locked) | Sofia → Diego → Tomás + NCS-310 Patient Impact (RA/CMO light) |

---

## 0. Shared rules (same as Batch)

1. **Trigger comes from SoR / channels** — primary operator **claims** the case; no separate Allocator persona.  
2. **AEGIS closes orchestration**; regulated finals happen **outside** (global safety DB / inventory–eQMS).  
3. **Banner always:** Advisory only · `execution_status = not_executed`.  
4. **Story Mode** coach marks + **Expert layer** (hashes, abstention codes).  
5. Every major screen shows **product chip** (NCX / NCB / NCS / NCR) and **stakes one-liner**.

### Case state machine (PV & Supply)

```text
New (in queue from trigger)
 → Claimed / Allocated
 → Evidence_Gathering
 → Supporting_Tasks_Open
 → Packet_Draft
 → Awaiting_Accountable_Review
 → Escalated (optional)
 → Human_Review_Complete | Insufficient | Conflicted
```

Never set by AEGIS: Released, Allocated-stock, Shipped, Reportable-final, Signal-confirmed.

---

# PART A — Workflow 2: Pharmacovigilance intake support

## A1. Demo objects & fixtures

| Item | Value |
|---|---|
| Primary demo case | `CASE-PV-001` → objects `PV-1001` (+ cluster `PV-1009`, `PV-1014`) |
| Secondary | `CASE-PV-002` → `PV-1009` (listedness / DPO path) |
| Product | **NCB-204** |
| Fixtures | PUB-04, PUB-05, PUB-06 |
| Intent | Duplicates, clocks, terminology, listedness, multilingual preservation |

## A2. Personas (depth from artefact 39)

| Role | Persona | UI participation |
|---|---|---|
| Primary operator | **Priya Nair** (P-INT) | Claim, reconcile, dispatch, packet, hand to medical |
| Primary accountable (finals outside) | **Dr. Markus Keller** (P-MED) | Advisory packet review; finals in safety DB (simulated external) |
| Escalation | **Dr. Amira Soliman** (P-PVH) | Policy / high uncertainty / signal-concern escalation |
| Supporting | **Aisha Rahman** (P-RA) | Listedness / labelling source authority |
| Supporting | **Laura Mendes** (P-DPO) | Purpose binding, narrative minimisation, sensitive segments |
| Informed (conditional) | **James Okonkwo** / QP lane | Product-quality complaint → batch link |
| Contestability | **Samira Ali** (P-PSR) | Plain-language contest after the fact |
| Cross-cut | Chen / Kai | Stop, continuity, poisoned tools |

## A3. Real-world trigger (not Priya inventing a case)

```text
Multi-channel intake receipts land
  (call centre | affiliate inbox | vendor portal | literature)
        ↓
Global PV Operations queue (Priya’s team)
        ↓
Priya Claims / Opens intake-support case in AEGIS
        ↓
Runs reconciliation → exceptions → supporting tasks
        ↓
Hands intake support packet to Markus
        ↓
Markus advisory accept / request more / escalate Amira
        ↓
Finals recorded in global safety database (OUTSIDE AEGIS)
```

**UI Intake Queue card shows:** channel badges, earliest awareness candidate dates (conflicted), product alias, language flags, `trigger_source=multi_channel_receipt`.

## A4. End-to-end persona path (demo)

| Step | Login as | Screen focus | Action | Handover |
|---|---|---|---|---|
| 0 | Priya | Control Centre → PV lane | See `CASE-PV-001` live | — |
| 1 | Priya | Workflow Case · Claim | Claim PV-1001 cluster; purpose=`pv_intake_support` | Self |
| 2 | Priya | Run reconciliation + Safety Case Twin | Surface clocks, duplicates, terms, listedness, languages | — |
| 3 | Priya | RBE Workbench | Dispatch RA (listedness), DPO (purpose/narrative) | Aisha, Laura |
| 4a | Aisha | Listedness task | Cite CCDS/local/IB applicability; comment; return | Priya |
| 4b | Laura | Privacy task | Purpose bind; flag sensitive segments; minimisation note; return | Priya |
| 5 | Priya | Packet assemble + checklist | Multilingual preserved; no silent translation; hand to medical | Markus |
| 6 | Markus | Medical advisory review | Accept packet for external finals / request more / escalate | Amira optional |
| 7 | Amira | Escalation (branch) | Policy / signal-concern note; return | Markus/Priya |
| 8 | Priya/Markus | Optional quality link | If complaint–batch link → notify James (Cross-Impact) | James informed |
| 9 | Any authorized | Audit export | Hashed intake support packet | Demo end |

## A5. Screens — what the UI shows

### A5.1 Control Centre (PV lane)

- Cards from `live_cases.csv` (`CASE-PV-001`, `CASE-PV-002`)
- Badges: duplicate uncertainty · clock conflict · waiting on RA/DPO
- Portfolio chip **NCB-204**
- Microcopy: *“Intake support only — AEGIS does not decide seriousness, causality, expectedness, reportability or confirm signals.”*
- Drill-through → Workflow Case

### A5.2 Portfolio Command → NCB-204

- Shortcut: “Open live PV intake cluster PV-1001 / 1009 / 1014”
- Stakes: pivotal biologic safety + scale-up convergence
- Link to Cross-Impact if quality–safety edge exists (`cross_impact_links.csv` X-03)

### A5.3 Workflow Case — Priya home

**Header:** case ids · product · purpose · readiness/abstention chips · Story Mode step

**Primary CTA:** Run intake reconciliation (PUB-04 class)

**Evidence board columns:**  
source channel · receipt id · awareness_date (verbatim) · narrative language · MedDRA version · product alias · hash/provenance

**Conflict register (must show):**
| Conflict | Demo data / fixture focus |
|---|---|
| Awareness / reporting clock conflict | Multiple dates across affiliate/vendor/GSDB |
| Duplicate uncertainty | PV-1001 / 1009 / 1014 cluster — no auto-merge |
| Terminology / MedDRA version mismatch | Dictionary version conflict |
| Listedness evidence conflict | CCDS vs local label / IB |
| Multilingual preservation | Arabic / German / English — no silent “correction” |
| Sensitive content (if present) | Pregnancy/paediatric flags → DPO |

**Task dispatch mapping:**
| Exception | Suggested assignee |
|---|---|
| Listedness / labelling authority | Aisha (RA) |
| Purpose / minimisation / sensitive narrative | Laura (DPO) |
| Product-quality complaint linkage | Notify James (informed) — not a supporting “fix” |
| Terminology uncertainty | Priya retains + abstain, or RA consult |

### A5.4 Safety Case Twin (`TWIN-PV-1001`)

From `twin_nodes.csv` / `twin_edges.csv`:
- Timeline swim of awareness candidates (red if conflict)
- Duplicate cluster nodes (amber)
- Listedness source nodes
- Narrative language pins (preserve original text side-by-side; translation = optional **human-labelled** aid, never silent replace)
- Click node → verbatim + comment thread

### A5.5 Review-by-Exception (PV)

From `review_by_exception_queue.csv` (e.g. EX-08) + PUB focus:
- Red/amber exceptions expanded
- Green collapsed (e.g. stable product master alias where verified)
- CTA: Create task · Add comment · Abstain reason code
- **Disabled:** Merge duplicates · Set reporting clock · Mark reportable · Confirm signal

### A5.6 Supporting workspaces

**Aisha (RA)**  
- Listedness task: source status, effective date, authority  
- Actions: Applicable / Not applicable / Abstain + comment · Return to Priya  
- Cannot: declare expectedness/listedness final for the case

**Laura (DPO)**  
- Purpose binding checklist; residency; narrative minimisation  
- Flag segments that must not leave region / must not enter LLM path  
- Return with privacy constraints attached to packet  
- Cannot: delete required GxP narrative silently — minimise with audit

### A5.7 Packet assembly (Priya)

Checklist (all addressed or abstained):
- [ ] Clock conflicts acknowledged  
- [ ] Duplicate candidates listed with uncertainty (not merged)  
- [ ] Terminology conflicts visible  
- [ ] Listedness citations present / abstained  
- [ ] Multilingual originals preserved  
- [ ] DPO purpose constraints attached (if triggered)  
- [ ] Human medical review required acknowledged  

CTA: **Hand over to Pharmacovigilance Medical Reviewer**

### A5.8 Markus — Medical advisory review

**Shows:** full packet + twin + supporting comments (read-only evidence)

**Advisory intents only:**
| Intent | Resulting AEGIS state | Outside AEGIS |
|---|---|---|
| Request more evidence | `Insufficient` → back to Priya | — |
| Escalate to Global Head PV | `Escalated` → Amira | — |
| Accept packet for external medical/regulatory finals | `Human_Review_Complete` + export | Markus records seriousness/causality/expectedness/reportability/signal **in global safety DB** (simulated external panel) |
| Notify Quality (quality–safety link) | Informed notify James | Complaint/batch follow-up outside |

**Disabled section:** Final safety decisions (seriousness, causality, expectedness, reportability, confirm signal)

**Simulated external panel label:**  
*“Global safety database disposition (outside AEGIS) — storytelling acknowledgement only.”*

### A5.9 Amira — Escalation branch

- Sees escalation reason, uncertainty summary, optional signal-concern note field  
- Actions: Guidance comment · Return to Markus/Priya  
- Cannot: confirm signal inside AEGIS

### A5.10 Wiring to other catalogue features

| Feature | PV wiring |
|---|---|
| Cross-Impact Graph | PV ↔ Batch quality link; PV packet → Inspection War Room |
| Obligations Desk | OB-02 (PV finals human), OB-04/05/09 (oversight, transparency, privacy) |
| Case studies | CS-04 clock conflict |
| Continuity Console | Safety DB region outage → AI-disabled / offline intake path |
| Patient Safety view | Samira: plain-language “why duplicates were not auto-merged” |
| Inspection War Room | IWR-02 task — attach PV packet to IR-72H |
| Comments | Required on task return and on medical advisory intent |

## A6. Explicit PV non-goals on UI

No buttons/flows for: final seriousness, causality, expectedness, reportability, signal confirmation, silent translation that replaces source narrative, auto-merge of duplicates, auto-setting of reporting clock.

---

# PART B — Workflow 3: Supply recovery optioning

## B1. Demo objects & fixtures

| Item | Value |
|---|---|
| Primary | `CASE-SUP-001` → shipment `SH-901` / NCB-204 shortage–cold-chain (PUB-07) |
| Critical SLA | `CASE-SUP-002` → `SH-902` / **NCS-310** customs hold (PUB-08) |
| Product pressures | NCB-204 trial/commercial/compassionate; NCS-310 hospital/compassionate |
| Intent | Non-executing recovery options under quality, ethics, cold-chain, capacity |

## B2. Personas (depth from artefact 39)

| Role | Persona | UI participation |
|---|---|---|
| Primary operator | **Sofia Almeida** (P-SP) | Claim, gather, simulate options, packet, hand to gatekeeper |
| Primary execution gate (outside) | **Tomás Rivera** (P-QG) | Reviews options + quality holds; approvals in eQMS/ERP outside |
| Supporting | **Diego Fernández** (P-LOG) | Cold-chain / serialisation / transport evidence |
| Supporting | **Ananya Krishnan** (P-CMO) | External capacity constraints |
| Supporting | **Michael Brandt** (P-MFG) | Internal capacity / schedule |
| Supporting | **Nadia Hussain** (P-SQ) | Material / supplier constraints (when relevant) |
| Supporting | **Aisha Rahman** (P-RA) | Market authorisation / distribution constraints |
| Supporting | **Oliver Grant** (P-PRC) | Vendor capacity / exit terms (when relevant) |
| Informed | Elena / James | Batch hold driving shortage; recall consult |
| Ethics escalation | Ruth / Amira (as needed) | Trial vs compassionate vs commercial |
| Contestability | Samira | Opaque allocation rationale challenge |

## B3. Real-world trigger

```text
Shortage signal / cold-chain dispute / customs or quarantine hold
  (inventory, shipment, logger, demand channels)
        ↓
Global Supply Planning queue (Sofia)
        ↓
Sofia Claims case in AEGIS (purpose=supply_recovery_optioning)
        ↓
Evidence + Cold-Chain Twin + constraints
        ↓
Supporting tasks (Diego, CMO, MFG, RA, …)
        ↓
Draft non-executing options (+ optional What-if simulator)
        ↓
Hand to Tomás (Quality Status Gatekeeper)
        ↓
Tomás advisory accept / block / escalate ethics or QP
        ↓
Allocation / shipment / inventory status / recall
   ONLY in source systems OUTSIDE AEGIS after human approval
```

## B4. End-to-end persona path (demo)

| Step | Login as | Focus | Action | Handover |
|---|---|---|---|---|
| 0 | Sofia | Control Centre → Supply lane | See SH-901 + SH-902 (critical SLA) | — |
| 1 | Sofia | Portfolio NCS-310 / NCB-204 | Open Patient Impact SLA panel | — |
| 2 | Sofia | Claim CASE-SUP-001 (and/or 002) | Purpose bind; run reconciliation | Self |
| 3 | Sofia | Cold-Chain Twin + RBE | Logger/pallet/serialisation exceptions | Diego |
| 4 | Diego | Logistics task | Confirm/deny logger–pallet evidence; comment; return | Sofia |
| 5 | Sofia | Dispatch capacity/RA | CMO capacity, MFG schedule, MA constraints | Ananya, Michael, Aisha |
| 6 | Supporting | Return with comments | Constraints cited | Sofia |
| 7 | Sofia | Options pack (+ What-if if enabled) | Draft options; no side effects | Tomás |
| 8 | Tomás | Gatekeeper review | Accept pack for external approval path / request more / escalate ethics or QP | Ruth/Elena optional |
| 9 | Export | Audit | Options + approvals_required list | End |

## B5. Screens — what the UI shows

### B5.1 Control Centre (Supply lane)

- `CASE-SUP-001` (high), `CASE-SUP-002` (**critical**, 6h SLA from `patient_impact_sla.csv`)
- Badges: quarantine · customs_hold · ethics conflict · waiting on Logistics/QG
- Microcopy: *“Options only — AEGIS never allocates, reserves, ships, changes inventory quality status, or initiates recall.”*

### B5.2 Portfolio Command

**NCB-204:** demand bars commercial / clinical_trial / compassionate (`demand_forecast.csv`)  
**NCS-310:** strict timeline hero + Patient Impact panel (`SLA-01`, `SLA-02`)  
Message: *“Priority visibility ≠ automatic allocation.”*

### B5.3 Workflow Case — Sofia home

**Header:** shipment/product · inventory quality statuses · channel demand · `no_side_effects=true` chip

**Primary CTA:** Run supply optioning reconciliation (PUB-07/08)

**Evidence board:** inventory (released vs quarantine) · shipments · loggers · serialisation · CMO capacity · allocation constraints · market authorisations · AI use boundaries

**Conflict / constraint register:**
| Item | Demo focus |
|---|---|
| Logger clock / pallet mismatch | SH-901 / LG-31 (PUB-07 class) |
| Serialisation aggregation gap | Pedigree strip |
| Quality status constraint | Released-only vs quarantine stock |
| Ethics / priority conflict | Trial vs compassionate vs commercial |
| Capacity shortfall | CMO / internal MFG |
| MA / distribution constraint | RA citations |

**Task dispatch:**
| Exception | Assignee |
|---|---|
| Cold-chain / serialisation | Diego |
| External capacity | Ananya |
| Internal schedule/capacity | Michael |
| Market authorisation | Aisha |
| Supplier/material | Nadia |
| Vendor/contract capacity | Oliver |

### B5.4 Cold-Chain / Pedigree Twin

`TWIN-CC-SH-901` / SH-902 nodes:
- Shipment header · logger UTC vs local_unknown · pallet IDs · serialisation aggregation  
- Red edges for identity/time disputes (`twin_edges.csv` E-06)  
- Comments pinned by Diego  

### B5.5 Review-by-Exception (Supply)

Exceptions EX-06, EX-07 style:
- Red: logger/pallet identity  
- Amber: channel ethics under customs hold  
- Green collapsed: stable lane metadata when verified  
- **Disabled:** Allocate · Reserve · Ship · Change quality status · Initiate recall  

### B5.6 What-if Supply Simulator (catalogue feature — see v1 priority §C)

**UI:** choose constraint toggles (released_only, include_compassionate_priority_visibility, capacity caps) → show **draft options** aligned to product option IDs (e.g. prioritise released-stock visibility review; escalate ethics; document shortfall).

**Labels:** `Simulate impact (no side effects)` · each option `status=draft`  
**Output panel:** `approvals_required`: inventory_status_change, allocation, shipment, recall_initiation, quality_assessment  

If **dropped from v1 demo**, Sofia still builds the same options pack via static reconciliation results (PUB-07/08) without interactive toggles.

### B5.7 Patient Impact & Ethics panel

From `patient_impact_sla.csv`:
- Hours to impact · channel · constrained object  
- CTA: Escalate ethics (Ruth / medical-ethics path) · Comment  
- Never: auto-prioritise channel fulfillment  

### B5.8 Packet assembly (Sofia)

Checklist:
- [ ] Cold-chain / pedigree conflicts acknowledged or abstained  
- [ ] Inventory quality statuses cited (not changed)  
- [ ] Channel demand cited  
- [ ] Options listed as draft / non-executing  
- [ ] Approvals_required non-empty  
- [ ] Ethics escalation flagged if trial/compassionate/commercial conflict  
- [ ] Human gatekeeper review required  

CTA: **Hand over to Quality Status Gatekeeper**

### B5.9 Tomás — Gatekeeper advisory review

**Shows:** options pack · quality holds · twin · supporting comments · Patient Impact  

**Advisory intents:**
| Intent | AEGIS state | Outside AEGIS |
|---|---|---|
| Request more evidence | Back to Sofia | — |
| Escalate ethics (CQO / medical) | `Escalated` | Ethics forum |
| Consult QP (batch hold / recall implications) | Informed Elena | eQMS consult |
| Accept options pack for external execution path | `Human_Review_Complete` | Tomás/authorized humans approve allocation/shipment/status/recall **in ERP/WMS/eQMS** (simulated external panel) |
| Document shortfall — no execution | `Conflicted`/`Insufficient` with abstention | No stock movement |

**Disabled:** Allocate · Ship · Change inventory quality status · Initiate recall  

**Simulated external panel:**  
*“Inventory / shipment / quality-status approvals (outside AEGIS).”*

### B5.10 Wiring to other catalogue features

| Feature | Supply wiring |
|---|---|
| Cross-Impact | Batch hold → SH-901; SH-902 → inspection; NCS batch pending ↔ SLA |
| Obligations | OB-03 supply ethics; OB-04 human oversight; OB-11 boundaries |
| Case studies | CS-05 cold-chain; CS-06 compassionate vs commercial |
| Inspection War Room | IWR-03 attach supply options packet |
| Continuity | Logistics outage / ransomware → degraded optioning |
| NCX Obligations Desk | Not primary; supply may appear as service risk context only |
| Comments | Required on option rationale and gatekeeper intent |

## B6. Explicit Supply non-goals on UI

No working controls for: allocate stock, reserve capacity, change inventory quality status, ship product, initiate recall, or present options as already executed.

---

# PART C — v1 demo feature priority (locked for freeze)

Use this to accept / drop features without rewriting workflow logic.

| Feature | Workflow 1 Batch | Workflow 2 PV | Workflow 3 Supply | v1 recommendation |
|---|---|---|---|---|
| Persona picker + comments + handovers | Required | Required | Required | **Keep** |
| Control Centre live lanes | Required | Required | Required | **Keep** |
| Portfolio Command (4 products) | Required | Required | Required | **Keep** |
| Evidence Twin (Batch / Safety / Cold-Chain) | Batch Twin | Safety Case Twin | Cold-Chain Twin | **Keep** |
| Review-by-Exception | Keep | Keep | Keep | **Keep** |
| Cross-Impact Graph | Keep | Keep | Keep | **Keep** (high wow / low risk) |
| Obligations & Exclusivity Desk | Link | Link | Link | **Keep** (esp. NCX + EU Act) |
| Patient Impact / Ethics panel | Light | Light | **Critical for NCS-310** | **Keep** |
| Story Mode narrator | Keep | Keep | Keep | **Keep** |
| Continuity & Trust Console | Demo flash | Demo flash | Demo flash | **Keep thin** (one screen) |
| **Inspection War Room** | Optional attach | Optional attach | Optional attach | **Deferred (v1.1)** — thin IR-72H chip only in v1 |
| **What-if Supply Simulator** | — | — | Interactive toggles | **Deferred (v1.1)** — static PUB-07/08 options pack in v1 |
| Handover Process Twin (process mining) | Nice | Nice | Nice | **Defer** unless time allows |
| Plain-language PSR view | Thin | Thin | Thin | **Keep thin** (one panel) |

### v1 freeze set (**agreed 2026-08-12**)

**Include:** Control Centre · Portfolio · Workflow Cases (all 3) · Twins (3 types) · RBE · Cross-Impact · Obligations Desk · Patient Impact · Story Mode · thin Continuity · comments/handovers  

**Defer:** Inspection War Room (full board), interactive What-if Simulator, full Process-Mining Handover Twin  

War Room / What-if **data already exists** in `demo_data/` so enabling later is additive, not a redesign.

### Control Centre visibility (locked)

- **Every persona** lands on Control Centre after login.
- **All personas can see** the centre; content is **role-filtered** (operators: own lane + my tasks; reviewers: awaiting me; supporting: task inbox; oversight: multi-lane watch).
- No single “Control Centre owner” persona — widest watch lens for Ruth / Chen / Kai in demo.

### What-if Simulator (v1)

- **Deferred** as interactive toggles.
- Sofia still presents **static non-executing options** from PUB-07/08 reconciliation in the options pack.

### Inspection War Room (v1)

- **Deferred** as full board.
- Optional thin chip on Control Centre only (“IR-72H defence pack — v1.1”) without task board UI.

---

# PART D — Side-by-side resolution model (all three workflows)

| Workflow | AEGIS closes when | External SoR resolves |
|---|---|---|
| Batch | Elena accepts readiness packet (advisory) | Certification / hold / reject in **eQMS** |
| PV | Markus accepts intake support packet (advisory) | Finals in **global safety database** |
| Supply | Tomás accepts options pack (advisory) | Allocation / ship / status / recall approvals in **ERP/WMS/eQMS** |

Each external step is a **labelled simulated acknowledgement** in UI — never an AEGIS-executed side effect.

---

# PART E — Demo beat sheet (PV then Supply, ~8–10 min each)

### PV beat
1. Control Centre → Priya claims PV-1001  
2. Safety Case Twin — clock + duplicate red/amber  
3. RBE → tasks to Aisha + Laura → comments return  
4. Packet → Markus advisory accept → external safety DB note  
5. Optional: Cross-Impact notify Quality · Obligations OB-02  

### Supply beat
1. Control Centre → critical NCS-310 SLA card  
2. Patient Impact panel → claim SH-902 / SH-901  
3. Cold-Chain Twin → Diego task/comment  
4. Options pack (static PUB options) → Tomás gate  
5. Disabled allocate/ship strip → external approval simulation  
6. Cross-Impact to batch hold (War Room full board deferred)

---

# PART F — Decisions log (closed)

| # | Topic | Decision |
|---|---|---|
| 1 | v1 deferrals | War Room + What-if deferred; data retained |
| 2 | PV demo depth | Priya → Aisha + Laura → Markus (+ optional Amira) |
| 3 | Supply demo depth | Sofia → Diego → Tomás + NCS-310 Patient Impact; RA/CMO light |
| 4 | Default home | Control Centre for all personas, role-filtered, visible to all |
| 5 | Build | **Not started** — await explicit “freeze and build” |

No further UI catalogue additions required unless product scope changes.

---

*End of artefact 41 — PV & Supply UI specs.*
