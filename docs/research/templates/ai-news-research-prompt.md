---
title: AI News 目錄深度研究 Prompt
type: template
---

# AI News 目錄深度研究 Prompt
# 目標：research/ai-news/ 全部內容分類 → 可實作 prompt 檔 + 研究報告
# 使用方式：先貼 /goal，再貼工作 Prompt

---

## STEP 1：貼入 /goal 條件

```
/goal 下列三個條件同時成立（評估依據是 Claude 在 transcript 中執行命令的實際輸出）：
1. wc -m research/reports/[DATE]-ai-news-synthesis-report.md 的輸出數字 ≥ 3000
2. ls research/prompts/ | grep "ai-" | wc -l 的輸出數字 ≥ 4
3. git log --oneline -1 包含 "research: ai-news" 字樣
若以上輸出尚未在對話中出現，Claude 需執行 Step 5 驗證命令並展示結果，再由評估器判斷。
若超過 20 輪仍未達成，停止並輸出截至目前的完成狀態報告。
```

---

## STEP 2：貼入工作 Prompt

```
你是一個自主研究 Agent。執行以下任務，不需要任何人工確認，直接推進到完成。

---
## 任務目標

研究 research/ai-news/ 目錄的全部內容，按主題整理核心洞察，產出：
1. 4 個可實作 prompt 檔（存至 research/prompts/，前綴 ai-）
2. 完整研究報告（存至 research/reports/[DATE]-ai-news-synthesis-report.md，目標 ≥ 3000 字元，wc -m 計算）

---
## 設計說明（必讀）

research/ai-news/ 已有預先合成的 digest 檔（Q1/04/05 各一份）與 TOPIC-INDEX.md。
**讀 digest 與 index，不要逐篇讀 131 篇個別日報**（會造成 context rot）。
策略：digest 提供廣度，最新週 2026-05/ 個別檔補充新鮮度。

---
## Step 1：讀取全局結構

依序執行：
```bash
cat research/ai-news/README.md
cat research/ai-news/TOPIC-INDEX.md
```

從中提取：
- 4 個來源分類（Daily Briefings / Research & Deep Dives / Insights & Strategy / Community）
- 8 大主題（前沿模型競逐 / Agentic 架構 / 開源模型 / AI 產品經濟學 / 地緣政治 / 物理 AI / 開發工具 / AI 對齊安全）
- 各 digest 檔路徑清單

---
## Step 2：平行 Sub-Agent 深讀（4 個並發，單一訊息同時派遣）

**Sub-Agent A — 最新月份（2026-05）深讀**
- Read：`research/ai-news/2026-05-digest.md`、`research/ai-news/2026-05-brief.md`
- 補充：從 `research/ai-news/2026-05/` 任選 3–5 篇最近（≥05-12）的個別文章（優先 Latent Space、Wisely Chen AI）
- 任務：提取主題 1–8 中 2026-05 的關鍵發展、數據、引用
- 回傳格式（≤600 字）：
  ```
  ## 2026-05 關鍵發展摘要
  ### 主題 N：[主題名]
  - 核心事件：
  - 數據/引用（來源 + 日期）：
  - 可操作洞察：
  ```

**Sub-Agent B — 2026-04 月份深讀**
- Read：`research/ai-news/2026-04-digest.md`、`research/ai-news/2026-04-brief.md`
- 任務：提取主題 1–8 的 4 月核心發展，識別跨主題的關聯性
- 回傳格式（≤600 字）：同 A，標注「2026-04」

**Sub-Agent C — Q1 歷史基線**
- Read：`research/ai-news/2026-q1-digest.md`、`research/ai-news/2026-q1-brief.md`
- 任務：建立 Q1 基線，識別哪些趨勢持續延伸到 Q2，哪些已消退
- 回傳格式（≤600 字）：
  ```
  ## Q1 基線摘要
  ### 持續延伸趨勢：
  ### 已消退或被取代趨勢：
  ### Q1→Q2 轉變的關鍵拐點：
  ```

**Sub-Agent D — Digests + 來源分析**
- Read：`research/ai-news/digests/` 最新 3–4 份（`latest-ai.md` 或最近日期的 `ai.md`）
- 任務：①識別哪些來源最具洞察力（高密度 vs 低密度）②找出跨來源的共識與分歧 ③標注 Wisely Chen AI 的獨特中文視角
- 回傳格式（≤600 字）：
  ```
  ## 來源品質分析
  ### 高洞察密度來源（Tier 1）：
  ### 中洞察密度來源（Tier 2）：
  ### 跨來源共識：
  ### 跨來源分歧：
  ### Wisely Chen AI 獨特視角：
  ```

---
## Step 3：產生 4 個主題 Prompt 檔

根據 Sub-Agent 回傳，為 8 主題合併成 4 個可實作 prompt 檔（每個覆蓋 2 個相關主題）：

**檔案 1：`research/prompts/ai-frontier-models-prompt.md`**
- 覆蓋主題：前沿模型競逐（主題 1）+ 開源模型與本地部署（主題 3）
- 用途：追蹤前沿模型競爭格局、評估開源 vs 封閉模型選型
- 結構：
  ```markdown
  # 前沿模型競逐 + 開源生態 — 分析 Prompt
  > 資料來源：research/ai-news/ Q1-2026 ~ 2026-05

  ## 使用方式
  [適用場景：模型選型決策、競品追蹤、技術路線評估]

  ## 核心洞察（來自 AI News）
  [從 Sub-Agent 提取的關鍵數據與事件，每條附日期來源]

  ## 分析 Prompt 範本
  \`\`\`
  你是 AI 模型評估專家。基於以下背景：
  [插入核心洞察]

  請分析：[具體分析任務]
  評估維度：benchmark 表現、推理成本、部署門檻、生態系成熟度
  \`\`\`

  ## 追蹤指標
  [需要持續監測的數據點：benchmark 排行、開源社區活躍度等]
  ```

