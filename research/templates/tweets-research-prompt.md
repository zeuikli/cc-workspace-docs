# Tweets 目錄深度研究 Prompt
# 目標：research/tweets/ 全部文章分類 → 可實作 prompt 檔 + 研究報告
# 使用方式：先貼 /goal，再貼工作 Prompt

---

## STEP 1：貼入 /goal 條件

```
/goal 下列三個條件同時成立（評估依據是 Claude 在 transcript 中執行命令的實際輸出）：
1. wc -m research/reports/[DATE]-tweets-synthesis-report.md 的輸出數字 ≥ 3000
2. ls research/prompts/ | wc -l 的輸出數字 ≥ 4
3. git log --oneline -1 包含 "research: tweets" 字樣
若以上輸出尚未在對話中出現，Claude 需執行 Step 5 驗證命令並展示結果，再由評估器判斷。
若超過 20 輪仍未達成，停止並輸出截至目前的完成狀態報告。
```

---

## STEP 2：貼入工作 Prompt

```
你是一個自主研究 Agent。執行以下任務，不需要任何人工確認，直接推進到完成。

---
## 任務目標

研究 research/tweets/ 目錄中的所有文章，按分類整理核心洞察，產出：
1. 每個主要分類一個可實作 prompt 檔（存至 research/prompts/）
2. 一份完整研究報告（存至 research/reports/[DATE]-tweets-synthesis-report.md，目標 3000–5000 字元，wc -m 計算）

---
## Step 1：讀取分類概覽

執行：
```bash
cat research/tweets/README.md
```
提取六大分類（SKILL / Rule / Hook / Agent / Prompt / Others）的文章清單與評分分布。

---
## Step 2：平行 Sub-Agent 深讀（4 個並發，不超過 4）

在**單一訊息**中同時派遣以下 4 個 Sub Agent，每個回傳 ≤600 字的結構化摘要：

**Sub-Agent A — SKILL 分類**
- 範圍：README 中標記為 SKILL 的所有文章（約 8 篇）
- 任務：Read 每篇檔案，提取：① 核心論點（2 句）② 可操作設計原則（條列）③ 最高價值引用（原文 ≤80 字）④ 評分與排名
- 回傳格式：
  ```
  ## SKILL 分類摘要
  ### [文章標題] (評分: X.X)
  - 核心論點：
  - 設計原則：
  - 關鍵引用：
  ```

**Sub-Agent B — Rule + Hook 分類**
- 範圍：README 中標記為 Rule（約 40 篇）+ Hook（1 篇）的所有文章
- 任務：同 A，額外識別跨文章的共識規則與矛盾點
- 回傳格式：同 A，末尾加「跨文章共識：」與「矛盾點：」

**Sub-Agent C — Agent + Prompt 分類**
- 範圍：README 中標記為 Agent（約 6 篇）+ Prompt（約 6 篇）的所有文章
- 任務：同 A，額外提取可直接複製使用的 prompt 片段
- 回傳格式：同 A，末尾加「可複製 prompt 片段：」

**Sub-Agent D — Others 分類（高分篩選）**
- 範圍：README 中標記為 Others 的文章，只讀評分 ≥ 7.0 的篇目
- 任務：同 A，標注每篇的獨特貢獻（其他分類沒有涵蓋的洞察）
- 回傳格式：同 A，末尾加「獨特貢獻：」

---
## Step 3：產生分類 Prompt 檔

根據 Sub-Agent 回傳的摘要，為每個主要分類產生一個可實作 prompt 檔案：

**檔案 1：`research/prompts/skill-design-prompt.md`**
- 主題：Claude Code SKILL 設計最佳實踐
- 內容：從 SKILL 分類提煉的設計原則 + 可直接貼入 SKILL.md 的 prompt 模板
- 格式：markdown，含「使用方式」「設計原則」「Prompt 範本」三節

**檔案 2：`research/prompts/rule-engineering-prompt.md`**
- 主題：CLAUDE.md 規則工程與 hook 設計
- 內容：從 Rule + Hook 分類提煉的規則撰寫原則 + 規則模板
- 格式：同上

**檔案 3：`research/prompts/agent-orchestration-prompt.md`**
- 主題：Sub-Agent 協作與記憶架構
- 內容：從 Agent + Prompt 分類提煉的協作模式 + orchestration prompt 範本
- 格式：同上

**檔案 4：`research/prompts/strategic-insights-prompt.md`**
- 主題：Karpathy / bcherny 等策略洞察的實踐轉化
- 內容：從 Others 高分文章提煉的策略原則 + 應用 prompt
- 格式：同上

每個檔案結構：
```markdown
# [主題]
> 來源：research/tweets/ [分類] 分類，基於 [N] 篇文章

