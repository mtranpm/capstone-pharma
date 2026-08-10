# A3 — Ubiquitous Language Glossary: NovaCura Therapeutics Group (Project AEGIS-PHARMA)

## 1. Stage 3 Mission

Stage 3 converts the Stage 2 domain and subdomain map into a shared business language for governed evidence reconciliation and review support across the three advisory workflows. The purpose is to define the words that quality, manufacturing, laboratory, pharmacovigilance, regulatory, supply chain, privacy, cybersecurity, biostatistics and patient-safety roles must use consistently before bounded contexts are designed. This stage does not solve batch, safety or supply issues, does not approve batch release or rejection, does not disposition safety cases, does not allocate stock or initiate recalls, does not provide medical, regulatory or legal advice, and does not create architecture or implementation design.

## 2. Input Summary

The main business domain is **governed evidence reconciliation and review support for regulated pharmaceutical workflows**. The case focuses on preparing, validating, reconciling, explaining, packaging and defending evidence so accountable human roles can perform batch review, pharmacovigilance case handling and supply recovery across Workflow A (GxP evidence reconciliation for batch-review readiness), Workflow B (PV case-intake and signal-support) and Workflow C (bounded supply-shortage and cold-chain recovery planning).

The key scenario concerns the disputed biologics batch NCB204-B24071 (missing single-use assembly lot SUA-88 genealogy branch, mg/L vs µg/mL unit assumption, disputed OOS/OOT state, unverified supplier-audit commitment, back-entered batch-record step), emerging safety reports (duplicate ICSR candidates, disputed awareness date, MedDRA version mismatch, listedness conflict), a sterile-area excursion, a cold-chain failure (disputed logger clocks and pallet association, missing aggregation), a sole-source excipient shortage with CMO capacity conflict, a ransomware event with a 47-minute audit-capture gap, and a multi-agency inspection request. These are workflow and domain-language inputs only; they are not batch, safety, quality or supply decisions.

## 3. Ubiquitous Language Principles

- Use language from the regulated pharmaceutical review work, not from systems or technology (LIMS, MES and safety databases are sources, not the domain).
- Define terms as they apply to this case, not as broad regulatory or medical dictionary terms.
- Every safety-sensitive term must have a clear business meaning and likely owner or participant.
- A term that implies approval, release, rejection, certification, completion, allocation, shipment or recall must not be used unless the required regulated review or approval condition is satisfied.
- Batch release, batch rejection, QP certification and PV disposition language must preserve accountable human ownership.
- Authority language must be per business object, jurisdiction and effective date; a later timestamp is not automatically more authoritative than an approved signed record.
- Consent, entitlement and privacy language must remain explicit, not assumed.
- Audit language must cover recommendation, draft, approval, override, release, escalation, action, outcome and closure.
- Known genealogy, unit, terminology, authority and evidence gaps must be named clearly but not resolved in this stage.
- Terms that imply an executed regulated action (release, rejection, reprocess, re-label, recall, allocation, shipment) must never be used for a proposed or advisory outcome.

## 4. Core Domain Glossary