**檔案 2：`research/prompts/ai-agentic-devtools-prompt.md`**
- 覆蓋主題：Agentic 架構成熟化（主題 2）+ 開發工具與組織革命（主題 7）
- 用途：設計 agentic 系統、評估 Claude Code / Cursor 等工具、規劃工程組織轉型
- 結構：同上模式

**檔案 3：`research/prompts/ai-business-finops-prompt.md`**
- 覆蓋主題：AI 產品經濟學與 FinOps（主題 4）+ 物理 AI 與機器人（主題 6）
- 用途：AI 投資決策、Token 成本優化、機器人/具身 AI 技術評估
- 結構：同上模式

**檔案 4：`research/prompts/ai-safety-geopolitics-prompt.md`**
- 覆蓋主題：地緣政治與 AI 安全（主題 5）+ AI 對齊與安全研究（主題 8）
- 用途：供應鏈風險評估、對齊策略規劃、地緣風險分析
- 結構：同上模式

---
## Step 4：產生完整研究報告

撰寫報告，存至 `research/reports/[DATE]-ai-news-synthesis-report.md`。

報告結構與字元配額（wc -m，含標點符號）：
```markdown
# research/ai-news 深度研究報告
**涵蓋期間**：2026 Q1 ~ [DATE] | **來源數**：17 | **主題數**：8

## 執行摘要（目標 300 字元）
[Q1–Q2 AI 發展的 3 個主旋律，各 1 句]

## 1. 前沿模型競逐：三方鼎立到新格局（目標 600 字元）
[GPT-5.5 / Claude Mythos / DeepSeek V4 的能力演進，含 benchmark 數據]

## 2. Agentic 架構成熟：Harness Engineering 的崛起（目標 700 字元）
[從 Q1 到 05 月的 agentic 系統設計演進，含 Claude Code / MCP 進展]

## 3. 開源追平封閉前沿（目標 500 字元）
[Qwen 3.6、DeepSeek V4 Flash 等開源模型縮差，本地部署 TCO 分析]

## 4. AI 產品經濟學：融資戰與 Token 計費危機（目標 500 字元）
[Anthropic 10x 成長 vs 裁員潮，Token 計費模型的可持續性]

## 5. 地緣政治與晶片戰：中美 AI 差距演變（目標 400 字元）
[晶片管制效果、中國模型追趕速度、供應鏈安全事件]

## 6. 物理 AI 與機器人：World Models 走向實用（目標 400 字元）
[JEPA、Google Genie 3、AMI Labs 的進展與距離量產的差距]

## 7. 開發工具革命：Two-Slice Team 與 Cognitive Surrender（目標 500 字元）
[Claude Code / Cursor 生產力數據，認知依賴風險，工程組織轉型]

## 8. AI 對齊與安全：供應鏈攻擊到 Glasswing（目標 400 字元）
[npm 供應鏈攻擊案例、Project Glasswing、Subliminal Learning 研究]

## 9. 跨主題綜合：Q1→Q2 的 5 個拐點（目標 400 字元）
[哪些 Q1 預測在 Q2 成真，哪些被推翻，下半年最值得關注的信號]

## 10. 來源品質評估：17 個 newsletter 的洞察密度（目標 300 字元）
[Tier 1 / Tier 2 / Tier 3 來源分級，推薦訂閱優先序]

## 附錄：8 主題文章索引（目標 200 字元）
[每主題代表性文章 2–3 篇，附路徑]
```

