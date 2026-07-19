---
name: context-monitor
description: Monitors conversation context usage, warns at ~50% of the limit, and provides actionable advice on saving tokens and optimizing conversations. Helps users avoid waste and maintain performance. Trigger on long chats, heavy tool use, or mentions of context/tokens.
disable-model-invocation: true
---

# Context Monitor

## Overview

This skill tracks conversation context consumption and intervenes helpfully when usage grows high. It not only warns about limits but also teaches **token optimization techniques** so users can continue efficiently or start fresh with better habits.

## Token Usage Guidelines (Approximate)
- **Low** (<30%): Normal operation — no action needed.
- **Medium** (~50%): Gentle warning + optimization tips.
- **High** (>70%): Strong recommendation to summarize or new session.

## Instructions

1. **Estimate usage** based on:
   - Total messages exchanged
   - Number and size of tool calls/results (searches, code execution, file reads)
   - Loaded skills and long outputs (code blocks, images, tables)
   - Conversation complexity and history length

2. **Trigger notifications** proactively (max 1–2 times per session):
   - At ~50%: Friendly heads-up.
   - Include **specific token-saving methods** tailored to the current conversation.

3. **Core Optimization Advice** (rotate and customize these):
   - **Start a new chat** — best for long/complex topics.
   - **Ask for summaries** before continuing.
   - **Be more concise** in prompts (use effort calibrator).
   - **Avoid repeating information** — reference previous points briefly.
   - **Limit tool calls** — batch requests when possible.
   - **Upload key files** once and refer to them instead of repasting content.
   - **Use structured formats** (bullets, tables) only when helpful.
   - **Close off sub-topics** cleanly.

4. **Response Template** (example at 50% threshold):
   ```
   ⚠️ Context usage is getting high (~50% of window). 

   Quick tips to optimize tokens:
   - Start a fresh chat (best for performance)
   - Ask me for a summary of key points so far
   - Use briefer prompts or the response-effort-calibrator skill
   - Avoid repasting long code/files — refer to them instead

   Would you like a concise summary of our conversation to continue in a new session?
   ```

5. **Advanced Tips** (for high usage):
   - Extract important artifacts (code, decisions) into files.
   - Focus prompts on next actions only.
   - Combine with `response-effort-calibrator` for shorter replies.

## Best Practices for Users
- Shorter, focused prompts = better results + lower cost.
- New sessions reset context fully → often faster and cheaper.
- This skill works great alongside `response-effort-calibrator` and `git-commit-helper`.

Stay proactive — better token hygiene leads to consistently high-quality responses!