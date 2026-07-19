# 03 — setup-rohitas-skills (rename + vault SSOT)

**What to build:** Per-repo setup is Rohitas-branded, configures tracker/labels/domain docs, and owns vault path SSOT so hard-dep and vault skills share one config story.

**Blocked by:** 02 — Skills rehoused into buckets

**Status:** ready-for-agent

**Parent:** Spec issue https://github.com/rohitas-git/ai-skills/issues/1 · local `SPEC.md`

- [ ] `setup-matt-pocock-skills` renamed to `setup-rohitas-skills` (directory, frontmatter `name`, lock entry, cross-references)
- [ ] User-facing copy says Rohitas skills (no “Matt Pocock’s skills” as product name)
- [ ] Skill still walks issue tracker → triage labels → domain docs one section at a time and writes `docs/agents/*` plus `## Agent skills` block
- [ ] Vault root SSOT is written (e.g. `docs/agents/vault.md` or equivalent section) and documented for personal vault skills
- [ ] Skill is user-invoked (`disable-model-invocation: true`)
