# Harness Engineering: Leveraging Codex in an Agent-First World

**原始來源**：https://openai.com/index/harness-engineering/  
**作者**：Ryan Lopopolo（OpenAI Member of Technical Staff）  
**發表日期**：2026-02-11  
**評分日期**：2026-05-05

---

## 繁體中文全文摘要

### 核心命題

OpenAI 內部實驗：以 3 位工程師（後擴至 7 位）驅動 Codex Agents，在 5 個月內用 **零行手寫代碼** 建立並部署了一個擁有 **百萬行代碼** 的真實內部產品，開出 ~1,500 個 PR，吞吐量達每位工程師每天 3.5 個 PR。

**核心哲學**：人類掌舵（設計、規格、驗收）；Agent 執行（寫碼、測試、PR、review、merge）。

### 工程師角色的重新定義

傳統角色 → Agent-first 角色的轉變：

- **傳統**：直接撰寫代碼
- **Agent-first**：設計環境、指定意圖、建立反饋循環

當 Agent 失敗時，問題從不是「再試一次」，而是：「**缺少什麼能力？如何讓這個能力對 Agent 可見且可執行？**」

### 知識庫設計：把 AGENTS.md 當目錄，不是手冊

最重要的架構決策之一：**短 AGENTS.md（約 100 行）作為 table of contents，真正的知識住在結構化 docs/ 目錄**。

失敗的「一個大 AGENTS.md」的四個問題：
1. **Context 是稀缺資源**：一個巨大指令檔案擠壓了任務、代碼和相關文件
2. **過多指引變成無指引**：當一切都「重要」，就沒有什麼重要
3. **立即過時**：單體手冊變成陳舊規則的墓地
4. **無法機械驗證**：無法進行覆蓋率、新鮮度、交叉連結等檢查

```
AGENTS.md（100 行 map）
ARCHITECTURE.md
docs/
├── design-docs/（索引 + 核心信念）
├── exec-plans/（active/ completed/ 技術債追蹤）
├── generated/（db-schema.md）
├── product-specs/
└── references/（llms.txt 格式）
```

### 應用程式可讀性（Application Legibility）

讓 Codex 可以直接與應用程式互動：
- **每個 git worktree 可啟動獨立 app 實例**：Codex 可並行處理多個變更
- **Chrome DevTools Protocol 整合**：Codex 可截圖、觀察 DOM、驗證 UI 行為
- **本地 observability stack（Victoria Logs/Metrics）**：讓「確保 API 在 800ms 內完成」這樣的指令可執行

Codex 可以在 agent 不間斷運行長達 **6 小時**（通常在工程師睡覺時）。

### 架構強制執行：黃金原則

不微管理實作方式，但強制執行不變量（invariants）：

- 每個業務領域有固定層次（Types → Config → Repo → Service → Runtime → UI）
- 嚴格的依賴方向，由自定義 linter 機械性執行
- Cross-cutting concerns（auth、telemetry）透過 Providers 單一介面進入

**Agent-first 時代的架構規律**：在人類主導的工作流中，這些規則顯得迂腐；但在 Agent 主導時，它們是速度不衰減的倍增器。

### 垃圾回收機制（Entropy Management）

Agent 複製現有模式，包括不良模式，最終導致漂移（drift）：

- **以前**：每週五花 20% 的時間清理「AI slop」，無法擴展
- **現在**：Golden Principles 寫入 repo，定期 background Codex 任務掃描偏差、更新品質分數、開 refactoring PR

「技術債是高利率貸款：持續小增量還債遠比讓它複利然後痛苦清算更好。」

### 全自動化端到端能力

成熟後，一個提示詞可讓 Codex 完成：
1. 驗證當前代碼庫狀態
2. 重現回報的 bug，錄製影片
3. 實作修復，再錄影片驗證
4. 開 PR，回應 agent/human 反饋
5. 偵測並修復 build 失敗
6. 只在需要人類判斷時才上升報告
7. 合併

### 對 Workspace 的啟示

1. **AGENTS.md 作為目錄**：cc-workspace 的 CLAUDE.md 應保持精簡（100 行內），詳細規則用 @-import 按需載入，與本文發現完全一致。
2. **知識必須住在 repo**：Slack 討論、口頭約定對 Agent 不可見 = 不存在。所有架構決策應提煉為 markdown（docs/、`.claude/refs/`）。
3. **黃金原則 + 機械性執行**：linter rules、pre-commit hooks 是 Agent 的護欄，比口頭指令更可靠。
4. **Progressive disclosure**：docs/ 分層索引、skills 按需載入 — 這正是 cc-workspace 的設計。

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 9/10 | AGENTS.md 目錄化、docs/ 知識庫設計、垃圾回收機制均直接可套用 |
| B. 創新性 | 8/10 | 零手寫代碼的完整工程實驗，「知識必須住在 repo」的認識論突破 |
| C. 證據品質 | 9/10 | 真實產品，百萬行代碼，1,500 PR，數百內部用戶，5 個月實驗 |
| D. 技術深度 | 9/10 | 架構圖、層次設計、linter 機制、observability stack 均有詳細說明 |
| E. 泛化性 | 8/10 | 核心模式（精簡 AGENTS.md、層次化 docs、機械性約束）普遍適用 |
| **加權總分** | **8.65/10** | 9×0.3 + 8×0.2 + 9×0.2 + 9×0.15 + 8×0.15 = 2.7+1.6+1.8+1.35+1.2 |

**整合決策**：Rule  
**整合位置**：`.claude/rules/core.md` 或 `.claude/refs/anthropic-insights.md`  
**整合狀態**：待實作

**TODO**：
- 在 CLAUDE.md 中強化「AGENTS.md 作為目錄」的明確說明
- 參考 Golden Principles 概念，將「黃金不變量」加入 core.md 的「外科刀式修改」章節
- 考慮建立 doc-gardening 型 Agent（定期掃描過時文件）
