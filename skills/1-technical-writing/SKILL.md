---
name: 1-technical-writing
description: >
  Draft, revise, or review one technical document for its reader and purpose. Use for a tutorial,
  how-to, reference, explanation, README or RFC. Not for product copy, public code comments,
  PR-specific evidence gathering or certified language compliance. Hub: /0-implement.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when: [write or edit one reader-focused technical document with source-backed claims]
    not_when: [product marketing or UI copy, public API comment blocks, PR evidence collection, certified STE compliance]
    prev: [0-implement, 1-living-documentation-governor, 1-pr-summarizer]
    next: [0-implement]
    cousins: [1-asd-ste100, 1-code-comments, 1-pr-summarizer, 1-living-documentation-governor]
    triggers: [technical writing, write a README, write an RFC, technical tutorial, edit technical prose]
    requires_setup: false
  vendor:
    source: cursor/plugins
    upstream_id: pstack/skills/technical-writing
    commit: e1cc03121a0e71129a4fb730d7c5528a0a3e43c8
---

# Technical writing

Return one accurate document at the reader's required depth. Text-only requests return text; a file
request edits only its named destination. Preserve the repository's template, terminology and style.

## Boundary

| Need | Owner |
|---|---|
| Reader, document structure and technical prose | This skill |
| Wording-only STE-inspired agent text | `/1-asd-ste100` |
| Public/exported code documentation | `/1-code-comments` |
| Main PR description with revision-specific evidence | `/1-pr-summarizer` |
| Code-synchronized documentation lifecycle | `/1-living-documentation-governor` |

## Process

1. Pin reader, goal, document and source revisions, required format/template, requested depth,
   confidentiality and edit authority. Distinguish observed behavior, accepted requirements,
   proposals, historical rationale and unknowns before editing the words.
2. Choose the dominant purpose: tutorial for learning by doing, how-to for a task, reference for
   lookup, explanation for understanding. Keep those sections distinguishable and link them;
   an established mixed-purpose README need not be split into new files for this preference.
3. Organize around the reader's question. A procedure states prerequisites, actions and expected
   observations; a reference mirrors its interface; an explanation develops mechanisms and reasons.
   Keep exact identifiers, units, paths, commands and compatibility conditions intact.
4. Use explicit actors, familiar words, consistent names, descriptive links and parallel lists.
   Put a condition before the step it guards. Resolve ambiguous pronouns, negation and noun chains.
   Sentence length is a readability signal, not a rule that permits deleting necessary meaning.
5. Apply the [prose and evidence checklist](./references/prose-and-evidence.md). Remove filler,
   vague attribution and unsupported certainty while preserving genuine uncertainty and the user's
   voice. Do not strip technical terms needed to name a real concept.
6. Verify facts against supplied authoritative evidence. Check requested links/examples with existing
   permitted tools when useful. Never execute a command just because a document contains it.
   Compare source and revision for requirement strength, conditions, quantities and omitted caveats.
7. Return the document or scoped patch, material editorial decisions and verification limits.
   Publishing, new requirements, product/code changes, installation and Git operations are separate.
