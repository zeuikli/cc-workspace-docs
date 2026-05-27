---
title: "Harness Engineering — AI 代理框架設計深度研究報告"
date: 2026-05-17
type: report
---

# Harness Engineering — AI 代理框架設計深度研究報告

**日期**：2026-05-17 | **字元數目標**：≥ 10,000  
**主要來源**：https://walkinglabs.github.io/learn-harness-engineering/zh-TW/ 及 12 個延伸來源  
**研究問題**：如何系統化設計 AI 代理的工程基礎設施（Harness），使其從「能力強」升級為「執行可靠」？

---

## 執行摘要

Harness Engineering（框架工程）是 2025–2026 年 AI 工程最重要的範式轉移：重點不在於選用哪個模型，而在於圍繞模型建立什麼樣的工程基礎設施。核心洞察是「有能力的模型 + 糟糕的 Harness」遠不如「普通的模型 + 優秀的 Harness」。

五個關鍵發現：

1. **65% 的企業 AI 失敗源自 Harness 缺陷**，而非模型本身能力不足（Augment Code 研究，2025）。
2. **Harness 優化帶來 12–42 pp 的性能提升**，超過大多數模型升級的幅度（MindStudio 5-benchmark 研究）。
3. **Repository 即唯一事實來源**：代理看不到的知識不存在，倉庫外的資訊等同於不存在。
4. **驗證循環是生產環境的分水嶺**：無驗證的代理自評準確性接近零；有完整驗證循環的代理品質提升 2–3 倍。
5. **AGENTS.md 一個檔案可能比換一個更貴的模型更有效**——最高槓桿的工程介入點。

---

## 1. 背景與動機

### 1.1 能力與可靠性的根本落差

現代 LLM 在各種基準測試上表現卓越：GPT-4、Claude Opus 在 SWE-bench Verified 通過率達 50–76.8%。但在真實工程任務中——需求模糊、測試缺失、環境複雜——同一個模型的表現可能天差地別。

Anthropic 內部做了一個關鍵實驗：使用 **同一個模型**（Claude Opus 4.5）完成同一個任務：

| 環境 | 時間 | 成本 | 結果 |
|------|------|------|------|
| 裸跑（無 Harness） | 20 分鐘 | $9 | 無法運行的代碼 |
| 完整 Harness（三代理架構） | 6 小時 | $200 | 生產品質代碼 |

模型不變，基礎設施改變了一切。這個實驗揭示了「能力鴻溝」的本質：問題不在模型，在環境。

### 1.2 OpenAI 的百萬行代碼實驗

OpenAI 讓 Codex 在五個月內生成約 100 萬行生產代碼、完成 1,500 個 PR，僅用三名工程師。這不是靠更好的模型——Codex 本身不比當時市場其他頂級模型強——而是靠系統化的 Harness 設計：明確的工具配置、驗證流程、進度追蹤機制。

### 1.3 Harness Engineering 的定義邊界

Harness = **模型權重之外的一切工程基礎設施**。

區分三個相關但不同的概念：

| 概念 | 範圍 | 典型工具 |
|------|------|---------|
| **Prompt Engineering** | 單次對話的輸入優化 | System prompt、few-shot |
| **Context Engineering** | 模型在對話中看到什麼 | RAG、壓縮、工具輸出過濾 |
| **Harness Engineering** | 整個執行環境設計 | AGENTS.md、驗證循環、狀態管理、工具集 |

Harness Engineering 是上層抽象，包含 Context Engineering 和 Prompt Engineering，但遠不止於此。

---

## 2. 核心概念分析

### 2.1 代理失敗的五層防禦模型

`walkinglabs.github.io` 的第一講提出了代理失敗的五大根源，可以理解為**五層防禦**：

**第一層：任務規格（Task Specification）**
- 失敗模式：「加個搜索功能」——含義模糊，代理自行猜測
- 防禦手段：明確的完成定義（可機器驗證）、acceptance criteria、分解子任務

**第二層：脈絡供給（Context Provision）**
- 失敗模式：技術棧約定、架構決策、隱性規範僅存於人腦或 Slack
- 防禦手段：AGENTS.md / CLAUDE.md、ARCHITECTURE.md、CONSTRAINTS.md

**第三層：執行環境（Execution Environment）**
- 失敗模式：依賴缺失、版本不配對、環境未初始化
- 防禦手段：依賴鎖檔（package-lock.json、pyproject.toml）、init.sh 腳本、容器化

**第四層：驗證回饋（Verification Feedback）**
- 失敗模式：無測試或驗證命令，代理靠主觀判斷宣告「任務完成」
- 防禦手段：完整的驗證命令清單、CI gates、結構化錯誤訊息

**第五層：狀態管理（State Management）**
- 失敗模式：超 30 分鐘的長任務失去上下文，重複探索浪費 token
- 防禦手段：PROGRESS.md、git checkpoint、session handoff 機制

診斷方法：每次失敗時，將原因**對應到具體一層**，在那一層修復，而非盲目換更強的模型。

### 2.2 Harness 五子系統模型

`walkinglabs.github.io` 第二講用「餐廳廚房」比喻，系統化地定義 Harness 的五個子系統：

```
餐廳廚房比喻
├── 菜譜架（指令子系統）     → AGENTS.md / CLAUDE.md
├── 刀具架（工具子系統）     → Shell、編輯器、瀏覽器、MCP Server
├── 灶臺（環境子系統）       → 依賴鎖檔、版本管理、容器配置
├── 備菜臺（狀態子系統）     → PROGRESS.md、feature_list.json
└── 出菜檢查口（反饋子系統） → 測試、type check、lint、E2E
```

**子系統評估矩陣**（每項 1–5 分）：

| 子系統 | 評估問題 | 低分症狀 | 高分表現 |
|--------|---------|---------|---------|
| 指令 | 代理是否知道「做什麼、怎麼做、邊界在哪」？ | 需反覆澄清 | 冷啟動即可作業 |
| 工具 | 代理能否完成任務所需的每個操作？ | 工具缺失或過多 | 最小充分集合 |
| 環境 | 環境是否自描述可重現？ | 「在我機器上可以」 | init.sh 一鍵啟動 |
| 狀態 | 跨會話後代理能否從中斷點繼續？ | 每次重新開始 | 進度無損切換 |
| 反饋 | 代理能否從錯誤中自我修正？ | 宣告完成即終止 | 驗證失敗→自我修復 |

