# AWS Alarm as Code — KKStream 告警即代碼架構

> **Source positions**: KKStream / KKCompany 2019–2021（SRE + DevOps）
> **Last ingested**: 2026-04-22（from KKStream_Code codebase analysis）
> **Confidence**: high（直接從 aws-alarm-police、videopass/tfc/saku/prism-lambda-system-alarm-police 代碼提煉）
> **Linted**: 2026-04-22

---

## Context

KKStream 管理 Videopass、Telasa、TFC 三個平台，各有獨立的告警 Lambda（prism/videopass/tfc 各自一套）。早期手動管理 CloudWatch alarm 造成規則不一致、閾值靠直覺、新增資源不自動建立告警。

**alarm-police 框架**解決這個問題：**告警定義 = YAML 配置 + Lambda 定期執行**，達成：
- 告警量降低 50%（降噪 + threshold override）
- 新資源自動建立告警（Lambda 掃描現有資源對照規則）
- 告警規則版本化（YAML in git）

---

## Core Architecture（雙層設計）

### Layer 1 — 告警定義層（alarm_default_setting.yml）

每個 namespace（AWS/ELB、AWS/RDS、AWS/EC2 等）定義預設告警規則：

```yaml
AWS/ELB:
  LatencyCritical:
    MetricName: Latency
    Namespace: AWS/ELB
    Threshold: 1.0                # 預設 threshold
    Statistic: Average
    AlarmActions: arn:aws:sns:...:p0-videopass-system-alarm
    Period: 60
    EvaluationPeriods: 3
    Environment:
      - prod
      - production
    CustomParameters:             # regex pattern override
      - RegexPattern: ^vp-prod-nodejs-api$
        Threshold: 5.0            # 特定服務寬鬆閾值（避免 false positive）
        EvaluationPeriods: 10
      - RegexPattern: ^videopass-production-demo-api$
        AlarmActions: arn:...:p1-videopass-system-error  # 降級到 p1
```

**CustomParameters 是核心**：同一個 metric，不同服務不同 threshold + 不同 SNS topic（severity 路由）。避免每個服務手動維護告警。

### Layer 2 — 過濾層（filter.yml）

環境隔離 + region 選擇：

```yaml
environment_patterns:
  prod:
    - "^vp-prod-"
    - "^videopass-production-"
  stag:
    - "^vp-stag-"
regions:
  - ap-northeast-1
```

只在符合 pattern 的環境建立告警，dev/test 資源不被誤建生產告警。

---

## Execution Flow（main.py 執行邏輯）

```
[Lambda 定期排程（monthly / weekly）]
    ├─ 載入 alarm_default_setting.yml + filter.yml
    ├─ 拉取所有 AWS 資源名稱：
    │   ├─ EC2 instance names（tag-based）
    │   ├─ ELB load balancers
    │   ├─ RDS instances
    │   ├─ ElastiCache clusters
    │   └─ ECS services
    ├─ for each resource:
    │   ├─ match environment pattern（filter.yml）
    │   ├─ match custom parameter regex（alarm_default_setting.yml）
    │   ├─ override threshold / evaluation periods / alarm actions
    │   └─ create / update CloudWatch alarm
    ├─ DeleteAlarms（舊資源清理，避免 alarm 孤兒）
    └─ publish summary to Slack
```

**結果**：每次 Lambda 執行後，所有資源的告警狀態與 YAML 定義完全一致。新增 EC2/RDS 下次執行就自動有告警。

---

## Auto-Remediation 延伸（alarm-automation）

告警品質管理的下一步：符合特定 pattern 的告警不只通知，而是直接自動補救。

