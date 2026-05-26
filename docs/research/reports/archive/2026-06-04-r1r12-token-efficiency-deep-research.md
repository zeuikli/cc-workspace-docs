---
title: "R1-R12 行為條文 Token 效率深度研究（遵守度不降前提）"
date: 2026-06-04
baseline_bytes: 18455
branch: feature/autoload-slimming-apply
cap_bytes: 19000
headroom_bytes: 545
method: 3 researcher 並行（官方最佳實踐 + prompt-compression papers + 論文真實性驗證）+ core.md inline TYPE 盤點 + advisor 三輪校準
mode: 純研究 + 計劃書（零修改 auto-load）
question: R1-R12 有什麼方法可以讓 Claude 遵守但不浪費 auto-load token？
type: research
verified_papers: ["arXiv:2604.07192 (Compact Constraint Encoding — EXISTS, 親驗 Cliff's δ<0.01)", "arXiv:2512.17920 (CDCT U-curve — EXISTS, 親驗)"]
---

# R1-R12 行為條文 Token 效率深度研究

> **核心問題**：R1-R12 怎麼讓 Claude 遵守，但不浪費 auto-load token？
> **執行模式**：純研究 + 計劃書，**零修改 auto-load**（使用者指令「產出獨立的研究報告和可執行計劃書」）。R1-R12 實際調整為下一個 gated session。

---

## 0. TL;DR — 兩個 supersede 前一輪的關鍵發現（Fail-Loud 先行）

本輪證據**翻轉**了 #449（autoload-slimming）的兩個核心假設。使用者明令「遵照 papers + 官方最佳實踐」，故必須以證據為準，不繼承舊框架：

### 發現 1 — 槓桿翻轉：proven-safe 是 REFORMAT，不是 DELETE-rationale

- **#449 框架**：「刪 TYPE C/D rationale 回收 byte」。
- **本輪一手證據反對此框架**：
  - **arXiv:2604.07192**（親驗，Tencent 2026-04，11 模型/16 benchmark/830+ calls）：compact **re-encoding**（同 constraint 換緊湊格式）省 25-30% token，**Constraint Satisfaction Rate 無統計顯著差異**（Cliff's δ < 0.01）。但它證明的是「**重編碼**安全」，**不是「刪除 rationale」安全**。
  - **官方 Finding 4.3**（Anthropic prompt eng 文件）：「Providing context or motivation behind your instructions helps Claude better understand your goals」——舉例 bare `NEVER use ellipses`（弱）vs 解釋 TTS 引擎不懂省略號（強）。
  - **推論**：12-Rule Canon 的設計核心「每條回答防止哪個失敗模式」**正是這種 adherence-supporting motivation**。刪掉「為何」= 刪掉官方背書的遵守支撐。
- **修正後槓桿**：**主力 = compact re-encode（verbose 散文 -> 緊湊結構化，語義 + 枚舉 verbatim 保留）**；刪除只限真正死重（TYPE D 過期日期/一次性決策史已在 MEMORY + TYPE C 跨檔重複）。**不刪「為何」。**

### 發現 2 — MAST κ=0.88 框架錯誤，須糾正不可繼承

- **#449 + MEMORY 多處**把 MAST 的 κ=0.88 寫成「specification 品質指標」，作為「不可壓行為條文」的下限論證。
- **本輪 researcher 親驗 arXiv:2503.13657**：κ=0.88 是**失敗分類法的標注者間一致性（inter-annotator agreement）**，**不是 spec-quality 指標**。這是定義錯誤。
- **後果**：(a) 本報告下限**重新接地**在證據真正支持的東西（見 §3）；(b) **flag MEMORY 待修**（Lesson 待補：κ 誤讀散佈多處）。此為 Fail-Loud / Surface-Conflict，不靜默修。

---

## 1. 全 auto-load Token/Byte 量測（OBSERVE，使用者要求「對所有 autoload token 量測」）

