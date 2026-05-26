# Resolve Technology — Lessons Learned

> **Tenure**: 2021–2022（approx）| **Role**: Lead DevOps + Consultant（dual role）
> **Last ingested**: 2026-04-21 | **Confidence**: high

---

## Context

首次跨 AWS + GCP + Huawei 三層異構 cloud 的 IaC。同時扮演 consultant（client enablement + docs + training），影響力從單一團隊擴到多客戶。

## Key Lessons

1. **Multi-cloud 不是追「best of breed」，是合規 / 供應商需求**
   - 技術上跨雲維運成本 > 省的錢；誠實回答客戶這個問題
   - 見 [[terraform-multi-cloud]]

2. **Provider-agnostic abstraction 在實務上做不到**
   - AWS IAM / GCP IAM / Huawei 權限模型差太多；embrace 差異比強制抽象好
   - Module 結構 `{feature}/{provider}/` 比 `{feature}-abstracted/` 穩

3. **Huawei Stack 的 1–2 年功能落差必須預期**
   - Image hardening / state lock / registry — 都要自製補上
   - Timeline 估算加 30–50% buffer

4. **Consulting 的 scaling 瓶頸是 reviewer 可用性**
   - Per-provider reviewer × 時差 → 平均 4–8 hr 核准等待
   - 文件 + training 比 hands-on help 更能 scale

5. **Kafka / Confluent 客戶最常犯 4 類錯誤**
   - Partition 數誤設（當並行度）/ 跳過 Schema Registry / 用 Kafka 當 DB / 無 rebalance 中斷處理
   - 見 [[kafka-confluent-streaming]]

6. **TFE 版本遷移：Replicated → FDO 的三個地雷**
   - 版本不一致（Replicated v.A → FDO v.B）= DB schema 衝突，靜默損壞
   - GCP 環境 Docker MTU 必須設 1460（預設 1500 造成 workspace run 卡住，無報錯）
   - `TFE_ENCRYPTION_PASSWORD` 新舊必須完全一致，否則 restore 後 workspace sensitive data 全無法解密
   - 見 [[terraform-enterprise-fdo]]

7. **Air-gap 環境的 Ansible 部署：Collection 離線安裝是最常踩的坑**
   - `ansible-galaxy install` 需要網路；air-gap 環境需提前下載 tarball 傳入
   - Collection 安裝路徑 `-p ./collections` 不在預設搜尋路徑，要在 playbook 同目錄執行
   - CIS hardening playbook 全 section 一次跑通常有 fail；先 `--check` 看影響，再逐 section 確認
   - 見 [[ansible-gha-automation]]#CIS-hardening

8. **Linux 加入 AD：Kerberos 時間同步是最常見失敗原因**
   - 時差 > 5 分鐘 = KRB5KRB_AP_ERR_SKEW，認證失敗；VM 剛啟動特別容易
   - `realm join` 整合度高（自動配 SSSD + authselect + oddjobd），比手動設定 winbind 可靠
   - AD 服務帳號需要目標 OU 的「Create Computer Objects」權限；事先確認比 join 時發現更省時
   - 見 [[linux-ad-integration]]

## What I'd Do Differently

- **明確拒絕** 客戶「一個 Terraform module 支援三雲」的要求 — 產出彩禍多於價值
- 先做 `onboarding playbook` 給客戶自學，比每次 ad-hoc consulting 高效
- Debezium CDC 初始 snapshot **必在 off-peak** 執行，client 要 upfront 告知
- TFE 版本遷移前先建 staging 環境驗證 encryption password 可 restore
- Air-gap 部署前建立「離線 package 清單」並在有網路的 lab 完整測試一輪

## Cross-references

- 核心 pages：[[terraform-multi-cloud]]、[[kafka-confluent-streaming]]、[[ansible-gha-automation]]、[[consultant-client-enablement]]
- 新增 pages：[[terraform-enterprise-fdo]]、[[linux-ad-integration]]

## References

- `raw/career-summary.md#7-resolve-technology--senior-devops--consultant-dual-role`
- Source: UpNote BJJ Data Migration.html, BJJ New TFE Setup Steps.html, CIS Hardening Setup note.html, Linux join AD.html（local only）
