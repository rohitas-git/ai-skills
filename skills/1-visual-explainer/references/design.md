# Visual and language guidance

Use this before authoring HTML. User requirements and the project's design system take priority.
For repository-branded work, follow its applicable `docs/brand.md`.

## Choose a visual register

| Register | Best use | Adaptable treatment |
|---|---|---|
| Instrument | Metrics, status, evidence comparisons | Aligned cells, tabular numbers, labeled status shapes |
| Blueprint | Architecture, system boundaries, data paths | Restrained grid, dashed boundaries, direct edge labels |
| Paper | Concepts and mechanisms | Narrow text measure, generous figures, quiet source notes |
| Editorial | Context recaps and narrative | Clear typographic hierarchy, varied density, deliberate empty space |

The register is a layout choice, not a dependency on upstream CSS. Define a small set of local
CSS variables for spacing, type, color, and meaningful status. Use available local fonts.
A system font stack is acceptable. Avoid adding external fonts merely to satisfy a style preference.

## Let the figure carry the explanation

- One claim per figure. Write its caption as the fact it teaches, not just its topic.
- Draw the mechanism: a request reading the cache, not a box named “cache.”
- Label arrows with actions such as “reads” or “sends.” Mark sync/async meanings in a legend.
- Show changes as a changed box, edge, state, or value. Use the same layout across cases.
- Keep one dominant visual element per section. Place related labels close to what they describe.
- Start with space, then subtle rules, then frames. Avoid repetitive cards, nested cards,
  decorative gradients, unnecessary icons, and motion that competes with the explanation.
- Encode meaning through text, position, shape, or line style as well as color.
- Use an overview and separate detail when one drawing becomes crowded. Do not shrink labels
  until a complex system fits into a tiny screen.

## Words and reading load

Answer first. Use headings that state takeaways. Prefer active voice, short sentences,
one idea per sentence, and one term for one concept. Define abbreviations once.
Aim for sentences around 20 words, but preserve exact meaning over a length target.
Use brief paragraphs and numbered steps for real sequences. Keep uncertainty when evidence is uncertain.
Do not force every number into a chart or remove necessary reasoning to meet a prose quota.

## Accessibility and responsiveness

- Use semantic headings, `<main>`, `<figure>`, and `<figcaption>`.
- Give an SVG a `viewBox`, title, and accessible description. Include its core claim in text.
- Maintain readable contrast: 4.5:1 for normal text and 3:1 for meaningful graphical boundaries.
- Keep essential labels available without hovering. Provide keyboard equivalents and visible focus.
- Keep code in its own scroll container. Let long paths wrap. Avoid horizontal page overflow.
- Stack comparison panels on narrow screens. Keep labels readable at the rendered size.
- If supporting light/dark themes, test both. Do not claim accessibility compliance from structural checks alone.
- Ensure print, reduced-motion, and no-JavaScript views retain a useful explanation.

Sources belong in a visible final section, with exact code locators or direct source links.
Extra raw material may sit in `<details>`; key limits and counterexamples must remain visible.
