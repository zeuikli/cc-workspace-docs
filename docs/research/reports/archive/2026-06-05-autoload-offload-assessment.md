---
title: "Auto-load 下沉評估 — 5 源逐段 TYPE 分類 + on-demand 下沉執行"
date: 2026-06-05
branch: feature/autoload-research-merge-2026-06-05
method: 逐段 byte 量測（wc -c / awk）+ TYPE 分類（判準 core.md §Framework Integrity）+ 主對話親自驗指針 anchor
result: "回收 405 byte（18,999 → 18,594），餘裕 1 → 406"
trigger: 使用者要求「12 原則下哪些 auto-load 內容可下沉到 on-demand ref」
type: assessment + execution report
---

# Auto-load 下沉評估與執行

> **背景**：承接同 session #5/#6 gap 加入後，auto-load 逼近 19,000 byte cap（剩 1 byte）。使用者要求在 12-Rule Canon 框架下，評估哪些常駐內容可下沉到 path-scoped on-demand ref，完整量測後執行並更新文件。

---

## 0. TL;DR

- **判準**：core.md §Framework Integrity「移除後 Claude 在哪犯錯？」——移除**不即時致錯**者（純參考表 / 低頻細節 / 已在 ref 重複 / rationale）可下沉；12-Rule 強制條文 + 安全紅線 + 語言鐵律 + 核心輸出紀律 = TYPE A 不可下沉。
- **執行（保守方案，零行為風險）**：下沉 2 段 → 回收 **405 byte**，18,999 → **18,594**（餘裕 1 → 406），重回「12-Rule Canon 完整正當化區間」舒適帶。
- **守紀律關鍵**：Dynamic Workflow 段**不整段下沉**——其中「subagent/workflow verdict 非證據，必 grep 重驗」是 R12.1 延伸鐵律（TYPE A），保留於 auto-load；僅下沉六大 pattern / token guardrail 細節。
- **無新增 byte 預算**：下沉的 ref 落點全部**事前親 grep 確認內容實存**（無死鏈），control-semantics 表更是 error-handling.md 已 100% 重複。

---

## 1. 量測基準（逐段 byte 分布）

五源現況（執行前）：18,999 / 19,000 byte。

| 檔 | byte | 行數 |
|---|---|---|
| CLAUDE.md | 2,585 | 43 |
| core.md | 9,062 | 101 |
| context-management.md | 2,007 | 27 |
| output-discipline.md | 1,490 | 21 |
| subagent-strategy.md | 3,855 | 67 |

### core.md 段分布（最大檔，逐 `##` 段）

| 段 | byte | TYPE |
|---|---|---|
| 語言 | 235 | A（繁中鐵律） |
| 生產環境安全紅線 | 148 | A |
| §R1–§R12（12 段合計） | ~5,539 | **A（行為契約，全不可下沉）** |
| Framework Integrity | 811 | A（含 byte cap 機制） |
| 暫存檔案 | 193 | A（路徑慣例，高頻） |
| 長任務執行 | 297 | A（Bash 慣例，高頻致錯） |
| 長期記憶回路 | 617 | A（self-improving 觸發，高頻） |
| Git 工作流程 | 1,033 | A 紅線 + C 細節（worktree/PR 衝突 rationale 可下沉，本輪未動）|

### subagent-strategy.md 段分布

| 段 | byte（執行前）| TYPE | 裁決 |
|---|---|---|---|
| Agent Input Security | 307 | A | 保留（injection 防護高頻）|
| 委派決策 | 705 | A | 保留（核心判準）|
| 拓撲規則 Fan-out | 591 | A | 保留（並行紀律）|
| **Agent 控制語義表** | **638** | **C** | **✅ 下沉**（error-handling.md 已全含）|
| Routines | 112 | A | 保留 |
| Frozen Snapshot | 120 | A | 保留 |
| Advisor 模式 | 172 | A | 保留 |
| 模型選擇 | 493 | A | 保留 |
| Background Agent | 267 | A | 保留 |
| **Dynamic Workflow 紀律** | **412** | **A+C 混合** | **✅ 部分下沉**（保留 verdict 鐵律，下沉 pattern 細節）|

---

## 2. TYPE 分類原則（12-Rule 框架）

| TYPE | 定義 | 下沉？ | 範例 |
|---|---|---|---|
| **A** | 移除即時致錯 | ❌ 不可 | §R1–§R12、安全紅線、繁中鐵律、核心輸出紀律、委派決策 |
| **C** | rationale / 低頻參考 / 純對照表 / 已在 ref 重複 | ✅ 下沉 refs | 控制語義表、workflow pattern 細節、cache 監控公式 |
| **D** | 與他段 / ref 重複 | ✅ 刪 | model-drift（已在 prompt-lifecycle）|

> **混合段處理**：一段內可同時含 A 鐵律 + C 細節（如 Dynamic Workflow）→ **拆**：鐵律句留 auto-load，細節下沉，留指針。不整段下沉。

---

## 3. 執行紀錄（保守方案）

### 下沉 1：Agent 控制語義表（零損）

- **前**：638 byte 完整三語義對照表（interrupt/steer/gate）+ pause_turn 說明
- **後**：1 行指針 → `refs/error-handling.md §Agent 控制語義`
- **零損依據**：error-handling.md L48-58 已 100% 含相同表（親 grep 確認）
- **回收**：~425 byte

### 下沉 2：Dynamic Workflow 紀律（拆 A/C）

