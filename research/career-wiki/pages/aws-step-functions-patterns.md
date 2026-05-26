# AWS Step Functions — Production Patterns

> **Source positions**: KKStream / KKCompany 2019–2021（streaming event automation）
> **Last ingested**: 2026-04-21
> **Confidence**: high（Zeuik 實施 Step Functions + ECS 流媒體自動化）
> **Linted**: 2026-04-21

---

## Context

KKStream 用 AWS Step Functions + ECS 做 streaming event 自動化（轉碼 / 儲存 / 索引 / 計費）。長流程 + 狀態機 + 視覺化 + 跨服務協調是其優勢。選型與成本模型錯誤是最常見踩坑 — 本頁整合 6 個 production pattern + 4 個 anti-pattern。

**代碼佐證**：`saku-chatops-slack/lambda_function/alarm-automation/`（alarm → Step Functions）、`videopass-encoding-system-worker/jack/core.py`（SWF heartbeat，Step Functions 前身）、`saku-chatops-slack/lambda_function/start-stepfunctions-state-machines/template.yaml`（chatops async 啟動）

---

## Core Methodology（6 Production Patterns）

### Pattern 1 — Saga（分散式交易）

- **What**: 多服務長事務無中央協調；某步失敗走 compensating actions
- **Why**: streaming event 涉及轉碼 / 儲存 / 索引 / 計費；失敗需回滾比手工重試少 50% 複雜度
- **Gotcha** [KKStream]: Compensation 必須**冪等**；轉碼後儲存無法刪除（存檔成本）→ 改「標記廢棄」；新人常忽略 compensation 層 → 孤兒資源堆積

### Pattern 2 — Callback + Token（等外部事件）

- **What**: Task 給外部系統（GPU 轉碼農場）不 polling；狀態機停止監聽 SQS/SNS callback token
- **Why**: Polling 每秒 check = 不必要 API 成本；改事件驅動只在結果回來時喚醒
- **Gotcha** [KKStream]: Callback token 預設 timeout 1hr，轉碼可達 3–5hr → 參數化 timeout 或分段；回錯誤 token 時無法區分「真失敗」vs「超時」→ 加 error code 層
- **演進路徑**：KKStream 早期用 AWS SWF heartbeat（`videopass-encoding-system-worker/jack/core.py`）— Worker 每 30s 向 SWF Activity Task 發 heartbeat，heartbeat 失敗超過 max_retry 就 terminate 整個 process（非 task）。SWF 已停用後應遷移到 Step Functions callback pattern + SNS token

### Pattern 3 — Map State（平行 fan-out）

- **What**: 批次（manifest 含 100 個 segments）→ Map 自動展開為並行任務
- **Why**: 順序處理需 100× 時間；Map max concurrency 可調，成本 vs 速度 trade-off
- **Gotcha** [KKStream]: concurrency 太高 ECS pod evicted；太低隊列堆積；實戰 concurrency = **ECS cluster CPU cores × 1.2**；Map timeout 是整個 loop 時間非單筆

### Pattern 4 — Express vs Standard Workflow

- **What**: Express（< 5 min，高頻，低成本）vs Standard（1 year，審計軌跡，高成本）
- **Why**: 選型錯誤 = KKStream 早期成本爆表主因；Standard 按 state transition 計費（每 4KB 區塊）、Express 按執行時間（1M 次 $1）
- **Gotcha** [KKStream]: 7 分鐘流程誤用 Standard；Map 內每 iteration 都算 transition（100 元素 × 10 step = 1000 transitions → 幾萬 USD/月 [需確認]）

### Pattern 5 — Nested Workflow + Retry Policy

- **What**: 狀態機呼另一個狀態機（nested）+ exponential backoff retry
- **Why**: 複雜邏輯拆小機 → 提高重用；retry 自動化取代 app-layer 手工 retry
- **Gotcha** [KKStream]: Nested workflow 超時不自動傳播父機；retry backoff 預設 2s–3600s，streaming 場景常需**更短**（100ms 重試 transient network error）
- **ChatOps 的特殊需求**：`saku-chatops-slack` 啟動 Step Functions 的 Lambda timeout 只有 10s，state machine 執行超過 10s 時 Lambda 已結束 → 必須非同步 StartExecution（先回 Slack ack），結果透過 SNS/webhook 回呼，不能同步等 state machine 完成

### Pattern 6 — Observability + X-Ray

- **What**: Step Functions 原生 X-Ray；每 state 執行時間 / 錯誤 / 重試自動記錄；CloudWatch Logs Insights 查複雜路徑
- **Why**: streaming 複雜度高需秒級找瓶頸
- **Gotcha** [KKStream]: X-Ray 預設只記 full duration 不記 state 內 Lambda cold start → 要 Lambda 層自己記；Logs Insights 查詢 timeout → 預過濾（只記 slow > 30s）

