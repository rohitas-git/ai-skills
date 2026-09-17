---
name: 2-hatch-pet-install
description: >
  Install one already validated Codex v2 pet candidate into one exact local Codex pet destination. Requires explicit
  install authority and never builds, repairs, publishes, or cleans up. Parent: /1-hatch-pet.
disable-model-invocation: true
metadata:
  catalog:
    hub: 1-hatch-pet
    role: leaf
    when: ["install one validated Codex v2 pet candidate locally"]
    not_when: ["build → 2-hatch-pet-build", "repair → 2-hatch-pet-repair", "validate only → 2-hatch-pet-validate", "remote publish or sync"]
    prev: [1-hatch-pet, 2-hatch-pet-validate]
    next: [1-hatch-pet, 2-hatch-pet-validate]
    cousins: [2-hatch-pet-build, 2-hatch-pet-repair, 2-hatch-pet-validate]
    triggers: [install Codex pet, add local pet, activate custom pet]
    requires_setup: false
---

# Install Hatch Pet

**Atomic job:** copy one hash-pinned, already validated v2 package into one exact local Codex pet directory and
verify the installed bytes. It grants no build, repair, cleanup, selection, activation, sync, or publication authority.

1. Require an explicit install request. Pin caller, candidate root and hashes, successful validation evidence bound
   to those hashes, exact Codex home and pet id, destination, collision policy, rollback copy/retention, and write
   authority. Do not infer the home directory, current pet selection, or overwrite from environment-variable text.
2. A worktree is optional source provenance only; it does not isolate the global Codex home, installed pet registry,
   running app, account, or synced settings. Recheck source hashes, manifest `spriteVersionNumber: 2`, referenced
   spritesheet identity, destination containment, symlinks, and collision immediately before writing.
3. If destination exists, stop unless the user explicitly authorized replacement of that exact pet id and the prior
   package can be preserved at an agreed recovery location. Stage both files in a fresh sibling directory, verify
   their hashes and manifest relationship there, then promote the complete directory atomically when the filesystem
   permits. Never expose a half-installed manifest/spritesheet pair.
4. Re-read installed files and run the structural validator against the installed spritesheet. Report atomicity or
   filesystem limitations honestly. On partial failure, preserve both source and recovery material; do not delete,
   retry blindly, activate the pet, restart an app, or clean old packages without separate authority.
5. Return destination, source/installed hashes, validation evidence, collision/backup decision, exact effects, and
   residual risks to `/1-hatch-pet` or caller. Repair, activation, distribution, sync, and cleanup are new operations.

