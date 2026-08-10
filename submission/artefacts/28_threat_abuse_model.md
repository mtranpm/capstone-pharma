# 28 — Threat & Abuse Model

| Field | Entry |
|---|---|
| Owner | CISO / Security |
| Version / date | 1.0.0 / 2026-08-10 |
| Status | Phase 5 — OWASP LLM Top 10 mapped |
| Sources | OWASP LLM Top 10 2025, `Docs/specs/Security/OWASP_LLM_TOP10_THREAT_CONTROLS.md`, `19`, `29` |

---

## 1. Threat actors

| Actor | Goal |
|---|---|
| External attacker | Exfiltrate PV data, poison tools, trigger unsafe actions |
| Malicious insider | Bypass gates, export tampered packet |
| Careless user | Paste untrusted instructions / over-trust draft |
| Compromised vendor | Model or API supply-chain attack |

---

## 2. OWASP LLM01–LLM10 → control → test ID

| ID | Threat | AEGIS control | Test ID | REQ |
|---|---|---|---|---|
| **LLM01** Prompt injection | Retrieved text / user paste treated as data; fixed system policy; schema-only tool args | `19` §5; manifest | T-LLM-01 | XC-01 |
| **LLM02** Sensitive disclosure | Redaction in telemetry; minimize logs; purpose binding | ADR-005, `30` | T-LLM-02 | XC-03 |
| **LLM03** Supply chain | Pin manifest/model versions; vendor review `36` | `18`, `36` | T-LLM-03 | — |
| **LLM04** Data/model poisoning | Governed corpus only; hash verify `12` | `19` §2 | T-LLM-04 | NN-04 |
| **LLM05** Improper output handling | Pydantic strict; prohibited guard | ADR-003, `prohibited.py` | T-LLM-05 | NN-01..03 |
| **LLM06** Excessive agency | No write tools; budgets; KS-AGENT | ADR-007, `20` | T-LLM-06 | XC-05 |
| **LLM07** System prompt leak | No secrets in prompts; separate config | `19` | T-LLM-07 | — |
| **LLM08** Vector/embedding weakness | Corpus allow-list; chunk hash | `19` | T-LLM-08 | NN-04 |
| **LLM09** Misinformation | Abstention; conflict register; human gate | NN-05, G-HR-01 | T-LLM-09 | BAT-01 |
| **LLM10** Unbounded consumption | Token/cost caps | `20`, `33`, `34` | T-LLM-10 | XC-06 |

---

## 3. Abuse cases (workshop fixtures)

| Case | PUB / inject | Expected |
|---|---|---|
| Poisoned tool descriptor | PUB-09 / D09 | Block before invoke; G-HR-04 |
| Injection in knowledge doc | Authority untrusted | NN-04 strip |
| Prompt to “release batch” | NN-01 | Guard + no UI control |
| Token burn loop | PUB-14 | STOP-BUDGET |

---

## 4. Security testing plan

| Phase | Activity | Status |
|---|---|---|
| Unit | prohibited + schema tests | **Pending** |
| Integration | manifest tamper | **Pending** |
| Red team | `31` scenarios | **Pending** |

---

## 5. Traceability

Primary link: XC-01, RTM §8 LLM columns.
