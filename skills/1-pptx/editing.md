# PPTX template and OOXML compatibility notes

Load only for an authorized template/XML operation. `SKILL.md` remains operative; this reference grants no
source read, mutation, cleanup, app, subagent, overwrite, or publication authority.

- Hash and render the immutable template, inventory slide/layout/master/theme/media/notes/relationship parts,
  and confirm license/attribution plus allowed reuse before adapting it.
- Complete a planned structural mapping before text/media edits. Delete or duplicate slides through a
  relationship-aware helper; manual file copying can orphan notes, media, content types, and relationship IDs.
- Preserve stable slide IDs, masters, layouts, themes, transitions, notes, comments, accessibility properties,
  unknown extensions, and untouched package parts unless explicitly in scope.
- Target XML elements by stable identity plus expected current content. Do not replace every matching string or
  globally normalize namespaces/formatting. XML edits must preserve required ordering and significant whitespace.
- Use semantic paragraph/list structures rather than literal bullet glyphs. Preserve original run/paragraph
  formatting unless the operation changes it. Longer replacement text requires rendered overflow inspection.
- Removing a placeholder means removing only the mapped placeholder group and its now-unreferenced resources;
  blanking text alone can leave misleading visuals. Cleanup is allowed only inside the exact output copy.
- Bundled helpers include `scripts/add_slide.py`, `scripts/clean.py`, `scripts/thumbnail.py`, and `scripts/office/`
  packaging utilities. Observe their help/version and test on a disposable copy before user content.
- Parallel slide editing is optional only when separately authorized, files/relationships are proven disjoint,
  and one owner integrates and verifies the entire package. It is never mandatory.

After repacking, validate package relationships/content types, independently reopen, compare retained features,
extract content/notes, and render the relevant slide set. XML validity does not prove visual fidelity.
