---
url: "https://layer5.io/blog/engineering/the-claude-code-source-leak-512000-lines-a-missing-npmignore-and-the-fastest-growing-repo-in-github-history/"
title: "The Claude Code Source Leak: 512,000 Lines, A Missing .npmignore, and the Fastest Growing Repo in GitHub History"
author: "Layer5"
date: 2026-03-31
status: SUCCESS
---

# The Claude Code Source Leak: 512,000 Lines, A Missing .npmignore, and the Fastest Growing Repo in GitHub History

## Technical Details from the Claude Code Leak

The exposure revealed several key components:

### Architecture & Framework

The codebase used "a modular system prompt with cache-aware boundaries, approximately 40 tools in a plugin architecture" and a 46,000-line query engine with React and Ink terminal rendering.

### Unreleased Features

The source contained 44 feature flags gating over 20 unshipped capabilities, including:

#### KAIROS
An autonomous daemon mode allowing Claude to operate as a persistent background agent with proactive decision-making via periodic prompts.

#### autoDream
A background memory consolidation process running as a forked subagent during idle time.

#### ULTRAPLAN
Offloads complex planning to remote cloud sessions with extended thinking time.

#### BUDDY
A Tamagotchi-style terminal companion with 18 species and rarity tiers.

### Security & Anti-Competitive Measures

The leak exposed "inject[ion of] fake tool definitions into API requests, designed to poison the training data of competitors" and an "undercover mode" that strips attribution in external repository contributions.

### Internal Metrics

Benchmarks revealed Capybara v8 had a 29-30% false claims rate, representing a regression from earlier versions, plus evidence of 250,000 wasted API calls daily from autocompact failures.
