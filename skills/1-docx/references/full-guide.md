# DOCX compatibility guide

Selective, version-sensitive guidance only. `../SKILL.md` is operative. This reference grants no source read,
tool installation/execution, destination write/overwrite, app/cloud access, author identity, cleanup, conversion,
publication, or distribution authority. Confirm installed tool help and the target viewer before relying on a rule.

## Capability routing

| Need | Candidate capability when already available | Proof required |
|---|---|---|
| Read text/revisions | DOCX-aware extractor such as Pandoc | Compare headings, tables, notes, and revisions to rendered pages |
| Create | OOXML library such as npm package `docx` | Package validation plus independent open/render |
| Surgical edit/comments/revisions | Unpack XML, edit minimum parts, repack | Schema/package validation and feature comparison |
| Accept tracked changes | Office-compatible application/helper | Confirm all intended revisions resolved and other features retained |
| Legacy `.doc` conversion | LibreOffice/Word converter | Compare content, layout, fields, and pagination |
| Render | LibreOffice/Word PDF export plus a renderer | Inspect changed pages and representative unchanged pages |

Do not confuse the catalog skill ID `1-docx` with a package or executable. There is no authorized default
installation command. Resolve bundled helpers under this skill's `scripts/` directory rather than assuming a
caller working directory. Test any helper on a disposable copy before user content.

## OOXML invariants

- DOCX is a ZIP package. Preserve content types, relationships, document parts, styles, numbering, themes,
  sections, headers/footers, footnotes/endnotes, comments, custom XML, metadata, embedded objects, and unknown
  extensions unless explicitly in scope.
- Reject archive traversal, symlink-like extraction, decompression bombs, duplicate/ambiguous paths, malformed
  XML, external relationships, active/embedded content, and unexpected macros before deep processing.
- Preserve element ordering required by the applicable OOXML schema and `xml:space="preserve"` where whitespace
  is significant. Do not normalize XML globally for a local edit.
- Use document numbering/list structures rather than literal bullet characters when semantic lists matter.
- Use explicit page dimensions/margins and table/cell widths when cross-viewer layout is a requirement; values
  come from the requested template/locale, not a universal Letter/A4 default.
- Page breaks belong in valid paragraph structures. Images need correct content types, relationships, dimensions,
  and meaningful alternative text when informative.
- Headings should retain outline semantics when navigation or a generated table of contents is required.

## Revisions and comments

- Make the smallest XML change and preserve run formatting. Insertions/deletions wrap whole valid runs as
  siblings; deletion text uses the deletion elements required by the target OOXML version.
- Deleting an entire paragraph may require its paragraph mark to be revision-marked; verify behavior in the
  intended editor rather than assuming XML validity proves semantic acceptance.
- Comment range markers are paragraph children, not nested inside text runs. Allocate collision-free IDs and
  update every required comments relationship/part consistently.
- Never rewrite another author's history to simulate acceptance/rejection. Preserve provenance and use the
  explicitly approved author identity and timestamp policy.
- Accepting all changes or stripping comments/metadata is destructive semantic cleanup, not routine validation.

## Verification

Record source/output hashes, sizes, package members, tool versions, operation, and intended feature changes.
Validate the ZIP and relevant XML/schema, reopen independently, compare extracted content and retained features,
then render and inspect changed pages plus risk-based samples. Verify tables, lists, headings, links, images,
alt text, fields, sections, headers/footers, comments, revisions, metadata, signatures, and accessibility only
to the extent supported by actual evidence. Viewer agreement is not standards compliance.