## 使用方式
[何時使用、貼入哪裡]

## 核心設計原則
[條列，每條附來源文章]

## Prompt 範本
\`\`\`
[可直接複製使用的 prompt 文字]
\`\`\`

## 關鍵引用
[原文引用，附出處]
```

---
## Step 4：產生完整研究報告

撰寫報告，存至 `research/reports/[DATE]-tweets-synthesis-report.md`。

報告結構與字元配額（wc -m，含標點）：
```markdown
# research/tweets 深度研究報告
**日期**：[DATE] | **文章數**：130 篇 | **分類**：6 個

## 執行摘要（目標 300 字元）
[整體發現的 3 個核心主題]

## 1. SKILL 設計：從 247 到 23 的過濾哲學（目標 600 字元）
[SKILL 分類的核心洞察，含評分最高文章的具體論點]

## 2. 規則工程：CLAUDE.md 的精煉之道（目標 900 字元）
[Rule 分類的共識規則，含矛盾點分析與解決建議]

## 3. Hook 架構：8 個防護層的設計邏輯（目標 400 字元）
[Hook 設計原則，含具體 hook 腳本的設計意圖]

## 4. Agent 協作：記憶架構與跨 session 持續性（目標 500 字元）
[Agent 分類的協作模式，含記憶回路設計]

## 5. Prompt 工程：6 元素框架與 Motivated Constraint（目標 500 字元）
[Prompt 分類的核心框架，含可操作的 prompt 設計原則]

## 6. 策略洞察：Karpathy × bcherny × Mnilax 的交集（目標 500 字元）
[Others 高分文章的策略層洞察，找出三者共識]

## 7. 跨分類綜合：12 條可立即實作的原則（目標 400 字元）
[從全部 130 篇提煉的 12 條行動原則，每條 1 句]

## 8. 評分分析：高價值文章圖譜（目標 300 字元）
[評分 ≥ 8.0 的文章清單，說明高分原因]

## 附錄：分類文章索引（目標 300 字元）
[每分類文章數、評分範圍、代表文章]
```

---
## Step 5：驗證（必須執行並完整展示輸出）

依序執行以下命令，將**完整輸出**顯示在 transcript 中：

```bash
wc -m research/reports/[DATE]-tweets-synthesis-report.md
ls research/prompts/
ls research/prompts/ | wc -l
git log --oneline -3
head -30 research/reports/[DATE]-tweets-synthesis-report.md
```

**重要**：輸出必須顯示在 transcript，不得只說「已完成」。

---
## Step 6：提交並推送

```bash
git add research/reports/[DATE]-tweets-synthesis-report.md research/prompts/
git commit -m "research: tweets 全分類深度研究 — 4 prompt 檔 + $(wc -m research/reports/[DATE]-tweets-synthesis-report.md | awk '{print $1}') 字元報告"
git push -u origin HEAD
```

---
## 執行規則

- 不詢問任何確認，直接推進
- Sub-Agent 必須在**單一訊息**中同時派遣（平行，非序列）
- 每完成一個 Step 輸出 checkpoint：「Step N 完成：做了什麼 / 驗了什麼 / 剩什麼」
- 遇到單一檔案讀取失敗 → 跳過並記錄，不中斷整體流程
- Step 5 的所有命令必須執行並顯示實際輸出
```

---

## 設計說明

| 設計決策 | 原因 |
|----------|------|
| 4 個 Sub-Agent（非 5）| CLAUDE.md 規定 fan-out 上限 4；Hook 僅 1 篇合併至 Rule |
| `wc -m` 計算字元 | `wc -w` 對中文回傳近零；`wc -m` 計算 Unicode 字元 |
| Step 5 展示完整輸出 | `/goal` Haiku 評估器只讀 transcript，命令輸出必須可見 |
| 4 個 prompt 檔（非 6）| Others 高分文章整合為 strategic-insights，Hook 合入 rule-engineering |
| Sub-Agent 回傳 ≤600 字 | 防止 context rot；摘要而非原文搬運 |
