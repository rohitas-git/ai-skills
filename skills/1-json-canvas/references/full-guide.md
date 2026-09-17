# JSON Canvas compatibility guide

Version-sensitive format notes only. `../SKILL.md` is operative. This file grants no source/vault read,
destination write/overwrite, URL fetch, app/plugin, collaboration, sync, publication, or sharing authority.
Confirm the target consumer and current specification before depending on optional fields.

## Core shape

```json
{"nodes": [], "edges": []}
```

Common node types are `text`, `file`, `link`, and `group`. A node normally has unique `id`, `type`, `x`, `y`,
`width`, and `height`, plus its type-specific `text`, `file`, `url`, or group fields. Edges have a unique `id`,
`fromNode`, and `toNode`, with optional sides, ends, color, and label. Preserve fields unknown to this guide.

Array order can affect z-order. Coordinates may be negative. Colors may be consumer presets or hex values;
do not assume preset rendering is identical across applications. Geometry follows actual content/readability,
not fixed spacing or size quotas.

## Integrity rules

- IDs must be unique across the namespace expected by the pinned consumer. Generate unpredictable collision-free
  IDs for new elements; preserve existing IDs and all inbound/outbound references during edits.
- Every edge endpoint must resolve to an existing node. Validate side/end enum values only against the pinned
  consumer/spec rather than silently deleting newer values.
- Text contains Markdown-like data. JSON serialization encodes actual newlines as `\n`; do not pre-escape them
  into literal `\\n` content before serializing.
- File nodes store vault/consumer-relative references. Prove containment and syntax without opening the target.
  Subpaths commonly identify headings/blocks but do not prove that the target exists.
- Link nodes store URLs. Syntax validation is not permission to fetch, preview, authenticate, or follow them.
- Group backgrounds and other paths are references, not authority to read or embed their targets.

## Verification

Parse the final bytes independently, compare source/output hashes, verify the exact changed IDs/properties,
check uniqueness, endpoint integrity, required fields, finite geometry, intended order, and preservation of
unknown/untouched data. A schema-valid file may still render poorly or differently across consumers. App-level
visual verification is a separately authorized operation.

Primary specification locator: <https://jsoncanvas.org/spec/1.0/>. Treat this URL as provenance, not automatic
network access; use current primary documentation when version-sensitive behavior matters.
