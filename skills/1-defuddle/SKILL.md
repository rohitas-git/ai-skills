---
name: 1-defuddle
description: >
  Extract clean markdown content from web pages using Defuddle CLI, removing clutter and
  navigation to save tokens. Use instead of WebFetch when the user provides a URL to
  read or analyze, for online documentation, articles, blog posts, or any standard web
  page. Do NOT use for URLs ending in .md — those are already markdown, use WebFetch
  directly. Use when: Extract clean markdown content from web pages using Defuddle CLI,
  removing clutter and navigation to. Hub: /0-office.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-office
    role: leaf
    when:
      - "Extract clean markdown content from web pages using Defuddle CLI, removing clutter and navigation to"
    triggers:
      - "1-defuddle"
      - "defuddle"
    requires_setup: false
---

# Defuddle

## Process

1. Follow the steps and hard rules in this skill.
2. Load linked `references/` only when the branch needs them.


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


## Related

**Next:** `/0-office`. Parent hub: `/0-office`.
