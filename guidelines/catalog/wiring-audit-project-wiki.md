# Project-wiki-manager wiring audit

Date: 2026-09-11  
Skill: `1-project-wiki-manager`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete main skill and all eight operative references, Architecture parent body/HTML/
workflow/flow and generated route, catalog descriptions, worktree/write authority, and regressions.
This audit validates the wiki workflow; it does not create or inspect a separate project's wiki.

## Decisions and changes

- Kept one atomic job: maintain or query one repository's source-grounded concept wiki. Living-doc
  trigger governance, personal Obsidian notes, design-time domain decisions, and standalone resource
  extraction retain their specialist owners.
- Preserved Architecture ownership and F-D1/F-D2 boundaries. Clear destinations route directly;
  users are not forced through a second selection or silent cousin activation.
- Added project and caller provenance: root, exact worktree/branch/HEAD, wiki/source roots, dirty-file
  ownership, query/audit/write mode, and caller return. Query/audit need no worktree; authorized edits
  reuse the matching caller worktree or conditionally obtain isolation through `1-git-worktrees`.
- Made layout repository-sensitive. Existing conventions outrank a fixed `docs/raw`/`docs/wiki`
  layout; that structure is only a new-wiki default, not an automatic migration target.
- Resolved the code-access contradiction. Declared raw material remains immutable, while explicitly
  in-scope project docs, source code, tests, schemas, and decisions may be read and cited. Secrets and
  unrelated user content remain excluded. Code evidence establishes repository implementation, not
  deployed behavior or product intent by itself.
- Replaced redundant approval ceremony. A clear initialize/ingest/update request authorizes scoped
  wiki writes; the skill pauses only for materially different roots, source authority, destructive
  restructuring, or unresolved high-blast decomposition.
- Replaced quotas and hard-coded format dogma with evidence-dependent choices: no fixed takeaway/page
  counts, word thresholds, flat-layout mandate, sentinel requirement, English rewrite, or graph-density
  target. Existing local conventions win.
- Simplified the mandatory Q&A template to answer + contributing sources + present conflicts/limits.
  Empty quote blocks, separator boilerplate, and automatic “wiki gap” promotion are gone; query mode
  remains read-only.
- Strengthened grounding by separating observed claims, agent synthesis, user-confirmed decisions,
  and unknown/conflicting evidence, with format-appropriate locators and no fabricated access data.
- Kept audit separate from repair. Audits report evidence, impact, confidence, coverage, and smallest
  fix; authorized changes inspect the scoped diff and validate links, sources, index, and log.
- Reduced operative package instructions from 652 lines to 425 while retaining all eight mode-specific
  references and making every reference no more than 59 lines.
- Prohibited branch switching, stashing, installs, shared resets, source mutation, commit, publication,
  deployment, merge, remote knowledge-system writes, and cross-worktree output copying.

## Verification

- `python3 -m unittest scripts/test-routing.py`: **77 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 63 informational findings, and
  0 hub-member orphans.
- `git diff --check`: passed.
- `ProjectWikiRouteTests` covers parent/F-D1 agreement, caller/worktree/mode authority, local link
  resolution, reference size, code-source support, nonredundant approval, flexible language/layout,
  and removal of the rigid response template.

## Remaining limits

- A concrete repository may impose different wiki conventions, which deliberately remain local
  authority and therefore cannot be prevalidated here.
- Other Architecture documentation children remain semantically pending.
