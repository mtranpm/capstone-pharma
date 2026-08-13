# 42 — Template-to-Artefact Mapping (Definition of Done)

| Field | Entry |
|---|---|
| Owner | Governance / defence lead |
| Version / date | 1.0.0 / 2026-08-13 |
| Status | DoD evidence — **All 30 required templates mapped to equivalent submission artefacts** |
| Definition of done | *All 30 required artefacts are completed or mapped to equivalent evidence.* |
| Templates root | `templates/` (30 scaffolds — blank forms, not answers) |
| Evidence root | `submission/artefacts/` (+ supporting `submission/evidence/`, `submission/runbooks/`, tests) |
| Rule | Challenge `templates/` stay immutable; completed equivalents live under `submission/` |

---

## 1. Summary scorecard

| Metric | Count |
|---|---|
| Required templates | **30** |
| Mapped to primary equivalent artefact(s) | **30 / 30** |
| Status: **Completed** (primary artefact exists and addresses template intent) | **30** |
| Status: **Gap / unmapped** | **0** |
| Extra submission artefacts beyond the 30 (supporting / UI / discovery) | See §4 |

**DoD verdict:** **MET** — every template has one or more equivalent evidence artefacts in `submission/artefacts/` (and cited supporting evidence where noted).

---

## 2. Master mapping (templates 01–30 → submission evidence)

