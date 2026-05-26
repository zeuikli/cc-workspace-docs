---
url: "https://www.deeplearning.ai/the-batch/claude-codes-source-code-leaked-exposing-potential-future-features-kairos-and-autodream/"
title: "Claude Code's Source Code Leaked - Exposing Potential Future Features: KAIROS and autoDream"
author: DeepLearning.AI
date: 2026-03-31
status: SUCCESS
---

# Claude Code's Source Code Leaked - KAIROS and autoDream

## The Incident

Claude Code's source code was exposed when Anthropic accidentally published a source map file with version 2.1.88 in March 2026. An intern discovered this translation key and decoded over 512,000 lines of code across 1,900 files before the package was removed.

## How Claude Code Functions

The system operates "built less like a chatbot wrapper and more like a small, dedicated operating system." Notable architectural features include:

- **Modular tools**: Over 40 specialized tools with individual permission gates
- **Sub-agent swarms**: Multiple agents with delegated permissions and shared memory
- **Three-tier memory system**: Uses indexed pointers, markdown files, and JSON transcripts to prevent context bloat
- **Compression strategy**: Employs three stages to manage conversation length within context limits

## Unreleased Features

The leaked code revealed several in-development capabilities:

### Kairos
An always-on background agent enabling continuous operation without user interaction.

### autoDream
A logic system that "merges duplicate memories, eliminates contradictions, resolves speculations, and otherwise prunes memory."

### Additional In-Development Features

- Voice interface
- Cloud task processing (Ultraplan)
- An engagement feature called Buddy
- An "undercover mode" allowing repository commits without detection signatures

## Implications

The leak demonstrates how advanced agentic systems manage complexity while raising community concerns about unintended consequences when AI agents operate autonomously.