---

## Concrete Numbers

| 指標 | 值 | 備註 |
|------|----|------|
| Standard state transition cost | $0.000025 / transition | 100 state workflow × 1000 exec/day = $2.5 |
| Express 執行計費 | $1 / 1M executions | < 1 min ≈ $0.00001 |
| State data 上限 | 32,768 chars | 超過自動 fail；大 payload 用 S3 indirect |
| Max execution history | 25,000 events | 含每 state entry/exit/retry；拆 nested 減深度 |
| Map max concurrency | 無上限（無設時）| 建議 = ECS CPU cores × 1.2 [需 Zeuik 確認 KKStream 實際] |
| Callback token 預設 timeout | 3600s (1hr) | 可客製至 max 1yr |
| Express 執行 timeout | 5 min | Hard limit |
| Standard 執行 timeout | 1 year | Configurable |
| Cold start（Express）| 100–500 ms | vs Standard 50–100 ms |

> [需 Zeuik 確認] KKStream 月度 Step Functions 成本、實際 manifest 平均元素數、轉碼平均時間

---

## SWF → Step Functions 演進路徑（KKStream 實戰）

| 層 | 舊架構（SWF）| 新架構（Step Functions）|
|----|------------|----------------------|
| 協調 | SWF Activity Task | Step Functions Standard/Express |
| Worker 存活確認 | heartbeat API 每 30s | Callback token + SNS |
| Worker 失敗處理 | heartbeat fail N 次 → terminate process | State machine Retry + Catch |
| 平行化 | 手動 SQS fan-out | Map state（concurrency 可調）|
| 可觀測性 | CloudWatch Logs | X-Ray + Logs Insights |
| 成本模型 | Activity/Decision 各計費 | Express < Standard（用對才便宜）|

**遷移 Gotcha**：SWF Worker heartbeat timeout 是 process-level（整個 worker 死掉），Step Functions 的 heartbeat timeout 是 task-level（只有該 task fail，可 retry）— 遷移時需重新設計 failure granularity。

---

## Anti-patterns

1. **短流程用 Standard（浪費 transition 成本）**
   - 問題：5 分鐘流程誤用 Standard，每 transition 都計費
   - KKStream 踩坑：7 分鐘流程誤 Standard，應拆 Express × nested 或單 Lambda，省 90%

2. **所有業務邏輯塞進 ASL**
   - 問題：ASL 不支援迴圈（只 Map）、無 local variable，複雜邏輯像正則
   - 解：Lambda 預處理後傳狀態機

3. **沒用 Callback Pattern → 輪詢 Lambda**
   - 問題：Lambda 內每 10s 問一次「轉完了嗎」，1hr = 360 次 Lambda 計費
   - 解：原生 Callback + SQS，轉碼農場 SNS 推 token 喚醒

4. **Large payload 塞 state data**
   - 問題：Video manifest（MB 級）作 input，每 transition 都傳一遍，state size > 32KB 爆
   - 解：Manifest 存 S3，state 只傳 S3 URI

---

## Decision Tree

```
需要自動化工作流？
├─ < 3 steps + < 1 min → 純 Lambda
├─ 3–10 steps + < 5 min + 高頻 → Express Workflow
│  ├─ 平行化 → Map + concurrency = CPU cores × 1.2
│  └─ transient error → Retry + exponential backoff（100ms 基礎）
├─ > 10 steps OR > 5 min OR 需審計（金融）→ Standard
│  ├─ 成本敏感 → 評估拆 nested Express
│  ├─ 外部系統耗時（轉碼）→ Callback + token
│  └─ 觀測 → X-Ray + CloudWatch Logs Insights
└─ 分散式交易（多服務一致性）→ Saga + compensation
```

---

## References

- 職涯段：`raw/career-summary.md#4-kkstream--kkcompany--sre--devops--dba--architect`
- [AWS Step Functions docs](https://docs.aws.amazon.com/step-functions/)
- [Step Functions Pricing](https://aws.amazon.com/step-functions/pricing/)
- [Callback Pattern Guide](https://docs.aws.amazon.com/step-functions/latest/dg/connect-parameters.html#connect-wait-token)
- [AWS Well-Architected Serverless Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/)
- 關聯：[[kafka-confluent-streaming]]、[[finops-savings-plans-roi]]、[[sre-oncall-training-program]]、[[aws-alarm-as-code]]
- Code source: `saku-chatops-slack/`、`videopass-encoding-system-worker/jack/core.py`（local only）
