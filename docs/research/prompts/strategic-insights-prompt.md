---
title: 策略洞察：Karpathy × Mnilax × bcherny 的實踐轉化
type: prompt
---

# 策略洞察：Karpathy × Mnilax × bcherny 的實踐轉化
> 來源：research/tweets/ Others 高分文章（評分≥7.0）+ Rule 分類策略層
> 核心共識：Context Engineering First；Thin Harness, Fat Skills；Token Budget 是 Compliance 前提

## 使用方式

**何時使用**：架構決策前、設計 AI Engineering 工作流、評估技術選型時。
**貼入哪裡**：CLAUDE.md 策略節、`subagent-strategy.md`、`harness-design.md`；或作為架構評審 checklist。

---

## 核心設計原則

### 1. Context Engineering 是工業級 LLM App 核心（@karpathy，7.35分）
- 「Prompt engineering」已過時，精確術語是「Context engineering」
- Context 是雙刃劍：太少 → 失敗；太多（不相關）→ 成本上升 + 效能下降
- 工業強度 LLM App 的厚重層：控制流設計 / LLM 路由 / generation-verification UIUX / guardrails / evals / parallelism
- **可操作定義**：「精準填充 context window，既是科學也是藝術」

### 2. 三層架構：Thin Harness + Fat Skills + Fat Data（@garrytan，8.8分）
- **Thin Harness**（≤200 行確定性代碼）：只做路由、工具調度、錯誤邊界
- **Fat Skills**（≥90% 判斷工作）：每個 Skill 是「函數呼叫」，可自我改進
- **Fat Data**（知識層）：Agent 擁有並維護，包含 MEMORY.md、規則庫、範例庫
- 生產力 100x 差距來自架構設計，非模型智能

### 3. Latent vs. Deterministic 分野（@garrytan 原創，Others 獨有洞察）
- **Latent（用 Claude）**：分類 / 摘要 / 提取 / 創意生成 / 判斷
- **Deterministic（用確定性代碼）**：路由 / 重試 / HTTP status code / 數學計算
- 最常見的 Agent 設計錯誤：讓 LLM 做確定性決策（or 讓確定性代碼做模糊判斷）
- **Diarization 能力**：讀取多文件後生成單頁結構化摘要，是 RAG/SQL 無法替代的核心

### 4. CLAUDE.md 是會腐爛的 Cache（@Mnilax，8.95分，Others 獨有洞察）
- 73% 規則在 90 天後已過時（80行 Python 實測 100 sessions / 6M tokens）
- 三類刪除原因：① 一次性修正變成永久規則 ② context 過期 ③ 自我矛盾
- **Dreaming 維護週期**：dream → diff → apply → 14-30 天 → 再 dream
- 成本：$4.20/pass，cache hit 後 $0.80；個人 7 天追蹤改善 41%

### 5. Multi-Model Router 架構（@DeRonin_，7.15分）
- $4,200 → $312/月（92.6% 降幅）的具體策略
- **三層 Router**：Premium（Opus，10% 架構/設計決策）→ Workhorse（Kimi 2.6，90% 日常實作）→ Utility（Haiku，cleanup/格式化）
- Kimi 2.6 對比：$0.04 vs Sonnet $0.12 per refactor，品質 9.2 vs 9.0（幾乎無差）
- 批次請求：70-90% input token 節省
- **30 天 Rollout 方案**：Week 1 計量 → Week 2 分類任務 → Week 3 路由器 → Week 4 微調

### 6. Karpathy 4 Rule → 12 Rule 擴展（@Mnilax，7.55分）
**原始 4 條（Floor，適用任何 LLM）**：
1. Think Before Coding（實作前顯露假設）
2. Simplicity First（最小能解決問題的代碼）
3. Surgical Changes（只動最小必要範圍）
4. Goal-Driven Execution（先寫成功條件，迭代到達標）

