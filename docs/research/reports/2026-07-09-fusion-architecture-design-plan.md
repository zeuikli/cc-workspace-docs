---
title: "通用 Fusion 架構設計 + Token 節省策略 + GLM×Kimi 執行計畫"
date: 2026-07-09
status: reviewed-revised
authors: [GLM-5.2, Kimi-K2.7]
sources: ["https://cognition.com/blog/devin-fusion", "https://docs.factory.ai/cli/configuration/mixed-models.md", "https://docs.factory.ai/web/factory-router.md", "https://docs.factory.ai/cli/configuration/custom-droids.md", "https://docs.factory.ai/api-reference/sessions/update-a-session.md", "https://docs.factory.ai/cli/user-guides/choosing-your-model.md", research/ai-articles/scored/2026-07-02-cognition-devin-fusion-sidekick-routing.md, research/DAILY-RESEARCH/2026-07-02.md, research/reports/archive/2026-06-12-multi-mode-agent-skill-design.md, .claude/skills/multi-mode-skill/SKILL.md, .claude/agents/multi-mode-agent.md, .claude/refs/delegation-protocol.md, .claude/refs/model-profiles.md, .claude/rules/context-management.md, .claude/rules/subagent-strategy.md]
type: architecture-design-plan
---

# 通用 Fusion 架構設計 + Token 節省策略 + GLM×Kimi 執行計畫

> 本報告基於完整閱讀 workspace 全部 DAILY-TOPICS（22 檔）、DAILY-RESEARCH（23 檔）、NEW-DOMAINS（2 報告）、WEEKLY-REPORT（4 份）、Session Reports（22 份）後,結合 Cognition Devin Fusion 原始博客、Factory Droid 官方文件、workspace 現有 multi-mode 架構,提出的跨 harness 通用 Fusion 設計。

---

## 第一部分：現狀分析

### 1.1 Cognition Devin Fusion 核心機制

Devin Fusion 的兩大技術支柱:

**Sidekick 雙模型並行架構**:
- frontier 模型（主 agent）與 cost-effective sidekick 模型（副 agent）**平行部署**,各自維護獨立且持久的 cached context
- 主 agent 扮演「tech lead」: 只讀取絕對必要的資訊,委派給 sidekick（須具名效益: context isolation / parallelism / mechanical volume）,保留規劃/歧義判斷/最終審查
- sidekick 處理機械性工作（測試執行、批量重構、文件掃描）
- 關鍵: 避免 advisor pattern 的跨 context 查詢 cache miss 問題

**Dynamic Mid-Session Routing**:
- 輕量分類器在任務執行中偵測何時需要切換模型
- **關鍵洞見**: 模型切換綁定在 context compaction 階段 — compaction 本就觸發 cache 失效。**精確區分**: compactionModel 切換 = 零額外 cache 懲罰（compaction 本就失效）; 主模型切換 = 一次性 prefix re-cache 成本（新模型需重建快取前綴）,但仍比 mid-turn 切換便宜。此 claim 繼承自 Cognition 自報,Factory API 層快取行為未經獨立驗證
- 可在 sidekick 之間升級（不回主模型）,也可從 sidekick 回主模型

**量化結果**:
- 35% 成本降低（非 Fable 配置）,41% 降低（Fable 5 配置）— **注意**: 此為 Cognition 自報,未經第三方獨立驗證; workspace 模擬顯示成本加權 -35.2% 但頻率加權僅 +2.8%,節省 84% 來自大規模遷移任務（10% 頻率）
- 88% 已合併 PR 由 Fusion routing 全自動完成
- FrontierCode 分數維持 frontier-level（57.6 vs 純 Fable 5 的 57.0）

### 1.2 Workspace 現有 multi-mode 架構

