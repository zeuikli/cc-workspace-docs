---
url: "https://arxiv.org/abs/2606.20683"
title: "From Question Answering to Task Completion: A Survey on Agent System and Harness Design"
archived_date: 2026-06-24
arxiv_id: 2606.20683
authors: ["Jianyuan Guo", "Zhiwei Hao", "Chengcheng Wang", "Cheng Fan", "Tingzhang Luo", "Hongguang Li", "Ying Gao", "Hefei Mei", "Jiankun Peng", "Rongjian Xu", "Minjing Dong", "Han Wu", "Mengyu Zheng", "Kai Han", "Shiqi Wang", "Chang Xu", "Yunhe Wang"]
domains: [cs.AI, cs.CL]
html: "https://arxiv.org/html/2606.20683v1"
pdf_path: pdfs/2606.20683.pdf
published_date: 2026-06-14
---

# From Question Answering to Task Completion: A Survey on Agent System and Harness Design

**Authors**: Jianyuan Guo, Zhiwei Hao, Chengcheng Wang, Cheng Fan, Tingzhang Luo, Hongguang Li, Ying Gao, Hefei Mei, Jiankun Peng, Rongjian Xu, Minjing Dong, Han Wu, Mengyu Zheng, Kai Han, Shiqi Wang, Chang Xu, Yunhe Wang
**Published**: June 14, 2026
**Source**: https://arxiv.org/abs/2606.20683 · [HTML](https://arxiv.org/html/2606.20683v1)
**arXiv ID**: 2606.20683
**Categories**: cs.AI, cs.CL
**PDF**: [research/papers/pdfs/2606.20683.pdf](https://arxiv.org/abs/2606.20683) (29 pp, full text archived)

---

## Abstract (quoted)

> LLM-based agents mark a shift from passive question answering to active task completion: they perceive environments, invoke tools, maintain state, and act over extended horizons. As agent systems have evolved from prompt engineering to workflows and context engineering, harness engineering, and agent-native training with co-evolution, a central question has become increasingly important: where does the bottleneck in agent performance reside, in the foundation model, in the execution harness, or in the coupling between them? This survey examines LLM-based agents through a model-harness lens. We first clarify the functional definition of agents and the implementation view of an LLM-based agent as a foundation model coupled with an execution harness. We then analyze the limits of model-centric scaling, trace four paradigms of agent engineering, and decompose the execution harness into six coupled runtime responsibilities: observation, context, control, action, state, and verification. Using this decomposition, we map task properties and domain pressures to harness configurations, review benchmark and evaluation practices, and synthesize model-harness evidence on how runtime design affects long-horizon task completion, efficiency, and reliability. Finally, we identify open challenges in value-aware evaluation, safety, harness generalization, and model-harness co-evolution. Rather than treating agents as models with auxiliary tools, this survey argues that agent quality -- including success, efficiency, safety, and generalization -- emerges from the interaction between model capability, runtime infrastructure, task structure, and evaluation design.

---

## 結構化摘要

### 核心貢獻
以 **model-harness lens** 的 survey，把 LLM agent 視為「foundation model ⊕ execution harness」。中心問題：bottleneck 在模型、harness、還是兩者耦合？

1. **四個 agent engineering 範式演進**：prompt engineering → workflows / context engineering → harness engineering → agent-native training（co-evolution）。
2. **execution harness 拆為六大耦合 runtime 責任**：**observation · context · control · action · state · verification**。
3. **task↔harness 映射**：依任務屬性與領域壓力映射到 harness 配置。
4. 綜整 benchmark / evaluation 實務，分析 runtime design 對 long-horizon 完成度、效率、可靠度的影響。

### 關鍵發現
- agent 品質（成功 / 效率 / 安全 / 泛化）**源於模型能力 × runtime infra × 任務結構 × 評估設計的交互**，非單靠模型。
- model-centric scaling 有上限；runtime design 顯著影響長程任務。

### 開放挑戰
value-aware evaluation · safety · harness generalization · model-harness co-evolution。

---

## Workspace 關聯（評估，非既成結論）

- **六維 runtime 責任 vs 本 workspace harness 分類**：observation/context/control/action/state/verification 可與 HarnessX 九維（D1–D9）、CAR 14-component、agent-harness-survey 對照，補強 KNOWLEDGE-MAP / SURVEY.md 的分類學。
- **「四範式演進」定位 The Loop**：本 workspace 的規則庫屬 harness engineering 範式（context + control + verification），尚未進 agent-native co-evolution（與 HarnessX co-evolution 同為長期 P2 方向）。
- **verification 列為一級 runtime 責任**：背書 core.md TEST/`unverified_success` 閘門在 harness 中的一級地位。
- ⚠️ 為 survey（29 pp），價值在分類框架與證據綜整；可作 harness-meta 稽核時的 taxonomy 對照基準，優先級高於多數單點 paper。
