# ISO 27017 Cloud Security Audit & Certification

> **Source positions**: CathaySec 國泰證券 2024–now
> **Last ingested**: 2026-04-21
> **Confidence**: high（Zeuik 主導 phase 1–2 audit，取得認證；認證機構：**BSI**，user confirmed 2026-05-08）
> **Linted**: 2026-04-21

---

## Context

金融業（尤其台灣證券）雲端遷移的必備里程碑。ISO 27017 是 ISO 27001/27002 在雲端環境的延伸（Code of practice for information security controls for cloud services），涵蓋 **37 個 cloud-specific controls**（CLD.1–CLD.14 領域）。證券業要同時應對 ISO 27001/27017 與台灣金管會《金融機構資訊安全主管管理辦法》[需 Zeuik 確認最新版本] 的雙層要求。

---

## Core Methodology

| 步驟 | What | Why | Gotcha（CathaySec 實戰）|
|------|------|-----|---------|
| **1. Gap Analysis** | 37 項控制逐項比對現狀（自動化程度、人工流程、缺陷） | 量化缺陷範圍，決定投資優先序 | 過度樂觀評估 GCP IAM 設定安全性，忽略 custom role 權限蔓延 |
| **2. Scope Statement** | 明確界定 in-scope 系統（GCP projects、hybrid edge、on-prem backup）、人員、合規邊界 | 避免稽核員指出範圍不清，要求重做 | 忘記納入「交易單位」組織架構決策鏈路 → 內部稽核卡檔 3 週 |
| **3. 風險評估 + 控制落地** | Risk Register（資產 × 威脅 × 弱點 = 風險等級），對應 ISO 控制選擇路線：Terraform codify / 手工 checklist / 人員訓練 | 將抽象控制轉為可測試的技術/組織措施 | Terraform 模組未版本化 → external audit 查不到「誰在哪個時刻改了 IAM」，補 git blame 數週 |
| **4. 證據收集** | Evidence chain：自動化 logs、access review、change record、訓練紀錄、滲透測試報告、**備份機制（冷備份系統上雲作為主要取證項目）** | 稽核員不看陳述，只看**時間序列證據** | Cloud Audit Logs retention 初設 30 天，稽核需 6 個月回溯 → 緊急升為 365 天；Dell PowerProtect Data Domain VE 整合 GCP 作為備份加密 + 跨區備援的主要稽核 evidence |
| **5. 稽核配合** | Stage 1（文件審查）→ Stage 2（現場查驗、IT 訪談、技術測試）→ 非符合項整改（15–30 天） | 外部稽核員驗證自評。TAF 認可機構（BSI、DNV、SGS）依 ISO/IEC 17021-1 程序評估 | Initial audit 被問「ISO 27017 × 金管會辦法」對應，花 3 天補 mapping [需 Zeuik 確認最新法規版本] |

---

## GCP-specific Control Mapping

| ISO 27017 Control | 目的 | GCP Native Service | CathaySec 實作備註 |
|---|---|---|---|
| **CLD.6.3.1** Shared roles & responsibilities | 界分 CSP vs 客戶責任 | IAM Roles + Org Policy | 用 Org Policy 強制 MFA、禁止 compute external IP、限制 billing change |
| **CLD.8.1.5** Asset removal | 數據銷毀 SLA + 驗證 | Cloud Storage retention + Bucket lock | 證券交易數據須符「金融業留存年限」（通常 5 年 + 稅期）；Terraform 定義 lifecycle |
| **CLD.12.4** Logging & monitoring | 完整活動追蹤 | Cloud Logging + Audit Logs + Security Command Center | 365 天 retention；IAM change / GCS 上傳 / VM 開關機皆 sink → BigQuery |
| **CLD.12.1.5** Capacity management | 資源用量預警（防 DoS 抗性降低）| Cloud Monitoring + GKE autoscaling + Quotas | Prometheus rule：CPU > 70% → alert；GKE max node 限制防失控成本 |
| **CLD.14.2.8** System security testing | 定期滲透測試、漏洞掃描 | Cloud Build security scanning + Cloud Armor + Security Assessment Partner | Partner 每季滲透測試結果入 evidence chain；tfsec 整合 Terraform CI |
| **CLD.12.3** Backup（雲端備份控制）| 備份加密、存取控制、恢復演練 | GCS（冷儲存）+ Cloud KMS + GCP Audit Log | **主要取證項目**：Dell PowerProtect Data Domain VE 整合 GCP；備份加密 at-rest + in-transit；定期恢復演練 log 作為 BSI 稽核 evidence（user confirmed 2026-05-08）|

