---
name: 1-verify-work
description: >
  Check your work with a verification subagent that reviews diffs, runs builds
  and tests, and evaluates correctness. Read this file for instructions. Use when
  asked to "check work", "verify changes", "self-verify", "/1-verify-work", "/check",
  "/verify", or "/self-verify".
metadata:
  short-description: "Verify changes with a subagent"
disable-model-invocation: true
---

# /1-verify-work -- Self-Verification

## Boundary

| Need | Skill |
|------|--------|
| Mid-build verification subagent (diffs, build, tests) | **verify-work** (this) |
| Multi-axis change/PR review closer | `/1-code-review` |
| Security audit | `/1-security-auditor` |
| Over-engineering review only | `/1-ponytail-review` |
| Ship implement loop | `/0-implement` |

**Not for:** open-ended “which review?” → `/0-review` F-R1. Prefer this mid-build; prefer `/1-code-review` as Ship closer.


Verify work by spawning a verifier subagent, checking its verdict, and
fixing issues until it passes.

## Process

1. Read [references/full-guide.md](./references/full-guide.md) for full steps, templates, and detail.
2. Execute the procedure from that guide.
3. Stay within this skill's Boundary (above or in guide).

## Progressive disclosure

| Load when | File |
|-----------|------|
| Full workflow / detail | [references/full-guide.md](./references/full-guide.md) |

## Related

See Boundary table and hub membership in `skills/0-butler/references/flows.md`.
