"""Exercise the audit report checker with synthetic files, never real findings."""
import copy
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "skills/1-security-auditor/scripts/validate-findings.js"
NODE = shutil.which("node")


def report():
    return {
        "audit_metadata": {
            "project": "fixture", "timestamp": "2026-09-11T00:00:00Z",
            "scope": "synthetic", "phases_completed": ["recon", "validation"],
            "candidate": "fixture revision, no real repository",
        },
        "findings": [{
            "id": "SEC-001", "title": "synthetic finding", "severity": "High",
            "category": "security", "location": {"paths": ["fixture.js:1"]},
            "scenario": "synthetic scenario", "impact": "synthetic impact",
            "evidence": "synthetic evidence", "confidence": "high", "status": "confirmed",
        }],
        "summary": {"total_confirmed": 1, "by_severity": {"High": 1},
                    "by_category": {"security": 1}},
    }


@unittest.skipUnless(NODE, "Node required to test the existing Node helper")
class FindingsValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.file = self.directory / "findings.json"

    def run_checker(self, args):
        return subprocess.run([NODE, str(CHECKER), *map(str, args)],
                              cwd=self.directory, text=True, capture_output=True, timeout=5)

    def check(self, value, expected=1):
        self.file.write_text(json.dumps(value), encoding="utf-8")
        before = self.file.read_bytes()
        result = self.run_checker([self.file])
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        self.assertEqual(before, self.file.read_bytes())
        self.assertNotIn("TypeError", result.stderr)
        self.assertNotIn(" at Object.", result.stderr)
        return result

    def test_valid_report_and_empty_confirmed_set(self):
        self.check(report(), 0)
        value = report()
        value["findings"] = []
        value["summary"] = {"total_confirmed": 0, "by_severity": {"High": 0}}
        self.check(value, 0)

    def test_primitives_and_null_never_crash(self):
        for value in [None, 5, False, "not an object", [], {}]:
            with self.subTest(root=value):
                self.check(value)
        for value in [None, 0, [], "invalid"]:
            for field in ["audit_metadata", "findings"]:
                data = report()
                data[field] = value
                with self.subTest(field=field, value=value):
                    self.check(data)
        for value in [None, 7, [], "bad"]:
            data = report()
            data["findings"] = [value]
            self.check(data)

    def test_required_fields_types_and_falsy_enums(self):
        for field in list(report()["findings"][0]):
            for value in [None, False, 0, ""]:
                data = report()
                data["findings"][0][field] = value
                with self.subTest(field=field, value=value):
                    self.check(data)
            data = report()
            del data["findings"][0][field]
            self.check(data)
        for field, value in [("project", 1), ("timestamp", False),
                             ("phases_completed", "recon"), ("phases_completed", [1]),
                             ("prior_findings_loaded", "yes")]:
            data = report()
            data["audit_metadata"][field] = value
            self.check(data)

    def test_location_array_members_and_empty_paths(self):
        for value in [{}, {"paths": []}, {"paths": [""]}, {"paths": [None]},
                      {"paths": "fixture.js"}, {"paths": ["a"], "functions": [5]}]:
            data = report()
            data["findings"][0]["location"] = value
            self.check(data)

    def test_unique_ids_and_summary_consistency(self):
        data = report()
        data["findings"].append(copy.deepcopy(data["findings"][0]))
        data["summary"] = {"total_confirmed": 2}
        self.check(data)
        for summary in [{"total_confirmed": 0}, {"total_confirmed": -1},
                        {"by_severity": {"High": 2}}, {"by_category": {"security": 0}},
                        {"by_category": {"security": "1"}}, {"total_confirmed": 1.5}]:
            data = report()
            data["summary"] = summary
            self.check(data)

    def test_rejected_findings_not_counted_as_confirmed(self):
        data = report()
        data["findings"][0]["status"] = "rejected"
        self.check(data)
        data["summary"] = {"total_confirmed": 0, "by_severity": {"High": 0}}
        self.check(data, 0)

    def test_metadata_and_causality_extensions(self):
        data = report()
        data["findings"][0]["change_relation"] = "worsened"
        data["findings"][0]["is_new"] = False
        self.check(data, 0)
        data["findings"][0]["change_relation"] = "invented"
        self.check(data)

    def test_format_annotation_is_not_claimed_as_verified(self):
        data = report()
        data["audit_metadata"]["timestamp"] = "not a valid timestamp"
        result = self.check(data, 0)
        self.assertIn("date-time format are not verified", result.stdout)

    def test_unavailable_and_nonregular_inputs(self):
        self.assertEqual(self.run_checker([self.directory / "missing"]).returncode, 2)
        self.assertEqual(self.run_checker([self.directory]).returncode, 2)
        self.file.write_text(json.dumps(report()), encoding="utf-8")
        link = self.directory / "linked.json"
        link.symlink_to(self.file)
        self.assertEqual(self.run_checker([link]).returncode, 2)
        if hasattr(os, "mkfifo"):
            fifo = self.directory / "pipe"
            os.mkfifo(fifo)
            self.assertEqual(self.run_checker([fifo]).returncode, 2)
        self.file.write_bytes(b" " * (5 * 1024 * 1024 + 1))
        self.assertEqual(self.run_checker([self.file]).returncode, 2)

    def test_explicit_input_and_help(self):
        self.file.write_text(json.dumps(report()), encoding="utf-8")
        self.assertEqual(self.run_checker([]).returncode, 2)
        self.assertEqual(self.run_checker([self.file, self.file]).returncode, 2)
        self.assertEqual(self.run_checker(["--help"]).returncode, 0)

    def test_unsupported_schema_keyword_fails_closed(self):
        # Isolated copy proves schema evolution cannot silently weaken validation.
        scripts = self.directory / "skill/scripts"
        references = self.directory / "skill/references"
        scripts.mkdir(parents=True)
        references.mkdir()
        copied_checker = scripts / CHECKER.name
        shutil.copyfile(CHECKER, copied_checker)
        schema_path = CHECKER.parent.parent / "references/findings-schema.json"
        schema = json.loads(schema_path.read_text())
        schema["maxProperties"] = 0
        (references / schema_path.name).write_text(json.dumps(schema), encoding="utf-8")
        self.file.write_text(json.dumps(report()), encoding="utf-8")
        result = subprocess.run([NODE, str(copied_checker), str(self.file)],
                                text=True, capture_output=True, timeout=5)
        self.assertEqual(result.returncode, 2)
        self.assertIn("validation unavailable", result.stderr)

    def test_private_values_and_unknown_keys_not_echoed(self):
        secret = "SYNTHETIC_PRIVATE_MARKER"
        data = report()
        data["findings"][0]["severity"] = secret
        data["summary"]["by_category"] = {secret: secret}
        result = self.check(data)
        self.assertNotIn(secret, result.stdout + result.stderr)
        self.file.write_text('{"key":"' + secret + '" INVALID}', encoding="utf-8")
        result = self.run_checker([self.file])
        self.assertEqual(result.returncode, 1)
        self.assertNotIn(secret, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
