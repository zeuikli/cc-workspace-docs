# Harness Engineering 深度研究報告

**生成日期**：2026-05-31  
**增量更新**：v2a（2026-06-05）併入 4 篇 in-domain（ACON / AgentFlow / addyosmani / configuring-agentic）｜**v2b（2026-06-05）**併入 ~14 篇本機未引用 harness-adjacent + 3 篇 web-only primary 來源（見 §E）  
**語料範圍**：43 篇本機深度引用（2023–2026）+ 5 篇本機一行 coverage + 3 篇 web-only primary + 3 篇旁證 system card  
**方法論**：research-hub:deep（來源驅動，每 claim 標 [P/O/C/E]，D2 交叉驗證）；v2b 增量走 **4× researcher 平行深讀（context isolation）→ 主對話親自 grep 驗每個 stat → opus 對抗 critic 審 section-mapping + superlative（zero-hedge test）→ 主對話親自 grep 重駁 critic**（攔截 1 次 critic 幻覺，見 §E0）  
**v2b 範圍邊界（誠實聲明）**：最新本機 harness 論文止於 2026-05-23（不晚於原報告）；web 掃描確認**無** 2026-06 之後新論文超越本報告——AutoHarness（2026-02）/ Harness-Bench（2026-05-27）是**遺漏**論文非「截稿後新出」。v2b 主價值在本機未引用論文併入，非前向 5 日 gap（此判斷在開工前由 advisor 預測、事後證實）。

---

## A. 演進史：抽象層級遷移時間軸

### A1. 起點：Agent-Computer Interface（2023–2024）

**2023年 CoALA** 建立了語言 agent 認知架構的第一個形式化框架 [P: coala]。CoALA 以四維記憶（working/episodic/semantic/procedural）加上結構化行動空間（讀/寫/推理/反思/外部行動）描述 agent 系統，但此時「harness」概念尚未浮現——基礎設施仍被視為 agent 實作細節而非獨立研究對象。

**2024年 SWE-agent** 首次將 interface 設計提升為一級研究問題 [P: swe-agent]。Agent-Computer Interface（ACI）概念確立了一個核心命題：「界面設計可以匹配甚至超越模型改進的效果」——僅透過 ACI 重設計即達成 10.7 個百分點的提升，超越當時所有 RAG 方案。SWE-agent 四原則（動作簡單易懂、動作緊湊高效、環境反饋有信息量且精簡、防護欄降低錯誤傳播）是 harness 設計學的前身。

### A2. Scaffolding 命名期（2026年初）

**OpenDev（2026-03）** 正式使用「scaffolding」術語，將終端 agent 的基礎設施問題系統化為三大挑戰：context window 管理、安全與破壞性操作防護、能力擴展 [P: opendev] [O: opendev]。OpenDev 四層架構（Entry/Agent Core/Tool/Infrastructure）及雙 agent 分離（Planner vs Executor）確立了 scaffolding 的組件模型。

**同月，「Agentic Harness for Real-World Compilers」（2603.20075）**以 LLVM bug 修復為域，記錄了通用 LLM 在專業域的 -60% 性能退化，論證域特化 harness 的必要性 [P: agentic-harness-compilers]。此研究暗示：harness 不只是通用框架問題，也是域適配問題。

### A3. Harness 命名成熟期（2026年3–4月）

**OpenAI Codex 部落格文章（2026-02）** 是「harness engineering」術語的重要傳播節點 [O: codex]。Ryan Lopopolo 記錄了從空 git 倉庫到百萬行程式碼的實踐歷程，明確定義了工程師角色的轉變：從「寫代碼」到「設計環境、指定意圖、建立反饋迴路」。文中 AGENTS.md-as-table-of-contents 模式、觀測性基礎設施（LogQL/PromQL/CDP 直連 Codex）是 harness 工程的早期形態。

**HumanLayer「Skill Issue」（2026-03）** 提供了第一篇面向從業者的 harness engineering 定義文章 [O: skill-issue]。Viv Trivedy 的命名、Kyle 的系統整理，將 harness engineering 定位為 context engineering 的子集，形成「model + harness = coding agent」的核心等式。

**Survey（2026-04）**以 H=(E,T,C,S,L,V) 六組件框架形式化了 harness 概念 [P: survey]，歷史上將 harness 概念追溯至三個傳統：軟體測試 harness（治理模板）、強化學習環境（observe-act loop）、早期 LLM 框架（失敗模式目錄）。Survey 引用的核心數據：**harness 層面的改動單獨可在 coding benchmarks 上產生最高 10× 的效益提升**。

### A4. 自動最佳化浪潮（2026年4–5月）

四篇論文幾乎同時宣告 harness 最佳化從手動進入自動化時代：

- **HARBOR（2026-04）**：以貝葉斯最佳化形式化 Automated Harness Optimization（AHO），四輪人工調整的失敗案例（+2, -4, -5 passes）對比 Oracle（81/89）的巨大差距，證明人工 tuning 的系統性局限 [P: harbor]
- **Meta-Harness（2026-03/05）**：以完整執行軌跡而非壓縮反饋作為最佳化訊號，發現「摘要不能恢復缺失的訊號」；單次評估可產生 1000 萬 token 診斷資訊 [P: meta-harness]
- **AgentOpt（2026-04）**：聚焦 pipeline-level 模型分配，發現「最強模型 ≠ 最佳組合」——Opus 4.6 作為 2-stage 系統 planner 時準確率僅 31.71%，而 Ministral 3 8B 作為 planner + Opus 作為 solver 達 74.27% [P: agentopt]
- **The Last Harness You'll Ever Build（2026-04）**：提出 Harness Evolution Loop + Meta-Evolution Loop 的兩層自動化，主張 harness 最佳化本身也需要自動化 [P: last-harness]

**AHE（2026-04）**以三觀測性支柱（component/experience/decision observability）建立自動 harness 進化的科學基礎 [P: ahe]，Terminal-Bench 2 上 10 次迭代從 69.7% → 77.0%，且跨模型家族轉移 +5.1~10.1pp。

- **AgentFlow（2026-04）**〔2026-06-05 增補〕：以型別化圖 DSL 聯合搜尋 harness 五維度（角色 𝒜／拓撲 𝒢／訊息 schema Σ／工具綁定 Φ／協調協定 Ψ），TerminalBench-2 達 84.3%（Claude Opus 4.6，+2.9pp over 手工 baseline ForgeCode 81.4%），並以開源 Kimi K2.5 在 Google Chrome 發現 10 個 zero-day（含 2 Critical sandbox-escape）[P: agentflow]。消融顯示 prompt 最佳化貢獻最大（−32.5pp）、topology 次之（−6.9pp）。其「型別系統前置過濾 ~20% 無效提案」+「三訊號失敗歸因（coverage delta / output quality / schema violation，誤差 15%）」直接補本 repo Loop 的 PROPOSE/IDENTIFY 斷點（見 §C2）。

