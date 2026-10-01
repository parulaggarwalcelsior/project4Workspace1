# Implementation Plan: Test Evidence Definition

**Branch**: `002-test-evidence-definition` | **Date**: 2026-09-30 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/002-test-evidence-definition/spec.md`

## Summary

Create the documentation records for the evidence-definition-only candidate. The candidate records the work-unit operator as the scope-owner role, an explicitly unavailable acceptance artifact, the selected documentary evidence-review evaluation type, and the documented limits of the legacy reading. It neither executes the Java estate nor defines a Go implementation, expected legacy output, or parity result. The scope owner has stated `Acceptance boundaries: (none stated)`, so this plan is blocked from advancing acceptance planning or acceptance validation.

## Technical Context

**Language/Version**: Markdown documentation; the legacy reading reports Java, while Go is only a declared future target.

**Primary Dependencies**: Permitted legacy readings in `../../old/docs/`; [spec.md](spec.md); the project constitution.

**Storage**: Versioned Markdown records under `specs/002-test-evidence-definition/`.

**Testing**: Documentary evidence review using [quickstart.md](quickstart.md) may verify evidence classifications, reading limits, and the blocked acceptance-criteria gate. It MUST NOT report an acceptance-validation result; no executable legacy or migration test is in scope.

**Target Platform**: This workspace's documentation review.

**Project Type**: Evidence-definition documentation candidate.

**Performance Goals**: None; no runtime system is proposed.

**Constraints**: Preserve documented unavailable and unsearched areas as reading limits; classify every estate-related claim; do not state an expected legacy output, execution result, or Java-to-Go parity result.

**Scale/Scope**: One bounded evidence-definition candidate concerning the documented 115-item Java inventory; it does not select an estate behaviour or an inventory-wide test target.

## Acceptance-Criteria Gate

**Scope-owner response (2026-10-01)**: `Acceptance boundaries: (none stated)` ([spec.md](spec.md#acceptance-criteria-gate)).

**Plan status: BLOCKED.** No relevant acceptance criteria are available for this candidate. The plan may retain its documentary record structure, but no further acceptance planning or acceptance validation may proceed until the scope owner supplies the criteria. The frozen acceptance basis recorded by [approach.md](../../../../old/docs/approach.md) does not supply those criteria here.

## Constitution Check

| Gate | Plan status | Evidence / treatment |
|---|---|---|
| I. Evidence-Bound Description | Pass | The plan cites only permitted readings and labels the selected boundary, unavailable artifact, and evaluation type as proposed scope decisions. |
| II. Unknowns Remain Explicit | Pass | The acceptance artifact is recorded as unavailable; persistence, endpoints, security, edge cases, and workflows remain documented limits. |
| III. Specification Precedes Delivery | Blocked | The specification's [Acceptance-Criteria Gate](spec.md#acceptance-criteria-gate) records the scope-owner response `Acceptance boundaries: (none stated)`. This plan cannot advance acceptance planning or acceptance validation without relevant criteria. |
| IV. Migration Preserves Established Semantics | Pass | No behaviour is re-expressed, executed, or compared between Java and Go. |
| V. Traceable Acceptance | Blocked | The review process distinguishes cited evidence, reading limits, proposed decisions, and blocked outcome assertions, but no acceptance criteria are supplied to trace to an acceptance result. |

**Post-design re-check**: Blocked for acceptance planning and acceptance validation. The data model and validation guide retain the evidence-only boundary, but cannot establish an acceptance result without scope-owner criteria.

## Project Structure

### Documentation (this feature)

```text
specs/002-test-evidence-definition/
├── spec.md                    # Scope, decisions, requirements, and evidence basis
├── plan.md                    # This plan
├── research.md                # Recorded planning decisions
├── data-model.md              # Candidate documentation-record schemas
├── quickstart.md              # Documentary validation procedure
├── scope-intake.md            # Created by implementation tasks
├── evidence-register.md       # Created by implementation tasks
├── claim-review-checklist.md  # Created by implementation tasks
├── evidence-review.md         # Created by implementation tasks
├── next-test-slice.md         # Created by implementation tasks
└── tasks.md                   # Task-stage output; not modified by this plan
```

No `contracts/` directory is created: this candidate exposes no runtime, API, CLI, or other external interface. Its record shapes are internal documentation schemas in [data-model.md](data-model.md).

**Structure Decision**: Retain all work in the feature documentation directory. The implementation-stage records named above are separated by review purpose, not by a runtime architecture.

## Complexity Tracking

No constitution violations or complexity exceptions apply.
