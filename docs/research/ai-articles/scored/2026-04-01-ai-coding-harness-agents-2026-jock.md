> Source: https://thoughts.jock.pl/p/ai-coding-harness-agents-2026
> Fetched: 2026-05-08

# Claude Code vs Codex vs Aider vs OpenCode vs Pi 2026

## Overview

This comprehensive comparison examines AI coding harnesses—tools that enable autonomous code execution without direct human supervision. The author, Pawel Jozefiak, distinguishes between pair programming tools (which assist supervised development) and agent orchestrators (which operate autonomously).

## Key Distinction: Categories

The article emphasizes that not all "AI coding harnesses" serve the same purpose:

**Coding Tools** function as pair programmers requiring human direction at each step. Examples include Aider and Codex CLI, designed for incremental improvements rather than autonomous overnight execution.

**Agent Orchestrators** tackle goals independently across multiple files and decision points. Claude Code exemplifies this category, maintaining coherence across lengthy task chains without human intervention.

## The Harness Effect

A critical finding: harness quality matters as much as the underlying model. Research demonstrates identical models produce dramatically different results in different harnesses. One study showed "the same model inside different harnesses achieved 77% versus 93% performance" depending on implementation architecture rather than model capability.

## Tool Evaluations

### Claude Code
**Strengths:** Excels at complex multi-file tasks and overnight autonomous runs. Includes CLAUDE.md for project context persistence, Agent Teams functionality, and computer use capabilities.

**Limitations:** Context loss after 2-hour sessions; 3-4x higher token consumption than alternatives.

**Best for:** Architecture-level changes requiring consistent context across numerous steps.

### Codex CLI
**Strengths:** Exceptional at app development (iOS, macOS, web). Operates in cloud containers, enabling disconnected task execution.

**Limitations:** Struggles maintaining coherence across multi-step chains with dependencies.

**Best for:** Focused, contained coding tasks with clear specifications.

### Aider
**Strengths:** Open-source, 4.2x token efficiency advantage, git-first approach creating auditable commits, BYOM flexibility.

**Limitations:** Doesn't orchestrate across extensive file bases or coordinate sub-agents.

**Best for:** Budget-conscious setups and incremental refactoring with full audit trails.

### OpenCode
**Strengths:** Supports 75+ LLM providers with seamless switching, accommodating various backends from Anthropic to open-weight models.

**Limitations:** Lacks persistent project context and deep autonomous capabilities.

**Best for:** Model experimentation and teams with multiple provider subscriptions.

### Pi
**Strengths:** Primitives-first design offering full configuration control. RPC mode enables embedding within larger systems. Fast and flexible implementation.

**Limitations:** Anthropic doesn't permit Max subscription credits on third-party harnesses, requiring separate API billing for Claude access.

**Best for:** Custom harness architectures and systems where coding agents integrate as components (with GPT or open-weight models).

### Cursor
**Strengths:** Superior IDE experience with supervised agent mode. Design Mode for mockup-to-implementation workflows. Parallel agent tabs.

**Limitations:** Not designed for autonomous overnight execution; requires human supervision.

**Best for:** Developers present at the keyboard seeking integrated IDE-plus-agent functionality.

## Benchmark Context

**SWE-bench Pro** provides cleaner metrics than the contaminated original SWE-bench, with GPT-5.4-Codex leading at 56.8%.

**Terminal-Bench 2.0** better reflects agentic autonomous work, showing "Claude Code harness at 92.1% versus Codex CLI at 77.3%"—a more relevant signal for overnight tasks than standard code-editing scores.

## Decision Framework

Selection depends on specific workflow requirements:

- **Autonomous overnight execution:** Claude Code (infrastructure designed for this purpose)
- **App development:** Codex CLI with GPT-5.4
- **Budget constraints:** Aider with cheaper backends
- **Model flexibility:** OpenCode or Aider
- **Custom systems:** Pi (with GPT or open-weight models)
- **Supervised development:** Cursor

## Additional Tools Mentioned

