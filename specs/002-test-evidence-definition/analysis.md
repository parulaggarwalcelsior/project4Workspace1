## Specification Analysis Report

| ID | Category | Severity | Location(s) | Summary | Recommendation |
|----|----------|----------|-------------|---------|----------------|
| C1 | Constitution Alignment | CRITICAL | constitution.md:L60-64; spec.md:L22-26, L91; plan.md:L35-41 | The constitution requires the scope owner to supply or identify relevant acceptance criteria before a feature is specified. The specification instead records the acceptance artifact as unavailable and expressly does not define an acceptance check; the plan nevertheless marks the constitution check as passing. The candidate's documentary review criteria do not identify the missing legacy acceptance criteria. | Before implementation, have the scope owner supply or identify the relevant acceptance criteria and update the artifacts with their provenance. If the evidence-definition candidate is intentionally permitted without them, amend the constitution through its separate amendment workflow; do not reinterpret this MUST requirement in the feature artifacts. |
| A1 | Ambiguity / Inconsistency | HIGH | spec.md:L86, L105-108; tasks.md:L62-64, L78-80 | FR-002 mandates one of four classifications for every estate-related statement, while SC-004 and T015 use a different three-state vocabulary: `evidence-supported`, `proposed`, or `blocked`. The latter has no defined mapping to the required classifications, so a blocked next-slice field cannot be shown to satisfy FR-002. | Separate `Classification` (the four FR-002 values) from `Review status` (for example, supported/unresolved/blocked/rejected) in the specification, record model, and T015. State how every next-slice statement receives both fields. |
| A2 | Ambiguity | HIGH | spec.md:L105-108; plan.md:L54-59; tasks.md:L62-64, L90-91 | SC-001's “next test-slice specification” is not a defined artifact: the plan defines `next-test-slice.md` as a record, not a specification. SC-002 also does not define the corpus whose references must be counted. Consequently, the stated 100% outcomes cannot be measured or independently checked. | Name the exact review corpus (paths and claim types) for SC-001 and SC-002, define its enumeration method, and make the final validation task record the numerator, denominator, and any excluded non-claim text. |
| G1 | Coverage Gap / Ordering | HIGH | spec.md:L86; tasks.md:L62-66, L78-91, L104-108 | T010 performs the explicit classification sweep before T011, T012, T014, and T015 add or review further candidate claims. Its scope is only the scope intake and evidence review, while later work creates `next-test-slice.md`. T016 audits records but does not require recording the four FR-002 classifications. Thus no task conclusively covers FR-002 for claims introduced after T010. | Add a final, post-T015 classification-and-register task that covers every candidate record and records each claim's FR-002 classification, citation/decision label, and review status; make T016 depend on it. |
| U1 | Underspecification | MEDIUM | spec.md:L77-79; plan.md:L52-58; tasks.md:L30-32, L62-64 | The edge case for an acceptance artifact that conflicts with an unavailable or unsearched reading requires recording the conflict and its provenance. No planned record schema or task expressly captures a conflict, its two sources, and a non-resolution outcome. | Add a conflict/provenance field or a dedicated review finding format, plus a task and independent check requiring conflicting evidence to remain unresolved rather than become a legacy fact. |

### Coverage Summary

| Requirement Key | Has Task? | Task IDs | Notes |
|-----------------|-----------|----------|-------|
| FR-001 | Yes | T004, T007, T008 | Boundary decisions and provenance are recorded. |
| FR-002 | Yes, incomplete | T002, T006, T010, T012, T016 | See G1: later claims are not explicitly classified in the final state. |
| FR-003 | Yes | T005, T006, T011, T012, T016 | Reading-limit controls cover all named areas. |
| FR-004 | Yes | T006, T009, T012, T014, T015, T016 | Outcome and parity assertions are blocked. |
| FR-005 | Yes | T004, T007 | The specification's Clarifications also record the decisions before the plan. |
| FR-006 | Yes | T004, T007, T008 | Tasks retain the evidence-definition-only boundary. |
| FR-007 | Yes | T004, T007, T008 | Tasks retain the unavailable acceptance artifact. |
| FR-008 | Yes | T004, T008, T009, T014, T015 | Tasks retain documentary-only evaluation. |
| SC-001 | Yes, ambiguous | T010, T012, T016 | See A2 and G1: the corpus and final classification sweep are missing. |
| SC-002 | Yes, ambiguous | T005, T011, T012, T016 | See A2: the population of references is undefined. |
| SC-003 | Yes | T004, T007 | The three decisions are also already present in Clarifications. |
| SC-004 | Yes, inconsistent | T006, T014, T015, T017 | See A1: its labels do not align with FR-002's taxonomy. |

### Constitution Alignment Issues

- **C1 (CRITICAL):** The missing legacy acceptance criteria conflict with the prerequisite in the Specification Workflow. Implementation should not begin until this is resolved through supplied/identified criteria or a separate constitution amendment.

### Unmapped Tasks

None. Each of T001–T017 supports at least one requirement, success criterion, or their shared documentary-review controls.

### Metrics

- Total Requirements: 12
- Total Tasks: 17
- Coverage: 100% (12 of 12 requirements have at least one associated task; qualitative gaps are listed above)
- Ambiguity Count: 2
- Duplication Count: 0
- Critical Issues Count: 1

### Next Actions

- Resolve C1 before `/speckit-implement`; it is a constitution MUST conflict.
- Run `/speckit-specify` to define the measurable review corpus and reconcile classification/status terminology, then run `/speckit-plan` and `/speckit-tasks` to update the downstream design and task ordering.
- Add the conflict-provenance control for the stated edge case before implementation.

Would you like me to suggest concrete remediation edits for the top 4 issues?
