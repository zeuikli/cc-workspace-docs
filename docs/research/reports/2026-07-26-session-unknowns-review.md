# Session Blindspot Review — 用 T1–T11 回審 v5 重寫

> 對象：2026-07-26 的 The Loop Harness v5 重寫 session（約 40 個 commit）。
> 框架：thariqs `html-effectiveness/unknowns`（T1–T11）+ Anthropic《The new rules of context engineering for Claude 5 generation models》。
> 立場：**證偽式**——找我做錯了什麼，不找我做對了什麼。

## 0. 一個必須先問的問題：v5 是否走反了方向？

Blog 第 1 條：移除過度約束的指令，Anthropic 砍掉 Claude Code system prompt 的 80% 而無性能損失。
v5 卻**新增**了 `loop.md` + `graph.md` 兩個常駐檔。表面上正好相反。

量測後才發現我先前盯錯指標：

| | auto-load | 全文層 | **教義總表面** |
|---|---|---|---|
| v4 | 18,931 | `HARNESS-CORE-v4.md` 25,732 | **44,663** |
| v5 | 22,785 | 無（單一 canonical 裁決） | **22,785** |

v5 的 auto-load 漲了約 3,900，但**教義總量砍半**——消滅了 25,732 bytes 的重複全文層。方向與 blog 一致。

**但我先前整輪都在盯 auto-load 那個數字**，甚至為它做了門檻上調的程序瑕疵辯護（見 `model-profiles.md` §2.1 的 PROVISIONAL 聲明）。這本身就是 `core.md §TEST`「Gate 選擇稽核：非 proxy 子集」的實例——我用一個子集指標代表了整體。

**後續已結案**：`graph.md` 的閘門語密度只有 **13%**（`core.md` 35%、`loop.md` 47%），意即它大半是判斷指引而非閘門。依 blog 第 1 條與 `core.md`「程序性指導與能力成反比」，**graph.md 是 v5 中最該再剪的一檔**。已於 `7af6e2b` 剪枝——同一輪順帶吸收了外部 Graph Engineering 視角的兩條新條文，仍達成淨剪：剪掉的是已由 `refs/delegation-protocol.md` 擁有的效益清單、三處重複表述的 verify 檔位選擇、以及屬歷史敘述的吸收說明，`[E]`/`[E*]` 一字未動。

---

## 1. 逐技巧回審

### T1 Blindspot Pass — 本 session 最大的缺席

**沒做的事**：改 4 支 hook 的輸出通道前，沒有掃過「這些 hook 到底在哪個執行路徑上開火」。

**代價**：F19 對應的 `taste-reference-lint.sh` 只接在 `PreToolUse(Agent|Workflow)`，而 F19 的 fixture 是**直接使用者請求**——hook 根本不在該路徑上。我卻把那個 commit 標題寫成「處理 F19 紅軸」。**換通道不可能移動一條 Body 不在路徑上的軸。**

更難堪的是：v4 backlog 早就寫著「TASTE_RE 補模糊詞（待執行）」，而 F19 fixture 的原句「專業一點」正是 TASTE_RE 沒有的詞。**線索在檔案裡躺著，我沒去 Blindspot Pass 就先動手。**

已修（覆蓋擴大、非放寬）：接上 `UserPromptSubmit`、payload 兩種形狀都吃、補模糊品味詞、`hookEventName` 改動態。

### T7 Point at a Reference — 我餵了一個會漂移的「reference」

**做錯的事**：給 Fable 5 做 `[E]` 對等性審查時，v4 對照組用 `git show HEAD~1` 抽取。

**為什麼錯**：auto-sync commit 在期間落地，`HEAD~1` 已經漂移到 v5 重寫 commit 本身。結果索引的「v4 節」與「v5 節」內容相同，`subagent-strategy.md` 那節全空（該 rev 檔已刪）。

**若 verifier 採信該索引**，會得出「`[E]` 一字未動、`subagent-strategy` 無 `[E]` 可失」的**完美假陰性**，再疊上我 commit message 的自報收據，形成三層自證閉環。

**沒出事的原因不是我**：Fable 未採信該索引，自行回具名 rev 取真本。這是 `graph.md §G5`「verdict 非證據，採信前機械重驗」在對方身上生效，不是在我身上。

**正解**：reference 必須是**不會漂移的具名 SHA**，不是相對 ref。這正是 T7「Point at a Reference」的字面意思——我提供了一個指標，但那個指標會動。

### T9 Implementation Notes — 三次「先做後發現」

三個本可用 T9 攔下的偏離，我都是做完才發現：

| 偏離 | 發現時點 | 若有 T9 |
|---|---|---|
| fixtures 遷入 v5 並改名 `EVAL-PACK-v5-*` | 使用者指出後才反轉 | 寫下「為何改名」時就會問「它量測的是哪版契約」 |
| `EVAL-BASELINE-v5` 命名 | 使用者詢問時才查出內文寫著 v4 | 同上 |
| `PORTABLE-PROMPT-KIT` 遷入 | 使用者指出後才刪 | 同上 |

**三次同一個簽名**：舊世代內容穿 v5 檔名。`core.md §RECORD` 說「同簽名重現 ≥2 次才改規則」——這裡是 3 次（連同 `HARNESS-CARD`、`.factory`、`evals/INDEX` 共 **6 次**），早已越過門檻。

### T3 Four Design Directions — 靜默錨定了第一個可行解