驗證指令：`wc -c CLAUDE.md .claude/rules/{core,context-management,output-discipline,subagent-strategy}.md`

| 檔案 | bytes | chars | est. tokens† | 佔比 | 角色 |
|------|------:|------:|------------:|-----:|------|
| `core.md` | 8,518 | 5,063 | ~2,700 | 46.2% | R1–R12 + Git + 生產紅線 |
| `subagent-strategy.md` | 3,855 | 2,390 | ~1,250 | 20.9% | 委派 / fan-out / advisor |
| `CLAUDE.md` | 2,585 | 1,944 | ~1,000 | 14.0% | Canon 表 + harness loop + 模式 |
| `context-management.md` | 2,007 | 1,234 | ~640 | 10.9% | token budget / compact / caching |
| `output-discipline.md` | 1,490 | 785 | ~410 | 8.1% | 輸出紀律 |
| **總計** | **18,455** | 11,416 | **~6,000** | 100% | vs cap 19,000，餘 **545** |

† **token 估算方法學**（誠實標注）：本機無 tiktoken/ttok。混合中英；CJK 約 1.0-1.5 char/token、ASCII 約 4 char/token。粗估 ~6,000 tokens（±15%）。官方 cache 最低門檻 1,024 tokens（Opus/Sonnet）-> 遠超，**精簡不碰 cache 底線**（官方 Finding 3.1）。

### core.md §R 各條 byte 分布（inline 盤點）

| 條 | byte | 性質摘要 | 主要可 re-encode 內容 |
|----|-----:|---------|---------------------|
| §R1 | 1,039 | 假設顯露 + Ask-rate 校準 + 不可逆例外清單 | **散文框架**可緊湊化；**枚舉清單 verbatim 保留**（危險區）|
| §R3 | 692 | 外科刀 + 量化界線 + P0 grep 細節 | 量化數字保留；P0 流程散文可緊湊 |
| §R2 | 548 | Simplicity + Rule of 3 + 安全例外 | 散文可緊湊；Rule of 3 數字保留 |
| §R12 | 548 | Fail Loud + PGE + 截斷標示 | 散文可緊湊 |
| §R7 | 286 | 衝突浮現 + 優先序 | TODO 格式 verbatim 保留 |
| §R11 | 275 | 規範優先 | 散文可緊湊 |
| §R5 | 259 | 判斷 vs 決定 | 已精簡（範例對照）|
| §R8 | 259 | 改前先讀 | 已精簡 |
| §R4 | 512 | 目標導向 | 驗證指令 verbatim 保留 |
| §R9 | 190 | 測試驗證意圖 | 已精簡 |
| §R10 | 178 | Checkpoint | 已精簡 |

**關鍵**：§R1 byte 最大，但大半是**行為子規則 + 不可逆枚舉**（DELETE/TRUNCATE/DROP...）-> 刪枚舉在**危險區**（見 §3 表）。**biggest ≠ most compressible**——讓危險表選目標，非 byte 排名。

---

## 2. 證據彙整（3 researcher 並行 + advisor 校準）

### 2.1 官方最佳實踐（Anthropic / Claude Code 一手）

| # | Finding | 來源 | 對本任務啟示 |
|---|---------|------|------------|
| O1 | 「Bloated CLAUDE.md -> Claude ignores your actual instructions」；過長 = 重要規則被淹沒 | code.claude.com/docs/best-practices | **官方支持精簡提升遵守**（signal/noise）|
| O2 | 「Target under 200 lines per CLAUDE.md」 | code.claude.com/docs/memory | 200 行軟上限（本 workspace core.md 100 行 ✓）|
| O3 | 過長補救 = **Ruthlessly prune**，不是加更多規則 | best-practices | 精簡方向正確 |
| O4 | **加「為什麼/motivation」比加 CAPS 更提升遵守** | prompt eng 文件 | **rationale 不該全刪**（翻轉 #449）|
| O5 | XML tags 減少 misinterpretation（無 A/B 數字）| prompt eng 文件 | 結構化方向，但無定量 |
| O6 | IMPORTANT/YOU MUST 在 **CLAUDE.md 脈絡**官方背書；但 API 工具觸發脈絡新模型應 dial back | best-practices vs prompt eng | **脈絡相依**（auto-load 屬 CLAUDE.md 脈絡 -> 保留強調詞合理）|
| O7 | CLAUDE.md 是 **user message 非 system prompt**，無嚴格遵守保證 | code.claude.com/docs/memory | 架構事實：規則清晰度更重要 |

