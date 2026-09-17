#!/usr/bin/env python3
"""Regression tests for the Agent Evaluation descriptive aggregator."""

from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/1-agent-evaluation/scripts/aggregate_results.py"
SPEC = importlib.util.spec_from_file_location("agent_eval_aggregate", SCRIPT)
assert SPEC and SPEC.loader
AGG = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AGG)


class AgentEvaluationAggregateTests(unittest.TestCase):
    def write_jsonl(self, directory: Path, records: list[object]) -> Path:
        path = directory / "results.jsonl"
        path.write_text("".join(json.dumps(record) + "\n" for record in records), encoding="utf-8")
        return path

    def test_load_rejects_duplicate_identity_nonfinite_and_missing_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            duplicate = self.write_jsonl(root, [
                {"case_id": "a", "variant": "v", "run_id": "1", "score": 0.2, "passed": True},
                {"case_id": "a", "variant": "v", "run_id": "1", "score": 0.3, "passed": False},
            ])
            with self.assertRaisesRegex(ValueError, "duplicate record identity"):
                AGG.load_records(duplicate, score_min=0, score_max=1, require_passed=True)

            nonfinite = self.write_jsonl(root, [{"case_id": "a", "score": float("nan"), "passed": True}])
            with self.assertRaisesRegex(ValueError, "score must be finite"):
                AGG.load_records(nonfinite, score_min=0, score_max=1, require_passed=True)

            missing = self.write_jsonl(root, [{"case_id": "a", "score": 0.5}])
            with self.assertRaisesRegex(ValueError, "passed is required"):
                AGG.load_records(missing, score_min=0, score_max=1, require_passed=True)

    def test_summary_reports_missing_pass_denominator_and_descriptive_scope(self):
        records = [
            {"case_id": "a", "variant": "v", "score": 1.0, "passed": True, "category": "safe"},
            {"case_id": "b", "variant": "v", "score": 0.0, "category": "safe"},
        ]
        summary = AGG.summarize(records, score_min=0, score_max=1, baseline=None, candidate=None)
        self.assertEqual(summary["pass_rate"]["observed_records"], 1)
        self.assertEqual(summary["pass_rate"]["missing_records"], 1)
        self.assertEqual(summary["pass_rate"]["total_records"], 2)
        self.assertIn("does not certify", summary["scope"])

    def test_comparison_requires_both_arms_and_labels_independent_interval(self):
        records = [
            {"case_id": "a", "variant": "old", "score": 0.2, "category": "x"},
            {"case_id": "b", "variant": "old", "score": 0.4, "category": "x"},
            {"case_id": "a", "variant": "new", "score": 0.5, "category": "x"},
            {"case_id": "b", "variant": "new", "score": 0.7, "category": "x"},
        ]
        result = AGG.comparison_summary(records, "old", "new")
        self.assertAlmostEqual(result["candidate_minus_baseline_mean"], 0.3)
        self.assertIn("candidate_minus_baseline_ci95_normal_approx_independent", result)
        with self.assertRaisesRegex(ValueError, "no records found"):
            AGG.comparison_summary(records, "missing", "new")

    def test_atomic_output_rejects_input_aliases_and_writes_exact_payload(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = self.write_jsonl(root, [{"case_id": "a", "score": 1, "passed": True}])
            original = source.read_text(encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "must not be the input"):
                AGG.write_text_atomic(source, source, "bad")

            symlink = root / "summary-link.json"
            symlink.symlink_to(source)
            with self.assertRaisesRegex(ValueError, "symbolic link|resolve to the input"):
                AGG.write_text_atomic(source, symlink, "bad")

            output = root / "summary.json"
            AGG.write_text_atomic(source, output, "{\"ok\": true}\n")
            self.assertEqual(output.read_text(encoding="utf-8"), "{\"ok\": true}\n")
            self.assertEqual(source.read_text(encoding="utf-8"), original)


if __name__ == "__main__":
    unittest.main()
