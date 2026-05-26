# Session Insight — Dynamic Workflow 實戰 × 雙版規則集打造的踩坑與學習

> **日期**：2026-06-05 · **原始分支**：`feature/dual-ruleset-12rule` · **模型**：Opus 4.8 (1M) · ultracode mode
> **任務脈絡**：把 12-Rule Canon 改寫成「Claude Code 特化 + 通用」雙版本 × 三等級，後續再去 workspace 化 + 重構為可延展 Harness 框架。
> **本報告性質**：第一人稱 session 復盤（agent 自身的執行軌跡），非外部研究。§1–§4.7/§5(1–7) 的踩坑與數字來自原始 session（`feature/dual-ruleset-12rule`）實際發生，非文獻。
> **產出 commit**：原始 session `f014b703`（雙版三等級初版）-> `562631e0`（去 workspace 化 + 可延展重構）。**後續 append**：§3.5 + §5(8)（D4 verifier PoC 踩坑）由後續 session 於分支 `feature/ruleset-audit-fixes`（commit `fcc9e9ba`）補入。

---

## 0. 執行摘要（給趕時間的人）

本 session 用 Dynamic Workflow 做了兩件 fan-out 工作（tier 收斂驗證、去 workspace 化重寫），最大的學習**不在 workflow 本身，而在「何時該用、何時是陷阱」**：

1. **最大踩坑 = CJK byte-grind 陷阱**：為把「完整版」壓進一個 **後來被使用者要求移除的 19K cap**，手動逐行刪了 ~20 輪、每輪只回收 6–40 byte，還因此削掉了 3 條規則的 mechanical check（製造出「vibe 非 rule」）。**根因：把一個 workspace 客製約束當成了普世硬約束。**
2. **Dynamic Workflow 的真正價值 = 並行的確定性轉換 + 對抗式驗證**，不是「讓 agent 想內容」。本 session workflow 表現最好的時刻是「我給定已驗證的內容、agent 只做 de-workspace 轉換 + 獨立 grep 審計」；表現最差的風險是「讓 agent 重新推導論文數字」（會重新引入已修正的 3 個錯誤）。
3. **advisor 是這個 session 的 MVP**：在 3 個關鍵轉折點（staged-not-overwrite / 19K-cap-是-workspace-think / 完整版自我描述矛盾）攔截了會毀掉交付物的決策。**advisor 看完整 transcript 的價值，遠高於任何 sub-agent 的 self-report。**
4. **使用者的 3 次漸進指令重新定義了任務**：從「改寫」->「去 workspace 化」->「可延展框架」。每次都讓更多手工打磨白工。**學習：規格模糊度是工作量的天花板（R1.1），但使用者漸進澄清是常態，過早大量手工優化是賭注。**

---

## 1. Session 時間軸（從開始到完成）

