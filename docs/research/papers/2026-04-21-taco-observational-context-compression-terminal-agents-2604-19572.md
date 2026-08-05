---
url: "https://arxiv.org/abs/2604.19572"
title: "A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression"
archived_date: 2026-06-24
arxiv_id: 2604.19572
authors: ["Jincheng Ren", "Siwei Wu", "Yizhi Li", "Kang Zhu", "Shu Xu", "Boyu Feng", "Ruibin Yuan", "Wei Zhang", "Riza Batista-Navarro", "Jian Yang", "Chenghua Lin"]
domains: [cs.CL, "context management"]
html: "https://arxiv.org/html/2604.19572v1"
pdf_path: pdfs/2604.19572.pdf
published_date: 2026-04-21
---

# A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression

**Authors**: Jincheng Ren, Siwei Wu, Yizhi Li, Kang Zhu, Shu Xu, Boyu Feng, Ruibin Yuan, Wei Zhang, Riza Batista-Navarro, Jian Yang, Chenghua Lin
**Published**: April 21, 2026
**Source**: https://arxiv.org/abs/2604.19572 · [HTML](https://arxiv.org/html/2604.19572v1)
**arXiv ID**: 2604.19572
**Categories**: cs.CL, context management
**PDF**: [research/papers/pdfs/2604.19572.pdf](https://arxiv.org/abs/2604.19572) (27 pp, full text archived)

---

## Abstract (quoted)

> As terminal agents scale to long-horizon, multi-turn workflows, a key bottleneck is not merely limited context length, but the accumulation of noisy terminal observations in the interaction history. Retaining raw observations preserves useful environment feedback, but also leads to context saturation and high token cost; conversely, naive compression may discard task-critical signals needed for subsequent actions. Because terminal environments are highly heterogeneous across repositories, commands, and execution states, heuristic-based or fixed-prompt compression methods are difficult to generalize. We propose TACO, a plug-and-play, training-free, self-evolving Terminal Agent Compression framework for existing terminal agents. TACO automatically discovers, refines, and reuses structured compression rules from interaction trajectories, enabling workflow-adaptive filtering of low-value terminal outputs while preserving task-relevant observations. Experiments on TerminalBench (TB 1.0 and TB 2.0) and four additional terminal-related benchmarks, including SWE-Bench Lite, CompileBench, DevEval, and CRUST-Bench, show that TACO consistently improves task performance and token efficiency across agent scaffolds and backbone models. On TerminalBench, TACO yields 1%-4% accuracy gains across strong agentic models and improves accuracy by around 2%-3% under the same token budget. On additional terminal-related benchmarks, it reduces total token consumption while maintaining or improving task success rates. These results suggest that self-evolving, workflow-adaptive observation compression is an effective path toward more reliable and efficient long-horizon terminal agents. The code is publicly available at https://github.com/multimodal-art-projection/TACO.

---

## 結構化摘要

### 核心貢獻

- 提出 **TACO**（Terminal Agent Compression framework）：plug-and-play、training-free、self-evolving 的 observation 壓縮框架，可掛接現有 terminal agent 而無需重新訓練。
- 核心機制：從 interaction trajectory 自動**發現、精化、重用** structured compression rules，達到 workflow-adaptive 的低價值 terminal output 過濾，同時保留 task-critical observations。
- 解決 terminal 環境高度異質性（不同 repo、command、execution state）導致 heuristic / fixed-prompt 壓縮方法難以泛化的問題。
- 在六個 benchmark（TerminalBench TB 1.0/2.0、SWE-Bench Lite、CompileBench、DevEval、CRUST-Bench）上驗證跨 agent scaffold 與 backbone model 的一致性提升。

### 關鍵結果

- **TerminalBench**：accuracy +1%–4%（strong agentic models）；相同 token budget 下準確率提升約 2%–3%。
- **其他四個 terminal-related benchmarks**：在維持或提升 task success rate 的前提下，降低 total token consumption。
- 結果顯示 self-evolving、workflow-adaptive observation compression 是長 horizon terminal agent 提升可靠性與效率的有效路徑。

### 限制

- 論文未列明確 limitation 章節。
- 潛在弱點判斷：(1) self-evolving rule discovery 依賴足夠的 trajectory 資料，cold-start 場景效果未知；(2) compression rules 的品質上限受 backbone model 推理能力限制，弱模型可能產生劣質規則；(3) 實驗僅覆蓋 terminal/code agent 場景，對 browser agent 或其他工具型 agent 的泛化性未驗證。

---

## Workspace 關聯（評估，非既成結論）

- **Context management / NLAH 原則**：TACO 的核心問題（context saturation vs. 壓縮遺失 task-critical signal）直接對應 `context-management.md` 中「Right context > more context」的 NLAH 原則；TACO 的 workflow-adaptive filtering 是此原則在 agent 軌跡層的具體實現。
- **The Loop RECORD 階段 / 自我演化迴圈**：TACO 的 self-evolving rule refinement 與 `core.md` RECORD 階段「task 失敗 → 結構化反思 → 下次同類任務注入」高度同構，可視為該迴圈在 observation compression 層的 automated 版本；⚠️ TACO 屬訓練外 trajectory 挖掘，workspace 的 self-evolution 目前依賴人工 LESSONS.md 更新，自動化程度仍有落差。
- **unverified_success 閘門 / `core.md §PROPOSE 委派`（原 subagent-strategy.md）**：TACO 壓縮後保留「task-relevant observations」的判準問題，對應 `core.md` TEST 階段的 `unverified_success` 閘門——壓縮結果本身是中間態，需確定性驗證才能信任；⚠️ 本庫 `core.md §PROPOSE 委派` 目前無自動化 observation 壓縮機制，落地需額外工程。
- **Token budget / memory-compactor**：TACO 減少 token consumption 的實驗結果與 `context-management.md` token budget 軟性管控（per-task ~4,000 / per-session ~30,000）直接相關；⚠️ workspace 的 `memory-compactor` skill 處理的是跨 session memory 整合，與 TACO 的 intra-session observation 壓縮屬不同層次，概念可互補但不直接等同。
