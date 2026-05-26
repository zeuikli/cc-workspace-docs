# CathaySec 國泰證券 — Lessons Learned

> **Tenure**: 2024–now | **Role**: SRE Lead + Manager
> **Last ingested**: 2026-04-21 | **Updated**: 2026-05-17 (added Cloud Run + Vertex AI FinOps + SLA monitoring)
> **Confidence**: high

---

## Context

台灣證券業雲端轉型 + ISO 27017（BSI）認證 + FinOps NT$400k 節省。工作範疇：GCP Landing Zone、應用系統上雲（7R + 雲化改造）、Vertex AI 導入、CNAPP 評估、TFE 全新部署、FinOps 工具（Apptio）、冷備份系統上雲作為 ISO 27017 主要取證項目。金融業合規嚴苛 + tech leadership 職責同時上身。

## Key Lessons

1. **合規不是 afterthought，是架構 baseline**
   - Landing Zone 建置階段就嵌入 ISO 27017 控制比事後補省 50% 整改成本
   - 見 [[gcp-landing-zone]]、[[iso27017-audit]]

2. **Terraform state 屬於 change management 範疇**
   - IaC 好處 = 可審計；但 state 改無 commit log / 無人簽核 → 稽核員一樣要求補人工單
   - Git commit GPG 簽署 + 強制 PR review

3. **Org Policy 不能後補**
   - 晚 6 個月補 policy → 200+ 資源違反，整改 4–6 週
   - 建置時就決策 2 年政策目標；先 report-only mode 試 3 個月

4. **FinOps 副產物：資產盤點發現 idle 資源**
   - 合規專案的副產品是 NT$400k/年的 waste 消除
   - 合規 + FinOps 綁一起做比分開做高效

5. **Hybrid cloud 的 Interconnect 需提前 3 個月啟動**
   - Partner Interconnect 申請週期 6–8 週，卡進度的是合約而非技術

6. **監控培訓要從「指標意涵」切入，不從工具切入**
   - CathaySec 內部培訓（2025-10）發現：工程師會用 Cloud Monitoring，但不知道「CPU 80% 代表什麼業務影響」
   - 正確順序：業務情境（使用者抱怨什麼）→ 對應技術指標 → 再學工具操作
   - 見 [[gcp-monitoring-alerting]]（監控指標矩陣 + 判讀指南）

7. **異常通報流程必須書面化且有時間記錄要求**
   - 金融業稽核要求：異常發現時間、通報時間、處置時間、恢復時間都要記錄
   - 口頭通報不算，截圖 + 文字記錄才算 evidence
   - 見 [[sre-oncall-training-program]]（CathaySec 異常通報升級鏈）

8. **應用上雲 7R 評估要先做，不要直接 Lift & Shift**
   - 7R（Rehost / Replatform / Refactor / Rearchitect / Repurchase / Retire / Retain）評估讓上雲路徑圖有優先序
   - 金融業常見陷阱：以為 Rehost 最快，但上雲後 licensing cost + 舊架構 bottleneck 反而讓 TCO 更高
   - 雲化改造（Replatform/Refactor）短期更複雜，但長期符合 Cloud Native 架構的維運成本才是真正優化點

9. **Vertex AI 導入：RAG + LLM 整合的 PoC 必須限定問題域**
   - Gemini API / LLM 整合 + Vertex AI Search / RAG 是 CathaySec AI 應用的兩條主線
   - 金融業 AI PoC 陷阱：問題太廣泛 → accuracy 達不到業務要求 → 被否定整個 AI 方案
   - 正確做法：先限定問題域（如：內部 FAQ 查詢、法遵文件檢索）→ 證明 accuracy 可接受 → 再擴展
   - RAG pipeline 的 chunk strategy 和 embedding model 選擇對 retrieval quality 影響比 LLM 本身更大

10. **CNAPP 評估：CSPM 先、CWPP 後的分階策略**
    - 三方對比：GCP SCC Premium（原生）vs 第三方工具 vs Microsoft Defender for Cloud
    - 評估已完成，有明確結論（具體選型不公開）
    - **原則**：先解決「看清楚自己有什麼風險」（CSPM = 設定錯誤 + 合規掃描），再解決「runtime 防護」（CWPP）；不要兩個同時上，部署複雜度 × 2
    - 金融業 CNAPP 採購陷阱：供應商 demo 環境整合良好，但實際金融業 workload（mainframe legacy + GCP hybrid）整合複雜度被低估

