# 39 — All Personas Mapped to Batch, Pharmacovigilance, and Supply Workflows

| Field | Entry |
|---|---|
| Owner | Product / domain lead |
| Version / date | 1.0.0 / 2026-08-12 |
| Status | Phase 3 companion — persona × workflow end-to-end flows |
| Naming rule | Full forms preferred; avoid unexplained acronyms |
| Three mandatory workflows | **1. Batch evidence readiness** · **2. Pharmacovigilance intake support** · **3. Supply recovery optioning** |
| Note on “Supplier” | Supplier Quality is a **persona** inside Batch (and sometimes Supply). The third workflow is **Supply** (shortage / cold-chain recovery), not a separate “Supplier workflow”. |
| Sources | `38_persona_current_state_system_flows.md`, `03`, `05`, `06`, `case/STAKEHOLDER_PACK.md`, `case/SOURCE_SYSTEM_FACT_PACK.md`, `PRD_AEGIS_Google_AI_Studio.md` |

---

## 1. Purpose

Provide a **detailed end-to-end flow for each of the three mandatory workflows**, with **every persona** mapped as Primary, Supporting, Informed, or Out of lane — including designation, team, systems touched, and human-only decisions.

---

## 2. Master persona register

| Identifier | Name | Designation | Team |
|---|---|---|---|
| P-QP | Elena Vargas | European Union Qualified Person | Quality Release, Ireland site |
| P-QR | James Okonkwo | Quality Release Reviewer | Batch Review Coordination, Quality Operations |
| P-SQ | Nadia Hussain | Supplier Quality Specialist | Supplier Quality, Quality Operations |
| P-LAB | Dr. Helen Cho | Laboratory Investigation Owner | Analytical Laboratory / Out-of-Specification investigations |
| P-MFG | Michael Brandt | Manufacturing Operations Director | Manufacturing / Sterile Fill-Finish |
| P-INT | Priya Nair | Pharmacovigilance Case Intake Coordinator | Global Pharmacovigilance Operations |
| P-MED | Dr. Markus Keller | Pharmacovigilance Medical Reviewer | Global Pharmacovigilance Medical Review |
| P-PVH | Dr. Amira Soliman | Global Head of Pharmacovigilance | Global Pharmacovigilance Leadership |
| P-SP | Sofia Almeida | Supply Planning Lead | Global Supply Chain Planning |
| P-QG | Tomás Rivera | Quality Status Gatekeeper | Quality Operations (inventory status) |
| P-LOG | Diego Fernández | Logistics and Cold-Chain Coordinator | Global Logistics |
| P-CMO | Ananya Krishnan | Contract Manufacturing Organization Planner | External Manufacturing Coordination |
| P-RA | Aisha Rahman | Regulatory Affairs Manager | Global Regulatory Affairs |
| P-CQO | Dr. Ruth Okeke | Chief Quality Officer | Pharmaceutical Quality System leadership |
| P-SEC | Chen Wei | Chief Information Security Officer delegate | Cybersecurity and Resilience |
| P-DPO | Laura Mendes | Data Protection Officer | Privacy and Data Protection Office |
| P-PSR | Samira Ali | Patient Safety Representative | Patient and participant voice / safety governance |
| P-PRC | Oliver Grant | Procurement Manager | Procurement and vendor assurance |
| P-PLT | Kai Nakamura | Platform / Continuity Engineer | Digital Platform and Operations |

### 2.1 Persona × workflow participation matrix

