# Career Wiki Schema

> **Pattern**: Karpathy LLM Wiki (2026-04)
> **Three-layer**: Raw sources → Wiki pages (LLM-owned) → Schema (this file)
> **Three ops**: Ingest / Query / Lint
> **Owner**: Zeuik Li | **Started**: 2026-04-21

---

## 目的

把 Zeuik 跨 8 段職涯（2013–2026，10+ 年）的可重複方法論、踩坑、關鍵決策，壓縮成 LLM 可即時檢索的知識庫。

- **不是履歷** — 履歷是給人看的；wiki 是給 agent 用的（含流程、參數、判斷閾值）。
- **不是事後美化** — 寫下真實發生的失敗與妥協，否則失去決策價值。
- **每頁 ≤ 400 行** — 超過拆子頁；LLM 每次檢索只應載入最小需要範圍。

---

## 三層結構

```
research/career-wiki/
├── schema.md              ← 本檔（結構定義、不 LLM-modified）
├── INDEX.md               ← 導航表（LLM 可更新）
├── raw/                   ← 原始素材（immutable）
│   ├── career-summary.md  ← 履歷全文 + 時序
│   └── artifacts/         ← 真實工件（censored 後的 Terraform snippet、runbook 片段）
└── pages/                 ← LLM-owned wiki pages（可 ingest/query/lint）
    ├── {domain}.md        ← 跨職涯主題頁（redis-zero-downtime, iso27017-audit, ...）
    └── {company}-lessons.md ← 職涯段 lessons learned（soundon-lessons.md ...）
```

---

## Page 標準格式（必守）

每個 `pages/*.md` 必須包含以下 sections，**順序固定**：

```markdown
# {Page Title}

> **Source positions**: {職涯段清單，例如 SoundOn 2022-2023, KKStream 2019-2021}
> **Last ingested**: {YYYY-MM-DD}
> **Confidence**: {high|medium|low} — 真實執行過 / 旁觀過 / 推論的
> **Linted**: {YYYY-MM-DD}

## Context

1-2 句話：什麼情境會需要這個知識？誰會問？

## Core Methodology

3-5 個步驟，每個步驟含：
- **What**: 做什麼
- **Why**: 為什麼這樣做（含原因，不只命令）
- **Gotcha**: 真實踩過的坑（來自哪段職涯）

## Concrete Numbers

| 指標 | 值 | 來源場景 |
|------|----|---------|
| ... | ... | ... |

**原則**：不說「大幅降低」，說「降低 X%，節省 $Y/月」— 沿用 CLAUDE.md 的 FinOps 偏好。

## Anti-patterns（不要做）

至少 2 個反面案例 — 來自真實踩坑。

## Decision Tree

> 什麼情境該用這個方法？什麼情境不該用？

## References

- 職涯段落摘要
- 外部權威來源（官方文件 URL）
- 關聯 wiki pages（用 [[page-name]] 語法）
```

---

## Three Ops

### 1. Ingest（新增/更新）

**觸發**：新職涯事件、新踩坑、新學到方法論。

**流程**：
1. 先補 `raw/` 下的原始素材（真實數據/事件）
2. 決定影響的 pages（通常 1–3 個，不超過 5 個）
3. 每個 page 更新 `## Last ingested` + 相關 section
4. 更新 `INDEX.md` 的 last-updated 標記

### 2. Query（檢索）

**觸發**：`zeuik-senior-architect` agent 被諮詢、用戶問「以前遇過類似的嗎」。

**流程**：
1. 讀 `INDEX.md` 找候選 pages（≤3 個）
2. 只讀需要的 sections（Core Methodology / Concrete Numbers / Anti-patterns）
3. 引用時標註 `pages/{name}.md#section`
4. 若找不到：**明說** wiki 沒有此主題，建議 ingest

### 3. Lint（健康檢查）

**觸發**：每 2 週或新 ingest 5 個 pages 後。

