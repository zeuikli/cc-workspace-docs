# Multi-Agent 架構與 Sub-Agent 模式

整合官方文件、社群實戰（claudekit.cc）與 12 個可重用 Harness 模式，系統性地掌握多代理人協作架構。

## Sub-Agent 的正確定位

官方文件與 Claude Code 團隊成員 Adam Wolf 的明確指引：

> "Sub agents work best when they just looking for information and provide a small amount of summary back to main conversation thread."

### 正確用途 vs 錯誤用途

| 正確用途 | 錯誤用途 |
|---------|---------|
| 平行蒐集資訊（搜尋、讀取多個檔案）| 平行實作不同模組（每個 agent 都「視野盲目」）|
| 執行探索性任務（不需完整專案 context）| 跨模組重構（需要完整 context 才能正確推理）|
| 隔離「會污染主 context 的雜訊」| 序列依賴任務（A 的輸出決定 B 的輸入）|
| 研究型工作（讀取 log、搜尋結果）| 需要知道彼此決策的協作實作 |

---

## 拓撲限制

根據官方規範：

- **Fan-out 上限 4**：單一 turn 最多同時啟動 4 個 sub-agent
- **不支援 sub-agent spawning sub-agent**：child 不能再開 child（防止無限嵌套）
- **通訊限 parent ↔ child**：child 間不能直接溝通，只能透過 parent 彙整
- **Child 不 self-retry**：失敗必須返回 parent 決策

---

## Explore → Plan → Execute 模式

實戰驗證最有效的三階段架構：

```
Phase 1 (Sub-agents, parallel):  Explore — 各自蒐集資訊
Phase 2 (Main agent):            Plan    — 統整決策
Phase 3 (Main agent or 1 agent): Execute — 有完整 context 才實作
```

**為什麼這樣設計**：Sub-agent 的 context isolation 防止 context rot，但也造成盲點。Phase 1 讓資訊蒐集平行化，Phase 2 讓主 agent 在完整視野下做決策，Phase 3 確保實作者看得見完整架構。

---

## Strategic Model Routing

| 角色 | 模型 | 適用工作 |
|------|------|---------|
| 主 Agent | Opus 4.7 | 高層次推理、架構決策 |
| Implementation | Sonnet 4.6 | 中等複雜度的實作工作 |
| Simple Lookup | Haiku 4.5 | 低成本蒐集、格式化 |

```yaml
# .claude/agents/researcher.md 範例
---
model: claude-haiku-4-5
allowed-tools: Read, Grep, Glob, WebSearch
description: "Information gathering only. Returns ≤600 word summaries."
---
```

---

## 明確 Definition of Done

在 sub-agent prompt 末尾加入驗收 checklist，防止「premature victory declaration」：

```
## 完成條件（必須全部成立才能回傳）
- [ ] 已讀取所有指定路徑的檔案
- [ ] 摘要 ≤ 600 字
- [ ] 未修改任何檔案（只讀取）
- [ ] 若有錯誤，明確說明「失敗原因」而非口頭聲稱成功
```

---

## Tool 最小化原則

```yaml
# 不好的設定（給太多工具）
allowed-tools: Read, Write, Edit, Bash, WebSearch, WebFetch

# 好的設定（研究型 agent）
allowed-tools: Read, Grep, Glob

# 好的設定（實作型 agent，只給必要工具）
allowed-tools: Read, Edit, Bash
```

---

## 12 個可重用 Harness 模式

從 Claude Code 的設計中提煉的 12 個系統性模式，覆蓋四大領域：

### 記憶與上下文（5 個模式）

| 模式 | 說明 |
|------|------|
| **Persistent Instruction File** | 配置檔案在 Session 啟動時自動注入，定義架構規則與命名約定 |
| **Scoped Context Assembly** | 指令按工作目錄動態加載，支持單體倉庫的分層規則 |
| **Tiered Memory** | 精簡索引常駐上下文，細節按需加載，完整日誌離線存儲 |
| **Dream Consolidation** | 背景進程定期去重複與剪除過時記憶，防止索引膨脹 |
| **Progressive Context Compaction** | 近期交互保留細節，舊交互逐層摘要化，支持 20-30+ 輪 |

> **核心思路**：高頻訪問的決策常駐 context，低頻歷史卸載至磁盤——「主記憶」與「輔助儲存」的二級制。

### 工作流程與編排（3 個模式）

