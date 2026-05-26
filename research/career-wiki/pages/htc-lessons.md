# HTC — Lessons Learned

> **Tenure**: Mar 2018 – Aug 2018（6 months）| **Role**: System & Storage Engineer
> **Last ingested**: 2026-04-21 | **Updated**: 2026-05-08 (confirmed dates + details)
> **Confidence**: high
> **Note**: 專案制任務（Security Zone project），完成後轉至 SPQ（user confirmed）

---

## Context

企業 on-prem 環境；VMware ESXi 6.0 + NSX micro-segmentation + Security Zone project + Commvault backup（TSM → Commvault 遷移）+ MS stack（MFA/RDGW/NPS/WSUS/SCCM）+ VR 團隊 Linux mirror + proxy + Docker PoC（早期 container 評估：結論可導入，對應專案待議）。

## Key Lessons

1. **Micro-segmentation 比 perimeter 防禦更 scale**
   - 傳統 firewall 主要防 north-south；NSX DFW 防 east-west 橫向移動
   - Ransomware 場景下 east-west 隔離是救命的
   - 見 [[vmware-nsx-security-zone]]

2. **DFW rule 沒 section 分組必爆**
   - 12 個月累積 ~800 rules，性能衰退 + 無人敢改
   - 按 tier 分 section（Foundation / Application / Reject），**單 section ≤ 200**

3. **「Allow-all 先放著」是技術債的原型**
   - 初期為快速上線放 allow-all → 被當預設政策 3 個月沒人改
   - 加 rule 時**同時加 expiration / review date**

4. **企業 IT 與 R&D team 的防線要協商而非強制**
   - VR 小組一開始自建 GCP bucket 繞過 proxy → 資安事件後才收斂
   - 先理解業務需求（VR 大檔案協作）再提 proxy 白名單方案

5. **Commvault / Tiered storage 的成本優化是持續題**
   - 存檔週期 + 還原週期 + 冷熱分層
   - Cloud storage 不是 always cheaper — 要看 egress / 還原頻率

6. **Docker PoC：結論「可導入，但對應專案待議」的現實**
   - PoC 技術驗證通過（image hardening、container registry、compose 部署流程）
   - HTC 企業規模的障礙：資安政策審核週期長 + 現有 VM workload 無明顯遷移動機
   - 帶走的 pattern：**PoC 結論不是 yes/no，而是「哪個 workload 最適合先 container 化」** — 沒有明確 workload 就沒有優先序，導入自然卡關
   - 這個 pattern 在後續 CathaySec CNAPP 評估也重現（分階導入 CSPM 先、CWPP 後）

7. **VR 團隊的 Shadow IT 問題與 sanctioned solution**
   - VR 大檔案協作需求無法通過企業 proxy → 工程師自建 GCP bucket 繞過
   - 正確解法：先理解需求 → 建立 Linux mirror site + proxy 白名單 → 提供合規路徑
   - **關鍵洞察**：安全政策「禁止」比「提供替代方案」貴 — 禁止不能解決業務需求，只讓人繞路

## What I'd Do Differently

- **不** 放 allow-all rule 上線，從 day 1 就用 staging rule set
- DFW rule 起始就按 section 分組（改架構成本低，改 1000 rule 成本高）
- VR 團隊的雲端需求用 sanctioned solution 先滿足（避免 shadow IT）

## Cross-references

- 核心 pages：[[vmware-nsx-security-zone]]、[[iso27017-audit]]（合規 mapping）

## References

- `raw/career-summary.md#2-htc--infra--storage-engineer`
