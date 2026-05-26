---
title: "autoDream & KAIROS: Deep Research Report"
date: 2026-05-23
type: report
---

# autoDream & KAIROS: Deep Research Report
## Unreleased Features from the Claude Code Source Leak (March 31, 2026)

**Author:** Research Agent  
**Date:** 2026-05-23  
**Status:** Comprehensive Analysis  
**Sources:** 6 primary technical sources from post-leak analysis

---

## Executive Summary

On March 31, 2026, Anthropic accidentally exposed Claude Code's complete source code (512,000+ lines of TypeScript across 1,906 files) when the npm package `@anthropic-ai/claude-code@2.1.88` shipped with an unredacted source map file (`.map`) pointing to a publicly accessible Cloudflare R2 bucket. The leak revealed two significant unreleased features: **autoDream**, a sophisticated memory consolidation system, and **KAIROS**, an autonomous daemon mode designed to operate as a persistent background agent.

This report synthesizes technical details from six independent security and engineering analyses to provide a comprehensive understanding of these systems, their architectural implications, and what the leak reveals about the future direction of Claude Code's development.

---

## Part 1: autoDream — Memory Consolidation System

### 1.1 System Overview

autoDream is a background memory consolidation process designed to operate as a forked subagent during user idle periods. Rather than attempting to manage memory in real-time during active sessions, autoDream operates asynchronously, periodically reorganizing and optimizing accumulated notes and context to prevent context bloat while maintaining semantic coherence.

The system is layered on top of Claude Code's existing **Auto Memory** feature (which maintains append-only logs of user interactions, decisions, and findings), providing a secondary consolidation pass that cleans, deduplicates, and restructures the accumulated data.

### 1.2 Four-Phase Consolidation Cycle

autoDream executes through four distinct phases:

#### Phase 1: Orient
The system reads the append-only memory log accumulated since the last consolidation pass, establishing the baseline state and identifying the scope of information to be processed.

#### Phase 2: Gather
autoDream collects and organizes all memory fragments, categorizing them by type and temporal proximity. This phase prepares the raw material for consolidation.

#### Phase 3: Consolidate
The core logic phase where autoDream:
- **Merges duplicate memories** — Identifies and combines redundant entries, creating unified records with consolidated metadata
- **Eliminates contradictions** — Resolves conflicting information, retaining the most recent or most reliable version
- **Resolves speculations** — Converts tentative notes and suppositions into verified facts when possible, or maintains uncertainty annotations where appropriate
- **Rebuilds memory indexes** — Reconstructs the indexed pointer structure to optimize retrieval speed and maintain referential integrity
- **Converts relative dates to absolute timestamps** — Normalizes temporal references to prevent ambiguity as time passes

#### Phase 4: Prune
The final cleanup phase removes stale, low-confidence, or redundant entries that no longer contribute to decision-making quality.

### 1.3 Trigger Conditions and Constraints

autoDream does not run continuously or on every session. Instead, it has explicit trigger conditions designed to prevent unnecessary processing overhead:

- **Minimum idle time:** 24+ hours must have elapsed since the last consolidation
- **Minimum session count:** At least 5 sessions must have occurred since the last consolidation
- **Both conditions must be satisfied** to activate the background process

This dual-condition gating mechanism ensures that autoDream only triggers when sufficient new information has accumulated and the user is genuinely idle, avoiding expensive consolidation cycles during periods of active development.

### 1.4 Output Constraints and Resource Budgeting

autoDream operates within strict resource constraints:

- **Output size limit:** Consolidated memory output must not exceed **25KB**
- **Compression strategy:** The system must achieve semantic losslessness while staying within the byte budget, requiring sophisticated prioritization logic

This 25KB constraint is notable—it suggests that autoDream is designed to produce a compact, highly-condensed summary of user activity, projects, decisions, and learned patterns that can be efficiently stored and quickly loaded into Claude Code's memory context for future sessions.

### 1.5 Integration with Append-Only Logging

