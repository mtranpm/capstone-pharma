# ISO/IEC 42001 + EU AI Act compliance specification

- **Spec ID:** `iso-iec-42001-and-eu-ai-act`
- **Version:** `1.0.0`
- **Kind:** `compliance-standard-spec`
- **Companion files:** `iso_42001_eu_ai_act.spec.json` (machine-readable), `iso_42001_eu_ai_act.schema.json` (JSON Schema)

Generic, machine-readable specification of ISO/IEC 42001:2023 controls, Regulation (EU) 2024/1689 obligations, their crosswalk, risk-tier classification, applicability, delta and severity rules, and required output artifacts. The spec is organisation-agnostic: it contains no repository, evidence, scope or naming tied to any single deployment and is intended as the single source of truth for building compliance workbench applications.

## 1. Source of the standards

### ISO/IEC 42001

- **ISO/IEC 42001:2023**
- Requirement summaries are implementation aids. Licensed standard wording is not reproduced; applications must not treat this spec as a substitute for the standard.

### EU AI Act

- **Regulation (EU) 2024/1689 (EU AI Act)**
- Official source: https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
- Obligation summaries are implementation aids, not legal advice or a substitute for the Official Journal text.

## 2. ISO/IEC 42001 requirements

Total requirements: **36** (Clauses 4-10 and Annex A controls A.2-A.10).

| ID | Section | Requirement | Summary | Criticality |
|----|---------|-------------|---------|-------------|
| 4.1 | Clause | Organization and context | Determine internal and external issues relevant to the AI management system and its intended outcomes. | High |
| 4.2 | Clause | Interested parties and requirements | Determine interested parties and their relevant AI-related needs, expectations and obligations. | High |
| 4.3 | Clause | AIMS scope | Define and maintain the boundaries and applicability of the AI management system. | High |
| 4.4 | Clause | AI management system | Establish, implement, maintain and continually improve an AI management system and its processes. | High |
| 5.1 | Clause | Leadership and commitment | Top management demonstrates accountability, direction, support and integration for the AI management system. | High |
| 5.2 | Clause | AI policy | Maintain an AI policy aligned to purpose, objectives, commitments and continual improvement. | High |
| 5.3 | Clause | Roles, responsibilities and authorities | Assign and communicate responsibilities and authorities relevant to the AI management system. | High |
| 6.1.1 | Clause | Actions for risks and opportunities | Plan actions to address AI management system risks and opportunities. | High |
| 6.1.2 | Clause | AI risk assessment | Define and apply a repeatable AI risk assessment process. | High |
| 6.1.3 | Clause | AI risk treatment | Select and implement treatment measures and retain an applicability decision for controls. | High |
| 6.1.4 | Clause | AI system impact assessment | Define and apply AI system impact assessment processes where relevant. | High |
| 6.2 | Clause | AI objectives and planning | Set measurable AI objectives and plan actions, resources, owners and evaluation. | Medium |
| 6.3 | Clause | Planning of changes | Plan AI management system changes in a controlled manner. | Medium |
| 7.1 | Clause | Resources | Provide resources needed for the AI management system. | Medium |
| 7.2 | Clause | Competence | Determine and demonstrate competence for people performing AI management system work. | Medium |
| 7.3 | Clause | Awareness | Ensure personnel understand the policy, objectives, contribution and consequences of nonconformity. | Medium |
| 7.4 | Clause | Communication | Determine relevant internal and external communications for the AI management system. | Medium |
| 7.5 | Clause | Documented information | Create, update and control documented information required by the AI management system. | Medium |
| 8.1 | Clause | Operational planning and control | Plan, implement and control processes needed to meet AI management system requirements. | High |
| 8.2 | Clause | AI risk assessment operation | Perform AI risk assessments at defined intervals and when relevant changes occur. | High |
| 8.3 | Clause | AI risk treatment operation | Implement and evaluate AI risk treatment actions. | High |
| 8.4 | Clause | AI system impact assessment operation | Perform AI system impact assessments under defined conditions and retain results. | High |
| 9.1 | Clause | Monitoring, measurement, analysis and evaluation | Determine and evaluate what is monitored or measured, methods, timing, analysis and results. | High |
| 9.2 | Clause | Internal audit | Conduct internal audits at planned intervals using an audit programme and objective results. | High |
| 9.3 | Clause | Management review | Conduct management reviews with required inputs, decisions and actions. | High |
| 10.1 | Clause | Continual improvement | Continually improve the suitability, adequacy and effectiveness of the AI management system. | Medium |
| 10.2 | Clause | Nonconformity and corrective action | React to nonconformities, determine causes, implement actions and evaluate effectiveness. | High |
| A.2 | Annex A | AI policies | Maintain topic-specific policies that support AI governance and control objectives. | High |
| A.3 | Annex A | Internal organization | Establish AI governance roles, accountability and routes for reporting concerns. | High |
| A.4 | Annex A | Resources for AI systems | Identify and manage resources necessary for responsible AI system operation. | Medium |
| A.5 | Annex A | Assessing AI system impacts | Define, document and apply AI system impact assessment activities. | High |
| A.6 | Annex A | AI system life cycle | Control objectives, design, validation, deployment, operation, change, technical documentation and incident communication across the AI lifecycle. | High |
| A.7 | Annex A | Data for AI systems | Manage data acquisition, quality, provenance, preparation and documented data processes. | High |
| A.8 | Annex A | Information for interested parties | Provide relevant system information, external reporting and incident communications to interested parties. | Medium |
| A.9 | Annex A | Responsible use of AI systems | Define responsible use processes, objectives and intended-use controls. | High |
| A.10 | Annex A | Third-party relationships | Define AI responsibilities and governance controls for suppliers and customers. | High |

