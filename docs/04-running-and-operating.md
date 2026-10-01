# Running and Operating

After reading this page, an engineer will know the only supported local command, what it verifies, how to diagnose a failed review, and why this repository has no runtime deployment procedure. Operations here mean maintaining and reviewing a Markdown candidate.

## Prerequisites

| Requirement | Version | Why |
|---|---|---|
| Python | 3; exact version not pinned | Runs the standard-library `unittest` referee. | [referee test: module docstring and imports](../.referee/002-test-evidence-definition/test_evidence_definition.py) |
| Markdown reader/editor | Not specified | Candidate records are Markdown files. | [plan.md: Language/Version and Storage](../specs/002-test-evidence-definition/plan.md#technical-context) |
| Permitted legacy readings | Not versioned in this tree | Provides the evidence basis for estate claims. | [constitution: Evidence and Scope Constraints](../.specify/memory/constitution.md#evidence-and-scope-constraints) |

No Java runtime, Go toolchain, package manager, database, service account, or network endpoint is declared ([plan.md: Technical Context](../specs/002-test-evidence-definition/plan.md#technical-context)).

## Commands

```bash
# Build
# Not present: there is no build manifest or executable implementation.

# Run
# Not present: the candidate exposes no application, CLI, service, or API.

# Test / documentary quality gate
python3 -m unittest discover -s .referee/002-test-evidence-definition -v

# Lint
# Not present: no lint command or linter configuration is declared.
```

The test command is stated in `.referee/002-test-evidence-definition/test_evidence_definition.py`. The plan designates review as documentary rather than executable testing ([referee test: module docstring](../.referee/002-test-evidence-definition/test_evidence_definition.py); [plan.md: Testing](../specs/002-test-evidence-definition/plan.md#technical-context)).

## Configuration

| Variable or setting | Default | Purpose and effect | Source |
|---|---|---|---|
| Runtime configuration variables | None declared | There is no runtime to configure. | [plan.md: Project Type](../specs/002-test-evidence-definition/plan.md#technical-context) |
| Acceptance-criteria gate | `BLOCKED` | Prohibits acceptance planning and acceptance-validation claims until relevant criteria are supplied. | [scope intake: Acceptance-criteria gate](../specs/002-test-evidence-definition/scope-intake.md) |
| Evaluation type | `documentary specification and evidence review` | Excludes legacy execution and legacy-to-target parity evaluation for this candidate. | [scope intake: Evaluation type](../specs/002-test-evidence-definition/scope-intake.md) |

The latter two rows are candidate-record settings, not environment variables.

## Deployment

No deployment is present in this tree because there is no deployable runtime. `docs/deploy.md` is not present, so there is no Ship-phase runbook to link; the plan says the candidate exposes no external interface ([plan.md: Project Structure](../specs/002-test-evidence-definition/plan.md#project-structure)).

## Logs and diagnostics

There is no application log stream, metric, health endpoint, or tracing configuration in this tree. Use the verbose unittest output and inspect the named Markdown record in a failing assertion; `record()` reports a missing record as `Required candidate record is missing: ...` ([referee test: `record()`](../.referee/002-test-evidence-definition/test_evidence_definition.py)).

### Current referee status

The command was run against the current tree while preparing this documentation and it fails. This is a documentary-check failure, not a Java, Go, deployment, or parity result. The failing assertions are in `EvidenceDefinitionAcceptanceTests`: `test_scope_intake_records_all_fixed_boundary_decisions_with_provenance`, `test_unavailable_and_unsearched_readings_remain_limits_not_negative_findings`, `test_evidence_review_records_documentary_status_without_execution_or_parity_result`, and the Constitution-section subchecks of `test_final_review_records_cross_cutting_audit_and_remaining_blockers` ([referee test: those methods](../.referee/002-test-evidence-definition/test_evidence_definition.py)).

This documentation task does not authorize changing `specs/` or `.referee/`. A maintainer responsible for the candidate should use the assertion output to amend the affected candidate records, then rerun the same command. In particular, the source test requires the literal normalized phrase `supplied on`, a nearby `edge_cases.md` citation for the edge-case limit, and wording that does not match its prohibited expected-output pattern ([referee test: `test_scope_intake_records_all_fixed_boundary_decisions_with_provenance`, `test_unavailable_and_unsearched_readings_remain_limits_not_negative_findings`, and `test_evidence_review_records_documentary_status_without_execution_or_parity_result`](../.referee/002-test-evidence-definition/test_evidence_definition.py)).

## Known failure modes

| Symptom | Likely cause | Operator action | Evidence |
|---|---|---|---|
| `Required candidate record is missing` | One of the five required records is absent. | Restore or create the required candidate record with traceable content; rerun the referee. | [referee test: `test_required_documentary_records_exist`](../.referee/002-test-evidence-definition/test_evidence_definition.py) |
| Current scope-intake check fails on `supplied on` | The candidate currently uses the field spelling `Supplied-on date`, while the test searches normalized text for `supplied on`. | Candidate maintainer: change the candidate record to meet the test, then rerun. This documentation change intentionally does not modify the candidate. | [scope intake: `Supplied-on date`](../specs/002-test-evidence-definition/scope-intake.md); [referee test: scope-intake test](../.referee/002-test-evidence-definition/test_evidence_definition.py) |
| Current edge-case reading-limit check fails | The test's local edge-case context does not contain its required `edge_cases.md` citation. | Candidate maintainer: retain `Could not search`, make the citation local to that entry, then rerun. | [evidence review: User Story 2 Reading-Limit Review](../specs/002-test-evidence-definition/evidence-review.md#user-story-2-reading-limit-review); [referee test: reading-limits test](../.referee/002-test-evidence-definition/test_evidence_definition.py) |
| Current outcome wording check fails | The review includes text that matches the test's prohibited expected-outcome pattern, even though the prose intends to deny an outcome assertion. | Candidate maintainer: reword the candidate review so it remains a blocked documentary statement without matching the prohibited pattern, then rerun. | [evidence review: User Story 1 Boundary Review](../specs/002-test-evidence-definition/evidence-review.md#user-story-1-boundary-review); [referee test: review-status test](../.referee/002-test-evidence-definition/test_evidence_definition.py) |
| Reading-limit check fails | A record turned `UNAVAILABLE` or `Could not search` into an estate absence claim. | Restore the status as a documented reading limit and cite the relevant legacy document. | [claim review checklist: Reading-limit check](../specs/002-test-evidence-definition/claim-review-checklist.md#claim-review-checks) |
| Outcome/parity control fails | An expected outcome, execution result, or parity assertion lacks contract evidence and an acceptance check. | Remove the assertion or retain it as blocked; obtain permitted evidence before redefining it. | [claim review checklist: Outcome-assertion check](../specs/002-test-evidence-definition/claim-review-checklist.md#claim-review-checks) |
| Acceptance claim cannot proceed | Scope-owner response remains `Acceptance boundaries: (none stated)`. | Obtain relevant acceptance criteria from the scope owner and reconcile them across the candidate before making an acceptance claim. | [spec.md: Acceptance-Criteria Gate](../specs/002-test-evidence-definition/spec.md#acceptance-criteria-gate) |

## Gaps against the specification

The candidate can complete documentary review but cannot report acceptance validation, a test result, legacy execution, or Java-to-Go parity. Its remaining blocked inputs are an observable contract, input, expected outcome, evidence source, acceptance check, and evaluation basis ([evidence review: Completion criterion and Remaining blocked inputs](../specs/002-test-evidence-definition/evidence-review.md#t017-quickstart-documentary-validation)).
