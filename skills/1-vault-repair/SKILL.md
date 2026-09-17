---
name: 1-vault-repair
description: >
  Revalidate and repair one accepted, evidence-backed Vault Lint finding within an exact
  file scope. Not for broad cleanup, fresh auditing, ingest, or unrelated improvements.
  Hub: /0-rohitas-vault-wiki.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-rohitas-vault-wiki
    role: leaf
    when: ["apply one accepted Vault Lint finding after revalidating its current evidence"]
    not_when: ["find issues → 1-vault-lint", "knowledge/source update → 1-vault-ingest", "bulk vault cleanup"]
    triggers: ["fix this vault lint finding", "repair vault finding V", "apply this accepted vault repair"]
    prev: [0-rohitas-vault-wiki, 1-vault-lint]
    next: [0-rohitas-vault-wiki, 1-vault-lint, 1-vault-ingest]
    requires_setup: true
---

# Vault Repair

**Atomic job:** revalidate and repair exactly one accepted Vault Lint finding, then return
targeted evidence without widening into a new audit.

1. Require the finding ID, original snapshot/evidence, accepted disposition, configured
   root/SSOT, exact allowed files/actions, privacy boundary, caller, and write/destructive/
   external authority. A vague “fix the vault” returns to `/1-vault-lint` for scope.
2. Canonically contain targets. For Git-backed content, pin repository/worktree/branch/`HEAD`,
   dirty ownership, and working-tree candidate; create no worktree or touch unrelated state.
   Worktrees do not isolate sync clients, plugins, accounts, or remote services.
3. Re-read the finding's exact evidence and target versions. If it no longer reproduces,
   conflicts with current user edits, or depends on unknown schema/plugin/runtime state, make
   no change and return `stale`, `conflicted`, or `needs evidence`.
4. Classify the smallest fitting repair. Knowledge/provenance changes route to
   `/1-vault-ingest`; unsupported runtime/plugin behavior returns to its specialist. Rename,
   move, delete, merge/split, source consumption, schema expansion, and `.obsidian/` changes
   require explicit action-specific authority and an affected-link/path preview.
5. Re-scan immediately before writing and change only the accepted files/hunks. Preserve
   unrelated content, metadata, source wording, and dirty work. Never stage, stash, reset,
   normalize, or overwrite a whole note for convenience.
6. Re-run only the finding's reproduction plus fitting syntax/link checks. Re-read the diff,
   verify containment/idempotence and no new dangling references, and record before/after
   evidence. Do not claim the whole vault is clean.
7. Return finding disposition, exact files/deltas, versions, checks, and residual limits to
   `/1-vault-lint`, `/0-rohitas-vault-wiki`, or the caller.

Repair does not start another lint pass, fix adjacent findings, log, ingest, archive, install,
sync, commit, publish, push, or merge unless separately requested through the owning workflow.