**已實現的部分**:
- `multi-mode-skill`（主對話 router）: 依獨立位置數分類 → 選 model/effort/mode → inline 或 spawn worker
- `multi-mode-agent`（sub-agent worker）: 四檔位紀律（cost/quality/ceiling/frontier）內聯,spawn 時綁定 model
- `delegation-protocol.md`: 指揮官不下場、委派須具名效益、升降級路徑（現行規則以 subagent-strategy.md 為準）
- `model-profiles.md`: 四檔位 ↔ 當代模型對應表 + 定價矩陣 + prompt cache 門檻

**與 Devin Fusion 的差距**:

| 維度 | Devin Fusion | workspace 現有 | 差距 |
|------|-------------|--------------|------|
| 雙模型並行 | sidekick + frontier 平行,各自持久 context | parent 規劃 + child 執行（fan-out）,但 child 是一次性 spawn | workspace child 不保持持久 context,無法「監控並委派」 |
| Mid-session 切換 | compaction 時切換（compactionModel = 零懲罰; 主模型 = 一次性 re-cache） | **禁止** mid-session 切換（context-management.md 鐵律） | workspace 用「新 session / sub-agent override」規避,非主對話內切換 |
| 路由分類器 | 輕量分類器在執行中偵測 | 依「獨立位置數」靜態分類 | workspace 無執行中動態升降級（只有失敗後的升降級重派） |
| Cache 隔離 | 雙獨立快取,互不破壞 | 主對話 cache 為主,sub-agent 各自獨立但一次性 | workspace sub-agent 的 cache 無法跨 spawn 持久化 |

### 1.3 Factory Droid 的 Fusion 相關能力

**已具備的 Fusion 基礎設施**:

| Factory 功能 | 對應 Fusion 概念 | 狀態 |
|-------------|----------------|------|
| **Mixed Models** | spec mode 用強模型規劃,default model 執行 | ✅ 已上線（Shift+Tab 配置） |
| **Factory Router** | per-task 自動模型路由,考慮 prompt cache 維護 | ✅ GA,43% 成本降低 |
| **Custom Droids** | sidekick agent（獨立 model + tools + prompt） | ✅ 已上線 |
| **Session API PATCH** | **mid-session 切換 model + reasoningEffort + compactionModel** | ✅ API 支援 |
| **providerLock** | ⚠️ 非 CLI 可設定; 相容性由 Mixed Models 規則自動強制（OpenAI↔OpenAI; Anthropic reasoning on↔Anthropic; reasoning off↔非 OpenAI）。`providerLockTimestamp` API 欄位存在但語意未文件化 | ⚠️ 自動強制 |
| **compactionModel** | compaction 時指定不同模型（= Devin Fusion 的 compaction 時切換） | ✅ Session 層級 |
| **childInclusiveTokenUsageBySessionId** | per-child token 追蹤（含 cache 命中） | ✅ API 回傳 |
| **BYOK** | 接入開源模型（GLM/Kimi/MiniMax）作 sidekick | ✅ 已上線 |
| **Claude Code agent import** | 直接將 `.claude/agents/` 導入為 Droids | ✅ 已上線 |

**關鍵發現**: Factory 的 Session API `PATCH /sessions/{sessionId}` 支援 mid-session 切換 `model` + `reasoningEffort` + `compactionModel`,這正是 Devin Fusion「compaction 時切換模型」的 API 層實現。且 `compactionModel` 可設為與主模型不同的模型,等同 Devin Fusion 的「compaction 時順便換模型」。

**Factory vs Claude Code 的關鍵差異**:

| 維度 | Claude Code | Factory Droid |
|------|-----------|--------------|
| Mid-session model 切換 | ❌ 禁止（破 prompt cache） | ✅ API 支援（PATCH session） |
| Compaction model 選擇 | ❌ 用當前模型 | ✅ 可指定不同模型 |
| 跨廠商 reasoning trace | ❌ 不相容 | ⚠️ Mixed Models 相容性規則自動強制（非 providerLock CLI 開關） |
| 開源模型 sidekick | ❌ 僅 Anthropic 系列 | ✅ GLM/Kimi/MiniMax/DeepSeek 等 |
| Per-child token 追蹤 | ❌ 無 API 層級 | ✅ childInclusiveTokenUsageBySessionId |
| Agent 可攜性 | Claude Code 專用 | ✅ Custom Droids + Claude Code import |

