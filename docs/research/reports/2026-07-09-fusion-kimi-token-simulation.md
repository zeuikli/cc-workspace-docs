---
title: "Fusion 架構 Token 節省量化模擬（5 種典型 workspace 任務）"
date: 2026-07-09
status: proposed
authors: [Kimi-K2.7-Code]
inputs: ["research/reports/2026-07-09-fusion-architecture-design-plan.md (§2 Fusion 架構, §3 Token 節省策略)", ".claude/refs/model-profiles.md (§0 四檔位定價表, §1 路由, §2.3 定價矩陣, §2.4 cache 門檻)", ".claude/refs/delegation-protocol.md (§1 指揮官不下場, §2 檔位與參數, §3 交辦三要素, §4 回報合約, §6 驗證不自驗)", "research/DAILY-RESEARCH/2026-06-28.md (Vercel TS7 700M 行遷移案例)"]
related: [research/reports/2026-07-09-fusion-architecture-design-plan.md]
type: token-simulation-report
---

# Fusion 架構 Token 節省量化模擬

> 本報告執行 GLM×Kimi 執行計畫的 **任務 KIMI-A**（見 fusion-architecture-design-plan.md §4.3）。
> 方法: 用 `model-profiles.md` §0/§2.3 官方定價矩陣 + `delegation-protocol.md` §2/§3 委派門檻, 模擬 5 種典型 workspace 任務在「現有 multi-mode 架構」與「通用 Fusion 架構」下的加權 token 成本, 並附節省百分比。
> 所有定價數字取自 `model-profiles.md` §2.3（per 1M tokens, 標準 in/out）, 未編造。token 估算基於 `delegation-protocol.md` §3 交辦三要素的 context 大小量級 + §4 回報合約的回灌限制。品質影響參考 fusion-architecture-design-plan.md §3.3 品質保障機制。

---

## §1 模擬方法與共用參數

### 1.1 官方定價矩陣（來源: model-profiles.md §0 + §2.3）

| 檔位 | 當代模型 | Standard in/out (per 1M) | Diff 軟上限 | prompt cache 最低門檻 |
|------|---------|--------------------------|------------|---------------------|
| cost | Haiku 4.5 | $1 / $5 | ≤30 行 | 4,096 tokens |
| quality | Sonnet 5 | $3 / $15 | ≤120 行 | 2,048 tokens |
| ceiling | Opus 4.8 | $5 / $25 | ≤300 行 | 4,096 tokens |
| frontier | Fable 5 | $10 / $50 | ≤600 行（機讀兜底）| 2,048 tokens |

> 註: Sonnet 5 intro 定價 $2/$10 至 2026-08-31; 本模擬採標準 $3/$15（intro 為限時優惠, 非長期成本基線）。
> 註: ceiling tokenizer 較舊版多耗 ~35% token（§2.3 註記）→ 本模擬對 ceiling 模型 input 乘 1.35 修正因子; cost/quality 模型不加乘。

### 1.2 現有架構 vs Fusion 架構（模型分配原則）

| 項目 | 現有 multi-mode 架構 | Fusion 架構 |
|------|---------------------|------------|
| 主對話模型 | 依位置數路由（0-1→cost, 2-9→quality, 10+/架構→ceiling, 稀缺→frontier）| ceiling（規劃/審查）; 簡單任務例外可降 quality |
| Sidekick 模型 | N/A（現有無持久 sidekick; sub-agent 一次性 spawn 用同檔位或降一檔）| cost（機械執行/測試/掃描）|
| Compaction 模型 | 用當前主對話模型 | cost（Haiku 4.5, compaction 非推理）|
| 委派策略 | delegation-protocol.md §1（預設委派, 例外親做）| 同 + sidekick 預設承接機械任務 |
| 回報合約 | §4 只回結論 + 檔案:行號 | 同 |
| 驗證 | §6 驗證不自驗 + 異模型互審鏈 | 同 + sidekick 產出由 main 機械重驗 |

