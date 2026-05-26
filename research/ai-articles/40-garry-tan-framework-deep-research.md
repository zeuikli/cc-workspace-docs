---
url: https://github.com/garrytan/gbrain
title: Garry Tan「Thin Harness, Fat Skills」五核心概念深度研究
author: Research Compilation (2026-05-23)
date: 2026-05-23
status: SUCCESS
sources:
  - https://www.forbes.com/sites/josipamajic/2026/04/12/the-yc-chief-who-codes-10000-lines-a-day-has-a-simple-secret/
  - https://github.com/garrytan/gbrain
  - https://yage.ai/share/thin-harness-fat-skills-en-20260414.html
  - https://github.com/garrytan/gbrain/blob/master/docs/ethos/THIN_HARNESS_FAT_SKILLS.md
---

# Garry Tan「Thin Harness, Fat Skills」五核心概念深度研究

> 本文延伸 Forbes 文章（`39-forbes-garry-tan-yc-chief-10000-lines.md`），蒐集原始發文、實作細節、學術對應。

---

## 框架總覽

Garry Tan（YC CEO）主張：

> "The 2x people and the 100x people are using the same models. The difference is five concepts that fit on an index card."

> "every step in the system is either latent space (model makes a judgment) or deterministic space (program executes reliably)"

框架名稱：**Thin Harness, Fat Skills**
實作：**gbrain**（MIT licensed，2026-04-05 釋出）
GitHub：https://github.com/garrytan/gbrain
規模：146,646 知識頁面、24,585 人物 profiles、5,339 公司索引、43 個 skill files

---

## 概念一：Skill Files

### 定義

Skill files 是可重用的 markdown 文件，**編碼流程（process）而非內容（content）**。

> "A skill file is a reusable program written in markdown that describes a process of judgment, not a fixed answer."

> "The same /investigate skill, pointed at a safety scientist or at FEC filings, produces radically different outputs because the skill describes judgment and the invocation supplies the world."
> — Garry Tan, Forbes / X post

> "Skill files encode process, not content. Think of them as method calls, with markdown as the programming language and human judgment as the runtime."

> "The same procedure produces radically different capabilities depending on what you pass in."
> — gbrain THIN_HARNESS_FAT_SKILLS.md

> "Every skill you write is a permanent upgrade to your system. Skills remain stable and benefit automatically when models improve, while the underlying deterministic system remains stable and reliable."

### Garry Tan 原始 X 發文

