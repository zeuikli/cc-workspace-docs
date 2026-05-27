---
title: "AI 內容評分系統"
type: documentation
---

# AI 內容評分系統

> 本檔涵蓋兩套評分系統，適用不同類型的研究產出：
> - **§1 文章評分** — 單篇 AI 文章，由 `/score-article` 和 `/twitter-research` Skill 引用
> - **§2 Synthesis 報告評分** — 週報 / 季報型 synthesis，手動執行

---

## §1 文章評分（單篇）

> **Manual-only by design.** 沒有自動觸發；只在判斷文章值得深度處理時手動執行。
> **Cadence**：遇到值得的 AI / LLM / Claude Code 文章時 → 人工觸發 `/score-article` skill。
> **Pipeline**：`score-article` → 填模板 → 算加權 → 若 > 6 依 decision tree 提升為 SKILL / Agent / Rule → 記錄到 `scored/<date>-<slug>.md`。
> **產出紀錄**：當前 3 個已評分檔案全數成功轉化（`bugfix` skill / `anthropic-insights` rule / `skill-authoring` rule）。

每篇新增文章須先評分，分數 > 6 才考慮整合進 Workspace。

### 評分維度（各維度 1-10 分）

| 維度 | 權重 | 說明 |
|------|------|------|
| **A. Workspace 可行動性** | 30% | 能否直接在 cc-workspace 套用？產出具體 prompt / 工具 / 流程改善 |
| **B. 創新性** | 20% | 是否提出現有 Skills/Agents 未涵蓋的思路或方法？ |
| **C. 證據品質** | 20% | 是否有實驗數據、可重現的結果、真實測試？ |
| **D. 技術深度** | 15% | 細節夠嗎？能否直接參照實作？ |
| **E. 泛化性** | 15% | 是否跨任務 / 跨 codebase 通用，而非高度特化情境？ |

**加權總分** = A×0.3 + B×0.2 + C×0.2 + D×0.15 + E×0.15

### 整合決策樹（分數 > 6 才進入）

```
分數 > 6？
├── No  → 歸入 inbox/low-score/，記錄原因，不整合
└── Yes → 判斷整合方式：
    │
    ├── 核心是「靜態提示詞 / 方法論」（單一呼叫即可執行）
    │   └── → SKILL（.claude/skills/<name>/prompt.md）
    │       觸發詞：「/<name>」或描述詞
    │
    ├── 核心是「多步驟自主流程」（需要迭代、工具呼叫、決策）
    │   └── → Agent（.claude/agents/<name>.md）
    │       整合進 subagent-strategy.md 委派規則
    │
    └── 核心是「通用原則 / 規則」（適用所有任務）
        └── → 更新 .claude/rules/ 相關規則檔案
```

### 評分模板

複製下方模板到 `scored/<date>-<slug>.md`：

```markdown
## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | X/10 | ... |
| B. 創新性 | X/10 | ... |
| C. 證據品質 | X/10 | ... |
| D. 技術深度 | X/10 | ... |
| E. 泛化性 | X/10 | ... |
| **加權總分** | **X.X/10** | |

**整合決策**：[SKILL / Agent / Rule / 不整合]  
**整合位置**：`.claude/skills/<name>/` 或 `.claude/rules/<name>.md`  
**整合狀態**：[待實作 / 已完成 / 不適用]
```

---

## §2 Synthesis 報告評分

> **用途**：評估 `research/ai-news/` 中的 synthesis 報告，決定是否值得整合到 career-wiki。
> **適用範圍**：僅 synthesis 檔案（`synthesis-*.md`、`synthesis-q*.md`）；日報與原始日誌不在評分範圍。
> **觸發方式**：手動執行（每新增一份 synthesis 後評分一次）。

### 評分維度（各 0-10 分，加權）

| 維度 | 權重 | 說明 |
|------|------|------|
| **1. 覆蓋廣度 Coverage** | 20% | 來源數、文章數、主題類別數；是否有跨類別話題熱度矩陣 |
| **2. 洞見品質 Insight** | 30% | 有無超越「標題彙整」的獨特角度、跨文章連結、趨勢判斷、反常識觀點 |
| **3. 可行動性 Actionability** | 25% | SRE / DevOps / 架構師視角，行動清單能否直接轉為待辦？有無分時程（短/中/長期）？ |
| **4. 時效性 Timeliness** | 15% | 距今多久？資訊是否仍有效？週報 vs 季報的衰減曲線不同 |
| **5. 格式品質 Format** | 10% | 有無目錄、表格、跨來源矩陣、時間線；一致性與可導航性 |

**加權總分** = Coverage×0.20 + Insight×0.30 + Actionability×0.25 + Timeliness×0.15 + Format×0.10

### 決策樹