---

## 第二部分:通用 Fusion 架構設計

### 2.1 設計原則

1. **Bi-harness（Claude Code + Factory）**: 設計適用 Claude Code 和 Factory Droid 兩個 harness,非 universal harness-neutral（AGENTS.md §1 portability note: switching to Codex/Cursor = rebuild enforcement layer）
2. **Cache-first**: 所有模型切換决策必須考慮 cache 影響。compactionModel 切換 = 零懲罰; 主模型切換 = 一次性 prefix re-cache（非零）
3. **漸進落地**: 分三階段（Phase 1-3）,每階段可獨立驗證,不一次性重建
4. **外部驗證**: 採信前必須機械重驗（workspace 既有原則）

### 2.2 三層架構 + 1 cross-cutting gate

```
┌─────────────────────────────────────────────────┐
│          Fusion Router (L0 — 決策層)              │
│  輕量分類器: 任務複雜度信號 → 主/副模型分配        │
├─────────────────────────────────────────────────┤
│     Main Agent (L1 — frontier 持久 context)      │
│  規劃 · 歧義判斷 · 最終審查 · 監控 sidekick        │
│  cache: 穩定前綴（CLAUDE.md/AGENTS.md + system）  │
├─────────────────────────────────────────────────┤
│   Sidekick Agent (L2 — cost 持久 context)        │
│  機械執行 · 測試運行 · 批量掃描 · 文件讀取         │
│  cache: 獨立前綴（任務-specific context）         │
├─────────────────────────────────────────────────┤
│         Compaction Gate (L3 — 切換時機)           │
│  compaction 觸發 → 評估是否升級/降級模型           │
│  compactionModel: 零懲罰; 主模型: 一次性 re-cache  │
└─────────────────────────────────────────────────┘
```

### 2.3 Claude Code 實現路徑（Phase 1-2）

**Phase 1: Sidekick via Sub-agent（現有能力,零修改）**

workspace 現有的 `multi-mode-skill` + `multi-mode-agent` 已近似 Sidekick 模式:
- 主對話（frontier/ceiling）= Main Agent
- spawn `multi-mode-agent` with `model: haiku` = Sidekick Agent
- 主對話保持持久 context,sidekick 一次性執行回報

**優化項（不改架構,改使用模式）**:
1. 主對話委派機械任務給 cost 檔 sidekick（具名效益: low-risk mechanical volume）,只在「規劃/歧義/審查」時親做
2. sidekick 回報只含結論 + 檔案:行號（delegation-protocol.md §4 既有規則）
3. 主對話的 cache 前綴保持穩定（context-management.md Static First 既有規則）

**Phase 2: Persistent Sidekick via Background Agent（需 Claude Code 新功能）**

Claude Code v2.1.191 的 background agents 已支援 nested subagents（depth 5）,但 sub-agent context 不持久。若未來 Claude Code 支援「persistent background agent with cached context」（類似 Devin Fusion 的 sidekick 持久 context）,則可實現真正的雙獨立快取。

**現狀替代方案**: 用 `claude-progress.json` checkpoint 模擬持久性 — sidekick 每次 spawn 時讀取 checkpoint 恢復狀態,而非從零開始。這不是真正的 cache 持久化,但可減少重複 context 建構的 token 開銷。

### 2.4 Factory Droid 實現路徑（Phase 1-3）

**Phase 1: Mixed Models + Custom Droid Sidekick（現有能力）**

1. 主 session 用 ceiling/frontier 模型（Opus 4.8 / Fable 5）
2. 配置 Mixed Models: spec mode 用更強模型規劃,default model 用 quality 執行
3. 建立 Custom Droid `sidekick-executor`: `model: haiku` 或 `model: glm-5.2`,限制 `tools: read-only` 或 `tools: ["Read", "Grep", "Glob", "Execute"]`
4. 主 session 透過 Task tool 委派機械任務給 sidekick-executor