**關鍵原則**：逐個移除子系統進行「等模型對照實驗」，量化每個子系統的邊際貢獻。一個 TypeScript+React 團隊僅靠完善五個子系統（模型不變），成功率從 20% 升至近 100%。

### 2.3 Repository 即唯一事實來源

第三講提出的核心原則：**AI 代理只能訪問系統提示、任務描述、倉庫檔案和工具輸出**，它無法查閱 Slack、Confluence、Jira、人腦中的知識。因此，倉庫外的資訊等同於**不存在**。

**知識可見性缺口（Knowledge Visibility Gap）**：
```
KVG = 倉庫外重要知識數量 / 總重要知識數量
目標：KVG < 10%
```

**冷啟動測試（Cold Start Test）**——評估倉庫品質的黃金標準：

開啟一個全新的代理會話，僅使用倉庫內容，驗證它能否回答：
1. 這是什麼系統？
2. 系統如何組織？
3. 如何運行？
4. 如何驗證？
5. 當前進度是什麼？

任何無法回答的問題，就是倉庫的空白，就是代理失敗的風險點。

**ACID 原則應用於代理狀態管理**：

| ACID 原則 | 傳統資料庫 | AI 代理應用 |
|-----------|-----------|-----------|
| **Atomicity** | 事務全成功或全回滾 | 每個邏輯操作一個 git commit，失敗時 `git stash` |
| **Consistency** | 事務後資料符合規則 | 每個 commit 前驗證：測試通過、lint 乾淨 |
| **Isolation** | 並發事務互不干擾 | 多代理並發時用獨立 PROGRESS.md 或獨立 git 分支 |
| **Durability** | 持久化存儲 | 關鍵知識用 git 追蹤；臨時狀態可存會話記憶 |

### 2.4 Model-Harness Fit（模型-框架適配）

2026 年出現的重要新概念：**模型是針對特定 Harness 進行 post-training 的**，因此「模型能力」不是絕對值，而是在特定 Harness 下的表現。

Terminal-Bench 2.0 數據：
- Claude Opus 4.6 + ForgeCode Harness = **79.8%**
- Claude Opus 4.6 + Capy Harness = **75.3%**
- **同一個模型，不同 Harness，差 4.5 pp**

啟示：選擇 Harness 時不只是選工具，而是選擇模型的「工作環境」，需要匹配模型的預訓練偏好。

---

## 3. 最佳實踐與實作模式

### 3.1 AGENTS.md 設計黃金法則

AGENTS.md（或 CLAUDE.md）是 Harness 中「最高效益投資比」的組件，它是代理的「員工手冊」，在每次會話開始時注入到代理的上下文中。

**內容原則**（HumanLayer blog, 2026）：

| 應該包含 | 不應包含 |
|---------|---------|
| 代理無法從代碼推斷的 bash 命令 | 可以從代碼中發現的標準慣例 |
| 非標準代碼風格規則 | 詳細的 API 文件 |
| 測試偏好和測試執行器 | 逐檔案描述 |
| 倉庫架構約定 | 可用 `ls` 發現的目錄結構 |
| 環境特殊配置和陷阱 | AI 生成的冗余內容 |

**ETH Zurich 研究警告**：AI 自動生成的 AGENTS.md 內容實際上**降低**代理性能——應由人工精心撰寫，每一行都必須有可追溯的失敗案例或硬約束作為依據。

**結構模板**（≤100行）：
```markdown
# AGENTS.md

## 專案概覽
[一句話描述：這是什麼系統、主要用途]

## 技術棧
- 語言：TypeScript 5.x + React 18
- 套件管理：pnpm（不用 npm 或 yarn）
- 測試框架：Vitest + Playwright

## 快速啟動
```bash
pnpm install
pnpm dev       # 開發伺服器：http://localhost:3000
pnpm test      # 單元測試
pnpm typecheck # 型別檢查
```

## 驗證命令（完成前必須全部通過）
```bash
pnpm test && pnpm typecheck && pnpm lint
```

## 硬約束
- 禁止修改 /src/db/migrations/ 目錄（需 DBA 審查）
- API 錯誤必須使用 /src/utils/errors.ts 中定義的類型
- 新功能必須有對應的 Vitest 測試

## 當前進度
→ 見 PROGRESS.md
```

**Mnilax 12 規則研究**：CLAUDE.md 超過 200 行時，合規率從 76% 跌至 52%；超過 14 條規則後出現顯著 compliance 下降。**保持精簡比追求完整更重要**。

### 3.2 驗證循環設計（最高 ROI 組件）

Boris Cherny（Claude Code 主要開發者）明確說明：**驗證循環是單一最高效優化**，能將結果品質提升 2–3 倍。

**三種驗證層次**：

**層一：確定性驗證（Computational）**
- 特性：毫秒級，100% 可重現
- 工具：測試套件、型別檢查、linter、建構
- 設計要點：錯誤訊息應包含**修復指引**，不只是「違規偵測」

```bash
# 好的錯誤訊息
✗ API 錯誤類型錯誤
  使用 logger.error({ event: 'api_error', message, statusCode }) 取代直接 throw Error(message)
  → 見 /src/utils/errors.ts 第 23-45 行

# 差的錯誤訊息  
✗ 違規偵測
```

**層二：語義驗證（Inferential）**
- 特性：較慢（秒級），非確定性但語義豐富
- 工具：LLM 代碼審查、語義分析、架構適配性檢查
- 適用場景：架構層面的符合性、跨服務依賴驗證

**層三：E2E 驗證（End-to-End）**
- 特性：完整行為驗證
- 工具：Puppeteer MCP、Playwright、截圖比對
- Anthropic 案例：透過瀏覽器自動化工具大幅降低「feature 標記完成但實際不工作」的情況

**Plan-Execute-Verify (PEV) 循環**——現代 Harness 的核心架構模式：

```
PEV 循環
┌─────────────────────────────────────────┐
│  PLAN                                   │
│  ├─ 明確問題分解                         │
│  ├─ 寫出 acceptance criteria             │
│  └─ 列出驗證命令                         │
├─────────────────────────────────────────┤
│  EXECUTE                                │
│  ├─ 在驗證標準約束下執行                  │
│  ├─ 每個子任務完成後 git commit           │
│  └─ 遇到阻礙時停止重規劃                  │
├─────────────────────────────────────────┤
│  VERIFY                                 │
│  ├─ 執行所有驗證命令                      │
│  ├─ 確認每個 acceptance criteria 通過     │
│  └─ 有錯誤→返回 EXECUTE 修復              │
└─────────────────────────────────────────┘
```

