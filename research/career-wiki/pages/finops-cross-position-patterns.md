# FinOps 跨職涯共通模式

> **Source positions**: KKStream 2019–2021、SoundOn/Goodnight 2022–2023、CathaySec 2024–now
> **Last ingested**: 2026-04-21 | **Updated**: 2026-05-08 (SoundOn FinOps corrected from PDF v2024.2)
> **Confidence**: medium（跨 3 段職涯 synthesis；部分細節推論，具體參數見各段 lessons）
> **Linted**: 2026-04-21

---

## Context

三段職涯累積 FinOps 節省：KKStream $150k USD/年 + SoundOn $60k USD/年（CDN migration，PDF v2024.2 confirmed）+ CathaySec NT$400k/年（約 $12k USD）。雖然雲端平台不同（AWS vs AWS vs GCP）、產業不同（影音串流 vs 聲音媒體 vs 金融），但每次成功節省都依賴同一組核心動作。這頁 synthesize 跨職涯的**可重複方法論**，而非個別平台技巧。

---

## Core Methodology

### Step 1 — 資產盤點與標籤化（Tag Everything）

- **What**: 列出所有 cloud 資源（VM、RDS、Storage、LB、NAT、Snapshot）並強制加 tag：`env`、`team`、`project`、`owner`
- **Why**: 沒有 tag 就沒有成本歸因（cost allocation）；沒有歸因就無法找負責人；沒有負責人就沒人在意 idle 資源
- **Gotcha** [CathaySec, confirmed]: ISO 27017 audit 期間整理資產清冊，**副產品發現 GCP VM + GKE node 長期開著但無使用 → 清除後節省 NT$400k**。盤點本身就是最佳的 FinOps 觸發器；audit 強制盤點 = 免費的 FinOps review
- **KKStream 的 GitOps 資產管理**（`infra-asg-manager`）：ASG Launch Config 用 `lc_cfg.yml` 聲明式定義，git push 觸發 GitLab CI 自動 create 新 LC 版本、更新 ASG、清除舊 LC（AWS 有 100 個/region 上限，不清理會撞牆）。Git history = 完整資產版本歷史，`git diff HEAD~1` 就知道這次變更了哪個服務的 LC

### Step 2 — 成本視覺化與告警

- **What**: 設定 Budget Alert（80% / 100% threshold）；用 Cost Explorer（AWS）或 GCP Billing Report 按 tag 拆出各 service / team 的每日花費；每週 email digest 給 stakeholder
- **Why**: 「看不到就不在意」是雲端成本最大的心理陷阱；數字公開後工程師自然開始 care
- **CathaySec 工具組**（user confirmed）：Apptio（成本分析 SaaS）+ GCP 原生 Billing Export → BigQuery + Looker Studio 看板；三層可視化：原始帳單（GCP）→ 分析層（BigQuery/Apptio）→ 管理報表（Looker Studio）
- **Gotcha** [KKStream]: AWS Savings Plans 購買時沒有先完成盤點，部分 compute 在 RI/SP 生效後才發現是低使用率機型，折扣買了但 coverage rate 偏低；盤點必須**早於**承諾購買

### Step 3 — Right-sizing（由大到小）

- **What**: 用 2 週 CPU / Memory 利用率（P90/P99）找出 consistently over-provisioned 機器；降規（vertically）或合併工作負載
- **Why**: Cloud infra 常沿用最初「安全估算」的機型，6–12 個月後使用模式穩定，通常有 30–50% 過度佈建
- **Gotcha** [SoundOn, confirmed]: RDS 在 DB query 優化後（10x speed）CPU 降低 → 判斷可降規 RDS → 但瓶頸轉移至 IOPS；降規後 query 延遲飆升，需加回 provisioned IOPS 才解決。**先查 CloudWatch `ReadIOPS`/`WriteIOPS`，再決定降規幅度**
- **SoundOn Beanstalk 做法**（confirmed）：multi-instance type + Spot instance 混搭（web tier stateless，適合 Spot）→ compute 成本下降，無需 RI commitment

### Step 4 — Commitment Discount（Savings Plans / RI / CUD）

- **What**: 分析 On-Demand baseline（過去 3 個月穩定用量）→ 購買 1-year Compute Savings Plans（AWS）或 1-year CUD（GCP）覆蓋 baseline；spike / 測試環境保留 On-Demand 或 Spot
- **Why**: SP/RI/CUD 在 1-year 計劃通常給 20–40% 折扣（Compute SP 最靈活，不鎖 instance type）；用 3 個月數據避免購買「昨天的規格」
- **Gotcha** [KKStream]: 最大節省來自 SP — 年省 $150k USD；SP 靈活性（可跨 instance family）讓後來的 right-sizing 不影響 coverage；RI 則相反，right-sizing 後常需要 RI modification 或賣 Marketplace [需 Zeuik 確認 KKStream 具體 SP 類型與期限]

### Step 5 — 排程關機（Scheduled Shutdown）

