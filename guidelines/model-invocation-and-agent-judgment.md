# Model invocation & Agent judgment

## Runtime-specific invocation

Invocation and installation are separate controls:

| Runtime | Control | Implicitly invocable | Manual-only |
|---------|---------|----------------------|-------------|
| Claude | `SKILL.md` → `disable-model-invocation` | only `1-coding-standards` | every other live skill sets `true` |
| Codex | `agents/openai.yaml` → `policy.allow_implicit_invocation` | top-level `metadata.catalog.role: hub` skills plus `1-coding-standards` | every other live skill explicitly sets `false` |

Manual-only does not mean unavailable: explicit `$skill-name` / `/skill-name` invocation still loads the skill. Codex installation filtering is independent and uses per-skill `skills.config[].enabled`; do not infer enablement from `allow_implicit_invocation`.

`scripts/lint-skills` reports Claude and Codex independently, including names, violations, and context-budget warnings. See [ADR 0010](../docs/adr/0010-runtime-specific-invocation-and-catalog-evaluation.md).

## Fork option: **Agent judgment**

Canonical name — do not rename.

**Meaning:** The agent chooses the best branch for this fork (using the skill’s recommended default when unsure) and continues **without asking again** on that decision. The user can still interrupt later.

**Placement:** List concrete branches first; put **Agent judgment** last.

**Required** on every ask-user fork in flows, hubs, and skill bodies.
