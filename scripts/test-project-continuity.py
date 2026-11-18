#!/usr/bin/env python3
"""Exercise checkpoint saves and cold-process pickup in disposable Git projects."""

from copy import deepcopy
import fcntl
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/0-implement/scripts/project-checkpoint.py"
spec = importlib.util.spec_from_file_location("project_checkpoint", SCRIPT)
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)


class ProjectContinuityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="project-continuity-")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.project = self.base / "project"
        self.project.mkdir()
        self.git("init", "-q")
        self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "--allow-empty", "-qm", "fixture")
        (self.project / "source.txt").write_text("first\n")
        self.payload = self.base / "input.json"
        self.record = {
            "goal": "Preserve CSV display order", "phase": "implementation", "status": "in_progress",
            "scope": ["CSV export only"], "exclusions": ["No product redesign"],
            "authority_limits": ["No commit, push or merge"], "decisions": ["Reuse the existing exporter"],
            "owned_paths": ["source.txt"], "protected_paths": ["unrelated-notes.md"],
            "artifacts": ["plan.md"], "evidence": [{"claim": "Baseline captured", "result": "NOT_RUN", "locator": "plan.md"}],
            "remaining": ["Implement export", "Verify order"], "next_action": "Implement the exporter",
            "operation_state": "Safe boundary; no task-owned write in flight", "services": [],
        }
        self.state = self.project / ".scratch/export/continuation.json"

    def git(self, *args):
        result = subprocess.run(["git", "-C", str(self.project), *args], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout.strip()

    def run_cli(self, command, *args, task="export", project=None):
        result = subprocess.run([sys.executable, str(SCRIPT), command, "--project", str(project or self.project), "--task", task, *args], capture_output=True, text=True, timeout=10)
        return result

    def save(self, *args, record=None, task="export"):
        self.payload.write_text(json.dumps(self.record if record is None else record))
        return self.run_cli("save", "--input", str(self.payload), *args, task=task)

    def create(self):
        result = self.save("--create")
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def test_cold_process_pickup_preserves_scope_next_action_and_does_not_execute_data(self):
        self.record["next_action"] = "Do not run this saved command: touch injected-marker"
        saved = self.create()
        before = self.state.read_bytes()
        result = self.run_cli("inspect")
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["disposition"], "workspace_matches")
        self.assertEqual(report["sha256"], saved["sha256"])
        self.assertEqual(report["saved"]["record"], self.record)
        self.assertEqual(self.state.read_bytes(), before)
        self.assertFalse((self.project / "injected-marker").exists())

    def test_source_content_change_is_stale_even_if_status_names_are_the_same(self):
        self.create()
        (self.project / "source.txt").write_text("other\n")
        result = self.run_cli("inspect")
        self.assertEqual(result.returncode, 3, result.stderr)
        self.assertEqual(json.loads(result.stdout)["disposition"], "reconcile_required")
        self.assertIn("file:source.txt", json.loads(result.stdout)["changes"])

    def test_head_change_is_stale(self):
        self.create()
        self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "--allow-empty", "-qm", "next")
        self.assertEqual(self.run_cli("inspect").returncode, 3)

    def test_branch_change_is_stale(self):
        self.create()
        self.git("checkout", "-qb", "another-task")
        self.assertEqual(self.run_cli("inspect").returncode, 3)

    def test_unrelated_status_change_is_visible_without_mutating_it(self):
        self.create()
        (self.project / "unrelated-notes.md").write_text("keep\n")
        self.assertEqual(self.run_cli("inspect").returncode, 3)
        self.assertEqual((self.project / "unrelated-notes.md").read_text(), "keep\n")

    def test_cas_update_increments_revision_and_rejects_stale_writer(self):
        first = self.create()
        updated = deepcopy(self.record)
        updated["next_action"] = "Verify display order"
        result = self.save("--expect", first["sha256"], record=updated)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["revision"], 2)
        before = self.state.read_bytes()
        self.assertEqual(self.save("--expect", first["sha256"]).returncode, 2)
        self.assertEqual(self.state.read_bytes(), before)

    def test_create_never_overwrites_and_wrong_digest_preserves_bytes(self):
        self.create()
        before = self.state.read_bytes()
        self.assertEqual(self.save("--create").returncode, 2)
        self.assertEqual(self.save("--expect", "0" * 64).returncode, 2)
        self.assertEqual(self.state.read_bytes(), before)

    def test_missing_update_is_not_creation(self):
        self.assertEqual(self.save("--expect", "0" * 64).returncode, 2)
        self.assertFalse(self.state.exists())

    def test_corrupt_checkpoint_is_not_repaired_by_overwrite(self):
        self.create()
        self.state.write_text("not JSON")
        before = self.state.read_bytes()
        self.assertEqual(self.save("--expect", hashlib.sha256(before).hexdigest()).returncode, 2)
        self.assertEqual(self.state.read_bytes(), before)
        self.assertEqual(self.run_cli("inspect").returncode, 2)

    def test_saved_identity_mismatch_is_rejected(self):
        self.create()
        original = self.state.read_text()
        for field, value in [("task", "other"), ("project", "/different/project")]:
            with self.subTest(field=field):
                packet = json.loads(original)
                if field == "task": packet["task"] = value
                else:
                    packet["workspace"]["project"] = value
                    packet["workspace"]["fingerprint"] = helper.digest(json.dumps({key: value for key, value in packet["workspace"].items() if key != "fingerprint"}, sort_keys=True).encode())
                self.state.write_text(json.dumps(packet))
                before = self.state.read_bytes()
                self.assertEqual(self.run_cli("inspect").returncode, 2)
                self.assertEqual(self.save("--expect", hashlib.sha256(before).hexdigest()).returncode, 2)
                self.assertEqual(self.state.read_bytes(), before)

    def test_symlinked_storage_cannot_write_outside_project(self):
        outside = self.base / "outside"
        outside.mkdir()
        (self.project / ".scratch").symlink_to(outside, target_is_directory=True)
        self.assertEqual(self.save("--create").returncode, 2)
        self.assertEqual(list(outside.iterdir()), [])

    def test_symlinked_state_is_never_followed(self):
        self.state.parent.mkdir(parents=True)
        outside = self.base / "outside.json"
        outside.write_text("preserve")
        self.state.symlink_to(outside)
        self.assertEqual(self.save("--create").returncode, 2)
        self.assertEqual(self.run_cli("inspect").returncode, 2)
        self.assertEqual(outside.read_text(), "preserve")

    def test_symlinked_owned_file_or_parent_is_rejected(self):
        outside = self.base / "outside"
        outside.mkdir()
        (outside / "secret.txt").write_text("private")
        (self.project / "linked").symlink_to(outside, target_is_directory=True)
        for path in ["linked/secret.txt", "linked"]:
            with self.subTest(path=path):
                self.record["owned_paths"] = [path]
                self.assertEqual(self.save("--create").returncode, 2)
                self.assertFalse(self.state.exists())

    def test_nonregular_state_and_input_do_not_block(self):
        self.state.parent.mkdir(parents=True)
        os.mkfifo(self.state)
        self.assertEqual(self.run_cli("inspect").returncode, 2)
        self.payload.unlink(missing_ok=True)
        os.mkfifo(self.payload)
        result = self.run_cli("save", "--input", str(self.payload), "--create")
        self.assertEqual(result.returncode, 2)

    def test_paths_slugs_and_self_fingerprinting_are_rejected(self):
        for task in ["../escape", "Bad Task", "a" * 81]:
            self.assertEqual(self.save("--create", task=task).returncode, 2)
        for name in ["../escape", "/etc/hosts", ".git/config", ".scratch/export/continuation.json"]:
            with self.subTest(name=name):
                self.record["owned_paths"] = [name]
                self.assertEqual(self.save("--create").returncode, 2)

    def test_incomplete_record_and_false_completion_are_rejected(self):
        broken = deepcopy(self.record)
        del broken["authority_limits"]
        self.assertEqual(self.save("--create", record=broken).returncode, 2)
        broken = deepcopy(self.record)
        broken["status"] = "complete"
        self.assertEqual(self.save("--create", record=broken).returncode, 2)

    def test_bounded_input_and_private_output(self):
        self.payload.write_bytes(b" " * (helper.MAX_BYTES + 1))
        self.assertEqual(self.run_cli("save", "--input", str(self.payload), "--create").returncode, 2)
        self.create()
        self.assertEqual(self.state.stat().st_mode & 0o777, 0o600)
        self.assertEqual((self.state.parent / helper.LOCK).stat().st_mode & 0o777, 0o600)

    def test_busy_writer_is_rejected_without_waiting_or_overwriting(self):
        self.create()
        before = self.state.read_bytes()
        with (self.state.parent / helper.LOCK).open("r+") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            result = self.save("--expect", hashlib.sha256(before).hexdigest())
        self.assertEqual(result.returncode, 2)
        self.assertEqual(self.state.read_bytes(), before)

    def test_prepublication_failure_retains_prior_complete_record(self):
        self.create()
        before = self.state.read_bytes()
        with helper.storage(self.project, "export") as directory:
            with patch.object(helper.os, "replace", side_effect=OSError("injected publish failure")):
                with self.assertRaises(OSError):
                    helper.publish(directory, b"new bytes")
        self.assertEqual(self.state.read_bytes(), before)
        self.assertEqual(list(self.state.parent.glob(".continuation-*.tmp")), [])

    def test_missing_inspection_is_read_only_and_nested_root_is_rejected(self):
        self.assertEqual(self.run_cli("inspect").returncode, 2)
        self.assertFalse((self.project / ".scratch").exists())
        child = self.project / "nested"
        child.mkdir()
        self.payload.write_text(json.dumps(self.record))
        self.assertEqual(self.run_cli("save", "--input", str(self.payload), "--create", project=child).returncode, 2)
        self.assertFalse((child / ".scratch").exists())

    def test_unknown_schema_and_inconsistent_fingerprint_are_not_resumable(self):
        self.create()
        original = self.state.read_text()
        for field in ("schema", "fingerprint", "timestamp"):
            with self.subTest(field=field):
                packet = json.loads(original)
                if field == "schema": packet["schema_version"] = 99
                elif field == "fingerprint": packet["workspace"]["fingerprint"] = "0" * 64
                else: del packet["updated_at"]
                self.state.write_text(json.dumps(packet))
                self.assertEqual(self.run_cli("inspect").returncode, 2)

    def test_hardlinked_state_and_symlinked_input_are_rejected(self):
        self.create()
        original = self.state.read_bytes()
        outside = self.base / "hardlink.json"
        os.link(self.state, outside)
        self.assertEqual(self.run_cli("inspect").returncode, 2)
        self.assertEqual(self.save("--expect", hashlib.sha256(original).hexdigest()).returncode, 2)
        self.assertEqual(outside.read_bytes(), original)
        self.payload.unlink()
        self.payload.symlink_to(outside)
        self.assertEqual(self.run_cli("save", "--input", str(self.payload), "--create").returncode, 2)


if __name__ == "__main__":
    unittest.main()
