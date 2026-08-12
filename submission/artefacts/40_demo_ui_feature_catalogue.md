# 40 — Demo UI Feature Catalogue (Industry-aligned, advisory-only)

| Field | Entry |
|---|---|
| Owner | Product / UX demo lead |
| Version / date | 1.1.0 / 2026-08-12 |
| Status | **Ready to freeze** — decisions locked below; build only after explicit go |
| Companion specs | Workflow 1 agreements (chat) · `41_pv_supply_ui_specs.md` |
| Sources | Artefacts `05`, `06`, `26`, `38`, `39`; `case/INTEGRATED_CASE.md`; `data/*`; industry patterns (control towers, digital twins, review-by-exception, inspection war rooms) |
| Demo data | `submission/demo_data/` (synthetic overlays; does **not** alter challenge evidence) |

### Freeze decisions (2026-08-12)

| Decision | Locked value |
|---|---|
| Login | Demo persona picker |
| Default home | **Control Centre for every persona** (role-filtered; visible to all) |
| Comments | Append-only on conflicts, tasks, twin nodes, packets |
| Batch demo depth | James claims from SoR hold → Nadia/Helen/Michael/Aisha → James packet → Elena (+ optional Ruth) → eQMS outside |
| PV demo depth | Priya → Aisha + Laura → Markus (+ optional Amira) → safety DB outside |
| Supply demo depth | Sofia → Diego → Tomás (+ NCS-310 Patient Impact panel; RA/CMO as light cards unless time) → ERP/eQMS outside |
| v1 include | Control Centre · Portfolio · Workflow Cases (3) · Twins (Batch/Safety/Cold-Chain) · RBE · Cross-Impact · Obligations Desk · Patient Impact · Story Mode · thin Continuity |
| v1 defer | Full Inspection War Room · interactive What-if Simulator · full process-mining Handover Twin (data retained for v1.1) |

---

## 1. Design intent for the live demo

The UI must be **descriptive enough that a non-specialist follows the story**, and **rich enough that specialists feel the real complexity** — without ever executing regulated decisions.

| Demo principle | How it appears in UI |
|---|---|
| Always know where you are | Persistent banner: persona · purpose · product · workflow · `not_executed` |
| Always know why it matters | One-line **patient / business / compliance stakes** on every major screen |
| Complexity without clutter | Progressive disclosure: summary → conflict → twin → raw citation |
| Handovers are visible | Timeline + comments + “waiting on” chips |
| Wow = reconciliation intelligence | Twins, cross-impact graph, review-by-exception — not fake auto-release |

---

## 2. Industry patterns adopted (and how we stay safe)

| Industry pattern | Typical market claim | AEGIS demo adaptation (allowed) | Explicitly blocked |
|---|---|---|---|
| **Quality / supply control tower** | Real-time orchestration of release & logistics | Live Control Centre of advisory cases + SLA heat | Auto-reroute, auto-allocate, auto-release |
| **Digital twin (batch / inventory / cold-chain)** | Predict & act on disruptions | Evidence Twin Studio — conflict-visible mirror of SoR | Plant control, inventory status change |
| **Review-by-exception (RBE)** | Only show what needs judgement | Exception Workbench — green/amber/red evidence slots | One-click batch release |
| **Process mining twin of release workflow** | Find bottlenecks in handovers | Handover Bottleneck view across personas | Bypassing Quality/QP gates |
| **Inspection war room** | 72h multi-agency response | Inspection War Room seeded from `IR-72H` | Fabricating missing evidence |
| **Serialization / pedigree visibility** | DSCSA-style chain | Pedigree strip on shipment twin | Silent repair of aggregation breaks |
| **Signal detection cockpit** | Safety surveillance | Early-warning **candidates** with uncertainty | Signal confirmation |
| **What-if supply simulation** | Scenario planning | Non-executing option simulator | Reserve / ship / change quality status |
| **Patent / exclusivity intelligence** | Competitive planning | Obligations Desk exclusivity brief for humans | Auto patent draft / legal conclusion |
| **Plain-language patient impact** | Access & ethics | Patient Impact panel (NCS-310 / NCR-415) | Clinical eligibility decisions |

---

## 3. Full UI map (demo-ready)