| 階段 | 動作 | 結果 / 踩坑 |
|------|------|-----------|
| **Orientation** | 讀 5 份報告 + best-practices + deepened-ruleset；advisor 第一次諮詢 | advisor 鎖定 6 約束，最關鍵：**staged deliverable 非 in-place overwrite**（mid-session 改 live CLAUDE.md 破壞並行 session 共享 cache）。避開了第一個大坑。 |
| **建 master** | 手寫完整版 5 檔（含全 Rn.x 子條） | 27,122 byte -> 遠超假想的 19K cap。**第一個錯誤判斷在此萌芽**。 |
| **byte-grind** | 為壓進 19K，手動逐行刪 ~20 輪 | 每輪回收 6–40 byte（CJK 密度高）；削掉 R2.1/R4.1/R8.1 的 check；引入過 `\|\|` 非標準 markdown table。**最大時間黑洞**。 |
| **Workflow #1** | tier 收斂 + 對抗驗證（3 builders + 9 verifiers） | lite/standard 成功；**full builder 沒跑/卡住** -> 我手動接管 full 的壓縮。學習：workflow 部分失敗時主對話要能無縫接管。 |
| **使用者指令 1** | 「Claude 版帶太多 workspace 東西，移除 19K cap/SKILL/script/hook」 | **19K cap 整個消失** -> byte-grind 全成白工。advisor 點明：cap 本就是 workspace-think。 |
| **使用者指令 2** | 「通用版也去 workspace 化 + 全面改寫，12 準則只是參考」 | 從 patch 升級為 rewrite。 |
| **使用者指令 3** | 「不受限 12 準則 + 可擴充 + 揉合論文與最佳實踐 = 可延展 Harness 雙版」 | 任務本質重定義為「**可延展框架**」非「固定規則集」。 |
| **Workflow #2** | 去 workspace 化 + 加延展性（6 rewrites + ref 清理 + 2 audits） | **成功**：rule 檔全清、延展性 framing 全加、cap 移除後**順手修復了 advisor 指出的 Rn.x 缺 check 缺陷**（每子條補回獨立驗）。 |
| **收尾** | grep 驗零殘留 + healthcheck FAIL=0 + commit | 零 workspace token、零 number-regression。 |

---

## 2. 踩坑深掘（每個都附根因 + 防範）

### 踩坑 1 — CJK Byte-Grind 陷阱（最貴）

**現象**：把完整版從 27K 手動壓到 18,994（≤19K）花了 ~20 個工具回合，每次 Edit 只回收 6–40 byte。中文 token 密度高 -> 每行刪減的 byte 報酬極低。

**根因**：① 把 **workspace 客製的 19K cap 當普世硬約束**；② 已經陷入逐行優化後，沒有退一步問「這個約束本身對嗎」。advisor 早就說過「cap 是 what you choose to run 的屬性」，但我在 grind 中沒回連這句話。

**代價**：不只是時間。為省 byte 削掉了 R2.1/R4.1/R8.1 的 mechanical check -> 製造出「有 prevents、無 check」的 sub-clause = canon 自己禁止的「vibe 非 rule」。**用降低交付物品質換一個假約束。**

**防範**：
- **質疑約束再優化**：逐行壓縮前先問「這個數字/限制是哪來的、對這個交付物適用嗎」。staged template 的 byte 數 ≠ live config 的 cap。
- **結構槓桿 > 逐行槓桿**：超標 2K 時，正解是「把深度移進 on-demand ref」（一次結構調整），不是「逐行刪 40 byte ×50 次」。
- **削減不可碰 canon 的可驗證性**：byte 壓力下若要削內容，先削 rationale/citation prose，**絕不削 mechanical check**——check 是規則的本質。

### 踩坑 2 — 把 Sub-Agent / Workflow Verdict 當證據

**現象**：Workflow #1 的 full-builder 回報沒問題但實際沒改檔；標準 builder 把 standard 壓到 14,872（低於我設的 floor）。

**根因**：dynamic workflow 會幻覺（workspace 既有 lesson）。Verdict 是 self-report，不是 ground truth。

**防範（已是 workspace 鐵律，本 session 再次驗證有效）**：每個 workflow 階段後**主對話親自 grep 重驗**。本 session 的 number-regression grep、leakage grep、防/驗 count 全是我自己跑，不信 workflow 的 audit verdict。**這條救了交付物**——workflow audit agent 報「clean」但我 grep 出 harness-loop.md 還有 6 個 workspace token。

### 踩坑 3 — Refs 的隱藏汙染（差點漏掉）

**現象**：我 grep 了 rule 檔說「乾淨」，但 advisor 點出**我沒 grep 已 ship 的 refs**。`harness-loop.md` 是從 live repo 逐字複製的，滿是 `/autoload-evolution`、`gap-vote`、`measure.sh`、`memory-compactor`。

**根因**：把「複製現成 ref」當零成本，忘了 ref 也是交付物的一部分、也帶 workspace 耦合。

