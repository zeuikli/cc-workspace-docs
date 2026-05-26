---
title: "Claude Code Harness: The Runtime Architecture That Turns an LLM into an Autonomous Agent (2026 Guide)"
date: 2026-03-01
type: article
---

> Source: https://pasqualepillitteri.it/en/news/1892/claude-code-harness-runtime-architecture-2026-guide
> Fetched: 2026-05-08

# Claude Code Harness: The Runtime Architecture That Turns an LLM into an Autonomous Agent (2026 Guide)

## Introduction

The claude-opus-4-7 model functions as a token generator in isolation. Everything enabling Claude Code to read files, execute shell commands, open pull requests, and maintain session preferences exists in a software layer surrounding the model called the **harness**. This runtime architecture transforms a language model into an autonomous coding agent capable of real-world actions.

## What an Agent Harness Is and Why the Model Alone Is Not Enough

According to Anthropic's official documentation, "Claude Code serves as the agentic harness around Claude: it provides the tools, context management, and execution environment that turn a language model into a capable coding agent."

The same model limited to text responses in claude.ai can modify source code, run tests, and commit changes when operating within Claude Code's harness. The distinction lies entirely in this surrounding framework rather than the model itself.

The typical Claude Code workflow follows three phases: gathering context, taking action, and verifying results. None of these phases executes within the model strictly speaking. The model determines what actions to take, while the harness handles file reading, command execution, permission checking, conversation storage, and networking.

## The Agent Loop: A Surprisingly Simple Core

The harness core consists of a straightforward iterative loop:

```python
# Main harness loop (simplified)
while needs_follow_up:
    history = gather_conversation_history()
    response = call_model(history, tools=available_tools)
    for tool_call in response.tool_calls:
        result = execute_tool(tool_call)
        history.append(result)
    needs_follow_up = response.stop_reason != "end_turn"
```

Claude Code's apparent intelligence derives from this tight iterative cycle around the model. The model cannot perceive the loop itself; it only sees accumulated conversation history, decides whether to invoke tools or return final text, and the harness manages everything else. Anthropic deliberately avoided complex planning systems, instead relying on simple tool-calling loops that terminate when the model declares completion.

## The Real Components of the Claude Code Runtime

Eight independent components comprise the Claude Code harness:

### 1. Tool Executor

This module transforms structured tool-use requests from the model into real actions. Native tools fall into five categories: file operations (Read, Write, Edit), search (Glob, Grep), execution (Bash with sandboxing), web (WebFetch, WebSearch), and code intelligence (definitions, references, compiler errors). Each execution ties to the original request through a call identifier, enabling the model to establish cause and effect.

### 2. Permission Manager

Before tool execution, the harness validates permissions through four modes: default (confirmation required for edits and commands), auto-accept edits (auto-approves file modifications), plan mode (read-only operations only), and auto mode (uses a background safety classifier on Sonnet 4.6 evaluating only user requests and tool calls, not model prose).

### 3. Hook System

Hooks are shell commands executed in response to lifecycle events. Documentation lists twelve hooks including SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, and Stop. Configuration through settings.json enables context injection, dangerous command blocking, audit trail logging, and external system integration.

### 4. Context Manager

The context window (tokens the model sees per call) has hardware limits: 200K in standard versions, 1M in some enterprise configurations. Management techniques include older tool output cleanup, automatic conversation compaction, prompt caching with five-minute TTL, lazy MCP schema loading, and skill snapshots. Anthropic recommends placing persistent rules in CLAUDE.md files when context fills.

### 5. MCP Layer

The Model Context Protocol enables adding third-party tools without recompilation. MCP servers define tools in JSON with descriptions and schemas. The harness acts as client, presenting tools as native ones to the model. To minimize token consumption, MCP schemas defer: the model sees only tool names until invoking specific tools, triggering full schema loading.

### 6. Skill System

Skills bundle markdown and scripts encapsulating domain knowledge. Each skill directory contains a SKILL.md file with YAML frontmatter and descriptions the model reads at session start. Full skill content loads only upon model invocation through dedicated tools, maintaining low token costs. Anthropic maintains an official skill repository with growing community contributions.

### 7. Subagent Framework

Subagents are model instances with separate context windows and configurable tool subsets, spawnable from the main model through the Agent tool. They parallelize independent work, isolate research-heavy tasks preventing main conversation saturation, and specialize on domains (frontend, security, debugging). Subagents receive initial prompts, run private loops, and return summary messages. Configuration uses Markdown files with frontmatter under `.claude/agents/` (project level) or `~/.claude/agents/` (user level).

