# Session Blindspot Review 二輪 — 規則已經在了，我又違反四次

> 對象：2026-07-26～27 的 v5 收尾 session（209 個 commit）。
> 框架：thariqs `html-effectiveness/unknowns` T1–T11 + Anthropic《The new rules of context engineering for Claude 5 generation models》。
> 與一輪（`2026-07-26-session-unknowns-review.md`）的關係：**一輪的結論在本輪被證明不夠**。

## 0. 一輪的結論、以及它為什麼不夠

一輪找到單一根因：「我採信了一個報告狀態的東西，卻沒有先驗那個東西本身」，並據此把 `core.md §TEST` 的 oracle 範圍由「先於 loop」擴為「先於採信」，條文明白寫著**「你自己剛寫的 grep」也是 oracle**。

**本輪我又違反四次。** 條文在、範圍對、措辭精確，就是不會開火。

| # | 壞 oracle | 錯在哪 | 後果 |
|---|---|---|---|
| 1 | `grep -E '^[+-][^+-]'` 審 diff | `+- **項目**` 第二字元是 `-`，被否定字元類排除；同時多抓刪除行 | 誤判 sub-agent 少做兩項編輯（實際做了）|
| 2 | brief 裡的 Done-when 用 Python `len(s)` | canonical 是 `wc -c`（bytes），CJK 3 bytes/字 | child 回報數字看似縮水 30%，實為微幅增長 |
| 3 | 裸檔名 regex 掃 hook 引用 | 撈到外部文章引用、通用範例、截斷字串 | 誤報 32 個「死引用」，實際 0 |
| 4 | 用**命中數**比較兩個 grep pattern | 兩者都回 3，但是**不同的三條** | 差點放行 #1；當場現形 |

**#4 發生在我正在寫這份 review 的過程中**——我用計數驗證 #1 的修法，計數相同就差點收工。這不是修辭，是同一輪內的實時重現。

## 1. 為什麼加規則沒用（本輪最重要的判斷）

Blog 第 1、2 條：移除過度約束的指令，新世代模型判斷力足夠；Anthropic 砍掉 Claude Code system prompt 的 80% 而無性能損失。

對照本輪：**規則不是不夠精確，是精確到指名了「你剛寫的 grep」仍然無效。** 再寫第五條「記得驗證你的 grep」只會讓常駐層更長、服從率更低。

一輪的收尾句已經寫過：「缺的是在該檢查的時點會自己開火的東西」。本輪把它推進一步：

> **臨時驗證指令不會有 hook 幫你開火**（它不是工具呼叫、不是檔案寫入，就是一行 bash）。所以唯一有效的介入是**讓正確做法比錯誤做法更好用**——把易錯的 idiom 換成一支正確的工具，而不是要求自己每次都想起來。

這是 `loop.md §L3`「結構防線 > prompt 禁令」套用在**自己的驗證習慣**上。

## 2. 逐技巧回審

### T1 Blindspot Pass — 仍是最大缺席，但缺席位置變了

一輪缺在「改 hook 前沒掃執行路徑」。本輪缺在**更小的尺度**：每次手寫一行驗證 grep 之前，沒有問「這個 pattern 會漏掉哪種輸入」。四次失效全部出在這個尺度。

尺度小到不值得跑正式 Blindspot Pass——這正是為何處置是工具化而非流程化。

### T7 Point at a Reference — 這次錯在「指向了重寫版而非原件」

一輪錯在指標會漂移（`git show HEAD~1`）。本輪錯在 **Done-when 重新實作了一個已有 canonical 命令的量測**。T7 的字面意思是指向 reference，我卻自己抄了一份——抄的那份單位不同。

已修：`task-templates.md` 的 `Done-when` 欄位加註「已有 canonical 命令的量測，逐字照抄，不得改寫或重實作」。

### T9 Implementation Notes — 本輪做對了

四次失效**全部在同一輪內被自己抓到並當場更正**（誤判 sub-agent 後立刻重驗、單位不符後同命令重測、32 個死引用後改問法重掃、計數比較後改比內容）。一輪的三次是「使用者指出後才反轉」。

