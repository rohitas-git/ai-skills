"""Dependency-free regression tests for the imported Tailwind compatibility helper."""

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from tailwind_config_gen import TailwindConfigGenerator


def strip_to_javascript(config: str) -> str:
    lines = []
    for line in config.splitlines():
        if line.startswith("import type") or line.strip() == "export default config":
            continue
        lines.append(
            line.replace("const config: Config =", "const config =").replace(
                "module.exports =", "const config ="
            )
        )
    return "\n".join(lines)


class TailwindConfigGeneratorTests(unittest.TestCase):
    def test_framework_content_paths_are_explicit(self):
        expected = {
            "react": "src/**/*.{js,jsx,ts,tsx}",
            "vue": "src/**/*.{vue,js,ts,jsx,tsx}",
            "svelte": "src/**/*.{svelte,js,ts}",
            "nextjs": "app/**/*.{js,ts,jsx,tsx}",
        }
        for framework, fragment in expected.items():
            with self.subTest(framework=framework):
                paths = TailwindConfigGenerator(framework=framework).config["content"]
                self.assertTrue(any(fragment in path for path in paths))

    def test_requested_extensions_are_serialized(self):
        generator = TailwindConfigGenerator(framework="nextjs")
        generator.add_colors({"brand": "#123456"})
        generator.add_fonts({"sans": ["Inter", "sans-serif"]})
        generator.add_spacing({"section": "4rem"})
        generator.add_breakpoints({"wide": "120rem"})
        generator.add_plugins(["tailwindcss-animate"])
        output = generator.generate_config_string()
        for value in ("brand", "Inter", "section", "wide", "tailwindcss-animate"):
            self.assertIn(value, output)

    def test_duplicate_plugins_are_removed(self):
        generator = TailwindConfigGenerator()
        generator.add_plugins(["tailwindcss-animate", "tailwindcss-animate"])
        self.assertEqual(generator.config["plugins"], ["tailwindcss-animate"])

    def test_plugin_name_rejects_generated_code_injection(self):
        generator = TailwindConfigGenerator()
        generator.add_plugins(["safe'); process.exit(1); //"])
        with self.assertRaises(ValueError):
            generator.generate_config_string()

    def test_property_before_plugins_is_comma_terminated(self):
        for typescript in (True, False):
            with self.subTest(typescript=typescript):
                generator = TailwindConfigGenerator(typescript=typescript)
                generator.add_colors({"brand": "#6366f1"})
                output = generator.generate_config_string()
                self.assertNotIn("}\n  plugins:", output)
                self.assertIn("},\n  plugins:", output)

    @unittest.skipUnless(shutil.which("node"), "node not available")
    def test_generated_typescript_and_javascript_shapes_parse(self):
        with tempfile.TemporaryDirectory() as temp:
            for typescript in (True, False):
                with self.subTest(typescript=typescript):
                    generator = TailwindConfigGenerator(typescript=typescript)
                    generator.add_colors({"brand": "#6366f1"})
                    generator.add_plugins(["tailwindcss-animate"])
                    path = Path(temp) / f"config-{typescript}.cjs"
                    path.write_text(strip_to_javascript(generator.generate_config_string()))
                    result = subprocess.run(
                        [shutil.which("node"), "--check", str(path)],
                        capture_output=True,
                        text=True,
                    )
                    self.assertEqual(result.returncode, 0, result.stderr)

    def test_validate_rejects_missing_content_paths(self):
        generator = TailwindConfigGenerator()
        generator.config["content"] = []
        valid, message = generator.validate_config()
        self.assertFalse(valid)
        self.assertIn("No content paths", message)

    def test_write_targets_only_the_explicit_path(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "tailwind.config.ts"
            generator = TailwindConfigGenerator(output_path=destination)
            generator.add_colors({"brand": "#123456"})
            success, message = generator.write_config()
            self.assertTrue(success)
            self.assertIn(str(destination), message)
            self.assertIn("brand", destination.read_text())


if __name__ == "__main__":
    unittest.main()
