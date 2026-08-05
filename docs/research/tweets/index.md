# tweets/INDEX.md

> Type: raw:corpus
> Harness-Layer: L4-knowledge
> **Type:** raw:tweet — 393 tweets；Claude Code / AI Engineering 技術 thread 歸檔  
> **Updated**: 2026-08-04 | **Authors**: 215 | **Files**: 393 .md（`ls research/tweets/*.md | grep -v -E '(INDEX|README)\.md' | wc -l` 實測）  
> **Query pattern**: BRAIN.md → 本表（Author / Topic）→ `<date>-@<handle>-<id>.md`  
> **Frontmatter**: canonical YAML（`url`/`author`/`handle`/`published`/`archived`/`type`/`stats`）；`type` ∈ {tweet, twitter-article, note-tweet, thread, twitter-video, daily-digest}
> **評分標準**：SCORING.md §3（與 §1 相同，A-E 五維 /10 加權）；整合狀態見各欄。

---

## 2026-07-31 gap-harvest 執行紀錄（首輪示範）

> 首次以「外部語料 → skill/rule 養分」為明確目標跑的收成批次，方法論見新 SKILL `gap-harvest`；合成報告 → `research/reports/2026-07-31-tweets-corpus-nutrient-synthesis.md`。24 篇高分（≥8.2）推文深讀分類：11 reinforces-existing／3 discard／10 refs-patch-candidate／0 new-skill-signal。以下 9 篇已實際落地為 refs 補丁（下方各主題表格的逐列 ✅ 同步為後續 gap-harvest 跑次待辦，本輪未逐列更新，不代表未落地——落地位置見下表）：

| 推文 | 落地位置 | 摘要 |
|------|---------|------|
| `2026-06-12-@nfcampos-517180.md` | `refs/error-handling.md`「Oracle 偏差排查案例」 | xlsx-corpus-bench 96% locale 誤判案例，補齊 `loop-engineering.md` §L4 原斷鏈 |
| `2026-07-19-@TaoMachina-226249.md` | `refs/graph-engineering.md` §G4 | 高風險 handoff 前 child 覆述理解的意圖偏差檢查 |
| `2026-07-03-@addyosmani-042327.md` | `refs/graph-engineering.md` §G4 + `refs/judgment-rubrics.md` §R7 | Handoff Contract 補 Budget/Tools&Permissions 欄；高自主三問 + 4 個委派反模式命名 |
| `2026-06-15-@addyosmani-594363.md` | `refs/judgment-rubrics.md` §R5c | Review 深度三變數（blast radius/存活時間/理解人數） |
| `2026-06-11-@PawelHuryn-549362.md` | `refs/model-profiles.md` §1 | 巢狀 sub-agent 1.63–1.84× 乘法開銷 caveat（信心：中，部分內容付費牆後） |
| `2026-06-09-@RLanceMartin-071163.md` + `2026-06-13-@servasyy_ai-597508.md` | `refs/harness-loop.md` RECORD 段 | 記憶品質 5 階段診斷（fail→investigate→verify→distill→consult），雙獨立來源三角驗證 |
| `2026-06-09-@mem0ai-233179.md` | `refs/harness-loop.md` RECORD 段 | JIT 引用重驗：用記憶前先重讀 citation 確認未過期 |
| `2026-07-02-@cyrilXBT-058492.md` | `refs/judgment-rubrics.md` §R3 | assessment-mode vs action-mode 邊界（使用者自言自語 ≠ 動作指令） |

**已知缺口（不靜默略過）**：本次未逐列把上方主題表格（Harness Engineering／CLAUDE.md-Rules／Memory 等）對應行的 🔵/📋 手動改成 ✅——留給下一輪 `gap-harvest` 執行時批次同步，目前以本節作為可查詢的替代索引。另有 4 篇（`elvissun-864954` Forced-Entropy／`wquguru-253843` overnight 摘要風格／`hanakoxbt-513286` compact 存活範圍與 skill body 截斷數字／`addyosmani-594363` 異質 reviewer 落地 review-hub）評為 refs-patch-candidate 但因信心中等或需先查證官方文件，本輪未套用，列入報告「待辦」而非略過。

---

## Author 索引（快速定位 · 篇數為實際檔案統計）