```
加權總分 ≥ 8.0？
├── Yes → 推薦整合到 career-wiki
│         └── 確認對應 page（見評分記錄的「整合建議」）
│             → 更新 wiki page 的 Last Ingested + 補充 Lessons
│
├── 7.0-7.9 → 留存為參考資料
│             → 在對應 wiki page 的「Reference」欄標記本 synthesis 路徑
│             → 下次 wiki ingest 時優先讀取
│
└── < 7.0 → 保留但不推薦主動閱讀
             → 無需整合 wiki
```

### 評分模板

複製下方模板用於新增 synthesis 評分：

```markdown
---

## [YYYY-MM-DD / QN-YYYY] `<檔名>`

> **期間**：YYYY-MM-DD ~ YYYY-MM-DD | **來源**：N 個 | **文章**：N 篇

| 維度 | 分數 | 評分理由（具體引用 synthesis 中的章節/表格/數量） |
|------|------|--------------------------------------------------|
| 1. Coverage | X/10 | ... |
| 2. Insight | X/10 | ... |
| 3. Actionability | X/10 | ... |
| 4. Timeliness | X/10 | ... |
| 5. Format | X/10 | ... |
| **加權總分** | **X.X/10** | Coverage×0.20 + Insight×0.30 + Actionability×0.25 + Timeliness×0.15 + Format×0.10 |

**決策**：[整合 wiki / 留存參考 / 不推薦]
**相關 wiki pages**：[頁面名稱清單]
```

### 評分記錄

---

#### 2026-04-25 `2026-04/synthesis-2026-04-25.md`

> **期間**：2026-04-19 ~ 2026-04-25 | **來源**：16 個 | **文章**：57 篇

| 維度 | 分數 | 評分理由 |
|------|------|---------|
| **1. Coverage** | 9/10 | 16 來源 / 57 文章 / 7 主題（前沿模型、Agentic 架構、開源、產品經濟學、地緣政治、物理 AI、組織革命）；附 13 欄位話題熱度矩陣（§跨來源話題熱度矩陣）+ 「各來源獨家角度」表格覆蓋 14 個來源。唯一缺口：無學術 arxiv 層；-1 |
| **2. Insight** | 8/10 | 三項高價值非標題洞見：(1) Wisely Chen harness bug post-mortem 揭示「模型層 ≠ harness 層 ≠ API 層」的分層失效（§主題二工程啟示）；(2) AI 訂閱制走向「soft limit + 超量計費」的結構性預測（§主題四）；(3) Kimi K2.6 300 parallel agents 開源 Agent Swarm 架構對 multi-agent 設計的意義（§主題二）。弱點：話題廣但交叉連結較少（各主題彼此孤立分析）；-2 |
| **3. Actionability** | 9/10 | 「工程師行動清單」精確分三期（本週 / 本月 / 本季），共 9 條 checkbox 可直接轉 TODO：升級 Claude Code v2.1.116+、審查 system prompt token 成本（含具體 token 類型分類）、建立 harness regression test suite、規劃 CLI vs MCP 路徑。每條附具體技術根據，非空泛建議；-1 因缺少優先級排序（9 條全部同層） |
| **4. Timeliness** | 10/10 | 生成日期 2026-04-25，與評分當日同步（今日報）；本週所有事件（GPT-5.5 發布、DeepSeek V4 發布、Google $40B 投資）均屬現時最新；無衰減 |
| **5. Format** | 9/10 | 含 10 節目錄（錨點連結）、4 個表格（本週大事件 / 模型排行 / Token 計費倍率 / 融資戰）、話題熱度矩陣（16 來源 × 13 話題）、ASCII 架構圖（2 處）、事件時間線；格式完備，可導航。-1 因「各來源獨家角度」表格缺少「最值得讀的文章」連結（無法直接跳轉到原始 digest） |
| **加權總分** | **9.0/10** | 9×0.20 + 8×0.30 + 9×0.25 + 10×0.15 + 9×0.10 = 1.80 + 2.40 + 2.25 + 1.50 + 0.90 = **8.85 ≈ 9.0** |

**決策**：整合 wiki（分數 ≥ 8.0）
**相關 wiki pages**：`karpathy-ai-orchestration`、`finops-cross-position-patterns`（token 成本策略）、待建 `agentic-architecture-patterns`（harness 分層 + multi-agent swarm）

---

#### Q1 2026 `q1-2026/synthesis-q1-2026.md`

> **期間**：2026-01-01 ~ 2026-03-31 | **來源**：13 個 | **文章**：155 篇

