# Linux 加入 Windows Active Directory（realm + adcli + SSSD）

> **Source positions**: Resolve Technology 2021–2022（Lead DevOps + Consultant）
> **Last ingested**: 2026-04-22（from UpNote Linux join AD.html）
> **Confidence**: high（Zeuik 為香港客戶 ICLCLOUD.HK 執行 RHEL Linux AD 整合）
> **Linted**: 2026-04-22

---

## Context

企業環境中，Linux 伺服器需要加入 Windows Active Directory 以統一身份驗證（SSO）、集中帳號管理、稽核追蹤。Resolve 幫香港客戶（ICLCLOUD.HK）的 RHEL 伺服器完成 AD 整合，使用 `realm` + `adcli` + SSSD 組合。

**此組合的優點**：
- `adcli` 比 winbind 輕量，不需要 Samba
- SSSD 提供 caching（AD 短暫不可達時仍可登入）
- `authselect` 自動設定 PAM + nsswitch（RHEL 8+ 官方推薦）

---

## 完整加入 AD 流程

### 前置需求確認

```bash
# 確認 DNS 能解析 AD domain
nslookup iclcloud.hk
dig _ldap._tcp.iclcloud.hk SRV    # 驗證 SRV record 存在

# 確認 NTP 同步（Kerberos 時間差 < 5 分鐘）
timedatectl status
chronyc tracking

# 安裝必要套件
dnf install realmd sssd adcli sssd-tools oddjob oddjob-mkhomedir -y  # RHEL
apt install realmd sssd adcli sssd-tools oddjob oddjob-mkhomedir -y  # Ubuntu
```

### 執行 realm join

```bash
realm join --verbose ICLCLOUD.HK \
    --computer-name redhat-agent-testvm \
    --computer-ou="OU=Testing OU,DC=iclcloud,DC=hk" \
    --user="CY-PCCW-SYS@ICLCLOUD.HK" \
    --membership-software=adcli \
    --install=/
```

**參數說明**：
- `--computer-ou` — 指定電腦物件要建立在哪個 OU（需要目標 OU 的寫入權限）
- `--membership-software=adcli` — 使用 adcli 而非 winbind（推薦）
- `--install=/` — dry-run 不安裝時省略此參數

### 驗證加入成功

```bash
realm list                          # 顯示已加入的 domain
id CY-PCCW-SYS@ICLCLOUD.HK         # 驗證 AD 帳號可解析
getent passwd CY-PCCW-SYS@ICLCLOUD.HK  # 驗證 nsswitch 有 sss
```

---

## realm join 完成後的自動設定

`realm join` 成功後會自動完成：

```
1. Kerberos 設定
   └─ /etc/krb5.conf 加入 domain realm 設定
   └─ /etc/krb5.keytab 存入電腦帳號 keytab

2. SSSD 設定
   └─ /etc/sssd/sssd.conf 自動生成
   └─ systemctl enable --now sssd

3. PAM + nsswitch
   └─ authselect select sssd with-mkhomedir --force
   └─ 覆寫 passwd, group, netgroup, automount, services 的 nsswitch maps
   └─ systemctl enable --now oddjobd（自動建立家目錄）
```

**with-mkhomedir 的作用**：AD 用戶首次 SSH 登入時，自動建立 `/home/username@domain` 家目錄（需要 oddjobd 服務運行）。

---

## Keytab 內容（成功後）

```
/etc/krb5.keytab 包含：
- redhat-agent-testvm$@ICLCLOUD.HK
- host/redhat-agent-testvm@ICLCLOUD.HK
- host/redhat-agent-testvm.ICLCLOUD.HK@ICLCLOUD.HK
- RestrictedKrbHost/redhat-agent-testvm@ICLCLOUD.HK
- RestrictedKrbHost/redhat-agent-testvm.ICLCLOUD.HK@ICLCLOUD.HK
```

RestrictedKrbHost 限制 keytab 只能用於 Kerberos 身份驗證，不能當 service ticket。

---

## Concrete Numbers

