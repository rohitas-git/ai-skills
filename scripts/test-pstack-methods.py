#!/usr/bin/env python3
"""Executable source-integrity negative controls and TypeScript contract checks."""

from __future__ import annotations

import importlib.machinery
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
loader = importlib.machinery.SourceFileLoader("pstack_methods", str(ROOT / "scripts/check-pstack-methods"))
spec = importlib.util.spec_from_loader(loader.name, loader)
checker = importlib.util.module_from_spec(spec)
loader.exec_module(checker)


class LedgerChecks(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="pstack-method-check-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.data = json.loads((ROOT / checker.MANIFEST).read_text())
        paths = {checker.MANIFEST, self.data["skill_review"]}
        for item in self.data["entries"] + self.data["supporting_sources"]:
            paths.add(item["archive_path"])
        for item in self.data["entries"]:
            paths.update(item["targets"])
            paths.update(f"skills/{owner}/SKILL.md" for owner in item["owners"])
        paths.update(item["path"] for item in self.data["adopted_files"])
        for relative in paths:
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)

    def write_manifest(self):
        (self.root / checker.MANIFEST).write_text(json.dumps(self.data))

    def test_complete_snapshot(self):
        methods, _, skills = checker.check(self.root)
        self.assertEqual((methods, skills), (80, 61))

    def test_missing_or_duplicate_skill_review_row_is_rejected(self):
        report = self.root / self.data["skill_review"]
        original = report.read_text()
        row = next(line for line in original.splitlines() if line.startswith("| [setup-benny]"))
        for replacement in ("", f"{row}\n{row}"):
            with self.subTest(replacement=replacement), self.assertRaisesRegex(ValueError, "skill-by-skill review row"):
                report.write_text(original.replace(row, replacement))
                checker.check(self.root)

    def test_missing_method_is_not_complete(self):
        self.data["entries"].pop()
        self.write_manifest()
        with self.assertRaisesRegex(ValueError, "missing or extra"):
            checker.check(self.root)

    def test_duplicate_identity_is_rejected(self):
        self.data["entries"][0]["id"] = self.data["entries"][1]["id"]
        self.write_manifest()
        with self.assertRaisesRegex(ValueError, "duplicate method"):
            checker.check(self.root)

    def test_source_drift_is_rejected(self):
        (self.root / self.data["entries"][0]["archive_path"]).write_text("changed source")
        with self.assertRaisesRegex(ValueError, "source archive drift"):
            checker.check(self.root)

    def test_target_drift_is_rejected(self):
        (self.root / self.data["adopted_files"][0]["path"]).write_text("changed adoption")
        with self.assertRaisesRegex(ValueError, "adopted-file drift"):
            checker.check(self.root)

    def test_missing_owner_is_rejected(self):
        self.data["entries"][0]["owners"] = ["1-missing-owner"]
        self.write_manifest()
        with self.assertRaisesRegex(ValueError, "missing or nonlocal"):
            checker.check(self.root)

    def test_nonlocal_path_is_rejected(self):
        for relative in ["../private", "/etc/hosts"]:
            with self.subTest(relative=relative), self.assertRaisesRegex(ValueError, "unsafe relative"):
                checker.local_file(self.root, relative)


class TypeScriptContracts(unittest.TestCase):
    def test_compile_rejections_and_runtime_validation(self):
        node = os.environ.get("PSTACK_TEST_NODE") or shutil.which("node")
        compiler = ROOT / "skills/1-pr-repair/scripts/node_modules/typescript/bin/tsc"
        bun = shutil.which("bun")
        if not node or not compiler.is_file() or not bun:
            self.skipTest("existing Node, TypeScript and Bun required; no dependency install is performed")
        with tempfile.TemporaryDirectory(prefix="pstack-ts-contract-") as directory:
            work = Path(directory)
            shutil.copyfile(ROOT / "skills/1-typescript-best-practices/examples/contracts.ts", work / "contracts.ts")
            (work / "typechecks.ts").write_text('''import {parseDuration, endAt, first, describe, type Load} from "./contracts";
endAt(1, parseDuration(3));
first(["a"]);
// @ts-expect-error an empty collection is not a nonempty tuple
first([]);
// @ts-expect-error a raw number has not passed the duration boundary
endAt(1, -3);
// @ts-expect-error ready states require a value
const missing: Load<string> = {kind: "ready"};
// @ts-expect-error arbitrary indexed access may be undefined even on a nonempty tuple
const arbitrary: string = (["a"] as readonly [string, ...string[]])[Math.random()];
describe({kind: "ready", value: "yes"});
// A predicate annotation is trusted even when its body establishes too little.
function lyingGuard(value: unknown): value is {id: string} {
  return typeof value === "object" && value !== null && "id" in value;
}
const untrusted: unknown = {id: 42};
if (lyingGuard(untrusted)) { const compilerTrustsThis: string = untrusted.id; }
// Contextual inference varies: satisfies neither universally widens nor freezes literals.
const wide = {tag: "initial"} satisfies {tag: string};
wide.tag = "changed";
const narrow = {flag: true} satisfies {flag: boolean};
// @ts-expect-error this context retains the true literal
narrow.flag = false;
''')
            result = subprocess.run([node, str(compiler), "--ignoreConfig", "--strict", "--noUncheckedIndexedAccess", "--noEmit", "--target", "es2022", "--module", "esnext", "--moduleResolution", "bundler", "contracts.ts", "typechecks.ts"], cwd=work, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            (work / "runtime.ts").write_text('''import {strict as assert} from "node:assert";
import {parseDuration, endAt, first, describe} from "./contracts";
for (const invalid of [-1, NaN, Infinity, -Infinity, "3", null, undefined, {}])
  assert.throws(() => parseDuration(invalid), RangeError);
assert.equal(endAt(10, parseDuration(0)), 10);
assert.equal(endAt(10, parseDuration(3)), 13);
assert.equal(first(["one", "two"]), "one");
assert.equal(describe({kind:"pending"}), "waiting");
assert.equal(describe({kind:"ready",value:"yes"}), "yes");
assert.equal(describe({kind:"failed",error:"no"}), "no");
function lyingGuard(value: unknown): value is {id: string} {
  return typeof value === "object" && value !== null && "id" in value;
}
const malformed: unknown = {id: 42};
assert.equal(lyingGuard(malformed), true);
if (lyingGuard(malformed)) assert.equal(typeof malformed.id, "number");
''')
            result = subprocess.run([bun, "run", str(work / "runtime.ts")], cwd=work, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
