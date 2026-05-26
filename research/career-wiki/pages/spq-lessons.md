# SPQ — Lessons Learned（Co-founder / CTO）

> **Tenure**: Sep 2018 – Dec 2018（4 months）| **Role**: Co-founder + CTO（startup）
> **Last ingested**: 2026-04-21 | **Updated**: 2026-05-08 (confirmed dates + outcome)
> **Confidence**: high
> **Note**: Zeuik 主動離開轉往 KKStream；SPQ 於其離開後繼續進行（user confirmed）

---

## Context

金融科技創業；AWS Serverless（API Gateway + Lambda）+ Stripe payment gateway + mobile app + UI/UX。技術選型的決策必須同時考慮 fundraising、PCI-DSS、cash flow。

## Key Lessons

1. **PCI-DSS scope minimization 是架構核心決策**
   - Stripe tokenization 把 PCI scope 轉給 Stripe；自己只處理 token
   - 多付 Stripe 手續費 vs 自己過 PCI audit 幾乎都是前者划算
   - 見 [[stripe-serverless-fintech]]

2. **Serverless cold start 在 fintech 是 UX 問題**
   - Ruby Lambda cold start 3–5s；用戶支付時「轉圈圈」感受不好
   - 解：Provisioned Concurrency（有成本）或改 ECS/Fargate（運維成本）
   - 見 Medium blog #9

3. **創業 CTO 的技術決策要優先考慮 due diligence**
   - 投資人會問「你們 PCI 怎麼處理？」— Stripe 有現成答案
   - 選擇「好解釋的方案」比「技術最優方案」更重要（創業期）

4. **AWS Secrets Manager 從 day 1 就用**
   - 環境變數存 API key 是第一個會被安全審查員 flag 的問題
   - Secrets Manager 成本低、但結構清晰

5. **Product + UI/UX collaboration 改變了我對 infra 的認知**
   - Backend 工程師常忽略的「下單流程流暢度」其實是架構決策
   - 單一 Lambda timeout 設定可能破壞整個 funnel

6. **4 個月創業 CTO 的轉身時機：主動離開 vs 項目結束**
   - SPQ 在 Zeuik 離開後繼續進行（不是倒閉）；Zeuik 主動轉往 KKStream 尋求規模化 SRE 經驗
   - **創業 CTO 的 honest assessment**：4 個月的 Co-founder 經驗讓技術選型決策能力大幅提升（要對融資方解釋你的架構）；但也發現個人想深耕大規模 infra 工程，而非早期 startup 全棧推動
   - 保持好聚好散：離開時的完整技術文件交接讓 SPQ 能繼續

## What I'd Do Differently

- **不** 考慮 RDS 快取卡片資訊做「重複扣款優化」（PCI scope 爆）
- Webhook signature 驗證從 day 1 強制（不要等測試環境漏再補）
- 選 container 而非 Lambda for payment hot path（cold start 問題）

## Cross-references

- 核心 pages：[[stripe-serverless-fintech]]
- 延伸：[[postgres-microsec-tuning]]（Lambda + pg 連線）、[[aws-step-functions-patterns]]（reconciliation flow）

## References

- `raw/career-summary.md#3-spq-副技術長`
- Medium blog #9（2022-09）：AWS Lambda + Ruby + PostgreSQL
