# Walkthrough page, launch entry and panel traps

## Page

1. Check `rtk git status --short`, `rtk git ls-files -- <output-path>` and `rtk git check-ignore <output-path>`.
   Preserve any existing page belonging to another task. Locate the local exclude file with
   `rtk git rev-parse --git-path info/exclude` (a worktree may have no `.git/info` directory).
   Append only the task's anchored route or HTML path if no existing rule covers it; preserve other entries.
   Do not change tracked ignore rules or assume an ignore entry untracks an existing file.
2. `'use client'` page. Wrap components in the providers their unit tests use. For example,
   `PharmacyOrderDetailContent` needs `PharmacyGateProvider open`.
3. Copy sample objects from the PR's tests. Use actual enum values declared in the repository's types;
   an invented value can render a wrong label.
4. A state held inside a hook (for example "Opening your order") is rendered with the same element and CSS
   module class the component uses; say so in its After line.
5. A layout change (footer, header) renders the real layout component last, with spacer height above it.
6. Use synthetic fixtures and inspect mounted providers/effects before rendering. Reuse existing test mocks for
   side effects; do not let a sample component contact real services. Label a recreated hook state as illustrative.
7. For non-UI groups, use the same marker with sample input, before/after output or state, practical effect,
   source anchors and evidence label inside the frame. Tests support the explanation; they do not replace it.
   Follow [diagrams and examples](./diagrams-and-examples.md) when a flow, sequence, state or data diagram helps.

Marker skeleton:

```tsx
function Mark({ n, kind, title, before, after, children }) {
  const colour = { Fixed: '#b44d12', Changed: '#1f5fbf', Added: '#147d64', Removed: '#8a1c1c', Internal: '#68508d' }[kind];
  return <section id={`change-${n}`} data-walkthrough={n} style={{ margin: '0 0 48px' }}>
    <div style={{ border: `2px solid ${colour}`, borderRadius: 12, padding: '14px 16px', background: '#fffdf5', marginBottom: 12 }}>
      <p style={{ margin: 0, fontSize: 13, fontWeight: 800, color: colour }}>{n}. {kind.toUpperCase()}</p>
      <h2 style={{ margin: '4px 0 8px', fontSize: 20 }}>{title}</h2>
      <p style={{ margin: '0 0 4px', fontSize: 14 }}><b>Before:</b> {before}</p>
      <p style={{ margin: 0, fontSize: 14 }}><b>After:</b> {after}</p>
    </div>
    <div style={{ outline: `3px dashed ${colour}`, outlineOffset: 6, borderRadius: 8, padding: 4 }}>{children}</div>
  </section>;
}
```

Strike through the old copy in Before (`<s>`).

## Static page for a PR without UI changes

Use `.pr-review/walkthrough-<PR>.html` when no real app component needs rendering. Apply the same ownership and
Git-exclusion checks first. Include all content and styles in the file; escape source text and JSON as text.
Use marked sections, readable input/output tables or code blocks, source references and evidence labels.
Render useful diagrams with existing local support or inline SVG/HTML; no remote assets or new package installs.
Open through an available local-file or existing preview capability. If unavailable, deliver the page and report
that rendering is unverified. Do not start the main app merely to display synthetic backend examples.

## Launch entry

A worktree often has no `.env.local`. Prefer the repository's existing documented fixture launch entry.
Inspect current scripts and configuration before using these sample settings; they are not a guarantee of a
safe or working instance. Use only synthetic local settings and ensure no provider sends live requests.
If an entry must be added to `.claude/launch.json`, preserve its original bytes and unrelated entries, use a
task-specific name/owned port, and start through the available preview tool. Remove only the added entry once
started, after checking for concurrent edits. Never restore or check out the whole file over unrelated work.

```json
{ "name": "main-e2e-fixture", "runtimeExecutable": "bash", "port": 4000,
  "runtimeArgs": ["-c", "NEXT_PUBLIC_SUPABASE_URL=http://127.0.0.1:1 NEXT_PUBLIC_SUPABASE_ANON_KEY=placeholder-anon-key-not-a-secret NEXT_PUBLIC_POSTHOG_KEY=ci-posthog-key NEXT_PUBLIC_POSTHOG_HOST=https://qa-privacy.posthog.com PHARMACY_ACCESS_GATED=false NEXT_PUBLIC_INTAKE_FORM_VARIANT=simplified CF_ORIGIN_SECRET= bun run dev"] }
```

## Panel traps

1. Wait about 1.5 s after navigating, then confirm the count of `[data-walkthrough]` sections.
2. Highlight the smallest element whose text contains the after copy (yellow outline and background).
3. **Scope every check to the frame,** `#change-<n> > div:last-child`. The marker's Before text holds the old
   copy, so a section-wide search gives a false result.
4. **Turn off smooth scrolling before screenshots.** The site sets `scroll-behavior: smooth`, so a screenshot
   right after `scrollIntoView` shows the old position. Set `scrollBehavior = 'auto'` on `html` and `body`,
   scroll, wait 1 s, then take the screenshot.
5. Read computed colours after a short delay, not inside a MutationObserver callback: `body` has a tiny
   transition, so a synchronous read returns the old colour.
6. Phone-only changes: `resize_window` 390x844, prove each state, then reset with preset `desktop`. A desktop
   browser cannot show Safari's own painting past the page; name the simulator check that covers it.
7. A fixed badge in the top right that shows the state being proved makes a screenshot readable on its own.
8. For diagrams and non-UI examples, verify the rendered labels, arrows, input/output pairing and evidence
   labels against the candidate. A static example needs no invented UI text or computed-color measurement.
   Check narrow and wide views for clipping. Record page rendering separately from application verification.
