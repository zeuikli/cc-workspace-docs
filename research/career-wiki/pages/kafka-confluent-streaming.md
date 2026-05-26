# Kafka / Confluent Streaming（Consulting 場景）

> **Source positions**: Resolve Technology 2021–2022（GitLab CI + Kafka + Confluent real-time streaming）
> **Last ingested**: 2026-04-21
> **Confidence**: high（Zeuik 為多客戶實施 Confluent + Debezium CDC）
> **Linted**: 2026-04-21

---

## Context

event-driven 架構 / log aggregation / 跨服務 fan-out 的首選。Resolve 的 consulting 場景讓 Zeuik 看到「新客戶最常犯的錯誤」— 本頁整合客戶 onboarding 時的共通陷阱。

---

## Core Methodology

### Step 1 — Topic Design

- **What**: Partition 數、replication factor、retention
- **Why**: 直接決定吞吐量上限、failure domain、成本
- **Gotcha** [Resolve consulting]: 客戶常誤以為「partition = 並行度」，沒考慮 controller 壓力 / metadata 同步；建議 **partition = 預期 consumer 數 × 1.5 上限**

### Step 2 — Schema Registry + Evolution

- **What**: Avro / Protobuf 版本化透過 Confluent Schema Registry（或 Karapace OSS）
- **Why**: Kafka payload 無 schema；consumer 解析失敗 = 整條 chain 掛；Avro 壓縮比 ~1/4 vs JSON（對頻寬敏感場景重要）
- **Gotcha** [Resolve consulting]: 新客戶常跳過 schema registry 直用 JSON string → 不到 3 個月出現「consumer 無法解析新欄位」緊急 incident

### Step 3 — Producer Idempotency + Transactions

- **What**: `acks=all` + `enable.idempotence=true` + 事務邏輯
- **Why**: 防止 partition rebalance / broker 故障時重複發送或丟失
- **Gotcha**: exactly-once 保證**需要 consumer 側支援事務**（Kafka Streams / Confluent 內置）；純 producer 的 exactly-once 只到 broker 邊界

### Step 4 — Consumer Group + Offset Management

- **What**: Consumer group 自動分 partition、offset 儲 `__consumer_offsets` topic、rebalance 策略
- **Why**: Partition lag 監控 = 系統健康度；rebalance 造成 stop-the-world
- **Gotcha** [Resolve]: 大型 group（50+ 成員）rebalance 耗 30s~2min，客戶未預期 → 應在 alert 上標「rebalance 中斷服務」；`__consumer_offsets` replication factor 預設 3 **勿改**

### Step 5 — Kafka Connect / Streams

- **What**: Debezium（MySQL/PostgreSQL CDC）、S3 sink（batch archive）、ksqlDB（stream processing）
- **Why**: 無需寫 consumer code，快速對接資料湖
- **Gotcha** [Resolve]: Debezium CDC 初始 snapshot **會鎖表**（> 10GB 大表風險高）→ 遷移常卡在 snapshot 階段

---

## Concrete Numbers

| 指標 | 典型值 | Resolve 客戶案例 |
|------|-------|----------------|
| Partition 數（公式）| consumer × 1.5 | 50 consumer → 75 partition |
| Replication factor | 3（HA）| production 不可低於 3 |
| ISR 最低 | ≥ 2 | `min.insync.replicas` |
| Retention（log）| 7 天 | 客戶 compliance 90 天 → cost +30% |
| Consumer lag tolerance | < 1 min（real-time）| 金融 < 5s；流媒體 5 min |
| Confluent Cloud 成本 | $0.5/GB ingress | 100GB/day ≈ $450/月 |
| Avro 壓縮比（vs JSON）| ~1/4 | 100MB/day → 25MB/day |
| Debezium snapshot（MySQL 5GB）| 30–90 min | 鎖表；避峰時段 |

> [需 Zeuik 確認] Confluent Cloud 2026 精確定價、Resolve 客戶具體規模、Debezium CDC lag 實際數值

---

## Anti-patterns

1. **Partition 數決策誤區**
   - 問題：「scaling 就設 100+ partition」→ controller overhead、metadata replication lag、heartbeat timeout
   - 解：按 consumer 數基線算；監控 controller lag

2. **跳過 Schema Registry**
   - 問題：JSON raw string → 新欄位 parse error → consumer chain 崩
   - 解：Schema Registry（Confluent）或 Karapace（OSS）強制版本化；推 Avro

3. **Partition 太多 → ISR 崩潰**
   - 問題：leader 複寫到所有 replicas，partition 太多 → bandwidth 飽和 → ISR 縮 → block producer
   - 解：監控 `UnderReplicatedPartitions`；replication factor 降 2 是應急非永久

4. **用 Kafka 當 database**
   - 問題：retention 有期限（7–30 天），topic 刪不可逆，無 query language
   - 解：適合 event streaming / sourcing；長期存檔用 S3 + Parquet（Confluent S3 connector）

5. **Consumer rebalance 無 service 中斷處理**
   - 問題：rebalance 期間 consumer 無法消費 → lag 爆 → 下游 timeout
   - 解：app layer 加 circuit breaker（lag > X fallback）；監控 rebalance duration 納入 SLA

---

## Decision Tree

```
需要 event streaming？
├─ 微服務異步通信 → Kafka
├─ 資料湖 + 批次 → Kafka + Confluent S3 sink
├─ DB 變更實時同步 → Debezium CDC on Kafka
└─ 單向 pub/sub（< 100 events/sec）→ Redis pub/sub 夠

Self-managed vs Confluent Cloud？
├─ < 10GB/day → AWS MSK / Confluent Cloud（省運維）
├─ 10–100GB/day → Self-managed on K8s
├─ > 100GB/day → Self-managed + Confluent Platform（多機房）
└─ Compliance（金融 on-prem）→ Self-managed data residency

Schema 格式？
├─ 吞吐敏感（IoT / log）→ Avro（最小最快）
├─ gRPC 生態 → Protobuf
├─ 臨時驗證 → JSON（無 registry）
└─ 複雜嵌套 + 版本化 → Avro 或 Protobuf

Consumer lag 處理？
├─ < 1 min → auto-scale consumer（K8s HPA / ECS）
├─ 1–5 min → app layer circuit breaker
├─ > 5 min → trigger incident, page oncall
└─ 追不上 → increase partition 或 producer rate limit
```

---

## References

- 職涯段：`raw/career-summary.md#7-resolve-technology--senior-devops--consultant-dual-role`
- [Apache Kafka Design](https://kafka.apache.org/documentation/#design)
- [Confluent Platform Architecture](https://docs.confluent.io/platform/current/architecture.html)
- [Debezium MySQL Connector](https://debezium.io/documentation/reference/stable/connectors/mysql.html)
- [Confluent Cloud Pricing](https://www.confluent.io/confluent-cloud/)
- 關聯：[[aws-step-functions-patterns]]、[[consultant-client-enablement]]（Session 3）