| Term | Business meaning in this case | Likely owner or participant | Valid context | Risk if misunderstood |
|---|---|---|---|---|
| Governed evidence reconciliation and review support | The coordinated business work of preparing, validating, reconciling, explaining, packaging and defending evidence so accountable humans can perform batch review, PV case handling and supply recovery | Quality, Safety, Regulatory, Clinical and Supply roles across Workflows A, B and C | Main business domain | The problem may be reduced to system integration or data plumbing instead of the full regulated review work |
| Evidence-complete | Every item required for the review at hand is present, attributable to a source, and resolvable to a business object, jurisdiction and effective date | Quality release reviewers, PV case intake, supply planners, audit/quality | Batch review, PV intake, supply recovery, inspection | A packet may be treated as ready while required evidence is missing, unattributed or unresolved |
| Conflict-visible | Contradictions and discrepancies between sources are shown to accountable owners, never silently resolved or merged | All accountable roles; audit/quality oversight | Any evidence reconciliation in Workflows A, B and C | Conflicting evidence may be hidden by a tool that silently picks a winner |
| Provenance-backed | Every fact traces to an identified source record, with lineage and attribution | All evidence-producing roles | Release packets, PV evidence, inspection evidence | Evidence may be used without knowing where it came from |
| Authority-respected | For each business object, jurisdiction and effective date the appropriate source is treated as binding; no system is universally authoritative | Regulatory Affairs, Quality, Privacy/Legal, master-data governance | Authority determination, batch review, listedness, supply | A convenient system may be treated as authoritative even when it is not |
| Fail-closed | When any required state (identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation, checkpoint) is unresolved, no evidence output is produced and the matter is escalated | All workflows and all accountable roles | Any reconciliation output | Unresolved states may be bypassed and unreliable evidence may flow downstream |
| Read-only advisory | The system prepares, reconciles, explains and packages evidence; it never executes a regulated action | All accountable roles | All three workflows | An advisory recommendation may be mistaken for an executed action |
| Batch-review readiness | The state where the evidence needed for batch release review is assembled, complete or explicitly unresolved with ownership, so accountable Quality roles and the EU QP can assess it | Quality release reviewers, EU Qualified Person, batch-review coordination | Workflow A | The batch may be assumed ready for review, or release-ready, while gaps remain open |
| Release-ready | The state where accountable Quality and QP roles judge that all conditions for batch release are met; only these roles may reach it | EU Qualified Person, Quality release decision owners | Workflow A | Review readiness may be confused with actual release approval |
| Abstention / no-answer | The declared response when the system cannot resolve a required state; it provides no output rather than a guess | All workflows | Any unresolved identity, unit, terminology, authority, consent, validation or checkpoint state | The system may produce an ungrounded answer instead of honestly abstaining |

## 5. Subdomain-Specific Glossary

### 5.1 Identity and Genealogy

| Term | Business meaning | Risk if misunderstood |
|---|---|---|
| Product identity | The set of attributes that uniquely identify a pharmaceutical product in a given market | A product may be confused across markets or names |
| Batch identity | The unique identifier of a manufactured batch of product | Records from different batches may be mixed |
| Material identity | The unique identifier of a raw material, component, single-use assembly or excipient | A wrong lot may be attributed to a batch |
| Compound identity | The identity of the investigational or marketed compound (e.g., NCB-204) | Lineage may be attributed to the wrong programme |
| Genealogy | The record of materials, components and operations that fed a batch | A missing branch hides the true lineage of a batch |
| Material/batch lineage | The chain of identity linking raw materials, intermediates, single-use assemblies and batches | Incomplete lineage may mask contaminated or wrong materials |
| Genealogy break | A missing or unlinked branch in the lineage of a batch | A batch may be evaluated against incomplete genealogy |
| Single-use assembly lot | The lot of a disposable assembly (e.g., SUA-88) used in manufacture | A disputed or missing assembly lot breaks genealogy |
| Consumption record | The warehouse record showing issue or consumption of a material lot | Conflict with the MES genealogy branch may go unexplained |
| Product master | The governed reference for products, batches, materials and attributes | Master-data defects propagate into every workflow |
| Aggregation hierarchy | The linkage between product, case, pallet and shipment identifiers | A break hides which cases are on which pallet |

### 5.2 GxP Evidence Reconciliation (batch review)

| Term | Business meaning | Risk if misunderstood |
|---|---|---|
| Batch review | The regulated review of evidence for a batch before any release decision | Review may be confused with the release decision itself |
| GxP evidence | Records produced under good manufacturing or practice controls that support batch disposition | Non-GxP or untrusted records may be treated as evidence |
| Laboratory result | An analytical outcome produced by a laboratory operation | A result may be treated as valid before its OOS/OOT state is resolved |
| OOS (Out of Specification) | A test result outside the registered specification limits | OOS state may be confused with a final rejection |
| OOT (Out of Trend) | A result statistically unusual versus historical trend, even if within specification | OOT may be ignored or over-weighted |
| Environmental monitoring excursion | A cleanroom or environmental monitoring result outside alert or action limits | An excursion near fill-finish may be underplayed |
| Deviation | A departure from an approved process, procedure or standard | A deviation may be treated as closed before investigation |
| CAPA | Corrective and preventive action owned by Quality to address a root cause | CAPA closure may be confused with root-cause verification |
| Change control | The governed process for changing a process, system or specification | An unapproved change may be treated as effective |
| Validation state | The qualified status of a process, system or equipment (validated, conditionally released, research-only) | An unvalidated system may be treated as qualified |
| Batch-record step | A step in the electronic batch record describing manufacture or testing | A back-entered step may be treated as contemporaneous |
| Back-entered record | A record entered after the event, e.g., after network degradation | It may be mistaken for a contemporaneous record without evidence |
| Release packet | The assembled evidence set supporting a batch release review | A gap in the packet may be hidden |
| Release-packet completeness | Whether all required release-packet items are present and attributed | A packet may be treated as complete while items are missing |
| Supplier evidence | Audit, commitment and certificate evidence from contract sites and suppliers | Unverified commitments may be treated as closed |
| QP certification | The EU Qualified Person's accountable decision on batch certification | An advisory package may be confused with certification itself |

