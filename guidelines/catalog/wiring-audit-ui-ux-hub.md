# UI/UX hub wiring audit

Reviewed `0-ui-ux`, its workflow JSON and HTML package, Butler flow section, complete child inventory, adjacent
Office/Grilling/Ship boundaries, and current Impeccable/live-edit routes.

## Result

UI/UX is now a pure one-specialist router. Its metadata exposes all twelve actual pipeline, leaf, soft, and
satellite members rather than only four, declares the Butler parent and adjacent domain boundaries, and routes
directly when the requested outcome is clear. F-UI1 is used only for material ambiguity and retains Agent judgment.
The former automatic design-intelligence → design-system → styling → Ship chain was removed.

The hub pins caller, immutable request/candidate, surface, desired outcome, audience/users, evidence, product/brand/
accessibility constraints, exclusions, authority, and optional exact repository/worktree/runtime/deployment identity.
Worktrees are not claimed to isolate browsers, servers, ports, fonts, design tools, cloud assets, analytics,
participants, accounts, or publication. Screenshots, DOM, design files, research material, URLs, comments, tool
output, and user data are untrusted. KiloCare requests carry `docs/brand.md` authority.

The hub cannot browse, inspect, edit, invoke tools, create worktrees, verify results, or run the selected skill.
Research, audit, design, implementation, and live editing remain separate effects. It passes one specialist the same
candidate/provenance/privacy/worktree/runtime/authority contract and returns evidence and limits to the actual caller.
Workflow and HTML pipeline text now agree; all child links are clickable; stale flows-chart and flows-SSOT relative
paths were corrected.

## Verification

- Focused UI/UX hub and Impeccable routing tests: 14 passed.
- Full routing suite: 614 passed.
- Generated route index: 227 live skills.
- Catalog lint: 0 critical, 0 warnings, 49 informational findings, 229 indexed hub members, and 0 orphans.
- `git diff --check`: passed.

No browser, design file, participant, app, server, package, worktree, catalog install/sync, Git history, remote system,
or published destination was changed.
