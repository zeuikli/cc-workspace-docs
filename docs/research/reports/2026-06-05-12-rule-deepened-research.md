# 12-Rule Canon 深化研究 — 論文接地的全面改寫

> **產出日期**：2026-06-05
> **分支**：`feature/karpathy-mnilax-operational-layer`
> **任務**：以 Karpathy R1–R4 + Mnilax R5–R12 為基線，回到「原始 12 條準則本身」做深入發想與延伸改寫，每處延伸都以論文指引／借鏡／引用接地，並把 7 個運行維度（Prompt Caching / Context Management / Agent Teams / Sub-Agent / Memory Management / LLM 自我演化 / Harness Engineering）融入各條規則的深化，而非疊加為獨立矩陣。
> **配對產物**：`2026-06-05-12-rule-deepened-ruleset.md`（可直接部署的改寫準則全文）
> **基線報告**：本研究承接 #465（universalization-research）/ #466（雙版成品 + TESTBANK），定位為「**深化層**」——前作做通用化與可部署化，本作做**論文發想延伸**。

---

## 0. 框架誠實聲明（讀本報告前必讀）

1. **基線數字是作者自報，非同儕審查**：Karpathy「41%->11%」與 Mnilax「41%->3%（30 codebases / 6 weeks / 50 tasks）」皆為作者在 GitHub / X 上的個人聲明，**無公開方法論、無控制組、無同儕審查**。廣泛轉載 ≠ 獨立驗證。本報告引用時一律標 **作者自報 / LOW-MEDIUM**。
2. **論文接地是「平行失敗模式」非「同一性」**：本研究引用的論文多來自 agent / memory / multi-agent 領域，與「單一 coding assistant 紀律」**不是同一個系統**。論文證據的角色是「在不同層級觀察到平行的失敗模式」，提供 empirical 背書與機制借鏡，**不是證明這些規則本身**。
3. **mapping 信度三分級**：每條「論文 -> 規則」對應標 **Direct**（論文直接證明此規則的失敗模式或機制）/ **Analogous**（不同領域但失敗模式平行）/ **Inferential**（需推理跳躍）。grep 證明「數字存在」≠ 證明「數字接地此規則」（Lesson 2026-06-04-G）。需要 hedge 字眼的對應一律降級或剔除。
4. **社群最佳實踐分官方與軼事**：官方 Anthropic docs 標 HIGH；部落格 / Reddit 軼事標 LOW；唯一接近系統性的跨 repo 數據（AGENTS.md 2,500+ repo）原始方法論未公開，標 MEDIUM。

---

## 1. 任務與基線

### 1.1 原始 12 條的來源鏈

```
2026-01 Karpathy X thread（抱怨 Claude 寫碼 3 大失敗模式）
   └-> Forrest Chang 封裝成 4 條行為規則 CLAUDE.md（65 行）-> GitHub 爆紅（作者自報 120k stars）
        └-> Mnilax 在 30 codebases / 6 weeks 實測 -> 確認 4 條有效（41%-><3% on tasks playing to strengths）
             └-> 補 8 條（R5–R12）涵蓋 2026-05 的 agent 編排問題 -> 12 條
                  └-> cc-workspace 落為 §R1–§R12 強制條文（AB4.0 基線，workspace 耦合）
                       └-> #465/#466 通用化 + 雙版成品
                            └-> 【本研究】論文接地的深化延伸改寫
```

### 1.2 Mnilax 原文揭示的「為何補 8 條」（親取自 X article，12,397 字元）

每條 R5–R12 都來自一個具體失敗時刻（"the moment"），這是基線文件最有價值卻最少被轉載的部分：

| 規則 | Mnilax 的 the moment（親取原文摘要） |
|------|-----------------------------------|
| R5 | 用 Claude「決定 503 是否重試」運作兩週後開始 flaky——模型把 request body 當決策 context，retry policy 變隨機 |
| R6 | 一次 debug session 跑 90 分鐘，模型在同一個 8KB error message 上反覆迭代，最後建議的修法是 40 條訊息前已被拒絕的；token budget 會在第 12 分鐘殺掉它 |
| R7 | codebase 有兩種 error-handling pattern，Claude 寫的新碼兩種都做 -> 雙重 handler，error 被吞兩次，花 30 分鐘才查出 |
| R8 | Claude 在一個它沒讀過的同功能函式旁加了一個一模一樣的函式，因 import order 新的覆蓋舊的，而舊的當了 6 個月 source of truth |
| R9 | Claude 為 auth 函式寫 12 個測試全過，但 production auth 壞了——測試只測「有回傳」不測「回傳對的」，函式回傳常數也能過 |
| R10 | 6 步 refactor 在第 4 步出錯，等發現時 Claude 已在壞狀態上做完第 5、6 步，解纏比重做還久 |
| R11 | Claude 把 React hooks 引進 class-component codebase，能跑但破壞了假設 componentDidMount 的測試模式，花半天移除重寫 |
| R12 | Claude 說 migration「completed successfully」，實際靜默跳過 14% 違反 constraint 的紀錄，11 天後報表異常才發現 |

### 1.3 Mnilax 的 6 個「what didn't work」（反面教訓，是改寫的負面約束）