---

## Concrete Numbers

| 指標 | 值 | 備註 |
|------|----|------|
| 控制項覆蓋率 | 初期 40% → Phase 1 結束 85% → cert 前 100% | Gap analysis 37 項初期僅 15 項部分符合 |
| Terraform 模組數（控制碼化）| 8 → 22（IAM / logging / encryption / network isolation）| IaC 標準化 |
| 證據收集工時 | Gap analysis 80h + logging pipeline 120h + 週期審查 40h（持續）| 含文件與訓練 |
| Internal audit 缺失數 | Stage 1 前預演 18 項；external Stage 2 發現 2–3 項重要（正常）| external 發現率控在 5–10% |
| Certification 時間 | Gap analysis → cert 約 **4–5 個月** | 含組織圖修訂 + 法規 mapping 額外耗時 |
| FinOps（同期副產品）| **NT$400,000+/年** | 資產清冊整理過程發現 idle 資源 |

> [需 Zeuik 確認] 實際控制項覆蓋的精確百分比、工時精確值、滲透測試供應商。

---

## Anti-patterns（不要做）

1. **直接套用 ISO 27001 文件到雲端**
   - 問題：27001 資產清冊列「伺服器 XX 台、儲存 YY TB」；雲端沒有實體資產概念
   - 解：雲端資產應列 GCP projects、跨 region 複製路徑、hybrid on-prem 連線；CathaySec 初期用舊 checklist 被退回，花 10 天重做

2. **稽核前才補 evidence**
   - 問題：日常無 logging、變更單存 email，稽核前 1 個月「回溯補證據」→ 稽核員會質疑「這些 logs 是哪時補的」
   - 解：**Continuous compliance（日常 PDCA）**，每週檢查 evidence 完整性

3. **Terraform state 未納入 change management**
   - 問題：IaC 很方便，但若 state 改動無 commit log、無人簽核 → 稽核員要求補人工 change ticket
   - 解：Git commit 強制 GPG 簽署；所有 state 變更進 audit log；PR 需至少 1 人 approve

---

## Decision Tree

```
是否需要 ISO 27017？
├─ 金融業（銀行、證券、保險）→ 幾乎必須（監理壓力）
├─ 政府、公營單位 → 視採購合約（常見）
├─ SaaS 賣給金融業客戶 → 客戶會要求
├─ 內部合規要求（母公司或集團）→ 視情況
└─ 純消費者 B2C / 新創 MVP 階段 → 通常 overkill

選擇 PKI / 認證機構？
├─ 優先 TAF 認可（台灣合規場景必要）
│  └─ BSI, DNV, SGS, AFNOR 等
├─ 若涉及跨國 → UKAS, ANAB 認可機構
└─ 檢查稽核員是否有「金融業 sector」經驗 — 沒有很容易溝通不順

啟動時間點？
├─ 新雲端遷移：Landing Zone 設計階段就納入（省 50% 後續整改成本）
├─ 既有雲端：Gap analysis 先做，avoid cold start
└─ 組織改造期（併購、業務轉型）：延後，不要和組織變動同時進行
```

---

## References

- 職涯段：`raw/career-summary.md#8-cathaysec-國泰證券--sre-lead--manager-current`
- [ISO/IEC 27017:2015 官方](https://www.iso.org/standard/43757.html)
- [GCP Cloud Security Compliance](https://cloud.google.com/security/compliance)
- [GCP ISO 27017 page](https://cloud.google.com/security/compliance/iso-27017) [需 Zeuik 確認最終 URL]
- [TAF 台灣認證暨驗證推動中心](https://www.taf.org.tw/)
- 金管會《金融機構資訊安全主管管理辦法》[需 Zeuik 確認最新版本編號與發布日期]
- 關聯：[[gcp-landing-zone]]、[[terraform-multi-cloud]]、finops-cost-reduction-playbook（尚未建立）
