# SRE Oncall 訓練計畫

> **Source positions**: KKStream / KKCompany 2019–2021（SRE + DevOps + DBA + Architect）
> **Last ingested**: 2026-04-26（CathaySec SRE 訓練時程補充）
> **Confidence**: high（Zeuik 在 KKStream 建立 SRE oncall 文件與訓練計畫；CathaySec SRE Lead 直接設計）
> **Linted**: 2026-04-26

---

## Context

KKStream 影音串流服務（Saku/TFC 等）對可用性要求高，oncall 工程師需要在深夜或假日快速判斷並處置告警。Zeuik 負責建立「SRE oncall 文件 + 訓練計畫」，目標是讓新工程師在 4–8 週內達到**獨立值班**的能力，並讓老手 oncall 告警量降低 50%。

---

## Core Methodology

### Step 1 — Runbook 設計（Actionable，非 Wiki）

- **What**: 每個告警對應一份 runbook，包含：觸發條件、初步 check list（3–5 個指令）、升級閾值（何時叫醒 lead）、預期解決時間
- **Why**: Oncall 工程師在凌晨告警時，大腦 context 為零；runbook 不是解釋「這個系統是什麼」，而是「接下來做什麼」
- **Gotcha** [KKStream]: 初版 runbook 寫得像教學文件（長達 10 頁，有背景介紹），oncall 遇到問題沒時間看完；改為「決策樹 + 3 個 check 指令」格式，MTTR 縮短 30%

### Step 2 — Oncall Schedule 設計

- **What**: 輪班制（每人每週一輪）；primary + secondary 雙層（primary 先接，15 分鐘未回應升 secondary）；值班行事曆整合到 PagerDuty / OpsGenie
- **Why**: 單人 oncall 無 backup 導致疲勞累積和 burnout；primary/secondary 制度讓每個人知道自己的角色，減少「這誰負責」的模糊地帶
- **Gotcha** [KKStream]: 台灣公司常見問題：非正式文化下 oncall 等於「有空的人接」，責任不清 → 導致高壓工程師永遠值班、新人不參與；明確 schedule + 輪班制才解決

### Step 3 — 告警品質管理（Alarm Tuning → Alarm as Code → Auto-Remediation）

- **What**: 分析過去 3 個月告警歷史：哪些是 actionable（需要人處理）、哪些是 noise（自行恢復）；noise 告警 suppress 或降級（從 pager 改 Slack notify）；與 R&D 合作修復根因
- **Why**: KKStream 透過 Lambda 智慧告警系統 + R&D 合作，**告警量降低 50%**；噪音告警讓人麻木（alarm fatigue），真實事故反而被忽略
- **Gotcha** [KKStream]: 降告警量的阻力來自「萬一降了就漏掉真實問題」的恐懼；解法是**先只調閾值或 suppress 重複告警**，不直接刪除；觀察 2 週確認沒有漏報才正式移除
- **KKStream 的告警進化三階段**：
  1. **手動管理** → 每次手動 create/update CloudWatch alarm（散亂、不一致）
  2. **Alarm as Code**（`aws-alarm-police`）→ YAML 定義 + Lambda 定期執行，告警規則與 IaC 同等管理，見 [[aws-alarm-as-code]]
  3. **Auto-Remediation**（`saku-chatops-slack/alarm-automation`）→ alarm 符合特定 pattern 時自動啟動 Step Functions state machine 執行補救腳本（如 RDS CPU 高 → auto scale），oncall 只需處理 state machine 無法自動修復的問題
- **Runbook = State Machine 視覺化**：簡單 runbook 可直接編碼成 Step Functions（決策樹 → Choice state），複雜 runbook 拆成 Lambda + Step Functions 組合。此設計讓 runbook 可測試、可驗證、可審計

### Step 4 — 新人 Oncall 訓練計畫（Junior / Senior 雙軌）

KKStream SRE onboarding 依資歷分為兩條軌道，共同目標相同（獨立值班），但節奏不同。

#### Junior 軌（3 個月）

| 月份 | 重點 | 說明 |
|------|------|------|
| **第 1 個月** | 技能培養 | 閱讀系統文件、runbook、架構圖；跟著 lead 觀察日常維運（Shadow 模式）；無值班責任 |
| **第 2 個月** | 白天實作與值班 | 白天獨立處理維運操作；進入 Reverse Shadow 模式——新人主操作，lead 在旁 standby；只排白天班，不排夜間告警 |
| **第 3 個月** | 完整值班和維運（含晚上）| 加入夜間 oncall rotation；lead 降為 secondary；進入 Solo 模式 |

