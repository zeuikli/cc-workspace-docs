---
title: "Auto-load 完整測試框架藍圖 + 多輪修正計劃"
date: 2026-06-04
status: 藍圖 + 安全機械缺口本 session APPLY；R1-R12 打包 gate out-of-band
btw: 規劃 auto-load 在不影響效能/功能下完整測試 + 調整
decision: 先建測試能力 -> gated 調整（使用者定奪）
goal: 依報告 + Harness Loop 多輪修正直到全部 auto-load 修正完畢
type: blueprint + execution-plan
---

# Auto-load 完整測試框架藍圖 + 多輪修正計劃

> 走 Harness Loop。**核心修正**（advisor 校準）：建測試**只 stage protection 不 deliver**——R1-R12 遵守度 eval 不可 inline（須 per-model fresh session + sandbox），故 loop 終止條件**不可定義為「R1-R12 re-encoded」**。

---

## 0. Loop 終止條件（§R4，機械可驗證）

「全部 auto-load 修正完畢」**字面詮釋會指回剛 DEFER 的 §R re-encode**（grep-only 驗證不足）。終態**重定義**為三條件全綠：

| # | 終止條件 | 機械驗證 |
|---|---------|---------|
| T1 | 機械 test gates 就位且綠 | `measure.sh` byte gate exit 0 + §R header 存活檢查 PASS + healthcheck FAIL=0 |
| T2 | 無待修事實錯誤 | grep 確認 κ/cache/stale 已修（#451 + 本輪）|
| T3 | R1-R12 re-encode **打包**（非執行）| 計劃書 D1-D4 before/after + danger-table 就緒，明確 block 在 out-of-band eval + user gate |

**不接受**「直到所有 §R 條文都 re-encode」當終止——那是 hacked goal（用不足驗證換 byte，違 adherence-first 研究結論 + advisor）。

---

## 1. 既有測試資產（OBSERVE，researcher 盤點 + 主對話抽驗 4/4 屬實）

| 資產 | 功能 | 覆蓋維度 | 可 inline？ |
|------|------|---------|-----------|
| `healthcheck.sh` | 13 section 結構健檢（PASS 108/WARN 3/FAIL 0）| 功能（@ 連結/CLAUDE.md 行數/on-demand 路徑）| ✅ |
| `measure.sh` | byte 量測 + 三段門檻文字 | 功能（byte）| ✅ 但**無 exit gate** |
| `measure-cache.sh` | cache_hit_rate（jq 確定性聚合）| 效能（cache）| ❌ 須 live transcript |
| `eval-score-behavioral.sh` | task07/08 確定性 scorer | 遵守度 | ✅ scorer / ❌ transcript 須 out-of-band |
| `test-block-dangerous.sh` | hook allow/block 單元測試 | 功能（hook 行為）| ✅ |
| task-01..06（PGE）| 規則知識/修改/分析 eval | 遵守度 | ❌ LLM 評分須委派 |
| task-07/08 + RUNBOOK | ask-rate/fan-out behavioral | 遵守度 | ❌ 須 per-model fresh + sandbox |
| cold-start hook 數字 | 7 hooks 實測 ms（一次性）| 效能 | ❌ 無可重跑腳本 |

---

## 2. 缺口（IDENTIFY，scope 限 §R 外安全機械項）

advisor 校準：大部分能力**已存在**，只補真缺口，**不重建** eval harness。

| 缺口 | 嚴重 | 本 session？ | 落點（離 hot path）|
|------|------|------------|------------------|
| G-A：`measure.sh` 無 byte cap exit gate | 中 | ✅ APPLY | measure.sh 加 exit 斷言 |
| G-B：§R1–§R12 header 存活無自動驗證 | 中 | ✅ APPLY | **measure.sh / standalone**（**不放 healthcheck**——已佔 pre-commit 96%，違「不影響效能」）|
| G-C：hook 計時無可重跑腳本 | 低 | ✅ APPLY | standalone `scripts/measure-hook-timing.sh`（不 wire 進 hook）|
| G-D：task-07/08 verdict 未跑 | 中 | ❌ out-of-band | RUNBOOK 既有；須 instrumented session |
| G-E：auto-load 載入延遲量測 | — | ❌ **不建** | cold-start 已證 auto-load 非瓶頸（cache->0.1×），建它是測非瓶頸 |

**「不影響效能」字面遵守**：① 新結構斷言**不入任何 hook**（off hot path）；② auto-load 非效能槓桿（cold-start 既證）-> 「不影響效能」近乎免費，因為 auto-load 本就不是 lever。

---

## 3. 多輪修正計劃（PROPOSE -> 逐輪 Harness Loop）

### Round 1 — 建安全機械 gate（§R 外，本 session）

- **R1.1 G-A**：measure.sh 末尾加 `if total > 19000: exit 1`（CI gate；保留 informational 輸出）。
- **R1.2 G-B**：建 §R header 存活檢查——驗 core.md 含 §R1-R5/§R7-R12（11）+ context-management 含 §R6。放 measure.sh 新 section 或 standalone。
- **R1.3 G-C**：建 `scripts/measure-hook-timing.sh`——可重跑量測 7 hooks ms（標方法學：n/dummy stdin/cache 狀態，依 Lesson 2026-06-03-C）。**不 wire 進 hook**。
- **驗證**：三腳本各自跑通 + healthcheck FAIL=0 不變 + measure.sh byte gate 對 18,455 exit 0、對 >19000 exit 1（注入測試）。

### Round 2 — 終態確認（T1/T2 機械驗證）

- 跑全 gate 確認綠；grep 確認無待修事實錯誤（κ/cache/stale）。
- 量測新腳本對 pre-commit 效能 delta（證 §R 外 standalone 不影響 hot path）。

