---
url: "https://arxiv.org/abs/2509.25140"
title: "ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory"
date: 2025-09-29
arxiv_id: 2509.2514
authors: "Siru Ouyang, Jun Yan, I-Hung Hsu, Yanfei Chen, Ke Jiang"
referenced_by: warmwater.dev
source: arxiv
---

## Abstract

With the growing adoption of large language model agents in persistent real-world roles, they naturally encounter continuous streams of tasks. A key limitation, however, is their failure to learn from the accumulated interaction history, forcing them to discard valuable insights and repeat past errors. We propose ReasoningBank, a novel memory framework that distills generalizable reasoning strategies from an agent's self-judged successful and failed experiences. At test time, an agent retrieves relevant memories from ReasoningBank to inform its interaction and then integrates new learnings back, enabling it to become more capable over time. Building on this powerful experience learner, we further introduce memory-aware test-time scaling (MaTTS), which accelerates and diversifies this learning process by scaling up the agent's interaction experience. By allocating more compute to each task, the agent generates abundant, diverse experiences that provide rich contrastive signals for synthesizing higher-quality memory. The better memory in turn guides more effective scaling, establishing a powerful synergy between memory and test-time scaling. Across web browsing and software engineering benchmarks, ReasoningBank consistently outperforms existing memory mechanisms that store raw trajectories or only successful task routines, improving both effectiveness and efficiency; MaTTS further amplifies these gains. These findings establish memory-driven experience scaling as a new scaling dimension, enabling agents to self-evolve with emergent behaviors naturally arising.

## 主要貢獻

- **ReasoningBank 記憶框架**：從 agent 自我評判的成功與失敗經驗中，蒸餾出可泛化的推理策略（reasoning strategies），而非儲存原始軌跡或只儲存成功例子。
- **自我進化循環**：agent 在測試時從 ReasoningBank 檢索相關記憶以指導當前任務，完成後將新學習整合回記憶庫，實現持續能力提升。
- **MaTTS（Memory-aware Test-Time Scaling）**：透過為每個任務分配更多算力，讓 agent 生成豐富、多元的互動經驗，提供更強的對比信號以合成更高品質記憶；更好的記憶反過來引導更有效的 scaling，形成正向循環。
- **雙向對比學習**：同時利用成功與失敗的自我評判經驗作為對比信號，優於只儲存成功例子的方法。
- **實驗結果**：在 web browsing 和 software engineering benchmark 上，ReasoningBank 在效果與效率上均優於儲存原始軌跡或只儲存成功例子的記憶機制；MaTTS 進一步放大收益。
- **記憶驅動的經驗 scaling**：確立了以記憶驅動的經驗 scaling 作為新的 scaling 維度，使 agent 能夠自我進化並展現湧現行為。

## 論文全文

> HTML 全文暫不可用（arxiv HTML 轉換尚未完成）。以下為摘要頁面完整資訊。

**Title**: ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory
**Authors**: Siru Ouyang, Jun Yan, I-Hung Hsu, Yanfei Chen, Ke Jiang
**arXiv ID**: 2509.25140
**Published**: 2025-09-29
**URL**: https://arxiv.org/abs/2509.25140

### Full Abstract

With the growing adoption of large language model agents in persistent real-world roles, they naturally encounter continuous streams of tasks. A key limitation, however, is their failure to learn from the accumulated interaction history, forcing them to discard valuable insights and repeat past errors. We propose ReasoningBank, a novel memory framework that distills generalizable reasoning strategies from an agent's self-judged successful and failed experiences. At test time, an agent retrieves relevant memories from ReasoningBank to inform its interaction and then integrates new learnings back, enabling it to become more capable over time. Building on this powerful experience learner, we further introduce memory-aware test-time scaling (MaTTS), which accelerates and diversifies this learning process by scaling up the agent's interaction experience. By allocating more compute to each task, the agent generates abundant, diverse experiences that provide rich contrastive signals for synthesizing higher-quality memory. The better memory in turn guides more effective scaling, establishing a powerful synergy between memory and test-time scaling. Across web browsing and software engineering benchmarks, ReasoningBank consistently outperforms existing memory mechanisms that store raw trajectories or only successful task routines, improving both effectiveness and efficiency; MaTTS further amplifies these gains. These findings establish memory-driven experience scaling as a new scaling dimension, enabling agents to self-evolve with emergent behaviors naturally arise.

### Key Concepts

**ReasoningBank vs. prior memory approaches**:
- Raw trajectory storage: Stores full interaction history → context bloat, noise
- Success-only memory (e.g., EXPEL, Voyager): Misses failure lessons, incomplete signal
- ReasoningBank: Distills strategies from both successes and failures via self-judgment → higher-quality, generalizable memory

**Memory-aware Test-Time Scaling (MaTTS)**:
- Allocates more compute per task to generate diverse interaction experiences
- These diverse experiences provide richer contrastive signals for memory synthesis
- Improved memory quality feeds back into better scaling effectiveness
- Establishes a synergy loop: better memory → better scaling → better memory

**Self-evolution mechanism**:
1. Agent receives task, retrieves relevant memories from ReasoningBank
2. Agent attempts task, generating multiple experiences (with MaTTS: more diverse attempts)
3. Agent self-judges which experiences were successful vs. failed
4. System distills generalizable reasoning strategies from the contrastive signal
5. New strategies are integrated back into ReasoningBank
6. Repeat → agent capability improves over time

**Benchmarks**: Web browsing tasks + software engineering tasks (likely WebArena, SWE-bench or similar)

**Core claim**: Memory-driven experience scaling is a new scaling dimension distinct from model size scaling or inference compute scaling, enabling genuine agent self-evolution.
