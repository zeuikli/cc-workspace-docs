> Source: https://www.decodingai.com/p/agentic-harness-engineering
> Fetched: 2026-05-08

# Agentic Harness Engineering: LLMs as the New OS

## Introduction

At a financial personal assistant startup, the author discovered that stripping away complex frameworks like LlamaIndex and MCP in favor of plain Python, simple API calls, and a custom ReAct engine produced better results. This experience revealed a critical insight: the LLM model itself isn't the bottleneck—the infrastructure surrounding it determines whether an agent functions reliably in production.

Most engineering teams obsess over model selection, debating choices between GPT-4o, Claude Opus, and Gemini while chasing benchmark scores. However, the equation involves two equal parts: the model and the harness. TerminalBench 2.0 demonstrated this principle when changing only the harness architecture moved the DeepAgent from LangChain outside the top 30 to the top 5.

## What Is a Harness?

The concept of a harness draws from an agricultural analogy. A horse possesses inherent power but remains useless for farming without a harness to direct its strength toward productive work. Similarly, LLMs have intelligence but require tools, memory, state management, guardrails, and orchestration to operate reliably.

LangChain provides a clear definition: **"An agent equals a model plus a harness."** The harness encompasses every piece of code, configuration, and execution logic excluding the model itself.

A basic agent consists of a model, prompt, tools, and planning loop. A comprehensive harness extends this foundation by incorporating:

- Memory systems
- Guardrails and safety constraints
- Advanced orchestration mechanisms
- Context engineering techniques
- Multi-agent coordination

The harness typically includes a serving layer connecting the agent to various interfaces—terminal applications, web dashboards, IDE plugins, and messaging applications like Telegram.

Ultimately, harness engineering means constructing real software applications using LLMs as the operating system. Applications like Claude Code, OpenCode, OpenClaw, and Codex exemplify this approach. While the underlying model could theoretically be swapped, the genuine engineering value resides within the harness itself.

## Three Levels of Engineering

The field encompasses three distinct levels:

1. **Prompt Engineering**: Crafting specific instructions for the model
2. **Context Engineering**: Managing what information the model observes and when
3. **Harness Engineering**: Building complete application infrastructure controlling when context loads, which tools remain available, which actions are permitted, and how failures are handled

Each level encompasses the previous one, creating a hierarchy of engineering sophistication.

## The Anatomy of a Harness

A complete harness consists of eight interconnected components:

1. The LLM at the core
2. Tools for interaction
3. A planning loop determining actions
4. Context engineering managing information flow
5. A sandbox for secure execution
6. Memory systems across multiple layers
7. An orchestration layer coordinating operations
8. A serving layer connecting to user interfaces

### Multi-Surface Architecture

Modern harnesses employ multi-surface architecture, serving the same agent across different interfaces. OpenClaw exemplifies this approach, delivering consistent agent functionality across command-line interfaces, web UIs, desktop applications, and messaging platforms through a centralized Gateway using typed WebSocket protocols.

Codex evolved from a simple terminal tool into an App Server using JSON-RPC over standard input and output. OpenCode utilizes a Bun JS HTTP server where clients connect via HTTP, with an Event Bus broadcasting results in real-time.

These architectures introduce challenges: multiple messages arrive in parallel from different clients while users submit new requests during ongoing processing. To address this, systems implement priority queues and message buses. OpenClaw uses a lane-aware FIFO queue ensuring only one active run per session while enabling parallelism across different sessions.

### The Filesystem as Foundation

The filesystem emerges as the most foundational harness primitive, enabling durable storage, workspace management, multi-agent collaboration, and versioning. Remarkably, production harnesses typically use the filesystem as their primary state mechanism rather than implementing fancy vector databases.

This approach differs from traditional orchestration tools like Airflow in three critical ways:

- The agent loop operates non-deterministically
- Context management becomes a first-class concern
- The programmer inside the loop is the LLM itself

Systems like Prefect, Temporal, and DBOS provide durability while supporting dynamic pipelines rather than rigid, predefined DAGs.

## How Agents Decide What to Do Next

The ReAct (Reasoning and Acting) pattern represents the most common planning loop architecture. The model receives current state, reasons about the next action, executes that action through a tool call, and observes the result. This cycle repeats until a strict stopping condition triggers.

Consider a concrete example: fixing a failing test. First, the model reads test output, reasons that the import path is incorrect, and edits the file through a tool. Second, it reruns tests, identifies a new type mismatch error, and fixes it. Third, it runs tests again, they pass, and the model reasons the task is complete.

The harness orchestrates this loop while the model reasons and selects actions.

### Orchestrator-Worker Patterns

For complex tasks exceeding a single agent's capacity, harnesses implement orchestrator-worker patterns where the orchestrator decomposes tasks, delegates subtasks to specialized workers, and aggregates results. In OpenCode, a dedicated task tool spawns subagents, each receiving its own session, context window, and restricted tool set.

For tasks spanning multiple context windows, Claude Code implements Ralph Loops—a harness mechanism that intercepts the model's exit attempt, reinjects the original prompt in a clean context window, and forces continuation toward a completion goal using filesystem-persisted state.

