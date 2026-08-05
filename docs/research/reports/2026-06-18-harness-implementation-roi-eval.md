---
title: "Harness 實作有效性與 ROI 評估 — 12-unit fan-out + 落地計畫"
date: 2026-06-18
status: complete
caveat: "byte 節省為各 unit 字元估算（±15%），實作以 wc -c 實測為準；每 cycle 後重量測"
method: 12-unit dynamic-workflow fan-out（researcher，context isolation，3 批 ≤4）→ 主對話親驗（grep/wc/ls）→ fable-pilot anti-hack 紀律
scope: 評估 2026-06-18-harness-derivation-deep-research §7 四候選 + autoload byte 優化；實作範圍限 .claude/ + CLAUDE.md
type: research
verification: "親驗 HARNESS-CARD 存在(8049B)、AGENTS.md 存在、CJK→英文+32%byte、8 個 ref 目標存在、gate 腳本齊備"
---

# Harness 實作有效性與 ROI 評估

> **TLDR**：對「上一份報告 §7 的 4 個演化候選 + autoload byte 優化」做 12-unit fan-out ROI 評估。結論：**§7 四候選全部 DEFER/DROP**（B1 缺 eval 歷史前置；B2 HarnessCard **已存在**、報告 gap 過期；B3 白盒 99.6% 黑盒 API 不可達；B4 pilot 模式已覆蓋 70% 且違反「不為未來鋪設」）。唯一高 ROI、in-scope、低風險、使用者明確要求的實作 = **autoload byte 優化**（現 18,990B，距 19,000 審視線僅 10B）。關鍵策略修正：**CJK→英文省 token 但 +32% byte**（canonical 單位是 byte），故正確降法 = **刪冗餘/修辭 + 下沉既有 refs**，非翻譯。保守可降 ~2,600–3,700B → 目標 ≤17,000B（緩衝 ~2,000B）。

---

## 0. 方法與驗證

12 個 researcher sub-agent 並行（3 批，每批 ≤4，遵 fan-out 上限），每個產出一張 ROI Card。主對話親驗關鍵發現（防 agentic-laziness，承上一 session Cluster-E 教訓）：

| 親驗項 | 結果 |
|--------|------|
| HARNESS-CARD.md 是否存在（B2） | ✅ `research/agent-harness/HARNESS-CARD.md` 8049B/82 行，8 欄齊全（2026-06-12）→ B2 報告 gap **過期** |
| AGENTS.md 是否存在（U11 疑 bug） | ✅ root 存在 → CLAUDE.md L2「Read AGENTS.md first」**有效非 bug**（推翻 U11 該點）|
| CJK byte vs token（U3） | ✅ cjk-token-efficiency.md 親驗「英文省~20% token 但 +32% byte」→ 不翻譯 |
| 8 個下沉目標 refs 存在 | ✅ 全 OK（下沉前置通過）|
| gate 腳本 | ✅ healthcheck.sh / measure.sh 齊備 |
| 全 12 unit tool_uses | ✅ 全 >0（無杜撰）|

---

## 1. ROI 評估矩陣（12 unit 彙整）

| Unit | 候選 | In-scope | 有效性 | byte 影響 | 風險 | Verdict |
|------|------|:--:|:--:|--------|:--:|:--:|
| U1 | core.md 下沉/壓縮 | ✅ | 5/5 | **−~2,200** | low-med | **DO-NOW** |
| U2 | subagent+context 下沉 refs | ✅ | 4/5 | **−~1,175** | low | **DO-NOW** |
| U10 | frontier 約束削減（B1/B5/B6）| ✅ | 4/5 | **−~290** | low | **DO-NOW** |
| U9 | lazy-load×caching 衝突 | ✅ | 3/5 | 0 | none | **DO-NOW**（純澄清，關 TODO）|
| U4 | 跨檔去重 | ✅ | 3/5 | −~150 | low | **DO-NOW**（併入 U1/U2）|
| U3 | CJK→英文 | ✅ | 1/5 | **+byte!** | — | **DROP**（方向相反）|
| U11 | CLAUDE.md/README 精簡 | ✅ | 2/5 | −~35 | med(快取) | **DEFER**（微利不值破快取；AGENTS.md 非 bug）|
| U5/B1 | 先驗過濾 gate | ✅ | 2/5 | 0 | — | **DEFER**（缺 ≥10 cycle eval 歷史；AHE 回歸預測 11.8%≈無資訊）|
| U6/B2 | HarnessCard 化 | ✅ | 1/5 | 0 | — | **DROP**（已存在；另建=雙版本 drift）|
| U7/B3 | pre-LLM untrusted 過濾 | ✅ | 2/5 | 0 | med(誤判) | **DEFER**（白盒 99.6% 黑盒不可達；shell regex 僅邊際）|
| U8/B4 | variant routing 預備 | ✅ | 2/5 | +byte | — | **DROP**（pilot 已覆蓋 70%；違反「不為未來鋪設」）|

