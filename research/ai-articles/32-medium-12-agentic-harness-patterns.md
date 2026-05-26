---
url: https://medium.com/@simranjeetsingh1497/agent-harness-12-agentic-harness-patterns-from-claude-code-5505b7c239c4
alternative_urls:
  - https://generativeprogrammer.com/p/12-agentic-harness-patterns-from
  - https://www.epsilla.com/blogs/2026-04-18-deep-dive-12-reusable-agentic-harness-design-patte
title: 12 Agentic Harness Patterns from Claude Code
status: RETRIEVED_FROM_ALTERNATIVE
original_status: URL_REDIRECT_FAIL
date_retrieved: 2026-05-18
---

# 12 Agentic Harness Patterns from Claude Code

## 來源說明

原始 Medium 文章需要登入。本文內容已從以下替代來源成功抓取：
- [GenerativeProgrammer](https://generativeprogrammer.com/p/12-agentic-harness-patterns-from)
- [Epsilla Engineering Blog](https://www.epsilla.com/blogs/2026-04-18-deep-dive-12-reusable-agentic-harness-design-patte)

## 核心摘要（繁體中文）

Claude Code 的設計中發現了 12 個可重用的 Agentic Harness 模式，系統性地解決生產級 AI Agent 的四大關鍵領域：記憶與上下文、工作流程與編排、工具與權限、自動化。

**記憶與上下文（5 個模式）** 的核心思路在於分層與動態加載。`Persistent Instruction File` 模式將架構規則與命名約定封裝於配置檔案中，在每次 session 開始時自動注入，消除用戶重複輸入。`Scoped Context Assembly` 在單體倉庫中動態載入特定目錄層級的指令，確保 Agent 看到與其工作環境相符的規則。`Tiered Memory` 透過分層策略保持高頻索引始終在上下文中，專題細節按需加載，完整日誌只供離線搜尋。`Dream Consolidation` 利用後台進程在閒置時定期去重複與剪除過時記憶，防止長期運行中的索引膨脹。`Progressive Context Compaction` 採用多級壓縮，近期交互保留完整細節，舊交互逐層摘要化，支持 20-30+ 輪交互。

**工作流程與編排（3 個模式）** 強調階段隔離與並行處理。`Explore-Plan-Act Loop` 將工作分為唯讀研究、對齐規劃與代碼變更三個階段，權限逐級提升，防止基於不完整理解的倉促改動。`Context-Isolated Subagents` 為不同角色（研究者、規劃者、執行者）分配沙箱化上下文，實現任務特定的隔離與可控性。`Fork-Join Parallelism` 將工作分片至多個 Subagent，各自在隔離的倉庫副本中獨立運作，最後合併結果，實現並行執行。

**工具與權限（3 個模式）** 實踐「最小權限原則」與可審計設計。`Progressive Tool Expansion` 默認使用不超過 20 個核心工具的最小集合，按需動態啟用專化工具，而非一次性暴露全工具庫。`Command Risk Classification` 在執行前以確定性的風險矩陣評估命令影響範圍，低風險操作自動批准，高風險操作閘門人工審批。`Single-Purpose Tool Design` 用特定、確定性的工具（如 FileReadTool、GrepTool）替代通用 Shell 包裝器，提升可審計性與認知負荷。

**自動化（1 個模式）** 的關鍵在於確定性與非依賴 LLM 記憶。`Deterministic Lifecycle Hooks` 將非協商的操作綁定至 Agent 生命週期事件（25+ 個鉤子），通過中間件在提示外自動執行，確保程序步驟可靠執行，不依賴模型上下文合規性。

這 12 個模式構成了「Harness Engineering」的核心框架，與 Karpathy 的 4 條基礎規則及 Mnilax 的 8 條增量規則形成完整的 12-Rule Canon，實現從探索→規劃→執行的系統性 Agent 工程。

## 12 個模式清單

### 記憶與上下文
1. **Persistent Instruction File** — 配置檔案在 Session 啟動時自動注入，定義架構規則與命名約定
2. **Scoped Context Assembly** — 指令按工作目錄動態加載，支持單體倉庫的分層規則
3. **Tiered Memory** — 精簡索引常駐上下文，細節按需加載，完整日誌離線存儲
4. **Dream Consolidation** — 背景進程定期去重複與剪除過時記憶，防止索引膨脹
5. **Progressive Context Compaction** — 近期交互保留細節，舊交互逐層摘要化

### 工作流程與編排
6. **Explore-Plan-Act Loop** — 唯讀研究 → 規劃討論 → 代碼變更，權限逐級提升
7. **Context-Isolated Subagents** — 角色特定的沙箱化上下文，防止工作階段污染
8. **Fork-Join Parallelism** — 多 Subagent 並行工作，隔離倉庫副本，合併結果

### 工具與權限
9. **Progressive Tool Expansion** — 最小工具集（<20）默認加載，專化工具按需啟用
10. **Command Risk Classification** — 確定性風險評估，低風險自動批准，高風險人工審批
11. **Single-Purpose Tool Design** — 特定工具替代通用 Shell，提升可審計性

### 自動化
12. **Deterministic Lifecycle Hooks** — 25+ 鉤子綁定生命週期事件，可靠執行程序步驟

## 關鍵引用

### 記憶與上下文層面

> "A lean, high-level index remains persistently in the active context. Task-specific details are dynamically loaded on-demand" while comprehensive logs stay on disk.

這個設計體現了上下文預算的明智分配：高頻訪問的決策與狀態保持在 LLM 窗口中，低頻的歷史與細節卸載至磁盤，實現「主記憶」與「輔助儲存」的二級制。

### 工作流程層面

> "Workflows separate into read-only research, alignment planning, and code mutation phases with escalating permissions."

此模式直接對應 Karpathy Rule 1（Think Before Coding）與 Rule 3（Surgical Modifications）——先通過完全探索期減少盲目決策，再在規劃確認後才執行變更，從系統級層面強制「寧可謹慎也不倉促」的原則。

### 工具與權限層面

> "Middleware evaluates command blast radius against risk matrices, routing low-risk operations while gating high-risk actions for human approval."

這是 Rule 5（Latent vs Deterministic 邊界）的工程實踐——風險評估這種確定性邏輯不交由 LLM，而由確定性代碼（中間件）負責，LLM 專注於「應該做什麼」，確定性層專注於「能否做」。

## 與 Karpathy/Mnilax 規則的關聯

| 規則 | 對應模式 | 工程實踐 |
|------|--------|--------|
| R1 — Think Before Coding | Explore-Plan-Act Loop | 強制唯讀探索期，延遲決策 |
| R2 — Simplicity First | Progressive Tool Expansion | 最小工具集默認，杜絕工具過載 |
| R3 — Surgical Modifications | Context-Isolated Subagents | 隔離階段，防止副作用污染 |
| R4 — Goal-Oriented | Deterministic Lifecycle Hooks | 可觀測的生命週期檢查點 |
| R5 — Latent vs Deterministic | Command Risk Classification | 風險評估交由確定性層 |
| R6 — Context Budget | Tiered Memory | 主記憶精簡，按需加載 |
| R7 — Surface Conflicts | Scoped Context Assembly | 動態加載，暴露衝突 |
| R8 — Read Before Write | Progressive Compaction | 完整日誌保留，按需讀取 |
| R9 — Test Intent | Deterministic Lifecycle Hooks | 鉤子層驗證業務邏輯 |
| R10 — Checkpoint | Progressive Context Compaction | 定期檢查點，防止上下文漂移 |
| R11 — Convention First | Persistent Instruction File | 架構規則中央化，自動加載 |
| R12 — Fail Loud | Deterministic Lifecycle Hooks | 鉤子層確保容錯可觀測 |

## 實踐路徑

1. **Foundation**（基礎）：實現 Persistent Instruction File + Explore-Plan-Act Loop
2. **Scale**（擴展）：加入 Tiered Memory + Progressive Tool Expansion
3. **Robustness**（穩定性）：部署 Deterministic Lifecycle Hooks + Command Risk Classification
4. **Optimization**（最佳化）：調整 Dream Consolidation + Progressive Context Compaction

此順序遵循「核心優先，邊界邊界清晰，自動化最後」的原則，確保每一層都能獨立驗證。

---

**抓取來源驗證**：
- generativeprogrammer.com — 完整文章，12 個模式清晰分類（2026-05-18 快取驗證）
- epsilla.com — 深度解析，工程實踐細節補充（2026-05-18 快取驗證）
