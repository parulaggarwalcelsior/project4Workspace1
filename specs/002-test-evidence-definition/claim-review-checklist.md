# Claim Review Checklist

## Claim Review Checks

- [ ] **Claim identifier**: References an intake or register entry.
- [ ] **Citation/decision label**: Required for every estate-related claim.
- [ ] **Reading-limit check**: Rejects a negative estate finding based only on an unavailable or unsearched reading.
- [ ] **Outcome-assertion check**: Blocks an expected legacy outcome or parity assertion without supplied observable-contract evidence and acceptance checks.
- [ ] **Citation or proposed-decision check**: For every estate-related claim, verify a citation to a permitted legacy reading or an explicit `proposed scope decision` label. Reject the claim when neither is present.
- [ ] **Reading-limit check**: When a claim relies on an `UNAVAILABLE` or `Could not search` reading, verify that it describes the limit of the reading. Reject any unsupported negative finding that the estate lacks the relevant behaviour, data, endpoint, control, edge case, or workflow.
- [ ] **Outcome-assertion check**: Before recording an expected legacy outcome, test result, or legacy-to-target parity assertion, verify supplied observable-contract evidence, an acceptance check, and an execution or other evaluation basis. Block the assertion when any of those inputs is absent.
- [ ] **Acceptance-criteria gate check**: Before recording any acceptance-planning or acceptance-validation claim, verify that relevant acceptance criteria are supplied by the scope owner, their permitted source is recorded, and the specification, plan, tasks, and documentary records have been reconciled. When the recorded response is `Acceptance boundaries: (none stated)`, record only `BLOCKED`.
- [ ] **Result**: `pass`, `unresolved`, `blocked`, or `rejected`; never an execution result.