---
## Step 5：驗證（必須執行並完整展示輸出）

依序執行以下命令，將**完整輸出**顯示在 transcript 中：

```bash
wc -m research/reports/[DATE]-ai-news-synthesis-report.md
ls research/prompts/ | grep "ai-"
ls research/prompts/ | grep "ai-" | wc -l
git log --oneline -3
head -30 research/reports/[DATE]-ai-news-synthesis-report.md
```

**重要**：輸出必須顯示在 transcript，不得只說「已完成」。

---
## Step 6：提交並推送

```bash
git add research/reports/[DATE]-ai-news-synthesis-report.md research/prompts/ai-*.md
git commit -m "research: ai-news Q1~2026-05 深度研究 — 4 prompt 檔 + $(wc -m research/reports/[DATE]-ai-news-synthesis-report.md | awk '{print $1}') 字元報告"
git push -u origin HEAD
```

---
## 執行規則

- 不詢問任何確認，直接推進
- Step 2 的 4 個 Sub-Agent 必須在**單一訊息**中同時派遣（平行，非序列）
- 每完成一個 Step 輸出 checkpoint：「Step N 完成：做了什麼 / 驗了什麼 / 剩什麼」
- **不要逐篇讀 131 篇個別日報**：優先 digest 檔，個別檔只補充最新 1 週的新鮮度
- Step 5 的所有命令必須執行並顯示實際輸出
- 遇到單一檔案讀取失敗 → 跳過並記錄，不中斷整體流程
```

---

## 設計說明

| 設計決策 | 原因 |
|----------|------|
| 讀 digest 非 131 篇個別文章 | ai-news 已預先合成 Q1/04/05 digest；逐篇讀會 context rot |
| 4 Sub-Agent 對應 8 主題（2:1 合併） | CLAUDE.md fan-out ≤ 4；8 主題兩兩相關合併為 4 群 |
| Sub-Agent D 讀 digests/ 分析來源品質 | 17 個 newsletter 品質差異大，來源評級是可操作洞察 |
| `ls research/prompts/ | grep "ai-"` | 避免計入舊有非 ai-news 的 prompt 檔（前綴隔離） |
| `wc -m` 非 `wc -w` | 報告含中文，`wc -w` 回傳近零 |
| Step 5 展示完整輸出 | `/goal` Haiku 評估器只讀 transcript，命令輸出必須可見 |
| 4 月 + Q1 作為歷史基線 | 趨勢分析需要時間縱深；僅讀 05 月會缺乏對比脈絡 |
