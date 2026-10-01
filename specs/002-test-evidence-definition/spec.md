# Feature Specification: Test Evidence Definition

**Feature Branch**: `not created (no before_specify hook is registered)`

**Created**: 2026-09-30

**Status**: Blocked — the scope owner stated that no acceptance boundaries are specified; no acceptance planning or validation is authorized

**Input**: User description: "Build the candidate for run run-c2e45037447e4cff. Declared source language: java; intended target: go; declared goal: test."

## Evidence Basis and Scope Boundary

This specification defines a proposed evidence-definition gate for the declared goal `test`; it does not describe a verified behaviour of the legacy estate. The permitted legacy reading records `115` inventory items, `0.0%` coverage, and `0 of 115` execution-grounded items. It says, verbatim, `The interpretive pass has not run for this engagement, so there is no narrative to render. This is a missing reading, NOT an estate with nothing in it.` ([overview.md](../../../old/docs/overview.md)).

Known limits retained by this specification:

- Persistence is `UNAVAILABLE`; this does not establish that the estate stores no data ([data_model.md](../../../old/docs/data_model.md)).
- No endpoint was recorded; this does not establish that the estate exposes no endpoint ([api_surface.md](../../../old/docs/api_surface.md)).
- Searches for security, edge-case, and workflow evidence could not run; each reading attributes the limit to `UnsafeEngagementIdError: engagement id is empty or a relative path segment; it must name one directory` ([security.md](../../../old/docs/security.md), [edge_cases.md](../../../old/docs/edge_cases.md), [workflows.md](../../../old/docs/workflows.md)).
- The frozen acceptance basis is recorded as present but its contents are not supplied ([approach.md](../../../old/docs/approach.md)).

The legacy summary names `Book`, `Borrower`, and `Librarian`, but the documented interpretive reading did not verify their behaviour. This specification therefore makes no claim about their contracts, rules, workflows, persistence, routes, access control, or test outcomes.

## Clarifications

- Q: Is the immediate target evidence-definition only, a specified behaviour or asset, or the full 115-item inventory? → A: The immediate target is the evidence-definition candidate only; no specified legacy behaviour, asset, or inventory-wide test target is selected. This is the bounded slice supported by the missing behavioural reading and the documented need to surface and agree what is to be tested before testing or migration validation. (chosen by the fix run)
- Q: What artifact(s) define the acceptance checks and who can supply them? → A: The frozen acceptance basis is recorded as present, but no acceptance artifact, contents, location, or named supplier is included in the permitted material. The candidate records the acceptance artifact as explicitly unavailable and the work-unit operator as the scope-owner role; it does not define acceptance checks. (chosen by the fix run)
- Q: Is `test` limited to specification/evidence review, legacy execution, legacy-to-target parity, or another stated evaluation? → A: `test` is limited to documentary specification and evidence review for this candidate. Legacy execution and legacy-to-target parity are excluded because the reading supplies no observable contract, acceptance check, or execution/evaluation basis. (chosen by the fix run)

## Acceptance-Criteria Gate

**Scope-owner response (2026-10-01)**: `Acceptance boundaries: (none stated)`.

No relevant acceptance criteria were supplied or identified. This is scope-owner input, not legacy evidence and not an acceptance criterion. It accords with the permitted reading's statement that the frozen acceptance basis is present but its contents are not supplied ([approach.md](../../../old/docs/approach.md)).

**Gate status: BLOCKED.** Until the scope owner supplies relevant acceptance criteria, a plan may document this blocked state only; it MUST NOT advance acceptance planning or state that the candidate meets acceptance criteria. Likewise, validation MAY review whether this gate and the documented reading limits are recorded, but MUST NOT report an acceptance-validation result. This gate supersedes any earlier wording that could treat documentary-review completion as acceptance validation, in accordance with Constitution §III.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Define the Test Boundary (Priority: P1)

As the work-unit operator, I need the selected evidence-only boundary and acceptance-artifact status recorded so that this candidate has a bounded, reviewable target instead of implying behaviour from the declared migration direction.

**Why this priority**: The available reading reports no verified business rules and no execution-grounded behaviour, so no observable behaviour can yet be selected for testing.

