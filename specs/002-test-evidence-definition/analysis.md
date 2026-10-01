## Specification Analysis Report

| ID | Category | Severity | Location(s) | Summary | Recommendation |
|----|----------|----------|-------------|---------|----------------|
| C1 | Constitution alignment / inconsistency | CRITICAL | tasks.md:L185; spec.md:L32-L36; plan.md:L33-L35 | Completed T020 says relevant acceptance criteria were obtained and planning and validation no longer proceed without them. The specification and plan instead record `Acceptance boundaries: (none stated)` and an active `BLOCKED` gate. This conflicts with Constitution III and V; the task cannot truthfully be complete from the stated evidence. | Reopen or replace T020. Retain the blocked gate and limit work to recording its status until the scope owner supplies criteria; do not claim their receipt or an acceptance result. |
| C2 | Constitution alignment / unmapped work | CRITICAL | tasks.md:L181; spec.md:L89-L118; plan.md:L49-L70 | Completed T019 is expressly labelled `unrequested` and has no mapped functional requirement, success criterion, user story, or planned record. Constitution V requires every task to link to supporting evidence or be explicitly identified as a proposed decision; this task does neither. | Remove T019, or add an evidence-backed proposed decision and corresponding specification/plan traceability before scheduling it. |
| A1 | Ambiguity | HIGH | spec.md:L93 | FR-001 requires provenance “verbatim enough,” but gives no review rule for deciding what wording, citation, or source excerpt is sufficient. | Define an objective minimum, such as an exact citation plus the quoted documented status or scope-owner response for each of the four recorded decisions. |
| A2 | Ambiguity / underspecification | HIGH | spec.md:L114, L117; tasks.md:L78-L80 | SC-001 and SC-004 measure claims in a “next test-slice specification,” while the planned deliverable is a blocked `next-test-slice.md` record. Neither criterion defines the claim population or the review boundary, so 100% coverage and “every claimed expected outcome” cannot be consistently measured. | Name the exact record(s) and sections to review, or defer these success criteria until a later observable-contract specification exists. |

**Coverage Summary Table:**

| Requirement Key | Has Task? | Task IDs | Notes |
|-----------------|-----------|----------|-------|
| FR-001 | Yes | T004, T007, T008 | Boundary decisions and provenance are recorded. |
| FR-002 | Yes | T006, T010, T012, T015 | Classification controls and review are specified. |
| FR-003 | Yes | T005, T011, T012 | Reading-limit entries and findings are covered. |
| FR-004 | Yes | T006, T009, T012, T015 | Unsupported outcome assertions are blocked. |
| FR-005 | Yes | T004, T007, T018 | T018 is retrospective; the pre-planning disposition is documented in the specification. |
| FR-006 | Yes | T004, T007, T008 | Evidence-only scope is recorded. |
| FR-007 | Yes | T004, T008 | Unavailable acceptance artifact is recorded. |
| FR-008 | Yes | T004, T008, T009, T015 | Documentary review is selected; execution/parity are excluded. |
| FR-009 | Yes | T004, T017, T020 | T020 conflicts with the active blocked gate (C1). |
| SC-001 | Yes | T010, T012, T015 | Coverage exists, but the assessed claim set is ambiguous (A2). |
| SC-002 | Yes | T005, T011, T012 | Reading-limit preservation is covered. |
| SC-003 | Yes | T004, T007, T008, T018 | Bounded target, unavailable artifact, and evaluation type are covered. |
| SC-004 | Yes | T013, T014, T015 | Coverage exists, but the assessed claim set is ambiguous (A2). |
| SC-005 | Yes | T004, T017, T020 | T020 contradicts the criterion's blocked-gate condition (C1). |

**Constitution Alignment Issues:**

- C1 conflicts with Constitution III (specification before delivery) and V (traceable acceptance): the required acceptance criteria remain absent, so acceptance planning and acceptance-validation claims must remain blocked.
- C2 conflicts with Constitution V because T019 has no evidence or proposed-decision traceability in the core artifacts.

**Unmapped Tasks:**

- T019 is unmapped. Its stated source is only other task descriptions, not a requirement, success criterion, user story, or planned record.

**Metrics:**

- Total Requirements: 14 (9 functional requirements; 5 buildable success criteria)
- Total Tasks: 23
- Coverage: 100% (14 of 14 requirements have at least one mapped task)
- Ambiguity Count: 2
- Duplication Count: 0
- Critical Issues Count: 2

## Next Actions

- Resolve C1 and C2 before `/speckit-implement`; both are constitution conflicts.
- Run `/speckit-specify` to refine FR-001 and SC-001/SC-004, then `/speckit-plan` and `/speckit-tasks` to regenerate aligned work.
- Do not treat the current documentary review as acceptance planning or acceptance validation while the acceptance-criteria gate remains `BLOCKED`.

Would you like me to suggest concrete remediation edits for the top 2 issues?
