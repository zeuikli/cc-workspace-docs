# KKStream / KKCompany — Lessons Learned

> **Tenure**: 2019–2021（approx）| **Role**: SRE + DevOps + DBA + Architect
> **Last ingested**: 2026-04-21 | **Confidence**: high

---

## Context

Streaming 服務 infrastructure；AWS 400% 效能提升、**$150k USD/yr Savings Plans**、Step Functions 自動化、SQL tuning 200%、alarm -50%。產品線：Videopass（台灣）、Telasa（日本）、TFC（日本），共三套平台同時維運。

## Key Lessons

1. **Savings Plans > RI（彈性 + 相近折扣）**
   - 3yr Partial Upfront SP = sweet spot（~60% 折扣 + 現金流可控）
   - 但要先確認機型方向；否則 Compute SP 試水半年再改 Instance SP
   - **實作層面**：`kkstream-ri-sp-report` Lambda 每月排程，跨多帳戶拉 Cost Explorer 數據，輸出 XLSX → Slack，完全自動化月度 SP 決策報告
   - 見 [[finops-savings-plans-roi]]

2. **Step Functions 選型錯誤 = 成本爆表主因**
   - 7 min 流程誤用 Standard → 每 transition 計費，成本比 Express 高 10x
   - Map state 內 transitions 更恐怖（100 元素 × 10 step = 1000 transitions）
   - **實際代碼印證**：`saku-chatops-slack/lambda_function/alarm-automation/src/main.py` 的 StartExecution 呼叫顯示後期已改用事件驅動方式啟動 state machine，而非同步等待結果
   - 見 [[aws-step-functions-patterns]]

3. **Alarm -50% 來自「告警即代碼（Alarm as Code）」**
   - 不只是降噪，而是把告警定義從手動操作搬進 YAML + Lambda 自動管理
   - **具體實現**：`aws-alarm-police` 框架 — 雙層設計：(1) `alarm_default_setting.yml`（告警規則 + regex pattern override），(2) `filter.yml`（環境 pattern）
   - Lambda 定期掃描所有 AWS 資源（ELB/EC2/RDS/ECS/ElastiCache），按 YAML 規則自動 create/update/delete CloudWatch alarms
   - 後期延伸：alarm → SNS → Lambda 自動補救（`saku-chatops-slack/alarm-automation`），用 jmespath 解析告警維度，符合條件自動啟動 Step Functions state machine
   - 見 [[aws-alarm-as-code]]

4. **SQL tuning 200% 往往在 app 層改動**
   - Saku/TFC project 的關鍵是減少 round-trip + batch + denormalize
   - 不是 DB 慢，是 query pattern 設計錯

5. **ChatOps 是「人工操作轉代碼」的橋梁**
   - 5 套 Slack ChatOps（saku/tfc/jcl/up/product）的共通架構：user email → team ownership → environment config → 確定性執行
   - `config42` 讀環境別配置，同一份 code 多環境復用；`lookup_by_email` 自動對應 ownership（不是個人，是 team）
   - 每個自動化操作都有 Slack ack + execution ID，可審計

6. **跟 AWS Solution Architects 建立 framework 合作**
   - Partner 資源在大客戶身份下很有價值
   - 定期 architecture review + 新 feature PoC 會先於文件公告

## Architecture Patterns（從代碼提煉）

### 三平台共用 Lambda 框架

- CDK 模板化：`FunctionPython38` + `RequirementsLayer`，預設 runtime Python 3.8、memory 128MB、timeout 60s、log retention 6 months
- requirements.txt 自動打包成 Lambda layer（內容尋址哈希，避免重複上傳）
- 所有資源帶預設 tags（Environment/ServiceName/Product）

### 轉碼系統三層架構（舊：SWF 時代）

```
S3 upload → Lambda Manager（解析 manifest）
         → Decider service（決定轉碼品質 profile）
         → Worker pool（SWF heartbeat + ffmpeg）
         → post-processor（計費/索引）
```

Worker 每 30s heartbeat，若失敗超過 N 次 terminate 整個 process（避免 zombie）。

### 直播容量預測

- `telasa-promotion`：Excel 促銷時間表 → 計算分步啟動 schedule → CloudWatch EventRule 自動 scale ASG
- 核心公式：`step = ceil(increment / batch_increment)`，分批啟動避免 thundering herd
- 見 [[live-streaming-capacity-planning]]

## What I'd Do Differently

- 從 day 1 強制 `runbook-first` — 建立服務前先寫 oncall playbook
- Step Functions 選型 decision tree 納入 onboarding（避免新人踩坑）
- Savings Plans 決策寫成 SOP（已有 kkstream-ri-sp-report 自動化，但 SOP 文件需補）
- 告警框架從 day 1 統一（不要讓 videopass/tfc/saku/prism 各自獨立，難以聯邦化管理）

## Cross-references

- 核心 pages：[[finops-savings-plans-roi]]、[[aws-step-functions-patterns]]、[[aws-alarm-as-code]]
- 延伸：[[sre-oncall-training-program]]、[[live-streaming-capacity-planning]]

## References

- `raw/career-summary.md#4-kkstream--kkcompany--sre--devops--dba--architect`
- Code source: `/Users/zeuik/Desktop/KKStream_Code`（local only，未公開）
