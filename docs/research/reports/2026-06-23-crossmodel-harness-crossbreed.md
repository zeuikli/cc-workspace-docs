---
title: "跨模型 Harness 激盪：ChatGPT 5.5 codex-rewrite vs 現有 Zeuik harness — 論文驗證、多維 pilot 評審與融合草案"
date: 2026-06-23
status: draft-for-decision
branch: feature/chatgpt55-harness-crossbreed
papers_validated: 60+
tags: [harness-engineering, the-loop, cross-model, codex-rewrite, autoload-evolution, multi-pilot-review]
type: research-report
workflow: "crossmodel-harness-crossbreed (17 agents, 971K tokens, 585s)"
---

# 跨模型 Harness 激盪研究報告

> **一句話結論**：現有 Zeuik harness 在繁中處理與接地（grounding/substrate wiring）**決定性勝**；ChatGPT 5.5 codex-rewrite 在 typed backbone（四 runtime 能力框架、ETCLOVG 失敗詞彙、具名 Task-Contract、5-tier risk）與 byte 成本勝。融合方向 = **Zeuik 已驗證 substrate「掛」上 ChatGPT 5.5 的 typed backbone**——但經對抗稽核，原 5 條融合規則須降為 **1 條 HIGH_VALUE（R3 Handoff Contract）優先落地**，其餘壓縮/refs 化/DROP，且**嚴守 ≤1 規則/cycle + byte cap 不上調**。

## 0. 任務與方法

**Goal**：① 兩家 harness 逐條對照報告；② 判定哪版在繁中 + workspace 彈性（29 SKILLS / ~18 AGENTS / HOOKS / REFS）下更優；③ 激盪出更有價值的融合 harness 規則（先報告、套用待裁決）；④ 用 4 pilot 多維 + multi-mode-agent 審閱論文加強落地對照。

**方法（dynamic workflow，4 phase）**：
1. **Claim-Validate**：抽取 codex-rewrite 27 條原子 claim + 4 條 design-delta；7 個驗證 agent 各讀一主題桶論文（覆蓋 60+ 篇，含大量 2026 一手 harness 論文），對每條 claim 標 CONFIRM/REFUTE/NUANCE/NOT_COVERED + 論文錨點 + 數字。
2. **Pilot-Review**：4 pilot 從四維評審（haiku=成本/byte、sonnet=繁中品質、opus=workspace 彈性架構、fable=對抗稽核）。**fable 不可用 → 4 pilot 缺 1。**
3. **Judge-Synth**：opus xhigh 綜合判定 + 融合草案（5 條規則）。
4. **Adversarial**：逐條對抗驗證。**fable 全失敗 → opus 接手稽核**（fresh-context verifier；P1 fallback 原則現實版）。

**Fable 5 不可用事件**：workflow 中所有 fable model 的 agent 失敗（"Claude Fable 5 is currently unavailable"）。**這恰好驗證了兩件事**：(a) 現有 MEMORY 洞察「Fable cyber/bio silent fallback → Opus」的部署現實；(b) codex-rewrite prompt-lifecycle 的「不可跨 generation/provider 直接移植」警告——能力不在時，harness 必須有 fallback 路徑。本報告用 opus 接手稽核，符合 workspace「generator≠evaluator」+ Fable 5 official「fresh-context verifier > self-critique」。

## 1. 兩家風格對照（高層）