**新增 8 條（May 2026，修補 agent-driven 盲點）**：
5. LLM Only for Judgment（routing/retry/status 留給確定性代碼）
6. Hard Token Budget（per-task 4k / per-session 30k）
7. Surface Conflicts（兩個矛盾模式 → 選一，不混用）
8. Read Before Write（改動前先讀 exports/callers/utilities）
9. Test Verifies Intent（能通過任何實作的測試 = 沒有測試）
10. Checkpoint（每重要步驟：做了什麼/驗了什麼/剩什麼）
11. Convention First（codebase 慣例 > 個人偏好）
12. Fail Loud（略過步驟或跳過驗證必須明示，不用「完成」掩蓋）

**量化效果**：錯誤率從 41% 降至 3%；compliance 4條→78%，12條→76%（零額外 overhead）

### 7. Goal-Driven 哲學（@karpathy，7.15分，20年工作流最大改變）
- Karpathy：「20 年最大工作流改變」是交出 Goal 而非步驟
- Slopacolypse 預言：平均 AI 代碼品質會下降，精英差距拉大
- **系統設計師角色**：人從「prompt 保姆」升級為「系統設計師」；循環週期從每分鐘 → 每週
- 可外包思考，無法外包理解（@stephzhan）：執行可外包；「懂這個為什麼」不能

### 8. Capability vs Discipline Skill 框架（@Mnilax，Others 補充獨有洞察）
- 社群 90% 品質改善不是來自新 Capability 而是 Discipline enforcement
- 安裝順序比清單更重要（週期性稽核優於靜態清單）
- 247個 Skills → 23個（9.3% pass rate）的篩選哲學

---

## Prompt 範本

### 架構評審 Prompt（Fat vs Thin 決策）

```
評審以下架構設計，識別 Latent vs Deterministic 邊界是否正確：

[描述當前架構]

請回答：
1. 哪些決策被錯誤地委給了 LLM？
   - routing 邏輯（應確定性）
   - retry 策略（應確定性）
   - HTTP status code 選擇（應確定性）
   - 錯誤分類（可能是 LLM 判斷）

2. 哪些確定性代碼可以改為 LLM 判斷以提升靈活性？

3. Harness 是否 ≤200 行？若超過，哪些部分可移到 Skills？

輸出：重構建議 + 優先級（高/中/低）
```

### CLAUDE.md Dreaming 稽核 Prompt（每 14-30 天執行）

```
你是一個分析 CLAUDE.md 規則品質的稽核 Agent。

讀取以下 CLAUDE.md 內容：
[貼入當前 CLAUDE.md]

假設這些規則服務的是一個 AI coding session。請分析：

1. **一次性修正型規則**：哪些規則像是「有一次 Claude 做錯了，所以我加了這條」？（加入後未再被測試）
2. **過期 context**：哪些規則引用了不存在的檔案/工具/流程？
3. **自我矛盾**：哪兩條規則互相衝突？
4. **永久規律**：哪些規則確實在持續防止真實問題？

輸出：
- 刪除候選（附理由）
- 精簡版 CLAUDE.md（≤200 行）
```

### 策略洞察綜合 Prompt（季度技術決策）

```
我需要評估以下技術決策，請從 Context Engineering 和 Harness Design 兩個視角分析：

[描述決策]

評估框架：
1. **Context 影響**：這個決策如何影響 context 品質？會增加還是減少 token overhead？
2. **Latent/Deterministic 邊界**：這個決策是否尊重了邊界？
3. **Harness Thickness**：這個設計讓 harness 變厚還是變薄？
4. **可觀測性**：能否量化改善（像 27%→65% productive tokens）？

輸出：建議 + 最主要的 trade-off + 量化成功標準
```

---

## 關鍵引用

> 「Context engineering 是工業級 LLM App 的核心技術；精準填充 context window 既是科學也是藝術。」—— @karpathy（2025-06-25）

> 「LLM 生產力 100x 差距來自架構設計，非模型智能。Fat Skills，Thin Harness。」—— @garrytan（2026-04-11）

> 「CLAUDE.md 是會腐爛的 cache。73% 規則在 90 天後已過時。需要維護週期，不是一次性設定。」—— @Mnilax（2026-05-14）

> 「你可以外包思考，但無法外包理解。人的角色從執行者上移至理解者與指揮者。」—— @stephzhan（2026-04-29）

> 「20 年來最大的工作流改變：交出 Goal，不是步驟。」—— @karpathy（2026-01-26）
