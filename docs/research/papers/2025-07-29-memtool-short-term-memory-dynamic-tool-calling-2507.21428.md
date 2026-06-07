---
title: "MemTool: Optimizing Short-Term Memory Management for Dynamic Tool Calling in LLM Agent Multi-Turn Conversations"
arxiv_id: 2507.21428
authors: "Elias Lumer, Anmol Gulati, Vamse Kumar Subbiah, Pradeep Honaganahalli Basavaraju, James A. Burke"
fetched: 2026-05-26
published: 2025-07-29
source: "https://arxiv.org/abs/2507.21428"
source_tier: P
---

# MemTool: Optimizing Short-Term Memory Management for Dynamic Tool Calling in LLM Agent Multi-Turn Conversations

**Authors**: Elias Lumer, Anmol Gulati, Vamse Kumar Subbiah, Pradeep Honaganahalli Basavaraju, James A. Burke (Commercial Technology and Innovation Office, PricewaterhouseCoopers, U.S.A.)
**Published**: July 2025
**Source**: https://arxiv.org/abs/2507.21428
**arXiv ID**: 2507.21428
**Categories**: cs.CL (Computation and Language)

---

## Abstract

Large Language Model (LLM) agents have shown significant autonomous capabilities in dynamically searching and incorporating relevant tools or Model Context Protocol (MCP) servers for individual queries. However, fixed context windows limit effectiveness in multi-turn interactions requiring repeated, independent tool usage. We introduce MemTool, a short-term memory framework enabling LLM agents to dynamically manage tools or MCP server contexts across multi-turn conversations. MemTool offers three agentic architectures: 1) Autonomous Agent Mode, granting full tool management autonomy, 2) Workflow Mode, providing deterministic control without autonomy, and 3) Hybrid Mode, combining autonomous and deterministic control. Evaluating each MemTool mode across 13+ LLMs on the ScaleMCP benchmark, we conducted experiments over 100 consecutive user interactions, measuring tool removal ratios (short-term memory efficiency) and task completion accuracy. In Autonomous Agent Mode, reasoning LLMs achieve high tool-removal efficiency (90–94% over a 3-window average), while medium-sized models exhibit significantly lower efficiency (0–60%). Workflow and Hybrid modes consistently manage tool removal effectively, whereas Autonomous and Hybrid modes excel at task completion. We present trade-offs and recommendations for each MemTool mode based on task accuracy, agency, and model capabilities.

---

## Core Thesis

MemTool addresses the gap in short-term tool memory management for LLM agents in multi-turn conversations: while existing work focuses on compressing conversational context via summarization/truncation, no prior work evaluated how agents manage dynamic tool context (adding and removing tools) across 100+ sequential turns. Three architectures with varying autonomy levels are proposed and benchmarked across 13+ LLMs, revealing that reasoning models handle autonomous tool removal well (90–94%), while smaller models require deterministic workflow scaffolding to achieve comparable removal efficiency.

---

## 1. Introduction

The LLM is the CPU, and its context window is the RAM (adapted from Andrej Karpathy, "Software in the Era of AI," Y Combinator AI Startup School, June 2025).

Recent breakthroughs in LLM agents enable scalable agentic systems that autonomously search, discover, equip, and use a dynamic repository of tools or MCP servers. Dynamic tool calling allows agents to interact with external APIs without being constrained to a fixed toolset at initialization — analogous to a human navigating a mobile app store.

As LLM agents become embedded in session-based applications (chat, voice, video), managing limited context windows becomes necessary for multi-turn conversations. **Context engineering** and **memory management** systems allow multi-turn interactions to persist within a session (short-term memory) and across sessions (long-term memory).

**The gap**: Current literature on short-term memory focuses on compressing conversation history via summarization or truncation of messages, but does not address the dynamic retrieval and management of tools within an agent's context window. Previous work shows agents can handle thousands of tools via RAG without accuracy drops — but none addresses the *removal and management* of tools across 100+ multi-turn sessions while using native function calling.

MemTool fills this gap with three modes for managing an LLM agent's context window of tools across multi-turn conversations.

---

## 2. Background

### 2.1 Memory for LLM Agents

Existing literature divides memory for AI systems into:
- **Short-term memory**: memories within the session; includes sensory memory (multi-modal inputs, tool calls) and working memory (system/assistant/human messages, chain of thoughts). Context engineering strategies involve summarization or truncation of previous messages.
- **Long-term memory**: persists across sessions. Includes explicit memory (episodic + semantic) and implicit memory (learned skills). Frameworks: Mem0, Zep, Letta.

