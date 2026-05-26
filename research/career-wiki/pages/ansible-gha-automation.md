# Ansible + GitHub Actions 自動化配置管理

> **Source positions**: Resolve Technology 2021–2022（Lead DevOps + Consultant）
> **Last ingested**: 2026-04-21
> **Confidence**: high（Zeuik 親自設計並實作 multi-cloud 配置自動化流程）
> **Linted**: 2026-04-21

---

## Context

Resolve 跨 AWS + GCP + Huawei 三雲並存的環境，基礎設施配置（OS hardening、package install、service config）若全靠人工，重複性高且出錯率高。需要一套 IaC 流程把「機器配置」也納入版本控制與 CI/CD 管線，與 Terraform 管理的「資源佈建」互補。這頁記錄 GitHub Actions 驅動 Ansible Playbook 的完整方法論，含 multi-cloud secret 管理與 idempotency 驗證。

---

## Core Methodology

### Step 1 — Inventory 設計：靜態 vs 動態

- **What**: 靜態 hosts 適合小型固定環境；動態 inventory（`aws_ec2` / `gcp_compute` / `huawei_ecs` plugin）適合 cloud 環境自動發現目標機器
- **Why**: Cloud 的 VM IP 是動態的（Spot / Auto Scaling）；硬編碼 IP 在 GHA workflow 每次都要更新，維護成本高
- **Gotcha** [Resolve]: Huawei Cloud ECS inventory plugin 版本落後（約 1–2 年），缺少 `filter_by_tag` 功能 → 改用 Huawei Stack API 自行撰寫 dynamic inventory Python script，時間額外加 3 天

### Step 2 — GitHub Actions Workflow 結構

- **What**: 分三層 workflow：`validate.yml`（PR 時跑 `ansible-lint` + `--check` dry-run）、`deploy-staging.yml`（merge to main）、`deploy-prod.yml`（手動 trigger + environment gate）
- **Why**: `--check` + `--diff` 讓 reviewer 在 PR 看到「這個 playbook 如果跑會改什麼」，等同 Terraform `plan`，降低生產事故
- **Gotcha** [Resolve]: GHA `environment` gate（需要 reviewer approve）與 Ansible playbook 的等冪性（idempotency）是兩個不同維度；gate 控制「何時跑」，idempotency 控制「重跑不壞」— 兩個都要設，缺一不可

### Step 3 — Secret 管理：GHA Secrets vs Ansible Vault

- **What**: 拆分 secret 層級：
  - **GHA Secrets**：SSH private key、cloud API token（跨 workflow / runner 共用的 CI 憑證）
  - **Ansible Vault**：`vars/vault.yml`（應用層機密：DB password、API key、cert — 跟著 playbook 版本走）
- **Why**: 把所有 secret 放 GHA 等於讓 CI 系統成為單點洩漏來源；Vault 把機密跟程式碼放一起但加密，適合有 code review 的場景
- **Gotcha** [Resolve]: Huawei Cloud 的 image hardening 腳本需要 **root** SSH 連線，但客戶 security policy 禁止 root SSH → 改用 `ansible_become: true` + `sudo` NOPASSWD group，並在 vault 放 become password；多耗 1 週修改 customer 端安全政策

### Step 4 — Playbook Idempotency 驗證

- **What**: 每個 task 加 `changed_when` / `failed_when` 覆寫；service 用 `systemd` module 而非 `shell: systemctl restart`；file 操作用 `copy` / `template` 而非 `shell: cat > file`
- **Why**: Idempotent playbook 可以安全重跑（rolling restart、CI re-trigger）；非 idempotent 的 `shell` task 會在第二次跑時重設狀態或累積副作用
- **Gotcha** [Resolve]: `lineinfile` module 在 multi-line config 場景下會重複插入同一行，確認 `regexp` 必須精確匹配；生產上踩到 nginx.conf 重複 include 行導致 reload 失敗

### Step 5 — Multi-cloud Secret + Role 結構

- **What**: Ansible Role 結構：`roles/{feature}/tasks/main.yml`；provider-specific 差異用 `when: ansible_cloud_provider == 'aws'` 判斷；共用 tasks 放 `common/`
- **Why**: 三雲共用 Role 骨架但允許 per-provider 覆寫；比 per-cloud 完全獨立 repo 維護成本低，比強制單一 abstraction 更誠實
- **Gotcha** [Resolve]: `group_vars/all.yml` 放了不該共用的 secret（誤以為 vault 加密了整個 group_vars dir）→ 實際上 vault 只加密 `vault.yml`，`all.yml` 是明文；code review 發現才修正

