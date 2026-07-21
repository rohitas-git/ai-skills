# Skill-manager hard rules

1. **No atoms** — Do not create concept pages, wiki atoms, Obsidian Concepts, or project-wiki nodes. Skill stewardship ≠ knowledge wiki.
2. **Confirm before multi-file write** — Any op that touches more than one file (indexes, lock, flows, moves) must present a plan and wait for human confirmation. Dry-run is the default.
3. **Never promote `using-agent-skills`** — dual meta-router is forbidden.
4. **Never invent skills in query** — recommend only skills that exist on disk under discoverable buckets (or explicit deprecated tombstones when explaining successors).
5. **Prefer merge** — if a candidate collides with an existing skill's job, merge content into the winner rather than adding a peer.
6. **Depth-prefix names (hard)** — live skill dir, frontmatter `name`, slash, and hub package (if any) **must** be `{depth}-{kebab-slug}` for **full hub-tree depth** (0…max; **no artificial cap**):
   - **0-** ★ domain hubs (incl. `0-butler`) — identity wins over dual edges
   - **1-** children of domain hubs; **sub-hubs** at parent_depth+1 (today often 1)
   - **2-** children of depth-1 hubs (sub-hub children → `2-…`)
   - **3- / 4- / 5- / 6- / …** same recurrence: `max(parent_hub_depth + 1)` over all hub parents
   - Dual membership: depth = **deepest** attachment; `"primary": true` is ownership/docs only (may still rename if dual adds a deeper parent)
   - Bare unprefixed live names are **forbidden**. Vendor archive keeps upstream names until place/ingest assigns depth.
   - Full rule: [depth-prefix-names.md](./depth-prefix-names.md). Lint: `depth-prefix`, `depth-hub`, `depth-graph`.
7. **Hard setup deps** — `1-to-spec`, `1-to-tickets`, `0-triage` must point at `/0-setup-rohitas-skills`. Soft deps (1-tdd, 0-diagnosing-bugs, 0-improve-codebase-architecture, vocabulary skills) use CONTEXT/ADR if present only.
8. **Tombstones** — deprecations stay under `archive/` with successor named in README and skill body.

9. **Butler does not mutate** — multi-file catalog writes are 0-skill-manager only; 0-butler only routes.
10. **One hub per domain** — never add a peer top skill that splits a domain without new-hub + deprecate old hub.
11. **Forks ask the user** — pipeline branches must have F# questions; agents ask (recommend first), never silent branch.
12. **Butler links every domain hub** — every ★ domain hub is a routing child of `/0-butler`. Non-butler hub packages parent-link 0-butler; 0-butler lists every domain hub (ADR 0005).
13. **Hub package dir required** — each flows.md domain hub has `hubs/{hub}/` where `{hub}` is the depth-prefixed hub skill name (flat — **no** bucket nesting under `hubs/`).
14. **Hub HTML + workflow JSON** — each package contains `hub.html` and `workflow.json`; `workflow.json` sets `parent` → 0-butler (`null` only for butler); update `hubs/manifest.json`.
15. **Hub pages link the chart** — every `hub.html` links `flows-chart.html`; chart matrix links each `hubs/{hub}/hub.html`.
16. **Hub membership** — every live skill (flat `skills/` leaves) must appear under a domain hub workflow (flows.md and/or `hubs/*/workflow.json` children). Orphans are skill-lint **critical** (ADR 0006).
17. **skill-lint gate** — create/place/ingest/new-hub/update-that-touches-SKILL require `/1-skill-linter` **Gate: PASS** (0 critical) before the skill is considered healthy; lint op loads skill-linter + may run `scripts/lint-skills`.
18. **lean SKILL.md** — main file stays thin (router + steps + chain blurb); depth in `references/` / siblings. 1-skill-linter enforces lean/disclosure; new skills fail `gate-lean` if SKILL.md is fat without a disclosure map (1-writing-great-skills).
19. **Chaining** — place skills on a hub chain with link type; pipeline skills name next (e.g. 0-implement → 1-tdd → 1-code-review). Do not ship essay-only orphans.
20. **Sprawl → thin, chain, split, then sub-domain** — oversized skills: progressive disclosure first, then child skills or sub-domain hub (`parent_domain_hub` + 0-butler apex). Sub-hub package depth = **parent_depth + 1** (often **1-**; nested → **2- / 3- / …**).
21. **Atomic skills** — one primary job per skill; **Boundary** table for cousins; hard redirect asks the user (never silent cousin load). See [atomic-skills.md](./atomic-skills.md). Apply via **`/1-skill-atomize`**.
22. **Forks on collision** — when two live skills share triggers, document an F# ask-user fork in flows.md and both skill bodies (recommended option first).
23. **Wiki index** — after place/ingest/organize/deprecate, update `wikis/index.md` and append `wikis/log.md` (1-project-wiki-manager index pattern).
24. **Skills/ paths** — after place/rename, keep `skills/{depth}-{slug}/` as the only live path; update lock + flows + hubs in the same organize pass.
25. **Route surface (ADR 0009)** — live skills use description contract + **`metadata.catalog` only** (no top-level route keys). New place/ingest: `gate-route` critical. Spec: [skill-route-surface.md](./skill-route-surface.md).
26. **Route index** — after place/ingest/organize/rename/catalog frontmatter change, run `scripts/generate-route-index` so butler skim stays current.
27. **Catalog version + feature log** — convention changes and accepted ADRs bump root `catalog.yaml` `version` and prepend [docs/FEATURE-LOG.md](../../../docs/FEATURE-LOG.md) (not every commit).

**Agent judgment:** every user-facing fork must offer **Agent judgment** (agent chooses best branch and proceeds without more questions on that fork).
