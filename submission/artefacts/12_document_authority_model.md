# 12 — Document Authority Model

| Field | Entry |
|---|---|
| Owner | Quality / RA governance |
| Version | 0.1.0 |
| Status | Phase 4 — draft |
| Sources | `data/knowledge_catalog.csv`, `data/document_catalog.csv`, `data/document_lineage.csv`, A5 Source Governance, `09`, NN-04 |

## 1. Purpose

Define how AEGIS classifies documents for **decision support** — trusted, untrusted, superseded, pending — with **as-of** verification. This model gates retrieval and citations; it does not replace document control in the QMS.

## 2. Authority states

| State | Meaning | May support readiness? | Example (catalog) |
|---|---|---|---|
| **trusted** | Approved, effective, integrity verified | Yes, after jurisdiction + as-of match | `K-006` BATCH_RELEASE_EVIDENCE_POLICY |
| **pending** | Draft or not yet effective | No — risk flag only | Draft SOPs (if present) |
| **superseded** | Replaced by newer controlled version | No — historical context only | `K-007` BATCH_RELEASE_POLICY_OLD |
| **untrusted** | Unknown authority, failed verification, or quarantined | **Never** — NN-04 | `K-999` FAKE_PV_EXPEDITED_RULE |

Runtime mapping uses catalog columns: `authority`, `effective`, `status`, `trust`, `jurisdiction`, `supersedes`, `sha256`.

## 3. Verification pipeline

| Step | Check | Fail behaviour |
|---|---|---|
| V-01 **Identity** | `doc_id` resolves to catalog row | Abstain: unknown document |
| V-02 **Integrity** | SHA-256 of `knowledge/{file}` matches catalog | Quarantine as untrusted |
| V-03 **Lifecycle** | `status` ∈ {approved, superseded, …} | Pending/superseded rules apply |
| V-04 **Effective date** | Evaluation as-of ≥ effective (policy-defined) | Pending |
| V-05 **Jurisdiction** | Applicable to workflow market | Abstain or scoped citation |
| V-06 **Supersession** | If superseded, link to successor id | Do not authorize from old doc |
| V-07 **Provenance** | Emit audit: doc_id, hash, classifier version | Required on every cite |

Implementation seam: **`AuthorityPort.classify_document(doc_id)`** (+ file hash helper in adapter).

## 4. As-of and concurrent versions

| Situation | Rule |
|---|---|
| IB vs CCDS vs local label (listedness) | Present **comparison**; Authority context does not pick winner |
| Effective policy update mid-run | Run pins catalog snapshot id + as-of at start |
| Superseded policy cited in old packet | Export shows successor pointer from `supersedes` |

## 5. Untrusted inputs (non-catalog)

| Source | Treatment |
|---|---|
| User upload / chat paste | Untrusted until V-01..V-07 |
| Tool description / manifest | `ToolManifestPort`; poisoned → block |
| Prompt-injection PDF (case) | Quarantine; audit security event |
| Shared-account spreadsheet (`spreadsheet_inventory.csv`) | Untrusted or conditional per validation state |

## 6. Packet citation shape (minimum)

Each material policy claim in a packet should carry:

```json
{
  "doc_id": "K-006",
  "authority_status": "trusted",
  "effective": "2026-06-01",
  "jurisdiction": "Global",
  "sha256": "<from catalog>",
  "retrieved_at": "<run timestamp>",
  "as_of": "<evaluation parameter>"
}
```

Values must match catalog verbatim — no normalization of dates or status strings.

## 7. Roles

| Role | Responsibility |
|---|---|
| Document owner | Maintains catalog + knowledge file |
| Quality | Approves trusted set for GxP gates |
| RA | Jurisdiction applicability |
| Platform | Implements AuthorityPort + hash checks |
| CISO | Untrusted/quarantine security incidents |

## 8. Tests & requirements

| REQ | Test intent |
|---|---|
| NN-04 | Superseded/untrusted cannot authorize |
| BAT-01 / PV-01 / SUP-01 | Citations include authority_status |
| PUB-09 | Poisoned doc blocked |

## 9. Links

- Data governance: [`09_data_governance_lineage_contracts.md`](09_data_governance_lineage_contracts.md)  
- Ontology class `KnowledgeDocument`: [`10_ontology_semantic_layer.md`](10_ontology_semantic_layer.md)  
- Source corpus: `data/knowledge_catalog.csv`, `knowledge/*.md`