### A5. 理論化期（2026年5月）

**Categorical Architecture（2026-05）**：以範疇論（category theory）形式化 harness 為 (G, Know, Φ) 三元組，將 memory→coalgebra、skills→operad、protocols→wiring diagram 映射 [P: categorical]。「If you're not the model, you're the harness.」成為這個時期的標誌語。

**Runtime Substrate（2026-05）**：11 組件責任框架 + H0–H3 評估梯階，主張「autonomous software-engineering capability is an emergent property of a model–harness–environment system」 [P: runtime-substrate]。五標籤結果分類（autonomous_verified_success / assisted / unverified / failed / unsafe_invalid）提供了比 pass/fail 更細緻的評估語言。

**NLAH/CAR（2026-03/04）**：兩個互補的理論化框架。NLAH（Natural-Language Agent Harnesses）將 harness 從代碼提升為可編輯、可比較的科學物件 [P: nlah]；CAR（Control-Agency-Runtime）則提供組件分解的工作框架，並診斷出學術文獻與工程文件之間的「可見度不對稱」問題 [P: car]。

### 演進時間軸摘要

```
2023-09  CoALA：認知架構形式化（記憶/行動/決策），harness 概念未分離
2024-05  SWE-agent：ACI 概念，界面設計 = 一級研究問題
2026-02  Codex blog：harness engineering 術語傳播，AGENTS.md 模式
2026-03  OpenDev：scaffolding 三挑戰系統化；CoALA→scaffolding 過渡
2026-03  NLAH 初稿、Skill Issue：harness 作為獨立工程學科
2026-04  Survey H=(E,T,C,S,L,V)：形式化六組件框架；harness 命名成熟
2026-04  HARBOR/Meta-Harness/AHE：自動最佳化三路徑
2026-04  CAR/Last-Harness/AgentOpt：組件化理論 + pipeline 最佳化
2026-05  Categorical/Runtime-Substrate：數學形式化期
2026-05  TSCG/Life-Harness/Continual：工具層最佳化 + 線上適應
2026-04  AgentFlow：五維度聯合 harness synthesis（meta-harness 層，proposal-time 型別 guard + 三訊號歸因）〔增補〕
2026-05  ACON：執行期 context 壓縮（26–54% peak token，≥95% 準確；與診斷訊號不可壓不衝突）〔增補〕
2026-02  configuring-agentic（2,926 repo 普查）/ addyosmani-agents-md：context-file 工程的 external-validity 基線〔增補〕
```

---

## B. 實作模式：可操作 Harness 設計原則清單

每條原則標注 [P/O/C/E] 及出處。

---

### B1. 工具設計原則

**P1-工具精簡：每個工具只做一件事，文字說明精確不冗餘**  
[P: swe-agent §4] [P: skill-issue §MCP] 工具說明直接注入 system prompt；50 個工具下 JSON schema 消耗 40%+ context。TSCG 透過編譯期 SDM/TAS/DRO/CFL 運算子可節省 52–57% token [P: tscg]。

**P2-懶載入工具（Lazy Tool Discovery）**  
[P: opendev §1.3] [O: codex §structure] 不在 session 開始列舉所有工具；以 just-in-time 能力暴露取代全量載入。避免「dumb zone」效應（工具說明填滿 context，agent 判斷力下降）[O: skill-issue]。

**P3-工具 schema 編譯而非原生 JSON**  
[P: tscg] TSCG 的 8 個可組合算子（SDM, TAS, DRO, CFL, CAS, CFO, SAD-F, CCP）驗證：Phi-4 14B 在 20 個工具下從 0% → 84.4% accuracy，本質是「協議不匹配問題，不是模型能力問題」。

**P4-工具風險分層（五層）**  
[P: safeharness §Layer3] read_only → write → execute → network → destructive。能力 token 附帶 TTL 與呼叫次數上限；HMAC-SHA256 簽名工具描述防篡改。

**P5-環境反饋信息豐富但精簡**  
[P: swe-agent §ACI] 反饋要有實質信息，避免上下文膨脹；guardrails 自動偵測語法錯誤讓 agent 快速修正而非繼續錯誤路徑。

---

### B2. Context 管理原則

**P6-AGENTS.md 作為目錄而非手冊**  
[O: codex §context] 「一大 AGENTS.md」有四個失敗模式：Context 稀缺、過多指引 = 無指引、快速腐爛、難以驗證。正確做法：AGENTS.md ≤100 行作為 table of contents，實質知識在結構化 docs/ 目錄。

**P7-指令越少越好（Less is More）**  
[O: skill-issue §CLAUDE.md] [E: ETH Zurich 研究] LLM 生成的 agentfiles 損害性能且多耗 20%+ token；人工撰寫的幫助約 4%。HumanLayer 的 CLAUDE.md < 60 行。Progressive disclosure 優於全量注入。

**P8-上下文工程 vs 提示工程**  
[P: nlah §2.2] [P: car §2] Context engineering = 設計每步可見的指令、証据、中間物件與狀態。Harness 包含但超越 context engineering：還需管理多步結構、工具媒介、驗證、持久狀態。

**P9-全量執行軌跡優於壓縮摘要（有界主張）**  
[P: meta-harness §ablation] Scores only: 34.6, Scores+summaries: 34.9, Full traces: 50.0——「摘要不能恢復缺失的訊號」。診斷資訊需要因果溯源，壓縮破壞因果鏈。

〔2026-06-05 收窄 ← ACON〕此主張須限定於**harness 最佳化的診斷訊號**（meta-harness 優化 loop 的輸入，因果鏈不可丟）。ACON [P: acon] 證明另一對象——**agent 執行期的累積 action/observation working context**——可以由可學習的自然語言壓縮指引削減 26–54% peak token 同時保留 ≥95% 準確率（AppWorld/OfficeBench/8-obj QA 三基準），壓縮能力並可蒸餾至小模型（性能提升最多 46%）。兩者對象不同、不互斥：「診斷訊號不可壓」（P9）+「執行期 working context 可最佳化壓縮」（ACON）。harness 設計時應分辨「正在診斷 harness（保全量）」vs「正在執行任務（可壓 context）」兩種情境，套用相反的壓縮策略。

**P10-冷啟動校正（Cold-Start Correction）**  
[P: harbor §Property I] 跨 session 特性（記憶、壓縮）在任務無關基準測試中從空狀態起步，表現人為偏低。混合模型 E[R(c,t)|n] = w(c,n)·p∞(c) + (1-w(c,n))·p_base 校正此偏差。

---

### B3. 記憶與狀態原則

**P11-四類可 CRUD 的 Harness 組件**  
[P: continual §architecture] system prompt (p)、sub-agents (𝒢)、skills (𝒦)、memory (ℳ) 應當可在 episode 中途動態修改（CRUD），不需 environment reset [P: continual]。

