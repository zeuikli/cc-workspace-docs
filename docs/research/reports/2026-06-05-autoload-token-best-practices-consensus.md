---
title: "Auto-load Token 最佳實踐 — 五報告合併綜述 + gap-vote 共識"
date: 2026-06-05
status: 5 份原報告就地更新（append-only 增量段）+ 本合併報告為 SSoT 索引/綜述
branch: feature/autoload-research-merge-2026-06-05
corpus: research/papers/ 近期 76 篇 md（2025-06 起，扣已接地 9 篇）
merges: [2026-05-12-best-practices-simplicity.md, 2026-05-18-auto-load-token-best-practices.md, 2026-06-04-autoload-slimming-feasibility-research.md, 2026-06-04-autoload-test-framework-blueprint.md, 2026-06-04-autoload-test-gates-execution-report.md]
method: "gap-vote 三技能共識（research-hub / overnight-research / autoresearch:reason）+ 主對話親自 grep 接地"
new_gaps_confirmed: 13
type: consensus + index (SSoT)
---

# Auto-load Token 最佳實踐 — 五報告合併綜述

> **定位**：本報告是 5 份 auto-load/token/simplicity 主題報告的 **single source of truth 索引 + 跨報告綜述 + 2026-06-05 gap-vote 共識記錄**。原 5 份報告保留（已就地更新增量段，可追溯）；本報告不取代它們，作為導覽與最新共識入口。
> **鐵律遵守**：所有量化主張的 verbatim + 行號接地由**主對話親自 grep 重驗**（subagent verdict 非證據，MEMORY Lesson 2026-06-05-E/B）。

---

## 0. TL;DR

- **5 份報告已高度成熟**：多份在 2026-06-05 前已多輪 re-check，核心主張（auto-load ≤3,500 token / ≤19,000 byte cap、prompt caching 前綴穩定、大道至簡有下限、測試 gate 三條件全綠）穩定。
- **本次新增 13 個 confirmed gap**（gap-vote 2/3 共識 + 主對話親自驗），來自近期 76 篇 corpus 中先前未併入的論文，全數以 append-only 增量段落地對應報告。
- **無推翻既有結論**：13 gap 皆為「補強 / 量化接地 / 時間維度延伸」，不改任一報告的核心裁決（優化軸關閉、測試 loop 終態、精簡機會性執行）。
- **最高價值的 3 條新洞見**：① tokenizer 變更使 token 門檻失準 -> byte cap 設計獲背書；② 自生成 context/skill 反傷（SkillsBench −1.3pp / SkillLearnBench 人寫 74.5% vs 自動 30%）-> 人工 gate 是品質來源；③ Model Drifting -> auto-load 規則須隨模型升級重評，不可累加沿用。

---

## 1. 五報告索引（SSoT 導覽）

| 報告 | 主題 | 核心結論 | 本次新增 gap |
|------|------|---------|------------|
| [2026-05-18-auto-load-token-best-practices](2026-05-18-auto-load-token-best-practices.md) | auto-load token 上限與控制 | ≤3,500 token / 三層載入 / cache 穩定 | 7（補充 4–10）|
| [2026-05-12-best-practices-simplicity](2026-05-12-best-practices-simplicity.md) | 大道至簡 / 成本效率 | 加法思維是效率陷阱；簡潔有下限 | 5（補充 A–D + ACE 佐證）|
| [2026-06-04-autoload-slimming-feasibility-research](2026-06-04-autoload-slimming-feasibility-research.md) | 精簡可行性 | 機械可行、低優先、機會性執行 | 2（補充 8.1–8.2）|
| [2026-06-04-autoload-test-framework-blueprint](2026-06-04-autoload-test-framework-blueprint.md) | 測試框架藍圖 | 只 stage protection；§R re-encode 須 user gate | 3（補充 G-F/G-G/G-H）|
| [2026-06-04-autoload-test-gates-execution-report](2026-06-04-autoload-test-gates-execution-report.md) | 測試 gate 執行 | T1/T2/T3 全綠，loop 終止 | 1（byte-cap tokenizer 免疫）|

---

## 2. 跨報告主軸綜述（四大支柱）

### 支柱 A — Prompt Caching / 前綴穩定性

5 報告共識 + 本次接地：auto-load（CLAUDE.md + rules）是**靜態前綴**，天然適合 system-prompt-only 快取（78.5% 成本降 / 22.9% TTFT，dont-break-cache 已接地）。反模式：把 `currentDate`/session-id/mid-session tool-list 變更注入前綴 -> cache miss。本次新增 **5 階段 context shaper**（dive-into-CC）定位 auto-load 在「所有 shaper 上游」，前綴 byte × N calls 是控制大小的根本原因。

