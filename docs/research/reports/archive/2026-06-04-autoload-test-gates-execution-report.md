---
title: "Auto-load 測試 gate 建置執行報告（Round 1-3）"
date: 2026-06-04
status: 終態三條件全綠（T1/T2/T3）— loop 達終止
branch: feature/autoload-test-gates
companion: 2026-06-04-autoload-test-framework-blueprint.md
goal: 依報告 + Harness Loop 多輪修正直到全部 auto-load 修正完畢
type: execution-report
---

# Auto-load 測試 gate 建置執行報告（Round 1-3）

> Harness Loop 多輪修正。loop 終止條件（§R4 機械可驗證）：T1 gate 就位且綠 + T2 無待修事實錯誤 + T3 R1-R12 打包（非執行）。
> **「不影響效能/功能」字面達成**：auto-load byte 不變（18,455）+ 新腳本確認離 hook hot path。

---

## Round 1 — 建安全機械 gate（§R 外，APPLY）

### R1.1 + R1.2 — measure.sh 加 `--gate` CI 模式（G-A byte cap + G-B §R 存活）

- **設計**：opt-in `--gate` flag。預設行為**完全不變**（exit 0，informational）——零破壞既有 caller（INDEX.md/settings 白名單；確認 measure.sh **不在任何 hook**）。
- **G-A**：總 byte >19,000 -> `GATE_FAIL+1`。
- **G-B**：core.md §R header != 11 或 context-management 無 §R6 -> `GATE_FAIL+1`（偵測規則檔截斷）。
- `--gate` 且 `GATE_FAIL>0` -> exit 1 + "GATE FAIL"；否則 "GATE PASS"。

### R1.3 — `scripts/measure-hook-timing.sh`（G-C 可重跑 hook 計時）

- standalone，**不 wire 進 hook**（離 hot path）。dummy stdin / n=3 median / 標方法學（Lesson 2026-06-03-C）。
- **重現 cold-start 報告數字**（驗證可信）：pre-commit-review 2805ms（報告 2965）/ session-init 566ms（592）/ user-prompt-submit 126ms（146）/ block-dangerous 51ms（53）。
- **新發現**（OBSERVE 副產品，不擅自優化 §R3）：`session-stop.sh 3520ms`（cold-start 報告未列）。記錄供後續評估。

---

## TEST（展示真實輸出，前/後）

### Falsifiable Prediction 5/5 通過

```
P1 measure.sh --gate 現況 exit=0；注入 19001 分支 FAIL+1 ✓
P2 §R 條文存活: ✅ core.md 11/11 + context-management §R6 ✓
P3 hook 計時可重跑 + 方法學標注 ✓
P4 healthcheck 統計：PASS 108 / WARN 3 / FAIL 0（== 基線）；新腳本不在任何 hook（hot path delta=0）✓
P5 auto-load byte: 18455 total（不變）✓
```

### 端對端 gate 真能 FAIL（R9 假測試防範，advisor 攔截補驗）

> advisor 指出：只驗 PASS 路徑 + 隔離 detection 邏輯 ≠ 整合腳本真 exit 1。補端對端注入故障：

```
測試 A（破壞 §R1 header）：
  破壞後 §R count: 10 -> measure.sh --gate exit=1 + "GATE FAIL" ✓
  git checkout 還原後 §R count: 11 ✓
測試 B（注入 >cap byte，19066）：
  measure.sh --gate exit=1 + "GATE FAIL" ✓
  git checkout 還原後總 byte: 18455 ✓
```

-> gate 是**真的**，非裝飾性。auto-load 檔乾淨還原。

---

## 終態判定（§R4，loop 終止）

| 終止條件 | 機械驗證 | 結果 |
|---------|---------|------|
| **T1** gate 就位且綠 | `measure.sh --gate` exit 0 | ✅ GATE PASS |
| **T2** 無待修事實錯誤 | auto-load κ 誤用 0 處 / cache 0.94 0 處 | ✅ 已修（#451 + 本 session）|
| **T3** R1-R12 打包（非執行）| 計劃書 8,887 B 含 danger-table gate + before/after（PR #450）| ✅ 就緒，block 在 out-of-band eval + user gate |

