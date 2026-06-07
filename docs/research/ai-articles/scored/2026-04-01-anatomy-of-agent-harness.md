> Source: https://blog.dailydoseofds.com/p/the-anatomy-of-an-agent-harness
> Fetched: 2026-05-08

# The Anatomy of an Agent Harness

## Introduction

Before foundation models emerged, developing AI features required collecting labeled training data, training custom models, and investing significant compute before validating user demand. Foundation models disrupted this by offering pre-trained capabilities via API, enabling teams to ship MVPs in days rather than months.

However, agentic systems introduce a new complexity layer. Agent design must follow product definition because "the agent's capabilities, workflows, and memory requirements are what determine what knowledge it needs and which model providers make sense downstream."

## The Canvas Framework

MongoDB published the Canvas Framework, which structures agent development in two phases:

**POC Canvas** covers eight areas: product validation, agent design (capabilities, autonomy, memory), data requirements (knowledge sources, update frequency), and model integration (provider selection, prompt strategy, cost).

**Production Canvas** adds eleven elements for scaling: fault tolerance, multi-agent coordination, unified data architecture, security hardening, and governance.

## What Is an Agent Harness?

An agent harness represents "the complete software infrastructure wrapping an LLM, including the orchestration loop, tools, memory, context management, state persistence, error handling, and guardrails."

The distinction matters: the agent itself is emergent behavior—the goal-directed, tool-using entity users interact with. The harness is the machinery producing that behavior.

Using Beren Millidge's analogy, a raw LLM functions like a CPU without RAM, disk, or I/O:
- Context window = RAM (fast, limited)
- External databases = disk storage (large, slow)
- Tool integrations = device drivers
- The harness = operating system

## Three Levels of Engineering

**Prompt engineering** crafts model instructions. **Context engineering** manages what models see and when. **Harness engineering** encompasses both plus complete application infrastructure: tool orchestration, state persistence, error recovery, verification loops, safety enforcement, and lifecycle management.

## The 11 Components of a Production Harness

### 1. The Orchestration Loop

This implements the Thought-Action-Observation cycle, repeating: assemble prompt, call LLM, parse output, execute tool calls, feed results back. Anthropic describes this as a "dumb loop" where intelligence resides in the model, not the orchestration mechanism.

### 2. Tools

Tools function as the agent's interface to external systems. They're defined as schemas injected into the LLM's context. The tool layer manages registration, schema validation, argument extraction, sandboxed execution, result capture, and formatting. Claude Code provides tools across six categories: file operations, search, execution, web access, code intelligence, and subagent spawning.

### 3. Memory

Memory operates across multiple timescales. Short-term memory comprises conversation history within sessions. Long-term memory persists across sessions—Anthropic uses project files and auto-generated memory files; LangGraph uses namespace-organized JSON stores.

Claude Code implements a three-tier hierarchy: lightweight indexes (~150 characters per entry, always loaded), detailed topic files loaded on demand, and raw transcripts accessed via search only.

### 4. Context Management

Context rot represents a critical challenge: "model performance degrades 30%+ when key content falls in mid-window positions." Production strategies include:

- **Compaction**: summarizing conversation history while preserving architectural decisions and unresolved issues
- **Observation masking**: hiding old tool outputs while keeping tool calls visible
- **Just-in-time retrieval**: maintaining lightweight identifiers and loading data dynamically
- **Sub-agent delegation**: returning condensed 1,000-2,000 token summaries rather than full context

### 5. Prompt Construction

This assembles what the model receives at each step—system prompt, tool definitions, memory files, conversation history, and current user message. OpenAI's Codex uses a strict priority stack with server-controlled system messages at highest priority, followed by tool definitions, developer instructions, and user instructions.

### 6. Output Parsing

Modern harnesses rely on native tool calling, where models return structured `tool_calls` objects rather than free-text requiring parsing. The harness checks for tool calls, executes them if present, and loops accordingly.

### 7. State Management

