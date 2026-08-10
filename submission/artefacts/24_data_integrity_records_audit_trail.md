# 24 — Data Integrity, Records & Audit Trail

| Field | Entry |
|---|---|
| Owner | Quality / Data integrity |
| Version / date | 1.0.0 / 2026-08-10 |
| Status | Phase 5 — ALCOA+ design |
| Sources | `09`, ADR-012, `12`, 21 CFR Part 11 principles, NN-04 |

---

## 1. ALCOA+ mapping

| Principle | AEGIS control |
|---|---|
| **Attributable** | User id, role, purpose on run start; human attestation on export |
| **Legible** | Structured JSON + human UI; audit export readable |
| **Contemporaneous** | UTC timestamps with preserved precision from SoR |
| **Original** | SoR row ids + document hashes in citations |
| **Accurate** | No silent unit conversion (BAT-02); conflicts surfaced |
| **Complete** | Abstention when gaps (NN-05) |
| **Consistent** | Schema version in packet |
| **Enduring** | Audit events to WORM/archive (target) |
| **Available** | Offline export path |

---

## 2. Record types

| Record | Content | SoR? |
|---|---|---|
| SoR fixture/API row | Authoritative measurements, movements | **Yes** |
| Knowledge document | Policy/SOP with authority state | Reference |
| Advisory packet | Draft for human review | **No** — derivative |
| Audit event | Who/when/what adapter/hash | AEGIS record |
| Human sign-off | Export approval | **Yes** (when in QMS) |

---

## 3. Audit trail events (minimum)

| Event | Fields |
|---|---|
| `run.started` | run_id, user, purpose, object, idempotency_key, adapter_modes |
| `sor.loaded` | source paths/ids, row counts |
| `authority.checked` | doc_id, state, hash |
| `graph.queried` | workflow, focus_id, mode stub/neo4j |
| `tool.invoked` | tool_id, version, arg hash (not PHI) |
| `llm.completed` | model id, token counts, schema pass/fail |
| `packet.drafted` | packet_sha256, schema_version |
| `review.gate` | gate id G-HR-*, outcome |
| `export.approved` | human user, packet_sha256 |
| `abstain` | reason codes |

Implementation: `AuditPort` / `adapters/audit.py`.

---

## 4. Integrity controls

| Control | Detail |
|---|---|
| Hash chain (optional target) | Each event includes prev_hash |
| Immutability | Challenge `data/` not overwritten in submission policy |
| Time sync | NTP on servers; log clock skew warnings |
| Backdating | Denied — server time authoritative for AEGIS events |

---

## 5. Retention & privacy

| Data | Retention | Notes |
|---|---|---|
| Audit events | ≥ QMS record policy (e.g. 7–15y programme-defined) | Legal holds |
| Telemetry | Short TTL; redacted | `30` |
| PV narratives in packets | Minimize in logs; full text in controlled export only | DPO review |

---

## 6. Tests

| Test ID | Assertion | Status |
|---|---|---|
| T-AUD-01 | Export without G-HR-01 leaves no `export.approved` | **Pending** |
| T-AUD-02 | Packet hash stable for canonical JSON | **Pending** |
| T-AUD-03 | Untrusted doc citation blocked or flagged | **Pending** |

---

## 7. Traceability

| REQ | Section |
|---|---|
| NN-04 | §3 authority events |
| BAT-02 | §1 Accurate/Original |
