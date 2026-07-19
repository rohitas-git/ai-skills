# Model invocation & Agent judgment

## `disable-model-invocation`

**Default: `true`** on every live skill.

| Exception (model may auto-load) | Why |
|---------------------------------|-----|
| `coding-standards` | Always-on while writing/reviewing code |
| `ponytail` | Always-on lazy ladder while coding |

All other skills are user- or butler-invoked so they do not steal context.

## Fork option: **Agent judgment**

Canonical name — do not rename.

**Meaning:** The agent chooses the best branch for this fork (using the skill’s recommended default when unsure) and continues **without asking again** on that decision. The user can still interrupt later.

**Placement:** List concrete branches first; put **Agent judgment** last.

**Required** on every ask-user fork in flows, hubs, and skill bodies.