**檢查項**：
- [ ] 是否有 page > 400 行？拆子頁
- [ ] 是否有兩頁互相矛盾的陳述？標紅 + 在 INDEX 列 review
- [ ] 是否有 page > 90 天未 ingest？標 stale
- [ ] 是否有 page 缺 Concrete Numbers section？補實際數字
- [ ] 是否有 orphan page（沒被 INDEX 或其他 page 引用）？評估保留/刪除

**工具**：`scripts/wiki-lint.sh`（待建立於 Session 4）。

---

## Naming Conventions

| 類型 | 格式 | 範例 |
|------|------|------|
| Domain page | `{topic-kebab}.md` | `redis-zero-downtime.md` |
| Company lessons | `{company}-lessons.md` | `soundon-lessons.md` |
| Raw artifact | `raw/artifacts/{company}-{topic}.md` | `raw/artifacts/kkstream-stepfn-draft.md` |

**Topic list**（Zeuik 職涯橫跨主題，非 exhaustive）：
- `redis-zero-downtime`、`postgres-microsec-tuning`、`postgres-upgrade-sop`
- `iso27017-audit`、`gcp-landing-zone`、`terraform-multi-cloud`
- `cdn-cache-tuning`、`high-traffic-media-arch`
- `aws-step-functions-patterns`、`kafka-confluent-streaming`
- `kernel-tuning-mmorpg`、`haproxy-patterns`
- `vmware-nsx-security-zone`、`commvault-migration`
- `stripe-serverless-fintech`、`finops-savings-plans-roi`

---

## Quality Bars

- **Concrete > Abstract**：「PG 13→15 pglogical 升級」> 「PG 版本升級」
- **Numbers > Adjectives**：「RTT 降 2ms」> 「大幅降低延遲」
- **Gotchas > Best Practices**：業界最佳實踐網路到處有；踩坑記憶是差異化
- **Honesty > Polish**：失敗的嘗試與妥協要寫進去（`Anti-patterns` 或 `Gotcha`）

---

## Interaction with Other Workspace Components

| 互動對象 | 關係 |
|---------|------|
| `.claude/agents/zeuik-senior-architect.md` | Primary consumer — 諮詢時讀 wiki pages |
| `.claude/skills/autoresearch/SKILL.md` | Extend `:wiki` subcommand — Ingest/Query/Lint loops |
| `.claude/skills/finops/SKILL.md` | wiki 提供歷史 Savings Plan ROI 真實數字作佐證 |
| `.claude/skills/sre-incident/SKILL.md` | wiki 提供踩坑參考（`{topic}.md#anti-patterns`）|
| `.claude/skills/tech-eval/SKILL.md` | wiki 提供跨廠商真實經驗作評分依據 |
| `CLAUDE.md` | 新增按需觸發詞：「以前怎麼做的」「踩過類似坑嗎」|

---

## LOG.md 規範（Karpathy append-only op log）

`research/career-wiki/LOG.md` 是 wiki 操作的不可刪除歷史紀錄。

**Entry 格式**：
```
## [OP] YYYY-MM-DD — 一句摘要
- Action: 做了什麼
- Outcome: 結果（pages created/updated, issues found）
- By: 誰執行（agent name 或 human）
- Ref: 相關報告或 PR（選填）
```

**OP prefix 清單**：
| Prefix | 說明 |
|--------|------|
| `[INGEST]` | 新增/更新 wiki pages |
| `[QUERY]` | 重要查詢並產生新 page |
| `[LINT]` | wiki 健康檢查 |
| `[EVOLVE]` | 架構/schema 更新 |

**不可刪除**：append-only，錯誤用新條目修正，不改舊條目。

---

## Version

- **v0.1** (2026-04-21): Initial schema + 2 pilot pages + senior-architect agent
- **v0.2** (2026-05-25): LOG.md 規範新增（Karpathy pattern completeness）
- 後續版本走 git log 追蹤
