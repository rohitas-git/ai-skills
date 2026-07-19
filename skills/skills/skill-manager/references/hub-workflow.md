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
2. Integration test (checks 1–9, including **skill-lint**).
3. Dry-run plan: flows.md diff, hub `workflow.json` children, README lines, lock.
4. Confirm → apply → run **`/skill-linter`** mode **skill** (must Gate: PASS).

If no suitable hub exists → offer **new-hub** instead of inventing a peer top-level skill.
If skill-linter reports **subdomain-candidate** → offer split or sub-domain hub (see skill-linter `sprawl-and-subdomain.md`) before or after place.

## new-hub

Create a **workflow domain** (ADR 0005):

1. **Name the domain** and **hub skill** (slash name == dir name).
2. Scaffold hub SKILL.md via skill-creator if missing (thin router preferred).
3. Choose Matt **bucket** for the **live skill** (engineering / productivity / misc / personal). Hub *artifacts* do **not** nest under that bucket.
4. Add flows.md section: Top · Children table · Pipeline · Forks (F# ask-user questions).
5. Seed children (may be empty).
6. **Hub package** — create flat dir `hubs/{hub}/` with:
   - `hub.html` — parent link to **butler** (unless this hub *is* butler), link to `flows-chart.html`, `./workflow.json`, flows.md SSOT, children/pipeline/forks
   - `workflow.json` — `parent.hub = "butler"` + `relationship = "routed_by"` (or `parent: null` if butler); children, pipeline, forks, artifacts
7. **Butler link** — add hub to `hubs/butler/hub.html` domain list and `hubs/butler/workflow.json` `domain_hubs_routed`.
8. **Manifest** — add entry in `hubs/manifest.json`.
9. **flows-chart** — add matrix/nav link to `hubs/{hub}/hub.html`.
10. Integration test → confirm → apply → **skill-linter** hub/package checks (`hub-dir`, `hub-html`, `hub-workflow-json`, `butler-hub-link`, `hub-chart-link`).

### sub-hub (optional)

When skill-linter marks **subdomain-candidate** (or user asks to split a mega-skill tree):

1. Prefer extract child skills + thin router under an **existing** domain hub.
2. Else create flat package `hubs/{sub}/` (same ADR 0005 files) with:
   - `parent` → butler (house apex)
   - `parent_domain_hub` → owning domain hub name
   - `children` → extracted skills
3. Parent domain workflow/flows: `link_type: "sub-hub"` → `{sub}`.
4. skill-lint parent + sub + children.

Never create a second hub that collides with an existing domain’s job — merge or extend instead.
Never leave a flows.md domain without a `hubs/{hub}/` package + butler parent link.
Never leave a live skill without hub membership (ADR 0006).

## Forks

Every pipeline branch needs an **F#** entry:

- Question text (one ask)
- Recommended default
- Edges → next skills

Agents must **ask the user** at each fork (recommend first); skill-manager ensures the map records the fork.
