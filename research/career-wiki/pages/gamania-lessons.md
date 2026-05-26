# Gamania 遊戲橘子 — Lessons Learned

> **Tenure**: Aug 2015 – Feb 2018 | **Role**: System Engineer（天堂 M）
> **Last ingested**: 2026-04-21 | **Updated**: 2026-05-08 (confirmed dates + details)
> **Confidence**: high

---

## Context

MMORPG infrastructure；~150 server racks（HP/DELL）、近 500 VMs、50K+ 並發、Linux kernel tuning + HAProxy（TCP + HTTP 雙用途）+ MySQL/Redis Cluster + Cacti/Grafana + Kafka + Hadoop（遊戲行為 + 營運數據雙用途）+ Telegram alerts + **早期 AWS PoC（CloudFront + HiNet CDN）**。

## Key Lessons

1. **極限規模下 kernel default 是瓶頸**
   - `somaxconn=128` 對 50K+ 連接就是錯
   - `fs.file-max` 須拉到 2M 以上才夠 150 racks
   - 見 [[kernel-tuning-mmorpg]]

2. **Health check 設計比配置更重要**
   - 2s interval + 1 fail 判定 → 網路抖動就大量 server 上下線
   - 5s + 連續 3 fail 是實戰下的平衡
   - 見 [[haproxy-patterns]]

3. **Semi-sync + MHA 比 Group Replication 可靠（2014 時期）**
   - 新功能 bug 多；老牌穩定技術在生產更值得用
   - 見 [[mysql-redis-cluster-ha]]

4. **Redis Cluster 跨機房佈局是 partition tolerance 的保險**
   - 3 master 都在 rack A → partition 時全掛
   - 3 master 分 3 機房 = 標配

5. **Cacti + Grafana 監控覆蓋 > 單一工具**
   - 指標粒度 / alerting 靈活度不同；混搭比被迫選一個好
   - 早期的 Cacti 歷史圖表在 root cause 分析時救命多次

6. **AWS CloudFront + HiNet CDN PoC 的決策**
   - 跨 CDN 分流 = region-specific 流量優化
   - 早期雲端 PoC 是後續職涯轉向 cloud-native 的 foundation

7. **HAProxy 在 MMORPG 的雙用途：TCP + HTTP**
   - TCP level：遊戲客戶端 → game server 分流（連線保持、封包轉送）
   - Layer 7 HTTP：管理工具 / web API 負載均衡
   - Software LB 取代硬體 LB → 硬體成本下降；但 TCP keepalive 設定要獨立調，HTTP 預設值會造成遊戲連線中斷

8. **Kafka + Hadoop：遊戲行為 + 營運數據雙管道**
   - Kafka 接收遊戲即時事件流（登入、打怪、交易等行為）+ 每日結算 KPI 數據
   - Hadoop 做批次分析：營運報表 + 玩家行為挖掘（培育率、掉線熱點）
   - **Gotcha**：遊戲事件量級在推廣活動時暴衝 5–10x；Kafka partition 數要提前規劃，臨時 rebalance 延遲高

9. **硬體驅動缺失是 IDC 建置最容易忽略的風險**
   - 新型號伺服器採購後發現無對應 Linux kernel driver → 無法安裝作業系統
   - 解法：採購前先在 staging 機器跑 `lshw` / `dmesg` 驗證驅動支援；或鎖定 HCL（Hardware Compatibility List）清單

10. **NUMA 架構對高並發遊戲服務的影響**
    - 多 socket 伺服器（NUMA node 跨節點 memory access）在高並發下延遲飆升
    - `numactl --interleave=all` 對部分場景有效；更好解：按 NUMA node 綁定 game server instance
    - 問題特徵：單機 CPU 使用率 50–60% 但 latency 很高 → 優先懷疑 NUMA

11. **流量風暴 / 硬體故障 / IDC 事件同時踩過**
    - 登入風暴（推廣/節日）：排隊機制 + 限流比擴充 server 更快見效
    - RAID 崩潰 / 記憶體發熱：Cacti 歷史圖表是 root cause 的第一線索
    - IDC 網路分區：MySQL Semi-sync 延遲累積 → 切換 MHA failover；跨機房 3 master 佈局是救命的

## What I'd Do Differently

- Kernel tuning **迭代式**（每次 1–2 參數 + 1 週監控），不做「全局大調」
- iSCSI crash dump target **絕不用 network**（改本機 SSD）
- ESXi upgrade 前先確認 guest kernel 的 I/O scheduler 相容性

## Cross-references

- 核心 pages：[[kernel-tuning-mmorpg]]、[[haproxy-patterns]]、[[mysql-redis-cluster-ha]]
- 原始素材：`raw/artifacts/gamania-research-raw.md`（完整 3 主題摘要）

## References

- `raw/career-summary.md#1-gamania-遊戲橘子--system-engineer`
