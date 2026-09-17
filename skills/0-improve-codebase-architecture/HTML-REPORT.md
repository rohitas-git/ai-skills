# Static architecture report

Use only when the user asks for HTML or an interactive/visual artifact materially improves the
candidate comparison. Markdown remains the default. The report is read-only evidence output, not
permission to edit the repository or implement a candidate.

## Output and safety

- Write to a user-approved path or a unique file under the OS temporary directory; never overwrite
  an existing path without approval. Return the absolute path and do not open a browser/app unless
  requested.
- Produce one standalone UTF-8 HTML file with inline CSS and optional inline SVG. Do not import
  Tailwind, Mermaid, fonts, analytics, images, or any other network asset. Do not execute scripts.
- HTML-escape all repository paths, snippets, branch names, ADR titles, and other inspected text.
  Never place secrets, credentials, environment values, raw logs, or unnecessary source content in
  the report.
- Record repository/worktree identity, scope, comparison/base, generated time, excluded areas, and
  whether the scan is partial. Do not claim the report reflects unscanned code.

## Structure

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Architecture candidates — {{escaped repository}}</title>
  <style>
    :root { color-scheme: light dark; font-family: system-ui, sans-serif; }
    body { margin: 0; line-height: 1.5; }
    main { max-width: 72rem; margin: auto; padding: 2rem; }
    article { border: 1px solid #8888; border-radius: .75rem; padding: 1rem; margin-block: 1rem; }
    .meta { color: #777; }
    .comparison { display: grid; grid-template-columns: repeat(auto-fit,minmax(18rem,1fr)); gap: 1rem; }
    code, pre { overflow-wrap: anywhere; }
  </style>
</head>
<body><main>
  <header>...</header>
  <section aria-labelledby="candidates">...</section>
  <section aria-labelledby="recommendation">...</section>
</main></body>
</html>
```

## Candidate card

Each candidate includes:

- title and confidence (`Strong`, `Worth exploring`, or `Speculative`);
- exact inspected files and observed evidence;
- current caller/dependency/effect shape and proposed responsibility shift;
- before/after diagram only when it clarifies the relationship;
- expected leverage/locality plus compatibility and migration cost;
- verification plan, contradictory evidence, ADR conflict, and residual risk.

Use semantic headings, readable contrast, visible focus if links exist, and text alternatives for
SVG diagrams. Keep prose concise, but use the repository's actual domain language. The top
recommendation explains why it outranks the others; it does not authorize implementation.

## Completion check

- File is unique, local, standalone, script-free, and contains no remote references.
- Untrusted text is escaped and sensitive data excluded.
- Every claim links to visible local evidence in the report; uncertainty and coverage gaps are
  labeled.
- The returned response provides the path and waits for a user decision when one is required.
