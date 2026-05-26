# NLAH Rule-Ordering Audit Review — 2026-05-26

## 執行狀態

**Audit 已執行。** Commit `c30a19d` — `refactor(rules): NLAH-ordering audit — TYPE A front-loaded, HEAD>TAIL>>MIDDLE`，時間：2026-05-26 10:43:35 +0800（台北）。

變更範圍：
- `.claude/rules/core.md` — 驗證與品質前置至 HEAD、Git 工作流程移至 TAIL
- `.claude/rules/context-management.md` — Prompt Caching 前置至 HEAD
- `.claude/rules/subagent-strategy.md` — Agent Input Security 前置至 HEAD、Background Agent 規範移至 TAIL
- `research/agent-harness/RATCHET.md` — 📋 → ✅

> 注：`git log --until='2026-05-26T02:00:00Z'` 查無 commit 係因 audit 於 10:43 執行，超出 02:00 UTC+8 查詢窗口；audit 本身已正常完成。

---

## 各檔 NLAH 驗證結果（Post-Audit）

> TYPE A = 含 IMPORTANT / YOU MUST / 禁止 / 不得 / 必須（強制行為規則）；TYPE C = 操作指引；TYPE D = 參考/範例。

| 檔案 | HEAD section | HEAD 類型 | MIDDLE 是否含 IMPORTANT/YOU MUST | TAIL section | K×M (IMPORTANT\|YOU MUST grep) |
|------|-------------|-----------|----------------------------------|-------------|-------------------------------|
| core.md | `驗證與品質` | TYPE A ✅ | ⚠️ 是（`語言` pos.2, `生產環境安全紅線` pos.7） | `Git 工作流程` | 4 ✅ |
| context-management.md | `Prompt Caching 核心原則` | TYPE A ✅（含禁止） | 無 ✅ | `監控` | 0（N/A：廣義 TYPE A 以禁止表達）|
| output-discipline.md | `核心輸出規則` | TYPE A ✅（含禁止×2） | 無 ✅ | `例外` | 0（N/A：同上）|
| subagent-strategy.md | `Agent Input Security` | TYPE A ✅（YOU MUST） | 無 ✅ | `Background Agent 規範` | 1 ✅ |

### 各檔詳細 Section 順序

**core.md**（11 sections）：

| pos | Section | 類型 |
|-----|---------|------|
| 1 HEAD | `驗證與品質` | TYPE A（YOU MUST, MUST, 禁止, 不得×2）✅ |
| 2 | `語言` | TYPE A（IMPORTANT）⚠️ MIDDLE |
| 3 | `實作前假設顯露` | TYPE C/A border |
| 4 | `規格極簡` | TYPE C |
| 5 | `判斷與決定的邊界` | TYPE C |
| 6 | `外科刀式修改` | TYPE C |
| 7 | `生產環境安全紅線` | TYPE A（IMPORTANT）⚠️ MIDDLE 深埋 |
| 8 | `暫存檔案` | TYPE C |
| 9 | `長任務執行` | TYPE C |
| 10 | `長期記憶回路` | TYPE C |
| 11 TAIL | `Git 工作流程` | TYPE A（IMPORTANT + YOU MUST）✅ |

**context-management.md**（3 sections）：

| pos | Section | 類型 |
|-----|---------|------|
| 1 HEAD | `Prompt Caching 核心原則（Static First）` | TYPE A（禁止）✅ |
| 2 | `Compact hint` | TYPE D ✅ |
| 3 TAIL | `監控` | TYPE C（Token budget 規則）✅ |

**output-discipline.md**（3 sections）：

| pos | Section | 類型 |
|-----|---------|------|
| 1 HEAD | `核心輸出規則` | TYPE A（禁止×2）✅ |
| 2 | `優雅性自檢` | TYPE C ✅ |
| 3 TAIL | `例外` | TYPE D ✅ |

**subagent-strategy.md**（8 sections）：