| # | Template (`templates/`) | Primary equivalent(s) (`submission/artefacts/`) | Supporting evidence (optional) | Coverage notes | DoD status |
|---|---|---|---|---|---|
| 01 | `01_BUSINESS_CASE.md` | `01_discovery_problem_baseline_value.md`, `SCQA.md` | `02_no_ai_and_solution_options.md` | Problem, baseline, value, AI vs no-AI framing | **Completed** |
| 02 | `02_DMAIC_WORKBOOK.md` | `04_dmaic_benefits_stop_pivot.md` | `01_discovery_problem_baseline_value.md` | DMAIC, benefits, stop/pivot | **Completed** |
| 03 | `03_STAKEHOLDER_DECISION_RIGHTS.md` | `03_stakeholders_decision_rights.md` | `38_persona_current_state_system_flows.md`, `39_persona_to_workflow_e2e_flows.md` | Decision rights, RACI-style accountability | **Completed** |
| 04 | `04_PRODUCT_SERVICE_BLUEPRINT.md` | `05_product_operating_model.md`, `PRD_AEGIS_Google_AI_Studio.md` | `06_human_oversight_and_emergency_stop.md`, `07_adoption_accessibility_change.md`, `40_*`, `41_*` | Personas, JTBD, in/out scope, operating cadence | **Completed** |
| 05 | `05_DDD_CONTEXT_MAP.md` | `08_ddd_context_map.md` | `ddd/README.md`, `assumptions_decision_log.md` | Bounded contexts, context map | **Completed** |
| 06 | `06_DATA_GOVERNANCE_INTEGRITY.md` | `09_data_governance_lineage_contracts.md`, `24_data_integrity_records_audit_trail.md` | `12_document_authority_model.md` | Lineage, contracts, ALCOA+ / audit | **Completed** |
| 07 | `07_ONTOLOGY_SEMANTIC_LAYER.md` | `10_ontology_semantic_layer.md` | `12_document_authority_model.md` | Semantic / ontology layer | **Completed** |
| 08 | `08_KNOWLEDGE_GRAPH_DECISION.md` | `11_knowledge_graph_decision.md` | Graph adapters under `submission/src/aegis/adapters/` | Build/buy/stub KG decision | **Completed** |
| 09 | `09_REQUIREMENTS_TRACEABILITY.md` | `13_requirements_traceability_matrix.md` | `traceability_inject_workflow.csv` | RTM + inject↔workflow | **Completed** |
| 10 | `10_C4_ARCHITECTURE.md` | `14_architecture_c4_adrs.md` | `15_brownfield_modernization_plan.md`, `19_ai_context_and_tool_design.md` | C4 views in architecture pack | **Completed** |
| 11 | `11_ADR_REGISTER.md` | `14_architecture_c4_adrs.md` (ADR sections) | `assumptions_decision_log.md`, `18_model_baseline_selection_substitution.md` | ADRs co-located with C4 pack | **Completed** |
| 12 | `12_INTEGRATION_CONTRACTS.md` | `09_data_governance_lineage_contracts.md`, `14_architecture_c4_adrs.md` | `submission/src/aegis/contracts/`, evaluation contract samples | Schema/contracts, SoR read-only boundary | **Completed** |
| 13 | `13_GXP_LIFECYCLE_VALIDATION.md` | `23_gxp_lifecycle_validation_strategy.md` | `16_reproducibility_and_offline_execution.md`, `22_intended_use_regulatory_applicability.md` | Validation lifecycle strategy | **Completed** |
| 14 | `14_COMPUTER_SOFTWARE_ASSURANCE.md` | `23_gxp_lifecycle_validation_strategy.md`, `25_quality_risk_and_safety_assurance.md` | `16_*`, `submission/tests/`, `32_tevv_evaluation_strategy.md` | CSA / risk-based assurance via validation + QRM + tests | **Completed** |
| 15 | `15_QUALITY_RISK_MANAGEMENT.md` | `25_quality_risk_and_safety_assurance.md` | `27_assurance_case_residual_risk.md`, `06_*` | QRM / safety assurance | **Completed** |
| 16 | `16_THREAT_ABUSE_MODEL.md` | `28_threat_abuse_model.md` | `29_zero_trust_tool_governance.md`, `31_red_team_and_remediation.md` | Threats, abuse, red-team | **Completed** |
| 17 | `17_PRIVACY_ETHICS.md` | `30_privacy_by_design_assessment.md` | `22_*`, supply ethics in `39_*` / knowledge refs | Privacy-by-design + ethics | **Completed** |
| 18 | `18_RESPONSIBLE_AI_HUMAN_FACTORS.md` | `06_human_oversight_and_emergency_stop.md`, `07_adoption_accessibility_change.md` | `22_*`, `26_*`, `40_*` UI labelling | Human oversight, a11y, intended use | **Completed** |
| 19 | `19_EU_AI_ACT_APPLICABILITY.md` | `22_intended_use_regulatory_applicability.md`, `26_ai_governance_analysis.md` | `demo_data/obligation_register.csv` (UI overlay) | EU AI Act crosswalk + intended use | **Completed** |
| 20 | `20_ISO42001_GOVERNANCE.md` | `26_ai_governance_analysis.md` | `22_*`, `27_*` | ISO 42001 ↔ programme controls | **Completed** |
| 21 | `21_ASSURANCE_CASE.md` | `27_assurance_case_residual_risk.md` | `25_*`, `32_*` | Assurance case + residual risk | **Completed** |
| 22 | `22_EVALUATION_SCORECARD.md` | `32_tevv_evaluation_strategy.md` | `submission/evidence/`, `submission/evaluation/`, PUB run JSONs | TEVV / evaluation strategy + run evidence | **Completed** |
| 23 | `23_TOKEN_FINOPS.md` | `33_token_efficiency_economics.md`, `34_ai_finops_model.md` | `20_agent_budget_stop_checkpointing.md` | Token economics + FinOps + budgets | **Completed** |
| 24 | `24_RELIABILITY_OBSERVABILITY.md` | `35_operations_slo_incident_dr.md` | `21_degraded_mode_kill_switch_continuity.md`, OTEL rules/runbooks | SLO, observability, degraded mode | **Completed** |
| 25 | `25_INCIDENT_RECOVERY.md` | `35_operations_slo_incident_dr.md`, `21_degraded_mode_kill_switch_continuity.md` | `submission/runbooks/AI_DISABLED_CONTINUITY.md`, `RESET_ROLLBACK.md` | Incident, DR, kill switch, continuity | **Completed** |
| 26 | `26_TARGET_OPERATING_MODEL.md` | `05_product_operating_model.md`, `07_adoption_accessibility_change.md` | `37_production_readiness_roadmap_defence.md`, `39_*` | Operating model + adoption + TOM trajectory | **Completed** |
| 27 | `27_VENDOR_EXIT_RETIREMENT.md` | `36_vendor_exit_retirement.md` | `18_model_baseline_selection_substitution.md` | Exit / retirement / substitution | **Completed** |
| 28 | `28_PRODUCTION_READINESS.md` | `37_production_readiness_roadmap_defence.md` | `16_*`, `00_implementation_task_list.md`, runbooks | Production readiness / defence pack | **Completed** |
| 29 | `29_NINETY_DAY_ROADMAP_HANDOVER.md` | `37_production_readiness_roadmap_defence.md`, `15_brownfield_modernization_plan.md` | `00_implementation_task_list.md` | Roadmap + brownfield + task list handover | **Completed** |
| 30 | `30_ELEVATOR_PITCH.md` | `SCQA.md`, `37_production_readiness_roadmap_defence.md` (§ defence / pitch) | `PRD_AEGIS_Google_AI_Studio.md`, `01_*` | SCQA Answer + defence pitch narrative | **Completed** |