LangGraph models state as typed dictionaries flowing through graph nodes. Checkpointing occurs at super-step boundaries, enabling resumption after interruptions. OpenAI offers four mutually exclusive strategies: application memory, SDK sessions, server-side Conversations API, or lightweight response chaining.

### 8. Error Handling

A 10-step process with 99% per-step success still achieves only ~90.4% end-to-end success due to compounding failures. LangGraph distinguishes four error types: transient (retry with backoff), LLM-recoverable (return error as ToolMessage), user-fixable (interrupt for input), and unexpected (bubble up for debugging).

### 9. Guardrails and Safety

OpenAI's SDK implements three levels: input guardrails (on first agent), output guardrails (on final output), and tool guardrails (on every invocation). Anthropic separates permission enforcement from model reasoning—the model decides what to attempt; the tool system decides what's allowed. Claude Code gates approximately 40 discrete tool capabilities independently with three stages: trust establishment, permission checking, and user confirmation for high-risk operations.

### 10. Verification Loops

This separates production agents from demos. Recommended approaches include rules-based feedback (tests, linters), visual feedback (screenshots), and LLM-as-judge (separate subagent evaluation). "Giving the model a way to verify its work improves quality by 2 to 3x."

### 11. Subagent Orchestration

Claude Code supports three execution models: Fork (byte-identical context copy), Teammate (separate terminal with file-based communication), and Worktree (own git worktree). OpenAI supports agents-as-tools (specialist handling bounded subtasks) and handoffs (specialist taking full control).

## Step-by-Step Walkthrough

**Step 1 (Prompt Assembly)**: Construct full input combining system prompt, tool schemas, memory files, conversation history, and current message. Important context positions at beginning and end.

**Step 2 (LLM Inference)**: Send assembled prompt to model API. Model generates text, tool calls, or both.

**Step 3 (Output Classification)**: If text without tool calls, terminate loop. If tool calls requested, proceed to execution. If handoff requested, update current agent and restart.

**Step 4 (Tool Execution)**: Validate arguments, check permissions, execute in sandboxed environment, capture results. Read-only operations run concurrently; mutating operations run serially.

**Step 5 (Result Packaging)**: Format results as LLM-readable messages. Return errors as error results enabling model self-correction.

**Step 6 (Context Update)**: Append results to conversation history. If approaching context limits, trigger compaction.

**Step 7 (Loop)**: Return to Step 1 until termination conditions met.

Termination occurs when the model produces responses without tool calls, maximum turn limits exceeded, token budgets exhausted, guardrails trigger, users interrupt, or safety refusals occur.

For long-running tasks spanning multiple context windows, Anthropic developed the "Ralph Loop" pattern: an Initializer Agent sets up environments, then a Coding Agent in subsequent sessions reads git logs and progress files to orient itself, selecting highest-priority incomplete features.

## Framework Implementations

**Anthropic's Claude Agent SDK** exposes the harness through a single `query()` function creating the agentic loop and returning an async iterator. The runtime is a "dumb loop" where all intelligence lives in the model. Claude Code uses a Gather-Act-Verify cycle: gather context, take action, verify results.

**OpenAI's Agents SDK** implements the harness through the Runner class with three modes: async, sync, and streamed. It's "code-first," expressing workflow logic in native Python rather than graph DSLs.

**LangGraph** models the harness as explicit state graphs with two nodes (`llm_call` and `tool_node`) connected by conditional edges. It evolved from LangChain's deprecated AgentExecutor, which lacked multi-agent support and extensibility.

**LangChain's Deep Agents** explicitly use "agent harness" terminology: built-in tools, planning, file systems for context management, subagent spawning, and persistent memory.

**CrewAI** implements role-based multi-agent architecture: Agent (harness around LLM defined by role, goal, backstory, tools), Task (unit of work), and Crew (agent collection). Its Flows layer adds "deterministic backbone with intelligence where it matters."

## The Scaffolding Metaphor

