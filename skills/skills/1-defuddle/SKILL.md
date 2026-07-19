---
name: 1-defuddle
description: Extract clean markdown content from web pages using Defuddle CLI, removing clutter and navigation to save tokens. Use instead of WebFetch when the user provides a URL to read or analyze, for online documentation, articles, blog posts, or any standard web page. Do NOT use for URLs ending in .md — those are already markdown, use WebFetch directly.
disable-model-invocation: true
---

# Defuddle

Use Defuddle CLI to extract clean readable content from web pages. Prefer over WebFetch for standard web pages — it removes navigation, ads, and clutter, reducing token usage.

If not installed: `npm install -g 1-defuddle`

## Usage

Always use `--md` for markdown output:

```bash
1-defuddle parse <url> --md
```

Save to file:

```bash
1-defuddle parse <url> --md -o content.md
```

Extract specific metadata:

```bash
1-defuddle parse <url> -p title
1-defuddle parse <url> -p description
1-defuddle parse <url> -p domain
```

## Output formats

| Flag | Format |
|------|--------|
| `--md` | Markdown (default choice) |
| `--json` | JSON with both HTML and markdown |
| (none) | HTML |
| `-p <name>` | Specific metadata property |