Summarizing long multi-turn dialogues is prone to over-summarization or information loss. MemTool is the first study to address and evaluate short-term memory for dynamic tool-use across multi-turn conversations.

### 2.2 Tool Selection and Retrieval for LLM Agents

Leading model providers impose limits of 128–512 tools per LLM API request. Prior work circumvents this with RAG strategies: storing large toolsets externally in vector databases or knowledge graphs, dynamically selecting only necessary tools at runtime.

Agentic RAG frameworks give LLM agents specialized tool-discovery tools that autonomously identify and invoke appropriate tools. Recent work (ScaleMCP) enables agents to dynamically query a repository of 5,000+ MCP servers. However, none address the removal and management of dynamic tools for 100+ multi-turn sessions.

### 2.3 Tool Calling / LLM Invocation

MemTool deliberately adopts plug-and-play methodology compatible with out-of-the-box models and standard embedding solutions from OpenAI, Google, Anthropic, and Meta — no fine-tuning required. The framework equips the LLM with explicit operations for adding and removing tools from its active context.

---

## 3. Method: MemTool

MemTool enables an LLM agent to manage its own context window of dynamic tools across multi-turn sessions. The broader implication: LLM agents can operate in production environments with a non-fixed set of tools, searching, equipping, and removing tools or MCP servers, similarly to a human navigating a mobile app store.

### 3.1.1 Autonomous Agent Mode

Grants full autonomy to the LLM agent to manage its context window while simultaneously answering the user task, across multi-turn conversations. Two additional tools are equipped to the agent:

1. **Search_Tools(keywords: List[str])**: adds tools from vector store to context (adapted from ScaleMCP)
2. **Remove_Tools(tool_names: List[str])**: removes listed tools from the API call's tools parameter

**Algorithm (summarized):**
1. Prune previous messages (truncation or summarization) if token overflow
2. Add Search_Tools and Remove_Tools to the prior tool set
3. Enter a while loop: LLM calls tools as needed (searching, removing, executing)
4. If tool count exceeds limit L=128, raise an error prompting tool removal
5. Return final answer

**Key implementation note**: A dynamic variable for current tool count is passed in the system prompt on every query — this was critical for good removal behavior (without it, models failed to remove tools).

**Recommendations:**
- Use reasoning models (GPT-o3, Gemini 2.5 Pro/Flash, Claude Opus 4) for high removal efficiency
- Include current tool count as a dynamic variable in the system message
- Upper limit tool errors (e.g., 128) "encourage" LLMs to remove tools
- Prompting with detailed guidelines on when to remove/add tools improves performance

### 3.1.2 Workflow Mode

Limits LLM autonomy by abstracting tool management to a fixed deterministic workflow after every user query. Two fresh LLM calls occur in sequence:
1. A **prune LLM call** removes irrelevant tools (no longer relevant to current query)
2. A **search LLM call** identifies keywords and retrieves new tools via vector search

Only after this prune-then-search pipeline is the main LLM agent initialized with the updated tool set (without Remove_Tools, only with Search_Tools for any additional retrieval).

**Recommendations:**
- Recommended first choice for simplicity and reliability
- Once LLM agent is initialized, no mechanism to revert to searching new tools
- Self-correcting patterns become overly complex; Workflow intentionally avoids them

### 3.1.3 Hybrid Mode

Combines both approaches: the deterministic prune step (a fresh LLM call removes irrelevant tools) followed by full agent autonomy for searching and adding tools. Motivated by the observation that LLMs struggle with removal but perform well at searching/adding.

**Algorithm (summarized):**
1. Prune LLM call removes irrelevant tools deterministically
2. LLM agent enters while loop with Search_Tools (no Remove_Tools) — free to search and add
3. If tool count exceeds L, a prune LLM call is triggered again before continuing

**Recommendations:**
- Search_Tools enables re-querying if retrieved tools are insufficient
- Agent is abstracted from tool removal, preventing removal errors
- As models improve, Hybrid can transition to full Autonomous Agent Mode

### 3.2 Dataset

5,000 tools/MCP servers from the ScaleMCP benchmark. 100 instances sampled (stratified by number of tool calls per turn; average 5.0 tool calls per turn) for a 100 multi-turn tool-use dialogue.

---

