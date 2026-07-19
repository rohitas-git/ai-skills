# Butler hard rules (query / orient)

1. **No atoms** — never create wiki/concept pages.
2. **No multi-file catalog writes** — mutations are **`/0-skill-manager`** only.
3. **Never invent skills** — disk + flows.md only.
4. **Never promote `using-agent-skills`**.
5. **Depth-prefix names (hard)** — recommend only live skills as `/{depth}-{slug}` (e.g. `/0-implement`, `/1-to-tickets`). Domain hubs are **0-**; their children **1-** (deeper **2+**). Bare unprefixed names are not live catalog paths — if the user says “implement”, resolve to `/0-implement` when that skill exists. Full rule: `0-skill-manager/references/depth-prefix-names.md`.
6. **Forks ask the user** — one question, recommend first; never silent branch. **Every** option list must include **Agent judgment** (agent picks best branch and proceeds without more questions on that fork).
7. **Hub first** — route via domain hub when recommending a path.
8. **Tombstones** — if user hits a deprecated name, name the successor hub/skill (depth-prefixed).
9. **Every domain hub is a butler routing target** — orient/query names `/0-butler` then the ★ domain hub; do not invent orphan top-level paths outside flows.md (ADR 0005).
10. **Hub packages** — each domain hub has `hubs/0-{hub}/hub.html` + `workflow.json` under `hubs/` (name matches hub skill); missing artifacts → hand off **`/0-skill-manager`** new-hub/place (query mode does not invent them).
