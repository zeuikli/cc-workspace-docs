# 實作專案

本課程的實作專案讓你從「看懂理論」進入「動手建立」。每個專案都有具體的任務清單、參考實作和可驗證的驗收標準。

四個專案是一條連續的路徑：**建立 workspace → 設計 harness → 把驗證變成資產 → 推廣成基礎建設**。

## 專案清單

### [Project 01：從零建立你的第一個 Workspace](/projects/project-01-init-workspace/)

建立一個能跨 session 記憶、自動初始化環境、有明確驗收定義的完整工作環境。含對照實驗（有／無 CLAUDE.md）與定期審閱機制。

**前置課程**：Lecture 01、02、05
**產出**：CLAUDE.md、claude-progress.md、feature_list.json、SessionStart / Stop hooks

---

### [Project 02：設計你的 Harness](/projects/project-02-harness-design/)

設計並實作 Planner / Generator / Evaluator 三層架構，加上獨立的對抗性 verifier 與安全 hooks。含 Oracle 先驗與 gate 選擇稽核。

**前置課程**：Lecture 03、04、06
**產出**：Planner 提示詞、`scripts/evaluate.sh`、adversarial verifier agent、PreToolUse security hook

---

### [Project 03：把驗證編碼成 Skill](/projects/project-03-verification-skill/)

把 Project 02 的 shell 腳本升級成可重用、可被 Claude 主動呼叫的 Skill。走一遍評估驅動開發與 Claude A / Claude B 迭代法。

**前置課程**：Lecture 07、10
**產出**：驗證 Skill（含 Progressive Disclosure 結構）、3 個評估場景與 baseline、迭代記錄

---

### [Project 04：Plugin 化與自動化治理](/projects/project-04-plugin-automation/)

把前三個專案的成果打包成可分發的 Plugin，接上排程或事件觸發的自動化，補上成本與安全護欄。

**前置課程**：Lecture 11、12
**產出**：可安裝的 Plugin、一個運作中的 Routine 或 GitHub Actions、憑證隔離設定、審閱機制

---

## 對照表

| 專案 | 解決的問題 | 完成後你能說 |
|------|-----------|------------|
| 01 | Claude 每次都要重新告知專案規則 | 「新 session 開起來它就知道」 |
| 02 | Claude 宣布完成但實際沒完成 | 「它宣布完成時，我有獨立證據」 |
| 03 | 驗證綁在一個專案、要我記得跑 | 「驗證是資產，會自己在對的時機發動」 |
| 04 | 只有我的機器上有這套設定 | 「團隊裝一個 plugin 就有相同的護欄」 |

## 學習建議

1. **按順序完成**：每個專案都建立在前一個的產出上。
2. **用你自己的實際專案**：比用範例專案學得快得多，而且產出立刻可用。
3. **記錄失敗**：每個失敗都是 Ratchet 原則的素材——規則應該追蹤到一次具體的失敗。
4. **從小開始**：先建立最小可用 Harness，再逐步迭代。
5. **注意可刪與不可刪的邊界**：程序性鷹架會隨模型進化而過時，**驗證閘門與不可逆操作確認不會**。每次審閱都重新確認這條線。
