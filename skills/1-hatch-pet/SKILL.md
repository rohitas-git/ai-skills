---
name: 1-hatch-pet
description: >
  Route one Codex v2 animated-pet request to build, repair, validate, or install. The router performs no image,
  file, package, cleanup, or installation work. Not for general raster images. Hub: /1-hatch-pet under /0-office.
disable-model-invocation: true
metadata:
  catalog:
    hub: 1-hatch-pet
    role: sub-hub
    when: ["build, repair, validate, or install one Codex v2 animated pet"]
    not_when: ["general raster generation/edit → 1-imagine", "diagram → 1-diagram-maker", "several pet operations without an explicit sequence"]
    prev: [0-office]
    next: [2-hatch-pet-build, 2-hatch-pet-repair, 2-hatch-pet-validate, 2-hatch-pet-install, 0-office]
    cousins: [1-imagine, 1-diagram-maker]
    triggers: [hatch pet, Codex pet, pet spritesheet, animated mascot pet, validate pet, repair pet, install pet]
    requires_setup: false
---

# Hatch Pet

**Atomic job:** choose exactly one pet operation for one immutable candidate/request and return that leaf's result
to the actual caller. The hub never researches, generates, reads an image, edits a file, validates, cleans up, or
installs a package.

| Requested outcome | Route |
|---|---|
| Produce one new validated v2 candidate package in a run-owned destination | `/2-hatch-pet-build` |
| Apply one bounded repair to a copied candidate and revalidate it | `/2-hatch-pet-repair` |
| Read-only assessment of one existing atlas/package | `/2-hatch-pet-validate` |
| Install one already validated candidate into one exact local Codex pet destination | `/2-hatch-pet-install` |
| Generate or edit a general raster image | `/1-imagine` |

1. Pin actual caller, one request/candidate version, desired operation, source and destination identities, expected
   v2 contract, evidence, sensitivity/rights, overwrite/cleanup rules, authority, and optional exact repository/
   worktree/branch/`HEAD` with dirty ownership. A worktree does not isolate image providers, Codex home, installed
   pets, accounts, generated-image stores, or remote sources.
2. Direct-route when the outcome is explicit. Use **F-PET1** only when build versus repair versus validate versus
   install materially changes the requested result. Never infer installation from “hatch,” validation from a file
   extension, repair authority from a failed check, or research authority from a brand name.
3. Hand exactly one leaf the same pinned candidate, evidence, exclusions, paths, and effect authority. Building,
   repairing, validating, installing, publishing, and cleanup are separate effects and are never chained silently.
4. Return artifact/evidence locators, hashes where available, verification, mutations, residual risks, and limits to
   `/0-office` or the actual caller. A follow-on operation requires a new explicit request.

**F-PET1 — Which one pet result is needed?** Recommend the explicit verb or strongest candidate-state evidence;
offer only build, repair, validate, install, or **Agent judgment**.

## Child-owned references

The router does not load these. The selected leaf loads only what it names: [v2 contract](./references/codex-pet-contract.md),
[animation rows](./references/animation-rows.md), [QA rubric](./references/qa-rubric.md),
[build pipeline](./references/build-pipeline.md), and [helper safety](./references/helper-safety.md).
The [former monolithic guide](./references/full-guide.md) is historical provenance, not execution guidance.
