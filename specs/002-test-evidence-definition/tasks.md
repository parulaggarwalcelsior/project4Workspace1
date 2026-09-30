---

description: "Task list for the Test Evidence Definition documentation candidate"
---

# Tasks: Test Evidence Definition

**Input**: [spec.md](spec.md), [plan.md](plan.md), [research.md](research.md), [data-model.md](data-model.md), [quickstart.md](quickstart.md), the [project constitution](../../.specify/memory/constitution.md), and the permitted legacy readings in `../../../old/docs/`.

**Boundary**: All tasks create or review Markdown records for the evidence-definition-only candidate. The fixed decisions are: the work-unit operator is the scope-owner role; the test target is the evidence-definition candidate only; the acceptance artifact is explicitly unavailable; and evaluation is documentary specification and evidence review. No task executes the Java estate, creates Go code, defines an expected legacy output, or evaluates Java-to-Go parity.

**Tests**: No automated-test tasks are included. The specification requests documentary review, and the plan explicitly excludes executable legacy and migration testing. The independent checks below are the review procedures from [quickstart.md](quickstart.md).

## Phase 1: Setup (Shared Documentation Infrastructure)

**Purpose**: Create the record locations and review control described by the plan and record model.

- [x] T001 [P] Create the scope-intake record headings and fields from the Scope Intake Record schema in `specs/002-test-evidence-definition/scope-intake.md`
- [x] T002 [P] Create the evidence-register headings and allowed classification fields from the Evidence Register Entry schema in `specs/002-test-evidence-definition/evidence-register.md`If you have this question- "implement: ists/requirements.md:28:- [x] User scenarios cover primary flows specs/002-test-evidence-definition/checklists/requirements.md:29:- [ ] Feature meets measurable outcomes defined in Success Criteria — SC-003 depends on the scope owner specs/002-test-evidence-definition/checklists/requirements.md:30:- [x] No implementation details leak into specification codex | Checklist | Total | Checked | Unchecked | Status | |---|---:|---:|---:|---| | requirements.md | 15 | 12 | 3 | ✗ FAIL | Some checklists have unchecked items. Do you want to proceed with implementation anyway? (yes/no) tokens used 17,530", then Answer is Yes.
- [x] T003 [P] Create the claim-review checklist headings and checks from the Claim Review Record schema in `specs/002-test-evidence-definition/claim-review-checklist.md` if you have this question 'implement: ' \""'$f" | wc -l) printf '"'%s\\t%s\\t%s\\t%s\\n' \""'$(basename "$f")" "$total" "$checked" "$unchecked" done fi' in /synthetix/new/project4Workspace1 succeeded in 40ms: {"FEATURE_DIR":"/synthetix/new/project4Workspace1/specs/002-test-evidence-definition","AVAILABLE_DOCS":["research.md","data-model.md","quickstart.md","tasks.md"]} requirements.md 16 13 3 codex | Checklist | Total | Checked | Unchecked | Status | |---|---:|---:|---:|---| | requirements.md | 16 | 13 | 3 | ✗ FAIL | Some checklists have unchecked items. Do you want to proceed with T003 anyway? (yes/no) tokens used 17,956' then Answer is Yes.

---

## Phase 2: Foundational (Evidence Controls)

**Purpose**: Establish the shared provenance and reading-limit controls that block any unsupported outcome assertion.

**⚠️ CRITICAL**: Complete this phase before reviewing a user-story record. It must preserve missing and unsearched readings as limits, not negative findings.

