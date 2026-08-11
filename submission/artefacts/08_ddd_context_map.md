# 08 — DDD Context Map (Submission Synthesis)

| Field | Entry |
|---|---|
| Owner | Architecture / domain lead |
| Version | 0.1.0 |
| Status | Phase 4 — synthesised from DDD-Lab |
| Sources | `Docs/DDD-Lab/Phase 2/A2`, `Phase 4/A4`, `Phase 5/A5`, `Phase 7/A7`; [`09`](09_data_governance_lineage_contracts.md), [`SCQA.md`](SCQA.md) |

## 1. Purpose

Condense NovaCura’s ten DDD-Lab bounded contexts into **five programme views** (Batch, PV, Supply, Authority, Evidence) for implementation traceability while preserving regulated boundaries from A4/A5/A7.

**Immutable rule:** AI is read-only and advisory; contexts prepare evidence — they do not disposition batches, finalize PV, allocate stock, or initiate recall.

## 2. Five context views (mapped from A4)

| Programme context | DDD-Lab bounded contexts (A4) | Owns (business) | Does not own |
|---|---|---|---|
| **Batch** | GxP Batch Evidence Reconciliation; Identity/Genealogy/Product Master (upstream); Unit/Terminology (partnership); Supplier/Audit Evidence (upstream) | Batch-review **readiness**, release-packet completeness, OOS/OOT **visibility** | QP certification, release/reject/reprocess/recall |
| **PV** | PV Case Intake and Signal Support; Unit/Terminology; Consent/Entitlement/Privacy (gate) | Intake packets, duplicates, clock **evidence**, listedness **comparisons**, multilingual prep | Final seriousness, causality, expectedness, reportability, signal |
| **Supply** | Supply, Cold-Chain and Allocation Planning; Identity (aggregation); Supplier (CMO/excipient) | Recovery **options**, cold-chain evidence, constraint reports | Inventory status change, reservation, allocation, shipment, recall |
| **Authority** | Authority, Effective-Date and Jurisdiction; Source and Document Governance; Validation-state aspects | Which source wins **per object/jurisdiction/as-of**; trusted vs quarantined | Picking listedness “winner” for filing (human RA/PV) |
| **Evidence** | Audit, Evidence and Continuity; cross-cutting audit sink | Audit envelopes, continuity posture, inspection packaging trail | Underlying regulated decision |

Supporting contexts (Identity, Unit, Consent, Source, Supplier) appear as **upstream partners** — not merged into Batch/PV/Supply aggregates (A7 invariant).

## 3. Context map (relationships)

```text
                    ┌─────────────────────┐
                    │     Authority       │
                    │ (effective-date,    │
                    │  trust, jurisdiction)│
                    └──────────┬──────────┘
                               │ policy gate (fail-closed)
         ┌─────────────────────┼─────────────────────┐
         ▼                     ▼                     ▼
   ┌──────────┐          ┌──────────┐          ┌──────────┐
   │  Batch   │          │   PV     │          │  Supply  │
   │ readiness│          │  intake  │          │  options │
   └────┬─────┘          └────┬─────┘          └────┬─────┘
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │      Evidence       │
                    │ (audit, continuity, │
                    │  inspection export) │
                    └─────────────────────┘

Upstream partners (all workflows):
  Identity/Genealogy ──► Batch, PV (product link), Supply (aggregation)
  Unit/Terminology ──► Batch, PV, Supply
  Source Governance ──► Authority gate input
  Consent/Privacy ──► PV (+ audit retention constraints)
  Supplier/Audit ──► Batch release packet, Supply CMO/excipient
```

Relationship types (from A5): **upstream/downstream**, **partnership** (shared kernel terms), **policy gate** (Authority, Consent, Source).

## 4. Shared kernel (must not drift)

| Term / status | Cross-context risk if inconsistent |
|---|---|
| Batch identity (`NCB204-B24071`) | Wrong evidence bundle |
| Material lot / SUA-88 | Hidden genealogy break |
| Unit + conversion assumption status | 1000× concentration error |
| MedDRA / terminology state | Split or merged safety cases |
| Effective date / as-of | Wrong label or protocol version cited |
| Authority registry | Later timestamp mistaken for signed record |
| Evidence status (complete / flagged / unresolved) | False “ready” |
| Audit event envelope | 47-minute gap undetected |

## 5. Anti-corruption layers (implementation)

| Boundary | Corruption risk | ACL pattern in AEGIS |
|---|---|---|
| SoR CSV → domain | Silent unit conversion, merged IDs | Pydantic strict loaders; verbatim fields; `FixturePort` |
| Knowledge markdown → decisions | Untrusted PDF treated as SOP | `AuthorityPort` + catalog `trust` / `status` |
| Graph → SoR | KG edge overrides batch status | `GraphPort` responses tagged `advisory: true`; never write SoR |
| LLM narrative → PV case | “Corrected” patient text | Separate advisory translation field; gate G-HR-05 |
| External tool manifest → agent | Poisoned tool execution | `ToolManifestPort`; quarantine |
| ERP/WMS semantics → Supply UI | “Ship now” affordance | Non-executing option contract; NN-03 guards |

ACLs live in **adapters** (`submission/src/aegis/adapters/*`), not in domain aggregates — per hexagonal ports spec.

## 6. Case gaps placed by context (unchanged from A2)

| Gap | Primary context |
|---|---|
| SUA-88 genealogy break | Batch (+ Identity partner) |
| mg/L vs µg/mL | Batch (+ Unit partner) |
| Duplicate ICSR / awareness date / MedDRA / listedness | PV (+ Authority, Unit) |
| Logger clock / pallet / serialisation aggregation | Supply (+ Identity) |
| Excipient shortage / CMO capacity | Supply (+ Supplier) |
| Untrusted supplier PDF | Authority (+ Source) |
| Audit-capture gap | Evidence |

Gaps remain **visible**; synthesis does not resolve them.

## 7. Traceability

| Submission artefact | DDD source |
|---|---|
| This file | A2 subdomain map, A4 canvases, A5 matrix, A7 invariants |
| Ontology `10` | A3 glossary terms + A7 object register |
| RTM `13` | Workflows Batch/PV/Supply ↔ contexts above |
| DDD index | [`ddd/README.md`](ddd/README.md) |

## 8. Workshop context list (full A4 names)

For audit against DDD-Lab originals, retain all ten names in reviews:

1. Identity, Genealogy and Product Master  
2. GxP Batch Evidence Reconciliation  
3. Unit and Terminology Standardisation  
4. Authority, Effective-Date and Jurisdiction  
5. Consent, Entitlement and Privacy  
6. PV Case Intake and Signal Support  
7. Supply, Cold-Chain and Allocation Planning  
8. Source and Document Governance  
9. Supplier and Audit Evidence  
10. Audit, Evidence and Continuity  