### 8. Session Storage

Conversations save in JSONL format (one JSON object per line) under `~/.claude/projects/`. This design enables: resuming interrupted sessions with `claude --continue`, forking with `--fork-session` or `/branch` exploring alternatives, and rewinding individual edits through checkpoint snapshots taken before modifications. Pressing Escape twice triggers rewinding—a local mechanism separate from git covering only file edits, not remote system side effects.

## The Three Execution Environments

The Claude Code harness operates in three environments:

**Local:** Default mode. Code runs on your machine with full filesystem, terminal, and git access. Maximum freedom with maximum responsibility.

**Cloud:** Code executes on Anthropic-managed VMs. Useful for offloading lengthy tasks and working on non-local repositories. The harness remains identical; only the underlying filesystem changes.

**Remote Control:** Code runs locally, but browser-based harness control bridges web UI with local power.

## Settings.json: The Hierarchy That Rules Everything

Configuration follows a three-tier hierarchy that cascades: `~/.claude/settings.json` (global preferences), `<repo>/.claude/settings.json` (project level, committable), and `<repo>/.claude/settings.local.json` (private overrides, non-committable). More local settings override global ones. Main fields include: permissions (tool pattern allowlists/denylists), hooks (event-to-command mapping), env (environment variables), model (default override), and statusLine (custom CLI badge).

The CLAUDE.md file at project level receives special attention: the harness reads it at every startup and injects it into system prompts as stable instructions. Similarly, the auto-memory system preserves learnings between sessions within `~/.claude/projects/<repo>/memory/`.

## Comparison with Codex and Cursor

**OpenAI Codex** integrates harness components more tightly with model APIs; tool calling is native to model specifications rather than a separate layer. **Cursor** prioritizes IDE integration and maintains code indices for context retrieval instead of loading entire files. Claude Code emphasizes transparency with explicit approval gates for destructive operations. Codex reduces latency through harness-model coupling, while Cursor minimizes context bloat through retrieval-based approaches.

## Harness Security: The Real Differentiator

The primary harness risk involves the model executing injected instructions from external content—a threat called prompt injection. The harness implements immutable system prompt rules preventing destructive actions without user confirmation, isolating untrusted content, and filtering output for copyright and privacy concerns.

Anthropic invested significantly in this layer because code-executing agents on personal filesystems represent attractive attack vectors. The Apple case involving CLAUDE.md files in the Support app demonstrated how sensitive harness metadata can be. Enterprise direction emphasizes code scanning and patch suggestions through Claude Security.

## Frequently Asked Questions

### Can I use the Claude Code harness with another LLM?

No, not officially. The harness is designed for Anthropic's Claude API. Open source projects attempt model-agnostic abstractions but lack feature parity and Claude-specific optimizations like native prompt caching and deferred tools.

### What distinguishes Claude Code (CLI) from the Claude Agent SDK?

The SDK exposes the harness without the CLI. Both use identical primitives: agent loops, tool definitions, MCP clients, context management. The SDK enables custom agents within applications rather than terminal assistants, sharing the same underlying runtime.

### How many tokens does the harness consume beyond user prompts?

Between 10K and 50K tokens of system overhead. The system prompt uses several thousand tokens for safety rules, tool definitions, and base instructions. Additional consumption includes variable CLAUDE.md content, capped auto-memory (25KB), unexecuted skill descriptions, and initial git state dumps. The `/context` command shows real-time breakdowns.

### Does the harness work offline?

Only for local tools. Filesystem, Bash, Glob, and Grep operations run locally without network access. However, every loop iteration requires API calls for model decisions, preventing agent progression without connectivity. Experimental workarounds exist using local models through Ollama or vLLM with third-party harnesses, but official setups require connectivity.

### Can I write custom harnesses?

Yes. The Claude Agent SDK enables exactly this. Import the SDK in Python or TypeScript, configure desired tools, define system prompts, manage permissions, and build tailored harnesses for specific use cases. Enterprises adopt this pattern for legal review pipelines, code audits, and report generation.

## Conclusions

The harness represents the actual product design. The model functions as interchangeable infrastructure, while the harness determines agent safety, ergonomics, real-world costs, and productivity. Claude Code versus Codex versus Cursor comparisons fundamentally compare different harnesses, not models.

For maximum Claude Code value, configure settings.json and CLAUDE.md deliberately, write modular skills over monolithic prompts, and invest in hooks automating safety checks. Anthropic's product roadmap confirms this direction: reducing prompt engineering emphasis while increasing harness engineering focus.

