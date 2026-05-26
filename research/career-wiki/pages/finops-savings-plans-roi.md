# AWS Savings Plans ROI — Streaming Service Case Study

> **Source positions**: KKStream / KKCompany 2019–2021
> **Last ingested**: 2026-04-21
> **Confidence**: high（Zeuik 直接主導 FinOps 決策）
> **Linted**: 2026-04-21

---

## Context

KKStream 是流媒體服務，EC2 長期穩定負載（12 個月變化 < 20%）、高可用要求 — 這種 workload 特徵讓**長期 commitment 折扣**（Savings Plans / RI）合理可控。本頁總結 $150k USD/yr 節省的 5 步採購評估方法論。

---

## Core Methodology

### Step 1 — Baseline Analysis

- **What**: Cost Explorer 拉 12 個月 Usage data（family / region / AZ 維度）篩 stable workload（Coefficient of Variation < 20%）
- **Why**: 不穩定 workload commitment 會買過多（unused commitment）或過少（無法覆蓋尖峰）；12 個月涵蓋季節波動
- **Gotcha** [KKStream]: 初期用 3 個月數據假設「夏天高」而高估，實際串流業務平穩；**必須用完整 12 個月**找真 baseline

### Step 2 — Coverage Target

- **What**: 決定 SP coverage 70% / 80% / 90%
- **Why**: 100% = 完全 lock-in（轉 serverless 或 Graviton 時廢）；70% 保留彈性但折扣少；80% 是 sweet spot
- **Gotcha** [KKStream]: 初期 80% → 2 年穩定後達 90%；Coverage 太激進會買到「升級窗口關閉後的遠期 commitment」

### Step 3 — SP 類型選擇（Compute SP vs EC2 IP SP vs SageMaker SP）

- **What**: 
  - **Compute SP**: 跨 family / region / OS，折扣 ~30%，最彈性
  - **EC2 Instance SP**: 綁 family（m5.large），折扣 60–72%，折扣最深
  - **SageMaker SP**: 專用（不在此範疇）
- **Why**: 折扣差 42 個百分點；選型決定年省金額上限
- **Gotcha** [KKStream]: 一開始買 Compute SP（怕換機型），3 個月後改 EC2 IP SP，**損失初期折扣差**。推薦：先 Compute SP 試 → 續約改 Instance SP

### Step 4 — Term + Payment Model

- **What**: 1yr（20–35% off）vs 3yr（40–60% off）；All / Partial / No Upfront
- **Why**: 3yr 折扣更深但業務風險高；Partial Upfront 平衡折扣與現金流
- **Gotcha** [KKStream]: 初 All Upfront 現金流壓力大 → 改 Partial Upfront；**事先協調 CFO** 現金規劃

### Step 5 — Rollout + Ongoing Monitoring（自動化月報）

- **What**: Cost Explorer recommendation engine、每季 utilization review、unblended cost 走勢
- **Why**: AWS 定期更新推薦；workload 轉變需要調整；unused commitment 每月損耗
- **Gotcha** [KKStream]: 某季 utilization 只 82%（買太多）→ 下次降 coverage 至 75%
- **KKStream 自動化實作**（`kkstream-ri-sp-report` Lambda）：
  1. 每月排程觸發，從 S3 讀 `KKS-account-list.csv`（多帳戶清單）
  2. 跨帳戶呼叫 Cost Explorer：`GetSavingsPlansUtilization`（現況）+ `GetSavingsPlansUtilizationRecommendation`（建議購買量）+ `GetSavingsPlans`（現有 SP portfolio）
  3. 產出 XLSX 報告（各帳戶 coverage%、hourly commitment to purchase、estimated savings）
  4. 上傳 S3 並 Slack 通知各 cost center 負責人
  - **結論**：Step 5 不是人工檢查，是全自動月度決策支援系統

### 多帳戶聯合採購的特殊考量