| 模式 | 說明 |
|------|------|
| **Explore-Plan-Act Loop** | 唯讀研究 → 規劃討論 → 代碼變更，權限逐級提升 |
| **Context-Isolated Subagents** | 角色特定的沙箱化上下文，防止工作階段污染 |
| **Fork-Join Parallelism** | 多 Subagent 並行工作，隔離倉庫副本，合併結果 |

### 工具與權限（3 個模式）

| 模式 | 說明 |
|------|------|
| **Progressive Tool Expansion** | 最小工具集（<20）默認加載，專化工具按需啟用 |
| **Command Risk Classification** | 確定性風險評估，低風險自動批准，高風險人工審批 |
| **Single-Purpose Tool Design** | 特定工具替代通用 Shell，提升可審計性 |

### 自動化（1 個模式）

| 模式 | 說明 |
|------|------|
| **Deterministic Lifecycle Hooks** | 25+ 鉤子綁定生命週期事件，可靠執行程序步驟，不依賴模型記憶 |

---

## Thin Harness, Fat Skills（Garry Tan）

Garry Tan 的核心原則：harness 應只做四件事：

1. **Run the model in a loop**
2. **Read and write files**
3. **Manage context**
4. **Enforce safety**

**Fat Harness 的問題**：過多的工具定義消耗 context window，引入效能瓶頸。量化案例：Playwright CLI 執行瀏覽器操作只需 100ms，Chrome MCP 需要 15 秒——**75 倍差距**。

**解決方案：方向性架構**

```
Intelligence ↑  → Skill Files（可重用指令）
Execution   ↓  → Deterministic Tools（確定性工具）
Middle Layer   → 盡可能薄
```

> "Every skill you write is a permanent upgrade to your system." — Garry Tan

Skill 在模型升級時自動受益（智慧提升），Deterministic Tool 保持可靠（確定性不變）。

---

## 失敗模式速覽（六大類 38 個 Gotcha）

### Delegation Trigger 失敗

| Gotcha | 症狀 | 修復 |
|--------|------|------|
| 自動委派過於保守 | Opus/Sonnet 傾向自己處理 | 在 CLAUDE.md 明確寫「Spawn multiple subagents when...」|
| Agent type 選錯 | researcher 開始寫程式碼 | Agent description 加明確禁止清單 |
| Fan-out 過小 | 3 個任務只啟動 1 個 sub-agent | 明確說「請同時委派給 3 個 sub-agent」|

### Context Isolation 失敗

| Gotcha | 症狀 | 修復 |
|--------|------|------|
| Sub-agent 重複工作 | 兩個 agent 讀同一個檔案 | Fan-out 前明確分配任務邊界 |
| Sub-agent 架構不一致 | Frontend agent 的決策與 Backend 衝突 | Execute phase 集中在主 agent，sub-agent 只 Explore |
| 忘記隔離 context | Sub-agent 看到主線 context 污染 | 驗證 sub-agent system prompt 不引用主線狀態 |

### 輸出品質失敗

| Gotcha | 症狀 | 修復 |
|--------|------|------|
| 過早宣告成功 | Sub-agent 說「完成了」但實際沒讀完 | 加 Definition of Done checklist |
| 摘要過長 | Sub-agent 返回 2000 字，污染主 context | 明確限制「回傳 ≤ 600 字」|
| 無結構輸出 | 自由文字難以被主 agent 解析 | 要求 JSON 或 markdown 表格格式 |

---

## 與 Karpathy/Mnilax 規則的關聯

| 規則 | 對應模式 |
|------|--------|
| R1 — Think Before Coding | Explore-Plan-Act Loop |
| R2 — Simplicity First | Progressive Tool Expansion |
| R3 — Surgical Modifications | Context-Isolated Subagents |
| R5 — Latent vs Deterministic | Command Risk Classification |
| R6 — Context Budget | Tiered Memory |
| R9 — Test Intent | Deterministic Lifecycle Hooks |
| R12 — Fail Loud | Deterministic Lifecycle Hooks |

---

## 延伸閱讀

- [Sub-Agents 官方文件](https://code.claude.com/docs/en/sub-agents)
- [Hooks 設計模式](/resources/best-practices/hooks)
- [Lecture 05：記憶系統與工作區設計](/lectures/lecture-05-memory-workspace/)
- [Lecture 04：Harness 三層架構](/lectures/lecture-04-harness-architecture/)
