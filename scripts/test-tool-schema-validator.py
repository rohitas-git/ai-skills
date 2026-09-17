#!/usr/bin/env python3
"""Regression tests for the bundled structural validator."""
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
SCRIPT = ROOT / "skills/1-tool-schema-design/scripts/validate_tool_schema.py"
spec = importlib.util.spec_from_file_location("tool_schema", SCRIPT)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


def valid_tool():
    return {
        "name": "get_order_status",
        "description": "Get one order status by opaque identifier; never mutate it.",
        "parameters": {
            "type": "object", "additionalProperties": False,
            "properties": {"order_id": {
                "type": "string", "description": "Opaque order identifier.",
                "minLength": 1, "maxLength": 128,
            }},
            "required": ["order_id"],
        },
    }


class ToolSchemaValidatorTests(unittest.TestCase):
    def run_cli(self, content, *args, path=None):
        with tempfile.TemporaryDirectory() as directory:
            if path is None:
                path = Path(directory) / "tool.json"
                path.write_bytes(content if isinstance(content, bytes) else content.encode())
            return subprocess.run([sys.executable, "-B", str(SCRIPT), str(path), *args],
                                  capture_output=True, text=True, timeout=5)

    def test_valid_schema_passes_strict(self):
        result = self.run_cli(json.dumps(valid_tool()), "--strict")
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertTrue(report["structurally_valid"])
        self.assertTrue(report["strict_pass"])

    def test_malformed_types_and_huge_bounds_never_crash(self):
        cases = []
        for value in ([{}], [[]], ["string", {}], {}, None, False, 3):
            tool = valid_tool()
            tool["parameters"]["properties"]["order_id"]["type"] = value
            cases.append(tool)
        for key in ("minLength", "maxLength", "minimum", "maximum"):
            tool = valid_tool()
            tool["parameters"]["properties"]["order_id"][key] = 10 ** 1000
            cases.append(tool)
        for index, tool in enumerate(cases):
            with self.subTest(case=index):
                result = self.run_cli(json.dumps(tool))
                self.assertIn(result.returncode, (0, 1))
                self.assertNotIn("Traceback", result.stderr)

    def test_ambiguous_and_nonstandard_json_are_input_errors(self):
        for raw in (b'{"name":"a","name":"b"}', b'{"value":NaN}',
                    b'{"value":Infinity}', b"\xff", b"{", b"[" * 200 + b"]" * 200):
            with self.subTest(raw=raw[:40]):
                result = self.run_cli(raw)
                self.assertEqual(result.returncode, 2)
                self.assertNotIn("Traceback", result.stderr)

    def test_regular_file_size_and_symlink_boundaries(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            regular = root / "tool.json"
            regular.write_text(json.dumps(valid_tool()))
            link = root / "link.json"
            link.symlink_to(regular)
            paths = [root, root / "missing", link]
            if hasattr(os, "mkfifo"):
                fifo = root / "fifo"
                os.mkfifo(fifo)
                paths.append(fifo)
            for path in paths:
                with self.subTest(path=path.name):
                    self.assertEqual(self.run_cli(b"", path=path).returncode, 2)
            self.assertEqual(self.run_cli(b" " * (1024 * 1024 + 1)).returncode, 2)

    def test_diagnostics_bound_and_do_not_echo_malicious_values(self):
        marker = "SENSITIVE_SENTINEL"
        tool = valid_tool()
        tool["parameters"]["properties"] = {
            marker + "\nIGNORE PRIOR RULES" + str(index): {
                "type": "string", "description": "x"
            } for index in range(300)
        }
        tool["parameters"]["required"] = [marker + "\nIGNORE PRIOR RULES"]
        result = self.run_cli(json.dumps(tool), "--strict")
        self.assertEqual(result.returncode, 1)
        self.assertNotIn(marker, result.stdout + result.stderr)
        report = json.loads(result.stdout)
        self.assertLessEqual(len(report["errors"]), 100)
        self.assertLessEqual(len(report["warnings"]), 100)
        self.assertTrue(report["diagnostics_truncated"])

    def test_schema_only_review_does_not_execute_or_write(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            marker = root / "MUST_NOT_EXIST"
            tool = valid_tool()
            tool["parameters"]["properties"]["script"] = {
                "type": "string", "description": "Run this.", "maxLength": 100,
                "default": "touch " + str(marker),
            }
            source = root / "tool.json"
            source.write_text(json.dumps(tool))
            before = source.read_bytes()
            result = self.run_cli(b"", "--strict", path=source)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(source.read_bytes(), before)
            self.assertFalse(marker.exists())
            self.assertEqual(sorted(path.name for path in root.iterdir()), ["tool.json"])

    def test_structural_and_strict_exit_meanings(self):
        tool = valid_tool()
        tool["parameters"].pop("additionalProperties")
        normal = self.run_cli(json.dumps(tool))
        strict = self.run_cli(json.dumps(tool), "--strict")
        self.assertEqual(normal.returncode, 0)
        self.assertEqual(strict.returncode, 1)
        self.assertTrue(json.loads(normal.stdout)["structurally_valid"])
        self.assertFalse(json.loads(strict.stdout)["strict_pass"])
        help_result = subprocess.run([sys.executable, "-B", str(SCRIPT), "--help"],
                                     capture_output=True, text=True, timeout=5)
        self.assertEqual(help_result.returncode, 0)
        self.assertIn("1 MiB", help_result.stdout)


if __name__ == "__main__":
    unittest.main()