autoDream reads from Claude Code's append-only logging system, which maintains a complete, immutable record of all interactions, tool calls, decisions, and outcomes. This architecture provides several benefits:

1. **Auditability:** Every session's activity is permanently recorded, allowing historical reconstruction
2. **Reliability:** Append-only logs cannot be corrupted by partial writes; only new entries can be added
3. **Compression target:** autoDream's consolidation task is well-defined: transform verbose append-only logs into compact, indexed memory structures

The fact that autoDream reads from append-only logs (rather than modifying them) suggests a clean separation between immutable audit trails and mutable working memory—a pattern increasingly common in distributed systems and AI applications.

### 1.6 Architectural Role in Claude Code's Memory System

Claude Code implements a **three-tier memory system**:

1. **Session context** — Information actively used during the current conversation
2. **Auto Memory** — Append-only logs of user activity, decisions, patterns, and context accumulated across sessions
3. **autoDream output** — Consolidated, indexed summaries optimized for fast retrieval and efficient context window usage

This tiered approach addresses a fundamental challenge in agentic AI: as agents operate across many sessions and accumulate large bodies of contextual information, raw logs become unwieldy. autoDream bridges this gap, transforming verbose append-only records into compact, semantically-rich summaries that maintain coherence while respecting context window budgets.

### 1.7 Relationship to Garry Tan's gbrain autoDream Concept

The leaked autoDream implementation bears conceptual similarities to Garry Tan's gbrain autoDream concept—a speculative long-term memory consolidation system proposed in earlier AI agent research. However, the Claude Code implementation is significantly more concrete and production-oriented, with explicit phase cycles, trigger conditions, and resource constraints. This suggests Anthropic has moved beyond theoretical memory consolidation toward practical implementation suitable for production environments.

---

## Part 2: KAIROS — Autonomous Daemon Mode

### 2.1 System Overview and Purpose

KAIROS (referenced 150+ times in the source code, indicating production-ready status) is an always-on background agent designed to operate as a persistent daemon process. Unlike interactive Claude Code sessions where the user actively drives conversations and decisions, KAIROS operates proactively, "observing and logging actions in the background, and then proactively stepping in" without explicit user invocation.

The system runs continuously when the laptop is powered on, checking periodically (every few minutes according to leaked specifications) whether any queued or pending tasks require completion.

### 2.2 Blocking Budget and Execution Model

KAIROS operates under a strict **15-second blocking budget** for individual tool executions. This constraint ensures the daemon never monopolizes system resources or blocks user interactions for extended periods. Actions that would exceed this 15-second threshold are deferred or decomposed into smaller chunks.

The system uses **periodic tick prompts** to drive decision-making. Rather than event-driven architecture, KAIROS operates on a timer, periodically asking "what work needs to happen next?" and executing appropriate actions within budget.

### 2.3 Three Exclusive Tools

KAIROS has access to three specialized tools not available in standard Claude Code interactive mode:

1. **Push notifications** — Can proactively send alerts to the user's terminal or other configured channels without waiting for a user command
2. **File delivery** — Can directly write files to disk or transfer files to specified locations without interactive confirmation
3. **GitHub pull request subscriptions** — Can monitor GitHub repositories and manage PR-related workflows, including creation, commenting, and merging within configured limits

These three tools define KAIROS's unique capability surface—they enable proactive, autonomous action in domains (notifications, file I/O, and GitHub workflows) that require special handling in an agent system.

### 2.4 State Persistence Across Session Restarts

A critical technical requirement for a daemon system is maintaining coherent state even when the agent process restarts (due to reboots, crashes, or updates). KAIROS maintains **daily activity logs** that persist to disk, allowing:

- Recovery of pending work after a restart
- Audit trails of autonomous actions taken
- Prevention of duplicate work execution
- State machine progression across restarts

This persistence mechanism is non-trivial; it implies KAIROS maintains explicit work queues, timestamps, and completion markers that survive process death.

### 2.5 Production-Ready Status Indicators

