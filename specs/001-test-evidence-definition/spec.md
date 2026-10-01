# Feature Specification: Test Evidence Definition

**Feature Branch**: `not created (no before_specify hook is registered)`

**Created**: 2026-09-30

**Status**: Draft — blocked pending scope-owner decisions

**Input**: User description: "Build the candidate for run run-5e6c783b97234ef4 … stated goal, verbatim: \"test\"."

## Evidence Basis and Scope Boundary

This specification describes a proposed evidence-definition gate for the declared goal `test`; it does not describe a verified behaviour of the legacy estate. The allowed legacy reading records `115` inventory items, `0.0%` coverage, and `0 of 115` execution-grounded items. The reading says, verbatim, `The interpretive pass has not run for this engagement, so there is no narrative to render. This is a missing reading, NOT an estate with nothing in it.` ([overview.md](../../../old/docs/overview.md)).

Known limits retained by this specification:

- Persistence is `UNAVAILABLE`; this does not establish that the estate stores no data ([data_model.md](../../../old/docs/data_model.md)).
- No endpoint was recorded; this does not establish that the estate exposes no endpoint ([api_surface.md](../../../old/docs/api_surface.md)).
- Searches for security, edge-case, and workflow evidence could not run; each reading attributes the limit to `UnsafeEngagementIdError: engagement id is empty or a relative path segment; it must name one directory` ([security.md](../../../old/docs/security.md), [edge_cases.md](../../../old/docs/edge_cases.md), [workflows.md](../../../old/docs/workflows.md)).
- The frozen acceptance basis is recorded as present but its contents are not supplied ([approach.md](../../../old/docs/approach.md)).

The summaries mention names such as `Book`, `Borrower`, and `Librarian`, but the documented interpretive reading did not verify their behaviour. This specification therefore makes no claim about their contracts, rules, workflows, persistence, routes, access control, or test outcomes.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Define the Test Boundary (Priority: P1)

As the scope owner, I need to provide the concrete subject and acceptance basis for `test` so that a test candidate has a bounded, reviewable target instead of implying behaviour from the declared migration direction.

**Why this priority**: The available reading reports no verified business rules and no execution-grounded behaviour, so no observable behaviour can yet be selected for testing.

**Independent Test**: Provide a test subject, the form and contents of the acceptance basis, and an identified owner; confirm that the candidate records each item as supplied evidence or an explicit proposed decision.

**Acceptance Scenarios**:

1. **Given** the current legacy reading, **When** the scope owner supplies a concrete test subject and acceptance artifacts, **Then** the candidate records their provenance and does not represent them as discovered legacy behaviour.
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

As the scope owner, I need to choose the kind of testing and the observable contract to evaluate so that a later specification can define test cases and measurable completion criteria without relying on migration intent alone.

**Why this priority**: The current goal is only `test`; the available approach records that there is nothing concrete to design tests against until discovery produces a runnable inventory and behavioural model.

**Independent Test**: After the scope owner selects the testing intent and supplies contract evidence, review a proposed slice to confirm that every expected outcome cites that evidence or is labelled as a proposed decision.

**Acceptance Scenarios**:

1. **Given** an identified observable contract and acceptance check, **When** a later test slice is specified, **Then** it can name its inputs, expected outcome, evidence source, and acceptance check.
2. **Given** no identified observable contract, **When** a later test slice is proposed, **Then** it remains blocked from claiming a test result or migration-parity result.

### Edge Cases

