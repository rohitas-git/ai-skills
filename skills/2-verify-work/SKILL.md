---
name: 2-verify-work
description: >
  Run an evidence-focused verification pass: inspect diffs, run relevant builds/tests, and check stated behavior.
  Use when checking work, verifying changes, or self-verifying. Not for: multi-axis ship review (1-code-review) or design
  grill (0-grilling). Hub: /1-code-review. Triggers: check work, verify changes, self-verify.
disable-model-invocation: true
metadata:
  short-description: "Verify scoped outcomes against evidence"
  catalog:
    hub: 1-code-review
    role: cousin
    when:
      - "mid/post-build verify with builds/tests"
      - "self-verify"
    not_when:
      - "full multi-axis review → 1-code-review"
      - "requirements unclear → 0-grilling"
    next: [1-code-review]
    cousins: [1-code-review, 1-tdd]
    triggers:
      - "check work"
      - "verify changes"
      - "self-verify"
      - "2-verify-work"
      - "run verification"
      - "verify before PR"
    requires_setup: false
---

# /2-verify-work -- Self-Verification

## Boundary

| Need | Skill |
|------|--------|
| Evidence-focused verification of scoped work or claims | **verify-work** (this) |
| Multi-axis change/PR 0-review closer | `/1-code-review` |
| Security audit | `/1-security-auditor` |
| Over-engineering 0-review only | `/2-ponytail-review` |
| Harsh maintainability-only / thermo-nuclear | `/2-thermo-nuclear-code-quality-review` |
| Ship 0-implement loop | `/0-implement` |

**Not for:** open-ended “which review?” → `/0-review` F-R1. Prefer this mid-build; prefer `/1-code-review` as Ship closer.


**Iron law (evidence gate):** no completion claims without fresh verification evidence. See [references/superpowers-evidence-gate.md](./references/superpowers-evidence-gate.md).

Verify the requested work or claims against authoritative evidence. Remain read-only
unless a separate implementation caller has repair authority; report back to that
caller rather than owning a repair loop. Delegation is optional and permission-bound.

## Process

1. Read [the full guide](./references/full-guide.md) and [candidate contract](../0-review/references/review-candidate.md). Pin the caller, active request, candidate and allowed checks; do not infer all historical chat tasks as scope.
2. Map each requirement or claim to its evidence, using [the evidence gate](./references/superpowers-evidence-gate.md). Inspect sources and run only relevant permitted checks; reuse results only when their candidate and relevant environment still match.
3. Classify each item as verified, contradicted, unverified/blocked, or not applicable. Check current state before reporting; distinguish local evidence from published PR/CI evidence.
4. Return PASS, FAIL or BLOCKED with the supporting checklist and limits. No automatic fixes, retry loop, branch movement, test installation, publication or finish-branch handoff. If an authorized caller repairs a failure, verify the refreshed candidate when called again.

## Progressive disclosure

| Load when | File |
|-----------|------|
| Full workflow / detail | [references/full-guide.md](./references/full-guide.md) |
| Evidence-before-claims iron law | [references/superpowers-evidence-gate.md](./references/superpowers-evidence-gate.md) |
| Evidence from another agent's run | [source adaptation](./references/source-adaptation.md) |

## Related

See Boundary table and hub membership in `skills/0-butler/references/flows.md`.

Vendor adaptation: BuilderIO `agent-watchdog` contributes contract reconstruction and independent claim checking, not ambient monitoring or repair authority.