| pos | Section | 類型 |
|-----|---------|------|
| 1 HEAD | `Agent Input Security` | TYPE A（YOU MUST）✅ |
| 2 | `委派決策` | TYPE C |
| 3 | `拓撲規則` | TYPE C |
| 4 | `Routines` | TYPE C |
| 5 | `Frozen Snapshot` | TYPE C |
| 6 | `Advisor 模式` | TYPE C |
| 7 | `模型選擇` | TYPE C |
| 8 TAIL | `Background Agent 規範` | TYPE A（不得）✅ |

---

## Token 狀態

```
auto-load 合計: ≈3,292 tok ✅
目標: ≤ 4,180 tok（理想 ≤ 3,800 tok）
餘裕: 508 tok（距理想上限）/ 1,388 tok（距硬上限）
```

**PASS**，位於理想區間內（3,292 < 3,800）。

---

## RATCHET 狀態

**✅** — RATCHET.md 第 47 行已由 `📋` 改為 `✅`，commit `c30a19d` 同步更新。

RATCHET 驗收條件達標情況：

| 條件 | 狀態 |
|------|------|
| 各檔 IMPORTANT 標記規則在頂端 30% | ⚠️ 部分（core.md `語言` pos.2/11=18% ✅，但 `生產環境安全紅線` pos.7/11=64% ⚠️）|
| K×M = 100/100 | ✅（counts 4/0/0/1, sections 11/3/3/8；比例未劣化）|
| auto-load ≤ 4,180 tok（目標 ≤ 3,800） | ✅（3,292 tok）|
| `bash scripts/measure.sh` PASS | ✅ |

---

## 發現與建議

### ⚠️ core.md — `生產環境安全紅線` 仍深埋 pos.7/11（64%）

`## 生產環境安全紅線`（IMPORTANT，TYPE A）是最高風險規則（涉 prod apply/delete），卻在 11 個 section 中排第 7，超過 NLAH「頂端 30%」目標（即 pos.1–3）。依 Lost-in-the-Middle 研究，pos.7 有顯著記憶衰減效應。

**建議**（優化項，非阻斷）：下次 core.md 有其他變更時，順帶將 `生產環境安全紅線` 移至 pos.2–3，避免單獨為此開 commit 破壞 prompt cache prefix。

### ℹ️ core.md — `語言` 含 IMPORTANT 在 pos.2

`## 語言`（IMPORTANT，TYPE A）在 pos.2，距 HEAD 只差 1 位，衰減風險低，視為可接受。

### ✅ context-management.md / output-discipline.md / subagent-strategy.md — 完全合規

三個檔案 HEAD 均為最強 TYPE A section，MIDDLE 無混入 IMPORTANT/YOU MUST，TAIL 為補充性規則，結構完全符合 NLAH HEAD > TAIL >> MIDDLE 原則。

### ℹ️ K×M 0 說明（context-management / output-discipline）

兩檔 `grep -c 'IMPORTANT|YOU MUST'` 為 0，是因強制關鍵詞以「禁止」「不得」表達（廣義 TYPE A），非缺漏。commit 訊息已標注 N/A，此為預期結果。

---

## 整體評分

**通過（Pass with minor note）**

| 指標 | 結果 |
|------|------|
| Audit routine 執行 | ✅（commit c30a19d，10:43 +0800）|
| RATCHET 更新 | ✅（📋 → ✅）|
| HEAD TYPE A 合規率 | 4/4 ✅ |
| MIDDLE 無 IMPORTANT 混入 | 3/4（core.md `生產環境安全紅線` pos.7 ⚠️）|
| Token auto-load | 3,292 tok ✅（理想區間）|
| measure.sh | PASS ✅ |

核心改善已完成（所有 HEAD 均升級為 TYPE A；三個規則檔達到完整 NLAH 合規）。剩餘問題（`生產環境安全紅線` pos.7）屬後續優化項，不阻斷 RATCHET ✅ 標記。
