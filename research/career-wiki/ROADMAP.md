# Career-Wiki Roadmap

> **Session 1（2026-04-21, 已完成）**：scaffold + 2 pilot pages + senior-architect agent + Medium 索引
> **Session 2–4**：按下方規劃逐步執行

---

## Session 2 — Fill Core Wiki Pages（目標 8–10 頁）

**策略**：三層 Agent 派發，每個主題一個 researcher（Haiku）平行抽取 + implementer（Sonnet）整合寫入 + senior-architect（Opus）稽核。

**優先序（依諮詢頻率 × 差異化價值）**：

1. [[gcp-landing-zone]] — CathaySec 現役，與 iso27017-audit 強耦合
2. [[finops-savings-plans-roi]] + [[finops-cross-position-patterns]] — NT$400k + $270k USD 可信度最強
3. [[postgres-microsec-tuning]] — 整合 Medium #8
4. [[cdn-cache-tuning-97pct]] — 整合 Medium #6、#7（壹蘋 97% cache hit）
5. [[terraform-multi-cloud]] — Resolve AWS/GCP/Huawei 跨雲經驗
6. [[aws-step-functions-patterns]] — KKStream streaming 自動化
7. [[kafka-confluent-streaming]] — Resolve 即時資料串流
8. [[vmware-nsx-security-zone]] — HTC enterprise security
9. [[mysql-redis-cluster-ha]] — Gamania MMORPG 高可用
10. [[kernel-tuning-mmorpg]] — Gamania Linux 核心調校

**產出**：pages/ 從 2 擴到 12；每頁含 ≥ 5 筆 Concrete Numbers + ≥ 2 個 Anti-patterns。

**驗證 metric**：Lint pass rate — 所有 pages 符合 schema.md Quality Bars。

---

## Session 3 — Fill Secondary Pages + New Skills Gap Analysis

**Pages**（追加約 5–7 頁，依需要）：
- `stripe-serverless-fintech` — SPQ + Medium #9
- `aws-sa-pro-prep` — Medium #3、#4
- `consultant-client-enablement` — Resolve consulting track
- `sre-oncall-training-program` — KKStream
- `haproxy-patterns` — Gamania
- 8 個 `{company}-lessons.md` 頁（精簡版，每頁 ≤ 200 行）

**新 Skills（基於 wiki 實際內容決定，empirical）**：

初估缺口 2–3 個，候選：
- `db-zero-downtime`：從 wiki 抽取可重複 SOP（redis + pg）
- `iso27017-prep`：合規審計 checklist（基於 iso27017-audit page）
- `finops-roi-calculator`：Savings Plans 評估範本（基於 finops wiki pages）

**Kill criteria**：若現有 skill 已覆蓋 80%+，不新增。

**驗證 metric**：gap-analysis.md 列出每個候選 skill 的 「existing overlap %」。只接受 ≤ 30% 的新增。

---

## Session 4 — Autoresearch:wiki Subcommand + Hooks

**目標**：把 wiki ingest/query/lint 三個 ops 整合進 `.claude/skills/autoresearch/` 現有 framework。

**設計草稿**（細節留給 Session 4 實作）：

```
/autoresearch:wiki ingest
  — 從新 raw 素材（user 貼上經驗 / 新 blog post / incident postmortem）
    產出 / 更新 1–3 個 wiki pages
  — 每個 ingest 強制更新 INDEX.md 的 last-updated
  — Metric: pages updated × Quality Bar pass rate

/autoresearch:wiki query "<question>"
  — 模擬 senior-architect agent 的查詢邏輯
  — 回傳匹配 pages 清單 + 關鍵 sections
  — 用於驗證 agent 能否找到正確知識

/autoresearch:wiki lint
  — 掃描所有 pages + INDEX 做健康檢查
  — 產出 lint-report.md
  — Metric:
      lint_score = (pages_within_size_limit × 20)
                 + (pages_with_concrete_numbers × 20)
                 + (no_contradictions × 30)
                 + (no_stale_pages × 20)
                 + (no_orphans × 10)
      滿分 100；目標 ≥ 85
```

**配套 hooks**（`.claude/settings.json`）：
- `PostToolUse matcher=Edit|Write on research/career-wiki/pages/*` → auto-update INDEX last-updated
- Weekly（user 手動）：`/autoresearch:wiki lint` 做健康檢查

**驗證 metric**：ingest cycle 的 turnaround time（從 raw → wiki page reviewed < 10 min）。

---

## Success Criteria（整體）

完成所有 4 個 session 後：

| Metric | Target |
|--------|--------|
| Wiki pages 總數 | 12–18 |
| INDEX 覆蓋率 | 100%（每個職涯段都有對應 page 或 lessons）|
| Agent 查詢命中率 | ≥ 80%（用 10 個 sample 問題驗證）|
| Lint score | ≥ 85 |
| CLAUDE.md token 增量 | ≤ +300 tokens |
| 新 skill 數 | ≤ 3（empirical，基於 gap analysis）|
| 每頁 Concrete Numbers 數 | ≥ 5 筆 |
| 每頁 Anti-patterns 數 | ≥ 2 個 |

---

## Three-layer Dispatch Map

| Session | Haiku researcher | Sonnet implementer | Opus advisor |
|---------|-----------------|---------------------|---------------|
| 1 ✅ | 抽取 SoundOn + CathaySec SOP | 寫 2 pilot pages + agent | 策略顧問（本次 advisor 諮詢）|
| 2 | 平行抽取 8–10 主題 | 整合寫入 8–10 pages | 稽核完整性 + 矛盾檢測 |
| 3 | 補充 secondary + blog fetch | 寫次要 pages + gap-analysis | 決定新 skill 去留 |
| 4 | — | 實作 autoresearch:wiki | 審查 metric 設計 |

**關鍵規則**：每 session 結束前強制 `advisor()` 諮詢一次確認方向，不省略。