**Independent Test**: Review the candidate record and determine its target, scope-owner role, acceptance-artifact status, evaluation type, and provenance without treating any as discovered legacy behaviour.

**Acceptance Scenarios**:

1. **Given** the current legacy reading, **When** the candidate is reviewed, **Then** it records the evidence-definition-only target, the explicitly unavailable acceptance artifact, and their provenance without representing either as discovered legacy behaviour.
2. **Given** a requested test subject with no supporting evidence, **When** the candidate is reviewed, **Then** it identifies the missing evidence and does not state an expected legacy outcome.

---

### User Story 2 - Preserve Reading Limits (Priority: P2)

As a reviewer, I need the candidate to distinguish verified evidence, unavailable readings, and proposed decisions so that unsearched or unobserved parts of the estate are not treated as absent.

**Why this priority**: The source documentation expressly distinguishes unavailable readings from negative findings.

**Independent Test**: Review each claim about the estate against the cited documentation and confirm that unavailable areas remain labelled as unavailable.

**Acceptance Scenarios**:

1. **Given** the unavailable persistence reading, **When** the candidate identifies data dependencies, **Then** it records them as unknown rather than asserting that no data exists.
2. **Given** the unsearched security, edge-case, and workflow readings, **When** the candidate identifies test risks, **Then** it names the search limitation and does not assert the absence of the corresponding behaviour.

---

### User Story 3 - Author a Testable Next Slice (Priority: P3)

As the work-unit operator, I need the documentary evaluation decision and absent observable contract recorded so that a later specification can define test cases and measurable completion criteria only when evidence is supplied.

**Why this priority**: The available approach records that there is nothing concrete to design tests against until discovery produces a runnable inventory and behavioural model.

**Independent Test**: Review a proposed later slice to confirm that it remains blocked until it cites observable-contract evidence; this candidate records no expected outcome.

**Acceptance Scenarios**:

1. **Given** an identified observable contract and acceptance check, **When** a later test slice is specified, **Then** it can name its inputs, expected outcome, evidence source, and acceptance check.
2. **Given** no identified observable contract, **When** a later test slice is proposed, **Then** it remains blocked from claiming a test result or migration-parity result.

### Edge Cases

