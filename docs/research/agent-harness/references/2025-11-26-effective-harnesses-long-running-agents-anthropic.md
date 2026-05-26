---
title: "Effective harnesses for long-running agents"
source: "https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents"
author: "Justin Young"
date: "2025-11-26"
tags: [agent-harness, anthropic, research, long-running-agents]
---

# Effective harnesses for long-running agents

**Published:** Nov 26, 2025  
**Author:** Justin Young

---

## Overview

Anthropic researchers developed solutions enabling AI agents to maintain consistent progress across multiple context windows when working on extended tasks. The core challenge: agents work in discrete sessions without memory of prior work, making multi-day projects difficult.

## The Core Problem

Long-running agents face two critical failure modes. First, they attempt excessive work simultaneously, exhausting context mid-implementation and leaving undocumented half-finished features. Second, agents may prematurely declare projects complete after observing partial progress.

## Two-Part Solution

**Initializer Agent:** Runs once to establish the foundational environment, including:
- A comprehensive feature list (200+ items marked as "failing")
- An `init.sh` script for launching development servers
- A `claude-progress.txt` file tracking work history
- An initial git repository

**Coding Agent:** Executes subsequent sessions to:
- Review progress files and git history
- Work on single features incrementally
- Leave code in production-ready condition
- Commit changes with descriptive messages

## Key Environmental Components

The feature list uses JSON format with detailed requirements. As researchers note, "the model is less likely to inappropriately change or overwrite JSON files compared to Markdown files."

Testing proved essential. Claude performed better when given explicit browser automation tools (Puppeteer) to verify features end-to-end as human users would, rather than relying solely on unit tests.

## Session Structure

Each session begins with standardized steps: checking directory location, reading progress files, reviewing git logs, examining the feature list, and running basic verification tests before implementing new features.

## Future Directions

Researchers question whether multi-agent architectures with specialized agents (testing, QA, cleanup) might outperform single general-purpose agents. Additionally, these findings currently apply to web development but may generalize to scientific research or financial modeling.
