# PPTX capability routing

Version-sensitive guidance only; `../SKILL.md` is operative. This file grants no source read, installation,
execution, destination write/overwrite, app/cloud/network access, cleanup, export, presentation, or publication
authority. Confirm installed tool help and the intended viewer before relying on a capability.

| Need | Candidate capability when already available | Proof |
|---|---|---|
| Read text/notes | PPTX-aware extractor | Reconcile slide order, notes, tables, and charts with render |
| Inspect overview | bundled `scripts/thumbnail.py` | Confirm every slide represented and readable enough for triage |
| Template/XML edit | unpack, focused edit, `scripts/add_slide.py`/`clean.py`, repack | Package validation and feature comparison |
| Create from code | PptxGenJS compatible with installed version | Independent open plus content/render checks |
| Render for QA | trusted office renderer to PDF/images | Inspect changed slides and risk-based samples |

Resolve every helper from this skill directory; do not assume stale `scripts/0-office/` paths or caller CWD.
Rendering or extraction of an untrusted deck requires a verified low-privilege sandbox with active/external
content disabled. Temporary PDF/images are QA artifacts, not deliverables, and need bounded paths and cleanup
authority. External fonts/images require separate provenance, rights, privacy, and network checks.

Design follows the supplied brand/template, audience, purpose, content density, and viewer constraints. No
palette, font, margin, layout variation, visual-per-slide quota, or title ornament is universally correct.
Charts must preserve units, scales, denominators, uncertainty, and cited source meaning.

Verification must distinguish package validity, semantic content, rendered appearance, and target-viewer
compatibility. Check leftover placeholders based on the actual template, not only a fixed word list.
