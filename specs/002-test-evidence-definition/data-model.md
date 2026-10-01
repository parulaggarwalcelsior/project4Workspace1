# Candidate Record Model: Test Evidence Definition

These are documentation-record schemas, not data structures claimed to exist in the legacy estate.

## Scope Intake Record

| Field | Required value for this candidate | Validation |
|---|---|---|
| Scope-owner role | `work-unit operator` | Do not invent a named individual. |
| Test target | `evidence-definition candidate only` | Must not name a legacy behaviour, asset, or full-inventory test target. |
| Acceptance artifact | `explicitly unavailable` | Must state that contents and location are not supplied. |
| Evaluation type | `documentary specification and evidence review` | Must exclude legacy execution and parity evaluation. |
| Supplied-on date | `2026-09-30` | Records this fix-run decision. |
| Provenance | Proposed scope decision; citations to [spec.md](spec.md) and its permitted legacy sources | Must not label a decision as legacy evidence. |
| Blocked status | Outcome assertions blocked | Must not report a test result. |

## Evidence Register Entry

| Field | Validation |
|---|---|
| Claim | State the claim verbatim enough for review. |
| Classification | One of `verified legacy evidence`, `documented reading limit`, `supported inference`, or `proposed scope decision`. |
| Source or decision reference | Cite a permitted legacy reading or the recorded scope decision. |
| Provenance | Retain whether it is a legacy reading or a proposed decision. |
| Review status | Supported, unresolved, blocked, or rejected. |

## Claim Review Record

| Field | Validation |
|---|---|
| Claim identifier | References an intake or register entry. |
| Citation/decision label | Required for every estate-related claim. |
| Reading-limit check | Rejects a negative estate finding based only on an unavailable or unsearched reading. |
| Outcome-assertion check | Blocks an expected legacy outcome or parity assertion without supplied observable-contract evidence and acceptance checks. |
| Result | `pass`, `unresolved`, `blocked`, or `rejected`; never an execution result. |

## Next-Test-Slice Record

| Field | Validation |
|---|---|
| Bounded subject, input, expected outcome, observable contract, evidence source, acceptance check, evaluation type | A future record may fill each only from supplied evidence. |
| Blocked status | Required for every unsupplied contract or acceptance field. |

## Relationships

The scope intake supplies proposed-scope-decision entries to the evidence register. The claim review evaluates both records. A next-test-slice record can reference them, but remains blocked from an outcome assertion because this candidate supplies no observable contract or acceptance check.
