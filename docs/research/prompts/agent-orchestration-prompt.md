---
title: "Sub-Agent 協作與記憶架構"
type: prompt
---

# Sub-Agent 協作與記憶架構
> 來源：research/tweets/ Agent（7篇）+ Prompt（6篇）分類
> 核心設計：fan-out 上限 4、Frozen Snapshot、三類記憶框架

## 使用方式

**何時使用**：設計多 Agent 工作流、建立跨 session 記憶架構、撰寫高品質 Agent prompt 時。
**貼入哪裡**：`.claude/agents/` 目錄、CLAUDE.md 的 Agent 協作節、或直接作為 sub-agent system prompt。

---

## 核心設計原則

### 1. /goal 工業級 Prompt 的 4 個核心技巧（@MinLiBuilds，8.1分）
- **`<untrusted_objective>` 防注入**：包裹用戶輸入，防止 prompt injection
- **Checklist 具體化**：替代「仔細/認真」等模糊詞，列出可驗證的步驟清單
- **偏向修正句**：「把不確定性當作未完成」—— 一句話翻轉模型的預設停止偏向
- **「停 ≠ 完成」分離**：預算壓力下「虛假完成」是穩定失敗模式，需明確說明持續條件

### 2. 記憶架構三類框架（@lxfater，6.80分）
- **情景記憶**：特定事件、session 歷史（時間序列，自然衰減）
- **語義記憶**：通用知識、技術概念（穩定，需明確更新）
- **程序性記憶**：操作技能、工作流模式（**Agent Skill 蒸餾**：重複任務後自動提煉通用打法）

EverOS 擴展分類（企業級）：
- **Foresight（未來記）**：帶有效時間的提醒，到期自動清除
- **Agent Skill 蒸餾**：含成熟度分評估（0-100%），成熟後凍結

### 3. Frozen Snapshot 設計原則（@BTCqzy1，7.00分）
- 記憶檔案在 session **開始**時注入，非實時更新
- 保護 KV Cache 前綴穩定性（防止 prefix invalidation）
- Agent-curated 非全量記錄：只有 Agent 判斷「重要」的內容才寫入
- 字元硬限制：MEMORY.md ≤ 2,200 字元、USER.md ≤ 1,375 字元

### 4. Fan-out 上限 4（CLAUDE.md 規定）
- 單一訊息最多同時啟動 4 個 sub-agent（防止 context 過載）
- 平行 fan-out 用於：獨立子任務 ≥ 3 個、研究型任務、各類別深讀
- Sub-agent 不自 retry：失敗返回主 Agent 決策，不在 child 層重試
- 通訊限 parent ↔ child：child 間不直接溝通

### 5. 序列執行複合效益（@heynavtoor，6.25分）
- 同一業務流程：Researcher → Editor → Analyst 序列執行
- 每步驟的輸出是下一步驟的高質量輸入（複利效應）
- 角色設計要點：每個 agent 含 YAML frontmatter + 禁止清單 + 結尾語
- 禁止詞清單範例（Editor agent）：leverage / robust / seamless / delve

### 6. 6 Elements of Expert Prompt（@eng_khairallah1，6.35分）
1. **Role**：具體身份（「你是一位審查生產代碼的資深 Go 開發者」，非「helpful assistant」）
2. **Context**：行業、受眾、限制、目標（背景足夠讓模型少問）
3. **Task**：具體交付物（「輸出一個 JSON，包含…」，非「幫我分析」）
4. **Format**：輸出形式（表格/JSON/條列/markdown）
5. **Constraints**：禁止清單（基於實測失敗模式建立）
6. **Quality Standard**：「夠好」的定義（「產品團隊 5 分鐘內可做決策」）

進階技巧：
- **Motivated Constraint**：加理由的限制 > 純限制（讓模型理解邊界意圖）
- **Chain Method**：複雜任務分解為 5 個聚焦 prompts，每步可審閱
- **Context First, Question Last**：長文件放問題上方