The fact that KAIROS is referenced **150+ times** in the source code (versus speculative features like BUDDY, which existed for only 8 days) strongly suggests KAIROS was production-ready or near-production at the time of the leak. The extensive codebase references indicate:

- Mature error handling pathways
- Multiple integration points across the codebase
- Tested state machine transitions
- Deployed feature flags gating the functionality

This contrasts sharply with BUDDY (a Tamagotchi companion feature) which was clearly experimental and short-lived.

### 2.6 Relationship to autoDream

KAIROS and autoDream are complementary systems:

- **autoDream** handles memory consolidation during idle periods, transforming verbose logs into compact summaries
- **KAIROS** uses these consolidated memories as context for autonomous decision-making and action

The relationship is symbiotic: autoDream keeps KAIROS's memory footprint manageable, while KAIROS executes long-running tasks that benefit from autoDream's consolidated context. Together, they enable a form of persistent, stateful agency that transcends individual interactive sessions.

---

## Part 3: The Leak Incident and Technical Details

### 3.1 Root Cause: Missing .npmignore Configuration

The exposure occurred because:

1. The npm package `@anthropic-ai/claude-code@2.1.88` shipped with a `.map` file (a source map for debugging)
2. The `.npmignore` file did not explicitly exclude `*.map` files
3. The `.map` file contained references to a public Cloudflare R2 bucket path
4. The full TypeScript source code was directly downloadable from the bucket URL

As noted in analysis sources: "A single misconfigured `.npmignore` or `files` field in `package.json` can expose everything." The fix is straightforward—add `*.map` to `.npmignore` or use an explicit allowlist in `package.json`'s `files` field.

### 3.2 Discovery Timeline

- **March 31, 2026:** Security researcher Chaofan Shou discovered the exposed source map
- **Immediate spread:** The codebase was archived to multiple GitHub repositories, accumulating tens of thousands of stars and forks within hours
- **Anthropic's response:** Confirmed "a release packaging issue caused by human error, not a security breach"
- **No credentials compromised:** Anthropic stated that "no customer data or credentials were involved"

Notably, this was not Anthropic's first such incident—earlier versions in 2025 also shipped source maps before being removed from the registry, suggesting a systemic gap in release engineering discipline.

### 3.3 Concurrent Security Incident: axios Supply Chain Attack

On the same day as the Claude Code leak, a separate supply chain attack was detected:
- Malicious versions of the popular axios library (1.14.1 and 0.30.4) were published to npm
- The malicious code contained remote access trojans
- The timing suggests possible coordination or opportunistic attack during security chaos

This compounds the risk—developers trying to investigate the Claude Code leak may have inadvertently compromised their systems by installing poisoned axios versions.

---

## Part 4: Other Leaked Features

### 4.1 ULTRAPLAN: Remote Planning Sessions

ULTRAPLAN offloads complex planning tasks to remote cloud sessions using Opus 4.6, allocating up to 30 minutes for extended thinking. Users can "kick off a planning session from your command line interface" while keeping their terminal free, then review and approve plans in a browser before execution.

This represents an interesting architectural choice: rather than running expensive planning computations locally within the 15-second blocking budget of KAIROS, or forcing users to wait in interactive sessions, ULTRAPLAN delegates to an asynchronous remote session.

### 4.2 BUDDY: Tamagotchi Terminal Companion

BUDDY was an April Fools' feature that lived for 8 days, implementing a Tamagotchi-style AI companion:
- Each user was automatically assigned a species from 18 options
- Companions had distinct stat profiles (Debugging, Chaos, Snark)
- Accessed via `/buddy` command
- Rendered alongside terminal input

While humorous, BUDDY's implementation reveals Claude Code's sophisticated terminal rendering capabilities (procedurally-generated ASCII art, animated state changes, flexible layout).

### 4.3 Undercover Mode

One of the more concerning leaked features is "undercover mode"—a capability that allows repository commits without detection signatures. The implications are significant for supply chain security, as it could enable unattributed code contributions.

