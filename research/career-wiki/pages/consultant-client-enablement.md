# 技術顧問的客戶賦能（Client Enablement）

> **Source positions**: Resolve Technology 2021–2022（Lead DevOps + Consultant）
> **Last ingested**: 2026-04-21
> **Confidence**: high（Zeuik 在 Resolve 兼任 consulting track，直接交付文件、訓練與 stakeholder 管理）
> **Linted**: 2026-04-21

---

## Context

技術顧問與純工程師的差異在於：**工程師交付 code，顧問交付能力（capability）**。Resolve 的 consulting 工作包含幫多個客戶設計 IaC 架構、撰寫技術文件、執行 hands-on training、管理跨時區 stakeholder。這頁記錄「讓客戶能自己跑」（enablement）的 SOP，以及顧問角色特有的時間與知識管理挑戰。

---

## Core Methodology

### Step 1 — Onboarding Playbook 優先於 Ad-hoc Help

- **What**: 每個新客戶或新技術主題，先建立 onboarding playbook（20–40 頁）：背景說明、環境設定、常見操作、FAQ、Gotcha 清單
- **Why**: Ad-hoc help 線性擴展（顧問時間 = 客戶問題數量）；playbook 讓客戶能自己查，顧問時間從解答移到審查
- **Gotcha** [Resolve]: 初期沒有 playbook，每個新客戶都從頭講同樣的 Terraform 基礎；累積 10 個客戶後顧問自己成了瓶頸；改為「先出 playbook 版本 1，再迭代」後，onboarding 效率提升 3x

### Step 2 — 文件分層：Operation vs Reference vs Tutorial

- **What**:
  - **Tutorial**（入門導引）：手把手，有 screenshot，給剛接觸的工程師
  - **How-to**（操作 SOP）：解決特定任務，假設讀者有基礎，對照操作用
  - **Reference**（完整說明）：API 參數、設定選項、完整清單，查詢用
- **Why**: 同一份文件試圖同時兼顧三種讀者會讓所有人都不滿意；分層後讀者找到對應文件，理解成本大幅下降
- **Gotcha** [Resolve]: 常見錯誤是「教學型文件+完整 reference」混在同一份，前半部 tutorial、後半部 API reference；初學者看到 reference 就放棄，進階用戶略過 tutorial 浪費時間

### Step 3 — Training 設計：動手 > 講投影片

- **What**: 每場 training 最多 40% 講解 + 60% hands-on lab；lab 用真實客戶環境（或 sandbox 複製），操作真實問題
- **Why**: 講 Terraform 不如讓工程師自己 `init / plan / apply` 一次；記憶留存率 10%（聽）vs 75%（做）
- **Gotcha** [Resolve]: 客戶工程師環境（OS 版本、network policy、proxy）千奇百怪；hands-on lab 前 1 天要求統一檢查清單（tool version、auth 驗證），否則 training 當天 30% 時間在解 env issue，而不是學內容

### Step 4 — 跨時區 Stakeholder 管理

- **What**: 每個工作項目明確設定：owner（決策者）、reviewer（技術把關）、informed（知情不決策）；所有決定在 async 工具（Confluence / Notion / GitHub comment）留下書面記錄
- **Why**: 跨時區 4–8 小時的顧問合作，一個問題口頭討論然後沒書面 → 下次見面雙方記憶不同；書面記錄是唯一的 source of truth
- **Gotcha** [Resolve]: Reviewer 可用性是瓶頸（每個 cloud provider 要對應的 reviewer，時差 4–8hr 核准等待）；改為「先讓客戶 reviewer 在 PR comment 非同步 review」 → 等待時間從 4–8hr 降到 1–2hr（可在自己工作時間處理）

### Step 5 — ROI 量化與報告

- **What**: 每季一份 consulting deliverable 報告：已完成事項 + **量化成果**（環境數量 / 自動化節省時數 / 事故降低數）；用客戶的語言（business impact），不用顧問的語言（技術細節）
- **Why**: 顧問合約續約決定者是 PM / 業務，不是工程師；他們看的是 ROI，不是 Terraform module 設計有多優雅
- **Gotcha** [Resolve]: 顧問常認為「工作品質好，客戶自然知道」；實際上需要主動報告（proactive communication）；沒有報告等於沒做