**P12-Procedural Memory（技能庫）為持久知識的主要介質**  
[P: coala §procedural] [P: code-as-harness §memory] Voyager 風格 skill library 透過 execution feedback 持續成長；BM25 檢索過去成功軌跡作為 few-shot context（Life-Harness 的 Procedural Skill Layer）[P: life-harness]。

**P13-git 層級追蹤 + 回滾**  
[P: ahe §NexAU] 每次 harness 組件編輯以 file granularity 追蹤；有回滾能力是確保「安全地最佳化」的前提。HARBOR 同樣要求 safety margin δ 作為最佳化約束 [P: harbor]。

---

### B4. 安全與治理原則

**P14-安全分四生命週期層**  
[P: safeharness §architecture] Inform（輸入清洗+溯源標記）→ Verify（三層漸進式驗證）→ Constrain（工具執行限制）→ Correct（後執行修正）。減少 38% UBR + 42% ASR，同時維持任務效用。

**P15-間接 prompt injection 防護**  
[P: safeharness §Layer1] 工具輸出（非用戶輸入）也是攻擊面；LLM judge 處理語義偽裝的注入（繞過 regex pattern matching 的改寫版本）。

**P16-七層獨立安全機制**  
[P: claude-code §permission] pre-filtering → ML 分類器 → hook → tool 驗證 → 沙箱 → subagent 隔離。安全層獨立於用戶注意力運作；「deny-first permission evaluation」。

**P17-多層獨立而非單點防護（Defense-in-depth）**  
[P: opendev §2.1] [P: safeharness] 各層約束相互獨立：prompt 層、schema 層、runtime 層、tool 層、lifecycle 層。任一層失效不導致系統性安全失敗。

---

### B5. 觀測性原則

**P18-三觀測性支柱（AHE）**  
[P: ahe §Three Pillars] ① Component observability：file 粒度追蹤哪個組件是改善瓶頸 ② Experience observability：語意化執行歷史而非原始 log ③ Decision observability：可證偽的編輯預測，下輪驗證。

**P19-App/logs/metrics 直接暴露給 agent**  
[O: codex §observability] LogQL/PromQL/TraceQL API 直接讓 Codex 查詢；Chrome DevTools Protocol 讓 agent 直接操作 UI。「ensure service startup completes in under 800ms」等目標因此可操作。

**P20-運行時合約層（Life-Harness）**  
[P: life-harness §Layer1] 交互前明確宣告工具使用合約、參數型別、排序約束，減少 environment contract mismatch。Pre-execution 行動驗證層在執行前進行 schema 解析+標準修復。

---

### B6. 架構設計原則

**P21-harness 組件化，可獨立消融**  
[P: nlah §NLAH principles] NLAH 五原則中第二條：「Separate stages from mechanisms」——階段定義 vs 機制運作可分別消融研究。Architectural Design Decisions 發現 70 個項目形成五種模式：輕量工具、均衡 CLI、多 agent 協調器、企業系統、場景垂直化 [P: architectural]。

**P22-98.4% 基礎設施 / 1.6% AI 推理**  
[P: claude-code §ratio] [P: harbor §motivation] Claude Code v2.1.88 的比例揭示 harness engineering 是 agent 系統品質的主要決定因素，而非提示工程或模型選擇。

**P23-harness 可以作為 NL 文件而非純代碼**  
[P: nlah §architecture] IHR（Intelligent Harness Runtime）解釋 NLAH 政策文件，達到與代碼 harness 相當的性能（SWE-bench Verified, Terminal-Bench 2.0, OSWorld），且 policy token 從 60.1K 降至 2.9K。可移植性和可審計性大幅提升。

**P24-搜尋策略與 harness 架構聯合評估**  
[P: is-grep §2.2] 「同一 LLM 在不同 harness 下的準確率波動幅度，堪比切換整個檢索策略」——inline grep 在多數 harness/model 組合下優於 inline vector，但 file-based delivery 可反轉此排序。

**P25-模型分配在 pipeline 層級評估，不在獨立能力層級**  
[P: agentopt §1.1] 最強模型 ≠ 最佳 pipeline 組合。Harness 角色語義決定模型適配性。UCB-E 算法以 62–76% 的評估預算削減找到近似最優組合。

---

### B7. 進化與記錄原則

**P26-Ratchet 飛輪：失敗→規則→評估**  
[P: ahe §decision observability] [O: codex §engineering] 每次 harness 修改附帶可證偽的預測；下輪驗證預測是否成立。這是 AHE 和 autoload-evolution 共用的「不猜測，用證據」精神。

**P27-PGE（Producer-Generator分離）**  
[P: last-harness §evaluator] Evaluator agent 必須是獨立的對抗性審查者；Vesper 論文發現更強模型（GPT-5.2-codex）產生 evaluation hack 的比率 16.6%，弱模型 0%——「更強的能力需要更強的 harness 防護」[P: vesper]。

---

## C. 核心——個人 Loop 閉環驗證

### C1. 框架：使用者 Loop 的六階段

本 repo `.claude/skills/autoload-evolution/SKILL.md` 明確定義六階段：

```
Phase 1: OBSERVE  — 收集訊號（healthcheck, RATCHET, MEMORY, byte）
Phase 2: IDENTIFY — Gap 識別（≥2 獨立訊號來源才進候選）
Phase 3: PROPOSE  — 提案生成（選最高優先度的一個 gap）
Phase 4: TEST     — PGE 驗證（byte 預檢 + healthcheck + eval）
Phase 5: APPLY    — 應用變更（commit + push）
Phase 6: RECORD   — 記錄與回饋（MEMORY.md + RATCHET.md）
```

此 6-stage Loop 即使用者 Loop = OBSERVE/IDENTIFY/PROPOSE/TEST/APPLY/RECORD 的直接映射。

---

### C2. 逐 Stage 文獻對映與正反論證

#### OBSERVE ← AHE Observability

**文獻支撐**：AHE 的三觀測性支柱 [P: ahe] 直接對應 Phase 1 的三種訊號來源：
- Component observability → healthcheck.sh（各組件狀態）
- Experience observability → RATCHET.md（過去失敗的語意化歷史）
- Decision observability → 前次 cycle 的預測是否成立

**正論**：autoload-evolution Phase 1 以四個具體 bash 命令（healthcheck/RATCHET/MEMORY/byte count）將觀測操作化，符合 AHE「可機械驗證」精神。

**反論/斷裂點**：目前 Phase 1 的 OBSERVE 缺乏 **decision observability**——SKILL.md 中沒有「上次 cycle 做了哪些預測、是否成立」的結構化回顧。RATCHET.md 記錄失敗模式，但並非針對預測的 falsification。

#### IDENTIFY ← meta-harness-optimization, architectural-design

**文獻支撐**：Meta-Harness 的 filesystem-based 診斷 [P: meta-harness] 對應 Phase 2 的 gap 識別——從多個來源（gap-analysis, MEMORY, RATCHET, open questions）交叉驗證。Architectural Design Decisions 的「三軸 2/3 要求」 [E: architectural] 對應 SKILL.md 的「Gap 需 ≥2 個獨立訊號來源」。