- [x] T004 [P] Populate the fixed scope-owner role, evidence-definition-only target, explicitly unavailable acceptance artifact, documentary-review evaluation type, supplied-on date, provenance, and blocked-outcome status in `specs/002-test-evidence-definition/scope-intake.md`
- [x] T005 [P] Populate documented-reading-limit entries for persistence, endpoints, security, edge cases, and workflows, each with its permitted legacy citation and `UNAVAILABLE` or `Could not search` status, in `specs/002-test-evidence-definition/evidence-register.md`
- [x] T006 [P] Define citation-or-proposed-decision, reading-limit, and outcome-assertion checks that reject unsupported negative findings and block unsupported expected outcomes in `specs/002-test-evidence-definition/claim-review-checklist.md`implement: total=$(rg -N '"'"'^- '"\\[[ xX]\\]' \""'$f" | wc -l) checked=$(rg -N '"'"'^- '"\\[[xX]\\]' \""'$f" | wc -l) unchecked=$(rg -N '"'"'^- '"\\[ \\]' \""'$f" | wc -l) printf '"'%s\\t%s\\t%s\\t%s\\n' \""'$(basename "$f")" "$total" "$checked" "$unchecked" done fi' in /synthetix/new/project4Workspace1 succeeded in 0ms: requirements.md 16 13 3 codex | Checklist | Total | Checked | Unchecked | Status | |---|---:|---:|---:|---| | requirements.md | 16 | 13 | 3 | ✗ FAIL | Some checklists have unchecked items. Do you want to proceed with implementation anyway? (yes/no) tokens used 16,950, answer is yes for this

**Checkpoint**: Scope decisions and shared controls exist, while all legacy outcomes remain blocked pending an observable contract, acceptance check, and evaluation basis.

---

## Phase 3: User Story 1 - Define the Test Boundary (Priority: P1) 🎯 MVP

**Goal**: Record the selected evidence-only target, scope-owner role, unavailable acceptance artifact, and documentary evaluation type without presenting a proposed decision as legacy behaviour.

**Independent Test**: Review `scope-intake.md`, `evidence-register.md`, and `evidence-review.md` using [quickstart.md](quickstart.md) steps 1–3. A reviewer can identify all four boundary decisions and their provenance, and finds no expected legacy outcome or execution result.

### Implementation for User Story 1

- [x] T007 [US1] Trace each fixed boundary decision in the scope intake to its matching clarification and FR-006 through FR-008 in `specs/002-test-evidence-definition/scope-intake.md`
- [x] T008 [US1] Add proposed-scope-decision register entries for the selected target, scope-owner role, unavailable acceptance artifact, and documentary evaluation type with citations to `spec.md` in `specs/002-test-evidence-definition/evidence-register.md`
- [x] T009 [US1] Record the results of the User Story 1 boundary review as `pass`, `unresolved`, `blocked`, or `rejected`, without reporting an execution result, in `specs/002-test-evidence-definition/evidence-review.md`

**Checkpoint**: The candidate’s bounded target is reviewable and no legacy behaviour, asset, or inventory-wide test target is selected.

---

## Phase 4: User Story 2 - Preserve Reading Limits (Priority: P2)

**Goal**: Ensure that every estate-related candidate claim is traceable and that unavailable or unsearched reading areas remain explicit limits.

**Independent Test**: Review every claim in the candidate records against its cited legacy reading or decision label using [quickstart.md](quickstart.md) step 4. A reviewer confirms that persistence, endpoints, security, edge cases, and workflows are never stated as absent estate behaviour.

### Implementation for User Story 2

- [x] T010 [US2] Classify every estate-related statement in the scope intake and evidence review as verified legacy evidence, documented reading limit, supported inference, or proposed scope decision in `specs/002-test-evidence-definition/evidence-register.md`
- [x] T011 [US2] Add separate review findings for persistence, endpoint discovery, security, edge cases, and workflows that retain the documented unavailable or unsearched status in `specs/002-test-evidence-definition/evidence-review.md`
- [x] T012 [US2] Apply the citation, reading-limit, and outcome-assertion checks to all candidate records and record unsupported, unresolved, blocked, or rejected claims in `specs/002-test-evidence-definition/evidence-review.md`implement: ists/requirements.md:28:- [x] User scenarios cover primary flows specs/002-test-evidence-definition/checklists/requirements.md:29:- [ ] Feature meets measurable outcomes defined in Success Criteria — SC-003 depends on the scope owner specs/002-test-evidence-definition/checklists/requirements.md:30:- [x] No implementation details leak into specification codex | Checklist | Total | Checked | Unchecked | Status | |---|---:|---:|---| | requirements.md | 16 | 13 | 3 | ✗ FAIL | Some checklists have unchecked items. Do you want to proceed with implementation anyway? (yes/no) tokens used 17,268, the answer is yes.

**Checkpoint**: Every estate-related claim is classified and cited or explicitly labelled as a proposed decision; unsupported claims are retained as unresolved or blocked rather than converted into findings.

---

## Phase 5: User Story 3 - Author a Testable Next Slice (Priority: P3)

**Goal**: Provide a future-slice record that only permits inputs, expected outcomes, contracts, evidence, acceptance checks, and evaluation types when supplied evidence supports them.

**Independent Test**: Review `next-test-slice.md` using [quickstart.md](quickstart.md) step 5. A reviewer finds each absent observable-contract or acceptance field marked blocked, with no claimed test or parity result.

### Implementation for User Story 3

- [x] T013 [US3] Create the bounded-subject, input, expected-outcome, observable-contract, evidence-source, acceptance-check, evaluation-type, and blocked-status fields in `specs/002-test-evidence-definition/next-test-slice.md`
- [ ] T014 [US3] Populate the next-test-slice record only with the fixed documentary boundary and mark the observable contract, input, expected outcome, evidence source, and acceptance check as blocked when not supplied in `specs/002-test-evidence-definition/next-test-slice.md`
- [ ] T015 [US3] Review each next-slice field as evidence-supported, proposed, or blocked and record that no execution or parity conclusion is available in `specs/002-test-evidence-definition/evidence-review.md`

**Checkpoint**: The next-slice record remains reviewable without inventing a legacy contract, expected outcome, or acceptance check.

---

## Phase 6: Polish & Cross-Cutting Documentary Review

**Purpose**: Confirm that the completed candidate remains internally consistent and constitution-compliant.

- [ ] T016 Audit the scope intake, evidence register, checklist, evidence review, and next-slice record for Constitution §§I–V traceability, explicit unknowns, and evidence-only scope in `specs/002-test-evidence-definition/evidence-review.md`
- [ ] T017 Execute the five documentary validation steps in `quickstart.md` and record the candidate’s completion criterion and remaining blocked inputs in `specs/002-test-evidence-definition/evidence-review.md`

---

## Dependencies & Execution Order

### Phase Dependencies

```text
Phase 1: T001, T002, T003
             ↓
Phase 2: T004, T005, T006
             ↓
US1: T007 → T008 → T009 (MVP)
US2: T010 → T011 → T012
US3: T013 → T014 → T015
             ↓
Polish: T016 → T017
```

- **Setup (Phase 1)**: T001–T003 have no prerequisites and create separate records.
- **Foundational (Phase 2)**: Depends on the corresponding setup records and blocks all story reviews.
- **User Story 1 (P1)**: Depends on T004–T006; it defines the MVP reviewable boundary.
- **User Story 2 (P2)**: Depends on T004–T006 and the completed US1 boundary records; it reviews them as a separately testable reading-limit increment.
- **User Story 3 (P3)**: Depends on T004–T006 and requires the boundary from US1; it preserves blocked fields where observable-contract evidence is absent.
- **Polish (Phase 6)**: Depends on the completed story records.

### User Story Dependencies

- **US1 (P1)**: No dependency on another user story after the foundational controls complete.
- **US2 (P2)**: Reviews the US1 boundary records but remains a separately testable reading-limit increment.
- **US3 (P3)**: Depends on the documented US1 boundary; it does not depend on any executable test result.

### Parallel Opportunities

- T001, T002, and T003 can run in parallel because they create different files.
- T004, T005, and T006 can run in parallel after their corresponding setup records exist because they update different files.
- No tasks within an individual user-story phase are marked parallel because each subsequent task reviews or extends the prior record.

## Parallel Examples

### Setup

```text
Task: "Create scope-intake record headings and fields in specs/002-test-evidence-definition/scope-intake.md"
Task: "Create evidence-register headings and classification fields in specs/002-test-evidence-definition/evidence-register.md"
Task: "Create claim-review checklist headings and checks in specs/002-test-evidence-definition/claim-review-checklist.md"
```

### User Story 1

```text
No parallel tasks: T007 → T008 → T009 preserves the decision-to-register-to-review chain.
```

### User Story 2

```text
No parallel tasks: T010 → T011 → T012 preserves the classification-to-review chain.
```

### User Story 3

```text
No parallel tasks: T013 → T014 → T015 preserves the template-to-blocked-record-to-review chain.
```

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete T001–T006 to establish the candidate records and safeguards.
2. Complete T007–T009 to create and review the fixed evidence-definition boundary.
3. Stop and validate the P1 independent test before creating a future-slice record or making any claim about execution or migration parity.

### Incremental Delivery

1. Deliver the P1 boundary record and documentary review.
2. Add P2 claim classification and reading-limit review.
3. Add P3’s explicitly blocked next-slice record.
4. Complete the cross-cutting constitutional and quickstart review.

## Notes

- All tasks are proposed documentation work, not observed legacy implementation behaviour.
- A future task may only replace a blocked next-slice field when newly supplied permitted evidence identifies its observable contract and acceptance check.