11. **TFE From Scratch 在金融環境的挑戰**
    - 全新安裝 TFE：需同時處理 network isolation（air-gap 或半隔離）+ 合規 audit log + SAML SSO 整合
    - 金融業特殊要求：workspace 的 approval policy 必須有人工簽核環節，純 automation 無法通過稽核
    - Sentinel policy 作為 compliance-as-code：把 ISO 27017 控制項轉為 Sentinel rule 讓 IaC 部署前自動檢查

12. **FinOps Culture 建置比工具更難**
    - 工具組：Apptio（成本分析 SaaS）+ GCP 原生 Billing + Looker Studio 視覺化帳單
    - 工具好建，難的是讓業務單位接受「雲端費用是他們的責任」
    - 有效做法：Looker Studio 帳單看板按 team/project tag 拆分 → 季度 FinOps review 邀請 PM 參加 → 費用與績效連結
    - 見 [[finops-cross-position-patterns]] §Step 2（成本視覺化）

13. **冷備份系統上雲 = ISO 27017 主要取證項目**
    - Dell PowerProtect Data Domain Virtual Edition 整合 GCP 作為冷備份方案
    - 在 BSI ISO 27017 審查中，備份機制（特別是雲端備份加密 + 跨區域備援）是主要稽查控制項目
    - 取證要點：備份加密 at-rest + in-transit、備份存取 IAM 控制記錄、定期恢復演練 log 作為稽核證據
    - 對比 HTC 時期用磁帶備份：雲端備份最大優勢是稽核 trail 自動化（每次備份 / 恢復都有 GCP Audit Log）

---

## GCP FinOps 實踐 — Cloud Run & Vertex AI Gemini

> 更新於 2026-05-17，作為 CathaySec 執行 FinOps 的參考資料與實踐指引。

### Cloud Run 費用優化

Cloud Run 按 **vCPU + Memory × 實際請求處理秒數** 計費，核心優化方向：

| 優化項目 | 做法 | 預估節省 |
|---------|------|---------|
| **CPU 分配模式** | 預設 `CPU only during request` 即可；background job 才考慮 `CPU always allocated + min-instances=1` | 視 idle 比例而定 |
| **Concurrency 調高** | 預設 80，可提升至 200–1000（視 workload memory 安全範圍）| 20–40%（instance 費）|
| **Non-prod min-instances=0** | Staging / Dev 完全按需，非工時零成本 | 60%（non-prod）|
| **Right-sizing** | P90 CPU < 20%、Memory < 50% → 降規一格；先改 staging 觀察 2 週 | 10–20% |
| **CUD（1 年）** | baseline vCPU 用量穩定後購買 Compute CUD | ~17% |

**CathaySec 注意事項**：金融業 prod 環境建議保留 `min-instances=1` 確保冷啟動不影響交易 SLA；Non-prod 排程關機即可大幅降低閒置成本。

---

### Vertex AI Gemini — 費用優化

#### 模型分層（Model Tiering）

| 模型 | 定位 | 適用場景 |
|------|------|---------|
| **Gemini 2.5 Pro** | 最強推理、1M token context | 法遵文件分析、複雜 RAG、程式碼生成 |
| **Gemini 2.5 Flash** | 價效比平衡，具 thinking 能力 | 80% 日常任務首選（內部問答、摘要）|
| **Gemini 2.5 Flash-Lite** | 最低成本，比 2.0 Flash 快 1.5x | 高吞吐量批次處理、簡單分類意圖識別 |

#### Context Caching（最高 ROI，優先做）

Gemini 原生支援 context caching，重複使用的 system prompt / few-shot examples 快取後：

| 計費類型 | 成本比例 |
|---------|---------|
| 一般 input tokens | 1x |
| Cache write | ~1x（一次性）|
| **Cache read** | **0.25x（省 75%）** |

```python
# Vertex AI context caching
cached_content = genai.caching.CachedContent.create(
    model="gemini-2.5-flash",
    contents=[system_prompt, reference_docs],
    ttl=datetime.timedelta(hours=24)
)
```

適用場景：固定 system prompt > 1,000 tokens、RAG context、法遵文件 few-shot examples。

#### Batch Prediction（非即時任務省 ~50%）

報告生成、資料標注、離線合規掃描 → 改用 Batch API，費用約 Online API 的一半。

---

### Provisioned Throughput（Gemini GSU）決策框架

Provisioned Throughput 是預購 TPM（tokens/min）容量，折扣約 **20–40%**，但使用率不足會虧損。

#### Break-even 計算

```
break_even_utilization = provisioned_price / pay_per_use_price
```
若折扣 30% → 使用率需 > **70%** 才回本。

