---
name: 1-setup-issue-tracker
description: >
  Configure one repository's issue-tracker SSOT for engineering skills. Use when setting GitHub, GitLab,
  local markdown, or another tracker. Not for: triaging issues (0-triage) or domain-doc setup (1-setup-domain-docs).
  Hub: /0-setup-rohitas-skills.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-setup-rohitas-skills
    role: leaf
    when: ["configure issue tracker", "set GitHub/GitLab/local tracker"]
    not_when: ["triage incoming issues → 0-triage", "configure domain docs → 1-setup-domain-docs"]
    prev: [0-setup-rohitas-skills]
    next: [0-setup-rohitas-skills]
    cousins: [1-setup-domain-docs, 1-setup-triage-labels]
    triggers: [setup issue tracker, configure GitHub issues, configure GitLab issues, local markdown tracker]
    requires_setup: false
---

# Setup Issue Tracker

**Atomic job:** configure one consumer repository's local issue-tracker SSOT and
one pointer to it. Do not operate the tracker.

## Required inputs

Pin the target repository root, exact worktree path, branch or detached state,
`HEAD`, dirty-state ownership, applicable agent-instructions file, allowed paths,
requested tracker, and write authority. Default outputs are
`docs/agents/issue-tracker.md` plus one pointer in that instructions file.

- Read-only inspection creates no worktree.
- For authorized writes, use the matching non-protected worktree. If isolation is
  needed, return through `/0-setup-rohitas-skills` to `/1-git-worktrees`, then
  resume this same setup task.
- A worktree does not isolate tracker projects, accounts, credentials, labels,
  issues, or pull/merge requests.
- Never stash, reset, clean, switch branches, or overwrite unrelated dirty work.

## Process

1. Inspect repository remotes, `.scratch/`, the current SSOT, and the applicable
   agent-instructions hierarchy without changing them. Do not authenticate to or
   query a tracker merely to choose a template.
2. Honor an explicitly named tracker. Otherwise infer GitHub or GitLab only from
   an unambiguous remote; use local Markdown only when repository evidence or the
   user selects it. Ask once when evidence conflicts or no choice is grounded.
3. Adapt the matching template from `/0-setup-rohitas-skills`. Record the pinned
   tracker/project convention and command shapes, but state that examples grant no
   external-write authority. For another tracker, use concise user- or
   repository-supplied instructions rather than inventing a workflow.
4. Preview when requested or when resolving ambiguity. With direct write
   authority, create or minimally update the SSOT and exactly one relative pointer
   in the applicable existing instructions file. If no file or convention selects
   `AGENTS.md` versus `CLAUDE.md`, ask before creating one.
5. Re-read both outputs, resolve the pointer, and inspect the scoped diff. Verify
   idempotence: a second application would not duplicate the block or pointer.
6. Return the pinned candidate, changed or proposed paths, diff summary,
   verification result, and any unresolved choice to `/0-setup-rohitas-skills` or
   the direct caller. Stop without configuring another setup concern.

## Boundary

Tracker-location documentation only. Do not create, edit, label, assign, comment
on, close, or otherwise mutate remote issues/PRs/MRs; do not authenticate, commit,
push, or merge. Domain docs → `/1-setup-domain-docs`; label mapping →
`/1-setup-triage-labels`; incoming-work sorting → `/0-triage`.