### 2.2 學術 papers（親驗關鍵 2 篇）

| # | Paper | 核心數字 | 安全/危險判定 |
|---|-------|---------|--------------|
| P1 | **2604.07192** Compact Constraint Encoding（親驗）| compact header 省 25-30% token，CSR **無顯著差異 δ<0.01** | **REFORMAT 安全**（最直接一手）|
| P2 | **2512.17920** CDCT U-curve（親驗）| 中間壓縮（~27 字模糊區）CC 最差（U 型，97.2% prevalence）| **壓到語義模糊 = 危險** |
| P3 | 2510.05106 Rule Encoding | 低 syntactic entropy + anchor token（if/then）-> 提升 pointer fidelity | **條列/if-then 結構有理論優勢** |
| P4 | 2601.18554 MOSAIC | 15+ constraints 全面劣化；Claude 有 recency effect | **不可把 12 條拆成更多**；重要規則放首/末 |
| P5 | 2605.06445 Constraint Decay | 每加 1 constraint dimension -19.3pp | constraint **數量**傷遵守 -> 不增量 |
| P6 | 2407.08892 Prompt Compression 比較 | SQL CREATE TABLE 內 token 被移除 -> 嚴重劣化 | **definition/枚舉內 token 高危** |
| P7 | 2403.12968 LLMLingua-2 | 均勻 token 剪法，指令不享保護 | **自動壓縮工具不適用規則檔** |
| P8 | 2502.14255 Prompt Length | 縮短「含資訊」指令一致劣化 | 砍**有資訊**內容危險（≠砍冗餘措辭）|

### 2.3 已知研究空白（誠實標注）

- **無 paper 直接實證「移除每條規則的 rationale 對 adherence 的影響」**。間接證據（P1 + O4）傾向「constraint 清晰度 > 解釋長度」，但官方 O4 明確「motivation 提升遵守」-> **淨判定：保留 rationale，只 re-encode 表達**。

---

## 3. 安全/危險分類表（IDENTIFY -> 這是 APPLY 的 gate）

> 由危險表（非 byte 排名）決定可動目標。下限**重新接地**（不用誤讀的 MAST κ）。

| 操作 | 判定 | 證據 |
|------|------|------|
| verbose 散文 -> 緊湊結構化（語義保留）| ✅ **安全** | P1 (δ<0.01) + P3 |
| 移除跨檔**重複**陳述（同義保留一處）| ✅ **安全** | TYPE C；#449 C3 已驗 |
| 移除**過期日期/一次性決策史**（已在 MEMORY）| ✅ **安全** | TYPE D；#449 C1 已驗 |
| 保留條文 verbatim、砍 rationale 解釋 | ⚠️ **不建議** | O4 反對（motivation 助遵守）；無 paper 支持移除安全 |
| 壓條文到語義模糊（~27 字 U-curve 區）| ❌ **危險** | P2 CDCT |
| 移除**枚舉清單**（DELETE/TRUNCATE/DROP、不可逆動作）| ❌ **危險** | P6 (2407.08892) + 2304.08467 |
| 移除**驗證指令字面**（healthcheck/wc -c/grep）| ❌ **危險** | spec 可驗證性（R4/R12）|
| 增加 constraint 數量 / 拆條文 | ❌ **危險** | P4 (15+) + P5 (-19.3pp/dim) |
| 重要規則移到中間位置 | ❌ **危險** | P4 primacy/recency |

