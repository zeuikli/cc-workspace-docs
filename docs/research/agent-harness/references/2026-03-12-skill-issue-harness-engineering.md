---
title: "Skill Issue: Harness Engineering for Coding Agents"
authors: Kyle (HumanLayer)
published: 2026-03-12
source: "https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents"
---

# Skill Issue: Harness Engineering for Coding Agents

**Author**: Kyle (HumanLayer)  
**Published**: 2026-03-12  
**Read time**: ~23 min  
**Source**: https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents  
**Tags**: #agents #claudecode #best-practices

---

## Introduction

The article opens by documenting widespread failures in coding agents over the past year: ignoring instructions, executing dangerous commands unprompted, and failing on simple tasks. Rather than waiting for better models ("GPT-6 will fix it"), the author argues the real issue is **configuration**, not model capability.

The key insight: "it's not a model problem. It's a configuration problem." Even as models improve, they'll continue failing in unexpected ways because non-deterministic systems inherently produce unpredictable failure modes.

---

## Core Definition: The Coding Agent Harness

The foundational equation presented:

> coding agent = AI model(s) + harness

The "harness" encompasses configuration points like skills, MCP servers, sub-agents, memory systems, and instruction files (CLAUDE.md/AGENTS.md). These represent the agent's runtime and environmental interfaces.

---

## Harness Engineering Explained

**Harness engineering** (coined by Viv Trivedy) means systematically improving agent performance by engineering solutions whenever agents make mistakes. Mitchell Hashimoto's definition captures this: whenever an agent fails, spend time ensuring it never fails that way again.

The article positions harness engineering as a subset of **context engineering** (a Dex Horthy concept from "12-factor agents"), which itself encompasses prompt engineering and systematic reliability improvements.

Harness engineering specifically addresses:
- Granting new capabilities
- Teaching codebase knowledge beyond training data
- Adding determinism beyond system prompt instructions
- Adapting behavior for specific codebases
- Improving success rates beyond "magic prompts"
- Managing context window inflation

---

## Implementation: Key Configuration Points

### CLAUDE.md & AGENTS.md Files

These markdown files at repository root inject deterministically into the agent's system prompt. Key principles from prior HumanLayer guidance:

- Avoid auto-generation; craft carefully
- "Less is more" regarding instructions
- Use progressive disclosure
- Keep content concise and universally applicable
- HumanLayer's own CLAUDE.md runs under 60 lines

**The ETH Zurich Study Context**: A 2025 study tested 138 agentfiles and found:
- LLM-generated files hurt performance while costing 20%+ more tokens
- Human-written ones helped approximately 4%
- Agents spent 14-22% more reasoning tokens processing context instructions without improving resolution rates

However, the article argues careful reading shows the study validates their recommendations: avoid auto-generation, minimize instruction bloat, use progressive disclosure, keep universally applicable content.

### MCP Servers for Tools

MCP servers extend agent capabilities beyond file I/O and bash commands. While the specification includes resources, prompts, and elicitations, these features lack robust harness support. MCP servers can run locally or via HTTP, connecting agents to services like Linear and Sentry.

**Critical Warning**: Tool descriptions from MCP servers inject into system prompts, creating prompt injection vectors. Never connect untrusted servers.

**Problem: Too Many Tools**
- Context window fills with tool descriptions
- Agents enter "the dumb zone" faster
- Each irrelevant tool description consumes instruction budget

Solution: Anthropic released experimental MCP tool search to progressively disclose tools when excessive numbers are connected.

**Alternative Strategy**: If an MCP server duplicates CLI functionality already in training data (GitHub, Docker, databases), prompt agents to use the CLI instead for better composability and context efficiency.

**HumanLayer Example**: They replaced the Linear MCP server with a custom CLI wrapper providing context-efficient responses, adding six example usages in CLAUDE.md. This saved thousands of tokens from MCP tool definitions.

### Skills for Reusable Knowledge

Skills provide **progressive disclosure**—agents access specific instructions, knowledge, or tools only when needed. When activated, SKILL.md files load as user messages, and agents learn the skill directory location.

Skills can bundle multiple markdown files with creative progressive disclosure: main SKILL.md can reference additional files agents should read conditionally.

**Limitation**: Cannot directly bundle MCP servers or custom agent tools. Instead, distribute as executables, CLIs, NPM packages, or instruct agents to install via the SKILL.md file.

**Warning**: Skill registries have distributed malicious skills. Treat like untrusted npm packages—review before installation.