1. **抄 Reddit/X 的規則** -> 多半是 R1–R4 換句話說，或不通用的 domain-specific（「always use Tailwind」）-> 砍。
2. **超過 12 條** -> 測到 18 條，合規率 76%->52%（過 14 條開始崩）。200 行天花板真實存在。
3. **依賴可能不存在的工具**（「always use eslint」eslint 沒裝就靜默失敗）-> 改 capability-agnostic 措辭（「match the codebase's enforced style」）。
4. **放 examples 而非 rules** -> 3 個 example ≈ 10 條 rule 的 context 成本，且模型 over-fit。用 rule 不用 example。
5. **「be careful」「think hard」「really focus」** -> 純噪音，合規率掉到 ~30%（不可測）-> 換成具體祈使句（「state assumptions explicitly」）。
6. **叫 Claude 當「senior」** -> 沒用，Claude 已自認 senior；gap 在「想 vs 做」之間，imperative rule 能補，identity prompt 不能。

> **對改寫的直接含義**：深化 ≠ 加規則數。深化必須在「保持 ≤12 條主規則」前提下，把每條的**機制、邊界、可驗證條件、反模式**寫深，並用 capability-agnostic + imperative + testable 措辭。這正是把運行維度「融入」而非「疊加」的根本原因。

### 1.4 Mnilax 自承的 4 個斷裂點（Karpathy 4 條的 gap，是深化的切入點）

1. **長時運行 agent 任務**：R1–R4 只針對「正在寫碼的瞬間」，對 multi-step pipeline 沉默 -> pipeline drift（R6/R10/R12 補）。
2. **多 codebase 一致性**：「match existing style」假設只有一種 style，monorepo 12 服務時隨機挑或平均（R7/R11 補）。
3. **測試品質**：Goal-Driven 把「tests pass」當成功，沒說測試要有意義（R9 補）。
4. **production vs prototype**：同一套 Simplicity 規則保護 production 卻拖慢正當需要 100 行 scaffold 探方向的 prototype（R2 的情境化）。

---

## 2. 源頭校驗（primary-source discipline）

| 來源 | 取得方式 | 信度 | 備註 |
|------|---------|------|------|
| Karpathy CLAUDE.md（R1–R4） | WebFetch raw.githubusercontent（SDD cache hit，304 unchanged） | 文件親驗 HIGH；數字 LOW | 文件本身無 Karpathy quote、無方法論 metadata |
| Mnilax article（R5–R12 + moments） | fxtwitter API 親取（12,397 字元 Draft.js blocks） | 文件親驗 HIGH；數字 LOW | X 本體需登入；fxtwitter 為公開鏡像 |
| 12 篇 memory/演化論文 | researcher sub-agent 讀 .md + grep 親驗數字 | 數字 HIGH；mapping 見 §3 分級 | MemGPT/Reflexion/Voyager 等數字逐句 grep |
| MAST 14 失敗模式 + κ=0.88 | sub-agent grep `2503-13657.md` 原文 | HIGH | κ=0.88 **第三度親驗 = inter-annotator agreement，非 spec-quality** |
| 社群/官方最佳實踐 | sub-agent WebSearch + WebFetch | 官方 HIGH / 軼事 LOW | 詳見 §6 |

---

## 3. 12 條規則的論文接地深化分析

> 每條格式：**原則回顧 -> 論文深化（含信度）-> 延伸的新子條/邊界 -> 可機械驗證條件 -> 反模式**。
> 這一節是研究分析；可部署的精煉版見配對 ruleset 檔。

### R1 — Think Before Coding（深化：規格模糊度是天花板）

**原則**：不假設、不藏困惑、浮現 tradeoff；多解釋列選項不靜默選。

**論文深化**：
- **MAST FM-7「Fail to ask for clarification」**（Direct）：MAST 跨 7 框架 200+ 任務發現，「面對不清楚/不完整資料時無法請求補充資訊，導致錯誤行動」是 14 失敗模式之一。**一句零 hedge**：多 agent 架構層的「不清楚不問」與 assistant 紀律層的「沉默假設」是同一失敗在不同層的投影，MAST 提供跨框架 empirical 背書。
- **MetaGPT SOP 結構化 -> token 效率 124.3 vs ChatDev 248.9 tokens/loc（省 ~50%）**（Direct，數字親驗 `2308-00352.md`）：規格（角色/任務的結構化定義）的明確度決定 multi-agent 系統的效率天花板；**前期投資精確規格比加 agent 數量更有效**。**一句零 hedge**：結構化規格使 token 效率翻倍，與 R1「假設顯露、列選項確認」同向。〔註：原稿引「任務完成時間 −40%」係轉引自 Anthropic 官方工具描述改良資料，非 MetaGPT 論文數字，已替換為論文可親驗的 token 效率數字；−40% 改標為「Anthropic 官方資料（二手引用，LOW）」見 §5。〕

**延伸的新子條**：
- **R1.1 規格模糊度優先於運算資源**：遇模糊先釐清規格，不靠「多跑幾次/多開 agent」掩蓋規格缺口。
- **R1.2 Ask-rate 校準**（承 AB4.0）：等價瑣碎選擇（命名/格式/預設值）自決並一句註明；scope 變更/破壞性動作必問。**論文背書缺口**：此校準目前無論文直接支撐，是工程經驗（Opus 4.8 官方 nudge −12pp over-reach），標 **工程經驗 MEDIUM**。

**可機械驗證**：實作前輸出是否含「詮釋 ≤2 句 + 假設 + 多解釋列選項」三要素（grep transcript）。

**反模式**：用「直接做」掩蓋規格缺口；把「不可逆動作」（DELETE/DROP/prod deploy）也自決。

---

### R2 — Simplicity First（深化：情境化 + 記憶庫的 speculative accumulation）

**原則**：最小能解決問題的碼；不投機加 feature、不為單次使用抽象。

