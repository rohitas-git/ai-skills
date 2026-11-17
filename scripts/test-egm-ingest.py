#!/usr/bin/env python3
"""Check EGM source integrity, capability coverage, links and catalog handoffs.

Static catalog checks only: this does not execute upstream skills or model reviews.
"""
from pathlib import Path
import hashlib
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "archive/vendor/elephant-goldfish-model"
COMMIT = "0dfb5bf3eebd551d1e805c3ab16cbaa9b1c2c42a"
CAPABILITIES = {
    "egm-brainstorm", "egm-draft", "egm-review", "egm-review-loop",
    "egm-resolve", "egm-bootstrap", "egm-drift-report",
}


class EGMIngestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads((ARCHIVE / "manifest.json").read_text())
        cls.lock = json.loads((ROOT / "skills-lock.json").read_text())["skills"]["1-design-review"]
        cls.routes = {
            row["skill"]: row for row in json.loads(
                (ROOT / "skills/0-butler/references/route-index.json").read_text()
            )["skills"]
        }

    def test_source_commit_and_lock_are_consistent(self):
        self.assertEqual(self.manifest["commit"], COMMIT)
        self.assertEqual(self.lock["commit"], COMMIT)
        self.assertEqual(self.manifest["algorithm"], "sha256")
        main = (ROOT / "skills/1-design-review/SKILL.md").read_text()
        self.assertIn(COMMIT, main)
        self.assertEqual(self.lock["computedHash"], self.manifest["files"]["skills/egm-review/SKILL.md"]["sha256"])

    def test_original_files_are_contained_text_and_byte_identical(self):
        base = ARCHIVE / "upstream"
        self.assertEqual({p.relative_to(base).as_posix() for p in base.rglob("*") if p.is_file()}, set(self.manifest["files"]))
        for rel, entry in self.manifest["files"].items():
            with self.subTest(rel=rel):
                path = base / rel
                self.assertTrue(path.resolve().is_relative_to(base.resolve()))
                self.assertFalse(path.is_symlink())
                self.assertIn(path.suffix, (".md", ""))
                self.assertFalse(path.stat().st_mode & 0o111)
                data = path.read_bytes()
                data.decode("utf-8")
                self.assertEqual(len(data), entry["bytes"])
                self.assertEqual(hashlib.sha256(data).hexdigest(), entry["sha256"])

    def test_all_seven_upstream_capabilities_have_live_owners(self):
        originals = {
            Path(rel).parent.name for rel in self.manifest["files"]
            if rel.startswith("skills/") and rel.endswith("/SKILL.md")
        }
        self.assertEqual(originals, CAPABILITIES)
        self.assertEqual(set(self.lock["adaptations"]), CAPABILITIES)
        workflow = (ROOT / "skills/1-design-review/references/workflow-and-connections.md").read_text()
        for capability, destination in self.lock["adaptations"].items():
            with self.subTest(capability=capability):
                self.assertTrue((ROOT / destination).is_file())
                self.assertIn(f"`{capability}`", workflow)
                self.assertNotIn(capability, self.routes)

    def test_license_is_preserved(self):
        self.assertEqual((ROOT / "skills/1-design-review/LICENSE").read_bytes(),
                         (ARCHIVE / "upstream/LICENSE").read_bytes())

    def test_public_routes_have_distinct_jobs(self):
        cases = {
            "1-brainstorm": ("0-grilling", "EGM brainstorm"),
            "1-to-spec": ("0-implement", "EGM draft"),
            "1-design-review": ("0-review", "goldfish review"),
            "1-living-documentation-governor": ("0-improve-codebase-architecture", "EGM drift report"),
        }
        for name, (hub, trigger) in cases.items():
            with self.subTest(skill=name):
                row = self.routes[name]
                self.assertEqual(row["hub"], hub)
                self.assertIn(trigger, row["triggers"])
                for target in row["next"]:
                    self.assertIn(target, self.routes)
        self.assertIn("EGM bootstrap", self.routes["1-living-documentation-governor"]["triggers"])

    def test_design_review_is_connected_and_manual(self):
        row = self.routes["1-design-review"]
        self.assertEqual(row["role"], "pipeline")
        self.assertIn({"hub": "0-review", "role": "pipeline"}, row["memberships"])
        for source in ("1-brainstorm", "1-to-spec", "0-review"):
            self.assertIn("1-design-review", self.routes[source]["next"])
        for target in ("1-to-spec", "1-write-plan", "1-to-tickets", "0-implement"):
            self.assertIn(target, row["next"])
        self.assertIn("allow_implicit_invocation: false", (ROOT / "skills/1-design-review/agents/openai.yaml").read_text())

    def test_new_and_merged_reference_links_resolve(self):
        paths = [*sorted((ROOT / "skills/1-design-review").rglob("*.md")),
                 ROOT / "skills/1-brainstorm/references/egm-concept-review.md",
                 ROOT / "skills/1-to-spec/references/spec-format.md",
                 ROOT / "skills/1-living-documentation-governor/references/egm-contracts-and-drift.md",
                 ARCHIVE / "README.md"]
        for path in paths:
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text()):
                if target.startswith(("https://", "http://", "#")):
                    continue
                with self.subTest(source=str(path.relative_to(ROOT)), target=target):
                    self.assertTrue((path.parent / target.split("#", 1)[0]).resolve().exists())


if __name__ == "__main__":
    unittest.main()