- **Why**: Junior 需要較長的「無壓力技能建構期」（第 1 個月）才能在值班壓力下正確判斷；直接跳到 reverse shadow 會讓人緊張無法語言化決策
- **Gotcha** [KKStream]: Reverse shadow 階段新人有時因緊張不說出決策過程，lead 直接接手 → 退回 shadow 模式；需要主動問「你現在打算怎麼做？」引導語言化

#### Senior 軌（1 個月，4 週）

| 週次 | 重點 | 說明 |
|------|------|------|
| **第 1 週** | 閱讀文件 | 精讀 runbook、架構圖、告警定義、SLO；不值班、不操作；有疑問直接找 lead 討論 |
| **第 2 週** | 參與日常維運和開發 | 跟 lead 一起處理白天維運與 sprint 任務；了解工具鏈與告警處置流程 |
| **第 3 週** | 實際值班和維運（含晚上）| 進入正式 oncall rotation，包含夜間；lead 為 secondary |
| **第 4 週** | 回饋與文件修訂 | 根據前三週值班體驗，回饋 runbook 不準確、流程死角；直接修訂文件（Senior 修訂 = 知識傳承，見 CathaySec 迭代框架）|

- **Why**: Senior 已具備背景知識與壓力下決策經驗，壓縮技能培養期；第 4 週的文件修訂讓 Senior 的到位同時強化 team 知識庫（雙贏）
- **Gotcha** [KKStream 推論]: Senior 軌的第 1 週易被跳過（「Senior 還需要看文件？」），但跳過後第 3 週夜間值班常出現「我以為系統架構是 X」的誤判；強制要求第 1 週文件閱讀

### Step 5 — Postmortem 文化建立

- **What**: 每個 P1/P2 事故 48 小時內完成 blameless postmortem，包含：事故時序（timeline）、根本原因（5-Why）、改善行動（有負責人 + deadline）；每月分享會討論當月 postmortem
- **Why**: Postmortem 的目的是防止同樣事故重發，不是找人背鍋；Blameless 文化讓工程師願意說實話；每月分享讓知識在團隊擴散
- **Gotcha** [KKStream]: Action items 常在 postmortem 寫完就沒人 follow up；改為 action items 直接開 Jira ticket 並 assign，每兩週 check-in

### Step 6 — SLO / Error Budget 作為決策基準

- **What**: 為每個服務設定 SLO（例如 availability 99.9% / 月）；計算 error budget 消耗速率；error budget 快耗盡時暫停功能發布，專注穩定性
- **Why**: 沒有 SLO 的 oncall 是無限責任（任何問題都要處理）；有 SLO 才能說「這個問題在 error budget 內，可以等白天處理」，保護工程師睡眠
- **Gotcha** [KKStream 推論]: 初期 SLO 設太嚴（99.99%）導致 error budget 幾乎為零，等於回到無限責任狀態；建議從 99.5–99.9% 開始，熟悉後再調緊 [需 Zeuik 確認 KKStream 實際 SLO 數字]

---

## CathaySec 實作補充（2025 培訓簡報萃取）

### 異常通報升級鏈

```
異常發生
  ↓
SRE 第一動作：先讓系統恢復正常（不是先找原因）
  ↓
收集：系統異常 Log + 監控指標截圖
  ↓
升級：SRE → 架構師（視情況找 AP 團隊負責人）→ 各單位主管
  ↓
記錄：異常處理內容 + 各時間點（符合公司異常處理回應時間規定）
  ↓
事後：異常討論 + 再優化（Postmortem）
```

**金融業特殊要求**：
- 異常處理時間點（發現、通報、處置、恢復）都要記錄，確保符合公司 SLA 回應時間規定
- 截圖留存（非選項）：監控指標截圖和處置步驟必須保存，方便事後異常追蹤與 audit

### CathaySec SRE 人才培育三大指標

1. **雲端監控指標**：能看懂並解釋每個 dashboard 指標代表什麼（不只是數字，要知道業務意涵）
2. **異常處理紀錄**：能獨立完成異常事件記錄，時序清楚、有截圖、有處置說明
3. **異常通報流程標準化**：知道何時升級、升給誰、如何記錄

### 雲端技能三主軸（CathaySec 版）