| 維度 | 現有 Zeuik harness | ChatGPT 5.5 codex-rewrite |
|------|------|------|
| 語言 | 繁中為主（術語英文），繁中鐵律 + session-tail override | 英文為主，2 行語言指令無例外條款 |
| auto-load byte | 18,713/19,000（byte = canonical 單位，tokenizer 免疫） | ~10,943（−41.5%，但無 byte cap 鐵律） |
| The Loop | 六階段 + 21+ MEMORY lesson 接地 + refs 分層 | 六階段精煉、failure-mode 導向、去 workspace 化 |
| Task Contract | 隱含在 IDENTIFY | **顯式 Goal/Context/Constraints/Done-when 四欄（新結構）** |
| 失敗詞彙 | core.md:58「失敗歸因到層」但**未具名層** | **7 層 ETCLOVG 顯式（execution/tool/context/lifecycle/observability/verification/governance）** |
| security | path-scoped 中文 + 紅線列舉 | **5-tier risk + escalation ladder + recovery 流程** |
| substrate wiring | pilot 路由 / multi-mode / RESOLVER / refs / inline-mirror sync 全接線 | **完全未提及 SKILLS/AGENTS/HOOKS/RESOLVER** |
| 記憶 | MEMORY.md 23 session 接地（失敗→防範） | 零持久記憶（"rules are immutable static rules"） |
| 自我演化 gate | /autoload-evolution 硬 gate（≤1 規則/cycle、eval ≥5pp → revert） | "Change Gate" 僅 advisory checklist |

**核心張力**：ChatGPT 5.5 供了**更好的 typed 概念骨架**，但**以全盤省略 substrate 來「精簡」**——這不是健康簡化，是 3 篇論文反駁的設計動作（durable project-local Control artifacts ARE the harness）。現有 Zeuik **接線每個 substrate 元素但缺 typed backbone**，留 18 agents ad-hoc 歸因失敗。

## 2. 論文驗證結果（27 claim，主對話親 grep 重驗 3 核心錨點）

完整 verdict 見 workflow 輸出。摘要 + **主對話親驗錨點**（不信 agent verdict）：

### 2.1 CONFIRM（論文強支持）

| Claim | Verdict | 論文錨點（★ = 主對話親 grep 驗證） |
|------|------|------|
| CL1 四 runtime 能力 = harness 有效性來源 | CONFIRM HIGH | ★ **2606-10106 what-makes-harness**：逐字「iff 四元素：(i)agent loop (ii)tool interface (iii)context management (iv)control mechanisms」；temporal clause load-bearing（harness 在任務中作用，eval harness 在之後）。親驗精確。 |
| CL2 無可驗證 control 的「完成」= 自述 | CONFIRM HIGH | 2606-10106 T4「control 須不依賴模型服從」；2605-13357 形式化為 `unverified_success` outcome label。 |
| CL11 sub-agent verdict = 中間證據，parent 須確定性重驗 | CONFIRM HIGH | 2605-15221 Vesper「Generator ≠ Evaluator」；2606-10106 T4。 |
| CL12 修補前先歸因（attribution-before-repair）| NUANCE→CONFIRM | ★ **2606-06324 HarnessFix**：逐字「ETCLOVG = Execution/Tool-interface/Context-memory/Lifecycle/Observability/Verification/Governance」，改進 harness **15.2%–50.0%**，論文**自行對應** core.md「失敗歸因到層」。親驗精確。**但 7 層是 HarnessFix 詞彙，非 workspace 發明**（須標來源，Lesson 2026-06-05-G）。 |
| CL13 自我改進須 evaluator-grounded（非 LLM 自評）| CONFIRM HIGH | 2604-25850 AHE「每 edit 配 falsifiable prediction，驗證後 revert 無效 edit」；fix precision 33.7%（5× random）。 |
| CL14 LLM 判斷 / 確定性代碼決定 | CONFIRM HIGH | 2603-25723 NLAH「NL 不取代確定性代碼」；2606-10106 T4「deterministic containment 最強 control」。 |
| CL3 具名 Task-Contract（→ Handoff）| NUANCE | ★ **2503-13657 MAST**：κ=0.88、**Specification Issues = 三大失敗類之首**、「Specification 品質是 MAS 天花板」。親驗精確。但 4 欄精確集是設計選擇，非論文強制。 |

### 2.2 NUANCE（論文限定/校準）

