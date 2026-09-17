"""Dependency-free regression tests for the imported shadcn compatibility helper."""

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).parent.parent))

from shadcn_add import ShadcnInstaller


class ShadcnInstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "components.json").write_text(
            json.dumps({"aliases": {"components": "@/components"}})
        )
        (self.root / "components/ui").mkdir(parents=True)

    def tearDown(self):
        self.temp.cleanup()

    def test_configuration_and_installed_components_are_read_locally(self):
        (self.root / "components/ui/button.tsx").write_text("export {}")
        installer = ShadcnInstaller(self.root)
        self.assertTrue(installer.check_shadcn_config())
        self.assertEqual(installer.get_installed_components(), ["button"])

    def test_missing_or_malformed_configuration_is_bounded(self):
        missing = self.root / "missing"
        missing.mkdir()
        self.assertEqual(ShadcnInstaller(missing).get_installed_components(), [])
        (self.root / "components.json").write_text("not-json")
        self.assertEqual(ShadcnInstaller(self.root).get_installed_components(), [])

    def test_dry_run_uses_pinned_fallback_without_executing(self):
        installer = ShadcnInstaller(self.root, dry_run=True)
        with patch("subprocess.run") as run:
            success, message = installer.add_components(["button", "card"])
        self.assertTrue(success)
        self.assertIn("npx shadcn@2.3.0 add button card", message)
        run.assert_not_called()

    def test_project_declared_version_overrides_fallback(self):
        (self.root / "package.json").write_text(
            json.dumps({"devDependencies": {"shadcn": "^2.4.1"}})
        )
        installer = ShadcnInstaller(self.root, dry_run=True)
        success, message = installer.add_components(["button"])
        self.assertTrue(success)
        self.assertIn("shadcn@2.4.1", message)

    def test_existing_component_requires_explicit_overwrite(self):
        (self.root / "components/ui/button.tsx").write_text("export {}")
        installer = ShadcnInstaller(self.root, dry_run=True)
        success, message = installer.add_components(["button"])
        self.assertFalse(success)
        self.assertIn("Use --overwrite", message)

    def test_apply_uses_exact_project_root_and_component_list(self):
        installer = ShadcnInstaller(self.root)
        with patch("subprocess.run") as run:
            run.return_value = MagicMock(stdout="ok", stderr="", returncode=0)
            success, _ = installer.add_components(["button"])
        self.assertTrue(success)
        run.assert_called_once_with(
            ["npx", "shadcn@2.3.0", "add", "button"],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=True,
        )

    def test_all_mode_is_visible_in_dry_run(self):
        success, message = ShadcnInstaller(self.root, dry_run=True).add_all_components()
        self.assertTrue(success)
        self.assertIn("add --all", message)

    def test_list_is_read_only_and_sorted(self):
        (self.root / "components/ui/zeta.tsx").write_text("export {}")
        (self.root / "components/ui/alpha.tsx").write_text("export {}")
        success, message = ShadcnInstaller(self.root).list_installed()
        self.assertTrue(success)
        self.assertLess(message.index("alpha"), message.index("zeta"))


if __name__ == "__main__":
    unittest.main()
