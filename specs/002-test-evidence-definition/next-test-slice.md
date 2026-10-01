# Next-Test-Slice Record

Each row assigns one FR-002 classification to the claim and records outcome eligibility separately as its review status. `blocked` is a review status, not a classification.

| Field | Claim | FR-002 classification | Source or decision reference | Review status |
|---|---|---|---|---|
| Bounded subject | The test target is the evidence-definition candidate only; no legacy behaviour, asset, or inventory-wide test target is selected. | proposed scope decision | [Clarification: immediate target](spec.md#clarifications); [FR-006](spec.md#functional-requirements) | supported |
| Input | No input is supplied with observable-contract evidence. | supported inference | [overview.md](../../../../old/docs/overview.md) — the interpretive pass has not run; [approach.md](../../../../old/docs/approach.md) — there is nothing concrete to design tests against; [FR-004](spec.md#functional-requirements) | blocked |
| Expected outcome | No expected legacy outcome is supplied. | supported inference | [overview.md](../../../../old/docs/overview.md) — the interpretive pass has not run; [approach.md](../../../../old/docs/approach.md) — no behaviour has been described; [FR-004](spec.md#functional-requirements) | blocked |
| Observable contract | No observable contract is supplied. | supported inference | [approach.md](../../../../old/docs/approach.md) — no behaviour has been described and there is nothing concrete to design tests against; [FR-004](spec.md#functional-requirements) | blocked |
| Evidence source | No evidence source for an observable contract is supplied. | supported inference | [overview.md](../../../../old/docs/overview.md) — the interpretive pass has not run; [FR-004](spec.md#functional-requirements) | blocked |
| Acceptance check | The acceptance artifact is explicitly unavailable; its contents and location are not supplied. | proposed scope decision | [Clarification: acceptance checks and supplier](spec.md#clarifications); [FR-007](spec.md#functional-requirements) | blocked |
| Evaluation type | Evaluation is documentary specification and evidence review and excludes legacy execution and legacy-to-target parity evaluation. | proposed scope decision | [Clarification: meaning of `test`](spec.md#clarifications); [FR-008](spec.md#functional-requirements) | supported |
| Blocked status | An outcome assertion cannot be recorded because the observable contract, input, expected outcome, evidence source, and acceptance check are unsupplied; no test result or legacy-to-target parity conclusion is recorded. | supported inference | [FR-004](spec.md#functional-requirements); the blocked fields above | blocked |
