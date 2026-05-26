---
url: "https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents"
title: "Skill Issue: Harness Engineering for Coding Agents"
date: 2026-03-12
type: article
---

# Skill Issue: Harness Engineering for Coding Agents

**原始來源**：https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents  
**作者**：Kyle（HumanLayer）  
**發表日期**：2026-03-12  
**評分日期**：2026-05-05

---

## 繁體中文全文摘要

### 核心命題

Coding Agent 的失敗主要是**配置問題，而非模型限制**。作者引入「harness engineering」——透過配置點（system prompts、tools、skills、sub-agents）來優化 Agent 的執行環境，而不是等待更好的模型。

> 「在把 Agent 失敗歸因於模型限制之前，先檢查 harness。」

### Harness Engineering 與 Context Engineering 的關係

Harness engineering 是 **context engineering 的子集**，核心問題是：
1. Agent 如何獲得新能力？
2. 不在訓練資料中的代碼庫知識如何教導 Agent？
3. 如何在提示詞指令之外增加確定性？
4. 如何防止 context window 快速膨脹？

### 五大配置點（Configuration Surfaces）

#### 1. CLAUDE.md / AGENTS.md 文件

- ETH Zurich 研究：LLM 生成的文件**損害**效能；精心撰寫的人工文件帶來適度提升（~4%）
- 最佳實踐：保持 **60 行以下**，使用**漸進式揭露（progressive disclosure）**

#### 2. MCP Servers（工具擴展）

- 工具描述消耗系統提示 token
- 過多工具**降低**效能
- 對有良好文件的工具，直接 CLI 使用往往優於 MCP Server
- **原則**：只啟用需要的 Server

#### 3. Skills（可重用知識模組）

漸進式揭露的核心機制——Agent 只在需要時取用能力：
- 打包指令、markdown 文件、CLI/執行檔參考
- 採用前需安全審查

#### 4. Sub-Agents（隔離 Context）

| 優勢 | 說明 |
|------|------|
| **Context 防火牆** | 防止中間噪音在父執行緒累積 |
| **一致性** | 長期多 session 項目保持聚焦 |
| **成本優化** | 按任務選擇模型（Haiku 研究、Sonnet 實作）|
| **避免 Context Rot** | Chroma 研究記錄的問題 |

最適用場景：代碼庫探索、模式分析、資訊研究。

#### 5. Hooks（事件驅動腳本）

- 執行驗證檢查（typecheck、formatting）
- 管理核准與拒絕
- 建立通知與整合
- 在 session 中途浮現 build/type 錯誤

### 反向壓力機制（Back-Pressure）

驗證系統讓 Agent 能驗證自己的工作：
- Type checking 和 builds
- 單元測試和整合測試
- 程式碼覆蓋率回報
- UI 互動測試

**關鍵原則**：只浮現**錯誤**，保持成功輸出靜默 — 保護 context window 效率。

### 什麼有效 vs. 什麼無效

| 有效 | 無效 |
|------|------|
| 從簡單開始；只在遇到真實失敗後才加配置 | 在看到真實失敗之前預先設計理想配置 |
| 把經過測試的配置發佈給整個團隊 | 「以防萬一」安裝 skill/server |
| 優化迭代速度而非第一次嘗試的成功率 | 每次 session 後跑完整測試套件 |
| 謹慎修剪暴露的能力至實際需求 | 過度設計工具存取權限 |

### 對 Workspace 的啟示

1. **Back-pressure = cc-workspace 的 pre-commit hooks**：只在錯誤時輸出、成功靜默，這正是現有 hook 設計應遵循的原則
2. **Skills 的漸進式揭露**：RESOLVER.md + @-import 機制的理論基礎
3. **Sub-agent 按任務模型選擇**：haiku-implementer（研究）→ implementer（跨模組）的分層已在實踐
4. **60 行以下的 CLAUDE.md**：與 OpenAI Codex 文章和 Addy Osmani 的建議完全一致
5. **MCP 謹慎原則**：只啟用需要的 MCP server，避免工具列表膨脹 context

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 9/10 | 直接講 Claude Code 的五大配置點，與 cc-workspace 現有設計一一對應，可立即對照審計 |
| B. 創新性 | 7/10 | Back-pressure 機制和「失敗前不加配置」的哲學有新意；但大部分是對已知概念的整合 |
| C. 證據品質 | 6/10 | 引用 ETH Zurich 和 Chroma 研究，但本文是 blog，無獨立實驗數據 |
| D. 技術深度 | 7/10 | 五大配置點有具體說明，但每個都是概述，缺乏實作細節 |
| E. 泛化性 | 8/10 | 通用 coding agent harness 優化模式，不限 Claude Code |
| **加權總分** | **7.55/10** | 9×0.3 + 7×0.2 + 6×0.2 + 7×0.15 + 8×0.15 = 2.7+1.4+1.2+1.05+1.2 |

**整合決策**：Rule  
**整合位置**：`.claude/refs/harness-design.md`（配置點框架與 back-pressure 原則）  
**整合狀態**：待實作

**TODO**：
- 將 back-pressure「只浮現錯誤、成功靜默」原則寫入 pre-commit hook 設計規範
- 確認 MCP server 清單，移除不必要的已啟用 server
