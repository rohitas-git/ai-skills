#!/usr/bin/env python3
"""Regression tests for the catalog's AI-native skill evaluation helper."""

from __future__ import annotations

import json
import runpy
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
EVAL = runpy.run_path(str(ROOT / "scripts/evaluate-skills"))


class SkillEvaluationTests(unittest.TestCase):
    def case(self, **overrides):
        case = {
            "id": "route-diagnose",
            "kind": "route",
            "invoked_skill": "0-butler",
            "prompt": "Use Butler to route a nondeterministic timeout investigation.",
            "expected_skill": "0-diagnosing-bugs",
            "forbidden_skills": ["0-implement"],
            "runtimes": ["codex", "claude"],
            "risk": "normal",
            "assertions": [
                {"type": "contains", "value": "/0-diagnosing-bugs"},
                {"type": "not_contains", "value": "implemented the fix"},
            ],
        }
        case.update(overrides)
        return case

    def test_validate_cases_accepts_minimal_fixed_contract(self):
        cases = EVAL["validate_cases"]({"schema_version": 1, "cases": [self.case()]})
        self.assertEqual(cases[0]["id"], "route-diagnose")
        self.assertEqual(EVAL["require_safe_label"]("candidate-1", "variant"), "candidate-1")
        with self.assertRaisesRegex(ValueError, "path-safe label"):
            EVAL["require_safe_label"]("../escape", "variant")

    def test_validate_cases_rejects_duplicate_ids_and_unknown_runtime(self):
        duplicate = self.case()
        with self.assertRaisesRegex(ValueError, "duplicate case id"):
            EVAL["validate_cases"]({"schema_version": 1, "cases": [duplicate, duplicate]})
        with self.assertRaisesRegex(ValueError, "unsupported runtime"):
            EVAL["validate_cases"]({
                "schema_version": 1,
                "cases": [self.case(runtimes=["other"])],
            })
        with self.assertRaisesRegex(ValueError, "path-safe label"):
            EVAL["validate_cases"]({
                "schema_version": 1,
                "cases": [self.case(id="../../escape")],
            })
        with self.assertRaisesRegex(ValueError, "forbidden_skills"):
            EVAL["validate_cases"]({
                "schema_version": 1,
                "cases": [self.case(forbidden_skills="0-implement")],
            })

    def test_grade_output_requires_all_assertions_and_expected_skill(self):
        case = self.case()
        result = EVAL["grade_output"](
            case,
            "**Use:** `/0-diagnosing-bugs`\nInvestigate and return evidence only.",
        )
        self.assertTrue(result["passed"])
        self.assertEqual(result["score"], 1.0)
        self.assertEqual(result["selected_skill"], "0-diagnosing-bugs")

        failed = EVAL["grade_output"](
            case,
            "Use 0-implement; I implemented the fix.",
        )
        self.assertFalse(failed["passed"])
        self.assertLess(failed["score"], 1.0)

        explained_alternative = EVAL["grade_output"](
            case,
            "**Use:** `/0-diagnosing-bugs`\n**Why not:** `/0-implement`",
        )
        self.assertTrue(explained_alternative["passed"])
        self.assertIn(
            "forbidden_skill",
            {item["type"] for item in explained_alternative["assertions"]},
        )

        forbidden_selection = EVAL["grade_output"](
            case,
            "**Use:** `/0-implement`\nThe diagnosis skill is `/0-diagnosing-bugs`.",
        )
        self.assertFalse(forbidden_selection["passed"])
        self.assertEqual(forbidden_selection["selected_skill"], "0-implement")

    def test_fixture_materialization_rejects_escape_and_writes_inside_workspace(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory)
            EVAL["materialize_fixture"](
                {"fixture": {"src/example.py": "VALUE = 1\n"}}, workspace
            )
            self.assertEqual((workspace / "src/example.py").read_text(), "VALUE = 1\n")
            with self.assertRaisesRegex(ValueError, "escapes workspace"):
                EVAL["materialize_fixture"](
                    {"fixture": {"../outside.txt": "bad"}}, workspace
                )

    def test_summary_keeps_denominators_and_runtime_slices(self):
        records = [
            {"case_id": "a", "runtime": "codex", "score": 1.0, "passed": True},
            {"case_id": "b", "runtime": "codex", "score": 0.5, "passed": False},
            {"case_id": "a", "runtime": "claude", "score": 1.0, "passed": True},
        ]
        summary = EVAL["summarize_records"](records)
        self.assertEqual(summary["total_records"], 3)
        self.assertEqual(summary["passed_records"], 2)
        self.assertEqual(summary["by_runtime"]["codex"]["total"], 2)
        self.assertEqual(summary["by_runtime"]["claude"]["passed"], 1)

    def test_runtime_commands_keep_prompts_out_of_variadic_options(self):
        workspace = Path("/tmp/skill-eval")
        codex = EVAL["runtime_command"]("codex", workspace, "prompt", allow_writes=False)
        claude = EVAL["runtime_command"]("claude", workspace, "prompt", allow_writes=False)
        self.assertNotIn("-a", codex)
        self.assertIn('approval_policy="never"', codex)
        self.assertNotIn("--mcp-config", claude)
        self.assertIn("--skip-git-repo-check", codex)
        self.assertNotIn("--ignore-user-config", codex)
        self.assertIn("--add-dir", codex)
        self.assertIn("--add-dir", claude)
        self.assertEqual(codex[codex.index("-s") + 1], "read-only")
        self.assertIn(str(Path.home() / ".claude" / "skills"), claude)
        self.assertEqual(claude[claude.index("--permission-mode") + 1], "acceptEdits")
        self.assertNotIn("Edit,Write", claude)
        self.assertEqual(claude[-2], "--")
        self.assertEqual(codex[-1], "prompt")
        self.assertEqual(claude[-1], "prompt")

        writable = EVAL["runtime_command"]("claude", workspace, "prompt", allow_writes=True)
        self.assertEqual(writable[writable.index("--permission-mode") + 1], "acceptEdits")
        self.assertIn("Read,Glob,Grep,Bash,Edit,Write", writable)
        writable_codex = EVAL["runtime_command"](
            "codex", workspace, "prompt", allow_writes=True
        )
        self.assertEqual(writable_codex[writable_codex.index("-s") + 1], "workspace-write")

    def test_skill_set_derivation_matches_frozen_catalog_candidates(self):
        full_live = EVAL["derive_skill_set"]("full-live")
        hub_spine = EVAL["derive_skill_set"]("hub-spine")
        self.assertEqual(len(full_live), 299)
        self.assertEqual(len(hub_spine), 28)
        self.assertIn("1-coding-standards", hub_spine)
        self.assertIn("2-verify-work", hub_spine)
        self.assertTrue({path.parent.name for path in (ROOT / "hubs").glob("*/workflow.json")} <= hub_spine)
        self.assertFalse(any(name.startswith("browser-use") for name in full_live))

    def test_codex_skill_set_override_is_process_local_and_path_scoped(self):
        workspace = Path("/tmp/skill-eval")
        command = EVAL["runtime_command"](
            "codex",
            workspace,
            "prompt",
            allow_writes=False,
            skill_set="hub-spine",
            enabled_skills={"0-butler", "2-verify-work"},
            all_live_skills={"0-butler", "1-example", "2-verify-work"},
            model="gpt-5.6-sol",
            reasoning_effort="high",
            service_tier="default",
        )
        self.assertNotIn("--ignore-user-config", command)
        self.assertEqual(command[command.index("-m") + 1], "gpt-5.6-sol")
        configs = [command[index + 1] for index, value in enumerate(command) if value == "-c"]
        override = next(value for value in configs if value.startswith("skills.config="))
        self.assertIn('enabled=true', override)
        self.assertIn('enabled=false', override)
        self.assertIn("/0-butler/SKILL.md", override)
        self.assertNotIn("config.toml", " ".join(command))
        self.assertEqual(command[-1], "prompt")

    def test_disposable_codex_home_uses_only_controlled_config(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            destination = root / "destination"
            (source / "skills" / "1-example").mkdir(parents=True)
            (source / "skills" / "1-example" / "SKILL.md").write_text("example")
            (source / "auth.json").write_text('{"token":"fixture"}')
            (source / "config.toml").write_text("must_not_copy = true\n")

            workspace = root / "workspace"
            EVAL["prepare_disposable_codex_home"](
                destination, source=source, trusted_project=workspace
            )

            self.assertEqual((destination / "auth.json").read_text(), '{"token":"fixture"}')
            self.assertTrue((destination / "skills" / "1-example").is_symlink())
            self.assertEqual(
                (destination / "skills" / "1-example").resolve(),
                (source / "skills" / "1-example").resolve(),
            )
            config = (destination / "config.toml").read_text()
            self.assertIn(f'[projects."{workspace.resolve()}"]', config)
            self.assertIn('trust_level = "trusted"', config)
            self.assertNotIn("must_not_copy", config)

    def test_repetitions_and_provenance_are_stable_and_complete(self):
        cases = [self.case(id="a"), self.case(id="b")]
        plan = EVAL["build_run_plan"](cases, 3)
        self.assertEqual(len(plan), 6)
        self.assertEqual([run_id for run_id, _ in plan], [
            "rep-1", "rep-1", "rep-2", "rep-2", "rep-3", "rep-3"
        ])
        provenance = EVAL["build_provenance"](
            cases_path=ROOT / "guidelines/catalog/evals/ai-native-cases.json",
            skill_set="hub-spine",
            enabled_skills={"0-butler", "2-verify-work"},
            model="gpt-5.6-sol",
            reasoning_effort="high",
            service_tier="default",
            codex_version="codex-cli 0.test",
        )
        self.assertEqual(provenance["enabled_skill_count"], 2)
        self.assertEqual(provenance["codex_version"], "codex-cli 0.test")
        self.assertEqual(provenance["skill_set"], "hub-spine")
        for field in (
            "git_revision", "git_dirty_fingerprint", "catalog_version",
            "catalog_content_hash", "evaluation_case_hash", "enabled_skill_set_hash",
            "model", "reasoning_effort", "service_tier",
        ):
            self.assertTrue(provenance[field])

    def test_compare_requires_repeated_routing_gain_without_behavior_regression(self):
        def records(skill_set, route_counts, behavior_failure=None):
            result = []
            for repetition, route_passes in enumerate(route_counts, start=1):
                run_id = f"rep-{repetition}"
                for index in range(6):
                    passed = index < route_passes
                    result.append({
                        "skill_set": skill_set, "run_id": run_id,
                        "case_id": f"route-{index}", "category": "route",
                        "expected_skill": "1-right", "selected_skill": "1-right" if passed else "1-wrong",
                        "passed": passed, "score": float(passed), "runtime_warnings": [],
                        "usage": {"input_tokens": 100}, "latency_ms": 10, "error": None,
                        "runtime": "codex", "git_revision": "abc", "git_dirty_fingerprint": "dirty",
                        "catalog_version": "1.0.0", "catalog_content_hash": "catalog",
                        "evaluation_case_hash": "cases", "codex_version": "codex-cli test",
                        "model": "model", "reasoning_effort": "high", "service_tier": "default",
                    })
                for index in range(4):
                    passed = (run_id, index) != behavior_failure
                    result.append({
                        "skill_set": skill_set, "run_id": run_id,
                        "case_id": f"behavior-{index}", "category": "behavior",
                        "expected_skill": "1-right", "selected_skill": None,
                        "passed": passed, "score": float(passed), "runtime_warnings": [],
                        "usage": {"input_tokens": 100}, "latency_ms": 10, "error": None,
                        "runtime": "codex", "git_revision": "abc", "git_dirty_fingerprint": "dirty",
                        "catalog_version": "1.0.0", "catalog_content_hash": "catalog",
                        "evaluation_case_hash": "cases", "codex_version": "codex-cli test",
                        "model": "model", "reasoning_effort": "high", "service_tier": "default",
                    })
            return result

        comparison = EVAL["compare_result_sets"](
            records("full-live", [4, 4, 5]),
            records("hub-spine", [5, 5, 5]),
        )
        self.assertEqual(comparison["routing_gain"], 2)
        self.assertEqual(comparison["improved_repetitions"], 2)
        self.assertEqual(comparison["reduced_only_behavior_failures"], [])
        self.assertTrue(comparison["recommend_selectable_profiles"])

        regression = EVAL["compare_result_sets"](
            records("full-live", [4, 4, 5]),
            records("hub-spine", [5, 5, 5], behavior_failure=("rep-2", 1)),
        )
        self.assertFalse(regression["recommend_selectable_profiles"])

        mismatched = records("hub-spine", [5, 5, 5])
        mismatched[0]["model"] = "different-model"
        with self.assertRaisesRegex(ValueError, "matched provenance"):
            EVAL["compare_result_sets"](
                records("full-live", [4, 4, 5]), mismatched
            )

    def test_route_grading_rejects_the_wrong_non_forbidden_skill(self):
        result = EVAL["grade_output"](
            self.case(forbidden_skills=[]),
            "**Use:** `/1-code-review`",
        )
        self.assertFalse(result["passed"])
        self.assertEqual(result["selected_skill"], "1-code-review")

    def test_diagnosis_oracle_grades_semantics_not_exact_source_formatting(self):
        cases = EVAL["load_cases"](
            ROOT / "guidelines/catalog/evals/ai-native-cases.json"
        )
        case = next(item for item in cases if item["id"] == "behavior-diagnosis-only")
        values = [item["value"] for item in case["assertions"] if item["type"] == "contains"]
        self.assertEqual(values, ["n + 1"])

    def test_case_file_in_repo_is_valid_and_covers_pilots(self):
        path = ROOT / "guidelines/catalog/evals/ai-native-cases.json"
        document = json.loads(path.read_text(encoding="utf-8"))
        cases = EVAL["validate_cases"](document)
        expected = {case["expected_skill"] for case in cases}
        self.assertEqual(len(cases), 10)
        self.assertTrue({
            "0-butler", "0-skill-manager", "0-skill-creator", "0-implement",
            "0-diagnosing-bugs", "1-code-review", "2-verify-work",
        }.issubset(expected))

    def test_runtime_metrics_capture_usage_cost_model_and_context_warnings(self):
        codex = "\n".join([
            json.dumps({"type": "item.completed", "item": {
                "type": "error",
                "message": "Skill descriptions were shortened to fit the skills context budget.",
            }}),
            json.dumps({
                "type": "error",
                "message": "Selected model is at capacity. Please try a different model.",
            }),
            json.dumps({"type": "turn.completed", "usage": {
                "input_tokens": 100, "cached_input_tokens": 25, "output_tokens": 10,
            }}),
        ])
        codex_metrics = EVAL["extract_runtime_metrics"]("codex", codex)
        self.assertEqual(codex_metrics["usage"]["input_tokens"], 100)
        self.assertEqual(len(codex_metrics["warnings"]), 2)

        claude = json.dumps({
            "total_cost_usd": 0.05,
            "usage": {"input_tokens": 2, "output_tokens": 20},
            "modelUsage": {"claude-sonnet-5": {"canonicalModel": "claude-sonnet-5"}},
        })
        claude_metrics = EVAL["extract_runtime_metrics"]("claude", claude)
        self.assertEqual(claude_metrics["cost_usd"], 0.05)
        self.assertEqual(claude_metrics["model"], "claude-sonnet-5")


if __name__ == "__main__":
    unittest.main()
