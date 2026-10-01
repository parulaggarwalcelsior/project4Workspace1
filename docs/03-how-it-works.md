# How It Works

After reading this page, an engineer will be able to follow the documentary review flows using the actual record names and see the exact outputs they produce. There are no application functions to invoke: the main flows are Markdown-record review and the Python referee test.

## Data structures

The repository defines documentation schemas rather than runtime types. `Scope Intake Record` contains the owner, target, acceptance artifact, source, gate, evaluation type, provenance, and blocked status; `Evidence Register Entry` contains a claim, one classification, source/decision reference, provenance, and review status ([data model: Scope Intake Record and Evidence Register Entry](../specs/002-test-evidence-definition/data-model.md#scope-intake-record)).

Allowed claim classifications are `verified legacy evidence`, `documented reading limit`, `supported inference`, and `proposed scope decision`; allowed review states are `supported`, `unresolved`, `blocked`, and `rejected` ([evidence register: Allowed Classification Values and Allowed Review Status Values](../specs/002-test-evidence-definition/evidence-register.md#allowed-classification-values)).

## Flow 1: define the boundary

1. `specs/002-test-evidence-definition/spec.md`, **Clarifications**, fixes the candidate to evidence definition, an unavailable artifact, and documentary review.
2. `scope-intake.md`, **Scope Intake Record**, records those decisions with their provenance and blocks outcome assertions.
3. `evidence-register.md`, **Evidence Register Entries**, labels each boundary claim `proposed scope decision`.
4. `evidence-review.md`, **User Story 1 Boundary Review**, records the documentary review result.

Worked example:

```text
Input:  Test target = evidence-definition candidate only
Output: Classification = proposed scope decision; Review status = supported
```

Those exact values appear in the scope intake and evidence register ([scope intake: Test target](../specs/002-test-evidence-definition/scope-intake.md); [evidence register: selected test target entry](../specs/002-test-evidence-definition/evidence-register.md#evidence-register-entries)). The flow does not select a legacy behaviour, asset, or inventory-wide target ([scope intake: Fixed Decision Traceability](../specs/002-test-evidence-definition/scope-intake.md#fixed-decision-traceability)).

## Flow 2: preserve a reading limit

1. `evidence-register.md`, **Evidence Register Entries**, copies a reading status and cites its legacy source.
2. `claim-review-checklist.md`, **Reading-limit check**, requires the claim to remain a reading limit and rejects unsupported negative findings.
3. `evidence-review.md`, **User Story 2 Reading-Limit Review**, confirms that the status remains a limit.

Worked example:

```text
Input:  Persistence reading status = UNAVAILABLE
Output: Classification = documented reading limit; Review status = supported
```

The output is not “the estate has no persistence.” The legacy document says the instrument had no view of persistence, and the register retains that distinction ([legacy data model: What was read](../../old/docs/data_model.md#what-was-read); [evidence register: persistence entry](../specs/002-test-evidence-definition/evidence-register.md#evidence-register-entries)). Endpoint, security, edge-case, and workflow entries use the same pattern ([evidence review: User Story 2](../specs/002-test-evidence-definition/evidence-review.md#user-story-2-reading-limit-review)).

## Flow 3: consider a future test slice

1. `next-test-slice.md`, **Next-Test-Slice Record**, lists the bounded subject plus input, expected outcome, observable contract, evidence source, acceptance check, evaluation type, and blocked status.
2. Unsupplied fields are marked `blocked` and classified separately from their review state.
3. `evidence-review.md`, **User Story 3 Next-Slice Field Review**, confirms no execution or parity conclusion is available.

Worked example:

```text
Input:  Expected outcome = no expected legacy outcome is supplied
Output: Classification = supported inference; Review status = blocked
```

The exact row and status are in `next-test-slice.md`; the reason is that no observable contract or acceptance check supports an outcome ([next-test-slice: Expected outcome](../specs/002-test-evidence-definition/next-test-slice.md); [evidence review: User Story 3](../specs/002-test-evidence-definition/evidence-review.md#user-story-3-next-slice-field-review)).

## Flow 4: run the automated documentary check

1. Run `python3 -m unittest discover -s .referee/002-test-evidence-definition -v`.
2. `test_evidence_definition.py`, `record()`, reads each required candidate record.
3. `EvidenceDefinitionAcceptanceTests` validates boundary decisions, classifications, preserved reading limits, checklist controls, blocked future fields, and the cross-record audit.
4. Python reports the unittest outcome; it is only a check of these documents.

Worked example:

```text
Input:  candidate record name "scope-intake.md"
Output: normalized Markdown text, or AssertionError("Required candidate record is missing: ...")
```

`record()` provides that exact failure path; the test class then checks contents ([referee test: `record()` and `EvidenceDefinitionAcceptanceTests`](../.referee/002-test-evidence-definition/test_evidence_definition.py)).

## Errors and edge cases

A missing required candidate record raises `AssertionError` in `record()`. An uncited claim, an unsupported negative claim from an unavailable reading, or an outcome/parity assertion without contract evidence must be rejected or blocked by the checklist; this is a documentation control, not runtime error handling ([referee test: `record()`](../.referee/002-test-evidence-definition/test_evidence_definition.py); [claim review checklist](../specs/002-test-evidence-definition/claim-review-checklist.md#claim-review-checks)). Legacy edge cases themselves are unknown because the legacy search could not run ([legacy edge cases](../../old/docs/edge_cases.md)).

## Gaps against the specification

No named Go or Java function, executable flow, or legacy input/output pair is built. The specification forbids claiming these until an observable contract, acceptance check, and evaluation basis are supplied ([spec.md: FR-004](../specs/002-test-evidence-definition/spec.md#functional-requirements)).
