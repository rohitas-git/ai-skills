---
name: 1-plow-ahead
description: >
  Continue an already-authorized workflow through routine, reversible ambiguity when
  the user explicitly requests autonomy. Not for new scope, destructive or external
  authority, speculative fixes, or bypassing a required decision. Hub: /0-butler.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-butler
    role: soft
    when:
      - "the user explicitly asks the active workflow to keep going through routine ambiguity"
    not_when:
      - "no substantive workflow is active"
      - "the next step needs new scope, authority, secrets, or an irreversible choice"
    cousins: [1-karpathy-guidelines, 0-ponytail, 1-handoff]
    triggers: ["plow ahead", "do not stop", "use your best judgment", "finish while I am away"]
    prev: [0-butler]
    next: [0-butler, 1-handoff]
    requires_setup: false
---

# Plow Ahead

**Atomic job:** set an autonomy overlay on the current workflow. It removes routine
preference pauses; it does not execute work independently or expand permission.

## Contract

1. Inherit the exact objective, accepted/excluded scope, candidate/worktree/branch/
   `HEAD`, dirty-state ownership, shared-resource ownership, allowed tools/actions,
   acceptance criteria, and verification obligations from the active workflow.
2. Turn only low-impact, reversible implementation preferences into explicit,
   conservative assumptions grounded in repository instructions, current evidence,
   and nearby patterns.
3. Continue through ordinary failures when a bounded evidence-led diagnosis or fix
   remains inside the existing authority. Record consequential assumptions and their
   evidence for the final handoff.
4. Stop at the first decision that requires new product scope, destructive or
   irreversible action, credentials/private data, external publication or mutation,
   production/shared-service effects, history rewrite, force push, conflict with user
   instructions, or a broad speculative change.
5. Return completion, evidence limits, assumptions, and the exact missing decision
   to the owning workflow. Create `/1-handoff` output only when explicitly requested.

## Hard rules

- “Do not stop” is persistence, not blanket authority. It never authorizes a commit,
  push, merge, deploy, deletion, install, purchase, message, permission change,
  production action, or acceptance of risk that was not already authorized.
- This overlay does not create/switch/remove a worktree, stash/reset/clean state,
  select extra skills, spawn subagents, weaken checks, change task/goal status, or
  decide that a repeated obstacle is formally `blocked`.
- Choose the smallest reversible assumption; if different reasonable answers would
  materially change user-visible behavior, compatibility, cost, or risk, ask.
- Never conceal failed/skipped verification or treat a workaround as the requested
  outcome.

Historical source only:
[BuilderIO Plow Ahead snapshot](../../archive/vendor/builderio-skills/skills/plow-ahead/SKILL.md)
@ `8cd5958`.