fixtures 該遷入 v5 還是留在封存，我**沒有列成選項**，直接選了「遷入」並給了一個聽起來合理的理由（「fixtures 是量測工具不隨契約過期」）。

該理由站不住：這些 fixture 的 `deterministic_check` 是**對 v3/v4 條文撰寫並凍結**的。若當初列出兩個方向，「它們綁定哪一版條文」這個問題會在選之前浮出來。

`core.md §PROPOSE` 本來就寫著「scope 有量級選擇時列 ≥2 級由使用者選，不靜默錨定第一個可行解」——**我違反了自己剛寫進去的條文**。

### T6 The Interview — 做對的一次

「四個相關的 playbook」是我自己上一則訊息裡講得不精確的詞。我沒有猜，用 `AskUserQuestion` 列出四個選項讓使用者選，並標明推薦與理由。刪錯 playbook 是不可逆的，這裡問對了。

### T11 Quiz Me Before I Merge — 結構上做到，形式上沒有

每個 commit 前跑 `healthcheck` / `check-references` / `check-anchors` 並展示輸出，實質是機械版的 T11。但**沒有一次是針對「我是否真的理解這個改動的下游影響」**——`generator-ref-check` 要防的四次失效，正是「改動的下游影響沒被檢查」。

已機械化：新增 `generator-ref-check.sh`（PreToolUse Bash），刪除／搬移路徑前自動列出硬編碼引用它的腳本。

### T2 / T4 / T5 / T8 / T10 — 本 session 不適用

分別是需求詞彙轉譯、可點擊原型、干預時間軸、可調計畫、買單文件。本 session 是既有系統的重構，需求由使用者逐輪明確給出，這五項無施力點。**列出來是為了說明「沒用」是判斷結果而非遺漏。**

---

## 2. 跨技巧的單一根因

上述 T1 / T7 / T9 的失效，加上本 session 其餘幾次，可歸為**同一類**：

> **我採信了一個報告狀態的東西，卻沒有先驗那個東西本身。**

| # | 被採信的 oracle | 它錯在哪 | 後果 |
|---|---|---|---|
| 1 | `git show HEAD~1` | auto-sync 使其漂移 | 餵給 verifier 的對照組是 v5 自己 |
| 2 | 我自寫的章節級掃描器 | regex 只抓第一個詞，`§The Loop` 被截成 `§The` | 回報 135 筆懸空，絕大多數是誤判 |
| 3 | `f11` fixture 的 `deterministic_check` | known-good 與 known-bad 皆 PASS | 零區辨力，分數不可採信 |
| 4 | 我自算的 `EXPECTED_SETTINGS` | 我數 hook 命令數，healthcheck 數 matcher 群組數 | 寫入 32 導致 FAIL |
| 5 | `check-references` 的 `dangling=0` | 只驗檔案級，章節級未涵蓋 | 拿 proxy 子集當完整覆蓋 |
| 6 | auto-load byte 數 | 只是教義總表面的一半 | 為子集指標做了門檻上調辯護 |

六次中只有 #3、#5 發生在 loop 內。而 `loop.md §L4` 的 oracle 資格條文，**範圍寫的是「建 loop 前」**——另外四次因此不在其涵蓋內。

**這是條文的 scope bug，不是執行者的疏忽。**

### 已修

`core.md §TEST` 的條文由

> Oracle 資格**先於 loop**：壞 oracle 比沒有更糟

改為

> Oracle 資格**先於採信**：**任何用來判定真偽的東西都是 oracle**——test、checker script、索引、baseline、`git` ref、你自己剛寫的 grep。採信其輸出前先驗它能區辨已知好／已知壞。

+199 bytes，常駐 22,785（門檻 23,000 內）。這是**閘門加嚴**，符合「驗證閘門與能力成正比」。

---

## 3. 本輪落地的兩個機械化

| 修 | 防的失效 | 型態 | 收據 |
|---|---|---|---|
| `core.md §TEST` oracle 範圍擴大 | 上表六次中的四次（loop 外的 oracle） | 條文加嚴 | byte 量測在門檻內 |
| `generator-ref-check.sh`（PreToolUse Bash） | 生成器復活死節點（session 內 4 次） | 可見提醒、不阻斷 | 正例列出 4 支硬編碼腳本；三個反例（repo 外路徑／非刪除指令／無引用檔）全靜默 |

`generator-ref-check` 刻意不阻斷：硬編碼引用不等於不能刪，多數情況是「刪之前先改腳本」。阻斷會擋住正當操作；正確強度是**在該知道的時點把清單攤開**。

---

## 4. 明確不修的

| 項 | 為何不修 |
|---|---|
| `pre-commit-review` 三個誤傷 | 屬閘門變更，`core.md §APPLY` 要求先過異 context 對抗複審 |
| `.factory` port 過期 | 已止血（過期警語），修復需使用者裁決 generated-vs-雙軌 |
| v5 fixtures 與 baseline | 需獨立撰寫（backlog #9/#5），非本 review 範圍 |

---

## 5. 給下一個 session 的一句話

這個 session 的所有主要失誤，都不是「不知道規則」——**六條規則我全都寫在 `core.md` 裡，然後逐條違反**（Gate 選擇稽核、oracle 資格、列 ≥2 級選項、數字對帳、verdict 非證據、避免與 agent 動同一批檔）。

規則已經夠了。**缺的是在該檢查的時點會自己開火的東西**——所以本輪的產出是兩個機械化，不是六條新規則。
