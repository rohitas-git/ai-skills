---
name: 1-github-cli
description: >
  Use the GitHub CLI (`gh`) for an explicitly requested GitHub repository, issue, pull
  request, or release operation. Read-only inspection is the default. Not for repairing
  PR code or automatic merging/pushing. Hub: /0-git.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-git
    role: leaf
    when:
      - "perform an explicitly requested GitHub CLI repository, issue, pull-request, or release operation"
    not_when:
      - "repair PR code or checks → 1-pr-repair or 1-pr-review-and-repair"
      - "finish a local branch → 1-finish-branch"
      - "merge or push without explicit authorization → stop"
    cousins: [1-github-pr-comment-intake, 1-pr-repair, 1-finish-branch, 1-shipping-and-launch]
    triggers: ["GitHub CLI", "gh issue", "gh repo", "gh release", "GitHub operation", "create GitHub issue", "post PR comment", "inspect GitHub PR"]
    requires_setup: true
---

# GitHub CLI

Use `gh` for one user-authorized GitHub operation, with the repository and effect made explicit.

## Boundary

| Need | Skill |
|---|---|
| One GitHub CLI repository, issue, PR, or release operation | **this skill** |
| Read and classify existing PR discussion | `/1-github-pr-comment-intake` |
| Repair PR code, checks, or findings | `/1-pr-repair` or `/1-pr-review-and-repair` |
| Branch outcome after verification | `/1-finish-branch` |
| Release rollout plan | `/1-shipping-and-launch` |

## Process

1. Confirm `gh` is installed and authenticated. Inspect repository context read-only before any mutation.
2. Identify the exact operation, owner/repository, target object, and effect. Read-only requests may proceed after context verification.
3. For a mutation—creating/editing/commenting/closing an issue or PR, creating/forking a repo, publishing a release—summarize the intended external change and obtain explicit user authorization unless the user already requested that exact action.
4. For a comment edit, identify the exact existing comment; for creation, identify the PR/issue and optional parent thread, then capture the returned new comment ID. Build actual multiline text through a structured tool argument or the CLI's body-file mechanism. Do not use JSON serialization as shell escaping.
5. Read back the exact created/edited object before reporting success. Compare paragraph breaks and content with the intended draft, preserving literal escapes in code samples. Report rendering as verified only if actually observed.
6. Use the narrowest command and preserve templates. Creation is not generally idempotent: after a timeout or uncertain response, inspect whether the intended object already exists before retrying, to avoid duplicate comments, issues, PRs, or releases. Return the resulting URL or identifier.
7. Report the action, target, and result. Never claim remote state without checking the command result.

## Caller and workspace

Return the object URL/ID, resulting state, and any uncertain outcome to the requesting
workflow. Repository selection must be explicit when the current checkout differs
from the target. API inspection/publication needs no new worktree; commands that
would alter a local checkout return to the appropriate Git workflow first.

## Hard rules

- Never merge a PR into `origin/main`, push directly to `origin/main`, delete a repository, or change permissions without explicit user permission.
- Never expose tokens, authentication output, private issue content, or repository secrets.
- Do not broaden a request to create a PR, publish a release, fork, or alter a repository.
- Do not use JSON escaping or shell interpolation as a comment-formatting mechanism; multiline content must survive command construction and read-back verification intact.
- A local branch workflow stays under `/1-finish-branch`; this skill operates the GitHub interface only after the action is authorized.

## Source

Adapted from trumppo's `gh` workflow without downloading its installer or code. [Vendor source](./references/vendor-source.md).
