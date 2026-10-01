# Testing and Quality

After reading this page, an engineer will know exactly what the repository tests, what each test file proves, and which quality limits apply. The automated checks validate documentation safeguards only; they do not test the legacy Java estate or a Go migration.

## Test command

```bash
python3 -m unittest discover -s .referee/002-test-evidence-definition -v
```

This is the command documented in the referee test itself ([referee test: module docstring](../.referee/002-test-evidence-definition/test_evidence_definition.py)). No build, application test suite, coverage tool, lint configuration, formatter, or CI workflow is present in this tree ([plan.md: Technical Context](../specs/002-test-evidence-definition/plan.md#technical-context)).

## Current result

At the documentation handoff, this command fails against the checked-in candidate. The failure is limited to the documentary referee and is not evidence about the legacy estate or a Go implementation. The failing checks are the scope-intake provenance test, the edge-case reading-limit subcheck, the evidence-review prohibited-result test, and the Constitution-section subchecks ([referee test: `EvidenceDefinitionAcceptanceTests`](../.referee/002-test-evidence-definition/test_evidence_definition.py)). The candidate records and referee test are outside this documentation-only change; see [Running and operating: Current referee status](04-running-and-operating.md#current-referee-status) for remediation boundaries.

## Test inventory

| Test file | Coverage / proof | Evidence |
|---|---|---|
| `.referee/002-test-evidence-definition/test_evidence_definition.py` | Requires the five candidate records; checks fixed boundary decisions and provenance; requires all four claim classes; protects unavailable/unsearched limits; checks review controls and blocked next-slice fields. | [`EvidenceDefinitionAcceptanceTests`](../.referee/002-test-evidence-definition/test_evidence_definition.py) |

The repository has no source-level unit, integration, end-to-end, performance, or migration-parity test file. That is a tree observation, consistent with the plan's explicit documentary-testing scope ([plan.md: Testing](../specs/002-test-evidence-definition/plan.md#technical-context)).

## What the referee acceptance tests prove

| Test method | What it checks | What it does not prove |
|---|---|---|
| `test_required_documentary_records_exist` | The five expected Markdown candidate records exist. | That their claims describe legacy runtime behaviour. |
| `test_scope_intake_records_all_fixed_boundary_decisions_with_provenance` | Scope owner, target, unavailable artifact, evaluation type, blocking, and FR traceability exist. | A legacy contract or acceptance outcome. |
| `test_evidence_register_has_all_four_claim_classes_and_boundary_entries` | The classification vocabulary and fixed boundary entries exist. | Classification correctness beyond the document text checked. |
| `test_unavailable_and_unsearched_readings_remain_limits_not_negative_findings` | The five reading limits remain limits and prohibited absence phrases are not used. | That the legacy estate lacks or contains those capabilities. |
| `test_checklist_rejects_unsupported_claims_and_outcomes` | Checklist text includes controls for citations, limits, and unsupported outcomes. | Execution of a legacy test. |
| `test_evidence_review_records_documentary_status_without_execution_or_parity_result` | Review carries documentary status and avoids forbidden result claims. | Java-to-Go equivalence. |
| `test_final_review_records_cross_cutting_audit_and_remaining_blockers` | Constitution audit, validation steps, completion criterion, and blockers are documented. | Acceptance validation. |
| `test_next_test_slice_keeps_unsupplied_contract_fields_blocked` | Future input, outcome, contract, evidence, and acceptance fields remain blocked. | Expected legacy outputs. |

All names and checks are from the single referee test class ([referee test: `EvidenceDefinitionAcceptanceTests`](../.referee/002-test-evidence-definition/test_evidence_definition.py)).

The table describes the checks that the test source implements; it does not claim that they currently pass. The current failure is actionable from the assertion names and source conditions in that same test file.

## Quality gates

The documentary quality gates are: cite each estate-related claim or label it a proposed decision; preserve unavailable/unsearched statuses; block unsupported outcome claims; and retain the acceptance-criteria gate. The claim-review checklist is the authoritative local control list ([claim review checklist](../specs/002-test-evidence-definition/claim-review-checklist.md#claim-review-checks)).

The constitution adds evidence-bound description, explicit unknowns, ordered specification workflow, semantic preservation before migration, and traceable acceptance ([constitution: Core Principles I–V](../.specify/memory/constitution.md#core-principles)).

## Local review procedure

1. Run the unittest command above.
2. Follow the six review steps in `quickstart.md`: check the gate, clarifications, requirements, downstream records, reading limits, and future records.
3. Keep the result bounded to documentary review; do not infer an acceptance or execution result.

The process and its completion qualification are stated in [quickstart.md: Review procedure and Completion criterion](../specs/002-test-evidence-definition/quickstart.md#review-procedure).

## Gaps against the specification

The docs candidate records five documentary validation steps as complete, but acceptance planning and acceptance validation remain blocked because no relevant acceptance criteria were supplied ([evidence review: T017 and T028](../specs/002-test-evidence-definition/evidence-review.md#t017-quickstart-documentary-validation)). Therefore no test result for the legacy estate or Go target is present.
