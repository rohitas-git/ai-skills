# Catalog rules (agents)

Hard rules only. Navigation → [README.md](./README.md). Layout detail → [guidelines/layout.md](./guidelines/layout.md). Index → [wikis/index.md](./wikis/index.md).

## Six folders

| Dir | Holds | Discovered? |
|-----|--------|-------------|
| `skills/` | Live skill bodies (`skills/<name>/SKILL.md`) | yes |
| `inbox/` | New / in-progress skills | yes (not promoted) |
| `archive/` | Tombstones + `archive/vendor/` | **no** |
| `hubs/` | Hub packages (`hub.html`, `workflow.json`) | no |
| `guidelines/` | Layout, reorg history, human guides | no |
| `wikis/` | Catalog wiki (`index.md`, `log.md`) | no |

No other top-level directories. Root files: this file, `README.md`, `AGENTS.md`, `skills-lock.json`.

## Skill rules

1. One skill = `skills/<name>/` named after frontmatter `name`.
2. Dual membership is **logical only** (hubs + flows) — no second copy/symlink.
3. Route: **butler**. Mutate: **skill-manager**. Lint: **skill-linter** (Gate: PASS on place/ingest).
4. place: `inbox/<name>` → `skills/<name>` + hub slot + `wikis/index.md` + `wikis/log.md`.
5. deprecate: `skills/<name>` → `archive/<name>`.
6. new-hub: write `hubs/{hub}/`.
7. Main `SKILL.md` stays lean; depth in `references/`.
8. **`disable-model-invocation: true` by default.** Only omit it for true always-on skills (today: `1-coding-standards`, `0-ponytail`). Prefer user/butler invoke over auto-steal.
9. **Forks** always offer **Agent judgment** — agent picks the best branch and proceeds without further questions on that fork.

## Forbidden

- Second meta-router · promoting `using-agent-skills` · discovering `archive/` · inventing skills not on disk + flows · silent fork branches without **Agent judgment** option.
