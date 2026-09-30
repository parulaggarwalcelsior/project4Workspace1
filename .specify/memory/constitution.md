<!--
Sync Impact Report
- Version change: none → 1.0.0
- Modified principles: none (initial adoption)
- Added sections: Core Principles; Evidence and Scope Constraints; Specification Workflow;
  Governance
- Removed sections: none
- Follow-up TODOs: [NEEDS CLARIFICATION: What precisely does the operator's stated goal
  "test" require, including the estate in scope, acceptance basis, and test type?]
-->
# Legacy Estate Evidence Constitution

## Core Principles

### I. Evidence-Bound Description
All statements about the legacy estate MUST be supported by the allowed legacy documentation
or by earlier artifacts in this working tree. A named code symbol and the evidence for a rule
MUST be reproduced verbatim from the documented source. The work MUST describe observed
behaviour only; it MUST NOT treat a declared migration goal, a missing reading, or an
unavailable analysis as evidence of behaviour. Rationale: faithful reconstruction depends on
preserving the distinction between evidence, inference, and absence of evidence.

### II. Unknowns Remain Explicit
The work MUST preserve documented uncertainty. An unavailable view, zero-item inventory, or
failed search MUST NOT be restated as a finding that the estate has no corresponding behaviour.
When necessary information is absent, the artifact MUST include a


### III. Specification Precedes Delivery
Any proposed work on the estate MUST follow the ordered flow: specification, plan, tasks, then
implementation. Each stage MUST state its evidence basis and must not broaden scope beyond the
approved specification. Rationale: the declared Java-to-Go direction and the word "test" do not
define a system boundary, acceptance criteria, or behaviour to implement.

### IV. Migration Preserves Established Semantics
If a Java behaviour is later re-expressed in Go, its specification MUST identify the source
evidence, externally observable contract, and acceptance check before implementation begins.
The target language MUST NOT change the claimed behaviour solely by implication. Rationale:
language direction is contextual information, not a substitute for a verified behavioural model.

### V. Traceable Acceptance
Every requirement, plan item, task, and validation claim MUST link to its supporting legacy
evidence or explicitly identify itself as a proposed decision. Validation MUST distinguish a
verified result from an untested or unavailable result. Rationale: the current documentation
states that its acceptance basis is frozen but does not provide its contents.

## Evidence and Scope Constraints

The subject of this work is the legacy estate described in `../../old/docs/`, not the incidental
contents of this workspace or unrelated repositories. The documented reading identifies Java as
the source language and records zero interpreted components, rules, and behaviours. It also
marks persistence, API surface, security, edge cases, and workflows as unavailable or
unsearched; those limits MUST be retained as limits, not converted into negative findings.

[NEEDS CLARIFICATION: What precisely does the operator's stated goal "test" require, including
the estate in scope, acceptance basis, and test type?]

## Specification Workflow

Before a feature is specified, the scope owner MUST supply or identify the relevant legacy
evidence and acceptance criteria. A specification MUST enumerate what is known, label all
inferences, and retain open questions. Planning MUST map each proposed outcome to the
specification. Tasks MUST be independently checkable against their plan and evidence. No
implementation may begin until these preceding artifacts exist and define a bounded slice.

## Governance

This constitution governs all work artifacts in this workspace and supersedes conflicting local
process guidance, except for higher-priority operator instructions. Amendments MUST document the
change, its evidence or rationale, its effects on dependent artifacts, and an updated Sync Impact
Report. A compliance review MUST occur when creating or amending a specification, plan, tasks,
or implementation artifact; the reviewer MUST verify evidence traceability, explicit unknowns,
and adherence to the required workflow.

Constitution versions use semantic versioning: a MAJOR version removes or incompatibly redefines
a governing principle; a MINOR version adds a principle or materially expands governance; a PATCH
version makes a clarification, wording change, or other non-semantic refinement. The ratification
date records original adoption and remains unchanged by later amendments; the last-amended date
changes whenever the constitution changes.

**Version**: 1.0.0 | **Ratified**: 2026-09-29 | **Last Amended**: 2026-09-29
