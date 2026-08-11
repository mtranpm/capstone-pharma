# 07 — Adoption, Accessibility & Change Management

| Field | Entry |
|---|---|
| Owner | Product / change lead |
| Version | 0.1.0 |
| Status | Phase 3 — draft for review |
| Sources | `03`, PV-02 / NN-05 in `13`, `data/usability_findings.csv`, `knowledge/K-005` (model change), GxP lifecycle policies |

## 1. Change management

| Phase | Activities | Exit criteria |
|---|---|---|
| **Prepare** | Stakeholder map (`03`); training needs per persona (`05`); identify SOP touchpoints (batch release evidence, PV intake, supply planning) | Signed comms plan; no promise of autonomous decisions |
| **Pilot** | Batch + PV workflows on PUB fixtures; offline drill | Contract tests green; human gates enforced |
| **Scale** | Add Supply; enable optional LLM behind port | TEVV gates (`32`) before model promotion |
| **Sustain** | Weekly regression; catalog/version drift checks | Abstention taxonomy stable; audit exports inspectable |

### Change categories

| Category | Examples | Approvers | AEGIS behaviour |
|---|---|---|---|
| **Model / prompt** | LLM swap, prompt template | Quality + RA + DPO | Version pin; rollback; AI-disabled default on failure |
| **Knowledge catalog** | New `knowledge_catalog.csv` row | Document owner + Quality | `AuthorityPort` must classify before use |
| **Ontology / graph** | New relationship type in Neo4j load | Architecture + Quality | Graph remains advisory; stub parity test |
| **UI / workflow** | New review checklist field | Product + workflow owner | a11y review below |
| **Emergency** | ES-01 activation | CISO + Quality | Pre-documented continuity runbook (`K-002`) |

Resistance patterns from case: Manufacturing speed vs Quality completeness — messaging must repeat **humans keep regulated pen** ([`SCQA.md`](SCQA.md)).

## 2. Multilingual operations (PV-focused)

| Rule | Rationale | Implementation |
|---|---|---|
| Preserve verbatim narrative | Legal/medical meaning must not drift | Store original language in packet; translations labelled **advisory** |
| No silent “fix” | INJ class / PV-02 | LLM may suggest glossaries; human approves any displayed translation |
| Locale in metadata | Inspection defence | `icsr_cases.csv` `language` field echoed in lineage |
| RTL scripts (e.g. Arabic cases) | Readability | UI supports directionality in review pane |

Machine translation may **assist** reviewers; it must not replace accountable PV assessment.

## 3. Accessibility (a11y) baseline

Target: **WCAG 2.2 Level AA** orientation for the React human-review UI (workshop scope — full VPAT deferred to production).

| Requirement | Design choice |
|---|---|
| **Keyboard** | All review actions (expand conflict, approve checklist, export) reachable without mouse; visible focus order |
| **No color-only state** | Conflict / abstention / trusted authority use icon + text label (e.g. “Conflict”, “Abstained”, “Untrusted source”) |
| **Contrast** | Status badges meet AA contrast; dark mode optional later |
| **Screen readers** | Packet sections as landmarks; citations read as “Source: {system}, status: {authority}” |
| **Motion** | Respect `prefers-reduced-motion` for progress indicators |
| **Timeouts** | Session expiry warns before gate loss; no silent discard of draft review |

Reference synthetic usability signals: `data/usability_findings.csv` (if present in evaluation narratives).

## 4. Training & competency

| Role | Minimum competency | Assessment |
|---|---|---|
| Workflow operator | Purpose binding, abstention interpretation | Scenario drill on PUB fixture |
| Human reviewer | Recognize prohibited UI patterns | Sign-off on NN-01..03 checklist |
| Platform admin | Emergency stop, offline stub | Run CLI eval without Neo4j/LLM |

## 5. Metrics

| Metric | Target direction |
|---|---|
| Time-to-proficiency (pilot users) | Decrease without cutting review time |
| a11y defect backlog | Zero blocker issues at pilot exit |
| Change-related incidents | Track model/catalog changes linked to audit ids |

## 6. Links

- Data governance: [`09_data_governance_lineage_contracts.md`](09_data_governance_lineage_contracts.md)  
- Human oversight: [`06_human_oversight_and_emergency_stop.md`](06_human_oversight_and_emergency_stop.md)