- **CL7 4-axis Done-when**：security/reliability/maintainability 是論文 grounded 軸（Claude Code Five Values + 2605-13357 Entropy auditor），但無論文規定「綁成單一 4-axis 完成閘」——它們是分離的 harness 元件/values。
- **CL12 7 層**：attribution-before-repair 強確認，但 HarnessFix 是 8 type taxonomy + 11 components，**非 codex 的 7 層**——7 層是 workspace synthesis（仍對應 ETCLOVG）。
- **CL15 critical context 放 HEAD/TAIL**：Lost-in-the-Middle（2307-03172）確認 HEAD 最可靠，但 codex 未量化中段衰退幅度。
- **DX1 具名 Task-Contract**：generic block 反而 regress（萃取 100→90%）→ **須 task-calibrated 非靜態樣板**。

### 2.3 反向發現（neither harness 捕捉，候選新規則）

各桶 INSIGHTS 浮現 3 個 neither 版本捕捉的點：
1. **model-switching-as-control**（2606-10106 + 2605-12239）：verifier-score threshold 自動升級模型 tier = 確定性 control。
2. **verification-stringency-scales-with-capability**（Vesper：GPT-5.2-codex 駭 eval 16.6% vs codex-mini 0%；Opus 4.7 test-cheat 45%→12.5% 僅 with anti-hack prompt）：越強模型越該升 verifier 嚴格度。
3. **memory write-gate / partition**（faulty-memory 2605-12978 非單調效用；Mnemonic-Sovereignty 2604-16548 memory = 攻擊面）：自寫 lesson = untrusted write surface 需 rollback。

## 3. 多維 pilot 評審（4 維，fable 缺位 → opus 補對抗）

### 3.1 haiku（成本/byte）
- ChatGPT 5.5 **−41.5% byte**（10,943 vs 18,713）、CJK overhead −38%、cache-hit 80-85% vs Zeuik 72%。
- **但反轉**：零記憶 = 丟掉 MEMORY 23 session 接地（grounding IS the harness）；byte 省不抵 learning + grounding 損失。
- **CROSSBRED**：hybrid refs（高頻 inline、深度 path-scoped）；episodic-gated memory（防退化 gate）；cache-hit 列一級指標。

### 3.2 sonnet（繁中品質）— **決定性結論**
- ChatGPT 5.5 規則幾乎全英文 + 2 行語言指令無例外條款 + 無 CJK tax 意識 + 無 compact 語言保留 + 無 session-tail override → **移除每一個讓繁中穩定的營運防護**。
- 實證：llms-get-lost 多輪 adherence 衰退 +112%、無 front-load consolidation 僅 15-20% 復原；beyond-context-window compaction 毀 ~25% constraint-class（語言 register 正是此類）；Lost-in-the-Middle HEAD 最可靠。
- 現有 harness 正確把「繁體中文優先」放第一 token、session-tail override 標 IMPORTANT、CJK split、compact hint 保留繁中——全 production grounded（Lesson 2026-06-07-G）。
- **值得採 2 點**：sub-agent handoff 顯式寫 rules（語言繼承）+ post-compact re-anchor。

### 3.3 opus（workspace 彈性架構）— **決定性結論**
- 兩版**反方向失敗**：ChatGPT 5.5 供 superior typed scaffold 但**全盤省略 substrate**；Zeuik 接線每元素但缺 typed backbone。
- **融合 backbone**：開頭放四 runtime 能力，把 SKILLS→tool-interface / AGENTS→agent-loop / HOOKS→deterministic-control / refs→context-management 映上去；ONE task-calibrated Task-Contract（加 [mode:] 欄）；ETCLOVG 為共用失敗詞彙；5-tier 綁 HOOK；保留 pilot 路由 / refs 分層 / byte-cap / inline-mirror。

