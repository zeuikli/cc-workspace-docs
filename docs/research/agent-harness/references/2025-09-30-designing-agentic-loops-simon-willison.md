---
title: "Designing Agentic Loops"
author: "Simon Willison"
date: 2025-09-30
source: "https://simonwillison.net/2025/Sep/30/designing-agentic-loops/"
tags: [agent-harness, research]
---

# Designing Agentic Loops

An agent is defined as something that "runs tools in a loop to achieve a goal."

## YOLO Mode and Safety

The tension between agent effectiveness and safety is critical. While approval-required modes are tedious, unrestricted operation risks data loss, system compromise, and exfiltration attacks.

**Recommendation**: Run agents in isolated environments like GitHub Codespaces or Docker containers with restricted network access rather than on personal machines.

## Tool Selection

Rather than relying on Model Context Protocol (MCP), focus on shell commands and creating documentation files listing available tools. LLMs already understand many existing utilities like Playwright and FFmpeg.

## Credential Management

When authentication is necessary:
- Provide access only to test environments
- Implement strict budget limits on spending-capable credentials
- Example: Create a dedicated Fly.io organization for a specific investigation

## Ideal Use Cases

Agentic loops work best for problems with clear success criteria requiring trial-and-error iteration:
- Debugging
- Performance optimization
- Dependency upgrades
- Container optimization

Strong automated test suites amplify agent effectiveness.

## Emerging Skillset

This represents an emerging skillset, with Claude Code's February 2025 release marking early adoption of agentic loop design patterns.