### 5.3 Unit and Terminology Standardisation

| Term | Business meaning | Risk if misunderstood |
|---|---|---|
| Unit-conversion assumption | The assumption about how a reported unit maps to the receiving system's expected unit | mg/L mistaken for µg/mL changes concentration by 1000x |
| Reported unit | The unit as transmitted by the producing interface | The true transmitted unit may be overwritten |
| Receiving-interface assumed unit | The unit the receiving interface assumes without confirmation | A silent mismatch corrupts the evidence |
| Terminology normalisation | The process of mapping terms to a governed reference vocabulary | Mismatched terms may split or merge records |
| MedDRA version | The version of the MedDRA dictionary used for coding medical terms | Two versions may change the preferred term for the same event |
| Preferred term | The standard MedDRA term selected for an event | A wrong preferred term misroutes a safety case |
| Reference data | Governed sets such as units, products, sites and dictionary versions | Undocumented reference data produces silent conflicts |
| Terminology state | Whether the terminology used is aligned, approved and versioned | Unaligned terminology corrupts safety, quality and supply evidence |

### 5.4 Authority, Effective Date and Jurisdiction

| Term | Business meaning | Risk if misunderstood |
|---|---|---|
| Authority | The designated source or record that is binding for a business object, jurisdiction and effective date | The wrong record may be treated as binding |
| Authoritative source | The record that governs a given fact for a given object, jurisdiction and date | A convenient but non-authoritative system may be used |
| Effective date | The date from which a record, decision or version is applicable | Records may be applied before or after their effective period |
| Jurisdiction | The regulatory or legal scope in which a record applies | A record approved in one country may be applied elsewhere |
| Approval date | The date an approval took effect | It may be confused with the effective date |
| Signed record | A record carrying an accountable signature or equivalent | An unsigned or back-entered record may be treated as approved |
| Validation state | The qualified status of an application or system for its intended use | An unvalidated system may be treated as authoritative |
| Master-data repair | The governed correction of master data after an incident such as ransomware | Repair windows may overlap audit-capture gaps |
| Protocol version | A version of a clinical protocol in effect for sites | Sites may execute a version not approved in a country |

### 5.5 Consent, Entitlement and Privacy

| Term | Business meaning | Risk if misunderstood |
|---|---|---|
| Consent | The lawful permission boundary for using a person's data | Data may be used without a valid basis |
| Entitlement | The role-based right to access, use or act on data | Users may act beyond their role |
| Privacy boundary | The constraint around access, use, sharing and cross-border routing of personal data | Privacy obligations may be bypassed |
| Cross-border routing | The transfer of data across jurisdictions under applicable law | Data may be routed without a lawful basis |
| Secondary use | Use of personal data beyond its original purpose | Data may be reused without a lawful basis |
| Sensitive segment | A portion of data carrying heightened privacy or special-category sensitivity | Sensitive content may sit in general queues |
| Lawful basis | The legal justification for processing personal data | Processing may proceed without justification |

### 5.6 PV Case Intake and Signal Support

