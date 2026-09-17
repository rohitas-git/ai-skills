# Design System compatibility notes

`SKILL.md` owns scope and authority. This file documents bundled compatibility assets without turning them into a
mandatory pipeline.

## Contract model

A contract set may contain a source schema plus explicitly requested derived representations. The common
primitive → semantic → component model is useful when:

- raw values change independently of meaning;
- themes remap semantic roles;
- components need demonstrated local variation.

Use fewer layers when consumers do not need those seams. Existing repository schema and consumers outrank the
bundled examples.

## Local helpers

Resolve the live skill directory and inspect the helper before invocation:

```text
node <skill-dir>/scripts/generate-tokens.cjs --config <exact-source>
node <skill-dir>/scripts/validate-tokens.cjs --dir <exact-scope>
```

The generator defaults to stdout; prefer that for comparison. Writing with `-o` changes a file and requires an exact
destination, current-revision check, and overwrite authority from the main skill. The validator is read-only even
with its misleading `--fix` flag (it only changes report wording), but it is regex-based and can emit false positives
or miss context. Neither helper validates contrast, runtime rendering, naming fitness, or consumer compatibility.

`embed-tokens.cjs` searches upward from the current directory for a project-specific path and is unsuitable unless
that discovery rule is explicitly accepted. `html-token-validator.py` contains project-layout and palette
assumptions; it is not a general design-system verifier.

## Legacy slide assets

The following files remain physically in this imported package for compatibility, but presentation behavior is owned
by `/1-slides` or `/1-pptx` and they are non-operative here:

- `data/slide-*.csv`;
- `scripts/search-slides.py` and `slide_search_core.py`;
- `scripts/generate-slide.py` and `fetch-background.py`;
- `scripts/slide-token-validator.py` and slide/infographic modes in `html-token-validator.py`.

They grant no network, image-download, HTML-generation, deck-writing, dependency-install, browser, or publication
authority. Rehousing them requires a separate dependency-preserving catalog maintenance change.

## Evidence limits

- A valid schema is not a usable design system.
- A resolved alias is not proof of accessible contrast.
- A clean hardcoded-value scan is not proof that every value should be tokenized.
- Generated CSS equality is not runtime visual equivalence.
- Example defaults and cited standards can become stale; verify current requirements when the decision depends on
  them and current-source/network authority exists.