| 主軸 | 培訓目標 | 對應 GCP 服務 |
|------|---------|-------------|
| 主機 | Serverless 優先，了解 Cloud Run 預設指標 | Cloud Run、Compute Engine |
| 資料庫 | Cloud SQL 預設指標、各資料庫基本指標建立告警 | Cloud SQL |
| 網路 | VPN Tunnel 斷線告警與監控（金融業 hybrid 特殊需求）| Cloud VPN |

### CathaySec SRE 訓練時程（3 個月）

| 月份 | 重點 | 說明 |
|------|------|------|
| **第 1 個月** | 熟悉金融業規範 / 了解 Landing Zone | 閱讀 FSC 相關法規、公司 IS policy；了解 GCP Landing Zone 架構（Org Policy、VPC、IAM 層次）；不參與變更、不值班 |
| **第 2 個月** | 參與定期會議 / SIT 開發實作 / IaC 工具 / 撰寫 SOP | 開始出席 sprint / 架構 / 變更會議；投入專案 SIT（System Integration Test）開發與實作；學習 Terraform 等 IaC 工具並動手寫；**同步撰寫 SOP 文件**（趁剛學最能察覺文件空白）|
| **第 3 個月** | 參與變更審查會議 / 值班和日常維運 / 完善 SOP | 正式進入 change review 流程（金融業特有：每次生產環境變更需審查簽核）；加入 oncall rotation（日間為主）；根據前兩個月實際操作經驗完善並修訂 SOP |

- **Why**: 金融業 SRE 不能繞過合規知識直接上手維運 — 第 1 個月的規範理解是後續所有操作（Landing Zone 設計、Terraform 寫法、變更審查）的心智框架；跳過會導致後來發現操作不符合稽核要求需要大幅整改
- **Why（SOP 在月 2 而非月 3 寫）**: 剛學會一個東西時是最好的文件作者 — 知道哪裡卡關、哪裡需要解釋；等到月 3 熟悉後反而覺得「這很理所當然」而漏寫；月 2 寫初稿、月 3 精修是最有效的分工
- **Gotcha** [CathaySec]: 變更審查會議（月 3）對工程師是陌生流程 — 很多人第一次被問「這個變更的回滾計畫是什麼」會不知道如何回答；建議月 2 就旁聽幾次變更審查，熟悉問題格式再正式參與

**與 KKStream 方法論對照**：
- KKStream 重點：**runbook 設計 + shadow 訓練 + alarm tuning**（scale 大、服務複雜，技術技能優先）
- CathaySec 重點：**合規脈絡建立 + IaC 落地 + 變更審查流程 + SOP 文件化**（金融監管、稽核需求驅動）
- 共通核心：從**監控起手**，唯有充分了解監控的意思才能知道維運要處理什麼
- 關鍵差異：CathaySec 月 1 強制「先了解為何要這樣做」，KKStream 月 1 是「先學怎麼做」——金融業的稽核風險讓順序不能翻轉

### 定期 On-call 的迭代價值（CathaySec 框架）

> 「從定期 On-call 可反覆驗證 SOP 文件準確度，運用敏捷迭代可逐步完善文件內容，方便累積為團隊知識庫」

- 每次 on-call 事件 = 一次 SOP 驗證機會
- SOP 不準確 → 更新文件 → 下次 on-call 更快
- 時間軸：異常處理 SOP → 累積 → 系統架構設計 + 軟體開發設計的參考依據

---

## Concrete Numbers

| 指標 | 值 | 來源場景 |
|------|----|---------|
| 告警量降低 | **50%** | KKStream Lambda 智慧告警 + R&D 合作 |
| Oncall 訓練週期（KKStream Junior → 獨立值班）| **3 個月** | 技能培養 → 白天值班 → 完整值班含夜間 |
| Oncall 訓練週期（KKStream Senior → 獨立值班）| **1 個月（4 週）** | 文件閱讀 → 日常維運 → 完整值班 → 回饋修訂 |
| Oncall 訓練週期（CathaySec SRE → 參與值班）| **3 個月** | 合規規範 → SIT + IaC + SOP → 變更審查 + 值班 |
| Runbook 長度目標 | < 1 頁（A4）| 決策樹 + 3–5 個 check 指令 |
| Postmortem 完成時限 | 48 小時內 | P1/P2 事故 |
| Primary 升 Secondary 等待時間 | 15 分鐘 | PagerDuty escalation policy |
| Error budget（99.9% SLO）| 43.2 分鐘/月 | 標準計算 |
| 每人值班頻率 | [需 Zeuik 確認] | KKStream SRE 團隊規模 |
| KKStream SRE 團隊規模 | [需 Zeuik 確認] | 影響 oncall rotation 密度 |