- KKStream 有 Videopass/Telasa/TFC 等多個 linked accounts，consolidated billing 讓 SP 可跨帳戶共享
- 各帳戶 usage pattern 不同（Telasa 日本用戶集中深夜 JST，Videopass 台灣分散）→ 合併分析才能找真 baseline
- 跨帳戶 coverage 最適化（全公司層級）比逐帳戶購買省 10–15%（避免各帳戶各留 buffer）

---

## Concrete Numbers

| 指標 | 值 | 備註 |
|------|----|------|
| **年度節省** | **$150,000 USD** | KKStream 2019–2021 實績 |
| Compute SP 折扣 | ~30% | AWS 2021 報價 |
| EC2 Instance SP 折扣（m5.large）| ~72% | KKStream 採購 |
| 折扣差距 | 42 pp | IP SP vs Compute SP |
| 1yr SP 折扣 | 20–35% | 官方 |
| 3yr SP 折扣 | 40–60% | 官方 |
| KKStream 選擇 | 3yr Partial Upfront | 平衡折扣與現金流 |
| Utilization 目標 | ≥ 90% | 每季檢查 |
| Partial Upfront break-even | 6–9 個月 | monthly 攤銷 + discount |
| RI exchange fee | ~25–30% 差價 | 中途改 family 代價 |
| Cost Explorer recommendation 採用率 | 80–90% | 10–20% 需人工調 |
| Review 頻率 | 每季 | 對應業務/架構變化 |

> [需 Zeuik 確認] Partial Upfront 月餘額計算、實際 RI exchange case

---

## Anti-patterns

1. **買太多 RI/SP → Lock-in 無法轉向**
   - 問題：估「未來 3 年成本升」買滿 3yr All Upfront，1 年後業務轉 Lambda/Fargate → RI 廢鐵
   - 解：1–1.5 年試水，不急 3 年全 commit

2. **All Upfront 忽略現金流 + FinOps 預算**
   - 問題：帳面年省 $150k 但 upfront $200–300k，壓 CFO
   - 解：Partial Upfront 30–50% + 月付，仍達 80–90% 折扣

3. **忽視 RI/SP 轉換限制**
   - 問題：中途換 family 被收 25–30% 差價
   - 解：購買前確認 12–24 個月架構方向；彈性高用 Compute SP，確定用 Instance SP

4. **跨 AZ/region 購買策略錯誤**
   - 問題：假設「要擴 us-west-2」買 region-flexible SP，實際業務沒擴 → 大量 SP 閒置
   - 解：只買**當前 + 已規劃 region**的 SP

---

## Decision Tree

```
考慮 SP / RI？
├─ Workload 穩定度 > 80% 且計畫 ≥ 12 個月
│  └─ SP（比 RI 更靈活）
│     ├─ Coverage: 70% / 80% / 90%
│     ├─ 機型確定嗎？
│     │  ├─ Yes (m5.large 等) → EC2 IP SP（60–72%）
│     │  └─ No (未來轉 Graviton 等) → Compute SP（~30%）
│     └─ 現金流：
│        ├─ 充足 → All Upfront
│        ├─ 緊張 → Partial（30–50% + 月付）
│        └─ 需彈性 → No Upfront
├─ 波動 < 60% 或短期 → Spot + On-Demand
├─ 創業期 / 架構試驗 → On-Demand 為主
└─ 不能 AWS lock-in → 評估 multi-cloud（須算遷移成本）

監控：
├─ 每季 review Cost Explorer + utilization
├─ Utilization < 85% → 下次降 coverage
├─ 新專案上線 → 評估補購 SP
└─ AWS 新機型（Graviton）→ 評估遷移
```

---

## References

- 職涯段：`raw/career-summary.md#4-kkstream--kkcompany--sre--devops--dba--architect`
- [AWS Savings Plans docs](https://docs.aws.amazon.com/savingsplans/latest/userguide/)
- [AWS Cost Explorer Recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-rightsizing.html)
- [AWS Pricing Calculator](https://calculator.aws/)
- [AWS SP vs RI Comparison](https://aws.amazon.com/savingsplans/compute-pricing/)
- 關聯：[[aws-step-functions-patterns]]、[[finops-cross-position-patterns]]（Session 3）