| Persona | 1. Batch | 2. Pharmacovigilance | 3. Supply |
|---|---|---|---|
| European Union Qualified Person (Elena Vargas) | **Primary accountable** | Informed if product-quality / safety link | Informed if recall / quality hold |
| Quality Release Reviewer (James Okonkwo) | **Primary operator** | Supporting if complaint–batch link | Supporting on quality holds |
| Supplier Quality Specialist (Nadia Hussain) | **Supporting (supplier evidence)** | Rare | Supporting (Contract Manufacturing Organization / material constraints) |
| Laboratory Investigation Owner (Dr. Helen Cho) | **Supporting (laboratory evidence)** | Rare | Out of lane |
| Manufacturing Operations Director (Michael Brandt) | **Supporting / pressure for speed** | Out of lane | Supporting (capacity / schedule) |
| Pharmacovigilance Case Intake Coordinator (Priya Nair) | Informed if product complaint link | **Primary operator** | Out of lane |
| Pharmacovigilance Medical Reviewer (Dr. Markus Keller) | Informed if quality–safety link | **Primary accountable (finals)** | Out of lane |
| Global Head of Pharmacovigilance (Dr. Amira Soliman) | Escalation only | **Escalation / policy** | Escalation if shortage ethics / safety |
| Supply Planning Lead (Sofia Almeida) | Informed on holds affecting service | Out of lane | **Primary operator** |
| Quality Status Gatekeeper (Tomás Rivera) | Supporting on inventory status | Out of lane | **Primary gate (execution approvals)** |
| Logistics and Cold-Chain Coordinator (Diego Fernández) | Supporting if warehouse / distribution | Out of lane | **Supporting (cold-chain / serialisation)** |
| Contract Manufacturing Organization Planner (Ananya Krishnan) | Supporting (site capacity / genealogy) | Out of lane | **Supporting (capacity)** |
| Regulatory Affairs Manager (Aisha Rahman) | Supporting (commitments / inspection) | Supporting (labelling / listedness sources) | Supporting (market authorisation constraints) |
| Chief Quality Officer (Dr. Ruth Okeke) | Escalation / policy | Escalation | Escalation |
| Chief Information Security Officer delegate (Chen Wei) | Cross-cutting control | Cross-cutting control | Cross-cutting control |
| Data Protection Officer (Laura Mendes) | Light (batch data) | **Supporting (narratives / purpose)** | Light |
| Patient Safety Representative (Samira Ali) | Contestability | Contestability | Contestability |
| Procurement Manager (Oliver Grant) | Supporting (vendor / audit contracts) | Out of lane | Supporting (vendor exit / capacity contracts) |
| Platform / Continuity Engineer (Kai Nakamura) | Cross-cutting continuity | Cross-cutting continuity | Cross-cutting continuity |

---

## 3. Workflow 1 — Batch evidence readiness

| Field | Entry |
|---|---|
| Intent | Assemble conflict-visible evidence for batch review / European Union certification support |
| Public fixtures | PUB-01, PUB-02, PUB-03 |
| Example object | Biologics batch `NCB204-B24071` |
| Primary operator | Quality Release Reviewer (James Okonkwo) |
| Primary accountable decision | European Union Qualified Person (Elena Vargas) — **outside AEGIS** |
| AEGIS role (future) | Advisory packet only; `execution_status = not_executed` |
| Must never | Release, reject, reprocess, relabel, or recall a batch |

### 3.1 Persona roles in Batch

| Persona | Role in Batch flow | Systems they interact with |
|---|---|---|
| Quality Release Reviewer | Assembles evidence; runs reconciliation; prepares packet | Manufacturing Execution System; Electronic Batch Record; warehouse management; Laboratory Information Management System; Electronic Quality Management System; supplier quality; document management |
| European Union Qualified Person | Reviews pack; decides certification or hold | Electronic Quality Management System; release packet; cited Manufacturing / Laboratory extracts |
| Supplier Quality Specialist | Confirms supplier / Contract Manufacturing Organization audit commitments | Supplier quality module; vendor portals; audit reports |
| Laboratory Investigation Owner | Clarifies out-of-specification / out-of-trend / invalid states | Laboratory Information Management System; Chromatography Data System; notebooks; statistical tooling |
| Manufacturing Operations Director | Explains schedule / downtime / genealogy context; pressures cycle time | Manufacturing Execution System; Electronic Batch Record; Enterprise Resource Planning schedule |
| Regulatory Affairs Manager | Confirms registration / commitment applicability for release evidence | Regulatory Information Management; document management; labelling |
| Chief Quality Officer | Escalation on systemic risk / inspection posture | Pharmaceutical quality system dashboards; Electronic Quality Management System |
| Procurement Manager | Vendor contractual evidence for audits | Procurement contracts; vendor management |
| Logistics coordinator | Warehouse movement confirmation for genealogy | Warehouse management; serialisation if packing-related |
| Contract Manufacturing Organization Planner | Site genealogy / capacity clarifications | Contract Manufacturing Organization portals; Manufacturing Execution System extracts |
| Data Protection Officer | Rare; personal data in deviations if present | Purpose registers |
| Chief Information Security Officer delegate | If tool / access / ransomware degrades Manufacturing Execution System or Electronic Quality Management System | Identity and access management; incident registers |
| Platform engineer | Continuity / offline evidence path | Platform monitoring |
| Patient Safety Representative | Contests opaque rationale after the fact | Safety governance forum |
| Pharmacovigilance Intake / Medical Reviewer | Enter only if product-quality complaint links to batch | Global safety database; product complaints |
| Supply Planning / Quality Status Gatekeeper | Informed when hold blocks supply | Inventory quality status |