---

## 繁體中文全文摘要

### 核心命題：Harness 才是真正的產品

claude-opus-4-7 模型本身只是 token 生成器。讓 Claude Code 能讀取檔案、執行 shell 命令、開 PR、維持 session 偏好的，是圍繞模型的軟體層——**harness**。

Claude Code 的智慧來自這個簡單的迭代循環：
```
gather history → call model → execute tools → append result → loop
```
模型感知不到循環本身，只看到累積的對話歷史。Anthropic 刻意避免複雜的規劃系統，仰賴簡單工具呼叫循環。

### 八大獨立組件

| 組件 | 職責 | 關鍵細節 |
|------|------|---------|
| **1. Tool Executor** | 將結構化工具請求轉為實際動作 | 5 類原生工具：檔案操作、搜尋、執行、網路、程式智能 |
| **2. Permission Manager** | 工具執行前驗證權限 | 4 模式：預設/自動接受編輯/Plan Mode/Auto（背景安全分類器）|
| **3. Hook System** | 生命週期事件觸發的 shell 命令 | 12 個 hooks：SessionStart、UserPromptSubmit、PreToolUse、PostToolUse、Stop 等 |
| **4. Context Manager** | 管理 context window 使用 | 200K（標準）/ 1M（部分企業）；舊輸出清理、自動 compaction、Prompt Caching（5 分鐘 TTL）|
| **5. MCP Layer** | 無需重新編譯即可加入第三方工具 | MCP 工具名稱延遲載入，只有被呼叫時才載入完整 schema |
| **6. Skill System** | 封裝領域知識的 Markdown + scripts | Session 開始時讀取 SKILL.md，完整內容僅在呼叫時載入 |
| **7. Subagent Framework** | 可獨立 context window 的子模型實例 | 並行獨立工作、隔離研究任務、領域專業化；`.claude/agents/` 配置 |
| **8. Session Storage** | JSONL 格式的對話持久化 | `~/.claude/projects/` 下；支援 `--continue`、`--fork-session`、Escape×2 回退 |

### Permission 四種模式

1. **預設**：編輯和命令需要確認
2. **自動接受編輯**：檔案修改自動核准
3. **Plan Mode**：僅唯讀操作
4. **Auto**：Sonnet 4.6 背景安全分類器（只評估用戶請求和工具呼叫，不評估模型散文）

### 三種執行環境

- **本機**：完整檔案系統、終端機、git 存取；最大自由也最大責任
- **雲端**：在 Anthropic 管理的 VM 上執行；適合卸載長時間任務
- **遠端控制**：本機執行但透過瀏覽器介面控制

### Settings 三層層級（優先序：本機 > 專案 > 全域）

```
~/.claude/settings.json           # 全域偏好
<repo>/.claude/settings.json      # 專案層級（可提交）
<repo>/.claude/settings.local.json # 私人覆蓋（不提交）
```

### Token 系統負擔

每次 session 的 harness 系統負擔：**10K–50K tokens**（安全規則、工具定義、基礎指令、CLAUDE.md 內容、auto-memory 上限 25KB、未執行 skill 描述、初始 git 狀態）。`/context` 指令顯示即時分解。

### 與 Codex/Cursor 比較

- **Codex**：harness 組件與模型 API 更緊密整合；工具呼叫原生於模型規格
- **Cursor**：優先 IDE 整合，用程式碼索引進行 context 檢索而非載入完整檔案
- **Claude Code**：強調透明度，破壞性操作有明確審批閘門

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 8/10 | 8 組件詳解、settings.json 三層層級、10K-50K token 負擔量化均可直接使用 |
| B. 創新性 | 8/10 | Deferred tools 機制、diff-based memory management、4 種 Permission 模式詳解 |
| C. 證據品質 | 8/10 | Token 系統負擔 10K-50K、session JSONL 格式、prompt caching 5 分鐘 TTL 等具體數字 |
| D. 技術深度 | 9/10 | 8 組件全部有程式碼/config 範例，FAQ 回答 5 個常見問題 |
| E. 泛化性 | 8/10 | Harness 架構知識跨 SDK 使用場景通用 |
| **加權總分** | **8.15/10** | 8×0.3+8×0.2+8×0.2+9×0.15+8×0.15 = 2.4+1.6+1.6+1.35+1.2 |

**整合決策**：Rule  
**整合位置**：`.claude/refs/harness-design.md`（Runtime 架構參考區段）  
**整合狀態**：待實作
