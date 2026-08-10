# OWASP LLM Top 10 — Threat Controls Spec

**Spec ID:** `aegis-owasp-llm-top10`  
**Version:** `1.0.0`  
**Implement during:** Phases 5 (threat model), 7 (build), 8 (tests)

## 1. Purpose

Map OWASP LLM Top 10 threats to AEGIS build controls, tests, and evidence. Advisory evidence orchestration only — never regulated execution.

## 2. Control catalogue

| ID | Threat | Build control | Test / grader |
|---|---|---|---|
| LLM01 | Prompt injection | Retrieved docs/tools are data not instructions; quarantine untrusted content | `G-OWASP-LLM`, PUB-09 |
| LLM02 | Sensitive information disclosure | Purpose limitation; redact/minimise; export allow-lists; no secrets in logs/OTel | `G-PRIVACY`, PUB-11 |
| LLM03 | Supply chain | Pin deps; approved tool manifest only; reject poisoned manifests | PUB-09, tool-manifest tests |
| LLM04 | Data/model poisoning | Authority/status/effective-date checks; untrusted docs never authority | `G-AUTHORITY` |
| LLM05 | Improper output handling | Pydantic-strict outputs; no raw model text to side-effecting tools | Contract tests |
| LLM06 | Excessive agency | Prohibited-action guard; no write tools for release/PV/allocate/recall; human review | `G-EXEC-BOUNDARY` |
| LLM07 | System prompt leakage | Separate system vs user/retrieved; never echo secrets | Security suite |
| LLM08 | Vector/embedding weaknesses | Authority filters before similarity; Neo4j/CSV provenance over blind RAG | Authority + graph tests |
| LLM09 | Misinformation / overreliance | Cite evidence; abstain on unresolved identity/unit/time/authority | `G-ABSTENTION`, `G-PROVENANCE` |
| LLM10 | Unbounded consumption | Budgets, timeouts, max steps/tokens; OTel metrics; stop policy | `G-FINOPS`, PUB-13/14 |

## 3. Non-negotiables

1. AI never releases/rejects/recalls a batch, makes final PV decisions, or allocates/ships stock.
2. Fail closed on missing authority, stale auth, untrusted instructions, unresolved identity/unit/time.
3. Deterministic graders gate safety — not LLM-as-judge.

## 4. Evidence

- Artefact `28` threat model maps each LLM0x → control → test ID → residual risk.
- Artefact `31` red-team records adversarial cases and remediation.
- Cursor rule `.cursor/rules/aegis-owasp-llm-top10.mdc` enforces deny-by-default while coding.

## 5. Related

- `Docs/Regulations/iso_42001_eu_ai_act.md` (Art.5, 14, 15; ISO A.7, A.9)
- `evaluation/public_fixtures/PUB-09.json` … `PUB-15.json`
