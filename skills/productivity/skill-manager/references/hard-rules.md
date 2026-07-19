# Skill-manager hard rules

1. **No atoms** — Do not create concept pages, wiki atoms, Obsidian Concepts, or project-wiki nodes. Skill stewardship ≠ knowledge wiki.
2. **Confirm before multi-file write** — Any op that touches more than one file (indexes, lock, flows, moves) must present a plan and wait for human confirmation. Dry-run is the default.
3. **Never promote `using-agent-skills`** — dual meta-router is forbidden.
4. **Never invent skills in query** — recommend only skills that exist on disk under discoverable buckets (or explicit deprecated tombstones when explaining successors).
5. **Prefer merge** — if a candidate collides with an existing skill's job, merge content into the winner rather than adding a peer.
6. **Hard setup deps** — `to-spec`, `to-tickets`, `triage` must point at `/setup-rohitas-skills`. Soft deps (tdd, diagnosing-bugs, improve-codebase-architecture, vocabulary skills) use CONTEXT/ADR if present only.
7. **Tombstones** — deprecations stay under `deprecated/` with successor named in README and skill body.

8. **Butler does not mutate** — multi-file catalog writes are skill-manager only; butler only routes.
9. **One hub per domain** — never add a peer top skill that splits a domain without new-hub + deprecate old hub.
10. **Forks ask the user** — pipeline branches must have F# questions; agents ask (recommend first), never silent branch.

