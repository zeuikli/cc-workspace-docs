---
title: "Agent Engineering: How the Harness Became the Product"
date: 2026-03-01
type: article
---

> Source: https://www.morphllm.com/agent-engineering
> Fetched: 2026-05-08

# Agent Engineering: How the Harness Became the Product

Agent engineering is the discipline of building the harness around an LLM that turns it into a reliable coding agent. IMPACT framework, harness patterns, test-first workflows, and lessons from Manus, Cursor, Claude Code, and OpenCode.

March 1, 2026 · 6 min read

## What Is Agent Engineering?

**Agent engineering** involves creating dependable systems surrounding language models. The field emerged from recognition that "LLM + tools + loop" oversimplifies what actually matters in production systems.

swyx introduced this terminology at the 2025 AI Engineer Summit, arguing that minimal agent definitions overlook memory, planning, and authority—the exact components distinguishing deployed agents from impressive demos.

Simon Willison characterizes agentic engineering more precisely: building software where coding agents can both generate and execute code. The execution component differentiates this from chat assistants. Agents write code, run it, observe errors, fix mistakes, and re-execute—no manual copying required.

Phil Schmid frames the shift from "better models" to "better harnesses" using hardware analogies. The model provides processing capability. The context window functions like RAM. The **harness operates as the operating system**, managing context selection, tool coordination, and providing essential infrastructure. The agent becomes the application layer. Organizations deploy operating systems to users, not CPUs.

### Why the harness is worth billions

Meta acquired Manus for approximately $2 billion in December 2025—not for the underlying model, but specifically for the harness infrastructure. Manus rebuilt their agent harness five times within six months, with each iteration enhancing reliability and task completion rates.

## The IMPACT Framework

swyx created the **IMPACT framework** because simplified definitions cause engineers to neglect components determining actual agent quality: planning, memory, and authority.

### Components

**Intent**: Goals communicated through multimodal interfaces and validated through evaluation systems. Agents require explicit success definitions before taking action.

**Memory**: Persistent memory across sessions creates continuity and enables improvement. This extends beyond conversation history to include skill libraries and reusable workflow templates.

**Planning**: Editable, sequential plans. Tools like Devin and Deep Research demonstrate that mid-execution plan modifications significantly improve outcomes compared to fixed approaches.

**Authority**: Frequently overlooked element representing human-agent trust. Permission frameworks, approval gates, and sandbox boundaries become critical.

**Control Flow**: Higher agency means the model increasingly determines execution paths. This distinguishes genuine agents from predetermined workflows.

**Tools**: Everyone acknowledges RAG, search, code execution, and browser automation. Disagreement centers on management approaches: static registration versus dynamic discovery versus logit masking.

OpenAI's official framework (TRIM) excludes Planning and Authority despite their importance in production environments.

## The Agent Loop

Every coding agent implements some version of the same fundamental loop. Princeton and Google's **ReAct (Reason + Act) pattern** from 2022 formalized the cycle: models alternate between generating reasoning traces and selecting actions.

```
while task_not_complete:
    # 1. READ — gather relevant context
    state = read_files() + read_test_output() + read_errors()
    context = harness.select_context(state, task)

    # 2. PLAN — decide what to do next
    plan = model.reason(context, task)

    # 3. ACT — execute via tools
    result = harness.dispatch_tool(plan.next_action)

    # 4. OBSERVE — check the outcome
    outcome = harness.evaluate(result)

    if outcome.needs_retry:
        context = harness.add_error_trace(outcome.error)
        continue

    if outcome.needs_human:
        harness.escalate(outcome)
        break

    harness.checkpoint(result)  # git commit, progress file
```

Differences between Claude Code, Cursor, Codex CLI, Cline, and Aider lie not in this loop's existence but in **how the harness executes each step**: context selection mechanisms, tool distribution methods, failure handling approaches, and stopping condition determination.

### The loop requires reliable feedback

Test suites, linters, and type checkers provide essential feedback. Addy Osmani emphasizes this directly: "You absolutely have to test what it writes." Agents accessing test suites progress rapidly through projects. Agents without testing frameworks generate hallucinated progress.

## Harness Engineering

Martin Fowler and Birgitta Boeckeler at ThoughtWorks define harness engineering as tooling and practices preventing AI agents from destabilizing large applications. Their framework includes three elements:

### Context Engineering

A continuously refined knowledge repository embedded in codebases, supplemented by dynamic sources like observability data and browser navigation systems for agent use.

