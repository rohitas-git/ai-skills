# Placement examples

These are decision patterns, not prescribed filenames.

## Changed authentication behavior

Update the existing current authentication guide and public contract owner if their claims changed.
Do not edit an accepted ADR unless the repository's ADR lifecycle permits status metadata changes;
a materially new consequential decision may warrant a successor through `/1-domain-modeling`.

## New internal implementation detail

If no reader needs to operate, integrate with, or understand a non-obvious constraint, no living-doc
update may be necessary. Record a reviewed no-doc-impact attestation when a trigger matched.

## Changed public API

The governing OpenAPI/schema/interface contract is primary for the public surface; a guide may also
need updated examples or migration notes. Route compatibility design to `/1-api-and-interface-design`.

## Superseded design

First ensure current docs describe supported behavior. Preserve historical rationale according to
the repository's archive/ADR convention and link forward. Never rewrite history to look current.

## New term

Update the established glossary/domain model if it changes shared language. Do not create a page for
one definition when the canonical glossary already owns it.

## Duplicate guide

Prefer the existing canonical owner. If ownership is genuinely split, document the boundary and
navigation rather than copying the same explanation into two files.
