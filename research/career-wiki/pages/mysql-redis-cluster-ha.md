# MySQL + Redis Cluster HA for MMORPG Game State

> **Source positions**: Gamania 2013–2016（天堂 M 遊戲狀態持久化）
> **Last ingested**: 2026-04-21
> **Confidence**: high（Zeuik 設計並運營 MHA + Redis Cluster）
> **Linted**: 2026-04-21

---

## Context

MMORPG（150+ racks、400+ VMs）MySQL 存帳號 / inventory / 金幣，Redis Cluster 快取玩家位置 / 技能冷卻。核心要求：**inventory 強一致性（不可丟）**、Redis failover < 5s。本頁記錄 5 步高可用方法論。

---

## Core Methodology

### Step 1 — MySQL Replication 架構

- **What**: Master–Slave async（主力）+ critical data（account / inventory）走 semi-sync
- **Why**: Async 吞吐高但 slave lag 可達秒級；Semi-sync 保證 single write 傳到 ≥ 1 replica
- **Gotcha** [Gamania]: 2014 某次 master crash 時 semi-sync 卡 timeout；嘗試 group replication 但舊版 bug 多 → **回到 semi-sync + ProxySQL failover**

### Step 2 — Failover Strategy（MHA + ProxySQL）

- **What**: MHA 偵測 master down → 自動提升 best slave；ProxySQL routing 切換
- **Why**: 遊戲不可停機；failover < 10s 才不影響玩家
- **Gotcha** [Gamania]: MHA 曾誤判 network partition 觸發**雙 master 衝突**；加 SANity check 確認 VIP 所有權

### Step 3 — Redis Cluster Topology

- **What**: 3 master + 3 replica（1:1 ratio）分佈在不同機架
- **Why**: 高並發讀（位置快取）需冗餘；cluster gossip protocol failover 快
- **Gotcha** [Gamania]: 初配 1 master + 2 replica → master down 後兩 replica 無法自動 promote；改 **3+3 或切 Sentinel**

### Step 4 — Client-side Sharding vs Proxy

- **What**: Game server 用 client-side sharding（一致性 hash）直連 cluster；API 層用 twemproxy 做 connection pooling
- **Why**: Client-side 減代理層延遲；twemproxy 穩定性驗證過
- **Gotcha** [Gamania]: Client-side hash key 分佈不均（玩家依角色分桶）→ 某 redis node CPU 飆；重 hash seed + 定期檢查 key distribution

### Step 5 — Cross-Replica Consistency

- **What**: Inventory write 用 MySQL semi-sync（等 replica ack）；位置快取 eventual consistency（Redis async）
- **Why**: 金幣 / 裝備丟失損營收；位置延遲 1s 可接受
- **Gotcha** [Gamania]: 同時寫 MySQL + Redis 但 Redis 先完成 → 玩家看到**幽靈物品**；加應用層 **distributed transaction ID 去重**

---

## Concrete Numbers

| 指標 | 值 | 場景 |
|------|----|------|
| MySQL replication lag（async）| 100–500ms | 正常負載；DDL 可達秒級 |
| MySQL failover time（MHA）| 5–8s | detect + promote + DNS TTL |
| Redis Cluster failover（gossip）| 300–800ms | 自動 failover |
| Split-brain detection window | 3–5s | VIP 移轉確認 |
| MySQL 並發連線（150+ racks）| 400–500 / master | proxy pool 各 20–50 |
| Redis cluster node count | 6（3M + 3R）| 50K+ 玩家位置快取 |

---

## Anti-patterns

1. **MySQL Master 無備份**
   - 問題：只做 async replication 無額外備份，硬碟故障資料部分損壞
   - 解：**日備份 + binlog 歸檔**；復原窗口從「無法復原」→ < 1 hr

2. **Redis Cluster 跨機房分佈不當**
   - 問題：3 master 都在 rack A，network partition 時失效
   - 解：3 master 分 **3 個不同機房**；cluster node timeout 調為 < partition detection time

---

## Decision Tree

```
MySQL Master 掉線，inventory 怎辦？
├─ Semi-sync 仍運作 → MHA 自動提升 best slave，RPO = 0
├─ Semi-sync 斷 → 檢查 network partition；可重連 or backup restore
└─ 多 master 活躍（split-brain）→ 手動判定主權、停另一個、單向複製追趕

Redis Cluster node 故障？
├─ Replica 故障 → cluster 自動調度，無玩家影響
└─ Master 故障 → 自動 failover replica→master（< 1s）

遊戲寫入選 sync or async？
├─ 金幣 / 裝備 → MySQL semi-sync（必 ack）
├─ 位置 / 技能冷卻 → Redis async（eventual consistency）
└─ 排行榜 / 聊天 → Kafka stream（at-least-once）
```

---

## References

- 職涯段：`raw/career-summary.md#1-gamania-遊戲橘子--system-engineer`
- [MySQL 5.7/8.0 Replication](https://dev.mysql.com/doc/refman/8.0/en/replication.html)
- [Redis Cluster Specification](https://redis.io/docs/reference/cluster-spec/)
- [MHA Manager docs](https://github.com/yoshinorim/mha4mysql-manager/wiki)
- 關聯：[[kernel-tuning-mmorpg]]、[[haproxy-patterns]]、[[redis-pg-zero-downtime]]、[[gamania-lessons]]
