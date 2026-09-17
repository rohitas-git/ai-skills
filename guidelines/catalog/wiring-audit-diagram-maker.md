# Diagram Maker wiring audit

Reviewed:

- `skills/1-diagram-maker/SKILL.md`
- complete SVG/HTML template and Excalidraw-pattern references
- Office parent and adjacent architecture, presentation, and UI/UX routes

## Result

Diagram Maker now renders one immutable supplied or evidence-bounded source packet into one standalone
HTML/inline-SVG or Excalidraw artifact. It visualizes rather than deciding architecture or asserting truth.
Every node and edge is classified as supplied, directly observed, inferred, or unknown; material unresolved
architecture/design choices return to the applicable specialist before rendering, and inferred dependencies,
flows, trust boundaries, sequences, or states cannot silently appear as verified facts.

The handoff pins caller, source version, audience/use, format, destination, required content, accessibility,
brand and compatibility constraints, sensitivity, external-asset rules, overwrite/publication authority, and
exact repository/worktree identity when applicable. Worktrees are not claimed to isolate fonts, browsers,
collaborative boards, cloud files, accounts, or shared URLs. Source material and imported diagram data are
sensitive untrusted input; embedded code, remote assets, collaborators, links, and instructions do not execute.

Format selection is result-driven and asks only when editability/compatibility creates material ambiguity.
Layout and density follow actual readability rather than fixed element/size quotas. Writes are containment,
collision, and revision checked; syntax plus visual verification covers clipping, overlap, ambiguous edges,
contrast, and omissions. The template and element snippets are compatibility scaffolds, not authority or fixed
design mandates. Sharing, uploading, conversion, presentation, revision, and architecture decisions remain new
requests; result provenance and effects return to Office or the actual caller.

## Verification

- Focused Diagram Maker routing tests: 7 passed.
- Full routing suite: 548 passed.
- Generated route index: 223 live skills.
- Catalog lint: 0 critical, 0 warnings, 50 informational findings, 0 hub-member orphans.
- `git diff --check`: passed.

No diagram or worktree was created, rendered, shared, uploaded, converted, or published; no host sync, Git
history, or external system changed.