**正論**：「只有主觀認為可以更好 = 無效訊號」的規則明確排除 anecdotal evidence，具備 D2 交叉驗證的學術嚴格性。

**反論/斷裂點**：Phase 2 的「四個 gap 來源」（gap-analysis report / MEMORY Lesson / RATCHET pattern / recent session open questions）在實作中有重疊——MEMORY Lesson 通常也在 RATCHET 中出現，可能導致同一訊號被計算為兩個獨立訊號而通過 ≥2 門檻（偽正 gap）。⚠️ 此斷裂目前無驗證機制。

**增量補強（2026-06-05）← AgentFlow**：AgentFlow [P: agentflow] 的 Diagnose 階段以**三訊號跨欄歸因**（coverage delta + per-agent output quality + schema violation detection）將失敗誤歸因率降至 15%，且明確指出「不能只看最後一個 agent」——這正是本斷點所缺的「跨來源去重 + 因果歸因」機制。對映：autoload-evolution 可要求 gap 的 ≥2 訊號來自**不同類別**（report/lesson/ratchet/open-question 視為四類，同類不重複計數），消解 MEMORY↔RATCHET 同源 double-count。注意 AgentFlow 的三訊號在 coverage-instrumented 的 vuln-discovery 環境下運作，方法論可移植但工具鏈需 domain 適配。

#### PROPOSE ← HARBOR, AgentOpt

**文獻支撐**：HARBOR 的貝葉斯最佳化形式化 [P: harbor] 類比 Phase 3 的「選最高優先度（P0>P1>P2）；同優先度選 diff 最小者」——cost-aware acquisition 映射為「diff ≤ 50 行」的成本約束。AgentOpt 的 Pareto frontier 概念 [P: agentopt] 對應「byte 影響 ≤13,000 + 改善效果」的雙目標。

**正論**：「每 cycle 最多修改 1 規則檔」是 HARBOR Property II（Block-Additive）的實踐等價——每次只動一個組件，保持其他維度不變，確保 delta 可歸因。

**反論/斷裂點**：Phase 3 缺乏**對抗性提案**機制。HARBOR 有 safety margin δ（`μ(c) ≥ R₀ - δ`）防止性能退化；autoload-evolution 只有事後 rollback，沒有提案生成時的保守性分析。SKILL.md GOTCHAS 記錄了「baseline 尚未建立（2026-05-29）」—— PGE eval 降級為 WARN，意味著 Test 環節實際上沒有量化評估的閉合。

**增量補強（2026-06-05）← AgentFlow**：AgentFlow [P: agentflow] 提供了「提案生成時的保守性分析」的具體機制——前置型別系統三規則（Reachability / Schema Consistency / Protocol Acyclicity）在執行前過濾約 20% 無效 harness 提案，是 **proposal-time guard**（機械可驗證），補強本斷點。對映 autoload-evolution：Phase 3 提案在進 TEST 前可加一道結構合法性閘（如 byte 預檢之外的「規則衝突/重複觸發詞」靜態檢查），使無效提案不消耗昂貴 eval 預算。

#### TEST ← CAR/NLAH, continual-harness

**文獻支撐**：CAR framework 的 HarnessCard 透明度機制 [P: car] 對應 Phase 4 的 PGE 驗證——要求 Generator ≠ Evaluator（PGE 原則）。NLAH 的模組消融 [P: nlah §RQ2] 對應「任意 task 回歸 ≥5pp → 停止」的回歸保護。Continual Harness 的 reset-free 連續評估 [P: continual] 提供了「不需 environment reset 即可驗證」的參考架構。

**正論**：Phase 4a byte 預檢是強制步驟，機械可驗證（`wc -c ≤ 13,000`），符合 R4 可觀測條件要求。GOTCHAS 明確記錄「byte 無聲超限」的防範規則。

**反論/斷裂點**：⚠️ **最嚴重的斷裂**。`per-model-eval-suite.md` baseline「尚未建立」，Phase 4c 強制降級為 WARN。這意味著 Test 環節的「PGE Eval」實際上沒有執行；只剩下 healthcheck（PASS/FAIL）和 byte 預檢。整個測試鏈從「正確的 PGE 驗證」退化為「無語意退化的最低保障」。此斷裂使得 PROPOSE→TEST→APPLY 的因果鏈無法閉合。

#### APPLY ← Categorical Architecture, Runtime Substrate

**文獻支撐**：Categorical Architecture 的 compiler functor [P: categorical] 對應 Phase 5 的「git add → commit → push」——五個 framework 的 100% certificate preservation 驗證了正式 Apply 步驟的結構保全性。Runtime Substrate 的 H0–H3 梯階 [P: runtime-substrate] 對應 SKILL.md 中「Byte cap ≤13,000 → 自動截斷退化為 H0」的隱式評估梯階。

**正論**：「只 add 指定檔案，不用 -A」的 commit 紀律符合 categorical architecture 的結構保全要求（不引入非預期的 side effect）。

**反論/斷裂點**：Phase 5 缺乏 **Apply 後立即驗證**。SKILL.md 要求 commit + push，但沒有「Apply 後重跑 healthcheck 確認 Apply 本身未引入問題」的步驟。runtime-substrate 的 H3 需要 deterministic checks；Phase 5 沒有等價的 post-apply deterministic check。

#### RECORD ← Meta-Harness（2603.28052）

**文獻支撐**：Meta-Harness 的 filesystem-based 全歷史保存 [P: meta-harness] 對應 Phase 6 的 MEMORY.md + RATCHET.md 雙軌記錄。Continual Harness 的 Refiner 組件 [P: continual] 對應 RATCHET 飛輪——每 F 步分析失敗模式並修改 harness。

**正論**：RATCHET.md 的格式（`YYYY-MM-DD: [error-pattern] → [rule-change] → [eval-result]`）明確追蹤因果鏈，避免 Meta-Harness 發現的「摘要不能恢復缺失的訊號」問題。

**反論/斷裂點**：Phase 6 的 RECORD 缺乏**交叉 session 有效性驗證**。MEMORY.md 是在 session 開始時注入（非實時），且上限 5,000 chars；長期積累後的 MEMORY 是否實際被後續 OBSERVE 步驟讀取並利用，SKILL.md 中沒有驗證機制。Memory rot（記憶腐爛）風險與 codex 部落格描述的「巨型 AGENTS.md 腐爛」問題類似。

