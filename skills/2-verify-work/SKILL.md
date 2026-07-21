---
name: 2-verify-work
description: >
  Verification subagent: review diffs, run builds/tests, check correctness. Use when
  check work / verify changes / self-verify. Not for: multi-axis ship review (1-code-review) or design
  grill (0-grilling). Hub: /1-code-review. Triggers: check work, verify changes, self-verify.
disable-model-invocation: true
metadata:
  short-description: "Verify changes with a subagent"
  catalog:
    hub: 1-code-review
    role: cousin
    when:
      - "mid/post-build verify with builds/tests"
      - "self-verify"
    not_when:
      - "full multi-axis review → 1-code-review"
      - "requirements unclear → 0-grilling"
    cousins: [1-code-review, 1-tdd]
    triggers:
      - "check work"
      - "verify changes"
      - "self-verify"
      - "2-verify-work"
    requires_setup: false
---

# /2-verify-work -- Self-Verification

## Boundary

| Need | Skill |
|------|--------|
| Mid-build verification subagent (diffs, build, tests) | **verify-work** (this) |
| Multi-axis change/PR 0-review closer | `/1-code-review` |
| Security audit | `/1-security-auditor` |
| Over-engineering 0-review only | `/2-ponytail-review` |
| Ship 0-implement loop | `/0-implement` |

**Not for:** open-ended “which review?” → `/0-review` F-R1. Prefer this mid-build; prefer `/1-code-review` as Ship closer.


**Iron law (evidence gate):** no completion claims without fresh verification evidence. See [references/superpowers-evidence-gate.md](./references/superpowers-evidence-gate.md).

Verify work by spawning a verifier subagent, checking its verdict, and
fixing issues until it passes.

## Process

1. Read [references/full-guide.md](./references/full-guide.md) for full steps, templates, and detail.
2. Apply the evidence gate before any “done/fixed/passing” claim ([superpowers-evidence-gate.md](./references/superpowers-evidence-gate.md)).
3. Execute the procedure from the full guide.
4. Stay within this skill's Boundary (above or in guide).

## Progressive disclosure

| Load when | File |
|-----------|------|
| Full workflow / detail | [references/full-guide.md](./references/full-guide.md) |
| Evidence-before-claims iron law | [references/superpowers-evidence-gate.md](./references/superpowers-evidence-gate.md) |

## Related

See Boundary table and hub membership in `skills/0-butler/references/flows.md`.