- **保留（TYPE A 鐵律）**：「subagent/workflow verdict 非證據，採信前必機械 grep 重驗（連 agent 轉述的確定性結果亦不可信，見 §R12.1）」
- **下沉（TYPE C）**：六大 pattern / 「when not to use」token guardrail / 全紀錄 → `harness-meta-GOTCHAS.md §Dynamic Workflow` + research 檔
- **回收淨額**：併下沉 1 後總回收 405 byte

### 死鏈防範（過程修正）

- 執行中一度把 Dynamic Workflow 指針誤改指向 `refs/harness-design.md`（grep = 0 hits，內容不存在）→ 立即修回確實存在的 `harness-meta-GOTCHAS.md`（2 hits）。
- **教訓**：下沉留指針前，必親 grep 確認 ref 落點 anchor 實存，否則造成死鏈（R12 Fail Loud 攔截）。

---

## 4. 驗證（確定性 gate，主對話親自跑）

| 檢查 | 結果 |
|---|---|
| 五源 byte | **18,594 / 19,000**（餘裕 406）|
| 指針 `error-handling.md §Agent 控制語義` | ✅ 1 anchor 實存 |
| 指針 `harness-meta-GOTCHAS.md §Dynamic Workflow` | ✅ 2 hits 實存 |
| 指針 research dynamic-workflows 檔 | ✅ 實存 |
| healthcheck | **PASS 110 / WARN 3 / FAIL 0**（含 Auto-load Budget Gate PASS）|

---

## 5. 未執行的下沉候選（供未來 cycle）

保守方案僅取零損 2 段。以下候選經評估可行但本輪未動（守 ≤1 cycle 紀律 + 需更細拆分）：

| 候選 | byte | 落點 | 為何延後 |
|---|---|---|---|
| Git 工作流程 worktree/PR 衝突細節 | ~500 | 新 ref 或 harness-loop | 需拆「紅線句保留」vs「rationale 下沉」，多一層判斷 |
| context-management 監控 cache 公式 | ~450 | cache-health-metrics.md（已存在）| 需確認公式不在高頻路徑 |

→ 兩者合計可再回收 ~950 byte，降到 ~17,650。建議走 `/autoload-evolution` 獨立 cycle 執行。

---

## 5b. 反向稽核發現（refs → auto-load，2026-06-05 追加）

> **方法（反向思考）**：不從 auto-load 往外查死鏈，而是從 refs/ 回看 auto-load 鏈健康度。建「ref ↔ auto-load 引用矩陣」（grep -F 反查，注意 `.md` 的 `.` 會被正則吃掉 → 必用 `-F` 固定字串 + 陣列展開檔列表，否則全 0 假陰性）。委派 researcher 機械掃描，主對話親自 grep 重驗每條 verdict。

### 矩陣結論
- **死鏈 0**：auto-load 所有 `refs/xxx.md §anchor` 指針的目標檔 + anchor 全實存。
- **真孤兒 0**：9 個「auto-load 0 直接引用」的 ref 全部經 refs/README + trigger-index 二跳可達（非完全不可達）。
- **trigger-index 自身 0 個 auto-load 直接引用**（MEMORY 早記的已知斷鏈，現況仍然；二跳工具用，非阻塞）。

### 修正的真實缺陷（親驗屬實）

| # | 缺陷 | 親驗 | 修正 |
|---|---|---|---|
| 1 | **byte cap stale**：`harness-loop.md:21`（canonical TEST gate）寫 `≤18,000`，auto-load 本體已 19,000 | ✅ grep 確認 | 改為 19,000（canonical 須現值）|
| 2 | `model-upgrade-harness-tuning.md:78-79` 歷史提案快照寫 18,000 | ✅ grep 確認 | **加註不竄改**（歷史快照保留 + 標明現值 19,000）|
| 3 | `removed-content-manifest.txt` 未登錄 refs/README | ✅ grep=0 | refs/README 加機制資料登錄行 |
| 4 | refs/README L3 寫「12 docs」但實列 17 | ✅ | 改 17 |
| 5 | refs/README L42 宣稱 agent-team-patterns 被 subagent-strategy 引用，實際 grep=0 | ✅ | 改誠實標注（SA-2 待辦未建入口）|

### 關鍵判斷（researcher 未分辨、主對話拍板）
**同樣的「18,000」，一個該改一個不該改**：
- `harness-loop.md` = harness loop **canonical 定義**（CLAUDE.md 直接引用）→ 必須現值 → **改 19,000**
- `model-upgrade-harness-tuning.md` = **歷史提案快照**（記錄 2026-05 當時 cap）→ 竄改會破壞紀錄真實性 → **加註不改數字**

→ 反向稽核的最高價值：抓到「ref 內 stale 閾值會誤導 harness 預檢」這類**正向稽核（從 auto-load 出發）看不到**的缺陷——因為這些 ref 不被 auto-load 直接引用，只在跑 harness loop / model-upgrade 時才載入，正向掃不到。

---

## 6. 結論

- **下沉是 auto-load 飽和的正解**（優於上調 cap）：cap 上調受 core.md L79 自身禁令約束（不接受為單一規則湊 byte）；下沉把低頻內容移到「需要時才載入」的 path-scoped ref，**既守 byte 預算又零功能損失**。
- **12-Rule 框架下的下沉鐵律**：強制條文（§R1–§R12）+ 安全紅線 + 鐵律句永不下沉；純參考 / 低頻 / 重複內容才下沉；混合段拆而非整段移。
- **餘裕 406 byte**：足夠容下次小幅規則增補，但近滿狀態應持續以下沉換空間，非反覆逼近 cap。

---

*評估日期：2026-06-05 | 方法：逐段 byte 量測 + TYPE 分類 + 主對話親自驗指針 | 回收 405 byte | healthcheck PASS 110/0 | 保守零損方案*
