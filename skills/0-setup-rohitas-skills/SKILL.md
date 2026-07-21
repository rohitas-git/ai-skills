---
name: 0-setup-rohitas-skills
description: >
  Configure a consumer repo for Rohitas engineering skills (issue tracker, domain docs,
  optional vault, opt-in triage labels). Use when first setting up agent skills for a repo or switching
  trackers. Not for: day-to-day triage of issues (0-triage), writing specs (1-to-spec). Hub: /0-setup-rohitas-skills.
  Triggers: setup skills, configure issue tracker, agent skills setup.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-setup-rohitas-skills
    role: hub
    when:
      - "first-time repo setup for engineering skills"
      - "switch issue tracker / domain SSOT"
    not_when:
      - "triage incoming issues → 0-triage (opt-in)"
      - "implement tickets → 0-implement"
    next: [0-grilling, 0-implement]
    triggers:
      - "setup skills"
      - "configure issue tracker"
      - "0-setup-rohitas-skills"
    requires_setup: false
---

# Setup Rohitas Skills

Scaffold the per-repo configuration that the engineering skills assume:

- **Issue tracker** — where issues live (GitHub by default; local markdown is also supported out of the box)
- **Domain docs** — where `CONTEXT.md` and ADRs live, and the consumer rules for reading them
- **Vault root** (optional) — SSOT path for personal vault skills
- **Triage labels** (opt-in) — only if the user wants `/0-triage` for incoming issues/PRs

This is a prompt-driven skill, not a deterministic script. Explore, present what you found, confirm with the user, then write.

## Process

### 1. Explore

Look at the current repo to understand its starting state. Read whatever exists; don't assume:

- `git remote -v` and `.git/config` — is this a GitHub/GitLab repo? Which one?
- `AGENTS.md` and `CLAUDE.md` at the repo root — does either exist? Is there already an `## Agent skills` section in either?
- `CONTEXT.md` and `CONTEXT-MAP.md` at the repo root
- `docs/adr/` and any `src/*/docs/adr/` directories
- `docs/agents/` — does this skill's prior output already exist?
- `.scratch/` — sign that a local-markdown issue tracker convention is already in use
- Is the `0-triage` skill available? (informational only — does **not** force triage setup)
- Monorepo signals — a `pnpm-workspace.yaml`, a `workspaces` field in `package.json`, or a populated `packages/*` with its own `src/`. Present only in a genuinely large multi-package repo; their absence means single-context, which is almost every repo.

### 2. Present findings and ask

Summarise what's present and what's missing. Then take the sections in order — one section, one answer, then the next.