```text
Persona Picker
 └── Shell (banner + guided demo narrator toggle)
      ├── 1. Control Centre (default home)
      ├── 2. Portfolio Command (NCX / NCB / NCS / NCR)
      ├── 3. Workflow Cases (Batch | PV | Supply)  ← persona handovers
      ├── 4. Evidence Twin Studio
      ├── 5. Review-by-Exception Workbench
      ├── 6. Cross-Impact Graph
      ├── 7. Obligations & Guidance Desk
      ├── 8. Inspection War Room
      ├── 9. Continuity & Trust Console (CISO / Platform)
      └── 10. Audit & Defence Export
```

---

## 4. Feature specs (additive to prior Workflow 1 notes)

### 4.1 Control Centre — “Mission control”

**Audience wow:** three live swimlanes; portfolio chips pulse; waiting-on persona avatars.

**UI content**
- Portfolio pulse (from `portfolio_products.csv` + `demo_data/portfolio_pressure_board.csv`)
- Live case cards (from `demo_data/live_cases.csv`)
- Signal strip: conflicts, abstentions, prohibited blocks, AI-disabled
- KPI conflict transparency (INJ-002): Manufacturing speed vs Quality completeness — shown as **tension**, not a score to optimize away Quality
- **Demo Narrator** (toggle): floating coach marks (“James claimed NCB204-B24071 because SoR status = quality_hold”)

**Descriptive copy example**
> “This board does not release medicine. It shows which humans are reconciling which evidence right now.”

---

### 4.2 Portfolio Command — four product theatres

| Product | Hero message (UI) | Special panels |
|---|---|---|
| **NCX-101** | “19 months to exclusivity cliff — accelerate evidence, not shortcuts” | Exclusivity countdown; link to Obligations Desk brief |
| **NCB-204** | “Pivotal + scale-up — batch, safety and supply collide” | Batch Twin + PV Twin shortcuts; trial/commercial/compassionate demand bars |
| **NCS-310** | “Hospital & compassionate channels — hours matter” | Patient Impact SLA; Cold-Chain Twin; shortage options |
| **NCR-415** | “Rare-disease gene therapy — privacy first, research models gated” | Genomic privacy gate; unqualified-model warning (INJ-011) |

---

### 4.3 Evidence Twin Studio — digital twins

**Twin types**
1. **Batch Twin** — genealogy · LIMS · warehouse · release packet · supplier (NCB-204 / NCS-310)
2. **Cold-Chain / Pedigree Twin** — logger · pallet · serialisation · shipment (NCS-310 / NCB-204)
3. **Safety Case Twin** — receipts · clocks · duplicates · listedness (NCB-204)
4. **Handover Process Twin** — persona swimlane delays (process-mining style)

**Rich interactions**
- Node click → verbatim SoR value + hash + authority state + persona comments
- Red pulse on unresolved conflicts; amber on abstentions; green on verified citations
- As-of time scrubber
- Split-view: MES genealogy vs warehouse consumption (SUA-88 story)

**Demo line**
> “The twin mirrors reality — including disagreements. It never ‘fixes’ the plant.”

---

### 4.4 Review-by-Exception Workbench (industry RBE)

Inspired by batch intelligence / exception review — **adapted to advisory packets**.

**UI**
- Completeness radar / checklist slots for the active object
- Only **exceptions** expanded by default (unit mismatch, genealogy break, unverified audit, clock conflict, logger mismatch)
- Green slots collapsed with “verified citation” count
- CTA: “Send exception task to persona” (Nadia / Helen / …)

**Never:** “Release all green items” button.

Data: `demo_data/review_by_exception_queue.csv`

---

### 4.5 Cross-Impact Graph

**Problem it sells:** one quality hold ripples into supply service and sometimes PV complaints.

**UI:** force-directed or layered graph:
- Batch `NCB204-B24071` (hold) → Supply shortage risk on NCB-204 → optional PV product-complaint link → Inspection IR-72H packet demand

Click edge → opens the linked workflow case. Descriptive caption under graph.

---

### 4.6 Obligations & Guidance Desk

Sections:
1. Obligation register (GxP, human oversight, AI boundaries)
2. EU AI Act ↔ ISO 42001 crosswalk (from artefact `26`)
3. Guideline / source shelf (authority-gated)
4. Case-study defence patterns (unit mismatch, cold-chain, duplicates)
5. **NCX-101 exclusivity / patent-support brief** — outline for human counsel only
6. Disease-timeline obligations (compassionate / rare disease)