| 維度 | 分數 | 評分理由 |
|------|------|---------|
| **1. Coverage** | 8/10 | 13 來源 / 155 文章 / 7 主題（代理成熟化、開源分化、推理效率、本地部署、多代理治理、物理 AI、訂閱制危機）；附 7 主題 × 13 來源的話題熱度矩陣（§3）+ Q1 重大事件時間線（§4）+ 各來源定位表（§5）。來源較週報少 3 個（Decoder、The Neuron、One Useful Thing 等週報有的 Q1 未涵蓋），-2 |
| **2. Insight** | 9/10 | 三項高品質跨文章洞見：(1) 執行摘要明確點出「模型競賽 → 代理編排」的本質轉移，而非逐條彙整（§1 Executive Summary）；(2) 本地部署經濟反轉時刻量化分析（Qwen 3.6-27B on-prem 3年 TCO $4.7k vs API $22.5k，§2.4）；(3) 訂閱制危機根因：平台挪用訂閱戶算力做實驗 + One Useful Thing「Harness 層成為控制點」的連結（§2.7）。各主題有「工程師啟示」段落點明戰略意義；-1 因物理 AI 主題略顯薄弱（目前商業難度大，洞見密度低） |
| **3. Actionability** | 8/10 | 行動清單（§6）分三時程（0-2 週 / 1-3 個月 / Q2-Q3 2026），共 9 條，涵蓋 0-trust 沙箱化、四維評估框架試用、本地部署 TCO 建模、Harness 層投資等。品質高於週報的「根據是什麼」部分，每條均有來源 newsletter 名稱佐證；-2 因季報性質導致「0-2 週」行動清單有些已過期（例如 Anthropic Pentagon 事件是 2026-03-16） |
| **4. Timeliness** | 6/10 | Q1 2026 報告，覆蓋期結束於 2026-03-31，距評分日（2026-04-25）已 25 天；大部分趨勢判斷（代理成熟化、開源分化、本地 TCO）仍然成立，但部分具體事件（Anthropic Pentagon 移除、claude-code leak）已非新聞；-4 反映季報的天然衰減（非報告品質問題） |
| **5. Format** | 9/10 | 含 6 節目錄、執行摘要（§1）、話題熱度矩陣（★/◐/— 三層）、Q1 事件時間線表（§4）、各來源定位表（§5）、分時程行動清單（§6）；各主題均有「代表案例」+ 「工程師啟示」的一致結構。-1 因缺少跨主題的「本季最重要的 3 個決策點」摘要（需讀完整 6 節才能萃取） |
| **加權總分** | **8.1/10** | 8×0.20 + 9×0.30 + 8×0.25 + 6×0.15 + 9×0.10 = 1.60 + 2.70 + 2.00 + 0.90 + 0.90 = **8.10** |

**決策**：整合 wiki（分數 ≥ 8.0）
**相關 wiki pages**：`karpathy-ai-orchestration`（代理成熟化 + 組系統思維）、`finops-cross-position-patterns`（本地 TCO 反轉分析）、待建 `agentic-architecture-patterns`（代理治理 + Harness 層控制點）

---

### 整合建議

> 基於上方兩篇 synthesis 的評分，以下是對 career-wiki 各 page 的更新建議。

#### 可立即更新的既有 wiki pages

| Wiki Page | 更新依據 | 具體補充內容 | 來源 synthesis |
|-----------|---------|------------|----------------|
| `karpathy-ai-orchestration` | 兩篇均高度相關（9.0 + 8.1 分） | 補充：(1) harness 層分層失效 post-mortem（模型≠harness≠API）；(2) 代理從 demo 走向生產的標誌性案例（2 名工程師 + AI = 8-10 人輸出）；(3) Kimi K2.6 Agent Swarm 300 parallel agents 架構 | 2026-04-25 週報 §主題二、Q1 §2.1 |
| `finops-cross-position-patterns` | Token 成本策略 + 本地 TCO 反轉 | 補充：(1) Token taxonomy（輸入 1x / 輸出 2-6x / Reasoning 15x / Cached 0.1-0.3x）；(2) Qwen 3.6-27B on-prem 3 年 TCO $4.7k vs API $22.5k 量化案例；(3) 訂閱制走向 soft limit 的結構性預測 | 2026-04-25 週報 §主題四、Q1 §2.4 §2.7 |

#### 建議新建的 wiki page

| 新 Page 名稱 | 分類 | 觸發理由 | 核心內容來源 |
|-------------|------|---------|------------|
| `agentic-architecture-patterns` | AI / Orchestration & Engineering Practice | 兩篇 synthesis 均出現「harness 分層」+「multi-agent 治理」+「0-trust tool invocation」三個高密度工程洞見，現有 `karpathy-ai-orchestration` 偏向概念性，缺乏具體架構模式 | 2026-04-25 週報 §主題二（CLI vs MCP、harness bug）；Q1 §2.5（多代理治理缺口、沙箱驗證） |

#### 優先順序建議

1. **優先**：更新 `karpathy-ai-orchestration`（最多覆蓋、兩篇均高度相關）
2. **次優**：新建 `agentic-architecture-patterns`（兩篇均觸及，且現有 wiki 缺口明顯）
3. **選做**：更新 `finops-cross-position-patterns`（TCO 數字有價值，但可等下次 wiki ingest session）