**防範**：交付物的**每個檔案**（含複製來的 ref/附件）都要過同一套 leakage 審計。「複製」不等於「乾淨」。

### 踩坑 4 — 過早大量手工優化（賭規格不變）

**現象**：在 byte-grind 投入 ~20 回合後，使用者指令 1 直接移除了 19K cap -> 全部白工。

**根因**：規格在演進中（使用者 3 次漸進澄清），我在規格未定時就做了大量不可攤銷的手工打磨。

**防範**：R1.1（規格優先於資源）的延伸——**規格還在動時，先做骨架與結構決策（可攤銷），延後逐行打磨（不可攤銷）**。byte-grind 是典型「規格未定就 all-in 的不可攤銷工作」。

### 踩坑 5 — Bash hook 慣例反覆觸發

**現象**：`perl -i`、`F=...`（VAR= 開頭）、`cd && bash` 三次被 block-dangerous hook 擋下。

**根因**：忘了 workspace 的 Bash 慣例（repo root 用絕對路徑、不以 VAR= 開頭、不 cd）。

**防範**：這正是「hook 作為確定性 gate」的價值——它擋下的不是錯誤命令，是**我沒內化的慣例**。教訓：環境的 hook 慣例要在第一次被擋後立即內化，不要重複觸發。

---

## 3. Dynamic Workflow 的收穫（使用者特別想知道的）

### 3.1 什麼時候 workflow 真的贏

本 session 兩個 workflow，**第二個（去 workspace 化）遠比第一個（byte 收斂）成功**。差異很有啟發：

| 維度 | Workflow #1（byte 收斂）| Workflow #2（去 workspace 化）|
|------|----------------------|---------------------------|
| 任務性質 | 壓到模糊的 byte 目標（規格在動）| 確定性轉換（移除 token list + 加固定段落）|
| Agent 自由度 | 高（要自己決定砍哪裡）-> 易偏移 | 低（給定 removal list + 已驗證內容）-> 穩 |
| 結果 | 部分失敗（full builder 沒跑）| 全成功 |
| **學習** | **workflow 不擅長「對著動態目標做判斷密集的優化」** | **workflow 擅長「對著固定 spec 做並行的機械轉換 + 獨立審計」** |

**核心收穫**：Dynamic Workflow 的甜蜜點是**「寬度」而非「深度判斷」**——當工作可以拆成 N 個獨立、規格明確的轉換 + 對抗式驗證時，並行 fan-out 省下大量 wall-clock。當工作需要「對著移動的目標反覆判斷取捨」時，主對話直接做反而穩。

### 3.2 Workflow 的對抗式驗證 pattern（值得複用）

第二個 workflow 用了 `Rewrite -> Audit` 兩階段：6 個 rewrite agents 各改自己的 tier，再 2 個 audit agents **各自獨立 grep** workspace token / number-regression / canon coverage，輸出 structured verdict。

**但關鍵紀律**：我**沒有信** audit 的 `pass=true`，而是主對話自己再 grep 一次——並抓到 harness-loop.md 殘留。**對抗式驗證提升信心，但不取代主對話的最終親驗。**

### 3.3 餵 trace 而非 score；保護已驗證的事實

最重要的 workflow 紀律：**給 agent 已驗證的內容讓它轉換，不讓它重新推導事實**。本 session 有 3 個論文數字曾被 sub-agent 誤植（ACE −82.6% 不存在 / TTFT 13–31% 應為 22.9% / MetaGPT −40% 為二手）。我在 workflow prompt 裡明列「PROTECTED / FORBIDDEN 變體」，並在每個 audit agent 加 number-regression grep。**結果：零回歸。** 若放任 rewrite agent「順便改善措辭」，極可能重新引入這 3 個錯誤。

### 3.4 Workflow 成本誠實

