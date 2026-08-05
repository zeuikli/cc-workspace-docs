---
title: "Harness 36 任務執行評估與計畫（The Loop gated）"
date: 2026-06-24
branch: claude/clever-einstein-571f2k
discipline: core.md The Loop（harness 自我改進 → APPLY 前置 gate）
source: research/reports/2026-06-24-harness-synthesis-from-archived-papers.md
type: execution-plan
---

# Harness 36 任務執行評估與計畫

> **OBSERVE/IDENTIFY 已完成**：gate-vote 3-lens 共識 + SIA path validity 1.0 + skill 審計（無刪除）。
> 本檔 = 執行前完整評估：readiness / 波次 / gate 要求 / 可機械驗證成功條件。
> **harness 自我改進紅線**：每項 APPLY 前 show diff，TEST 後才 RECORD；canonical 鐵律（core.md 四維等）+ conflict 項 **不執行**，待人類決策。

## Readiness 分級

| 等級 | 定義 | 動作 |
|------|------|------|
| READY | 共識 P0/P1、路徑存在、不動 canonical、無 conflict | 依波次執行 |
| GATED | 動 auto-load canonical 或 byte ceiling 風險 | 執行需 byte 親測 + 不變式檢查 |
| BLOCKED | 第 4 節 conflict / P2 | **不執行**，待人類裁示 |

## 執行波次

### Wave 1 — P0 低風險（現有檔補欄/章節，不動 canonical）→ 本輪執行
| Task | 動作 | 檔案 | 成功條件（機械） | readiness |
|------|------|------|------------------|-----------|
| T28 | autoresearch 加 block-runtime-write-.claude/skills guardrail | `.claude/skills/autoresearch/SKILL.md` | grep 到新 guardrail 句 + healthcheck PASS | READY |
| T4 | autoload-evolution:propose 加 Falsifiable Prediction 欄 | `.claude/skills/autoload-evolution/SKILL.md` | propose 段含 "Falsifiable Prediction" | READY |
| T23 | autoload-evolution 加 eval-driven regression 偵測 | `.claude/skills/autoload-evolution/SKILL.md` | 含 regression/MVES gate 句 | READY |
| T7 | LESSONS.md 加 provenance 欄慣例 | `memory/LESSONS.md` | header 含 provenance 格式說明 | READY |
| T22 | the-loop-best-solution 補 verification gate 量化模型 | `.claude/refs/the-loop-best-solution.md` | 含 0.55→0.999 幾何放大段 | READY |

### Wave 2 — P0 eval 地基 + 協調閘（部分需新檔/腳本）→ 待 Wave 1 驗證後
T2（seesaw 回歸 checklist）· T5（coreset.md，**依賴 research/evals/ 已建**）· T9（observe retrieve LESSONS/MEMORY top-N）· T12（fan-out aggregation gate）· T13（self-escalate 達標主動 stop）· T27（skill-evolution empirical eval gate）· T36（session-stop healthcheck gate 補強，**已部分存在**）。
> 註：T7/T9 原報告誤標 LESSONS.md 不存在（stale worktree）——主 tree 已驗存在，路徑正確。

### Wave 3 — P1 觀測 + context 操作化
T1/T3/T6/T8/T11/T14/T16/T19/T21/T24/T26/T30/T32/T33/T35。多為 refs 新增（on-demand 不佔 auto-load）或 hook 增量。

### BLOCKED — 待人類決策（不執行）
| Task | conflict | 待決問題 |
|------|----------|----------|
| T18 | 動 core.md 四維 canonical 鐵律 | 改走 refs/goal-engineering（T20）還是真的加第五維？ |
| T34 | PreToolUse 硬 token gate 違「行為信號優先」+ budget 為「非硬牆」 | 接受軟 warn（T30/T32）取代硬 exit2？ |
| T15 | 三票分歧（credit_horizon 投機性 vs handoff 膨脹） | 先 autoload 內部試行還是直接推 handoff？ |
| T10 | 與「child 不加確認句」鐵律 | confirmation gate 設在 parent 端（responsibility）可降衝突，確認方向？ |

### DEFER（共識 P2 淘汰）
T20（除非 T18 決策走 refs）· T25 · T29 · T31 · T17。

## Gate 流程（每項）
1. PROPOSE：show diff（最小變更，外科刀）。
2. APPLY：Edit；不動 canonical；byte 風險檔每 Edit 後 `wc -c`。
3. TEST：grep 成功條件 + `bash scripts/healthcheck.sh`（FAIL=0）+ 若動報告/eval 跑 SIA evaluate.py（overall≥0.90）。
4. RECORD：commit（清楚 message）+ checkpoint；push。

## 不變式（執行全程）
- 不動 auto-load canonical（core.md/CLAUDE.md 四維、The Loop 順序）未經 autoload-evolution + 人類 gate。
- conflict 項一律不執行。
- 每波 commit 後 healthcheck FAIL 必為 0，否則回退。

---

## 執行紀錄 + 衝突裁決（使用者「一次處理」· 2026-06-24）

### Wave 1（完成 · commit bd7d117）
T28 · T4 · T23 · T7 · T22 — 皆 on-demand，healthcheck FAIL 0、auto-load byte 18936。

### Wave 2（完成本批）
| Task | 狀態 | 落地 |
|------|------|------|
| T5 | ✅ | 新建 `research/evals/coreset.md`（10 失敗模式回歸基準）|
| T9 | ✅ | autoload-evolution Phase 1 加 1f retrieve LESSONS/PLAYBOOK + coreset |
| T2 | ✅ | harness-audit-CHECKLIST 加 Seesaw 回歸 Checklist |
| T13 | ✅ | self-escalate 補「達標主動 stop」（converged+conf≥0.85→next_action=stop）|
| T27 | ✅ | skill-evolution 加 Empirical eval gate（AAE replay = seesaw）|
| T36 | ✅ 已滿足 | session-stop.sh L309-318 已有 warn-only healthcheck gate，無需改（PROPOSE 最小化）|