### 3.4 opus 對抗稽核（補 fable 缺口）— **推翻 synth 多項過度樂觀**
| 規則 | 對抗 verdict | 理由 |
|------|------|------|
| R1 Runtime Contract（+290B）| **REVISE 壓縮 / DEFER** | Half-A 是 CLAUDE.md:8 複述；workspace mapping 是「可推導=噪音」(core.md:47)；唯一淨值 = framing 句。+290B 破硬 cap。 |
| R2 ETCLOVG（+60B）| **REVISE 縮到 ~20B refs 指針** | core.md:58 已有「失敗歸因到層」；7 詞 taxonomy 屬 refs 不屬 auto-load。 |
| R3 Task-Contract（Handoff）| **KEEP（最強）** | grep 確認 subagent-strategy 無 Goal/Done-when/Allowed-paths → 真淨新增、有真實失敗背書（Lesson 2026-06-04-C/2026-06-14-A 子產物落錯 worktree）。**但「~0B」是假的**，實際 +150-250B。 |
| R4 繁中 compact 第 4 項（+35B）| **DROP** | 繁中 after-compact 已在 core.md:9 + context-management:11 兩處 → 第 3 份重複；**Lesson 2026-06-07-G 已證純文字強化無效**，R4 正是被記為無效的動作。 |
| R5 SafeHarness 5-tier | **REVISE 去重** | path-scoped cap-free，但與既有 No-Commit/Boundary/destructive 三列重複 → 第 4 列「矛盾不混用」陷阱（core.md:70）；「HOOK enforced」overclaim。 |

## 4. 關鍵裁決議題（對抗稽核浮現）

### 4.1 byte cap — **不上調**（紅線）
- synth 提「(a) 上調 cap 到 19,200」**直接違反 core.md:79**（「不接受為塞單一新規則反推湊 byte」）→ **移出選項**。
- 主對話親測：**18,713/19,000 = 287B headroom**（canonical 六源；MEMORY 記的 18,967 已過時）。
- 正解：**defer/refs-pointer R1 + 每 cycle ≤1 壓縮規則**（core.md:80）。

### 4.2 不可一次落 5 規則
- core.md:80 = ≤1 規則/cycle、≤50 行 diff。crossbred-as-drafted **獨立於 byte 數即違反 autoload-evolution gate**。
- **落地優先序**：R3（真 gap，ChatGPT 5.5 authored — 須 credit）> R1-壓縮或 defer > R2-refs 指針 > R5-去重。**R4 DROP**。

### 4.3 home-team bias 校正
opus 對抗稽核抓出 synth「crossbred beats both」有 home-team 味。ChatGPT 5.5 被低估 3 處：
1. **R3 Handoff Contract — ChatGPT 寫得更好**（顯式 Non-goals + Allowed-paths + Return-format，現有 workspace 全無）→ R3 ~90% 是 ChatGPT 內容，須 credit。
2. **codex「delta updates over full rewrites」+「commit only when user asks」** 比現有更銳利（現有 core.md:95「改動完成 YOU MUST git add」可能 over-commit）。
3. **結構簡潔/maintainability 軸**（core.md:34 四軸品質之一）favor ChatGPT 更多——現有 harness 累積了 rewrite 已 shed 的 clutter。
- **修正結論**：「crossbred beats both」應降為「**僅當採 ChatGPT 結構（R3/R5）+ 守既有 byte-cap governance 時** crossbred 才勝；as-drafted 違反 cap + cycle gate，比兩個 parent 都差**直到修正**」。

## 5. 融合規則最終草案（經對抗稽核修正）

> **原則**：採 ChatGPT 5.5 最佳 typed 結構**僅在 pilot+論文確認價值處**；保留 Zeuik 防過真實失敗的 grounding；嚴守 byte cap 不上調 + ≤1 規則/cycle。

### 落地優先序（建議分 cycle）