## 3. EU AI Act obligations

Total obligations: **18**. Risk tiers: Prohibited, High-Risk, GPAI, Limited / Minimal Risk, Out of stated EU scope.

| ID | Article | Obligation | Risk-tier relevance | Unique EU delta | Criticality |
|----|---------|-----------|---------------------|-----------------|-------------|
| Art. 4 | Article 4 | AI literacy | High-Risk, GPAI, Limited / Minimal Risk | No | Medium |
| Art. 5 | Article 5 | Prohibited AI practices | Prohibited | Yes | High |
| Art. 9 | Article 9 | High-risk risk management system | High-Risk | No | High |
| Art. 10 | Article 10 | Data and data governance | High-Risk | No | High |
| Art. 11 | Article 11 | Technical documentation | High-Risk | No | High |
| Art. 12 | Article 12 | Record-keeping and logs | High-Risk | No | High |
| Art. 13 | Article 13 | Transparency and information to deployers | High-Risk | No | High |
| Art. 14 | Article 14 | Human oversight | High-Risk | No | High |
| Art. 15 | Article 15 | Accuracy, robustness and cybersecurity | High-Risk | No | High |
| Art. 16-18 | Articles 16 to 18 | Provider duties, quality management and retention | High-Risk | No | High |
| Art. 26 | Article 26 | Deployer obligations | High-Risk | No | High |
| Art. 27 | Article 27 | Fundamental rights impact assessment | High-Risk | Yes | High |
| Art. 43 | Article 43 | Conformity assessment | High-Risk | Yes | High |
| Art. 49 | Article 49 | EU database registration | High-Risk, Limited / Minimal Risk | Yes | High |
| Art. 50 | Article 50 | Transparency obligations and synthetic-content marking | Limited / Minimal Risk, High-Risk | Yes | High |
| Art. 51-55 | Articles 51 to 55 | GPAI model duties and systemic risk | GPAI | Yes | High |
| Art. 72 | Article 72 | Post-market monitoring | High-Risk | No | High |
| Art. 73 | Article 73 | Serious-incident reporting | High-Risk, GPAI | Yes | High |

### 3.1 Obligation details and keywords

**Art. 4 - AI literacy**

- Summary: Take measures to ensure sufficient AI literacy for people operating or using AI systems on the organisation's behalf.
- Keywords: AI literacy, training, awareness, competence

**Art. 5 - Prohibited AI practices**

- Summary: Do not place, deploy or use AI practices that are prohibited; retain a documented classification decision for the intended use.
- Keywords: prohibited, social scoring, subliminal, emotion recognition, biometric categorisation

**Art. 9 - High-risk risk management system**

- Summary: For high-risk AI systems, establish, implement, document and maintain a continuous risk-management process across the lifecycle.
- Keywords: risk management, risk assessment, risk treatment, testing, residual risk

**Art. 10 - Data and data governance**

- Summary: For high-risk AI systems, apply data governance and management practices covering data quality, relevance, representativeness, errors and bias as applicable.
- Keywords: data governance, data quality, bias, dataset, provenance

**Art. 11 - Technical documentation**

- Summary: Prepare and keep current technical documentation for high-risk AI systems before market placement or putting into service.
- Keywords: technical documentation, system card, model card, documentation, intended purpose

**Art. 12 - Record-keeping and logs**