**Phase 2: Factory Router + Compaction Model（現有能力,配置層）**

1. 啟用 Factory Router 作為主 session 模型 — 自動 per-task 路由,43% 成本降低
2. 配置 `compactionModel` 為 cost 檔模型（Haiku 4.5） — compaction 由便宜模型執行,省 token 又不破壞主對話 cache
3. ~~設定 `providerLock: anthropic`~~ — **修正**: providerLock 無 CLI 開關; Mixed Models 相容性規則自動強制（reasoning on = Anthropic only; reasoning off = 可配非 OpenAI）。無需手動設定

**Phase 3: API 層 Mid-Session Fusion（需 API 整合開發）**

> ⚠️ **M14 修正**: Phase 3 的 compaction-trigger 偵測機制尚未有 Factory 文件佐證的 event/polling contract。以下為設計推測,落地前需確認 Factory 是否提供 compaction webhook、polling API、或 CLI hook。

透過 Session API `PATCH /sessions/{sessionId}` 實現 Devin Fusion 的動態路由:

```
1. 偵測 compaction 觸發:
   - 方案 A: polling GET /sessions/{id} 檢查 compactionThresholdCheckEnabled + token usage
   - 方案 B: CLI hook（若 Factory 支援 pre-compact hook,類似 Claude Code PreCompact）
   - 方案 C: webhook（若 Factory 提供 compaction event notification）
   - ⚠️ 三方案均未經 Factory 文件確認,屬整合開發待驗證項
2. PATCH session:
   - 若任務變複雜 → model 升級（quality → ceiling）
   - 若任務變機械 → model 降級（ceiling → cost）
   - compactionModel 始終用 cost 檔
3. 繼續 session（model 已切換,cache 本就因 compaction 失效）
```

這是 Factory 獨有的能力 — Claude Code 目前無 API 層 mid-session model 切換。

### 2.5 跨 Harness 通用層:AGENTS.md Fusion Protocol

在 `AGENTS.md` 新增一個 Fusion Protocol 段落（harness-neutral）:

```markdown
## Fusion Protocol（跨 harness 通用）

### 角色分配
- Main Agent: 規劃、歧義判斷、最終審查、監控 sidekick（委派須具名效益,例外親做）
- Sidekick Agent: 機械執行、測試運行、批量掃描（回報結論 + 檔案:行號）

### 切換時機
- 模型切換綁定 compaction（compactionModel = 零懲罰; 主模型 = 一次性 re-cache）
- 執行中複雜度信號: 連續失敗 → 升級; 機械模式確認 → 降級
- 非 compaction 時: 用 sub-agent spawn（新 context）取代主對話切換

### Cache 紀律
- 主對話/主 session: 穩定前綴不動（CLAUDE.md/AGENTS.md + system prompt）
- Sidekick: 獨立 context,不污染主對話
- Compaction model: 用 cost 檔模型執行（省 token）
```

---

## 第三部分:Token 節省策略（兼顧品質）

### 3.1 從 workspace 22 份 DAILY-RESEARCH 萃取的 token 節省洞見

| 策略 | 來源 | 節省幅度 | 品質影響 | workspace 落地狀態 |
|------|------|---------|---------|------------------|
| Devin Fusion sidekick 路由 | 07-02 DAILY-RESEARCH | 35-41% | 維持 frontier | ⏳ 觀察中,未實作 |
| Coinbase prompt caching 5%→60% | 06-30 DAILY-RESEARCH | ~50% AI 支出 | 無負面 | ⏳ 待落地 |
| Factory Router per-task 路由 | Factory 官方 | 43%（中位 81%） | 維持 frontier | N/A（Factory 專用） |
| Compaction 用 cost 模型 | 本報告設計 | compaction token 省 ~80% | 無負面（compaction 非推理） | N/A（待落地） |
| Sidekick 機械任務用開源模型 | 本報告設計 | sidekick token 省 90%+ | 需驗證開源模型能力 | N/A（Factory BYOK） |
| NLAH context 放置 | context-management.md 既有 | 減少 lost-in-the-middle | 正面 | ✅ 已落地 |
| Sub-agent context 隔離 | subagent-strategy.md 既有 | 主對話不收 bulk 輸出 | 正面 | ✅ 已落地 |
| Decision-Log 外化 | multi-mode-agent 既有 | 減少重複推理 | 正面 | ✅ 已落地 |

