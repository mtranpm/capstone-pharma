# AEGIS-PHARMA — Event Storming (Graphical Board)

| Field | Entry |
|---|---|
| Owner | Architecture / domain lead |
| Version / date | 1.0.0 / 2026-08-16 |
| Audience | Leadership presentation, defence |
| Sources | `Docs/DDD-Lab/Phase 6/A6_Event_Storming_Board.md` (44 events), `A5` context map |

## Legend

```
 [event]   workflow / evidence event        [!]  exception / conflict (stays visible)
 [H]       human decision (never AI)        [A]  no-answer / abstention (fail-closed)
 [E]       audit / continuity event         [R]  regulatory event
```

---

## Master timeline — four lanes

```
  LANE 1  BATCH (PUB-01..03)
  ───────────────────────────────────────────────────────────────────────────────
  [Open batch review NCB204-B24071] ──► [Identity/product-master checked]
        │                                          │
        ▼                                          ▼
  [Genealogy check requested] ──► [!Genealogy gap SUA-88] ──► [Warehouse record found]
        │                                                      (contradiction visible)
        ▼
  [!Unit conflict mg/L vs µg/mL] ──► [A Unit state unresolved, no-answer]
        │
        ▼
  [!OOS/OOT/invalid dispute] ──► [!Sterile-area excursion] ──► [!Organism ID corrected]
        │
        ▼
  [!Supplier-audit commitment unverified] ──► [!Back-entered batch-record step]
        │
        ▼
  [!Release packet evidence-incomplete] ──► [Batch-review readiness assessed, gaps open]
        │
        ▼
  [H QP certification pending — human, AI prepares evidence only]

  LANE 2  PV INTAKE (PUB-04..06)
  ───────────────────────────────────────────────────────────────────────────────
  [PV case intake opened] ──► [Consent/entitlement check requested]
        │
        ▼
  [!ICSR duplicate cluster (PV-1001/1009/1014)] ──► [!Awareness-date dispute]
        │
        ▼
  [!MedDRA version mismatch] ──► [!Listedness conflict IB vs CCDS vs label]
        │
        ▼
  [Reporting-clock evidence prepared] ──► [Multilingual review requested]
        │
        ▼
  [Case-review material prepared] ──► [H Accountable PV review — never AI final PV]

  LANE 3  SUPPLY (PUB-07..08)
  ───────────────────────────────────────────────────────────────────────────────
  [!Cold-chain excursion (logger/pallet dispute)] ──► [!Case-to-pallet aggregation gap]
        │
        ▼
  [!Serialisation aggregation gap] ──► [!Excipient shortage (8-wk recovery)]
        │
        ▼
  [!CMO capacity conflict] ──► [Allocation constraint check completed]
        │
        ▼
  [Allocation option proposed — advisory, awaiting approval] ──► [H Approval requested]
                                                                    (never executed by AI)

  LANE 4  CROSS-CUTTING (PUB-09..15)
  ───────────────────────────────────────────────────────────────────────────────
  [!Validation state ambiguous] ──► [Master-data repair window opened]
        │
        ▼
  [E Audit record captured] ──► [!E Audit-capture gap detected (47 min)]
        │
        ▼
  [E AI-off continuity mode activated] ──► [R Inspection request received (72h)]
        │
        ▼
  [Evidence package assembled] ──► [Escalation created] ──► [A No-answer where unresolved]
        │
        ▼
  [H Human approval recorded] ──► [H Human override recorded]
```

---

## Key board facts

| Fact | Value |
|---|---|
| Total events | **44** (16 batch, 9 PV, 8 supply, 11 cross-cutting) |
| Exception events (stay visible, never resolved silently) | SUA-88, mg/L vs µg/mL, OOS/OOT, supplier commitment, back-entered step, duplicates, awareness date, MedDRA, listedness, cold-chain, aggregation, shortage, CMO, validation, 47-min gap |
| Abstention (no-answer) | Required whenever identity, unit, authority, as-of, consent, validation or checkpoint state is unresolved |
| Human-decision events | QP certification · PV seriousness/causality/expectedness/reportability/signal · allocation approval · overrides |
| Audit events | Every recommendation, draft, approval, override, escalation, action and closure |

## Boundary reminders (from A6 §11)

- Opening a review ≠ release approval; readiness ≠ QP certification.
- Intake ≠ final PV disposition; the reporting clock is never set by AI.
- An allocation option is never an executed allocation.
- Gaps are surfaced as unresolved domain state — never repaired, merged, or guessed.
- Audit is part of the workflow, not an afterthought.

Full row-level board (command, actor, policy, evidence source, failure condition, audit need) is in `Docs/DDD-Lab/Phase 6/A6_Event_Storming_Board.md`.
