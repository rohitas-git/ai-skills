# Catalog governance wiring audit

Date: 2026-09-12  
Status: reviewed; final catalog sweep pending

## Scope

Reviewed the complete live packages and operative routing surfaces for:

- `0-skill-manager`
- `0-skill-creator`
- `1-create-skill`
- `1-discover-skills`
- `1-session-skill-reflect`
- `1-skill-atomize`
- `1-skill-linter`
- `1-source-backed-skill`
- `1-writing-great-skills`

Also reviewed both hub workflow/HTML packages, the Catalog and Author sections of Butler flows, all manager/creator/linter/atomize references, the complete 3,080-line Writing Great Skills package, and its helper assets.

## Findings and changes

- Replaced automatic dry-run/confirm gates with one explicit-authority rule: a create/fix/update/ingest/organize request permits its bounded reversible catalog files. Material ambiguity, deletion, overwrite, identity-changing merge/split, install, sync, publication, or external/global effects remain separate gates.
- Pinned catalog root, repository/worktree, branch/`HEAD`, dirty ownership, target revision, allowed files, and evidence cutoff before edits; every writer re-reads targets and reports applied/unapplied ledger items.
- Made Skill Manager one catalog change-set owner and Skill Creator one body-candidate/evaluation owner. Placement, installation, activation, sync, commit, push, and publication no longer follow automatically.
- Reduced Create Skill to a true authoring wrapper.
- Made Discover Skills read-only and removed `npx`/global-install execution from discovery. Fixed-source supply-chain review and catalog/runtime installation are distinct later operations.
- Made Session Skill Reflect a read-only observed/inferred/unknown proposal rather than an automatic backup/edit/commit/push workflow.
- Removed the redundant F-A3 “write files?” fork and F10 “place now?” fork. F-A1/F-A2 now apply only to material overlap scope or identity-retention decisions.
- Strengthened Skill Linter's candidate/cutoff/tool-version/coverage contract and explicit limit: structural PASS is not semantic or security proof.
- Added corpus hashes/provenance, exact private destination, PII/copyright, worktree/global-state, and no-auto-placement boundaries to Source-Backed Skill.
- Reduced every main governance body to 37–70 lines. Converted the Superpowers/Anthropic/TDD/persuasion mega-guides into short provenance adaptations; disabled the archived renderer and removed implicit delegation, downloads, installs, viewers, deployment, or persuasion-as-compliance.
- Reconciled manager/creator workflow JSON, live HTML links, Butler flows, README, wiki index, and generated route index.

## Verification

- Focused `CatalogGovernanceRouteTests`: 11 passed.
- Full `scripts/test-routing.py`: 715 passed.
- `scripts/generate-route-index`: 232 live skills.
- `scripts/lint-skills`: Gate PASS; 0 critical, 0 warnings, 44 informational findings; 234 hub members, 0 orphans.
- `git diff --check`: passed.

## Boundaries

No skill/runtime installation, symlink sync, commit, push, merge, publication, external mutation, worktree creation, package execution, or subagent run was performed. The dirty worktree's unrelated changes were left untouched. Catalog-wide semantic reconciliation remains pending.

