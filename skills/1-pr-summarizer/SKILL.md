---
name: 1-pr-summarizer
description: >
  Draft a reviewer-ready pull-request description from verified intent, change, and validation evidence.
  Use when: write a PR description, summarize a PR for reviewers, or prepare a branch change summary.
  Not for: drafting a single PR comment (1-pr-comment-drafter), collecting review threads (1-github-pr-comment-intake),
  posting to GitHub (1-github-cli), or creating commits (1-atomic-git-commits). Hub: /0-git.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-git
    role: soft
    when:
      - "draft a reviewer-ready pull-request description from existing evidence"
      - "summarize a branch or PR for reviewers"
    not_when:
      - "draft one PR response/comment → 1-pr-comment-drafter"
      - "collect review threads → 1-github-pr-comment-intake"
      - "post or edit a remote PR → 1-github-cli"
      - "create commits → 1-atomic-git-commits"
    next: [1-github-cli]
    cousins: [1-pr-comment-drafter, 1-github-cli, 1-github-pr-comment-intake, 1-atomic-git-commits]
    triggers: [pr summarizer, write PR description, summarize changes for PR, reviewer-ready PR summary, prepare PR description]
    requires_setup: false
---

# PR Summarizer

Turn verified intent, decisions, diff evidence, and validation results into one concise,
reviewer-ready PR description. Draft only; never create, edit, or post a PR.

## Boundary

| Need | Skill |
|---|---|
| Draft the main PR description | **this skill** |
| Draft one response or status comment | `/1-pr-comment-drafter` |
| Collect existing PR discussion | `/1-github-pr-comment-intake` |
| Post PR prose remotely | `/1-github-cli` |
| Group and commit changes | `/1-atomic-git-commits` |

## Process

1. **Gather evidence.** Pin repository, PR or local branch, declared base and head SHAs, stated problem, linked issue/spec, PR template, final diff, decisions, and actual validation output. Distinguish local-only changes from the published PR. Ask one focused question if the why is unavailable; never infer it from filenames alone. Drafting needs no worktree creation or checkout mutation.
2. **Assess reviewability.** Group the change by behavior, not file order. Flag mixed-purpose or unusually broad changes as reviewer notes only when the evidence supports a possible independent split.
3. **Draft the repository template.** Preserve required headings. Otherwise scale the compact shape below to the change: a small fix may need just a short explanation and validation. Rewrite around the final behavior after scope changes; omit abandoned work and conversation history unless needed to explain a current trade-off.
4. **Audit claims.** Include only tests actually run, observed risks, known limitations, migrations, rollout requirements, and explicitly unknown items. Associate CI/test evidence with its tested revision; a green result from an earlier PR head does not validate later changes. Do not manufacture metrics, status, issue links, or claims that all CI passed.
5. **Return Markdown and handoff.** Provide the title, body, and intended head/base to the caller. `/1-github-cli` publishes only when requested; `next` is conditional, not an automatic post.

## Default shape

```markdown
## Summary
<what changed and why, in 1–3 sentences>

## Changes
- <behavior-focused change group>
- <behavior-focused change group>

## Validation
- `<command>` — <observed result>

## Risk / reviewer notes
- <migration, rollout, limitation, or focused review guidance>
```

## Related

For individual comment prose use `/1-pr-comment-drafter`; for remote publication use
`/1-github-cli` after explicit authorization. Adapted from the
[community PR-enhancement source](./references/vendor-source.md).