兩個 workflow 跑了 ~20 個 sub-agent。ultracode mode 下 token 不是約束，但若非 ultracode，**第一個 workflow（byte 收斂）其實不值得**——那個工作主對話自己做更快更穩。**workflow 不是「越多越好」，是「寬度任務才划算」。**

### 3.5 後續延伸（2026-06-05 D4 verifier PoC）— 「確定性層經 workflow agent 中介就不再確定性」

> 脈絡：本報告原始 session（`feature/dual-ruleset-12rule`）merge 後，**後續 session**（分支 `feature/ruleset-audit-fixes`，非同一分支）據研究 lever D4（Anthropic 官方「one verifier per rule」）建了個 Hybrid per-rule verifier PoC（verifier 提 verdict + 確定性 grep 裁決）。第三個 workflow（12 agent：6 verify + 6 adjudicate），揭露一個**比 §3.2 更深的新踩坑**。詳見 `2026-06-05-d4-per-rule-verifier-poc.md`。

**踩坑 6 — 把「確定性裁決」實作成 workflow agent stage，它就不再確定性。**

**現象**：PoC 的 adjudicate stage 委派 sub-agent 跑 `adjudicate.sh`（已 self-validate 6/6 的確定性腳本）。workflow 回報 `mechanicalVsGroundTruth: 4/6`——2 個 known-good 被判 FAIL exit=2。但**主對話親自跑同一腳本 = 6/6 全對**。

**根因（grep 鐵證，非臆測）**：workflow 內腳本**無 shell/FS 直接存取**，只能透過非確定性 agent 的 Bash 觸達。那條路徑被 `block-dangerous.sh` hook 擋下（`First word detected: 'adjudicate.sh'`，連 `bash <path>` retry 也 BLOCKED）。agent **忠實回報**了 hook 的 exit=2（**沒腦補、沒誤報**）——但那不是裁決邏輯的輸出。

**這比 §3.2 更深的地方**：§3.2 的教訓是「不信 audit agent 的 `pass=true`，主對話再 grep」——針對的是 agent **判斷** verdict。踩坑 6 證明：**連「確定性層」經 agent 中介都會失真**。不是 agent 騙你，是**執行環境（hook gate / PATH / sandbox）污染了本應確定性的結果**。所以「我跑的是確定性 grep 啊」不足以信任——**重點是誰跑的**：主對話親自跑才是 ground truth，workflow sub-agent 跑的「確定性」結果一樣要被主對話親自驗。

**防範（正確架構，PoC 已驗證）**：
- **verify = workflow fan-out**（判斷密集、找 suspect、產**可機械複驗的 inspectable claim** -> agent 適任，本 PoC 6/6 成立）。
- **adjudicate = 主對話 / 真實 hook / CI**（確定性裁決 -> **絕不**經 sub-agent）。
- 判別：問「這個 stage 的輸出若被 hook 擋/缺工具/環境變了，會不會靜默變成假結果？」會 -> 那不是能交給 sub-agent 的「確定性」工作。

**這 PoC 諷刺地自我示範了它要證明的紀律**：它本是為「強化 auto-load 規則遵循率驗證」而建，結果第一手撞上的就是「even mechanical verdict 經 agent 中介不可信」——正是 #439 + dynamic-workflow 紀律的最強佐證。**唯一可信的 mechanical verdict 是主對話親自跑的那個。**

---

## 4. 對 Claude Code 各元件的認識與強化建議

> 本 session 密集使用了 advisor / Workflow / hooks / sub-agents / skills / CLAUDE.md / refs。以下是對每個元件的實戰認識 + 落地建議。

### 4.1 CLAUDE.md / auto-load 規則

