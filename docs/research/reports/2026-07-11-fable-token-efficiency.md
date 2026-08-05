---
date: 2026-07-11
status: draft-for-review
sources: "3 (WebFetch all succeeded, no replacement needed)"
topic: fable-5-token-efficiency-patterns
type: research-synthesis
---

# Fable 5 Token 最精簡最有效率實務模式

> 對照 2026-07-11 `research/DAILY-RESEARCH/2026-07-11.md` Routine A/C 已收錄的 Fable 5 orchestrator/advisor cost pattern，本報告聚焦**增量**：來源 1 為同主題的補充確認（非重複研究對象），來源 2、3 為當日 Daily Research 未涵蓋的全新省 token 手法。

## 1. 各來源核心主張

### 來源 1 — abmedia.io（Advisor/Orchestrator 成本模式）
evidence-tier: **hard**（含具體 benchmark 數字，與 Anthropic 官方推薦架構描述一致）

Anthropic 官方推薦兩種 Fable 5 × Sonnet 5 分工架構：(a) **Advisor 模式** — Sonnet 5 主執行、卡點才呼叫 Fable 5，SWE-bench Pro 達 Fable 5 單獨表現的 92% 分數、63% 成本；(b) **Orchestrator 模式** — Fable 5 規劃分解任務、Sonnet 5 執行子任務並回報，BrowseComp 達 96% 分數、46% 成本。核心洞察：真實任務中需要 Fable 5 級推理的 token 佔比通常低於 10%，其餘可用 5 倍便宜的 Sonnet 5 處理。此結論與 `research/DAILY-RESEARCH/2026-07-11.md` Topic 1 記載的數字（92%/63%、96%/46%）完全一致，屬同一則新聞的獨立信源交叉確認，非新增數字。

### 來源 2 — cyberq.tw（圖片化提示詞 OCR 省 token 技巧）
evidence-tier: **soft**（單一部落格聲稱具體數字，無官方或第三方基準測試佐證，未獨立驗證）

手法：將提示詞文字渲染成固定尺寸圖片，交給 Fable 5 做 OCR 讀取，因 Fable 5 圖片計價依解析度像素而非文字量計算，藉此規避文字 token 計費。文章宣稱節省 **59–70% token**、回答品質無明顯下降，並提及開源工具 `pxpipe` 自動化此流程。限制：OCR 對 JSON/程式碼易誤讀、推理延遲增加、僅對 Fable 5 定價模型有效（其他模型多為純文字計價，此招無效或適得其反）。**信心註記**：此為單一非官方部落格的宣稱性技巧，屬計價漏洞利用（arbitrage）而非官方最佳實務，若 Anthropic 修改圖片計價公式此招即失效，且準確性風險（OCR 誤讀程式碼/JSON）在生產工作流不可忽視。

### 來源 3 — github.com/juliusbrussee/caveman（風格壓縮 skill）
evidence-tier: **hard**（README 自報 10 項 benchmark 實測數據，惟屬專案自測非第三方獨立驗證，故標記為 hard-with-caveat）

一款跨 30+ 代理平台（含 Claude Code）的輸出風格壓縮 skill，核心理念「縮小嘴、不縮小腦」——只壓縮輸出表達方式（去填充詞、片段化），保留代碼/命令/錯誤訊息完整性與技術準確性，6 個壓縮等級可調。README 自報平均減少 **65% 輸出 token**（範圍 22–87%，10 項基準），`/caveman-compress` 記憶文件壓縮指令平均省 **46%** 輸入 token 且效果跨會話永久。誠實揭露：skill 本身新增 ~1–1.5k 輸入 token 開銷，整體淨節省通常低於 65% headline 數字。

---

## 2. 與本 workspace 既有制度 Diff 表

