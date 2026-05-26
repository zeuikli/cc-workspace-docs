# R12 強化提案 — unverified_success 閘門狀態 + 失敗歸因分層

> **來源**：`research/reports/2026-05-17-harness-engineering.md` §「2026-06-05 深度更新」5 補充主題的「對 cc-workspace 的意義」。
> **接地**：5 標籤分類 / H0–H3 ladder / 8 trace types 經主對話親自 grep `research/papers/2026-05-13-ai-harness-engineering-runtime-substrate-2605-13357.md`（行 46–73）原文確認。
> **狀態**：APPLY 完成（commit b5715db8）。Landing 經 AskUserQuestion 核准（R12.1 進條文 + R12.2/3 進 GOTCHA）。
> **Falsifiable Prediction（prompt-lifecycle 慣例）**：R12.1 添加**不削弱 R1–R11 compliance**——eval 條件 = ① healthcheck FAIL=0（實測 110/0/3 ✅）② auto-load byte ≤ 19,000（實測 18,993，餘 7 ✅）③ 既有 §R1–§R11 anchor 不變（measure.sh --gate PASS ✅）。回歸 ≥5pp -> `git revert`（R11 / autoload-evolution 閉環）。
> **接地審計（R12.1 dogfood）**：5 標籤 / H0–H3（Runtime Substrate `2605.13357` 行 46–73）+ Categorical 8B 全 0（`2605.12239` 行 92–93）+ Vesper 16.6%/0%（`2605.15221` 行 107–110）**全經主對話親自 grep**，非報告轉述。

---

## 0. 動機 — 本提案自身的 unverified_success 範例

來源報告審計表（行 1156）標 Runtime Substrate「✅ 原文命中」，且本次更新聲明「每數字親 grep」（行 1091）——**卻 ship 了一個錯誤 cross-ref**：報告行 1117 引用「MEMORY Lesson 2026-06-05-B」指稱「subagent 報 clean 但實際殘留問題」，但 MEMORY 實際的 2026-06-05-B 是「provenance header 過度宣稱」。真正命中 `unverified_success` 的是：

- **Lesson 2026-06-05-A**：sub-agent 自稱「親驗」的數字直接寫進產物 -> advisor 攔截 3 處誤植（ACE −82.6% / TTFT 13–31% / MetaGPT −40%）。
- **Lesson 2026-06-04-G**：memory-compactor 自報「32 保留」實際流失 12 個 Lesson。
- **Lesson 2026-06-05-D**：同一 adjudicate.sh 主對話跑 6/6、經 sub-agent 中介 4/6（block-dangerous hook 污染）。

「聲明已驗證 + 審計表打勾 + 實際 ship 錯誤」= 教科書級 `unverified_success`：correct-looking behavior without proper evidence structure。這正是本提案要防的失敗模式。

---

## 1. 核心概念（Runtime Substrate 2605.13357，親 grep 接地）

### 5 標籤結果分類（原文行 69–73，報告只列了 3 個）

| 標籤 | 定義 | 對應 cc-workspace |
|------|------|------------------|
| `autonomous_verified_success` | 需求達成 + 充分證據 + 無缺 harness 介入 | 主對話親自跑驗證 + 展示輸出（R4/R12 達標態）|
| `assisted_verified_success` | patch 正確但需人工協助 | advisor / 使用者 gate 後達成 |
| **`unverified_success`** | 行為看似正確但**缺證據結構** | **本 workspace 反覆失敗模式**（A/D/G）|
| `failed` | 行為或測試失敗 | R12 Fail Loud 已涵蓋 |
| `unsafe_invalid` | 測試被削弱 / 出現無關編輯 | 命中 R3 外科刀 + compactor over-prune（G）|

### H0–H3 成熟度梯度（原文行 58–61）

- H0 task + repo｜H1 +tool/test registry｜H2 +memory/task-state｜**H3 +deterministic checks / failure attribution / verification protocols**
- 四層**全能產出能跑的 patch**，但只有 H3 有可審計證據包。「通過測試」≠「有可審計的可靠性」。
- cc-workspace 現況 ≈ H2–H3 之間（K×M 稽核到位，Entropy Auditor 缺）。

### 失敗歸因分層（Life-Harness 2605.22166 4 類 + Runtime Substrate attribution log）

報告引入 Life-Harness 4 generic layers，但 advisor 指示**改用本 workspace 實際反覆失敗**而非進口標籤：

