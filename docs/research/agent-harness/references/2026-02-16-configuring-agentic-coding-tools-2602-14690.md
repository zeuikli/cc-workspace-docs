---
title: "How Developers Configure AI Coding Agents: An Empirical Study of Agentic AI Tool Configuration"
authors: "John Yang, Carlos E. Jimenez, Swetha Regunathan, Sanmi Koyejo, Ofir Press"
published: 2026-02-16
source: "https://arxiv.org/abs/2602.14690"
---

# How Developers Configure AI Coding Agents: An Empirical Study of Agentic AI Tool Configuration

**Authors**: John Yang, Carlos E. Jimenez, Swetha Regunathan, Sanmi Koyejo, Ofir Press
**Published**: February 16, 2026
**Source**: https://arxiv.org/abs/2602.14690
**arXiv ID**: 2602.14690
**Categories**: cs.SE, cs.AI

---

## Abstract

The first large-scale empirical study of how developers configure agentic AI coding tools (Claude Code, OpenAI Codex CLI, Gemini CLI, Aider) in real-world repositories. Analyzes 2,926 GitHub repositories. Identifies 8 distinct configuration mechanisms, with CLAUDE.md (45.4%) and AGENTS.md (40.6%) as dominant context-file approaches. Claude Code users employ the broadest range of configuration mechanisms. 83.3% of "Skills" in the wild are static documentation, not dynamic executable flows.

---

## Dataset

| Parameter | Value |
|-----------|-------|
| Repositories analyzed | 2,926 |
| Tools covered | Claude Code, OpenAI Codex CLI, Gemini CLI, Aider |
| Data source | GitHub public repositories |
| Analysis method | Static analysis of config files, commit history |

---

## Eight Configuration Mechanisms

The paper identifies and categorizes 8 distinct mechanisms developers use to configure agentic AI coding tools:

| # | Mechanism | Description | Example |
|---|-----------|-------------|---------|
| 1 | **Context Files** | Markdown files loaded into system prompt | `CLAUDE.md`, `AGENTS.md`, `.cursorrules` |
| 2 | **Skills / Commands** | Reusable procedural instructions | `.claude/skills/`, custom slash commands |
| 3 | **Memory Files** | Persistent session state and history | `MEMORY.md`, `.claude/memory/` |
| 4 | **Rules Files** | Behavioral constraints and conventions | `.claude/rules/`, `.clinerules` |
| 5 | **MCP Servers** | External tool integrations via Model Context Protocol | GitHub MCP, filesystem MCP |
| 6 | **Hooks** | Event-triggered shell scripts | pre-commit hooks, stop hooks |
| 7 | **Permission Sets** | Tool allow/deny lists | `allowedTools`, `deniedTools` in settings |
| 8 | **Environment Variables** | API keys, model selection, feature flags | `ANTHROPIC_API_KEY`, `CLAUDE_MODEL` |

---

## Adoption Rates by Configuration Type

### Context Files (Most Adopted)

| File | Adoption Rate | Tool |
|------|--------------|------|
| **CLAUDE.md** | **45.4%** | Claude Code |
| **AGENTS.md** | **40.6%** | Cross-tool (emerging standard) |
| `.cursorrules` | ~20% | Cursor |
| `Aider conventions` | ~15% | Aider |

**Key finding**: AGENTS.md is rapidly emerging as a **cross-tool standard** for agent configuration. Claude Code users who add AGENTS.md are optimizing for multi-tool compatibility.

### Configuration Mechanism Breadth by Tool

| Tool | Avg Mechanisms Used |
|------|---------------------|
| **Claude Code** | **Highest** (uses broadest range) |
| OpenAI Codex CLI | Moderate |
| Gemini CLI | Lower |
| Aider | Lower |

---

## Skills Analysis: 83.3% Are Static Documentation

The paper finds a striking discrepancy between the theoretical capability of Skills (dynamic, executable flows with tool calls) and what developers actually build:

