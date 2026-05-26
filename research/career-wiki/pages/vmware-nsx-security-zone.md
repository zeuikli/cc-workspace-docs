# VMware NSX Security Zone（Enterprise on-prem）

> **Source positions**: HTC 2017–2019（Security Zone Project）
> **Last ingested**: 2026-04-21
> **Confidence**: high（Zeuik 親自設計與運營）
> **Linted**: 2026-04-21

---

## Context

企業 on-prem 環境做 micro-segmentation（東西向流量隔離、細粒度控制）的首選。HTC 的 Security Zone Project 結合 NSX + Squid Proxy + MS MFA/RDGW/NPS + Commvault，支撐 R&D（含 VR 小組）遠端存取與資安合規。本頁整合 5-step 方法論 + 3 個 HTC 實戰踩坑。

---

## Core Methodology

### Step 1 — Security Zone 規劃

- **What**: DMZ / Trust / Untrust / Management / Backup 5 區設計
- **Why**: 東西向流量隔離，限制橫向移動風險（Ransomware 擴散防護）
- **Gotcha** [HTC]: VR 小組初期要求「proxy 直通」忽視 DLP 風險；後因資安事件強制落地審核

### Step 2 — NSX Distributed Firewall（DFW）

- **What**: 東西向 micro-segmentation rules（VM-to-VM isolation），作用於 vNIC 層**無法繞過**
- **Why**: 細粒度超過傳統 VLAN
- **Gotcha** [HTC]: DFW rule 爆量（峰值 > 800）；需 section 分組（Foundation / Application / Reject）與優先序重構，最終收斂為 ~250 有效 rules

### Step 3 — NSX Edge + VPN / NAT

- **What**: 北南向流量（internet-facing）、VPN gateway for remote access
- **Why**: 集中出口控制、logging；hybrid on-prem 時 NSX Edge 作為 anchor
- **Gotcha** [HTC]: 舊 Cisco ASA 遺留配置未清，VPN session 衝突

### Step 4 — Squid Proxy + MFA / RDGW

- **What**: Application-layer filtering + Windows MFA（Azure AD / on-prem NPS）+ RDGW 給遠端桌面
- **Why**: 內容檢查 + 身份驗證 + 審計；比網層 firewall 細粒度
- **Gotcha** [HTC]: Squid cache miss rate 高 → 團隊感知延遲；需 cache 預熱 + SSL bump 調優

### Step 5 — Compliance Mapping

- **What**: ISO 27001/27017、PCI-DSS、內部政策與 NSX rules 對應表
- **Why**: 稽核時需證明「這條 rule 對應哪項控制」減少解釋開銷
- **Gotcha** [HTC]: 金融客戶要求 ISO mapping 時 HTC 初無文件 → 事後補 [需 Zeuik 確認細節]

---

## Concrete Numbers

| 指標 | 值 | 備註 |
|------|----|------|
| Security Zone 數 | 5（DMZ / Trust / Untrust / Management / Backup）| 複雜組織可 10+ |
| NSX DFW rules（峰值）| ~800 | 缺 section 分組時爆量 |
| NSX DFW rules（收斂後）| ~250 有效 | 加 section 分組後 |
| NSX Edge throughput | ~10 Gbps [需確認] | VR 小組 peak |
| ESXi 主機數 | 12–15 | HTC R&D cluster |
| VM 密度 | ~150–200 VMs [需確認] | on 12–15 hosts |
| Squid cache hit ratio | 45–55% | 動態內容多；減 bandwidth 25% |
| 遠端連線（concurrent）| 50–100 peak | VR 團隊常駐 + mobile 偶發 |

---

## Anti-patterns

1. **Allow-all rule 放最上面 → 下層規則全失效**
   - 問題：NSX DFW 從上而下評估；一條 allow-all 讓下層永遠無效
   - HTC 踩坑：「為了快速上線」先放 allow-all → 3 個月後無人改，被當預設策略
   - 解：section 分組（Foundation / Secure / Reject），order 大到小

2. **VR / R&D 小組繞過 Squid 直連 public cloud**
   - 問題：DLP 無法檢查、audit trail 斷、資安風險
   - HTC 踩坑：VR 小組自建 GCP bucket 備份資產，被發現後強制納入 proxy
   - 解：NSX Org Policy 禁 external IP；強制南北流量經 NSX Edge → Squid

3. **DFW rule 不分 section → > 1000 條性能衰退**
   - 問題：DFW 線性掃描；rule 越多越慢；維護者定位故障困難
   - HTC 踩坑：12 個月後 ~800 rules，每次加 rule 都擔心破壞舊邏輯 → 重構花 2 週
   - 解：按 tier 分 section，**單 section ≤ 200 rule**

---

## Decision Tree

```
需要 network micro-segmentation？
├─ 雲原生（K8s）→ VPC-level（SG / firewall rules）夠，NSX overkill
├─ Hybrid（on-prem + cloud）→ NSX-T + cloud peering gateway
├─ Pure on-prem enterprise（金融 / 政府 / R&D）→ NSX-V / NSX-T
│  ├─ > 500 VMs / 資安要求高 → NSX-T（新建）
│  └─ vSphere 5.5–6.5 穩定 → NSX-V 維持或漸進升
└─ 小規模（< 100 VMs，無合規）→ VLAN + 傳統 firewall 可能夠

east-west 流量加密？
├─ 無合規 + 物理隔離信任 → NSX VLANs 夠
├─ ISO 27017 / PCI-DSS → NSX + TLS/IPsec（DFW verify）
└─ 金融 / 政府 → TLS all the way + NSX session trace

遠端存取管理？
├─ VPN only → 基本
├─ VPN + Squid → 加 DLP layer
└─ Zero-trust → MFA + device posture check + 內部 DFW
```

---

## References

- 職涯段：`raw/career-summary.md#2-htc--infra--storage-engineer`
- [VMware NSX-T Docs](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/)
- [NIST Zero Trust Architecture (SP 800-207)](https://csrc.nist.gov/publications/detail/sp/800-207/final)
- [ISO/IEC 27017:2015 CLD.9 Access Control](https://www.iso.org/standard/43757.html)
- 關聯：[[iso27017-audit]]、[[htc-lessons]]（Session 3）、[[gcp-landing-zone]]
