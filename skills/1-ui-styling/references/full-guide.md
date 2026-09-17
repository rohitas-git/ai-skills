# UI Styling compatibility notes

`SKILL.md` is the only live scope and authority contract. These notes classify imported material so an
example cannot silently become a required workflow.

## Version-sensitive examples

The shadcn, Radix, Tailwind, responsive, theming, and accessibility references were imported from a
vendor snapshot. They can help interpret an already-installed matching stack after its actual version
and repository conventions are inspected. They do not prove current CLI syntax, package compatibility,
browser support, accessibility conformance, token ownership, or product requirements.

Examples containing package installs, `npx`, framework initialization, copied components, fixed
breakpoints, universal target sizes, hard-coded palettes, fake links/data, or demo event handlers are
illustrative only. Never execute or transplant them without satisfying the main skill's scope and
authority contract.

## Bundled helpers

- `scripts/shadcn_add.py` can invoke `npx`, download/execute a package, overwrite components, and mutate
  dependencies/source. It is non-operative for this styling skill, including its `--all` and
  `--overwrite` modes. `--dry-run` only prints a prospective command and does not prove safety.
- `scripts/tailwind_config_gen.py` can replace a destination with generated framework defaults. It is
  non-operative here. Its validation checks only a small internal shape and does not prove syntax in
  the installed Tailwind version, preservation of an incumbent config, consumer coverage, or runtime UI.
- `scripts/tests/coverage-ui.json` is a historical coverage snapshot, not current verification.

Dependency/library initialization belongs to `/1-frontend-ui-engineering` with an exact candidate,
dependency source/version, lockfile, files, network/install authority, diff review, and project checks.
Reusable token/config contracts belong to `/1-design-system`.

## Canvas and fonts

`references/canvas-design-system.md` and `canvas-fonts/` remain packaged only for imported compatibility.
Canvas artwork belongs to `/1-design` or `/1-diagram-maker`; font selection/licensing and asset
installation require their own evidence and authority. Bundled files must not be installed, copied,
loaded, or treated as approved brand assets merely because they are present.

## Evidence limits

- Existing classes compiling does not prove the intended element is visible or usable.
- A screenshot captures one state, viewport, font/rendering environment, and moment.
- Matching a generic example does not prove alignment with the repository's brand or component system.
- A clean visual diff does not prove interaction, semantics, data, analytics, or accessibility behavior.