**論文深化**：
- **Dynamic Cheatsheet Curator 寫入前評估「有用性與可遷移性」，低品質不寫入**（Direct）：DC 把 R2 從「碼的簡潔」延伸到「**記憶庫的簡潔**」。**一句零 hedge**：記憶庫不累積所有輸出，只存真正有複用價值的 snippet，直接防止記憶庫膨脹與品質退化。
- **DC 小模型（GPT-4o-mini）記憶庫被錯誤策略污染、受益反轉**（Direct，數字親驗：DC Claude 3.5 在 AIME 2024 23.3%->50.0%，但小模型受益有限）：speculative accumulation 在記憶層的代價比在碼層更隱蔽。
- **Anthropic「Teams frequently make this choice incorrectly」**（Direct）：錯置委派（為複雜任務自動拆 agent）製造 coordination overhead 抵消平行收益。**一句零 hedge**：Rule of 3 有 multi-agent 版本——不因任務看起來複雜就自動拆 agent。

**延伸的新子條**：
- **R2.1 記憶層 Simplicity**：寫入持久記憶/cheatsheet 前先問「這條有跨任務複用價值嗎」，無 -> 不寫（防 DC 觀察到的記憶污染）。
- **R2.2 委派 Simplicity**：不因任務複雜就自動 fan-out；委派門檻（≥10 檔/>20 tool call/≥3 獨立子任務）未達 -> 主對話直接做。
- **R2.3 情境化例外**（補 Mnilax 斷裂點 4）：prototype / spike 階段正當需要 speculative scaffold 探方向時，Simplicity 不過火——**明示標註「prototype 模式」**，達方向後再砍。

**可機械驗證**：diff 行數 vs 任務最小解的比值；持久記憶寫入是否附「複用理由」一行。

**反模式**：為「未來可能需要」鋪設；把每次互動都存進記憶庫；prototype 階段過早 over-engineer 或 production 階段假裝 prototype 放縱。

---

### R3 — Surgical Changes（深化：cache 前綴穩定性 = prompt 層的外科精度）

**原則**：只動必須動的；不順手改周邊、不重構沒壞的；改動造成的孤兒才清。

**論文深化**：
- **Don't Break the Cache（arXiv 2601.06007）：prompt caching 在 agentic workflow 降 API 成本 41–80%，但動態內容造成的 cache invalidation 是關鍵風險；建議 system-prompt-only caching（Claude Sonnet 4.5 達 78.5% cost reduction / 22.9% TTFT improvement）**（Direct，數字親驗 `2601-06007.md`）：**一句零 hedge**：快取前綴設計若把動態內容放前段污染靜態邊界，引發的成本劣化與「改動污染周邊代碼」同構——靜態前綴穩定性是 surgical 精度在 prompt 層的投影。〔修正：原稿誤植「TTFT 13–31% / 500+ session」，論文原數字為 22.9% TTFT / 78.5% cost（system-prompt-only），已更正。〕
- **SWE-agent「Cascading Failed Edits」是失敗分布最大宗（首次失敗恢復率 90.5% -> 追加失敗後 57.2%）**（Analogous）：**一句零 hedge**：過寬/缺理解的編輯引發連鎖失敗，與「bug fix 順手清理」引發的周邊污染機制相同；surgical 邊界一旦破壞，後果指數惡化（90.5%->57.2% 量化此惡化）。
- **MemoryBank Ebbinghaus 衰減 + Reflexion episodic-only（只追加不修改）**（Analogous）：記憶寫入應最小化、append-only（不就地改寫現有記憶），與 R3「只動最小範圍」平行。Reflexion 此設計在 HumanEval 達 91%。

**延伸的新子條**：
- **R3.1 Prompt-層 Surgical**：CLAUDE.md / system prompt 的靜態前綴 mid-session 不動（破快取 = full cache miss）；動態狀態經 `<system-reminder>` 注入 TAIL，不寫進靜態前綴。
- **R3.2 記憶 append-only**：對持久記憶優先 append 不就地改寫；需修正舊記憶時保留原條目作 rollback（承 Operational Layer）。

**可機械驗證**：每行改動可追溯到任務要求（grep）；`cache_hit_rate = cache_read / input_tokens > 0.7`（長跑 session）；記憶寫入是 append 或有 rollback 備份。

**反模式**：mid-session 改 CLAUDE.md/切 model/增刪 tool（四大破快取源）；就地覆蓋舊記憶無備份。

---

### R4 — Goal-Driven Execution（深化：Reflexion/Voyager/ReAct 的迭代演化迴圈）

**原則**：定義可觀測成功條件，迭代到達標而非走步驟；完成條件必須可機械驗證。

**論文深化**（這是「LLM 自我演化」維度的主接地點）：
- **ReAct Thought-Action-Observation 交錯（ALFWorld +34%、WebShop +10% vs RL baseline）**（Direct）：**一句零 hedge**：ReAct 的 iterative action-observation loop 是 R4「成功條件可機械驗證、迭代至達標」的 harness 實作；無 Observation 接地 = 目標狀態不可觀測。Act-only（無 reasoning trace）在 long-horizon 系統性低於 ReAct，量化了「無迭代迴圈」的代價。
- **Reflexion：失敗後生成語言反思存入 episodic buffer，下次注入（HumanEval pass@1 91.0% > GPT-4 80.1%；ALFWorld 97% vs ReAct 53%）**（Direct）：**一句零 hedge**：反思機制使代理人每次嘗試後明確「驗證失敗原因 -> 迭代」而非盲目重試，是 R4「迭代到達標」的機械實現。
- **Voyager：技能生成後在環境實際執行驗證，通過才入庫（技術樹 15.3× 快）**（Direct）：**一句零 hedge**：成功條件是「環境中可執行並達成目標」這種可機械驗證的條件，而非 LLM 自評。
- **Reflexion 的 Evaluator 元件是反思的前提**（Direct，亦接地 R9）：**一句零 hedge**：沒有獨立 evaluator 給出明確失敗訊號，LLM 就無法生成有意義的反思——可驗證的成功條件是自我演化的先決條件。