---

## 3. One-glance index (template → primary path)

```text
01 Business case          → artefacts/01_*.md + SCQA.md
02 DMAIC                  → artefacts/04_*.md
03 Stakeholders           → artefacts/03_*.md
04 Product blueprint      → artefacts/05_*.md + PRD_*.md
05 DDD context map        → artefacts/08_*.md
06 Data governance        → artefacts/09_*.md + 24_*.md
07 Ontology               → artefacts/10_*.md
08 Knowledge graph        → artefacts/11_*.md
09 Requirements RTM       → artefacts/13_*.md
10 C4 architecture        → artefacts/14_*.md
11 ADR register           → artefacts/14_*.md (+ assumptions_decision_log.md)
12 Integration contracts  → artefacts/09_*.md + 14_*.md + src/aegis/contracts/
13 GxP lifecycle          → artefacts/23_*.md
14 CSA                    → artefacts/23_*.md + 25_*.md (+ tests)
15 Quality risk           → artefacts/25_*.md
16 Threat / abuse         → artefacts/28_*.md
17 Privacy / ethics       → artefacts/30_*.md
18 Responsible AI / HF    → artefacts/06_*.md + 07_*.md
19 EU AI Act              → artefacts/22_*.md + 26_*.md
20 ISO 42001              → artefacts/26_*.md
21 Assurance case         → artefacts/27_*.md
22 Evaluation scorecard   → artefacts/32_*.md (+ evidence/)
23 Token / FinOps         → artefacts/33_*.md + 34_*.md
24 Reliability / o11y     → artefacts/35_*.md
25 Incident / recovery    → artefacts/35_*.md + 21_*.md (+ runbooks/)
26 Target operating model → artefacts/05_*.md + 07_*.md
27 Vendor exit            → artefacts/36_*.md
28 Production readiness   → artefacts/37_*.md
29 90-day roadmap         → artefacts/37_*.md + 15_*.md
30 Elevator pitch         → SCQA.md + artefacts/37_*.md
```

---

## 4. Extra submission artefacts (not required by the 30 templates)

These strengthen defence/demo but are **beyond** the 30-template DoD:

| Artefact | Role |
|---|---|
| `00_case_discovery_understanding.md` | Case folder literacy |
| `00_implementation_task_list.md` | Build gates / checklist |
| `02_no_ai_and_solution_options.md` | Extends business case / no-AI option |
| `12_document_authority_model.md` | Authority model (feeds 06/07/19) |
| `17_cursor_engineering_evidence.md` | Engineering process evidence |
| `19_ai_context_and_tool_design.md` | Tool/agent design |
| `20_agent_budget_stop_checkpointing.md` | Agent budgets (feeds FinOps) |
| `38_persona_current_state_system_flows.md` | Persona × systems AS-IS |
| `39_persona_to_workflow_e2e_flows.md` | Persona × workflow E2E |
| `40_demo_ui_feature_catalogue.md` | UI catalogue (AEGIS demo) |
| `41_pv_supply_ui_specs.md` | PV/Supply UI specs |
| `PRD_AEGIS_Google_AI_Studio.md` | Detailed PRD |
| `SCQA.md` | SCQA spine (also maps to T01/T30) |
| `assumptions_decision_log.md` | Assumptions / decisions |
| `traceability_inject_workflow.csv` | Inject matrix (feeds T09) |
| `ddd/` | DDD companion notes |

---

## 5. Naming note (why not 1:1 filenames)

Submission artefacts follow the **CURSOR_SPEC phase numbering** (e.g. product model as `05`, DMAIC as `04`), which does **not** always equal the template number (e.g. template `02_DMAIC` ↔ artefact `04_dmaic_*`). This mapping is the authoritative crosswalk for assessors.

---

## 6. Assessor quick-check

- [x] All 30 `templates/*.md` appear in §2  
- [x] Each row has ≥1 primary path under `submission/artefacts/`  
- [x] No template left **Unmapped**  
- [x] Templates themselves remain blank scaffolds (not overwritten)  
- [x] SCQA included as business-case / pitch spine  

---

## 7. Traceability

| Related | Use |
|---|---|
| `13_requirements_traceability_matrix.md` | Requirements ↔ tests ↔ fixtures |
| `37_production_readiness_roadmap_defence.md` | Defence order / readiness |
| `00_implementation_task_list.md` | Phase completion checklist |
| This file (`42`) | Template DoD crosswalk |

---

*End of artefact 42 — Template-to-artefact mapping. DoD: 30/30 mapped.*