- A scope owner supplies a broad estate-wide target without identifying a behaviour, entry point, or acceptance artifact: retain the target as proposed scope and block outcome assertions.
- An acceptance artifact conflicts with an unavailable or unsearched reading: record the conflict and its provenance; do not resolve it as a legacy fact without additional evidence.
- A request asks for a legacy-to-target parity result before a legacy baseline or observable contract is supplied: report that parity cannot be evaluated from the current reading.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The candidate MUST record the scope owner's supplied test target, acceptance artifacts, and evidence provenance verbatim enough to distinguish them from legacy findings. **Traceability**: Proposed decision required by Constitution §III; supporting limit: `0 of 115` execution-grounded items ([overview.md](../../../old/docs/overview.md)).
- **FR-002**: The candidate MUST classify every estate-related statement as verified legacy evidence, documented reading limit, supported inference, or proposed scope decision. **Traceability**: Constitution §I and §II; supporting reading: `This is a missing reading, NOT an estate with nothing in it.` ([overview.md](../../../old/docs/overview.md)).
- **FR-003**: The candidate MUST preserve unavailable persistence, endpoint, security, edge-case, and workflow information as limits of the reading and MUST NOT convert them into negative findings. **Traceability**: `UNAVAILABLE` and `Could not search` statements in [data_model.md](../../../old/docs/data_model.md), [api_surface.md](../../../old/docs/api_surface.md), [security.md](../../../old/docs/security.md), [edge_cases.md](../../../old/docs/edge_cases.md), and [workflows.md](../../../old/docs/workflows.md).
- **FR-004**: The candidate MUST NOT claim a test execution result, expected legacy output, or legacy-to-target parity result until a scope owner supplies the relevant observable contract, acceptance check, and execution or other evaluation basis. **Traceability**: `no behaviour has been described` and `there is nothing concrete to design tests against or to validate a migration` ([approach.md](../../../old/docs/approach.md)); Constitution §IV and §V.
- **FR-005**: The candidate MUST identify each unresolved decision that materially affects the testing scope, acceptance basis, or evaluation type before planning begins. **Traceability**: Constitution §III; [approach.md](../../../old/docs/approach.md) lists the acceptance basis, runnable entry points, priority behaviours, environments, and required parity level as open questions.
- **FR-006**: The scope owner MUST select the test boundary: [NEEDS CLARIFICATION: Is the immediate target evidence-definition only, a specified behaviour or asset, or the full 115-item inventory?]
- **FR-007**: The scope owner MUST provide or identify the frozen acceptance basis: [NEEDS CLARIFICATION: What artifact(s) define the acceptance checks and who can supply them?]
- **FR-008**: The scope owner MUST select the intended evaluation type: [NEEDS CLARIFICATION: Is `test` limited to specification/evidence review, legacy execution, legacy-to-target parity, or another stated evaluation?]

### Key Entities

- **Legacy evidence item**: A statement or inventory fact from the permitted legacy documentation, carrying a source citation and its documented evidence class or limitation.
- **Reading limit**: An unavailable or unsearched area of the legacy reading that cannot support a negative claim about estate behaviour.
- **Test target**: The owner-supplied behaviour, asset, or bounded inventory slice to be evaluated; it is a proposed scope decision until supported by evidence.
- **Acceptance artifact**: The owner-supplied source that defines an expected outcome or completion check; the current documentation says the acceptance basis is frozen but does not include its contents.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of estate-related claims in the next test-slice specification cite a permitted legacy document or are explicitly labelled as a proposed decision.
- **SC-002**: 100% of references to persistence, endpoints, security, edge cases, and workflows preserve the documented unavailable or unsearched status unless new permitted evidence is supplied.
- **SC-003**: Before planning begins, the scope owner has supplied one bounded test target, one identified acceptance artifact or explicit statement that it is unavailable, and one selected evaluation type.
- **SC-004**: A reviewer can determine, for every claimed expected outcome in the next test slice, whether it is evidence-supported, proposed, or blocked, with no unlabelled category.

## Assumptions

- `test` is treated as an operator-declared goal and proposed scope direction, not as evidence of a legacy capability or required behaviour.
- The legacy documentation under `../../old/docs/` and artifacts created in this working tree are the only permitted evidence sources for this run.
- The declared migration direction supplies vocabulary and context only; it does not establish a test target, observable contract, or acceptance outcome.
- No additional acceptance artifact, runnable entry point, execution trace, or behavioural model has been supplied in the current request.
- Planning and implementation remain out of scope until the three scope-owner decisions in FR-006 through FR-008 are resolved.
