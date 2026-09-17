---
name: 1-setup-triage-labels
description: >
  Configure the opt-in label mapping used by 0-triage in one repository. Use when enabling or changing
  triage labels. Not for: actually triaging incoming work. Hub: /0-setup-rohitas-skills.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-setup-rohitas-skills
    role: leaf
    when: ["configure triage labels", "enable 0-triage labels"]
    not_when: ["sort incoming issues → 0-triage", "configure issue tracker → 1-setup-issue-tracker"]
    prev: [0-setup-rohitas-skills]
    next: [0-setup-rohitas-skills]
    cousins: [1-setup-issue-tracker, 0-triage]
    triggers: [setup triage labels, enable triage, configure 0-triage]
    requires_setup: false
---

# Setup Triage Labels

**Atomic job:** configure one repository-local mapping from `/0-triage` roles to
tracker label strings. Do not create labels or triage work.

## Required inputs

Pin the repository root, exact worktree path, branch or detached state, `HEAD`,
dirty-state ownership, applicable instructions file, issue-tracker SSOT, allowed
paths, desired mapping, and write authority. Default outputs are
`docs/agents/triage-labels.md` plus one relative pointer.

- Read-only inspection creates no worktree and does not query the remote tracker.
- For authorized writes, use the matching non-protected worktree. If isolation
  is needed, return through `/0-setup-rohitas-skills` to `/1-git-worktrees`, then
  resume this task.
- A worktree does not isolate tracker accounts, label vocabularies, or issues.
- Never stash, reset, clean, switch branches, or overwrite unrelated dirty work.

## Process

1. Confirm `/0-triage` and the issue-tracker SSOT are available. An explicit
   configure/enable request supplies opt-in; do not add a second confirmation gate.
2. Start from the five canonical roles: `needs-triage`, `needs-info`,
   `ready-for-agent`, `ready-for-human`, and `wontfix`. Honor explicit repository
   label strings; otherwise default each role to its canonical name. Do not claim
   a remote label exists without current evidence.
3. Adapt [triage-labels.md](../0-setup-rohitas-skills/triage-labels.md). Require
   every canonical role exactly once, a non-empty target string, and no duplicate
   target that would collapse distinct states unless the user explicitly accepts
   that loss of distinction.
4. Preview when requested or when a mapping is ambiguous. With direct write
   authority, create or minimally update the local mapping and exactly one
   relative pointer in the applicable existing instructions file. Ask before
   creating `AGENTS.md` or `CLAUDE.md` when no convention selects one.
5. Re-read both outputs, validate the mapping and pointer, inspect the scoped
   diff, and verify a second application would not duplicate the block or pointer.
6. Return the pinned candidate, proposed/applied paths, mapping validation, diff
   summary, verification result, and any unknown remote-label existence to
   `/0-setup-rohitas-skills` or the direct caller. Stop.

## Boundary

Local mapping only. Do not create, rename, delete, or apply remote labels; do not
read or triage issues; do not authenticate, commit, push, or merge. Remote label
administration needs separately scoped tracker authority. Sort and brief incoming
work through `/0-triage`.
