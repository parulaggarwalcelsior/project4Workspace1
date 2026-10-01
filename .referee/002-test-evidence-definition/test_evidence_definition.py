"""Acceptance tests for work order 002-test-evidence-definition.

Run explicitly because .referee is intentionally hidden from normal recursive
test discovery:

    python3 -m unittest discover -s .referee/002-test-evidence-definition -v
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CANDIDATE = PROJECT_ROOT / "specs" / "002-test-evidence-definition"


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower())


def record(name: str) -> str:
    path = CANDIDATE / name
    if not path.is_file():
        raise AssertionError(f"Required candidate record is missing: {path.relative_to(PROJECT_ROOT)}")
    return normalized(path.read_text(encoding="utf-8"))


def block_after(text: str, heading_words: str) -> str:
    """Return the local entry-sized context following a record field/topic."""
    match = re.search(heading_words, text, flags=re.IGNORECASE)
    if not match:
        return ""
    return text[match.start() : match.start() + 1_000]


class EvidenceDefinitionAcceptanceTests(unittest.TestCase):
    """Documentary acceptance checks; no legacy execution is authorized."""

    def test_required_documentary_records_exist(self) -> None:
        for name in (
            "scope-intake.md",
            "evidence-register.md",
            "claim-review-checklist.md",
            "evidence-review.md",
            "next-test-slice.md",
        ):
            with self.subTest(record=name):
                self.assertTrue(
                    (CANDIDATE / name).is_file(),
                    f"{name} must be created for the evidence-definition candidate",
                )

    def test_scope_intake_records_all_fixed_boundary_decisions_with_provenance(self) -> None:
        text = record("scope-intake.md")

        required_concepts = {
            "scope-owner role": ("work-unit operator",),
            "test target": ("evidence-definition",),
            "acceptance artifact": ("unavailable",),
            "evaluation type": ("documentary", "evidence review"),
            "outcome status": ("blocked",),
            "supplied-on date": ("supplied on",),
            "provenance": ("spec.md", "clarification"),
        }
        for label, terms in required_concepts.items():
            with self.subTest(decision=label):
                for term in terms:
                    self.assertIn(term, text, f"Scope intake must record {label}: {term!r}")

        self.assertRegex(
            text,
            r"proposed\s+(scope\s+)?decision",
            "Fixed boundary decisions must be labelled as proposed, not discovered legacy behaviour",
        )
        for requirement in ("fr-006", "fr-007", "fr-008"):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, text, "Scope intake must trace the fixed decisions to FR-006 through FR-008")
        self.assertRegex(
            text,
            r"(?:not select|does not select|no).{0,180}(legacy behaviour|legacy behavior|asset|inventory.wide)",
            "The selected target must not be represented as a behaviour, asset, or inventory-wide target",
        )
        self.assertRegex(
            text,
            r"(exclude|not in scope|out of scope).{0,160}(legacy execution|execution).{0,160}(parity|legacy.to.target)",
            "Scope intake must exclude execution and legacy-to-target parity from this candidate",
        )

    def test_evidence_register_has_all_four_claim_classes_and_boundary_entries(self) -> None:
        text = record("evidence-register.md")

        for classification in (
            "verified legacy evidence",
            "documented reading limit",
            "supported inference",
            "proposed scope decision",
        ):
            with self.subTest(classification=classification):
                self.assertIn(classification, text, "The register must expose every allowed claim classification")

        for decision in ("work-unit operator", "evidence-definition", "acceptance artifact", "documentary"):
            with self.subTest(decision=decision):
                self.assertIn(decision, text, "Every fixed boundary decision needs a register entry")

        self.assertIn("spec.md", text, "Proposed boundary entries must cite their decision source")

    def test_unavailable_and_unsearched_readings_remain_limits_not_negative_findings(self) -> None:
        register = record("evidence-register.md")
        review = record("evidence-review.md")
        combined = register + "\n" + review

        expectations = {
            "persistence": ("data_model.md", "unavailable"),
            "endpoint": ("api_surface.md", "unavailable"),
            "security": ("security.md", "could not search"),
            "edge case": ("edge_cases.md", "could not search"),
            "workflow": ("workflows.md", "could not search"),
        }
        for topic, (citation, status) in expectations.items():
            with self.subTest(topic=topic):
                section = block_after(combined, re.escape(topic))
                self.assertTrue(section, f"A separate documented-limit finding is required for {topic}")
                self.assertIn(citation, section, f"{topic} finding must cite its permitted legacy reading")
                self.assertIn(status, section, f"{topic} finding must preserve its documented reading status")
                self.assertRegex(
                    section,
                    r"(documented reading limit|reading limit|unknown|unsearched|unavailable)",
                    f"{topic} must be represented as a limit of the reading, not an estate finding",
                )

        # These are direct negative findings the candidate must not make from the
        # unavailable readings.  Protective wording such as "must not claim no
        # endpoint" belongs in the checklist and is deliberately not rejected.
        candidate_records = "\n".join(
            record(name)
            for name in ("scope-intake.md", "evidence-register.md", "evidence-review.md", "next-test-slice.md")
        )
        impermissible = (
            r"\b(?:there is|there are|estate has|system has) no (?:persistence|data|endpoint|endpoints|security|edge cases?|workflows?)\b",
            r"\b(?:persistence|data|endpoint|endpoints|security|edge cases?|workflows?) (?:does not|do not|don't) exist\b",
        )
        for pattern in impermissible:
            self.assertNotRegex(candidate_records, pattern, "Reading limits cannot be converted into negative estate findings")

    def test_checklist_rejects_unsupported_claims_and_outcomes(self) -> None:
        text = record("claim-review-checklist.md")
        required_controls = (
            r"citation.{0,120}proposed.{0,120}decision",
            r"reading.{0,80}limit",
            r"outcome.{0,80}(assertion|claim)",
            r"(reject|block).{0,180}(unsupported|uncited).{0,180}(negative|absence)",
            r"(block|reject).{0,180}(expected outcome|legacy output|execution result|parity)",
        )
        for control in required_controls:
            with self.subTest(control=control):
                self.assertRegex(text, control, "Checklist must contain the required evidence-control check")

    def test_evidence_review_records_documentary_status_without_execution_or_parity_result(self) -> None:
        text = record("evidence-review.md")

        self.assertRegex(text, r"\b(pass|unresolved|blocked|rejected)\b", "Review findings need an allowed review status")
        self.assertIn("documentary", text, "Review must identify the documentary evaluation boundary")
        self.assertRegex(text, r"no.{0,100}(execution|parity).{0,100}(conclusion|result|available)", "Review must explicitly retain the blocked execution/parity conclusion")

        impermissible_results = (
            r"\b(?:test|execution) (?:passed|succeeded|completed successfully)\b",
            r"\b(?:java|legacy).{0,80}(?:matches|is equivalent to|has parity with).{0,80}(?:go|target)\b",
            r"\bexpected legacy (?:output|outcome)\s*(?:is|:)\s*[^.]{3}",
        )
        for pattern in impermissible_results:
            self.assertNotRegex(text, pattern, "The evidence review may not report an execution, output, or parity result")

    def test_final_review_records_cross_cutting_audit_and_remaining_blockers(self) -> None:
        text = record("evidence-review.md")
        self.assertIn("constitution", text, "The final review must audit Constitution §§I–V")
        for numeral in ("i", "ii", "iii", "iv", "v"):
            with self.subTest(constitution_section=numeral):
                self.assertRegex(
                    text,
                    rf"(?:§|section\\s+){numeral}\\b",
                    "Evidence review must retain traceability for every constitutional section",
                )
        self.assertRegex(text, r"quickstart|validation step", "The five documentary validation steps must be recorded as executed")
        self.assertRegex(text, r"completion criterion", "The review must state the candidate completion criterion")
        self.assertRegex(text, r"remaining blocked|blocked inputs|remaining inputs", "The review must identify inputs still blocked")

    def test_next_test_slice_keeps_unsupplied_contract_fields_blocked(self) -> None:
        text = record("next-test-slice.md")

        for field in (
            "bounded subject",
            "input",
            "expected outcome",
            "observable contract",
            "evidence source",
            "acceptance check",
            "evaluation type",
            "blocked status",
        ):
            with self.subTest(field=field):
                self.assertIn(field, text, f"Next-slice record must include the {field} field")

        for unsupplied in ("input", "expected outcome", "observable contract", "evidence source", "acceptance check"):
            section = block_after(text, re.escape(unsupplied))
            with self.subTest(unsupplied=unsupplied):
                self.assertTrue(section, f"Next-slice record needs a {unsupplied} entry")
                self.assertIn("blocked", section, f"Unsupplied {unsupplied} must be blocked, not invented")

        self.assertRegex(
            text,
            r"(evidence.supported|proposed|blocked).{0,160}(evidence.supported|proposed|blocked)",
            "Each next-slice field must be reviewable as evidence-supported, proposed, or blocked",
        )
        self.assertRegex(text, r"no.{0,100}(execution|parity).{0,100}(conclusion|result|available)", "No execution or parity conclusion is available")


if __name__ == "__main__":
    unittest.main(verbosity=2)
