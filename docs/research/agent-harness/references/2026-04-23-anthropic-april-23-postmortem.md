---
title: "An update on recent Claude Code quality reports"
author: "Anthropic"
date: 2026-04-23
source: "https://www.anthropic.com/engineering/april-23-postmortem"
tags: [agent-harness, anthropic, research, claude-code, quality]
---

# An update on recent Claude Code quality reports

**Published:** Apr 23, 2026

## Summary

Anthropic identified and resolved three separate issues affecting Claude Code quality reported over the past month. The API remained unaffected throughout.

## The Three Issues

**1. Reasoning Effort Default Change**
On March 4, the team shifted Claude Code's default reasoning from `high` to `medium` to reduce latency issues. Users preferred intelligence over speed, so this was reverted April 7. The company now defaults to `xhigh` for Opus 4.7 and `high` for other models.

**2. Caching Bug Caused Memory Loss**
A March 26 optimization introduced a bug where Claude's reasoning history was cleared every turn instead of once per session. This made the model appear forgetful and repetitive, affecting Sonnet 4.6 and Opus 4.6. Fixed April 10, the issue persisted because "internal experiments and display changes suppressed visibility."

**3. System Prompt Verbosity Instruction**
A new instruction limiting response length to "keep text between tool calls to ≤25 words" shipped April 16 with Opus 4.7. Broader evaluation testing revealed a 3% intelligence drop, prompting immediate reversion on April 20.

## Response and Prevention

Anthropic reset usage limits for all subscribers and outlined preventive measures: broader internal testing on public builds, enhanced Code Review tools, stricter system prompt controls with comprehensive evaluations, and gradual rollouts for intelligence-affecting changes.
