# Migration From Legacy

After reading this page, an engineer will understand the narrow, evidence-bound relationship between the legacy Java estate and this Markdown candidate. It maps only documented behaviours and limits; it does not present an unbuilt Go implementation as a migration.

## Legacy baseline

The legacy reading identifies Java as the source language, 115 inventory items, and `Project/src/LMS` as its sole listed component. It also says the interpretive pass did not run and records zero execution-grounded items, so it does not establish executable behaviour to reproduce ([legacy overview: Shape and How much is verified](../../old/docs/overview.md#shape)).

The model-composed legacy summary describes a library-management context and names library entities such as books, borrowers, requests, holds, librarians, staff, and clerks. Those names provide vocabulary only; their behavioural contracts are not verified by the permitted reading ([legacy summary: What this system is for and Who it serves](../../old/docs/summary.md#what-this-system-is-for); [spec.md: Evidence Basis and Scope Boundary](../specs/002-test-evidence-definition/spec.md#evidence-basis-and-scope-boundary)).

## Legacy-to-current mapping

| Legacy behaviour or reading | Current implementation location | Preservation / change |
|---|---|---|
| 115-item Java inventory, with 0 execution-grounded items | `spec.md` Evidence Basis; `evidence-register.md` classification model | Preserved as a reason not to select a behaviour-level test target. | [spec.md: Evidence Basis](../specs/002-test-evidence-definition/spec.md#evidence-basis-and-scope-boundary) |
| Persistence reading `UNAVAILABLE` | `evidence-register.md` persistence entry; `evidence-review.md` User Story 2 | Preserved as a reading limit; no data model is invented. | [evidence register](../specs/002-test-evidence-definition/evidence-register.md#evidence-register-entries) |
| Endpoint reading `UNAVAILABLE` | Same records' endpoint entry and review | Preserved as a reading limit; no route or API is implemented. | [evidence review: User Story 2](../specs/002-test-evidence-definition/evidence-review.md#user-story-2-reading-limit-review) |
| Security, edge-case, and workflow searches `Could not search` | Same records' three entries and review | Preserved as unsearched; no security, failure, or workflow behaviour is claimed absent. | [evidence register](../specs/002-test-evidence-definition/evidence-register.md#evidence-register-entries) |
| Frozen acceptance basis, contents not supplied | `scope-intake.md` and `next-test-slice.md` | Preserved as explicitly unavailable; it does not become an oracle. | [scope intake: Acceptance artifact](../specs/002-test-evidence-definition/scope-intake.md) |
| Java-to-Go direction | No code location; recorded only as context | Dropped from implementation: neither Java execution nor Go code is built. | [AGENTS.md: operator goal](../AGENTS.md); [plan.md: Summary](../specs/002-test-evidence-definition/plan.md#summary) |

## What changed, what was preserved, and what was dropped

The current candidate changes the form of the work from a legacy estate reading to reviewable Markdown records. It preserves the reported inventory facts and uncertainty labels, because the constitution requires unknowns to remain explicit ([constitution: Principles I and II](../.specify/memory/constitution.md#core-principles)).

It deliberately drops a Go implementation, a Java baseline run, a parity harness, behavioural test cases, persistence, endpoints, security controls, and deployment. These are not claims that the legacy estate lacks them; none is present in this tree, and the evidence-only scope excludes execution and parity evaluation ([research.md: Decisions 1, 3, and 4](../specs/002-test-evidence-definition/research.md#decision-1-immediate-boundary)).

## Compatibility notes

Consumers of the old estate cannot substitute this repository for a library-management application. It has no API, data model, runtime command, or compatibility guarantee; its only executable command checks documentation records ([plan.md: Project Structure](../specs/002-test-evidence-definition/plan.md#project-structure); [referee test: module docstring](../.referee/002-test-evidence-definition/test_evidence_definition.py)).

Before a compatibility or migration claim can be made, a later slice needs a supplied observable contract, acceptance check, and evaluation basis; the current next-slice record marks those inputs blocked ([next-test-slice record](../specs/002-test-evidence-definition/next-test-slice.md)).

## Gaps against the specification

The specified candidate intentionally stops before migration. The acceptance-criteria gate remains blocked, so no acceptance-planning, acceptance-validation, expected-output, or parity claim is available ([spec.md: Acceptance-Criteria Gate](../specs/002-test-evidence-definition/spec.md#acceptance-criteria-gate); [evidence review: T028](../specs/002-test-evidence-definition/evidence-review.md#t028-acceptance-criteria-source-and-cross-artifact-reconciliation)).
