"""Exercise SDD helpers against disposable local Git repositories."""
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HELPERS = ROOT / "skills/1-subagent-implement/references/scripts"


class HelperTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="skill-sdd-tests-")
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.repo = self.directory / "repo"
        self.repo.mkdir()
        self.git("init", "-b", "fixture")
        self.git("config", "user.name", "Skill Fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        self.git("config", "commit.gpgsign", "false")
        self.git("config", "core.hooksPath", str(self.directory / "no-hooks"))
        (self.repo / "feature.txt").write_text("baseline\n")
        self.git("add", "feature.txt")
        self.git("commit", "-m", "test: baseline")
        self.base = self.git("rev-parse", "HEAD")

    def git(self, *args):
        return subprocess.check_output(
            ["git", *args], cwd=self.repo, text=True, stderr=subprocess.PIPE
        ).strip()

    def helper(self, name, *args, ok=True):
        result = subprocess.run(
            ["bash", str(HELPERS / name), *map(str, args)],
            cwd=self.repo, text=True, capture_output=True,
        )
        if ok:
            self.assertEqual(result.returncode, 0, result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0)
        return result

    def change(self, text, subject):
        (self.repo / "feature.txt").write_text(text)
        self.git("add", "feature.txt")
        self.git("commit", "-m", subject)
        return self.git("rev-parse", "HEAD")

    def test_all_helpers_have_valid_shell_syntax(self):
        for name in ("task-brief", "review-package", "sdd-workspace"):
            with self.subTest(helper=name):
                result = subprocess.run(
                    ["bash", "-n", str(HELPERS / name)], text=True, capture_output=True
                )
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_package_covers_multiple_commits_and_target_repository(self):
        self.change("baseline\nfirst\n", "test: first")
        head = self.change("baseline\nfirst\nsecond\n", "test: second")
        result = self.helper("review-package", self.base, head)
        artifact = Path(result.stdout.strip())
        content = artifact.read_text()
        self.assertIn(str(self.repo), content)
        self.assertIn(self.base, content)
        self.assertIn(head, content)
        self.assertIn("test: first", content)
        self.assertIn("test: second", content)
        self.assertIn("+first", content)
        self.assertIn("+second", content)
        self.assertEqual(self.git("status", "--porcelain"), "")
        self.assertEqual(artifact.stat().st_mode & 0o777, 0o600)

    def test_dirty_work_is_rejected_and_preserved(self):
        target = self.repo / "untracked.txt"
        target.write_text("do not omit me\n")
        before = self.git("status", "--porcelain")
        result = self.helper("review-package", self.base, "HEAD", ok=False)
        self.assertIn("dirty checkout", result.stderr)
        self.assertEqual(target.read_text(), "do not omit me\n")
        self.assertEqual(self.git("status", "--porcelain"), before)
        self.assertFalse((self.repo / ".superpowers").exists())

    def test_staged_changes_are_rejected_without_index_mutation(self):
        (self.repo / "feature.txt").write_text("staged\n")
        self.git("add", "feature.txt")
        before = self.git("diff", "--cached")
        self.helper("review-package", self.base, "HEAD", ok=False)
        self.assertEqual(self.git("diff", "--cached"), before)

    def test_unique_packages_and_existing_output_preserved(self):
        first = Path(self.helper("review-package", self.base, "HEAD").stdout.strip())
        second = Path(self.helper("review-package", self.base, "HEAD").stdout.strip())
        self.assertNotEqual(first, second)
        existing = self.directory / "existing.diff"
        existing.write_text("user artifact")
        self.helper("review-package", self.base, "HEAD", existing, ok=False)
        self.assertEqual(existing.read_text(), "user artifact")

    def test_invalid_commit_and_nonancestor_rejected(self):
        self.helper("review-package", "--help", "HEAD", ok=False)
        later = self.change("later\n", "test: later")
        self.helper("review-package", later, self.base, ok=False)
        self.assertFalse((self.repo / ".superpowers").exists())

    def test_task_heading_fences_and_section_boundary(self):
        plan = self.directory / "plan.md"
        plan.write_text(
            "# Plan\n~~~text\n## Task 2: fake\n~~~\n"
            "## Task 1: first\nignore\n## Task 2: real\nkeep\n"
            "```md\n## Task 3: fenced\n```\n"
            "### Details\nkeep detail\n## Verification\nnot part of task\n"
        )
        result = self.helper("task-brief", plan, "2")
        content = Path(result.stdout.strip()).read_text()
        self.assertTrue(content.startswith("## Task 2: real\n"))
        self.assertIn("## Task 3: fenced", content)
        self.assertIn("keep detail", content)
        self.assertNotIn("not part of task", content)
        self.assertNotIn("fake", content)

    def test_brief_unique_and_missing_task_has_no_output(self):
        plan = self.directory / "plan.md"
        plan.write_text("# Task 1: one\nfirst\n")
        first = Path(self.helper("task-brief", plan, "1").stdout.strip())
        plan.write_text("# Task 1: one\nrevised\n")
        second = Path(self.helper("task-brief", plan, "1").stdout.strip())
        self.assertNotEqual(first, second)
        self.assertIn("first", first.read_text())
        self.assertIn("revised", second.read_text())
        out = self.directory / "missing.md"
        self.helper("task-brief", plan, "9", out, ok=False)
        self.assertFalse(out.exists())
        self.helper("task-brief", plan, "../escape", out, ok=False)
        self.assertFalse(out.exists())
        self.helper("task-brief", plan, "1", first, ok=False)
        self.assertIn("first", first.read_text())

    def test_workspace_preserves_existing_ignore_rules(self):
        workspace = self.repo / ".superpowers/sdd"
        workspace.mkdir(parents=True)
        ignore = workspace / ".gitignore"
        original = "# user rule\n*\n"
        ignore.write_text(original)
        result = self.helper("sdd-workspace")
        self.assertEqual(Path(result.stdout.strip()), workspace.resolve())
        self.assertEqual(ignore.read_text(), original)
        ignore.write_text("# not ignored\n")
        self.helper("sdd-workspace", ok=False)
        self.assertEqual(ignore.read_text(), "# not ignored\n")

    def test_workspace_refuses_symlink_and_tracked_artifacts(self):
        other = self.directory / "outside"
        other.mkdir()
        (self.repo / ".superpowers").symlink_to(other, target_is_directory=True)
        self.helper("sdd-workspace", ok=False)
        self.assertEqual(list(other.iterdir()), [])
        (self.repo / ".superpowers").unlink()
        workspace = self.repo / ".superpowers/sdd"
        workspace.mkdir(parents=True)
        tracked = workspace / "notes.md"
        tracked.write_text("tracked notes")
        self.git("add", ".superpowers/sdd/notes.md")
        self.helper("sdd-workspace", ok=False)
        self.assertEqual(tracked.read_text(), "tracked notes")
        self.assertFalse((workspace / ".gitignore").exists())

    def test_actual_artifact_ignore_exceptions_are_respected(self):
        workspace = self.repo / ".superpowers/sdd"
        workspace.mkdir(parents=True)
        ignore = workspace / ".gitignore"
        ignore.write_text("*\n!review.*\n!task-*-brief.*\n")
        self.helper("review-package", self.base, "HEAD", ok=False)
        plan = self.directory / "plan.md"
        plan.write_text("# Task 1: example\nwork\n")
        self.helper("task-brief", plan, "1", ok=False)
        self.assertEqual([p.name for p in workspace.iterdir()], [".gitignore"])
        self.assertEqual(ignore.read_text(), "*\n!review.*\n!task-*-brief.*\n")


if __name__ == "__main__":
    unittest.main()