## 4. Evaluations

### 4.1 Experiment Settings

- **13 LLM models** evaluated (closed and open source)
- **Embedding model**: Azure OpenAI text-embedding-ada-002
- **Tool limit**: 128 tools (standardized across all models; some models support 256–512)
- **100 sequential user queries** per experiment; each query may be related or unrelated to the prior
- **Judge model**: OpenAI GPT-4o mini (for Task Completion alignment scoring)

**Metrics:**
- **Removal Ratio**: proportion of tools successfully removed after being added (cumulative)
- **AvgRemovalRatio_3T**: rolling 3-turn window average removal ratio (primary efficiency metric)
- **AvgResidual_3T**: average number of tools remaining after a 3-turn grace window (tool accumulation)
- **Task Completion**: LLM-as-judge alignment between agent's final response and expected answer
- **Tool Correctness**: proportion of tool calls matching expected tool calls

### 4.2 Autonomous Agent Mode Results

| LLM | Avg Removal Ratio 3T | Avg Residual 3T | Tool Correctness | Task Completion |
|-----|---------------------|-----------------|-----------------|-----------------|
| GPT-o3 | 0.941 | 7.44 | 0.75 | 0.90 |
| Gemini 2.5 Pro | 0.924 | 6.51 | 0.81 | 0.80 |
| Gemini 2.5 Flash | 0.905 | 5.08 | 0.74 | 0.65 |
| Claude Opus 4 | 0.878 | 13.85 | 0.86 | 0.84 |
| Claude Sonnet 4 | 0.840 | 24.44 | 0.80 | 0.83 |
| GPT-4.1 | 0.834 | 48.12 | 0.86 | 0.88 |
| GPT-4.1 Mini | 0.733 | 58.93 | 0.78 | 0.80 |
| GPT-4o | 0.713 | 37.48 | 0.68 | 0.76 |
| LLaMA 3 70B | 0.244 | 123.33 | 0.42 | 0.72 |
| Claude 3.5 Sonnet | 0.062 | 124.00 | 0.38 | 0.59 |
| GPT-4.1 Nano | 0.000 | 0.00 | 0.13 | 0.60 |

**Key findings:**
- Reasoning models (GPT-o3, Gemini 2.5 Pro/Flash, Claude Opus 4) achieve 90–94% rolling 3-window removal; they remove ~95% of total tools across 100 conversations and score 80–90% on Task Completion and Tool Correctness.
- Smaller/medium models without large RL reasoning budgets (GPT-4o Mini, GPT-4.1 Mini, Claude 3.5 Sonnet, LLaMA 3 70B) fail to remove tools — LLaMA 3 70B and Claude 3.5 Sonnet hit the 128 limit within turn 20.
- GPT-4.1 Nano: 0.000 removal ratio — completely failed to remove tools.
- Gemini 2.5 Flash is the only small model above 90% removal ratio, but struggles at task completion (0.65).

**Discussion**: The system prompt must include the current tool count as a dynamic variable; without it, models fail to remove tools. This reveals an inability of LLMs to introspect the count of tools available via the API function calling parameter.

### 4.3 Workflow Mode Results

| LLM | Avg Removal Ratio 3T | Avg Residual 3T | Tool Correctness | Task Completion |
|-----|---------------------|-----------------|-----------------|-----------------|
| GPT-4o | 0.938 | 7.19 | 0.71 | 0.70 |
| GPT-4.1 | 0.934 | 7.48 | 0.82 | 0.83 |
| LLaMA 3 70B | 0.932 | 8.64 | 0.51 | 0.71 |
| Gemini 2.5 Pro | 0.929 | 6.90 | 0.69 | 0.66 |
| Gemini 2.5 Flash | 0.928 | 6.60 | 0.50 | 0.60 |
| GPT-o3 | 0.925 | 7.59 | 0.88 | 0.84 |
| GPT-4.1 Mini | 0.922 | 7.72 | 0.72 | 0.81 |
| Claude 3.5 Sonnet | 0.917 | 7.83 | 0.82 | 0.82 |
| Claude Opus 4 | 0.917 | 7.92 | 0.71 | 0.78 |
| Claude Sonnet 4 | 0.917 | 8.00 | 0.77 | 0.81 |
| GPT-4.1 Nano | 0.904 | 8.96 | 0.64 | 0.66 |

