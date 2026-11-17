---
name: 1-pr-splitter
description: >
  Split one large, complex, messy, or hard-to-review pull request into smaller reviewable PRs.
  Use when: planning stacked PRs, extracting independent branch changes, separating refactors from behavior,
  or preserving original intent while managing review drift in a newly split stack.
  Not for: grouping commits only (1-atomic-git-commits), repairing an existing stack (1-stacked-pr-repair),
  or discovering review findings (1-stacked-pr-review-and-repair). Hub: /0-git.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-git
    role: pipeline
    when:
      - "split one large PR into smaller independently reviewable PRs"
      - "plan stacked or parallel PRs and preserve source intent through review drift"
    not_when:
      - "group commits without splitting PRs → 1-atomic-git-commits"
      - "repair an existing stack → 1-stacked-pr-repair"
      - "discover and repair stack findings → 1-stacked-pr-review-and-repair"
    prev: [0-git]
    next: [1-pr-summarizer]
    cousins: [1-atomic-git-commits, 1-stacked-pr-repair, 1-stacked-pr-review-and-repair]
    triggers: [split PR, split large pull request, extract independent PRs, plan stacked PRs, separate refactor and behavior, track split PR drift]
    requires_setup: false
---

# PR Splitter

Preserve one source PR, extract coherent review units, and account for remaining intent as feedback changes the split.

## Boundary

| Need | Owner |
|---|---|
| Plan or execute a split of one source PR; maintain its split ledger | **this skill** |
| Group, stage, and commit changes | `/1-atomic-git-commits` |
| Repair known blockers across an already established stack | `/1-stacked-pr-repair` |
| Discover and repair stack findings | `/1-stacked-pr-review-and-repair` |
| Resolve an active conflict | `/1-resolving-merge-conflicts` |
| Draft final reviewer-facing descriptions | `/1-pr-summarizer` |

## Process

1. **Pin the request.** Record repository/worktree, branch/HEAD, source PR and tip SHA, intended base and base SHA, dirty ownership, and plan versus execution scope. Inspect `git status`, graph, and repository rules first. Planning stays read-only; a split request authorizes scoped local extraction, while commits, publication, pushes, history rewrites, and deletion require authority from the request. Preserve unrelated edits; use an isolated workspace if necessary, never an automatic stash/reset.
2. **Snapshot before touching history.** Before execution, create a local backup such as `git branch backup/original-large-pr <source-sha>` and record its SHA. Treat that reference as immutable throughout the split. If the name exists, verify it matches the intended snapshot or choose a unique name; never overwrite it. A branch captures committed history only: identify uncommitted source intent separately. Retain the original branch and backup until completion; deletion remains a separate explicit action.
3. **Inventory the source.** Inspect `git diff --stat <base>...<source>`, `git diff --name-only <base>...<source>`, and `git log --oneline <base>..<source>` using pinned revisions, not an assumed current HEAD. Classify prep/refactor, API/types, behavior, tests, docs, cleanup, and generated/lock files. Identify cross-file dependencies and package/release policy.
4. **Start a local ledger.** During execution, create an uncommitted scratchpad, preferably `.notes/pr-split.md`, using the [templates](./references/templates.md). Preserve an existing file; keep notes ignored locally or untracked, and never stage them incidentally. For a planning-only request, return its proposed path and contents without writing. Track extracted files/hunks, verification, release notes, remaining intent, and intentional drift.
5. **Choose review units and topology.** Use stacked PRs for dependencies, parallel PRs only for independent units, or foundation plus parallel follow-ups for shared prep. Group by behavior and review story, not filenames alone. Each PR must build against its immediate base and carry its necessary tests, docs, and generated artifacts. Infer routine choices; use **F-G6** only when a material topology decision remains unresolved.
6. **Extract safely.** Load [extraction and drift](./references/extraction-and-drift.md) before mutation. Prefer fresh branches from the correct base and selective restoration from the snapshot. Use whole paths only for clean ownership; mixed files need hunk selection. Never copy the entire original file over reviewed parent changes. Inspect each candidate's full diff against its immediate base and record extracted and remaining intent.
7. **Verify each PR.** Run the narrowest relevant build, typecheck, lint, and tests against that PR's actual candidate and immediate base. Verify descendants against updated parents. In repositories using Changesets, replace carried-over source changesets with PR-scoped entries under the [release-note procedure](./references/templates.md); otherwise follow repository policy and record why Changesets is inapplicable. Stage exact paths only when committing is authorized.
8. **Manage drift deliberately.** Reviewed decisions become the current direction for the affected behavior. After an authorized earlier-PR change/rebase, update dependents base-to-tip, preserve reviewed intent, and log intentional differences from the snapshot. Use the original diff to locate missing intent, not to force byte-for-byte equality. Run `git range-diff` on recorded old/new ranges after history rewrites or conflict resolution. Summarize meaningful changes before any authorized stack update.
9. **Return evidence.** Report PR sequence, branches and immediate bases, scratchpad path/contents, extraction commands, verification per PR, remaining original intent, drift, and next steps. Separate planned commands from executed results and local checks from provider CI. Use the concise description template; keep the full extraction ledger local. No automatic merge or source cleanup.

## Fork

| Fork | Question | Recommended | Branches |
|---|---|---|---|
| **F-G6** | How should these PRs depend on each other? | derive dependencies from coherent review units | stacked · parallel · foundation plus parallel follow-ups · **Agent judgment** |

## Load when needed

| Need | Reference |
|---|---|
| Execute extraction, restack, compare intent, or summarize range-diff | [Extraction and drift](./references/extraction-and-drift.md) |
| Initialize scratchpad, draft descriptions, or scope Changesets | [Templates and release notes](./references/templates.md) |

## Common failure modes

Avoid file-only splits that break behavior, tests detached from their code, uncompilable descendants, overwritten dirty work, premature source deletion, reverting review feedback, copying the combined changeset into every PR, and force-pushing without a meaningful reviewer summary.

## Related

Parent: `/0-git`. Optional description handoff: `/1-pr-summarizer`. Specialist helpers return here with evidence; their mention does not authorize a separate operation.
