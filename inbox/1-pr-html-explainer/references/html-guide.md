# HTML review page guide

## Shared visual guidance

Use Visual Explainer's [design guidance](../../../skills/1-visual-explainer/references/design.md)
for visual hierarchy, simple English, accessibility, and responsive layout.
Use its [figure patterns](../../../skills/1-visual-explainer/references/figures.md) for consistent
before/after diagrams and source-backed state or request flows.
For optional reviewer-controlled steps or toggles, use its
[interaction guidance](../../../skills/1-visual-explainer/references/interaction.md).
The PR workflow retains the section order, focused snippets, evidence requirements, and output path below.

## Recommended sections

Adapt this order only when another order teaches the PR more clearly.
Keep the takeaway brief and finish with an evidence reference or link to verification.

| Section | Content |
|---|---|
| Hero | PR number/title, one-sentence summary, branch, optional link, and observed status. Include files changed, tests added, or packages affected only when known and useful. |
| Problem | Previous behavior and why it was wrong, confusing, missing, or risky. Attribute stated reasons and label inferred intent. |
| System context | Product or architecture location, upstream callers, downstream effects, and rationale for the layer when supported. Mention behavior intentionally preserved when relevant. |
| Before/after flow | Old and new paths under the same conditions. Show changes in state, ownership, permissions, requests, data, or component relationships. |
| Code walkthrough | Ordered feature groups, focused snippets, file paths, what each change does, and why it belongs in the story. |
| Tests / verification | Added or updated tests, exact available commands, results, tested revision, manual checks, warnings, failures, and unknowns. |
| Reviewer takeaway | A short explanation the reader can remember and specific areas to examine in the actual diff. Avoid approval or correctness claims. |

For internal refactoring, say when behavior is intended to remain the same.
Explain the changed structure and who maintains or uses it.
Do not invent a user-visible benefit.

## Diagrams

Add a diagram only if you can say what it helps the reader understand faster.
Prefer HTML/CSS with an equivalent reading order in text.
Label both paths and conditions. Do not rely on color or arrows alone.

Useful forms include:

- Request flow: Client → Server → Handler → Service → Result.
- Before/after path: previous path alongside changed path.
- Ownership map: package or module responsibility boundaries.
- Data transformation: input → normalized form → output.
- State machine: pending → running → complete or error.

Use only nodes and transitions supported by the source.
Stack diagrams vertically on narrow screens when needed.

## Focused diff snippets

Select important snippets along the explanation path. Show enough context to preserve meaning.
Each snippet needs a file path, relevant added/removed lines, visual distinction,
a short explanation, and its connection to the PR story.

This pattern demonstrates presentation only. Replace its content with escaped, source-backed lines.
Include its styles in the page's embedded stylesheet.

```html
<figure class="diff">
  <figcaption>packages/example/src/file.ts</figcaption>
  <pre><code><span class="del">- old behavior</span>
<span class="add">+ new behavior</span></code></pre>
  <p>Explain what this change does and why it matters here.</p>
</figure>
```

Keep the literal `+` and `-` markers so color is not the only distinction.
Escape `&`, `<`, and `>` in code and source text. Escape attribute values separately.
Preserve whitespace. Allow horizontal scrolling inside snippets instead of across the page.
Keep snippets small rather than hiding giant patches in disclosure controls.

## Verification presentation

Separate application evidence from checks of the generated page.
For each observed application check, show its exact command, result, and tested revision when known.
If the revision is unknown, say so. Link supplied CI evidence when available.

Use explicit labels such as **Passed**, **Failed**, **Not run**, or **Revision unknown**.
Never manufacture commands, test output, test totals, package counts, timing, or passing status.
An example command from a supplied guide is not proof that the command ran in this repository.

State recommended but unexecuted commands separately. Mention relevant warnings or failures,
including the evidence for calling them unrelated. Finish with what remains unverified.