**量測現有使用率**：
```bash
gcloud monitoring time-series list \
  --filter='metric.type="aiplatform.googleapis.com/publisher/online_serving/token_count"' \
  --interval="<start>/<end>"
```
查 P50 / P90 / Peak TPM，算出 baseline vs peak 比值。

#### 採購決策矩陣

| 流量特徵 | 建議策略 |
|---------|---------|
| P50 > 70% of Peak，流量平穩 | 全量買 Provisioned Throughput |
| P50 約 40–60% of Peak，有明顯尖峰 | **Hybrid**：Provisioned 覆蓋 baseline + Pay-per-use 吃 burst |
| 流量不穩定 / 剛上線 | 先跑 2–3 個月 pay-per-use，累積數據再評估 |
| Batch / 非即時任務 | 改用 Batch Prediction，不需 Provisioned |

#### Hybrid 策略（企業最常見做法）

```
Provisioned TPM = P70 使用量（非 Peak）
剩餘 burst      → Pay-per-use 自動 fallback
```

避免為 10% 時間的尖峰付整月固定費用。

#### 採購前 Checklist

- [ ] 至少 **2 個月** token 用量數據（P50 / P90 / Peak TPM）
- [ ] 確認目標模型支援 Provisioned Throughput（2.5 Flash / 2.5 Pro 均支援）
- [ ] P50 使用率 > break-even（通常 > 70%）才採購
- [ ] Batch 任務已分離，不佔用 Provisioned 容量
- [ ] 承諾期（1 年）內預估流量成長 → **少買**，之後再加購
- [ ] 設 Cloud Monitoring alert：使用率 < 60% 連續 1 週 → 重新評估

#### 優化路徑總覽（依 ROI 排序）

| 優先級 | 措施 | 預估節省 | 難度 |
|--------|------|---------|------|
| P0 | Gemini context caching | 40–70%（token 費）| 低 |
| P1 | Cloud Run concurrency 調高 | 20–40%（instance 費）| 低 |
| P1 | Staging 非工時 min-instances=0 | 60%（non-prod）| 低 |
| P2 | Gemini Flash 取代 Pro（低複雜度任務）| 80%（該 tier）| 中（需 evals）|
| P2 | Batch Prediction 離線任務 | 50%（batch 部分）| 中 |
| P3 | Cloud Run CUD + Vertex Provisioned Throughput | 17–40% | 低（需承諾）|

> **執行建議**：先做 P0/P1（本週可完成，不需架構改動），跑 2 週數字後再決策 P2/P3。

---

## GCP SLA 監控與外部稽核取證

> 更新於 2026-05-17。金融業外部稽核（ISO 27017 / 金管會）高頻問題：如何確認 GCP SLA 有如宣稱達標？

### 核心原則

**GCP 的 SLA 是他們自己宣告的；稽核員要的是你方的獨立量測證據。**

```
Layer 1: GCP 官方事件紀錄（Google 側）
Layer 2: 你方獨立量測（內部 + 外部探針）
Layer 3: 稽核證據鏈（自動保存 + 可查詢）
```

---

### Layer 1 — GCP 官方事件追蹤

使用 **Service Health API** 程式化查詢歷史事件：

```bash
gcloud alpha service-health events list \
  --location=global \
  --filter="services:compute.googleapis.com" \
  --format="table(name,startTime,endTime,title)"
```

或訂閱事件推播（整合進 alerting pipeline）。歷史 JSON 也可從 https://status.cloud.google.com 下載。

> **稽核員反問**：「這是 Google 自己說的，你怎麼獨立驗證？」→ 需要 Layer 2。

---

### Layer 2 — 你方獨立量測

#### 方法一：Cloud Monitoring Uptime Checks（最快部署）

```bash
gcloud monitoring uptime-check-configs create \
  --display-name="API Uptime Check" \
  --http-check-path="/health" \
  --host="your-service.run.app" \
  --period=60s \
  --timeout=10s
```

設對應 alerting policy，SLA 違反時自動通知並留 alert 記錄。

#### 方法二：外部第三方探針（稽核最有說服力）

| 工具 | 特點 | 適用情境 |
|------|------|---------|
| **Pingdom / UptimeRobot** | 從非 GCP 節點探測 | 最直接的獨立量測 |
| **Datadog Synthetic** | 可模擬用戶操作路徑 | 端到端 SLA 驗證 |
| **Grafana Cloud** | 自架可控 | 資料不離境需求 |

**關鍵**：探針必須來自 **GCP 外部**，否則 GCP 自身故障時探針也會同步失效，喪失獨立性。