- A scope owner supplies a broad estate-wide target without identifying a behaviour, entry point, or acceptance artifact: retain the target as proposed scope and block outcome assertions.
- An acceptance artifact conflicts with an unavailable or unsearched reading: record the conflict and its provenance; do not resolve it as a legacy fact without additional evidence.
- A request asks for a legacy-to-target parity result before a legacy baseline or observable contract is supplied: report that parity cannot be evaluated from the current reading.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The candidate MUST record the selected evidence-definition-only test target, work-unit-operator scope-owner role, explicitly unavailable acceptance artifact, and evidence provenance verbatim enough to distinguish them from legacy findings. **Traceability**: Proposed decision required by Constitution §III; supporting limit: `0 of 115` execution-grounded items ([overview.md](../../../old/docs/overview.md)).
- **FR-002**: The candidate MUST classify every estate-related statement as verified legacy evidence, documented reading limit, supported inference, or proposed scope decision. **Traceability**: Constitution §I and §II; supporting reading: `This is a missing reading, NOT an estate with nothing in it.` ([overview.md](../../../old/docs/overview.md)).
- **FR-003**: The candidate MUST preserve unavailable persistence, endpoint, security, edge-case, and workflow information as limits of the reading and MUST NOT convert them into negative findings. **Traceability**: `UNAVAILABLE` and `Could not search` statements in [data_model.md](../../../old/docs/data_model.md), [api_surface.md](../../../old/docs/api_surface.md), [security.md](../../../old/docs/security.md), [edge_cases.md](../../../old/docs/edge_cases.md), and [workflows.md](../../../old/docs/workflows.md).
- **FR-004**: The candidate MUST NOT claim a test execution result, expected legacy output, or legacy-to-target parity result until a scope owner supplies the relevant observable contract, acceptance check, and execution or other evaluation basis. **Traceability**: `no behaviour has been described` and `there is nothing concrete to design tests against or to validate a migration` ([approach.md](../../../old/docs/approach.md)); Constitution §IV and §V.
- **FR-005**: Before planning begins, the candidate MUST record the disposition of each decision material to its evidence-only testing scope, acceptance-artifact status, and evaluation type; for this candidate, the three decisions are fixed in Clarifications. **Traceability**: Constitution §III; [approach.md](../../../old/docs/approach.md) lists the acceptance basis, runnable entry points, priority behaviours, environments, and required parity level as open questions.
- **FR-006**: The candidate MUST use evidence-definition documentation only as its immediate test boundary and MUST NOT select a legacy behaviour, asset, or inventory-wide test target. **Traceability**: The interpretive pass `has not run` and the approach says there is `nothing concrete to design tests against or to validate a migration` ([overview.md](../../../old/docs/overview.md), [approach.md](../../../old/docs/approach.md)); proposed scope decision recorded in Clarifications.
- **FR-007**: The candidate MUST record the frozen acceptance artifact as explicitly unavailable: the permitted material does not supply its contents, location, or a named supplier. It MUST NOT define an acceptance check from that absence. **Traceability**: The frozen acceptance basis is recorded as present but its contents are not supplied ([approach.md](../../../old/docs/approach.md)); proposed scope decision recorded in Clarifications.
- **FR-008**: The candidate MUST limit evaluation to documentary specification and evidence review and MUST exclude legacy execution and legacy-to-target parity evaluation. **Traceability**: `0 of 115` inventory items are execution-grounded and `no behaviour has been described` ([overview.md](../../../old/docs/overview.md), [approach.md](../../../old/docs/approach.md)); proposed scope decision recorded in Clarifications.
- **FR-009**: The candidate MUST preserve the scope-owner response `Acceptance boundaries: (none stated)` as an acceptance-criteria gate. Until relevant acceptance criteria are supplied, it MUST block acceptance planning and acceptance-validation claims; documentary review may verify the blocked state only. **Traceability**: Scope-owner response dated 2026-10-01; Constitution §III; the frozen acceptance basis is recorded as present but its contents are not supplied ([approach.md](../../../old/docs/approach.md)).

### Key Entities

- **Legacy evidence item**: A statement or inventory fact from the permitted legacy documentation, carrying a source citation and its documented evidence class or limitation.
- **Reading limit**: An unavailable or unsearched area of the legacy reading that cannot support a negative claim about estate behaviour.
- **Test target**: The selected evidence-definition-only documentation candidate; it is a proposed scope decision, not a legacy behaviour, asset, or inventory slice.
- **Acceptance artifact**: The source that would define an expected outcome or completion check; this candidate records it as explicitly unavailable because the documentation says the basis is frozen but does not include its contents.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of estate-related claims in the next test-slice specification cite a permitted legacy document or are explicitly labelled as a proposed decision.
- **SC-002**: 100% of references to persistence, endpoints, security, edge cases, and workflows preserve the documented unavailable or unsearched status unless new permitted evidence is supplied.
- **SC-003**: Before planning begins, the candidate records one bounded test target, an explicit statement that the acceptance artifact is unavailable, and one selected evaluation type.
- **SC-004**: A reviewer can determine, for every claimed expected outcome in the next test slice, whether it is evidence-supported, proposed, or blocked, with no unlabelled category.
- **SC-005**: While the scope-owner response remains `Acceptance boundaries: (none stated)`, no plan or evidence review records an acceptance-planning or acceptance-validation result; each records the acceptance-criteria gate as `BLOCKED`.

## Assumptions

- `test` is treated as an operator-declared goal and proposed scope direction, not as evidence of a legacy capability or required behaviour.
- The legacy documentation under `../../old/docs/` and artifacts created in this working tree are the only permitted evidence sources for this run.
- The declared migration direction supplies vocabulary and context only; it does not establish a test target, observable contract, or acceptance outcome.
- No additional acceptance artifact, runnable entry point, execution trace, or behavioural model has been supplied in the current request.
- The scope-owner role for this candidate is the work-unit operator; no named individual is supplied in the permitted material.
- The decisions in FR-006 through FR-008 are fixed for this candidate. A later candidate may only change them with newly supplied permitted evidence and a recorded proposed scope decision.