### 1.3 token 估算量級（基準假設）

- **CLAUDE.md/AGENTS.md auto-load 穩定前綴**: ~8,000 input tokens（常駐; cache 命中後近免費, 首次全額）。
- **單檔讀取**: ~2,000 input tokens（中型檔案; 大檔 5,000+）。
- **sub-agent 交辦 prompt**: ~1,500 input tokens（交辦三要素完整欄位, task-templates.md 五型態）。
- **sub-agent 回報**: ≤500 input tokens（§4 只回結論 + 檔案:行號; 長產物存檔回傳路徑 + ≤10 行摘要）。
- **工具呼叫結果回灌**: ~800 input tokens/次（grep/read 結果）。
- **output tokens**: diff 行數 × ~8 tokens/行（含推理 + 程式碼）; 報告類 ~6 tokens/行。
- **compaction**: 壓縮全 context 的 ~30% 為 summary output, 並以全 context 為 input。

### 1.4 節省計算公式

```
單任務成本 = Σ(input_tokens_i × price_in_model_i / 1M) + Σ(output_tokens_i × price_out_model_i / 1M)

節省 % = (現有成本 - Fusion 成本) / 現有成本 × 100

Fusion 五層優化（報告 §3.2）對應的節省槓桿:
- Layer 1 模型路由: 機械 token 從 quality/ceiling 價 → cost 價（5×-15× 單價差）
- Layer 2 Cache: compaction 用 cost 模型 + 切換綁 compaction 零 cache 懲罰
- Layer 3 Context: sub-agent 回報只結論（§4）, 減主對話 input
- Layer 4 委派: 預設委派 sidekick, main 只花在規劃/審查
- Layer 5 輸出: 結構化摘要, 不灌原文
```

---

## §2 五種任務模擬

### 任務 1: 單檔小改（0-1 檔, ≤3 工具呼叫, ≤30 行 diff）

**任務描述**: 改單一函式簽名或修單一 bug, 讀 1 檔, 1-2 次 grep, 30 行 diff。

**現有架構路由**: 0-1 位置 → cost 檔（Haiku 4.5）親做（delegation-protocol.md §1 T0 例外: ≤3 工具呼叫親做, 不委派）。

**Fusion 架構路由**: 主對話 ceiling 規劃 + sidekick cost 執行; 但本任務屬 T0（≤3 工具呼叫）→ main 親做例外仍適用, sidekick 不介入。主要節省來自 compaction 用 cost 模型（若觸發）。

#### 對比表

| 維度 | 現有架構 | Fusion 架構 | 節省 |
|------|---------|------------|------|
| 主對話模型 | cost (Haiku 4.5) | cost (T0 例外, main 親做) | — |
| Sidekick 模型 | N/A | N/A（T0 不委派） | — |
| Compaction 模型 | cost（=主對話） | cost（同） | — |
| 估算 input tokens | 10,500（8k 前綴 + 2k 檔 + 500 工具） | 10,500（同） | 0% |
| 估算 output tokens | 240（30 行 × 8） | 240（同） | 0% |
| 估算成本（USD） | $0.0105 + $0.0012 = $0.0117 | $0.0117（同） | **0%** |
| 品質影響 | baseline | 維持（T0 例外不變） | 無差異; T0 親做原則兩架構一致 |

**註**: 本任務 token 量小, Fusion 的 sidekick 路由不適用（T0 例外）。若 session 中途觸發 compaction, Fusion 用 cost 模型與現有相同（現有主對話已是 cost）→ 節省為 0。Fusion 對此類任務無優勢, 與報告 §3.1「T0 存在理由: fan-out 協調成本 > 收益」一致。

---

### 任務 2: 跨模組重構（6-9 檔, 跨 2-3 模組, ~120 行 diff）

**任務描述**: 重構 2-3 模組介面, 讀 8 檔, ~10 工具呼叫, 120 行 diff（quality 檔上限邊界）。