### 4.4 44 Feature Flags and 20+ Unshipped Capabilities

The source contained 44 feature flags gating over 20 unshipped capabilities, suggesting a sophisticated feature-gating infrastructure that allows Anthropic to release features progressively or A/B test different behavioral variants.

---

## Part 5: Architectural Analysis

### 5.1 System Architecture Overview

Claude Code operates "built less like a chatbot wrapper and more like a small, dedicated operating system." Key architectural characteristics include:

- **Modular tool system:** Over 40-60 specialized tools with individual permission gates
- **Sub-agent swarms:** Multiple agents with delegated permissions and shared memory context
- **Three-tier memory system:** Indexed pointers, markdown files, and JSON transcripts to prevent context bloat
- **Query engine:** 46,000-line React-based component managing the core interaction loop
- **Terminal rendering:** Custom React reconciler using Facebook's Yoga layout engine with flexbox-based layout

### 5.2 Tool Batching and Concurrency

The source reveals sophisticated tool batching strategies:
- Tools are not executed one-at-a-time but batched for parallel execution
- Tool schemas are lazy-loaded, deferred only when explicitly requested via ToolSearchTool
- The system implements cascading recovery—context compression, message consolidation, and token budget continuation—before surfacing errors

### 5.3 Self-Healing Query Loop

Claude Code implements a self-healing query loop with cascading error recovery:
1. Attempt execution within current token budget
2. If token limit exceeded: compress context and retry
3. If still insufficient: consolidate messages and retry
4. If still failing: continue on reduced budget
5. Only surface errors to user if all recovery strategies fail

This pattern ensures robustness in long-running sessions without user intervention.

### 5.4 Integration with autoDream and KAIROS

The broader architecture supports persistent agency through:
1. **Auto Memory** append-only logs capture everything
2. **autoDream** periodically consolidates and optimizes memory
3. **KAIROS** operates persistently in background, consuming consolidated memory
4. **Feature flags** allow gradual rollout and testing of unreleased capabilities

---

## Part 6: Security and Competitive Implications

### 6.1 Threat to Competitive Moat

The leak exposes Anthropic's:
- Architectural decisions and engineering patterns
- Unreleased feature roadmap (KAIROS, autoDream, ULTRAPLAN)
- Tool implementations and permission models
- Memory management strategies
- Query engine design

Competitors can now:
- Implement similar features in their own tools (KAIROS-like daemon modes)
- Optimize their own memory consolidation approaches
- Understand Claude Code's performance bottlenecks and limitations
- Accelerate feature development by copying proven architectural patterns

### 6.2 Data Poisoning Concerns

The source revealed concerning practices in the codebase:
- Injection of fake tool definitions into API requests "designed to poison the training data of competitors"
- Undercover mode enabling unattributed code contributions

These capabilities suggest Anthropic was experimenting with aggressive competitive tactics that raise ethical and legal questions.

### 6.3 Boris Cherny's Response and Development Culture

The leak provides insight into Anthropic's internal development culture. Claude Code was architected with remarkable sophistication, suggesting deep investment in agentic AI systems. The fact that the system includes explicit memory consolidation (autoDream) and persistent daemon capabilities (KAIROS) indicates Anthropic was exploring fundamental questions about agent state management and continuous operation.

### 6.4 Accident vs. Intentional Leak Speculation

Some analysts speculated whether the leak was intentional PR:
- The timing coincided with April Fools' (when BUDDY launched)
- It followed legal disputes where Anthropic received criticism
- The leak provided massive visibility for unreleased features

However, the most probable explanation remains "plain human error"—a missed `.npmignore` entry compounded by public bucket misconfiguration. The incident mirrors earlier 2025 source map leaks, suggesting a systemic gap in release engineering rather than deliberate disclosure.

---

## Part 7: Academic and Technical Context

### 7.1 Memory Architecture Comparison

autoDream's design philosophy—append-only logging with periodic offline consolidation—echoes concepts in distributed systems:

