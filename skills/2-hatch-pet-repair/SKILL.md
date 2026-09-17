---
name: 2-hatch-pet-repair
description: >
  Apply one bounded repair to a copied Codex v2 pet candidate and revalidate the affected contract. Never edits an
  installed pet in place or expands into redesign, installation, or cleanup. Parent: /1-hatch-pet.
disable-model-invocation: true
metadata:
  catalog:
    hub: 1-hatch-pet
    role: leaf
    when: ["repair one identified defect in one Codex v2 pet candidate"]
    not_when: ["new pet build → 2-hatch-pet-build", "review or validate only → 2-hatch-pet-validate", "install → 2-hatch-pet-install"]
    prev: [1-hatch-pet, 2-hatch-pet-validate]
    next: [1-hatch-pet, 1-imagine, 2-hatch-pet-validate]
    cousins: [2-hatch-pet-build, 2-hatch-pet-validate, 2-hatch-pet-install]
    triggers: [repair Codex pet, fix pet spritesheet, repair pet row, fix pet validation]
    requires_setup: false
---

# Repair Hatch Pet

**Atomic job:** repair one verified defect class in one immutable candidate copy, re-run affected gates, and return
the new candidate. The requested identity and design are protected scope; unrelated polish is excluded.

1. Pin caller, source candidate/hash, failing evidence, one defect class, protected identity/rows/features, repair
   destination, v2 contract revision, overwrite rule, and authority. If source is installed, copy it to a fresh
   run-owned destination; never modify the installed package. Carry exact optional worktree/branch/`HEAD` and dirty
   ownership. Worktrees do not isolate image providers, Codex home, installed pets, accounts, or shared destinations.
2. Read the parent [contract](../1-hatch-pet/references/codex-pet-contract.md), [row semantics](../1-hatch-pet/references/animation-rows.md),
   [QA rubric](../1-hatch-pet/references/qa-rubric.md), and [helper safety](../1-hatch-pet/references/helper-safety.md).
   Reproduce or validate the reported defect before mutation; distinguish deterministic geometry/chroma/extraction
   faults from visual identity, direction, continuity, and state-semantic faults.
3. Choose the smallest packaging-eligible repair. Deterministic faults use the narrow fitting helper. Visual faults
   call `/1-imagine` with the exact source and invariants. Repair one standard row or one complete coherent look row;
   never splice a newly generated look cell, regenerate passing rows, or reinterpret a warning as redesign authority.
4. Recheck source revision and destination collision before writing. Re-run every directly affected downstream gate
   plus final v2 validation and focused visual inspection. Preserve old and new hashes/evidence; a retry that merely
   moves the defect is failure, not progress. Stop without installing, cleanup, or broader regeneration.
5. Return defect evidence, changed artifact/row, before/after hashes, checks, residual warnings, effects, and limits
   to `/1-hatch-pet` or the caller. Validation-only follow-up is allowed only when the caller requested it; installation,
   publication, redesign, another defect, and deletion are separate operations.

