# TypeScript and JavaScript patterns

Use the repository's runtime target and existing libraries. Examples are original, narrow illustrations; they do not replace a schema validator or the application's transport and logging policy.

## Narrow failures and preserve causes

Treat caught values as `unknown`; third-party code can throw strings, objects, or `null`. Narrow before accessing properties, and do not cast to `Error` to silence the compiler. Prefer the project's `useUnknownInCatchVariables` setting. JavaScript uses the same runtime checks without type annotations. See [TypeScript catch variables](https://www.typescriptlang.org/tsconfig/useUnknownInCatchVariables.html).

Throw `Error` instances for new exceptional failures. Rethrow the same value when adding no information; use `new Error("Reading configuration failed", { cause: error })` when adding meaningful context. Causes can themselves be non-Errors. Check runtime and TypeScript library support for `ErrorOptions`; do not require V8-only `Error.captureStackTrace` in browser-neutral code. Keep these diagnostics internal. See [Error.cause](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause).

Use documented error codes, known local classes, or validated discriminants for decisions, not message substring matching. Error instances and prototypes do not survive JSON transport; decode a validated wire contract at that boundary. Node-specific channels and codes are documented in [Node errors](https://nodejs.org/api/errors.html).

## Expected failures as a discriminated union

When the project uses tagged outcomes, retain runtime validation. `JSON.parse(...) as T` proves neither shape nor validity. This complete example requires strict TypeScript and an ES2022-compatible library target:

```typescript
export type ReadLimitResult =
  | { ok: true; value: { limit: number } }
  | { ok: false; code: "INVALID_JSON" | "INVALID_LIMIT" };

export function readLimit(text: string): ReadLimitResult {
  let input: unknown;
  try {
    input = JSON.parse(text);
  } catch (error: unknown) {
    if (error instanceof SyntaxError) {
      return { ok: false, code: "INVALID_JSON" };
    }
    throw error;
  }

  if (typeof input !== "object" || input === null || Array.isArray(input)) {
    return { ok: false, code: "INVALID_LIMIT" };
  }
  if (!("limit" in input) || typeof input.limit !== "number") {
    return { ok: false, code: "INVALID_LIMIT" };
  }
  if (!Number.isInteger(input.limit) || input.limit < 1 || input.limit > 100) {
    return { ok: false, code: "INVALID_LIMIT" };
  }
  return { ok: true, value: { limit: input.limit } };
}
```

The 1–100 range is this example's contract, not a general input rule. Unknown fields are intentionally ignored and excluded from the returned value. Use the installed schema validator for richer contracts. Consumers must branch on `ok`; use exhaustiveness checks when handling a growing error union. See [TypeScript narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html).

## Async work and fetch

Every promise needs an owner: return it, await it, or attach a rejection handler that cannot itself leave an unobserved rejection. `void task()` alone does not handle failure. A surrounding synchronous `try` does not catch a later callback throw. In an async `try`, use `return await task()` when its rejection must reach that local catch/finally before cleanup.

Fetch fulfills for HTTP error statuses. Check `response.ok` or explicit contract statuses before decoding success data; JSON decoding can fail separately and parsed data still needs validation. Pass the caller's abort signal and a supported deadline strategy through request and body consumption. Replacing a caller signal with a timeout-only signal loses cancellation. `Promise.race` with a timer does not stop the underlying request. See [Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch).

Classify HTTP failure, network rejection, invalid payload, timeout, and caller cancellation separately. Do not label every non-2xx status a network error or retry any `TypeError` indiscriminately. Abort reasons may be arbitrary values; use the operation's signal state and the adapter's documented contract, avoiding a universal `error.name` test. Cancellation and a completed write may race, so do not assume abort rolled back remote effects.

## Concurrency and Node boundaries

`Promise.all` rejects when an input rejects; already-started siblings continue. It is not a transaction or a cancellation mechanism. If subsequent cleanup requires siblings to stop, request cancellation where supported and observe their settlement. Use `Promise.allSettled` when independent results need individual accounting; inspect every result and expose partial completion deliberately. Bound fan-out for large inputs. See [Promise.all](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all).

Node APIs may throw synchronously, reject promises, pass errors to callbacks, or emit an `error` event. Use the documented channel; an outer catch does not cover all four. Handle stream/event failures through existing lifecycle APIs. Process-level uncaught handlers are last-resort diagnostics/shutdown hooks, not a way to resume normal service in an unknown state. Follow the host's supported restart/shutdown contract. See [Node errors](https://nodejs.org/api/errors.html) and [uncaught-exception guidance](https://nodejs.org/api/process.html#warning-using-uncaughtexception-correctly).

## Cleanup must not replace the primary failure

Avoid returning from `finally`: it can override a return or exception. Await asynchronous cleanup before relinquishing ownership. When both stages may fail, this dependency-free example retains both values in a documented order; it does not log them or make them public:

```typescript
export async function runAndClose<T>(
  run: () => Promise<T>,
  close: () => Promise<void>,
): Promise<T> {
  let failed = false;
  let primaryError: unknown;
  try {
    return await run();
  } catch (error: unknown) {
    failed = true;
    primaryError = error;
    throw error;
  } finally {
    try {
      await close();
    } catch (cleanupError: unknown) {
      if (failed) {
        throw new AggregateError(
          [primaryError, cleanupError],
          "Operation and cleanup failed",
        );
      }
      throw cleanupError;
    }
  }
}
```

The boolean matters because a promise may reject with `undefined`. Use an existing transaction/resource manager instead when available; do not introduce this generic wrapper merely to match the example. If using explicit resource management, verify compiler/runtime support and the project's suppressed-error convention. See [try/catch/finally semantics](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch).

## Focused checks for these examples

- `readLimit`: valid lower/upper bounds; malformed JSON; `null`, arrays, missing field, numeric string, fractions, out-of-range numbers; output contains only the approved field.
- `runAndClose`: success; operation-only failure; cleanup-only failure; both fail; rejection with `undefined`; cleanup runs exactly once and finishes before settlement.
- For an actual fetch adapter: fulfilled 4xx/5xx responses, bad JSON, wrong shape, caller abort, timeout, and retry budget exhaustion. Test with the project's HTTP stub and timer facilities; parsing/cleanup checks alone do not verify networking behavior.
