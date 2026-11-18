declare const durationBrand: unique symbol;
type Duration = number & { readonly [durationBrand]: "Duration" };

export function parseDuration(value: unknown): Duration {
  if (typeof value !== "number" || !Number.isFinite(value) || value < 0)
    throw new RangeError("duration must be finite and nonnegative");
  // The runtime predicate above establishes the invariant this local brand records.
  return value as Duration;
}

export function endAt(start: number, duration: Duration): number {
  return start + duration;
}

export type Load<T> =
  | { readonly kind: "pending" }
  | { readonly kind: "ready"; readonly value: T }
  | { readonly kind: "failed"; readonly error: string };

export function describe(result: Load<string>): string {
  switch (result.kind) {
    case "pending": return "waiting";
    case "ready": return result.value;
    case "failed": return result.error;
    default: {
      const unreachable: never = result;
      return unreachable;
    }
  }
}

export function first<T>(items: readonly [T, ...T[]]): T {
  return items[0];
}
