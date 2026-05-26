# PostgreSQL 微秒級延遲調優

> **Source positions**: SoundOn 2022–2023（DB 效能 10x 提升）
> **Last ingested**: 2026-04-21
> **Confidence**: high（SoundOn 親自執行 + Medium blog #8 同步記錄）
> **Linted**: 2026-04-21

---

## Context

流媒體 / 廣告 / 遊戲 / 支付場景需要把 PostgreSQL 延遲壓到微秒級，SoundOn 於 2022–2023 達成 DB 10x 效能提升。此頁整合 SoundOn 實戰 + [Medium Blog #8](https://medium.com/@zeuik/how-to-optimize-postgresql-database-size-and-sql-query-7d1ec635c5ea) 的內容（著作權合規：paraphrase，非直接複製）。

---

## Core Methodology

### Step 1 — Query Plan Analysis

- **What**: `EXPLAIN (ANALYZE, BUFFERS)` + `pg_stat_statements` 找 hot path
- **Why**: 微秒環境必先確認瓶頸在 DB 還是 app 層；盲目 tuning DB 是最常見錯誤
- **Gotcha** [SoundOn]: 10–20 deploys/day 每次 deploy 後 query plan 可能改變（統計資訊陳舊）→ 自動觸發 `ANALYZE` 或在 deploy pipeline 加 post-deploy health check

### Step 2 — Index Strategy

- **What**: BTree（default）vs BRIN（時序 / log 省 90% 空間）vs GIN（全文 / jsonb），partial / expression index
- **Why**: 微秒場景每 μs 都算；wrong index 導致 seq scan 延遲爆升
- **Gotcha** [Blog #8]: Expression index（如 `CREATE INDEX ON tbl ((lower(email)))`）適合微秒 lookup，但 maintenance cost 高；複合索引**不超過 3 欄**（否則維護與寫放大失衡）

### Step 3 — Autovacuum + Bloat 治理

- **What**: 監控 `pg_stat_user_tables.dead_tuples`，調 `autovacuum_vacuum_cost_limit`（500→1000–5000）、`autovacuum_scale_factor`（0.2→0.02–0.03）
- **Why**: Bloat 導致 cache miss（表掃 > shared_buffers），微秒級不容許；但過度 VACUUM 會 lock 表
- **Gotcha** [SoundOn]: 高寫量下 autovacuum 跟不上，`dead_tuples > 百萬`；改 AGGRESSIVE 模式 + 拉高 `cost_limit`。**關掉 autovacuum 是最壞選擇**

### Step 4 — Connection Pool（PgBouncer）

- **What**: PgBouncer transaction / statement pool mode；`pool_size = (cores × 2) + max(readers)`
- **Why**: 微秒環境每個 socket 建立都是延遲來源；transaction mode 複用連線
- **Gotcha** [SoundOn]: transaction mode **破壞 prepared statement**；需確保 transaction 夠小；statement mode 最激進但限制最多

### Step 5 — OS / Kernel Tuning

- **What**: `shared_buffers = RAM × 25%`、`huge_pages = try` + `vm.nr_hugepages = total_memory / 2MB`、I/O scheduler = noop/kyber、NUMA 感知
- **Why**: 微秒延遲競爭 L3 cache 和 page fault；kernel 時片可能超過查詢時間
- **Gotcha**: 沒設 huge_pages 時大 shared_buffers 反而慢（TLB miss 多）；NUMA 跨節點存取延遲可差 2–3x

### Step 6 — Application Side

- **What**: 強制 prepared statement、batch insert/update、read replica routing
- **Why**: 每個 network round-trip 都不能浪費；batch 把 N 次打成 1 次
- **Gotcha** [SoundOn]: 原本未用 prepared statement，改善後查詢延遲 -30–40%；與 index 優化合作效益最大化

---

## Concrete Numbers

| 指標 | 典型值 | SoundOn 場景 | 來源 |
|------|-------|-------------|------|
| shared_buffers | RAM 的 25% | 128GB → 32GB | PG docs |
| work_mem（微秒場景）| 256–512 MB | 排序 / hash join 不能 spill | SoundOn |
| PgBouncer pool_size | (cores × 2) + readers | 16 cores + 50 readers → 82 conn | [Blog #8 推測] |
| `autovacuum_vacuum_scale_factor` | 0.05（5%）→ 0.02–0.03 | 高寫量微調 | SoundOn |
| `autovacuum_max_workers` | 預設 3 → 6–8 | 微秒環境 | SoundOn |
| p99 latency 目標 | **< 100–500 μs** | microsec SLA | SoundOn |
| Index bloat threshold | < 10%，> 30% 觸發 REINDEX | 經驗值 | |
| DB 層效能貢獻 | **~10x total**（SoundOn）| 含 index + vacuum + pool | career-summary |

> [需 Zeuik 確認] Blog #8 實際 `shared_buffers` / `work_mem` 建議值；SoundOn 實際 PgBouncer pool_size；autovacuum 實際 `cost_limit`

---

## Anti-patterns

1. **`OFFSET + LIMIT` pagination（大 offset）**
   - 問題：`SELECT * FROM t OFFSET 1000000 LIMIT 10` 掃 100 萬丟 → CPU 爆
   - 解：keyset pagination `WHERE id > last_id LIMIT 10` 或 BRIN on timestamp

2. **過度 INDEX（寫放大）**
   - 問題：15 個 index on 同表 → 每 insert 維護 15 個 B-tree，延遲 +50–100%
   - 解：複合 `(user_id, created_at)` + partial `WHERE status='active'`

3. **Autovacuum 關掉或極度保守**
   - 問題：「vacuum 太慢關掉」3 個月後 bloat 200%，表掃時間 +10x
   - 解：改參數（`cost_limit` 上調）而非關掉

4. **`SELECT *` in hot path**
   - 問題：微秒場景抓多餘欄位 = 浪費 network bandwidth + cache pollution
   - 解：只抓需要欄位；涉及 jsonb 時用 `->` 提取特定 key

---

## Decision Tree

```
PostgreSQL 延遲超過目標？
├─ 先確認不是 network RTT / app 層 GC
│  └─ EXPLAIN + pg_stat_statements：90% 查詢在哪？
├─ 查詢本身快但 bloat 大 → Step 3（Autovacuum）優先
├─ 讀多、查詢計畫差 → Step 1 + Step 2
├─ 寫多、connection pool 飽和 → Step 4 + batch insert
├─ Page fault 多 → Step 5（huge_pages + NUMA）
└─ 還沒達微秒 SLA → Step 6（prepared statement + read replica）

讀寫分離策略？
├─ 讀多寫少（90/10）→ read replica + PgBouncer routing
├─ 寫多 → partition（time-series）+ batch insert
└─ 混合 → logical replication 分流特定 tenant
```

---

## References

- 職涯段：`raw/career-summary.md#5-goodnight--soundon--sre--architect`
- **Zeuik blog #8**（2022-09）：[How to optimize PostgreSQL Database Size and SQL Query](https://medium.com/@zeuik/how-to-optimize-postgresql-database-size-and-sql-query-7d1ec635c5ea)
- [PostgreSQL: EXPLAIN](https://www.postgresql.org/docs/current/sql-explain.html)
- [PostgreSQL: pg_stat_statements](https://www.postgresql.org/docs/current/pgstatstatements.html)
- [PostgreSQL: VACUUM](https://www.postgresql.org/docs/current/sql-vacuum.html)
- [PgBouncer Manual](https://www.pgbouncer.org/)
- 關聯：[[redis-pg-zero-downtime]]、[[finops-cross-position-patterns]]（Session 3）
