# Hub membership

## Rule (ADR 0006)

Every **live** skill under flat `skills/` leaves (and vault/personal) must be a **child** of at least one domain hub workflow.

Live skill ids are **depth-prefixed**: `{depth}-{kebab-slug}` (hard rule — `0-skill-manager/references/depth-prefix-names.md`). Membership strings in `workflow.json` / flows.md must use that full name (e.g. `1-to-tickets`, not `to-tickets`).

## How to resolve membership

A skill `name` is a member if any of:

1. **Hub workflow JSON** — appears in `hubs/*/workflow.json` under any `children[].skills` array (string match on skill name).
2. **flows.md** — appears as a named skill under a domain’s Children / pipeline text (backtick names preferred: `` `skill-name` ``).
3. **It is a ★ domain hub itself** — directory name matches a hub package / flows ★ Hub (e.g. `0-butler`, `0-implement`).

## Not membership targets

- Ops verbs in workflow JSON that are not skills: `create`, `read`, `update`, `delete`, `place`, `new-hub`, `ingest`, `organize`, `lint` (unless a real skill with that name exists).
- Axis labels that are not skills: `Spec`, `Standards`, `Maintainability` (1-code-review axes).
- Deprecated tombstones and vendor packs.

## Orphans

If a live skill is not a member:

```text
[critical] hub-member path — skill not listed under any domain hub workflow
```

**Remediation:** 0-skill-manager **place** (parent hub + link type). Do not invent a new domain unless **new-hub** is justified.

## Sub-hub skills

Skills under a sub-domain hub still count as members if listed on the sub-hub’s `workflow.json` children. Parent domain should list the sub-hub with `link_type: "sub-hub"`.

## Building the membership index (agents / scripts)

```text
for each hubs/*/workflow.json:
  collect children[].skills (strings)
  if hub field set, add hub name as member
parse flows.md for `backticked-names` in Children rows (optional supplement)
live skills = dirs with SKILL.md in engineering|productivity|misc|personal
orphan = live - members - non-skill tokens
```