**延伸的新子條**：
- **R4.1 反思迴圈（自我演化）**：task 失敗 -> 生成結構化反思（失敗模式 + 修正假設）-> 下次同類任務注入。**前提**：反思必須由獨立 evaluator 的失敗訊號觸發，不由 LLM 自評觸發（否則是無根據自我反思）。
- **R4.2 技能/洞見入庫門檻**：成功經驗要進持久庫，須有可機械驗證的通過證明（碼執行/benchmark/對比軌跡），不接受文字自評（Voyager 原則）。
- **R4.3 完成條件機械化**：「make it work」是弱條件 -> 卡在「下一步」；強條件（測試/healthcheck/特定輸出）才能獨立 loop。

**可機械驗證**：開工前是否寫下可機械驗證的成功條件；宣告完成前是否展示前 5 行/後 5 行輸出（R12 連動）；反思是否由 evaluator 失敗訊號觸發。

**反模式**：把「tests pass」當唯一目標寫淺測試（-> R9）；LLM 自評觸發的反思（無 evaluator）；無 Observation 接地的盲目重試。

---

### R5 — Use the Model for Judgment, Code for Decisions（深化：RouteLLM/DC 的確定性化）

**原則**：LLM 只做判斷（分類/摘要/提取/生成）；確定性碼做決定（路由/重試/status code/數學）。

**論文深化**（這是最容易被 LLM 自己違反的規則，論文證據最硬）：
- **RouteLLM：學習型 router 比 LLM 自判路由節省 3.66× 成本，MT Bench 減少 GPT-4 呼叫 75% 仍恢復 95% 性能，routing overhead < 0.4%**（Direct）：**一句零 hedge**：RouteLLM 明確比較「LLM-as-router vs learned-classifier-as-router」，分類器全面勝出——把路由從 LLM 搬到確定性分類器的工程成本極低（< 0.4% overhead），沒有理由不做。
- **Dynamic Cheatsheet Game of 24：10%->99%（LLM 判斷「要不要用 Python 暴力解」，確定性 code 做實際計算）**（Direct）：**一句零 hedge**：把計算交給 LLM 是 baseline 停在 10% 的根因；路由「要不要用工具」= 判斷（LLM），執行計算 = 確定性（Python），這是 R5 的教科書案例。
- **MemGPT function chaining：LLM 決定「是否還需更多 context 再回應」（判斷），程式執行 page-in（確定性）**（Direct）：記憶操作層的 R5 體現。
- **Voyager 代碼技能（確定性）vs「該召用哪個技能」（LLM 判斷）明確分離**（Direct）。

**延伸的新子條**：
- **R5.1 路由確定性化**：模型/工具/重試路由用學習型分類器或規則，不用 LLM 即時判斷（RouteLLM 證據）。
- **R5.2 記憶操作分層**：「是否 page-in / 是否該整合記憶」是判斷（LLM 觸發）；「執行 page-in / 寫入記憶」是確定性（程式執行）。
- **R5.3 工具呼叫 vs 自算**：可被工具/程式精確算出的（數學、解析、轉換）一律交工具，LLM 只決定「要不要用」（DC 證據）。

**可機械驗證**：路由/重試/status-code 處理是否出現 LLM 呼叫（grep；應為 0）；計算密集任務是否委派工具。

**反模式**：用 Claude「決定 503 是否重試」（Mnilax R5 the moment，request body 變決策 context -> 隨機 policy）；讓 LLM 做算術。

---

### R6 — Token Budgets Are Not Advisory（深化：MemGPT 分層記憶 + Lost-in-the-Middle）

**原則**：per-task 4,000 / per-session 30,000 token 硬預算；接近預算 -> 摘要重啟，不硬推；浮現超標 > 靜默超支。

**論文深化**（這是「Memory Management」+「Context Management」維度的主接地點）：
- **MemGPT：context 滿時強制 evict，未 page-in 的資訊在決策期間不可見（DMR 92.5% vs 固定 context 32.1%，+28–60pp）**（Direct）：**一句零 hedge**：上下文預算硬性邊界直接決定代理人當前步驟能「看到」什麼，超出即資訊丟失——R6 的 budget 不只是省錢，是決定可見性。MemGPT 把 context 當 OS 主記憶、外部記憶當磁碟，用 function call page in/out，是 R6 的架構化實現。
- **Lost-in-the-Middle（arXiv 2307.03172）：中間位置準確率下降 30%+，1M 名義 context 可靠工作區實際約 64K–128K**（Direct）：**一句零 hedge**：context 名義大 ≠ 可用大；在 1M 中間段放關鍵資訊等於靜默丟棄——R6 的 budget 意識必須含**位置意識**（HEAD 放原始目標 / TAIL 放最新工具輸出 / 中間放動態狀態）。
- **MemoryBank Ebbinghaus 衰減曲線（R = e^(-t/S)）決定何時棄舊 context**（Analogous）：頻繁召回的記憶強度 S 增大，長期未用的衰減後淡出——提供「何時 evict」的機制借鏡。
- **ACE incremental delta updates 達 91.8% input tokens served from KV cache；移除 delta -> context collapse（「sharp performance declines as accumulated knowledge is overwritten」）；agents +10.6% / finance +8.6%**（Direct，數字親驗 `2510-04618.md`）：**一句零 hedge**：每次 full-rewrite 而非 delta 是 token 爆炸與 context collapse 的直接操作來源，ACE 的 91.8% KV reuse 是 R6 的量化錨點。〔修正：原稿誤植「帳單 −82.6%」，論文無此數字，已移除——abstract 僅稱「significantly reducing adaptation latency and rollout cost」。〕

