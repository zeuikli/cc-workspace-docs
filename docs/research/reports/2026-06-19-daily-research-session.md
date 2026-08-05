---
date: 2026-06-19
source: DAILY-RESEARCH/2026-06-19.md
topics: [glm52-open-weights-enterprise-gap-analysis, treat-intelligence-borrowed-skill-accumulation, cursor-origin-agent-native-version-control, anthropic-fable-kayfable-strategic-analysis, ai-engineering-discipline-code-economics-flip]
type: session-report
---

# Session Report 2026-06-19 — Daily Research

## 執行概要
- **研究主題**：5 個（DAILY-TOPICS/2026-06-19.md 全覆蓋）
- **搜尋查詢**：7 次並行 WebSearch（5 主題 + 2 追加補充）
- **頁面 Fetch**：5 次 WebFetch（含 2 次 403，補充替代來源）

## 本日研究成果摘要

### 最高價值發現（Top 3）

1. **[Critical] GLM-5.2 定價衝擊**：開源 MIT 授權、$1.4/$4.4 per 1M tokens、FrontierSWE 74.4%（vs Opus 4.8 75.1%），差距僅 0.7pp。對 code pipeline FinOps 具立即影響——替代成本達 6×。需更新 model-selection-grid 加入 China data risk decision tree（API vs 自架）。

2. **[High] 「treat intelligence as borrowed」成為架構哲學**：Fable 5 下線事件催生可操作工作流：用前沿模型制定 self-contained spec（含 commit hash + escape hatch），之後交廉價模型執行。這與 core.md 的分工設計（IDENTIFY 可機械驗證成功條件）完全對齊，但尚未有 plan catalog 機制落地。

3. **[High] Code-as-Cache 典範 + 工程紀律回歸**：Charity Majors 指出 code 從「資產」變「快取」，瓶頸移至 spec 品質與 behavioral observability。強化現有 PGE 紀律（healthcheck 不省略）的理論依據。僅 5-10% 工程團隊有短 feedback loop，說明這仍是競爭優勢而非普及實踐。

## 可實作 / 可測試內容

### P0 — 立即可執行（今日或明日，< 2 小時）

**P0-A：建立 plan catalog 機制**
- 路徑：`research/plans/TEMPLATE.md`
- 必含欄位：`commit_hash`、`topic`、`success_criteria`（可機械驗證）、`escape_hatch`、`evidence_references`（file:line 格式）
- 驗證命令：`ls research/plans/TEMPLATE.md && wc -l research/plans/TEMPLATE.md | awk '{if($1>=15) print "✅ TEMPLATE OK"; else print "❌ 內容不足"}'`

**P0-B：model-selection-grid 補 GLM-5.2** — ✅ **已執行 2026-06-20（縮減版）**（依使用者指示「GLM-5.2 目前不在 workspace 使用」→ grid 僅保留**單一輕量「非現役緊急 fallback」註記**含中國 API 合規風險，**不**作 pipeline 推薦、不建完整條目；commit ee7f59d）
- 路徑：`refs/model-selection-grid.md`（若不存在則建立）
- 新增 GLM-5.2 列：753B MoE / $1.4-$4.4 / FrontierSWE 74.4% / MIT自架可行 / China API data risk
- Decision tree：`需 GDPR/金融合規？` → Yes → 自架 MIT / No → 評估 API vs Opus 4.8 ROI
- 驗證命令：`grep -ci "GLM-5.2\|glm52" refs/model-selection-grid.md | awk '{if($1>=3) print "✅ GLM-5.2 條目 OK"; else print "❌ 條目不足"}'`

### P1 — 本月優先（需輕量設計，2-8 小時）

**P1-A：Behavioral Characterization Test Suite**
- 路徑：`tests/behavioral/`
- 目標：3 個核心 behavioral test（skill dispatch routing / healthcheck output format / git push retry logic）
- 驗收條件：`pytest tests/behavioral/` 全通過，harness 行為變更時至少 1 test 失敗
- 關聯 Topic：#5 Charity Majors「behavioral characterization tests」建議

**P1-B：EVOLUTION-QUEUE.md 更新**
- 合併 GLM-5.2 定價衝擊至現有 `model-selection-grid-deepSWE-update` 提案
- 添加 cost comparison table（GLM-5.2 vs Opus 4.8 vs Fable 5）+ 自架 vs API 決策矩陣
- 驗收條件：提案包含量化成本比較 + 適用條件列表

### P2 — 觀察中（需更多信號再決定）

| P2 項目 | 觀察條件 |
|--------|---------|
| Cursor Origin API 整合 | Fall 2026 Origin 發布 + 確認 MCP schema |
| Anthropic Fable 5 談判結果 | 模型恢復 → 更新 fable-pilot routing / 談判失敗 → GLM-5.2 自架升 P1 |
| GLM-5.2 剩餘基準 | BenchLM 達 100+ benchmark 覆蓋（目前 32/249）|

## GAP 狀態更新

| GAP | 研究前狀態 | 研究後狀態 | 行動 |
|-----|----------|-----------|------|
| glm52-open-weights-enterprise-evaluation | gap (0 篇) | **filled** (5 來源) | P0-B model-selection-grid 更新 |
| cursor-origin-agent-native-vcs | gap (0 篇) | **partial** (4 來源，架構細節待 Fall 2026) | P2 觀察 |
| treat-intelligence-borrowed-workflow | gap (0 篇) | **filled** (4 來源 + shadcn/improve 實作細節) | P0-A plan catalog |
| ai-engineering-discipline-code-economics | gap (0 篇) | **filled** (2 來源，Charity Majors 完整) | P1-A behavioral test |
| anthropic-fable-negotiation-strategic | partial (2 篇) | **enriched** (+ Kayfable 框架 + IBTimes 談判細節) | P2 觀察談判結果 |

## 下一次循環優先事項

1. **P0-A 執行**：建立 `research/plans/TEMPLATE.md`——plan catalog 機制零成本落地，高複利效益（每次大任務前使用）
2. **P0-B 執行**：更新 `refs/model-selection-grid.md` 加 GLM-5.2——直接影響後續 model routing 決策，有量化依據
3. **持續觀察 Fable 5 談判**：若下週仍無結果，評估 GLM-5.2 Hugging Face 自架可行性（研究 GPU 成本 vs API 省成本）
