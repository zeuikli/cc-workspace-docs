# Harness Engineering for Language Agents: The CAR Framework

**原始來源**：https://www.preprints.org/manuscript/202603.1756.v2  
**作者**：Chaoyue He 等 6 位（南洋理工大學）  
**發表日期**：2026-04-23  
**評分日期**：2026-05-05

---

## 繁體中文全文摘要

### 核心命題

Language Agent 的可靠性不是來自基礎模型品質或提示詞技術，而是來自「**harness 層**」——決定哪些指令具有權威性、可用動作、狀態持久化方式、跨時間失敗管理的基礎設施。

> 「許多報告的 Agent 效能提升可能源於 harness 改進，而非純粹的模型能力提升。」

### CAR 分解框架

論文提出以 **Control（控制）、Agency（代理）、Runtime（執行環境）** 三層分析 harness 結構：

---

#### C — Control Layer（控制層）

**定義**：執行前編碼行為約束的持久性 artifacts

**典型範例**：
- Repository maps 和導航結構
- AGENTS.md 文件（指定 Agent 角色和能力）
- 架構規則和權限政策
- 工具描述和介面 schema
- 測試套件和驗證程序
- Linting 規則和靜態檢查

**關鍵屬性**：Control 是語言性的且持久的；它透過明確限制可允許動作的空間來塑造 Agent 行為。

**代表性系統**：SWE-agent 的 repository 介面控制、Anthropic 的 Agent 安全指引

---

#### A — Agency Layer（代理層）

**定義**：Agent 與系統互動的動作基底和介面

**典型範例**：
- 程式碼執行環境（沙箱化/非沙箱化）
- 瀏覽器自動化介面
- 工具 API 及其 schema
- Orchestrator-worker 通訊模式
- 審核者角色和核准工作流
- 具體的介面定義（如 ReAct 的動作 schema）

**關鍵屬性**：Agency 定義了可能動作的「形狀」。能存取 Python REPL 的 Agent 與只能做 web search 的 Agent 有根本不同的 Agency。

**代表性系統**：SWE-agent 的 CLI 介面、CoOp 的瀏覽器介面

---

#### R — Runtime Layer（執行環境層）

**定義**：在延伸執行過程中維持系統一致性的時間性治理結構

**典型範例**：
- Context 組裝和優化
- 記憶管理（工作記憶、情節記憶、語義記憶）
- 狀態持久化和 checkpointing
- 重試策略和回溯
- 核准工作流和預算執行
- Trace 收集和可觀測性

**關鍵屬性**：Runtime 是執行層。它決定 Agent 如何在管理有限資源（context、計算、時間）的情況下導航長期任務。

---

### Harness 敏感性：為什麼歸因重要

**已記錄的 harness 效能影響**：
- SWE-agent CLI 介面重新設計改善效能約 40%（無模型改變）
- OS-Symphony 從 code-based → NL harness 遷移大幅改變效能
- Meta-Harness 顯示發現的 harness 優化跨模型遷移

**當前問題**：論文通常只報告改善幅度，不說明來源（模型改進 vs. harness 重設計 vs. 任務特化）。

### 63 篇文獻審計的發現

**學術文獻**強調：介面設計和評估協議、Agent 效能指標、提示詞技術

**工程文件**（Anthropic、OpenAI）強調：執行環境控制和狀態管理、記憶架構、安全治理機制

**差距詮釋**：Harness engineering 在實踐中比在學術發表中更可見，代表其作為研究對象被嚴重低估。

### HarnessCard：透明度披露標準

**動機**：現行實踐模糊 harness 細節，使可重現性和比較困難。HarnessCard 提供輕量披露模板。

```
## HarnessCard

**模型**：Claude 3.5 Sonnet, temperature=0.7, max_tokens=2048

**Control**:
- 工具存取：檔案讀寫（限 /project/），CLI 執行（命令白名單）
- 安全政策：破壞性操作需核准
- 測試套件：commit 前 linting 強制執行

**Runtime**:
- 記憶：Session 歷史（最後 10K tokens）+ 持久筆記
- Context 策略：80% window 使用率時壓縮
- 重試預算：每個失敗動作 3 次嘗試

**Agency**:
- Shell：/bin/bash 加命令限制
- 文件系統：僅限專案目錄

**評估**:
- 指標：SWE-bench Verified（500 任務）的任務成功率
```

### 常見失敗模式（按 Agent 類型）

| Agent 類型 | 常見失敗 |
|-----------|---------|
| **Repository coding agents** | Context 漂移——session 時間增加時失去 repository 結構感知 |
| **Browser agents** | Verifier 過擬合——Agent 學會利用評估信號而非真正解決任務 |
| **Enterprise support agents** | 政策違反——在長對話中超越授權邊界 |

### 對 Workspace 的啟示

1. **CAR = cc-workspace 的 harness 解剖**：
   - **Control** = CLAUDE.md + rules/ + linter hooks + 工具描述
   - **Agency** = Sub-agent 類型 + MCP servers + tool 清單
   - **Runtime** = context-monitor + compact 觸發 + session 記憶

2. **HarnessCard 標準**：
   - cc-workspace 的每個 Skill 和 Agent 應包含 HarnessCard 格式的元資訊
   - 這正是 SKILL.md 格式的延伸方向

3. **Context 漂移是已知失敗模式**：context-monitor-table.md 的設計就是在對抗這個問題

4. **Harness 改進 = 模型升級的替代品**：SWE-agent +40% 的例子支持在選擇升級模型之前先審計 harness

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 8/10 | CAR 框架可直接用於 cc-workspace 的 harness 審計；HarnessCard 可成為 SKILL.md 的元資訊標準 |
| B. 創新性 | 8/10 | HarnessCard 披露標準和 CAR 三層分解是學術貢獻；可見性不對稱的論點有說服力 |
| C. 證據品質 | 7/10 | 63 篇文獻的描述性審計；有具體案例（SWE-agent +40%），但為引用而非直接實驗 |
| D. 技術深度 | 8/10 | CAR 三層詳細定義、HarnessCard 模板、三種 Agent 類型的失敗模式分析均完整 |
| E. 泛化性 | 9/10 | CAR 框架明確設計為跨 Agent 類型、跨任務領域的通用分析框架 |
| **加權總分** | **7.95/10** | 8×0.3 + 8×0.2 + 7×0.2 + 8×0.15 + 9×0.15 = 2.4+1.6+1.4+1.2+1.35 |

**整合決策**：Rule  
**整合位置**：`.claude/refs/harness-design.md`（CAR 框架作為主要分析工具）  
**整合狀態**：待實作

**TODO**：
- 在 harness-design.md 採用 CAR 作為頂層分析框架，取代或補充現有說明
- 在 SKILL.md 模板中加入 HarnessCard 元資訊區塊（Control、Agency、Runtime 三段各一行摘要）
- 在 context-monitor-table.md 加入「Context 漂移」的 CAR 解釋（Runtime 層失效的典型案例）
