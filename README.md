# Test Evidence Definition

This repository contains an evidence-definition documentation candidate for a legacy Java estate, not a Java or Go application. It records what must be known before testing or a Java-to-Go parity claim can be made; the available legacy reading has no execution-grounded behaviour ([specification: Evidence Basis and Scope Boundary](specs/002-test-evidence-definition/spec.md#evidence-basis-and-scope-boundary)).

It is for engineers and reviewers who need to inspect the candidate, preserve the legacy-reading limits, and run the repository's documentary checks. The declared Java source, intended Go target, and goal `test` are context only; they do not provide an executable contract ([AGENTS.md: “THE OPERATOR'S DECLARED GOAL”](AGENTS.md)).

## In under a minute

Prerequisite: Python 3. The tree does not pin a Python version or declare a package manager; the referee test imports only `unittest`, `re`, and `pathlib` from the standard library ([.referee/002-test-evidence-definition/test_evidence_definition.py: imports](.referee/002-test-evidence-definition/test_evidence_definition.py)).

```bash
# Build: not present in this tree; the candidate is Markdown only.

# Run: not present in this tree; it exposes no runtime, API, CLI, or service.

# Test the documentary candidate.
python3 -m unittest discover -s .referee/002-test-evidence-definition -v
```

The test command is supplied verbatim by the referee test's module docstring. It checks the candidate records; it does not execute the legacy estate or a Go implementation ([referee test: module docstring and `EvidenceDefinitionAcceptanceTests`](.referee/002-test-evidence-definition/test_evidence_definition.py)).

## Configuration

| Variable | Default | Purpose and effect |
|---|---|---|
| None declared | — | No environment variable, flag, configuration file, runtime, or external interface is specified. The plan identifies the project type as an evidence-definition documentation candidate ([plan.md: Technical Context](specs/002-test-evidence-definition/plan.md#technical-context)). |

## Documentation

- [Overview](docs/01-overview.md) — audience, vocabulary, scope, and boundaries.
- [Architecture](docs/02-architecture.md) — records, review flow, and dependencies.
- [How it works](docs/03-how-it-works.md) — documentary flows and exact examples.
- [Running and operating](docs/04-running-and-operating.md) — prerequisites, commands, diagnostics, and failures.
- [Migration from legacy](docs/05-migration-from-legacy.md) — the limited legacy evidence and compatibility implications.
- [Testing and quality](docs/06-testing-and-quality.md) — referee coverage and local quality gates.
- [Decisions](docs/07-decisions.md) — cited decision log.

## Gaps against the specification

The requested scope is documentation and evidence review only. No Java execution, Go code, observable legacy contract, expected outcome, acceptance check, or Java-to-Go parity result is built; each is blocked pending supplied evidence and criteria ([spec.md: FR-004 and FR-006 through FR-009](specs/002-test-evidence-definition/spec.md#functional-requirements); [evidence review: Remaining blocked inputs](specs/002-test-evidence-definition/evidence-review.md#t017-quickstart-documentary-validation)).