### Single vs. Multiple Agents

The author's experience automating business operations revealed an important lesson: a single well-harnessed agent with memory and smart context engineering often outperforms multiple specialized agents. The recommendation: always start with one well-harnessed agent before pursuing multi-agent complexity.

## Tools That Enable Agent Action

Agent interaction with the environment occurs through specifically-designed toolkits for autonomous execution:

### General-Purpose Tools

**Bash** provides general-purpose capabilities, allowing agents to execute any shell command for tests, linters, or builds. This grants code execution capabilities, enabling models to design their own tools rather than remaining constrained by fixed options.

### Specialized Tools

**Filesystem tools** handle common operations—reading, writing, editing, and searching—more safely and efficiently than bash. A read tool might enforce absolute paths and line limits, while an edit tool validates replacement string uniqueness.

### State Management Tools

These track session-scoped tasks, providing working memory within a single session. OpenCode includes `ToDoAdd` and `ToDoRead` tools that manage task queues, helping agents track their execution plans.

### Orchestration Tools

These launch subagents with isolated prompts and context windows, such as OpenCode's task tool or Claude Code's agent tool.

### Feedback Loop Principle

The most important principle involves feedback loops. Boris Cherny, Claude Code's creator, noted that providing the model with verification capabilities improves quality by two to three times. OpenCode integrates the Language Server Protocol (LSP) to supply real-time code definitions and diagnostics, feeding undefined variables and type errors back to the LLM for immediate correction.

### Access Control

Harnesses enforce tool access control. In OpenCode, the planning agent cannot call edit tools, preventing exploratory agents from accidentally modifying code.

## Where Agents Run: Sandboxes

Agents execute code that can fail, crash, or cause system damage. Sandboxes isolate agent execution, preventing failures from affecting the host system or other agents while enabling horizontal scaling across parallel environments.

### Security vs. Capability Tradeoff

Different harnesses balance this tradeoff differently:

**Hard Sandbox Approach (Codex)**: Each task runs in an isolated cloud container with the repository preloaded. This provides maximum safety but prevents filesystem access beyond the container.

**Soft Sandbox Approach (OpenClaw)**: The workspace is the default working directory, granting maximum capability but introducing greater risk.

Most production harnesses occupy the middle ground, depending on the trust model.

### Cloud Sandboxes

When submitting a task to Codex, the harness spins up a fresh cloud container. The agent works inside, reading files, running tests, and installing packages, unable to touch the local machine. Upon completion, results are extracted and the container is destroyed.

Cloud sandboxes provide powerful computing resources—agents can train models using GPUs in sandbox environments powered by accelerators, similar to manually SSHing to different VMs. Multiple cloud sandboxes can be spun up for parallel agent execution.

### Local Sandboxes

Docker containers or isolated processes provide local alternatives, similar to Cursor's approach—useful for testing while granting agents full permissions to avoid requiring supervision.

## Memory Across Three Layers

To survive across sessions and context windows, every harness manages state across three distinct memory layers:

### Layer 1: Filesystem (Long-Term Memory)

This durable, persistent layer survives across sessions, storing progress files, git history, and session transcripts.

### Layer 2: RAM (Short-Term/Working Memory)

This fast but volatile layer holds conversation history and tool results during active sessions.

### Layer 3: Context Window (What the Model Sees)

This strictest constraint contains everything the model knows about the current task, with size limitations determining what's visible.

The harness orchestrates dynamics between these layers. On the read path, it selectively loads relevant state from disk into RAM, then assembles the context window using techniques like compaction, progressive disclosure, and just-in-time retrieval. On the write path, it persists important state back to disk after processing.

OpenClaw enforces a strict invariant: memory is always flushed to disk before being discarded from context. Rehydration is treated as a tool-shaped action where agents search and retrieve specific data rather than dumping everything into the context window.

### Context Engineering Techniques

Context engineering enables this management. When token counts exceed ninety percent of capacity, OpenCode automatically summarizes conversations. Codex assembles prompts from multiple sources and exploits prompt caching. Anthropic recommends structured note-taking files and sub-agent architectures to isolate context.

In Anthropic's long-running agent pattern, an initializer agent creates a script, progress file, and feature list. The coding agent reads git logs and progress files at each session start, updating progress as it advances. Notably, this requires no database or vector store—just the filesystem.

## What's Next

The field is witnessing a new software development paradigm. Rather than software engineers building traditional frontend and backend applications, the next generation will construct harnesses. Harness engineering merges software engineering with AI, operating at a higher level of abstraction.

Popular tools like Claude Code represent only the beginning. No company will indefinitely depend on proprietary harnesses. Even open-source solutions like OpenCode cannot address every specific use case. Companies will inevitably build their own custom systems.

At ZTRON, the author experienced firsthand that custom systems and infrastructure finally enable agents to function reliably in production.

### Current Limitations

However, current approaches have honest limitations:

- Memory still breaks across long sessions
- Validation loops still miss edge cases
- Orchestrating hundreds of parallel agents on shared codebases remains an open research problem

Harness engineering represents genuine engineering. The harness becomes its own product with its own bugs, drift, and maintenance burden.

---

**Key Takeaway**: The model alone doesn't determine production success. The harness—the infrastructure surrounding it—is what truly matters for reliable agent deployment.

---

## 繁體中文全文摘要

### 核心命題：LLM 是新的作業系統

去除 LlamaIndex、MCP 等複雜框架，改用純 Python、簡單 API 呼叫和自製 ReAct 引擎——結果反而更好。這個親身經歷揭示：**模型本身不是瓶頸，圍繞它的基礎設施才決定 Agent 是否能在生產中可靠運作**。

TerminalBench 2.0 驗證了這個原則：僅改變 harness 架構，就把 DeepAgent 從 LangChain 的前 30 名外提升到前 5 名。

### 三層工程階梯

```
Harness Engineering ⊇ Context Engineering ⊇ Prompt Engineering
```

| 層次 | 職責 |
|------|------|
| **Prompt Engineering** | 為模型撰寫特定指令 |
| **Context Engineering** | 管理模型觀察到什麼資訊及時機 |
| **Harness Engineering** | 建立完整應用基礎設施（何時載入 context、哪些工具可用、哪些操作被允許、如何處理失敗）|

### 完整 Harness 的八大組件

1. 核心 LLM
2. 工具（互動介面）
3. 規劃循環（決定下一步行動）
4. Context engineering（管理資訊流）
5. 沙箱（安全執行環境）
6. 記憶系統（多層記憶）
7. Orchestration 層（協調操作）
8. Serving 層（連接用戶介面）

### Multi-Surface 架構

現代 harness 採用多介面架構，跨不同平台提供相同 Agent 功能：
- **OpenClaw**：透過中央化 Gateway 使用型別化 WebSocket 協定，同時服務 CLI、Web UI、桌面應用、訊息平台
- **Codex**：從終端工具演化為使用 JSON-RPC over stdin/stdout 的 App Server
- **OpenCode**：Bun JS HTTP server + Event Bus 即時廣播結果

多客戶端並行訊息挑戰：用 lane-aware FIFO queue 確保每個 session 只有一個活躍執行，同時允許不同 session 並行。

### 檔案系統是最基礎的 Harness Primitive

生產 harness 通常使用**檔案系統**作為主要狀態機制，而非花俏的向量資料庫。不同之處：
- Agent 循環非確定性執行
- Context 管理是一等關注點
- 循環中的「程式設計師」是 LLM 本身

Anthropic 長期執行 Agent 模式：初始化代理建立 script、進度檔、功能清單 → 每次 coding agent session 讀取 git log + 進度檔 → 無需資料庫或向量儲存，僅用檔案系統。

### Ralph Loops 機制

針對跨多個 context window 的任務，Claude Code 實作 **Ralph Loops**：攔截模型的退出嘗試 → 在乾淨 context window 重新注入原始 prompt → 使用檔案系統持久化狀態強制繼續向完成目標推進。

### 三層記憶架構

| 層次 | 類型 | 特性 |
|------|------|------|
| **檔案系統** | 長期記憶 | 跨 session 持久，儲存進度檔、git 歷史、session transcript |
| **RAM** | 短期/工作記憶 | 快速但揮發，持有對話歷史和工具結果 |
| **Context Window** | 模型所見 | 最嚴格的限制，決定模型對當前任務的了解 |

OpenClaw 強制不變量：記憶在從 context 丟棄前必定刷新到磁碟。Rehydration 是工具形狀的操作——agent 搜尋並檢索特定資料，而非把一切倒入 context window。

### 單代理 vs. 多代理

親身經驗教訓：**有記憶和智慧 context engineering 的單一優良 harness agent，往往優於多個專業化 agent**。建議永遠先以一個良好 harness 的 agent 開始，然後才考慮多代理複雜性。

### 誠實的局限性

- 記憶在長 session 中仍會中斷
- 驗證循環仍會遺漏邊緣情況
- 在共享代碼庫上協調數百個並行 Agent 仍是開放研究問題

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 8/10 | 3 層工程層級、Ralph Loops 機制、3 層記憶體架構可直接參照設計 |
| B. 創新性 | 8/10 | LLM-as-OS 比喻、Ralph Loops 命名、filesystem-as-foundation 視角原創 |
| C. 證據品質 | 7/10 | 多面架構描述豐富但缺乏量化實驗數據 |
| D. 技術深度 | 8/10 | 8 個組件、3 層記憶體、multi-surface 架構均有技術細節 |
| E. 泛化性 | 8/10 | LLM-as-OS 框架適用任何 agent 實作 |
| **加權總分** | **7.8/10** | 8×0.3+8×0.2+7×0.2+8×0.15+8×0.15 = 2.4+1.6+1.4+1.2+1.2 |

**整合決策**：Rule  
**整合位置**：`.claude/refs/harness-design.md`  
**整合狀態**：待實作