**Key findings:**
- All models achieve >90% removal ratio — dramatic improvement over Autonomous Agent Mode for weaker models
- LLaMA 3 70B: 0.244 removal in Autonomous → 0.932 in Workflow
- Claude 3.5 Sonnet: 0.062 → 0.917
- GPT-o3 leads on Tool Correctness (88%) and Task Completion (84%)
- GPT-4.1 Nano and Gemini 2.5 Flash: excellent removal but weaker at reasoning over tools
- Workflow removes the burden of memory optimization from the model, enabling even smaller models to perform well

**Recommendation**: Use Workflow Mode when cost efficiency and reliability are priorities. Model selection can hinge on Task Completion needs rather than memory management ability.

### 4.4 Hybrid Mode Results

| LLM | Avg Removal Ratio 3T | Avg Residual 3T | Tool Correctness | Task Completion |
|-----|---------------------|-----------------|-----------------|-----------------|
| GPT-4o | 0.943 | 7.15 | 0.77 | 0.76 |
| GPT-4.1 | 0.941 | 7.29 | 0.82 | 0.80 |
| LLaMA 3 70B | 0.938 | 7.52 | 0.60 | 0.76 |
| Gemini 2.5 Pro | 0.938 | 6.52 | 0.74 | 0.75 |
| Claude 3.5 Sonnet | 0.935 | 7.32 | 0.81 | 0.83 |
| GPT-o3 | 0.932 | 9.33 | 0.82 | 0.87 |
| Gemini 2.5 Flash | 0.932 | 6.15 | 0.59 | 0.66 |
| GPT-4.1 Mini | 0.929 | 7.26 | 0.81 | 0.79 |
| Claude Opus 4 | 0.920 | 10.46 | 0.82 | 0.81 |
| Claude Sonnet 4 | 0.912 | 10.27 | 0.82 | 0.81 |
| GPT-4.1 Nano | 0.869 | 6.94 | 0.48 | 0.63 |

**Key findings:**
- Hybrid Mode achieves the highest overall removal ratios across most models (GPT-4o: 0.943, GPT-4.1: 0.941)
- GPT-o3 retains strong task completion (0.87) with high removal (0.932)
- Claude 3.5 Sonnet recovers to 0.935 removal and 0.83 task completion (vs 0.062 in Autonomous)
- LLaMA 3 70B: strong recovery to 0.938 removal with 0.76 task completion
- GPT-4.1 Nano remains weakest (0.869) but significantly better than Autonomous (0.000)

---

## 5. Mode Selection Recommendations

| Priority | Recommended Mode |
|----------|-----------------|
| Maximum task completion + model is a reasoning LLM | Autonomous Agent Mode |
| Cost efficiency + reliability + any model size | Workflow Mode |
| Balance of task completion and tool memory efficiency | Hybrid Mode |
| Small/medium models in production | Workflow or Hybrid |
| Reasoning models (GPT-o3, Gemini 2.5 Pro, Claude Opus 4) | Any mode performs well |

**Overall trade-off summary:**
- **Autonomous**: highest task completion for strong models, but breaks for weaker models; requires dynamic tool count in system prompt
- **Workflow**: most reliable removal across all model sizes; limited self-correction after agent initialization
- **Hybrid**: best balance; deterministic removal + agentic search; can escalate to Autonomous as models improve

---

## Key References

- Lumer et al. (2025b) — ScaleMCP benchmark (5,000 MCP servers for dynamic tool retrieval evaluation)
- Lumer et al. (2025c, 2025d) — Dynamic tool retrieval with RAG for LLM agents
- Wu et al. (2025b) — Short-term and long-term memory survey for LLM agents
- Karpathy (2025) — "Software in the Era of AI" (LLM as CPU, context window as RAM)
- Model Context Protocol (2025) — MCP server specification
- Mem0, Zep, Letta (2025) — Long-term memory frameworks
- OpenAI (2024) — Tool limit constraints in chat completions API (128–512 tools)
- Google (2025a), Anthropic (2025), Meta Platforms (2025) — Embedding and model APIs
- Chen et al. (2024) — RAG for large-scale tool selection
- Zhang et al. (2025); Hao et al. (2025); Cheng et al. (2025) — Long-term memory for tool usage personalization
- Confident AI (2025) — LLM-as-judge evaluation framework
- Laban et al. (2025); Hong et al. (2025) — Context pruning for multi-turn dialogue
- Park et al. (2023); Zhong et al. (2023) — Long-term memory for LLM agents