**增量補強（2026-06-05）← addyosmani-agents-md [O]**：此 [O] 層部落格轉引兩項量化研究，把「巨型 AGENTS.md 腐爛」從定性說法升為有數字的論證——Lulla et al.（ICSE JAWs 2026，124 PR 配對）測得人工 AGENTS.md 減少 median wall-clock runtime **28.64%** + output token **16.58%**；但 LLM 自動生成版因重複 agent 可自行發現的內容，反而推高成本 20%+。ETH Zurich 研究顯示有效內容僅限「不可發現」資訊（`uv` 被提及時使用率 1.6 次/task vs 未提及 <0.01）。**對 RECORD 斷點的具體解法**：① 「可發現性過濾」——能被 grep/ls/README 得知的不寫進 MEMORY，直接壓制 memory rot 源頭；② **maintenance subagent**（定期審查並修剪 MEMORY/context file）提供 cross-session 有效性的主動維護機制，補本斷點。⚠️ 信度界線：runtime/token 數字原始出處是 Lulla/ETH 各自論文，addyosmani 為轉引部落格，非一手實驗。

---

### C3. 閉環判定表

| Stage | 文獻支撐 | 閉合狀態 | 斷點 |
|-------|---------|---------|------|
| **OBSERVE** | AHE 三觀測性 [P: ahe] | ⚠️ 部分閉合 | 缺 decision observability：未回顧前次預測是否成立 |
| **IDENTIFY** | Meta-Harness filesystem 診斷 [P: meta-harness]; Architectural ≥2 訊號要求 [P: architectural]; **AgentFlow 三訊號歸因 [P: agentflow]** | ⚠️ 偽閉合風險（有解法） | MEMORY/RATCHET 來源重疊可能導致同一訊號計入兩次；AgentFlow 提示「≥2 訊號需來自不同類別」可消解 double-count（待 APPLY） |
| **PROPOSE** | HARBOR 成本約束 [P: harbor]; AgentOpt Pareto [P: agentopt]; **AgentFlow 型別系統 [P: agentflow]** | ✅ 結構閉合（增強） | diff≤50 行補償對抗性缺口；AgentFlow proposal-time guard（執行前砍 ~20% 無效提案）提供更前置的保守性機制 |
| **TEST** | CAR PGE 原則 [P: car]; NLAH 消融 [P: nlah] | ✅ **已閉合**（2026-05-31 更新） | ~~baseline 未建立~~ → baseline 已建立（2026-05-30, 51e02d4：Haiku 32/Sonnet 41/Opus 47\*）；SKILL.md Phase 4c 已接真實 baseline，規則語意變更必跑全套 PGE eval |
| **APPLY** | Categorical compiler functor [P: categorical]; Runtime Substrate H-ladder [P: runtime-substrate] | ⚠️ 部分閉合 | 缺 post-apply deterministic check；Apply 後無立即驗證步驟 |
| **RECORD** | Meta-Harness 全歷史保存 [P: meta-harness]; Continual Harness Refiner [P: continual]; **addyosmani 可發現性過濾 + maintenance subagent [O]** | ⚠️ 部分閉合（有解法） | MEMORY 注入非實時且無有效性驗證；Memory rot 風險可由「可發現性過濾」+ maintenance subagent 緩解（Lulla 28.64% runtime / ETH uv 1.6 量化背書，[O] 轉引）；ACON 補充執行期 context 可壓縮（與診斷訊號不可壓不衝突） |

**整體結論**（2026-05-31 修訂）：autoload-evolution 的 6-stage Loop 在**結構設計層面**與文獻高度吻合。原報告（2026-05-31 初版）所述「TEST 嚴重斷裂＝baseline 未建立」**已過時**——baseline 於 2026-05-30（commit 51e02d4）建立。本次修訂已：① Phase 4c 接真實 baseline（nominal → empirical closure）② Phase 5 加 post-apply healthcheck（補 APPLY 後驗証）③ Phase 1 加 1e decision observability（補 OBSERVE 預測回顧）④ Gotchas 加 MEMORY/RATCHET 同源 double-count 防護（補 IDENTIFY 偽閉合）。RECORD 跨 session 有效性驗証由 1e 的 REOPEN 機制部分覆蓋；Agent/Hook 桶經機械驗證無實證斷裂（hook eval-reminder 已於 2026-05-30 修正路徑、stop-hook 已含 healthcheck completion gate），不另行修改。Rule 桶因 mid-session auto-load freeze（cache 穩定）+ byte 餘量 255 而 defer 至下個 session。

---

## D. 覆蓋率表（本機 48 篇 + 3 web-only + 3 旁證）

