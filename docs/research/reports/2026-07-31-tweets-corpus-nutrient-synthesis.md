---
title: "Tweets 語料養分合成報告——從「躺在那邊的文章」到可重複利用的 skill/rule 養分"
date: 2026-07-31
method: Graph Engineering（fan-out 深讀＋比對）+ Loop Engineering（verifier 分離＋終止條件）
scope: "research/tweets/*.md（389 篇語料中，24 篇經 INDEX.md 既有評分篩出 ≥8.2/10 高分樣本）"
type: synthesis
---

# Tweets 語料養分合成報告

> **起心動念**（使用者原話）：「那些文章要怎麼變成 AI 可以再次利用的養分，而不是躺在那邊的文章而已。」本報告是這個問題的第一次正式回答——不只是「再寫一份摘要報告」，而是把整個「讀→分類→補丁→建管線」的過程本身，變成一個可重複執行的 SKILL（`gap-harvest`，見文末），讓下一批文章不需要再手動走一次這個流程。

---

## 0. 為什麼不是重新讀 389 篇

第一步盤點就發現：`research/tweets/INDEX.md` 本身已經是一個成熟的養分管線產出——389 篇推文已有 A-E 五維評分（`/10`）、Author/Topic 雙索引、以及一個「整合決策分類」表（依 Rule/Agent/SKILL/Others 四種落地類型分組並排序）。這代表過去的 session 已經做完「掃描＋評分＋粗分類」這一層工作。

重新用 fan-out agent 讀全部 389 篇，等於無視既有勞動、重複花費——違反這個 workspace 自己的 Graph Engineering 紀律（G0：「說不出口就別派」）。正確的做法是把 INDEX.md 的既有評分當作**第一層 scan 節點的產出**，只對其中「評分達標但尚未真正落地」的子集做**第二層**：深讀全文＋機械比對現有規則檔（grep 驗證，非印象判斷）＋分類＋落地。

**取樣**：從「整合決策分類」表的 Rule/Agent/SKILL/Others 四類中，篩出評分 ≥8.2/10 且主題非純促銷/純行情的 24 篇，分 4 批（每批 6 篇）平行派給 `researcher` agent 深讀。這是本次任務的實際 Graph：4 個 quality 檔位 scan/transform 節點平行讀取（各自唯讀對應檔案 + grep 比對 `.claude/rules|refs|skills`），結果彙整回主對話（ceiling 檔位）做 synthesize/judge——不多開一層額外的合成 agent，因為主對話本身就在 ceiling 檔位，符合 G0「產出值不值 brief 成本」判準。

---

## 1. 分類結果總覽（24 篇）

| 分類 | 篇數 | 說明 |
|------|------|------|
| `reinforces-existing` | 11 | 核心主張已被現行規則吸收（部分甚至逐字對應），只構成外部驗證佐證 |
| `discard` | 3 | 領域不符（商業策略類）或純趨勢報告，無可操作技術框架 |
| `refs-patch-candidate` | 10 | 有具體、非重複、可佐證的新內容 |
| `new-skill-signal` | 0 | **本批 24 篇沒有任何一篇單獨構成「需要一個全新 SKILL」的訊號** |

**`new-skill-signal` 掛零本身就是一個重要發現**——不是說「這批語料沒有新 skill 的養分」，而是說：新 SKILL 的需求不是來自任何單一篇文章的內容，而是來自**這整個任務執行過程本身暴露的結構性缺口**（見第 4 節）。這與「多篇獨立來源三角收斂到同一個結論才算真訊號」的處理方式一致——本次真正有意義的模式，是好幾個獨立現象疊加起來才看得出來的。

---

## 2. 兩個獨立方法論發現（比任何單篇技術內容都重要）

### 2.1 評分高不等於養分新——選擇偏誤

Batch 1 與 Batch 2 兩個**互不知道對方存在**的 agent，各自獨立觀察到同一件事並寫進總結：

> 「這批高分推文與 workspace 現有規則的重疊度異常高……暗示評分系統的高分可能部分反映『與 workspace 哲學高度共鳴』而非『帶來全新養分』。」（Batch 1）
> 「本批 6 篇高分推文的技術養分絕大多數已被 workspace 吸收甚至逐字引用，反映評分系統的『高分』與『規則新穎度』是兩個獨立軸：高分反映文章本身品質，不代表對本 workspace 而言是未消化養分。」（Batch 2）