- **認識**：CLAUDE.md 是 **advisory context 非 enforced config**（官方：no guarantee of strict compliance）。過長 -> reduce adherence（規則被噪音淹沒）。本 session 親身驗證：規則檔越想塞滿，越要靠 byte-grind 搶救，治標不治本。
- **強化建議**：
  1. **分級載入策略 > 單一大檔**：把規則拆成「always-load 骨架 + on-demand refs 深度」。本 session 三等級的正解最終就是這個（lite 骨架 / full + refs）。
  2. **每條規則附 mechanical check**：無 check 的規則是 vibe，模型遵循率低。這是本交付物的核心設計，也適用於任何人的 CLAUDE.md。
  3. **byte/行數是『報告值』非『設計約束』**：除非有實證的 cap，不要為湊一個數字犧牲規則可驗證性（本 session 最痛的教訓）。

### 4.2 Hooks

- **認識**：hook 是**確定性 gate**，與 CLAUDE.md 的 advisory 本質互補。本 session 的 block-dangerous hook 三次擋下我違反 Bash 慣例的命令——它擋的不是「危險」，是「我沒內化的慣例」。
- **強化建議**：
  1. **確定性需求一律交 hook，不要寫進 CLAUDE.md**（「commit 前必跑 X」「禁某操作」）——CLAUDE.md 不保證遵循。
  2. **hook 在共用資源上必 fail-open（warn 不 block）**：多 session / 背景自動化共用同一 hook，exit 2 會連帶 block 別人。
  3. **hook 錯誤訊息要可操作**：block-dangerous 的訊息有「First word detected / To allow this」——這讓我能立即修正而非卡住。好的 hook = 好的錯誤訊息。

### 4.3 Sub-Agents / Dynamic Workflow

- **認識**：見 §3。核心：**寬度任務的並行轉換 + 對抗驗證是甜蜜點；深度判斷密集的動態優化是陷阱**。Verdict 永遠是 self-report 非 ground truth。
- **強化建議**：
  1. **委派門檻要嚴**：未達「≥10 檔 / >20 tool call / ≥3 獨立子任務」就主對話直接做。本 session 第一個 workflow 違反了這條（byte 優化不是寬度任務）。
  2. **給 agent 已驗證的事實 + 明列 forbidden 變體**：防止「順便改善」重新引入已修正的錯誤。
  3. **workflow 後主對話必親 grep 重驗**：對抗式 audit 提升信心不取代親驗。本 session 靠這條抓到 ref 殘留。
  4. **part-failure 接管**：workflow 部分 agent 失敗時，主對話要能無縫接手（本 session full-builder 失敗後我手動接管）。

### 4.4 advisor

- **認識**：本 session 的 MVP。advisor 看**完整 transcript**，在 3 個關鍵轉折攔截毀滅性決策：staged-not-overwrite、19K-cap-是-workspace-think、完整版自我描述矛盾。它的價值正在於「看到我看不到的全局」。
- **強化建議**：
  1. **大量不可逆/不可攤銷工作前必諮詢 advisor**：byte-grind 那 20 回合若早一步問 advisor「這 cap 對 staged template 適用嗎」，能省下全部白工。
  2. **advisor 指出但我『騎過去』的點要回頭結算**：本 session 完整版 R6 缺 check 的問題，我在 grind 中標了「acceptable 但記一下」然後騎過去——advisor 在 done-check 又抓回來。**「記一下然後繼續」是技術債，advisor 會記得。**
  3. **advisor ≠ rubber stamp**：它給的是 discriminating check，不是背書。

### 4.5 Skills

- **認識**：skill 是**按需載入的深度知識 / workflow**，與 advisory 規則互補。本 session 沒重度用 skill，但去 workspace 化時發現「規則檔引用 skill 名」是耦合源——skill 名是 workspace 特定的。
- **強化建議**：通用規則集不要 hardcode skill 名（`/haiku-pilot` 等）；用能力描述（「依任務複雜度選模型」）取代具名 skill 呼叫，才能跨 workspace 移植。

### 4.6 refs（on-demand 參考）

