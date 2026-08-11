# 13 — Requirements Traceability Matrix (Discovery baseline)

| Field | Entry |
|---|---|
| Owner | Product / QA evidence lead |
| Version | 0.2.0 |
| Status | Phase 5 — ISO/EU + OWASP LLM01–10 crosswalk added (§8) |
| Sources | PUB index, inject register, contracts under `evaluation/contracts/`, artefacts `01`–`04`, `09` |

## 1. Traceability columns

| Column | Meaning |
|---|---|
| REQ-ID | Stable requirement id |
| Statement | Shall / shall-not |
| Workflow | Batch / PV / Supply / CrossCut / Enterprise |
| Injects | Primary INJ-* |
| Fixtures | PUB-* |
| Contract / test | Schema or grader |
| Human owner | Accountable role |
| Artefact | Spec / discovery doc |

## 2. Non-negotiables (shall-not)

| REQ-ID | Statement | Workflow | Injects | Fixtures | Contract / test | Human owner | Artefact |
|---|---|---|---|---|---|---|---|
| NN-01 | Shall not autonomously disposition, release, reject, reprocess, relabel or recall a batch | Batch | INJ-006, INJ-028 | PUB-01..03 | `batch_response`; prohibited-action guard | QP / Quality | `01`, `02`, `03` |
| NN-02 | Shall not finalize PV seriousness, causality, expectedness, reportability or signal | PV | INJ-006 | PUB-04..06 | `pv_response`; guard | Global Head PV | `01`, `03` |
| NN-03 | Shall not allocate/reserve/ship stock or change inventory quality status or initiate recall | Supply | INJ-006 | PUB-07..08 | `supply_response`; guard | Supply + Quality | `01`, `03` |
| NN-04 | Shall not treat untrusted/superseded knowledge as authority | CrossCut | Authority injects | PUB-01..15 | Authority gate tests | Quality / RA | `09`, `12` |
| NN-05 | Shall abstain when identity, unit, time, terminology, jurisdiction or evidence incomplete | All | INJ-021..024, clocks | PUB-01..08 | Graders G-* | Workflow owner | `01`, `04` |
| NN-06 | Shall provide offline / AI-disabled continuity path | Enterprise | Outage injects | PUB-10 | Offline stub tests | Platform | `16` (Phase 5) |

## 3. Workflow requirements

| REQ-ID | Statement | Workflow | Injects (examples) | Fixtures | Contract / test | Human owner | Artefact |
|---|---|---|---|---|---|---|---|
| BAT-01 | Produce contract-valid batch readiness packet with conflicts/gaps explicit | Batch | INJ-021 genealogy, INJ-023 OOS/OOT, INJ-024 units, INJ-028 QP gap | PUB-01..03 | `batch_response.schema.json` | QP / Quality release | `01`, `09` |
| BAT-02 | Preserve verbatim lab values, units and time precision; no silent unit conversion | Batch | INJ-024 | PUB-01 | Contract + grader | Lab / Quality | `09` |
| BAT-03 | Surface genealogy / material identity conflicts (e.g. SUA-88 class) | Batch | INJ-021, INJ-008 | PUB-01 | Graders | Manufacturing + Quality | `01` |
| PV-01 | Produce contract-valid PV intake support packet (duplicates, clocks, listedness evidence) | PV | D06 injects in register | PUB-04..06 | `pv_response.schema.json` | PV case intake | `01`, `03` |
| PV-02 | Preserve original multilingual narrative; no silent “fix” that changes meaning | PV | Multilingual injects | PUB-04..06 | Privacy/TEVV later | PV + DPO | `07`, `09` |
| SUP-01 | Produce non-executing supply recovery options with constraint evidence | Supply | Cold-chain / shortage injects | PUB-07..08 | `supply_response.schema.json` | Supply planning | `01`, `03` |
| SUP-02 | Options shall not imply executed allocation or shipment | Supply | INJ-006 | PUB-07..08 | Guard | Supply + Quality | `02`, `04` |
| XC-01 | Security fixture: detect/block poisoned tool or injection; never execute regulated action | Security | D09 class | PUB-09 | Participant security contract | CISO | `28`, `29` |
| XC-02 | Reliability / degraded mode: fail closed, continue offline | Reliability | Outage | PUB-10 | Continuity tests | Platform | `21` |
| XC-03 | Privacy: purpose binding and minimisation on retrieval/export | Privacy | Privacy injects | PUB-11 | Privacy tests | DPO | `30` |
| XC-04 | Integration: typed clients, retries, no silent merge across SoRs | Integration | Interface injects | PUB-12 | Contract tests | Architecture | Eng specs |
| XC-05 | Agent: budgets, checkpoints, stop; no unbounded tool loops | Agent | Agent injects | PUB-13 | Budget tests | Platform | `20` |
| XC-06 | FinOps: token/cost visibility; refuse unbounded spend | FinOps | Cost injects | PUB-14 | FinOps artefact | Procurement / Platform | `33`, `34` |
| XC-07 | Clinical: no eligibility decisions; evidence-only if in scope | Clinical | D03 injects | PUB-15 | Clinical guard | Clinical ops | `01` |

## 4. Data / knowledge / source-document links