```python
# saku-chatops-slack/lambda_function/alarm-automation/src/main.py

def alarm_handler(event, context):
    for record in event.get('Records', []):
        alarm = json.loads(record['Sns']['Message'])

        # Case: RDS CPU 高 → 自動啟動 Step Functions 補救
        if (alarm.get('NewStateValue') == 'ALARM'
                and alarm.get('AlarmName', '').startswith('auto ')
                and 'AWS/RDS' == jmespath.search('Trigger.Namespace', alarm)
                and 'CPUUtilization' == jmespath.search('Trigger.MetricName', alarm)):

            rds = jmespath.search('Trigger.Dimensions[?name==`DBInstanceIdentifier`].value | [0]', alarm)
            arn = StepFunctionStateMachine(STATEMACHINE_ARN).start_execution({'rds': rds})
            logger.info(f'Start state machine execution {arn}')
            return

        logger.warning(f'not matched alarm: {alarm}')  # 不拋 exception，避免循環
```

**設計要點**：
- 只有告警名稱以 `auto ` 開頭才觸發補救（明確 opt-in）
- 用 jmespath 查詢 nested dict（比 try/except key access 更安全）
- unmatched alarm log warning 而非 exception（避免 Lambda retry 造成重複補救）

---

## Concrete Numbers

| 指標 | 值 | 備註 |
|------|----|------|
| 告警量降低 | **50%** | KKStream 實績（alarm-police + R&D 合作） |
| CustomParameters 作用 | threshold override + SNS topic routing | 同一 namespace 不同服務不同嚴重度 |
| Lambda 執行頻率 | monthly（可調） | 足以覆蓋新資源建立週期 |
| 支援 namespace 數 | AWS/ELB、AWS/RDS、AWS/EC2、AWS/ECS、AWS/ElastiCache | 可擴展 |
| 告警孤兒清除 | 自動（DeleteAlarms） | 服務下線後不留殭屍 alarm |

---

## SNS Topic 分級路由（p0 / p1）

```
p0-videopass-system-alarm  → PagerDuty（立即叫醒 oncall）
p1-videopass-system-error  → Slack #sre-alerts（上班時段處理）
```

**CustomParameters 中的 AlarmActions override** 讓同一個 metric 在不同服務有不同 severity：
- API gateway latency 5s → p0
- demo/staging API latency 5s → p1
- 一份 YAML 表達完整的 severity policy

---

## Anti-patterns（不要做）

1. **各服務各自手動建告警**
   - 問題：50 個服務 = 50 個地方要維護 threshold；新人搞不清哪個 threshold 對
   - 解：集中 YAML，變更有 git review

2. **閾值全部相同（一刀切）**
   - 問題：vp-prod-nodejs-api latency threshold 1s 正常服務是 OK 的，但某些後端 API 本來就慢
   - 解：CustomParameters regex override，例外規則明文化

3. **告警補救直接刪 resource**
   - 問題：auto-remediation 誤判，把 production DB 刪掉
   - 解：補救 state machine 只做保守操作（scale / restart / notify），不刪資源

4. **多平台各自獨立 alarm-police**
   - 問題：KKStream 有 videopass/tfc/saku/prism 四套，規則很難保持一致
   - 解：應統一 alarm-police 框架 + 中央 SNS routing（這個 KKStream 當時沒做到）

---

## Decision Tree

```
需要管理 CloudWatch alarms？

資源數量
├─ < 20 個資源 → 手動 + Terraform resource 可行
└─ > 20 個資源 → alarm-police 框架（否則維護地獄）

告警定義複雜度
├─ 所有資源同一 threshold → 簡單 YAML，無 CustomParameters
└─ 不同服務不同 threshold → CustomParameters regex override

自動補救
├─ 補救腳本 < 5 步 + 明確可逆 → State Machine（Choice state + retry）
├─ 補救步驟複雜 + 需人工確認 → State Machine 執行到 Human Approval 步驟再暫停
└─ 未知服務 / 不確定補救方式 → 只通知，不自動補救（safer default）
```

---

## Cross-references

- 關聯：[[kkstream-lessons]]、[[sre-oncall-training-program]]、[[aws-step-functions-patterns]]

## References

- Code source: `aws-alarm-police/`、`videopass-lambda-system-alarm-police/alarm_default_setting.yml`、`saku-chatops-slack/lambda_function/alarm-automation/`（local only，未公開）
- 職涯段：`raw/career-summary.md#4-kkstream--kkcompany--sre--devops--dba--architect`