### Architectural Constraints

Guardrails enforced through LLM agents and deterministic custom linters and structural tests monitoring code quality.

### Entropy Management

Periodic cleanup agents identifying documentation inconsistencies and architectural violations. Codebases degrade without active maintenance.

Anthropic's guidance for long-running agents addresses a specific challenge: agents spanning multiple context windows. Their pattern employs an **initializer agent** setting up the environment and a **coding agent** inheriting progress files and git logs for context understanding.

```
# Session 1: Initializer agent sets up the scaffold
harness.create("init.sh")           # environment setup script
harness.create("progress.json")     # structured feature list
harness.create("claude-progress.txt") # human-readable status
git commit -m "Initialize project scaffold"

# Session N: Coding agent picks up where it left off
progress = read("claude-progress.txt")
git_log = run("git log --oneline -10")
features = read("progress.json")

# Select highest-priority incomplete feature
next_feature = features.find(f => f.status == "incomplete")

# Implement ONE feature per session (prevents context exhaustion)
implement(next_feature)
run_tests()
update("claude-progress.txt")
git commit -m "Implement {next_feature.name}"
```

**Critical principle**: tackle one feature per context window session. Attempting excessive work within a single window causes mid-implementation context exhaustion. Clean commit states ensure production readiness before context limits are reached.

## Harness Patterns Across Tools

Each major coding agent has revealed harness implementation details, showing how different teams addressed the same core challenges:

| Component | Claude Code | Cursor | Manus | OpenCode |
|-----------|-------------|--------|-------|----------|
| Loop pattern | Initializer + coding agent | Model-specific harness | KV-cache-optimized ReAct | Server-client with LSP |
| Context strategy | CLAUDE.md + just-in-time retrieval | Repo indexing + reasoning trace preservation | Filesystem-as-context + todo.md recitation | Built-in LSP for immediate feedback |
| Tool management | MCP + lazy loading (95% context reduction) | Renamed tools per model + explicit dispatch | Logit masking via state machines | 75+ provider-agnostic tool layer |
| Error recovery | Git checkpoints + progress files | Reasoning trace alerting (30% drop if lost) | Error trace preservation in context | Approval-based execution gates |
| Multi-agent | Agent Teams via MCP | Subagent system for parallel tasks | Sub-agents for context isolation | Primary agents + subagents |
| Permission model | Configurable levels + hooks | Sandbox with filesystem/network boundaries | Sandboxed environment | Plan-first with approval gates |

### Cursor: Training the Harness Into the Model

Cursor uses an unconventional approach. Rather than training generic models and wrapping them, they trained their Composer model on **tool-use trajectories**: action sequences demonstrating tool usage timing. Each frontier model receives customized harness instructions and tool definitions, measured against internal evaluation suites.

A critical discovery: **removing reasoning traces from GPT-5-Codex caused a 30% performance decline.** Harnesses must maintain reasoning continuity across multi-turn interactions. Cursor implemented alerting to prevent accidental reasoning trace removal.

### Manus: Five Harnesses in Six Months

Manus prioritized in-context learning over fine-tuning, banking that context engineering enables faster iteration (hours versus weeks) while maintaining model independence. Production insights include:

* **Prioritize KV-cache hit rate.** Agent workloads feature approximately 100:1 prefill-to-decode ratios. Cache efficiency represents the single most critical production metric. Cached tokens cost approximately 10 times less than uncached tokens.

* **Apply tool masking rather than removal.** Dynamically modifying tool definitions invalidates KV-cache and confuses models about prior actions. Use logit masking and state machines for action constraint instead.

* **Leverage the filesystem as extended context.** Large observations overflow context windows. Offload to sandbox storage while preserving restorable references.

* **Recite objectives into context ends.** A todo.md file updated throughout execution maintains goal visibility in the model's recent attention. Without this, agents drift after roughly 50 tool calls.

* **Preserve error traces.** Keeping failed attempt messages helps models avoid repetition.

## Test-First & Spec-Driven Workflows

Two complementary practices emerged as most effective, both shifting work before agent code writing.

### Test-First Development

Simon Willison's red/green pattern: write failing tests, then let the agent make them pass. The agent observes test failure output, diagnoses issues, writes code, and re-runs tests. This tight loop produces superior code with minimal human intervention versus open-ended prompts.

