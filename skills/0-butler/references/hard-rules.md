# Butler hard rules (query / orient)

1. **No atoms** — never create wiki/concept pages.
2. **No multi-file catalog writes** — mutations are **`/0-skill-manager`** only.
3. **Never invent skills** — disk + flows.md only.
4. **Never promote `using-agent-skills`**.
5. **Depth-prefix names (hard)** — recommend only live skills as `/{depth}-{slug}` (e.g. `/0-implement`, `/1-to-tickets`, `/2-verify-work`). Domain hubs are **0-**; children **1-**; deeper **2- / 3- / 4- / 5- / 6- / …** from full hub-tree depth `max(parent+1)` (no artificial cap). Dual-domain skills keep one name (deepest parent sets the number). Bare unprefixed names are not live catalog paths — if the user says “implement”, resolve to `/0-implement` when that skill exists. Full rule: `0-skill-manager/references/depth-prefix-names.md`.
6. **Applicable forks ask the user** — one material question, grounded recommendation first; never silently choose a required branch. Every option list includes **Agent judgment**. Skip a fork when one direct route is already established.
7. **Smallest skill first** — report the owning hub for orientation, but recommend the directly matching child instead of invoking its parent router first.
8. **Tombstones** — if user hits a deprecated name, name the successor hub/skill (depth-prefixed).
9. **Every domain hub is a butler routing target** — orient/query names `/0-butler` then the ★ domain hub; do not invent orphan top-level paths outside flows.md (ADR 0005).
10. **Hub packages** — each domain hub has `hubs/0-{hub}/hub.html` + `workflow.json` under `hubs/` (name matches hub skill); missing artifacts → hand off **`/0-skill-manager`** new-hub/place (query mode does not invent them).
11. **Read-only router** — Butler never edits, installs, syncs, invokes external services, creates a worktree, or executes the selected workflow.
12. **No automatic setup detour** — missing optional repository setup files do not override a direct task route.
