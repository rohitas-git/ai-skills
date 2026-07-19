# Hub workflow — place & new-hub

## Link types (child → hub)

| Type | Meaning |
|------|---------|
| `wrapper` | Thin entry that loads SSOT hub or sibling body |
| `hard` | Must run setup / hard-dep pointer |
| `soft` | CONTEXT/ADR if present |
| `pipeline` | Ordered next/prev on a path |
| `on-ramp` | Merges into another domain’s pipeline |
| `leaf` | Tool under a hub tree (e.g. misc leaves) |
| `axis` | Dimension under multi-axis hub (e.g. code-review) |
| `satellite` | Optional related skill (e.g. ponytail-*) |

## place

Attach an **existing** skill directory to a **domain hub** documented in flows.md.

1. Identify skill path + proposed hub + link type + pipeline slot (if any).
2. Integration test (incl. checks 7–8).
3. Dry-run plan: flows.md diff, README lines, lock.
4. Confirm → apply → lint.

If no suitable hub exists → offer **new-hub** instead of inventing a peer top-level skill.

## new-hub

Create a **workflow domain**:

1. **Name the domain** and **hub skill** (slash name == dir name).
2. Scaffold hub SKILL.md via skill-creator if missing (thin router preferred).
3. Choose Matt **bucket** for the hub.
4. Add flows.md section: Top · Children table · Pipeline · Forks (F# ask-user questions).
5. Seed children (may be empty).
6. Update chart note / flows-chart when present.
7. Integration test → confirm → apply → lint.

Never create a second hub that collides with an existing domain’s job — merge or extend instead.

## Forks

Every pipeline branch needs an **F#** entry:

- Question text (one ask)
- Recommended default
- Edges → next skills

Agents must **ask the user** at each fork (recommend first); skill-manager ensures the map records the fork.
