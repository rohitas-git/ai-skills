---
name: code-explainer
description: Explain code (lines, blocks, functions, files, modules) at different audience levels (Noob, Learner, Junior, Senior) and depths (Brief, Standard, Deep). User can request any combination. Trigger on "explain this code", "what does this do", "break down this function", "ELI5 this".
---

# Code Explainer Skill

## Overview

This skill delivers clear, audience-adapted explanations of code. It adjusts depth and technical level based on user request, helping everyone from complete beginners to senior engineers understand the intent and mechanics.

## Audience Levels

- **Noob** (Complete Beginner)  
  Explain as if the person has never seen the language. Start with basic language concepts needed. Use simple analogies, everyday examples, and avoid jargon.

- **Learner** (Learning the language)  
  Focus on language fundamentals, first principles, mental models, idioms, and common patterns. Teach *why* the code works this way.

- **Junior** (1–2 years experience)  
  Clarify subtleties, edge cases, common mistakes, performance implications, and how it fits into real-world development practices.

- **Senior** (Experienced)  
  High-level purpose, architectural role, design trade-offs, potential improvements, and system-level implications.

## Explanation Modes (Depth Control)

- **Brief** (~1 min read)  
  Short, high-signal summary. Key points only.

- **Standard** (~3–5 min read)  
  Balanced explanation with good context.

- **Deep** (10+ min read)  
  Comprehensive breakdown: mental models, alternatives, historical context, edge cases, optimizations, and related concepts.

## Instructions

1. **Identify scope** — line/block/function/file/module.
2. **Detect language** and relevant concepts.
3. **Apply requested levels & modes** (default to Standard + Junior if unspecified).
4. **Structure the response clearly**:
   - Start with a short **Overall Purpose**.
   - Then sections for each requested level/mode combination (clearly labeled).
   - Use code snippets, diagrams (text-based), analogies as appropriate.
   - End with **Key Takeaways** and optional **Further Learning** suggestions.

**Best Practices**:
- Be accurate and precise at every level.
- Progress logically from what → how → why.
- Highlight potential gotchas and best practices.
- When explaining multiple levels, show progression of understanding.
- Use markdown for readability (headings, bullet points, code blocks).

You may combine levels (e.g. "Noob + Senior") or modes in a single response.
