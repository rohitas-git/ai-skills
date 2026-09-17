---
name: 0-setup-rohitas-skills
description: >
  Route first-time repository setup for Rohitas engineering skills to one focused configuration task.
  Use when: setting up skills, switching a tracker, or configuring domain docs, vault, or triage labels.
  Not for: day-to-day triage (0-triage) or implementation (0-implement). Hub: /0-setup-rohitas-skills.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-setup-rohitas-skills
    role: hub
    when: ["first-time repository setup for engineering skills", "switch repo configuration"]
    not_when: ["triage incoming issues → 0-triage", "implement tickets → 0-implement"]
    prev: [0-butler]
    next: [1-setup-issue-tracker, 1-setup-domain-docs, 1-setup-vault-root, 1-setup-triage-labels]
    cousins: [1-git-worktrees, 0-skill-manager, 0-triage]
    triggers: [setup skills, configure issue tracker, configure domain docs, configure vault root, configure triage labels]
    requires_setup: false
---

# Setup Rohitas Skills

**Atomic job:** route a repository-configuration request to one focused setup task. Do not configure unrelated systems in the same pass.

## Boundary

| Need | Skill |
|---|---|
| Choose the setup task | **this hub** |
| Configure issue-tracker SSOT | `/1-setup-issue-tracker` |
| Configure domain-doc layout | `/1-setup-domain-docs` |
| Record personal vault root | `/1-setup-vault-root` |
| Opt into triage-label mapping | `/1-setup-triage-labels` |
| Triage incoming work | `/0-triage` |

This hub only selects a setup child. It does not edit repository files, create
worktrees, mutate issue trackers or vaults, commit, push, or continue into
day-to-day work.

## Input and workspace contract

Before routing, identify the target consumer repository and record its exact
worktree path, branch or detached state, `HEAD`, dirty-state ownership, active
instruction file, and the paths the requested setup may change.

- Read-only inventory creates no worktree.
- If setup writes are authorized, use the task's matching non-protected
  workspace. Route required isolation to `/1-git-worktrees`, then resume here.
- A worktree isolates files and Git state, not tracker accounts, vaults,
  credentials, ports, databases, or other shared services.
- Never stash, clean, reset, switch branches, or overwrite unrelated dirty
  work merely to make setup convenient.

## Process

1. Inspect existing `AGENTS.md`/`CLAUDE.md`, `docs/agents/`, and relevant
   repository conventions without changing them.
2. If the user explicitly named one setup task, route directly. Otherwise ask
   F-S1 once.
3. Hand exactly one child the pinned repository/worktree identity, current
   contents, allowed paths, dirty-state ownership, and write authority.
4. Require the child to return the proposed or applied diff, verification
   evidence, and any unresolved external setup. Never replace surrounding user
   instructions.
5. Stop after that child. A fresh repository may need issue-tracker setup and
   domain-doc setup, but those remain separate invocations.

## Fork F-S1

**What should be configured now?**

- **Issue tracker** — recommended for a new repo; `/1-setup-issue-tracker`
- **Domain docs** — `/1-setup-domain-docs`
- **Vault root** — `/1-setup-vault-root`
- **Triage labels** — `/1-setup-triage-labels`
- **Agent judgment** — pick the narrowest missing prerequisite

## Shared assets

Children reuse the templates in this directory: issue tracker templates,
[domain.md](./domain.md), [vault.md](./vault.md), and
[triage-labels.md](./triage-labels.md). These are starting points, not active
configuration until the selected child adapts and writes them into the
authorized consumer repository.
