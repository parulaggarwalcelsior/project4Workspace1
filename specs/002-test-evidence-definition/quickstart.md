# Validation Guide: Test Evidence Definition

## Purpose

Validate the documentation candidate without running the legacy Java estate, creating Go code, or claiming a migration result.

## Prerequisites

- Read [spec.md](spec.md), [plan.md](plan.md), [research.md](research.md), and [data-model.md](data-model.md).
- Use only the permitted legacy readings linked by [spec.md](spec.md).
- Treat the future implementation-stage record paths in [plan.md](plan.md) as proposed documentation outputs, not as existing evidence.

## Review procedure

1. Confirm that [spec.md](spec.md) contains three resolved entries under `## Clarifications` and no unresolved clarification marker.
   - Expected result: the boundary is evidence-definition only, the acceptance artifact is explicitly unavailable, and evaluation is documentary evidence review.
2. Confirm that FR-006 through FR-008 and SC-003 state the same three decisions.
   - Expected result: no legacy behaviour, expected output, or test execution is selected.
3. Confirm that [plan.md](plan.md), [research.md](research.md), and [data-model.md](data-model.md) use the same boundary and preserve the unavailable acceptance artifact.
   - Expected result: all downstream artifacts agree with the specification.
4. Review claims about persistence, endpoints, security, edge cases, and workflows against their cited legacy readings.
   - Expected result: each remains an unavailable or unsearched reading limit, not an assertion that the estate lacks the relevant behaviour.
5. Review any future scope intake, register, review, or next-slice records against [data-model.md](data-model.md).
   - Expected result: every estate-related claim has a citation or proposed-decision label, and every unsupported outcome assertion is blocked.

## Completion criterion

The candidate passes documentary review when its decisions and classifications are internally consistent and its reading limits remain explicit. This is not a legacy execution, test-result, or Java-to-Go parity result.