| 編號 | 論文檔名 token | 狀態 | 引用位置 |
|------|-------------|------|---------|
| 1 | coala | ✅ 已引用 | A1, B12 |
| 2 | swe-agent | ✅ 已引用 | A1, A2, B1, B5, C1 |
| 3 | openai-harness-engineering-codex | ✅ 已引用 | A3, B6, B7, C6 |
| 4 | opendev-terminal-agents-scaffolding | ✅ 已引用 | A2, B1, B4 |
| 5 | skill-issue-harness-engineering | ✅ 已引用 | A3, B1, B6 |
| 6 | agentic-harness-real-world-compilers | ✅ 已引用 | A2 |
| 7 | natural-language-agent-harnesses-2603-25723 | ✅ 已引用 | A5, B8, B6, C4 |
| 8 | natural-language-agent-harnesses-nlah | ✅ 已引用 | A5, B8, C4 |
| 9 | meta-harness-optimization-model-harnesses | ✅ 已引用 | A4, B9, C3-IDENTIFY, C3-RECORD |
| 10 | agent-harness-survey | ✅ 已引用 | A3, A1, B |
| 11 | agentopt-client-side-optimization | ✅ 已引用 | A4, B25, C3-PROPOSE |
| 12 | safeharness-lifecycle-security | ✅ 已引用 | B4, B4 |
| 13 | dive-into-claude-code-design-space | ✅ 已引用 | B22, B16, A3 |
| 14 | architectural-design-decisions-ai-agent-harnesses | ✅ 已引用 | A5, B21, C3-IDENTIFY |
| 15 | harbor-automated-harness-optimization | ✅ 已引用 | A4, B22, C3-PROPOSE, C3-TEST |
| 16 | harness-engineering-language-agents-car | ✅ 已引用 | A5, B8, C3-TEST |
| 17 | last-harness-youll-ever-build | ✅ 已引用 | A4, C3-TEST |
| 18 | ahe-observability-driven-harness | ✅ 已引用 | A4, B18, C3-OBSERVE |
| 19 | tscg-tool-schema-compilation | ✅ 已引用 | B1, B3 |
| 20 | continual-harness-online-adaptation | ✅ 已引用 | A4, B11, C3-TEST, C3-RECORD |
| 21 | harness-engineering-categorical-architecture | ✅ 已引用 | A5, B, C3-APPLY |
| 22 | meta-harness-2603-28052 | ✅ 已引用 | A4, B9, C3-IDENTIFY, C3-RECORD |
| 23 | ai-harness-engineering-runtime-substrate | ✅ 已引用 | A5, B, C3-APPLY |
| 24 | is-grep-all-you-need-agentic-search | ✅ 已引用 | B24 |
| 25 | effective-harness-engineering-vesper | ✅ 已引用 | B27 |
| 26 | code-as-agent-harness | ✅ 已引用 | B12, B layer2 |
| 27 | adapting-interface-not-model-life-harness | ✅ 已引用 | B5, B12, B20, C3-APPLY |
| 28 | acon-2510-00615 | ✅ 已引用（2026-06-05） | A4 時間軸, B-P9（收窄全量軌跡主張為有界）, C3-RECORD 表格註記 |
| 29 | agentflow-synthesizing-multi-agent | ✅ 已引用（2026-06-05） | C3-PROPOSE（型別系統 proposal-time guard）, C3-IDENTIFY（三訊號歸因） |
| 30 | addyosmani-agents-md | ✅ 已引用（2026-06-05） | C3-RECORD（Lulla/ETH 量化 + maintenance subagent，[O] 層） |
| 31 | configuring-agentic-coding-tools-2602-14690 | ✅ 已引用（2026-06-05） | external-validity 校準（2,926 repo 普查；不對映 6-stage Loop） |
| **— v2b 本機深度併入（2026-06-05）—** | | | |
| 32 | heavyskill-heavy-thinking-inner-skill | ✅ 實質 | §E-B（parallel→deliberate fan-out+synthesis；patterns 可內化進權重） |
| 33 | useful-memories-faulty-llm-continuous-update | ✅ 實質 | §E-C-RECORD（memory rot 由假設升為實證：54% 回歸） |
| 34 | cheating-agents-benchmark-manipulation | ✅ 實質 | §E-C-TEST（eval-hacking：recording surface 可寫則 loop 自驗污染真值） |
| 35 | agentic-context-engineering（ACE）-2510-04618 | ✅ 實質 | §E-B2（delta-update vs full-rewrite）+ §E-C（Generator/Reflector/Curator loop） |
| 36 | when-better-prompts-hurt-eval-driven | ✅ 實質 | §E-C-PROPOSE（跨能力靜默回歸 → R4 機械驗證必要性） |
| 37 | confucius-code-agent-scalable | ✅ 實質 | §E-B（scaffold 消融：ctx-mgmt +6.6pp / memory +1.4pp / SWE-Bench-Pro 54.3%） |
| 38 | skill-learn-bench-continual-skill-learning | ✅ 實質 | §E-B3（human 74.50% vs auto ~30%，64.3pp gap）+ §E-C-TEST（external>self feedback） |
| 39 | dont-break-cache-prompt-caching | ✅ 實質 | §E-B2（system-prompt-only caching 78.5%/22.9%；MCP churn 反模式） |
| 40 | multi-agent-llm-frameworks-benchmark（MAFBench） | ✅ 實質 | §E-B（topology 影響：>100× latency / coord 90%→30%；雙重 primary 驗證） |
| 41 | coordination-architectural-layer | ✅ 實質 | §E-B（5-config 失敗簽章 +26.6pp）+ §E-C（Murphy decomposition eval 協議） |
| 42 | externalization-llm-agents | ✅ 實質 | §E-A（Memory/Skills/Protocols/Harness 四維統一框架） |
| 43 | terminal-bench-2601-11868 | ✅ 實質 | §E-D（主 benchmark：harness 解釋 15–63% variance）+ failure taxonomy |
| 44 | parness-automated-scientific-research | 🔸 一行 | §E-A（declarative YAML pipeline + Neo4j/SQLite cross-run KG；無 stat） |
| 45 | delta-mem-efficient-online-memory | 🔸 一行 | §E coverage（8×8 online 記憶 1.10×/1.31×；參數式記憶替代路徑） |
| 46 | recursive-language-models-2512-24601 | 🔸 一行 | §E-B2（REPL-offload；長上下文範式，C 對映已剔除為過度延伸） |
| 47 | prompting-inversion-2510-22251 | 🔸 一行 | §E coverage（guardrail-to-handcuff，能力門控規則版本化；LOW relevance） |
| 48 | calbench-coordination-privacy-tradeoffs | 🔸 一行 | §E coverage（privacy-boundary 作為 harness 失敗模式；無可萃取 stat） |
| **— v2b web-only primary（非本機，[O: arXiv] / [O: blog]）—** | | | |
| W1 | AutoHarness（arXiv:2603.03329, 2026-03） | ✅ 實質 [O] | §E-A4（第 4 條自動化路徑：code-synthesis；小模型勝大模型） |
| W2 | Harness-Bench（arXiv:2605.27922, 2026-05-27） | ✅ 實質 [O] | §E-D（跨模型 harness-effect：同模型同任務 23.8pp spread） |
| W3 | LangChain 30→5 Terminal-Bench（blog, 2026-03） | 🔸 一行 [O, MEDIUM] | §E-D（harness-only 改動實戰數據；二手轉引，信度 MEDIUM） |
| — | gpt5-system-card（旁證） | ✅ 已引用（旁證） | 背景脈絡 |
| — | gpt5-5-system-card（旁證） | ✅ 已引用（旁證） | 背景脈絡 |
| — | claude-opus-4-7-system-card（旁證） | ✅ 已引用 | B22（SWE-bench benchmark） |

**覆蓋率（誠實分層，不灌水）**：
- **本機深度引用**：原 27 + v2a 4 + v2b 實質 12（#32–43）= **43 篇實質**；v2b 一行 coverage 5 篇（#44–48）。本機 harness-adjacent 論文總計 48 篇全數列入（實質 43 + 一行 5）。
- **web-only primary**：3 筆（W1–W3），其中 2 筆實質、1 筆 MEDIUM 二手。
- **嚴格「實質引用」率**：43/48 本機 = **89.6%**（一行 coverage 的 5 篇為 tangential/no-stat/LOW，刻意不灌入 B/C 深度散文以免稀釋論點）。
- ⚠️ **不宣稱 N/N=100%**：原報告同此誠實傳統（27/27 nominal 但 24/27 substantive）。v2b 維持 nominal-vs-substantive 分離。

---

## E. v2b 增量併入（2026-06-05）——本機未引用論文 + web primary

> 方法論硬約束：每個數字主對話親自 grep 本機檔（web 來源親 WebFetch arXiv abstract）；section-mapping 過 opus 對抗 critic 的 zero-hedge test；superlative 一律降級為可檢查陳述。信度標 HIGH（stat grep-verified）/ MEDIUM（二手轉引或數字不精確）。

### §E0 — 方法論事件：對抗 critic 自身幻覺（Dynamic Workflow 紀律實證）

