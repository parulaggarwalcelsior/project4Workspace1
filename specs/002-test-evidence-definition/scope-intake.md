# Scope Intake Record

| Field | Value |
|---|---|
| Scope-owner role | work-unit operator |
| Test target | evidence-definition candidate only |
| Acceptance artifact | explicitly unavailable; contents and location are not supplied |
| Evaluation type | documentary specification and evidence review; excludes legacy execution and parity evaluation |
| Supplied-on date | 2026-09-30 |
| Provenance | Proposed scope decision; [spec.md](spec.md) and its permitted legacy sources ([overview.md](../../../../old/docs/overview.md), [approach.md](../../../../old/docs/approach.md)) |
| Blocked status | Outcome assertions blocked |

## Fixed Decision Traceability

| Fixed boundary decision in this intake | Matching clarification | Matching functional requirement |
|---|---|---|
| The immediate test target is the evidence-definition candidate only; no legacy behaviour, asset, or inventory-wide target is selected. | [Clarification: immediate target](spec.md#clarifications) — “Is the immediate target evidence-definition only, a specified behaviour or asset, or the full 115-item inventory?” | [FR-006](spec.md#functional-requirements) |
| The work-unit operator is the scope-owner role, and the frozen acceptance artifact is explicitly unavailable; its contents and location are not supplied, so no acceptance check is defined. | [Clarification: acceptance checks and supplier](spec.md#clarifications) — “What artifact(s) define the acceptance checks and who can supply them?” | [FR-007](spec.md#functional-requirements) |
| Evaluation is limited to documentary specification and evidence review; legacy execution and legacy-to-target parity evaluation are excluded. | [Clarification: meaning of `test`](spec.md#clarifications) — “Is `test` limited to specification/evidence review, legacy execution, legacy-to-target parity, or another stated evaluation?” | [FR-008](spec.md#functional-requirements) |
