---
url: "https://arxiv.org/abs/2605.03195"
title: "Terminus-4B: Can a Smaller Model Replace Frontier LLMs at Agentic Execution Tasks?"
archived_date: 2026-06-09
arxiv_id: 2605.03195
authors: ["Spandan Garg", "Vikram Nitin", "Yufan Huang"]
domains: [cs.AI, cs.SE]
license: CC BY-NC-ND 4.0
pdf_path: pdfs/2605.03195.pdf
published_date: 2026-05-04
tags: [agent, subagent, fine-tuning, SFT, RL, GRPO, token-efficiency, coding-agent, SWE-Bench]
---

# Terminus-4B: Can a Smaller Model Replace Frontier LLMs at Agentic Execution Tasks?

**arXiv**: https://arxiv.org/abs/2605.03195
**Authors**: Spandan Garg, Vikram Nitin, Yufan Huang
**Published**: 2026-05-04 | **Archived**: 2026-06-09

---

## Abstract（原文）

> We explore whether fine-tuning a small language model (SLM) can achieve performance comparable to frontier models on agentic terminal execution tasks. We introduce Terminus-4B, a Qwen3-4B model post-trained via supervised fine-tuning (SFT) and reinforcement learning (RL) with a rule-based LLM-judge reward mechanism. Terminus-4B is able to reduce main agent token usage by approximately 30% with no impact on performance compared to a no-subagent baseline. We conduct extensive evaluation across multiple frontier models, training ablations, and main agent configurations, demonstrating the practical potential of smaller, specialized models for agentic execution subtasks.

**中文說明**：研究核心問題是「4B 小模型能否在代理終端執行任務上媲美前沿模型」。答案是肯定的：Terminus-4B 透過 SFT + RL 訓練後，能讓主代理節省約 30% token，且不影響問題解決率。

---

## 1. Introduction（原文摘錄）

> "Terminal output is often the single largest consumer of context in coding agent trajectories," causing agents to waste tokens processing verbose build logs and test results that could be summarized concisely.

> Modern coding agents delegate specialized subtasks to smaller, focused agent loops. These subagents handle narrow responsibilities such as search, debugging, or terminal execution.

**中文說明**：終端輸出（build log、測試結果）是 coding agent context 最大的消耗源。現代架構趨勢是將此類子任務委派給更小的專門代理——這是本論文的切入點。

---

## 2. Solution Architecture（原文）

The execution subagent is configured with:
- Single Terminal tool access
- 10-turn limit (configurable)
- Structured XML-format responses
- System prompt enforcing concise summaries

**中文說明**：子代理設計極簡：只給一個 Terminal tool、限 10 輪、強制 XML 格式輸出摘要。這種約束設計讓主代理收到的是壓縮過的結果，而非原始終端噪音。

---

## 3. Training Pipeline（原文）

### Phase 1: Supervised Fine-Tuning

- Dataset: ~3,200 execution tasks across 730 GitHub repositories
- Languages: TypeScript (36.5%), C# (27.8%), Java (26.2%), JavaScript (7.1%), Python (2.3%)
- Method: Standard language modeling loss on assistant tokens only
- Duration: 2 epochs with peak learning rate of 2×10⁻⁵

### Phase 2: Reinforcement Learning

- Algorithm: Group Relative Policy Optimization (GRPO)
- Reward Design: Multi-dimensional rubric-based LLM-as-judge scoring:
  - 7 execution quality dimensions
  - 4 failure mode dimensions
  - 3 final-answer quality dimensions
- Formula: `r = (1-α)(s̄pos - s̄pit) + α·s̄fa`, where α=0.5

### Key Innovation: Subagent Rollout Framework

> Researchers decoupled the subagent from the main agent during training by using a lightweight pass-through model as the main agent, ensuring deterministic query forwarding, running rollouts in isolated Docker containers, and eliminating frontier LLM costs during training.

**中文說明**：
- **SFT 階段**：約 3,200 筆執行任務資料，覆蓋 730 個 GitHub repo，以多語言（TypeScript/C#/Java 為主）訓練。
- **RL 階段**：採 GRPO 演算法，獎勵函數由 LLM-as-judge 評分（14 個維度），兼顧執行品質與避免失敗模式。
- **關鍵創新**：訓練時用輕量 pass-through 模型替代前沿 LLM 作主代理，在 Docker 容器隔離執行 rollout，大幅降低訓練成本。

