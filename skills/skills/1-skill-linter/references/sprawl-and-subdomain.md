# Sprawl and sub-domain hubs

Aligned with **Matt lean** ([matt-lean-structure.md](./matt-lean-structure.md)): thin `SKILL.md` first; sub-domain hubs only for whole trees.

## Prefer (in order)

1. **Thin SKILL.md** — progressive disclosure to `references/` / sibling files (writing-great-skills ladder).
2. **Chain** — place under domain hub; name prev/next; do not embed other skills’ jobs.
3. **Split skill** — by invocation or by sequence (writing-great-skills).
4. **Sub-domain hub** — only if a multi-skill tree needs its own map under a parent domain.

## Thresholds (defaults)

| Signal | Threshold | Code |
|--------|-----------|------|
| SKILL.md lines | > 180 without disclosure map | `lean` (warn) |
| SKILL.md lines | > 250 without progressive disclosure | `sprawl` (warn) |
| SKILL.md lines | > 400 | `subdomain-candidate` (warn) |
| `references/` substantial files | > 5 and SKILL still fat | `subdomain-candidate` (warn) |
| Multiple independent pipelines in one skill | agent judgment | `subdomain-candidate` (warn) |
| **New** skill place/ingest | > 180 lines, no disclosure map | `gate-lean` (**critical**) |

**Progressive disclosure** = SKILL.md stays a router: ordered steps + context pointers that say **when** to load which ref.

## Sub-domain hub procedure

When split alone is not enough (large tree under one domain):

1. **Name** the sub-hub (`{sub}`) — slash name == hub skill dir if a hub skill exists.
2. skill-manager **new-hub** package (ADR 0005 layout, flat):

   ```text
   hubs/{sub}/
     hub.html
     workflow.json
   ```

3. **workflow.json** fields:
   - `parent`: butler (house apex)
   - `parent_domain_hub`: owning domain (e.g. `0-skill-manager`, `0-learn`)
   - `children`: extracted skills + link types (Matt chain)
4. Parent domain: `link_type: "sub-hub"` → `{sub}`.
5. **Thin** each skill’s SKILL.md to Matt lean; re-run skill-linter.
6. Update flows-chart if user-facing.

## Report snippet

```markdown
## Lean / Matt structure
- [lean] path — 220 lines, no disclosure map → move templates to references/
- [chain-next] path — pipeline skill missing next step (expect /1-tdd or /1-code-review)

## Sprawl / sub-domain candidates
- [subdomain-candidate] path — 512 lines → split or sub-hub; first try thin + chain
```

Do not create a sub-hub without skill-manager + human confirm.