**延伸的新子條**：
- **R6.1 分層記憶卸載**：context 達 70% -> 觸發 page-out（把舊狀態寫外部記憶，只留索引）；不在單一 context 裡硬撐到爆。
- **R6.2 位置意識**：原始目標放 HEAD、最新工具輸出放 TAIL、動態狀態放中間（NLAH 原則 + Lost-in-the-Middle 接地）。
- **R6.3 Delta 不 full-rewrite**：更新長文/記憶用 delta，不整篇重寫（ACE 證據，亦護 prompt cache）。

**可機械驗證**：session token 用量 `/usage` vs 預算；compact 觸發點（長 agentic 30–35% 主動）；`cache_hit_rate > 0.7`。

**反模式**：90 分鐘 debug 在同一 8KB error 上空轉（Mnilax R6 the moment）；關鍵資訊埋 context 中間段；每次 full-rewrite 長文。

---

### R7 — Surface Conflicts, Don't Average Them（深化：MAST Inter-Agent Misalignment + 辯論 echo-chamber）

**原則**：兩個矛盾 pattern 不靜默選、不混用；挑一個（較新/較測過）說明理由，另一個標記清理。

**論文深化**（這是「Agent Teams」維度的主接地點）：
- **MAST「Inter-Agent Misalignment」整類（coordinator 指令漂移、資訊傳遞失真、Ignored other agent's input）**（Analogous）：**一句零 hedge**：矛盾被平均化（agent 各自解讀指令取交集）是 R7「靜默選擇」在分散式系統的放大版；structured handoff + confirmation 是 R7 在多 agent 層的落地形式。
- **多 agent 辯論：GSM8K +8pp / MMLU +7.2pp，但 echo-chamber 固化錯誤是主要風險**（Analogous，代價 2.5–5× token）：**一句零 hedge**：多視角交叉驗證能提升正確率，但若各方互相強化同一錯誤（echo-chamber），等於把矛盾平均掉——R7 要求矛盾浮現而非收斂到舒適共識。
- **HippoRAG 知識圖譜：孤立 chunk 無法回答關聯問題，矛盾事實若不顯式連結就無法在檢索時被發現**（Inferential）：**一句零 hedge（標 Inferential，需跳躍）**：記憶條目間的矛盾若不顯式建立連結，檢索時不會浮現——與 R7「不靜默選擇矛盾」目標一致，但「知識圖譜檢索」到「codebase pattern 衝突」的連結需要推理跳躍，故降級。

**延伸的新子條**：
- **R7.1 多來源矛盾浮現**：sub-agent / 多視角輸出矛盾時，不收斂到「都滿足」的平均解，明列矛盾交主對話決策（child 不 self-resolve 矛盾）。
- **R7.2 記憶/洞見遷移前判矛盾**：跨任務注入洞見前判斷是否與當前任務矛盾，不靜默混用（ExpeL 任務相似度門控）。

**可機械驗證**：是否寫 `TODO(conflict): chose A over B; reason …; remove B before <milestone>`；矛盾是否被明列而非收斂。

**反模式**：寫同時滿足兩種 error-handling pattern 的碼（Mnilax R7 the moment，雙重 handler 吞兩次 error）；echo-chamber 式共識。

---

### R8 — Read Before You Write（深化：context failure 是新失敗主因 + SWE-agent 定位先於編輯）

**原則**：改動前讀目標 exports + 直接 caller + 共用 utility；不懂現有結構先問。「Looks orthogonal」最危險。

**論文深化**：
- **SWE-agent「find_file / search_dir 先於 edit」+ Zoom-in（dir->file->line）；跳過定位直接 edit = 23.4% cascading failure**（Direct）：**一句零 hedge**：「Reproduction-first（create, edit, python）」是機械化的 R8 執行，跳過定位直接 edit 的失敗代價被量化為 23.4% cascading failure。
- **「Most agent failures are now context failures, not model failures」（Anthropic/LangChain/Manus 三方共識）**（Analogous）：**一句零 hedge**：先讀 exports + caller + shared utility 在 context engineering 語義下等價於「先確認 context 邊界再寫入新資訊」；錯置的 context write 與未讀就改一樣破壞上游依賴。
- **四大破快取源（mid-session 切 model / 增刪 tool / 改 system prompt / 改 thinking 參數）**（Direct，接地 R8 的「先確認影響再動」）：**一句零 hedge**：任何 system prompt 修改前必先確認快取拓撲影響，「看起來正交」的模型切換實際上使整個前綴快取全失效。
- **CoALA：Working Memory（= context window）寫入前必先讀現有記憶狀態**（Direct）：對外部記憶庫寫入前，先讀相關條目確認重複/衝突（A-MEM Zettelkasten 互聯機制）。

**延伸的新子條**：
- **R8.1 記憶寫入先讀**：對持久記憶任何寫入前，用當前 query 做 similarity search 確認無重複/衝突再決定 append 或更新。
- **R8.2 快取拓撲先讀**：改 system prompt / 切 model / 增刪 tool 前先確認對 cache_hit_rate 的影響。

**可機械驗證**：是否先讀 exports/caller/utility（transcript）；記憶寫入前是否有 similarity check。