### 3.2 Detailed Batch end-to-end flow (all personas)

```mermaid
flowchart TB
  subgraph Trigger["1. Trigger"]
    T1[Batch NCB204-B24071 enters quality hold / pending review]
    T1 --> QR[Quality Release Reviewer<br/>James Okonkwo]
  end

  subgraph Gather["2. Evidence gathering — parallel system pulls"]
    QR --> MES[Manufacturing Execution System<br/>genealogy]
    QR --> EBR[Electronic Batch Record]
    QR --> WHS[Warehouse management<br/>movements]
    QR --> LIMS[Laboratory Information Management System]
    QR --> STAT[Statistical trend tooling]
    QR --> EQMS[Electronic Quality Management System<br/>deviations / holds]
    QR --> SQ[Supplier Quality Specialist<br/>Nadia Hussain]
    SQ --> AUD[Supplier audit / Contract Manufacturing Organization commitments]
    QR --> LAB[Laboratory Investigation Owner<br/>Dr. Helen Cho]
    LAB --> CDS[Chromatography Data System / notebooks]
    QR --> MFG[Manufacturing Operations Director<br/>Michael Brandt]
    MFG --> SCH[Schedule / downtime context]
    QR --> RA[Regulatory Affairs Manager<br/>Aisha Rahman]
    RA --> RIM[Regulatory Information Management commitments]
  end

  subgraph Conflicts["3. Conflicts surfaced — current state manual"]
    MES -.->|missing single-use assembly lot SUA-88| C1[Genealogy break]
    WHS -.->|lot consumed in warehouse| C1
    LIMS -.->|milligrams per litre vs micrograms per millilitre| C2[Unit mismatch]
    LIMS -.->|out of specification| C3[Out-of-specification / out-of-trend / invalid dispute]
    STAT -.->|out of trend| C3
    CDS -.->|invalid in notebook| C3
    AUD -.->|unverified audit commitment| C4[Authority gap]
  end

  subgraph Review["4. Human review chain"]
    C1 --> PACK[Draft release evidence pack]
    C2 --> PACK
    C3 --> PACK
    C4 --> PACK
    PACK --> QR2[Quality Release Reviewer checklist]
    QR2 --> QP[European Union Qualified Person<br/>Elena Vargas]
    QP -->|escalate systemic risk| CQO[Chief Quality Officer<br/>Dr. Ruth Okeke]
    QP -->|product-quality to safety link?| PVX[Pharmacovigilance Intake informed]
    QP -->|hold impacts service| SPX[Supply Planning informed]
  end

  subgraph Decide["5. Regulated decision — outside orchestration"]
    QP -->|Certify OR Hold / Reject<br/>human only in Electronic Quality Management System| OUT[Batch disposition recorded]
    PSR[Patient Safety Representative<br/>may contest rationale later]
    OUT -.-> PSR
  end

  subgraph Controls["Cross-cutting controls anytime"]
    SEC[Chief Information Security Officer delegate]
    PLT[Platform / Continuity Engineer]
    DPO[Data Protection Officer]
    SEC -.->|emergency stop / poisoned tools| QR
    PLT -.->|offline continuity| QR
    DPO -.->|purpose check if personal data| QR
  end
```

### 3.3 Batch sequence (persona swimlane)

