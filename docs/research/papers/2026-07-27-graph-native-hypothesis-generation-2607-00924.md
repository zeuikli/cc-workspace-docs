---
url: "https://arxiv.org/abs/2607.00924"
title: "Graph-Native Reinforcement Learning Enables Traceable Scientific Hypothesis Generation through Conceptual Recombination"
archived_date: 2026-07-27
arxiv_id: 2607.00924
authors: ["Subhadeep Pal", "Shashwat Sourav", "Tirthankar Ghosal", "Markus J. Buehler"]
domain: hypothesis-generation-infrastructure
published_date: 2026-07-01
source_routine: routine-e
---

# Graph-Native Reinforcement Learning Enables Traceable Scientific Hypothesis Generation through Conceptual Recombination

## 摘要 / 核心貢獻
提出 Graph-PRefLexOR，結合 graph-based 推理與強化學習（GRPO）改善 AI 生成科學假說的方式，將過程拆為「機制探索、圖構建、模式提取、假說合成」四階段，使因果關係被顯式構建成圖而可檢視、可重用。在材料科學與力學 100 道開放式問題上較 baseline 提升 40–65%，其中增益最大的維度是推理可溯源性而非答案本身。關鍵發現：增加測試期算力主要提升模型在有界概念空間內「重組」既有概念的能力，而非擴充語意知識庫本身，暗示 test-time compute 對真新穎性存在天花板。

## 為何屬「新領域」
「假說生成的推導鏈可溯源性」與 workspace 既有覆蓋集合中的 formal-verification-robotics（驗證對象為機器人控制器安全性質）屬同詞異指、非重複；核心關鍵詞 hypothesis / recombination 於既有覆蓋集合、既有論文標題集合反向 grep 命中皆為 0。