### Step 6 — 監控與失敗回報

- **What**: GHA workflow 的 `on.failure` 步驟把 Ansible stdout 截取最後 50 行貼到 Slack；`--diff` output 存 artifact 供回溯
- **Why**: Ansible 失敗訊息常埋在數百行輸出中；截取最後 N 行 + diff 是快速定位問題的最低成本方法
- **Gotcha**: Ansible 有些 module 在 `--check` 模式回傳 `changed: true`（因為 check 不真跑、無法驗證實際狀態），告警雜訊多 → 過濾掉 check-only 的 changed 通知

---

## Concrete Numbers

| 指標 | 值 | 來源場景 |
|------|----|---------|
| 手動配置時間（一台機器）| 45–90 分鐘 | Huawei ECS image hardening（before） |
| Ansible playbook 執行時間（一台）| 8–12 分鐘 | 含 package install + service config |
| 批量配置機器數（單次 run）| 20–50 台 | Resolve multi-cloud 部署 |
| GHA workflow P95 執行時間 | < 15 分鐘 | validate + staging deploy |
| Idempotency bug 發現時間（`--check`）| < 5 分鐘 | PR review 階段 |
| Secret 洩漏事件（`all.yml` 未加密）| 1 次（即時修復）| Resolve QA 環境 |
| Ansible Vault 金鑰輪換頻率 | 每季 | 客戶安全要求 [需 Zeuik 確認] |

---

## Anti-patterns（不要做）

1. **`shell` / `command` module 取代 idempotent module**
   - 問題：`shell: apt-get install -y nginx` 每次都執行、每次都回報 `changed`；無法用 `--check` 預覽；重跑有副作用
   - 何時踩：Huawei ECS hardening 初期版本全用 shell 腳本包 Ansible task；重跑導致 nginx 被停再啟，服務中斷 2 分鐘
   - 解：改用 `apt` / `package` module；需要 shell 時加 `changed_when: false`

2. **GHA Secrets 存放應用層機密（DB password / API key）**
   - 問題：GHA Secrets 不跟 code 版本走；某次 Ansible role 更版後需要新 DB password，但 GHA secret 是舊的，deploy 失敗才發現版本不同步
   - 解：應用層機密走 Ansible Vault（跟 repo tag 一起），CI 層機密（SSH key、cloud API token）才放 GHA Secrets

3. **動態 Inventory 跳過 tag filter 直接拉全量機器**
   - 問題：staging playbook 誤跑到 prod 機器（同帳號 / 同 VPC 但不同 tag）
   - 解：`filters.tag:Env` 必須在 inventory 層就過濾；不要在 playbook 內用 `when` 再過濾（too late）

---

## Decision Tree

```
需要 Ansible + GHA 嗎？

配置目標是...
├─ 雲端 VM（動態 IP / Auto Scaling）
│  └─ 動態 inventory（cloud plugin 或自訂 script）
├─ 固定 server / on-prem
│  └─ 靜態 hosts.ini + group_vars

Secret 放哪？
├─ CI 憑證（SSH key、cloud API token）→ GHA Secrets
├─ 應用層機密（DB pwd、cert）→ Ansible Vault（vault.yml）
└─ 兩者都要，用 Makefile 組合 ansible-playbook 指令

Idempotency 測試策略
├─ PR → validate.yml（ansible-lint + --check --diff）
├─ merge to main → staging deploy
└─ 手動 approve → prod deploy（environment gate）

Multi-cloud 差異處理
├─ 差異 < 20% → 共用 Role + when 判斷
└─ 差異 > 50% → 獨立 Role，共用 common tasks
```

---

## CIS Hardening with Ansible（Air-gap 環境）

> **Source**: Resolve Technology — RHEL8 / Ubuntu22 客戶環境（CIS Benchmark）

### Context

Resolve 客戶要求所有伺服器通過 CIS Benchmark Level 1/2 稽核，且伺服器在 air-gap 環境（無法直接存取 internet）。Ansible 是實施的最佳選擇，搭配 CIS Ansible Role（如 MindPoint Group 的 RHEL8-CIS）。