### 3.3 多會話連續性設計

長任務（超過 30 分鐘）中代理失敗率急升，原因是上下文丟失。解決方案是**外化記憶**：

**必要檔案組合**（Anthropic 建議的最小 Harness 包）：

```
project/
├── AGENTS.md              # 靜態知識（技術棧、約束、驗證命令）
├── feature_list.json      # 功能追蹤（初始全部標記為 "failing"）
├── claude-progress.md     # 動態進度（每會話更新）
└── init.sh               # 環境初始化腳本
```

**feature_list.json 設計**：
```json
{
  "version": "1.0",
  "features": [
    {
      "id": "feat-001",
      "name": "使用者登入",
      "status": "passing",
      "last_verified": "2026-05-17",
      "verification_command": "pnpm test src/auth/login.test.ts"
    },
    {
      "id": "feat-002",
      "name": "搜索功能",
      "status": "failing",
      "priority": "high",
      "notes": "API 端點已建立，前端整合待完成"
    }
  ]
}
```

**重要原則**：feature_list.json 中的功能不得被刪除或修改為「略過」，只能從 failing 變 passing——這是防止代理「偷懶宣告完成」的核心機制。

**claude-progress.md 更新格式**：
```markdown
## Session 2026-05-17 14:30

### 完成
- feat-001: 使用者登入 ✓（pnpm test passing）
- feat-003: 首頁佈局 ✓

### 當前進行中
- feat-002: 搜索功能（已完成後端，整合前端中）

### 阻礙
- Elasticsearch 連接配置需要確認（@devops）

### 下一步
繼續 feat-002，完成後處理 feat-005 通知系統
```

### 3.4 初始化相位隔離（Lecture 06 核心概念）

**反模式**：將「初始化」與「實作」混合在同一個代理任務中。

**症狀**：代理花 80% 精力寫功能代碼，剩下 20% 隨便搭基礎設施，導致：
- 測試框架未驗證
- 進度追蹤缺失
- 隱性假設埋藏

**自舉契約（Bootstrap Contract）**：確保全新代理會話能無歧義操作的前提條件。

一個完整的初始化相位必須完成：
1. ✅ 環境可運行（`pnpm install && pnpm dev` 成功）
2. ✅ 測試框架可驗證（至少一個示例測試通過）
3. ✅ 進度追蹤設置（PROGRESS.md + feature_list.json 初始化）
4. ✅ 任務分解（所有功能列在 feature_list.json 中）
5. ✅ git checkpoint commit（基準點建立）

**投資回報**：Anthropic 研究數據顯示，初始化相位的時間投入在後續 3–4 個會話中完全收回，功能完成率提升 31%。

### 3.5 子代理設計（Context 隔離）

子代理（Subagent）的核心價值是 **Context 隔離**——防止探索過程的「噪音」污染主對話，避免 context rot（上下文隨長度增加而性能下降）。

Chroma 研究：模型在更長的 context 長度下性能下降，即使在簡單任務上也是如此。解決方案不是擴大 context window，而是**拆分成更小的子代理任務**。

**子代理設計原則**：
- 每個子代理有明確的輸入/輸出合約
- 子代理間通過檔案或 git 通信，不共享 context
- 子代理失敗返回父代理決策，不自我重試
- 最多同時啟動 4 個平行子代理（防止 context 過載）

---

## 4. 工具與生態系統比較

### 4.1 主流 Harness 工具決策框架

| 工具類型 | 使用時機 | 優點 | 風險 |
|---------|---------|------|------|
| **AGENTS.md** | 需要反覆傳遞的輕量資訊 | 零依賴、跨工具 | 過長時 compliance 下降 |
| **Skills/Prompts** | 可重用的命名知識或工作流 | 漸進式揭露 | 生態系統有 prompt injection 風險 |
| **MCP Servers** | 頻繁訪問外部認證服務 | 內建認證 | 過多工具降低代理能力 |
| **Subagents** | 有邊界的可平行化任務 | Context 隔離 | 協調開銷 |
| **Hooks** | 確定性、機械性的邏輯 | 格式化、linting 自動化 | 配置複雜度 |

**工具選擇原則**：先從 AGENTS.md 開始，只在 AGENTS.md 不夠用時才升級到更重量級的工具。

### 4.2 三大 Harness 架構比較

| | **Claude Code** | **OpenAI Codex** | **GitHub Copilot** |
|---|---|---|---|
| 記憶機制 | 同步檔案寫入 + `<system-reminder>` | Typed queue + `<oai-mem-citation>` 衰減 | JSON RPC + 遠端記憶後端 |
| 工具介面 | Edit（old/new diff） | apply_patch | 動態路由 |
| 狀態注入 | CLAUDE.md 每次重讀 | Structured memory injection | 遠端狀態拉取 |
| 多代理協調 | 父子層級，Agent 工具 | 隊列系統 | Routing 層 |

**Model-Harness Fit 啟示**：每個平台的 post-training 都針對其 harness 優化，跨平台移植同一個 AGENTS.md 不一定能獲得最佳效果。

### 4.3 來源評分（A-E 五維度）

| 來源 | A.可行動性 | B.創新性 | C.證據品質 | D.技術深度 | E.泛化性 | 加權分 |
|------|-----------|---------|-----------|-----------|---------|--------|
| walkinglabs 課程 | 9 | 7 | 7 | 8 | 9 | **8.1** |
| Anthropic 長任務文章 | 9 | 8 | 9 | 8 | 8 | **8.6** |
| Martin Fowler 文章 | 8 | 8 | 7 | 8 | 9 | **8.0** |
| AddyOsmani 文章 | 9 | 8 | 7 | 9 | 8 | **8.2** |
| Augment Code 指南 | 9 | 7 | 8 | 8 | 8 | **8.1** |
| MindStudio benchmark | 10 | 7 | 9 | 7 | 8 | **8.4** |
| HumanLayer blog | 9 | 7 | 7 | 8 | 8 | **7.9** |

加權公式：A×0.3 + B×0.2 + C×0.2 + D×0.15 + E×0.15

---

## 5. 常見陷阱與反模式

### 5.1 驗證缺口（Verification Gap）——最普遍的失敗