Data: `obligation_register.csv`, `guidance_case_studies.csv`, `exclusivity_brief_outline.csv`

---

### 4.7 Inspection War Room (72h)

Seeded from `inspection_requests.csv` (`IR-72H`, deadline 72h).

**UI**
- Countdown clock
- Evidence request checklist across Batch + PV + Supply + AI controls
- Assign RA / Quality / PV / Supply owners
- Gap list with abstentions (never invent evidence)
- One-click assemble **defence export** from completed advisory packets

---

### 4.8 Continuity & Trust Console

For Chen (CISO) / Kai (Platform):
- Emergency stop / AI-disabled mode
- Poisoned tool manifest indicator (PUB-09 class)
- Offline continuity path status
- Privileged session / ransomware inject visibility (demo)

Banner everywhere when degraded: “Deterministic path active — advisory only.”

---

### 4.9 Guided Demo Narrator (mesmerize without confusing)

Toggle **Story Mode**:
- Step list: Trigger → Claim → Twin → Exceptions → Supporting personas → QP advisory → External eQMS note → Export
- Each step highlights the exact panel and shows 1–2 sentence plain language
- “Expert layer” toggle reveals hashes, contracts, abstention codes

---

### 4.10 Patient Impact & Ethics panel

Especially **NCS-310** compassionate / hospital and **NCR-415** rare disease:
- Open demand vs constrained supply (from demand forecast + allocation constraints)
- Ethics escalation path (trial vs compassionate vs commercial) — still **options only**
- Patient Safety Representative contestability entry

Data: `demo_data/patient_impact_sla.csv`

---

### 4.11 What-if Supply Simulator (non-executing)

Sofia selects constraints → system shows **draft options** (PUB-07/08 option IDs) with required approvals list.  
Buttons labelled **Simulate impact (no side effects)**.  
Disabled: Allocate, Reserve, Ship, Change quality status.

---

### 4.12 Comments & collaboration (confirmed)

Every conflict, twin node, task, packet, obligation row supports **append-only comments** with persona stamp — feeds Control Centre timeline.

---

## 5. Demo script (10–12 minutes, audience wow path)

1. **Persona picker** → James — Control Centre lights up NCB-204 batch hold + NCS-310 SLA amber.  
2. **Story Mode on** — claim `NCB204-B24071`.  
3. **Batch Twin** — red SUA-88 + unit mismatch; click raw LIMS citation.  
4. **RBE Workbench** — only exceptions open; dispatch Helen + Nadia.  
5. Switch personas (picker) — complete tasks **with comments** — return.  
6. **Cross-Impact Graph** — hold → supply risk → inspection packet.  
7. **Portfolio NCX-101** — 19-month cliff → Obligations Desk → exclusivity brief outline.  
8. **NCS-310** — Cold-Chain Twin + What-if simulator (options only).  
9. **Elena** — advisory QP accept → simulated eQMS note (outside).  
10. **Inspection War Room** — 72h pack export — hashes visible — `not_executed`.

---

## 6. Synthetic demo data created

All under `submission/demo_data/` — overlays for UI richness; join keys match challenge CSVs (`product_id`, `batch_id`, `shipment_id`, etc.). Challenge `data/` and `evaluation/` are **not** modified.

| File | Role |
|---|---|
| `README.md` | Mapping & rules |
| `live_cases.csv` | Control Centre cards |
| `portfolio_pressure_board.csv` | Portfolio Command metrics |
| `twin_nodes.csv` / `twin_edges.csv` | Twin Studio graph |
| `review_by_exception_queue.csv` | RBE workbench |
| `cross_impact_links.csv` | Cross-Impact Graph |
| `obligation_register.csv` | Obligations Desk |
| `guidance_case_studies.csv` | Defence patterns |
| `exclusivity_brief_outline.csv` | NCX-101 human brief |
| `patient_impact_sla.csv` | NCS-310 / NCR-415 urgency |
| `demo_ui_microcopy.csv` | Descriptive labels / coach marks |
| `inspection_war_room_tasks.csv` | IR-72H task board |

---

## 7. Non-negotiables (repeat for demo facilitators)

- No autonomous batch disposition, PV finals, allocate/ship/recall, patent filing, or clinical eligibility.
- Unresolved unit / identity / authority / time → abstain, keep visible.
- Synthetic demo rows must cite or join real challenge keys; never silently normalize conflicting SoR values.

---

*End of artefact 40.*