| Term | Business meaning | Risk if misunderstood |
|---|---|---|
| ICSR | Individual case safety report describing a suspected adverse event | A duplicate may be treated as a new report |
| Duplicate ICSR | Two or more records likely describing the same event | Duplicates distort counts and reporting clocks |
| Awareness date | The date the organisation first became aware of a case | A disputed awareness date shifts the reporting clock |
| Reporting clock | The countdown to a regulatory submission deadline triggered by awareness | A wrong clock start can cause late reporting |
| Reporting-clock reconstruction | The evidence-based reconstruction of the awareness date and clock start | The reconstruction may be disputed across sources |
| Seriousness | The regulatory classification of an event's severity | The AI never makes the final seriousness decision |
| Causality | The assessment of whether a product caused an event | The AI never makes the final causality decision |
| Expectedness | Whether an event is consistent with product information | The AI never makes the final expectedness decision |
| Listedness | Whether an event is listed in a governing source (IB, CCDS, local label) | Conflicts between sources must be visible, not resolved |
| Investigator brochure (IB) | The governing safety document for an investigational product | It may conflict with CCDS or local label |
| Core data sheet (CCDS) | The company core data sheet defining safety information for a marketed product | It may conflict with IB or local label |
| Local label | The country-specific approved labelling | It may differ from the CCDS |
| Product-quality complaint | A report about a possible product quality defect | It may link to a safety case |
| Multilingual review | Review across the languages of the reporting region | Mis-translation may distort case content |
| Reportability | Whether a case must be reported to a regulator within a timeframe | The AI never makes the final reportability decision |
| Signal confirmation | The confirmation that a signal requires regulatory action | The AI never confirms signals |
| Case-intake completeness | Whether all required intake fields and sources are captured | Incomplete intake may hide duplicate or mis-coded cases |

### 5.7 Supply, Cold-Chain and Allocation

| Term | Business meaning | Risk if misunderstood |
|---|---|---|
| Inventory status | The quality-bounded availability state of stock (e.g., released, quarantined) | A status change must not be made by advisory tools |
| Cold-chain excursion | A temperature excursion outside the product's required range | The shipment may be handled as safe or unsafe without evidence |
| Temperature logger | A device recording temperature over time | Disputed logger clocks undermine the evidence |
| Logger clock | The clock used by a temperature logger | A disputed clock changes the excursion window |
| Pallet association | The link between a shipment and its pallets or cases | A disputed association misattributes temperature evidence |
| Serialisation aggregation | The linkage of cases to pallets in the serialisation hierarchy | Missing aggregation hides which cases are affected |
| Sole-source excipient | An excipient supplied by a single supplier | A contamination halts supply with no alternative |
| Excipient shortage | A supply gap of an excipient with a stated recovery estimate | Recovery estimates may be treated as certainty |
| Recovery estimate | The supplier's estimated time to resume supply | It is an estimate, not a commitment |
| CMO capacity | The available production capacity at a contract manufacturer | The same CMO may over-promise to two sponsors |
| CMO capacity conflict | A CMO promising capacity that cannot serve all sponsors | Conflicting promises must be visible before options |
| Allocation constraint | A rule limiting how available stock may be distributed | Constraints may be ignored under shortage pressure |
| Allocation policy | The approved policy for distributing scarce stock across markets, trials and compassionate use | Allocation without approval violates the non-negotiables |
| Compassionate-use entitlement | The legal and regulatory right for a patient to receive an investigational product | Entitlements must be respected in constrained allocation |
| Market authorisation | The approval to place a product on a market | A product may not be distributable in a market without it |
| Trial demand | Demand for product for clinical trial supply | Trial and commercial demand compete for the same stock |
| Shipment | The physical dispatch of product | A shipment must never be executed by advisory tools |

### 5.8 Source and Document Governance

| Term | Business meaning | Risk if misunderstood |
|---|---|---|
| Source | The originating record of an item of evidence | A transcribed or tool-derived value may be treated as the source |
| Source authority | Which source governs a given fact (per object, jurisdiction and date) | The wrong source may be treated as binding |
| Document version | The version of a controlled document in effect | An obsolete version may be applied |
| Approved document | A document released under the document-control process | A draft may be treated as approved |
| Untrusted document | A document not yet governed for use (e.g., a supplier PDF) | A prompt-injection document may be treated as evidence |
| Manifest | A declaration of tool definitions and entitlements | Stale or unsigned manifests may be trusted |
| Quarantine | The state of an untrusted document pending governance review | A quarantined document may be used prematurely |
| Transcription | A re-entry of a source value (e.g., a certificate) | Transcribed values may drift from the signed original |
| Signed original | The record carrying the accountable signature | Copies without the signed original are weaker evidence |

### 5.9 Audit and Evidence