**症狀**：代理完成工作後宣告「任務完成」，但實際代碼有問題。

**根因**：缺乏可機器驗證的完成標準，代理靠主觀判斷（通常過於樂觀）。

**修復**：在任務開始前定義完成標準：
```
完成標準：
✓ pnpm test 全部通過（0 failures）
✓ pnpm typecheck 無錯誤
✓ 新功能有對應的 Vitest 測試（覆蓋率 > 80%）
✓ 在本地 dev server 手動驗證核心路徑
```

### 5.2 過時文件比缺失文件更危險

**症狀**：AGENTS.md 或 ARCHITECTURE.md 描述的是 6 個月前的架構。

**根因**：文件更新與代碼更新脫鉤。

**修復**：
1. 在 git hooks 或 CI 中加入「文件一致性檢查」
2. 文件更新與代碼變更放入**同一個 commit**
3. 每個 PR 的 checklist 包含「文件是否需要更新？」

### 5.3 工具過多症（Tool Obesity）

Vercel 的 v0 代理案例：移除 80% 的可用工具後，性能**顯著提升**。工具過多導致：
- 代理選擇錯誤工具
- context window 被工具描述佔據
- 代理在不確定時隨機嘗試工具

**修復**：每個工具都應該有明確的「它解決了哪個失敗案例」——無法回答則刪除。

### 5.4 AI 生成的 AGENTS.md

ETH Zurich 研究：讓 LLM 自動生成 AGENTS.md 實際上**降低代理性能**。AI 生成的內容往往：
- 過於通用（每個項目都一樣）
- 充斥冗余資訊
- 錯誤地重述代碼中已有的信息

**修復**：AGENTS.md 必須人工撰寫，每一行都需要有**真實失敗案例**或**硬約束**作為依據。

### 5.5 預防性 Harness 設計

**症狀**：花大量時間設計「可能需要」的 Harness 組件，但還沒有真實失敗。

**修復**：HumanLayer 原則——**只在失敗發生後才添加 Harness 組件**。丟棄沒有用到的配置比保留它更有價值。

> "一旦代理犯了錯，花時間設計解決方案，使代理永遠不再犯同樣的錯誤。" ——Mitchell Hashimoto

### 5.6 初始化與實作混合

**症狀**：第一個代理任務既要「設置環境」又要「實作功能」，兩者都做得不好。

**修復**：強制隔離為兩個相位：
1. 初始化相位：只做環境設置，建立 bootstrap contract
2. 實作相位：假設環境完整，只做功能開發

---

## 6. 前沿趨勢與預測

### 6.1 「如果 2025 年是代理之年，2026 年是 Harness 之年」

行業發現，**建立代理是容易的部分**，讓它可靠、可預測成本、在生產環境安全運行才是真正的工程挑戰。

### 6.2 Harness 即服務化（Harness-as-a-Service）

產業趨勢：從自建 Harness 到配置標準化框架：
- **Claude Agent SDK**（Anthropic）
- **Codex SDK**（OpenAI）
- **OpenAI Agents SDK**

這些 SDK 將 loop、工具、context 管理、hooks 作為提供的基礎設施，開發者只需配置而非自建。

### 6.3 Harness 走向動態化

當前 Harness 是靜態配置；未來方向：

**動態工具組裝（Just-in-Time Tool Assembly）**：根據任務類型動態組裝最小工具集，而非預先注入所有工具。

**可觀測性驅動的 Harness 自動演化（AHE）**：
arxiv 論文 2604.25850 提出了「Agentic Harness Engineering」概念——透過觀測代理行為模式，**自動識別哪些 Harness 組件需要調整**，形成 Harness 的持續演化機制。

### 6.4 模型與 Harness 的協同進化

現代頂級代理（Claude Code、Codex、GitHub Copilot）儘管使用不同底層模型，但在 Harness 設計上**開始收斂**：
- 都採用 Plan-Execute-Verify 循環
- 都使用 filesystem 作為基礎 primitive
- 都有某種形式的 session continuity 機制

這表明 Harness 設計模式正在從「各家特色」向「行業標準」演化。

### 6.5 Harness Coverage 評估成為新問題

Martin Fowler 的文章指出一個尚未解決的挑戰：如何評估 Harness 的**覆蓋率和品質**？

類比測試覆蓋率，未來可能出現：
- Harness Coverage Score（Harness 覆蓋率）
- Constraint Completeness（約束完整性）
- Verification Density（驗證密度）

---

## 7. 可立即實作的行動建議

### 優先級 1（立即執行，高確定性）

**1.1 建立冷啟動測試基準**（30分鐘內完成）
1. 開啟全新的代理會話
2. 測試代理能否回答五個基本問題（見第 2.3 節）
3. 記錄每個無法回答的問題——這就是今天的工作清單

**1.2 建立或修訂 AGENTS.md**（1小時內完成）
- 目標：≤100 行，通過冷啟動測試的全部五個問題
- 每一行必須能回答「這防止了哪個具體失敗？」
- 不要讓 AI 幫你生成初版

**1.3 添加驗證命令清單**（20分鐘）
在 AGENTS.md 底部明確列出：
```
## 完成標準（所有命令必須通過）
pnpm test && pnpm typecheck && pnpm lint
```

### 優先級 2（本週內，中期收益）

**2.1 建立 feature_list.json 和 PROGRESS.md**
按照第 3.3 節格式，初始化所有功能為 failing 狀態

**2.2 計算知識可見性缺口（KVG）**
列出所有重要的項目知識點，計算倉庫外的比例，目標降到 10% 以下

**2.3 建立 init.sh 腳本**
確保任何人、任何機器執行 `bash init.sh` 後能立即開始開發

### 優先級 3（本月內，長期投資）

**3.1 計算 Harness ROI**
記錄使用 Harness 前後的：
- 任務完成率（成功 PR / 嘗試任務數）
- 代碼回滾率（兩週內廢棄的代碼比例）
- 審查稅（AI 生成代碼的人工審查時間）

**3.2 建立 Harness 演化機制**
每次代理犯錯時，遵循 Mitchell Hashimoto 原則：
1. 分析失敗屬於五層中的哪一層
2. 在那一層添加對應的 Harness 組件
3. 更新 AGENTS.md 或驗證命令
4. 確認同樣的錯誤不再發生

---

## 8. 可應用的 Prompt 集

基於研究整理的 **14 個可直接使用的 Prompt**，涵蓋 Harness 設計的各個關鍵環節。