#### 方法三：Cloud Monitoring 自定義 SLO

```yaml
# SLO 設定：Cloud Run 服務 99.9% availability
slo:
  displayName: "Cloud Run SLO 99.9%"
  serviceLevelIndicator:
    requestBased:
      goodTotalRatio:
        goodServiceFilter: |
          metric.type="run.googleapis.com/request_count"
          metric.label.response_code_class="2xx"
        totalServiceFilter: |
          metric.type="run.googleapis.com/request_count"
  goal: 0.999
  calendarPeriod: MONTH
```

---

### Layer 3 — 稽核證據鏈

#### BigQuery 長期保存（必做，金融業 3 年 retention）

```bash
gcloud logging sinks create sla-audit-sink \
  bigquery.googleapis.com/projects/PROJECT/datasets/sla_audit \
  --log-filter='resource.type="cloud_run_revision"'
```

設定 BigQuery table expiration = **3 年**。

#### 每月 SLA 報告自動化（BigQuery 查詢）

```sql
SELECT
  DATE_TRUNC(timestamp, MONTH) AS month,
  COUNTIF(httpRequest.status < 500) / COUNT(*) AS availability,
  COUNT(*) AS total_requests,
  COUNTIF(httpRequest.status >= 500) AS error_count
FROM `project.dataset.cloudrun_logs`
WHERE timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 90 DAY)
GROUP BY 1
ORDER BY 1 DESC
```

用 Looker Studio 串接自動產出月報，送 PM / 合規部門。

#### SLA Credit 申請（稽核常被忽略的 evidence）

GCP 發生事件後，即使金額小，**主動申請 SLA credit** 本身就是「我們有積極監控」的稽核 evidence。

```
GCP Console → Billing → Credits → Request Service Credit
```

記錄：申請日期、事件 ID、影響服務、核准金額 → 放進稽核 evidence folder。

---

### 外部稽核常見問答對照

| 稽核員問題 | 對應的證據 |
|-----------|-----------|
| 「GCP 上個季度有沒有 outage 影響你們？」| Service Health API 事件清單 + 你方 alert 記錄 |
| 「你們怎麼知道 GCP 有達到 99.9%？」| Cloud Monitoring Uptime Check 月報 / 第三方探針數據 |
| 「SLA 沒達標時你們怎麼處理？」| GCP SLA credit 申請記錄 |
| 「資料保留多久？」| BigQuery sink 設定截圖 + table expiration policy |
| 「這些監控資料在哪裡？誰有權限看？」| IAM 存取設定 + Looker Studio 報表連結 |

---

### CathaySec 最小可行部署時程

| 週次 | 工作項目 |
|------|---------|
| Week 1 | Cloud Monitoring Uptime Check × 所有對外服務 |
| Week 2 | BigQuery log sink（3 年 retention）|
| Week 3 | Looker Studio 月報 dashboard（自動產出）|
| Week 4 | Service Health API → 事件自動記錄到 BigQuery |

四步完成後，下次稽核可直接出示數據，不需靠「GCP 說它達標」回答。

---

## What I'd Do Differently

- **更早** 啟動 VPC 規劃（subnet `/24` 階層化）而非事後擴增
- IAM custom roles 從 day 1 就限制 upper bound（max 15），避免權限蔓延
- 稽核 evidence chain 從 day 1 自動化（365 day retention 預設）
- Vertex AI token 用量從第一天就串 Cloud Monitoring，否則買 Provisioned Throughput 前缺數據依據
- SLA 監控從 day 1 就建外部探針 + BigQuery sink，而非等到稽核前才補建

## Cross-references

- 核心 pages：[[gcp-landing-zone]]、[[iso27017-audit]]、[[terraform-multi-cloud]]
- 延伸：[[finops-savings-plans-roi]]（FinOps 方法論）、[[gcp-monitoring-alerting]]（監控指標設計 + 告警架構）、[[sre-oncall-training-program]]（異常通報流程 + SRE 人才培育）

## References

- `raw/career-summary.md#8-cathaysec-國泰證券--sre-lead--manager-current`
- [Gemini 2.5 Pro on Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-pro)
- [Gemini 2.5 Flash on Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash)
- [Gemini 2.5 GA Blog](https://cloud.google.com/blog/products/ai-machine-learning/gemini-2-5-flash-lite-flash-pro-ga-vertex-ai)
- [GCP Service Health API](https://cloud.google.com/service-health/docs/overview)
- [GCP SLA 總覽](https://cloud.google.com/terms/sla)
