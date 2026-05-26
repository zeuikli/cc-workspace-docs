# SoundOn / Goodnight — Lessons Learned

> **Tenure**: 2022–2023 | **Role**: SRE + Architect
> **Last ingested**: 2026-04-21 | **Updated**: 2026-05-08 (PDF v2024.2) | **Confidence**: high

---

## Context

流媒體服務；4x API 效能（Beanstalk + CI/CD revamp）、10x DB query 速度、microsecond latency、DB size ↓3x（index cleanup）、**CDN migration $60k USD/yr 節省**（Cloudfront→Cloudflare）、零停機 PG 9→14 / Redis 2.8→5.0.6 升級、80% 告警減少（PDF v2024.2 confirmed）。

## Key Lessons

1. **微秒 SLA 會放大所有小問題**
   - Prepared statement 沒用 → -30–40% latency；autovacuum 太保守 → dead_tuples 百萬
   - 平常不重要的細節在微秒場景都爆
   - 見 [[postgres-microsec-tuning]]

2. **高頻部署 + 零停機升級 = 互相放大的挑戰**
   - 10–20 deploys/日時做 DB 升級需鎖部署窗口
   - CI/CD 要有 feature flag 機制允許 incremental rollout
   - 見 [[redis-pg-zero-downtime]]

3. **Connection pool 是微秒場景的第一瓶頸**
   - 不是 DB 慢，是 connection overhead 本身 > query time
   - PgBouncer transaction mode 是 default；但要小心 prepared statement 相容性

4. **SoundOn FinOps 雙管齊下：CDN 替換 + Right-sizing**
   - **CDN migration**：$60k/yr，Cloudfront → Cloudflare（PDF v2024.2 documented）
   - **Beanstalk right-sizing**：multi-instance type + Spot instance 混搭，降低 compute 成本（Spot 適合 stateless web tier）
   - **RDS 降規**：DB query 優化後（10x speed），原本的高規格 RDS 成為 over-provisioned → 降規節省費用（但需確認 IOPS 不是瓶頸，見 Lesson #5 IOPS gotcha）
   - 不靠 RI/SP — 那是 KKStream 的做法（見 [[finops-savings-plans-roi]]）

5. **Autovacuum 關掉是最壞決策**
   - 「vacuum 太慢」是 tuning 問題；關掉 3 個月後 bloat 200%，表掃時間 +10x
   - 改參數（`cost_limit`）而非關功能

5. **RDS 降規的 IOPS 陷阱**
   - DB query 優化後 CPU 降低 → 判斷可降規 RDS → 但 DB 瓶頸已轉移到 I/O，降規 CPU 不解決 IOPS 限額問題
   - 降規前必查：Provisioned IOPS vs actual IOPS usage（CloudWatch `ReadIOPS` / `WriteIOPS`）
   - Spot instance 適合 Beanstalk web tier（stateless），**不適合**有 local state 的服務

6. **告警降低 80% 來自程式碼層面合作**
   - 純 infra 調整不夠——SoundOn 的告警根本原因是 application logic + DB query 設計問題
   - 跟後端開發團隊 co-own 告警指標，讓 RD 直接看到告警影響，才有改程式的動力
   - 見 [[postgres-microsec-tuning]]（DB 層面），但 application-level 才是決定性因素

## What I'd Do Differently

- DB 升級必 lock 部署窗口 **30min 穩定期**（不是 5min）
- PgBouncer pool_size 從 `(cores × 2) + max(readers)` 起步，不用業界死板公式
- Autovacuum 的 aggressive 設定從 day 1 就要，不要等到 bloat 出事

## Cross-references

- 核心 pages：[[redis-pg-zero-downtime]]、[[postgres-microsec-tuning]]
- 延伸：[[finops-cross-position-patterns]]（待建立）、[[finops-savings-plans-roi]]

## References

- `raw/career-summary.md#5-goodnight--soundon--sre--architect`
- Medium blog #10（2022-08）：AWS PostgreSQL min-downtime 升級
- Medium blog #8（2022-09）：PostgreSQL 優化