```mermaid
sequenceDiagram
  participant MFG as Manufacturing Director
  participant LAB as Laboratory Owner
  participant SQ as Supplier Quality
  participant QR as Quality Release Reviewer
  participant RA as Regulatory Affairs
  participant QP as European Union Qualified Person
  participant CQO as Chief Quality Officer
  participant SP as Supply Planning

  MFG->>QR: Genealogy / downtime context from Manufacturing Execution System
  LAB->>QR: Laboratory results and investigation state
  SQ->>QR: Supplier / Contract Manufacturing Organization audit status
  RA->>QR: Applicable commitments / documents
  QR->>QR: Manual merge — conflicts remain visible
  QR->>QP: Evidence pack for certification review
  alt Evidence incomplete or conflicted
    QP->>CQO: Escalate risk acceptance / inspection posture
    QP->>QR: Request more evidence — no certification
  else Evidence accepted by Qualified Person
    QP->>QP: Human certification or hold in Electronic Quality Management System
    QP-->>SP: Notify if hold constrains supply
  end
```

---

## 4. Workflow 2 — Pharmacovigilance intake support

| Field | Entry |
|---|---|
| Intent | Prepare intake evidence: duplicates, clocks, terminology, listedness, multilingual preservation |
| Public fixtures | PUB-04, PUB-05, PUB-06 |
| Example objects | Cases `PV-1001`, `PV-1009`, `PV-1014` |
| Primary operator | Pharmacovigilance Case Intake Coordinator (Priya Nair) |
| Primary accountable finals | Pharmacovigilance Medical Reviewer (Dr. Markus Keller) — **outside AEGIS** |
| Escalation | Global Head of Pharmacovigilance (Dr. Amira Soliman) |
| Must never | Final seriousness, causality, expectedness, reportability, or signal confirmation |

### 4.1 Persona roles in Pharmacovigilance

| Persona | Role in Pharmacovigilance flow | Systems they interact with |
|---|---|---|
| Pharmacovigilance Case Intake Coordinator | Triage; assemble intake packet; preserve narratives | Global safety database; affiliate inboxes; vendor portals; call centre; literature feeds |
| Pharmacovigilance Medical Reviewer | Final medical / regulatory safety decisions | Global safety database; labelling / brochure sources |
| Global Head of Pharmacovigilance | Policy, escalation, system performance | Pharmacovigilance governance; metrics |
| Data Protection Officer | Purpose binding; minimisation of narratives / personal data | Purpose registers; residency; telemetry rules |
| Regulatory Affairs Manager | Listedness / labelling source authority | Labelling system; core data sheet; local label; investigator brochure |
| Quality Release / Qualified Person | Enter if product-quality complaint links to batch | Electronic Quality Management System; product complaints; batch history |
| Patient Safety Representative | Contestability of opaque intake / medical rationale | Safety governance forum |
| Chief Information Security Officer delegate | Access revocation / tool poisoning during case handling | Identity and access management; artificial intelligence gateway |
| Platform engineer | Continuity during outage of safety database region | Continuity runbooks |
| Chief Quality Officer | Joint escalation on quality–safety signals | Quality governance |
| Laboratory / Manufacturing / Supply personas | Generally out of lane unless quality–safety linkage | — |

### 4.2 Detailed Pharmacovigilance end-to-end flow (all personas)

