# tweets/INDEX.md

> **Type:** raw:tweet — 193 tweets + 5 daily-digest；Claude Code / AI Engineering 技術 thread 歸檔  
> **Updated**: 2026-06-09 | **Authors**: 93 | **Files**: 198 .md（193 tweet + 5 digest）  
> **Query pattern**: BRAIN.md → 本表（Author / Topic）→ `<date>-@<handle>-<id>.md`  
> **Frontmatter**: canonical YAML（`url`/`author`/`handle`/`published`/`archived`/`type`/`stats`）；`type` ∈ {tweet, twitter-article, note-tweet, thread, twitter-video, daily-digest}

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

---

## Skill / AGENTS.md 設計

| 日期 | Author | 核心主題 | 整合狀態 |
|------|--------|---------|---------|
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

---

## Context / Token 優化

| 日期 | Author | 核心主題 | 整合狀態 |
|------|--------|---------|---------|
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

---

## CLAUDE.md / Rules

| 日期 | Author | 核心主題 | 整合狀態 |
|------|--------|---------|---------|
| 2026-01-02 | @bcherny | vanilla 設定哲學 | 🔵 |
| 2026-02-11 | @bcherny | 客製化設計目標 | 🔵 |
| 2026-04-27 | @zodchiii | CLAUDE.md 五段落框架 | 🔵 |
| 2026-05-07 | @vincemask | CLAUDE.md 8 條實戰 | 🔵 |
| 2026-05-09 | @Mnilax | Karpathy 4 規則盲點 + 12 條 | ✅ → refs/karpathy-mnilax-best-solution.md |
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

---

## Others / 生態資源

| 日期 | Author | 核心主題 |
|------|--------|---------|
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

---

## 整合狀態說明

| 符號 | 說明 |
|------|------|
| ✅ | 已整合到 workspace 規則/文件 |
| 📋 | 待整合（分數達標）|
| 🔵 | 已歸檔，整合狀態未確認 |
| 🗂 | 已被其他資源涵蓋，跳過 |