### 支柱 B — 簡潔 vs 完整的張力（簡潔有下限）

主軸已從「越簡越好」精化為「**去 redundancy ✅ ≠ 削 domain insight ⚠️**」。本次三篇獨立論文佐證下限：
- ACE：brevity bias drops domain insights（已接地）
- beyond-context-window：35:1 壓縮失 specific facts / nuanced constraints，全文 vs 壓縮差 **33.4–35.2pp**（新）
- when-better-prompts-hurt（已接地）+ prompting-inversion（已接地）：通用「更好」prompt 反傷特定任務

-> 簡潔下限 = 保留 task-critical heuristics（安全紅線、驗證指令 = TYPE A，不可壓）。

### 支柱 C — Harness / 配置 > 模型；自動化有上限，人工 gate 不可省

- blueprint-first / openai-harness-codex（已接地）：確定性 blueprint + 機械 linter > prompt 措辭。
- **本次新增**：SkillsBench（自生成 skill −1.3pp，最佳 2–3 個）+ SkillLearnBench（人寫 74.5% vs 自動 ~30% ceiling）+ AHE（structured observability 使 harness 改進從「手工藝」變「工程」，69.7->77.0%）-> **workspace「人工建 skill + skill-evolution gate + 一次一條 §R + user gate」決策獲多論文背書**。

### 支柱 D — 模型升級的時間維度（新主軸）

本次浮現的新主軸：auto-load 規則是「為特定模型世代調的 prompt」，**不可假設跨模型/跨版本沿用無損**：
- Model Drifting（PromptBridge）：跨模型沿用 prompt 最壞 −10.77pp（GPT-5->Llama HumanEval）
- tokenizer 變更（Opus 4.7 card）：相同內容 token 數 ×1.0–1.35 -> token 門檻失準，**byte cap 免疫**
- Overthinking Tax（OckBench）：per-token 費率低 ≠ 總成本低（小模型 57% 更貴）

-> 行動建議：core.md §Framework Integrity 的「移除後 Claude 在哪犯錯？」應加上「**換模型後此規則是否仍最佳？**」；token 門檻引用須標「依當前 tokenizer」。

---

## 3. Vote-Matrix（gap-vote Phase 2）+ 主對話 Evidence Audit（Phase 3）

> 三技能：research-hub（P，架構）/ overnight-research（A，新能力）/ autoresearch:reason（C，演化）。各 agent 回傳 JSON verdict + verbatim + 行號。**主對話對全部 confirm 候選親 grep 重驗**（不採信 agent verdict）。

| Gap | 論文 (arXiv) | verdict | 親驗 verbatim | 報告 grep | 落點報告 |
|-----|------|---------|:---:|:---:|------|
| SkillsBench +16.2/−1.3pp, 最佳 2–3 | 2602.12670 | confirm | ✅ L20 | 0 hits | auto-load §3.2 |
| AHE observability 69.7->77.0% | 2604.25850 | confirm | ✅ L24/L163 | 0 hits | best-practices D / test-framework G-G |
| CC 五階段 context shaper | 2604.14228 | confirm | ✅ L99-103 | 0 hits | auto-load §6 |
| back-pressure: success silent | skill-issue | confirm | ✅ L144/146 | 0 hits | auto-load §5 |
| HARBOR telemetry 讀寫不對稱 | 2604.20938 | confirm | ✅ L100/126 | 0 hits | test-framework G-F |
| ETH 138 agentfiles 14-22% | skill-issue | confirm† | ✅ L64-67 | 0 hits | auto-load §3.1 |
| AgentOpt UCB-E 62-76% | agentopt | confirm | ✅ L22/100 | 0 hits | best-practices A3 |
| OckBench Overthinking Tax 57%/5.1× | 2511.05722 | confirm | ✅ L20/65 | 0 hits | best-practices A |
| PromptBridge Model Drifting −10.77pp | 2512.01420 | confirm | ✅ L22/65 | 0 hits | auto-load §6 / slimming 8.2 |
| SkillLearnBench 人寫74.5 vs 自動30% | 2604.20087 | confirm | ✅ L20/46/133 | 0 hits | best-practices C / test-framework G-H |
| Opus 4.7 tokenizer 1.0-1.35× | opus-4-7-card | confirm | ✅ L86-87 | 0 hits | auto-load §2 / test-gates / slimming |
| faulty-memory 顯式 gate consolidation | 2605.12978 | confirm | ✅ L27 | 0 hits | auto-load §3.3 |
| 35:1 壓縮失 nuanced constraints | 2603.04814 | confirm‡ | ✅ L91/20 | 0 hits | best-practices ACE佐證 / slimming 8.1 |

