---
url: "https://www.testventures.net/blog/fat-skills-thin-harness"
title: "Fat Skills, Thin Harness: The Framework I'm Using to Ship a Tech Grant in Ten Working Days"
author: Geordie (TestVentures/Powered by Finn)
date: 2026-04-14
status: SUCCESS
---

# Fat Skills, Thin Harness: The Framework I'm Using to Ship a Tech Grant in Ten Working Days

A week ago, Y Combinator CEO Garry Tan published "Thin Harness, Fat Skills," advocating a three-layer architectural approach: encode human judgment into markdown procedures, push deterministic work into proven code, and maintain a minimal software layer between them.

## Understanding Tan's Framework

The bottleneck in AI work isn't model intelligence—it's whether the model understands your specific schema, data conventions, and domain expertise.

### The Three-Layer Stack

1. **Fat skills (top):** Markdown playbooks encoding procedures and judgment specific to your operations. These capture "how we do things here" and represent 90% of the value.

2. **Thin harness (middle):** Minimal plumbing that runs the model and handles file I/O. Most teams overbuild this layer unnecessarily.

3. **Fat code (bottom):** Battle-tested, existing software for deterministic work requiring exactness—payments, authentication, database operations.

## Why This Matters for Non-Developers

"Your work with AI isn't what you say in one conversation. It's the set of skills—the markdown playbooks—that you accumulate" over time. These become your durable assets, regardless of which model you use.

For small operators, the leverage formula is:
- Your judgment written as procedures
- One functional harness
- Delegated work to existing, proven software

## The Charity Infrastructure Project Example

The author mapped a charity donation platform onto this framework:

### Fat Skills Identified (Nine Judgment Calls)

- Onboarding charities
- Generating jurisdiction-specific briefs
- Interpreting donor intent
- Vetting organizations
- Recording demos
- CEO-style document review
- Writing impact stories
- Charity database searches
- Preparing for funder convenings

### Fat Code Layer

Rather than building backend infrastructure, the author sourced existing solutions for payments, verification, and record-keeping.

### Thin Harness

A small server, single payment endpoint, simple database, donation page, basic dashboard—nothing more.

This approach allowed shipping a working prototype with real transactions in 48 hours.

## Eight-Point Self-Learning Practice

1. **Write skills during work, not after**—capture details only visible in real contexts
2. **Edit procedures, not outputs**—fix the rule to compound improvements
3. **Test new skills three times** before considering them reliable
4. **Maintain a skills changelog** with dated edits and rationale
5. **Study external skill packs weekly** for patterns to adapt
6. **Run monthly skill reviews** pruning unused and overlapping procedures
7. **Search for existing solutions before building** deterministic systems
8. **Keep skills model-agnostic**—write for generalist readers, not specific LLM quirks

## Core Insight

"The loop is a commodity. The skills are the compounding asset. The fat code is leverage you didn't have to build." Model churn happens every few weeks; skills remain constant. The judgment you document becomes your actual competitive advantage.