| Term | Business meaning | Risk if misunderstood |
|---|---|---|
| Audit trail | The chronological, tamper-evident record of who did what, when, and from what source | A gap makes the trail incomplete |
| Audit-capture gap | A period when audit capture was disabled (e.g., 47 minutes during repair) | The gap must remain visible, not silently filled |
| Auditability | The property that every recommendation, draft, approval, override, release, escalation, action, outcome and closure can be shown | Work may appear complete without proof |
| Recommendation | A suggested option or next step that remains subject to human review | A suggestion may be mistaken for a decision |
| Draft | A prepared but not yet approved item | A draft may be treated as final |
| Approval | Human review outcome that permits an item to proceed within its scope | Approval may be assumed without a named owner |
| Override | A human-authorized deviation from normal requirements with recorded reason | Overrides may occur without reason or evidence |
| Escalation | Routing a matter for attention because normal completion is blocked | An escalation may be treated as resolved |
| Final action | The actual completed action after review, approval, escalation or override | Planned actions may be confused with completed ones |
| Evidence lineage | The chain of sources behind a piece of evidence | Breaks in lineage weaken defensibility |
| Evidence package | The assembled, citable evidence set for a decision or inspection | A package may be treated as proof of approval |

### 5.10 Continuity, Reliability and Economy

| Term | Business meaning | Risk if misunderstood |
|---|---|---|
| Degraded mode | Operating with reduced system availability (e.g., MES/QMS degraded) | Work may proceed without required evidence |
| Ransomware response | Operating safely during and after a ransomware event | Historians may be isolated and unreachable |
| Operate safely without AI | Continuing accountable review work when AI inference is unavailable | Dependence on AI may halt regulated work |
| Master-data repair window | The period when master data is being repaired | It may overlap an audit-capture gap |
| Model outage | A period when an AI model is unavailable | Work must still proceed safely |
| Vendor concentration | Dependence on a single vendor for supply or services | A vendor exit may halt critical operations |
| Substitutability | The ability to replace a vendor or model | Missing substitutability increases supply risk |
| Token budget | The consumption limit for model usage | Cost and usage must be governed |
| Continuity requirement | The requirement to keep regulated work safe without key systems | Continuity may be an afterthought |
| Retirement | The governed removal of a system or model from service | Retired systems may still be relied on unknowingly |

## 6. Status, Exception, and Approval Language

| Language item | Meaning in this case | Must not be confused with |
|---|---|---|
| Evidence-complete | All required evidence present, attributed and resolvable | Approved, released or certified |
| Conflict-visible | Contradictions shown to owners, not resolved | A resolved conflict |
| Fail-closed | No output while required state is unresolved | Proceeding on a best guess |
| Pending | Waiting for required input, review or approval | Complete or approved |
| Incomplete | Required elements are missing | Merely delayed |
| Unresolved | A required state is open and owned | Closed or ignored |
| Needs review | Requires accountable human review | Resolved or safe to release |
| OOS | A result outside specification, under investigation | A final batch rejection |
| OOT | A result out of statistical trend | OOS or invalid |
| Invalid | A result judged invalid by the laboratory | OOS or OOT |
| Approved | Reviewed and accepted by the authorised human owner for a specific scope | Globally approved for every downstream use |
| Certified | QP certification decision made | Evidence package complete |
| Released | Batch released to the market by accountable Quality/QP | Review-ready or draft |
| Rejected | Batch rejected by accountable Quality | OOS or investigation pending |
| Allocated / reserved / shipped | Executed supply actions | Proposed allocation options |
| Recalled | A recall initiated by authorised roles | A recall candidate or recommendation |
| Overridden | A normal rule or gap bypassed by authorised human decision with reason | Automatically resolved |
| Closed | Completed with required outcome recorded | No longer visible |
| Checkpoint state | A required gate in a workflow with explicit pass/fail status | An informational status |
| Quarantined | An untrusted document held pending governance | Available for use |
| Auditable | Traceable with evidence, owner, timestamp and action | Merely documented somewhere |

## 7. Ambiguous Terms Requiring Care