**現有架構路由**: 6-9 位置 → quality 檔（Sonnet 5, effort high）親做; 不委派（≤10 檔門檻內, §1）。

**Fusion 架構路由**: 主對話 ceiling（Opus 4.8）規劃 + 審查; sidekick cost（Haiku 4.5）執行機械讀取/grep/批次編輯; compaction cost。品質: ceiling 規劃 + cost 執行 → 跨模組介面設計由 ceiling 把關, 機械編輯由 cost 完成, main 機械重驗（§6）。

#### 對比表

| 維度 | 現有架構 | Fusion 架構 | 節省 |
|------|---------|------------|------|
| 主對話模型 | quality (Sonnet 5) | ceiling (Opus 4.8) | —（升級, 非降級） |
| Sidekick 模型 | N/A | cost (Haiku 4.5) | — |
| Compaction 模型 | quality | cost (Haiku 4.5) | — |
| 估算 input tokens | 28,000（8k 前綴 + 16k 讀檔 + 4k 工具） | main 15,000 + sidekick 18,000 = 33,000 | +18%（token 增, 但單價降） |
| 估算 output tokens | 960（120 行 × 8） | main 400（規劃/審查） + sidekick 960（執行 diff） = 1,360 | +42%（token 增, 含審查） |
| 估算成本（USD） | in: 28k×$3/1M=$0.084; out: 960×$15/1M=$0.0144 → **$0.0984** | main in: 15k×1.35×$5/1M=$0.1013; main out: 400×$25/1M=$0.010; sidekick in: 18k×$1/1M=$0.018; sidekick out: 960×$5/1M=$0.0048 → **$0.1341** | **-36%（成本增）** |
| 品質影響 | baseline | 提升（ceiling 規劃 + §6 機械重驗） | 跨模組介面由 ceiling 把關, 降回歸風險; 但成本增 |

**註**: 本任務 Fusion 成本反增 36%。原因: 6-9 檔為 quality 甜蜜點（$3/$15）, 升級 main 至 ceiling（$5/$25, 且 tokenizer ×1.35）+ sidekick 額外 context, 加權後超過 quality 親做。Fusion 在此任務類型為「品質換成本」, 非節省。節省需待任務 3-5 的機械比例上升才顯現。

---

### 任務 3: 深度研究（10+ 檔讀取 + WebSearch + 報告撰寫, ~300 行輸出）

**任務描述**: 讀 12 檔 + 5 次 WebSearch + 撰寫 300 行研究報告。研究為 delegation-protocol.md §1 T1 一律委派（讀 >3 檔 + 預期輸出 >100 行）。

**現有架構路由**: 10+ 位置 → ceiling 檔（Opus 4.8, effort xhigh）主對話委派; spawn quality sub-agent 做讀取/搜尋, 主對話收結論後撰寫。或主對話 ceiling 親做全程。

**Fusion 架構路由**: 主對話 ceiling 規劃 + 審查 + 撰寫結論段; sidekick cost 做機械讀取/WebSearch/摘要; compaction cost。品質: ceiling 撰寫 + sidekick 機械掃描, main 機械重驗引用來源（§6 + §3.3 Source-Verify）。

#### 對比表