---

## 2. §7 四候選為何全部不實作（誠實歸因）

- **B1 先驗過濾 gate（DEFER）**：HARBOR posterior chance constraint 需「歷史 eval 後驗分布」；workspace 僅 per-model baseline（15 trials, 2026-05-30），**無 per-rule per-cycle eval 時序 log**，建不出統計後驗。且 AHE 實測回歸預測精度 **11.8% ≈ 無資訊**——即使資料足，先驗過濾誤拒率也高。重評前置：累積 ≥10 cycle eval log。
- **B2 HarnessCard 化（DROP）**：`research/agent-harness/HARNESS-CARD.md` **已存在**且 8 欄完整、有 5 次 audit changelog。報告 §5「缺機器可讀 harness spec」為 2026-06-12 前的過期判斷。另建一份 = 雙版本 drift（比缺口更糟）。低成本替代：harness-design.md L26 補精確路徑。
- **B3 pre-LLM 過濾（DEFER）**：IPI-defense 99.6% 是**白盒 MLP + hidden states**；Claude Code 黑盒 API 拿不到 hidden states，退化為 shell regex（對 base64/語意偽裝/多語幾乎無效），且誤判會擋正常 WebFetch/MCP。有意義的低成本下一步是 **data provenance 標籤**（非字面掃描），列為未來。
- **B4 variant routing（DROP）**：`/fable-pilot`等 pilot 模式 + multi-mode router + path-scoped rules 已覆蓋 ~70% 任務型別路由；任務流分布偏移是**單人 workspace 未觀察的遠期假設**，預先鋪設違反 core.md PROPOSE「不為未來可能鋪設 / Rule of 3」。

---

## 3. 落地計畫（DO-NOW，按 ≤1 規則檔/cycle 拆 cycle）

> 執行協議（U12）：每 cycle = 改 1 個 auto-load 規則檔（+ 對應 refs 不計數）。每 cycle 後：`wc -c` 六源重量測 + `bash scripts/healthcheck.sh`（FAIL=0）+ grep 驗下沉內容存在 refs + git diff 審 → atomic commit。回滾用 `git revert`。**下沉=資訊保留於 refs 不寫 manifest；純刪檔才寫 manifest**。

| Cycle | 檔案 | 動作 | 預估 −byte | 風險控制 |
|:--:|------|------|:--:|------|
| 1 | core.md | 下沉(Framework-Integrity 去重/APPLY 不可逆清單→best-solution/長期記憶細節/Git 命令序列) + 壓縮(TEST static-offline/RECORD) + 刪修辭(B1) | ~2,000 | 下沉前 grep 確認目標 ref 已含該內容；鐵律紅線清單禁動 |
| 2 | output-discipline.md | U10 B5 填充語清單→一句、B6 禁用詞→縮指針 | ~230 | frontier hyper-literalism 證據（Prompting Inversion −2.36pp）|
| 3 | subagent-strategy.md | 下沉(模型 grid→model-selection-grid/Routines/Background 壓縮/Dynamic 緊縮) | ~600 | Agent Input Security 紅線禁動 |
| 4 | context-management.md | 下沉(Compact hint→post-compact-checklist/Cache 健康→cache-health-metrics) | ~350 | Mid-session 禁止三條 + Token Budget 數字紅線禁動 |
| — | 文件衛生 | U9 報告 §4 關 TODO(conflict)；B2 修報告 §5 過期 gap + harness-design L26 補 HARNESS-CARD 路徑 | 0 | research/ 記錄誠實，非 harness 行為變更 |

**目標**：18,990 → **≤17,000**（緩衝 ~2,000B）；若各 cycle 乾淨可續推向 ~16,000。

### 紅線（絕不動，跨 unit 共識）
語言繁中規則 · 生產安全紅線 · OBSERVE 先讀+on-rails · **unverified_success 閘門** · 不可逆操作列舉觸發句 · eval 回歸 ≥5pp→revert · git `-A` 禁用 · 前5/後5 行展示 · Token Budget 數字 · Agent Input Security · RECORD Checkpoint 句。
> 二分原則（U10）：**驗證閘門/安全紅線 = 留**；**為弱模型寫的修辭/枚舉補丁 = 可刪**（core.md §Framework Integrity 自述「為弱模型寫的行為補丁該刪，驗證閘門該留」）。

---

## 4. 後續（記錄不實作）

1. data provenance 標籤（B3 低成本替代，外部輸入來源標記）— 待 OBSERVE 階段識別需求。
2. 先驗過濾 gate（B1）— 待累積 ≥10 cycle eval log 後重評。
3. variant routing（B4）— 待實際觀察到同任務型別 ≥3 次需手動指定同 skill 才升級。