| Ambiguous term | Why it requires care |
|---|---|
| Ready | Could mean review-ready, release-ready, approved, or merely planned |
| Complete | Could mean evidence gathered, packet assembled, review done, certification done, or action executed |
| Reviewed | Could mean glanced at, reconciled, statistically assessed, or formally approved |
| Approved | Must specify approved by whom, for what purpose, and for which downstream use |
| Authority | Could mean system authority, record authority, role authority, or regulatory authority |
| Effective date | Could mean approval date, implementation date, or the date a record governs |
| Version | Could mean document version, protocol version, MedDRA version, or label version |
| Unit | Could mean mg/L vs µg/mL, or units of material quantity; must be explicit |
| Genealogy | Could mean batch genealogy, material lineage, aggregation hierarchy, or device lineage |
| Deviation | Could mean quality deviation, process excursion, or environmental monitoring excursion |
| Complaint | Could mean product-quality complaint or a safety report |
| Intake | Could mean PV case intake, document intake, or data intake |
| Capacity | Could mean CMO capacity, trial capacity, warehouse capacity, or model capacity |
| Demand | Could mean market demand, trial demand, or compassionate-use demand |
| Monitoring | Could mean environmental monitoring, safety monitoring, or cold-chain monitoring |
| Evidence | Could mean a source record, a transcribed certificate, a tool output, or a notebook entry |
| Ownership | Could mean task ownership, decision ownership, or regulated accountability |
| Advisory | Could mean recommendation, option, or a prepared evidence package — never a decision |
| Correction | Could mean record correction, organism-identification correction, or master-data repair |

## 8. Terms That Must Not Be Used Loosely

These terms must be used carefully because they imply approval, release, rejection, certification, completion, ownership, or an executed regulated action:

- Batch release
- Batch rejection
- Reprocess
- Re-label
- Recall
- Seriousness
- Causality
- Expectedness
- Reportability
- Signal confirmation
- Inventory status change
- Capacity reservation
- Stock allocation
- Shipment
- Batch certification / release decision
- QP certification
- Certified
- Released
- Rejected
- Recalled
- Allocated
- Reserved
- Shipped
- Approved (in a regulated sense)
- Evidence-complete (unless the completeness condition is actually satisfied)
- Release-ready (unless the accountable release decision owners have reached it)
- Case dispositioned
- Signal confirmed

## 9. Known Gaps Expressed in Ubiquitous Language

The following gaps are standardized for later stages. They are not resolved here.

| Known gap | Standardized language |
|---|---|
| SUA-88 missing from one MES genealogy branch but present in warehouse consumption | Genealogy break: batch NCB204-B24071 material/batch lineage is unresolved; identity and lineage state requires ownership |
| Contract-laboratory concentration in mg/L while the receiving interface assumes µg/mL | Unit-conversion assumption unapproved and inconsistent; unit state unresolved and must be fail-closed |
| LIMS marks OOS, statistical tool marks OOT, notebook labels invalid | Assay result state disputed across OOS, OOT and invalid; conflict-visible with open investigation ownership |
| EU release packet lacks confirmation of a contract-site audit commitment | Supplier-evidence gap: audit commitment claimed closed but not independently verified; release-packet completeness open |
| Batch-record step back-entered after network degradation | Back-entered batch-record step with checkpoint and audit evidence requiring ownership |
| Audit capture disabled for 47 minutes during master-data repair | Audit-capture gap: audit trail incomplete for the repair window; must remain visible |
| Disputed awareness date across vendor receipt, affiliate inbox and global safety DB | Reporting-clock reconstruction disputed; awareness date unresolved with source-authority conflict |
| Duplicate ICSR cluster under different product names | Duplicate ICSR candidates exist; duplicate-detection outcome pending review |
| Two MedDRA versions change the preferred term | Preferred-term conflict across MedDRA versions; terminology state unresolved |
| IB, CCDS and local label disagree on listedness | Listedness-source conflict: expectedness evidence not aligned across governing sources |
| Biologic shipment exceeds range with disputed logger clocks and pallet association | Cold-chain excursion evidence disputed: temperature logger clock and pallet association unresolved |
| Case-to-pallet aggregation missing after a line restart | Serialisation aggregation gap: case-to-pallet linkage missing and requires evidence |
| Sole-source excipient contamination with eight-week recovery; CMO promises capacity to two sponsors; demand exceeds stock | Supply-shortage constraint: sole-source excipient, CMO capacity conflict and allocation constraint; no allocation without authorised human approval |
| Validation state ambiguous across inventories; unapproved macro-enabled spreadsheet in use | Validation-state ambiguity and unapproved tooling: checkpoint and source-governance state unresolved |
| Supplier deviation PDF with hidden prompt-injection text; stale/unsigned tool manifests; shared-account spreadsheets | Untrusted-source governance: supplier PDF and tool manifests require quarantine before use |