| Object class | Trace to | Control |
|---|---|---|
| `data/*.csv` SoR fixtures | Workflow loaders → BAT/PV/SUP REQs | Preserve source fields; lineage in packet |
| `knowledge/` catalog statuses | Authority gate NN-04 | Trusted vs untrusted |
| `source_documents/` | Provenance citations | Hash / path in audit |
| Inject register | [`traceability_inject_workflow.csv`](traceability_inject_workflow.csv) | 84 rows → workflows/fixtures |
| Public fixtures | `evaluation/PUBLIC_FIXTURE_INDEX.csv` | PUB-01..15 |

## 5. Human owners (summary)

| Domain | Primary owner | Escalation |
|---|---|---|
| Batch readiness | Quality release / QP | CQO |
| PV intake | PV case intake → medical reviewer | Global Head PV |
| Supply options | Supply planning | Supply Chain VP (+ Quality for status) |
| Security / tools | CISO | Security governance |
| Privacy | DPO | Privacy board |
| Platform continuity | Platform / Architecture | CISO + Quality |

## 6. Coverage checklist (Phase 1 exit)

| Check | Status |
|---|---|
| Batch linked to injects + data + PUB-01..03 + contract + human owner | Yes |
| PV linked to injects + data + PUB-04..06 + contract + human owner | Yes |
| Supply linked to injects + data + PUB-07..08 + contract + human owner | Yes |
| Prohibited actions listed (NN-01..03) | Yes |
| No-AI alternative documented (`02`) | Yes |
| Full inject register present | Yes (84) |

## 7. Deferred enrichment (ongoing)

- Attach grader IDs `G-*` and concrete test file paths as green runs land in `submission/tests/` and `submission/evidence/eval/`.  
- Refresh after major ADR or schema version changes in artefact `14`.

---

## 8. Control crosswalk — ISO 42001, EU AI Act (indicative), OWASP LLM01–10

**Note:** EU AI Act article references are **programme mapping aids**, not legal classification. ISO 42001 clauses cite AIMS themes from `26`.

| REQ-ID | ISO 42001 (theme) | EU AI Act (indicative) | OWASP LLM | Primary artefact | Test / grader |
|---|---|---|---|---|---|
| NN-01 | 8 Operation (prohibited use) | Art. 5 / oversight context | LLM05, LLM06 | `14` ADR-006, `06` | G-PROHIB; T-LLM-05 **pending** |
| NN-02 | 8 Operation | Art. 14 human oversight | LLM05, LLM09 | `06`, `22` | G-PROHIB **pending** |
| NN-03 | 8 Operation | Art. 14 | LLM06 | `05`, D-004 | G-PROHIB; T-LLM-06 **pending** |
| NN-04 | 7 Support (documented info) | Art. 10 data governance | LLM01, LLM04, LLM08 | `12`, `19` | G-AUTH; T-LLM-04 **pending** |
| NN-05 | 6 Planning (risk) | Art. 15 robustness | LLM09 | `14` ADR-008 | G-* abstention; TEVV `32` **pending** |
| NN-06 | 8 Operation (continuity) | Art. 15 / Art. 12 records | LLM10 | `16`, `21` | T-DEG-01; PUB-10 **pending** |
| BAT-01 | 8 Operation | Art. 15 accuracy | LLM09 | `14`, `32` | G-STRUCT, G-BAT-* **pending** |
| BAT-02 | 7 Support | Art. 10 | LLM05 | `09`, `24` | OQ diff **pending** |
| BAT-03 | 9 Performance evaluation | Art. 15 | — | `11`, `14` ADR-002 | G-BAT-CONFLICT **pending** |
| PV-01 | 8 Operation | Art. 14 | LLM09 | `22` | G-PV-* **pending** |
| PV-02 | 7 Support (privacy) | Art. 10 | LLM02 | `07`, `30` | T-PRV-01 **pending** |
| SUP-01 | 8 Operation | Art. 14 | LLM06 | `22` | G-SUP-* **pending** |
| SUP-02 | 8 Operation | Art. 14 | LLM06 | `02`, `04` | G-PROHIB **pending** |
| XC-01 | 10 Improvement / 8 Op | Art. 15 cybersecurity | LLM01, LLM06 | `28`, `29`, `31` | T-LLM-01..06 **pending** |
| XC-02 | 8 Operation | Art. 12 | — | `21`, `35` | T-DEG-* **pending** |
| XC-03 | 7 Support | Art. 10 | LLM02 | `30`, ADR-005 | T-LLM-02, T-PRV-01 **pending** |
| XC-04 | 8 Operation | Annex IV documentation | — | `14`, `15` | contract tests **pending** |
| XC-05 | 8 Operation | Art. 14 / 15 | LLM06, LLM10 | `20`, `19` | T-BUD-* **pending** |
| XC-06 | 8 Operation | Art. 12 / resource | LLM10 | `33`, `34` | T-LLM-10 **pending** |
| XC-07 | 6 Planning | Art. 5 context | — | `22` | clinical guard **pending** |
| G-HR-01..06 | 5 Leadership / 8 Op | Art. 14 | LLM06 | `06`, `14` ADR-006 | T-AUD-01 **pending** |

### 8.1 ISO 42001 clause rollup (programme)

| Clause | Satisfied by (artefacts) |
|---|---|
| 4–5 | `SCQA.md`, `03`, `05`, `22` |
| 6 | `25`, `27`, `04` |
| 7 | `07`, `09`, `12`, `17` |
| 8 | `14`–`21`, `submission/src` |
| 9 | `32`, `23`, `35` |
| 10 | `31`, `26`, assumptions log |

Gap **G-001**: enriched — remaining work is **executable test evidence**, not ID mapping.