### 3.2 五層 Token 優化體系

**Layer 1: 模型路由層（最大節省）**
- 機械任務 → cost 檔（Haiku $1/$5 或開源 GLM-5.2 $1.4/$4.4）— **節省為 workload-conditional**: 模擬顯示 -35.2% 成本加權但 +2.8% 頻率加權,84% 節省來自 10% 頻率的大規模遷移任務
- 標準任務 → quality 檔（Sonnet 5）
- 深推理 → ceiling 檔（Opus 4.8）
- 稀缺架構 → frontier 檔（Fable 5,使用者授權）
- **Fusion 優化**: 主對話用 ceiling,sidekick 用 cost,compaction 用 cost → 加權後接近 quality 價位但維持 ceiling 推理

**Layer 2: Cache 策略層**
- Static First: CLAUDE.md/AGENTS.md 永遠最前,session 內不動
- compactionModel 切換: 零額外 cache 失效; 主模型切換: 一次性 prefix re-cache（非零,但低於 mid-turn 切換）
- Compaction model 用 cost 檔（compaction 本身不需推理能力）
- prompt cache 最低門檻遵守（cost 檔 4096 tokens,quality 檔 2048 tokens）

**Layer 3: Context 管理層**
- NLAH: 目標放 HEAD,最新輸出放 TAIL
- Sub-agent 回報只含結論 + 檔案:行號（不回灌原文）
- 長產物存檔,回傳路徑 + ≤10 行摘要
- `claude-progress.json` checkpoint 防 compact 後記憶衰退

**Layer 4: 委派策略層**
- 委派須具名效益,例外親做（subagent-strategy.md 現行規則; delegation-protocol.md §1 已由 subagent-strategy.md 覆蓋）
- T0 親做例外: ≤3 次工具呼叫、確定性 gate、對話裁決
- Sidekick 失敗 1 次即升級（cost → quality）,不重試
- **部分失敗偵測（開源 sidekick 專用）**: 
  - 正交驗證: main agent 用不同 pattern 重跑 grep/檢查,非信任 sidekick 的相同方法
  - Scope-verification: 確認 sidekick 操作了正確的目標檔案（非鄰近檔案）
  - Citation-existence check: 研究 sidekick 的 URL 引用需機械驗證存在（grep URL,不信宣稱）
  - 邏輯正確性 spot-check: 對機械任務隨機抽 10% 由 main agent 重做,比對結果
- 降級: 高檔位解出模式寫成規則,降 cost 批次套用

**Layer 5: 輸出紀律層**
- 不加確認句、不加大段原文
- JSON 任務回純 JSON
- 結構化摘要非原始 dump
- 確定性 gate 結果據實回報

### 3.3 品質保障機制（節省不等於降質）

從 workspace DAILY-RESEARCH 萃取的品質保障:

1. **驗證不自驗**（delegation-protocol.md §6）: sidekick 產出由 main agent 機械重驗
2. **對抗審查**: 重要交付強制 fresh-context 異模型對抗審查
3. **eval-hack 防護**: 檔位越高驗證越嚴（frontier = +對抗稽核）
4. **量化委派基準**: sqlite-utils 案例（37 prompts / 5 blockers / $149.25）作為校準錨點
5. **跨模型互查**: GPT-5.5 複查 Fable 5 仍能抓到遺漏 → verdict 非證據,必須機械重驗

---

## 第四部分:GLM×Kimi 執行計畫

### 4.1 分工原則

