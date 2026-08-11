# 29 — Zero Trust Tool Governance

| Field | Entry |
|---|---|
| Owner | CISO / Platform |
| Version / date | 1.0.0 / 2026-08-10 |
| Status | Phase 5 — tool zero trust |
| Sources | NIST SP 800-207 concepts, ADR-007, `19`, `28` |

---

## 1. Zero trust principles (tools)

| Principle | AEGIS application |
|---|---|
| Never trust, always verify | Every tool call: identity, purpose, manifest version, schema |
| Least privilege | Role-scoped tool subsets per workflow |
| Assume breach | Kill switches `21`; no regulated write tools |
| Explicit policy | Deny by default on unknown tool id |

---

## 2. Tool lifecycle

```text
Design → Schema + risk tier → Security review → Manifest sign → Deploy → Monitor → Revoke/rotate
```

| Stage | Gate |
|---|---|
| Design | No side-effect tools for NN classes |
| Review | CISO + workflow owner |
| Deploy | Parity with `ToolManifestPort` version in audit |
| Revoke | Instant manifest bump; old version rejected |

---

## 3. Runtime verification chain

1. **User/session** — authN/authZ at API (`08` security boundary).
2. **Purpose binding** — batch id / case id scoped queries only.
3. **Manifest** — version match; signature when PKI available.
4. **Arguments** — JSON Schema validate; max size limits.
5. **Execution** — adapter in sandboxed process (target); timeout.
6. **Response** — schema validate before LLM re-ingest.
7. **Audit** — `tool.invoked` with hashes only (`24`).

---

## 4. Tool tiers

| Tier | Description | Approval |
|---|---|---|
| T0 | Read SoR / graph | Workflow owner |
| T1 | Search knowledge | Quality + RA |
| T2 | LLM format draft | Platform + Quality |
| T3 | **Prohibited** — any regulated write | **Not deployable** |

---

## 5. Integration with agent budgets

Tool calls decrement budget (`20`); T0/T1 may have higher caps than T2.

---

## 6. Tests

| Test | Status |
|---|---|
| T-ZT-01 Unknown tool denied | **Pending** |
| T-ZT-02 Role mismatch denied | **Pending** |
| T-ZT-03 Manifest rollback attack fails | **Pending** |

---

## 7. Traceability

XC-01, LLM06/08 in `28`.