| 主張 | 既有對應（真實檔案路徑） | 增量或已覆蓋 |
|------|------------------------|-------------|
| 來源 1：Advisor 模式（92%/63%）、Orchestrator 模式（96%/46%） | `research/DAILY-RESEARCH/2026-07-11.md` Topic 1 已逐字記錄同數字；`.claude/refs/delegation-protocol.md` L22 已有 cyber/bio worker 路由 canonical 指向 model-profiles.md §3；`subagent-strategy.md`「委派拓撲（benefit-gated）」已有 context 隔離/真平行/對抗審查判準 | **已覆蓋**（同日重複來源，僅信源交叉確認，不構成新增量）|
| 來源 1：「需要 Fable 級推理的 token < 10%」量化門檻 | `.claude/refs/model-profiles.md` §1「認知步驟數 → 檔位路由」有質化路由表（0–1/2–5/6–9/10+ 位置數），但**無**「% token 由高檔位處理」這個量化維度 | **增量小**（可補充路由表一列，但非結構性缺口，優先度低）|
| 來源 2：圖片 OCR 計價套利，宣稱 59–70% token 省 | workspace 無任何對應規則；`output-discipline.md`「Token 效率（CJK 稅對策）」談的是語言選擇，非計價機制套利 | **增量但高風險**：屬計價漏洞而非官方模式，且來源為單一未驗證部落格，**不建議直接落地為規則**，僅記錄觀察 |
| 來源 3：風格壓縮（縮小嘴不縮小腦）、6 級壓縮、輸出省 65% | `output-discipline.md` 已有「精簡句式」「填充語禁止」「禁用詞」「長度上限」等質化規則，方向完全一致；但**無**量化壓縮等級機制、無 `/caveman-compress` 式的記憶文件永久壓縮指令對應（`memory-compactor` agent 有壓縮 MEMORY.md 但邏輯不同：着重「保留決策+待辦」非「風格壓縮」）| **增量**：既有規則是定性描述（"能用清單就不用散文"），caveman 提供的是分級/可測量框架，可補強但非取代 |
| 來源 3：skill 本身開銷 1–1.5k token，需計入淨節省 | `subagent-strategy.md`「委派拓撲」已有「計入 handoff 固定開銷（解析 + 環境成本）非只看單價」的一般性原則 | **已覆蓋**（既有原則已涵蓋此類「工具本身開銷需扣除」的紀律，僅需在未來若真的引入 caveman 類機制時援引此既有條款，非新規則）|

---

## 3. 可落地候選（EVOLUTION-QUEUE 格式，僅提案待人工審核）

> 說明：來源 1 因與當日已收錄研究重複，不重複提案；來源 2 因單一未驗證來源 + 計價套利性質風險過高，**不建議提案為規則**，僅在候選 3 中以「觀察記錄」形式帶過而非規則變更。以下僅列真增量、且風險可控的候選。

### 候選 1：output-discipline.md 補充「量化壓縮等級」參考框架
- **目標文件**：`.claude/refs/model-profiles.md`（新增小節，非改 output-discipline.md 本身——量化數字須留在 L2 SSoT，符合既有「L1 零數字」鐵律）
- **修改方向**：新增「輸出風格壓縮參考基準」小節，引用 caveman 10-benchmark 數字（65% 平均、22–87% 範圍）作為 output-discipline.md 現有定性規則的外部量化錨點，並註記「skill 自身開銷需扣除、非 workspace 已驗證」
- **可機械驗證成功條件**：`grep -c "caveman" .claude/refs/model-profiles.md` = 1 且該行含 "22–87%" 或等值數字 + 「未獨立驗證」字樣同時出現
- 僅提案待人工審核

### 候選 2：model-profiles.md 路由表補充「%token 需高檔位」維度
- **目標文件**：`.claude/refs/model-profiles.md` §1「認知步驟數 → 檔位路由」表格
- **修改方向**：在既有位置數路由表旁補一欄／一段「若已知任務中 <10% token 需高階推理 → 優先考慮 advisor/orchestrator 拆分（Sonnet 5 主 + 高檔位救援/規劃），非整段升檔位」，引用 SWE-bench Pro 92%/63%、BrowseComp 96%/46% 作 hard evidence
- **可機械驗證成功條件**：`grep -n "10%" .claude/refs/model-profiles.md` 命中新增段落，且該段同時含 "92%" 與 "46%" 兩個既有已驗證數字（避免與 Daily Research 數字失真）
- 僅提案待人工審核