| 角色 | 模型 | 適合任務 | 理由 |
|------|------|---------|------|
| GLM | GLM-5.2（ceiling 檔,開源）⚠️ 合規 caveat | 架構設計驗證、跨 harness 對比分析、Phase 1 實作審查 | 1M context + SWE-bench Pro 62.1% 接近 Opus,成本 1/6。**注意**: Z.ai API 走中國伺服器有 GDPR/合規風險（model-profiles.md §0）,企業任務勿用 API 模式; 非 Claude 模型校正狀態 = BLOCKED-EXTERNAL（§6）,sidekick 部署前須完成校正程序 |
| Kimi | Kimi K2.7 Code（quality 檔,開源）⚠️ 合規 caveat | 文件撰寫、token 節省量化模擬、AGENTS.md Fusion Protocol 草稿 | 1000 tok/s 速度 + code 特化 + 成本 0.4×。**注意**: 非 Claude 模型校正狀態 = BLOCKED-EXTERNAL,須完成 §6 校正程序後方可用於 sidekick |

> **BYOK Sidekick 合規 Gate**: 開源模型（GLM/Kimi/MiniMax）用於 sidekick 前,必須完成 model-profiles.md §6 非 Claude 校正程序（5-10 代表性任務含 eval-hack trap; 目前 BLOCKED-EXTERNAL）。企業任務禁用 Z.ai API 模式（GDPR 風險）。

### 4.2 GLM 任務:架構驗證 + Phase 1 審查

**任務 GLM-A: Fusion 架構可行性驗證**
- 目標: 驗證本報告第二部分的 Fusion 架構在 Claude Code 現有功能下是否可落地
- 方法: 逐項檢查 Phase 1 的每個「優化項」是否依賴未確認的 Claude Code 功能
- 驗證命令: `grep -q 'multi-mode-agent' .claude/agents/ && grep -q 'multi-mode-skill' .claude/skills/multi-mode-skill/SKILL.md`
- 產出: `research/reports/2026-07-09-fusion-glm-architecture-validation.md`
- 驗收: 每個 Phase 1 優化項標注 ✅可落地 / ⚠️需修改 / ❌不可落地 + 理由

**任務 GLM-B: Factory Droid Phase 2 配置方案具體化**
- 目標: 將本報告 §2.4 Phase 2 的「配置層」方案具體化為可執行的 Factory 配置步驟
- 方法: 基於 Factory 官方文件（mixed-models / factory-router / custom-droids / session API）撰寫 step-by-step 配置指南
- 產出: `research/reports/2026-07-09-fusion-glm-factory-phase2-config.md`
- 驗收: 每個步驟附 Factory 文件 URL + 具體 CLI/API 指令

### 4.3 Kimi 任務:Token 節省量化 + Fusion Protocol 草稿

**任務 KIMI-A: Token 節省量化模擬**
- 目標: 模擬 5 種典型 workspace 任務在 Fusion 架構下的 token 消耗,對比現有架構
- 方法: 用 model-profiles.md §2.3 定價矩陣 + delegation-protocol.md 委派門檻,計算每種任務的加權 token 成本
- 五種任務: ① 單檔小改 ② 跨模組重構 ③ 深度研究（10+ 檔） ④ 安全審查 ⑤ 大規模遷移（700M 行類）
- 產出: `research/reports/2026-07-09-fusion-kimi-token-simulation.md`
- 驗收: 每種任務含「現有架構成本 vs Fusion 架構成本」對比表 + 節省百分比

**任務 KIMI-B: AGENTS.md Fusion Protocol 段落草稿**
- 目標: 撰寫 §2.5 的 AGENTS.md Fusion Protocol 完整段落,格式對齊 AGENTS.md 現有風格
- 方法: 參考 AGENTS.md §2 Agent Dispatch 表格 + §5 Harness vs Body 表格風格
- 約束: ≤30 行（AGENTS.md byte 門檻）,harness-neutral,不含模型名/數字（L1 零模型名鐵律）
- 產出: `research/reports/2026-07-09-fusion-kimi-agents-md-protocol-draft.md`
- 驗收: `wc -c` ≤ 1200 bytes + grep 無模型名 + 格式對齊 AGENTS.md 現有段落

