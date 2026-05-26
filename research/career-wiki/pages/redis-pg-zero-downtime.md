# Redis + PostgreSQL Zero-Downtime Upgrade

> **Source positions**: SoundOn / Goodnight 2022–2023
> **Last ingested**: 2026-04-21 | **Updated**: 2026-05-08 (PDF v2024.2 + user confirmed)
> **Confidence**: high（Zeuik 親自主導多次升級）
> **Linted**: 2026-04-21

---

## Context

SoundOn 流媒體環境：microsecond 級延遲、10–20 deploys/day、CDN migration $60k/yr FinOps。在這種**高變更率 + 高延遲敏感度**環境下，PostgreSQL 與 Redis 的版本升級不能接受任何停機窗口。這頁記錄了真實執行過的零停機升級方法論。

---

## Core Methodology

### Step 1 — 預升級狀態檢查與容量規劃

- **What**: 量測 baseline：replication lag、failover time、ops/sec、memory util、storage I/O。
- **Why**: 零停機升級會經歷短暫的版本不相容期；沒有 baseline 就無法判斷 lag spike 是升級副作用還是業務正常波動。流媒體環境 lag > 100ms 就破 SLA。
- **Gotcha** [SoundOn]: 10–20 deploys/day 下，升級窗口會被新部署搶占。**必須**預留 30 分鐘穩定期，且在 CI/CD 加 lock flag 禁止同時部署。

### Step 2 — PostgreSQL Logical Replication（pglogical / 官方 logical replication）

- **What**: 在舊 PG cluster 旁邊起新 PG cluster（新版本），用 pglogical 單向複寫所有表。
- **Why**: pglogical 是邏輯層複寫（不依 WAL 位置），允許跨小版本/中版本升級。MVCC 隔離讓讀寫不中斷。
- **Gotcha** [SoundOn]:
  - `max_replication_slots` + `wal_keep_segments` 要調高，否則複寫 slot lag 時 WAL 被 cleanup → 要重做 initial sync
  - Initial sync 速度 < 新寫入速度時 lag 會愈來愈大；調整 `max_parallel_apply_workers` 或改用 partition-wise replication
  - **pglogical 在 PG 14+ 官方不再維護**，建議改用 PG 官方 `CREATE PUBLICATION / SUBSCRIPTION`

### Step 3 — Redis 連線層雙寫（Application-level dual-write）

- **What**: 應用層改寫為「同時寫舊 Redis + 新 Redis」，讀流量 try-new-first、fallback 舊 cluster。
- **Why**: Redis 沒有內建 zero-downtime 升級（不像 PG 有邏輯複寫）；必須由應用層介入。雙寫確保新 cluster 趕上狀態；讀 fallback 保證升級期間 cache miss 不會直打 DB。
- **Gotcha** [SoundOn]:
  - Microsecond 場景：雙寫延遲會加倍（兩個 socket），必須改為**批量寫 + pipelining**
  - AOF rewrite 時 I/O 飆高會卡住複寫同步；調小 `auto-aof-rewrite-percentage` 或暫時只用 RDB
  - 跨機房時雙寫會累積 RTT，考慮用 `MSET` 打包或 Lua script 原子化

### Step 4 — 讀流量漸進式切換

- **What**: LB 權重或 feature flag，按 5% → 10% → 50% → 100% 逐步切換讀流量到新 cluster。
- **Why**: 發現新 cluster bug 時可秒級 rollback；同時驗證新 cluster 撐得住**實際流量**（壓測與真實有差）。
- **Gotcha** [SoundOn]:
  - 10–20 deploys/day 下切換期碰巧 deploy，會造成混亂 → lock 部署窗口或在部署 pipeline 加 pre-check
  - Redis 缺一致性保證，讀可能看到舊資料 → 業務層要能容忍**短暫不一致**；不能的（如 session）留最後切換

### Step 5 — 寫流量切換 + 舊資源下線

- **What**: 切換所有寫流量到新 cluster，等 PG 複寫 lag = 0（雙寫 queue 清空）後下線舊資源。
- **Why**: 最後一步保證新系統接收所有寫；lag = 0 表示舊 cluster 完全同步。
- **Gotcha**: 切換瞬間會有短暫 socket 重設 → 應用層要有 connection pool 熱備 + 自動重試機制（`pgbouncer` / `redis-cluster-proxy`）。

---

## Concrete Numbers

| 指標 | 典型值 | SoundOn 場景 | 關鍵性 |
|------|-------|-------------|--------|
| PG replication lag（初始）| < 100ms | microsec 要求故極低 | 🔴 高 |
| PG logical replication 吞吐 | 5k–50k rows/sec | 高寫量流媒體環境 | 🔴 高 |
| Redis MIGRATE 耗時 / million keys | 1–5 分鐘 | 依 RTT + key size | 🟡 中 |
| 雙寫延遲增幅 | +2–5ms（批量+pipelining） | microsec 場景**必須**最佳化 | 🔴 高 |
| 讀流量切換步長 | 5–10% / 5 min | 穩定性監測 + 快速 rollback | 🟡 中 |
| 連線切換時超時率 | < 0.01% | 10–20 deploys/day 高並發 | 🔴 高 |
| RPO（恢復點目標）| 0 sec | zero-downtime 承諾 | 🔴 高 |
| RTO（恢復時間目標）| < 30 sec | 應用層 failover | 🟡 中 |