### Step 6 — 知識轉移完成條件（Exit Criteria）

- **What**: 確認客戶能獨立操作的標準：能回答 3 個情境問題（不靠顧問）+ 能 trace 一個 incident 到根因 + 有一個內部人員能 on-call
- **Why**: 顧問工作若沒有明確 exit criteria，容易無限延伸（客戶永遠有新問題）；清楚的標準讓雙方知道「顧問任務完成」
- **Gotcha**: 客戶常說「我們學會了」但實際沒有；改為 **role reversal**：讓客戶工程師向其他同事教一遍（教學即是最佳學習驗證）

---

## Concrete Numbers

| 指標 | 值 | 來源場景 |
|------|----|---------|
| Onboarding playbook 長度 | 20–40 頁 | Resolve multi-cloud onboarding |
| 有 playbook 後 onboarding 效率提升 | 3x | vs ad-hoc help |
| Training 動手比例 | 60% hands-on | Resolve 客戶 training |
| Reviewer 等待時間（非同步 PR review）| 1–2 小時 | vs 口頭等待 4–8hr |
| 季度報告完成事項 | 5–10 deliverables | Resolve 每季 |
| 顧問合約平均長度 | [需 Zeuik 確認] | Resolve 客戶 |
| 服務客戶數（同期）| [需 Zeuik 確認] | 多客戶並行 |

---

## Anti-patterns（不要做）

1. **每次客戶問問題都直接回答（不建立 self-service）**
   - 問題：顧問時間線性消耗；客戶沒有學到獨立解決的能力；合約結束後客戶仍無法自立
   - 解：「Teach to fish」模式：回答問題前先問「你試過查哪裡？」，引導客戶建立自查習慣；同類問題第 3 次出現就寫進 playbook FAQ

2. **Scope Creep 沒有管控（顧問做了 engineer 的工作）**
   - 問題：客戶 engineer 遇到問題直接請顧問來解決，顧問成了外包工程師；consulting 費用燒完但客戶沒有能力提升
   - 解：合約明確寫 engagement type（advisory vs implementation）；implementation 工作由客戶 team 執行，顧問 review；口頭追加的工作要 change request

3. **技術導向的 update（每週講部署了什麼）**
   - 問題：業務方 stakeholder 不懂 Terraform module 細節，溝通成本高，且看不出 value
   - 解：改用 outcome 語言：「這週完成了 3 套環境自動化，預計省 N hr/月的手動操作」

---

## Decision Tree

```
顧問交付物類型決策

客戶問的是「怎麼做 X？」
├─ 同樣問題 ≥ 3 次 → 寫進 playbook / FAQ
├─ 複雜操作 → 建立 How-to SOP（step-by-step）
└─ 新服務 → Tutorial（從零開始，含 screenshot）

Training 設計
├─ 入門人員（0 經驗）→ Tutorial 先讀 + 全 hands-on lab
├─ 有經驗工程師 → How-to + 30% 講解 + 70% lab
└─ 管理層 → Architecture overview + ROI story（不動手）

文件交付格式
├─ 要查詢參考 → Reference（完整 API / 設定清單）
├─ 要照著操作 → How-to SOP（步驟清單）
├─ 要理解概念 → Tutorial（帶 why 的入門）
└─ 要做決策 → Architecture Decision Record（ADR）

Exit Criteria 設計
├─ 操作型工作 → 客戶能獨立執行 + 重現 3 個情境
├─ 設計型工作 → 客戶有人能 review + critique 架構
└─ On-call 型工作 → 至少 1 人能獨立處理 oncall + postmortem
```

---

## References

- 職涯段：`raw/career-summary.md#7-resolve-technology--senior-devops--consultant-dual-role`
- [Divio Documentation System（Tutorial / How-to / Reference / Explanation 四象限）](https://docs.divio.com/documentation-system/)
- [The Consulting Bible（Alan Weiss）— ROI 框架](https://www.amazon.com/Consulting-Bible-Everything-Building-Practice/dp/0470527935)
- [Stakeholder Management — RACI Matrix](https://www.projectmanagement.com/wikis/236452/RACI-Matrix)
- 關聯：[[ansible-gha-automation]]、[[terraform-multi-cloud]]、[[resolve-lessons]]、[[kafka-confluent-streaming]]