Lead each section with the recommended answer so the user can accept it in a word. Give a one-line explainer only when the choice genuinely branches; skip the section entirely when exploration already settled it (Section C when there's no monorepo; Section T when user declines opt-in).

**Section A — Issue tracker.**

> Explainer: The "issue tracker" is where issues live for this repo. Skills like `1-to-tickets`, `1-to-spec`, and (if configured) `0-triage` read from and write to it — they need to know whether to call `gh issue create`, write a markdown file under `.scratch/`, or follow some other workflow you describe. Pick the place you actually track work for this repo.

Default posture: these skills were designed for GitHub. If a `git remote` points at GitHub, propose that. If a `git remote` points at GitLab (`gitlab.com` or a self-hosted host), propose GitLab. Otherwise (or if the user prefers), offer:

- **GitHub** — issues live in the repo's GitHub Issues (uses the `gh` CLI)
- **GitLab** — issues live in the repo's GitLab Issues (uses the [`glab`](https://gitlab.com/gitlab-org/cli) CLI)
- **Local markdown** — issues live as files under `.scratch/<feature>/` in this repo (good for solo projects or repos without a remote)
- **Other** (Jira, Linear, etc.) — ask the user to describe the workflow in one paragraph; the skill will record it as freeform prose

Record the choice in `docs/agents/issue-tracker.md`. The GitHub and GitLab templates carry a "PRs as a request surface" flag, defaulted **off** — leave it off and don't raise it during core setup; a user who later enables triage can flip the flag in the file if external PRs should enter the triage queue.

**Section C — Domain docs.** Default to **single-context** — one `CONTEXT.md` + `docs/adr/` at the repo root. This fits almost every repo; write it without asking.

Offer **multi-context** — a root `CONTEXT-MAP.md` pointing to per-context `CONTEXT.md` files — only when exploration found monorepo signals. Then confirm which layout they want.

**Section V — Vault root (optional).** Skip if the user has no vault and does not want one configured. Otherwise record `docs/agents/vault.md` (see step 4b).

**Section T — Triage labels (opt-in only).** Do **not** open label vocabulary unless the user opts in.

First ask **F2** (always, once — even if `0-triage` is installed):

> **Configure `/0-triage` for this repo?** (recommended: **No**)
>
> **What triage is:** `/0-triage` sorts *incoming* issues/PRs from humans through labels (`needs-triage` → `ready-for-agent` / `ready-for-human` / `needs-info` / `wontfix`) and writes agent briefs. It is an on-ramp for raw tracker work — **not** part of grill → `1-to-spec` → `1-to-tickets` → implement. Do **not** re-triage tickets produced by `1-to-tickets`.
>
> Skip if you mostly create work via skills (spec/tickets) rather than managing a human issue queue.

Branches: **No** (skip triage entirely) · **Yes** (configure labels) · **Agent judgment**.

- On **No** / Agent judgment that declines: skip the rest of Section T. Write no `triage-labels.md` and no `### Triage labels` block.
- On **Yes**: only if `0-triage` is available. If it is not installed, say so and skip labels (offer installing later). If it is installed, ask exactly one follow-up:

> Do you want to keep the default 0-triage labels? (recommended: **yes**)

The defaults are the five canonical roles, each label string equal to its name: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. On **yes**, write them as-is. Only if the user says no — usually because their tracker already uses other names — collect the overrides so `0-triage` applies existing labels instead of creating duplicates.

### 3. Confirm and edit

Show the user a draft of:

- The `## Agent skills` block to add to whichever of `CLAUDE.md` / `AGENTS.md` is being edited (see step 4 for selection rules)
- The contents of `docs/agents/issue-tracker.md`, `docs/agents/domain.md`, and optionally `docs/agents/vault.md` / `docs/agents/triage-labels.md` (triage only when Section T ran and user opted in)

Let them edit before writing.

### 4. Write

**Pick the file to edit:**

- If `CLAUDE.md` exists, edit it.
- Else if `AGENTS.md` exists, edit it.
- If neither exists, ask the user which one to create — don't pick for them.

Never create `AGENTS.md` when `CLAUDE.md` already exists (or vice versa) — always edit the one that's already there.

If an `## Agent skills` block already exists in the chosen file, update its contents in-place rather than appending a duplicate. Don't overwrite user edits to the surrounding sections.

The block (core — always):

```markdown
## Agent skills

### Issue tracker

[one-line summary of where issues are tracked]. See `docs/agents/issue-tracker.md`.

### Domain docs

[one-line summary of layout — "single-context" or "multi-context"]. See `docs/agents/domain.md`.
```

Add **only when opted in / configured**:

```markdown
### Triage labels

[one-line summary of the label vocabulary]. See `docs/agents/triage-labels.md`.
```

```markdown
### Vault root

[one-line path or "not configured"]. See `docs/agents/vault.md`.
```

Include the `### Triage labels` sub-block, and write `docs/agents/triage-labels.md`, **only** when Section T ran with user opt-in. When it did not, both are omitted.

Then write the docs files using the seed templates in this skill folder as a starting point:

- [issue-tracker-github.md](./issue-tracker-github.md) — GitHub issue tracker
- [issue-tracker-gitlab.md](./issue-tracker-gitlab.md) — GitLab issue tracker
- [issue-tracker-local.md](./issue-tracker-local.md) — local-markdown issue tracker
- [domain.md](./domain.md) — domain doc consumer rules + layout
- [triage-labels.md](./triage-labels.md) — label mapping (**only** if Section T opted in)
- [vault.md](./vault.md) — vault root SSOT (**only** if Section V ran)

For "other" issue trackers, write `docs/agents/issue-tracker.md` from scratch using the user's description.

### 4b. Vault root SSOT (optional but recommended)

If personal vault skills (`0-rohitas-vault-wiki`, `vault-*`, `1-wiki-query`) will run against this machine, record the vault root once:

Write `docs/agents/vault.md` with:

```markdown
# Vault root (SSOT)

Absolute path to the Obsidian vault root used by personal vault skills.

- **vault_root:** `/path/to/vault`
- **notes:** edit this file when the vault moves; vault skills must read this path (or the `## Agent skills` vault pointer) instead of hard-coding home paths.
```

Skip this section if the user has no vault and does not want one configured.

### 5. Done

Tell the user the setup is complete and which engineering skills will now read from these files. Mention they can edit `docs/agents/*.md` directly later — re-running this skill is only necessary if they want to switch issue trackers or restart from scratch.

**Soft mention (once, when triage was skipped):**

> Optional later: `/0-triage` can sort *incoming* human issues/PRs into ready-for-agent/human. Not needed for grill → tickets → implement. To add labels, re-run `/0-setup-rohitas-skills` and answer **Yes** to the triage question (F2).

Do **not** open the full label questionnaire after Done unless the user asks in the same turn.