Construction scaffolding enables workers to build structures they couldn't reach otherwise. It doesn't perform construction but enables workers to access upper floors.

As models improve, harness complexity should decrease. Manus was rebuilt five times in six months, each rewrite removing complexity. Complex tool definitions became general shell execution; "management agents" became simple structured handoffs.

This reveals the co-evolution principle: models now post-train with specific harnesses in the loop. Claude Code's model learned to use its specific harness. Changing tool implementations can degrade performance due to tight coupling.

The future-proofing test states: "if performance scales up with more powerful models without adding harness complexity, the design is sound."

## Seven Harness Architecture Decisions

Every harness architect faces seven key choices:

**1. Single-agent vs. multi-agent**: Both Anthropic and OpenAI recommend maximizing single agents first. Multi-agent systems add overhead through extra LLM calls for routing and context loss during handoffs. Split when tool overload exceeds approximately 10 overlapping tools or clearly separate task domains exist.

**2. ReAct vs. plan-and-execute**: ReAct interleaves reasoning and action at every step (flexible but higher per-step cost). Plan-and-execute separates planning from execution. LLMCompiler reports 3.6x speedup over sequential ReAct.

**3. Context window management strategy**: Five production approaches include time-based clearing, conversation summarization, observation masking, structured note-taking, and sub-agent delegation. ACON research showed 26-54% token reduction while preserving 95%+ accuracy.

**4. Verification loop design**: Computational verification (tests, linters) provides deterministic ground truth. Inferential verification (LLM-as-judge) catches semantic issues but adds latency.

**5. Permission and safety architecture**: Permissive approaches (fast, risky) versus restrictive approaches (safe, slow) depend on deployment context.

**6. Tool scoping strategy**: More tools often mean worse performance. Vercel removed 80% of tools from v0 and achieved better results. Claude Code achieves 95% context reduction via lazy loading. The principle: expose the minimum tool set needed for the current step.

**7. Harness thickness**: How much logic lives in the harness versus the model. Anthropic bets on thin harnesses and model improvement. Graph-based frameworks bet on explicit control. Anthropic regularly deletes planning steps from Claude Code as new model versions internalize that capability.

## The Harness Is the Product

Two products using identical models can have wildly different performance based solely on harness design. TerminalBench evidence demonstrates that changing only the harness moved agents by 20+ ranking positions. One research project achieved 76.4% pass rates by having an LLM optimize the infrastructure itself, surpassing hand-designed systems. LangChain changed only infrastructure wrapping their LLM (same model, same weights) and jumped from outside the top 30 to rank 5 on TerminalBench 2.0.

The harness represents a non-commoditized layer where hard engineering lives: managing context as scarce resource, designing verification loops catching failures before compounding, building memory systems providing continuity without hallucination, and making architectural bets about scaffolding versus model capability.

The field moves toward thinner harnesses as models improve. But harnesses themselves won't disappear. "Even the most capable model needs something to manage its context window, execute its tool calls, persist its state, and verify its work."

The key insight: "The next time your agent fails, don't blame the model but rather look at the harness."

---

## 繁體中文全文摘要

### 核心命題：Harness 就是產品

兩個使用相同模型的產品，僅憑 harness 設計就能有天壤之別的效能。TerminalBench 2.0 實證：僅改變 harness，LangChain DeepAgent 從第 30 名外躍升至第 5 名；同一模型。**下次 Agent 失敗，不要怪模型，看 harness**。

### Canvas Framework：POC → Production 雙階段

**POC Canvas（概念驗證）**：8 個領域——產品驗證、Agent 設計（能力、自主性、記憶）、資料需求、模型整合

**Production Canvas**：再增加 11 個要素——容錯、多代理協調、統一資料架構、安全加固、治理

### 生產 Harness 的 11 大組件