## 10. Non-Negotiables Carried Forward

- The AI never releases, rejects, reprocesses, re-labels or recalls a batch.
- The AI never makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions.
- The AI never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval.
- The AI never changes formulation, specification, clinical eligibility, safety-case disposition, batch release or recall decisions.
- Regulated accountability remains with the accountable Quality, Safety, Regulatory, Clinical and Supply roles.
- Evidence output must not be produced while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
- Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable.
- The system operates read-only and advisory; it prepares, reconciles, explains and packages evidence.
- No product, batch, safety, quality or supply issue is considered resolved merely because it has been identified.

## 11. Open Questions for Stage 4

Stage 4 should carry these language-driven boundary questions into bounded context design:

- Which bounded context owns the meaning and lifecycle of batch-review readiness and release-ready status?
- Which bounded context owns release-packet completeness and QP-certification evidence packaging (not the certification decision)?
- Which bounded context owns genealogy and identity resolution, and the visible status of a genealogy break?
- Which bounded context owns unit-conversion assumptions and terminology/MedDRA version state?
- Which bounded context owns authority, effective-date and jurisdiction resolution per business object?
- Which bounded context owns PV case-intake completeness, reporting-clock reconstruction, duplicate detection, terminology alignment and listedness evidence?
- Which bounded context owns supply-shortage and cold-chain recovery option status (without executing allocation or shipment)?
- Which bounded context owns consent, entitlement and privacy boundary checks?
- Which bounded context owns source and document governance, including quarantine of untrusted documents?
- Which bounded context owns the audit trail, the audit-capture gap, and evidence packaging for inspection?
- Which bounded context owns validation-state ambiguity and continuity in degraded mode?
- Which terms must be shared across contexts without changing meaning (shared kernel or published language)?
- Which terms must be protected from being redefined differently by different functions?

## 12. STAGE_4_INPUT_BLOCK