```mermaid
flowchart TB
  subgraph Trigger["1. Trigger — multi-channel intake"]
    CALL[Call centre] --> INT[Pharmacovigilance Case Intake Coordinator<br/>Priya Nair]
    AFF[Affiliate inbox] --> INT
    VEND[Vendor portal] --> INT
    LIT[Literature vendor] --> INT
  end

  subgraph Gather["2. Evidence gathering"]
    INT --> GSDB[Global safety database]
    INT --> MEDDRA[Medical Dictionary for Regulatory Activities]
    INT --> LABL[Core data sheet / local label / investigator brochure]
    INT --> RA[Regulatory Affairs Manager<br/>Aisha Rahman — listedness sources]
    INT --> DPO[Data Protection Officer<br/>Laura Mendes — purpose / minimisation]
    INT --> COMP[Product complaint system]
    COMP -->|particle / quality link?| QR[Quality Release Reviewer informed]
  end

  subgraph Conflicts["3. Conflicts surfaced"]
    AFF -.->|awareness date A| CLK[Awareness / reporting clock conflict]
    VEND -.->|awareness date B| CLK
    GSDB -.->|awareness date C| CLK
    GSDB -.->|possible duplicates PV-1001 / 1009 / 1014| DUP[Duplicate uncertainty]
    MEDDRA -.->|dictionary version mismatch| TERM[Terminology conflict]
    LABL -.->|listedness disagreement across sources| LIST[Listedness evidence conflict]
    CALL -.->|Arabic / German / English narratives| LANG[Multilingual preservation required]
  end

  subgraph Review["4. Human review chain"]
    CLK --> PACK[Intake support packet]
    DUP --> PACK
    TERM --> PACK
    LIST --> PACK
    LANG --> PACK
    PACK --> INT2[Intake checklist — no silent translation]
    DPO --> INT2
    INT2 --> MED[Pharmacovigilance Medical Reviewer<br/>Dr. Markus Keller]
    MED -->|escalate| PVH[Global Head of Pharmacovigilance<br/>Dr. Amira Soliman]
    MED -->|quality linked| QP[European Union Qualified Person / Quality informed]
  end

  subgraph Decide["5. Regulated decisions — outside orchestration"]
    MED -->|Human finals in global safety database| FIN[Seriousness / causality / expectedness / reportability / signal]
    PSR[Patient Safety Representative may contest]
    FIN -.-> PSR
  end

  subgraph Controls["Cross-cutting"]
    SEC[Chief Information Security Officer delegate]
    PLT[Platform / Continuity Engineer]
    SEC -.-> INT
    PLT -.-> INT
  end
```

### 4.3 Pharmacovigilance sequence (persona swimlane)

```mermaid
sequenceDiagram
  participant CH as Call centre / Affiliate / Vendor
  participant INT as Pharmacovigilance Intake
  participant DPO as Data Protection Officer
  participant RA as Regulatory Affairs
  participant MED as Pharmacovigilance Medical Reviewer
  participant PVH as Global Head of Pharmacovigilance
  participant QR as Quality Release optional

  CH->>INT: Case narratives and receipts
  INT->>INT: Load global safety database + terminology
  RA->>INT: Labelling / listedness source context
  DPO->>INT: Purpose binding and narrative minimisation rules
  INT->>INT: Surface duplicates, clocks, language — do not merge or finalise
  INT->>MED: Intake support packet
  opt Quality–safety linkage
    INT->>QR: Notify product complaint / batch link
  end
  MED->>MED: Human finals in global safety database
  alt High uncertainty or signal concern
    MED->>PVH: Escalate
  end
```

---

## 5. Workflow 3 — Supply recovery optioning

| Field | Entry |
|---|---|
| Intent | Produce **non-executing** recovery options under quality, ethics, cold-chain, and capacity constraints |
| Public fixtures | PUB-07, PUB-08 |
| Example objects | `NCB-204` shortage; cold-chain / serialisation disputes |
| Primary operator | Supply Planning Lead (Sofia Almeida) |
| Primary execution gate | Quality Status Gatekeeper (Tomás Rivera) — **outside AEGIS** |
| Must never | Allocate, reserve, ship, change inventory quality status, or initiate recall without authorized human approval |

### 5.1 Persona roles in Supply

| Persona | Role in Supply flow | Systems they interact with |
|---|---|---|
| Supply Planning Lead | Builds option set; documents constraints | Demand planning; inventory; allocation tools; Contract Manufacturing Organization portals |
| Quality Status Gatekeeper | Approves any quality-status or release-to-ship path | Electronic Quality Management System; inventory quality status in Enterprise Resource Planning / warehouse |
| Logistics and Cold-Chain Coordinator | Logger / pallet / transport evidence | Cold-chain monitoring; serialisation; transport management |
| Contract Manufacturing Organization Planner | Capacity and external site constraints | Contract Manufacturing Organization portals |
| Manufacturing Operations Director | Internal capacity / schedule | Manufacturing Execution System; Enterprise Resource Planning schedule |
| European Union Qualified Person / Quality Release | Informed if batch hold drives shortage; recall consultation | Electronic Quality Management System; batch status |
| Supplier Quality Specialist | Material / supplier constraint evidence | Supplier quality; vendor portals |
| Regulatory Affairs Manager | Market authorisation / distribution constraints | Regulatory Information Management; registrations |
| Global Head of Pharmacovigilance / Medical | Ethics input for trial vs compassionate vs commercial | Medical / ethics forums |
| Procurement Manager | Vendor capacity contracts / exit terms | Procurement systems |
| Chief Quality Officer | Escalation on patient-impacting allocation ethics | Quality governance |
| Patient Safety Representative | Contestability of opaque allocation rationale | Safety governance |
| Data Protection Officer | Light touch unless patient-level logistics data | Purpose registers |
| Chief Information Security Officer delegate / Platform | Continuity and stop controls | Security / platform tooling |
| Pharmacovigilance Intake | Out of lane unless shortage links to safety communications | — |

