
## Deployable Release v1.0
## Case Study
# Regulated Evidence Reconciliation and Review Support for a Global Pharmaceutical Enterprise
This workshop teaches FDE participants how to move from **pharmaceutical business ambiguity** to **DDD artifacts** and finally to a safe **implementation**.
The participant-facing case must remain **business-only** at the beginning.
---
---
# Workshop Objective
By the end, FDE participants should be able to produce this chain:
```text
Business pain
→ Domain and subdomain map
→ Ubiquitous language
→ Bounded contexts
→ Context map
→ Event storming
→ Entities, value objects, aggregates, invariants
→ Rules vs reasoning separation
→ Human decision ownership
→ Evidence and audit model
→ RAG source design
→ Agent responsibility cards
→ MCP/tool boundary map
→ Minimum governed workflow
→ Production readiness blueprint
```

---
# Case Title
# Reducing Evidence-Reconciliation Time Across Development, Quality, Safety and Supply Without Taking Over Regulated Human Accountability
## Organization
**NovaCura Therapeutics Group (NTG)** is a fictional global pharmaceutical company.
It has:
```text
discovery laboratories
clinical-development programmes
pharmacovigilance hubs
manufacturing plants
quality laboratories
distribution networks
sites in India, Germany, Ireland, the United States, the UAE and Singapore
```
Its portfolio includes:
```text
NCX-101 — oral small-molecule oncology product approaching patent expiry
NCB-204 — monoclonal-antibody biologic in pivotal trials and commercial scale-up
NCS-310 — sterile injectable supplied through hospital and compassionate-use channels
NCR-415 — rare-disease gene-therapy research programme acquired with a biotech subsidiary
```
## Current Business Problem
NTG is fragmented across:
```text
LIMS, MES, electronic batch records, QMS, RIM, EDC, eConsent, IRT, CTMS
safety databases, serialization platforms, data lakes, spreadsheets, vendor portals, research environments
```
Identifiers, timestamps, terminology, access controls and authority hierarchies are inconsistent. No system is universally authoritative. During the capstone window a set of converging events tests every workflow: a pivotal-trial amendment, a disputed biologics batch, emerging safety reports, a sterile-area excursion, a cold-chain failure, an excipient shortage, a ransomware event and a multi-agency inspection request.
## Business Goal
NTG wants a redesigned evidence-reconciliation capability so that batch, safety and supply review work is:
```text
evidence-complete
conflict-visible
provenance-backed
authority-respected
fail-closed on uncertainty
owned by the right accountable human roles
auditable and defensible
```
The goal is a 14% reduction in end-to-end release lead time without changing registered specifications or weakening independent Quality authority.
## Non-Negotiables
```text
AI never releases, rejects, reprocesses, re-labels or recalls a batch.
AI never makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions.
AI never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorized human approval.
AI never changes formulation, specification, clinical eligibility, safety-case disposition, batch release or recall decisions.
Regulated accountability remains with the accountable Quality, Safety, Regulatory, Clinical and Supply roles.
Evidence output must not be produced while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable.
The system operates read-only and advisory; it prepares, reconciles, explains and packages evidence.
```
---
# Representative Scenario
## Converging Events
```text
Pivotal-trial amendment: three protocol versions in execution; one country has not approved the latest amendment.
Disputed biologics batch: NCB204-B24071 has genealogy gaps, a unit-conversion conflict, an OOS/OOT disagreement and a missing supplier audit commitment.
Emerging safety reports: a duplicate ICSR cluster, an awareness-date conflict and a MedDRA version mismatch.
Sterile-area excursion: environmental monitoring excursion near fill-finish with a corrected organism identification.
Cold-chain failure: a biologic shipment exceeded range with disputed logger clocks and pallet association.
Excipient shortage: a sole-source excipient supplier reports contamination with an eight-week recovery estimate.
Ransomware event: manufacturing historians are isolated; MES and QMS operate in degraded mode.
Multi-agency inspection: regulators request traceable evidence spanning trial data, batch history, safety cases and AI-system controls within 72 hours.
```
## Three Mandatory Advisory Workflows
```text
Workflow A — GxP evidence reconciliation for batch-review readiness.
Workflow B — Pharmacovigilance case-intake and signal-support.
Workflow C — Bounded supply-shortage and cold-chain recovery planner.
```
## Required Operating Properties
Every workflow must demonstrate:
```text
purpose limitation, least privilege, current authorization, evidence authority, temporal applicability, provenance
structured outputs, abstention, human review, idempotency, bounded steps, cost and token budgets
checkpointing, rollback, kill switch, degraded mode, auditability, AI-disabled continuity
```
---
# Inject Catalogue (84 injects, D01–D13)
```text
D01 Portfolio, strategy and product value      INJ-001..006
D02 Discovery, translational science and model risk  INJ-007..012
D03 Clinical development and trial integrity   INJ-013..020
D04 GMP manufacturing, laboratories and batch release  INJ-021..028
D05 Quality systems, validation and data integrity  INJ-029..036
D06 Pharmacovigilance and benefit-risk         INJ-037..044
D07 Regulatory information and submissions     INJ-045..050
D08 Supply chain, serialization and anti-counterfeit  INJ-051..058
D09 Privacy, ethics and cross-border data      INJ-059..064
D10 Cybersecurity, agentic security and Zero Trust  INJ-065..070
D11 Human factors, responsible AI and adoption INJ-071..074
D12 Economics, token efficiency and vendor concentration  INJ-075..078
D13 Reliability, business continuity and retirement  INJ-079..084
```
All challenge conditions are disclosed in `case/INTEGRATED_CASE.md`. Participants discover connections, contradictions and failure chains from supplied evidence rather than receive staged surprises.
---
# 10. The 16-Stage DDD Lifecycle
## Stage 1 — Frame Business Problem
|Item|Detail|
|---|---|
|What|Define the business problem without technology|
|Why|Prevents "AI-first" solutioning|
|How|Use problem framing canvas|
|Output|One-page business problem statement|
|Quality Gate|No mention of AI, LLM, agents, RAG, or MCP|
Expected output:
```text
NovaCura needs a governed evidence-reconciliation capability that helps Quality, Safety, Regulatory, Clinical and Supply teams prepare, validate, explain, package and defend evidence for batch review, pharmacovigilance case-intake and supply recovery while preserving regulated human accountability.
```
---
## Stage 2 — Identify Domain and Subdomains
Main domain:
```text
Regulated Evidence Reconciliation and Review Support
```
Core subdomains:
```text
Batch Review Evidence Readiness
Pharmacovigilance Case-Intake and Signal Support
Supply-Shortage and Cold-Chain Recovery Planning
```
Supporting subdomains:
```text
Batch and Material Genealogy
Laboratory Evidence and OOS/OOT
Deviation, CAPA and Change Control
Release-Packet and Qualified-Person Evidence
Terminology and Ontology Normalization (MedDRA, IDMP/SPOR, units)
Authority and Effective-Date
Regulatory Commitments and Submissions
Consent, Privacy and Jurisdiction
Supply, Inventory and Cold-Chain Evidence
```
Generic subdomains:
```text
Identity and entity resolution
Identity and access control / entitlements
Authorization (Zero Trust)
Audit logging and evidence capture
Notification and routing
Document storage
Reporting
Approval tracking
Exception and override recording
Checkpointing, rollback and kill switch
```
Quality gate:
```text
Participants must not call LIMS, MES, QMS or the safety database the domain.
Systems are systems. The domain is the regulated evidence-reconciliation and review work being performed.
```
---
## Stage 3 — Build Ubiquitous Language
Minimum glossary:
|Term|Meaning|
|---|---|
|Evidence reconciliation|Comparing, aligning and explaining evidence across authoritative sources for a business object such as a batch, case, product or shipment|
|Batch-review readiness|The state where batch evidence is complete enough for a human Quality reviewer to begin review, with gaps and conflicts visible|
|Genealogy|Traceable record of materials, components and operations that make up a batch|
|Release packet|The set of records a Qualified Person or Quality reviewer needs before batch release review|
|Deviation|Unplanned departure from a procedure, specification or expected condition|
|CAPA|Corrective and preventive action linked to a deviation, complaint or failure|
|Change control|Controlled approval of changes to product, process, system, or documentation|
|OOS / OOT|Out-of-specification result vs out-of-trend result; a disagreement between these is an evidence conflict|
|ICSR|Individual Case Safety Report in pharmacovigilance|
|Awareness date|The date a company first became aware of a safety event; feeds the reporting clock|
|Listedness|Whether an event is described in approved safety information (expectedness evidence)|
|Signal|Hypothesis of a new or changing safety relationship supported by aggregate evidence|
|Cold-chain excursion|A temperature range breach during transport or storage of a temperature-sensitive product|
|Allocation option|A traceable supply option that requires authorized human approval before any reservation or allocation|
|Evidence authority|The source that is authoritative for a given business object, jurisdiction and effective time|
|Effective date|The date from which a record, label, protocol version or rule applies|
|Abstention|The required behaviour of not producing an answer when evidence is missing or unresolved|
|Fail-closed|Defaulting to blocked, escalate-to-human, or abstain when a required precondition cannot be satisfied|
Quality gate:
```text
Every important term must identify:
meaning
owner
valid context
risk if misunderstood
```
---
## Stage 4 — Define Bounded Contexts
Final bounded contexts:
|Bounded Context|Purpose|
|---|---|
|Batch Genealogy and Material Traceability|Owns batch structure, material lots, component usage, warehouse movements and genealogy completeness|
|Laboratory Evidence and OOS/OOT|Owns lab results, units, OOS/OOT state, investigation linkage and instrument/reagent context|
|Deviation, CAPA and Change Control|Owns deviations, investigations, CAPA effectiveness and change control state|
|Release-Packet and Qualified-Person Evidence|Owns release-packet completeness, supplier audit evidence and QP certification readiness|
|Pharmacovigilance Case|Owns ICSR intake, duplicates, awareness dates, listedness context and signal-support state|
|Terminology and Ontology Normalization|Owns MedDRA, IDMP/SPOR, UCUM unit and terminology-version mapping|
|Authority and Effective-Date|Owns which record is authoritative for which object, jurisdiction and effective time|
|Knowledge and Retrieval Governance|Owns governed, versioned, access-controlled knowledge sources and no-answer rules|
|Supply, Inventory and Cold-Chain Evidence|Owns inventory, shipments, temperature evidence, CMO capacity and allocation constraints|
|Consent, Privacy and Jurisdiction|Owns consent, secondary use, pseudonymisation, residency and cross-border processing boundaries|
|Security and Tool Governance|Owns entitlements, signed tools, tool manifests, model registry and Zero Trust controls|
|Evidence and Audit Context|Owns traceability of sources, recommendations, drafts, approvals, overrides, releases, escalations and final actions|
Quality gate:
```text
No bounded context should own everything.
Each context must own language, data, decisions, statuses, risks and audit needs.
```
---
## Stage 5 — Create Context Map
Reference map:
```text
Authority and Effective-Date Context
    → provides authority for objects, jurisdictions and effective times across all contexts

Consent, Privacy and Jurisdiction Context
    → controls legitimate access/use across all contexts

Security and Tool Governance Context
    → gates entitlements, tool use and model/tool integrity

Batch Genealogy and Material Traceability Context
    → provides genealogy evidence to Laboratory, Deviation/CAPA, Release-Packet and Supply contexts

Laboratory Evidence and OOS/OOT Context
    → provides lab results and OOS/OOT state to Release-Packet and Deviation/CAPA contexts

Deviation, CAPA and Change Control Context
    → provides investigation and change state to Release-Packet and Supply contexts

Release-Packet and Qualified-Person Evidence Context
    → assembles batch-review readiness evidence for the human Quality reviewer

Pharmacovigilance Case Context
    → provides ICSR, duplicate, awareness-date and listedness state to the safety reviewer

Terminology and Ontology Normalization Context
    → feeds normalized terms and units into PV, Regulatory and Laboratory contexts

Knowledge and Retrieval Governance Context
    → publishes governed policy and reference sources

Supply, Inventory and Cold-Chain Evidence Context
    → provides inventory, shipment and temperature evidence to the supply planner

Evidence and Audit Context
    ← records source access, drafts, approvals, overrides, escalations and final actions
```
Relationships to identify:
|Relationship|Example|
|---|---|
|Upstream/Downstream|Batch Genealogy feeds Release-Packet|
|Partnership|Laboratory and Deviation/CAPA jointly affect batch-review readiness|
|Anti-Corruption Layer|LIMS↔MES↔QMS terminology must not pollute a shared domain language; supplier-portal and vendor PDFs are untrusted|
|Shared Kernel|Batch ID, material lot ID, product ID, effective date, authority flag, validation state|
|Published Language|Release-packet schema, ICSR handoff schema, allocation-option schema|
Quality gate:
```text
Each integration must identify source owner, consumer, translation risk and audit requirement.
```
---
## Stage 6 — Run Event Storming
Seed events:
```text
Batch created
Material lot issued
Genealogy gap detected
Laboratory result recorded
Unit-conversion conflict detected
OOS flagged
OOT flagged
Investigation opened
Deviation raised
CAPA opened
Change control raised
Release packet opened
Supplier audit commitment missing
ICSR received
Duplicate cluster detected
Awareness date disputed
MedDRA version mismatch detected
Listedness conflict found
Signal metric computed
Cold-chain excursion recorded
Inventory shortage flagged
Allocation option drafted
Recall candidate flagged
Inspection request received
Human review requested
Batch release certified by human
```
Commands:
```text
Create batch record
Reconcile genealogy
Check unit conversion
Flag OOS/OOT conflict
Open investigation
Raise deviation
Open CAPA
Open release packet
Check supplier audit evidence
Intake ICSR
Detect duplicate candidates
Reconstruct reporting clock
Normalize terminology
Check listedness
Compute signal metric
Record cold-chain excursion
Generate allocation options
Flag recall candidates
Respond to inspection request
Request human review
Certify release
```
Quality gate:
```text
Every major event should have:
actor
trigger
policy
system dependency
failure condition
audit need
```
---
## Stage 7 — Model Entities, Value Objects, Aggregates, and Invariants
Entities:
```text
Batch, MaterialLot, Product, BatchRecord, ReleasePacket
LaboratoryResult, OOSInvestigation, Deviation, CAPA, ChangeControl
SupplierAudit, QualityHold, ICSRCase, AdverseEvent, DuplicateCandidate
SafetyReceipt, SignalAssessment, InventoryItem, Shipment, TemperatureLoggerRecord
AllocationOption, RecallCandidate, InspectionRequest, AgentRun, AuditTrail
```
Value objects:
```text
BatchIdentifier, MaterialLotIdentifier, ProductIdentifier, CompoundIdentifier
UnitValue (UCUM), Concentration, TerminologyVersion, MedDRAPT, AuthorityDesignation
EffectiveDate, ReportingClock, AwarenessDate, ListStatus (listedness), Jurisdiction
ConsentStatus, ValidationState, ProvenanceReference, CheckpointState, FailClosedReason
```
Aggregates:
|Aggregate Root|Owns|
|---|---|
|Batch|batch record, genealogy, quality holds, release state (advisory), exceptions|
|ReleasePacket|release evidence items, supplier evidence, packet completeness, QP review state|
|OOSInvestigation|lab result linkage, investigation state, disposition (human-owned)|
|ICSRCase|narratives, source receipts, awareness dates, duplicate status, listedness context|
|Deviation|trigger, classification, CAPA linkage, effectiveness review state|
|AllocationPlan|inventory view, demand constraints, allocation options (draft only)|
|SignalAssessment|disproportionality metrics, exposure estimates, uncertainty|
|InspectionResponse|request, evidence mapping, deadline, response state|
|EvidenceBundle|source references, decisions, approvals, overrides, timestamps|
Invariants:
```text
An evidence output must not be produced while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
A batch must not be dispositioned, released, rejected, reprocessed, re-labelled or recalled by the system.
No final PV seriousness, causality, expectedness, reportability or signal-confirmation decision may be made by the system.
No allocation, reservation, stock-status change, shipment or recall may be executed without authorized human approval.
A release packet cannot be marked complete while required supplier evidence or audit commitments are missing.
An OOS/OOT disagreement must remain open until the authorized investigation owner disposes it.
A reporting clock must be reconstructed from authoritative awareness evidence before reportability is claimed.
Every recommendation must link to an evidence bundle with source, owner, timestamp, version and authority.
Generated evidence output remains advisory until human review.
Retrieval must block on untrusted, expired, superseded or non-applicable sources.
```
Quality gate:
```text
Every invariant must be implementable as a rule, policy check, workflow gate, or approval condition.
```
---
## Stage 8 — Separate Rules from AI Reasoning
|Work Item|Deterministic Rule|Human Decision|AI-Assisted Work|
|---|---|---|---|
|Batch/genealogy identity match|Yes|Exception only|No|
|Unit conversion and UCUM validation|Yes|Exception only|Detect mismatches|
|Authority and effective-date check|Yes|Exception only|No|
|Consent/entitlement/jurisdiction gate|Yes|Exception only|No|
|Batch evidence reconciliation|Rule-supported|Quality reviewer (QP/CQO) ownership|Draft conflict and gap view|
|OOS/OOT classification|Rule-supported|Investigation owner disposition|Surface disagreement|
|Reporting-clock arithmetic|Yes|Safety officer confirmation|Reconstruct from receipts|
|Duplicate detection|Heuristic + rule|PV reviewer confirmation|Candidate clusters|
|Listedness evidence gathering|Rule-supported|Safety officer decision|Retrieve cited sources|
|Supply option generation|Rule-supported|Supply + Quality approval|Generate traceable options|
|Batch release readiness summary|Rule-gated|Human Quality review|Evidence preparation only|
|Audit trail|Yes|No|No|
Quality gate:
```text
AI cannot own final batch release, OOS disposition, PV seriousness/causality/expectedness/reportability, signal confirmation, allocation, reservation, shipment, recall, or exception override.
```
---
## Stage 9 — Design RAG from DDD Artifacts
Knowledge sources:
```text
Batch release SOPs and QP guidance
Data-integrity policy (ALCOA+)
OOS/OOT investigation procedure
Deviation and CAPA procedure
Change-control procedure
Validation state policy
Supplier audit and commitment policy
Release-packet checklist
MedDRA coding rules and version policy
Listedness sources (IB, CCDS, local labels)
PV case-handling and reporting-clock policy
Signal-management procedure
Cold-chain and shipment policy
Allocation and shortage policy
Known untrusted sources (MALICIOUS_SUPPLIER_DEVIATION.md, tool manifests, vendor PDFs)
```
Required metadata:
```text
Document ID, Title, Owner, Approver, Business function, Workflow applicability
Product/batch/domain applicability, Effective date, Review date, Version, Status
Jurisdiction, Language, Sensitivity level, Allowed roles, Approved-for-use flag
Citation / evidence reference format, Hash where available, Source system
```
Retrieval rules:
```text
Retrieve only approved, current and applicable documents.
Respect product, domain, jurisdiction, role, language and effective time.
Do not use expired, draft, superseded or untrusted sources as authority.
Do not answer if evidence is missing; abstain or escalate.
Every recommendation must cite source title, version, date, section and authority.
Vendor-supplied content is untrusted data until governance review.
```
Quality gate:
```text
RAG source design must include ownership, lifecycle, versioning, access policy, no-answer rules and evaluation cases.
```
---
## Stage 10 — Design Agent Responsibilities
Agent map:
|Agent|Responsibility|Forbidden Action|
|---|---|---|
|Batch Evidence Reconciler|Compares batch records across systems and drafts a conflict/gap view|Cannot disposition a batch|
|Genealogy Gap Checker|Detects missing genealogy branches and warehouse-consumption mismatches|Cannot change genealogy records|
|Unit and Terminology Normalizer|Detects unit and terminology mismatches and version differences|Cannot silently convert units or approve a conversion rule|
|Release-Packet Gap Identifier|Identifies missing or unverified release-packet items|Cannot certify or release a batch|
|ICSR Duplicate Candidate Finder|Suggests duplicate clusters from patient-programme, literature and call-centre cases|Cannot merge cases irreversibly|
|Reporting-Clock Reconstructor|Reconstructs awareness and reporting-clock evidence from receipts|Cannot decide reportability|
|Listedness Evidence Gatherer|Retrieves IB, CCDS and label evidence for expectedness context|Cannot decide expectedness|
|Supply Option Generator|Generates traceable allocation and recovery options|Cannot reserve, allocate, ship or change stock status|
|Cold-Chain Evidence Reviewer|Assembles logger, pallet and timezone evidence for an excursion|Cannot release or block a shipment|
|Evidence Packager|Creates evidence bundle and audit package|Cannot alter source records|
|Guardrail and Policy Checker|Applies deterministic gates, budgets, idempotency and kill switch|Cannot override a gate|
Agent card template:
|Field|Required Answer|
|---|---|
|Agent name||
|Trigger||
|Inputs||
|Outputs||
|Allowed tools||
|Forbidden tools/actions||
|Human owner||
|Approval needed||
|Evidence required||
|Failure mode||
|Escalation path||
|Audit events||
Quality gate:
```text
No agent may have broad access, broad authority, or undefined human ownership.
No agent may take a regulated action or mutate a source record.
```
---
## Stage 11 — Define Human-in-the-Loop and Decision Ownership
|Decision|Responsible|Accountable|AI Role|
|---|---|---|---|
|Batch evidence readiness view|QA reviewer|Quality owner (CQO/QP)|Summarize gaps and conflicts|
|Final batch release/rejection|QA reviewer|CQO / EU QP (human-only)|Evidence preparation only|
|OOS/OOT investigation disposition|Investigation owner|Quality owner|Surface disagreement|
|Deviation closure and CAPA effectiveness|Quality owner|CQO|Track recurrence and taxonomy|
|Supplier audit commitment verification|Supplier quality|Quality owner|Flag unverified commitments|
|PV seriousness/causality/expectedness/reportability|Safety officer|Global Head of PV|Prepare evidence only|
|Signal confirmation|Safety governance|Global Head of PV|Present metrics and uncertainty|
|Allocation approval|Supply planner|Supply Chain VP + Quality approval|Generate options|
|Reservation / stock-status change|Supply planner|Authorized human approval|Never execute|
|Recall scope|Quality + Regulatory|CQO / Regulatory with authorities|Flag recall candidates|
|Inspection response|Regulatory + owners|Regulatory Affairs VP|Map evidence to request|
|Privacy/consent exception|DPO|DPO|Flag conflict|
|Security incident containment|Security team|CISO|Raise and route|
|Clinical eligibility / adjudication|Investigator/medical|Investigator / medical|Never decide|
Quality gate:
```text
Every regulated or safety decision must have a named accountable human owner.
```
---
## Stage 12 — Design Evidence and Audit Trail
Evidence bundle:
```text
Business object identity (batch/product/compound/ICSR/shipment)
Source system and source path
Authority and effective date
Document version and hash
Unit, terminology and jurisdiction context
Consent/entitlement/validation state
Relevant inject/evidence-map references
Generated draft and reasoning
Model/prompt/tool version
Human reviewer and human edits
Approval/rejection status
Override reason and authorized owner
Timestamp
Final action taken
Escalation and closure record
```
Audit events:
```text
Evidence source accessed
Authority/effective-date checked
Genealogy reconciled
Unit conversion flagged
OOS/OOT disagreement surfaced
Deviation/CAPA/change control reviewed
Release packet opened
Supplier audit commitment checked
ICSR intaken
Duplicate candidate surfaced
Reporting clock reconstructed
Terminology normalized
Listedness evidence retrieved
Allocation option drafted
Cold-chain evidence assembled
Human review requested
Human decision recorded
Override recorded
Inspection response mapped
Case or review closed
```
Quality gate:
```text
Every generated output must answer:
What was generated?
From what evidence?
By which tool/model/template?
Reviewed by whom?
Changed where?
Approved when?
Released to whom?
```
---
## Stage 13 — Define Evaluation Using DDD Vocabulary
Evaluation layers:
|Layer|Evaluation Question|
|---|---|
|Domain correctness|Does output use correct batch/PV/supply language?|
|Regulatory safety|Does it avoid unsafe or prohibited statements?|
|Retrieval quality|Are sources approved, current, authoritative and cited?|
|Evidence authority|Is authority and effective date respected?|
|Fail-closed behaviour|Does it abstain when evidence is unresolved?|
|Tool-use correctness|Was the right bounded tool called with the right scope?|
|HITL quality|Were decisions routed to the right human owner?|
|Audit quality|Is every recommendation traceable?|
|Workflow value|Did it reduce rework and evidence-reconciliation time?|
|Risk control|Did it avoid unauthorized actions?|
Golden scenarios:
```text
Batch with genealogy break and unit-conversion conflict (PUB-01, NCB204-B24071)
OOS/OOT disagreement with open investigation
Release packet missing supplier audit commitment
Duplicate ICSR cluster under different product names
Awareness-date conflict across receipt sources
MedDRA version mismatch changing preferred term
Cold-chain excursion with disputed logger clocks
Excipient shortage with competing demand
Prompt injection in a supplier deviation PDF
Tool-manifest poisoning and stale entitlements
Model outage, checkpoint corruption and AI-disabled continuity
```
Quality gate:
```text
Evaluation must test evidence authority, fail-closed behaviour, retrieval, tool use, human routing, audit and workflow value.
```
---
## Stage 14 — Build Minimum Governed Workflow
MVP scope:
```text
Batch-review readiness evidence reconciliation for batch NCB204-B24071 (PUB-01)
for one biologic manufacturing site
with deterministic reconciliation first, governed retrieval, and human-approved advisory output only.
```
MVP workflow:
```text
1. Batch record identified and authorities/effective dates established
2. Genealogy reconciled across MES, warehouse and eBR
3. Laboratory results normalized with UCUM and unit-conflict flagged
4. OOS/OOT disagreement surfaced with investigation state
5. Deviations, CAPA and change control summarized
6. Release-packet items checked, supplier audit commitment flagged
7. Governed sources retrieved with authority and provenance
8. Evidence bundle created
9. Conflict and gap view drafted (advisory)
10. Human Quality review requested
11. Reviewer approves, edits, or escalates
12. Batch readiness summary produced (no disposition)
13. Audit trail stored
14. AI-disabled manual fallback verified
```
Out of scope:
```text
Autonomous batch release, rejection, reprocessing, re-labelling or recall
Autonomous OOS disposition or investigation closure
Autonomous PV seriousness, causality, expectedness, reportability or signal decisions
Autonomous allocation, reservation, stock-status change, shipment or recall initiation
Autonomous formulation or specification changes
Unreviewed regulated advice
```
Quality gate:
```text
The MVP must be narrow, safe, auditable, measurable, and human-supervised.
```
---
## Stage 15 — Pilot, Learn, and Refine Domain Model
Pilot design:
|Area|Design|
|---|---|
|Domain|Batch review evidence readiness (Workflow A)|
|Scope|Batch NCB204-B24071 scenario, one site, one product|
|Mode|Advisory draft, human-approved, read-only|
|Duration|4–6 weeks|
|Users|QA reviewers, QP, PV officers, supply planners|
|Output|Evidence-readiness and conflict/gap views, no dispositions|
|Safety gate|No regulated action without human approval; AI-disabled continuity verified|
Learning questions:
```text
Which terms were misunderstood?
Which events were missing?
Which contexts were too broad?
Which agent responsibility was unsafe?
Which retrieved sources were weak or untrusted?
Which drafts needed heavy editing?
Which exceptions repeated?
Which approval step caused delay?
Which audit record was insufficient?
Which rule was missing?
Which fail-closed default fired unexpectedly?
```
Quality gate:
```text
Pilot must update the domain model, language, events, rules, source register, evaluation cases and production risk register.
```
---
## Stage 16 — Production Readiness and Handover
Production checklist:
|Area|Readiness Requirement|
|---|---|
|Domain model|Approved by Quality, Safety, Regulatory, Clinical and Supply owners|
|Bounded contexts|Clear ownership and integration boundaries|
|Ubiquitous language|Reflected in UI, prompts, schemas, APIs, training|
|Workflow|Validated with real users|
|Regulatory safety|Human approval and escalation enforced; prohibited actions blocked|
|Privacy|Consent, secondary-use, pseudonymisation, residency controls|
|Security|Zero Trust, signed tools, least privilege, audit logging|
|Knowledge|Approved, versioned, monitored sources; untrusted-data warnings|
|RAG|Retrieval evals, no-answer rules, citation quality, authority checks|
|Agents|Bounded responsibilities and forbidden actions|
|MCP/tool layer|Tool permissions, schemas, logging, approval gates|
|Evaluation|Golden tests and regression suite against injects/fixtures|
|Monitoring|Quality, safety, usage, latency, cost, drift|
|Incident response|Unsafe output, wrong retrieval, wrong action, privacy breach|
|Rollback|Disable model, agent, tool, connector, or workflow|
|Training|QA, QP, PV, Regulatory, Supply, Security training|
|Governance|Quality owner, safety owner, product owner, technology owner|
|Handover|Runbook, support model, escalation path|
Quality gate:
```text
Production readiness is not deployment readiness alone.
It is regulatory, quality, clinical, operational, technical, security, privacy, governance and support readiness.
```
---
# 11. DDD-to-Technical Conversion Map
|DDD Artifact|Technical Translation|
|---|---|
|Domain|Product capability: Regulated Evidence Reconciliation and Review Support|
|Subdomain|Capability module|
|Bounded context|Service/API/tool/MCP boundary|
|Ubiquitous language|UI labels, schemas, prompts, eval terms|
|Context map|Integration architecture|
|Domain event|Workflow event, audit event, event-bus message|
|Command|API action, workflow task, agent tool call|
|Entity|Domain object|
|Value object|Strongly typed schema|
|Aggregate|Consistency and transaction boundary|
|Invariant|Guardrail, policy rule, validation rule|
|Human decision|Approval workflow|
|Evidence bundle|Audit and observability record|
|RAG source register|Governed knowledge base|
|Agent card|Agent contract|
|Context relationship|MCP/tool access pattern|
|Evaluation vocabulary|Test suite and scorecard|
|MVP workflow|First deployable slice|
---
# 12. MCP / Tool Boundary Map
|MCP-Style Boundary|Example Tools|Access Mode|
|---|---|---|
|Batch Evidence Server|read batch record, read genealogy, read release packet|Read-only|
|Laboratory Server|read results, read OOS state, validate UCUM|Read-only + controlled flag write|
|Quality Server|read deviations, read CAPA, read change control|Read-only|
|Safety Server|read ICSR, read receipts, read listedness sources|Read-only|
|Terminology Server|normalize units, map MedDRA/IDMP versions|Read-only + flag only|
|Authority Server|resolve authority/effective date, apply jurisdiction|Read-only|
|Knowledge Server|retrieve governed SOP/policy|Read-only|
|Supply Server|read inventory, read shipments, draft allocation options|Draft-only|
|Tool Governance Server|register tools, validate manifests, apply entitlements|Controlled write|
|Audit Server|write audit event, create evidence bundle|Append-only|
MCP safety rules:
```text
No broad database access.
No silent unit conversion.
No batch disposition, release, rejection, reprocessing, re-labelling or recall.
No PV final disposition or signal confirmation.
No reservation, allocation, stock-status change or shipment without authorized human approval.
No tool without schema validation and manifest verification.
No write action without policy check.
No hidden tool execution.
No missing audit event.
No evidence access without entitlement, authority and consent/jurisdiction checks.
No use of unregistered or poisoned tools.
No tool description without owner, purpose, input schema, output schema, failure mode and audit event.
```
---
# 13. Target Technical Architecture
```text
QA / QP / PV / Regulatory / Supply User
    ↓
Evidence Reconciliation Workspace
    ↓
Identity + Authority + Consent + Entitlement Check
    ↓
Evidence Reconciliation Workflow Orchestrator
    ↓
Bounded Agents
    ├── Batch Evidence Reconciler
    ├── Genealogy Gap Checker
    ├── Unit and Terminology Normalizer
    ├── Release-Packet Gap Identifier
    ├── ICSR Duplicate Candidate Finder
    ├── Reporting-Clock Reconstructor
    ├── Listedness Evidence Gatherer
    ├── Supply Option Generator
    ├── Cold-Chain Evidence Reviewer
    ├── Evidence Packager
    └── Guardrail and Policy Checker
    ↓
Governed MCP Tool Layer
    ├── Batch Evidence Server
    ├── Laboratory Server
    ├── Quality Server
    ├── Safety Server
    ├── Terminology Server
    ├── Authority Server
    ├── Knowledge Server
    ├── Supply Server
    ├── Tool Governance Server
    └── Audit Server
    ↓
Enterprise Systems (LIMS, MES, eBR, QMS, EDC, IRT, safety DB, serialization) + Approved Knowledge Sources
    ↓
Evidence Bundle
    ↓
Human Review and Approval
    ↓
Advisory Evidence Readiness / Case / Supply View
    ↓
Observability + Evaluation + Audit + Continuous Improvement
```
---
# 14. Expected Output Examples
## Example Bounded Context Canvas
|Field|Example|
|---|---|
|Context name|Release-Packet and Qualified-Person Evidence|
|Business owner|Quality Assurance / QP function|
|Main users|QA reviewer, Qualified Person|
|Owned terms|Release packet, packet completeness, supplier audit commitment, QP certification readiness|
|Owned data|Release-packet item status, supplier evidence, validation state|
|Decisions owned|Packet completeness (advisory), QP review routing|
|Decisions not owned|Final batch release or rejection|
|External dependencies|LIMS, MES, eBR, QMS, supplier quality portal|
|Risk|Release proceeds on incomplete or unverified evidence|
|Audit need|Who checked what, from which source, when, with what approval|
## Example Agent Card
|Field|Example|
|---|---|
|Agent name|Genealogy Gap Checker|
|Trigger|Batch record opened for review readiness|
|Inputs|batches.csv, material_genealogy.csv, warehouse_movements.csv, ebr_steps.csv|
|Output|Genealogy conflict and gap view (advisory)|
|Allowed tools|read batch record, read genealogy, read warehouse movements|
|Forbidden actions|modify genealogy, disposition batch, release batch|
|Human owner|QA reviewer / Quality owner|
|Evidence required|genealogy source rows, timestamps, authorities|
|Failure mode|missing genealogy branch or conflicting warehouse consumption|
|Escalation|Quality investigation required; review blocked until resolved|
## Example Evidence Bundle
```text
Bundle ID: EVB-2026-0007
Business Object: Batch NCB204-B24071
Product: NCB-204 (mAb biologic)

Sources Used:
- material_genealogy.csv (missing branch SUA-88)
- lab_results.csv / interface_mappings.csv (mg/L vs µg/mL conflict)
- oos_investigations.csv (LIMS OOS vs OOT tooling vs notebook)
- release_packets.csv / supplier_audits.csv (missing CMO audit commitment)
- inject_evidence_map.csv (INJ-021, INJ-024, INJ-023, INJ-028)

Detected Exceptions:
- Genealogy missing branch for single-use assembly lot SUA-88
- Unapproved unit-conversion assumption between mg/L and µg/mL
- OOS/OOT/invalid disagreement with open investigation
- Supplier audit commitment claimed closed but not independently verified

Human Review:
- QA reviewer review pending
- Qualified Person review pending

Audit Status:
- Advisory draft only; no batch disposition made
```
---
# 15. Scoring Rubric
|Area|Weight|
|---|---|
|Business problem clarity|10%|
|Domain/subdomain decomposition|10%|
|Ubiquitous language quality|10%|
|Bounded context correctness|10%|
|Context map and ownership clarity|10%|
|Event storming depth|10%|
|Domain model and invariants|10%|
|Rules vs AI reasoning separation|10%|
|HITL, evidence, audit, and governance|10%|
|RAG, agent, MCP, MVP, and production blueprint|10%|
Scoring levels:
|Score|Meaning|
|---|---|
|5|Strong, production-aware, domain-led|
|4|Good, minor gaps|
|3|Usable but incomplete or generic|
|2|Weak, technology-first or shallow|
|1|Unsafe, unclear, or not domain-driven|
---
# 16. Common Mistakes Checklist
Use this actively during facilitation.
```text
Starting with AI instead of domain
Calling LIMS/MES/QMS the domain
Creating one giant pharmaceutical agent
Letting AI disposition or release a batch
Letting AI decide PV seriousness, causality, expectedness or reportability
Letting AI confirm signals
Letting AI reserve, allocate or ship stock
Silently converting units or merging safety cases
Ignoring authority and effective date
Using RAG as a document dump with untrusted content
Creating MCP connectors without bounded context ownership
Skipping audit trail
Confusing workflow automation with regulated accountability
Ignoring evidence authority and temporal applicability
Ignoring multilingual narrative quality
Ignoring exceptions, overrides and abstention
Designing MVP too broadly
Skipping production monitoring, rollback and kill switch
Ignoring tool-level security and manifest poisoning
Ignoring source document lifecycle and prompt/template versioning
Ignoring AI-disabled continuity and degraded mode
```
---
# 17. Final Team Submission Template
```text
Team Name:

1. Business Problem Framing
2. Stakeholder Map
3. Domain and Subdomain Decomposition
4. Ubiquitous Language Glossary
5. Bounded Context Canvases
6. Context Map
7. Event Storming Board
8. Domain Model
9. Aggregate and Invariant Model
10. Rules vs AI Reasoning Matrix
11. Governed RAG Source Register
12. Agent Responsibility Cards
13. MCP/Tool Boundary Map
14. Human Decision Ownership Matrix
15. Evidence and Audit Schema
16. Evaluation Suite
17. Minimum Governed Workflow
18. Pilot Plan
19. Production Readiness Checklist
20. Final Technical Implementation Blueprint
21. Risks and Assumptions
22. Open Questions
```
---
# 18. Final Deployment Checklist for the Facilitator
Before running the workshop:
|Item|Ready?|
|---|---|
|Participant case printed/shared|☐|
|Synthetic evidence pack shared|☐|
|Whiteboard or collaboration board ready|☐|
|Team roles assigned|☐|
|DDD templates ready|☐|
|Reveal sequence planned|☐|
|Scoring rubric shared with judges|☐|
|Final submission format shared|☐|
|Time boxes visible|☐|
|Regulated safety constraints explained|☐|
|AI/MCP not revealed too early|☐|
|Final presentation slots assigned|☐|
---
# 19. Final Verdict
This is now **workshop-deployable**.
It can be run independently as a:
```text
1-day executive-intensive workshop
2-day deep FDE × DDD workshop
3-day capstone with architecture and evaluation
```
The design is now strong because it forces participants to learn the correct FDE operating sequence:
```text
Do not start with AI.
Start with the domain.

Do not start with architecture.
Start with language, boundaries, events, rules and ownership.

Do not let agents own regulated accountability.
Use agents only inside governed, bounded, auditable workflows.

Do not use MCP as random connector plumbing.
Derive tool boundaries from bounded contexts.

Do not use RAG as document dumping.
Use governed, versioned, evidence-backed retrieval with authority checks.

Do not call a pilot production.
Production requires safety, audit, monitoring, rollback, support and ownership.
```
This is now a serious, deployable **AI FDE × DDD × Pharma GenAI implementation workshop kit**.