- Summary: Design high-risk AI systems to enable automatic event logging at an appropriate level and retain logs under the operator's control.
- Keywords: logging, event logs, audit trail, records, monitoring

**Art. 13 - Transparency and information to deployers**

- Summary: Provide high-risk system information and instructions that enable deployers to interpret output and use the system appropriately.
- Keywords: transparency, instructions for use, user information, limitations, intended purpose

**Art. 14 - Human oversight**

- Summary: Design and enable effective human oversight for high-risk AI systems, proportionate to risk, including ability to understand, monitor and intervene.
- Keywords: human oversight, override, monitor, intervention, training

**Art. 15 - Accuracy, robustness and cybersecurity**

- Summary: Design high-risk AI systems for appropriate accuracy, robustness, resilience and cybersecurity, including relevant AI-specific vulnerabilities.
- Keywords: accuracy, robustness, cybersecurity, drift, adversarial, validation

**Art. 16-18 - Provider duties, quality management and retention**

- Summary: Where acting as provider of a high-risk system, operate a quality management system, meet provider obligations and retain required documentation.
- Keywords: quality management, provider, documentation, retention, conformity assessment

**Art. 26 - Deployer obligations**

- Summary: Where acting as deployer of a high-risk system, use it according to instructions, assign competent human oversight, monitor operation and keep logs where applicable.
- Keywords: deployer, instructions, human oversight, monitoring, logs

**Art. 27 - Fundamental rights impact assessment**

- Summary: Where the deployer category and high-risk use trigger the obligation, complete and update a fundamental rights impact assessment before first use and make the required notification.
- Keywords: fundamental rights impact assessment, FRIA, affected persons, complaint mechanism, fundamental rights

**Art. 43 - Conformity assessment**

- Summary: Before placing or putting a high-risk system into service, complete the applicable conformity assessment route and preserve evidence of the result.
- Keywords: conformity assessment, CE marking, declaration of conformity, notified body

**Art. 49 - EU database registration**

- Summary: Register applicable high-risk systems in the EU database before placing on the market or putting into service, including documented non-high-risk Annex III assessments where relevant.
- Keywords: EU database, registration, Annex III, provider, deployer

**Art. 50 - Transparency obligations and synthetic-content marking**

- Summary: Meet applicable transparency duties for interactive, emotion-recognition, biometric-categorisation or synthetic-content AI, including machine-readable marking of generated or manipulated synthetic content where required.
- Keywords: synthetic content, watermark, machine-readable, deepfake, chatbot, transparency

**Art. 51-55 - GPAI model duties and systemic risk**

- Summary: Where acting as GPAI model provider, maintain model and downstream documentation, copyright policy and training-content summary; systemic-risk models require evaluation, risk mitigation, incident reporting and cybersecurity controls.
- Keywords: general-purpose AI, GPAI, model evaluation, training content, copyright, systemic risk

**Art. 72 - Post-market monitoring**

- Summary: For high-risk systems, establish and document proportionate post-market monitoring that collects and analyses performance data throughout the lifecycle.
- Keywords: post-market monitoring, monitoring plan, performance, lifecycle, feedback

**Art. 73 - Serious-incident reporting**

- Summary: For applicable high-risk systems, maintain a process to investigate and report serious incidents to the relevant EU market-surveillance authority within the statutory timelines.
- Keywords: serious incident, market surveillance, incident reporting, authority, corrective action


## 4. ISO 42001 -> EU AI Act crosswalk

> ISO/IEC 42001 coverage is operational support for EU AI Act obligations. An ISO match never by itself proves EU legal compliance; role, market, scope, legal trigger and article-specific evidence must be validated.

| EU obligation | Mapped ISO 42001 controls |
|---------------|---------------------------|
| Art. 4 | 7.2, 7.3 |
| Art. 5 | 4.1, 6.1.4, A.5, A.9 |
| Art. 9 | 6.1.1, 6.1.2, 6.1.3, 8.2, 8.3, A.5 |
| Art. 10 | A.7, 7.5 |
| Art. 11 | 7.5, A.6 |
| Art. 12 | 7.5, 9.1, A.6 |
| Art. 13 | 7.4, A.8, A.9 |
| Art. 14 | 5.3, A.9 |
| Art. 15 | 8.1, 9.1, A.6, A.7 |
| Art. 16-18 | 4.4, 5.1, 7.5, 9.2, A.6 |
| Art. 26 | 5.3, 7.2, A.8, A.9, 9.1 |
| Art. 27 | 6.1.4, 8.4, A.5 |
| Art. 43 | 8.1, 7.5, A.6 |
| Art. 49 | _No mapped ISO control_ |
| Art. 50 | 7.4, A.8, A.9 |
| Art. 51-55 | 6.1.1, 7.5, 9.1, 10.2, A.6, A.7 |
| Art. 72 | 9.1, A.6 |
| Art. 73 | 7.4, 9.1, 10.2, A.6, A.8 |

