---
name: 1-pi-agent-rust
description: >
  Supply repository-specific surfaces, invariants, and candidate verification commands
  for work in a confirmed pi_agent_rust checkout, then route diagnosis, implementation,
  review, or CI work to its owning workflow. Hub: /0-butler.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-butler
    role: soft
    when:
      - "the active repository is confirmed as pi_agent_rust and project-specific guidance is needed"
    not_when:
      - "generic Rust work or an unconfirmed repository"
      - "perform the full diagnosis, implementation, review, or CI workflow here"
    triggers: ["1-pi-agent-rust", "pi_agent_rust", "pi agent rust repository"]
    prev: [0-butler]
    next: [0-butler, 0-diagnosing-bugs, 0-implement, 0-review, 1-ci-cd-and-automation]
    requires_setup: false
---

# Pi Agent Rust Adapter

**Atomic job:** identify the smallest relevant pi_agent_rust surface and return a
repository-specific evidence/verification packet to the proper general workflow.
This adapter does not diagnose, edit, test, install, or finish work by itself.

## Checkout

1. Confirm repository identity from its current files/instructions; do not infer it
   from a directory name alone.
2. Record the exact repository/worktree path, branch or detached state, `HEAD`, dirty
   state and ownership, requested mode, accepted/excluded scope, and allowed actions.
3. Read the applicable `AGENTS.md`/repository rules and current build metadata before
   trusting any command or file map in this catalog snapshot.
4. Identify one surface and route:
   - unexplained failure/root cause → `/0-diagnosing-bugs`;
   - authorized source/config/docs change → `/0-implement`;
   - read-only candidate assessment → `/0-review`;
   - workflow/check contract → `/1-ci-cd-and-automation`.
5. Return relevant current files, invariants, smallest candidate reproduction/check,
   broader risk-based verification, shared-resource needs, and stale/unknown guidance.

## Project map candidates

- providers/stream parsing and tool-call normalization;
- session persistence/index compatibility;
- extension runtime/capability policy;
- CLI/TUI/RPC event parity;
- installer/uninstaller, artifact verification, and managed-skill lifecycle.

Use [command candidates](./references/COMMANDS.md) or
[symptom playbooks](./references/DEBUGGING-PLAYBOOKS.md) only after verifying paths,
scripts, test names, tool availability, and semantics against the current checkout.

## Authority and worktrees

- Read-only routing does not create a worktree. Authorized edits use the exact active
  worktree or the matching isolated checkout selected by the owning workflow.
- A worktree does not isolate Cargo caches/targets, temp paths, credentials, network
  services, release assets, installer destinations, or host-installed skills. Assign
  unique resources or use repository-native isolation only when authorized.
- Never export hard-coded shared temp/target paths, install/uninstall artifacts, edit
  host skill directories, delete/replace destinations, or run release/network commands
  from snapshot guidance alone.
- Preserve user changes. Never stash, reset, clean, switch branches, commit, push,
  merge, force-push, or bypass hooks unless the owning workflow and user authority
  explicitly permit the exact action.
- Return evidence to the actual owning workflow; do not silently chain to branch
  finishing or claim unrun commands passed.
