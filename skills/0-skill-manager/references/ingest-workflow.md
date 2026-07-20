# Ingest workflow

Add or promote a skill into the catalog without dual routers, collisions, or silent multi-file writes.

## Sources

| Source | Example |
|--------|---------|
| Draft path | `.scratch/new-skill/` or user-provided folder with `SKILL.md` |
| Existing folder | already under a bucket but incomplete indexes |
| Vendor candidate | `vendor/agent-skills/skills/<name>/` |

## Modes

- **Dry-run (default):** run integration test, propose plan, **do not write**.
- **Apply:** only after explicit human confirmation of the plan.

## Integration test (promote gate)

All must **pass** before apply. Report as a table.

| # | Check | Pass criteria |
|---|-------|---------------|
| 1 | **Gap** | flows.md / catalog has a real gap this skill fills (not vanity) |
| 2 | **Collision / merge** | no name collision; if job overlaps a winner, **prefer merge** plan over second skill |
| 3 | **Prev/next** | explicit previous/next chain slots if it sits on a flow (or "standalone" documented) |
| 4 | **Hard vs soft setup** | hard deps only for to-spec/1-to-tickets/0-triage → `/0-setup-rohitas-skills`; soft skills no forced setup spam |
| 5 | **Matt-short or disclosure** | SKILL.md thin enough or progressive-disclosure plan for sprawl |
| 6 | **Forbidden** | never `using-agent-skills`; never second meta-router; never whole vendor pack |
| 7 | **Hub slot** | parent domain hub + link type (wrapper/hard/soft/pipeline/on-ramp/leaf/axis/satellite/sub-hub) |
| 8 | **Forks** | if skill sits on a branch, F# ask-user question exists or is proposed |
| 9 | **skill-lint** | `/1-skill-linter` mode skill would Gate: PASS (SKILL.md + refs + hub membership plan) |

Fail any row → do not promote; propose merge, rewrite, or defer.

## Apply steps (after confirm)

1. Place under correct bucket (`git mv` / move).
2. **Depth-prefix name (hard):** set dir + frontmatter `name` to `{depth}-{kebab-slug}` per [depth-prefix-names.md](./depth-prefix-names.md) (★ hub → `0-`; hub child → `1-`; under sub-hub → `2-`; deeper nesting → `3-` / `4-` / `5-` / `6-` / … via `max(parent+1)`). Ensure `name` == directory name. Never leave a bare unprefixed live skill.
3. Add one-line entry to bucket README.
4. If promoted bucket: add line to root README; if not: ensure root does **not** list it.
5. Update `flows.md` **and** parent `hubs/{hub}/workflow.json` children so the skill is a hub member.
6. Update `skills-lock.json` if the skill is locked/sourced.
7. Run **`/1-skill-linter`** mode **skill** on the new path — require **Gate: PASS**.
8. Never create wiki/concept atoms.

## 1-create-skill 1-handoff

`1-create-skill` / `0-skill-creator` scaffold bodies only. Then **skill-manager** place/ingest for catalog citizenship, including **skill-lint**. Routing stays with **butler**.

## Demo dry-run

Example: dry-run ingest of `vendor/agent-skills/skills/security-and-hardening` (or any candidate):

1. Load SKILL.md
2. Fill integration-test table (expect: may pass gap for security, fail if collision with future security skill, must not promote using-agent-skills)
3. Propose bucket `engineering`, chain slot "optional ship/security on-ramp", standalone until flows updated
4. Stop without writing unless user confirms