### 衝突裁決（採建議方向）
| Task | 裁決 | 落地 |
|------|------|------|
| T18 | **改 refs，不動 core.md 四維鐵律** | ✅ 新建 `.claude/refs/goal-engineering.md`（= T20）；core.md 指針待 autoload-evolution gate |
| T34 | **軟 warn 取代硬 exit2**（budget 為「非硬牆」+ 行為信號優先）| 決議記錄；軟預算 warn 由 Wave 3 T30/T32 落地，**不做 PreToolUse 硬 gate** |
| T15 | **先 autoload 內部試行** credit_horizon | 決議記錄；於 autoload-evolution RATCHET 內部試行，驗證有用再推 handoff |
| T10 | **confirmation gate 設 parent 端**（responsibility 歸屬，非 child 加確認句）| 決議記錄；實作觸 subagent-strategy(auto-load) → 併入下方 autoload-evolution 提案 |

### 觸 auto-load → 統一 autoload-evolution 提案（GATED，不直接編輯）
**T12**（fan-out aggregation gate）· **T16**（intent-gate 詞彙）· **T19**（goal-restatement anchor）· **T10-impl**（parent confirmation gate）· **T18 core.md 指針** —— 全部需改 `subagent-strategy.md`/`core.md`（auto-load 六源，現 18936/19000 僅 64B headroom）。
→ 依 core.md Framework Integrity：**必走 `autoload-evolution` cycle**（≤1 規則/cycle + byte 補償 + per-task eval 回歸 + 人類 APPLY gate），**不可直接 Edit**。列為下一階段提案，本批不執行。

### DEFER（共識 P2）
T25 · T29 · T31 · T17（self-escalate node state machine：已有 next_action+bounded 終止合約，過度工程，不做）。

---

## #2 autoload-evolution 提案（ready-to-apply，下個 fresh session 套用）

> **為何不 mid-session 套**：T12/T16/T19/T10-impl 皆改 auto-load（subagent-strategy.md / core.md）。雙 gate 擋下：① byte ceiling 18936/19000 僅 64B headroom；② context-management「mid-session 禁改 auto-load」（破 prompt cache）。故走 `autoload-evolution` cycle，fresh session 套用 + byte 補償 + per-model-eval 回歸。**≤1 規則/cycle → 分 4 cycle 或合併為 1 條 pointer**。

**最 byte-efficient 策略（建議）**：4 項詳細設計已存在於 on-demand（subagent-strategy 既有段 / refs/goal-engineering.md / 本執行計畫），auto-load 僅需 **1 條合併 pointer 行**（capability-agnostic），淨 byte ≈ 0（壓一條冗長行補償）：

| 項 | auto-load 最小新增（pointer）| 詳細落點（on-demand，已存在）|
|----|------|------|
| T12 | subagent-strategy §拓撲：「parallel fan-out 後做 aggregation consistency check」一句 | 本執行計畫 + harness-audit seesaw |
| T10 | 同句併入「confirmation gate 設 parent 端（responsibility 歸屬，非 child 加確認句）」 | （釐清版）|
| T19 | subagent-strategy：「長 session 每 N 步 goal-restatement anchor（HEAD）」 | `refs/goal-engineering.md` |
| T16 | core.md APPLY：「model 發 intent → 確定性 gate 驗 → execute」一句 | `the-loop-best-solution` verification gate |

**autoload-evolution cycle 套用步驟**（fresh session）：
1. `autoload-evolution:observe` → 量 byte + 跑 baseline eval（per-model-eval + coreset）。
2. `autoload-evolution:propose` → 上表 pointer 行 + `falsifiable_prediction`（預期 byte ±0、eval 不退）+ 標壓縮補償的冗長行。
3. `autoload-evolution:apply` → 4a byte 預檢（≤19000）+ 4a-prune guard + per-task eval（任一 ≥5pp 回歸 → revert）。
4. `byte-sweep`（選用）先壓出 headroom 再加，淨持平。
> 狀態：**部分落地（2026-06-25, branch claude/optimistic-noether-d08jtm）**——
> **T12（fan-out 聚合一致性）+ T10（confirmation gate 歸 parent 端）已併入 `subagent-strategy.md`**（byte-sweep 壓 3 處純重複語補償，byte 18,936→18,998 ≤19,000；healthcheck 187/3/0 + value-check PASS + coreset 綠）。
> **修正提案假設**：原「壓 1 冗長行 → 淨 byte≈0」不成立——親測純冗餘僅 ~56B，無 ~150B 可壓；硬塞全 3 項須砍 rationale glosses（C8 over-prune），故 byte-sweep 後仍只容 T12/T10。
> **core.md cycle 判定（2026-06-25 byte-sweep 分析）**：
> - **T16 → DISCARD**：語意已被 core.md line 69「判斷 vs 決定」+ line 58「`unverified_success` 閘門（確定性 gate 絕不經 sub-agent 中介）」覆蓋；「model intent→確定性 gate 驗→execute」即此 pattern。加行 = 重複，違「只寫無法從 repo 推導」。
> - **T19 → DEFER（byte 阻擋）**：terse pointer 需 ~85B；core.md 純冗餘僅 ~38–58B 不足，硬塞須砍 line 31/70 rationale glosses（C8 over-prune）或上調 cap（Framework Integrity L79 明禁為單一規則湊 byte）。詳細已在 on-demand `refs/goal-engineering.md`（可達）。需 promotion 時走「先壓他檔騰 headroom → 再加 core.md」多 cycle campaign（fresh session + per-model-eval）。
