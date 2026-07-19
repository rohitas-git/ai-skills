# Butler hard rules (query / orient)

1. **No atoms** — never create wiki/concept pages.
2. **No multi-file catalog writes** — mutations are **`/0-skill-manager`** only.
3. **Never invent skills** — disk + flows.md only.
4. **Never promote `using-agent-skills`**.
5. **Forks ask the user** — one question, recommend first; never silent branch. **Every** option list must include **Agent judgment** (agent picks best branch and proceeds without more questions on that fork).
6. **Hub first** — route via domain hub when recommending a path.
7. **Tombstones** — if user hits a deprecated name, name the successor hub/skill.
8. **Every domain hub is a butler routing target** — orient/query names `/0-butler` then the ★ domain hub; do not invent orphan top-level paths outside flows.md (ADR 0005).
9. **Hub packages** — each domain hub has `hubs/{hub}/hub.html` + `workflow.json` under `hubs/`; missing artifacts → hand off **`/0-skill-manager`** new-hub/place (query mode does not invent them).