| 維度 | 現有架構 | Fusion 架構 | 節省 |
|------|---------|------------|------|
| 主對話模型 | ceiling (Opus 4.8) | ceiling (Opus 4.8) | — |
| Sub-agent / Sidekick 模型 | quality (Sonnet 5, 一次性 spawn) | cost (Haiku 4.5, 持久 sidekick) | — |
| Compaction 模型 | ceiling | cost (Haiku 4.5) | — |
| 估算 input tokens | main 45,000 + sub 30,000 = 75,000 | main 30,000 + sidekick 35,000 = 65,000 | -13%（context 隔離 + §4 回報精簡） |
| 估算 output tokens | main 1,800（300 行報告 × 6） + sub 1,500（摘要） = 3,300 | main 1,800 + sidekick 2,000（機械摘要 + 摘要） = 3,800 | +15%（sidekick 摘要量增） |
| 估算成本（USD） | main in: 45k×1.35×$5/1M=$0.3038; main out: 1,800×$25/1M=$0.045; sub in: 30k×$3/1M=$0.09; sub out: 1,500×$15/1M=$0.0225 → **$0.4613** | main in: 30k×1.35×$5/1M=$0.2025; main out: 1,800×$25/1M=$0.045; sidekick in: 35k×$1/1M=$0.035; sidekick out: 2,000×$5/1M=$0.010 → **$0.2925** | **37%** |
| 品質影響 | baseline | 維持/提升 | ceiling 撰寫不變; sidekick 摘要經 main 機械重驗（§6）; 來源驗證由 ceiling 把關（§3.3 Source-Verify） |

**註**: 節省主要來自 Layer 1（sub-agent quality→cost, 機械讀取/搜尋單價降 3×/3×）+ Layer 3（§4 回報精簡減 main input 15k）+ Layer 2（compaction ceiling→cost, 80% 單價降）。品質風險: sidekick 摘要遺漏 → 由 main 機械重驗 + Source-Verify gate 把關。

---

### 任務 4: 安全審查（全 repo grep + pattern matching + 報告, fresh-context 對抗審查）

**任務描述**: 全 repo grep 掃 auth/payment/user-data pattern + 產出威脅報告。強制 fresh-context 異模型對抗審查（§3.3 機制 2 + §6 異模型互審鏈 T2）。

**現有架構路由**: 主對話 quality（Sonnet 5）親做掃描 + 報告; T2 異模型互審 → spawn ceiling sub-agent fresh-context 對抗審查。兩階段。

**Fusion 架構路由**: 主對話 ceiling（Opus 4.8）規劃掃描策略 + 最終威脅判定; sidekick cost（Haiku 4.5）跑機械 grep 批次; 對抗審查由 main ceiling fresh-context 自審（或 spawn frontier/ceiling 異模型）。compaction cost。品質: §3.3 對抗審查 + §6 驗證不自驗不變。

#### 對比表

| 維度 | 現有架構 | Fusion 架構 | 節省 |
|------|---------|------------|------|
| 主對話模型 | quality (Sonnet 5) | ceiling (Opus 4.8) | —（升級） |
| Sub-agent / Sidekick 模型 | ceiling (對抗審查, 一次性) | cost (grep 批次) + ceiling (對抗審查) | — |
| Compaction 模型 | quality | cost (Haiku 4.5) | — |
| 估算 input tokens | main 50,000（grep 結果回灌多） + sub 25,000（fresh-context 審查） = 75,000 | main 22,000（sidekick 回報精簡） + sidekick 40,000（grep） + adversarial 25,000 = 87,000 | +16%（token 增, 但結構化） |
| 估算 output tokens | main 2,400（400 行報告 × 6） + sub 600（審查意見） = 3,000 | main 2,400 + sidekick 1,000（pattern 命中清單） + adversarial 600 = 4,000 | +33% |
| 估算成本（USD） | main in: 50k×$3/1M=$0.15; main out: 2,400×$15/1M=$0.036; sub in: 25k×1.35×$5/1M=$0.1688; sub out: 600×$25/1M=$0.015 → **$0.3698** | main in: 22k×1.35×$5/1M=$0.1485; main out: 2,400×$25/1M=$0.06; sidekick in: 40k×$1/1M=$0.04; sidekick out: 1,000×$5/1M=$0.005; adversarial in: 25k×1.35×$5/1M=$0.1688; adversarial out: 600×$25/1M=$0.015 → **$0.4373** | **-18%（成本增）** |
| 品質影響 | baseline | 提升 | ceiling 主導威脅判定（§3.3 對抗審查由異模型 fresh-context）; sidekick 機械掃描經 main 重驗; eval-hack 風險因 ceiling 升級而升（§2.7 16.6%）→ 需 +對抗稽核（frontier 或 ceiling 互審） |