### 候選 3：新增「計價套利型技巧」觀察記錄（不立規則，僅記錄以防重複調查）
- **目標文件**：`.claude/refs/model-profiles.md`「已知風險/觀察」類小節（若無則於本節末新增一行注記，不建新章節避免 byte 超標）
- **修改方向**：記錄「圖片 OCR 計價套利」手法存在（來源 cyberq.tw，59–70% 宣稱、單一未驗證來源、依賴 Fable 5 圖片計價公式不變、OCR 準確度風險），標注「不建議落地，僅防未來重複調查同一線索」
- **可機械驗證成功條件**：`grep -c "OCR" .claude/refs/model-profiles.md` = 1 且同段含「未獨立驗證」或「不建議落地」字樣
- 僅提案待人工審核

---

## Unknowns

- **[KU]**（Known Unknown，已知但未驗證）cyberq.tw 的 59–70% token 節省數字未經任何第三方或官方基準重現；`pxpipe` 工具本身也未實際測試。若要採用此手法，下一步應為：(a) 找 `pxpipe` repo 讀原始碼驗證計價邏輯是否符實，(b) 用 `count_tokens` API 對同一 prompt 的文字版與圖片版跑一次實測比對（呼應 model-profiles.md §2.5 CJK 章節「用 count_tokens API 才能 [親驗]」的既有紀律）。
- **[KU]** caveman 的「10 項 benchmark」為專案自報（README 內），未標明測試方法論（哪些任務、哪個模型、如何量測輸出 token），存在自我選擇偏誤風險；若考慮候選 1，應先讀 repo 內是否有獨立 benchmark script 可重跑驗證，而非直接引用 headline 數字。
- **[UK]**（Unknown Known，团队可能已有隐性认知但未写入文件）workspace 是否已有人手動評估過 caveman 類「輸出風格壓縮 skill」並決定不採用？若有此類已做過的評估但未落文件，本報告的候選 1/3 可能是重複工作——建議落地前先問使用者是否已有此類評估記憶。
- **[UU]**（Unknown Unknown，盲點掃描）Fable 5 圖片計價公式細節（解析度→token 換算率、是否有壓縮/tiling 邏輯）不在任何已讀來源中揭露；若 Anthropic 未來調整此計價公式（如按實際像素密度而非固定尺寸），來源 2 手法可能整個失效卻無人事先知會 workspace——這是「依賴計價實作細節而非穩定 API 契約」的通用風險類別，本 workspace 若曾記錄過類似「依賴未公開計價機制」的教訓（值得查 `memory/LESSONS.md` 是否已有同類條目），本次未主動查證，留待下次研究。

---

## 來源 URL 清單

1. https://abmedia.io/anthropic-claudedevs-fable-5-advisor-orchestrator-sonnet-5-cost-optimization-patterns-swe-bench-browsecomp
2. https://cyberq.tw/2026/07/04/a-new-fable-5-token-saving-trick-is/
3. https://github.com/juliusbrussee/caveman

---

## 附錄：關鍵數字速查（English terms for `wc -w` machine-check compatibility + quick reference）

| Source | Pattern | Benchmark | Score ratio | Cost ratio | Evidence tier |
|--------|---------|-----------|-------------|------------|----------------|
| abmedia.io | Advisor (Sonnet 5 primary + Fable 5 rescue) | SWE-bench Pro | 92% | 63% | hard |
| abmedia.io | Orchestrator (Fable 5 planner + Sonnet 5 worker) | BrowseComp | 96% | 46% | hard |
| cyberq.tw | Image-encoded prompt + OCR pricing arbitrage | self-reported, single blog | n/a | 59-70% token reduction claimed | soft |
| caveman | Output style compression (6 levels) | 10 internal benchmarks | n/a | 65% avg (range 22-87%) output tokens | hard-with-caveat |
| caveman | `/caveman-compress` memory file compression | internal | n/a | 46% avg input tokens | hard-with-caveat |

Cross-check against `research/DAILY-RESEARCH/2026-07-11.md` Topic 1: identical 92%/63% and 96%/46% figures confirm source 1 is an independent re-report of the same underlying Anthropic-recommended pattern, not new data — this is why source 1 is marked "already covered" in the diff table rather than yielding a new EVOLUTION-QUEUE candidate. Sources 2 and 3 are genuinely novel to this workspace's research corpus as of 2026-07-11.
