---
name: 1-ponytail-help
description: >
  Show a one-shot quick reference for this catalog's Ponytail overlay, levels, and child skills. Not for
  activating the mode, reviewing code, or describing uninstalled hooks/configuration. Hub: /0-ponytail.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-ponytail
    role: satellite
    when: ["explain how this catalog's Ponytail skills and levels work"]
    not_when:
      - "activate minimal coding overlay → 0-ponytail"
      - "review code → 1-ponytail-audit or 2-ponytail-review"
    prev: [0-ponytail]
    next: [0-ponytail]
    cousins: [0-ponytail, 1-ponytail-audit, 2-ponytail-review]
    triggers: [ponytail help, Ponytail commands, how do I use Ponytail, explain Ponytail modes]
    requires_setup: false
---

# Ponytail Help

Display this catalog-accurate card once. Do not activate a mode, inspect code, write configuration, or
claim hook/session persistence.

## Levels

| Level | Invocation | Effect on one coding task/session |
|---|---|---|
| Lite | `/0-ponytail lite` | Build what was requested and mention one materially simpler alternative. |
| Full | `/0-ponytail` or `/0-ponytail full` | Apply the simplicity ladder; default when explicitly invoked. |
| Ultra | `/0-ponytail ultra` | Challenge speculative work and prefer deletion without dropping accepted requirements or safety. |

Say `stop ponytail` or `normal mode` to deactivate the conversational overlay. Actual cross-turn behavior
depends on the host; this catalog does not install or promise lifecycle hooks, environment-variable
activation, flag files, or `~/.config` state.

## Skills

| Need | Skill |
|---|---|
| Smallest correct implementation approach | `/0-ponytail` |
| One pinned diff: removable complexity only | `/2-ponytail-review` |
| Bounded repository snapshot audit | `/1-ponytail-audit` |
| Read-only `0-ponytail:` marker ledger | `/1-ponytail-debt` |
| Pinned upstream benchmark snapshot | `/1-ponytail-gain` |
| This card | `/1-ponytail-help` |

Ponytail is for coding. Use the direct domain skill for prose, summaries, translation, extensive
documentation, or unresolved product scope. It never overrides repository rules, acceptance criteria,
required explanations, safety controls, or action authority.