**Cycle 1（最高價值，建議先做）— R3 Task-Contract / Handoff**
- 落 `.claude/rules/subagent-strategy.md`。採 ChatGPT 5.5 的 Handoff Contract（Goal/Non-goals/Allowed-paths/Context/Done-when/Return-format）+ Zeuik 加 `語言模式:繁中` 欄 + `[mode:]` 路由欄；標 task-calibrated（非靜態）。
- 失敗模式：MAST spec-ambiguity = #1 MAS failure；子產物落錯 worktree（Lesson 2026-06-04-C/2026-06-14-A）。
- byte：實際 +150-250B（非 synth 的「~0B」）→ 須先壓 subagent-strategy 或核可上調以外的取回。

**Cycle 2 — R1 Runtime Contract（壓縮版或 refs 化）**
- 若 ≥250B headroom：壓縮版（~200B blockquote，去 Half-A 複述 + workspace mapping，僅留四能力 framing + 「更長 prompt ≠ 更好 harness」）。
- 若 <100B：refs 指針（≤40B：`> Harness=loop+tools+context+control 四能力（見 refs/harness-loop.md）`）+ 全文入 refs。

**Cycle 3 — R2 ETCLOVG refs 指針**
- core.md:58 末加 `（七層詞彙見 refs/harness-loop.md）`（~+20B），全 7 層入 refs。

**R5 — security-hygiene 去重融合**
- path-scoped（cap-free）。採 escalation ladder *概念*，tiers 折進既有結構（不另立第 4 列），不 overclaim HOOK enforcement。

**R4 — DROP**（繁中第 3 份重複，違反 Lesson 2026-06-07-G）。

### Open-question triage（對抗稽核）
| 議題 | triage | 理由 |
|------|------|------|
| model-switching-as-control | **HIGH_VALUE** | CLAUDE.md:22 Fable→Opus fallback + 本 session Fable 不可用實證 = 已依賴的 control，形式化有失敗背書 |
| memory write-gate | **HIGH_VALUE** | 多次污染記憶寫入（Lesson 2026-06-04-D / 2026-06-14-C；Fable Ex3 自欺寫入 memory）；落 memory-compactor SKILL（zero auto-load） |
| verification-stringency-scales | **ACADEMIC_DEFER** | 無「強模型需更少驗證反被燒」的真實失敗；推測性 |

## 6. 繁中 + workspace 彈性最終判定（回答使用者 2 問）

**(a) 哪版繁中更好？** — **現有 Zeuik 決定性勝**。ChatGPT 5.5 全英文 rule body 會在 session 後段/compact 後**量測上衰退繁中遵從**（auto-load prefix 是語言模式主錨點；Lesson 2026-06-14-G）。融合策略：**rule 檔保持繁中**，僅採 ChatGPT 的 handoff 顯式化 + post-compact re-anchor。

**(b) 哪版 workspace 彈性更高？** — **融合版勝**。ChatGPT 5.5 的 typed backbone（四能力 + ETCLOVG + Task-Contract + 5-tier）是讓 29-skill/18-agent substrate **可組合**的 typed schema；但它**全盤省略 substrate 會 flatten**。把 Zeuik 已驗證 substrate（pilot 路由 / RESOLVER / refs 分層 / inline-mirror / byte-cap）**掛上** ChatGPT 5.5 的 backbone → 嚴格比兩個 parent 都更有彈性。

## 7. 殘留風險與下一步

- **未套用**：本報告為交付物，融合規則**未動 auto-load**（守先報告後裁決）。套用走 `/autoload-evolution` gated loop，每 cycle ≤1 規則。
- **byte 取回前提**：R3 落地需先壓 subagent-strategy 取回 ~200B，或從別處壓——**不上調 cap**。
- **Fable 不可用**：對抗稽核由 opus 代行；若 Fable 恢復，可重跑 adversarial phase 交叉驗證（非必要，opus 稽核已 grounded）。
- **驗證狀態**：3 核心論文錨點主對話親 grep 驗證 exit=0；byte canonical 六源重測；對抗稽核推翻 synth 過度樂觀項。healthcheck 待 commit 前跑。
