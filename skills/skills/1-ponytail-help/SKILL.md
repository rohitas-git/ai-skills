---
name: 1-ponytail-help
description: >
  Quick-reference card for all 0-ponytail modes, skills, and commands.
  One-shot display, not a persistent mode. Trigger: /1-ponytail-help,
  "ponytail help", "what 0-ponytail commands", "how do I use ponytail".
disable-model-invocation: true
---

# Ponytail Help

Display this reference card when invoked. One-shot, do NOT change mode,
write flag files, or persist anything.

## Levels

| Level | Trigger | What change |
|-------|---------|-------------|
| **Lite** | `/0-ponytail lite` | Build what's asked, name the lazier alternative in one line. |
| **Full** | `/0-ponytail` | The ladder enforced: YAGNI → stdlib → native → one line → minimum. Default. |
| **Ultra** | `/0-ponytail ultra` | YAGNI extremist. Deletion before addition. Challenges requirements before building. |

Level sticks until changed or session end.

## Skills

| Skill | Trigger | What it does |
|-------|---------|--------------| 
| **ponytail** | `/0-ponytail` | Lazy mode itself. Simplest solution that works. |
| **ponytail-review** | `/1-ponytail-review` | Over-engineering 0-review: `L42: yagni: factory, one product. Inline.` |
| **ponytail-gain** | `/1-ponytail-gain` | Measured-impact scoreboard: less code, less cost, more speed. |
| **ponytail-help** | `/1-ponytail-help` | This card. |

## Deactivate

Say "stop ponytail" or "normal mode". Resume anytime with `/0-ponytail`.
`/0-ponytail off` also works.

## Configure Default Mode

Default mode = `full`, auto-active every session. Change it:

**Environment variable** (highest priority):
```bash
export PONYTAIL_DEFAULT_MODE=ultra
```

**Config file** (`~/.config/0-ponytail/config.json`, Windows: `%APPDATA%\ponytail\config.json`):
```json
{ "defaultMode": "lite" }
```

Set `"off"` to disable auto-activation on session start, activate manually
with `/0-ponytail` when wanted.

Resolution: env var > config file > `full`.

## More

Full docs + examples: https://github.com/DietrichGebert/0-ponytail