### Sub-Agents for Context Control

Sub-agents enable **context encapsulation**: dispatching agents see only the sub-agent prompt and final result, not intermediate tool calls, tool results, or messages. This maintains coherency across longer sessions.

**Key Benefit**: Sub-agents function as "context firewalls" preventing intermediate noise accumulation in parent threads.

**Context Rot Research**: Chroma's research confirms models perform worse at longer context lengths. Performance degradation steepens when low semantic similarity exists between questions and contextual information—distractors compound at longer context windows.

**Cost Control**: Use expensive models (Opus) for parent sessions handling planning/orchestration, cheaper models (Sonnet/Haiku) for discrete sub-agent tasks.

**Use Cases**:
- Locating specific definitions/implementations
- Analyzing codebase patterns
- Tracing information flow across service boundaries
- Code/documentation/web research tasks

Sub-agents should return highly condensed responses with source citations (filepath:line format) for progressive disclosure.

**Implementation Without Native Support**: Write MCP servers providing tools for launching new agent sessions, receiving parent prompts, launching sub-agents with those prompts, and returning final responses.

### Hooks for Control Flow

Hooks (in Claude Code/Opencode, similar to git hooks) execute automatically at lifecycle events and various agent moments. They can:
- Run silently when events occur
- Run on tool calls and return additional context
- Surface build/type errors forcing resolution before agent completion

**Use Cases**:
- Notifications (sounds when finished/needs attention)
- Approvals/denials of tool calls based on rules
- Integrations (Slack messages, GitHub PRs, preview environments)
- Verification (typecheck/build on agent stop)

**Example Hook**: The article includes a bash script that runs on agent stop to execute biome formatting and TypeScript typechecks. Success is silent; only errors surface to trigger agent re-engagement.

---

## Back-Pressure Mechanisms

Success likelihood correlates strongly with agent ability to verify its own work. Effective back-pressure mechanisms include:

- Typechecks and builds (in strongly-typed languages)
- Unit/integration tests
- Code coverage reporting
- UI interaction testing (Playwright, agent-browser)

**Critical Principle**: Verification must be context-efficient. Success should be silent; only failures produce verbose output.

HumanLayer learned this by initially running full test suites (4,000+ lines of passing tests), which flooded context windows causing agents to lose task focus. Now they surface only errors.

---

## Strategic Insights

### Long-Context Models: A Skeptical Take

Extended-context models don't necessarily solve problems better—they just make the haystack bigger. In needle-in-a-haystack tasks, bigger context windows don't improve finding ability; they deepen the "dumb zone" by allowing more instructions to accumulate.

The solution isn't longer context but better context isolation via sub-agents providing fresh, small, high-relevance windows.

### Working Backwards From Model Limitations

Viv's framework derives harness components by understanding what models can't do natively: system prompts provide instructions, tools/MCPs extend capabilities, context manages scope, sub-agents enable distributed work.

### Post-Training Coupling

Frontier models are post-trained on specific harnesses (Claude with Claude Code, GPT-5 Codex with Codex harness). While models may perform better with their training harness, they can be over-fitted to it.

Terminal Bench 2.0 data shows Opus 4.6 ranked #33 in Claude Code but jumped to #5 when placed in different harnesses—demonstrating harness configuration matters enormously.

---

## Practical Recommendations

### What Worked
- Starting simple, adding configuration only after actual failures
- Designing, testing, iterating, and discarding unhelpful changes
- Distributing battle-tested configurations team-wide
- Optimizing for iteration speed over one-shot success
- Carefully paring down exposed capabilities after understanding actual needs

### What Didn't Work
- Designing ideal harness upfront before real failures
- Installing dozens of skills/MCP servers preemptively
- Running full test suites at every session end (use subsets instead)
- Micro-optimizing sub-agent tool access (causes tool thrash)

---

## Conclusion

The article concludes that most coding agent performance issues stem from harness configuration, not model capability. Configuration points—agentfiles, MCP servers, skills, sub-agents, hooks, and back-pressure mechanisms—contain most leverage for improvement.

**Final insight**: "The model is probably fine. It's just a skill issue."

The approach emphasizes bias toward shipping: optimize harness configuration only when it enables faster, higher-quality code delivery. When failures occur, engineer specific solutions to prevent recurrence rather than pursuing preemptive optimizations.

---

## Related Content Links
- Previous: "Getting Claude to Actually Read Your CLAUDE.md" (March 17, 2026)
- Older: "A Brief History of Ralph" (January 6, 2026)
