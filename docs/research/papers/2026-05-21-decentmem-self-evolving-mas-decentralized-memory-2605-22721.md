---
url: "https://arxiv.org/abs/2605.22721"
title: "Self-Evolving Multi-Agent Systems via Decentralized Memory (DecentMem)"
affiliations: ["University of Cambridge", "University of Chicago"]
archived_date: 2026-06-18
arxiv_id: 2605.22721
authors: ["Guangya Hao", "Yunbo Long", "Zhuokai Zhao"]
domains: [cs.MA]
pdf_path: pdfs/2605.22721.pdf
published_date: 2026-05-21
---

# Self-Evolving Multi-Agent Systems via Decentralized Memory (DecentMem)

**Authors**: Guangya Hao (Cambridge), Yunbo Long (Cambridge), Zhuokai Zhao (Chicago)
**Published**: May 21, 2026
**Source**: https://arxiv.org/abs/2605.22721
**arXiv ID**: 2605.22721
**Categories**: cs.MA (Multiagent Systems)
**PDF**: [research/papers/pdfs/2605.22721.pdf](https://arxiv.org/abs/2605.22721) (27 pp, full text archived)

---

## Abstract (quoted)

> Self-evolving multi-agent systems (MAS) have emerged as a promising route to LLM agents that continually improve from experience, with persistent memory at their foundation. However, existing designs almost exclusively adopt a centralized repository shared across agents, incurring communication and coordination overhead, raising privacy concerns, and collapsing agent diversity. We propose DECENTMEM, a decentralized memory framework in which each agent maintains its own dual-pool memory — an exploitation pool of consolidated past trajectories and an exploration pool of LLM-generated candidates for unseen contexts. The two pools are reweighted online based on stage-wise feedback from an LLM-as-a-judge. Theoretically, we prove that this design guarantees global reachability of the solution space and achieves O(logT) cumulative regret, matching the stochastic bandit lower bound up to constants. In practice, across three MAS frameworks (AutoGen, DyLAN, AgentNet), three Qwen3 backbones (4B/8B/14B), two Gemma4 backbones (E2B/E4B) and five benchmarks spanning math, code, QA, and embodied tasks, DECENTMEM improves average accuracy by up to 23.8% over the strongest centralized memory baseline and by up to 52.5% over the no-memory baseline, while reducing token usage by up to 49%.

---

## 結構化摘要

### 問題陳述
集中式共享記憶池（centralized repository）為當前 self-evolving MAS 主流，但有四缺陷：通訊開銷、協調成本、隱私顧慮、**agent 多樣性崩潰**（所有 agent 收斂同一記憶表示 → 失去探索能力）。

### 方法（§4 DecentMem）
- **雙池記憶（§4.1）**：每 agent 獨立維護
  - *Exploitation pool*：整合過去軌跡的鞏固記憶（reuse）
  - *Exploration pool*：LLM 生成的候選，對應未見上下文
- **檢索（§4.2）**：similarity search + threshold filtering，memory-conditioned solving
- **更新（§4.3）**：兩池權重由 **LLM-as-a-judge** 依 stage-wise feedback 線上 reweight，自動平衡 exploit/explore

### 理論保證（§5）
- **全局可達性（§5.2）**：任何解都可被系統發現
- **O(log T) 累積後悔（§5.3）**：達 stochastic bandit 下界（至常數），理論最優
- 每 agent 獨立演化，不依賴全局協調

### 關鍵實驗結果（§6–7）
實驗矩陣：3 MAS 框架（AutoGen / DyLAN / AgentNet）× 3 Qwen3（4B/8B/14B）× 2 Gemma4（E2B/E4B）× 5 benchmark（math/code/QA/embodied）。
- **vs 最強集中式基線**：平均準確率 **+23.8%**，token **-49%**（同時達成，非取捨）
- **vs 無記憶基線**：**+52.5%**
- Cost analysis（§7.2）+ ablation（§7.3）支持雙池設計各自貢獻。

---

## Workspace 關聯（評估，非既成結論）

- **subagent 記憶設計**：本 workspace 所有 subagent 共享 `MEMORY.md`（集中式）；DecentMem 建議 per-agent-type 獨立記憶區塊（researcher/implementer/reviewer）。
- ⚠️ 適用性落差：DecentMem 的增益來自**同一 task 上多輪 self-evolving MAS 跑同質 backbone**；本 workspace 的 subagent 是**單次 fan-out、異質任務、跨 session 人工 MEMORY**——bandit regret 模型的前提（重複 trials、stationary reward）不直接成立。理論最優性 ≠ 對本 workspace 場景的最優性。
- **memory-compactor 演化方向**：可參考 exploitation/exploration 雙區塊壓縮，但需先驗證 workspace 是否真有「多樣性崩潰」病徵（目前無證據）。
- 列為需更多跨 session 數據才能評估的 P2 觀察項。
