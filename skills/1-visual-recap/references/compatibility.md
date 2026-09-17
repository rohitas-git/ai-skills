# Visual Recap compatibility notes

`SKILL.md` owns scope and authority. These concepts come from an archived BuilderIO snapshot and must be
reconciled with the installed Plan connector/renderer before a persisted artifact is authored.

- Visual blocks may include file trees, focused diffs/annotated code, schema/API maps, diagrams, and
  wireframes. Use only what materially improves the named review question.
- Structured content should carry stable unique IDs and exact source locators when the current schema
  supports them. Block/tag/property names are versioned; obtain them from the installed renderer.
- UI wireframes are explanatory reconstructions unless backed by captured runtime evidence. Preserve the
  incumbent product shell and label inference; do not present mockups as screenshots or implemented truth.
- Local files, hosted Plan writes, self-hosted writes, bridge preview, browser render, comments, sharing,
  export, and PR publication are distinct effects.
- A local-files mode can avoid Plan database writes but does not make the language model, hosted renderer,
  browser, or repository content local. Verify the actual data path and privacy contract.
- Absolute links must come from the store that actually owns the artifact. Never guess an origin or place
  capability/local-preview tokens in a URL shared with the model or reviewer.

The archive's mandatory publication, whole-thread scope, numeric block/tab budgets, automatic browser open,
GitHub Action, connector recovery, feedback-to-code loop, commands, ports, schemas, auth model, and `npx
@latest` recipes are non-operative.