---

## Anti-patterns（不要做）

1. **Runbook 寫成 Wiki（背景知識型）**
   - 問題：凌晨告警時沒時間看 10 頁教學文件；大量背景知識讓人找不到「現在要執行什麼指令」
   - 何時踩：KKStream 初版 runbook 被工程師抱怨「太長看不完」，改成 1 頁決策樹後 MTTR 縮短 30%
   - 解：Runbook = 流程圖 + 指令；背景知識放 Wiki（不同文件）

2. **Oncall 不輪班（讓「最懂的人」永遠值班）**
   - 問題：單人 oncall 知識不分享；那個人離職後系統無人維護；過勞 burnout
   - 解：強制輪班；用 Shadow 計畫確保知識轉移；「最懂的人」變成 secondary 兜底而非 primary

3. **Postmortem 找原因卻不追蹤 action item**
   - 問題：postmortem 寫了 5 個 action items，3 個月後 follow up 全都沒做；同樣問題再次發生
   - 解：postmortem action item 直接開 ticket 並 assign；技術 lead 的週會固定 review 未完成 action items；postmortem 品質計入 team KPI

---

## Decision Tree

```
建立 SRE Oncall 計畫，從哪裡開始？

現狀評估
├─ 沒有 on-call → 先從 runbook + schedule 開始（不要一步到位）
├─ 有 oncall 但無文件 → 先 runbook（最高 ROI）
└─ 有文件但告警太多 → 先 alarm tuning（降 noise）

Runbook 優先建哪些？
├─ 過去 3 個月最高頻告警 Top 5 → 優先
├─ 影響用戶的 P1/P2 服務 → 優先
└─ 不常觸發但影響大 → 次優先

新人訓練計畫選擇
├─ 資歷 < 3 年 SRE / 從未做過 oncall → Junior 軌（3 個月）
│   ├─ 月 1：技能培養（文件 + Shadow 觀察，無值班）
│   ├─ 月 2：白天實作與值班（Reverse Shadow，不含夜間）
│   └─ 月 3：完整值班含夜間（Solo，lead 為 secondary）
├─ 資歷 3 年以上 / 有 oncall 經驗 → Senior 軌（1 個月）
│   ├─ 週 1：閱讀文件（runbook + 架構 + SLO）
│   ├─ 週 2：參與日常維運和開發
│   ├─ 週 3：完整值班含夜間
│   └─ 週 4：回饋與 runbook 修訂
└─ 金融業 / 高合規環境（如 CathaySec）→ 合規優先軌（3 個月）
    ├─ 月 1：熟悉金融業規範 + Landing Zone（不參與變更）
    ├─ 月 2：SIT 開發 + IaC 工具 + 撰寫 SOP（出席會議）
    └─ 月 3：變更審查 + oncall + 完善 SOP

SLO 設定
├─ 第一次設 SLO → 從現有 availability 往下 1–2 個 9 設定（保守）
├─ 服務有 99.9% 可能性 → 99.5% 當 SLO，留 buffer
└─ 金融 / 醫療等高合規 → 99.9%+ 但要相應的 on-call 人力預算
```

---

## References

- 職涯段（KKStream）：`raw/career-summary.md#4-kkstream--kkcompany--sre--devops--dba--architect`
- 職涯段（CathaySec）：`raw/career-summary.md#8-cathaysec-國泰證券--sre-lead--manager-current`
- [Google SRE Book — Oncall chapter](https://sre.google/sre-book/being-on-call/)
- [Google SRE Book — Postmortem Culture](https://sre.google/sre-book/postmortem-culture/)
- [PagerDuty Incident Response Docs](https://response.pagerduty.com/)
- [SLO / Error Budget Primer (Google)](https://cloud.google.com/blog/products/management-tools/sre-error-budgets-and-the-consequence-of-missing-them)
- 關聯：[[kkstream-lessons]]、[[aws-step-functions-patterns]]、[[finops-savings-plans-roi]]、[[gcp-monitoring-alerting]]、[[cathaysec-lessons]]、[[aws-alarm-as-code]]
