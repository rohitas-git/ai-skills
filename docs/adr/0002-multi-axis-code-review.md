# ADR 0002: Multi-axis code-review

## Status

Accepted

## Context

`code-review` (maintainability-only) and `code-review-v2` (Spec + Standards) competed as post-implement closers. Flows historically described a two-axis review under the name `code-review`.

## Decision

- Single live skill **`code-review`** with three axes: **Spec**, **Standards**, **Maintainability**.
- Pre-review scan runs **every applicable** axis; soft-skips Spec without a spec source; Standards may run baseline smells when docs are thin; Maintainability always runs on a non-empty diff.
- **`code-review-v2`** is deprecated (tombstone → `code-review`).
- **`implement`** closer is multi-axis `code-review` only.
- Not axes: `check-work` (mid-build), `ponytail-review` (over-engineering satellite), `codebase-review-strategy` (whole-repo planning), `pr-summarizer` (PR prose).

## Consequences

One review entry for implement and branch review; axis reports stay separate so Spec fails cannot be masked by Standards passes.