兩個獨立 agent 收斂到同一個判斷，本身構成一種三角驗證。這對「怎麼挑下一批要讀的文章」有直接操作意義：**評分（A-E 五維）衡量文章本身品質，不是衡量「對本 workspace 的邊際資訊量」**。下一輪 gap-harvest 執行時，篩選候選不能只看分數，還要看「是否已被現行 refs/rules grep 命中」——這正是本次 24 篇任務的做法，也是新 SKILL `gap-harvest` 把它固定為流程步驟的原因。

### 2.2 一條規則庫自身的死連結

Batch 1 的 agent 在核對 `nfcampos` 那篇（LDD 實戰案例，評分 9.60，全樣本最高分）時發現：`.claude/refs/loop-engineering.md` §L4 有一句「看到失敗報表的聚合數字就派工是最貴的錯誤（案例 → `error-handling.md`）」，但 `error-handling.md` 全文根本沒有這個案例——是一條指向空氣的死連結。這不是這次任務的產出瑕疵，是既有規則庫裡已經存在、直到這次才被人發現的 bug。已在第 3 節的補丁清單中一併修復（順手把 nfcampos 的真實案例內容填進 `error-handling.md`，讓斷鏈變成有內容的連結）。

---

## 3. 已落地的補丁（9 篇 → 5 個檔案，本 session 已 commit）

| 推文 | 落地位置 | 內容 |
|------|---------|------|
| `2026-06-12-@nfcampos-517180.md`（9.60） | `refs/error-handling.md` | xlsx-corpus-bench 案例：281,941 個「mismatch」中 96%（270,337 筆）是 oracle-系統 locale 差異的測量誤差，非真 bug；補齊上述死連結 |
| `2026-07-19-@TaoMachina-226249.md`（8.25） | `refs/graph-engineering.md` §G4 | 高風險 handoff 前，要求 child 覆述對 Goal 的理解，parent 核對無誤才放行（IDENTIFY「多解釋列選項」原則在委派場景的操作化）|
| `2026-07-03-@addyosmani-042327.md`（8.3） | `refs/graph-engineering.md` §G4 + `refs/judgment-rubrics.md` §R7 | Handoff Contract 補 Budget/Tools&Permissions 兩欄；高自主三問（多快知錯/多乾淨撤銷/什麼證明你對）+ 4 個委派反模式命名（Autonomy as Status／Permission Laundering／Summary Substitution／Fleet Cosplay）|
| `2026-06-15-@addyosmani-594363.md`（8.3） | `refs/judgment-rubrics.md` §R5c | Review 深度三變數：blast radius／存活時間／理解人數——三者皆低才用最低驗證，任一高就升驗證深度而非加輪次 |
| `2026-06-11-@PawelHuryn-549362.md`（8.30） | `refs/model-profiles.md` §1 | 巢狀 sub-agent 相對扁平委派有 1.63–1.84× 乘法開銷；決策規則：只在下層計畫依賴上層發現時才巢狀（信心：中，部分細節在付費牆後）|
| `2026-06-09-@RLanceMartin-071163.md`（8.30）+ `2026-06-13-@servasyy_ai-597508.md`（7.8） | `refs/harness-loop.md` RECORD 段 | 記憶品質 5 階段診斷：fail→investigate→verify→distill→consult；兩個獨立來源用近乎相同措辭描述同一分型，三角驗證強度較高 |
| `2026-06-09-@mem0ai-233179.md`（7.20） | `refs/harness-loop.md` RECORD 段 | JIT 引用重驗：記憶條目引用 `file:line` 時，使用前先重讀該位置確認未過期，矛盾則顯式修正而非讓 staleness 變成 silent failure |
| `2026-07-02-@cyrilXBT-058492.md`（8.7） | `refs/judgment-rubrics.md` §R3 | assessment-mode vs action-mode 邊界：使用者描述問題/自言自語時只回評估，不擅自動手（此篇其餘內容——audit 語句模板、ultrathink/ultracode、HTTP 200 refusal 處理——已在更早的批次逐字吸收進 `quality-pipeline`/`model-profiles.md`/`error-handling.md`，本次只補這一個殘餘缺口）|

全部套用 `refs-patch-candidate` 分級（見 gap-harvest SKILL 的 blast-radius 分級表）：只動 `.claude/refs/*.md`，不動 `rules/*.md` 自動載入層——後者屬 scope 變更，按 core.md 規則需要使用者確認，本次全部克制在 refs 層級。

---

## 4. 待辦（明確記錄，非靜默捨棄）

四項評為 `refs-patch-candidate` 但本輪**未套用**，原因各異：