## 5. Preliminary risk-tier classification

> Preliminary risk-tier classification from a transparent questionnaire. It is decision support, not legal advice. 'Unsure' answers force a legal/compliance review flag.

### 5.1 Questionnaire

| Key | Question |
|-----|----------|
| `eu_market` | Will the AI system/model be placed on the EU market, put into service in the EU, or used in the EU? |
| `prohibited_practice` | Does the intended use match an Article 5 prohibited-practice trigger (for example, prohibited manipulation, social scoring, certain biometric or emotion-recognition uses)? |
| `safety_component` | Is it a product, or safety component of a product, covered by Annex I legislation and subject to third-party conformity assessment? |
| `annex_iii_use` | Is the intended use in an Annex III area (biometrics, critical infrastructure, education, employment, essential services/benefits, law enforcement, migration/border, or justice/democratic processes)? |
| `gpai_provider` | Is the organisation placing a general-purpose AI model on the EU market as its provider (rather than only using a third-party model)? |
| `systemic_risk` | For a GPAI model provider: is there a systemic-risk indicator, including high-impact capability or the current training-compute threshold? |
| `interactive_or_sensitive` | Does the system interact directly with people, perform emotion recognition/biometric categorisation, or generate/manipulate synthetic content? |
| `fria_trigger` | For a high-risk deployment: is the deployer a public body/public-service provider, or is the use one of the high-risk cases for which Article 27 applies? |

Answers: Unsure, Yes, No.

### 5.2 Decision rules (first match wins)

| Tier | Condition | Flags |
|------|-----------|-------|
| Out of stated EU scope | `eu_market != Yes` | - |
| Prohibited | `prohibited_practice == Yes` | gpai_provider, transparency |
| High-Risk | `safety_component == Yes OR annex_iii_use == Yes` | systemic, fria, gpai_provider, transparency |
| GPAI | `gpai_provider == Yes` | systemic, transparency |
| Limited / Minimal Risk | `interactive_or_sensitive == Yes` | transparency |
| Limited / Minimal Risk | `default` | - |

- **Out of stated EU scope** - EU market, service or use was not confirmed. Reassess if there is an EU nexus.
- **Prohibited** - An Article 5 prohibited-practice trigger was selected. Stop and obtain legal review before placement, deployment or use.
- **High-Risk** - Preliminary high-risk classification based on Annex I safety-component/product or Annex III intended-use. Confirm exclusions, provider/deployer role, and applicable conformity route.
- **GPAI** - The organisation identified itself as a provider of a general-purpose AI model.
- **Limited / Minimal Risk** - No high-risk or GPAI provider trigger was selected; an Article 50 transparency trigger was selected.
- **Limited / Minimal Risk** - No prohibited, high-risk, GPAI-provider or transparency trigger was selected. Confirm scope and intended use before treating this as minimal risk.

### 5.3 Derived flags

| Flag | Condition | Meaning |
|------|-----------|---------|
| `systemic` | `systemic_risk == Yes` | Potential GPAI systemic-risk trigger; include Articles 51-55 in legal and technical review. |
| `fria` | `fria_trigger == Yes` | Article 27 FRIA trigger; validate deployer category, first-use timing and notification requirements. |
| `gpai_provider` | `gpai_provider == Yes` | - |
| `transparency` | `interactive_or_sensitive == Yes` | - |

**Review requirement:** True when any question that influences the resulting tier is answered 'Unsure'.

## 6. Obligation applicability rules

> An EU obligation is 'Applicable' when the risk-tier rules below match the classification. Rules are evaluated against the preliminary tier and derived flags.

- **Default rule:** classification.tier is present in obligation.tiers
- **Out-of-scope exception:** tier == Out of stated EU scope makes every obligation Not applicable.

| Obligation | Rule | Note |
|------------|------|------|
| Art. 27 | `tier == High-Risk AND fria flag is set` | FRIA applies only when the deployer/use triggers it. |
| Art. 49 | `tier == High-Risk` | EU database registration for high-risk systems regardless of transparency flag. |
| Art. 50 | `transparency flag is set` | Transparency duties follow the interactive/synthetic trigger rather than tier alone. |
| Art. 51-55 | `gpai_provider flag is set` | GPAI duties follow provider role regardless of the base tier. |

