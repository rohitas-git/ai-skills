import { expect, test } from "bun:test";
import { spawnSync } from "node:child_process";

test("a cycle in PR base branches fails closed instead of hanging stack discovery", () => {
  const module = new URL("./github.ts", import.meta.url).href;
  const code = `import { orderStack } from ${JSON.stringify(module)};
try {
  orderStack({ owner: "fixture", repo: "sample", number: 1 }, [
    { number: 1, headRefName: "a", baseRefName: "b", isCrossRepository: false },
    { number: 2, headRefName: "b", baseRefName: "a", isCrossRepository: false },
  ]);
  process.exit(1);
} catch (error) {
  if (!String(error).includes("cycle")) process.exit(2);
  console.log("cycle rejected");
}`;
  const result = spawnSync(process.execPath, ["--eval", code], { encoding: "utf8", timeout: 1000 });
  expect(result.status).toBe(0);
  expect(result.stdout).toContain("cycle rejected");
});
