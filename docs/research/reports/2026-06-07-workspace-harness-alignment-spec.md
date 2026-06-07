---
title: "Workspace Harness Alignment 規格書"
date: 2026-06-07
status: PROPOSED — 待使用者核准後執行
disposition_authority: 破壞性項（routing 改動）→ core.md APPLY gate；非破壞性項可即執行
source: 全 workspace 盤點（兩路 researcher + 主對話親驗）
type: alignment-spec
---

# Workspace Harness Alignment 規格書

> **目的**：讓全 workspace 的檔案都依循 CLAUDE.md / AGENTS.md / The Loop 六階段準則。
> **核心紀律**：本規格書是 PROPOSE 產物，非授權執行。每條標「即執行」或「待核准」。
> **方法**：兩路 researcher 並行盤點 → 主對話親驗關鍵數字 → 規格書 → AskUserQuestion → APPLY。

---

## 第零節：盤點方法與誠實邊界

### 0.1 盤點覆蓋範圍

| 維度 | 盤點內容 | 工具 |
|------|---------|------|
| A | 27 SKILL.md 格式合規（frontmatter / description 雙段 / 行數）| researcher + grep |
| B | 19 hooks exit code 語義正確性 | researcher + grep |
| C | AGENTS.md §2 dispatch vs agents/ 目錄一致性 | researcher + ls |
| D | AGENTS.md §6 refs dead link | researcher + ls |
| E | RESOLVER.md Quick Reference vs AGENTS.md §6b naming 一致性 | researcher + grep + 主對話 diff |
| F | research/ INDEX.md 新鮮度（16 子目錄）| researcher + ls |
| G | MEMORY.md 行數健康 | wc -l |
| H | auto-load bytes 健康 | wc -c 親驗 |

### 0.2 親驗修正（unverified_success 閘門）

| researcher verdict | 主對話親驗 | 修正 |
|-------------------|-----------|------|
| auto-load 餘裕 72B（MEMORY 記錄值）| 實測 18,984/19,000 = **餘裕 16B** | MEMORY 記錄過時，飄移 56B，需更新 |
| RESOLVER 缺 `skill-evolution` 行 | grep 確認：QR table 無此行，§Harness 段有子命令列 | 屬實，QR table 需補 1 行 |
| AGENTS §2 缺 `self-escalate` | grep AGENTS.md 無輸出 | 屬實，agents/ 有但 §2 未登錄 |

---

## 第一節：盤點結論總覽（三類判定）

| 類別 | 數量 | 處置 |
|------|------|------|
| ✅ 設計正確，不動 | 4 項 | 記錄佐證 |
| 🟡 輕微 gap，非破壞性修正 | 4 項 | **即執行**（≤10 行改動）|
| 🔴 中型 gap，需設計決策 | 2 項 | **待核准** |

---

## 第二節：✅ 設計正確項（不動）

### C2 — AGENTS.md §6 refs 全存在
AGENTS.md §6 cross-reference 表的 12 個 refs 全部實際存在。**無 dead link。**

### B1 — Hooks exit code 語義全正確
- PreToolUse block → `exit 2` ✓（block-dangerous / protect-sensitive-files / pre-compact / pre-commit-review）
- PostToolUse / Stop → `exit 0` ✓
- memory-sync.sh `exit 1`（line 44）= dead code（ADR 停用後 `exit 0` 在 line 17 早返回），**不影響行為** ✓

### F1 — research/ INDEX.md 新鮮度正常
16 個子目錄中 15 個有 INDEX.md，最舊為 2026-06-01（6 天前），全在 30 天內。

### G1 — MEMORY.md 健康
98/200 行（49%），無需 compactor。

---

## 第三節：🟡 即執行項（非破壞性，≤10 行）

### FIX-1：RESOLVER.md Quick Reference table — 補 `skill-evolution` 行

**問題**：`skill-evolution` 在 AGENTS.md §6b 有列，但 RESOLVER.md Quick Reference table（第 1–40 行）完全缺席。§Harness 段（第 223-225 行）有子命令列，但 Quick Reference 找不到。

