# Ingest workflow

Add or promote one fixed skill candidate without dual routers, collisions, or hidden effects.

## Sources

| Source | Example |
|--------|---------|
| Draft path | `.scratch/new-skill/` or user-provided folder with `SKILL.md` |
| Existing folder | already under a bucket but incomplete indexes |
| Vendor candidate | `vendor/agent-skills/skills/<name>/` |

## Modes

- **Assess:** run the integration test and return a plan without writing.
- **Apply:** selected when the user explicitly asks to ingest/promote the fixed candidate; scoped reversible catalog edits need no second confirmation.

## Integration test (promote gate)

All must **pass** before apply. Report as a table.

| # | Check | Pass criteria |
|---|-------|---------------|
| 1 | **Gap** | flows.md / catalog has a real gap this skill fills (not vanity) |
| 2 | **Collision / merge** | no name collision; if job overlaps a winner, **prefer merge** plan over second skill |
| 3 | **Prev/next** | explicit previous/next chain slots if it sits on a flow (or "standalone" documented) |
| 4 | **Hard vs soft setup** | hard deps only for to-spec/1-to-tickets/0-triage → `/0-setup-rohitas-skills`; soft skills no forced setup spam |
| 5 | **thin or disclosure** | SKILL.md thin enough or progressive-disclosure plan for sprawl |
| 6 | **Forbidden** | never `using-agent-skills`; never second meta-router; never whole vendor pack |
| 7 | **Hub slot** | parent domain hub + link type (wrapper/hard/soft/pipeline/on-ramp/leaf/axis/satellite/sub-hub) |
| 8 | **Forks** | if skill sits on a branch, F# ask-user question exists or is proposed |
| 9 | **Route surface (`gate-route`)** | description contract (Use when / Not for / Hub) + `metadata.catalog` with `hub`, `role`, and `when` or `triggers`; **no** top-level route keys — [skill-route-surface.md](./skill-route-surface.md) |
| 10 | **skill-lint** | `/1-skill-linter` mode skill would Gate: PASS (SKILL.md + refs + hub membership + route surface) |

Fail any row → do not promote; propose merge, rewrite, or defer.

## Apply steps

For third-party package security/provenance review, hand the fixed source snapshot,
expected capabilities, proposed runtime permissions and optional prior version to
`/2-skill-supply-chain-audit`. It returns findings, coverage gaps and a recommendation
to this ingest workflow; it does not install, execute, enable or promote the source.
Resolve material gaps before treating source as trusted runnable content. Structural
`/1-skill-linter` results do not replace this security evidence. Adopted code or changed
permissions need review of the resulting candidate, not only the upstream snapshot.
The user's explicit mutation scope governs what this manager may place. Installation, code execution, activation, sync, commit, push, and publication remain separate effects.

1. Place under correct bucket (`git mv` / move).
2. **Depth-prefix name (hard):** set dir + frontmatter `name` to `{depth}-{kebab-slug}` per [depth-prefix-names.md](./depth-prefix-names.md) (★ hub → `0-`; hub child → `1-`; under sub-hub → `2-`; deeper nesting → `3-` / `4-` / `5-` / `6-` / … via `max(parent+1)`). Ensure `name` == directory name. Never leave a bare unprefixed live skill.
3. **Route surface:** write/verify description contract + `metadata.catalog` (hub matches place parent; never top-level `hub`/`when`/…).
4. Add one-line entry to bucket README.
5. If promoted bucket: add line to root README; if not: ensure root does **not** list it.
6. Update `flows.md` **and** parent `hubs/{hub}/workflow.json` children so the skill is a hub member.
7. Update `skills-lock.json` if the skill is locked/sourced.
8. Run **`scripts/generate-route-index`** so butler skim includes the new skill.
9. Run **`/1-skill-linter`** mode **skill** on the new path — require **Gate: PASS** (includes `gate-route` for new skills).
10. Never create wiki/concept atoms.

## 1-create-skill 1-handoff

`1-create-skill` / `0-skill-creator` scaffold bodies only. Then **skill-manager** place/ingest for catalog citizenship, including **skill-lint**. Routing stays with **butler**.

## Demo assessment

Example: assess `vendor/agent-skills/skills/security-and-hardening` (or any candidate):

1. Load SKILL.md
2. Fill integration-test table (expect: may pass gap for security, fail if collision with future security skill, must not promote using-agent-skills)
3. Propose bucket `engineering`, chain slot "optional ship/security on-ramp", standalone until flows updated
4. Stop without writing when the request was review/assess; apply only for an explicit ingest/promote request