差別在於本輪每次宣告前都實際跑了命令看輸出，而不是憑印象斷言。

### T11 Quiz Me Before I Merge — 機械版持續有效

每個 commit 前跑 healthcheck / check-references，本輪攔到一次真實漏登（`scripts/INDEX.md` 未登錄新腳本 → FAIL 1）。這是 gate 真的在工作的證據，不是裝飾。

### T3 Four Design Directions — 本輪主動用了一次

byte 門檻上調時列出兩條路（提高數字 vs 重新定義量測對象），並在記錄中說明使用者選了前者。一輪的失效正是「靜默錨定第一個可行解」。

### T2 / T4 / T5 / T6 / T8 / T10 — 不適用

需求由使用者逐輪明確給出，無需求轉譯／原型／方案空間探索／買單文件的施力點。**列出來是為了說明「沒用」是判斷結果而非遺漏。**

## 3. 本輪落地的處置

| 修 | 防的失效 | 型態 | 收據 |
|---|---|---|---|
| `scripts/diff-added.sh` | #1 #4（審 diff 用錯 pattern、用計數當 oracle）| **工具取代 idiom** | `--self-test` 比對內容；並驗舊壞 pattern 產出不同結果（證明測試有區辨力）；真實 diff 上重現 1 vs 3 行的差距 |
| `task-templates.md` `Done-when` 欄 | #2（重實作 canonical 量測導致單位漂移）| 條文加註（帶實例）| — |
| `score-evalpack-v5.sh` 的 `rejects()`/`asserted()` | 合成樣本系統性比真實回應容易 | 護欄 + 第三層語料 | `--qualify` 12/12 含真實 rp/rf |

**刻意不做的**：不新增「驗證你的 grep」類條文。理由見 §1。

## 4. 全域 CLAUDE.md 的狀態（查證結果：branch lag，非 drift）

`/root/.claude/CLAUDE.md` 只有一行 `@/tmp/cc-workspace/CLAUDE.md`；後者是 `main` 的淺 clone（`9b0c15d`）。該版本仍是 v4：auto-load 清單含已刪的 `subagent-strategy.md`、缺 v5 新增的 `loop.md`／`graph.md`、指標指向已封存的 `the-loop-harness-v4/`。

**但這不是獨立的漂移**——`CLAUDE.md` 是同一個 git-tracked 檔，本分支已含 v5 版本。**merge 後全域自動同步，無須另修。**

⚠️ **未 merge 前的實際風險**：新開的 session 會拿到 v4 全域路由（指示 auto-load 一個不存在的檔、且少載兩個承載 v5 一半教義的檔）。這不影響本 session（專案層 `CLAUDE.md` 同時載入且為 v5），但**v5 沒進 main 就等於沒生效**。

## 5. Blog 對照：本 workspace 已對齊與未對齊的

| Blog 條 | 本 workspace 狀態 |
|---|---|
| 1/2 移除過度約束、讓判斷生效 | **已對齊**：`output-discipline.md` 的硬性禁令已改判斷式；v5 教義總量較 v4 砍半 |
| 4 Progressive disclosure | **已對齊**：三層下沉（閘門→auto-load／細則→refs／流程→skills）為既有紀律 |
| 5 消除重複指令 | **本輪修過一次**：`CLAUDE.md` 五條 auto-load 描述刪除（五檔全載，描述對已載入檔零作用）|
| 6 自動記憶優於手抄 CLAUDE.md | **已有條文**：`core.md §RECORD`「平台 auto-memory 免除手抄義務，不免除入庫過門義務」|
| 7 Rich references 優於散文 spec | **已對齊**：`core.md §IDENTIFY`「References > 散文 spec」 |
| `/doctor` 自動 rightsize skills/CLAUDE.md | **未用過**——可作為 skill roster 常駐稅治理的外部對照，列為候選 |

## 6. 給下一輪的一句話

一輪說「規則已經夠了，缺的是會自己開火的東西」。本輪的補充是：**有些失效小到不會有東西幫你開火**——一行臨時 grep 不觸發任何 hook。對這一類，唯一的介入點是把正確做法做成預設路徑，而不是再寫一條要求自己記得的規則。
