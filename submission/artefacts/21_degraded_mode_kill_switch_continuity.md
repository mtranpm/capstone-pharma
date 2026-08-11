# 21 — Degraded Mode, Kill Switch & Continuity

| Field | Entry |
|---|---|
| Owner | Platform + CISO + Quality |
| Version / date | 1.0.0 / 2026-08-10 |
| Status | Phase 5 — continuity playbook |
| Sources | `06`, ADR-004, NN-06, XC-02, PUB-10, [`SCQA.md`](SCQA.md) |

---

## 1. Continuity goal

When AI, graph, network or vendor fails, NovaCura must still **assemble evidence** via rules + CSV/read APIs + human review — without regulated automation.

---

## 2. Degraded modes (ordered)

| Mode | Trigger | Behaviour | User messaging |
|---|---|---|---|
| **D0 Normal** | All adapters healthy | Optional LLM; Neo4j or stub | Standard |
| **D1 AI-disabled** | ES-01, budget kill, model outage | Rules + stubs only | “AI assistance unavailable — draft from SoR facts” |
| **D2 Graph-down** | Neo4j unavailable | `InMemoryGraphStub` or skip graph section | “Trace links limited — SoR citations primary” |
| **D3 Read-only SoR lag** | API stale timestamp | Abstain partial claims | “Evidence stale — verify in LIMS” |
| **D4 Full offline** | Network partition | CLI/local API + fixtures | PUB-10 class |
| **D5 Emergency stop** | Security incident ES-04/05 | Halt all agent runs; UI banner | Follow `06` |

---

## 3. Kill switch matrix

| Switch | Owner | Effect | Recovery |
|---|---|---|---|
| **KS-AI** | Platform | `AEGIS_LLM_ENABLED=0` globally | Change control + smoke tests |
| **KS-AGENT** | CISO | Tool calls disabled; read-only tools only | Manifest review |
| **KS-GRAPH** | Platform | Force memory stub | Neo4j RCA |
| **KS-EXPORT** | Quality | Block packet export; review only | Quality release |
| **KS-REGION** | Ops | Route to offline bundle | DR playbook `35` |

Kill switches are **fail-closed** — default deny on ambiguous state.

---

## 4. Emergency stop cross-reference

| ES id | From `06` | Degraded mode |
|---|---|---|
| ES-01 Operator halt | User button | D1 |
| ES-02 Security poisoned tool | G-HR-04 | D5 + KS-AGENT |
| ES-03 Model policy breach | Automated | D1 |
| ES-04 Cyber incident | CISO | D5 |
| ES-05 Regulatory hold | Quality | KS-EXPORT |

---

## 5. Runbook (abbreviated)

1. Confirm incident class (ops, security, quality).
2. Apply appropriate KS-* ; verify audit stream records mode transition.
3. Notify workflow owners (Batch/PV/Supply).
4. Continue on rules-only path; humans export manually if needed.
5. Post-incident: parity tests (`16`), red-team if security (`31`).

---

## 6. Testing

| Test | Expected | Status |
|---|---|---|
| T-DEG-01 | LLM unreachable → D1 packet still schema-valid | **Pending** |
| T-DEG-02 | Neo4j down → stub parity | **Pending** |
| T-DEG-03 | KS-EXPORT blocks API export | **Pending** |

---

## 7. Traceability

| REQ | Section |
|---|---|
| NN-06 | §2 D4 |
| XC-02 | §2–§3 |