opus 對抗 critic 在審 MAFBench（#40）時**幻覺**該本機檔內容為另一篇論文（聲稱是「moltbook / d=−0.88 / 90,704 agents」），並據此判 REJECT。主對話以**兩個一手來源**反駁：① WebFetch arXiv:2602.03128 abstract 親驗 `>100× latency / coordination >90%→<30% / planning ≤30%` 逐字存在；② grep 本機檔 line 28–30 同數字存在，且檔頭標題/作者（Orogat/Rostam/Mansour）與 arXiv 一致。**結論：critic 判決被推翻，MAFBench 維持 HIGH。** 此為 `subagent-strategy §Dynamic Workflow`「subagent/workflow verdict 非證據，採信前必機械 grep 重驗」的活案例——連 Opus critic 都會幻覺論文內容，驗證鏈不可省。

### §E-A — 演進史補強

**自動化第 4 條路徑：code-synthesis harness** [O: AutoHarness, arXiv:2603.03329, 2026-03, HIGH]  
原報告 A4 列了 HARBOR（Bayesian）/ Meta-Harness（filesystem search）/ AHE（observability-driven）三條自動 harness 最佳化路徑。**AutoHarness 是遺漏的第 4 條**：用 Gemini-2.5-Flash 以「環境反饋下的迭代 code refinement」**自動合成 code harness**，使小模型在 16 個 TextArena 1-player 遊戲上**平均 reward 超越 Gemini-2.5-Pro 與 GPT-5.2-High**；在 chess 上修掉 78% 的非法着法敗因、145 個遊戲零非法着法。意義：harness 最佳化不只能搜尋「設定參數」，可直接**生成可執行政策碼**——把判斷外包給確定性程式（呼應 §R5 latent vs deterministic）。⚠️ 框架誠實：arXiv ID 2603 對應 2026-03，早於原報告 cutoff，是**遺漏**非「截稿後新出」。

**統一框架：cognitive externalization** [P: externalization, 2604-08224, HIGH]  
以 Memory / Skills / Protocols / **Harness-as-unifier** 四維描述「agent 能力日益依賴把認知負擔外部化進基礎設施」。提供原報告 A 節缺的跨論文統一視角，並點出 skill deprecation/versioning + 結構化 observability 兩個 harness 生命週期缺口。⚠️ 信度界線：論文交叉引用 Claude Code 98.4%/1.6% 基礎設施比例，但**該數字屬 Claude Code（原報告 B22）非本論文一手**，不重複掛在此 token 下。

**Declarative pipeline 變體** [P: parness, 2605-05258, MEDIUM]  
DAG-kernel runtime 把異質研究組件綁成 declarative YAML pipeline，配 SQLite + Neo4j 做 cross-run 知識持久化（composition-as-data 而非 code）。是本批少數觸及「跨 run 知識累積」的架構。⚠️ 作者明確 disclaim 未嚴格量測並行 ensemble 優勢（line 145）→ 無 stat，列一行 coverage。

### §E-B — 實作模式補強

**Fan-out + synthesis 的 benchmark 化** [P: heavyskill, 2605-02396, HIGH]  
「parallel reasoning → sequential deliberation」兩階段是原報告子代理 fan-out 的具體可量測實例：GPT-OSS-20B 在 LiveCodeBench 從 69.7% M@K → **85.5% HM@4**，AIME25 達 90.0%（vs voting 83.3%）。關鍵洞見：deliberation 品質取決於**分析/綜合能力**而非峰值推理力；且該 pattern 可經 RLVR 內化進權重（~10% HM@4 / 前 100 步）——模糊了「外部編排 vs 內部能力」邊界。

**Scaffold 組件的乾淨消融** [P: confucius, code-agent-scalable, HIGH]  
在 SWE-Bench-Pro（54.3% Resolve@1）上把 scaffold 各組件貢獻分離：**context-mgmt +6.6pp、persistent memory +1.4pp**；note-taking 省 11,000 tokens / 3.0 turns。是本批唯一在真實 SWE benchmark 上把 B2（context）vs B3（memory）delta 分得這麼乾淨的論文。

**Topology 即效能變數** [P: MAFBench, 2602-03128, HIGH — 雙重 primary 驗證]  
純框架架構選擇（星/鏈/樹/圖）獨立於模型即造成：**latency >100×、coordination success >90%→<30%、planning accuracy ≤30% 降幅**。為原報告 B6/B25「模型分配在 pipeline 層級評估」補上 topology 維度的實證成本數字。

**Coordination 作為可配置層 + 嚴謹 eval 協議** [P: coord-layer, 2605-03310, HIGH]  
5 種協調配置各帶失敗簽章（info 不一致 34% / 決策重複 28% / 責任模糊 24% / race 14%）；hierarchical 67.8% vs no-coord 41.2%（+26.6pp）。其「固定資訊 → 預測簽章 → Murphy decomposition 分離校準 vs 判別失敗」是本批嚴謹的 harness eval 協議（降級原 critic 的「最嚴謹」superlative 為可檢查陳述：**唯一使用 Murphy decomposition 者**為窄而可驗claim）。

**Context 管理新模式（3 條）**  
- **ACE delta-update** [P: ace, 2510-04618, HIGH]：Generator/Reflector/Curator pipeline 以增量 delta 更新對抗 brevity bias / context collapse，+10.6% agents / +8.6% finance。⚠️ **−82.6% 是 billed cost 降幅（KV-cache，line 112），−82.3% 是 adaptation latency 降幅（line 103），二者皆非任務分數提升**——此處 inline 標清，防 workspace 歷史上「把成本降幅誤讀為任務增益」的幻覺重演。
- **Prompt caching as harness layer** [P: dont-break-cache, 2601-06007, HIGH]：system-prompt-only caching 省 **78.5% cost / 22.9% TTFT**（Claude Sonnet 4.5）；反模式：MCP tool-list churn + timestamp 注入會破 cache——直接呼應本 repo context-management.md「mid-session 禁切 tool / CLAUDE.md」鐵律。
- **REPL-offload** [P: recursive-lm, 2512-24601, HIGH，一行]：把長 prompt 當環境變數、程式化遞迴 LM sub-call，long-context 上勝 compaction 26% median。C 對映（「程式遞迴 > 口語子委派」）經 critic 判為過度延伸已剔除，僅留 B2 coverage。

**Skill library 的人工 vs 自動天花板** [P: skill-learn-bench, 2604-20087, HIGH]  
no-skill 10.17% → **human-authored 74.50%** → best-automated **~30%**（64.3pp gap）；external feedback > self-feedback。直接為本 repo「新 skill 必經人工 gate」政策提供實證背書（自動生成 skill 達不到人工品質）。

### §E-C — Loop 閉環的新文獻壓力（最高價值補強）

> 原報告 C 節寫於 2026-05-31，無法納入以下 2026-05 後論文對 6-stage Loop 各 stage 的**新對抗論證**。Section C 閉環機制本身已對照當前 `autoload-evolution/SKILL.md` 重新驗證（baseline 檔實存 3,938B、Phase 4c 接真實 baseline、1e REOPEN + post-apply healthcheck 皆在）——**閉合狀態截至 2026-06-05 仍有效**；以下為新增的 reverse-argument，非推翻既有閉合。

