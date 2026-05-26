---
url: https://yage.ai/share/thin-harness-fat-skills-en-20260414.html
title: "Garry Tan's Thin Harness, Fat Skills: Five Concepts Unpacked"
author: Garry Tan (Yage AI)
date: 2026-04-14
status: SUCCESS
---

# Garry Tan's Thin Harness, Fat Skills: Five Concepts Unpacked

## Core Principle

Garry argues the harness (the program running the model) should remain minimal, handling only four essential functions: "run the model in a loop, read and write files, manage context, and enforce safety."

## The Problem with Fat Harnesses

He opposes bloated architectures with excessive tool definitions. These consume significant context window space and introduce performance bottlenecks. His quantified example illustrates the issue: a Playwright CLI executes browser operations in 100ms, while a Chrome MCP requires 15 seconds for the same screenshot-find-click-wait-read sequence—a 75x performance gap.

## The Solution: Directional Architecture

The design principle pushes intelligence upward into reusable skill files and execution capability downward into deterministic tools. The middle layer stays as thin as possible.

## Key Insight

"Every skill you write is a permanent upgrade to your system." Skills remain stable and benefit automatically when models improve, while deterministic steps maintain reliability. This architecture separates the cognitive judgment layer (model-driven) from the execution layer (tool-driven), enabling scalability without context bloat.
