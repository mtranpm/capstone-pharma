# 27 — Assurance Case & Residual Risk

| Field | Entry |
|---|---|
| Owner | Quality / Assurance |
| Version / date | 1.0.0 / 2026-08-10 |
| Status | Phase 5 — GSN-style outline |
| Sources | `25`, `23`, `28`, `32`, CAE / GSN practice |

---

## 1. Top-level claim

**C-1:** AEGIS, when operated within intended use (`22`), provides **advisory, contract-valid, provenance-backed evidence packets** such that accountable humans retain regulated decisions, with acceptable residual risk for NovaCura pilot deployment.

---

## 2. Argument structure (GSN sketch)

```text
C-1
├── S-1: Scope excludes autonomous regulated acts (NN-01..03) — STRATEGY: definition
│   └── E-1: SCQA + RTM + prohibited.py tests [pending full OQ]
├── S-2: Evidence integrity preserved — STRATEGY: ALCOA
│   └── E-2: BAT-02 tests, audit schema `24` [pending]
├── S-3: Unsafe AI behaviour contained — STRATEGY: defence in depth
│   ├── E-3: Tool manifest + budgets `19`,`20`
│   ├── E-4: OWASP controls `28` → tests T-LLM-*
│   └── E-5: Human gates G-HR `06`
├── S-4: Continuity under failure — STRATEGY: degrade
│   └── E-6: Offline path `16`,`21` [pending PUB-10 run]
└── S-5: Governance maintained — STRATEGY: AIMS
    └── E-7: `26`, change control `23`
```

---

## 3. Residual risks (accepted for workshop)

| RR-ID | Description | Severity | Justification | Owner |
|---|---|---|---|---|
| RR-01 | LLM hallucinated conflict explanation | Medium | Human review; not used for auto-disposition | QP delegate |
| RR-02 | Graph link misleading vs SoR | Low | advisory:true; SoR ids primary | Architecture |
| RR-03 | Stale read API snapshot | Medium | Timestamps + abstention | Platform |
| RR-04 | κ < 0.6 on advisory labels | Medium | Soft threshold only; no auto-release | QA |
| RR-05 | Inspection finds audit gap | Medium | OQ pending | Validation |

**Not accepted without redesign:** any path to NN-01..03 execution.

---

## 4. Evidence status

| Evidence | Status |
|---|---|
| Contract tests | **Pending** green run |
| Eval graders G-* | **Pending** |
| Red-team report | **Pending** `31` |
| Production pilot OQ | Out of scope workshop |

---

## 5. Sign-off (target)

| Role | Workshop | Production |
|---|---|---|
| Quality | Review outline | Full acceptance |
| RA | Intended use | Labeling |
| CISO | Security tests | KS drills |
| DPO | Privacy `30` | DPIA |

---

## 6. Link to defence

[`37`](37_production_readiness_roadmap_defence.md) §5 — assurance summary for Gate 7.
