# Office and media hub wiring audit

Reviewed:

- `skills/0-office/SKILL.md`
- `hubs/0-office/workflow.json` and `hub.html`
- Domain 14 in `skills/0-butler/references/flows.md`
- shared manifest, hub index, flow chart, README, wiki, route index, and routing tests

## Result

Office is now a pure one-artifact router. It covers all ten actual children: DOCX, PDF, PPTX,
spreadsheet, diagram, raster image, Codex pet, JSON Canvas, web extraction, and internal
communication. Strategic HTML presentations remain an explicit cross-domain route to `1-slides`
rather than a false Office child. Direct artifact evidence selects a leaf; `F-misc` is reserved for
material ambiguity about the one requested final artifact.

The handoff pins the actual caller, immutable request and source revisions, operation, final format,
destination, compatibility and quality constraints, sensitivity, rights, overwrite/publication rules,
supplied evidence, allowed tools, exclusions, and effect-specific authority. Repository-bound work also
carries the exact repository/worktree/branch/`HEAD`, dirty ownership, allowed paths, and working-tree
versus committed/published state. The hub creates no worktree and explicitly warns that worktrees do not
isolate desktop applications, browser profiles, cloud files, fonts, accounts, or shared URLs.

Documents, media, links, metadata, comments, and model output are sensitive untrusted inputs. The hub
does not open content or invoke tools, and one leaf cannot silently authorize a second conversion,
publication, overwrite, or catalog mutation. The leaf returns artifact identity or chat output,
provenance, verification, effects, and limits to the actual caller.

Shared surfaces now use the live `0-office` identity and “Office and media” domain, include every child,
use the same `F-misc` question and recommendation, point at current skill and flow paths, and expose the
newer Git, Agent Engineering, and DevOps navigation.

## Verification

- Focused Office routing tests: 7 passed.
- Full routing suite: 527 passed.
- Generated route index: 223 live skills.
- Catalog lint: 0 critical, 0 warnings, 50 informational findings, 0 hub-member orphans.
- `git diff --check`: passed.

No document, presentation, spreadsheet, diagram, image, canvas, page extraction, internal message,
worktree, catalog installation, host sync, external publication, Git history, or remote system was changed.