```
# Step 1: Human writes the failing test
def test_token_refresh_handles_expiry():
    """When refresh token is expired, redirect to /login"""
    expired_token = create_expired_refresh_token()
    response = client.post("/api/refresh", token=expired_token)
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"

# Step 2: Run tests — they fail (red)
# FAILED test_token_refresh_handles_expiry - AssertionError

# Step 3: Tell the agent: "Make this test pass"
# Agent reads test, understands the contract, implements:

async def refresh_handler(request):
    try:
        new_token = await refresh(request.token)
        return JsonResponse({"token": new_token})
    except RefreshTokenExpired:
        return RedirectResponse("/login", status_code=302)

# Step 4: Tests pass (green). Commit.
```

### Spec-Driven Development

Addy Osmani's approach starts with a `spec.md` containing requirements, architectural decisions, and testing strategies. He characterizes this as "rapid waterfall": structured planning preventing agents from derailing. Key principles include:

* **Single function, single feature at a time.** LLMs produce "confused output" when given excessive scope simultaneously.
* **Commit after each chunk.** Commits provide rollback checkpoints.
* **Quality gates after each step.** Linters, type checkers, and test suites run post-implementation.
* **Cross-check with multiple models.** Different models have varying strengths.

Kiro from AWS formalizes spec-driven development into an IDE interface. The agent generates user stories with acceptance criteria, technical design documents, and task lists before implementing anything.

## Context Engineering in the Harness

Context engineering represents core competency within agent engineering. Every harness decision involves context: which tokens enter, timing, and ordering.

Anthropic defines it as "thinking in context: considering the holistic state available to the LLM at any given time and what potential behaviors that state might yield." The primary adversary is **context rot**: increasing token counts reduce model accuracy in recalling context information.

### Five Harness-Level Context Strategies

**CLAUDE.md / .cursorrules**: Project-level context files loaded into every session. Represents the minimum viable project context.

**Just-in-Time Retrieval**: Maintain lightweight references and load on demand. Never preload everything. Claude Code's MCP tool search achieves 95% context reduction.

**Compaction**: Summarize conversation history near context limits. Anthropic recommends combining with git commits and progress files.

**Sub-Agent Isolation**: Each sub-agent gets its own context window. Main agent stays clean for orchestration.

**Filesystem as Extended Context**: Write large observations to sandbox storage, maintaining only references in context. Prevents information loss from aggressive compaction while keeping active context lean.

## Multi-Agent Orchestration

Multi-agent orchestration addresses **harness engineering**, not model capabilities. Orchestrators coordinate specialized agents in parallel, each with dedicated context, then synthesize results. February 2026 witnessed every major tool shipping multi-agent support simultaneously.

| Tool | Architecture | Parallelism |
|------|--------------|-------------|
| Claude Code | Agent Teams via MCP | Specialized roles, message passing |
| Cursor | Subagent system | Discrete parallel subtasks from main agent |
| Windsurf | Cascade via git worktrees | 5 agents on 5 bugs simultaneously |
| Grok Build | Direct parallelism | 8 agents working simultaneously |
| Codex CLI | Agents SDK + worktrees | Parallel tasks across isolated branches |
| Devin | Parallel sandboxed sessions | Each Devin in its own cloud IDE |
| Cline CLI 2.0 | Parallel terminal agents | BYOM multi-agent for open source |

The fundamental advantage is **context isolation**. A single agent refactoring three modules simultaneously pollutes its context with unrelated details. Three parallel agents, each focused on one module, maintain clean context. The orchestrator needs only high-level status updates.

## Error Recovery & Permission Models

Harnesses define what occurs when problems arise. Reliable agents employ hierarchical recovery strategies rather than simple retries:

```
# Level 1: Retry with context
# Agent sees the error, adjusts approach, tries again
# Most errors resolve here (wrong file path, syntax error)

# Level 2: Rollback to checkpoint
# Agent reverts to last known good state via git
git reset --soft HEAD~1
# Re-attempt with different strategy

# Level 3: Decompose the task
# Break the failing task into smaller subtasks
# Delegate to sub-agents with focused context

# Level 4: Escalate to human
# Agent writes a clear summary of what it tried,
# what failed, and what it needs from the human
harness.escalate({
    attempted: ["approach_a", "approach_b"],
    errors: [error_trace_a, error_trace_b],
    suggested_next: "Need REDIS_URL env var to proceed"
})
```

### Permission Models

Authority components from IMPACT manifest through permission models. Tools make different safety-speed tradeoffs:

