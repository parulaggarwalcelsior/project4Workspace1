# Overview

After reading this page, an engineer will know that this is a documentation-only evidence gate, who reviews it, the limited facts available about the legacy estate, and which claims remain explicitly unknown. This page describes the built candidate rather than treating the migration intention as a system implementation.

## What this is and why it exists

The built system is the `specs/002-test-evidence-definition/` Markdown candidate plus its documentary review controls. Its immediate target is the “evidence-definition candidate only,” selected as a proposed scope decision because the legacy reading contains `0 of 115` execution-grounded items and no described behaviour ([scope intake: Test target](../specs/002-test-evidence-definition/scope-intake.md); [legacy overview: How much is verified](../../old/docs/overview.md#how-much-is-verified)).

It serves the work-unit operator and reviewers. The candidate lets them distinguish legacy evidence, limits of the reading, supported inferences, and proposed scope decisions before someone defines an observable test or migration contract ([spec.md: FR-001 through FR-004](../specs/002-test-evidence-definition/spec.md#functional-requirements); [evidence register: Allowed Classification Values](../specs/002-test-evidence-definition/evidence-register.md#allowed-classification-values)).

## What the legacy reading actually establishes

The legacy reading reports a Java estate with 115 inventory items and one component path, `Project/src/LMS`, but says its interpretive pass did not run. Its executive summary calls it a library-management system and names library, books, borrowers, requests, holds, librarians, and clerks; that is a model-composed summary, not execution-grounded behavioural evidence ([legacy overview: Shape and What this system is](../../old/docs/overview.md#shape); [legacy summary: What this system is for](../../old/docs/summary.md#what-this-system-is-for)).

Persistence and endpoint discovery are `UNAVAILABLE`; security, edge-case, and workflow searches are `Could not search`. These are limitations of the reading, not findings that the estate lacks those capabilities ([evidence register: first five entries](../specs/002-test-evidence-definition/evidence-register.md#evidence-register-entries)).

## Glossary

| Term | Meaning in this repository | Evidence |
|---|---|---|
| Legacy estate | The Java estate described by the permitted legacy documents, not code present here. | [constitution: Evidence and Scope Constraints](../.specify/memory/constitution.md#evidence-and-scope-constraints) |
| Evidence-definition candidate | The selected documentation-only test target. It is a proposed decision, not legacy behaviour. | [scope intake: Test target](../specs/002-test-evidence-definition/scope-intake.md) |
| Reading limit | An unavailable or unsearched legacy-reading area that cannot justify a negative claim. | [spec.md: Key Entities](../specs/002-test-evidence-definition/spec.md#key-entities) |
| Acceptance artifact | The source that would supply an expected outcome or completion check. Its contents and location are explicitly unavailable here. | [spec.md: Key Entities](../specs/002-test-evidence-definition/spec.md#key-entities) |
| Scope owner | The `work-unit operator` role recorded for this candidate; no named individual is supplied. | [scope intake: Scope-owner role](../specs/002-test-evidence-definition/scope-intake.md) |
| Documentary review | Review of citations, classifications, limits, and blocked claims; not test execution. | [plan.md: Testing](../specs/002-test-evidence-definition/plan.md#technical-context) |
| Blocked | A review status: required inputs for an outcome claim have not been supplied. It is not a claim that the legacy system fails. | [data model: Evidence Register Entry](../specs/002-test-evidence-definition/data-model.md#evidence-register-entry) |

## Deliberately out of scope

Legacy execution, Go implementation, Java-to-Go parity evaluation, an inventory-wide test target, a selected legacy behaviour, an expected legacy output, and an acceptance-validation result are out of scope or blocked ([scope intake: Fixed Decision Traceability](../specs/002-test-evidence-definition/scope-intake.md#fixed-decision-traceability); [evidence review: T020](../specs/002-test-evidence-definition/evidence-review.md#t020-acceptance-criteria-reconciliation)).

## Gaps against the specification

The specification itself requires an acceptance-criteria gate. The recorded response is `Acceptance boundaries: (none stated)`, so the candidate must not advance acceptance planning or acceptance validation ([spec.md: Acceptance-Criteria Gate](../specs/002-test-evidence-definition/spec.md#acceptance-criteria-gate)). No implementation files exist to document beyond these records.
