# 15 — Brownfield Modernization Plan

| Field | Entry |
|---|---|
| Owner | Architecture / programme lead |
| Version / date | 1.0.0 / 2026-08-10 |
| Status | Phase 5 — strangler pattern for advisory layer |
| Sources | [`SCQA.md`](SCQA.md), `05`, `08`, `14`, workshop starter under `submission/src`, `Docs/specs/Tasks/CURSOR_SPEC_DRIVEN_ENTERPRISE_APP_TASK.md` |

---

## 1. Brownfield baseline (conceptual review)

NovaCura’s estate is **brownfield**: decades of MES/LIMS/QMS/PV integrations, batch records on paper/PDF hybrids, and regional RIM variants. The workshop **starter** (`submission/src/aegis/`) is not a greenfield replacement — it is a **thin advisory slice**:

| Starter element | Maturity | Modernization role |
|---|---|---|
| Port protocols + composition | Implemented | **Anchor** for all future adapters |
| CSV `FixturePort` | Workshop-complete | Stands in for read-only SoR APIs |
| `InMemoryGraphStub` | Implemented | Default until Neo4j ops ready |
| FastAPI skeleton | Partial | Strangler **edge** for new consumers |
| React review UI | Planned / minimal | New UX without touching MES screens |
| Neo4j adapter | Placeholder | Optional acceleration path |

**Review conclusion:** Do not “big bang” replace LIMS/MES/QMS. Wrap evidence assembly with AEGIS while SoRs remain authoritative (ADR-010, `11`).

---

## 2. Strangler fig pattern

```text
Phase A (workshop):  SoR CSV/fixtures ──► AEGIS CLI/API ──► human export
Phase B (pilot):     SoR read APIs ─────► same ports ──────► review UI + audit
Phase C (scale):     Event bus (read) ──► cache/graph rebuild ──► optional Neo4j
Never in scope:      AEGIS ──write──► disposition / PV final / ERP ship
```

| Strangler slice | What stays in legacy | What AEGIS owns |
|---|---|---|
| Batch readiness | QP sign-off in QMS; lab in LIMS | Conflict-visible packet + citations |
| PV intake support | Medical review in safety DB | Duplicate/clock **evidence** packet |
| Supply recovery | TMS/WMS execution | Non-executing options + constraints |

---

## 3. Ports as modernization seams

Each legacy system maps to an **adapter** implementing an existing port — domain code unchanged.

| Legacy capability | Port | Adapter evolution |
|---|---|---|
| Batch/lab/genealogy tables | `FixturePort` → `SoRBatchPort` | CSV → REST/SOAP read client with lineage metadata |
| Document trust | `AuthorityPort` | Catalog CSV → ECM/RIM signed metadata API |
| Traceability graph | `GraphPort` | Stub → Neo4j fed by ETL from SoR |
| Narrative summarization (optional) | `LlmPort` | Stub → enterprise gateway with DLP |
| Audit / eGMP archive | `AuditPort` | File emit → validated archive API (human-triggered) |

Anti-corruption: adapters translate legacy quirks (unit strings, timezone-less timestamps) into **verbatim + uncertainty** fields — never silent normalization (`09`, BAT-02).

---

## 4. Data migration & coexistence

| Data class | Strategy | Risk control |
|---|---|---|
| Master data (materials, products) | Read-through; MDM id in every packet line | Abstain if id ambiguous (NN-05) |
| Transactional (results, movements) | Point-in-time snapshot + source row id | No merge across systems without explicit join key |
| Documents (SOPs, labels) | Hash + authority state from catalog | NN-04 |
| Derived graph | Rebuild job; drift test vs SoR | Prefer CSV/API on conflict (`11` §6) |

No bulk “lift and shift” of SoR into Neo4j as master.

---

## 5. Release waves

| Wave | Duration (indicative) | Exit criteria |
|---|---|---|
| **W0 Workshop** | Current | Contract tests green; offline PUB path documented (`16`) |
| **W1 Pilot site** | 8–12 weeks | One batch site on read API; G-HR gates in production UI |
| **W2 PV intake** | 8 weeks | Multilingual preserve verified; DPO sign-off on logs |
| **W3 Supply read-only** | 8 weeks | Options packet; no TMS write integration |
| **W4 Graph optional** | Parallel | Neo4j parity tests pass; kill-switch to stub (`21`) |

---

## 6. Decommissioning / rollback

| Trigger | Action |
|---|---|
| Prohibited-action near-miss in prod | Freeze LLM; rules-only + ES-01 (`06`) |
| Stub/Neo4j parity failure | Disable Neo4j; stub only |
| Vendor LLM exit | Swap `LlmPort` adapter (`36`, `18`) |
| Programme stop (`04` STOP-01) | Retire AEGIS edge; SoRs unchanged |

---

## 7. Dependencies & gaps

| Gap ID | Item | Owner | Artefact |
|---|---|---|---|
| G-003 | This brownfield plan | Architecture | **Closed** (this doc) |
| — | Live API contracts for NovaCura SoRs | Enterprise architecture | Out of workshop scope |
| — | ECM hash verification production keys | RA / IT | `12`, `24` |

---

## 8. Traceability

| REQ | Section |
|---|---|
| XC-04 | §3 adapters |
| NN-06 | §2 Phase A offline |
| NN-01..03 | §2 “Never in scope” |

*Starter code path: `submission/src/aegis/composition.py`, `adapters/fixture_loader.py`.*
