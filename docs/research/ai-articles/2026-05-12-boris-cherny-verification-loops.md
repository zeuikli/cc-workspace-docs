---
url: "https://x.com/bcherny/status/2007179861115511237"
title: "Boris Cherny on verification loops"
domain: x.com
fetched: 2026-05-12
source_tier: C
---

# Boris Cherny on Verification Loops

**Original Tweet Thread by Boris Cherny (@bcherny)**
**Date**: Tweet part of larger thread on Claude Code best practices
**Author**: Boris Cherny, creator of Claude Code at Anthropic

---

## Core Message: Verification Loops = 2-3x Quality Improvement

> "A final tip: probably the most important thing to get great results out of Claude Code -- give Claude a way to verify its work. If Claude has that feedback loop, it will 2-3x the quality of the final result. Claude tests every single change I land."

### Key Insight

Verification loops are **the single most impactful optimization** for Claude Code output quality.

**Impact**: Proper verification increases output quality by **2-3x**

### What Verification Looks Like

Verification is domain-specific and can take multiple forms:
- **Running tests**: Automated test suites validate code changes
- **Bash commands**: Simple shell commands that verify output correctness
- **UI testing**: Testing the application in a browser or phone simulator
- **Screenshots comparison**: Visually comparing before/after outputs
- **Custom validation**: Any mechanism that provides feedback on whether the result is correct

### Practical Application

According to Boris Cherny's workflow:
- Every single change he lands goes through verification
- For very long-running tasks, he uses background agents or Stop hooks to verify completion
- The ralph-wiggum plugin is used for additional verification in some workflows

### Why This Matters

Without clear success criteria and verification, Claude might produce something that **looks right but actually doesn't work**. When Claude has a feedback loop, it becomes self-correcting rather than requiring manual human review for every output.

This transforms Claude from "needs review after every change" to "self-verifying and trustworthy output."

### Related Best Practices from Boris Cherny

- Use `/loop` and `/schedule` for automated verification on intervals
- Configure Stop hooks to verify work deterministically
- Integrate background agents for verification of long-running tasks
- Combine verification with proper prompting and context management

---

## Context: Boris Cherny's Role

Boris Cherny is the creator of Claude Code at Anthropic. As of 2026, he:
- Hasn't hand-written a single line of code (fully agentic)
- Merges 50-150 PRs daily from his phone using hundreds of agents and loops
- Shares internal Anthropic workflows publicly to help developers use Claude Code effectively

This guidance comes from his direct experience building and shipping code entirely through Claude Code with autonomous agents.