---

## 4. Results（原文）

### SWE-Bench Pro (Multi-language)

| Configuration | Resolution Rate | Token Change |
|---|---|---|
| No Subagent | 30.0% | baseline |
| Opus Subagent | 32.0% | -10.5% |
| Vanilla-4B | 30.4% | +0.5% |
| SFT-4B | 32.4% | -13.0% |
| **Terminus-4B** | **31.5%** | **-12.7%** |

- Main Agent Terminal Calls: Reduced from 3.8 to 1.0 (~74% reduction)
- Subagent→Terminal Rate: 14% (vs. 27% for vanilla model)

### SWE-Bench C# (Internal Benchmark, Claude Opus 4.6 as main agent)

- Token Efficiency: Up to 31.4% reduction in main agent tokens
- Resolution Rate: 46.7% (matched baseline)
- Main Terminal Calls: Reduced from 6.2 to 1.7 calls
- Subagent→Subagent Distrust: 0.23 (matching frontier models)

### No-Terminal Ablation

> When Terminal tool removed entirely: Resolution 45.9% (comparable to Opus baseline of 45.3%), 18.2% frontier token reduction vs. Opus subagent, Subagent Repeat Rate 0.89 (matching Opus at 0.89).

### Cross-Model Generalization

Tested with three main agent models (Claude Opus, Sonnet, GPT-5.3-Codex):
- Consistent token savings: 17–32% reduction
- Stable resolution rates across all configurations
- Terminal usage reduction: 62–79%

### LLM-Judge Evaluation

Terminus-4B achieved comparable quality scores to frontier models across 5 dimensions: task completion, factual accuracy, informativeness, relevance, actionability.

**中文說明**：
- SWE-Bench Pro：Terminus-4B 解決率 31.5% 略低於 SFT-4B（32.4%），但 token 節省幾乎相同（-12.7% vs -13.0%）。重要的是主代理 Terminal 呼叫從 3.8 降至 1.0，代表主代理的「注意力」更集中。
- SWE-Bench C#：使用 Claude Opus 4.6 作主代理，token 節省達 31.4%，解決率維持 46.7%。
- 跨模型泛化：三個主代理（Opus/Sonnet/GPT-5.3-Codex）皆有穩定的 17–32% token 節省，證明子代理本身的設計是可遷移的。

---

## 5. Real-World Impact Example（原文）

> A Serilog C# issue:
> - Baseline: 2.46M main agent tokens across 40 turns with 18 direct terminal calls
> - With Terminus-4B: 740k main agent tokens across 32 turns with subagent handling
> - Result: ~70% token reduction, cleaner context window

**中文說明**：單一真實案例中 token 消耗從 2.46M 降至 740k（減少約 70%），同時輪次從 40 降至 32。這說明子代理不只是節省 token，也讓主代理的推理鏈更乾淨。

---

## 6. Limitations（原文）

- Unix/Bash-focused; limited Windows PowerShell/Command Prompt support
- Evaluation limited to SWE-Bench style benchmarks
- Only trained on Qwen3-4B; unclear transfer to other model families
- May not reflect real-world deployment complexity

**中文說明**：主要限制是平台偏（Unix/Bash）、基準單一（SWE-Bench 風格）、模型族群遷移性未知。實際部署複雜度可能超出論文評估範圍。

---

## 7. Conclusion（原文）

> "Terminus-4B not only closes the gap between the Vanilla Qwen model and frontier models like Claude Sonnet/Opus/GPT-5.3-Codex, but often even exceeds their performance" while enabling up to 30% token reduction for main agents. The approach demonstrates that smaller, specialized models can effectively replace frontier LLMs for narrowly-scoped agentic subtasks.

**中文說明**：核心結論是「範疇明確的子任務可以用小模型替代前沿 LLM」。這個方向對降低 agent 系統成本有直接意義——不需要在每個子任務都呼叫大模型。

---

## Workspace 相關性

- **Sub-agent 策略**：印證 `core.md §PROPOSE 委派`（原 `subagent-strategy.md`）的「任務分類先於委派」——終端執行是典型 on-rails 任務，委派給專門小模型合理
- **Token 預算**：30% 主代理 token 節省與 `context-management.md` 的 per-task budget 直接相關
- **訓練方法**：GRPO + LLM-as-judge 可作為 workspace eval 設計參考（對照 `refs/harness-meta`）
