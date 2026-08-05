---
url: "https://arxiv.org/abs/2606.04402"
title: "Not All Errors Are Equal: Consequence-Aware Reasoning Compute Allocation"
archived_date: 2026-07-25
arxiv_id: 2606.04402
authors: ["Jingbo Wen", "Liang He", "Ziqi He"]
domain: consequence-aware-compute-allocation
published_date: 2026-06-03
source_routine: routine-e
---

# Not All Errors Are Equal: Consequence-Aware Reasoning Compute Allocation

## 摘要 / 核心貢獻
本文質疑主流 test-time compute scaling 的隱含假設——「所有錯誤代價相同」。作者提出以輕量預測器估計每個任務答錯後的下游代價，據此（而非單純任務難度）將推理算力路由到更高的 compute tier，在固定總預算下最大化整體效益。在 SWE-bench Lite + Multi-SWE-bench mini 共 700 個軟體工程任務上的實測顯示：consequence 與 difficulty 兩軸近乎正交（現有模型未依代價充分分配算力）；consequence-aware scheduler 相對 difficulty-only routing 降低 cost-weighted loss 22–33%；預測器實作版本可達理論最優的 90% 以上。

## 為何屬「新領域」
本文提出的「代價感知」路由範式與 workspace 現有版圖（agent harness／FinOps／SRE）無內容重疊；核心關鍵詞（consequence、compute allocation、test-time scaling 等）於既有覆蓋集合、既有論文標題集合、既探勘新領域紀錄三處反向 grep 命中皆為 0。