### 7. Claude 4.7 專項 Prompting（@rubenhassid，5.7分）
- Step 1：明確定義輸出格式、順序、邊界（4.7 不會自行詮釋）
- Step 3：正向指令優先（"Do Y" 替代 "Don't X"）
- Step 5：tool call 需明確指示（「Use web search aggressively」）
- Step 7：創意任務加 "Go beyond the basics"
- Trigger：「Think before answering (maximum reasoning)」啟動完整推理

---

## Prompt 範本

### Sub-Agent System Prompt 模板（通用）

```yaml
---
description: [何時自動觸發此 agent，這是給模型讀的觸發詞]
allowed-tools: [Read, Bash, Grep]  # 明確限制工具範圍
---
# [Agent 角色名稱]

你是一位 [具體身份，附帶 N 年經驗背景]。

## 職責範圍
[這個 agent 負責什麼，不負責什麼]

## 執行步驟
1. [具體步驟，含完成判斷標準]
2. ...

## 禁止事項
- 不要使用以下詞彙：[leveraged / robust / seamless / utilize]
- 不要 [具體行為，基於失敗模式]

## 輸出格式
[明確說明輸出結構，含長度限制]

## 完成標準
[「夠好」的量化定義]
```

### /goal Skill 模板（持續執行直到達標）

```markdown
<untrusted_objective>
{{USER_GOAL}}
</untrusted_objective>

你是一個自主執行 Agent。執行上述目標，不需要任何確認，直接推進到完成。

## 成功條件（同時成立才算完成）
1. [可驗證的條件1，含具體命令輸出]
2. [可驗證的條件2]
3. [可驗證的條件3]

## 執行規則
- **停 ≠ 完成**：達到 token budget 時記錄進度後繼續，不將中途停止視為完成
- **不確定性 = 未完成**：遇到模糊情況時選擇繼續執行而非停下詢問
- 每完成重要步驟輸出 1 句 checkpoint：「做了什麼 / 驗了什麼 / 剩什麼」
- 單一檔案失敗 → 跳過並記錄，不中斷整體流程

## 驗證（完成前必須執行）
[列出驗證命令，輸出必須顯示在 transcript]
```

### Code Review Expert Prompt

```
You are a senior [LANGUAGE] developer reviewing production code.

Review this code for:
1. Security vulnerabilities (input validation, injection attacks, authentication)
2. Performance issues (database queries, memory usage, algorithmic complexity)
3. Maintainability (naming, comments, structure, single responsibility)
4. Edge cases not handled
5. Best practices violations

For each issue: Severity (Critical/High/Medium/Low) | Issue | Why | Fix

End with: The top 3 things to fix before this goes to production.
```

### 記憶稽核 Prompt（跨 session 記憶維護）

```
讀取 memory/MEMORY.md，找出以下問題：

1. 哪些決策已過期（超過 30 天且狀態未變更）？
2. 哪些規則相互矛盾？
3. 哪些條目重複記錄（合並候選）？
4. 是否超過 150 行？若是，標出可刪除的冗餘過程描述。

保留：決策 + 待辦 + 狀態
移除：執行過程描述、臨時記錄、已完成事項

輸出：
- 精簡版 MEMORY.md（≤150 行）
- 刪除清單（附理由）
```

---

## 關鍵引用

> 「發現模型總往一邊偏，就用一句話告訴它該往另一邊偏。模型本來就覺得自己在判斷。」—— @MinLiBuilds（2026-05-09）

> 「任何記憶系統只需搞懂：記憶分幾類、各存什麼 + 如何抽取、更新、檢索。」—— @lxfater（2026-05-13）

> 「序列執行的複合效益：每步驟的輸出是下一步驟的高質量輸入。」—— @heynavtoor（2026-05-10）

> 「Motivated Constraint：加理由的限制比純限制更有效，讓模型理解邊界意圖。」—— @eng_khairallah1（2026-04-22）
