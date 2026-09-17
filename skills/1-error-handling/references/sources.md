# Source ledger

Reviewed 2026-09-11. Scope: failure behavior in general software development, with TS/JS examples. The live skill is an original selective synthesis, not an installed upstream package. No upstream scripts, dependencies, hooks, permissions, or platform configuration were adopted or executed.

## Requested sources

| Source | Fixed revision and selected files | Contribution |
|---|---|---|
| [wshobson error-handling-patterns](https://github.com/wshobson/agents/blob/main/plugins/developer-essentials/skills/error-handling-patterns/SKILL.md) | [SKILL.md at be57c0b](https://github.com/wshobson/agents/blob/be57c0b2e3c05c528ca6132b87410b385718775f/plugins/developer-essentials/skills/error-handling-patterns/SKILL.md), [references/details.md at the same revision](https://github.com/wshobson/agents/blob/be57c0b2e3c05c528ca6132b87410b385718775f/plugins/developer-essentials/skills/error-handling-patterns/references/details.md) | Exception/result trade-offs, catch ownership, context, cleanup, and recovery patterns |
| [OWASP Skill Development Best Practices](https://owasp.github.io/www-project-agentic-skills-top-10/skill-development-guide) | [skill-development-guide.md at 0be41c0](https://github.com/OWASP/www-project-agentic-skills-top-10/blob/0be41c0cd68f3375a67c6bef7e6f161fca5db5f3/skill-development-guide.md) | Error Handling & Information Disclosure; error-handling/security-review checklist |

SHA-256 of retrieved UTF-8 source bytes:

| File | SHA-256 |
|---|---|
| wshobson SKILL.md | `5fb7f4d995fc05386a8c04b045f96fd3cb652cbd31fd52d78966f86323b373b8` |
| wshobson details.md | `6f6a48bdee3b8fccf5b73725e798725970826a53c0bb2d4cc2a8e19b1e69466f` |
| OWASP skill-development-guide.md | `74ff418404673551d3352e3e9ef6688350762dbf24c842a88237caa08840a5cb` |

These hashes identify reviewed source bytes; they do not prove publisher identity or package safety. Only selected text was reviewed, not either repository's full supply chain. The source ledger tracks this synthesis; `skills-lock.json` is not given a misleading upstream-installed-skill entry.

## Corrections and exclusions

- The upstream TS `parseJSON<T>` asserts both parsed values and caught errors. The live example uses `unknown`, a narrow syntax-error catch, and runtime shape/range checks.
- The upstream fetch example labels all HTTP errors as network failures. The live guidance separates transport, HTTP, decode, timeout, and cancellation behavior.
- The upstream examples include broad fallbacks and logging before rethrowing. The live policy requires a valid degraded contract and a selected diagnostic owner.
- OWASP's public-message separation is useful; its sample logging of filenames/exceptions still needs project redaction. Do not import its unrelated command denylist, string-prefix path checks, illustrative permission manifests, installer receipts, signing/certification claims, or storage code as working controls. That material is outside this skill's job.

These are local review conclusions, not claims that the sources themselves prescribe every correction. No source code was copied into the examples. General recovery and security recommendations need the target application's contract and tests.

## Primary documentation used to verify details

| Reference | Verified topic |
|---|---|
| [TypeScript useUnknownInCatchVariables](https://www.typescriptlang.org/tsconfig/useUnknownInCatchVariables.html) | Catch values need narrowing |
| [TypeScript narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html) | Type guards and discriminated unions |
| [MDN Error.cause](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause) | Preserve original cause; arbitrary cause types |
| [MDN Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) | HTTP statuses, JSON decoding, cancellation |
| [MDN Promise.all](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all) | Concurrent failure semantics |
| [MDN try/catch/finally](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch) | Conditional catches and finally overriding completion |
| [Node errors](https://nodejs.org/api/errors.html) | Error channels and stable codes |
| [Node process](https://nodejs.org/api/process.html#warning-using-uncaughtexception-correctly) | Uncaught exceptions are not normal recovery |
| [AWS timeouts, retries, and jitter](https://d1.awsstatic.com/builderslibrary/pdfs/timeouts-retries-and-backoff-with-jitter.pdf) | Retry amplification, timeout ambiguity, idempotency, backoff |
| [OWASP error handling](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html) | Public/internal error separation |
| [OWASP logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) | Sensitive data exclusion, event sanitation, log verification |

Runtime documentation is mutable; review date is above. Verify the actual supported runtime and framework before applying examples. This skill claims no universal error schema, production certification, or framework-specific middleware coverage.
