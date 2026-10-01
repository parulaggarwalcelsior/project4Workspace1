# Evidence Register

## Evidence Register Entries

| Claim | Classification | Source or decision reference | Provenance | Review status |
|---|---|---|---|---|
| Persistence reading status is `UNAVAILABLE`: no table or field was recorded because the instrument had no view of persistence; this is a limit of the reading, not a finding that the estate stores nothing. | documented reading limit | [data_model.md](../../../../old/docs/data_model.md) — `UNAVAILABLE` | Legacy reading | supported |
| Endpoint reading status is `UNAVAILABLE`: no endpoint was recorded; the reading does not determine whether the estate exposes none or whether its routing was unrecognised. | documented reading limit | [api_surface.md](../../../../old/docs/api_surface.md) — `UNAVAILABLE` | Legacy reading | supported |
| Security reading status is `Could not search`: the code graph could not be searched, so no security evidence was looked for. | documented reading limit | [security.md](../../../../old/docs/security.md) — `Could not search` | Legacy reading | supported |
| Edge-case reading status is `Could not search`: the code graph could not be searched, so no edge-case evidence was looked for. | documented reading limit | [edge_cases.md](../../../../old/docs/edge_cases.md) — `Could not search` | Legacy reading | supported |
| Workflow reading status is `Could not search`: the code graph could not be searched, so no workflow evidence was looked for. | documented reading limit | [workflows.md](../../../../old/docs/workflows.md) — `Could not search` | Legacy reading | supported |
| The selected test target is the evidence-definition candidate only; no legacy behaviour, asset, or inventory-wide test target is selected. | proposed scope decision | [Scope Intake — Test target](scope-intake.md); [Evidence Review — selected test target](evidence-review.md#user-story-1-boundary-review); [Clarification: immediate target](spec.md#clarifications); [FR-006](spec.md#functional-requirements) | Proposed scope decision | supported |
| The scope-owner role is the work-unit operator; no named individual is supplied. | proposed scope decision | [Scope Intake — Scope-owner role](scope-intake.md); [Evidence Review — scope-owner role](evidence-review.md#user-story-1-boundary-review); [Clarification: acceptance checks and supplier](spec.md#clarifications); [FR-001](spec.md#functional-requirements) | Proposed scope decision | supported |
| The acceptance artifact is explicitly unavailable; the permitted material does not supply its contents, location, or a named supplier, and this does not define an acceptance check. | proposed scope decision | [Scope Intake — Acceptance artifact](scope-intake.md); [Evidence Review — acceptance artifact](evidence-review.md#user-story-1-boundary-review); [Clarification: acceptance checks and supplier](spec.md#clarifications); [FR-007](spec.md#functional-requirements) | Proposed scope decision | supported |
| The evaluation type is documentary specification and evidence review; legacy execution and legacy-to-target parity evaluation are excluded. | proposed scope decision | [Scope Intake — Evaluation type](scope-intake.md); [Evidence Review — evaluation type](evidence-review.md#user-story-1-boundary-review); [Clarification: meaning of `test`](spec.md#clarifications); [FR-008](spec.md#functional-requirements) | Proposed scope decision | supported |
| Outcome assertions are blocked for this candidate. | proposed scope decision | [Scope Intake — Blocked status](scope-intake.md); [FR-004](spec.md#functional-requirements) | Proposed scope decision | supported |
| Selecting the evidence-definition candidate does not assert that the estate lacks a legacy behaviour, asset, or inventory. | supported inference | [Scope Intake — Test target](scope-intake.md); [Evidence Review — selected test target](evidence-review.md#user-story-1-boundary-review) | Inference from proposed scope decision | supported |
| Assigning the work-unit-operator role does not infer that the estate has no named acceptance-artifact supplier. | supported inference | [Scope Intake — Scope-owner role](scope-intake.md); [Evidence Review — scope-owner role](evidence-review.md#user-story-1-boundary-review) | Inference from proposed scope decision | supported |
| Recording the acceptance artifact as explicitly unavailable does not assert that no acceptance basis exists. | supported inference | [Scope Intake — Acceptance artifact](scope-intake.md); [Evidence Review — acceptance artifact](evidence-review.md#user-story-1-boundary-review); [approach.md](../../../../old/docs/approach.md) — `Acceptance basis frozen: yes` | Inference from a proposed scope decision and legacy reading | supported |
| Excluding legacy execution and parity evaluation from this candidate does not infer that either is impossible for the estate. | supported inference | [Scope Intake — Evaluation type](scope-intake.md); [Evidence Review — evaluation type](evidence-review.md#user-story-1-boundary-review) | Inference from proposed scope decision | supported |

## Allowed Classification Values

- `verified legacy evidence`
- `documented reading limit`
- `supported inference`
- `proposed scope decision`

## Allowed Review Status Values

- `supported`
- `unresolved`
- `blocked`
- `rejected`
