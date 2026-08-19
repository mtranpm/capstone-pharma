# AEGIS Evidence Orchestrator — Executive Brief

| Field | Entry |
|---|---|
| Owner | Product / value lead |
| Version / date | 1.0.0 / 2026-08-15 |
| Audience | CQO, QP, Global Head of PV, Supply VP, RA, CISO, DPO |
| Full brief | [`executive_summary.md`](./executive_summary.md) |

**One-line pitch:** *Faster, auditable evidence packets. Humans keep every regulated pen.*

---

## The problem

NovaCura must defend batch, safety, and supply decisions while records across LIMS, MES, QMS, safety, and cold-chain systems disagree. Humans reconcile by hand — too slow for inspection, too unsafe to "fix" silently.

## The answer

**AEGIS Evidence Orchestrator** — a read-only, advisory layer that finds, reconciles, explains, and packages evidence with provenance, authority checks, and human-review gates. It **never** releases, certifies, disposes, allocates, ships, or recalls.

## Why an FDE approach

**FDE (AI Forward Deployed Engineering)** means engineers are embedded with the business and work from the real problem to a governed, safe implementation — never assuming a solution upfront. For NovaCura, we started from the actual pain (contradictory, time-boxed evidence) and moved through domain modeling to a minimal, defensive AI intervention.

### How FDE runs here — SCQA to spec-driven delivery

| Stage | FDE discipline | Deliverable | What it proves |
|---|---|---|---|
| 1 | **Business discovery first** | Evidence/inject map, affected decisions, accountable roles | What must be solved — and what must never be crossed |
| 2 | **SCQA (locked)** | Situation → Complication → Question → Answer | Executive framing; intervention stays narrower than the problem |
| 3 | **PRD** | Personas, jobs-to-be-done, in/out of scope | What we build and what we refuse to build |
| 4 | **Domain-driven design** | Context map, bounded contexts, ubiquitous language, entities & invariants | Domain truth modelled with its owners — rules vs reasoning separated |
| 5 | **Rules vs reasoning** | Deterministic, testable core; optional switchable LLM | Fail-closed, offline-capable, audit-ready reasoning |
| 6 | **Human decision ownership** | Authority gates, review-by-exception, emergency stop | QP / PV / Supply keep every regulated pen |
| 7 | **Evidence & audit model** | Provenance hashes, as-of statuses, immutable export | Defensible inspection response, end-to-end traceable |
| 8 | **Architecture + ADRs** | C4 model, integration contracts, 15 ADRs | Traceable, replaceable design with recorded decisions |
| 9 | **Traceability matrix** | Requirement → control → test links | Every claim maps to an artefact — provable, not claimed |
| 10 | **Spec-driven build** | Contracts-first, tests-first, gated delivery (0→7) | Contract-valid outputs; **54/54 tests**, **15/15 fixtures**, 0 grader failures |

**Spec-driven principle:** business discovery explains *what* problem must be solved and which boundaries must hold; technical specs prove those boundaries through **contracts, tests, controls, evidence and reproducible execution** — so the solution is defensible, not just demonstrated.

The result: a *defensible*, minimal AI intervention that makes the **14% release lead-time target** and the **72-hour inspection pack** achievable while authority and integrity are *stronger*, not weaker.

## What we ask

**Conditional go** to package evidence on NCB-204, NCS-310, NCX-101, NCR-415. Not a go for autonomous Quality, PV, or allocation.

---

## Proof points (workshop wave W0)

| Evidence | Status |
|---|---|
| Public fixtures PUB-01..15 | **15/15 evaluated**, 0 grader failures |
| Deterministic tests | **54/54 passed** |
| Contract-valid packets, provenance on all evidence | Verified per fixture |
| Fail-closed / abstention on conflicts | Verified (e.g., PUB-01, PUB-08) |
| No execute actions (`not_executed`) | Verified on all fixtures |
| Human review gates in front of export | Verified (QP / PV / Supply / control roles) |
| EU AI Act / ISO 42001 indicative mapping | Verified (Art. 14 oversight) |
| Human-agreement κ | Not claimed (labels not collected) |
| Live systems of record; GxP OQ/PQ | Not done — this is a workshop, not go-live |

## Boundaries

- **Never:** batch release/reject/recall, final PV decisions, stock allocation/shipment, clinical eligibility, MES/LIMS/PV write-back.
- **15** prohibited actions blocked in code; **6** human-review gates before export; emergency stop and AI-off continuity built in.
- Pens stay with **QP / Quality**, **PV medical**, and **Supply + Quality**.

## Path forward

W1 pilot (8–12 wks) on one batch site with read-only SoR API → W2 PV intake → W3 supply options → W4 scale. All read-only; kill-switch to a stub kept at every step.