### 4.4 執行順序

```
Phase 1（並行）:
  GLM-A（架構驗證） ─┐
                      ├─→ 彙整 → 報告更新
  KIMI-A（token 模擬）┘

Phase 2（並行,Phase 1 完成後）:
  GLM-B（Factory 配置）─┐
                        ├─→ 彙整 → 最終交付
  KIMI-B（Protocol 草稿）┘
```

### 4.5 驗收標準

| 項目 | 驗收條件 | 驗證方法 |
|------|---------|---------|
| GLM-A | 每個 Phase 1 優化項有 ✅/⚠️/❌ 標注 | 人工核對 |
| GLM-B | 每個步驟附 Factory 文件 URL | `grep -c 'docs.factory.ai' <file>` ≥ 3 |
| KIMI-A | 5 種任務均有對比表 + 節省 % | 每種任務含「現有 vs Fusion」兩列 |
| KIMI-B | ≤1200 bytes + 無模型名 | `wc -c` + `grep -iE 'opus|sonnet|haiku|fable|glm|kimi' <file>` = 0 |

---

## 第五部分:與 workspace 既有研究洞見的對齊

### 5.1 本設計回應的跨主題洞見

從 22 份 DAILY-RESEARCH 的「跨主題洞見合成」段:

1. **「模型選擇」正被「路由/降級策略」取代**（07-02） → 本設計的 Fusion Router 就是路由/降級策略的具體實現
2. **回饋迴圈框架跨社群收斂**（07-02） → Compaction Gate 是回饋迴圈的切入點
3. **harness quality = 評測第一獨立變數**（06-18） → Fusion 架構是 harness 層優化,非模型層
4. **agent 記憶升格為系統層**（07-06） → Sidekick persistent context + checkpoint 是記憶基礎設施
5. **安全機制透明化需求**（07-02） → Fusion 切換必須對使用者可見（非靜默降級）
6. **供應商工具也需信任但驗證**（07-09） → Factory Router 是供應商工具,其路由决策仍需機械重驗

### 5.2 本設計不違背的既有鐵律

| 鐵律 | 來源 | 本設計如何遵守 |
|------|------|--------------|
| Mid-session 禁止切換模型 | context-management.md | Claude Code 路徑用 sub-agent spawn 不切主對話;Factory 路徑用 compaction 時切換（API 原生支援） |
| 指揮官不下場 | subagent-strategy.md（現行）/ delegation-protocol.md §1（已覆蓋） | Main Agent 委派須具名效益,例外親做 |
| 驗證不自驗 | delegation-protocol.md §6 | Sidekick 產出由 Main Agent 機械重驗 |
| L1 零模型名 | HARNESS-CORE-v3 §6 | AGENTS.md Fusion Protocol 不含模型名 |
| 確定性 gate 永遠 main 親跑 | subagent-strategy.md | Fusion 不改變 gate 執行者 |

---

## 第六部分:風險與限制

1. **Claude Code 無 API 層 mid-session 切換**: Phase 2 的 persistent sidekick 需 Claude Code 新功能,目前只能用 checkpoint 模擬
2. **Factory Router 為黑箱**: 其路由决策邏輯不公開,43% 節省為廠商自報,需獨立驗證
3. **跨廠商 reasoning trace 不相容**: OpenAI 模型只能配 OpenAI（Mixed Models 相容性規則）,限制 sidekick 選擇
4. **開源模型 eval-hack 風險未知**: model-profiles.md §1 將非 Claude 模型標為「未知=當最高處理」,sidekick 用開源模型需額外驗證
5. **AGENTS.md byte 門檻**: Fusion Protocol 段落 ≤1200 bytes 限制,可能需壓縮或 defer 到 byte 清理後

---

## 第六部分b:缺失維度補充（交叉審查 C6 修正）