* **Cursor**: Sandbox-aware harness with explicit filesystem paths and network controls.
* **Claude Code**: Configurable permission levels with hooks enabling custom automation.
* **Cline**: Explicit approval for every file modification. Safe but slower.
* **Devin**: Complete sandboxed cloud environment. Agents can do anything within boundaries.

The key tension: requiring approvals for every action frustrates developers and eliminates flow states making agents valuable. Skipping approvals risks unintended modifications. Optimal harnesses provide granular control: auto-approve reads and tests, require approval for writes to sensitive paths, block destructive operations completely.

## The Apply Layer

Every harness encounters the same bottleneck: **applying edits to files**. LLMs generate edit intentions, but merging that intent into existing code breaks frequently. Diffs fail when context shifts. Search-and-replace operations miss relocated code. Full-file rewrites waste tokens and risk overwriting concurrent changes.

Cursor invested in training a custom model specifically for this operation. Manus optimizes for KV-cache efficiency making repeated applies fast. Claude Code uses specialized Fast Apply models for deterministic merges.

The apply step requires exactly three context pieces: the original file, the edit intention, and the update snippet. Insufficient context causes merge failure. Excessive context confuses the model.

```
import { OpenAI } from 'openai';

const morph = new OpenAI({
  apiKey: process.env.MORPH_API_KEY,
  baseURL: 'https://api.morphllm.com/v1'
});

// The harness sends exactly 3 pieces of context:
// 1. The instruction (what to change)
// 2. The original code (what exists)
// 3. The update snippet (the LLM's edit)
const result = await morph.chat.completions.create({
  model: 'morph-v3-fast',
  messages: [{
    role: 'user',
    content: `<instruction>Add retry with exponential backoff</instruction>
<code>${originalFile}</code>
<update>${agentEditSnippet}</update>`
  }],
  stream: true
});
// Returns: complete merged file, deterministically
```

Isolating the merge in a specialized model keeps the coding agent's primary context window clean for planning and reasoning. The apply layer handles reliability. The reasoning model handles intelligence.

## Frequently Asked Questions

### What is agent engineering?

Building reliable systems surrounding language models. It encompasses the harness managing tool coordination, context handling, error recovery, and permissions; the agent loop cycling through reasoning and action; and workflows enabling production deployment.

### What is the IMPACT framework?

Six essential components created by swyx: **Intent** (goals verified via evaluation), **Memory** (persistent coherence), **Planning** (editable sequential plans), **Authority** (permission frameworks), **Control Flow** (dynamic execution paths), **Tools** (external capabilities).

### What is an agent harness?

Non-LLM infrastructure wrapping models for long-running tasks. It manages tool coordination, context selection, permissions, error recovery, and state management. Meta's $2 billion Manus acquisition reflected harness value—Manus rebuilt it five times achieving progressive reliability improvements.

### What is harness engineering?

A discipline involving context engineering (managing model visibility), architectural constraints (guardrails and structural tests), and entropy management (periodic cleanup). Defined by Fowler and Boeckeler at ThoughtWorks.

### What is test-first development with coding agents?

Simon Willison's pattern: write failing tests, let agents make them pass. Agents observe failures, diagnose problems, implement solutions, and verify success. This creates tight feedback loops producing superior code versus open-ended specifications.

### How do multi-agent systems work for coding?

Orchestrators decompose work and delegate to specialized agents with **isolated context windows**. Each agent focuses narrowly without pollution from parallel tasks. Key benefit: context cleanliness through scope restriction per agent.

---

© 2026 AutoInfra, Inc. All rights reserved.

---

## 繁體中文全文摘要

### 核心命題：Harness 就是競爭力本身

Agent 工程不是「讓 LLM 更聰明」，而是「圍繞 LLM 建立可靠系統」。Phil Schmid 的類比精準：**模型是 CPU、Context Window 是 RAM、Harness 是作業系統、Agent 是應用程式**。組織部署的是作業系統，不是 CPU。

Meta 以約 20 億美元收購 Manus，購買的不是模型，而是 harness 基礎設施——Manus 在六個月內重建了五次 harness，每次迭代都提升了可靠性和任務完成率。

### IMPACT 框架：六大核心組件

swyx 創立 IMPACT 框架，填補簡化定義遺漏的關鍵組件：

| 組件 | 說明 |
|------|------|
| **Intent（意圖）** | 透過多模態介面傳達目標，並由評估系統驗證 |
| **Memory（記憶）** | 跨 session 的持久記憶，包含技能庫與工作流模板 |
| **Planning（規劃）** | 可編輯的循序計劃；執行中途修改顯著優於固定方法 |
| **Authority（授權）** | 人機信任框架：權限系統、審批閘門、沙箱邊界 |
| **Control Flow（控制流）** | 模型決定執行路徑的程度，區分真正 Agent 與預定義工作流 |
| **Tools（工具）** | RAG、搜尋、程式執行、瀏覽器自動化的管理策略 |

