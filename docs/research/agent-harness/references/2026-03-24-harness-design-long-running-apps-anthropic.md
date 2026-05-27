---
title: "Harness Design for Long-Running Application Development"
author: "Prithvi Rajasekaran"
date: 2026-03-24
source: "https://www.anthropic.com/engineering/harness-design-long-running-apps"
tags: [agent-harness, anthropic, research, harness-design, multi-agent]
---

# Harness Design for Long-Running Application Development

**Published:** Mar 24, 2026  
**Author:** Prithvi Rajasekaran, Anthropic Labs

## Overview

This article explores how Anthropic improved Claude's ability to build complete applications without human intervention through innovative harness design patterns. The work addresses two key challenges: generating high-quality frontend designs and maintaining coherence during extended coding tasks.

## Core Innovation: Generator-Evaluator Architecture

Inspired by Generative Adversarial Networks (GANs), the author developed a multi-agent system pairing a generator with an evaluator. This separation addresses a fundamental problem: "agents tend to respond by confidently praising the work—even when, to a human observer, the quality is obviously mediocre."

### Frontend Design Application

Four grading criteria guide design quality:
- **Design quality:** Coherent visual identity and mood
- **Originality:** Evidence of custom decisions versus templates
- **Craft:** Typography, spacing, and color fundamentals
- **Functionality:** Usability and task completion

The evaluator used Playwright to interact with live pages before scoring, enabling iterative refinement across 5-15 cycles per generation.

### Full-Stack Development Harness

The final three-agent architecture includes:

1. **Planner:** Expands brief prompts into detailed product specifications with ambitious scope
2. **Generator:** Implements features using React, Vite, FastAPI, and SQLite/PostgreSQL
3. **Evaluator:** Tests functionality through user interactions via Playwright

Key improvements over single-agent approaches:
- Sprint contracts negotiated between generator and evaluator before implementation
- Structured file-based communication maintaining context
- Reduced "context anxiety" behavior in newer models

## Key Findings

**Performance Gap:** A retro game maker built with the full harness (6 hours, $200) produced dramatically superior results compared to solo generation (20 minutes, $9). The single-agent output had broken gameplay mechanics, while the harness version delivered functional, polished applications.

**Model Evolution:** Opus 4.6 eliminated the need for sprint-based decomposition, allowing longer uninterrupted generation sessions. The author demonstrates that "as models improve, the scaffold surrounding the model matters less over time."

**QA Effectiveness:** The evaluator caught subtle issues like route ordering bugs and incomplete feature implementations that solo generation missed, though comprehensive testing remained challenging.

## Cost-Performance Tradeoff

The simplified V2 harness (3 hours 50 minutes, $124.70) generated a functional Digital Audio Workstation with working timeline, mixer, and AI-assisted composition features—demonstrating that improved model capabilities enable harness optimization without sacrificing quality.

## Design Principles

The author emphasizes: "find the simplest solution possible, and only increase complexity when needed." As capabilities improve, practitioners should periodically audit which harness components remain load-bearing, removing unnecessary overhead while adding new capabilities at the frontier of what models can achieve.
