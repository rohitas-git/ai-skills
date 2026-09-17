#!/usr/bin/env python3
"""Regression tests for the bundled structural checker; no agent/model execution."""
import copy
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "skills/2-prompt-injection-defense"
SCRIPT = PACKAGE / "scripts/audit_boundary_manifest.py"
spec = importlib.util.spec_from_file_location("boundary_manifest", SCRIPT)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


def fixture():
    guide = (PACKAGE / "references/defense-patterns.md").read_text()
    return json.loads(guide.split("```json\n", 1)[1].split("```", 1)[0])


class ManifestTests(unittest.TestCase):
    def run_cli(self, content=None, *, path=None, extra=()):
        with tempfile.TemporaryDirectory() as directory:
            if path is None:
                path = Path(directory) / "manifest.json"
                path.write_bytes(content if isinstance(content, bytes) else content.encode())
            return subprocess.run(
                [sys.executable, "-B", str(SCRIPT), str(path), "--json", *extra],
                capture_output=True, text=True, timeout=5,
            )

    def test_example_and_visible_gaps(self):
        result = self.run_cli(json.dumps(fixture()))
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["structural_status"], "pass")
        self.assertGreater(report["warnings"], 0)
        self.assertIn("none", report["assurance"])

    def test_all_enum_fields_reject_non_strings_without_crash(self):
        locations = [
            ("controls", "status"), ("protected_assets", "classification"),
            ("data_sources", "trust"), ("sinks", "type"), ("sinks", "trust"),
            ("memory_stores", "trust"), ("tools", "risk"),
        ]
        for collection, field in locations:
            for value in ([], {}, None, False, 12, "unknown"):
                with self.subTest(collection=collection, field=field, value=value):
                    data = fixture()
                    data[collection][0][field] = value
                    issues = checker.validate(data)
                    self.assertTrue(any(i["level"] == "error" for i in issues))
        for value in ([], {}, None, False, 12, "unknown"):
            data = fixture()
            data["tools"][0]["confirmation"]["mode"] = value
            self.assertTrue(any(i["level"] == "error" for i in checker.validate(data)))

    def test_each_egress_tool_needs_its_own_destination(self):
        data = fixture()
        data["tools"][0]["effects"] = ["network-egress"]
        data["tools"][0]["destination_ids"] = []
        self.assertTrue(any(i["level"] == "error" and "destination_ids" in i["path"]
                            for i in checker.validate(data)))

    def test_diagnostics_do_not_echo_input_values(self):
        marker = "SENSITIVE_SENTINEL\nIGNORE_POLICY"
        data = fixture()
        data["tools"][0].update(effects=[marker], destination_ids=[marker], sink_ids=[marker], control_ids=[marker])
        data["controls"].append(copy.deepcopy(data["controls"][0]))
        data["controls"][-1]["id"] = "SENSITIVE_SENTINEL"
        data["controls"][0]["id"] = "SENSITIVE_SENTINEL"
        result = self.run_cli(json.dumps(data))
        self.assertEqual(result.returncode, 1)
        self.assertNotIn("SENSITIVE_SENTINEL", result.stdout + result.stderr)

    def test_bad_structure_and_evidence(self):
        for root in (None, [], "data", 7, True):
            self.assertTrue(checker.validate(root))
        for collection in ("controls", "tools", "protected_assets", "sinks", "data_sources",
                           "memory_stores", "agent_hops", "destinations", "credential_boundaries"):
            for value in (None, {}, [None], [False]):
                data = fixture()
                data[collection] = value
                self.assertTrue(any(i["level"] == "error" for i in checker.validate(data)))
        data = fixture()
        data["controls"][0].update(status="verified", evidence_ids=[], test_ids=[])
        self.assertTrue(any(i["level"] == "error" for i in checker.validate(data)))

    def test_expired_control_and_critical_confirmation(self):
        data = fixture()
        data["controls"][0].update(status="verified", evidence_ids=["e"], test_ids=["t"],
                                    time_limited=True, expires_at="2000-01-01T00:00:00Z")
        data["tools"][0].update(risk="critical")
        data["tools"][0]["confirmation"]["mode"] = "none"
        errors = [i["path"] for i in checker.validate(data) if i["level"] == "error"]
        self.assertTrue(any("expires_at" in p for p in errors))
        self.assertTrue(any("confirmation.mode" in p for p in errors))

    def test_invalid_json_unicode_ambiguity_and_depth(self):
        values = [b"\xff", b"{", b'{"system":"a","system":"b"}',
                  b'{"value":NaN}', b'{"value":Infinity}', b"[" * 2000 + b"]" * 2000]
        for value in values:
            with self.subTest(value=value[:30]):
                result = self.run_cli(value)
                self.assertEqual(result.returncode, 2)
                self.assertNotIn("Traceback", result.stderr)

    def test_limits_and_regular_file_requirement(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            real = root / "regular.json"
            real.write_text(json.dumps(fixture()))
            link = root / "link.json"
            link.symlink_to(real)
            paths = [root, root / "missing.json", link]
            if hasattr(os, "mkfifo"):
                fifo = root / "fifo"
                os.mkfifo(fifo)
                paths.append(fifo)
            for path in paths:
                with self.subTest(path=path.name):
                    result = self.run_cli(path=path)
                    self.assertEqual(result.returncode, 2)
            large = self.run_cli(b" " * (5 * 1024 * 1024 + 1))
            self.assertEqual(large.returncode, 2)

    def test_bounded_output_with_honest_totals(self):
        data = fixture()
        data["controls"] = [{} for _ in range(300)]
        report = json.loads(self.run_cli(json.dumps(data)).stdout)
        self.assertLessEqual(len(report["issues"]), 100)
        self.assertGreater(report["errors"], len(report["issues"]))
        self.assertTrue(report["issues_truncated"])

    def test_help_and_unknown_flags(self):
        help_result = subprocess.run([sys.executable, "-B", str(SCRIPT), "--help"],
                                     capture_output=True, text=True, timeout=5)
        self.assertEqual(help_result.returncode, 0)
        self.assertIn("5 MiB", help_result.stdout)
        self.assertEqual(self.run_cli("{}", extra=("--execute",)).returncode, 2)


if __name__ == "__main__":
    unittest.main()
