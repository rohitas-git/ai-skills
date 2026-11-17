---
name: 1-living-documentation-governor
description: >
  Govern the explicit contract between changed code/configuration and its canonical living docs.
  Use for documentation drift, doc ownership/placement, code-to-doc trigger maps, or updating docs
  with a scoped implementation. Not for: a source-ingestion concept wiki
  (1-project-wiki-manager), inline/API comments (1-code-comments), or personal Obsidian notes
  (0-rohitas-vault-wiki). Hub: /0-improve-codebase-architecture.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-improve-codebase-architecture
    role: soft
    when:
      - "assess or repair drift between changed code/configuration and canonical living docs"
      - "design a bounded code-to-doc ownership or trigger contract"
      - "bootstrap scoped source-grounded component contracts and parent documentation maps"
    not_when:
      - "source-ingestion project wiki → 1-project-wiki-manager"
      - "inline or public API comments → 1-code-comments"
      - "personal Obsidian vault → 0-rohitas-vault-wiki"
    prev: [0-improve-codebase-architecture, 0-implement]
    cousins: [1-project-wiki-manager, 1-domain-modeling, 1-code-comments, 1-ci-cd-and-automation, 1-git-worktrees]
    triggers: [living documentation, documentation drift, keep docs in sync with code, doc triggers, code to docs mapping, EGM bootstrap, EGM drift report]
    requires_setup: false
---

# Living Documentation Governor

**Atomic job:** keep one scoped code/configuration candidate and its canonical current documentation
truthfully aligned, or return evidence that they are not.

## Boundary

| Need | Route |
|---|---|
| Code↔living-doc ownership, drift, trigger, or scoped update | **this skill** |
| Source corpus → concept wiki | `/1-project-wiki-manager` |
| Design-time glossary or ADR decision | `/1-domain-modeling` |
| Inline/API comments | `/1-code-comments` |
| Implement/check CI enforcement | `/1-ci-cd-and-automation` through `/0-implement` |
| Changelog/release notes | `/1-git-changelog` or `/1-shipping-and-launch` |

F-D1 applies only when concept-wiki versus code-synced-doc intent is unclear. Clear requests route
directly and preserve their caller.

## Process

1. **Pin caller and candidate.** Record repository, exact worktree/branch/HEAD, requested base/head or
   PR endpoints, task scope, dirty-file ownership, and assess/update/design authority. Include the
   caller-owned committed, staged, unstaged, and untracked surfaces when relevant. This skill creates
   no worktree and switches no branch.
2. **Discover local authority.** Read repository instructions, current docs/index/ownership, ADR and
   archive conventions, configured doc checks, trigger map, and changed source. Do not initialize a
   docs tree, trigger system, hook, or CI job merely because none exists.
3. **Choose one mode.** Drift assessment is read-only. A scoped implementation caller may update
   canonical docs in its existing worktree. Designing a trigger/ownership contract returns a proposal;
   implementing scripts, CI, or hooks requires the requested Ship/CI workflow.
4. **Match claim to evidence.** Current repository behavior comes from the pinned code/config/tests;
   public contract from the governing schema/spec; intended rationale from accepted decisions; and
   deployed behavior from deployment/runtime evidence. No universal source-precedence list can answer
   every question. Archive is historical unless explicitly reactivated.
5. **Evaluate obligations.** Map changed paths/behavior to canonical owners and trigger rules. A
   matching doc filename or no-op edit is not proof of semantic alignment. Require an addressing doc
   delta or an explicit reviewable attestation with rationale. See [trigger enforcement](./references/trigger-enforcement.md).
6. **Make only authorized doc changes.** Update the existing canonical owner and navigation/ownership
   metadata required by local conventions. Do not create a duplicate guide, rewrite accepted history,
   edit source code, or create an ADR unless that separate decision workflow selected it.
7. **Verify and return.** Run existing doc checks and inspect the scoped diff; validate links, trigger
   targets, candidate coverage, assertions against source evidence, and unchanged protected files.
   Return paths/findings, worktree/candidate identity, checks, exemptions, gaps, and limits to the
   caller. Do not commit, publish, deploy, merge, install tools, fetch/switch branches, stash work, or
   mutate remote/shared services.

## Progressive disclosure

- EGM component-contract bootstrap or spec-to-code drift: [bounded contracts and drift](./references/egm-contracts-and-drift.md)
- Operating detail and placement: [full guide](./references/full-guide.md), [placement examples](./references/knowledge-placement-examples.md)
- Trigger schema/checking: [trigger enforcement](./references/trigger-enforcement.md), [example map](./references/generalized-doc-triggers.json)
- Optional hook trade-offs: [hook setup](./references/git-hooks-setup.md)
- Page/README baselines: [page template](./references/page-template.md), [README skeleton](./references/project-readme-skeleton.md)
- ADR boundary: [ADR criteria](./references/adr-criteria-examples.md)
- Read-only questions: [Q&A contract](./references/qa-response-template.md)
- Historical source only: [vendor guide](./references/vendor-docs-adrs-full.md)