- ["This is the simplest distillation of what I have learned about agentic engineering this year: Push smart fuzzy operations humans do into markdown skills. Fat skills. Push must-be-perfect deterministic operations into code. Fat code. The harness? Keep it thin."](https://x.com/garrytan/status/2043566215927328955)
- ["Thin Harness Fat Skills Fat Code = THE NEW DRY"](https://x.com/garrytan/status/2047039391978418569)
- ["So far basically fewer fatter skills makes the resolver shorter which itself is less context bloat. Short resolvers are better than long ones"](https://x.com/garrytan/status/2047184243164651648)
- ["I've been having such an amazing time with Claude Code I wanted you to be able to have my *exact* skill setup: Introducing gstack"](https://x.com/garrytan/status/2032014570118922347)
- ["The reason why I release my X articles about AI agents... is that we can have *PROCESS POWER*, which is the one super powerful specific moat that anyone can create for themselves."](https://x.com/garrytan/status/2056915511469023635)

### gstack 開源實作

**Repository：** https://github.com/garrytan/gstack（MIT）
**描述：** "Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA"

**gstack 核心 skill 範例：**

| Skill | 功能 |
|-------|------|
| `/investigate` | 系統性 debug + 根因分析（4 階段：investigate → analyze → hypothesize → implement） |
| `/office-hours` | YC 式產品審問（模擬 office hours） |
| `/review` | Staff engineer 代碼 review |
| `/plan-eng-review` | 架構鎖定決策 |
| `/plan-ceo-review` | 產品範疇 review |
| `/design-review` | 即時視覺稽核 |

**/investigate Skill 詳細流程（Iron Law: no fixes without root cause）：**
1. Root Cause Investigation：收集症狀、追蹤 code paths、檢查近期改動
2. Pattern Analysis：匹配已知模式（race conditions, null propagation, state corruption）
3. Hypothesis Testing：3-strike rule 驗證
4. Implementation：只修根因，最小改動
5. Verification & Report：重現 bug 確認修復

**Skill 格式：**
- YAML frontmatter（metadata）
- Markdown 指令主體
- 跨 session 持久化（不同於 one-off prompt）
- 可組合（skills can invoke other skills）

### gbrain 實作細節（43 個 skill 分類）

| 類別 | 功能 |
|------|------|
| 訊號偵測 | 每 session 常駐 |
| 內容攝取 | 截圖、影片、逐字稿 |
| 思考技能 | 腦力激盪、除錯、review |
| 運營 | 任務管理、排程、健康檢查 |
| 身份與存取控制 | 安全邊界 |

### CLAUDE.md 精簡路徑

**Tan 的親身經歷：**
> "Garry Tan's CLAUDE.md file was originally 20,000 lines, with every single thing he ran across going in there—every quirk, pattern, and lesson—which he describes as 'completely ridiculous.' The model's attention degraded, and Claude Code advised him to cut it back, with the fix being about 200 lines of pointers to documents, with the resolver loading the right one when it matters."

**結論：** 20,000 行 → 約 **200 行指標**（model attention 在噪音中降解是關鍵原因）

**Context Bloat 量化：**
> "A Playwright CLI executes browser operations in 100ms, while a Chrome MCP requires 15 seconds for the same screenshot-find-click-wait-read sequence—a 75x performance gap."

### 三層架構模型

```
┌─────────────────────────────────────┐
│         FAT SKILLS（頂層）           │
│  markdown procedures 編碼領域知識    │
│  90% of the value lives here        │
├─────────────────────────────────────┤
│         THIN HARNESS（中層）         │
│  ~200 行管理：loop/context/安全邊界  │
├─────────────────────────────────────┤
│         FAT CODE（底層）             │
│  Auth, validation, DB, payments     │
│  確定性操作，microseconds, 零成本    │
└─────────────────────────────────────┘
```

> "Push intelligence UP into skills. Push execution DOWN into deterministic tooling. Keep the harness THIN."

### 生產力數據

- Garry Tan 每日：**37,000 行程式碼**
- 每週（part-time YC CEO）：**~10,000 行**
- 大型 feature（4K+ LOC + 完整測試）：**~1 小時**
- 效能指標：**~810x vs. 2013 baseline**

### gbrain 效能指標

- P@5 retrieval accuracy：**97.6%**（LongMemEval 基準，無 LLM query rewriting）
- 知識庫規模：146,646 頁、24,585 人物 profiles、5,339 公司索引
- 每 session L1 載入：AGENTS.md + RESOLVER.md + master index

---

## 概念二：Harness

### 定義

Harness 在迴圈中執行模型，管理 context、讀寫檔案、強制安全邊界。

**反模式（Fat Harness）：**
- 40+ tool definitions 消耗半個 context window
- God-tools 帶來多秒 MCP round-trip
- REST API wrapper 把每個 endpoint 變一個 tool

### Claude Code 洩漏印證（2026-03-31）

#### 洩漏事件

- **日期**：2026-03-31 00:21 UTC
- **發現者**：Chaofan Shou（@Fried_rice，Solayer Labs intern）
- **原因**：`.npmignore` 遺漏 `*.map`，`@anthropic-ai/claude-code@2.1.88` npm 包夾帶 59.8 MB source map（cli.js.map）
- **規模**：512,000+ 行 TypeScript，1,906 個檔案
- **Boris Cherny 回應**：「plain developer error」，並補充：「100% of my contributions to Claude Code were written by Claude Code」
- **傳播速度**：clean-room rewrite 2 小時達 50,000 GitHub stars（可能是 GitHub 史上增速最快的 repo）

#### 洩漏揭示的 Harness 架構

**Self-Healing Query Loop（QueryEngine）**
```
系統提示構建 → slash-command 預處理 → 多輪工具呼叫迴圈
→ context 壓縮（5 種策略）→ 錯誤恢復 → transcript 持久化
```
> "Context compression, message consolidation, and token budget continuation—before surfacing errors to users"

**Concurrency-Safe Tool Batching**
> "Claude issues multiple Read, Glob, and Grep calls in a single turn, and the SDK merges results before the next reasoning step"

使用 async generator 作為 agent loop（非 callback），提供自然 backpressure 與乾淨取消機制。

**模組規模**
- 46,000 行 query engine（React + Ink terminal rendering）
- 40+ 專用 tool plugin
- 14 個 cache-break vectors
- 23 個 bash security check

**未發佈功能（44 個 feature flags）**

| 功能 | 說明 |
|------|------|
| **KAIROS** | 自主 daemon 模式：筆電關閉時持續背景執行，定期 tick prompt，15 秒/週期 blocking budget |
| **autoDream** | 記憶整合：4 階段（Orient → Gather → Consolidate → Prune），觸發條件：閒置 24h + 最少 5 sessions |
| **ULTRAPLAN** | 遠端規劃，30 分鐘 extended thinking budget |
| **BUDDY** | Tamagotchi 風格終端伴侶，18 種生物 + 稀有度 |

**autoDream 四階段：**
1. **Orient**：掃描近期 session logs
2. **Gather**：提取相關模式與決策
3. **Consolidate**：壓縮為持久記憶（≤25KB）
4. **Prune**：移除噪音

---

## 概念三：Resolvers

### 定義

Resolver 是 context 的**路由表**：task type X 出現時，載入 document Y。

> "Routing lives in skills/RESOLVER.md — the agent reads it once per request, picks the right skill, executes."
> — gbrain 文件

### 三層快取架構

| 層級 | 載入時機 | 內容 |
|------|---------|------|
| **L1（每 session）** | 常駐 | AGENTS.md、RESOLVER.md、master index |
| **L2（on demand）** | 按任務類型查詢 | Skills INDEX.md |
| **L3（on match）** | 匹配時 | 特定 skill markdown 檔案 |

每個 skill 帶 **description field + trigger words**，實現自動 intent 匹配，無需用戶明確指定。

### 學術對應

**RCR-Router**（arxiv:2508.04903）：
> "Dynamically selects semantically relevant memory subsets for each agent based on its role and task stage"
> 減少 token 使用達 30%

**Dynamic Context Loading（DCL）**：按需載入 tool，而非預載所有定義，維持精簡 context window。

---

## 概念四：Latent vs Deterministic

### 定義（Tan 原話）

> "every step in the system is either latent space (model makes a judgment) or deterministic space (program executes reliably)"

### 分工原則

| Latent Space（LLM） | Deterministic Space（程式碼） |
|--------------------|----------------------------|
| 判斷、合成、分類 | SQL 查詢、算術、組合優化 |
| 模式識別、摘要 | 路由、重試邏輯、HTTP status |
| 創意生成 | 驗證、policy check |

**反模式：** 強制確定性問題通過 LLM → 輸出「看起來合理但實際錯誤」

### ~90% 規則（生產實踐）

> "~90% of AI agent work is routing, validation, extraction, and policy checks—tasks that don't require LLM reasoning"

**生產案例：** triage agent 單次成本 $0.31 → $0.04（降 87%，年省 $56,160）

### 學術論文支撐

| 論文 | arXiv | 核心發現 |
|------|-------|---------|
| Blueprint First, Model Second | 2508.02721 | 確定性 Blueprint 引擎 + LLM 只做有邊界子任務 |
| Replayable Financial Agents | 2601.15322 | LLM 只在真正需要判斷時呼叫，其餘跑確定性程式，μs 級延遲 |
| Hybrid LLM Routing | 2507.08250 | 98.4% 準確率保留，cost 降 67.8%，token 降 66.3% |
| RouteLLM | 2406.18665 | 動態路由強/弱模型，成本降 2x+，路由遷移性強 |
| R2-Router | 2602.02823 | 使用 GNN + KNN 的資料驅動路由 |
| Latent State Estimation | 2405.11120 | 顯式推斷 latent state 的 agent 任務完成率高 1.6x |

---

## 概念五：Diarization

### 定義（Tan 原話）

> "Diarization: the model reads all materials about a subject and outputs a one-page structured profile... simultaneously reading GitHub commit history, the application, and advisor transcripts to discover that what the founder says and what they build are misaligned—something SQL queries or RAG cannot accomplish alone."

**具體案例：**
> "a founder claims to be building 'Datadog for AI agents,' but 80% of their commits are in the billing module"

**YC Startup School 應用：** 6,000 位 founder profiles，每晚執行，自動偵測「說的」與「做的」落差。

### 術語說明

⚠️ **「Diarization」是 Tan 的自創術語**。在 NLP/音訊領域，diarization 指說話人辨識（speaker diarization）。Tan 在此賦予全新含義：多源資料融合 → 單頁結構化摘要。

### 與 RAG 的差異

| 傳統 RAG | Diarization（Tan 定義）|
|---------|----------------------|
| 向量檢索相關片段 | 讀取主題所有材料 |
| 回答特定問題 | 生成跨源整合 profile |
| SQL 可部分替代 | SQL/RAG 無法單獨完成 |
| 點查詢 | 全面分析後提煉 |

### 學術對應（不同術語）

| 論文 | 核心相似點 |
|------|----------|
| [Step-Back Profiling](https://arxiv.org/pdf/2406.14275) | 從用戶歷史提煉高層概念 profile，高效記憶管理 |
| [Guided Profile Generation](https://arxiv.org/pdf/2409.13093) | 中間 guided profile 準確率提升 37% vs 原始 context |
| [GRAVITY](https://arxiv.org/pdf/2510.11952) | profile-grounded 合成偏好，>4% 偏好分提升 |

---

## Steve Yegge 生產力倍數

> "10x to 100x as productive as engineers using Cursor and chat today, and roughly 1,000x as productive as Googlers were back in 2005."
> — Steve Yegge（Tan 引用）

**限制（Pragmatic Engineer Podcast）：**
> "Engineers operating at maximum AI-assisted productivity can sustain it for roughly three hours per day. After that, the cognitive load of directing, reviewing, and integrating AI output becomes overwhelming."

---

## 與 cc-workspace Harness 的對應

| Tan 的概念 | cc-workspace 實作 |
|-----------|-----------------|
| Thin harness | CLAUDE.md ≤ 200 行（12-Rule Canon） |
| Skill files | `.claude/rules/*.md` + skills/ |
| Resolver | CLAUDE.md `@.claude/rules/` auto-load |
| Latent vs Deterministic | Rule 5（LLM only for judgment） |
| Diarization | `/research-hub` + `overnight-research` |
| KAIROS / autoDream | hooks（PreToolUse / Stop Hook） |

---

## 參考來源

### Garry Tan 原始資料
- [gbrain GitHub（MIT）](https://github.com/garrytan/gbrain)
- [THIN_HARNESS_FAT_SKILLS.md](https://github.com/garrytan/gbrain/blob/master/docs/ethos/THIN_HARNESS_FAT_SKILLS.md)
- [RESOLVER.md](https://github.com/garrytan/gbrain/blob/master/skills/RESOLVER.md)
- [Thin Harness, Fat Skills — 英文解析](https://yage.ai/share/thin-harness-fat-skills-en-20260414.html)
- [Medium 解析](https://moonsat.medium.com/thin-harness-fat-skills-a3dd6d2fe2af)

### Claude Code 洩漏分析
- [Layer5 工程分析](https://layer5.io/blog/engineering/the-claude-code-source-leak-512000-lines-a-missing-npmignore-and-the-fastest-growing-repo-in-github-history/)
- [DeepLearning.AI The Batch（KAIROS/autoDream）](https://www.deeplearning.ai/the-batch/claude-codes-source-code-leaked-exposing-potential-future-features-kairos-and-autodream/)
- [InfoQ 詳細分析](https://www.infoq.com/news/2026/04/claude-code-source-leak/)
- [Chaofan Shou 原始 X 貼文](https://x.com/Fried_rice/status/2038894956459290963)
- [Zscaler ThreatLabz 安全分析](https://www.zscaler.com/blogs/security-research/anthropic-claude-code-leak)

### 學術論文
- [Blueprint First, Model Second (arXiv:2508.02721)](https://arxiv.org/pdf/2508.02721)
- [Replayable Financial Agents (arXiv:2601.15322)](https://arxiv.org/pdf/2601.15322)
- [Hybrid LLM Routing (arXiv:2507.08250)](https://arxiv.org/abs/2507.08250)
- [RouteLLM (arXiv:2406.18665)](https://arxiv.org/abs/2406.18665)
- [R2-Router (arXiv:2602.02823)](https://arxiv.org/pdf/2602.02823)
- [Latent State Estimation (arXiv:2405.11120)](https://arxiv.org/pdf/2405.11120)
- [RCR-Router (arXiv:2508.04903)](https://arxiv.org/abs/2508.04903)
- [Step-Back Profiling (arXiv:2406.14275)](https://arxiv.org/pdf/2406.14275)
- [Guided Profile Generation (arXiv:2409.13093)](https://arxiv.org/pdf/2409.13093)
- [GRAVITY (arXiv:2510.11952)](https://arxiv.org/pdf/2510.11952)