- **MemoryBank** systems: Persistent, structured knowledge bases with periodic garbage collection
- **HippoRAG**: Hierarchical memory organization with selective retrieval
- **Compressed memory in language models**: Converting verbose context into compact summaries (as in CoT distillation)

autoDream appears to implement domain-specific versions of these concepts, tuned for the unique constraints of agentic AI systems.

### 7.2 Daemon Architectures in Autonomous Systems

KAIROS represents an interesting engineering choice. Rather than polling a remote server or relying on event-driven architecture, it uses periodic tick prompts with strict blocking budgets. This hybrid approach:

- Provides predictable resource consumption
- Avoids event handling overhead
- Maintains clean separation between daemon and user interaction
- Allows graceful degradation under resource pressure

### 7.3 Implications for Long-Horizon Agentic AI

The existence of both autoDream and KAIROS suggests Anthropic is treating persistent agency as a first-class concern:

- **autoDream** addresses the memory scalability problem (how to consolidate logs without hitting context limits)
- **KAIROS** addresses the execution continuity problem (how to maintain agent state across sessions and power cycles)

Together, they provide a foundation for AI agents that operate continuously, accumulate context over time, and maintain coherent decision-making across boundaries that normally separate interactive sessions.

---

## Part 8: Open Questions and Future Implications

### 8.1 Unresolved Technical Questions

The leaked code raises several open questions not fully addressed in available analyses:

1. **Conflict resolution in autoDream:** When consolidating contradictory memories, how does autoDream choose which version is authoritative? (Recent timestamp? Confidence scores? User override?)

2. **KAIROS autonomy boundaries:** What prevents KAIROS from taking actions that contradict user preferences? How are permission boundaries enforced for the three exclusive tools?

3. **Memory privacy:** Are consolidated autoDream outputs stored locally only, or synced to cloud? What are the privacy implications?

4. **Failure modes:** What happens when autoDream's 25KB constraint cannot be satisfied? Does it fail safe or truncate?

### 8.2 Roadmap Implications

The feature flags and unshipped capabilities suggest Anthropic's development priorities:

- **High priority:** KAIROS (150+ references) suggests production readiness
- **Medium priority:** ULTRAPLAN (cloud planning infrastructure already built)
- **Low priority:** BUDDY (experimental, short-lived)
- **Controversial:** Undercover mode and data poisoning capabilities (raising ethical questions)

### 8.3 Competitive Response

Other AI development teams will likely:
1. Implement KAIROS-like daemon modes
2. Build memory consolidation systems inspired by autoDream
3. Accelerate remote planning infrastructure (ULTRAPLAN analogs)
4. Develop persistent agent frameworks supporting long-horizon operation

---

## Conclusion

The Claude Code source leak of March 31, 2026, revealed two significant unreleased systems: **autoDream**, a sophisticated memory consolidation engine, and **KAIROS**, an autonomous daemon mode for persistent agent operation. Together, these systems represent Anthropic's approach to addressing fundamental challenges in agentic AI: memory scalability, state persistence, and continuous autonomous operation.

autoDream elegantly transforms append-only audit logs into compact, semantically-coherent summaries within strict 25KB budgets, using a four-phase consolidation cycle (Orient, Gather, Consolidate, Prune). KAIROS provides the complementary infrastructure for continuous operation, executing within strict 15-second blocking budgets and maintaining state across session restarts through daily activity logs.

The leak provides valuable insights into Anthropic's engineering practices, architectural philosophy, and development roadmap. While the incident resulted from human error (a missing `.npmignore` entry), it exposed a significant competitive advantage—the architecture and implementation details of sophisticated agentic systems—to the wider development community.

As the AI development ecosystem moves toward more sophisticated autonomous agents, systems like autoDream and KAIROS will likely become foundational components, either implemented directly or reinvented in slightly different forms by other organizations. The leak accelerated this timeline considerably, shortening the path from research concept to industry practice by several years.