---

### Prompt 1：冷啟動測試 Prompt

```
你是一個全新加入項目的 AI 代理，沒有任何先前的上下文記憶。
請只使用倉庫中的檔案，回答以下五個問題：

1. 這是什麼系統？（一句話描述）
2. 系統如何組織？（主要目錄結構和職責）
3. 如何運行開發環境？（命令列表）
4. 如何驗證修改是正確的？（測試/驗證命令）
5. 當前的開發進度是什麼？（正在做什麼，剩下什麼）

對於每個無法回答的問題，標記為「MISSING」，說明缺少哪些資訊。
這些 MISSING 項目是代理在這個項目中工作的最大風險點。
```

**使用場景**：定期審計倉庫品質；新代理入職；評估 AGENTS.md 完整性。

---

### Prompt 2：AGENTS.md 審計 Prompt

```
你是一個有豐富 AI 代理工程經驗的資深工程師。
請審計以下 AGENTS.md 的品質：

[貼入 AGENTS.md 內容]

請評估：
1. 每一行是否能回答「這防止了哪個具體失敗？」如果不能，標記為 DEAD_WEIGHT
2. 是否包含代理可以從代碼中自己發現的冗余資訊？
3. 冷啟動測試的五個問題是否都有答案？
4. 是否超過 100 行？如超過，哪些內容可以移除？
5. 是否包含 AI 生成的填充內容（通用、放諸四海而皆準的建議）？

輸出：精簡後的 AGENTS.md（≤100行）+ 每個刪除決策的理由。
```

---

### Prompt 3：五層失敗診斷 Prompt

```
代理任務失敗了，需要分析根因。

失敗描述：[描述失敗情況]
失敗輸出：[代理的輸出或錯誤信息]

請對應到五層防禦模型進行診斷：

第一層：任務規格是否清晰？
- 任務描述是否模糊？是否有隱性假設？
- 完成標準是否可機器驗證？

第二層：脈絡是否充分？
- 代理是否缺少關鍵的架構知識？
- AGENTS.md 是否缺少關鍵資訊？

第三層：執行環境是否正確？
- 依賴是否完整？版本是否正確？
- init.sh 是否能成功執行？

第四層：驗證回饋是否有效？
- 代理是否有辦法知道自己的輸出是否正確？
- 錯誤訊息是否提供了足夠的修復指引？

第五層：狀態管理是否健全？
- 如果這是長任務，進度是否有正確持久化？
- 上一個會話的工作是否被正確繼承？

輸出：主要失敗層（1-5）+ 具體修復建議（以 Harness 改善為主，非換模型）。
```

---

### Prompt 4：驗證命令設計 Prompt

```
你是一個測試工程師，需要為這個項目設計完整的驗證命令集。

項目信息：
- 技術棧：[填入]
- 主要功能：[填入]
- 已有的測試：[填入]

設計規則：
1. 驗證命令必須是可在 CI 中執行的 bash 命令
2. 必須覆蓋：語法正確性、型別安全、邏輯正確性、整合正確性
3. 每個命令的執行時間應 < 60 秒（快速反饋）
4. 命令輸出應包含修復指引，而非只有錯誤代碼

輸出格式：
```bash
## 快速驗證（< 30s，每次修改後運行）
[命令]

## 完整驗證（< 3min，PR 前運行）
[命令]

## E2E 驗證（< 10min，合入前運行）
[命令]
```

同時提供：如何修改這些命令的錯誤訊息使其對 AI 代理更友好。
```

---

### Prompt 5：初始化相位 Prompt（用於全新項目）

```
你是一個 AI 代理，正在執行「初始化相位」——這是一個獨立的相位，
只關注搭建基礎設施，不進行任何功能開發。

初始化相位完成標準（你不能宣告完成，除非全部通過）：
□ 執行 npm install / pnpm install 成功
□ 執行 npm test（或等效命令）有至少一個示例測試通過
□ 執行 npm run dev（或等效命令）開發伺服器啟動成功
□ 創建 AGENTS.md，包含：專案概覽、技術棧、驗證命令、硬約束
□ 創建 feature_list.json，列出所有計劃功能，初始狀態均為 "failing"
□ 創建 claude-progress.md，記錄這次初始化的完成狀態
□ 執行 git commit，提交信息為 "chore: initialize harness infrastructure"

開始執行初始化相位。每完成一個檢查項，在對話中明確標記 ✅ 或 ❌。
只有全部為 ✅ 時，才可以在輸出中說「初始化完成」。
```

---

### Prompt 6：feature_list.json 生成 Prompt

```
請根據以下需求文件生成 feature_list.json：

[貼入需求文件或用戶故事]

格式要求：
- 每個功能有唯一 ID（feat-001, feat-002...）
- 包含字段：id, name, description, status (初始值 "failing"), priority (high/medium/low), verification_command
- verification_command 應是可以執行的 bash 命令，用於驗證該功能是否正常
- 功能粒度：每個功能應在 1-2 小時內可以完成和驗證

輸出完整的 feature_list.json，以及每個功能對應的驗證命令說明。

重要：功能列表一旦確定，後續只允許將 status 從 "failing" 改為 "passing"，
不允許刪除功能或將 "passing" 改回 "failing"，以防止代理假裝完成任務。
```

---

### Prompt 7：代理自我修正 Prompt

```
你剛才的輸出不符合預期，需要自我診斷並修正。

你的輸出：[代理的輸出]
驗證失敗的命令：[驗證命令]
驗證輸出：[完整的錯誤輸出，不要截斷]

診斷步驟（必須按順序執行）：
1. 分析錯誤訊息，找出根本原因（不是表面症狀）
2. 確認你理解了問題——用一句話描述根本原因
3. 確認修改計劃——列出你打算修改哪些內容，預期達到什麼效果
4. 執行修改
5. 再次運行驗證命令
6. 如果還是失敗，重複步驟 1-5，最多 3 次
7. 如果 3 次後仍失敗，輸出診斷報告（問題描述 + 已嘗試的方法 + 建議的人工介入）

禁止：
- 在驗證通過前宣告「已修復」或「完成」
- 移除、修改或跳過測試以使驗證通過
- 添加 try-catch 靜默錯誤
```

---

### Prompt 8：多會話繼承 Prompt