### 5.2 Detailed Supply end-to-end flow (all personas)

```mermaid
flowchart TB
  subgraph Trigger["1. Trigger"]
    T1[Excipient shortage / cold-chain dispute / service risk on NCB-204]
    T1 --> SP[Supply Planning Lead<br/>Sofia Almeida]
  end

  subgraph Gather["2. Evidence gathering — parallel"]
    SP --> PLAN[Demand forecast<br/>commercial / trial / compassionate]
    SP --> INV[Inventory / warehouse<br/>released vs quarantine]
    SP --> ALLOC[Allocation constraint tools]
    SP --> LOG[Logistics and Cold-Chain Coordinator<br/>Diego Fernández]
    LOG --> CC[Cold-chain loggers]
    LOG --> SER[Serialisation / aggregation]
    LOG --> TMS[Transport management]
    SP --> CMO[Contract Manufacturing Organization Planner<br/>Ananya Krishnan]
    CMO --> CMOP[Contract Manufacturing Organization portals]
    SP --> MFG[Manufacturing Operations Director<br/>Michael Brandt]
    SP --> SQ[Supplier Quality Specialist<br/>Nadia Hussain]
    SP --> RA[Regulatory Affairs Manager<br/>Aisha Rahman]
    RA --> RIM[Market authorisation constraints]
    SP --> PRC[Procurement Manager<br/>Oliver Grant]
  end

  subgraph Conflicts["3. Conflicts surfaced"]
    CC -.->|logger clock / pallet mismatch| X1[Cold-chain identity / time dispute]
    SER -.->|aggregation break| X2[Serialisation gap]
    INV -.->|quarantine stock vs released-only rule| X3[Quality status constraint]
    PLAN -.->|trial vs compassionate vs commercial demand| X4[Ethics / priority conflict]
    CMOP -.->|capacity conflict| X5[Capacity shortfall]
  end

  subgraph Options["4. Non-executing options only"]
    X1 --> OPT[Draft options pack]
    X2 --> OPT
    X3 --> OPT
    X4 --> OPT
    X5 --> OPT
    OPT --> O1[Option: prioritise review of released-stock visibility]
    OPT --> O2[Option: escalate ethics / Quality for demand conflict]
    OPT --> O3[Option: document shortfall — do not allocate or ship]
  end

  subgraph Review["5. Human review chain"]
    O1 --> SP2[Supply Planning checklist]
    O2 --> SP2
    O3 --> SP2
    SP2 --> QG[Quality Status Gatekeeper<br/>Tomás Rivera]
    QG --> EQMS[Electronic Quality Management System]
    QG -->|batch-driven hold / recall consult| QP[European Union Qualified Person informed]
    QG -->|patient-impact ethics| CQO[Chief Quality Officer / medical ethics]
    QG -->|safety communications| PVH[Global Head of Pharmacovigilance informed]
  end

  subgraph Decide["6. Regulated execution — outside orchestration"]
    QG -->|Human approvals only| EXE[Allocation / shipment / inventory status change / recall]
    PSR[Patient Safety Representative may contest]
    EXE -.-> PSR
  end

  subgraph Controls["Cross-cutting"]
    SEC[Chief Information Security Officer delegate]
    PLT[Platform / Continuity Engineer]
    DPO[Data Protection Officer]
    SEC -.-> SP
    PLT -.-> SP
    DPO -.-> SP
  end
```

### 5.3 Supply sequence (persona swimlane)

