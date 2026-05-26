# AWS Certified Solutions Architect — Professional 備考方法論

> **Source positions**: 個人考證（2023，KKStream / SoundOn 之間）
> **Last ingested**: 2026-04-21
> **Confidence**: medium（Zeuik 通過 SAP-C02；細節來自 blog #3/#4，未 archive，以 URL 索引為準）
> **Linted**: 2026-04-21

---

## Context

AWS SAP-C02（Solutions Architect - Professional）是業界認可難度最高的 AWS 認證之一，合格率約 30–40%。Zeuik 在有 4 年 AWS 實戰經驗後備考並通過，分享的備考方法論對「有實戰但需要系統化知識」的工程師最有參考價值。這頁整合 [blog #3（心得）](https://medium.com/@zeuik/2023%E5%B9%B4-%E8%80%83%E5%8F%96-aws-certified-solutions-architect-professional-%E8%AD%89%E7%85%A7%E5%BF%83%E5%BE%97-ec9b40fe0a94) 與 [blog #4（準備方式）](https://medium.com/@zeuik/2023%E5%B9%B4-%E5%A6%82%E4%BD%95%E6%BA%96%E5%82%99-aws-certified-solutions-architect-professional-28da5b6dd817)。

---

## Core Methodology

### Step 1 — 評估起點：實戰 vs 理論缺口

- **What**: 用 AWS Skill Builder 的免費 SAP 官方 practice exam（20 題）自測；記錄錯題的 domain（Migration / Networking / Security / Cost Optimization / ...）
- **Why**: SAP 考試有 6 大 domain，實戰工程師常某幾個 domain 很強但其他完全沒碰過（例如 KKStream 背景 = 強 EC2/ECS/Lambda，但弱 Directory Service / Outposts）；先找缺口比全部重頭學省 60% 時間
- **Gotcha**: SAP practice exam 題目品質比實際考試簡單；自測 80% 不代表能過考試；真實題目更長、干擾選項更刁鑽

### Step 2 — 核心學習資源選擇（只選一套）

- **What**: 選定一套 video course（Adrian Cantrill SAP 或 Stephane Maarek on Udemy）+ 一套 practice exam（Tutorials Dojo / Jon Bonso）；不要同時多套
- **Why**: 資源冗餘讓人有「我還有材料沒看完」的安全感但實際學習效率下降；SAP 材料厚，選一套徹底比三套半懂強
- **Gotcha** [Zeuik blog 推論]: Adrian Cantrill 課程深度強但費時（80+hr）；Udemy 課程節奏快但廣度有限；有實戰經驗的人後者可以 1.5x 速刷，前者適合想深理解架構的人 [需 Zeuik 確認實際選哪套]

### Step 3 — 學習節奏：週時數計劃

- **What**: 設定 8–12 週備考期；前 6 週課程（每週 8–10hr）→ 後 2–4 週刷題（每週 10–15hr，含錯題 review）
- **Why**: SAP 知識廣度大，需要幾週讓知識沉澱；最後 2–4 週密集刷題才有效果（考試技巧 ≠ 知識理解）
- **Gotcha** [Zeuik blog 推論]: 邊上班邊備考每週真實可用時間通常比計劃少 30%；建議週計劃打 70% 折扣計算 [需 Zeuik 確認實際週時數]

### Step 4 — 模擬題策略（白板 + 分析）

- **What**: Tutorials Dojo / Jon Bonso practice test，分 domain 計時作答；錯題不只看答案，要理解「**為什麼這個服務而不是那個**」
- **Why**: SAP 多選題有 4–5 個看起來都對的選項，差異在 cost / scalability / managed service 取捨；理解 tradeoffs 比背答案重要
- **Gotcha**: 有些題目在更新的 AWS 功能下答案已過期（例如 S3 multipart upload size limit 有改動）；Tutorials Dojo 有標記 note 但要注意 last updated 日期

### Step 5 — 架構白板演練（高分關鍵）

- **What**: 選 5–10 個 SAP 高頻場景（hybrid connectivity / DR / multi-account security / data migration）親手畫架構；不用工具，用筆畫
- **Why**: SAP 考試是「給定條件 → 選最佳架構」，大腦需要有能調出的架構 pattern；白板演練強迫自己說出 why，比被動看 slide 記憶深
- **Gotcha**: 白板演練容易變成「畫圖」而非「思考」；每張圖都要問自己：這個設計在 failure / cost / compliance 三個維度下有什麼 tradeoff？

### Step 6 — 考試策略（時間管理）

- **What**: SAP 75 題 / 190 分鐘（約 2.5 分鐘/題）；先快速過一遍跳過難題，標記回頭；最後 20 分鐘掃描未作答
- **Why**: SAP 有長達 200 字的題幹；很多人時間不夠不是不會而是太慢；先答確定的題穩分
- **Gotcha**: 英文非母語考生閱讀速度建議抓 3 分鐘/題，留 15 分鐘 buffer；Zeuik 建議有中文考場選項時考慮使用（閱讀速度提升 20–30%）[需 Zeuik 確認是否選中文考場]

---

## Concrete Numbers

| 指標 | 值 | 備註 |
|------|----|------|
| SAP 考試合格率（業界） | 30–40% | AWS 官方未公開，業界估計 |
| 建議備考總時數 | 80–150 小時 | 視實戰背景調整；有 4 年 AWS 經驗可取低端 |
| 備考期長度 | 8–12 週 | 每週 8–15hr |
| Practice exam 刷題次數（目標）| 4–6 套 × 每套 1–2 次 | Tutorials Dojo / Jon Bonso |
| Tutorials Dojo 模擬題目標分數 | > 80% | 考試前 1 週達標 |
| 考試時間 | 190 分鐘 / 75 題 | 約 2.5 分鐘/題 |
| Zeuik 備考時間（估計）| [需 Zeuik 確認] | 有 4 年 AWS 實戰經驗 |
| Zeuik 考試分數 | [需 Zeuik 確認] | 通過（720 分合格） |

---

## Anti-patterns（不要做）

1. **沒有實戰直接考 SAP**
   - 問題：SAP 假設考生知道「在實際生產用過後的教訓」；純啃文件通過率低、通過了也沒用
   - 解：至少有 2 年 AWS 實戰後再考；或先過 SAA（Solutions Architect Associate）建立基礎

2. **刷題但不看 explanation（只看對錯）**
   - 問題：SAP 70% 的題型是「給出 A、B、C、D 四個架構，哪個最 cost-effective + scalable？」；看錯了但不知道為何錯，下次遇到變形還是不會
   - 解：每題 explanation 都看；整理「我以為是 X，實際是 Y，因為 Z」的錯題筆記

3. **備考期間 AWS 服務大量更新被忽視**
   - 問題：SAP 考試有時考新服務（SAP-C02 vs SAP-C01 差異很大）；2023 前的舊材料有過時題目
   - 解：購買課程前確認 last updated 日期；AWS 重大發布（re:Invent）後 1–2 個月更新考題機率高

---

## Decision Tree

```
是否適合現在考 SAP？

AWS 實戰年資
├─ < 2 年 → 先考 SAA-C03（Associate 級別）
├─ 2–3 年 → 可考，但備考時間估 120–150h
└─ > 4 年（如 Zeuik KKStream/SoundOn 背景）→ 適合，備考 80–100h

起點評估（官方 practice exam）
├─ < 50% → 需要從頭系統學習（Adrian Cantrill 深度課）
├─ 50–70% → 補缺口 + 大量刷題
└─ > 70% → 直接刷題 + 錯題 review

備考資源選擇
├─ 想深度理解架構 → Adrian Cantrill SAP 課程
├─ 趕時間 / 有實戰 → Stephane Maarek Udemy（1.5x 速）
└─ 題庫 → Tutorials Dojo（Jon Bonso）必備

考試語言
├─ 英文熟練（工作語言是英文）→ 英文
└─ 中文母語 → 中文選項（閱讀速度 ↑ 20–30%）
```

---

## References

- **Zeuik blog #4**（2023-06）：[如何準備 AWS SAP](https://medium.com/@zeuik/2023%E5%B9%B4-%E5%A6%82%E4%BD%95%E6%BA%96%E5%82%99-aws-certified-solutions-architect-professional-28da5b6dd817)
- **Zeuik blog #3**（2023-08）：[AWS SAP 考照心得](https://medium.com/@zeuik/2023%E5%B9%B4-%E8%80%83%E5%8F%96-aws-certified-solutions-architect-professional-%E8%AD%89%E7%85%A7%E5%BF%83%E5%BE%97-ec9b40fe0a94)
- [AWS SAP-C02 Exam Guide（官方）](https://d1.awsstatic.com/training-and-certification/docs-sa-pro/AWS-Certified-Solutions-Architect-Professional_Exam-Guide.pdf)
- [AWS Skill Builder — SAP practice exam](https://skillbuilder.aws/)
- [Tutorials Dojo SAP Practice Exams（Jon Bonso）](https://tutorialsdojo.com/courses/aws-certified-solutions-architect-professional-practice-exams/)
- 關聯：[[finops-savings-plans-roi]]、[[aws-step-functions-patterns]]、[[terraform-multi-cloud]]
