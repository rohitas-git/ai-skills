# PptxGenJS compatibility notes

Load only for an authorized code-generated PPTX. `SKILL.md` is operative. This file grants no dependency
installation, source/asset read, network fetch, code execution, destination write, or publication authority.
Confirm the installed PptxGenJS API/version; option names and behavior can change.

- Set layout/aspect ratio, document metadata, language, theme/fonts, and accessibility from the pinned request.
- Use fresh presentation and option objects; some versions mutate options during serialization.
- Use the library's list/bullet and line-break structures rather than literal bullet glyphs or accidental
  concatenation. Account for text-box margins when aligning shapes and text.
- Use six-digit hexadecimal colors in the representation required by the installed version; use explicit
  transparency/opacity fields rather than appending alpha when unsupported. Validate shadows and geometry.
- Preserve image aspect ratio deliberately, supply meaningful alternative text, and verify crop/resolution.
  A URL in content is not permission to fetch an image; prefer approved local assets with recorded provenance.
- Charts must use supplied, reconciled data and retain units, labels, baselines, denominators, uncertainty, and
  source citations. Styling cannot conceal material differences or fabricate precision.
- Reusable masters/components are justified by actual repetition. Avoid shared mutable option objects and
  premature abstractions for a single shape or slide.
- Run package validation, independent open/extraction, and rendered QA against the intended viewer. Library
  success only proves serialization returned, not that content, layout, accessibility, or compatibility is right.