> [需 Zeuik 確認] Redis MIGRATE batch size 實際值、pglogical 時期的 `max_replication_slots` 設定、AOF rewrite 頻率。

---

## Anti-patterns（不要做）

1. **用 `pg_upgrade` in-place**
   - 問題：需停寫，違反零停機承諾；全表 ANALYZE 時間比想像長
   - 何時踩：誤以為「pg_upgrade 速度快就夠」— 速度不是唯一指標，業務中斷與否才是

2. **Redis MIGRATE 不分批**
   - 問題：一次遷移百萬 key 阻塞 Redis 單執行緒，造成 < 100ms 服務中斷（microsec 場景等於 SLA 破）
   - 解：用 `MIGRATE ... KEYS key1 key2 ...` 分批，每批 100–500 keys，間隔 50ms

3. **pglogical 初始複寫不監控**
   - 問題：複寫 lag 超過應用層超時設定，業務看到「新 DB 連線超時」，實際是複寫還沒追上
   - 解：監控 `pg_stat_subscription.latest_end_time`，lag > 5s 即告警

---

## Decision Tree

```
升級 PostgreSQL？
├─ 小版本（13.0 → 13.5）
│  └─ PG 官方 logical replication + readonly standby 輪動
├─ 中版本（12 → 13）
│  ├─ 寫流量 < 1k ops/sec → pglogical 單向複寫
│  └─ 寫流量 > 1k ops/sec（SoundOn 場景）
│     └─ pglogical + 應用層雙寫 + 完整監控
└─ 大版本（11 → 14+）
   └─ 必須用 PG 官方 logical replication（pglogical 停維）

升級 Redis？
├─ 小版本（6.0 → 6.2）
│  └─ 原地升級 + AOF rewrite 分散到離峰時段
├─ 中版本（5 → 6）或 protocol 變更
│  ├─ 單機 / Sentinel
│  │  └─ Redis MIGRATE（分批）+ twemproxy 代理雙寫
│  ├─ Redis Cluster
│  │  └─ 漸進式 node 升級 + read replica fallback
│  └─ microsec 環境（SoundOn）
│     └─ 應用層雙寫 + pipelining + 讀流量漸進切換
└─ 以上都不行？
   └─ 接受 <5min 停機 + blue-green deployment
```

---

## Related Approach: AWS RDS 跍長備機（SoundOn PG 9→14 實際採用）

**SoundOn 的 PG 9→14 零停機升級實際採用 RDS 跍長備機方式**（user confirmed）：
1. 建立新 RDS PG 14 instance
2. 同步期間保持舊 instance 持續服務（讀寫不中斷）
3. 同步完成後切換 DNS/endpoint → 近零停機切換
4. 舊 instance 留觀察期後下線

**與 Blog #10 的差異**：Zeuik 於 2022-08 的 Medium 文章（[How to upgrade AWS PostgreSQL with minimum downtime](https://medium.com/@zeuik/how-to-upgrade-aws-postgresql-version-with-minimum-downtime-1107b3aab901)）記錄的是 RDS replica-promote + in-place major upgrade，實際 downtime ~4 小時（含 AWS 自動備份），適合可接受 maintenance window 的場景。SoundOn 的 production 升級則採跍長備機策略達到真零停機。

**判斷原則**：
- 有 maintenance window（weekend / 夜間離峰）→ RDS in-place major upgrade，簡單低風險
- RDS Managed + 零停機需求 → 跍長備機 + DNS cutover（SoundOn 做法）
- self-managed PG + 超高寫量 → pglogical + dual-write（本頁主要方法論）

## References

- 職涯段：`raw/career-summary.md#5-goodnight--soundon--sre--architect`
- Zeuik blog #10（2022-08）：[How to upgrade AWS PostgreSQL version with minimum downtime](https://medium.com/@zeuik/how-to-upgrade-aws-postgresql-version-with-minimum-downtime-1107b3aab901)
- [PostgreSQL Logical Replication](https://www.postgresql.org/docs/current/logical-replication.html)
- [pg_upgrade](https://www.postgresql.org/docs/current/pgupgrade.html)
- [pglogical repo (2ndQuadrant, maintenance ended)](https://github.com/2ndquadrant-it/pglogical)
- [Redis Replication](https://redis.io/docs/manual/replication/)
- [Redis Cluster Resharding](https://redis.io/docs/management/scaling/)
- 關聯：[[postgres-microsec-tuning]]（待建立）、[[mysql-redis-cluster-ha]]（待建立）