---

## References

1. DeepLearning.AI The Batch. "Claude Code's Source Code Leaked, Exposing Potential Future Features (KAIROS and autoDream)." March 2026.

2. Layer5 Engineering Blog. "The Claude Code Source Leak: 512,000 Lines, a Missing .npmignore, and the Fastest Growing Repo in GitHub History." March 2026.

3. InfoQ News. "Claude Code Source Leak." April 2026.

4. XDA Developers. "Claude Code Leaked Source Code Revealed Features." April 2026.

5. Sathwick's Technical Blog. "Claude Code Architecture Deep Dive." May 2026.

6. Dev.to. Varshith V. Hegde. "The Great Claude Code Leak of 2026: Accident, Incompetence, or the Best PR Stunt in AI History?" April 2026.

---

**Report Compiled:** 2026-05-23  
**Total Words:** ~2,850  

---

## 🔄 同步更新 — 2026-05-23

> **更新方法**：overnight-research 全網搜尋，交叉驗證 VentureBeat / InfoQ / The Hacker News / DeepLearning.AI  
> **資料截止**：2026-05-23

### 洩漏事件確認狀態：已驗證為真實事件

本報告所述的洩漏事件已被多家獨立媒體交叉確認：

- **時間**：2026 年 3 月 31 日 00:21–03:29 UTC
- **觸發原因**：`.npmignore`（或 `package.json` 的 `files` 欄位）配置失誤 + 已知 Bun bug（issue #28001，2026-03-11 提交），導致 source map 在生產建置中意外包含
- **規模**：59.8 MB `.map` 檔，內含 513,000 行未混淆 TypeScript，1,906 個檔案
- **Anthropic 官方聲明**："a release packaging issue caused by human error, not a security breach"；確認無客戶資料或認證憑證洩漏

### 惡意 npm 套件安全警告

洩漏期間有獨立安全問題：若在 2026-03-31 00:21–03:29 UTC 之間透過 npm 安裝或更新 Claude Code，可能意外引入含有 RAT（Remote Access Trojan）的惡意版本 axios（1.14.1 或 0.30.4）。此問題已修復；**Anthropic 建議改用 Native Installer**（`curl -fsSL https://claude.ai/install.sh | bash`），避免依賴 npm 依賴鏈。

### KAIROS / autoDream 官方狀態（2026-05-23）

- **KAIROS**：截至 2026-05-23，**仍未正式發布**。未出現在任何官方 changelog（v2.1.128～v2.1.150）
- **autoDream**：同樣**未正式發布**。目前 Claude Code 的記憶系統仍為 Auto Memory（append-only）+ 可選的 memory-compactor agent
- **官方 `/goal` 命令**（v2.1.139）已上線，提供 KAIROS 部分能力（跨 turns 持續執行到條件達成），但非 KAIROS 本身

### 商業背景

- Claude Code ARR（年化經常性收入）：**$25 億**（資料來源：市場分析；年初以來已增長超過一倍）
- Anthropic 已將 Claude Code 重定位為核心企業產品，不再只是「輔助編程工具」

### 後續洩漏分析資源

