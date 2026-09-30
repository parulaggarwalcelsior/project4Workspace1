# Research: Test Evidence Definition

## Decision 1: Immediate boundary

- **Decision**: Define only the evidence-definition documentation candidate; do not select a legacy behaviour, asset, or the 115-item inventory as a test target.
- **Rationale**: [overview.md](../../../old/docs/overview.md) states that the interpretive pass has not run, and [approach.md](../../../old/docs/approach.md) says there is `nothing concrete to design tests against or to validate a migration`.
- **Alternatives considered**: A behaviour-level or inventory-wide target would assert a scope for which the permitted material supplies no behavioural model or observable contract.

## Decision 2: Acceptance artifact treatment

- **Decision**: Record the frozen acceptance artifact as explicitly unavailable; record the work-unit operator as the scope-owner role, without inventing a named supplier or acceptance check.
- **Rationale**: [approach.md](../../../old/docs/approach.md) records that the acceptance basis is frozen and identifies concrete acceptance criteria as information still needed. No artifact contents or location are present in the permitted material.
- **Alternatives considered**: Treating the frozen basis as an available test oracle would incorrectly convert its recorded absence into evidence.

## Decision 3: Evaluation type

- **Decision**: Limit this candidate to documentary specification and evidence review.
- **Rationale**: [overview.md](../../../old/docs/overview.md) reports `0 of 115` execution-grounded items, and [approach.md](../../../old/docs/approach.md) says `no behaviour has been described`.
- **Alternatives considered**: Legacy execution and Java-to-Go parity evaluation require an observable contract, acceptance check, and evaluation basis that are not supplied.

## Decision 4: Documentation technology

- **Decision**: Use Markdown records in this feature directory and manual documentary review.
- **Rationale**: The selected target is an evidence-definition candidate, not a runnable component; its required records and review are specified in [spec.md](spec.md).
- **Alternatives considered**: A runtime, test framework, Java harness, Go harness, database, or CI integration would broaden the evidence-only scope.