| 組件 | 職責 | 關鍵細節 |
|------|------|---------|
| **1. Orchestration Loop** | Thought-Action-Observation 循環 | 「笨循環」—智能在模型，不在循環機制 |
| **2. Tools** | Agent 與外部系統的介面 | Schema 注入 context；6 類工具（檔案、搜尋、執行、網路、程式智能、子代理）|
| **3. Memory** | 多時間尺度記憶 | 短期（session 內）+ 長期（跨 session）；三層層級 |
| **4. Context Management** | 管理 context rot | 壓縮、觀察遮罩、即時載入、子代理委派 |
| **5. Prompt Construction** | 組裝模型輸入 | 系統提示 + 工具定義 + 記憶檔 + 對話歷史 + 當前訊息 |
| **6. Output Parsing** | 解析模型輸出 | 原生工具呼叫（`tool_calls` 物件）> 自由文字解析 |
| **7. State Management** | 管理執行狀態 | LangGraph 型別字典 + checkpoint；四種互斥策略 |
| **8. Error Handling** | 處理失敗 | 四類錯誤：瞬時/LLM 可恢復/需用戶介入/意外 |
| **9. Guardrails & Safety** | 安全護欄 | 輸入/輸出/工具三層；模型決定嘗試，工具系統決定是否允許 |
| **10. Verification Loops** | 驗證輸出 | 規則型（測試、linter）+ 視覺 + LLM-as-judge；驗證改進品質 2-3x |
| **11. Subagent Orchestration** | 子代理協調 | Fork / Teammate / Worktree 三種執行模式 |

### 關鍵量化數據

- **Context rot**：關鍵內容落在 context 中間時，模型效能下降 **30%+**
- **ACON 壓縮**：26-54% token 減少，同時保留 **95%+** 精準度
- **Verification 效果**：讓模型有方法驗證自己的工作，品質提升 **2-3x**
- **Tool 精簡**：Vercel 移除 80% 工具後結果更好；Claude Code 懶載入實現 **95%** context 減少

### 七大架構決策

1. **單代理 vs. 多代理**：優先最大化單代理；工具超過 ~10 個重疊或任務域清楚分離時才分割
2. **ReAct vs. 計劃-執行分離**：LLMCompiler 報告比循序 ReAct 快 3.6x
3. **Context Window 管理策略**：5 種生產方法（時間清除、對話摘要、觀察遮罩、結構化筆記、子代理委派）
4. **驗證循環設計**：計算驗證（確定性）vs. 推理驗證（LLM-as-judge，語義更佳但延遲更高）
5. **權限與安全架構**：寬鬆（快但風險）vs. 限制（安全但慢）
6. **工具範圍策略**：最少工具原則——只暴露當前步驟所需的最小工具集
7. **Harness 厚度**：Anthropic 押注薄 harness + 模型改進；圖形框架押注明確控制

### Co-Evolution 原則

模型現在與特定 harness 一起後訓練——Claude Code 的模型學習使用其特定 harness。改變工具實作可能因緊耦合而降低效能。**未來驗證測試**：「如果更強大的模型帶來效能提升且不增加 harness 複雜性，設計就是健全的。」

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 9/10 | Canvas Framework（POC vs Production）、7 個架構決策均可直接套用 |
| B. 創新性 | 8/10 | Canvas Framework 原創、ACON 壓縮指標、Co-Evolution 原則新穎 |
| C. 證據品質 | 8/10 | context rot -30%、ACON 26-54% 壓縮、驗證 2-3x 品質提升有量化數據 |
| D. 技術深度 | 8/10 | 11 個組件詳細說明、7 個架構決策、Context Manager 機制 |
| E. 泛化性 | 8/10 | Canvas Framework 適用任何規模的 harness 設計 |
| **加權總分** | **8.3/10** | 9×0.3+8×0.2+8×0.2+8×0.15+8×0.15 = 2.7+1.6+1.6+1.2+1.2 |

**整合決策**：SKILL  
**整合位置**：`.claude/skills/harness-eval/`（Canvas Framework 作為評估工具）  
**整合狀態**：待實作