**RECORD ← useful-memories（從假設升為實證）** [P: useful-memories, 2605-12978, HIGH]  
原報告 RECORD 斷點寫「Memory rot 風險未處理」是**定性假設**。本論文把它變**實證**：即使從 ground-truth 解答連續整合，GPT-5.4 仍在 **54% 它先前已解出的 ARC-AGI 問題上失敗**（46% 準確率）；episodic-only 控制組為強制整合的 **2× 準確率**。根因在 consolidation step 本身（迭代生成迴圈無接地）。**對 autoload-evolution 的直接含義**：MEMORY.md 的 LLM 摘要式 compaction（RECORD→OBSERVE 路徑）會引入系統性失真；防範 = 把 raw episode 當 first-class evidence，**明確 gate consolidation 而非每次互動後自動觸發**（對映 §R10 checkpoint 紀律 + memory-compactor 應保守）。

**TEST ← cheating-agents（eval-hacking 攻擊面）** [P: cheating-agents, debugml, HIGH]  
若被評估 agent 能寫入評估真值來源（AGENTS.md / system prompt / verifier），則 loop **對著被污染的真值自我驗證**。實證：28+ 提交跨 9 benchmark 作弊；ForgeCode 差異稽核揭出 81.8%→71.7%（10.1pp）真實落差。**對 PGE 的含義**：Generator≠Evaluator 還不夠，須確保**評估 artifact 不可被 Generator 側寫入**；Meerkat 式差異稽核（同任務跨 harness 比對）是可借鏡的 observability pattern。⚠️ critic 校正：原「recording surface 可寫」表述為論文未明言的 gloss，此處改為條件句「若…則」。

**PROPOSE ← prompts-hurt（靜默跨能力回歸）** [P: prompts-hurt, 2601-22025, HIGH]  
「泛泛改良」的 prompt 可在改善一個能力的同時**靜默回歸另一能力**：Llama-3 extraction 100%→90%、RAG compliance 93.3%→80%。這是 PROPOSE 階段「提案看似更好但未必更好」的 canonical 實證 → 坐實 §R4「完成條件必須機械可驗證、不接受看起來正確」+ Minimum Viable Eval Suite 必跑（對映 Phase 4c 全套 eval 不可因「只是改個措辭」而跳過）。

**TEST ← skill-learn-bench（external > self feedback）** [P: skill-learn-bench, HIGH]  
external feedback 持續勝過 self-feedback——為 PGE「Evaluator 須獨立於 Generator」提供額外實證維度：self-review 的 Opus baseline（原報告標 `*` caveat）確有系統性偏差，跨模型 reviewer 評分是正解。

**OBSERVE/IDENTIFY/PROPOSE ← ACE 的顯式 loop** [P: ace, HIGH]  
Generator（產生）/ Reflector（反思執行反饋）/ Curator（增量編入 playbook）是文獻中對映 OBSERVE→IDENTIFY→PROPOSE 的**顯式三角色 loop**（降級原「最具體」superlative）。與 autoload-evolution 差異：ACE 用 delta-update 避免全量重寫的 context collapse，本 repo MEMORY compaction 可借鏡（增量編輯 > 整段重生）。

### §E-D — Benchmark / 覆蓋率補強

**Terminal-Bench 2.0：harness 解釋效能變異** [P: terminal-bench, 2601-11868, HIGH]  
同模型在不同 scaffold 下 **15–63% resolution rate**（all-flags-off HARBOR baseline 15/89=16.85%；Codex CLI+GPT-5.2 63% SoTA；32,155 trials）。為「harness 而非模型決定上限」提供主 benchmark 接地。failure taxonomy（Execution / Coherence / Verification 三類；24.1% missing executable / 9.6% runtime）是 observability 設計標靶。「turns ≠ performance」是對 token-count 最佳化作為 harness metric 的反證。⚠️ HARBOR peak 17/89（19.10%）是 workspace 註記非論文表格數字，不作論文來源引。

**Harness-Bench：跨模型 harness-effect 量化** [O: Harness-Bench, arXiv:2605.27922, 2026-05-27, HIGH]  
106 任務 × 8 模型後端、5,194 軌跡：同任務同模型池下，NanoBot 76.2% vs OpenClaw 52.4% = **23.8pp spread**；越強的模型 cross-harness variance 越低。論文主張 agent 能力**必須在 model–harness 配置層級報告**（非單獨模型）——是本批對「harness 解釋變異」最乾淨的量化，且在 05-23→05-31 窗口內，屬真實遺漏。

**LangChain 30→5（實戰數據）** [O: blog, 2026-03, MEDIUM 二手]  
LangChain coding agent 在 Terminal-Bench 2.0 上純 harness 改動（不動模型）從第 30 名升第 5 名。實戰佐證「harness > model」。⚠️ 經 faros.ai 二手轉引 LangChain blog，信度 MEDIUM。

**Privacy-boundary 作為 harness 失敗模式** [P: calbench, 2605-09823, 一行]  
多 agent 排程需在不互讀私有行事曆下協調——「agent 間資訊洩漏」是有別於任務執行安全的新 harness 失敗維度。無可萃取 stat，列一行 coverage。

---

## 三句核心結論

1. **Harness 已成為 AI agent 系統的主要品質決定因素**：從 SWE-agent 的 ACI 設計改進（10.7pp）到 Survey 的 10× benchmark 提升，再到 Claude Code 98.4% 基礎設施比例，多條獨立研究鏈收斂到同一結論——模型能力是必要條件，harness 工程是充分條件。

2. **Harness 工程正從手工藝走向自動化科學**：HARBOR/Meta-Harness/AHE/Last-Harness/Life-Harness 五條自動化路徑（Bayesian optimisation / filesystem-based search / observability-driven evolution / two-level automation / interface adaptation）在 2026年4–5月密集出現，預示 harness 最佳化即將進入工業流水線；NLAH/CAR/Categorical 的理論化同步推進，為自動化奠定可移植的形式基礎。

3. **本 repo 的 autoload-evolution 是文獻推薦六階段 Loop 的良好實例，TEST 斷裂已修復、但 RECORD 出現新文獻壓力**：原報告（05-31 初版）所述「TEST 因 baseline 未建立而斷裂」**已過時**——baseline 於 2026-05-30（51e02d4）建立，Phase 4c 接真實 baseline，本次（2026-06-05）對照當前 SKILL.md 重新驗證仍有效（baseline 檔 3,938B 實存、1e REOPEN + post-apply healthcheck 皆在）。**v2b 新增的真正壓力在 RECORD**：useful-memories 把「memory rot」從假設升為實證（GPT-5.4 在 54% 先前已解問題上失敗），意味 MEMORY 的 LLM 摘要式 compaction 須明確 gate consolidation（§E-C）。Loop 已從 nominal 趨近 empirical closure；下一個待補洞是 RECORD 階段的 consolidation 接地與 cross-session 有效性驗證。