```mermaid
sequenceDiagram
  participant LOG as Logistics / Cold-Chain
  participant CMO as Contract Manufacturing Organization Planner
  participant MFG as Manufacturing Director
  participant SP as Supply Planning Lead
  participant RA as Regulatory Affairs
  participant QG as Quality Status Gatekeeper
  participant QP as European Union Qualified Person
  participant ETH as Chief Quality Officer / Ethics

  LOG->>SP: Cold-chain and serialisation evidence
  CMO->>SP: External capacity
  MFG->>SP: Internal schedule / capacity
  RA->>SP: Market authorisation constraints
  SP->>SP: Build draft non-executing options — no ship / allocate
  SP->>QG: Options pack + quality holds
  alt Quality or ethics block
    QG->>QP: Consult on batch / recall implications
    QG->>ETH: Escalate trial vs compassionate vs commercial
    QG->>SP: No execution — document abstention
  else Authorized humans approve in source systems
    QG->>QG: Human inventory status / allocation / shipment approvals outside advisory tool
  end
```

---

## 6. Cross-workflow persona map (one view)

```mermaid
flowchart LR
  subgraph BatchWF["1. Batch workflow"]
    QR[Quality Release Reviewer]
    QP[European Union Qualified Person]
    SQ[Supplier Quality]
    LAB[Laboratory Owner]
    MFG[Manufacturing Director]
  end

  subgraph PVWF["2. Pharmacovigilance workflow"]
    INT[Pharmacovigilance Intake]
    MED[Pharmacovigilance Medical Reviewer]
    PVH[Global Head of Pharmacovigilance]
    DPO[Data Protection Officer]
  end

  subgraph SupWF["3. Supply workflow"]
    SP[Supply Planning Lead]
    QG[Quality Status Gatekeeper]
    LOG[Logistics / Cold-Chain]
    CMO[Contract Manufacturing Organization Planner]
  end

  subgraph Shared["Shared across all three"]
    RA[Regulatory Affairs]
    CQO[Chief Quality Officer]
    SEC[Chief Information Security Officer delegate]
    PLT[Platform Continuity]
    PSR[Patient Safety Representative]
    PRC[Procurement]
  end

  QR --> QP
  INT --> MED --> PVH
  SP --> QG
  RA --- BatchWF
  RA --- PVWF
  RA --- SupWF
  CQO --- BatchWF
  CQO --- PVWF
  CQO --- SupWF
  SEC --- BatchWF
  SEC --- PVWF
  SEC --- SupWF
  QP -.->|hold impacts service| SP
  INT -.->|quality–safety link| QR
  QG -.->|recall / hold consult| QP
```

---

## 7. Human review gates by workflow

| Gate | Batch | Pharmacovigilance | Supply |
|---|---|---|---|
| Pre-export packet | Quality Release / Qualified Person delegate | Pharmacovigilance Intake lead | Supply Planning Lead |
| Authority unresolved | Quality or Regulatory Affairs | Quality or Regulatory Affairs | Quality or Regulatory Affairs |
| Abstention override | Workflow owner + Quality | Workflow owner + Quality | Workflow owner + Quality |
| Security poisoned tool | Chief Information Security Officer delegate | Same | Same |
| Multilingual narrative | — | Pharmacovigilance Intake (+ Data Protection Officer if needed) | — |
| Non-executing options | — | — | Supply Planning + Quality Status Gatekeeper |

---

## 8. What each workflow must never automate

| Workflow | Prohibited autonomous outcomes |
|---|---|
| Batch | Release, reject, reprocess, relabel, recall |
| Pharmacovigilance | Final seriousness, causality, expectedness, reportability, signal confirmation |
| Supply | Allocate, reserve, ship, change inventory quality status, initiate recall |

---

## 9. Traceability

| Artefact | Relationship |
|---|---|
| `38_persona_current_state_system_flows.md` | Persona examples and current-state system diagrams |
| `03_stakeholders_decision_rights.md` | Decision rights |
| `05_product_operating_model.md` | Jobs-to-be-done |
| `06_human_oversight_and_emergency_stop.md` | Gates |
| `PRD_AEGIS_Google_AI_Studio.md` | Future advisory product |
| `13_requirements_traceability_matrix.md` | BAT / PV / SUP requirements |

---

*End of artefact 39 — All personas mapped to Batch, Pharmacovigilance, and Supply workflows.*
