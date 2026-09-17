---
name: 1-pr-comment-drafter
description: >
  Draft one evidence-backed Markdown response or status comment for a pull request without posting it.
  Use when: reply to a PR review comment, draft a PR status update, or write a concise PR decision request.
  Not for: collecting comments (1-github-pr-comment-intake), PR descriptions (1-pr-summarizer),
  evaluating feedback (1-receive-review), or posting to GitHub (1-github-cli). Hub: /0-git.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-git
    role: leaf
    when:
      - "draft one outbound response or status comment for a pull request"
    not_when:
      - "collect existing PR discussion → 1-github-pr-comment-intake"
      - "draft PR description → 1-pr-summarizer"
      - "evaluate review feedback → 1-receive-review"
      - "post/edit GitHub comment → 1-github-cli"
    next: [1-github-cli]
    cousins: [1-github-pr-comment-intake, 1-pr-summarizer, 1-receive-review, 1-github-cli]
    triggers: [draft PR comment, reply to PR review, write PR status update, PR response draft]
    requires_setup: false
---

# PR Comment Drafter

Draft one precise, reviewer-readable PR comment from verified evidence. Return Markdown only;
do not post, edit, resolve, approve, commit, push, or merge.

## Boundary

| Need | Skill |
|---|---|
| Draft one response, update, or decision-request comment | **this skill** |
| Collect existing review discussion | `/1-github-pr-comment-intake` |
| Write the PR's main description | `/1-pr-summarizer` |
| Assess whether review feedback is correct | `/1-receive-review` |
| Post or edit the comment remotely | `/1-github-cli` |

## Process

1. **Identify the message.** Capture the PR, intended audience, exact thread or top-level target when known, and one purpose: response, implementation update, CI/status update, or decision request.
2. **Ground every claim.** Use only verified code, test, CI, or discussion evidence. If a review comment has not been assessed, state that it is being investigated rather than agreeing, rejecting, or promising a fix.
3. **Draft the smallest useful Markdown.** Lead with the conclusion, then include only relevant evidence, changed paths/commands when useful, and the next action or explicit question. Use real paragraph breaks and bullets. Preserve intentional literal escapes in quoted code; never substitute escaped newline text for paragraph separators.
4. **Check tone and scope.** Be direct, respectful, and non-defensive. Do not expose credentials, internal-only data, speculative root causes, unrelated cleanup, or claims of tests/CI passing without evidence.
5. **Hand off deliberately.** Return the draft plus its intended target to the caller. No checkout/worktree changes are needed for drafting. Route publication to `/1-github-cli` only when requested, carrying existing authority and the exact comment/thread target for read-back verification.

## Output shape

```markdown
<Evidence-supported conclusion or current status>.

- Evidence: <path, command, or observed result>
- Change/status: <what happened>

<next action or focused question>
```

For a blocker, lead with `Blocked:` and state the smallest decision or access needed.

## Related

Inbound discussion → `/1-github-pr-comment-intake`; validated feedback → `/1-receive-review`;
remote posting → `/1-github-cli`.
