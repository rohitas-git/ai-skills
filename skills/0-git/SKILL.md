---
name: 0-git
description: >
  Domain hub for safe Git workflows: worktrees, atomic commits, PR splitting, conflicts, and branch completion.
  Use when: the user asks for Git operations or the correct Git workflow is unclear.
  Not for: implementing product code (0-implement), reviewing code quality (0-review), or release rollout (1-shipping-and-launch).
  Hub: /0-git.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-git
    role: hub
    when:
      - "route Git work across isolation, commits, PR splitting, conflicts, and branch completion"
    not_when:
      - "implement product changes → 0-implement"
      - "review code quality → 0-review"
      - "plan a release rollout → 1-shipping-and-launch"
    next: [1-git-worktrees, 1-atomic-git-commits, 1-pr-splitter, 1-git-changelog, 1-git-text-normalization, 1-resolving-merge-conflicts, 1-github-cli, 1-github-pr-comment-intake, 1-pr-comment-drafter, 1-pr-summarizer, 1-pr-repair, 1-pr-review-and-repair, 1-stacked-pr-repair, 1-stacked-pr-review-and-repair, 1-finish-branch]
    cousins: [0-implement, 0-review]
    triggers: ["split large PR", "plan stacked PRs", "git workflow", "git help", "commit changes", "git changelog", "generate changelog", "binary diff", "git text normalization", "GitHub CLI", "gh issue", "gh repo", "gh release", "merge conflict", "finish branch", "fetch PR comments", "PR comment intake", "draft PR comment", "write PR description", "repair PR", "review and fix PR", "fix PR findings one by one", "review PR stack", "repair PR stack"]
    requires_setup: false
---

# Git

Route Git operations to one focused workflow. Never broaden an operation into a push, merge, cleanup, or history rewrite without authority.

## Dispatch

| Need | Skill |
|------|-------|
| Isolated workspace for feature work | `/1-git-worktrees` |
| Group, stage, verify, and commit changes | `/1-atomic-git-commits` |
| Draft changelog or release summary from local Git history | `/1-git-changelog` |
| Diagnose binary text diffs or normalize scoped encoding/EOL/attributes | `/1-git-text-normalization` |
| Split one large PR into coherent smaller PRs and track review drift | `/1-pr-splitter` |
| Resolve an active merge or rebase conflict | `/1-resolving-merge-conflicts` |
| Perform an explicitly requested GitHub CLI operation | `/1-github-cli` |
| Fetch and classify GitHub PR discussion | `/1-github-pr-comment-intake` |
| Draft one PR response or status comment | `/1-pr-comment-drafter` |
| Repair known findings and blockers on one PR, without review | `/1-pr-repair` |
| Review one PR, fix each in-scope finding one by one, then repeat review until clean | `/1-pr-review-and-repair` |
| Repair known findings and blockers across a PR stack, without review | `/1-stacked-pr-repair` |
| Review, repair, rebase, and verify a PR stack | `/1-stacked-pr-review-and-repair` |
| Choose merge, PR, retain, or cleanup after green | `/1-finish-branch` |
| Draft the main PR description | `/1-pr-summarizer` |

## Process

1. Inspect repository and operation state without mutating it.
2. Ask **F-G1** when the Git operation is unclear; recommend the narrowest matching workflow.
3. Load only the selected child.
4. Return to the requesting workflow with the child's evidence and preserved workspace state. A direct operation ends with its result; the pipeline and `next` list do not authorize every subsequent action.

## Fork

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-G1** | What Git operation is needed? | infer the narrowest operation from repository state | worktree · atomic commits · changelog · text normalization · conflict resolution · GitHub CLI operation · PR comment intake · PR comment draft · PR description · PR splitting · single-PR repair-only · single-PR review+repair · stack repair-only · stacked review+repair · finish branch · **Agent judgment** |
| **F-G3** | What is the intended base-to-tip PR order? | derive parent-child edges; stop if ambiguous | user order · provider/stack-tool order · **Agent judgment** |
| **F-G2** | How should mixed changes be grouped? | by independently revertible behavior | proposed atomic groups · user-specified grouping · leave ambiguous changes uncommitted · **Agent judgment** |
| **F-G4** | Which PR should be reviewed and repaired? | current branch's unique open PR | user-named PR · unique current-branch PR · **Agent judgment** |
| **F-G5** | What PR prose is needed? | main PR description | PR description → `1-pr-summarizer` · individual comment → `1-pr-comment-drafter` · **Agent judgment** |
| **F-G6** | How should these PRs depend on each other? | derive dependencies from coherent review units | stacked · parallel · foundation plus parallel follow-ups · **Agent judgment** |

## Pipeline

```text
1-git-worktrees? → return to requesting implementation/repair workflow
implementation → 1-atomic-git-commits (authorized) → return to caller
branch-outcome request → 1-finish-branch → 1-pr-summarizer? (chosen PR option)
active conflict → 1-resolving-merge-conflicts → resume interrupted operation
binary diff/encoding/EOL issue → 1-git-text-normalization diagnose|authorized fix → return to caller

large source PR → 1-pr-splitter → 1-pr-summarizer?
known PR findings/blockers → 1-pr-repair → 1-pr-summarizer?
GitHub PR discussion → 1-github-pr-comment-intake → 1-receive-review | 1-pr-repair
outbound PR comment → 1-pr-comment-drafter → 1-github-cli (authorized post/edit)
one PR → 1-pr-review-and-repair → 1-pr-summarizer?
known stack findings/blockers → 1-stacked-pr-repair → 1-pr-summarizer?
stack of PRs → 1-stacked-pr-review-and-repair → 1-pr-summarizer?
```

## Boundary

Git owns repository-state transitions. Product construction stays `/0-implement`; review judgment stays `/0-review`.
Text normalization does not imply staging or a commit; `/1-atomic-git-commits` is a separate optional effect.

## Shared reference

Single and stacked PR repair children load [PR repair checkpoints](./references/pr-repair-checkpoints.md) for workspace identity, scope reconstruction, contract reconciliation, and CI provenance. Read-only Git intake and prose need no worktree setup; mutation helpers retain the caller's checked workspace.

## Conditional methods

Load only for the requested phase, within this skill’s authority: [Bounded PR status and repair modes](./references/babysit-modes.md).