OpenAI 官方框架 TRIM 排除了 Planning 與 Authority，而這兩者在生產環境中至關重要。

### Agent 循環：ReAct 模式

所有 coding agent 都實作同一個基本循環（Princeton/Google 2022 年 ReAct 模式）：

```
while task_not_complete:
    state = READ → PLAN → ACT → OBSERVE
```

差異不在循環本身，而在 **harness 如何執行每一步**：context 選取機制、工具分配方式、錯誤處理策略、停止條件判斷。

測試套件、linter、型別檢查器提供關鍵回饋。沒有測試框架的 Agent 只會產生幻覺式進度。

### 主要工具的 Harness 差異

| 元件 | Claude Code | Cursor | Manus | OpenCode |
|------|-------------|--------|-------|----------|
| Context 策略 | CLAUDE.md + 即時載入 | Repo 索引 + 推理軌跡保留 | 檔案系統即 Context + todo.md 覆誦 | 內建 LSP 即時反饋 |
| 工具管理 | MCP + 延遲載入（95% context 減少）| 模型專屬重命名 | Logit masking via 狀態機 | 75+ 工具跨供應商層 |
| 錯誤恢復 | Git checkpoints + 進度檔 | 推理軌跡警報（丟失導致 30% 下降）| 錯誤軌跡保留在 context | 審批制執行閘門 |

**Cursor 關鍵發現**：從 GPT-5-Codex 移除推理軌跡導致 30% 效能下降；Harness 必須維持多輪推理連續性。

### 五大 Context 策略

1. **CLAUDE.md / .cursorrules**：每次 session 載入的最小專案 context
2. **即時載入（JIT Retrieval）**：輕量參照，按需載入；Claude Code MCP 實現 95% context 減少
3. **Compaction**：接近限制時摘要對話歷史
4. **Sub-Agent 隔離**：每個子代理獨立 context window，主代理保持乾淨
5. **檔案系統作為延伸 Context**：大型觀察值寫入沙箱儲存，只保留參照

### 工作流方法論

**Test-First（Simon Willison）**：先寫失敗測試，讓 Agent 讓測試通過。Agent 觀察失敗輸出→診斷→實作→重跑測試，緊密循環優於開放式提示。

**Spec-Driven（Addy Osmani）**：用 `spec.md` 包含需求、架構決策、測試策略。「一次一個功能、每塊提交、每步品質閘門、多模型交叉驗證」。

### 錯誤恢復四層架構

```
Level 1: 帶 context 重試（語法錯誤等）
Level 2: 回滾到 git checkpoint，換策略
Level 3: 分解任務，委派子代理
Level 4: 升級給人類（附嘗試記錄 + 建議下一步）
```

### Apply 層：專用合併模型

所有 harness 都面臨相同瓶頸：**將 LLM 生成的編輯意圖套用到現有檔案**。合併步驟需要恰好三個 context：原始檔案、編輯意圖、更新片段。不足導致合併失敗，過多使模型混亂。

Cursor 訓練了專用 Apply 模型；Manus 優化 KV-cache 效率；Claude Code 使用 Fast Apply 模型實現確定性合併。

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 8/10 | IMPACT 框架、4 層錯誤恢復、Test-First 工作流均可直接套用 |
| B. 創新性 | 8/10 | IMPACT 框架原創命名、Apply 層瓶頸分析、ReAct 迴圈視覺化 |
| C. 證據品質 | 8/10 | 多個 harness 比較表、Apply 模型機制說明、Manus/Cursor/Claude Code 實例 |
| D. 技術深度 | 9/10 | 程式碼層級 ReAct 範例、5 種 context 策略、4 層錯誤處理機制詳細說明 |
| E. 泛化性 | 8/10 | IMPACT 框架跨 agent 類型通用，不限於 Claude Code |
| **加權總分** | **8.15/10** | 8×0.3+8×0.2+8×0.2+9×0.15+8×0.15 = 2.4+1.6+1.6+1.35+1.2 |

**整合決策**：SKILL  
**整合位置**：`.claude/skills/harness-eval/` 或 `.claude/refs/harness-design.md`  
**整合狀態**：待實作
