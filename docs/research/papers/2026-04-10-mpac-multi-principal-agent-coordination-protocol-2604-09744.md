---
url: "https://arxiv.org/abs/2604.09744"
title: "MPAC: A Multi-Principal Agent Coordination Protocol for Interoperable Multi-Agent Collaboration"
archived_date: 2026-07-31
arxiv_id: 2604.09744
authors: ["Kaiyang Qian", "Xinmin Fang", "Zhengxiong Li"]
collected_at: 2026-07-31
collected_by: routine-d
domain: multi-agent
pdf_path: pdfs/2604.09744.pdf
published_date: 2026-04-10
---

# MPAC: A Multi-Principal Agent Coordination Protocol for Interoperable Multi-Agent Collaboration

## 摘要 / 核心貢獻
現有多代理協定多假設單一擁有者，MPAC 針對「跨組織代理需共享資源協作」的場景設計，提出五層架構與「顯式協調語意」（explicit coordination semantics），把衝突視為結構化物件並保留人工裁決選項。實作涵蓋 21 種訊息型別、狀態機、因果排序機制與並行控制，並提供 Python/TypeScript 兩版開源實作。基準測試顯示協調開銷降低 95%、相較序列化基線加速 4.8 倍——此加速來自協調層本身，非代理個別推理速度提升。

## 與 Harness 的關聯
MPAC 把「衝突」明確建模為結構化物件並保留人工裁決通道，呼應本 repo `core.md §PROPOSE 委派`（原 `graph.md`） 中「多 agent 矛盾上呈裁決者，child 不 self-resolve」的設計原則；其把協調語意獨立於個別代理推理之外的分層做法，也是 `core.md §PROPOSE 委派`「邊只存在於資料真的流動之處」的具體實踐參考。
