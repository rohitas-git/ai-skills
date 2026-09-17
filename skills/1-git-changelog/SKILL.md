---
name: 1-git-changelog
description: >
  Draft a release changelog or team change summary from local Git history. Use when
  comparing tags, releases, or commit ranges. Not for publishing a release, tagging, or
  changing Git history. Hub: /0-git.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-git
    role: leaf
    when:
      - "draft a changelog or release summary from local Git commit history"
    not_when:
      - "publish, tag, or roll out a release → 1-shipping-and-launch"
      - "draft a pull-request description → 1-pr-summarizer"
    next: [1-shipping-and-launch]
    cousins: [1-shipping-and-launch, 1-pr-summarizer, 1-atomic-git-commits]
    triggers: ["git changelog", "generate changelog", "release notes from commits", "compare git tags", "changelog from commits", "summarize commits for release"]
    requires_setup: false
---

# Git changelog

Turn an explicit local Git range into an accurate, reviewer-editable changelog.

## Boundary

| Need | Skill |
|---|---|
| Draft changelog or release summary from a Git range | **this skill** |
| Tag, publish, or roll out a release | `/1-shipping-and-launch` |
| Draft a PR description | `/1-pr-summarizer` |
| Create or reorganize commits | `/1-atomic-git-commits` |

## Process

1. Confirm the repository and range (for example, `v1.2.0..HEAD`). If neither a range nor an intended release boundary is known, ask rather than guessing.
2. Read local history only: commit hash, subject, date, and body as needed. Do not fetch, push, tag, or alter history.
3. Group conventional-commit subjects by user-facing category; retain unclassified commits in an explicit “Other changes” section rather than silently discarding them.
4. Detect breaking changes from `!` markers and `BREAKING CHANGE:` footers. Verify the wording against the diff or linked context when the commit subject is ambiguous.
5. Produce Markdown with the resolved start/end SHAs, categories, and short hashes. Label generated text as a draft and list incomplete or non-conventional history. Return it to the requesting workflow; no worktree setup is needed for read-only history. `/1-shipping-and-launch` applies only to a requested release task.

## Hard rules

- Never create tags, edit `CHANGELOG.md`, publish release notes, or call a remote host unless separately authorized.
- Do not claim semantic-version impact from commit prefixes alone; flag possible breaking changes for human review.
- Exclude merge noise where possible, but preserve a merged change when its commits are unavailable in the requested range.

## Source

Adapted only from the locally safe workflow described by `git-changelog`; no registry code or installer was used. [Source note](./references/vendor-source.md).