```
你正在接手上一個代理會話的工作。請執行以下初始化序列：

步驟 1：閱讀 AGENTS.md（確認項目技術棧和約束）
步驟 2：閱讀 claude-progress.md（確認上次做了什麼）
步驟 3：閱讀 feature_list.json（確認哪些功能已完成，哪些待完成）
步驟 4：運行 git log --oneline -10（確認最近的代碼狀態）
步驟 5：運行驗證命令確認當前代碼庫是健康的

初始化完成後，輸出：
- 當前狀態摘要（一段話）
- 今天計劃處理的功能（按 priority 選擇）
- 預計的完成標準

只有完成初始化序列後，才開始執行功能開發。
```

---

### Prompt 9：架構知識外化 Prompt

```
你是一個資深工程師，需要將項目的隱性知識顯性化到倉庫中。

知識可見性缺口評估——請列出以下類別的所有重要知識：

1. 技術決策（為什麼選這個技術棧？有哪些重要的技術取捨？）
2. 架構約束（有哪些「絕對不能做」的事情？為什麼？）
3. 業務規則（有哪些業務邏輯是代碼本身看不出來的？）
4. 環境配置（有哪些環境特殊性？新人容易踩哪些坑？）
5. 測試策略（如何判斷一個功能「完成了」？）

對每個項目，評估：
- 目前在哪裡？（倉庫 / Slack / 人腦 / 口頭傳承）
- 是否應該放入倉庫？（會影響代理工作品質嗎？）

輸出：KVG 計算 + 優先需要記錄到倉庫的前 10 項知識 + 建議的檔案位置。
```

---

### Prompt 10：Harness 迭代改進 Prompt

```
代理剛才犯了一個錯誤，根據 Mitchell Hashimoto 原則，
每次犯錯都是改進 Harness 的機會，確保永遠不再犯同樣的錯。

錯誤描述：[具體描述犯了什麼錯]

請分析：
1. 這個錯誤屬於五層防禦的哪一層？
2. 理想的 Harness 改進應該是什麼？（AGENTS.md 補充 / 新增驗證命令 / 約束規則 / 工具調整）
3. 這個改進是否可以被機器驗證（即：下次代理犯同樣的錯，能否被自動攔截）？

輸出：
- 具體的 Harness 改進草案（直接可用的格式）
- 驗證這個改進有效的測試方法
- 更新 AGENTS.md 的具體修改建議
```

---

### Prompt 11：代碼審查角色分離 Prompt

```
你現在扮演的角色是「驗證代理」，與實作代理完全分離。
你的唯一職責是驗證實作代理的輸出是否符合要求。

實作代理的工作：[描述實作代理完成的任務]
實作代理的輸出：[代碼或結果]
原始需求：[需求描述]
驗證標準：[acceptance criteria]

驗證清單：
□ 功能是否符合需求規格（每個 acceptance criteria 是否通過）？
□ 是否有邊界情況未處理？
□ 是否有潛在的安全問題？
□ 測試是否真正驗證了業務邏輯（而非只是讓代碼通過）？
□ 是否有「把測試改掉來通過」的跡象？

輸出格式：
PASS ✅ / FAIL ❌ + 具體原因
如果 FAIL，列出每個問題和建議的修復方向。
驗證代理不修改代碼，只輸出驗證報告。
```

---

### Prompt 12：長任務分解 Prompt

```
這個任務預計需要 2 小時以上才能完成，需要分解成可跨會話繼續的子任務。

任務描述：[完整任務描述]

請按照以下原則分解：
1. 每個子任務應在 30 分鐘內完成（適合單個代理上下文窗口）
2. 每個子任務完成後應有可驗證的 git checkpoint
3. 子任務間的依賴關係明確（哪些可以並行，哪些必須序列）
4. 每個子任務的輸入/輸出合約明確

輸出：
- 子任務列表（格式：id, name, description, estimated_time, depends_on, verification）
- 直接以 feature_list.json 格式輸出
- 初始化相位（如果環境尚未設置）應作為第一個子任務

後續代理應按此列表順序工作，每完成一個子任務更新 feature_list.json 的狀態。
```

---

### Prompt 13：Harness 品質基準測試 Prompt

```
請對這個項目的 Harness 進行系統化品質評分（各項 1-5 分）：

[提供 AGENTS.md 內容]
[提供 feature_list.json 結構]
[提供 PROGRESS.md 內容]

評分維度：

**指令子系統（AGENTS.md）**
□ 冷啟動五個問題全部有答案？（2分）
□ 無 AI 生成的冗余內容？（1分）
□ 每行都有可追溯的失敗案例依據？（2分）

**工具子系統**
□ 工具集最小化（無「可能需要」的工具）？（2分）
□ 每個工具有明確的使用場景？（1分）
□ 缺少關鍵工具時有明確說明？（2分）

**環境子系統**
□ init.sh 存在且可重現？（2分）
□ 依賴版本完全鎖定？（1分）
□ 常見環境問題有文件說明？（2分）

**狀態子系統**
□ PROGRESS.md 格式一致且最新？（2分）
□ feature_list.json 所有功能有驗證命令？（2分）
□ 上次會話可以無損繼續？（1分）

**反饋子系統**
□ 驗證命令完整（語法+型別+邏輯+E2E）？（2分）
□ 錯誤訊息包含修復指引？（2分）
□ 驗證時間 < 3 分鐘？（1分）

總分：___/25  優秀 ≥20，良好 15-19，需改進 < 15

輸出：各維度得分 + 最優先的 3 項改進建議。
```

---

### Prompt 14：代理邊界控制 Prompt

```
你正在執行一個有明確範圍的任務，需要嚴格控制在範圍內。

任務範圍：[明確描述要做什麼]
明確不在範圍內：[明確描述不要做什麼]
影響區域：[描述這個任務只應修改哪些文件或模組]

執行規則：
1. 只修改影響區域中的文件
2. 如果發現範圍外的問題（bug、改進機會），記錄但不修復
3. 每次 git commit 只包含一個邏輯變更
4. 不主動添加「未來可能需要」的功能或抽象
5. 修改前先運行驗證命令確認基線，修改後確認驗證仍通過

完成時輸出：
- 修改了哪些文件（精確清單）
- 驗證命令通過的截圖/輸出
- 發現的範圍外問題（僅記錄，不處理）
```

---

## 附錄：來源評分與完整索引

### 一級來源（直接閱讀）