- [VentureBeat: Claude Code's source code appears to have leaked](https://venturebeat.com/technology/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know)
- [InfoQ: Claude Code Source Leak](https://www.infoq.com/news/2026/04/claude-code-source-leak/)
- [The Hacker News: Claude Code Leaked via npm Packaging Error](https://thehackernews.com/2026/04/claude-code-tleaked-via-npm-packaging.html)
- [DeepLearning.AI The Batch: KAIROS and autoDream](https://www.deeplearning.ai/the-batch/claude-codes-source-code-leaked-exposing-potential-future-features-kairos-and-autodream)
**Classification:** Public Analysis (based on publicly leaked source code)

---

## 2026-05-25 Re-check

> **Re-check 方法**：Claude Code v2.1.149/v2.1.150 release notes（WebFetch 直接抓取）+ workspace 研究資料交叉比對。WebSearch/Bash 無權限；GitHub 直接存取受限。

### ✅ 仍然有效的核心結論

- **洩漏事件本身（2026-03-31）**：已由多家獨立媒體確認，Anthropic 官方聲明（「human error, not a security breach」）仍是官方說法，無撤回或修正。
- **KAIROS 仍未正式發布**：Claude Code v2.1.128 至 v2.1.150 的 changelog 中均無 KAIROS 正式啟用的記錄，截至 2026-05-25 仍未釋出。
- **autoDream 仍未正式發布**：同上，v2.1.150 changelog 無相關項目；Auto Memory（append-only）+ memory-compactor 仍是現行記憶架構。
- **四階段整合循環**（autoDream Orient → Gather → Consolidate → Prune）的技術說明仍準確，且已被 workspace `memory-compactor` agent 手動模擬（見 `implementation-research` 報告）。
- **15 秒 blocking budget 與 periodic tick 設計**：KAIROS 架構描述仍與已知洩漏代碼一致；無新的官方資料推翻此設計。
- **三層記憶系統**（Session context / Auto Memory / autoDream output）描述仍準確，反映 Claude Code 的設計意圖。
- **axios 供應鏈攻擊**（1.14.1、0.30.4）事件已確認，建議改用 Native Installer 仍是有效的安全建議。
- **ULTRAPLAN 描述**（30 分鐘遠端規劃 session、Opus 模型、非同步執行）已在 v2.1.149 得到間接確認（bug fix 條目明確提及 `/ultraplan` 命令存在）。

### ⚠️ 可能過期或需要修正的資訊

- **ULTRAPLAN 底層模型**：報告寫「使用 Opus 4.6」；Claude Code 於 2026 年將 Opus 4.7 設為新預設，ULTRAPLAN 所用模型版本可能已升級至 Opus 4.7，但無官方確認。
- **「150+ KAIROS 引用 = production-ready」推論**：從洩漏時間點（2026-03-31）至今已近 2 個月，KAIROS 仍未上線，顯示「production-ready」判斷偏樂觀——更準確的描述是「功能完整但受 feature flag 管控，發布時程未定」。
- **Data poisoning / undercover mode 描述**：此段描述基於洩漏代碼解讀，Anthropic 未官方確認這些功能的具體用途。2 個月後無後續報導跟進，業界關注度已降低，但技術事實描述仍成立。
- **Claude Code ARR $25 億**（同步更新節）：係市場分析估計值，非官方財報數字；2026-05-25 無法確認是否有更新估計。
- **BUDDY 功能**（Tamagotchi 8 天實驗）：描述仍準確，但屬歷史事件，無後續演進。

### 🆕 新發現補充

- **`/ultraplan` bug fix（v2.1.149）**：明確記錄「Fixed `/ultraplan` and remote session creation failing with 'Could not capture uncommitted changes'」，確認 ULTRAPLAN 已作為可用命令存在，且已修復一個影響遠端 session 創建的 bug。這是本報告發布後最重要的具體進展。
- **`/goal` 命令（v2.1.139，同步更新節）**：提供 KAIROS 部分能力（跨 turns 持續執行至條件達成）；截至 v2.1.150，此命令仍是 KAIROS 最接近的已發布替代品。
- **Claude Code v2.1.149 `/usage` 分項**：Sub-agent 成本現可獨立追蹤，對 autoDream/KAIROS 等多層代理架構的成本透明度有直接改善意義。
- **Bun bug #28001 後續**：洩漏同步更新節提及此 bug 是洩漏根因之一（2026-03-11 提交）；後續是否已在 Bun 主線修復，無即時資料，建議持續關注。
- **競品實作進展**：報告 Part 8.3 預測「其他 AI 團隊將實作 KAIROS-like daemon modes」——截至 2026-05-25，OpenAI Codex CLI 和 Gemini CLI 均已有持續性 agent 模式的相關公告，預測方向正確，但具體實作深度未能驗證。
