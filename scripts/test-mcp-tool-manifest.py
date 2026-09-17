#!/usr/bin/env python3
"""Regression tests for the MCP design-manifest validator."""

from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/1-mcp-server-building/scripts/validate_tool_manifest.py"
SPEC = importlib.util.spec_from_file_location("mcp_manifest", SCRIPT)
assert SPEC and SPEC.loader
MCP = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MCP)


def valid_manifest() -> dict[str, object]:
    return {
        "manifestProfile": MCP.MANIFEST_PROFILE,
        "server": {
            "name": "inventory-server",
            "version": "1.0.0",
            "protocolRevision": "2026-07-28",
            "usesProtocolSessions": False,
        },
        "tools": [
            {
                "name": "inventory.read",
                "description": "Read one authorized inventory record by identifier.",
                "inputSchema": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                    "additionalProperties": False,
                },
                "outputSchema": {"type": "object"},
                "errorSchemas": [
                    {
                        "code": "not_found",
                        "description": "The authorized record does not exist.",
                        "dataSchema": {"type": "object"},
                    }
                ],
                "effects": ["read"],
                "dataClasses": ["internal"],
                "authorization": {
                    "mode": "authenticated",
                    "enforcementPoint": "inventory handler",
                    "scopes": ["inventory:read"],
                },
                "idempotent": True,
            }
        ],
    }


class MCPToolManifestTests(unittest.TestCase):
    def test_valid_profile_manifest_has_no_issues(self):
        self.assertEqual(MCP.lint_manifest(valid_manifest()), [])

    def test_profile_and_revision_specific_session_mismatch_fail(self):
        wrong = valid_manifest()
        wrong["manifestProfile"] = "another-profile"
        self.assertTrue(any(item["path"] == "$.manifestProfile" for item in MCP.lint_manifest(wrong)))

        session = valid_manifest()
        session["server"]["usesProtocolSessions"] = True
        self.assertTrue(any("removed protocol sessions" in item["message"] for item in MCP.lint_manifest(session)))

    def test_description_effect_mismatch_warns_and_schema_mismatch_fails(self):
        data = valid_manifest()
        tool = data["tools"][0]
        tool["description"] = "Delete one authorized inventory record permanently."
        tool["inputSchema"]["required"] = ["missing"]
        issues = MCP.lint_manifest(data)
        self.assertTrue(any(item["level"] == "warning" and "delete" in item["message"] for item in issues))
        self.assertTrue(any(item["level"] == "error" and "not defined" in item["message"] for item in issues))

    def test_loader_rejects_symlink_and_oversized_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            real = root / "manifest.json"
            real.write_text(json.dumps(valid_manifest()), encoding="utf-8")
            self.assertEqual(MCP.load_manifest(real)["manifestProfile"], MCP.MANIFEST_PROFILE)

            linked = root / "linked.json"
            linked.symlink_to(real)
            with self.assertRaisesRegex(ValueError, "symbolic link"):
                MCP.load_manifest(linked)

            large = root / "large.json"
            large.write_bytes(b" " * (MCP.MAX_MANIFEST_BYTES + 1))
            with self.assertRaisesRegex(ValueError, "exceeds"):
                MCP.load_manifest(large)


if __name__ == "__main__":
    unittest.main()