- **Goose:** Open-source, MCP-based, general-purpose automation
- **Cline:** Multi-IDE support across VS Code, JetBrains, Neovim
- **Gemini CLI:** Free tier with generous limits (Google)
- **Devin:** Full autonomy with cloud sandbox at $20/month plus compute costs

## Conclusion

The author recommends Claude Code for autonomous execution, emphasizing that "harness tuning matters as much as model quality." The choice depends entirely on whether developers remain present, whether tasks require extensive chaining, budget constraints, and whether autonomy is essential.

---

## 繁體中文全文摘要

### 核心發現：Harness 品質與模型一樣重要

研究顯示：**相同模型在不同 harness 中達到 77% vs 93% 的效能**，差異完全來自實作架構而非模型能力。

### 兩大類工具的根本差異

| 類別 | 特性 | 代表工具 |
|------|------|---------|
| **Coding Tools（配對程式設計）** | 每步需要人工指示，增量式改進 | Aider、Codex CLI |
| **Agent Orchestrators（自主執行器）** | 跨多檔案獨立處理目標，無需人工監督 | Claude Code |

### 各工具詳細比較

**Claude Code**
- 優勢：複雜多檔案任務、夜間自主執行、CLAUDE.md 專案 context 持久化、Agent Teams 功能
- 限制：2 小時 session 後 context 丟失、token 消耗為其他工具的 3-4 倍
- 最適合：需要跨多步驟保持一致 context 的架構層面變更

**Codex CLI**
- 優勢：app 開發（iOS/macOS/Web）、雲端容器隔離執行（可離線）
- 限制：難以維持有依賴關係的多步驟鏈一致性
- 最適合：規格清楚的聚焦式程式任務

**Aider**
- 優勢：開源、4.2x token 效率優勢、git-first 方式建立可審計的 commit、BYOM 彈性
- 限制：不跨大型檔案庫編排，不協調子代理
- 最適合：預算敏感設定和需要完整審計軌跡的漸進式重構

**OpenCode**
- 優勢：支援 75+ LLM 供應商無縫切換
- 限制：缺乏持久專案 context 和深度自主能力
- 最適合：需要試驗多個模型供應商的團隊

**Pi**
- 優勢：primitives-first 設計、完整配置控制、RPC 模式可嵌入大型系統
- 限制：Anthropic 不允許 Max 訂閱積分用於第三方 harness，需額外 API 計費
- 最適合：客製化 harness 架構（搭配 GPT 或開源模型）

### Benchmark 比較

| Benchmark | 說明 | 結果 |
|-----------|------|------|
| **SWE-bench Pro** | 比被污染的原版更乾淨的指標 | GPT-5.4-Codex 領先 56.8% |
| **TerminalBench 2.0** | 更能反映 Agent 自主工作 | Claude Code 92.1% vs Codex CLI 77.3% |

TerminalBench 2.0 是夜間自主執行任務更相關的信號，比標準程式碼編輯分數更有意義。

### 決策框架

- 夜間自主執行 → **Claude Code**
- App 開發 → **Codex CLI + GPT-5.4**
- 預算限制 → **Aider + 較便宜的後端**
- 模型彈性 → **OpenCode 或 Aider**
- 自訂系統 → **Pi（搭配 GPT 或開源模型）**
- 人工監督開發 → **Cursor**

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 7/10 | 決策框架可直接用於工具選型；TerminalBench 2.0 補充 benchmark 視角 |
| B. 創新性 | 7/10 | 同模型不同 harness 77%→93% 提升是重要發現；工具分類方式新穎 |
| C. 證據品質 | 8/10 | TerminalBench 2.0 數據、多工具 benchmark 比較有具體數字 |
| D. 技術深度 | 7/10 | 每工具比較詳細但缺乏實作建議 |
| E. 泛化性 | 6/10 | 聚焦 AI coding 工具，領域特化程度較高 |
| **加權總分** | **7.05/10** | 7×0.3+7×0.2+8×0.2+7×0.15+6×0.15 = 2.1+1.4+1.6+1.05+0.9 |

**整合決策**：Rule  
**整合位置**：`.claude/refs/harness-design.md`（工具選型決策補充）  
**整合狀態**：待實作