```text
Stage 4 Input — Bounded Context Canvases

Main Business Domain:
Governed evidence reconciliation and review support for regulated pharmaceutical workflows

Core Subdomains:
- GxP Evidence Reconciliation for Batch-Review Readiness (Workflow A)
- Pharmacovigilance Case-Intake and Signal-Support (Workflow B)
- Bounded Supply-Shortage and Cold-Chain Recovery Planning (Workflow C)

Supporting Subdomains:
- Identity, Genealogy and Product-Master Resolution
- Unit, Terminology and Reference-Data Standardisation
- Authority, Effective-Date and Jurisdiction Management
- Consent, Entitlement and Privacy Management
- Source and Document Governance
- Supplier and Audit-Evidence Management
- Regulatory and Inspection-Readiness Coordination
- Quality-Event and Deviation Lineage
- Evidence and Audit-Trail Management
- Continuity, Reliability and Economy Management

Key Ubiquitous Language Terms:
- Governed evidence reconciliation and review support
- Evidence-complete
- Conflict-visible
- Provenance-backed
- Authority-respected
- Fail-closed
- Read-only advisory
- Batch-review readiness
- Release-ready
- Abstention / no-answer
- Batch identity
- Genealogy
- Material/batch lineage
- Genealogy break
- Single-use assembly lot
- OOS
- OOT
- Environmental monitoring excursion
- Deviation
- CAPA
- Change control
- Validation state
- Back-entered record
- Release packet
- Release-packet completeness
- QP certification
- Unit-conversion assumption
- Reported unit
- MedDRA version
- Preferred term
- Authority
- Authoritative source
- Effective date
- Jurisdiction
- Signed record
- Consent
- Entitlement
- Privacy boundary
- ICSR
- Duplicate ICSR
- Awareness date
- Reporting clock
- Reporting-clock reconstruction
- Seriousness
- Causality
- Expectedness
- Listedness
- Investigator brochure
- Core data sheet (CCDS)
- Local label
- Product-quality complaint
- Signal confirmation
- Inventory status
- Cold-chain excursion
- Temperature logger
- Pallet association
- Serialisation aggregation
- Sole-source excipient
- CMO capacity
- Allocation constraint
- Compassionate-use entitlement
- Market authorisation
- Source
- Untrusted document
- Quarantine
- Audit trail
- Audit-capture gap
- Recommendation
- Draft
- Approval
- Override
- Escalation
- Final action
- Evidence package
- Degraded mode
- Operate safely without AI

Terms Requiring Ownership Clarity:
- Batch-review readiness
- Release-ready
- Release-packet completeness
- Genealogy break
- Unit-conversion assumption
- OOS / OOT / invalid state
- Validation state
- Authority, effective date and jurisdiction
- Awareness date
- Reporting-clock reconstruction
- Duplicate ICSR
- Preferred-term conflict
- Listedness-source conflict
- Cold-chain excursion evidence
- Serialisation aggregation
- Allocation constraint
- Audit-capture gap
- Untrusted-source quarantine
- Consent and entitlement checks

Terms Requiring Approval Clarity:
- Batch release
- Batch rejection
- Reprocess
- Re-label
- Recall
- QP certification / batch certification decision
- Seriousness, causality, expectedness, reportability, signal confirmation
- Inventory status change
- Capacity reservation
- Stock allocation
- Shipment
- Override approved
- Evidence-complete
- Release-ready

Known Gaps in Standardized Language:
- SUA-88 genealogy break → Genealogy break: material/batch lineage unresolved; identity and lineage state requires ownership
- mg/L vs µg/mL → Unit-conversion assumption unapproved and inconsistent; unit state unresolved and fail-closed
- OOS vs OOT vs invalid → Assay result state disputed; conflict-visible with open investigation ownership
- Unverified supplier-audit commitment → Supplier-evidence gap; release-packet completeness open
- Back-entered batch-record step → Back-entered record with checkpoint and audit evidence requiring ownership
- 47-minute audit-capture gap → Audit trail incomplete for the repair window; must remain visible
- Disputed awareness date → Reporting-clock reconstruction disputed; awareness date unresolved
- Duplicate ICSR candidates → Duplicate-detection outcome pending review
- MedDRA version mismatch → Preferred-term conflict; terminology state unresolved
- Listedness conflict (IB/CCDS/local label) → Expectedness evidence not aligned across governing sources
- Cold-chain logger/pallet dispute → Cold-chain excursion evidence disputed; logger clock and pallet association unresolved
- Missing aggregation → Serialisation aggregation gap; case-to-pallet linkage missing
- Excipient shortage / CMO capacity conflict / demand exceeds stock → Supply-shortage constraint; no allocation without authorised human approval
- Validation-state ambiguity / unapproved spreadsheet → Checkpoint and source-governance state unresolved
- Untrusted supplier PDF and tool manifests → Untrusted-source governance; quarantine required

Non-Negotiables:
- AI never releases, rejects, reprocesses, re-labels or recalls a batch.
- AI never makes final PV seriousness, causality, expectedness, reportability or signal-confirmation decisions.
- AI never changes inventory status, reserves capacity, allocates stock, ships product or initiates a recall without explicit authorised human approval.
- AI never changes formulation, specification, clinical eligibility, safety-case disposition, batch-release or recall decisions.
- Regulated accountability remains with the accountable Quality, Safety, Regulatory, Clinical and Supply roles.
- No evidence output while identity, genealogy, unit, terminology, authority, effective date, jurisdiction, consent/entitlement, validation or checkpoint state is unresolved.
- Every recommendation, draft, approval, override, release, escalation, action, outcome and closure must be auditable.
- The system operates read-only and advisory; it prepares, reconciles, explains and packages evidence.
- No product, batch, safety, quality or supply issue is considered resolved merely because it has been identified.

Open Questions for Stage 4:
- Which bounded context owns batch-review readiness and release-ready lifecycle?
- Which bounded context owns release-packet completeness and QP-certification evidence packaging?
- Which bounded context owns genealogy/identity resolution and genealogy-break status?
- Which bounded context owns unit and terminology standardisation state?
- Which bounded context owns authority, effective-date and jurisdiction resolution?
- Which bounded context owns PV intake, reporting-clock reconstruction, duplicate detection and listedness evidence?
- Which bounded context owns supply-shortage and cold-chain recovery option status?
- Which bounded context owns consent, entitlement and privacy boundary checks?
- Which bounded context owns source/document governance and quarantine?
- Which bounded context owns the audit trail, audit-capture gap and evidence packaging?
- Which bounded context owns validation-state ambiguity and continuity in degraded mode?
- Which terms must be shared across contexts without changing meaning?
```

Stage 3 complete. Use the STAGE_4_INPUT_BLOCK as the main input for Stage 4.