**反模式**：在沒讀過的同功能函式旁加重複函式（Mnilax R8 the moment，import order 讓新的覆蓋當了 6 個月 source of truth 的舊的）。

---

### R9 — Tests Verify Intent, Not Just Behavior（深化：Evaluator 是演化先決 + 辯論交叉驗證）

**原則**：測試要能在業務邏輯改變時失敗；能通過任何實作的測試 = 沒測試；mock 外部邊界非業務核心。

**論文深化**：
- **MAST「Task Verification」整類（Premature termination / No verification / Incorrect verification）是最難自動修復的類別**（Direct）：**一句零 hedge**：MAST 原文「allowing errors to propagate undetected」直接映射 R9「假測試」與 R12「幻覺式完成」；Incorrect verification（驗證方法本身錯）正是 R9 的「假測試」。
- **Reflexion Evaluator：無獨立失敗訊號就無法生成有意義反思**（Direct，亦接地 R4）：**一句零 hedge**：可驗證的成功條件是自我演化的先決條件——R9 的「測試驗證意圖」是 R4 反思迴圈能運作的前提。
- **多 agent 辯論交叉驗證 vs echo-chamber**（Analogous）：**一句零 hedge**：多視角交叉驗證 = R9「測試要能在業務邏輯改變時失敗」；echo-chamber 等價於「通過任何實作的測試 = 假測試」。

**延伸的新子條**：
- **R9.1 Evaluator 獨立性**：成功條件的判定器（測試/healthcheck/對比）必須獨立於被測對象，不能由 LLM 自評充當（否則 R4 反思失去根據）。
- **R9.2 演化入庫驗證**：洞見/技能進持久庫前須通過可機械驗證（連動 R4.2）。

**可機械驗證**：測試是否會在業務邏輯 mutation 時失敗（mutation testing）；evaluator 是否獨立於被測對象。

**反模式**：12 個 auth 測試全過但函式回傳常數（Mnilax R9 the moment）；LLM 自評當 evaluator。

---

### R10 — Checkpoint After Every Significant Step（深化：ReAct Observation + 記憶整合門控）

**原則**：每完成重要步驟輸出 1 句 `[Checkpoint] 做了X/驗了Y/剩Z`；無法描述當前狀態時停下重述。

**論文深化**（這是「Context Management」+「Memory consolidation」維度的接地點）：
- **ReAct Thought-Action-Observation triple 克服 CoT 幻覺傳播**（Direct）：**一句零 hedge**：每個 Observation 迫使模型接地當前真實狀態、不在幻覺狀態上續推——這是 R10「無法描述當前狀態時停下」的形式化；Thought-Action-Observation = checkpoint loop 是 harness 層公認結構。
- **Summarization 資訊保留率僅 37%（Factory.ai，MEDIUM）**（Analogous）：**一句零 hedge**：compact 後若無 checkpoint 驗證（任務目標仍在？安全紅線仍在？），37% 資訊損失會變成 loss-of-state 在損壞狀態上續跑——R10 正是緩解此損失的機制。
- **SCM/MemoryBank 記憶控制器顯式門控「何時整合」+ Survey 2404.13501「整合是性能退化主要來源」+ Human->AI Survey「整合應由重要性篩選觸發，非自動」**（Direct）：**一句零 hedge**：記憶整合（consolidation）等同 checkpoint 寫入，必須在顯式觸發時才執行，不應每次互動後自動發生（自動整合 = 靜默失敗風險）。
- **ExpeL offline 批量整合 vs 即時整合**（Direct）：offline consolidation 等同多個 checkpoint 後才整合，防即時整合的噪聲退化。
- **MAST「Step repetition / Loss of conversation history」**（Direct）：無法判斷已在何處 -> 重複執行；R10 狀態追蹤防範。

**延伸的新子條**：
- **R10.1 Checkpoint 含記憶寫入**：checkpoint 不只記「做了什麼」，也記「寫入 episodic memory 什麼」（task ID + 成功/失敗 + 關鍵觀察，非完整軌跡）。
- **R10.2 整合門控**：記憶 consolidation（episodic->semantic）只在顯式觸發或 N 個 checkpoint 後執行，禁自動；整合前保留原 episodic 作 rollback。
- **R10.3 Compact 後自檢**：compact/summarize 後驗「任務目標/安全紅線/最近工具結果未失真」，任一失 -> rewind（緩解 37% 損失）。

**可機械驗證**：每步是否輸出 checkpoint 句；compact 後是否跑三項自檢；整合是否門控（非自動）。

**反模式**：6 步 refactor 第 4 步壞了還做完 5、6（Mnilax R10 the moment）；自動記憶整合無 rollback。

---

### R11 — Match the Codebase's Conventions（深化：多 codebase 一致性 + 有害慣例不 silent fork）

**原則**：codebase 既有慣例 > 個人偏好；不確定跟隨最近 3 commit；有害慣例明說另開議題，不 silent fork。

**論文深化**：
- **Mnilax 斷裂點 2（多 codebase 一致性）**：「match existing style」假設只有一種 style，monorepo 12 服務時隨機挑或平均（作者自報 LOW，但與 R7 同構）。
- **MemGPT/CoALA Procedural Memory（可執行 artifact 形式儲存慣例）**（Inferential）：**一句零 hedge（標 Inferential）**：把慣例存成可執行/可檢查的 artifact（lint config、template）比存成文字描述更不易漂移——但「procedural memory」到「codebase convention」的連結需推理跳躍，故降級。
- **capability-agnostic 措辭**（Mnilax what-didn't-work #3，作者自報）：「match the codebase's enforced style」優於「always use eslint」（工具沒裝就靜默失敗）。