**影響**：使用者查 RESOLVER 找不到 skill-evolution 入口，發現性為 0。

**修正**：在 RESOLVER.md Quick Reference table 補 1 行，置於 `autoload-evolution` 之後：

```
| `skill-evolution` | SKILL 品質評分（7 維）· Gap 改進 · 格式稽核 | `skill-evolution:scan`、`skill-evolution:apply <name>`、`skill-evolution:audit` |
```

**驗收**：`grep "skill-evolution" RESOLVER.md | grep "^|"` 有輸出。

---

### FIX-2：RESOLVER.md Quick Reference — 統一 skill 名稱（alias 補標）

**問題**：Quick Reference table 用縮寫（`media-r` / `media-t` / `security`），AGENTS.md §6b 用全名（`media-research` / `media-transcribe` / `security-compliance`）。使用者在兩處看到不同名稱會混淆。

**細節**：
- `media-r`：RESOLVER §166 有 alias 說明行，但 Quick Reference table header 未標全名
- `media-t`：無 alias 說明
- `security`：最嚴重——RESOLVER QR 只有 `security`（trigger `—`），AGENTS 對應的是 `security-compliance`（trigger `/security-compliance`）

**修正**（3 行 in-place 改動）：

```diff
- | `media-r` | 媒體研究（Twitter/X 分析、YouTube 報告、GitHub 抓取）| ...
+ | `media-research` / `media-r` | 媒體研究（Twitter/X 分析、YouTube 報告、GitHub 抓取）| ...

- | `media-t` | Twitter/X + YouTube 影片轉逐字稿 + 摘要 | ...
+ | `media-transcribe` / `media-t` | Twitter/X + YouTube 影片轉逐字稿 + 摘要 | ...

- | `security` | 資安合規 | — |
+ | `security-compliance` / `security` | 資安合規 · ISO 27017 · GCP 安全控制 | `security-compliance:audit`、`security-compliance:evidence` |
```

**驗收**：`grep "media-research\|media-transcribe\|security-compliance" RESOLVER.md | grep "^|"` 3 行有輸出。

---

### FIX-3：AGENTS.md §2 — 補登 `self-escalate` agent

**問題**：`.claude/agents/self-escalate.md` 存在，但 AGENTS.md §2 dispatch table 完全未列，使用者翻 AGENTS.md 找不到此 agent。

**影響**：self-escalate 是失敗收斂關鍵 agent（同類任務失敗 ≥3 次觸發），若使用者或 parent agent 讀 AGENTS.md 找不到，會繼續重試而非升級。違反 IDENTIFY 階段「顯露假設」原則。

**修正**：AGENTS.md §2 table 補 1 行：

```markdown
| 同類任務失敗 ≥3 次 / 是否繼續 vs 升級判斷 | `self-escalate` | Sonnet 4.6 | 分析當前任務狀態，輸出 JSON convergence verdict | 重試、實作、code review |
```

**驗收**：`grep "self-escalate" AGENTS.md` 有輸出。

---

### FIX-4：MEMORY.md — 更新 auto-load bytes 記錄

**問題**：MEMORY.md 記錄 auto-load 餘裕 72B，實測 18,984/19,000 = 餘裕 **16B**，飄移 56B。

**影響**：下次任何人讀 MEMORY 評估是否可增補 auto-load，會基於錯誤數字（72B）做判斷，實際只有 16B 可用。

**修正**：更新 MEMORY.md 待辦節中「19,000 近滿監控」一行：

```diff
- [ ] **19,000 近滿監控**：~~餘 45~~ → **餘 545**，下次 auto-load 增補前重新評估
+ [ ] **19,000 近滿監控**：實測 18,984/19,000，**餘裕 16B**（2026-06-07 量測）。任何 auto-load 增補前必先壓出空間。
```

**驗收**：`grep "16B\|18,984" MEMORY.md` 有輸出。

---

## 第四節：🔴 待核准項（需設計決策）

### DESIGN-1：overnight-research/SKILL.md 行數超限（395 行 > 350）

