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
| `axis` | Dimension under multi-axis hub (e.g. 1-code-review) |
| `satellite` | Optional related skill (e.g. ponytail-*) |

## place

Attach an **existing** skill directory to a **domain hub** documented in flows.md.

1. Identify skill path + proposed hub + link type + pipeline slot (if any).
2. **Assign depth-prefix name** ([depth-prefix-names.md](./depth-prefix-names.md)): hub parent depth **0** → child **`1-{slug}`**; under a sub-hub only → **`2-{slug}`** (or min dual). Rename dir + frontmatter **before** place if still bare.
3. Integration test (checks 1–9, including **skill-lint** `depth-prefix` / `name-dir`).
4. Dry-run plan: flows.md diff, hub `workflow.json` children, README lines, lock.
5. Confirm → apply → run **`/1-skill-linter`** mode **skill** (must Gate: PASS).

If no suitable hub exists → offer **new-hub** instead of inventing a peer top-level skill.
If 1-skill-linter reports **subdomain-candidate** → offer split or sub-domain hub (see 1-skill-linter `sprawl-and-subdomain.md`) before or after place.

## new-hub

Create a **workflow domain** (ADR 0005):

1. **Name the domain** and **hub skill** as **`0-{kebab-slug}`** (depth **0** hard rule; slash name == dir name == hub package name).
2. Scaffold hub SKILL.md via 0-skill-creator if missing (thin router preferred); frontmatter `name: 0-{slug}`.
3. Choose Matt **bucket** for the **live skill** (engineering / productivity / misc / personal). Hub *artifacts* do **not** nest under that bucket.
4. Add flows.md section: Top · Children table · Pipeline · Forks (F# ask-user questions) using depth-prefixed ids.
5. Seed children (may be empty); children use **1-** (or deeper) names.
6. **Hub package** — create flat dir `hubs/0-{slug}/` with:
   - `hub.html` — parent link to **0-butler** (unless this hub *is* 0-butler), link to `flows-chart.html`, `./workflow.json`, flows.md SSOT, children/pipeline/forks
   - `workflow.json` — `hub: "0-{slug}"`; `parent.hub = "0-butler"` + `relationship = "routed_by"` (or `parent: null` if 0-butler); children, pipeline, forks, artifacts
7. **Butler link** — add hub to `hubs/0-butler/hub.html` domain list and `hubs/0-butler/workflow.json` `domain_hubs_routed`.
8. **Manifest** — add entry in `hubs/manifest.json`.
9. **flows-chart** — add matrix/nav link to `hubs/0-{slug}/hub.html`.
10. Integration test → confirm → apply → **skill-linter** hub/package checks (`depth-prefix`, `depth-hub`, `hub-dir`, `hub-html`, `hub-workflow-json`, `butler-hub-link`, `hub-chart-link`).

### sub-hub (optional)

When 1-skill-linter marks **subdomain-candidate** (or user asks to split a mega-skill tree):

1. Prefer extract child skills + thin router under an **existing** domain hub.
2. Else create flat package `hubs/1-{sub}/` (depth **1** sub-hub; same ADR 0005 files) with:
   - `hub: "1-{sub}"`
   - `parent` → 0-butler (house apex)
   - `parent_domain_hub` → owning domain hub name (`0-…`)
   - `children` → extracted skills (`2-…` if only under this sub-hub; else min dual)
3. Parent domain workflow/flows: `link_type: "sub-hub"` → `1-{sub}`.
4. skill-lint parent + sub + children.

Never create a second hub that collides with an existing domain’s job — merge or extend instead.
Never leave a flows.md domain without a `hubs/{hub}/` package + 0-butler parent link.
Never leave a live skill without hub membership (ADR 0006).

## Forks

Every pipeline branch needs an **F#** entry:

- Question text (one ask)
- Recommended default
- Edges → next skills

Agents must **ask the user** at each fork (recommend first); 0-skill-manager ensures the map records the fork.