**註**: 本任務 Fusion 成本增 18%, 但品質提升（ceiling 威脅判定 + 對抗審查）。安全審查為 §3.3 機制 2「重要交付強制對抗審查」場景, 品質優先於成本。Fusion 在此為品質投資, 非節省。若去掉對抗審查（降級場景）, Fusion 可省 ~22%（sidekick cost 取代 quality 掃描 + compaction cost）, 但違反 §3.3 品質保障 → 不採。

---

### 任務 5: 大規模遷移（700M 行類, Vercel TS7 案例, 16 PR 分批）

**任務描述**: 參考 2026-06-28 DAILY-RESEARCH Topic 2: Vercel 7 百萬行 TypeScript 7 遷移, 16 PR 分批, 報告成本 $1,146（Twitter 來源, 確認度中）。Dynamic Workflows 平行 subagents。codemod `npx @ai-sdk/codemod v7` 自動化大部分機械改動。

**現有架構路由**: ceiling 檔（Opus 4.8, effort xhigh, ultracode/dynamic mode）主對話編排; fan-out 16 PR 各 spawn quality sub-agent 執行 codemod + 驗證; 主對話收 PR 結果 + 審查。每 PR ~50 行 diff × 16 = 800 行總 diff（分散）。

**Fusion 架構路由**: 主對話 ceiling（Opus 4.8）規劃 PR 分批策略 + 最終審查; sidekick cost（Haiku 4.5）批次跑 codemod + 機械驗證（16 PR 平行）; compaction cost。品質: §3.3 機制 1「驗證不自驗」+ §6 sidekick 產出由 main 機械重驗; pattern 由 ceiling 解出後降 cost 批次套用（delegation-protocol.md §5 降級判準）。

#### 對比表

| 維度 | 現有架構 | Fusion 架構 | 節省 |
|------|---------|------------|------|
| 主對話模型 | ceiling (Opus 4.8) | ceiling (Opus 4.8) | — |
| Sub-agent / Sidekick 模型 | quality (Sonnet 5, 16 PR × spawn) | cost (Haiku 4.5, 16 PR × sidekick) | — |
| Compaction 模型 | ceiling | cost (Haiku 4.5) | — |
| 估算 input tokens | main 60,000（編排 + 審查） + 16×sub 20,000 = 320,000; 總 380,000 | main 40,000 + 16×sidekick 22,000 = 352,000; 總 392,000 | +3%（token 微增, sidekick context 略大） |
| 估算 output tokens | main 3,000（編排決策） + 16×sub 400（每 PR 50 行 × 8） = 6,400; 總 9,400 | main 3,000 + 16×sidekick 400 = 6,400; 總 9,400 | 0%（output 同） |
| 估算成本（USD） | main in: 60k×1.35×$5/1M=$0.405; main out: 3,000×$25/1M=$0.075; sub in: 320k×$3/1M=$0.96; sub out: 6,400×$15/1M=$0.096 → **$1.536** | main in: 40k×1.35×$5/1M=$0.27; main out: 3,000×$25/1M=$0.075; sidekick in: 352k×$1/1M=$0.352; sidekick out: 6,400×$5/1M=$0.032 → **$0.729** | **53%** |
| 品質影響 | baseline | 維持/提升 | codemod 為機械改動, cost 執行能力足夠; ceiling 解出 pattern 後降 cost 批次套用（§5 降級）; 每個 PR 50 行在 cost 檔 ≤30 行軟上限邊緣 → 需 ceiling 審查每個 PR（已含）; §3.3 機制 5「跨模型互查」可加 ceiling 異模型抽查 2-3 個 PR |