### Round 3 — R1-R12 打包（T3，非執行）

- 確認計劃書 D1-D4 before/after + danger-table 就緒（已在 2026-06-04-r1r12 計劃書）。
- 明確標：execute 須 instrumented session（task-07/08 fresh run）+ 一次一條（≤1 規則/cycle）+ user gate。
- **本 session 不執行任何 §R 編輯。**

---

## 4. Falsifiable Prediction（Round 1）

**改動**：建 3 個 §R 外 standalone/measure.sh gate（不碰 auto-load 內容、不碰 hook/settings）。

**預測**：
1. measure.sh 對現況（18,455）exit 0；注入 >19,000 樣本 exit 1；
2. §R header 檢查對現況 PASS（11 + R6）；注入刪 header 樣本 FAIL；
3. hook 計時腳本可重跑，輸出含方法學標注；
4. healthcheck FAIL == 基線（0）；新腳本**不入 hook** -> pre-commit 效能 delta = 0；
5. auto-load 5 檔內容 byte **不變**（18,455）——本 round 只加測試，不改 auto-load。

**REFUTED 處置**：任一失守 -> 修腳本（非改 auto-load）；腳本無法達標 -> 回報不硬塞。

---

## 5. 不做什麼（範圍界線）

- ❌ 不執行任何 §R1-R12 re-encode（驗證不足 + 須 out-of-band + user gate）
- ❌ 不 wire 新檢查進 hook/settings.json（cold-start §5 gated scope；違「不影響效能」）
- ❌ 不建 auto-load 載入延遲量測（測非瓶頸，cold-start 已證）
- ❌ 不重建既有 eval harness（scorer/RUNBOOK 已存在）
- ❌ loop 不以「§R 全 re-encode」為終止（hacked goal）

---

## 6. 2026-06-05 增量併入（gap-vote 三技能共識，3 真 gap）

> **方法**：gap-vote（research-hub / overnight-research / autoresearch:reason 並行）對近期 corpus 找未併入 gap，2/3 共識 + **主對話親自 grep 重驗 verbatim**。本藍圖分得「測試框架 / observability / telemetry」相關 gap。皆為**未來 gated 增建的論文接地**，非本 loop 立即執行（本 loop 終態 T1/T2/T3 已綠）。

### 補充 G-F：telemetry 讀寫不對稱可抓 pass-rate 抓不到的靜默 bug（HARBOR，arXiv:2604.20938）

**對 §2 缺口分析（observability）的補完**：現有 gate（measure.sh `--gate` / healthcheck）驗「byte / §R header / 結構」，但無「行為層 telemetry」。HARBOR 提供一個 pass-rate 看不見的 bug 偵測模式：

**接地審計**：
- telemetry 模式 ← "**Telemetry counters**: cache_hits, token_savings, reflections_written, reflections_retrieved, predictions_fired — enables silent bug detection via read/write asymmetry."（2026-04-22-harbor-automated-harness-optimization-2604-20938.md L100）
- 實例 ← "`reflections_written=80, reflections_retrieved=0` -> container non-persistence"（同檔 L126）
- 安全約束 ← "HARBOR's safety constraint (posterior chance constraint) is directly analogous to `autoresearch`'s Guard: discard changes whose lower bound violates the safety margin."（同檔 L165）

**啟示**：未來若建 memory/skill 用量遙測（如 MEMORY 寫入 vs 召回計數），讀寫不對稱（written>0 但 retrieved=0）能抓出「寫了沒人讀 = 孤兒」的靜默缺陷——正是 MEMORY Lesson E「manual-read ref 孤兒 = 死重」的可遙測化。**落點**：非本 loop（須先有遙測基礎設施），記為 G-D 類 out-of-band 增建。

### 補充 G-G：harness 改進需 structured semantic observability（AHE，arXiv:2604.25850）

**對 OBSERVE 階段的學術接地**：

**接地審計**：
- 定義 ← "Observability is not just logging — it is structured semantic tracing that enables systematic harness improvement. Without observability, harness engineering is artisanal; with it, it becomes engineering."（2026-04-30-ahe-observability-driven-harness-2604-25850.md L163）
- 量化 ← "ten AHE iterations improved pass@1 from 69.7% to 77.0%"（同檔 L24）

**啟示**：本藍圖的 measure.sh/healthcheck 屬「功能/結構」可觀測，但 §R 遵守度（behavioral）仍須 out-of-band per-model session（T3 已 defer）。AHE 印證「無結構化語意追蹤 -> harness 改進是手工藝」——強化 G-D（task-07/08 behavioral verdict）的必要性，但不改本 loop 終態判定。

### 補充 G-H：自動化 skill 學習有 ~30% 天花板，人寫 gate 不可省（SkillLearnBench，arXiv:2604.20087）

**對「測試什麼 / 誰來 gate」的接地**：

**接地審計**：
- `~30%` ceiling vs `74.50%` human ← "Human-authored skills: 74.50%. Automated skill-learning methods: ~30% (ceiling)."（2026-04-22-skill-learn-bench-continual-skill-learning-2604-20087.md L20）
- 外部回饋 > 自我回饋 ← "External feedback outperforms self-feedback for skill refinement."（同檔 L20）

**啟示**：呼應本藍圖核心修正「測試只 stage protection 不 deliver，§R re-encode 須 user gate」——**自動化（self-feedback）有上限，人類 gate（external feedback）是品質來源**。直接背書「§R 調整一次一條 + user gate」的設計，非過度保守。

*增量併入日期：2026-06-05 | gap-vote 3 真 gap（HARBOR-telemetry / AHE-observability / SkillLearnBench-human-gate）| 全數主對話親自 grep 接地 | 皆 out-of-band 增建接地，不改本 loop 終態（T1/T2/T3 仍綠）*
