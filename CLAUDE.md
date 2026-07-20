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
2. **Depth-prefix names (hard):** live `name` / dir / slash / hub package = `{depth}-{kebab-slug}` from **hub-tree depth** (0 … max tree depth; **no artificial cap**).
   - **0-** = ★ domain hubs (incl. `0-butler`) — hub identity wins even if dual-listed elsewhere
   - **1-** = children of domain hubs; **sub-hubs** at parent+1 (today often 1)
   - **2-** = children of depth-1 hubs (e.g. under a sub-hub → `2-verify-work`)
   - **3- / 4- / 5- / 6- / …** = same recurrence: `max(parent_hub_depth + 1)` (nested sub-hubs and their children)
   - Dual membership: depth uses **deepest** hub parent; optional `"primary": true` is for ownership/docs only
   - No bare unprefixed live skills. Detail: `skills/0-skill-manager/references/depth-prefix-names.md`. Lint: `depth-prefix`, `depth-graph` critical.
3. Dual membership is **logical only** (hubs + flows) — no second copy/symlink.
4. Route: **`/0-butler`**. Mutate: **`/0-skill-manager`**. Lint: **`/1-skill-linter`** (Gate: PASS on place/ingest).
5. place: `inbox/<name>` → `skills/<name>` + hub slot + `wikis/index.md` + `wikis/log.md` (name already depth-prefixed).
6. deprecate: `skills/<name>` → `archive/<name>`.
7. new-hub: write `hubs/0-{hub}/` (depth **0** hub skill + package).
8. Main `SKILL.md` stays lean; depth in `references/`.
9. **`disable-model-invocation: true` by default.** Only omit it for true always-on skills (today: `1-coding-standards`, `0-ponytail`). Prefer user/butler invoke over auto-steal.
10. **Forks** always offer **Agent judgment** — agent picks the best branch and proceeds without further questions on that fork.

## Forbidden

- Second meta-router · promoting `using-agent-skills` · discovering `archive/` · inventing skills not on disk + flows · silent fork branches without **Agent judgment** option · **unprefixed live skill names** (must be `N-slug`).