- **認識**：refs 是「深度知識放這、不佔每 session 前綴」的機制。本 session 學到：**ref 也是交付物，複製來的 ref 一樣帶耦合**（harness-loop.md 踩坑）。
- **強化建議**：
  1. **ref 是延後深度的正解**：完整版的 Rn.x 全深度放 ref，骨架放 auto-load——這是「結構槓桿」勝「byte-grind」的體現。
  2. **複製的 ref 必過同套審計**：別假設現成 ref 乾淨。

### 4.7 Context Management（本 session 自身的 context 紀律）

- **認識**：本 session 很長（多次 compact 風險）。staged deliverable 全程寫進檔案（durable），不靠 context 記憶——這讓 compact / session 中斷不致丟工作。
- **強化建議**：長 session 的交付物**邊做邊落檔**（先 Write 再 advisor 再 commit），不把成果留在 context。本 session 兩次 commit（f014b703 / 562631e0）都在宣告完成前先讓交付物 durable。

---

## 5. 可遷移的 meta-learnings（跨 session 通用）

1. **質疑約束再優化**：逐行優化前先確認約束本身成立。最痛的白工來自「對著一個假約束努力」。
2. **結構槓桿 > 逐行槓桿**：超標就移結構（depth->ref），不要逐行刮。CJK 環境尤其——逐行刮的 byte 報酬極低。
3. **規格未定時做可攤銷的、延後不可攤銷的**：骨架/結構可攤銷（規格變了還能用），逐行打磨不可攤銷（規格變了全廢）。使用者漸進澄清是常態。
4. **Verdict 非證據，主對話必親驗**：sub-agent / workflow / 甚至自己上一輪的產物，都要 grep 重驗。
5. **advisor 的『記一下然後繼續』是技術債**：被指出的缺陷要當場結算或明確排程，不要騎過去——它會在 done-check 回來。
6. **Workflow 甜蜜點 = 寬度（並行確定性轉換 + 對抗驗證），非深度（動態判斷優化）**。
7. **每條規則/每個交付物元件都要可機械驗證**：無 check 的規則是 vibe；無 grep 的「乾淨」是猜測。
8. **「確定性」是執行者的屬性，不是腳本的屬性**（2026-06-05 D4 PoC）：同一個 self-validate 6/6 的確定性腳本，主對話親自跑 = 6/6，經 workflow sub-agent 中介跑 = 4/6（被 hook 擋成 exit=2）。第 4 點是「不信 agent 的**判斷** verdict」；第 8 點更深——**連 agent 轉述的「確定性」結果都不可信**，因執行環境（hook/PATH/sandbox）會污染。架構含義：**adjudicate 絕不經 sub-agent**，確定性 gate 只在主對話/真實 hook/CI 成立。

---

## 6. 數據附錄（本 session 實測）

- 雙版交付物：2 版 × 3 等級 + refs + README = 24 檔。
- Claude 版 byte（去 cap 後，內容範圍分級）：lite 11,146 / standard 15,658 / full 25,388。
- 通用版 byte：lite 3.8K / standard 11.5K / full 14.4K + ref。
- Workflow 用量：2 個 workflow、~20 sub-agent。
- byte-grind 回合數：~20（每輪 6–40 byte，最痛的反模式）。
- advisor 諮詢：5 次，攔截 3 個毀滅性決策 + 1 個 done-check 缺陷。
- 驗證 gate：workspace token 零殘留 · number-regression 零回歸 · 6 版本全有延展性 framing · healthcheck FAIL=0。
- commit：f014b703（初版）-> 562631e0（去 workspace + 可延展）。

---

> **一句話總結**：這個 session 最大的學習不是「Dynamic Workflow 很強」，而是「**Workflow 在寬度任務上很強、在深度判斷優化上是陷阱；而所有 agent 產物——含 workflow——都是 self-report 非 ground truth，主對話的親 grep 與 advisor 的全局視角才是最後防線**」。byte-grind 的 20 回合白工，是「對假約束努力 + 過早不可攤銷優化」的教科書案例，值得每次大量手工打磨前回看。