**註**: 節省 53% 主要來自 Layer 1（16 PR 執行從 quality $3/$15 → cost $1/$5, 單價降 3×/3×）+ Layer 4（§5 降級: ceiling 解 pattern → cost 批次套用）+ Layer 2（compaction cost）。對照報告 §3.1 Devin Fusion 35-41% 節省（非 Fable / Fable 配置）, 本模擬 53% 略高, 因大規模遷移機械比例極高（codemod 自動化）+ 16 PR 平行放大 cost 單價優勢。實際 Vercel 案例報告 $1,146 為全 Dynamic Workflow 成本（含編排 overhead）, 本模擬為單任務邏輯成本, 量級不同, 僅供架構對比。

---

## §3 彙整表: 5 種任務加權平均節省

### 3.1 單任務節省百分比彙整

| # | 任務類型 | 現有成本 | Fusion 成本 | 節省 % | 品質影響 | 主要節省來源（Layer） |
|---|---------|---------|------------|--------|---------|---------------------|
| 1 | 單檔小改 | $0.0117 | $0.0117 | **0%** | 維持 | 無（T0 例外） |
| 2 | 跨模組重構 | $0.0984 | $0.1341 | **-36%**（增） | 提升 | 無節省; ceiling 升級 + sidekick overhead |
| 3 | 深度研究 | $0.4613 | $0.2925 | **37%** | 維持/提升 | L1（sub→cost）+ L3（§4 回報精簡）+ L2（compaction cost） |
| 4 | 安全審查 | $0.3698 | $0.4373 | **-18%**（增） | 提升 | 無節省; ceiling 主導 + 對抗審查投資 |
| 5 | 大規模遷移 | $1.536 | $0.729 | **53%** | 維持/提升 | L1（16PR → cost）+ L4（§5 降級批次）+ L2 |

### 3.2 加權平均（依 workspace 任務頻率估計）

> 權重基於 workspace 22 份 DAILY-RESEARCH + 22 份 Session Reports 的任務類型分佈粗估（非精確統計）。

| 任務類型 | 估計頻率權重 | 節省 % | 加權貢獻 |
|---------|------------|--------|---------|
| 單檔小改 | 40% | 0% | 0% |
| 跨模組重構 | 25% | -36% | -9.0% |
| 深度研究 | 20% | 37% | +7.4% |
| 安全審查 | 5% | -18% | -0.9% |
| 大規模遷移 | 10% | 53% | +5.3% |
| **加權平均** | 100% | — | **+2.8%** |

### 3.3 成本加權（依 USD 金額加權, 反映實際支出結構）

> token 成本加權比頻率加權更能反映實際節省, 因大規模遷移單任務成本遠高於單檔小改。

| 任務類型 | 現有成本 | Fusion 成本 | 佔現有總成本比 | 加權貢獻 |
|---------|---------|------------|--------------|---------|
| 單檔小改 | $0.0117 | $0.0117 | 0.5% | 0% |
| 跨模組重構 | $0.0984 | $0.1341 | 4.0% | -1.4%（成本增） |
| 深度研究 | $0.4613 | $0.2925 | 18.6% | +6.8%（節省） |
| 安全審查 | $0.3698 | $0.4373 | 14.9% | -2.7%（成本增） |
| 大規模遷移 | $1.536 | $0.729 | 62.0% | +32.6%（節省） |
| **成本加權平均** | $2.477 | $1.605 | 100% | **+35.2%（節省）** |

### 3.4 兩種加權結果對比

| 加權方式 | 結果 | 解讀 |
|---------|------|------|
| 頻率加權 | +2.8%（微節省） | 若以「任務次數」算, Fusion 因跨模組/安全審查品質投資而幾乎不省 |
| 成本加權 | +35.2%（顯著節省） | 若以「USD 支出」算, Fusion 因大規模遷移佔 62% 成本且省 53% 而顯著節省 |

**結論**: Fusion 架構的 token 節省高度依賴任務結構。機械比例高的任務（大規模遷移、深度研究的掃描段）節省顯著; 品質投資型任務（跨模組重構、安全審查）成本反增但品質提升; T0 例外任務無差異。與報告 §3.1 Devin Fusion 35-41% 節省的對齊: 成本加權 35.2% 落在 Devin Fusion 35-41% 區間下緣, 驗證本模擬量級合理。