- **What**: 非生產環境（dev / staging / QA）設定排程：工作時間外（18:00–08:00）+ 週末自動關機
- **Why**: non-prod 環境通常佔 cloud bill 10–20%；下班時間關機直接省 40–60% 的 non-prod 成本
- **Gotcha** [SoundOn 推論]: 跨時區團隊（台灣 + 海外工程師）關機時間設定要統一協議，否則有人還在用 QA 被自動關掉；改用 tag-based override（`AutoShutdown: false`）讓個別資源豁免

### Step 6 — 廠商談判與企業協議

- **What**: 年花費 > $100k USD 時主動聯繫 CSP 帳客（TAM / 客戶經理）談 EDP（Enterprise Discount Program）或 Private Pricing；CathaySec 與 GCP 有直接合作
- **Why**: EDP 通常要求 commit $1M+ / 3 年，但 $100k 以上的客戶可以談 non-standard discount（10–20%）；公開 pricing 很少是你應該付的價格
- **Gotcha**: 談判前必須有清晰的 usage forecast + 成長計畫；沒有數字就沒有籌碼；EDP 簽了就有 minimum commitment，佈建計畫一定要保守估

---

## Concrete Numbers

| 職涯段 | 節省金額 | 主要手法 | 平台 |
|--------|---------|---------|------|
| KKStream（2019–2021） | $150,000 USD/年 | Savings Plans + RI | AWS |
| SoundOn（2022–2023） | **$60,000 USD/年**（PDF v2024.2 confirmed） | CDN migration：Cloudfront → Cloudflare | AWS |
| CathaySec（2024–now） | NT$400,000/年（約 $12k USD） | 資產盤點 → idle 清除 | GCP |
| **累積** | **$222,000 USD/年等值**（$150k + $60k + $12k） | — | 跨雲 |
| Right-sizing 節省率（業界） | 20–40% | CPU P90 持續 < 20% | 通用 |
| Non-prod 排程關機節省 | 40–60%（non-prod 成本） | 12h × 5d + 週末 | 通用 |
| SP vs On-Demand 折扣（1-year）| 20–40% | Compute SP 最靈活 | AWS |
| GCP CUD vs On-Demand（1-year）| 37% | N1/N2 機型 | GCP |

---

## Anti-patterns（不要做）

1. **盤點前就買 RI / Savings Plans**
   - 問題：KKStream 初期 RI 買了不匹配的 instance family，右移後 RI coverage rate 只剩 60%；差額還是付 On-Demand
   - 解：盤點 → right-sizing → **然後才**買 commitment；至少等 2 個月穩定數據

2. **非 tag 資源不管理**
   - 問題：CathaySec 初期 GCP 資源 tag 不齊，billing report 有 30% 成本歸在 `(untagged)`；無法追責
   - 解：Org Policy 強制 tag（`compute.restrictResourceWithoutTag`）；Terraform 模組預設帶 tag variable，沒傳就 validate 失敗

3. **FinOps 只有 infra 人知道，業務方不參與**
   - 問題：工程師省完錢，下一季 PM 又開一堆 staging 環境做 demo，成本反彈；沒有共識就沒有持續效果
   - 解：週報給 stakeholder；季度 FinOps review 邀請 PO 參與；讓業務方看到自己的成本中心數字

---

## Decision Tree

```
執行 FinOps 優化，從哪裡開始？

Step 0：是否有完整 tag?
├─ 否 → 先做 tag enforcement（Org Policy / Service Control Policy）
└─ 是 → 繼續

帳單規模
├─ < $10k/月 → right-sizing + 排程關機（ROI 最高）
├─ $10k–$100k/月 → + Savings Plans（1-year Compute，最靈活）
└─ > $100k/月 → + 廠商談判 EDP / Private Pricing

環境類型
├─ 生產（24/7）→ SP/RI/CUD（不關機）
├─ Staging → SP（1-year）+ 排程關機（8h off × 7d = -33%）
└─ Dev/QA → 完全 On-Demand + Spot + 排程關機（最大化省錢）

DB 優化
├─ CPU 利用率 < 20% P90 → 考慮降規，但先確認 IOPS 不是瓶頸
├─ RDS Multi-AZ 非必要 → 改 Single-AZ（dev/staging）
└─ Aurora Serverless v2 → bursty workload 的 right-sizing 替代
```

---

## References

- 職涯段：`raw/career-summary.md#4-kkstream--kkcompany--sre--devops--dba--architect`
- 職涯段：`raw/career-summary.md#5-goodnight--soundon--sre--architect`
- 職涯段：`raw/career-summary.md#8-cathaysec-國泰證券--sre-lead--manager-current`
- [AWS Savings Plans — official docs](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html)
- [GCP Committed Use Discounts](https://cloud.google.com/compute/docs/instances/committed-use-discounts-overview)
- [FinOps Foundation — Framework](https://www.finops.org/framework/)
- 關聯：[[finops-savings-plans-roi]]、[[gcp-landing-zone]]、[[kkstream-lessons]]、[[soundon-lessons]]、[[cathaysec-lessons]]
