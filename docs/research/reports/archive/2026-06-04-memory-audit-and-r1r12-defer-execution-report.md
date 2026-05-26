---
title: "MEMORY 稽核修正 + R1-R12 計劃書 DEFER 執行報告"
date: 2026-06-04
status: 步驟1-2 APPLY / 步驟3 全 DEFER（使用者定奪）
companion: [2026-06-04-r1r12-token-efficiency-execution-plan.md]
related_prs: ["#451 (κ + cache_hit_rate SSoT 修正)"]
type: execution-report
---

# MEMORY 稽核修正 + R1-R12 計劃書 DEFER 執行報告

> 使用者指令：依序執行 ① 確認雙 MEMORY 設計意圖 -> ② 清 machine-local 過期待辦 -> ③ R1-R12 計劃書 APPLY。
> 走 Harness Loop：OBSERVE->IDENTIFY->PROPOSE->TEST->APPLY->RECORD。

---

## 步驟 1 — 雙 MEMORY 設計意圖確認（OBSERVE -> 裁決：設計如此，不對齊）

### 證據（四源機械驗證）

| 證據 | 內容 | 來源 |
|------|------|------|
| repo SSoT L3 自宣告 | 「**SSoT：跨裝置 Git 追蹤記憶；Auto Memory（Mac 本地補充）不同步**」 | `memory/MEMORY.md:3` |
| 5/31d ADR | 「三檔 MEMORY.md（#1/#2 凍結 log；#3 machine-local 真實層）確認；依 **ADR 2層模型**退場」 | machine-local L55 |
| sync-workspace.sh §13 | 只管理 `$WORKSPACE_ROOT/memory/MEMORY.md`（repo SSoT），**完全不碰 machine-local** | scripts L374-420 |
| machine-local tracked 狀態 | `git ls-files` -> **NOT tracked**（在 `~/.claude/`，repo 外） | 機械驗證 |

### 裁決

**雙 MEMORY = 刻意設計，非漂移。** 角色分工：
- **repo SSoT**（200 行精煉版）：跨裝置權威，git-tracked，session-init 每次 pull，#448 壓縮維持 ≤200 行/≤25KB。
- **machine-local**（178 行流水帳）：Mac 本地真實層，Auto Memory，詳細 session 記錄，**不同步**。

-> **不對齊**。強行合併違反 ADR 2層模型 + 5/31d Lesson「ADR 衝突未察」。machine-local 比 SSoT 詳細是正常設計。

---

## 步驟 2 — machine-local 過期待辦清理（APPLY，機械驗證每項）

舊待辦區（machine-local L32-37）4 項，逐項機械驗證實際狀態：

| 待辦 | 判定 | 證據 |
|------|------|------|
| Memory compactor 驗證（截止 2026-05-20）| ✅ 完成 | PR #397/#448 兩次實際觸發 compactor（`git log` 確認）|
| 監控指標儀表板（metrics.json）| ✅ 退場 | 5/31d cosmetic monitor 退場 PR #397；metrics.json 依 ADR 刻意不建 |
| Career-Wiki 評估 | ✅ 關閉 | L9 決策「on-demand 無需主動改動」取代 |
| Subagent 實戰驗證 | ✅ 驗證 | 多 session + 本 session researcher×4 委派 |

**APPLY**：4 項全標 `[x]` + 一句證據，整區註記「早期 — 2026-06-04 稽核全數結清，最新待辦見文末」（保留歷史不抹除，符合 MEMORY 慣例）。最新待辦區（L168）與舊區無重複，不動。

**stale 數字（researcher 發現的 🟡 L43 3500 token / L95 16,927 bytes）**：在歷史 session 段落內、不影響當前決策（低信度）-> 依 §R3「不過度清理」**跳過**，記為已評估。

machine-local **NOT tracked -> 編輯即生效，不需 commit**。

---

## 步驟 3 — R1-R12 計劃書 APPLY（機械驗證後全 DEFER，使用者定奪）

### 機械驗證推翻計劃書多個假設（subagent/計劃書 verdict ≠ 證據）

| 候選 | 計劃書假設 | 機械驗證結果 |
|------|-----------|-------------|
| D6 | core.md 有 κ=0.88 誤用待修 | **no-op**：`grep κ\|MAST core.md` 零命中；κ 已由 #451 修 SSoT |
| D5 | CLAUDE.md ↔ context-management compact hint 重複 | **落空**：CLAUDE.md L34 只是 `@.claude/...` auto-load 引用指令，非 compact 內容重複；兩者非重複 |
| D1-D3 | §R1/R2/R3/R12 散文 re-encode 安全 | **驗證不足**（見下）|
| D4 | 長期記憶回路 re-encode（§R 外）| 可證明安全，但僅 ~70B |

### D1-D3 DEFER 的三個理由（advisor 校準）

1. **可證明性結構消失**：#449 安全是因 diff **全在 §R 區塊外**（`@@ -74`/`@@ -96`），可斷言「R1-R12 逐字未觸」。D1-D3 編輯 **§R 內部** -> 此證明 by construction 不可得。grep 不變量（G2 枚舉/G3 條數/G4 motivation）**無法偵測散文重寫的語義漂移**。
2. **遵守度 eval out-of-band**：唯一真檢查（task-07/08 behavioral eval）依 #439 須 per-model 跑，**不能 inline**。計劃書自承「本批不在 inline 範圍」。
3. **違自身 auto-load 規則**：core.md L79「≤1 規則/cycle」；D1-D3 一次動 4 條 canonical 規則（§R1/R2/R3/R12）。

### 效益反轉

餘裕已 **545B**（原 slimming 觸發是「餘 45 近滿」）；研究自評 **LOW 優先 + adherence-first**（「少省 byte 換不傷遵守」）。花行為條文風險換 D1-D3 ~220B + D4 ~70B，無 pending 增補，**風險/效益不划算**。

### 裁決（使用者定奪 AskUserQuestion）

**全部 DEFER。** D1-D3 + D4 全不在本 session APPLY。理由：餘裕充足、無 pending、研究 LOW、adherence 優先。**零行為條文風險。** 待真正需要餘裕或 instrumented session（可跑 behavioral eval）再執行。

---

## RECORD

| 項 | 狀態 | 落點 |
|----|------|------|
| 步驟1 雙 MEMORY 設計確認 | ✅ 裁決：不對齊 | 本報告 |
| 步驟2 machine-local 過期待辦清理 | ✅ APPLY（4 項標完成）| machine-local（不 commit）|
| 步驟3 R1-R12 D1-D6 | ✅ 全 DEFER | 計劃書保留待後續 gated/instrumented session |
| κ + cache 修正 | ✅ 已 merge | PR #451 |

### 後續（保留待辦）

- R1-R12 §R 內 re-encode（D1-D3）：須 instrumented session（可跑 task-07/08 behavioral eval）+ 一次一條（守 ≤1 規則/cycle）+ before/after 逐句語義等價人工核對。
- D4（長期記憶回路 ~70B）：機會性，與其他 §R 外精簡批次合併再做，不單獨破 cache。
- D5/D6 結案（落空/no-op）。

---

## 不做什麼（範圍守住，§R3）

- ❌ 不對齊雙 MEMORY（設計如此，違 ADR）
- ❌ 不動 §R1-R12 行為條文（驗證不足 + 違 ≤1 規則/cycle + 效益反轉）
- ❌ 不為 ~70B 單獨破 cache 走 PR（D4 機會性合併）
- ❌ 不清歷史 session 內 stale 數字（§R3 不過度，低信度不影響決策）