**延伸的新子條**：
- **R11.1 多 codebase 範圍判定**：monorepo / 多服務時，先判定當前檔案所屬服務的慣例（最近 commit + 該目錄 config），不跨服務平均。
- **R11.2 慣例存成可檢查 artifact**：能用 lint/template/config 表達的慣例優先存成 artifact，不只寫文字（降漂移）。

**可機械驗證**：新碼風格 vs 該目錄最近 3 commit 的一致性；是否 silent fork（無 issue 記錄就引入新 pattern）。

**反模式**：把 React hooks 引進 class-component codebase（Mnilax R11 the moment，破壞 componentDidMount 測試模式）；依賴可能不存在的工具。

---

### R12 — Fail Loud（深化：靜默失敗是最貴的 + 記憶污染的隱蔽性）

**原則**：不確定是否成功就明說；「migration completed」若靜默跳過紀錄是錯的；截斷必標示。

**論文深化**：
- **MAST「Information withholding / Premature termination / No verification」**（Direct）：**一句零 hedge**：agent 隱藏部分失敗（Information withholding）與 R12「不藏部分失敗」直接對應；Premature termination（未完成即宣告完成）= R12「幻覺式完成」。
- **DC 記憶污染：策略看似存入，實際引導後續決策時引入錯誤（小模型受益反轉）**（Direct）：**一句零 hedge**：記憶污染是靜默失敗——需要顯式的記憶品質指標讓退化可見。
- **Survey 2404.13501：長時運行後性能退化，根源是整合的資訊丟失**（Analogous）：**一句零 hedge**：記憶退化是靜默失敗的典型形態——系統繼續運作但輸出品質持續下降，需要可觀測退化指標（如召回準確率 benchmark）讓失敗顯露。
- **SWE-agent linting guardrail：no linting -> −3pp**（Direct）：**一句零 hedge**：linting 在語法錯誤時立即阻斷而非靜默接受，是 R12 的工具層實現，−3pp 量化了靜默失敗的代價。

**延伸的新子條**：
- **R12.1 記憶退化可觀測**：持久記憶/cheatsheet 須有品質指標（召回準確率/污染檢查），退化時 fail loud 而非靜默劣化。
- **R12.2 PGE（Proactive Generation & Evaluation）**：完成後跑 healthcheck 或委派 review，不接受口頭自評；略過步驟必明示。
- **R12.3 截斷標示**：讀 >200 行檔分段報「N-M/X 行，剩 Y」；搜尋超限標 `[CONTEXT BOUNDARY]`，靜默截斷禁止。

**可機械驗證**：完成宣告前是否展示驗證輸出前5/後5行；migration/批次是否報「成功 N / 跳過 M / 原因」；截斷是否標示。

**反模式**：migration「completed successfully」靜默跳過 14% 紀錄（Mnilax R12 the moment，11 天後才發現）；記憶靜默劣化。

---

## 4. 跨規則主題：Harness Loop 與 LLM 自我演化的整合

本研究的請求明確要求準則「符合 Harness Loop」並涵蓋「LLM 自身的演化能力」。這兩者不是新規則，而是**貫穿 R4/R9/R10/R12 的元迴圈**：

```
OBSERVE  ← R10 Checkpoint（觀測當前狀態）
IDENTIFY ← R1 Think（顯露問題/假設）
PROPOSE  ← R2 Simplicity（最小提案）
TEST     ← R9 Evaluator（獨立驗證，Reflexion 先決條件）
APPLY    ← R3 Surgical（最小改動）+ R12 gate（破壞性前確認）
RECORD   ← R4.1 反思迴圈 + R10.1 記憶寫入（演化的持久化）
```

**論文接地的演化迴圈**（信度分級）：
- **Reflexion**（Direct）：失敗 -> 語言反思 -> episodic buffer -> 下次注入。對應 RECORD -> OBSERVE 的閉環。
- **Voyager**（Direct）：成功技能環境驗證後入庫，可組合呼叫。對應 APPLY -> RECORD 的技能累積。
- **ExpeL**（Direct）：offline 批量對比成功/失敗軌跡提取洞見。對應 RECORD 的離線整合（防即時整合退化）。
- **Dynamic Cheatsheet**（Direct）：test-time learning，Curator 門控寫入。對應 RECORD 的品質門控。

**演化的安全邊界**（避免「自我演化」變成「自我污染」，DC 小模型污染證據）：
1. 反思只由獨立 evaluator 失敗訊號觸發，不由 LLM 自評觸發（R9.1）。
2. 洞見入庫須通過可機械驗證（R4.2 / R9.2）。
3. 整合門控、非自動（R10.2）。
4. 記憶退化可觀測（R12.1）。
5. 高錯誤率場景禁自動寫入（DC 證據）。

---

## 5. 與社群/官方最佳實踐的對照

### 5.1 官方 Anthropic 指引（HIGH 信度）強化的規則

| 官方指引 | 強化規則 | 來源 |
|---------|---------|------|
| CLAUDE.md 目標 ≤200 行，過長 reduce adherence | R6 | code.claude.com/docs/en/memory |
| CLAUDE.md 是 advisory，硬性執行用 hooks | R12 | best-practices |
| `.claude/rules/*.md` + `paths:` frontmatter conditional loading | R6 + R2 | memory docs |
| `/init` 生成後人工精簡 | R8（先讀 codebase 再寫規則） | best-practices |
| 「去掉這條 Claude 會犯錯嗎？否->刪」 | R3 | best-practices |
| Writer/Reviewer 雙 session adversarial review | R9 | best-practices |
| Subagents 隔離研究避免污染主 context | R5 | best-practices |
| `IMPORTANT`/`YOU MUST` 強調語提升遵循率 | R1 | 官方文件原文 |

