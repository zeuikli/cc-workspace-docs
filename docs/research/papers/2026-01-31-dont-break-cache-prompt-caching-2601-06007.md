---
title: "Don't Break the Cache: Efficient Prompt Caching for Agentic AI"
authors: "Benedikt Kolbe, Rania Mokhtar, David Müller, Barna Szabó"
published: "2026-01-31"
source: "https://arxiv.org/abs/2601.06007"
---

# Don't Break the Cache: Efficient Prompt Caching for Agentic AI

**Authors**: Benedikt Kolbe, Rania Mokhtar, David Müller, Barna Szabó
**Published**: January 31, 2026
**Source**: https://arxiv.org/abs/2601.06007
**arXiv ID**: 2601.06007
**Categories**: cs.AI, cs.LG

---

## Abstract

Prompt caching can reduce LLM API costs by 41–80% in agentic workflows, but cache invalidation from dynamic content is a critical, underexplored risk. This paper systematically evaluates three caching strategies for agentic AI coding tools, identifies the most common cache-breaking patterns, and recommends system-prompt-only caching as the optimal default strategy (78.5% cost reduction, 22.9% TTFT improvement with Claude Sonnet 4.5).

---

## Background: How Prompt Caching Works

### Provider Implementations

| Provider | Activation | Min Token Threshold | Cache TTL |
|----------|-----------|---------------------|-----------|
| Anthropic | Explicit `cache_control` parameter | 1,024 tokens | 5 min (extendable to 1 hr) |
| OpenAI | Automatic (no API change needed) | 1,024 tokens | ~5–10 min |
| Google Gemini | Automatic | 4,096 tokens | 1 min–1 day |

**Mechanism**: Caching reuses precomputed KV (Key-Value) states from the transformer's attention layers. When the prefix of a prompt matches a cached entry, computation for that prefix is skipped.

### Cost Reduction Mechanics

Cache hits are billed at a lower rate:
- Anthropic: ~90% discount on cached tokens
- OpenAI: 50% discount on cached input tokens
- Google: 75–85% discount

---

## Three Caching Strategies Evaluated

| Strategy | Description | Scope |
|----------|-------------|-------|
| **System-Prompt-Only** | Cache only the static system prompt | Fixed portion of context |
| **Full-Context** | Cache entire conversation history including tool results | All turns |
| **Exclude-Tool-Results** | Cache everything except dynamic tool outputs | History minus tool responses |

---

## Results: Strategy Comparison (Claude Sonnet 4.5)

| Strategy | Cost Reduction | TTFT Improvement | Cache Hit Rate |
|----------|---------------|------------------|---------------|
| **System-Prompt-Only** | **78.5%** | **22.9%** | Highest |
| Full-Context | 41–60% | Variable | Moderate |
| Exclude-Tool-Results | 55–70% | Moderate | Moderate |

**Key finding**: System-prompt-only caching is the most consistent strategy. Full-context caching can achieve higher absolute savings but is vulnerable to cache invalidation from dynamic content.

---

## Cache-Breaking Patterns

The paper identifies the most common sources of cache invalidation in agentic workflows:

### 1. Dynamic Tool Results
Tool outputs (file reads, web fetches, shell commands) vary between calls → any token in the cached prefix after a tool result is invalidated.

### 2. Timestamps and UUIDs
System prompts or messages containing `datetime.now()`, request IDs, or session UUIDs break the cache prefix on every call.

### 3. MCP (Model Context Protocol) Servers
MCP tool definitions are injected dynamically at runtime. If MCP tool lists change between calls (e.g., server restarts, capability negotiation), the tool block in the system prompt changes → **MCP breaks cache boundaries**.

### 4. Conversation Turn Insertion
Inserting a new user/assistant turn in the middle of a cached conversation invalidates everything after the insertion point.

---

## Provider-Specific Findings

### Anthropic
- Requires explicit `cache_control: {"type": "ephemeral"}` on the content block to cache
- Cache TTL defaults to 5 minutes; can request extended TTL up to 1 hour
- Tool definitions count toward the cacheable prefix if placed before the `cache_control` marker

### OpenAI
- Automatic prefix caching (no API change) at 1,024-token minimum
- Cache granularity: 128-token chunks
- Does not expose cache hit/miss in standard response (only via usage metadata)

### Google Gemini
- Explicit `cachedContent` API for system instruction caching
- 4,096-token minimum is higher barrier for short system prompts
- TTL configurable from 1 minute to 1 day — useful for batch processing

---

## Recommendations

### For Agentic AI Coding Tools

1. **Cache only the static system prompt** (system-prompt-only strategy) — highest consistency
2. **Keep tool definitions static**: avoid adding/removing MCP tools mid-session
3. **Remove dynamic content from system prompt**: no timestamps, session IDs, or per-request state
4. **Place dynamic content last**: structure prompts as `[static system prompt][static tool defs][dynamic history]`

### Anti-Patterns to Avoid

```
❌ System prompt with datetime.now()  →  breaks cache every second
❌ Tool results placed before cache_control marker  →  invalidates on every tool call
❌ MCP server restart between calls  →  tool list changes, cache miss
❌ UUID in system prompt header  →  unique per session, zero cache hits
```

### Recommended Prompt Structure

```
[CACHED]
<system>
  Static instructions (no dynamic content)
  Static tool definitions
  Static context documents
</system>
[cache_control marker here]

[DYNAMIC — NOT CACHED]
<tool_result>...</tool_result>
<human>...</human>
<assistant>...</assistant>
```

---

## Economic Impact at Scale

| Scale | Annual API Spend | Savings (System-Prompt-Only at 78.5%) |
|-------|-----------------|--------------------------------------|
| Startup (100K calls/day) | ~$36,500 | ~$28,600 |
| Mid-size (1M calls/day) | ~$365,000 | ~$286,600 |
| Enterprise (10M calls/day) | ~$3,650,000 | ~$2,866,000 |

TTFT (time-to-first-token) improvement of 22.9% is independently valuable for interactive tools where latency matters.

---

## Workspace Relevance

Directly actionable for workspace prompt caching configuration:

1. **78.5% cost reduction with system-prompt-only**: The workspace CLAUDE.md / AGENTS.md system prompt is static — this is exactly the target for caching. Apply `cache_control` to the static system prompt block.
2. **MCP breaks cache boundaries**: Any MCP server restart or tool-list change during a session invalidates the cache. Keep MCP tool lists stable within a session — don't add/remove MCP servers mid-task.
3. **No timestamps in CLAUDE.md**: Avoid including `currentDate` or session IDs in the auto-loaded system prompt (`@core.md`, `@output-discipline.md`) — these break caching.
4. **Dynamic tool results must come AFTER the cache marker**: In multi-tool agentic loops (`autoresearch`, `harness-meta`), place tool results in the dynamic (uncached) portion of context.
5. **22.9% TTFT improvement**: Prompt caching also reduces latency — relevant for interactive `sonnet-pilot` sessions where response time affects usability.
