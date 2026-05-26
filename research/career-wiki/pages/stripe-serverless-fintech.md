# Stripe + AWS Lambda — Serverless Fintech

> **Source positions**: SPQ Co-founder/CTO 2015–2017
> **Last ingested**: 2026-04-21
> **Confidence**: medium-high（Zeuik 實作 + Medium blog #9 背書）
> **Linted**: 2026-04-21

---

## Context

SPQ 創業期金融科技產品。Serverless（API Gateway + Lambda）對 fintech 的核心吸引力是**運維成本低 + 自動擴展**，但 **PCI-DSS 責任不會減少** — 必須把 scope 壓到最小（Stripe tokenization + Lambda 只處理 token）。整合 [Medium Blog #9](https://medium.com/@zeuik/how-to-build-aws-lambda-with-ruby-and-postgresql-4b6ee634bf04) Ruby Lambda + PostgreSQL 的部署經驗。

---

## Core Methodology

### Step 1 — API Gateway 授權閘道

- **What**: API Gateway + IAM resource policy 保護 Lambda endpoint；拒絕未授權請求
- **Why**: 第一線防守；減少 Lambda 層的 noise
- **Gotcha** [SPQ]: Ruby Lambda cold start ~3–5s（blog #9），首次驗簽延遲可感知

### Step 2 — Stripe Webhook 簽名驗證

- **What**: 收到 POST 後立即用 Stripe secret 驗 `Stripe-Signature` header（HMAC-SHA256）
- **Why**: 確保事件來自 Stripe，防止偽造支付事件
- **Gotcha**: 時鐘偏差可能導致驗簽失敗 → NTP sync 必須設定；容忍時窗不可過寬

### Step 3 — PCI-DSS Scope 最小化

- **What**: **絕不**在 Lambda / RDS 存原始卡片；Stripe 負責 tokenization，Lambda 只處理 token + metadata（customer_id / amount / currency）
- **Why**: 把 PCI-DSS 審計範圍壓到「AWS 基礎架構 100% + 應用層 0%」
- **Gotcha** [SPQ]: 創業期曾考慮 RDS 快取卡片資訊做「重複扣款優化」→ 立即放棄，PCI-DSS scope 爆炸不值

### Step 4 — Lambda Secrets + RDS Proxy

- **What**: Stripe secret / webhook secret 存 AWS Secrets Manager（不用明文 env var）；Lambda → RDS 走 RDS Proxy 做連線池
- **Why**: 防止 CI/CD log 洩漏 API key；Lambda cold start 時直連 RDS overhead 大
- **Gotcha** [blog #9]: Ruby 2.5 Lambda 打包 `pg` gem 需正確的 native extension build（deploy.sh 要對；container runtime 可簡化）

### Step 5 — CloudWatch 告警 + Webhook 重試

- **What**: Lambda error logs + Stripe 重試政策（36 小時內最多 5 次）+ webhook failure rate 監控
- **Why**: 支付不能漏；及早發現 Lambda 或下游故障
- **Gotcha**: Webhook timeout（29s）vs Lambda timeout（預設 3s，最大 15min）協調 — 設 Lambda timeout 60–300s 配 reconciliation flow

---

## Concrete Numbers

| 指標 | 值 | 備註 |
|------|----|------|
| Lambda cold start（Ruby + pg）| ~3–5s | Medium blog #9 實測 |
| Stripe webhook 重試次數 | 5 次 / 36 小時 | Stripe 官方 SLA |
| Lambda timeout（支付流程）| 60–300s | 容忍 reconciliation |
| PCI-DSS 審計週期 | 1 次 / 年 + pen test | 商業夥伴要求 |
| CloudWatch 事件成本 | ~$0.50 / 百萬 events | SPQ low volume |

> [需 Zeuik 確認] SPQ 實際月交易量 / cold start 對用戶感知的影響

---

## Anti-patterns

1. **明文環境變數存 API key**
   - 問題：CI/CD log 或 container image 洩漏
   - 解：**AWS Secrets Manager**（Lambda 動態拉取）

2. **跳過 Stripe webhook 簽名驗證**
   - 問題：偽造支付事件，財務漏洞
   - 解：所有 webhook endpoint 強制驗簽，驗失敗返 401

3. **Lambda 直連 RDS 無連線池**
   - 問題：Cold start 時 connection overhead 導致支付超時
   - 解：**RDS Proxy** 做連線池；Lambda 只管業務邏輯

4. **把卡片資訊存進 Lambda 日誌**
   - 問題：CloudWatch logs 變成 PII / PCI 敏感資料
   - 解：structured logging + allowlist（絕不 log raw payload）

---

## Decision Tree

```
何時用 Lambda + Stripe？
├─ payment volume < 100 / 日 + 容忍 cold start → ✅ Lambda 最適
├─ volume 100–1000 / 日 → Lambda with provisioned concurrency
├─ volume > 1000 / 日 + 需 sub-second 確認 → container（ECS / Fargate）
└─ 需複雜 reconciliation 流程 → Step Functions（見 [[aws-step-functions-patterns]]）

PCI-DSS scope 界線？
├─ 卡片 tokenization → Stripe（100% scope 轉移）
├─ Lambda 只處理 token + metadata → AWS Lambda in scope（base level）
├─ 從 RDS 讀卡號（反模式） → ❌ scope 爆炸
└─ Webhook signature 驗證 → 必做（防偽造）
```

---

## References

- 職涯段：`raw/career-summary.md#3-spq-副技術長`
- **Zeuik blog #9**（2022-09）：[How to build AWS Lambda with Ruby and PostgreSQL](https://medium.com/@zeuik/how-to-build-aws-lambda-with-ruby-and-postgresql-4b6ee634bf04)
- [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/)
- [AWS RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)
- [Stripe Webhooks: Check signatures](https://stripe.com/docs/webhooks/signatures)
- [AWS Lambda Quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)
- 關聯：[[aws-step-functions-patterns]]、[[postgres-microsec-tuning]]、[[spq-lessons]]
