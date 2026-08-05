---
title: "Session Insights — harness↔The Loop /loop 研究（兩輪動態迴圈）"
date: 2026-06-14
status: complete
commits: ["afa6eecb（5輪 gap 研究 + 6 論文）", d7068ffe（有效性對抗檢查附錄）]
related: ["2026-06-14-harness-loop-gap-research.md（findings + 有效性檢查附錄）", .claude/refs/harness-loop.md（比對基準）, .claude/rules/core.md（行為契約）]
scope: 方法論反思（非 findings）；findings 見 research/reports/2026-06-14-harness-loop-gap-research.md
type: session-insight
---

# Session Insights — harness↔The Loop /loop 研究

> 本檔記錄**迴圈如何跑**（process）的洞察，與 gap-research 報告的**findings**（what）分離。核心：兩輪 `/loop` 動態模式，第一輪求廣（找 gap），第二輪求真（有效性過濾）；最大方法論收穫 = `grep-confirmed-absent ≠ failure-validated`。

---

## 1. 兩輪迴圈的結構（self-pacing 動態模式）

| 輪 | 鏡頭 | 產出 | 收斂訊號 |
|----|------|------|---------|
| **Loop-1（AM，5 iter）** | **breadth**：harness-loop.md §Frontier vs research/papers 找未掛載 gap | 12 confirmed gap（橫跨六階段）+ 6 篇新論文收錄 | iter-5 MED 論文 dry round |
| **Loop-2（PM，1 iter）** | **validity**：對 12 gap 跑 APPLY-gate #2 有效性檢查 | 12→3 HIGH_VALUE + 2 REDUNDANT + 7 DEFER | gated（下一步 APPLY 需使用者核准） |

**洞察 A — 換鏡頭防 dry-round 空轉**：Loop-1 iter-5 已 dry（MED 論文 0 gap）。若 Loop-2 沿用同鏡頭（再掃論文）必然繼續 dry = 燒 token 無產出。**換鏡頭（breadth→validity）讓同一 /loop prompt 在語料耗盡後仍有真實工作**。動態 /loop 的價值不在「重複同動作」，在「self-pace 時判斷下一個值得做的 facet」。

---

## 2. 最大方法論收穫：grep-confirmed-absent ≠ failure-validated（Lesson 2026-06-14-C）

Loop-1 的 12 gap 全部通過「harness-loop.md 沒寫這條」的 **grep 檢查**（exit=1 = 0 命中）。看似嚴謹，但**漏了一道關**：

> gap「**沒寫**」（grep）與 gap「**該掛載**」之間，隔著 harness-loop.md APPLY 前置 gate 第 2 點的**有效性檢查**：「此規則若早存在，能否擋下一個**真實發生過**的錯誤？」

Loop-2 補做此檢查（對照 21 條 MEMORY lesson 為真實失敗 corpus），**12 gap 只有 3 通過**：
- 9 個是論文驅動（paper 有講）非失敗驅動（workspace 沒因此吃過虧）。
- 略過有效性檢查直接從「論文有講 + 我們沒寫」跳到「該掛載」= **self-preferential bias 的一種**：為了讓自己找的 gap 存活，硬把學術關切當成必要規則。

**接地三連**（HIGH_VALUE 才有的 workspace 鐵證）：
- **F9**：`harness-loop.md:68` 誤植 CAR「單視角偏差」→ grep CAR 全文 count=0（既存錯誤，非假想）。
- **F7**：≡ Lesson 2026-06-13-B（stop hook 寫 cost-log 但不重產衍生 usage-report.json = write>0∧read-stale；Portal 看舊資料靠手動補）。
- **F3**：6 起 advisor-rescue 全記「內容更正」、0 起記 assisted≠autonomous。

---

## 3. reverse-advisor 在對抗審查中推翻初判（F11 案例）

F11（typed-failure 叢集）初判傾向 CONFIRMED——「扁平 GOTCHAS lesson 不如三元組分群」聽起來合理。但 Opus/ceiling 的 reverse-advisor 自審推翻：

> `MEMORY:96「分支事件再應驗 2026-06-04-B」` 證明**扁平 lesson 能跨 session 正確召回**（worktree×11、verdict-非證據×4 是漸進精化非重複踩坑）。三元組分群是 organizational 升級，**非防真實失敗**。

**洞察 B — 對抗審查者必須能推翻提案者（含自己）**。若 validity 檢查只會確認 gap，等於沒檢查。F11 被推翻正是「proposer-separated 對抗審查」有實效的證明——預設懷疑 + 找反證（MEMORY:96）才擋下一個 plausible-but-academic 的 gap。

---

## 4. 委派紀律的實戰應驗

- **fan-out≤4 + model 配任務altitude**：Opus/ceiling 配架構映射 + 對抗審查（判斷重）；Sonnet/quality 配量化抽取（數字重）。3-way validity fan-out 各負責 ~4 gap，flat 非 nested。
- **verdict 非證據，主對話親 grep 重驗**：每輪 sub-agent 回 verdict 後，主對話親跑確定性 grep（exit code）才升 verified。F5 排除 false-positive 子字串命中、F10 抓出「Mechanistic→mechan」假命中——都是主對話重驗才發現，sub-agent verdict 不可直接採信。
- **worktree 隔離產物不在主 tree（Lesson 2026-06-14-A 再應驗）**：`multi-mode-agent` frontmatter 含 `isolation: worktree`，fetch 論文落 worktree 副本；委派寫檔後必 grep 主 tree → cp 取回 + worktree remove。researcher agent 無此設定故落主 tree——**同任務不同 agent type 的落地行為不同，必逐一驗**。

---

## 5. APPLY-gate 紀律守住（純研究零 .claude/ 編輯）

全程**研究交付物，提案未套用**：
- harness 檔變更是高風險 → 走 `/autoload-evolution` gated loop（≤1 規則/cycle、≤50 行 diff、eval 回歸 ≥5pp→revert）+ 使用者核准，**非研究迴圈自主 apply**。
- auto-load 18,243B 全程未動；healthcheck PASS 123/0 不變（雙重確認純研究）。
- 3 個 HIGH_VALUE 全小/零 byte（F9≈0、F7=healthcheck 腳本非 auto-load、F3 RECORD ~1 行），且 APPLY 決策明確標為**使用者的**，不靜默執行。

**洞察 C — 研究迴圈的正確終點是「gated 決策點」而非「自主 apply」**。Loop-2 結束於「3 HIGH_VALUE 待你核准走 autoload-evolution」，而非偷偷改檔。把高風險 APPLY 留給使用者，是 The Loop「破壞性 APPLY 前 gate」的正解。

---

## 可複用結論（提煉）

1. **動態 /loop 語料耗盡 → 換鏡頭**（breadth→validity→apply-decision），非重複同動作空轉。
2. **gap 提案前必過有效性檢查**：對照真實失敗 corpus（MEMORY/commit/revert 史），找不到錨點就 defer——`grep 沒寫` 不等於 `該掛載`。
3. **對抗審查者要能推翻自己**：reverse-advisor + 找反證（如 MEMORY:96）才擋得下 plausible-but-academic gap。
4. **sub-agent verdict 必主對話親 grep 重驗**：含排除 false-positive 子字串命中。
5. **高風險 APPLY 留 gated 決策點給使用者**，研究迴圈不自主改 live harness 檔。