### 5.2 12 條沒涵蓋的新洞見（官方 HIGH）

1. **Prompt caching × CLAUDE.md 靜態前綴**：CLAUDE.md 是 session 內最穩定快取前綴，mid-session 編輯不生效也不破壞快取；cache hit rate 是 Anthropic SEV 監控指標 -> 已整合進 R3.1 / R6.3 / R8.2。
2. **`claudeMdExcludes`（monorepo 多 team 污染）**：其他 team 的 CLAUDE.md 會被自動載入，用 `settings.local.json` glob 排除 -> 整合進 R11.1（多 codebase）。
3. **`<!-- HTML comment -->` zero-token 維護筆記**：注入前剝除，不耗 context -> R6 token 工具補充。
4. **官方 Auto Memory（v2.1.59+）**：MEMORY.md 前 200 行/25KB session start 載入，Claude 自決何時寫 -> 整合進 R10.1 記憶寫入。

### 5.3 社群數字的信度（不可當共識）

| 數字 | 信度 | 理由 |
|------|------|------|
| 官方 200 行上限 | HIGH | 官方文件 |
| AGENTS.md 2,500+ repo「中位 300-350 字最佳，>1,000 字負相關」 | MEDIUM | 二手引用，原始方法論未公開 |
| 「150-200 instructions 後合規率劣化」（Jaroslawicz et al. 2025） | LOW | 社群多次引用但原始論文連結無人提供，**不以學術背書口吻引用** |
| Mnilax 41%->3% / Karpathy 41%->11% | LOW | 作者自報，無控制組/同儕審查 |
| lazy loading 省 40-70% token | LOW | 部落格 tiktoken 計算，非官方計數器 |

---

## 6. 改寫策略總結（-> 配對 ruleset 檔的設計依據）

1. **保持 ≤12 條主規則**（Mnilax 14 條崩潰證據）：所有深化以「子條 Rn.x」形式掛在主規則下，不新增主規則編號。子條是「同一注意力預算下的細化」，非競爭新規則。
2. **7 運行維度融入而非疊加**：Memory->R6/R8/R10、演化->R4/R9、caching->R3/R6/R8、agent teams->R7、sub-agent->R2/R5、context->R6/R10、harness->R4/R10/R12。無獨立矩陣。
3. **每條深化保留信度標籤**：Direct 證據寫進規則正文；Inferential 證據（HippoRAG->R7、procedural memory->R11）只在研究報告提及，不寫進可部署 ruleset（避免 Lesson 2026-06-04-G 過度延伸）。
4. **capability-agnostic + imperative + testable 措辭**（Mnilax what-didn't-work #3/#5/#6）：每條附「可機械驗證條件」。
5. **Harness Loop 作元迴圈**而非規則：OBSERVE->…->RECORD 對應 R10->…->R4.1，不佔規則編號。

---

## 7. 參考論文（本研究實際引用）

> **親驗紀律說明**：論文數字的初次 grep 由 researcher sub-agent 執行；其中**載重數字**（MemGPT 92.5%/32.1%、Reflexion 91.0%/80%、RouteLLM 3.66×/75%/95%、Voyager 15.3×/3.3×/2.3×、DC Game of 24 10%->99%、ACE 91.8% KV reuse、Don't Break Cache 41–80%/22.9% TTFT、MetaGPT 124.3 vs 248.9 tokens/loc、SWE-agent 23.4% cascading / 90.5%->57.2% recovery）由主對話**二次 grep 親驗**（依 workspace 鐵律「subagent verdict 非證據」），二次驗證攔截並修正 3 處 sub-agent 誤植（ACE −82.6% 不存在；Don't Break Cache TTFT 應為 22.9% 非 13–31%；MetaGPT −40% 為二手引用非該論文）。未經主對話二次 grep 的次要數字標 **sub-agent grep（MEDIUM）**。


**Memory**：MemGPT (2310.08560) · SCM (2304.13343) · MemoryBank (2305.10250) · HippoRAG (2405.14831) · A-MEM (2502.12110) · CoALA (2309.02427) · Survey-Memory (2404.13501) · Human->AI Memory Survey (2504.15965)
**Self-Evolution**：Reflexion (2303.11366) · Voyager (2305.16291) · ExpeL (2308.10144) · Dynamic Cheatsheet (2504.07952)
**Agent Teams / Multi-Agent**：MAST (2503.13657) · MetaGPT (2308.00352) · AutoGen (2308.08155) · AgentVerse (2308.10848) · ChatDev (2307.07924) · Multi-Agent Debate (2305.14325) · MultiAgentBench (2503.01935)
**Harness / Sub-Agent**：ReAct (2210.03629) · SWE-agent (2405.15793) · RouteLLM (2406.18665)
**Context / Caching**：Lost-in-the-Middle (2307.03172) · StreamingLLM (2309.17453) · SnapKV (2404.14469) · ACE (2510.04618) · Don't Break the Cache (2601.06007)

**第一來源**：Karpathy CLAUDE.md（multica-ai/andrej-karpathy-skills，WebFetch 親驗）· Mnilax article（x.com/Mnilax/status/2053116311132155938，fxtwitter 親取 12,397 字元）
**官方文件**：code.claude.com/docs/en/memory · /best-practices

---

*本報告為深度研究分析。可直接部署的精煉準則見配對檔 `2026-06-05-12-rule-deepened-ruleset.md`。*
