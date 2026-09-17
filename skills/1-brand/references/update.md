# Historical brand-update workflow

This file records the retired imported `brand:update` behavior. It is not live execution guidance.

The former workflow combined:

- interviewing for brand choices;
- editing a brand-guideline document;
- synchronizing JSON and CSS design tokens;
- validating generated context;
- optionally generating an image;
- reporting the multi-file result.

Those are separate jobs and authority classes. Current routing is:

- `/2-brand-guidelines` for one brand-contract draft or authorized edit;
- `/2-brand-review` for one read-only candidate review;
- `/2-brand-context-extract` for one read-only context packet;
- `/1-design-system` for durable token specifications or an explicitly authorized synchronization;
- `/1-design` or `/1-banner-design` for creative assets.

This historical file grants no file write, token sync, tool execution, image generation, approval, publication, Git,
or downstream-work authority. Do not execute the archived presets, `.claude/skills` paths, or “sync all files” rule.
