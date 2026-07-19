# Skill-manager hard rules

1. **No atoms** — Do not create concept pages, wiki atoms, Obsidian Concepts, or project-wiki nodes. Skill stewardship ≠ knowledge wiki.
2. **Confirm before multi-file write** — Any op that touches more than one file (indexes, lock, flows, moves) must present a plan and wait for human confirmation. Dry-run is the default.
3. **Never promote `using-agent-skills`** — dual meta-router is forbidden.
4. **Never invent skills in query** — recommend only skills that exist on disk under discoverable buckets (or explicit deprecated tombstones when explaining successors).
5. **Prefer merge** — if a candidate collides with an existing skill's job, merge content into the winner rather than adding a peer.
6. **Hard setup deps** — `1-to-spec`, `1-to-tickets`, `0-triage` must point at `/0-setup-rohitas-skills`. Soft deps (1-tdd, 0-diagnosing-bugs, 0-improve-codebase-architecture, vocabulary skills) use CONTEXT/ADR if present only.
7. **Tombstones** — deprecations stay under `archive/` with successor named in README and skill body.

8. **Butler does not mutate** — multi-file catalog writes are 0-skill-manager only; 0-butler only routes.
9. **One hub per domain** — never add a peer top skill that splits a domain without new-hub + deprecate old hub.
10. **Forks ask the user** — pipeline branches must have F# questions; agents ask (recommend first), never silent branch.
11. **Butler links every domain hub** — every ★ domain hub is a routing child of `/0-butler`. Non-butler hub packages parent-link 0-butler; 0-butler lists every domain hub (ADR 0005).
12. **Hub package dir required** — each flows.md domain hub has `hubs/{hub}/` (flat — **no** Matt-bucket nesting under `hubs/`).
13. **Hub HTML + workflow JSON** — each package contains `hub.html` and `workflow.json`; `workflow.json` sets `parent` → 0-butler (`null` only for butler); update `hubs/manifest.json`.
14. **Hub pages link the chart** — every `hub.html` links `flows-chart.html`; chart matrix links each `hubs/{hub}/hub.html`.
15. **Hub membership** — every live skill (flat `skills/` leaves (house/ship/…/0-office + vault/personal)) must appear under a domain hub workflow (flows.md and/or `hubs/*/workflow.json` children). Orphans are skill-lint **critical** (ADR 0006).
16. **skill-lint gate** — create/place/ingest/new-hub require `/1-skill-linter` **Gate: PASS** (0 critical) before the skill is considered healthy; lint op loads skill-linter.
17. **Matt lean SKILL.md** — main file stays thin (router + steps + chain blurb); depth in `references/` / siblings. 1-skill-linter enforces lean/disclosure; new skills fail `gate-lean` if SKILL.md is fat without a disclosure map (1-writing-great-skills).
18. **Chaining** — place skills on a hub chain with link type; pipeline skills name next (e.g. 0-implement → 1-tdd → 1-code-review). Do not ship essay-only orphans.
19. **Sprawl → thin, chain, split, then sub-domain** — oversized skills: progressive disclosure first, then child skills or sub-domain hub (`parent_domain_hub` + 0-butler apex).
20. **Atomic skills** — one primary job per skill; **Boundary** table for cousins; hard redirect asks the user (never silent cousin load). See [atomic-skills.md](./atomic-skills.md). Apply via **`/1-skill-atomize`**.
21. **Forks on collision** — when two live skills share triggers, document an F# ask-user fork in flows.md and both skill bodies (recommended option first).

18. **Wiki index** — after place/ingest/organize/deprecate, update `wikis/index.md` and append `wikis/log.md` (1-project-wiki-manager index pattern).
19. **Skills/ symlinks** — after place/rename, refresh `skills/<name>` symlink to primary domain path.

**Agent judgment:** every user-facing fork must offer **Agent judgment** (agent chooses best branch and proceeds without more questions on that fork).
