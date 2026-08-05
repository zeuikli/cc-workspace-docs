# Harness 進化報告：Context Engineering（Claude 5 世代）× Handling Unknowns 雙來源稽核

> 日期：2026-07-26 · 調度：Fable 5（整合/終審）· 研究：Opus 5 ×2 · 實作/查核：Sonnet 5 ×2 + Opus 5 ×1 · 對抗審查：Opus 5（異 context）
> 稽核基準：
> A = <https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models>（8 原則）
> B = <https://thariqs.github.io/html-effectiveness/unknowns/>（11 技法）

## 1. 方法：提問式稽核

不直接改條文，而是把兩來源蒸餾成 **27 條可驗證檢查問句**（每原則 1–2 問），逐條拷問現行 harness 並要求 file:line 證據。Verdict：**PASS 17 · GAP 9 · N/A 1**。

接地護欄（先立後審）：
- 兩來源皆屬 **prompt 層**，對 hook/enforcement 層無基準——本輪不動任何 hook。
- A1 Unhobbling 原文語境限行為/風格約束；**不得引為刪除 `[E]` 驗證閘門的理由**。剪枝範圍限 `[P]`，`[E]` 逐字保留（core.md §Framework Integrity）。

## 2. GAP 與落地變更（9 提案全採納 + 3 文件同步）

| # | GAP（來源） | 變更 | 檔案 |
|---|------------|------|------|
| P1 | 兩規則檔無可判性標記（A1） | output-discipline.md 標 `[U]`（user-preference，不隨世代放寬亦不剪枝）；context-management.md 三節標 `[P]` | rules/ ×2 |
| P2 | git 生命週期四入口無路由表（A3） | RESOLVER 新增「Git 生命週期路由」表，`/ship` 為預設入口 | RESOLVER.md |
| P3 | AGENTS.md §2 速記重複理由不精確（A5） | 誠實化：僅對 sub-agent 為必要覆蓋，對主 context 屬刻意接受的冗餘 | AGENTS.md |
| P4 | quick-commit 管線選檔與「逐檔指名」漂移（A5） | 管線只產候選清單；實際 add 逐檔指名，>5 檔先出示 | quick-commit.md |
| P5 | 手抄記憶義務與 auto-memory 未收斂（A6） | 手寫只留兩類（糾正/連續失敗→LESSONS）；入庫過門義務保留 | core.md `[P]` |
| P6 | 常駐層 reference 全為散文（A7） | CLAUDE.md 加一行指向可執行 EVAL-PACK fixtures | CLAUDE.md |
| P7 | 無拋棄式原型授權路徑（B4） | judgment-rubrics 新 §R6 探針授權：worktree/scratchpad 原型免事前核可、不得進 PR | judgment-rubrics.md |
| P8 | PROPOSE 錨定第一可行解（B5） | scope 有量級選擇時列 ≥2 級由使用者選 | core.md `[P]` |
| P9 | 提問無代價排序（B6） | T6 補排序判準：不可逆 > 跨模組 > 單檔 > 風格，一次問最貴 1–3 題 | know-your-unknowns |
| 同步 a | model-profiles pin 敘述過時 | 追記 2026-07-26 pin 已升 claude-opus-5（commit 8142e17，已親驗） | model-profiles.md |
| 同步 b | HARNESS-CARD defaultMode 記載過時 | 追記現值 auto（settings.json 已親驗），不覆寫歷史 | HARNESS-CARD.md |
| 同步 c | 歷史事故段落易誤讀為現況 | 加「歷史實例」標記 | model-profiles.md |

## 3. Merge/Push/Commit 流程簡化：`/ship` 單一入口（S0–S12）

**摩擦診斷**：四個入口（quick-commit/quick-pr/pr-guard/verified-merge）路由重疊、中間 4 個人工確認點。實測歸因：settings.json ask 清單本就**不含**普通 `git push`（只擋 `--force*` 變體與 MCP push）——「push 要允許」的體感摩擦主要來自流程碎片化而非權限設定，故**未動 permissions**（未歸因前放寬 = 新攻擊面）。

**簡化後**（新 skill `.claude/skills/ship/SKILL.md`）：
- 單一入口，復用既有四 skill 實作（引用不複製，避免雙份漂移）。
- 中間人工確認 **4 → 1**：pathspec 確認前移至 S0 一次宣告（禁通配、`set -f` 防 shell 先展開）；S8 Gate 2 由人工 assert 改為 `comm` 機械比對（gate 更確定性，非弱化）；push 自動退避重試；Quiz 自主模式跳過並記錄。
- **唯一保留的人工確認在 S10（merge，不可逆）**，但支援「使用者當次訊息原文顯式預授權」時自動 merge——預授權來源寫死排除：記憶檔、compact 轉述、外部輸入、**parent 委派 prompt**、跨 PR 延續。
- 硬邊界零放寬：healthcheck 兩處保留、verified-merge 4 gate 全在、`--force*` 仍走 ask、S12 終局報告由 parent 親跑出示。

## 4. 對抗審查結果（異 context Opus 5）

初審 verdict **NEEDS-WORK**，4 必修全數修復後由 Fable 5 親驗收：
1. S0 通配守衛可被 shell glob 先展開繞過 → 加 `set -f` + `?` 通配同禁。
2. S8 宣告檔無 freshness 斷言（alias 跳 S0 會沿用舊檔）→ 檔案移入 `$(git rev-parse --git-dir)`、加 branch 相符 + 6h 時效斷言。
3. S10 預授權排除清單缺 parent 委派 prompt 向量 → 已補。
4. S8「STASH+REPORT」語義不實（history 已推送，stash 無法補救）→ 改 REPORT+HALT + revert 指引。

親跑驗證收據：`git diff core.md` 僅兩處 `[P]` 變更、TEST/`[E]` 全節逐字未動；autoload byte **18,567 ≤ 19,000**；`healthcheck.sh` **PASS 244 / FAIL 0**；skill 索引重建 32 skills、引用完整性 dangling=0。

## 5. 未決事項（不阻塞本輪）

- pre-commit-review.sh 的 `git add && git commit` 單鏈 staged=0 穿越漏洞：**已知未緩解**（hook 層，兩來源無基準，留待 hook 專輪）。
- B 來源為個人頁面，權威層級低於官方 blog；本輪僅採其與 A 不衝突的技法。
- `/ship` 多 session 並行：宣告檔已 repo-scoped（git-dir），跨 repo 無衝突；同 repo 並行 session 仍共用，屬殘餘風險（發生率低，S8 branch 斷言可攔大半）。