† **ETH 138 agentfiles 同源去重**：與 addyosmani 論文引的 ETH Zurich 是**同一份研究**（success −2-3%/cost +20%/human +4%）。仍是 gap（5 報告先前 grep ETH = 0 hits），但標明同源、skill-issue 獨有「14-22% reasoning overhead」新切面，**不當兩篇獨立論文計數**。

‡ **35:1 語意去重**：與既有 ACE「brevity bias / 簡潔有下限」是**同一概念點**，但 beyond-context-window 提供獨立論文 + 新量化（35:1 + 33.4-35.2pp + 10-turn break-even）。**掛 ACE 段下作佐證，不開新「發現」條目**。

### Evidence Audit 表（主對話親自驗）

| Agent | 角色 | confirm 候選 | 主對話抽驗結果 |
|-------|------|:---:|------|
| Agent 1 | research-hub (P1 harness/config) | 7 | ✅ G1-G7 verbatim 全屬實；G8 compilers defer 正確 |
| Agent 2 | overnight-research (P2 context/memory) | 2 | ✅ faulty-memory L27 + 35:1 L91 屬實；defer/reject 8 條 scope 判斷正確 |
| Agent 3 | autoresearch:reason (P3 simplicity/skill) | 8 | ✅ OckBench/PromptBridge/SkillLearnBench/Opus4.7/HeavySkill/Life-Harness verbatim 全屬實 |

**全部 confirmed gap 在 5 報告 grep 命中數 = 0** -> 真 gap（非已併入）。**全部 verbatim 主對話親自 grep 屬實**（無幻覺數字）。

---

## 4. Defer / Reject Ledger（scope mismatch，不落 5 報告）

| 論文 | verdict | 原因 |
|------|---------|------|
| ACON (2510.00615) | defer | mid-session 執行時 working context 壓縮，非 session-start auto-load |
| RCR-Router (2508.04903) | defer | multi-agent role-conditioned routing，非單 session auto-load |
| Recursive LM (2512.24601) | defer | REPL-based 長 context scaffold，非 auto-load/MEMORY |
| is-grep-all-you-need (2605.15184) | reject | 檢索策略，非 auto-load/token/caching |
| delta-mem (2605.12357) | reject | 神經架構層 memory，非 harness 層 |
| agentic-memory-unified (2601.01885) | reject | agent RL 訓練框架，非 MEMORY.md 檔管理 |
| externalization (2604.08224) | reject | 已在 harness-engineering 報告引；無新量化 |
| compilers-domain (2603.20075) | defer | harness body（−60%/+22%），非 auto-load 範圍 |
| HeavySkill (2605.02396) | confirm->best-practices | 弱模型當 synthesizer（已併 best-practices A 附近，作模型選擇校準）|
| Life-Harness (2605.22166) | confirm->未落 | BM25 procedural retrieval（88.5%）—skill 動態交付，scope 偏 harness body，記此 ledger 供未來 harness 報告 |

> HeavySkill / Life-Harness 經親驗 verbatim 屬實但 scope 偏「harness body / 模型選擇」而非 auto-load 核心，未強塞 5 報告（守 R2 不湊量）；記 ledger 供未來 harness-engineering 報告。

---

## 5. 方法論誠實校準（守 R12 Fail Loud）

- **未推翻任何既有結論**：13 gap 全是補強，不改報告裁決。誠實標明本次「邊際價值在補量化接地，非主張翻新」。
- **同源/語意去重 2 條**（ETH-138 / 35:1）：grep-verify 只驗「字串不在報告」，**不驗語意是否已被別篇講過**——此盲點由 advisor 攔截，補語意重複檢查後正確標同源/掛既有段（MEMORY 新 Lesson 候選）。
- **黑名單數字防誤植**：報告內所有易混百分比（−82.6% KV cost vs −82.3% latency / 35:1 vs 33.4-35.2pp / 1.0-1.35× tokenizer / 57% Overthinking）均配 verbatim + 行號 + ⚠️ 適用範圍註記。
- **scope 守紀**：10 篇 defer/reject 未強塞（HeavySkill/Life-Harness 親驗屬實仍因 scope 記 ledger 不落報告）。

---

*合併日期：2026-06-05 | 來源：5 報告 in-place 更新 + 76 篇近期 corpus gap-vote | 13 confirmed gap（含 2 同源/語意去重標注）| 全數主對話親自 grep 接地 | gap-vote 三技能共識（research-hub/overnight-research/autoresearch:reason）*
