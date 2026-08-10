# 30 — Privacy by Design Assessment

| Field | Entry |
|---|---|
| Owner | DPO |
| Version / date | 1.0.0 / 2026-08-10 |
| Status | Phase 5 — PbD summary |
| Sources | GDPR Art. 25, `07`, PV-02, XC-03, `24` |

---

## 1. Processing overview

| Activity | Personal data | Lawful basis (indicative) |
|---|---|---|
| PV intake support | Patient/reporter narratives, identifiers | Legitimate interest / legal obligation for PV — **confirm with DPO** |
| Batch/supply | Mostly non-personal; operator ids | Employment / legitimate interest |
| Audit logs | User ids, metadata | Security / compliance |

---

## 2. Privacy by design controls

| Principle | Control |
|---|---|
| Data minimisation | Load only fields required for workflow template |
| Purpose limitation | Purpose code on run; reject mismatch |
| Storage limitation | Short telemetry TTL; packets in controlled QMS |
| Accuracy | No silent narrative “fixes” (PV-02) |
| Integrity/confidentiality | TLS, RBAC, redaction ADR-005 |
| Transparency | UI explains AI assist + export recipients |

---

## 3. DPIA triggers

| Trigger | Action |
|---|---|
| New LLM vendor region | DPIA update |
| New retrieval corpus with PHI | DPIA + catalog classification |
| Export to third country | SCC / adequacy review |

Workshop: **DPIA lite** recorded here; full DPIA **pending** production.

---

## 4. Data flows

```text
SoR (PV DB) read-only → AEGIS memory (ephemeral) → draft packet → human export → authoritative PV system
                              ↓
                    redacted telemetry (no narrative)
```

---

## 5. Rights & retention

| Right | Support |
|---|---|
| Access | Via SoR systems of record |
| Erasure | AEGIS ephemeral; logs per retention policy |
| Restriction | KS-EXPORT stop |

---

## 6. Tests

| Test ID | Check | Status |
|---|---|---|
| T-PRV-01 | Span excludes narrative | **Pending** |
| T-PRV-02 | Purpose mismatch denied | **Pending** |

---

## 7. Traceability

XC-03, PV-02, LLM02 in `28`.
