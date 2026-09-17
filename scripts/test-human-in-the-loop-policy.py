#!/usr/bin/env python3
"""Regression tests for the conservative approval-policy validator."""

from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "skills/1-human-in-the-loop"
SCRIPT = PACKAGE / "scripts/validate_gate_policy.py"
SPEC = importlib.util.spec_from_file_location("hitl_policy", SCRIPT)
assert SPEC and SPEC.loader
POLICY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(POLICY)


class HumanInTheLoopPolicyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.template = json.loads(
            (PACKAGE / "assets/approval-policy-template.json").read_text(encoding="utf-8")
        )

    def messages(self, data: object) -> list[str]:
        return [item["message"] for item in POLICY.validate(data)]

    def test_template_conforms_to_named_profile(self):
        self.assertEqual(self.template["policy_profile"], POLICY.POLICY_PROFILE)
        self.assertEqual(POLICY.validate(self.template), [])
        self.assertIn(POLICY.POLICY_PROFILE, POLICY.VALIDATION_SCOPE)
        self.assertIn("does not certify", POLICY.VALIDATION_SCOPE)

    def test_wrong_profile_critical_single_control_and_self_approval_fail(self):
        wrong = copy.deepcopy(self.template)
        wrong["policy_profile"] = "another-profile"
        self.assertTrue(any("must equal" in message for message in self.messages(wrong)))

        critical = copy.deepcopy(self.template)
        critical["gates"][0]["risk_tier"] = "critical"
        self.assertTrue(any("critical single-control" in message for message in self.messages(critical)))

        self_approval = copy.deepcopy(self.template)
        self_approval["gates"][0]["requester_may_approve"] = True
        self.assertTrue(any("self-approval requires" in message for message in self.messages(self_approval)))

    def test_impossible_distinct_subjects_and_unknown_roles_fail(self):
        invalid = copy.deepcopy(self.template)
        invalid["gates"][0]["required_approver_roles"] = ["missing-role"]
        invalid["gates"][0]["minimum_distinct_subjects"] = 2
        messages = self.messages(invalid)
        self.assertTrue(any("unknown roles" in message for message in messages))
        self.assertTrue(any("exceeds eligible distinct" in message for message in messages))

    def test_loader_rejects_symlink_and_oversized_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            real = root / "policy.json"
            real.write_text(json.dumps(self.template), encoding="utf-8")
            self.assertEqual(POLICY.load_policy(real)["policy_profile"], POLICY.POLICY_PROFILE)

            linked = root / "linked.json"
            linked.symlink_to(real)
            with self.assertRaisesRegex(ValueError, "symbolic link"):
                POLICY.load_policy(linked)

            large = root / "large.json"
            large.write_bytes(b" " * (POLICY.MAX_POLICY_BYTES + 1))
            with self.assertRaisesRegex(ValueError, "exceeds"):
                POLICY.load_policy(large)


if __name__ == "__main__":
    unittest.main()