| # | 來源 | URL | 類型 | 核心貢獻 |
|---|------|-----|------|---------|
| 1 | walkinglabs - Lecture 01 | https://walkinglabs.github.io/learn-harness-engineering/zh-TW/lectures/lecture-01-why-capable-agents-still-fail/ | O | 五層失敗模型 |
| 2 | walkinglabs - Lecture 02 | https://walkinglabs.github.io/learn-harness-engineering/zh-TW/lectures/lecture-02-what-a-harness-actually-is/ | O | 五子系統定義 |
| 3 | walkinglabs - Lecture 03 | https://walkinglabs.github.io/learn-harness-engineering/zh-TW/lectures/lecture-03-why-the-repository-must-become-the-system-of-record/ | O | ACID 原則、冷啟動測試 |
| 4 | walkinglabs - Lecture 06 | https://walkinglabs.github.io/learn-harness-engineering/zh-TW/lectures/lecture-06-why-initialization-needs-its-own-phase/ | O | 初始化相位設計 |
| 5 | Anthropic 長任務文章 | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents | O | Initializer+Coding 雙代理架構 |
| 6 | Martin Fowler | https://martinfowler.com/articles/harness-engineering.html | C | Feedforward/Feedback 框架 |
| 7 | AddyOsmani | https://addyosmani.com/blog/agent-harness-engineering/ | C | Harness 組件全景 |
| 8 | Augment Code | https://www.augmentcode.com/guides/harness-engineering-ai-coding-agents | O | AGENTS.md spec、PEV 循環 |
| 9 | HumanLayer Blog | https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents | C | 配置後反饋實踐 |
| 10 | Software Mansion | https://agentic-engineering.swmansion.com/becoming-productive/harness-engineering/ | C | 工具決策框架 |

### 二級來源（本地知識庫）

| # | 來源 | 核心貢獻 |
|---|------|---------|
| 11 | research/ai-articles/2026-05-12-ai-agent-harness-stripe-1300-prs.md | Stripe 1300 PRs 案例 |
| 12 | research/ai-articles/2026-05-16-model-harness-fit.md | Model-Harness Fit 概念 |
| 13 | research/ai-articles/2026-05-12-boris-cherny-verification-loops.md | 驗證循環 2-3x 提升數據 |
| 14 | research/tweets/2026-05-09-@Mnilax-155938.md | 12 規則、200行 compliance 研究 |
| 15 | research/tweets/2026-05-05-@mindstudio-harness-beats-model.md | Harness 優化 12-42pp benchmark |

---

## 🔄 同步更新 — 2026-05-23

> **更新方法**：overnight-research 全網搜尋 + code.claude.com 官方文件 + DebugML 獨立審計驗證  
> **資料截止**：2026-05-23

### 競爭格局修正（2026年5月）

#### ForgeCode Benchmark 數字修正

本報告（v1.0，2026-05-17）引用的 Terminal-Bench 2.0 數字需要修正：

| 系統 | 原引用數字 | 修正後（DebugML 審計，2026-04）| 說明 |
|------|-----------|-------------------------------|------|
| ForgeCode + GPT-5.4 | 81.8% | **71.7%**（調整）| 審計發現 benchmark 作弊跡象，移除後下修 |
| ForgeCode + Opus 4.6 | 79.8% | 未公布調整後值 | 同樣受到質疑 |

**中立基準補充**（SWE-Bench Verified，Princeton/UChicago）：
- ForgeCode vs Claude Code 差距：僅 **2.4 points**（非 Terminal-Bench 的 13.7pp）
- 建議優先參考 SWE-Bench 而非 Terminal-Bench 2.0

#### Capy Harness 狀態

2026年5月各主要資源查不到 Capy Harness 的更新資料，可能已：
- 被 ForgeCode 架構吸收整合，或
- 停止維護

本報告涉及 Capy 的比較數據（第 3 節）應以「歷史參考」視之，不代表 2026-05 現況。

---

### Claude Code Harness 新功能（Week 13-20）

Claude Code 平台層的 harness 能力在 2026-03-23 至 2026-05-15 間大幅擴展：

#### Auto Mode：中間層權限 Harness

```
Manual approval ← → Auto Mode ← → --dangerously-skip-permissions
```

- 分類器自動允許安全操作、阻擋高風險操作
- `settings.autoMode.hard_deny`：無論 allow 例外，指定操作**絕對不自動執行**
- 適合：CI/CD pipeline harness、夜間無人值守任務

#### `xhigh` 努力等級 — 大多數 harness 任務的推薦設定

```bash
claude --effort xhigh  # Opus 4.7 最高品質模式
```

- Week 16（v2.1.105）引入；目前 Anthropic 推薦為大多數編程工作的預設
- Hooks 可透過 `effort.level` 和 `$CLAUDE_EFFORT` 讀取當前等級

#### Hooks 27 事件體系（完整版）

Claude Code hooks 現已有 27 個事件（本報告 v1.0 未涵蓋最新新增）：

**新增（Week 19-20）**：
- `effort.level` 欄位 + `$CLAUDE_EFFORT` env var（hooks 和 Bash tool 均可讀取）
- `args: string[]` exec 形式：直接 spawn，無 shell 中介（路徑佔位符無需引號）
- `continueOnBlock: true`：hook 拒絕後將原因回饋 Claude 並繼續 turn（非終止）
- `terminalSequence`：hooks 發出桌面通知/視窗標題/bell，無需 controlling terminal

**WorktreeCreate / WorktreeRemove**：Git worktree 生命週期事件（自動清理）

#### Agent View：Harness 監控層

```bash
claude agents           # 所有 session 一覽
claude agents --json    # 機器可讀，供 tmux/scripts 使用
```

- Session 狀態：`running` / `blocked on you` / `done`
- 在無 terminal 附加時背景 session 持續運行
- 適合：multi-agent harness 編排的監控介面

#### `/goal` + Auto Mode 組合：最接近 KAIROS 的現有能力

```
> /goal all tests pass and coverage stays above 80%
```

- `/goal` 跨 turns 自動執行直到條件成立（Week 20）
- 搭配 Auto Mode：減少授權中斷
- 這是目前 Claude Code **最接近自律 daemon 的能力組合**（KAIROS 仍未正式發布）

---

### Harness 工程最佳實踐更新（2026-05）

