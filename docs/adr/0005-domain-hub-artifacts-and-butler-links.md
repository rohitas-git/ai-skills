# ADR 0005: Domain hub packages and butler links

## Status

Accepted

## Context

The skills catalog routes work through **domain hubs** documented in `skills/productivity/butler/references/flows.md`. Humans and agents need:

1. A stable **hub of hubs** entry (`/butler`) that reaches every domain.
2. A **human-readable** page per domain hub (pipelines, forks, children).
3. A **machine-readable** workflow file per domain hub for lint, place, and new-hub ops.
4. A clear package layout that does not nest under Matt skill buckets (skills stay in Matt buckets; hub docs are separate projections).

Without a written rule, new domains risk landing in `flows.md` only—missing HTML, JSON, butler links, or chart updates.

## Decision

### Hub of hubs

- **`/butler`** is the only hub of hubs. Every other domain hub is a **routing child** of butler.
- Butler **routes / orients only**. Catalog mutations remain **`/skill-manager`**.

### Package layout (flat under `hubs/`)

Each ★ domain hub named in `flows.md` (including butler) has **one directory**:

```text
skills/.scratch/skills-catalog-reorg/hubs/{hub}/
  hub.html
  workflow.json
```

Plus house-level:

| Artifact | Path |
|----------|------|
| Index | `hubs/index.html` |
| Manifest | `hubs/manifest.json` |
| Chart | `flows-chart.html` (sibling of `hubs/`) |

**Do not** nest hub packages under Matt buckets (`hubs/engineering/...`). Live skills remain in Matt buckets (`engineering/implement/`); hub artifacts live only under flat `hubs/{hub}/`.

### Link requirements

1. **Butler → each domain hub** — `hubs/butler/hub.html` lists every domain hub; `hubs/butler/workflow.json` lists them under `domain_hubs_routed`.
2. **Each domain hub → butler** — non-butler `hub.html` links to `../butler/hub.html`; non-butler `workflow.json` sets `parent.hub` to `"butler"` with `relationship: "routed_by"`. Butler’s own `parent` is `null`.
3. **Each hub page → flows chart** — link to `../../flows-chart.html`.
4. **Each hub page → its workflow JSON** — link to `./workflow.json`.
5. **Chart → hub pages** — domain matrix and nav link to `hubs/{hub}/hub.html`.
6. **flows.md remains SSOT** for pipeline text and forks; HTML/JSON are projections that must not invent hubs absent from flows.

### Workflow JSON minimum shape

```json
{
  "schema_version": 1,
  "kind": "domain_hub_workflow",
  "domain_id": 0,
  "domain": "…",
  "hub": "…",
  "slash": "/…",
  "path": "bucket/skill",
  "package_dir": "hubs/{hub}/",
  "parent": null,
  "children": [],
  "pipeline": [],
  "forks": [],
  "artifacts": {
    "html": "./hub.html",
    "workflow_json": "./workflow.json",
    "flows_chart": "../../flows-chart.html",
    "flows_ssot": "…"
  }
}
```

Non-butler hubs set `parent` to butler (not `null`).

### Ops ownership

- **`skill-manager` new-hub / place / organize** must create or update: flows.md slot, `hubs/{hub}/` package (`hub.html` + `workflow.json`), butler links, flows-chart, manifest.
- **`butler`** never invents orphan domain hubs or multi-file catalog mutations.
- **One ★ hub per domain** — no peer top skill that splits a domain without new-hub + deprecating the old hub.

## Consequences

- Lint must flag missing hub package dir, missing `hub.html`, missing `workflow.json`, missing butler parent link, or missing chart link.
- Agents adding a domain without the package are non-compliant with this ADR.
- Projections live under `.scratch/skills-catalog-reorg/hubs/` next to the chart until a later ADR moves them.