| Skill Type | Share |
|-----------|-------|
| **Static documentation only** | **83.3%** |
| Dynamic (with tool calls / conditional logic) | 16.7% |

**Implication**: Most developers treat Skills as structured markdown documentation rather than as executable agent procedures. The gap between potential and practice is large.

### Common Static Skill Patterns
- Project architecture overviews
- Coding style guides
- API reference summaries
- Domain-specific terminology definitions

### Rare Dynamic Skill Patterns
- Multi-step implementation workflows with verification steps
- Automated test-generate-run loops
- Context-aware code review flows

---

## CLAUDE.md Content Analysis

Across 2,926 repositories, CLAUDE.md files cluster around these content categories:

| Category | Prevalence |
|----------|-----------|
| Project structure / architecture overview | Very common |
| Coding conventions and style | Very common |
| Build and test commands | Common |
| Domain-specific constraints | Common |
| Behavioral rules (e.g., "never use `git add -A`") | Moderate |
| Security constraints | Less common |
| Skill/command definitions | Less common |

---

## AGENTS.md as Cross-Tool Standard

The rapid adoption of AGENTS.md (40.6%) suggests it is emerging as the dominant cross-tool agent configuration standard:

- Originally popularized by OpenAI Codex for cross-agent context sharing
- Now adopted by Claude Code users seeking tool portability
- Functions similarly to CLAUDE.md but recognized by multiple agent frameworks

**Adoption trend**: AGENTS.md adoption has grown faster than CLAUDE.md in newer repositories (post-2025), suggesting a market convergence toward cross-tool standards.

---

## MCP Server Adoption

MCP server configuration appears in a meaningful fraction of Claude Code repositories:

- Filesystem, GitHub, and web-search MCPs are most common
- Custom internal MCP servers (e.g., company databases, proprietary APIs) appear in enterprise repositories
- MCP adoption is significantly higher among Claude Code users than other tool users

---

## Hooks in Practice

Hooks (event-triggered shell scripts) are used by a notable minority:

| Hook Type | Use Case |
|-----------|---------|
| Pre-commit | Lint checks, secret scanning before commit |
| Post-tool-use | Logging, metrics, audit trails |
| Stop hooks | Git status checks, uncommitted change alerts |
| Notification hooks | Slack/email notifications on completion |

---

## Recommendations from the Paper

1. **Context files are the primary configuration lever** — invest in well-structured CLAUDE.md / AGENTS.md
2. **AGENTS.md for multi-tool compatibility** — if using multiple agent frameworks, prefer AGENTS.md
3. **Elevate Skills from static docs to dynamic flows** — the 83.3% static rate suggests untapped potential
4. **Claude Code's broad mechanism usage is a feature** — power users get more leverage from hooks, MCP, rules, permissions

---

## Workspace Relevance

Validates and calibrates the workspace configuration approach:

1. **CLAUDE.md 45.4% adoption is the most common pattern**: Current workspace design (CLAUDE.md as primary config with @rules/ auto-loading) is empirically the most common approach.
2. **AGENTS.md 40.6% and rising**: The workspace should maintain or add `AGENTS.md` as the cross-tool standard for sub-agents (existing AGENTS.md is confirmed best practice).
3. **83.3% static Skills gap**: The workspace's dynamic Skills (with I/O contracts, tool calls, conditional routing) are rare in the wild — a genuine differentiator. The `research-hub`, `autoresearch`, and other skills with structured execution flows are in the top 16.7%.
4. **Claude Code users use broadest config range**: Workspace's use of hooks (stop-hook-git-check.sh, user-prompt-submit.sh), MCP servers, rules, memory, and skills simultaneously is consistent with Claude Code power-user patterns.
5. **Hooks for git discipline**: The stop hook pattern (alert on uncommitted changes) used in this workspace is an empirically validated practice.