**下限重述**（取代誤讀的 MAST κ=0.88）：
1. 行為**語義**不可變（CDCT U-curve：壓到模糊最傷）；
2. **枚舉/驗證指令 verbatim 保留**（compression paper：definition token 高危）；
3. **不增 constraint 數**（MOSAIC/Constraint Decay）；
4. **rationale 保留**（官方 O4：motivation 助遵守）——只改表達不刪意義。

---

## 4. 可精簡空間估算（保守）

僅限「✅ 安全」操作（re-encode + 去重 + 去死重），**不碰 ⚠️/❌**：

| 區塊 | 操作 | 估算回收 |
|------|------|--------:|
| §R1/§R2/§R3/§R12 散文框架 -> 緊湊（語義+枚舉 verbatim 保留）| re-encode | ~200-350 B |
| 長期記憶回路 (616B) 操作散文緊湊化 | re-encode | ~80-120 B |
| Git 工作流程 (1033B) PR 衝突段措辭 | re-encode | ~50-80 B |
| 跨檔殘餘重複（context-mgmt ↔ CLAUDE.md compact hint）| 去重 | ~50-100 B |
| **合計（保守）** | | **~380-650 B** |

**注意**：估算偏保守且**低於** #449 的 500B/單輪——因本輪**禁止刪 rationale**（最大宗 byte 來源），只能 re-encode。**這是正確的 trade-off：少省 byte，換不傷遵守**（使用者要的是「遵守但不浪費」，遵守優先）。

---

## 5. 裁決（PROPOSE）

| 問題 | 裁決 |
|------|------|
| R1-R12 能在不傷遵守下省 token？ | ✅ **能，但限 re-encode 不限 delete-rationale** |
| 主力槓桿 | **compact re-encode**（P1 親驗安全）|
| 最大 byte（§R1）可大砍？ | ❌ 不可——大半是枚舉/行為子規則（危險區）|
| 下限 | CDCT 語義 + 枚舉/驗證指令 verbatim + 不增 constraint 數 + 保留 motivation |
| 本輪交付 | **報告 + 計劃書**；R1-R12 edits = 下一 gated session（鏡像 #446）|
| 附帶 | **flag MEMORY κ=0.88 誤讀待修**（Fail-Loud）|

**不建議**：① 為省 byte 刪 rationale（官方 O4 反對）；② 用自動壓縮工具（LLMLingua 類，P7 不適用規則）；③ 把精簡當遵守度優化的主手段（官方 O7：clarity 才是）。

---

## 6. 後續（計劃書 handoff）

可執行計劃書見：`2026-06-04-r1r12-token-efficiency-execution-plan.md`（逐項 re-encode 候選 + 危險表 gate + falsifiable prediction + eval 驗證遵守度不降）。

**驗證指令（基線）**：
```bash
wc -c CLAUDE.md .claude/rules/{core,context-management,output-discipline,subagent-strategy}.md | tail -1   # 18455
grep -c "^## §R" .claude/rules/core.md   # 11（+R6 在 context-mgmt）
```

---

## 附錄：論文清單（驗證狀態）

- ✅ 親驗 EXISTS：`2604.07192`（Compact Constraint Encoding, Tencent 2026-04）、`2512.17920`（CDCT, 2025-12）
- 二手引用（researcher 標注，未逐一親驗）：`2503.13657` MAST、`2510.05106`、`2601.18554` MOSAIC、`2605.06445`、`2407.08892`、`2403.12968`、`2502.14255`、`2411.10541`、`2304.08467` GIST、`2310.05736` LLMLingua、`2304.12102` Selective-Context
- **κ=0.88 修正**：MAST 的 κ 是 inter-annotator agreement，非 spec-quality（親驗 abstract 確認）
