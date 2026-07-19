# Vendor

Third-party skill packs kept **out of default discovery**.

## Policy

- **Promote only via butler ingest** — never co-load a whole pack as peer skills, and never promote `using-agent-skills` (dual meta-router).
- Packs here are offline from symlink sync unless explicitly listed in `scripts/symlink-targets.json` `nestedSkillRoots` (default: empty).
- Prefer merging useful content into an existing catalog winner over promoting a near-duplicate.

## Packs

| Pack | Path | Status |
|------|------|--------|
| agent-skills (Addy Osmani et al.) | [agent-skills/](./agent-skills/) | Parked. Selective promotes only via butler ingest. TDD ideas merge into catalog `tdd`, not a second skill. |

## Deferred promotes

Candidates (not auto-promoted): security-and-hardening, shipping-and-launch, observability-and-instrumentation, performance-optimization, api-and-interface-design, frontend-ui-engineering, source-driven-development, code-simplification.

Do **not** promote as peers of grill / to-spec / to-tickets: interview-me, spec-driven-development, planning-and-task-breakdown.