**現況**：overnight-research SKILL.md 有 395 行（Step 0 + Phase 1-6 全在同一檔）。按 workspace 規範，非 pilot/hub skill 上限 350 行。

**兩種處置方向**：

| 選項 | 做法 | 利 | 弊 |
|------|------|----|----|
| **A. 拆出 Phase 細節**（推薦）| 將 Phase 1–6 操作細節移至 `overnight-research/references/phases.md`，SKILL.md 保留觸發/路由/參數/GOTCHA；預估 SKILL.md 壓至 ≤250 行 | 合規；SKILL.md 聚焦觸發層 | 需確認 Phase 細節讀取路徑不斷 |
| **B. 豁免列為 hub skill** | 認定 overnight-research 是「多 Phase 編排 hub」，比照 research-hub（357 行）豁免 | 零改動 | overnight-research 本質是單一流程（非多入口 hub），豁免理由較弱；設先例 |

**建議選項 A**，與 autoresearch 的 `references/` 子目錄結構一致（autoresearch 18 個 reference 文件）。

> **裁決等待**：選 A 或 B？

---

### DESIGN-2：research/scratch/ 缺 INDEX.md

**現況**：`research/scratch/` 無 INDEX.md，其他 15 個子目錄全有。

**兩種處置方向**：

| 選項 | 做法 |
|------|------|
| **A. 不建**（推薦）| scratch 是 session 暫存目錄（對應 core.md「臨時檔放 /tmp/claude-scratch/」精神），不需索引 |
| **B. 建空 INDEX.md** | 加一個說明「此目錄為 session 暫存，不索引」的佔位檔，讓 healthcheck 不報 WARN |

**建議選項 A**。但若 healthcheck 現在對此 WARN，需確認。

**驗收條件**：`bash scripts/healthcheck.sh 2>/dev/null | grep -i scratch`

---

## 第五節：執行排程

### 即執行（無需核准，非破壞性）

| # | 項目 | 改動規模 |
|---|------|---------|
| FIX-1 | RESOLVER.md 補 skill-evolution 行 | +1 行 |
| FIX-2 | RESOLVER.md 統一 3 個 skill 名稱 | 3 行 in-place 改 |
| FIX-3 | AGENTS.md §2 補 self-escalate | +1 行 |
| FIX-4 | MEMORY.md 更新 bytes 記錄 | 1 行 in-place 改 |

### 待核准（需設計決策）

| # | 項目 | 等待裁決 |
|---|------|---------|
| DESIGN-1 | overnight-research 行數超限處置 | 選項 A（拆）或 B（豁免）|
| DESIGN-2 | research/scratch/ INDEX.md 處置 | 選項 A（不建）或 B（建佔位）|

---

## 第六節：Self-Evolving 合規（The Loop 接入）

| Loop 階段 | 本規格書對應 |
|----------|------------|
| OBSERVE | 兩路 researcher 並行盤點 8 維度，主對話親驗 3 個關鍵數字 |
| IDENTIFY | 三類判定（✅/🟡/🔴），顯露假設（overnight-research 豁免理由弱） |
| PROPOSE | 本規格書；每條標類型/規模/驗收條件 |
| APPLY（gate）| 🟡 項即執行；🔴 項 AskUserQuestion 後執行 |
| TEST | 每條有 grep 驗收條件；APPLY 後跑 healthcheck |
| RECORD | APPLY 後追加 MEMORY session 節 + Lesson |

---

## 附錄：盤點數字彙整（親驗值）

| 指標 | 值 |
|------|----|
| Auto-load bytes（5 檔）| 18,984 / 19,000（餘裕 **16B**）|
| CLAUDE.md 行數 | 32 / 200 |
| MEMORY.md 行數 | 98 / 200 |
| Skills | 27 |
| Agents（agents/ 目錄）| 15（含 self-escalate）|
| AGENTS.md §2 列出 | 14（缺 self-escalate）|
| Hooks | 19 |
| RESOLVER QR table rows | 26（缺 skill-evolution）|
| overnight-research 行數 | 395（超限 +45 行）|
| media-research 行數 | 348（超限 −2 行；邊界）|