| 推文 | 為何暫緩 |
|------|---------|
| `2026-06-11-@elvissun-864954.md`（Forced-Entropy 反 local-maxima 手法） | 內容本身可操作，但來源標記 `single_source_or_promotional=true`（自售產品/自評 50× 改善無第三方驗證），信心僅 med；建議下一輪若有第二個獨立來源佐證再落地 |
| `2026-07-02-@wquguru-253843.md`（overnight 摘要輸出風格：完整句子/拼出術語全稱/不用箭頭鏈） | 內容具體且 grep 確認未覆蓋，但重要性偏低（風格類非機制類），信心 med，列入下次批次的低優先項 |
| `2026-07-27-@hanakoxbt-513286.md`（compact 存活範圍 + skill body 截斷上限 5,000/25,000 tokens） | **這是本批最需要小心的一項**——數字本身來自社群轉述而非官方文件連結，agent 明確標注「落地前應先查證官方文件（code.claude.com/docs），不可直接轉抄推文文字為 `[E]` 硬規則」。本 session 未做 WebFetch 查證（時間/用量考量），留給下一輪 gap-harvest 或使用者直接查證後再落地 |
| `2026-06-15-@addyosmani-594363.md`（異質 AI reviewer 並行策略落地到 `review-hub`/`verified-merge`） | 三變數評分軸已落地進 `judgment-rubrics.md`，但「異質工具並行審查」本身是對 SKILL 主體行為的修改（非 refs 補丁），需要 `skill-evolution` 的改動前後 empirical gate（見其 SKILL.md Phase 1），超出本輪 refs-only 的範圍，建議下次呼叫 `skill-evolution:apply review-hub` |

另有 `research/tweets/INDEX.md` 各主題表格（Harness Engineering／CLAUDE.md-Rules／Memory 等）的逐列 🔵/📋 狀態，本輪未逐一改成 ✅——已在 INDEX.md 新增一個「2026-07-31 gap-harvest 執行紀錄」小節作為可查詢的替代索引，逐列同步留給下一輪批次處理（見該檔案）。

---

## 5. 新 SKILL：為什麼是 `gap-harvest`，不是別的

本次任務暴露的真正缺口，不是「某篇推文教了一個新技巧」，而是：**這個 workspace 已經有評分（research-hub:score）、有共識投票（gap-vote）、有 SKILL 品質改進（skill-evolution）、有內部記憶固化（dreaming-consolidator），但沒有任何一個 SKILL 把「已評分/已歸檔的外部語料」與「現行規則的實際覆蓋狀態」接起來，變成可落地的補丁或新能力候選。**

這正是本次任務從頭到尾手動做的事——讀 INDEX 既有評分 → fan-out 深讀 → grep 比對現行規則 → 分類 → 分級套用（refs 直接補／新 SKILL 走人閘／rules 層改動走人閘）→ 更新來源索引。把這個流程固定下來，避免每次都要重新設計一次 fan-out 批次與比對基準，就是 `gap-harvest`（詳見 `.claude/skills/gap-harvest/SKILL.md`）。

它不重複造輪子：
- 抓取/評分 → 交給既有的 `research-hub`/`media-research`（本次直接沿用 INDEX.md 既有評分，沒有重新評分）
- 「這個候選算不算真缺口」的最終共識 → 交給既有的 `gap-vote`（3 技能投票）
- SKILL 本體品質改進 → 交給既有的 `skill-evolution`（7 維 rubric + empirical gate）
- 內部記憶反覆 pattern 蒸餾 → 交給既有的 `dreaming-consolidator`

`gap-harvest` 只做前面沒人做的那一段：**已評分外部語料 → 與現行規則的實際覆蓋比對 → 分級分流**。

---

## 6. 方法論限制（誠實記錄）

- 24 篇是 389 篇中的高分子集，不是全量普查——分數本身的選擇偏誤（見 2.1）代表這個取樣策略事後看有改進空間：下一輪應該混一些「未評分」或「中低分但主題陌生」的樣本做對照，才能檢驗「高分=高吸收率」這個相關性是否只是取樣造成的假象。
- 每篇的 `already_covered_by` 判斷主要靠 Grep 關鍵詞比對，非逐字全文比對——多個 agent 在 knowledge_gaps 中都誠實標注這點，可能有更細緻的既有覆蓋因用詞不同而漏判。
- 帶引號/量化數字的來源（PawelHuryn 的 1.63–1.84×、hanakoxbt 的 5,000/25,000 tokens）多數是社群轉述非原始文件，套用時都保留了「信心等級」與「未經獨立重現」的標注，沒有被無條件轉寫成 `[E]` 硬規則。
