# Architecture

After reading this page, an engineer will understand the repository's documentation components, how a claim moves through review, and why no runtime architecture is described. The architecture is a set of Markdown records and a Python documentary checker, not a deployed application.

## Components

| Component | Responsibility | Evidence |
|---|---|---|
| `spec.md` | Defines the evidence-only boundary, requirements, and blocked acceptance gate. | [spec.md: Acceptance-Criteria Gate](../specs/002-test-evidence-definition/spec.md#acceptance-criteria-gate) |
| `plan.md` | States the Markdown-only technical context and record layout. | [plan.md: Technical Context and Project Structure](../specs/002-test-evidence-definition/plan.md#technical-context) |
| `scope-intake.md` | Records scope owner, target, unavailable acceptance artifact, evaluation type, and outcome block. | [scope intake table](../specs/002-test-evidence-definition/scope-intake.md) |
| `evidence-register.md` | Holds classified claims and their source or decision references. | [evidence register](../specs/002-test-evidence-definition/evidence-register.md#evidence-register-entries) |
| `claim-review-checklist.md` | Specifies the citation, reading-limit, outcome, and acceptance-gate checks. | [claim review checks](../specs/002-test-evidence-definition/claim-review-checklist.md#claim-review-checks) |
| `evidence-review.md` | Records documentary review findings, audit, validation, and blockers. | [evidence review: T016 and T017](../specs/002-test-evidence-definition/evidence-review.md#t016-constitution-iv-cross-record-audit) |
| `next-test-slice.md` | Keeps future contract fields blocked until evidence is supplied. | [next-test-slice record](../specs/002-test-evidence-definition/next-test-slice.md) |
| `.referee/.../test_evidence_definition.py` | Verifies required record contents and protects against unsupported negative or execution/parity claims. | [`EvidenceDefinitionAcceptanceTests`](../.referee/002-test-evidence-definition/test_evidence_definition.py) |

## Data flow: entry to exit

```text
legacy reading + work-unit scope input
              |
              v
      spec.md / scope-intake.md
              |
              v
      evidence-register.md  --> classify claim
              |
              v
  claim-review-checklist.md --> pass / unresolved / blocked / rejected
              |
              v
  evidence-review.md + next-test-slice.md
              |
              v
  Python referee test verifies record shape and safeguards
```

The flow is defined by the record relationships: the scope intake supplies proposed-decision entries to the register; the claim review evaluates them; the next-slice record may reference them but cannot assert an outcome without a contract and acceptance check ([data model: Relationships](../specs/002-test-evidence-definition/data-model.md#relationships)). The only built automated exit is a `unittest` result from the referee test; it is not a legacy execution result ([referee test: `EvidenceDefinitionAcceptanceTests`](../.referee/002-test-evidence-definition/test_evidence_definition.py)).

## External dependencies

| Dependency | Why it is used | Version / interface |
|---|---|---|
| Legacy readings under `../../old/docs/` | Permitted evidence for statements about the legacy estate. | Markdown documents; no version declared ([constitution: Evidence and Scope Constraints](../.specify/memory/constitution.md#evidence-and-scope-constraints)) |
| Python standard library | Runs the referee test via `unittest`; the test imports `re` and `pathlib`. | Python 3, exact version not pinned ([referee test: imports](../.referee/002-test-evidence-definition/test_evidence_definition.py)) |

No service, database, network client, package dependency, API, or build tool is declared ([plan.md: Technical Context](../specs/002-test-evidence-definition/plan.md#technical-context)).

## Key design decisions

| Decision | Reason | Evidence |
|---|---|---|
| Keep the candidate in Markdown records | The target is evidence definition, not a runnable component. | [research.md: Decision 4](../specs/002-test-evidence-definition/research.md#decision-4-documentation-technology) |
| Treat the acceptance artifact as unavailable | Its contents, location, and supplier are absent from permitted material. | [research.md: Decision 2](../specs/002-test-evidence-definition/research.md#decision-2-acceptance-artifact-treatment) |
| Use documentary review only | The reading has no described behaviour and no execution-grounded item. | [research.md: Decision 3](../specs/002-test-evidence-definition/research.md#decision-3-evaluation-type) |
| Preserve unavailable searches as limits | A missing reading cannot support an absence claim. | [constitution: Principle II](../.specify/memory/constitution.md#core-principles) |

## Gaps against the specification

The planned structure explicitly says no `contracts/` directory is created because the candidate exposes no runtime, API, CLI, or other external interface ([plan.md: Project Structure](../specs/002-test-evidence-definition/plan.md#project-structure)). Therefore no executable component diagram, request protocol, persistence model, or deployment topology is present in this tree.