**三條件全綠 -> loop 達終止。** 不繼續硬塞 §R re-encode（「完畢」≠「§R 全 re-encode」，那是 hacked goal；使用者已選「先建測試再 gated 調整」defer §R）。

---

## 「不影響效能 / 功能」達成證明（btw 核心要求）

- **效能**：① auto-load byte **18,455 不變**（只加測試腳本，不改 auto-load 內容）；② 新 gate/計時腳本**確認不在任何 hook**（`grep -rl .claude/hooks/` 零命中）-> pre-commit/session hot-path delta = 0；③ auto-load 本就非效能瓶頸（cold-start 既證 cache->0.1×）。
- **功能**：① measure.sh 預設行為不變（opt-in `--gate`）-> 既有 caller 零影響；② healthcheck FAIL=0 == 基線；③ §R 條文 11/11 存活。

---

## RECORD

- 新增：`scripts/measure-hook-timing.sh`（可重跑 hook 計時 baseline）。
- 修改：`scripts/measure.sh`（+`--gate` CI 模式，預設不變）。
- 文件：本報告 + blueprint。
- **下一 gated session**（R1-R12 execute，非本 loop 範圍）：須 instrumented session 跑 task-07/08 behavioral verdict（out-of-band，per-model + sandbox）+ 一次一條（≤1 規則/cycle）+ before/after 逐句語義核對 + user gate。

### 保留待辦

- R1-R12 §R re-encode（D1-D4）：block 在 out-of-band eval + user 核准。
- `session-stop.sh 3520ms` / `pre-commit-review 2805ms`：hook 效能（非 auto-load，獨立 gated scope，cold-start §5）。
- gate wiring 進 pre-commit/CI：settings 變更 = 獨立 gated scope（本 loop 明確不做）。

---

## 不做什麼（範圍守住）

- ❌ 不執行 §R1-R12 re-encode（loop 不以此為終止；hacked goal）
- ❌ 不 wire gate 進 hook/settings（違「不影響效能」+ 獨立 gated scope）
- ❌ 不優化 session-stop/pre-commit hook（非 auto-load，§R3 範圍外）
- ❌ 不建 auto-load 載入延遲量測（測非瓶頸）

---

## 2026-06-05 增量併入（gap-vote 三技能共識，1 真 gap）

> **方法**：gap-vote 三角色並行找未併入 gap，2/3 共識 + **主對話親自 grep 重驗 verbatim**。本執行報告分得「byte cap 設計正當性」相關 1 條。**不改本報告終態判定**（T1/T2/T3 仍綠），僅補 measure.sh byte cap（vs token 門檻）設計選擇的論文接地。

### 補充：byte cap 對 tokenizer 變更免疫——measure.sh `--gate` 用 byte 而非 token 是正確選擇（Opus 4.7 card，arXiv 系統卡）

**對 G-A（measure.sh byte cap exit gate）設計選擇的接地**：本報告 R1.1 的 G-A 用「總 byte >19,000」而非「token >N」當 gate 條件。Opus 4.7 system card 揭露此選擇的隱性優勢：

**接地審計**：
- tokenizer 變更 ← "Same input produces **1.0–1.35× more tokens** vs Opus 4.6 (content-dependent)"（2026-04-16-claude-opus-4-7-system-card.md L86）
- 遷移指引 ← "Migration note: retest token budgets and cost estimates before upgrading"（同檔 L87）

**啟示**：若 G-A 以 token 門檻為 gate，模型升級換 tokenizer 時相同 auto-load 內容的 token 數會漂移（最壞 ×1.35），導致 gate 在無內容變更下誤觸或失效，且每次升級須 retest。**byte（`wc -c`）對 tokenizer 完全免疫**——auto-load 內容字元數不隨模型變。-> workspace「canonical 單位 = byte」（core.md §Framework Integrity）+ measure.sh byte gate 的設計，在模型升級韌性上優於 token-based gate。此為本 loop 既有設計的事後論文背書，**非新增測試**。

*增量併入日期：2026-06-05 | gap-vote 1 真 gap（byte-cap tokenizer 免疫）| 主對話親自 grep 接地 | 不改本報告終態（T1/T2/T3 仍綠），僅補設計選擇接地*
