# 36 — Vendor Exit & Retirement

| Field | Entry |
|---|---|
| Owner | Procurement / Architecture |
| Version / date | 1.0.0 / 2026-08-10 |
| Status | Phase 5 — exit strategy |
| Sources | ADR-001 ports, `18`, `21`, D-001 |

---

## 1. Portability principle

No vendor lock-in at **domain** layer — only adapters change (`14` ADR-001).

---

## 2. Vendor classes

| Vendor type | Exit mechanism | Max exit time (target) |
|---|---|---|
| LLM API | `LlmPort` stub; rules-only | 1 day |
| Neo4j | `InMemoryGraphStub`; CSV joins | 1 week |
| Cloud host | Redeploy containers + restore audit | 2 weeks |
| Embedding SaaS | Re-embed governed corpus | 4 weeks |

---

## 3. Data return & deletion

| Data at vendor | Action on exit |
|---|---|
| Prompts/logs (if any) | Contractual delete certificate |
| Fine-tuned weights | Not used in workshop |
| Neo4j | Export graph dump; rebuild from SoR |

---

## 4. Retirement (product)

If AEGIS programme stops (`04`):

1. Disable KS and exports.
2. Archive audit to QMS.
3. Remove API credentials.
4. Retain validation package 15y per policy.
5. SoRs unchanged — no data migration required.

---

## 5. Contract clauses (checklist)

- [ ] Data processing agreement
- [ ] Subprocessor list
- [ ] Exit assistance period
- [ ] Model version pinning
- [ ] SLA credits

---

## 6. Traceability

`36` supports `26` R-GOV-02, `18` §4.