| 指標 | 值 | 備註 |
|------|----|------|
| AD domain | ICLCLOUD.HK | 香港客戶 |
| Domain Controller | AZ1HCSADCV02.iclcloud.hk（10.16.33.2）| — |
| Computer password length | 120 characters | adcli 預設，高強度 |
| kvno（key version number）| 3 | keytab 版本，重新加入會遞增 |
| Kerberos 時間容差 | 5 分鐘 | 超過 → clock skew 錯誤，無法認證 |
| oddjobd 用途 | 自動建家目錄（mkhomedir）| 不啟動則首次登入失敗 |

---

## 常見錯誤排查

### Clock Skew 錯誤

```
KRB5KRB_AP_ERR_SKEW: Clock skew too great
```

**原因**：主機時鐘與 AD DC 時差 > 5 分鐘。  
**解法**：
```bash
chronyc makestep    # 立即同步
timedatectl set-ntp true
```

### 找不到 SRV Record

```
realm join: Couldn't resolve _ldap._tcp.iclcloud.hk
```

**原因**：DNS 沒有指向 AD DNS Server，或 AD DNS record 未設定。  
**解法**：
```bash
# 確認 /etc/resolv.conf 或 /etc/systemd/resolved.conf 指向 AD DC IP
nmcli con mod <interface> ipv4.dns "10.16.33.2"
```

### OU 無寫入權限

```
adcli: Couldn't join domain: Insufficient access
```

**原因**：加入帳號（CY-PCCW-SYS）對目標 OU 沒有「Create Computer Objects」權限。  
**解法**：請 AD 管理員給予目標 OU 的 `Create Computer Objects` 權限；或先由 AD 管理員建立 computer account 再 join。

### SSSD 快取問題

```bash
# 清除 SSSD 快取（帳號更新未生效時）
sss_cache -E    # 清除所有快取
systemctl restart sssd
```

---

## Anti-patterns（不要做）

1. **用 root 帳號加入 AD**
   - 問題：root 帳號不應有 AD 認證權限，稽核追蹤困難
   - 解：建立專用服務帳號（如 CY-PCCW-SYS），只給 Computer Objects 建立權限

2. **忽略 NTP 同步**
   - 問題：Kerberos 時間敏感，5 分鐘差即 authentication failure，特別是 VM 剛啟動後
   - 解：部署前確認 chronyd/ntpd 配置並指向可信 NTP 源

3. **所有機器加入同一 OU**
   - 問題：無法按環境/部門分別套用 Group Policy
   - 解：設計 OU 結構（Linux Servers / Production / Staging / Region）

4. **不設定 SSSD offline cache**
   - 問題：AD DC 不可達時所有 AD 帳號無法登入（包括 oncall 人員）
   - 解：sssd.conf 設定 `cache_credentials = true`（預設已開啟）

5. **authselect 改完沒重啟相關服務**
   - 問題：nsswitch 改了但現有 SSH 連線的 PAM 沒重載
   - 解：`systemctl restart sssd oddjobd sshd`

---

## Decision Tree

```
Linux 需要 AD 整合？

OS 類型
├─ RHEL 8+ / CentOS Stream → realm + adcli + SSSD（官方推薦）
├─ Ubuntu 20.04+ → realm + adcli + SSSD（同樣適用）
└─ 舊版（RHEL 6/7）→ winbind + Samba（legacy，不推薦）

整合深度
├─ 只需 AD 身份驗證 → sssd（基本）
├─ 需要 sudoers 從 AD 控制 → sssd + sudo provider
├─ 需要 Group Policy → adcli + SSSD（部分 GPO 支援）
└─ 需要完整 Windows 整合（GPO / 印表機）→ winbind + Samba

OU 設計
├─ 測試機器 → Testing OU（與 production 隔離）
├─ Production → Production Servers OU（GPO 套用不同策略）
└─ 跨 region → 每 region 獨立 OU（便於委派管理）
```

---

## Cross-references

- 關聯：[[resolve-lessons]]、[[ansible-gha-automation]]（用 Ansible 自動化 realm join）、cis-hardening-ansible（尚未建立）

## References

- 職涯段：`raw/career-summary.md#7-resolve-technology--senior-devops--consultant-dual-role`
- Client: ICLCLOUD.HK（香港）
- Source: UpNote Linux join AD.html（local only）
- [Red Hat — Connecting RHEL to AD](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/integrating_rhel_systems_directly_with_windows_active_directory/)
- [SSSD Documentation](https://sssd.io/docs/)