## 7. EU delta model

Evidence status values: Likely Demonstrated, Partially Demonstrated, Not Demonstrated, Not applicable.

### 7.1 Shared evidence columns

| Column | Meaning |
|--------|---------|
| Mapped ISO 42001 controls | Comma-separated ISO control IDs from the crosswalk. |
| Shared ISO evidence IDs | Union of evidence IDs found against those ISO controls in the shared ISO assessment. |
| ISO controls likely demonstrated | Count of mapped ISO controls assessed 'Likely Demonstrated' in the shared ISO assessment. |

### 7.2 Delta outcomes (first match wins)

| ID | Label | Condition |
|----|-------|-----------|
| not_applicable | Not applicable from current classification | `obligation is not applicable` |
| eu_specific_gap | EU-specific gap | `obligation.unique_delta is true AND EU evidence status != Likely Demonstrated` |
| shared_support | Shared evidence supports coverage - validate legal scope | `EU evidence status == Likely Demonstrated AND ISO controls likely demonstrated > 0` |
| eu_evidence_no_iso | EU evidence located; ISO linkage not demonstrated | `EU evidence status == Likely Demonstrated AND ISO controls likely demonstrated == 0` |
| partial | Partial shared coverage; EU evidence/action required | `default` |

## 8. Severity and finding model

- Criticality impact weights: High=5, Medium=3, Low=2
- Likelihood by status: Not Demonstrated=5, Partially Demonstrated=3, Likely Demonstrated=1
- Risk score = likelihood x impact
- Risk bands: Low, Medium, High, Critical (cutoffs: -1, 5, 11, 19, 25)

### 8.1 Finding classification rules

| Condition | Finding type |
|-----------|--------------|
| `status == Likely Demonstrated` | Conforming |
| `status == Not Demonstrated AND criticality == High` | Major NC |
| `status == Not Demonstrated OR (status == Partially Demonstrated AND criticality == High AND (caution present OR maturity <= 1))` | Minor NC |
| `default` | Observation |

## 9. Evidence model

- Inventory fields: Evidence ID, Path, Type, Bytes, SHA256-12, Extractable text, Caution cues, Text
- Supported file types: .md, .txt, .csv, .json, .yaml, .yml, .pdf, .docx, .xlsx
- Negative/caution cues: draft, pending, not implemented, not available, gap, missing, tbd, to be, no evidence, incomplete
- Match weights: keyword_hit=3, context_term=1, title_term_in_path=2
- Strong-match threshold: score >= 10 with >= 2 candidates and no caution cues
- Maturity scale: Integer 0-5.

### 9.1 Assessment columns

| Requirement ID | Section | Requirement | Requirement summary | Criticality | Applicable | Evidence IDs | Status | Maturity (0-5) | Reasoning / traceability | Additional evidence required | Recommendation | Finding type | Likelihood | Impact |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

### 9.2 Additional evidence expectations

| Status | Expected additional evidence |
|--------|----------------------------|
| Not Demonstrated | Approved/current procedure or register; sampled operating records; named owner; interview or review evidence of effectiveness. |
| Partially Demonstrated | Approved/current procedure or register; sampled operating records; named owner; interview or review evidence of effectiveness. |
| Likely Demonstrated | Sample implementation and effectiveness evidence during audit. |

### 9.3 Guardrails

- 'Not Demonstrated' means the supplied repository did not demonstrate the requirement; it does not assert the activity is absent.
- A document match is never sufficient on its own to prove implementation or effectiveness.
- Caution cues lower confidence and are surfaced in the reasoning, not used as automatic findings.
- Findings and severity are preliminary until an assessor validates them against source records, scope and interviews.

## 10. Output artifacts

| ID | Name | Format | Contents |
|----|------|--------|----------|
| assessment_workbook | Assessment workbook | xlsx | Evidence Matrix, Clause Compliance, Annex A Matrix, Gap Register, NC Register, Risk Heatmap, 90-Day Roadmap, Readiness Summary, Scope Statement, Quality Checklist |
| executive_summary | Executive audit-readiness summary | md | - |
| stage_one_decision | Stage 1 readiness decision | md | - |
| executive_presentation | Executive presentation | pptx | - |
| gap_register | Gap register | csv | - |
| eu_delta_report | EU AI Act delta analysis report | md | - |
| eu_crosswalk_workbook | EU AI Act crosswalk workbook | xlsx | EU Delta Summary, ISO to EU Crosswalk, EU Delta Actions |
| eu_action_register | EU action register | csv | - |