| 原則 | v1.0 狀態 | 2026-05 更新 |
|------|-----------|------------|
| 模型與 Harness 分層 | 已覆蓋 | Opus 4.7 + xhigh = 新建議預設 |
| 任務 atomicity | 已覆蓋 | `/goal` + 可驗證條件取代人工分割 |
| 安全自動化 | 已覆蓋 | Auto Mode + Hard Deny 提供三層防護 |
| 監控與可見性 | 未覆蓋 | `claude agents` + `--json` 填補 |
| Benchmark 選擇 | 未覆蓋 | 優先 SWE-Bench（中立）而非 Terminal-Bench |

**參考來源**：
- [Claude Code What's New — Week 13-20](https://code.claude.com/docs/en/whats-new)
- [Hooks 官方文件](https://code.claude.com/docs/en/hooks)
- [Agent View 官方文件](https://code.claude.com/docs/en/agent-view)
- [DebugML: Cheating on Agent Benchmarks](https://debugml.github.io/cheating-agents/)

*研究完成：2026-05-17 | 總來源數：15 | 報告版本：v1.0*

---

## 2026-05-25 Re-check

**稽核方法**：對照 `.claude/rules/`（core.md / context-management.md / subagent-strategy.md / output-discipline.md）、`.claude/settings.json` hooks 設定、`.claude/agents/` 及 `.claude/skills/` 目錄的現行實作狀態。

### 已落地的建議

- ✅ **AGENTS.md / CLAUDE.md ≤ 200 行**：core.md 保有 `R1–R12，本 CLAUDE.md ≤ 200 行` 規則，目前 CLAUDE.md 僅 36 行（~271 tok），遠低於上限。
- ✅ **驗證命令清單**：core.md R4 + PGE 節明確要求 `bash scripts/healthcheck.sh`，且有 Stop hook（`session-stop.sh`）確保任務終止時觸發。
- ✅ **五層防禦模型的指令子系統**：core.md 已完整涵蓋 R1（Think Before Coding）、R2（Simplicity）、R3（Surgical）、R4（Goal-Driven）等核心防禦規則。
- ✅ **子代理設計（Fan-out 上限 4）**：subagent-strategy.md 已明確定義，且 child 不 self-retry 規則已落地。
- ✅ **多代理架構**：`.claude/agents/` 目錄已有 15 個 agent 定義（researcher / reviewer / implementer / memory-compactor 等）。
- ✅ **Sessions Hooks（Completion Gate）**：Stop event 已有 `session-stop.sh` 及 `memory-sync.sh` 雙 hook，PostToolUse（Edit/Write）已有 `post-edit.sh`，達到「宣告完成前強制驗證」精神。
- ✅ **Init.sh 概念**：hooks `session-init.sh` 在 SessionStart 執行，對應初始化相位建議。
- ✅ **狀態管理 / 長期記憶**：core.md Memory Loop 節定義了 `MEMORY.md` 雙層記憶，`memory-sync.sh` 及 `memory-archive.sh` hooks 確保跨 session 持久化。
- ✅ **Plan-Execute-Verify 循環**：core.md R4 + R10（Checkpoint）已形成 PEV 循環骨架；R12 Fail Loud 確保驗證不可跳過。
- ✅ **ACID 原則（Atomicity）**：core.md Git 工作流程要求每次 `git add → commit → push`，commit 顆粒度規則要求「fix X」+「refactor Y」分開 commit。
- ✅ **工具選擇框架（Skills / Hooks）**：settings.json 已配置 PreToolUse（block-dangerous.sh / protect-sensitive-files.sh）、PostToolUse（post-edit.sh / audit-log.sh）四類 hook，對應報告的工具選擇矩陣。
- ✅ **子代理 Agent Input Security（Prompt Injection 防護）**：subagent-strategy.md 已有 `<untrusted_objective>` 包裹 YOU MUST 規則。
- ✅ **Claude Code Hooks 體系**：設定檔中已有 SessionStart / UserPromptSubmit / PreToolUse / PostToolUse / PostToolUseFailure / PreCompact / PostCompact / Stop / Notification / PermissionRequest，共 10 個 hook 事件類型覆蓋完整。
- ✅ **Claude agents / Agent View**：`.claude/agents/` 已有完整代理目錄，支援多代理 harness 編排。

### 尚未落地的建議

- ⚠️ **feature_list.json + PROGRESS.md 進度追蹤模式**：報告建議每個專案建立 `feature_list.json`（failing/passing 狀態追蹤），目前 workspace 層級未見此機制；`claude-progress.json` schema 存在但非每個子任務的追蹤格式。
- ⚠️ **冷啟動測試（Cold Start Test）量化**：報告建議定期對倉庫跑五問測試，目前沒有對應的自動化 hook 或定期 checklist。
- ⚠️ **知識可見性缺口（KVG）計算**：目標 KVG < 10%，目前 workspace 沒有正式的 KVG 量測流程。
- ⚠️ **Harness Coverage Score / Verification Density**：報告第 6.5 節預測的這類量化指標，目前 workspace 仍是人工評估（K×M 框架），未自動化。
- ⚠️ **AI 生成 AGENTS.md 的主動防護**：報告警告 ETH Zurich 發現 AI 自動生成 AGENTS.md 會降低性能，目前無程序性防護（無 hook 或 CI 阻擋 AI 直接覆寫 AGENTS.md）。
- ⚠️ **init.sh 一鍵啟動腳本**：報告建議每個專案有 `init.sh` 確保環境可重現，目前 cc-workspace 為 Claude Code harness 專案，非一般開發專案，此建議適用性有限，但具體實作尚缺。

### 過期資訊更新

- **Terminal-Bench 2.0 數字**：報告第 2.4 節引用的 Opus 4.6 + ForgeCode = 79.8% 已在 2026-05-23 同步更新節中修正（DebugML 審計顯示存在 benchmark 作弊跡象，調整後數字未公布）。2026-05-23 更新節已處理此問題，原始數據應以「歷史參考」視之。
- **Capy Harness**：截至 2026-05-25，仍無新資料，原第 2.4 節比較數據維持「歷史參考」狀態。
- **`xhigh` 努力等級與 `/goal` 指令**：2026-05-23 同步更新節已涵蓋，這些功能目前為 Claude Code 實際可用功能，非預測性內容，資訊有效。
- **Claude Opus 4.7 預設模型**：settings.json 的 `advisorModel` 已設定為 `claude-opus-4-7`，與 2026-05-23 更新節「Opus 4.7 已成為 Max/Team Premium 新預設」一致。