### 6b.1 延遲模型

Fusion 架構的 sidekick round-trip 成本（spawn/PATCH + 執行 + 回報）在 wall-clock 秒級別高於 inline 執行。

| 任務類型 | 延遲影響 | 建議 |
|---------|---------|------|
| 即時 incident response | ⛔ 不適用 Fusion | main agent inline 親做 |
| 即時 debugging | ⛔ 不適用 Fusion | main agent inline 親做 |
| 批量掃描/遷移 | ✅ 延遲可接受 | sidekick 並行,main 等回報 |
| 深度研究 | ✅ 延遲可接受 | sidekick 掃描 + main 彙整 |
| 安全審查 | ⚠️ 需權衡 | adversarial review 需 sidekick 但不能阻塞 |

**結論**: Fusion 不推薦用於 latency-bound 任務。適用於 throughput-bound 和 quality-bound 任務。

### 6b.2 路由可觀測性

Fusion 路由決策需可審計:

1. **路由日誌**: 每次 Fusion 路由決策記錄至 `evolution/cost-log.jsonl`（task, signal, route chosen, model, cost, outcome）
2. **A/B 測量計畫**: 2 週 Fusion-vs-non-Fusion A/B 對照,同類任務量測實際節省（非模擬）
3. **路由決策回放**: 錯誤路由可追溯原因（複雜度信號誤判 / sidekick 能力不足 / 任務分類錯誤）

### 6b.3 驗證成本量化

main agent 機械重驗 sidekick 輸出本身有 token 成本,未包含在 -35.2% 模擬中。

| 任務類型 | 驗證方式 | 估算驗證 token | 對節省的影響 |
|---------|---------|-------------|------------|
| 單檔小改 | 無需（T0 親做） | 0 | 無影響 |
| 跨模組重構 | diff review | ~2000 input + 500 output | 增加 ~$0.017,節省從 -36% 變 -38%（略加劇） |
| 深度研究 | citation check + scope verify | ~3000 input | 增加 ~$0.015,節省從 37% 降至 ~34% |
| 安全審查 | adversarial re-check | ~5000 input + 1000 output | 增加 ~$0.040,成本增從 -18% 變 -29%（顯著加劇） |
| 大規模遷移 | spot-check 10% | ~3000 input per PR x 16 | 增加 ~$0.048,節省從 53% 降至 ~50% |

**結論**: 驗證成本壓縮深度研究和大規模遷移的節省 ~3pp,但顯著加劇安全審查的成本增加。修正後成本加權節省預估從 -35.2% 降至約 -31%。

---

## 附錄:關鍵文件指針

| 項目 | 路徑 |
|------|------|
| Devin Fusion scored 文章 | `research/ai-articles/scored/2026-07-02-cognition-devin-fusion-sidekick-routing.md` |
| Devin Fusion DAILY-RESEARCH | `research/DAILY-RESEARCH/2026-07-02.md` Topic 2 |
| multi-mode-skill 設計 | `.claude/skills/multi-mode-skill/SKILL.md` |
| multi-mode-agent 設計 | `.claude/agents/multi-mode-agent.md` |
| multi-mode 設計報告 | `research/reports/archive/2026-06-12-multi-mode-agent-skill-design.md` |
| 委派守則 | `.claude/refs/delegation-protocol.md` |
| 模型對應表 | `.claude/refs/model-profiles.md` |
| Context 管理 | `.claude/rules/context-management.md` |
| Sub-agent 策略 | `.claude/rules/subagent-strategy.md` |
| Factory Mixed Models | `https://docs.factory.ai/cli/configuration/mixed-models.md` |
| Factory Router | `https://docs.factory.ai/web/factory-router.md` |
| Factory Custom Droids | `https://docs.factory.ai/cli/configuration/custom-droids.md` |
| Factory Session API | `https://docs.factory.ai/api-reference/sessions/update-a-session.md` |
| Devin Fusion 原始博客 | `https://cognition.com/blog/devin-fusion` |