### Air-gap Ansible Collection 安裝

標準 `ansible-galaxy install` 需要網路，air-gap 環境改用離線方式：

```bash
# 預先在有網路的機器下載 collection tarball
ansible-galaxy collection download ansible.posix -p ./downloads/
ansible-galaxy collection download community.crypto -p ./downloads/
ansible-galaxy collection download community.general -p ./downloads/

# 傳輸到 air-gap 環境後離線安裝
ansible-galaxy collection install ansible-posix-1.5.4.tar.gz -p ./collections
ansible-galaxy collection install community-crypto-2.16.0.tar.gz -p ./collections
ansible-galaxy collection install community-general-8.0.1.tar.gz -p ./collections
```

**Gotcha**：`-p ./collections` 安裝路徑不在 Ansible 預設搜尋路徑（`~/.ansible/collections`），需要在 playbook 同目錄執行，或設 `ANSIBLE_COLLECTIONS_PATHS`。

### CIS Hardening 執行指令

**RHEL8（以 service account + sudo 方式）**：

```bash
ansible-playbook site.yml \
    -i inventory/inventory.ini \
    --become-method sudo --become-user root \
    -u AU-RESO-ANS-P \
    -k -K --ask-pass \
    -e '{
        "rhel8cis_section1":true,
        "rhel8cis_section2":true,
        "rhel8cis_section3":true,
        "rhel8cis_section4":true,
        "rhel8cis_section5":true,
        "rhel8cis_section6":true
    }'
```

**Ubuntu22（同樣 service account 方式）**：

```bash
ansible-playbook site.yml \
    -i inventory/inventory.ini \
    --become-method sudo --become-user root \
    -u AU-RESO-ANS-P \
    -k -K --ask-pass \
    -e '{
        "ubtu22cis_section1":true,
        "ubtu22cis_section2":true,
        "ubtu22cis_section3":true,
        "ubtu22cis_section4":true,
        "ubtu22cis_section5":true,
        "ubtu22cis_section6":true
    }'
```

**NXLog 安裝（log shipping）**：

```bash
ansible-playbook playbook.yml \
    -i inventory/inventory.ini \
    --become-method sudo --become-user root \
    -u AU-RESO-ANS-P \
    -k -K --ask-pass \
    -e '{"install_nxlog_rhel_ubuntu":true}'
```

### CIS Section 分段說明

| Section | 內容 | 常見衝突 |
|---------|------|---------|
| 1 | Filesystem configuration（掛載選項、不使用的 fs type）| /tmp noexec 可能影響安裝腳本 |
| 2 | Services（停用不必要服務）| 確認 app 不依賴 rpcbind、xinetd |
| 3 | Network（kernel 參數、IPv6 停用）| IPv6 停用需確認 app 不用 ::1 |
| 4 | Logging & Auditing（auditd、syslog）| auditd 大量 syscall 監控影響 I/O |
| 5 | Access Control（SSH、PAM、sudo）| SSH MaxAuthTries 降低可能影響自動化 |
| 6 | System Maintenance（file permissions）| 部分 app 需要寬鬆 permission 需要排除 |

**Gotcha**：全 section 一次跑通常有部分 task fail（特別是 section 4 auditd 和 section 5 SSH hardening）。建議先用 `--check` 看影響，再逐 section 執行確認。

---

## References

- 職涯段：`raw/career-summary.md#7-resolve-technology--senior-devops--consultant-dual-role`
- [Ansible Best Practices — Playbook Structure](https://docs.ansible.com/ansible/latest/tips_tricks/sample_setup.html)
- [Ansible Vault Documentation](https://docs.ansible.com/ansible/latest/vault_guide/index.html)
- [GitHub Actions Environments (deployment protection)](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment)
- [Ansible AWS EC2 dynamic inventory plugin](https://docs.ansible.com/ansible/latest/collections/amazon/aws/aws_ec2_inventory.html)
- [MindPoint Group RHEL8-CIS Role](https://github.com/MindPointGroup/RHEL8-CIS)
- 關聯：[[terraform-multi-cloud]]、[[resolve-lessons]]、[[consultant-client-enablement]]、[[linux-ad-integration]]