---

## §4 品質保障對齊（報告 §3.3）

本模擬的品質影響評估均參考報告 §3.3 四項品質保障機制:

1. **驗證不自驗（§6）**: sidekick 產出由 main 機械重驗 → 適用任務 3/5（機械執行 sidekick）。
2. **對抗審查**: 重要交付 fresh-context 異模型審查 → 適用任務 4（安全審查）+ 任務 2（跨模組架構）。
3. **eval-hack 防護**: 檔位越高驗證越嚴 → 任務 4 ceiling 升級帶來 16.6% eval-hack 風險（§2.7）, 需 +對抗稽核。
4. **量化委派基準**: sqlite-utils 案例（37 prompts / 5 blockers / $149.25）作校準錨點 → 本模擬單任務成本 $0.01-$1.5 遠低於此基線, 因本模擬為邏輯成本（不含 session overhead / 重試 / 編排）, 量級差異屬正常。
5. **跨模型互查**: verdict 非證據 → sidekick 回報的「成功」需 main 機械重驗, 不信自評。

---

## §5 限制與不確定性

1. **token 估算為量級近似**: 實際 token 受 tokenizer（Sonnet 5 新 tokenizer +30%, ceiling +35%）+ CJK 倍率（§2.5, 繁中 1.3-2.3×）+ 檔案大小分佈影響, 本模擬用中位假設, 未逐案 count_tokens。
2. **Vercel TS7 案例確認度中**: $1,146 為 Twitter DeepSRT 來源, 未經 Vercel 官方確認（2026-06-28 DAILY-RESEARCH P2-2 待驗證）; 本模擬僅引用「16 PR + 700M 行 + 機械 codemod」結構, 不依賴該數字。
3. **權重為粗估**: §3.2 頻率權重基於 workspace 報告分佈主觀估計, 非精確統計; 實際 workspace 任務結構需跑 `evolution/cost-log.jsonl` 統計才精確。
4. **Fusion 假設 sidekick 持久 context**: 報告 §2.3 Phase 1 Claude Code 路徑 sidekick 為一次性 spawn, 真正持久 context 需 Phase 2（Claude Code 新功能）或 Factory 路徑。本模擬假設 Phase 2/Factory 已落地, 否則 sidekick 重複 context 建構會侵蝕節省。
5. **未計 session overhead**: 實際成本含 session init / auto-load / hook 執行 / handoff 解析等固定開銷（O9: cost 檔位固定開銷 76.2k tokens > quality 73.9k）, 本模擬為單任務邏輯成本, 實際節省會被 overhead 侵蝕, 尤其任務 1（單檔小改）。
6. **品質提升未量化**: 任務 2/4 成本增但品質提升（ceiling 規劃 + 對抗審查）, 本模擬僅標「提升」, 未將品質收益貨幣化; ROI 評估需另跑 eval（§2.6 baseline 47/50 vs 41/50）。

---

## §6 驗收對照（fusion-architecture-design-plan.md §4.5 KIMI-A）

| 驗收條件 | 本報告狀態 |
|---------|-----------|
| 5 種任務均有對比表 + 節省 % | ✅ §2 每種任務含「現有 vs Fusion」對比表 + 節省 % |
| 用 model-profiles.md §2.3 官方定價 | ✅ §1.1 引用 §0 + §2.3, 未編造 |
| token 估算基於 delegation-protocol.md §3 | ✅ §1.3 量級基於交辦三要素 + §4 回報合約 |
| 品質影響參考報告 §3.3 | ✅ §4 逐項對齊 §3.3 四機制 |
| 加權平均節省百分比 | ✅ §3.2 頻率加權 +2.8% / §3.3 成本加權 +35.2% |

---

*報告完成 2026-07-09 · Kimi K2.7 Code · 產出路徑: research/reports/2026-07-09-fusion-kimi-token-simulation.md*
