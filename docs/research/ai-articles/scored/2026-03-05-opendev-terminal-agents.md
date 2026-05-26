---
url: "https://arxiv.org/html/2603.05344v1"
title: "Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering"
date: 2026-03-05
type: article
---

# Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering

**原始來源**：https://arxiv.org/html/2603.05344v1  
**作者**：Nghi D. Q. Bui（OpenDev）  
**發表日期**：2026-03-05  
**評分日期**：2026-05-05

---

## 繁體中文全文摘要

### 研究背景

OpenDev 是一個開源命令列 Agent，專為自主軟體工程任務設計。論文系統性地解決三大終端 Agent 挑戰：有限的 context window、防止破壞性操作、在不耗盡 prompt budget 的情況下擴充能力。

### 四層架構

```
┌─────────────────────────────────────┐
│   Entry & UI Layer（CLI / TUI / Web） │
├─────────────────────────────────────┤
│   Agent Core Layer（推理與協調）       │
├─────────────────────────────────────┤
│   Tool & Context Layers（執行與 CM） │
├─────────────────────────────────────┤
│   Persistence Layer（Session / Logs） │
└─────────────────────────────────────┘
```

Agent Core 包含：Planner（戰略規劃）、Executor（戰術執行）、Critic（自我評估）、Orchestrator（路由與 context 管理）。

### 五層安全架構（Defense in Depth）

| 層次 | 機制 | 範例 |
|------|------|------|
| **L1 Prompt** | 系統提示中明確禁止破壞性操作 | 「未經確認不得刪除文件」 |
| **L2 Schema** | 工具 schema 包含安全約束 | `rm` 只有 `--confirm` 版本可用 |
| **L3 Runtime** | 破壞性操作需明確核准 | 互動式 `[y/n]` 確認 |
| **L4 Tool** | 工具調用前驗證，結果後驗證 | 路徑驗證防目錄穿越攻擊 |
| **L5 Hooks** | 使用者定義的生命週期鉤子 | 自訂鉤子對照 protected-files 清單 |

**核心原則**：任何單一層次的失效都不能危害安全，必須繞過多個獨立層次才能觸發有害操作。

### Context 工程（核心設計）

#### 動態系統提示
取代靜態提示，根據當前狀態動態組裝：
```
當前任務：修復 auth 模組的記憶體洩漏
進度：8 個子任務中的第 3 個
可用工具：[shell, file_read, grep, valgrind]
Context Budget：60% 剩餘（60K / 100K tokens）
```

#### 工具結果最佳化
終端輸出通常冗長且重複，OpenDev 智慧壓縮：
- **截斷 + 保留結構**：保留前 10 行（目錄結構）+ 後 10 行（摘要）
- **移除 ANSI color codes**：token 數減少 10-20%
- **錯誤摘要化**：2000 行編譯輸出 → 5 個錯誤類型 + 首個錯誤詳情
- **去重**：緩存結果，只提供 delta

#### 雙記憶架構

| 記憶類型 | 位置 | 大小 | 壽命 |
|---------|------|------|------|
| **Working Memory** | in-prompt | 10-20K tokens | 當前 session |
| **Episodic Memory** | 持久儲存 | 持續增長 | 專案壽命 |

#### 自適應 Compaction（80% 閾值）
達到 context 閾值時：
1. 辨識關鍵資訊（目標、最近 10 步、當前狀態）
2. 壓縮歷史（早期行動摘要化，同類操作合併）
3. 保持因果連續性
4. 典型壓縮率：40-60%

#### Context-Aware 提醒
對抗指令降解（instruction degradation）：
- 安全提醒：觸發於危險操作之前
- 目標提醒：觸發於偏離目標行為
- 資源提醒：context 接近上限時
- 進度提醒：固定間隔

### 多模型架構

| 角色 | 典型模型 | Token Budget |
|------|---------|-------------|
| 正常執行 | Claude 3.5 Sonnet | 2000 |
| 深度思考 | Claude 3.5 Opus | 5000 |
| 自我批判 | Claude 3.5 Sonnet | 1000 |
| 視覺分析 | Claude 3.5 Sonnet | 3000 |
| 領域專家 | Claude 3.5 Opus | 5000 |

### 雙代理分離：Planner vs. Executor

**Planner**：戰略任務分解，每個主要任務階段執行一次，Token 2000-3000
**Executor**：戰術具體行動，每分鐘多次，Token 1500-2500

### 懶加載工具發現（Lazy Tool Discovery via MCP）

**問題**：列出所有工具 = 5000+ tokens（docker、k8s、terraform、ansible...）
**解決方案**：
- 基礎工具：[shell, file_read, file_write]（永遠可用）
- 按需加載：當 Agent 需要編譯 C++ 時，動態加載 [gcc, clang, make, cmake]
- 成本：約 500 tokens，只在需要時才載入

### 效能結果

- SWE-agent（基準）：41% on SWE-bench Verified
- OpenDev（本論文）：**48% on SWE-bench Verified**

### 對 Workspace 的啟示

1. **五層安全架構**：cc-workspace 的 pre-commit hook + production 二次確認機制對應 L1/L3，可進一步加入 schema-level 的工具限制
2. **動態系統提示**：context-monitor-table.md 的觸發機制與此一致，可借鑒「context budget reminder」納入提示詞
3. **Lazy Tool Loading**：MCP server 按需啟用的策略與 Skill 按需載入一致，減少 context 污染
4. **Planner/Executor 分離**：cc-workspace 的 parent Agent（規劃）+ sub-agent（執行）架構的理論驗證

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 8/10 | 五層安全、動態提示、lazy tool loading 均可直接對照 cc-workspace 機制 |
| B. 創新性 | 7/10 | Lazy MCP tool discovery 和 context-aware reminders 是新穎的系統設計 |
| C. 證據品質 | 7/10 | SWE-bench 量化結果（48% vs 41%），但論文本身描述性偏多，ablation 不足 |
| D. 技術深度 | 9/10 | 全面的架構文件：四層架構、五層安全、六階段 ReAct、雙記憶架構，均有詳細說明 |
| E. 泛化性 | 8/10 | 通用終端 Agent 設計模式，不限特定代碼庫或語言 |
| **加權總分** | **7.75/10** | 8×0.3 + 7×0.2 + 7×0.2 + 9×0.15 + 8×0.15 = 2.4+1.4+1.4+1.35+1.2 |

**整合決策**：Rule  
**整合位置**：`.claude/refs/harness-design.md`（五層安全、雙代理模式）  
**整合狀態**：待實作

**TODO**：
- 將五層安全架構概念加入 harness-design.md 的「安全層」段落
- 在 context-monitor-table.md 中加入 context budget reminder 機制（80% 觸發）
- 評估是否採用 Planner/Executor 明確分離的 sub-agent 結構替代當前 parent + sub 模式