| Author | 篇數 | 主要主題 |
|--------|------|---------|
| [@trq212](#trq212-thariq) | 18 | Skill 設計·Session 管理·Prompt Caching·工具哲學·Dynamic Workflows |
| [@Mnilax](#mnilax) | 9 | 12-Rule Canon·Token 優化·CLAUDE.md 分析 |
| [@zodchiii](#zodchiii) | 8 | CLAUDE.md 框架·Hooks·Opus 4.8 配置 |
| [@stephzhan](#stephzhan-sequoia) | 8 | Agentic Engineering·Jaggedness·Software 3.0 |
| [@eng_khairallah1](#eng_khairallah1) | 8 | 實戰技巧合集·Prompt 架構·Slash Commands |
| [@bcherny](#bcherny-boris-cherny) | 8 | 官方技巧·Skill·隱藏功能·工作流自動化 |
| [@0x_kaize](#0x_kaize) | 6 | Skill 生態索引·Repo 精選 |
| [@karpathy](#karpathy-andrej) | 5 | Context Engineering·Goal-Driven·Agent Economy |
| [@sairahul1](#sairahul1) | 4 | Token 浪費·AI 工作流·Opus 4.8 |
| [@berryxia](#others)（各 1–4 篇）| 4 | Skills 2.0·中文解析 |
| [@Suryanshti777](#others) | 4 | 最佳實踐·Opus 4.7·AI 系統架構 |
| [其他作者](#others--生態資源)（各 1–3 篇）| 111 | 多主題 |

---

## Topic 索引（依主題分類）

| Topic | 代表 Tweets | 數量 |
|-------|-----------|------|
| [Harness Engineering](#harness-engineering) | akshay·SaitoWu·wsl8297·rohit4verse | 18 |
| [Graph Engineering](#graph-engineering) | 0xCodez·0xClodex·steipete·ericosiu | 7 |
| [Skill / AGENTS.md 設計](#skill--agentsmd-設計) | trq212·berryxia·Khazix0918·dotey | 22 |
| [Context / Token 優化](#context--token-優化) | Mnilax·DeRonin_·sairahul1·nateherk | 20 |
| [Memory / 記憶系統](#memory--記憶系統) | lxfater·aiedge_·Ni_luvya·BTCqzy1 | 12 |
| [CLAUDE.md / Rules](#claudemd--rules) | zodchiii·Mnilax·NainsiDwiv50980 | 15 |
| [Karpathy / stephzhan 原則](#karpathy--stephzhan-原則) | karpathy·stephzhan | 13 |
| [Boris / Thariq 官方技巧](#boris--thariq-官方技巧) | bcherny·trq212 | 19 |
| [Tools / MCP / Hooks](#tools--mcp--hooks) | MinLiBuilds·_avichawla·trq212 | 10 |
| [Workflow / Automation](#workflow--automation) | lxfater·cyrilXBT·garrytan | 10 |
| [Others / 生態資源](#others--生態資源) | 0x_kaize·polydao·GitTrend0x | 25 |

---

## Harness Engineering

| 日期 | Author | 核心主題 | 整合狀態 |
|------|--------|---------|---------|
| 2026-07-11 | @eng_khairallah1 | Loop Engineering 20 步路線圖：Done定義→外部化verifier→分層終止→state layer→人類checkpoint | 📋 → research/tweets/2026-07-11-@eng_khairallah1-565100.md |
| 2026-07-08 | @PrajwalTomar_ | Skill 蔓延三判準（overlaps/never-triggers/worse-version）+ before/after context 量化修剪 | 📋 → research/tweets/2026-07-08-@PrajwalTomar_-899896.md |
| 2026-07-19 | @TaoMachina | Agent OS：Deterministic Gate + Brain 記憶治理 + Human Mission Authority 治理層框架 | 📋 → research/tweets/2026-07-19-@TaoMachina-226249.md |
| 2026-07-18 | @sairahul1 | Loop over prompt：Slate CLI 可組合 agent Program（loop-as-job 概念與 Slate 產品推廣） | 🔵 |
| 2026-07-08 | @choopyplug1 | Boris Cherny Loop方法十步驟：goal/checker分離+STATE.md+worktree+MCP+accepted-change<50% | 📋 → research/tweets/2026-07-08-@choopyplug1-503774.md
| 2026-07-13 | @joon_h_lee | Fusion 架構：Fable 委派時機/約束式 brief 使成本降+分數升，Opus 晚期委派+插手重寫 | 📋 → research/tweets/2026-07-13-@joon_h_lee-173097.md
| 2026-07-08 | @addyosmani | Own the Outer Loop：Quality/Verdict/Answerability+三隱性成本 | 📋 → research/tweets/2026-07-08-@addyosmani-835916.md |
| 2026-07-08 | @Mnilax | 複製貼上 loop 模板：verifier+stop+state+worktree，7天實測數字 | 📋 → research/tweets/2026-07-08-@Mnilax-689957.md |
| 2026-07-07 | @keloneoneal | Loop engineering 框架：六原語+readiness score+11失敗模式目錄 | 📋 → research/tweets/2026-07-07-@keloneoneal-605379.md |
| 2026-07-01 | @0xCodila | Loop 三要件 verifier/state/stop；Karpathy AutoResearch；Bilevel 外層 loop 5x | 📋 → research/tweets/2026-07-01-@0xCodila-232639.md |
| 2026-07-07 | @albertgao | Loop engineering 實戰：orchestrator+programmer/reviewer，24票27h無人值守 | 📋 → research/tweets/2026-07-07-@albertgao-423939.md |
| 2026-03-17 | @rohit4verse | Harness SWE-bench +64% | 🔵 |
| 2026-03-25 | @JJEnglert | Claude Cowork 三層架構 | 🔵 |
| 2026-04-03 | @wsl8297 | Harness 五組件 92% 壓縮 | 🔵 |
| 2026-04-06 | @akshay_pachaar | Agent Harness 12 元件 | 🔵 |
| 2026-04-18 | @SaitoWu | Harness Engineering 定義 | 🔵 |
| 2026-05-04 | @nicbstme | Model-Harness-Fit 框架 | 🔵 |
| 2026-05-05 | @mindstudio | harness beats model | 🔵 |
| 2026-05-09 | @addyosmani | Harness Engineering 框架 | 🔵 |
| 2026-05-10 | @ShenHuang | Claude Code 9 個 Harness 元件 | 🔵 |
| 2026-05-10 | @dotey | AI Agent Harness 12 組件（譯）| 🔵 |
| 2026-05-11 | @freeman1266 | Harness 入門科普 | 🔵 |
| 2026-05-26 | @rohit4verse | swarm 架構 300 agents | 🔵 |
| 2026-05-26 | @yan5xu | Harness 螺旋三圈框架 | 🔵 |
| 2026-05-27 | @arvin17x | Harness 護城河 75%→95% | 🔵 |
| 2026-05-28 | @mfpiccolo | agent harness worker 架構 | 🔵 |
| 2026-05-30 | @EXM7777 | Eval loop 六步驟 Hermes | 🔵 |
| 2026-04-25 | @PawelHuryn | Compounding Agent 三原則 | 🔵 |
| 2026-05-11 | @PawelHuryn | Compounding Agent 三原則 | 🔵 |
| 2026-06-01 | @garrytan | Fat Skills/Thin Harness/Tokenmaxxing/Skillify — Foxconn 工廠反模式 | 🔵 |
| 2026-06-20 | @phosphenq | Loop Engineering: Build an AI That Codes While You Sleep（Automations+Sub-agents+Worktrees）| 🔵 |
| 2026-06-28 | @ArchiveExplorer | Harness/Loop 兩層模型；7 harness files × 5 loop steps；arXiv 2606.10209（91.6% vs 71%）；11 shortcuts agent fake done | 📋 → core.md+context-management.md |

---

## Graph Engineering

> 2026-07-18 @steipete 一句反問（「還在講 loop 還是已經換 graph 了？」）兩天內破 300 萬 views，引爆本波「Graph Engineering」術語熱潮；後續 @0xCodez／@0xClodex 長文把內容填實為 node/edge/fan-out/verifier 具體機制。**Turing Post FOD#159 事實查核**指出這波熱潮夾帶未經證實的外推宣稱（機構「獨立採用」、廠商「以 graph 取代 RAG」、具體百分比數字），本批 4 篇歸檔時已個別標注「原文宣稱，未經查證」，不作為可引用證據。

| 日期 | Author | 核心主題 | 整合狀態 |
|------|--------|---------|---------|
| 2026-07-18 | @steipete | 12 字原始貼文，引爆 Graph Engineering 術語熱潮（無技術內容） | 📋 → research/tweets/2026-07-18-@steipete-189132.md |
| 2026-07-20 | @0xCodez | Graph Engineering 14 步路線圖：node/edge 精確定義、schema contract、fan-out/fan-in diamond、router、verifier 三型、loop-until-dry dedup-against-seen、model tiering | 📋 → research/tweets/2026-07-20-@0xCodez-330317.md |
| 2026-07-21 | @0xClodex | Graph Engineering + Dynamic Workflows 7 步指南；Bun Zig→Rust 重寫案例（規模/工期未附來源）；與 @0xCodez 同批機制高度重疊 | 📋 → research/tweets/2026-07-21-@0xClodex-272354.md |
| 2026-07-22 | @ericosiu | Graph vs Loop 二分比喻（軌道 vs 引擎）；與 workspace 既有 `graph.md`／`loop.md` 分工吻合，外部獨立驗證 | 📋 → research/tweets/2026-07-22-@ericosiu-957131.md |
| 2026-07-27 | @0x_rody | Opus 5 graph engineering 成本配置：extraction low effort+cache 前綴 vs traversal high effort，effort 為 cache key 一部分不可 mid-session 切換 | 📋 → research/tweets/2026-07-27-@0x_rody-810178.md |
| 2026-07-25 | @undefinedKi | Graph Engineering 8 步落地指南：judge 先行+故意餵壞驗證、rulebook 單一事實來源、state on disk 可斷點續跑、雙盲互不可見審查者、成本分流檢查、昂貴操作單一 daemon 串行化（引 Bun Zig→Rust / Krieger Python→TS 真實遷移案例） | 📋 → research/tweets/2026-07-25-@undefinedKi-675775.md |
| 2026-07-24 | @AnatoliKopadze | Graph Engineering 全教學：fake-edge test 揪虛假依賴、diamond pattern（fan out/reduce/synthesize）、verifier 全新 context 隔離、三種破圖模式（context collapse/false independence/silent node failure）、anchors 拒絕被說服的真值錨點，附 5 組 Claude Code dynamic workflows 可直接貼上樣板 | 📋 → research/tweets/2026-07-24-@AnatoliKopadze-314331.md |

---

## Skill / AGENTS.md 設計

| 日期 | Author | 核心主題 | 整合狀態 |
|------|--------|---------|---------|
| 2026-07-07 | @BHolmesDev | 自建 LLM 知識庫五步驟：enrich-note+wiki skill+排程自動化 | 📋 → research/tweets/2026-07-07-@BHolmesDev-461170.md |
| 2026-03-17 | @trq212 | Skill 九分類框架 | ✅ → RESOLVER.md |
| 2026-03-26 | @berryxia | Skills 2.0 完全指南 | 🔵 |
| 2026-03-26 | @Khazix0918 | Superpowers 14 Skills | 🔵 |
| 2026-04-02 | @dotey | Skills Git+Symlink 版控 | 🔵 |
| 2026-04-22 | @0x_kaize | Skills 倉庫列表 | 🔵 |
| 2026-04-17 | @ClaudeCode_love | Claude Skills 67 選分類索引 + 導入順序（日文）| 🔵 |
| 2026-04-24 | @polydao | 1116 個 Skills 生態索引 | 🔵 |
| 2026-04-25 | @0x_kaize | 100 個 repo 完整索引 | 🔵 |
| 2026-05-03 | @nateherk | 100+ Skills 6 大實用技能 | 🔵 |
| 2026-05-04 | @zodchiii | Claude Skills 完全指南 | 🔵 |
| 2026-05-05 | @Mnilax | 247→23 Skills 篩選 | 🔵 |
| 2026-04-20 | @skill-authoring | → ai-articles/scored | ✅ |
| 2026-03-21 | @akshay_pachaar | .claude/ 資料夾解剖 | 🔵 |
| 2026-02-27 | @trq212 | 工具設計哲學 progressive disclosure | ✅ → refs/ |
| 2026-02-28 | @bcherny | /simplify /batch 新 Skill | 🔵 |
| 2026-04-27 | @zodchiii | CLAUDE.md 五段落框架 | 🔵 |
| 2026-04-22 | @eng_khairallah1 | Prompt 4 層架構 | 🔵 |
| 2026-04-24 | @eng_khairallah1 | 40 個 Slash Commands | 🔵 |
| 2026-04-26 | @eng_khairallah1 | 40 個通用 prompt 模板 | 🔵 |
| 2026-05-09 | @eng_khairallah1 | Managed Agents 7 步驟 | 🔵 |
| 2026-05-10 | @eng_khairallah1 | Context Engineering 課程 | 🔵 |
| 2026-04-29 | @elliotchen100 | 同事心智模型 32 技巧 | 🔵 |
| 2026-05-19 | @Mnilax | 9 個 slash command templates | 🔵 |
| 2026-06-01 | @hooeem | SkillOpt：validation gate+textual learning rate 自動進化 skill 文件 | 🔵 |
| 2026-06-27 | @trevin | Compound Engineering Update：skill-only 架構（移除 standalone agent）；/goal-ready unified plan；6h 無人工干預；cross-model adversarial review | 📋 → skill-design |

---

## Context / Token 優化

| 日期 | Author | 核心主題 | 整合狀態 |
|------|--------|---------|---------|
| 2026-07-27 | @hanakoxbt | Context 4 種失效模式（poisoning/distraction/confusion/clash）+ 刪除優先方法論；補充 compact 存活範圍（paths-scoped rules 不會從磁碟重注入）與 skill body 截斷上限（5000/25000 tokens）兩項未載明機制 | 📋 → research/tweets/2026-07-27-@hanakoxbt-513286.md |
| 2026-07-06 | @alex_prompter | 萃取強模型操作手冊移植便宜模型系統提示，陷阱題驗證 | 📋 → research/tweets/2026-07-06-@alex_prompter-181121.md |
| 2025-06-25 | @karpathy | Context Engineering 核心定義 | ✅ → context-management.md |
| 2026-02-19 | @trq212 | Prompt caching 五原則 | ✅ → context-management.md |
| 2026-03-20 | @_avichawla | KV caching 5x 推論加速 | 🔵 |
| 2026-04-09 | @0xKingsKuan | token 用量分析工具 | 🔵 |
| 2026-04-20 | @FinanceYF5 | Token 省錢工具集 | 🔵 |
| 2026-04-21 | @_avichawla | MCP token 陷阱 | 🔵 |
| 2026-04-23 | @HytidelLegend | Token 優化 80 方法 | 🔵 |
| 2026-05-01 | @Mnilax | 27% productive tokens 分析 | 🔵 |
| 2026-05-01 | @AYi_AInotes | Karpathy token 槓桿 | 🔵 |
| 2026-05-08 | @trq212 | HTML 取代 markdown 輸出 | 🔵 |
| 2026-05-12 | @DeRonin_ | $4200→$312 費用指南 | 🔵 |
| 2026-05-12 | @DeRonin_ | AI coding 帳單削減 80% | 🔵 |
| 2026-05-13 | @sairahul1 | 9 個隱性 token 浪費模式 | 🔵 |
| 2026-05-21 | @nateherk | Prompt caching 80/20 | 🔵 |
| 2026-05-23 | @Mnilax | 18 個 Claude 設定 $340→$87 | 🔵 |
| 2026-05-30 | @ellen_in_sf | 11 個免費 token 省量技巧 | 🔵 |
| 2026-06-01 | @0x_kaize | Opus 4.8 effort 分級 + fast mode + workflows token 指南 | 🔵 |
| 2026-05-31 | @Mnilax | Opus 4.8 四 effort 量化 | 🔵 |
| 2026-03-27 | @yanhua1010 | Token 省量三策略 | 🔵 |
| 2026-05-10 | @ashwingop | Contextmaxxing 品質決定效益 | 🔵 |
| 2026-05-10 | @sukh_saroy | Context engineering 6 支柱 | 🔵 |

---

## Memory / 記憶系統

| 日期 | Author | 核心主題 | 整合狀態 |
|------|--------|---------|---------|
| 2026-07-07 | @ataiiam | procedural/episodic/semantic 三型記憶 + Learning Containers | 🔵 |
| 2026-07-07 | @EXM7777 | 六階段 gate prompt：session 探勘→自我畫像→CLAUDE.md diff | 📋 → research/tweets/2026-07-07-@EXM7777-465089.md |
| 2026-03-27 | @techwith_ram | Agentic Memory 四類型 | 🔵 |
| 2026-04-09 | @Ni_luvya | Hermes 跨 session 記憶 | 🔵 |
| 2026-04-15 | @BTCqzy1 | Hermes Agent 記憶系統 | 🔵 |
| 2026-04-22 | @aiedge_ | 記憶三層系統 | 🔵 |
| 2026-04-23 | @lxfater | Hermes 郵件自動化 | 🔵 |
| 2026-04-23 | @cyrilXBT | Obsidian+Claude 知識系統 | 🔵 |
| 2026-05-07 | @anthropic | dreaming offline learning | 🔵 |
| 2026-05-13 | @lxfater | AI Agent 記憶系統拆解 | 🔵 |
| 2026-05-16 | @haopeng_uiuc | 記憶持續更新反而更蠢 | 🔵 |
| 2026-05-18 | @Phoenixyin13 | AI Agent 長期記憶工程反思 | 🔵 |
| 2026-05-29 | @aiedge_ | AI 致富三路線 | 🔵 |
| 2026-04-11 | @garrytan | Meta-Meta-Prompting 三層架構 | 🔵 |
| 2026-06-27 | @mvanhorn | Memory Is Quietly Making It Dumber：218→6 files；Skills-over-memory；Push vs Pull memory；CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 | 📋 → memory-design |

---

## CLAUDE.md / Rules

| 日期 | Author | 核心主題 | 整合狀態 |
|------|--------|---------|---------|
| 2026-01-02 | @bcherny | vanilla 設定哲學 | 🔵 |
| 2026-02-11 | @bcherny | 客製化設計目標 | 🔵 |
| 2026-04-27 | @zodchiii | CLAUDE.md 五段落框架 | 🔵 |
| 2026-05-07 | @vincemask | CLAUDE.md 8 條實戰 | 🔵 |
| 2026-05-09 | @Mnilax | Karpathy 4 規則盲點 + 12 條 | ✅ → refs/the-loop-best-solution.md |
| 2026-05-14 | @Mnilax | CLAUDE.md 73% 在說謊 | 🔵 |
| 2026-05-18 | @NainsiDwiv50980 | CLAUDE.md 錯誤防範系統 | 🔵 |
| 2026-05-19 | @shao__meng | 開發日誌提示詞 | 🔵 |
| 2026-05-27 | @zodchiii | CLAUDE.md 錯誤 + Hooks 修錯 | 🔵 |
| 2026-05-29 | @zodchiii | Opus 4.8 完整配置 | 🔵 |
| 2026-05-11 | @Mnilax | Hook 衝突三類型 34% 浪費 | 🔵 |
| 2026-04-04 | @MinLiBuilds | 8 個 Hooks 實戰腳本 | 🔵 |
| 2026-03-26 | @sitinme | HUD context 監控插件 | 🔵 |
| 2026-04-26 | @HiTw93 | Claude HUD 監控工具 | 🔵 |
| 2026-05-18 | @trq212 | implementation-notes.html | 🔵 |
| 2026-06-01 | @0xMoysei | 10 Lifehacks for Using Claude | 🔵 |
| 2026-06-01 | @AlphaSignalAI | dot-skill COLLEAGUE.SKILL 工作痕跡→versioned skill | 🔵 |
| 2026-07-27 | @sairahul1 | Opus 5 官方 prompting 精華：effort dial 取代冗長指令、刪除自我驗證指令、prompt 控制 verbosity、scope/checkpoint/subagent 邊界樣板（與既有 rules 高度重疊，可視為外部驗證） | 📋 → research/tweets/2026-07-27-@sairahul1-209385.md |

---

## Karpathy / stephzhan 原則

| 日期 | Author | 核心主題 | 整合狀態 |
|------|--------|---------|---------|
| 2025-06-25 | @karpathy | Context Engineering 定義 | ✅ → context-management.md |
| 2026-01-26 | @karpathy | Goal-Driven 哲學 | ✅ → core.md §R4 |
| 2026-04-30 | @karpathy | Sequoia 演講 agent economy | 🔵 |
| 2026-05-01 | @karpathy | context engineering shift | 🔵 |
| 2026-04-29 | @stephzhan | Agentic engineering 品質標準 | 📋 → quality.md |
| 2026-04-29 | @stephzhan | AI 代碼四缺陷 | 📋 → karpathy-principles.md |
| 2026-04-29 | @stephzhan | Jaggedness 框架 | 📋 → subagent-strategy.md |
| 2026-04-29 | @stephzhan | 外包思考不外包理解 | 🗂 已在 core.md |
| 2026-04-29 | @stephzhan | Software 3.0 核心問題 | 🗂 Karpathy 原文更完整 |
| 2026-04-29 | @stephzhan | Sequoia thread 入口 | 🔵 |
| 2026-04-29 | @stephzhan | agentic 工程師面試 | 🔵 |
| 2026-04-29 | @stephzhan | neural nets 主計算願景 | 🔵 |
| 2026-05-01 | @AYi_AInotes | Sequoia 演講中文摘要 | 🔵 |

---

## Boris / Thariq 官方技巧

| 日期 | Author | 核心主題 | 整合狀態 |
|------|--------|---------|---------|
| 2025-07-14 | @trq212 | Claude Code 通用 agent | 🔵 |
| 2025-09-22 | @trq212 | Agent 檔案系統狀態管理 | 🔵 |
| 2025-10-27 | @trq212 | 多用 bash 建議 | 🔵 |
| 2025-11-12 | @trq212 | multi-agent fan-out | 🔵 |
| 2026-01-31 | @bcherny | 10 個官方團隊技巧 | 🔵 |
| 2026-02-04 | @trq212 | /insights 瓶頸診斷 | 🔵 |
| 2026-02-19 | @trq212 | Prompt caching 五原則 | ✅ → context-management.md |
| 2026-03-10 | @trq212 | /btw 非阻塞指令 | 🔵 |
| 2026-03-14 | @trq212 | /effort max 上線 | 🔵 |
| 2026-03-17 | @trq212 | Skill 九分類框架 | ✅ → RESOLVER.md |
| 2026-03-21 | @trq212 | pinned thread 索引 | 🔵 |
| 2026-03-30 | @bcherny | /loop+/schedule PR 自動化 | 🔵 |
| 2026-03-30 | @bcherny | 隱藏功能 thread 起始 | 🔵 |
| 2026-04-15 | @trq212 | Session 管理決策樹 | 🔵 |
| 2026-04-23 | @bcherny | harness bug 修復公告 | 🔵 |
| 2026-05-08 | @trq212 | HTML 取代 markdown 輸出 | 🔵 |
| 2026-05-18 | @trq212 | implementation-notes.html | 🔵 |
| 2026-05-21 | @nateherk | Prompt caching 80/20 | 🔵 |
| 2026-06-02 | @trq212 | dynamic workflows 六大 pattern·三大失敗模式 | 🔵 |

---

## Tools / MCP / Hooks

| 日期 | Author | 核心主題 | 整合狀態 |
|------|--------|---------|---------|
| 2026-07-02 | @Serantych | Boris Cherny 實戰工作法：5+ 平行 session 獨立 git checkout、PR-time CLAUDE.md 修正、驗證迴圈 2-3x 品質 | 📋 → research/tweets/2026-07-02-@Serantych-003836.md |
| 2025-11-13 | @trq212 | frontend-design plugin | 🔵 |
| 2026-01-21 | @trq212 | TUI React 引擎 | 🔵 |
| 2026-01-29 | @trq212 | playground HTML plugin | 🔵 |
| 2026-03-19 | @trq212 | Channels Telegram/Discord MCP | 🔵 |
| 2026-04-04 | @MinLiBuilds | 8 個 Hooks 實戰腳本 | 🔵 |
| 2026-04-21 | @_avichawla | MCP token 陷阱 | 🔵 |
| 2026-05-08 | @anthropic | keep-rate eval metric | 🔵 |
| 2026-05-09 | @MinLiBuilds | Codex /goal 工業級 prompt | 🔵 |
| 2026-05-10 | @heynavtoor | 7 個 sub-agent prompt | 🔵 |
| 2026-04-25 | @codewithimanshu | Claude Code SDK 教學 | 🔵 |

---

## Workflow / Automation

| 日期 | Author | 核心主題 | 整合狀態 |
|------|--------|---------|---------|
| 2026-07-04 | @EXM7777 | Fable 5 Loop Library 25 workflows；Loop 五部分+state file；三色安全分級；cheap-first routing；Goal=proof-in-chat | 📋 → core.md+subagent-strategy.md |
| 2026-02-01 | @dontbesilent | 創作者工作流閉環 | 🔵 |
| 2026-03-15 | @akshay_pachaar | sub-agents orchestration pattern | 🔵 |
| 2026-04-22 | @cyrilXBT | 4 個 Claude 工作流 | 🔵 |
| 2026-04-25 | @suryanshti777 | 5 層 AI 系統架構論 | 🔵 |
| 2026-05-06 | @simonw | code-w-claude event | 🔵 |
| 2026-05-09 | @garrytan | Meta-Meta-Prompting 三層 | 🔵 |
| 2026-05-14 | @petradonka | Agents 需要 Feedback Loop | 🔵 |
| 2026-05-17 | @sairahul1 | AI 工作流 30 天夭折三規則 | 🔵 |
| 2026-05-26 | @chuhaiqu | Every 公司 AI 化一年 | 🔵 |
| 2026-05-30 | @sairahul1 | Opus 4.8 Dynamic Workflows | 🔵 |
| 2026-06-02 | @0xluffy_eth | Hermes Agent 完整使用指南（記憶+自我改進+信任） | 🔵 |
| 2026-06-20 | @phosphenq | Loop Engineering: Build an AI That Codes While You Sleep（多輪 loop+sub-agent fan-out+worktree）| 🔵 |

---

## Others / 生態資源

| 日期 | Author | 核心主題 |
|------|--------|---------|
| 2026-07-25 | @iiiichigo_chan | 入門級六檔案 Claude Code 架構（CLAUDE.md/product/architecture/decisions/current/verify.sh），workspace 已有更成熟版本 | 🔵 |
| 2026-07-27 | @iiiichigo_chan | Codex寫/Claude審 vs Claude寫/Codex審不對稱：角色分配比 agent 數量更重要（未附論文連結） | 🔵 |
| 2026-07-27 | @zodchiii | 轉推 Thariq（Anthropic Claude Code）28 分鐘演講：capability overhang／unhobbling、把自己放進 Claude 的處境、以調色示範磨除 unknown unknowns。⚠️ 推文引言「graph engineering: memory that stays」影片中完全未出現，為導流自家指南的錯誤歸因 | 🔵 |
| 2026-07-18 | @nurijanian | Via negativa 減法方法：purpose-locked subtraction，風險刪項強制寫明後果；Claude Code skill 產品業配 | 🔵 |
| 2026-07-27 | @nurijanian | McKinsey issue-tree（Why/What/How 三型）+ MECE 檢查包裝為 Claude Code skill 產品業配 | 🔵 |
| 2026-07-26 | @thedankoe | 學習控制論框架：目標驅動誤差訊號→filter→retention；筆記系統應為創作燃料非收藏庫；含明顯自家產品業配 | 🔵 |
| 2026-07-15 | @Khazix0918 | 啞鈴流程：Fable5規劃+GPT-5.6 Sol對抗審查+Codex目標模式全自動執行 | 🔵
| 2026-07-14 | @msg | 跨CLI訂閱token maxxing：CodexBar+fable-delegator配額failover+Herdr | 🔵
| 2026-07-14 | @JoePro | 反 AI 樣板前端 Skill：Abomination Checklist 否定清單+token-first | 🔵
| 2026-07-06 | @DataScienceDojo | Fable 5 orchestrator + Opus/Sonnet subagent 分工省成本 | 🔵 |
| 2026-03-27 | @0xKingsKuan | 官方免費課程導流 |
| 2026-03-27 | @AIExplorerTim | 非技術人入門引導 |
| 2026-03-27 | @AYi_AInotes | 中文工作流分析 |
| 2026-03-27 | @NainsiDwiv50980 | Boris Cherny 42 技巧 |
| 2026-04-18 | @0x_kaize | 生態系 repo 精選 |
| 2026-04-19 | @0x_kaize | 生態系 repo 精選 |
| 2026-04-19 | @cgtwts | Boris Cherny 技巧摘要 |
| 2026-04-20 | @0x_kaize | 生態系 repo 精選 |
| 2026-04-21 | @eng_khairallah1 | 35 個 Claude Code 技巧 |
| 2026-04-21 | @qloog | Cowork 多人協作設置 |
| 2026-04-22 | @Suryanshti777 | Opus 4.7 最佳實踐 |
| 2026-04-22 | @eng_khairallah1 | 6 Elements 課程 |
| 2026-04-24 | @GitTrend0x | Agent 項目星標盤點 |
| 2026-04-24 | @Suryanshti777 | Karpathy 9 個 prompt |
| 2026-04-25 | @nyk_builderz | — |
| 2026-04-26 | @dani_avila7 | — |
| 2026-04-29 | @elliotchen100 | 同事心智模型 32 技巧（重複版）|
| 2026-05-09 | @NFTCPS | 四級學習路徑策展 |
| 2026-05-09 | @SaitoWu | AI 編程底層原則 TDD |
| 2026-05-09 | @berryxia | GBrain 中文解析 |
| 2026-05-09 | @Michaelzsguo | 本地 LLM 5 層診斷 |
| 2026-05-10 | @rubenhassid | Claude 4.7 prompting 7 步驟 |
| 2026-05-11 | @karpathy | — |
| 2026-05-12 | @AlphaSignalAI | — |
| 2026-05-17 | @addyosmani | 別外包學習 6 提示姿態 |
| 2026-05-17 | @sairahul1 | AI 工作流 30 天夭折 |
| 2026-05-19 | @kfk_ai | FDE 是 Agent PMF 範式 |
| 2026-05-28 | @vista8 | AI 越強人越忙 |
| 2026-05-31 | @aiTinkle | AI 時代認知壓縮能力 |
| 2026-06-27 | @undefinedKi | 10 Claude Code Open-Source Repos（ECC/Graphify/SkillSpector/GBrain/DeerFlow/OpenClaw）；SkillSpector 安全掃描 |
| 2026-06-28 | @0xSlyth | 10 AI Loop Patterns 入門（Foundation/Execution/Advanced 三類）|

---

## 整合決策分類（Rule / Agent / SKILL / Others）

> 與上方 Author / Topic 索引為不同切法：本節依「整合決策分類」（該 tweet 該落地成 Rule 文件、Agent 定義、還是 SKILL）分組，依 A-E 五維 /10 加權評分排序（SCORING.md §1，與 §3 相同）。

### Rule

| 檔案 | 作者 | 日期 | 評分 | 摘要 |
|------|------|------|------|------|
| [2026-07-20-@0xCodez-330317.md](2026-07-20-@0xCodez-330317.md) | @0xCodez | 2026-07-20 | 7.05 | Graph Engineering 14 步路線圖：node/edge 定義+schema contract+diamond+router+verifier三型+loop-until-dry dedup-against-seen+model tiering，與 graph.md 高度收斂 |
| [2026-07-11-@eng_khairallah1-565100.md](2026-07-11-@eng_khairallah1-565100.md) | @eng_khairallah1 | 2026-07-11 | 7.65 | Loop Engineering 20 步路線圖：Done定義→外部化verifier→分層終止→state layer→人類checkpoint |
| [2026-07-02-@Serantych-003836.md](2026-07-02-@Serantych-003836.md) | @Serantych | 2026-07-02 | 8.1 | Boris Cherny 實戰工作法：5+ 平行 session 獨立 git checkout、PR-time CLAUDE.md 修正、驗證迴圈 2-3x 品質 |
| [2026-07-19-@TaoMachina-226249.md](2026-07-19-@TaoMachina-226249.md) | @TaoMachina | 2026-07-19 | 8.25 | Agent OS：Deterministic Gate + Brain 記憶治理 + Human Mission Authority 治理層框架 |
| [2026-07-08-@choopyplug1-503774.md](2026-07-08-@choopyplug1-503774.md) | @choopyplug1 | 2026-07-08 | 7.85 | Boris Cherny Loop方法十步驟：goal/checker分離+STATE.md+worktree+accepted-change率<50% |
| [2026-07-13-@joon_h_lee-173097.md](2026-07-13-@joon_h_lee-173097.md) | @joon_h_lee | 2026-07-13 | 7.65 | Fusion 架構下 Fable 委派時機/品質優於 Opus；早期+約束式 brief 使整體成本更低分數更高 |
| [2026-07-08-@addyosmani-835916.md](2026-07-08-@addyosmani-835916.md) | @addyosmani | 2026-07-08 | 7.7 | Quality/Verdict/Answerability；inner/outer loop；三隱性成本（surrender/debt/orchestration tax） |
| [2026-07-07-@keloneoneal-605379.md](2026-07-07-@keloneoneal-605379.md) | @keloneoneal | 2026-07-07 | 7.9 | Loop engineering 框架：六原語+readiness score+CLI工具鏈+11失敗模式 |
| [2026-07-01-@0xCodila-232639.md](2026-07-01-@0xCodila-232639.md) | @0xCodila | 2026-07-01 | 7.75 | Loop三要件verifier/state/stop；Karpathy AutoResearch；Bilevel外層loop 5x改善 |
| [2026-07-04-@EXM7777-697653.md](2026-07-04-@EXM7777-697653.md) | @EXM7777 | 2026-07-04 | 6.5 | Loop 五部分+state file+stop rule；Goal=proof-in-chat；25個Fable 5 agentic workflow；cheap-first routing |
| [2026-06-15-@addyosmani-594363.md](2026-06-15-@addyosmani-594363.md) | @addyosmani | 2026-06-15 | 8.3 | Review 成為最高槓桿技能；異質 AI reviewer 並行；人類上移一層 |
| [2026-06-15-@samueljmcd-634765.md](2026-06-15-@samueljmcd-634765.md) | @samueljmcd | 2026-06-15 | 6.8 | Loop engineering 核心是驗證；設計 verifier 而非 prompt；動態工作流程實現 |
| [2026-06-15-@qinzytech-371092.md](2026-06-15-@qinzytech-371092.md) | @qinzytech | 2026-06-15 | 6.75 | Self-evolving agents Model/Harness 二分框架；Memory 1 小時實作；Meta Harness 修改自身代碼 |
| [2026-06-14-@dongxi_nlp-081336.md](2026-06-14-@dongxi_nlp-081336.md) | @dongxi_nlp | 2026-06-14 | 7.7 | Markdown as context interface；AGENTS.md workspace policy vs SKILL.md task procedure；progressive disclosure |
| [2026-06-15-@sethrosen-316540.md](2026-06-15-@sethrosen-316540.md) | @sethrosen | 2026-06-15 | 7.1 | MVC 勝於公司大腦；stewardship pattern 讓 session 複利組織；dbt 中間 artifact 比喻 |
| [2026-06-28-@ArchiveExplorer-430283.md](2026-06-28-@ArchiveExplorer-430283.md) | @ArchiveExplorer | 2026-06-28 | 8.55 | Harness（靜態 .claude/）vs Loop（動態）兩層模型；arXiv 2606.10209 91.6% vs 71%；11 shortcuts agent fake done；MEMORY vs Vault 分層 |
| [2026-06-27-@trevin-948020.md](2026-06-27-@trevin-948020.md) | @trevin | 2026-06-27 | 7.3 | Compound Engineering 插件：skill-only 架構取代 standalone agent；/goal-ready 統一計劃文件；6h 無人工干預驗證 |
| [2026-06-27-@mvanhorn-795489.md](2026-06-27-@mvanhorn-795489.md) | @mvanhorn | 2026-06-27 | 7.75 | 218→6 記憶檔；技能教訓 PR 進 skill；CLAUDE.md 每行改決策才保留；Push vs Pull 記憶框架 |
| [2026-06-12-@nfcampos-517180.md](2026-06-12-@nfcampos-517180.md) | @nfcampos | 2026-06-12 | 9.60 | LDD in practice：Claude Code 兩 session（39h/800turns）建 xlsx-corpus-bench（6.8M cells）；人類只做四決策（oracle/properties/comparator/done）；281941→10604 cell（96% 是 locale 測量誤差）；「ask for the receipt」= unverified_success 閘門實戰 |
| [2026-06-12-@bibryam-435823.md](2026-06-12-@bibryam-435823.md) | @bibryam | 2026-06-12 | 8.80 | Loop-Driven Development：AI coding 五階段（autocomplete→prompt→context→harness→loop）；從 TDD→LDD；核心=verify（無驗證只是 repeated prompting）。與 workspace The Loop 一對一映射 |
| [2026-06-11-@PawelHuryn-549362.md](2026-06-11-@PawelHuryn-549362.md) | @PawelHuryn | 2026-06-11 | 8.30 | Fable 5 instruction audit prompt + migration gotchas + effort=high 即可 + nested overhead 量化（1.63-1.84×） |
| [2026-06-10-@davidvgilmore-743948.md](2026-06-10-@davidvgilmore-743948.md) | @davidvgilmore | 2026-06-10 | 7.30 | Subagent tokenomics：frontier=manager/trailing-edge=workers；subagent 是 cache-efficient 路由邊界；6 個月後預計 25-100 subagents/run |
| [2026-06-11-@techwith_ram-542820.md](2026-06-11-@techwith_ram-542820.md) | @techwith_ram | 2026-06-11 | 7.05 | Loop 適用邊界：成功條件客觀化（tests/score/template）才用自主 loop；code review loop（Greptile 4/5 gate）是最佳入門 |
| [2026-06-11-@mvanhorn-136666.md](2026-06-11-@mvanhorn-136666.md) | @mvanhorn | 2026-06-11 | 7.75 | Fable 5 Day 1 社群 9 條規則：去 babysitting、orchestrator 架構、medium effort 甜點、silent fallback 防禦 |
| [2026-06-09-@RLanceMartin-071163.md](2026-06-09-@RLanceMartin-071163.md) | @RLanceMartin | 2026-06-09 | 8.30 | Anthropic 官方：Fable 5 self-correction loop ~6× + verifier sub-agent > self-critique + 記憶 progression（73% verification） |
| [2026-06-08-@samueljmcd-825416.md](2026-06-08-@samueljmcd-825416.md) | @samueljmcd | 2026-06-08 | 7.95 | Dynamic Workflows 深度：confident plausibility 失敗模式、16-wide pipe、2N token economics、三呼叫模式決策準則 |
| [2026-06-08-@dongxi_nlp-163124.md](2026-06-08-@dongxi_nlp-163124.md) | @dongxi_nlp | 2026-06-08 | 7.75 | Harness Is The Product：六組件框架、Model 做 Proposal/Harness 做 Decision、failure→diagnostic 對應表（中文） |
| [2026-06-09-@alokbishoyi97-525741.md](2026-06-09-@alokbishoyi97-525741.md) | @alokbishoyi97 | 2026-06-09 | 7.25 | evo 自我演化 workflow：meta loop 在 optimize loop 運行時重寫 harness；detect-and-act 分離；Promise.all 雙 async loop |
| [2026-06-09-@mem0ai-233179.md](2026-06-09-@mem0ai-233179.md) | @mem0ai | 2026-06-09 | 7.20 | GitHub Copilot memory 深度拆解：citation-anchored 四欄 schema、JIT staleness verification、PR merge 83%→90% A/B |
| [2026-06-09-@Mnilax-225770.md](2026-06-09-@Mnilax-225770.md) | @Mnilax | 2026-06-09 | 7.30 | Fable 5 完整操作指南：silent fallback（cyber/bio/distill→Opus）、effort 五段、persistent memory 3×、SWE-Bench 80.3% |
| [2026-06-09-@seejayhess-263796.md](2026-06-09-@seejayhess-263796.md) | @seejayhess | 2026-06-09 | 7.35 | Fable/Mythos 實測：腳本化遷移範式、294 subagents 一次 pass、自主去重（負 diff）——「最強 big model smell」 |
| [2026-06-09-@0xCodez-773029.md](2026-06-09-@0xCodez-773029.md) | @0xCodez | 2026-06-09 | 8.25 | Loop 14 步驟路線圖：4 條件前置測試、Ralph Wiggum Loop 失敗模式、MVP 1+1+1+1 公式；520/17,022 skills 安全統計 |
| [2026-06-09-@JJEnglert-260388.md](2026-06-09-@JJEnglert-260388.md) | @JJEnglert | 2026-06-09 | 6.95 | 非工程師 1B token/$1,442 全面實測 Fable 5；Think→Build→Review 混合路由策略；effort 分檔；audit your setup 呼應 autoload-evolution |
| [2026-06-09-@AI_masaou-223206.md](2026-06-09-@AI_masaou-223206.md) | @AI_masaou | 2026-06-09 | 5.95 | Anthropic Thariq 影片摘要（日文）：Supervisor→Director 轉變；Context > Constraints；/goal + Workflows 範式 |
| [2026-06-09-@sairahul1-555684.md](2026-06-09-@sairahul1-555684.md) | @sairahul1 | 2026-06-09 | 6.40 | Loop Engineering 成本切入：1.7B tokens/$20 DeepSeek；六構件+五部分結構；Skills 三文件格式（VISION/ARCH/RULES） |
| [2026-06-08-@addyosmani-959567.md](2026-06-08-@addyosmani-959567.md) | @addyosmani | 2026-06-08 | 7.70 | Loop Engineering 五構件框架：Automations/Worktrees/Skills/Connectors/Sub-agents；bcherny「My job is to write loops」 |
| [2026-06-08-@mvanhorn-903149.md](2026-06-08-@mvanhorn-903149.md) | @mvanhorn | 2026-06-08 | 9.0 | WTF Is a Loop? Peter Steinberger vs. Boris Cherny |
| [2026-06-09-@ashwingop-539543.md](2026-06-09-@ashwingop-539543.md) | @ashwingop | 2026-06-09 | 7.10 | Company Brain = Feed 類比：注意力路由+記憶+效用函數；Permission-at-memory-level 架構；個人 AI→公司碎片化；MCP-style memory substrate（Sentra） |
| [2026-06-10-@startupideaspod-064018.md](2026-06-10-@startupideaspod-064018.md) | @startupideaspod | 2026-06-10 | 7.0 | Loop 反論：二元標準任務（code review, Greptile≥4, max 5 retry）才適合 loop；app 建構保留 human-in-the-loop；1000 行上限 guardrail |
| [2026-06-09-@smithandai-733882.md](2026-06-09-@smithandai-733882.md) | @smithandai | 2026-06-09 | 7.75 | Prompt→Context→Harness→Loop 四層演進；五部件 Loop（done check/context builder/act+capture/feedback/stop）；九步改造路徑 + 六接口（中文，綜合 arXiv 2606.05608） |
| [2026-06-09-@Smartpigai-968679.md](2026-06-09-@Smartpigai-968679.md) | @Smartpigai | 2026-06-09 | 6.80 | Loop Engineering vs Prompt Engineering：Agent 核心是循環非模型；同模型聊天 60 分→Agent 框架 90 分；未來最有價值的 AI 工程師設計 Loop（中文） |
| [2026-06-04-@freeman1266-804890.md](2026-06-04-@freeman1266-804890.md) | @freeman1266 | 2026-06-04 | 7.3 | Agent 四層工程每層皆有隱藏帳單，YAGNI 才是實踐準則 |
| [2026-06-05-@Khazix0918-763796.md](2026-06-05-@Khazix0918-763796.md) | @Khazix0918 | 2026-06-05 | 8.5 | Anthropic 首次公開 AI 驅動開發數據：Claude 撰寫 >80% 代碼，工程師產出 8× |
| [2026-06-02-@mvanhorn-473181.md](2026-06-02-@mvanhorn-473181.md) | @mvanhorn | 2026-06-02 | 7.3 | 22 個 agentic engineering hack：plan-first flip、多 session 並行、AgentMail、skill 複利 |
| [2026-06-08-@PawelHuryn-358857.md](2026-06-08-@PawelHuryn-358857.md) | @PawelHuryn | 2026-06-08 | 6.80 | Dynamic Workflows PM 指南：orchestrator off model、六 pattern、三失敗模式、113 agents/12min 案例 |
| [2026-06-09-@cxjwin-355193.md](2026-06-09-@cxjwin-355193.md) | @cxjwin | 2026-06-09 | 6.40 | prompt→context→harness→loop 四級演進；Felix "tasks→responsibilities" 升維；comprehension debt（中文） |
| [2026-06-02-@trq212-367865.md](2026-06-02-@trq212-367865.md) | @trq212 | 2026-06-02 | 8.8 | 動態 workflow 六大 pattern：fan-out/adversarial/tournament，解決 agentic laziness + goal drift |
| [2026-07-02-@milesdeutscher-711062.md](2026-07-02-@milesdeutscher-711062.md) | @milesdeutscher | 2026-07-02 | 6.3 | Fable 5 成本控制 10-80-10：Fable 規劃/審查(10%+10%)、Opus/Haiku 執行(80%)；/goal /loop 組合 |
| [2026-07-03-@noahduck283-497328.md](2026-07-03-@noahduck283-497328.md) | @noahduck283 | 2026-07-03 | 6.8 | Fable 5 全指南（中文）：硬/長/髒任務三特徵；工單六元素 prompt 模板；30天數據保留；分層路由 |
| [2026-07-02-@wquguru-253843.md](2026-07-02-@wquguru-253843.md) | @wquguru | 2026-07-02 | 8.6 | Fable 5 實戰（中文）：四要素 prompt 框架；notes/記憶系統；⚠️reasoning_extraction→Fable fallback；overnight 輸出風格 |
| [2026-07-02-@kingwilliam_-250287.md](2026-07-02-@kingwilliam_-250287.md) | @kingwilliam_ | 2026-07-02 | 6.0 | Fable 5 playbook（英文）：11條規則；Barbell strategy；Memory 四步自更新；Skills 三建法；checkpoint prompt |
| [2026-07-02-@KSimback-107866.md](2026-07-02-@KSimback-107866.md) | @KSimback | 2026-07-02 | 7.8 | Claude setup 7條優化：Fable=高判斷力 orchestrator；⚠️Haiku 禁 exploration（靜默錯誤放大）；model-routing CLAUDE.md 模板；plugin 按 project 啟用 |
| [2026-07-02-@cyrilXBT-058492.md](2026-07-02-@cyrilXBT-058492.md) | @cyrilXBT | 2026-07-02 | 8.7 | Anthropic 官方 Fable 5 guide 最完整解碼：`ultrathink`/`ultracode`；HTTP 200 refusal（stop_reason="refusal"）；「audit」語言驗證效果最佳（Anthropic 測試）；子代理失敗=資訊不得推斷；vision crop-and-zoom；7項遷移 checklist |
| [2026-07-03-@addyosmani-042327.md](2026-07-03-@addyosmani-042327.md) | @addyosmani | 2026-07-03 | 8.3 | Agentic 自主等級 6 階框架：Agency×Orchestration 雙軸；Agent 執行合約 8 欄位；4 反模式（Summary Substitution 最關鍵）；高自主三問；Anthropic 400K session 數據（70%規劃=人類/80%執行=Claude）；「驗證永遠是瓶頸」 |
| [2026-06-13-@servasyy_ai-597508.md](2026-06-13-@servasyy_ai-597508.md) | @servasyy_ai | 2026-06-13 | 7.8 | Fable 5 自我改進系統 14 步（中文）：Self-improving≠Self-learning；Memory 五階段（73%驗證率 vs Opus 17%）；STATE.md 六分區；Maker/Verifier 分離(+6x)；四模型路由；三種 Routine 觸發；Visual Verification |
| [2026-07-02-@0xMoysei-392194.md](2026-07-02-@0xMoysei-392194.md) | @0xMoysei | 2026-07-02 | 7.4 | Anthropic docs 8 條規則：⚠️reroute 持續生效（觸發語句留 context→每次 bounce）；5% session reroute rate；驗證塊應建入系統（非每次 paste）；"act when ready"；自我審計 prompt |
| [2026-07-02-@VincentLogic-426474.md](2026-07-02-@VincentLogic-426474.md) | @VincentLogic | 2026-07-02 | 7.2 | AI 工作負債（中文）：三層結構（長期上下文/Skills/審核機制）；七類 context debt；獨立審核 agent 分工（生成→審核→編輯→事實→人工）；審計 prompt 輸出 Diff 不直接覆蓋 |
| [2026-07-03-@sairahul1-598401.md](2026-07-03-@sairahul1-598401.md) | @sairahul1 | 2026-07-03 | 7.0 | Fable 5 成本管控（英文）：10-80-10 路由（Fable/Sonnet/Haiku）；CLAUDE.md 六模型路由表；/handoff trick；effort medium 甜點（非 xhigh）；⚠️reasoning_extraction=Mistake #3 |
| [2026-07-03-@zodchiii-328626.md](2026-07-03-@zodchiii-328626.md) | @zodchiii | 2026-07-03 | 6.2 | Fable 5 setup 指南（英文）：「weeks-by-hand→Fable/minutes-by-hand→Sonnet」路由公式；kickoff template（Goal/Scope/Constraints/Plan first/Done）；safeguard 誤報 reroute；30天 retention |
| [2026-06-13-@zero_goliath-976398.md](2026-06-13-@zero_goliath-976398.md) | @zero_goliath | 2026-06-13 | 6.6 | RLVR 瓶頸在難以確定性評分的領域；突破路徑是 AI 跑真實微型公司以商業指標為訓練訊號 |
| [2026-06-13-@PandaTalk8-745710.md](2026-06-13-@PandaTalk8-745710.md) | @PandaTalk8 | 2026-06-13 | 7.5 | /goal 達標即停、/loop 定時輪詢、/workflows 並行監控是三個正交維度，不可混用 |
| [2026-06-18-@freeman1266-239697.md](2026-06-18-@freeman1266-239697.md) | @freeman1266 | 2026-06-18 | 6.60 | Loop Engineering 人的角色：可驗證停止條件＋triage inbox＋理解力債務管理 |
| [2026-06-18-@alex_prompter-806800.md](2026-06-18-@alex_prompter-806800.md) | @alex_prompter | 2026-06-18 | 7.25 | Loop 成本診斷 + 5 plays：spec-first/cheap planner/caching/delegate reads/人工 gate |
| [2026-06-18-@Jeyxbt-190930.md](2026-06-18-@Jeyxbt-190930.md) | @Jeyxbt | 2026-06-18 | 7.75 | Sub-agent 設計 12 levers：描述即觸發、工具層權限、model 分層、invocation 四選一；fleet economics + delegation 決策表 |
| [2026-06-20-@addyosmani-871019.md](2026-06-20-@addyosmani-871019.md) | @addyosmani | 2026-06-20 | 7.3 | Chromium 架構全解：網路棧→Blink 渲染管線→V8 JIT→Site Isolation 多進程安全，瀏覽器黑盒完整指南 |
| [2026-06-20-@AnatoliKopadze-822149.md](2026-06-20-@AnatoliKopadze-822149.md) | @AnatoliKopadze | 2026-06-20 | 6.1 | Loop 大眾化教學（Claude/GPT/Mira）：5.1M views；有 verifier 才是 loop；先免費後付費；非技術受眾最佳入門 |
| [2026-06-21-@ma_zhenyuan-091828.md](2026-06-21-@ma_zhenyuan-091828.md) | @ma_zhenyuan | 2026-06-21 | 6.7 | 中文批判性視角（冷饭硬炒？）：四層演進梯度（Prompt/Context/Harness/Loop）；公式 Loop=Harness+Cadence+Gate+Feedback+Memory |
| [2026-06-20-@elliotchen100-602297.md](2026-06-20-@elliotchen100-602297.md) | @elliotchen100 | 2026-06-20 | 6.45 | 七個 Agent Loop 最高可用場景（中文）；observe 先於 repeat；判斷標準四問；從讓模型回答→讓系統交付 |
| [2026-06-22-@Easycompany333-849954.md](2026-06-22-@Easycompany333-849954.md) | @Easycompany333 | 2026-06-22 | 6.2 | LOOP 基礎：五步結構/三要素/四條件/成本複利分析；附可複製 Loop prompt 模板 |
| [2026-06-22-@akshay_pachaar-866051.md](2026-06-22-@akshay_pachaar-866051.md) | @akshay_pachaar | 2026-06-22 | 7.35 | Loop Engineering 四難點：turn≠task done/doom loop/idempotent tools/maker-checker分離；5步入門路徑 |
| [2026-06-22-@idoubicc-330953.md](2026-06-22-@idoubicc-330953.md) | @idoubicc | 2026-06-22 | 7.1 | Multi-agent 架構設計：多租戶架構原則、DB as truth source、session (user_id,agent_id,channel_type,chat_id) 4-tuple、context=競爭優勢、4-tier config inheritance |
| [2026-06-22-@dunik_7-864322.md](2026-06-22-@dunik_7-864322.md) | @dunik_7 | 2026-06-22 | 6.4 | 4-Loop 框架：Hill-climbing loop（trace→失敗分析→自動改寫 prompt/config）；1.01^365=37.8；Loops 3+4 is basically empty |
| [2026-06-25-@unicodef1wn-395916.md](2026-06-25-@unicodef1wn-395916.md) | @unicodef1wn | 2026-06-25 | 6.95 | Dynamic Workflow 三失敗模式（agentic laziness/self-preferential bias/goal drift）+ 六 pattern + Tournament（comparing beats scoring）|
| [2026-06-23-@Raytar-805179.md](2026-06-23-@Raytar-805179.md) | @Raytar | 2026-06-23 | 6.6 | Loop Charter 六段模板；/goal 二副本自查機制；cron vs loop（decision-maker inside）；LOOP-STATE.md 三態；Boris Cherny「writing loops is the job」|
| [2026-06-26-@Khazix0918-285575.md](2026-06-26-@Khazix0918-285575.md) | @Khazix0918 | 2026-06-26 | 6.25 | Prompt/Skill/Hook 三分法（對話/能力/時刻）；Hook 是門鈴 Skill 是幹活的人；PreCompact 摘要卡片 Hook；Bark 長任務推送 |

### Agent

| 檔案 | 作者 | 日期 | 評分 | 摘要 |
|------|------|------|------|------|
| [2026-07-07-@albertgao-423939.md](2026-07-07-@albertgao-423939.md) | @albertgao | 2026-07-07 | 6.95 | orchestrator+programmer/reviewer loop，24 票 27 小時無人值守 |
| [2026-06-11-@elvissun-864954.md](2026-06-11-@elvissun-864954.md) | @elvissun | 2026-06-11 | 8.45 | /goal 真正用途是 LFD：Target/Constraints/Instruments/Forced Entropy 四元素框架，30h/$40 逆向工程出 50× 效果 |
| [2026-06-10-@nateherk-399269.md](2026-06-10-@nateherk-399269.md) | @nateherk | 2026-06-10 | 6.90 | Four Cs AI OS（Context/Connections/Capabilities/Cadence）；Folders+Markdown 工具中立；「Keys not prompts」安全原則；Claude Fable 定價 $10/$50 per M |
| [2026-06-09-@mfpiccolo-995141.md](2026-06-09-@mfpiccolo-995141.md) | @mfpiccolo | 2026-06-09 | 6.75 | iii 框架四 Worker 架構（harness/context-manager/session-manager/llm-router）：無整合代碼，類比 React，Worker/Trigger/Function 為後端基礎抽象 |
| [2026-06-09-@lotte_verheyden-646410.md](2026-06-09-@lotte_verheyden-646410.md) | @lotte_verheyden | 2026-06-09 | 6.60 | Agent Slop 防範：AI 工程閉環 keep/automate 決策框架，保留 trace 人工閱讀，品味（taste）是差異化邊界（Langfuse） |
| [2026-06-09-@nifinet-440907.md](2026-06-09-@nifinet-440907.md) | @nifinet | 2026-06-09 | 6.65 | 六步驟 AI GTM Brain（Claude Code）：Sense→Judge→Act 閉環，$400/月 token 取代五名人力，command-line-first 設計隔離 adapter |
| [2026-06-08-@bcherny-754658.md](2026-06-08-@bcherny-754658.md) | @bcherny | 2026-06-08 | 7.3 | Claude Code 作者分享 5 個讓 Opus 長時間自主運行的關鍵技巧 |
| [2026-06-18-@djfarrelly-278630.md](2026-06-18-@djfarrelly-278630.md) | @djfarrelly | 2026-06-18 | 7.25 | Agent loop 三層架構：Loop+Skill+Orchestrator；sidecar 讓 agent 寫自身 durable skills |
| [2026-06-19-@jasonzhou1993-897143.md](2026-06-19-@jasonzhou1993-897143.md) | @jasonzhou1993 | 2026-06-19 | 7.45 | Loop engineer 框架：inner/outer loop 雙層 + 共享 artifact 讓多 loop 複利 |
| [2026-06-20-@phosphenq-364103.md](2026-06-20-@phosphenq-364103.md) | @phosphenq | 2026-06-20 | 7.9 | Loop 六構件（STATUS.md+Automations+Worktrees+Skills+Connectors+Sub-agents）+ 10 失敗模式，Claude Code/Codex 雙平台配置 |
| [2026-06-20-@mvanhorn-748331.md](2026-06-20-@mvanhorn-748331.md) | @mvanhorn | 2026-06-20 | 8.25 | 15 個真實 Loop 配方可直接偷用；/loop/goal/routine/harness 四類型；verifier = loop 最關鍵元素；roborev shipped |
| [2026-06-17-@0xMovez-044494.md](2026-06-17-@0xMovez-044494.md) | @0xMovez | 2026-06-17 | 6.75 | Kimi K2.6 300-agent swarm 10步 playbook：spec→swarm→Opus verify→skill→CONSTRAINTS 閉環 |
| [2026-06-22-@h100envy-623783.md](2026-06-22-@h100envy-623783.md) | @h100envy | 2026-06-22 | 8.2 | Loop 7步技術路線圖：stateless iteration/context budget/reward hacking gate/JSONL log/blast radius |

### SKILL

| 檔案 | 作者 | 日期 | 評分 | 摘要 |
|------|------|------|------|------|
| [2026-07-08-@Mnilax-689957.md](2026-07-08-@Mnilax-689957.md) | @Mnilax | 2026-07-08 | 7.75 | goal+獨立verifier+stop rule+state file+worktree，7天實測340cycles/$210 |
| [2026-07-06-@alex_prompter-181121.md](2026-07-06-@alex_prompter-181121.md) | @alex_prompter | 2026-07-06 | 6.35 | 萃取強模型操作手冊移植進便宜模型系統提示，陷阱題驗證是否生效 |
| [2026-07-07-@BHolmesDev-461170.md](2026-07-07-@BHolmesDev-461170.md) | @BHolmesDev | 2026-07-07 | 7.8 | raw notes→enrich-note→wiki skill→排程自動化，自建 LLM 知識庫五步驟 |
| [2026-07-07-@EXM7777-465089.md](2026-07-07-@EXM7777-465089.md) | @EXM7777 | 2026-07-07 | 6.55 | 六階段 gate prompt 探勘本機 agent session 歷史產出自我畫像與 CLAUDE.md diff |
| [2026-06-16-@freeman1266-227843.md](2026-06-16-@freeman1266-227843.md) | @freeman1266 | 2026-06-16 | 8.2 | 三文件自動化 loop：CLAUDE.md 協議+hooks 硬約束+fixer agent 破死局 |
| [2026-06-09-@Voxyz_ai-825921.md](2026-06-09-@Voxyz_ai-825921.md) | @Voxyz_ai | 2026-06-09 | 6.30 | Fable 5 印象 + design audit /goal prompt：boot→screenshot→audit→fix→skill 化；$200 plan xhigh 30min=2% quota；三層 auto-fix boundary |
| [2026-06-09-@meta_alchemist-433646.md](2026-06-09-@meta_alchemist-433646.md) | @meta_alchemist | 2026-06-09 | 6.20 | 病毒式 Repo Audit prompt（572K views/10K bookmarks）：四階段 + 八維度 + milestone 分級 + facts vs judgments 分離 |
| [2026-06-12-@op7418-427565.md](2026-06-12-@op7418-427565.md) | @op7418 | 2026-06-12 | 3.8 | 万字长文：Agent 不平權化而是放大能力差距；深層論證 Skills 時代的能力分化機制；284k 瀏覽、1.5k 讚（中文） |
| [2026-06-10-@vincemask-699973.md](2026-06-10-@vincemask-699973.md) | @vincemask | 2026-06-10 | 7.55 | Claude Code 五層安全護欄：OS 沙箱→deny/ask/allow→PreToolUse Hook→工程規則→遠端 CI；Codex 雙工具適配；命令風險分級（中文） |
| [2026-06-07-@mvanhorn-501832.md](2026-06-07-@mvanhorn-501832.md) | @mvanhorn | 2026-06-07 | 8.1 | Remotion Was My First Agentic Video Love. Then HyperFrames Stole Me. |
| [2026-06-14-@cyrilXBT-219807.md](2026-06-14-@cyrilXBT-219807.md) | @cyrilXBT | 2026-06-14 | 7.0 | 300 個針對 Fable 5 特性優化的提示詞，終極用法是編碼為自動執行的 SKILL 基礎設施 |
| [如何沉淀 SKILL：把重复劳动变成可复用的能力](2026-06-18-@PandaTalk8-915618.md) | @PandaTalk8 | 2026-06-18 | 7.9 | SKILL 設計四要素、三次門檻、四階段漸進法 |
| [2026-06-26-@KyrieCheungYep-627273.md](2026-06-26-@KyrieCheungYep-627273.md) | @KyrieCheungYep | 2026-06-26 | 7.85 | Loop Engineering 六實戰場景；daily-triage SKILL template；7-item 安全 checklist；3 hard brakes；成本公式 $0.2/round |
| [2026-06-24-@wquguru-780384.md](2026-06-24-@wquguru-780384.md) | @wquguru | 2026-06-24 | 8.2 | Agent Memory 5層分類（Rules/Resident Profile/History Recall/Governance Memory/Self-evolution）+ 5 設計原則 + 4 失敗模式 |
| [2026-06-25-@Jeyxbt-181660.md](2026-06-25-@Jeyxbt-181660.md) | @Jeyxbt | 2026-06-25 | 7.9 | Anthropic 內部 Skill 五課：4-type taxonomy；Description=trigger；Verification 2-3x；Gotcha=護城河（不能事先寫）；4 audit prompts |
| [2026-07-03-@trq212-215386.md](2026-07-03-@trq212-215386.md) | @trq212 | 2026-07-03 | 8.3 | Fable 5 unknowns 場域指南：7 技術（Blind Spot Pass/Interview/Prototype/Reference/Implementation Notes/Quiz）含具體 prompt |

### Others（評分分類）

| 檔案 | 作者 | 日期 | 評分 | 摘要 |
|------|------|------|------|------|
| [2026-07-22-@ericosiu-957131.md](2026-07-22-@ericosiu-957131.md) | @ericosiu | 2026-07-22 | 5.55 | Graph vs Loop「軌道 vs 引擎」比喻；與 graph.md/loop.md 既有分工吻合，外部驗證引用 |
| [2026-07-21-@0xClodex-272354.md](2026-07-21-@0xClodex-272354.md) | @0xClodex | 2026-07-21 | 4.75 | Graph Engineering 7 步指南；Bun Zig→Rust 重寫案例規模/工期無來源可查；與 @0xCodez-330317 機制重複 |
| [2026-07-18-@steipete-189132.md](2026-07-18-@steipete-189132.md) | @steipete | 2026-07-18 | 2.85 | 12 字原始貼文引爆 Graph Engineering 熱潮，無技術內容，僅史料價值 |
| [2026-07-18-@sairahul1-101097.md](2026-07-18-@sairahul1-101097.md) | @sairahul1 | 2026-07-18 | 4.95 | Loop over prompt：Slate CLI 可組合 agent Program（loop-as-job 概念與 Slate 產品推廣） |
| [2026-07-15-@Khazix0918-134531.md](2026-07-15-@Khazix0918-134531.md) | @Khazix0918 | 2026-07-15 | 5.1 | 啞鈴流程：Fable5出方案+GPT-5.6 Sol對抗審查+Codex目標模式全自動長跑執行 |
| [2026-07-14-@msg-575512.md](2026-07-14-@msg-575512.md) | @msg | 2026-07-14 | 5.15 | 跨CLI訂閱token maxxing：CodexBar監控+fable-delegator配額路由+Herdr terminal多工 |
| [2026-07-14-@JoePro-954311.md](2026-07-14-@JoePro-954311.md) | @JoePro | 2026-07-14 | 5.85 | 反 AI 樣板前端 Skill：否定清單優先+design tokens 先行+8項互動狀態 |
| [2026-07-06-@DataScienceDojo-195971.md](2026-07-06-@DataScienceDojo-195971.md) | @DataScienceDojo | 2026-07-06 | 4.5 | Fable 5 當 orchestrator，硬推理 Opus/機械工作 Sonnet subagent 分工 |
| [2026-07-07-@ataiiam-937703.md](2026-07-07-@ataiiam-937703.md) | @ataiiam | 2026-07-07 | 5.2 | procedural/episodic/semantic 三型記憶 + Learning Containers（CopilotKit 行銷） |
| [2026-06-15-@matanSF-680920.md](2026-06-15-@matanSF-680920.md) | @matanSF | 2026-06-15 | 5.7 | 軟體工廠架構：全 SDLC agent 化，Model Independence + Sovereign Intelligence |
| [2026-06-27-@undefinedKi-630023.md](2026-06-27-@undefinedKi-630023.md) | @undefinedKi | 2026-06-27 | 6.05 | 10 個 Claude Code open-source repos 導覽（ECC/Graphify/SkillSpector/DeerFlow/OpenClaw）；SkillSpector 安全掃描 + Graphify 71x token reduction 值得追蹤 |
| [2026-06-28-@0xSlyth-912219.md](2026-06-28-@0xSlyth-912219.md) | @0xSlyth | 2026-06-28 | 4.75 | 10 AI Loop 模式入門圖解：Retry/Reflection/Evaluation/Planning/Tool-Calling/Research/Memory/Multi-Agent/Human-in-Loop/Continuous Improvement |
| [2026-06-13-@dongxi_nlp-010332.md](2026-06-13-@dongxi_nlp-010332.md) | @dongxi_nlp | 2026-06-13 | 5.75 | Harness 系列 #4：slash 是 user→harness control plane（非 prompt）；input router 雙 parser boundary；/goal 為顯式 session state；/audit /doctor 走 deterministic local check（中文） |
| [2026-06-12-@haridigresses-963134.md](2026-06-12-@haridigresses-963134.md) | @haridigresses | 2026-06-12 | 8.00 | Anthropic 天命論：Steward→Sovereign 轉型四證據（CC 封鎖第三方 harness／道德霸權／SPV 事件／Fable 靜默降級）；合法性燃燒速度比市場份額更快 |
| [2026-06-10-@saranormous-400652.md](2026-06-10-@saranormous-400652.md) | @saranormous | 2026-06-10 | 8.80 | The Untrainable：AI 投資悲觀論反駁；2×2（飽和度×私有性）找護城河；MIT 10萬開發者研究：code +180% 但 shipped +30%；intelligence 不是瓶頸，permission 才是 |
| [2026-06-10-@nurijanian-289888.md](2026-06-10-@nurijanian-289888.md) | @nurijanian | 2026-06-10 | 6.40 | AI 需求評審三層 altitude 框架；weasel word 掃描清單（30+ 詞，1 分鐘代替 40 分鐘）；句子品質 vs. 目錄品質（9+9 特性）；open-source skill on GitHub |
| [2026-06-08-@akshay_pachaar-498924.md](2026-06-08-@akshay_pachaar-498924.md) | @akshay_pachaar | 2026-06-08 | 4.65 | Opik 贊助文：Harness 自我修復 4 層閉環（trace→Ollie→regression 鎖定）；觀測性 what/why/fix/prevent 框架 |
| [2026-06-09-@PandaTalk8-154694.md](2026-06-09-@PandaTalk8-154694.md) | @PandaTalk8 | 2026-06-09 | 5.70 | Loop Engineering 哲學根源：控制論/杜威/蘇格拉底；過程控制→目標治理；思考深度是 AI 時代護城河（中文） |
| [2026-06-09-@MatthewBerman-669176.md](2026-06-09-@MatthewBerman-669176.md) | @MatthewBerman | 2026-06-09 | 5.15 | Fable 一周個人測試：workflow mode、長 horizon 自主、過度 verbose + 慢；Pro tip：effort level 調低 |
| [2026-06-09-@aashatwt-930944.md](2026-06-09-@aashatwt-930944.md) | @aashatwt | 2026-06-09 | 4.65 | Agent loop 入門概念指南：loops vs workflows、open/closed、evals > prompts、memory + skills 角色 |
| [2026-06-09-@teach_fireworks-513451.md](2026-06-09-@teach_fireworks-513451.md) | @teach_fireworks | 2026-06-09 | 4.35 | Agent Loop 四層價值文獻綜述（中文）：執行/失敗暴露/長任務穩定/Autoloop；生產 checklist |
| [2026-06-08-@0xMoysei-344815.md](2026-06-08-@0xMoysei-344815.md) | @0xMoysei | 2026-06-08 | 5.5 | 14步驟將 Claude Code 打造成固定價格外包服務（提綱式，可信度低） |
| [2026-06-09-@Truunik-292077.md](2026-06-09-@Truunik-292077.md) | @Truunik | 2026-06-09 | 4.05 | 個人裝置防護 prompt：11 類加固步驟 + 模型自檢 RERUN_NOTICE flag |
| [2026-06-09-@meta_alchemist-490911.md](2026-06-09-@meta_alchemist-490911.md) | @meta_alchemist | 2026-06-09 | 4.90 | Fable 5 → 14 天窗口策略：audit/architecture 優先，cheaper 模型做 build |
| [2026-06-18-@akshay_pachaar-725258.md](2026-06-18-@akshay_pachaar-725258.md) | @akshay_pachaar | 2026-06-18 | 5.60 | Vibe Coding 安全盲點：agent 優化 correctness 非 operational safety；runtime-level boundary（identity/permissions/audit）在 prompt 之外；Retool 贊助文 |
| [2026-07-02-@EXM7777-955630.md](2026-07-02-@EXM7777-955630.md) | @EXM7777 | 2026-07-02 | 6.0 | Fable 5 入門全課：leader/workers 角色；三 secret（不過度引導/輕 CLAUDE.md/善用 /goal loops）；Pocock skills 引用；五 workflow；高重疊推廣內容 |
| [2026-06-27-@leanxbt-202609.md](2026-06-27-@leanxbt-202609.md) | @leanxbt | 2026-06-27 | 6.9 | Loop 應用於 prompt 自動優化：eval 可靠性等級（exact>label>verifiable>judge）；train/holdout 防過擬合；PATIENCE=3 高原偵測器；診斷優先改寫；comprehension debt 警告 |
| [2026-05-25-@akshay_pachaar-885210.md](2026-05-25-@akshay_pachaar-885210.md) | @akshay_pachaar | 2026-05-25 | 6.8 | Pydantic 修復 Agent Memory：Vector DB multi-hop 失敗；Knowledge Graph + schema ontology（EntityModel/EdgeModel）；10/10/10 強制聚焦；Schema = reasoning boundary；Zep 五步 extraction pipeline |
| [2026-07-01-@nateherk-008871.md](2026-07-01-@nateherk-008871.md) | @nateherk | 2026-07-01 | 6.0 | Anthropic 工程師 Fable 5 6 習慣：Fable low ≈ Opus xhigh（10-15% 使用率）；Silent routing 不告知用戶（API 可見/UI 不可見）；驗證塊 + 負向提示 + Say Less；與 wquguru/cyrilXBT 高度重疊 |
| [2026-06-10-@kirillk_web3-535033.md](2026-06-10-@kirillk_web3-535033.md) | @kirillk_web3 | 2026-06-10 | 5.7 | Fable 5 官方 10 個隱藏能力展示（官方 docs prompt 示例）；30天 prompt/output 保留（安全分類器訓練）；無新框架，高度重疊 |

---

## 整合狀態說明

| 符號 | 說明 |
|------|------|
| ✅ | 已整合到 workspace 規則/文件 |
| 📋 | 待整合（分數達標）|
| 🔵 | 已歸檔，整合狀態未確認 |
| 🗂 | 已被其他資源涵蓋，跳過 |
| 評分 | X.X/10（§1 加權總分） |