| 歸因層 | 本 workspace 實例 | 已知防範 |
|--------|------------------|---------|
| **Verdict 層** | subagent/workflow 自報 verdict 非證據 | subagent-strategy.md:67（已存在）|
| **Execution-env 層** | 確定性 gate 經 sub-agent 中介被污染 | Lesson 2026-06-05-D（adjudicate 絕不經 sub-agent）|
| **Provenance 層** | 數字 grep 存在 ≠ 對應正確；header 過度宣稱 | Lesson 2026-06-04-G / 2026-06-05-A/B |
| **Entropy 層** | 孤兒研究檔 / 殘留 worktree / stale cross-ref | Lesson 2026-06-04-E（無常態檢查）|

---

## 2. 強化提案（行為 delta，非重述既有）

> 自檢通過：以下每條都防一個 R12 + subagent-strategy.md:67 **尚未防**的失敗。

### 2.1 R12.1 — unverified_success 閘門狀態（核心）

> subagent / workflow 回報的「成功」一律記為 **`unverified_success`** 中間態，**直到主對話親自跑確定性檢查**（grep / test / healthcheck）才可升為 verified。`unverified_success` **不得**作為「完成」回報給使用者。確定性 gate（adjudicate / done-check）**絕不經 sub-agent 中介**（Lesson 2026-06-05-D）。

- **行為 delta**：subagent-strategy.md:67 說「verdict 非證據，採信前必 grep」；本條給這個中間態一個**名字 + 閘門語義**——明確「未驗證前不可宣告完成」，並把 Lesson 2026-06-05-D 的「gate 不經 sub-agent」從 MEMORY 提升為 R12 條文。

### 2.2 R12.2 — 失敗歸因到層

> 驗證失敗時，YOU MUST 將失敗歸因到一層（Verdict / Execution-env / Provenance / Entropy），不接受「隨機修補」。歸因 = 後續修復方向的前提（Runtime Substrate：observation ≠ diagnosis）。

- **行為 delta**：現 R12 只要求「Fail Loud」（失敗要明示），未要求**結構化歸因**。隨機修補是本 workspace 多次 debug 繞圈的根因。

### 2.3 R12.3 — Entropy 自檢（H3 補完）

> 宣告「完成」前的 PGE 除 healthcheck 外，加一道 entropy 自檢：① 本次產生的研究/報告檔已有入口引用（無孤兒，Lesson E）；② 無殘留 worktree（`git worktree list`）；③ 無 stale cross-ref / 被削弱測試（`unsafe_invalid` 防線）。

- **行為 delta**：把 Lesson 2026-06-04-E 的事後補救升為**常態 PGE 檢查項**，對應 Runtime Substrate Entropy Auditor。

---

## 3. Landing 選項（須使用者決策 — auto-load 修改 blocks）

byte 預算：auto-load 現 **18,455 / 19,000，餘 545 B**。

- **R12.1 條文**（≈ 350–400 B）放 core.md §R12 -> 餘裕剩 ~150 B，逼近上限。
- **R12.2 / R12.3** 全文放 GOTCHA（零 byte 成本）+ R12 一行指針（≈ 80 B/條）。

三種 landing 形狀見 AskUserQuestion。所有 auto-load 修改走 `/autoload-evolution`（≤1 規則/cycle、≤50 行 diff、eval 回歸 ≥5pp 則 revert）—— R11 convention-first。

---

## 4. 其餘 3 主題處置（章節完整性）

| 主題 | 「對 cc-workspace 的意義」 | 處置 |
|------|--------------------------|------|
| 1 自動優化三世代 | 「摘要丟失改進信號」與 workspace 同源 | **無新動作**——已由 subagent-strategy.md:67 + autoload-evolution 覆蓋；GOTCHA 補一句「trace 不壓縮」 |
| 3 能力下限 + 弔詭 | Capability Floor 升級為論文背書；升 Opus 須同步加強驗證 | **GOTCHA 補論文引用**（Categorical 8B 全 0 / Vesper 16.6% hack）+ 認知註記；不動 auto-load |
| 4 可遷移性 | 12-Rule = 可跨模型遷移 artifact | **無新動作**——認知確認（MEMORY R1-R12 存活已記）|

> 守 R2：主題 1/4 已被現有條文覆蓋，**不為湊「全部處理」而新增冗餘規則**。主題 3 僅補 GOTCHA 背書，不佔 auto-load byte。
