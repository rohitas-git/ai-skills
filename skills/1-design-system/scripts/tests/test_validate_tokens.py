"""Stdlib regression tests for the regex-based token-usage scanner."""

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "validate-tokens.cjs"


class ValidateTokensTests(unittest.TestCase):
    def _run(self, css: str) -> subprocess.CompletedProcess:
        node = shutil.which("node")
        if not node:
            self.skipTest("node not available")
        self._temporary = tempfile.TemporaryDirectory()
        directory = Path(self._temporary.name)
        (directory / "sample.css").write_text(css)
        return subprocess.run(
            [node, str(SCRIPT), "--dir", str(directory)],
            capture_output=True,
            text=True,
        )

    def tearDown(self):
        temporary = getattr(self, "_temporary", None)
        if temporary:
            temporary.cleanup()

    def test_flags_hardcoded_hex_sharing_line_with_token(self):
        result = self._run(
            ".btn { background: #FF6B6B; color: var(--color-primary); }\n"
        )
        self.assertIn("#FF6B6B", result.stdout)
        self.assertEqual(result.returncode, 1)

    def test_token_only_line_reports_no_violation(self):
        result = self._run(
            ".btn { background: var(--color-bg); color: var(--color-primary); }\n"
        )
        self.assertIn("No token violations", result.stdout)
        self.assertEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
