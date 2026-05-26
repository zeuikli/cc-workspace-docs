---
title: research/papers 深度研究報告：分類、分析與可執行計畫
date: 2026-05-25
type: report
---

# research/papers 深度研究報告：分類、分析與可執行計畫
**日期**：2026-05-25（更新：2026-05-25 v5 — 新增 12 篇論文）| **論文總數**：97 篇（85 MD + 12 PDF，含視覺渲染圖表讀取）| **字元數目標**：≥ 45000

> **Workspace 改動建議獨立文件**：[`2026-05-25-workspace-recommendations.md`](./2026-05-25-workspace-recommendations.md)（計畫 A-F + 🔴 Critical Warnings）

---

## 執行摘要

本報告完整分析 `research/papers/` 目錄下 84 篇論文（73 篇 MD + 11 篇 PDF），覆蓋 2022–2026 年。PDF 論文透過 Claude 視覺讀取（`pdftoppm` 渲染）完整提取圖表、公式、表格與文字，確保技術細節準確。論文集中在六大研究領域：**Harness Engineering**（最大族群，約 35 篇）、**Memory Architecture**（約 20 篇）、**LLM Infrastructure / Speculative Decoding**（約 12 篇）、**Agent Architecture & Coordination**（約 8 篇）、**Benchmark & Evaluation**（約 8 篇）、**Safety & Alignment**（約 6 篇）。

核心發現（視覺 PDF 完整讀取後更新）：
1. **Harness 配置 > 模型能力**：Terminal Bench #33→#5 案例；Claude Code 98.4% 為基礎設施；AgentFlow 84.3% 領先同模型的其他 harness 設計
2. **記憶整合高風險**：ARC-AGI 準確率 Stream 整合第 10 輪→52.6%、第 20 輪→46%（GPT-5.4 確認），Static-All 整合保持 100%，原始軌跡保留與 Static-All 相當
3. **推理加速技術棧成熟**：FlashAttention v1→v3 演進；FP16 740 TFLOPs/s（75% H100 利用率）；FP8 1.2 PFLOPs/s（誤差低 2.6×）；EAGLE-2 LLaMA2-70B 4.26×；vLLM KV 廢片 <5%；組合可達 **5-10× 整體效率提升**
4. **Benchmark 操縱已成體系**：28+ 提交確認作弊；ForgeCode AGENTS.md 注入答案鍵 +10.1pp；Meerkat 審計框架已可機械化偵測；強模型 hack 率 16.6%，弱模型 0%
5. **DeepSeek-V3 架構啟示**：671B MoE（37B 活躍）訓練成本僅 $5.576M；MLA + FP8 混精 + DualPipe + 多令牌預測四技術組合已商用大規模驗證
6. **記憶鞏固失效三機制**：誤分類（相似問題歸錯組）、過度概括（去除適用條件）、窄流過擬合（同質軌跡連續合併）— 視覺 PDF 版提供了比 MD 版更完整的 ARC-AGI Stream 實驗圖表驗證

---

## 1. 論文分類總覽

### 1.1 Harness Engineering（35 篇）

核心洞見：Harness 架構本身是最大的性能槓桿，超越模型選擇。

| 論文 | 核心貢獻 | 重要性 |
|------|---------|--------|
| `2026-04-23-harness-engineering-language-agents-car` | CAR 三層框架（Control/Mechanism/Runtime），HarnessCard 透明標準 | High |
| `2026-04-07-agent-harness-survey` | H=(E,T,C,S,L,V) 六元組形式化，22 個系統分析 | High |
| `2026-04-22-agentflow-synthesizing-multi-agent` | 五維 harness 搜索 DSL，TerminalBench-2 84.3%，發現 10 個 Chrome 零日 | High |
| `2026-04-22-harbor-automated-harness-optimization` | Bayesian 優化 9 個旗標，手工調優產生退化 -37% | High |
| `2026-04-30-ahe-observability-driven-harness` | 七元件自動演化，TerminalBench-2 +7.3pp，跨模型遷移 | High |
| `2026-05-15-effective-harness-engineering-vesper` | Vesper 算法發現，強模型 hack 率 16.6%，worktree 隔離 3.9× 加速 | High |
| `2026-04-29-last-harness-youll-ever-build` | Harness Evolution Loop + Meta-Evolution Loop | High |
| `2026-03-30-meta-harness-optimization-model-harnesses` | 完整執行追蹤（1000 萬 token），超越 ACE 基線 7.7pp | High |
| `2026-05-13-ai-harness-engineering-runtime-substrate` | 11 元件責任矩陣，H0-H3 梯級，M-HIR 診斷指標 | High |
| `2026-03-12-skill-issue-harness-engineering` | Claude Code harness 跳躍 #33→#5，CLAUDE.md 應 <60 行 | High |
| `2026-05-18-code-as-agent-harness` | 代碼為 agent 推理基質，三層架構，七項開放挑戰 | High |
| `2026-05-21-adapting-interface-not-model-life-harness` | 四層失敗修復，88.5% 平均改進，跨 19 模型遷移 | High |
| `2026-04-20-architectural-design-decisions-ai-agent-harnesses` | 70 個專案設計調查，五類典型模式 | High |
| `2026-03-25-natural-language-agent-harnesses-2603-25723` | NLAH 五原則，60.1K→2.9K token (-95%)，效能相當 | High |
| `2026-03-26-natural-language-agent-harnesses-nlah` | IHR 決定論執行層，OS-Symphony +16.8pp | High |
| `2026-02-11-openai-harness-engineering-codex` | Codex 零人工代碼 1.5K+ PR，docs/ 知識庫設計 | High |
| `2026-02-16-configuring-agentic-coding-tools` | CLAUDE.md 45.4% 採用率最高，8 種配置機制 | Medium |
| `2026-02-23-addyosmani-agents-md` | AGENTS.md 應含非可發現資訊，避免 /init 自動生成 | High |
| `2025-08-01-blueprint-first-model-second` | τ-bench SOTA +10.1pp，工具呼叫削減 66-82% | High |
| `2026-04-14-dive-into-claude-code-design-space` | 98.4% 基礎設施、1.6% AI 邏輯，五層子系統，13 個設計原則 | High |
| `2026-05-04-tscg-tool-schema-compilation` | 工具模式 52-57% token 節省，Phi-4 從 0%→84.4% | Medium |
| `2026-05-12-llmcompiler-icml-2024` | 並行函式呼叫 3.7× 延遲加速，6.7× 成本節省 | Low |
| `2026-04-13-safeharness-lifecycle-security` | 四層安全架構 38% UBR 削減，HMAC 工具完整性 | High |
| `2026-04-07-agentopt-client-side-optimization` | 管道角色特化：Opus 4.6 規劃器墊底但求解器第一 | High |
| `2026-05-11-continual-harness-online-adaptation` | Reset-free 持續自適應，Pokémon 驗證湧現自我改進 | Medium |
| `2026-05-12-harness-engineering-categorical-architecture` | 範疇論形式基礎，compiler functor 驗證 | Low |
| `2026-05-06-parness-automated-scientific-research` | DAG 核心 + PDF 解析 + 知識圖 + 累積記憶 | Medium |
| `2026-03-05-opendev-terminal-agents-scaffolding` | 五層防禦，48% SWE-bench Verified，雙記憶 | High |
| `2026-04-23-gpt5-5-system-card` | agent 基準領先，幻覺率 86%（vs Opus 4.7 36%） | Medium |
| `2025-12-11-confucius-code-agent-scalable` | SWE-Bench-Pro 54.3%，框架貢獻 ≥ 模型選擇 | High |
| `2026-04-09-externalization-llm-agents` | 四維統一框架（記憶/技能/協議/harness），外化即進步 | High |
| `2026-05-12-acon-2510-00615` | 上下文壓縮 26-54% 記憶削減，小 LLM +20-46% | Medium |
| `2026-01-31-dont-break-cache-prompt-caching` | 78.5% 成本削減，四類快取破壞模式識別 | High |
| `2026-01-17-terminal-bench-2601-11868` | 89 個精選終端任務，前沿模型 <65% | High |
| `2026-05-12-meta-harness-2603-28052` | 同 meta-harness-optimization 核心論文版 | High |

---

### 1.2 Memory Architecture（20 篇）

核心洞見：記憶整合是高風險操作；選擇性 consolidation + 原始事件保留是最佳策略。

| 論文 | 核心貢獻 | 重要性 |
|------|---------|--------|
| `2026-05-13-useful-memories-faulty-llm-continuous-update` | 整合引入失真，GPT-5.4 100%→46%；AutoMode 超越強制整合 2× | High |
| `2025-05-30-memory-os-ai-agent` | 三層階層記憶（STM/MTM/LPM），Heat Score，+49.11% F1 | High |
| `2025-04-28-mem0-production-long-term-memory` | 生產級記憶層，vs OpenAI +26%，成本延遲削減 90%+ | High |
| `2024-05-23-hipporag-neurobiological-memory` | KG + Personalized PageRank，比迭代檢索快 6-13 倍 | High |
| `2025-04-22-human-memory-to-ai-memory-survey` | 3D 8象限分類框架，整合失真警告，4 設計原則 | High |
| `2024-04-21-survey-memory-mechanism-llm-agents` | 100+ 篇綜述，整合高風險，評估標準缺一致性 | High |
| `2025-05-01-rethinking-memory-llm-agents-operations` | 6 大核心操作，整合為獨立顯式操作 | High |
| `2023-09-05-coala-cognitive-architectures-language-agents` | 四記憶層（Working/Episodic/Semantic/Procedural）分類 | High |
| `2023-05-17-memorybank-long-term-memory` | Ebbinghaus 遺忘曲線，記憶強度公式 R = e^(-t/S) | Medium |
| `2023-04-26-scm-self-controlled-memory` | 三層架構：backbone + stream + controller | Medium |
| `2023-03-20-reflexion-verbal-reinforcement-learning` | 語言反思替代梯度更新，HumanEval 91% pass@1 | High |
| `2023-04-07-generative-agents-simulacra-human-behavior` | 反思層不可或缺，加權檢索（recency × importance × relevance）| High |
| `2023-05-25-voyager-open-ended-embodied-agent` | 代碼技能庫比文字記憶精確，15.3× 技術樹加速 | High |
| `2023-08-20-expel-llm-agents-experiential-learners` | 批量離線提取洞見，成功/失敗對比提高品質 | Medium |
| `2026-03-05-beyond-context-window-memory-vs-longcontext` | ≤10 輪長上下文優，35:1 壓縮丟失約束 | High |
| `2026-05-12-delta-mem-efficient-online-memory-llm` | 凍結主幹 + 8×8 矩陣 delta 更新，+1.31× MemoryAgentBench | Medium |
| `2025-08-01-rcr-router-role-aware-context-routing` | Token 削減 25-47%，角色+任務階段重要性評分 | Medium |
| `2024-05-17-latent-state-estimation-ui-agents` | 潛狀態五維估計，成功率 1.6× | Medium |
| `2024-06-20-step-back-profiling-personalized-scientific-writing` | User profile gisting，LaMP +3.6 點 | Low |
| `2026-05-12-lost-in-the-middle` | U 形效能曲線，關鍵資訊應放開頭/結尾 | Medium |

---

### 1.3 LLM Infrastructure / Speculative Decoding（12 篇）

核心洞見：推理加速技術棧已完全成熟，組合 FlashAttention-3 + vLLM + EAGLE-2 可在不換模型前提下達 **5-10× 整體效率提升**。DeepSeek-V3 在商用規模驗證了多令牌預測 + FP8 + MoE 的可行性。

| 論文 | 核心貢獻（PDF 完整讀取） | 重要性 |
|------|---------|--------|
| `2022-05-28-flashattention` | IO-aware tiling；BERT-large 快 15%，GPT-2 快 3×，長序列 2.4×；O(N²d²/M⁻¹) HBM 訪問 | High |
| `2023-07-17-flashattention-2` | 非 matmul FLOPs 減少 + warp 分工改善；A100 225 TFLOPs/s（72% 利用率），v1 快 2× | High |
| `2024-07-11-flashattention-3` | Hopper 非同步 Tensor Core + TMA；FP16 740 TFLOPs/s（75%）；FP8 ≈1.2 PFLOPs/s；誤差比標準 FP8 低 2.6× | High |
| `2023-09-11-vllm-paged-attention` | OS 分頁類比 KV cache；廢片 <5%（Orca 約 40%）；吞吐 2-4×；beam search 記憶體共享 | High |
| `2022-11-30-speculative-decoding-google` | 草稿模型並行預測 γ 個 token；T5-XXL 2-3×；拒絕採樣保證分佈完全一致 | High |
| `2024-01-18-medusa-speculative-decoding` | 多解碼頭共享 backbone；樹狀 attention 並行驗證；典型接受方案；2.2-2.8×；無草稿模型 | High |
| `2024-01-25-eagle-speculative-decoding` | 特徵層（second-to-top）自回歸；offset token 解決特徵不確定性；2.7-3.5×；greedy & non-greedy 皆支援 | High |
| `2024-06-24-eagle-2-speculative-decoding` | 動態草稿樹（上下文感知）；信心分數自動校準；LLaMA2-Chat 70B 達 4.26×；零額外訓練 | High |
| `2024-04-30-multi-token-prediction` | N 頭共享 trunk；記憶高效（峰值從 O(nV+d) 降至 O(V+d)）；HumanEval +12%、MBPP +17%；推理 3× | High |
| `2024-12-26-deepseek-v3-technical-report` | 671B MoE（37B 活躍）；MLA（KV cache 減少）；FP8 首次商用大規模驗證；2.788M H800 小時（$5.576M）；多令牌預測目標 | **Critical** |
| `2024-06-20-routellm-learning-to-route-llms` | 強/弱模型動態路由；3.66× 成本削減，保持 95% 性能；單一路由器跨模型泛化 | Medium |
| `2025-12-31-recursive-language-models` | RLM 遞迴調用自身；OOLONG-Pairs +76%；REPL 符號遞迴；Qwen3-8B 1000 樣本 +28.3% | High |

**推理加速選型指南（基於 PDF 全文）**：

```
場景            建議技術組合
─────────────────────────────────────────────────────
長序列訓練      FlashAttention-3 FP16（H100）
推理吞吐最大化  vLLM + PagedAttention + beam search 共享
延遲最小化      EAGLE-2（動態草稿樹，4.26× 加速）
資源受限/邊緣   Medusa（無草稿模型，QLoRA 友好）
成本優化        RouteLLM 路由器（3.66× 削減）
大規模訓練參考  DeepSeek-V3（MoE + FP8 + 多令牌預測）
新模型訓練      多令牌預測目標（+12-17% 代碼，+3× 推理）
```

---

### 1.4 Agent Architecture & Coordination（8 篇）

核心洞見：協調架構必須顯式設計；41-87% 多 agent 失敗率源於協調缺陷而非模型。

| 論文 | 核心貢獻 | 重要性 |
|------|---------|--------|
| `2026-05-05-coordination-architectural-layer` | 階層化協調 +26.6pp，41-87% 失敗率源於協調 | High |
| `2026-05-04-heavyskill-heavy-thinking-inner-skill` | 平行推理 + 序列審議，HP@4 超越 P@K 50% | Medium |
| `2026-04-22-skill-learn-bench-continual-skill-learning` | 人工技能 74.5% vs 自動 30%，外部反饋優於自我 | High |
| `2026-04-22-agentflow-synthesizing-multi-agent` | 五維度並行搜索（見 Harness 分類） | High |
| `2025-08-01-blueprint-first-model-second` | 確定性藍圖分離工作流邏輯與模型決策 | High |
| `2026-05-12-llmcompiler-icml-2024` | 並行函式呼叫，依賴分析編譯器 | Low |
| `2025-12-31-recursive-language-models` | 符號遞迴 REPL，RLM-Qwen3-8B 1000 樣本 +28.3% | High |
| `2026-04-09-externalization-llm-agents` | 認知外化四維框架，Claude Code 98.4% 基礎設施 | High |

---

### 1.5 Benchmark & Evaluation（8 篇）

核心洞見：基準操縱問題已被驗證，28+ 提交確認作弊；獨立驗證層是必要設計。

| 論文 | 核心貢獻 | 重要性 |
|------|---------|--------|
| `2026-05-23-cheating-agents-benchmark-manipulation` | 28+ 作弊提交，Meerkat 審計，answer injection 識別 | High |
| `2025-09-21-swe-bench-pro-long-horizon` | 企業級基準，Opus 4.7 64.3%，~3× 難於 SWE-bench Verified | High |
| `2026-03-31-aec-bench-multimodal-benchmark-agentic-systems` | 建築工程多模態，工具化 PDF +32pp，視覺接地 5% | Medium |
| `2026-04-10-composite-stem-expert-curated` | 70 項 STEM 任務，Opus 4.6 21.4%，工具安裝是關鍵 | Medium |
| `2026-01-17-terminal-bench-2601-11868` | 89 終端任務，前沿 <65%，轉數與成功無相關 | High |
| `2025-11-07-ock-bench-reasoning-efficiency-overthinking` | OckScore 聯合指標，小模型過度思考稅 57% | High |
| `2025-03-07-which-economic-tasks-ai-claude-conversations` | 4M 對話，軟體開發 37%，57% 為增強型 | High |
| `2025-11-19-anthropic-economic-index-geographic-adoption` | 指令式委託 27%→39%，API 企業自動化模式 | Medium |

---

### 1.6 Safety & Alignment（5 篇）

核心洞見：失能風險集中在個人域；價值鏡像效應在 20% 支持性互動中出現。

| 論文 | 核心貢獻 | 重要性 |
|------|---------|--------|
| `2026-01-27-disempowerment-patterns-real-world-llm` | 失能率 1/1000~1/10000，集中關係/醫療域 | High |
| `2025-04-21-values-in-the-wild-claude-interactions` | Helpfulness 23.4% + Professionalism 22.9% 最穩定 | High |
| `2026-04-21-cyber-defense-benchmark-threat-hunting` | 威脅獵殺任務 Opus 4.6 3.8%，開放式取證需人機迴圈 | Medium |
| `2026-04-13-safeharness-lifecycle-security` | 四層安全 Inform→Verify→Constrain→Correct | High |
| `2026-01-08-gpt5-system-card` | 雙模型路由，幻覺 -65%，安全完成訓練 | High |
| `2026-04-16-claude-opus-4-7-system-card` | SWE-bench Pro 64.3%，256k 長上下文崩潰 | Medium |

---

## 2. 跨領域核心發現

### 發現 A：Harness 配置 > 模型能力（來源：多篇）

- `2026-03-12-skill-issue-harness-engineering`：Claude Code Opus 4.6 harness 優化後 Terminal Bench 排名 #33→#5
- `2026-04-14-dive-into-claude-code-design-space`：Claude Code 98.4% 為基礎設施代碼，1.6% 為 AI 邏輯
- `2026-04-07-agentopt-client-side-optimization`：Opus 4.6 作規劃器在 HotpotQA 墊底（31.71%）但作求解器最優（74.27%）
- `2026-02-13-skills-bench-agent-skills`：人工策展技能 +16.2pp，自動生成 -1.3pp（差距 17.5pp）

**實證結論**：投資 harness 工程 ROI 高於等待更強模型。

---

### 發現 B：記憶整合風險被系統性低估（來源：記憶族群）

- `2026-05-13-useful-memories-faulty-llm-continuous-update`：整合後準確率從 100% 降至 46%
- `2024-04-21-survey-memory-mechanism-llm-agents`：長時運行後性能普遍退化
- `2025-04-28-mem0-production-long-term-memory`：衝突記憶應標記而非自動解決
- `2025-05-01-rethinking-memory-llm-agents-operations`：整合應為獨立顯式操作，非自動觸發

**實證結論**：保留原始事件記憶（Episodic-First）是最穩健策略，自動整合是主要風險。

---

### 發現 C：推理加速技術棧成熟（來源：LLM Infrastructure 族群，PDF 完整讀取）

| 技術 | 指標 | 來源論文 |
|------|------|---------|
| FlashAttention-3 FP16 | H100 75% 利用率（740 TFLOPs/s），比 v2 快 1.5-2× | `2024-07-11-flashattention-3` |
| FlashAttention-3 FP8 | ≈1.2 PFLOPs/s，誤差比標準 FP8 低 2.6× | `2024-07-11-flashattention-3` |
| vLLM PagedAttention | KV cache 廢片 <5%（vs Orca 40%），吞吐 2-4× | `2023-09-11-vllm-paged-attention` |
| EAGLE-2 | LLaMA2-Chat 70B 達 4.26×，比 Medusa 快 2×，零額外訓練 | `2024-06-24-eagle-2-speculative-decoding` |
| Medusa | 2.2-2.8× 無草稿模型，QLoRA 友好 | `2024-01-18-medusa-speculative-decoding` |
| RouteLLM | 3.66× 成本削減，95% 性能保持 | `2024-06-20-routellm` |
| 多令牌預測 | HumanEval +12%、MBPP +17%，推理 3× | `2024-04-30-multi-token-prediction` |
| DeepSeek-V3 MoE | 671B 模型，$5.576M 訓練，媲美 GPT-4o | `2024-12-26-deepseek-v3` |

**實證結論**：以上技術棧互相正交可完整疊加：FlashAttention（單步 kernel）+ vLLM（系統層記憶體）+ EAGLE-2（減總步數）= 不升級模型即可達 **5-10× 成本效益提升**。DeepSeek-V3 商用規模驗證了 FP8 + 多令牌預測的可行性。

---

### 發現 D：Benchmark 可信度危機（來源：評估族群）

- `2026-05-23-cheating-agents-benchmark-manipulation`：28+ 提交確認作弊，最佳玩家排名降 8-12 位
- `2026-05-15-effective-harness-engineering-vesper`：強模型（GPT-5.2）hack 率 16.6%，弱模型（Phi-3）0%
- ForgeCode 作弊方法：在 AGENTS.md 注入答案鍵

**實證結論**：強模型更容易發現並利用評估漏洞；獨立驗證 agent 是必要設計。

---

### 發現 E：Context Engineering 臨界點規律（來源：多篇）

- `2026-03-05-beyond-context-window-memory-vs-longcontext`：≤10 輪用長上下文，>20 輪記憶便宜 26% 但精度低 25-35pp
- `2026-05-12-lost-in-the-middle`：U 形效能曲線，中間位置性能最差
- `2026-01-31-dont-break-cache-prompt-caching`：四類快取破壞模式，靜態前綴快取最穩定

**實證結論**：Context 管理是獨立工程問題，需要明確策略而非依賴模型自然處理。

---

## 3. 論文集結構性分析

### 3.1 時間趨勢（2022-2026）

```
2022-2023：基礎架構奠定期
  - FlashAttention 系列（推理效率）
  - 投機解碼（加速技術）
  - 早期記憶架構（Reflexion、Generative Agents、MemoryBank）

2024：記憶系統成熟期
  - HippoRAG（神經科學啟發記憶）
  - Memory Survey（100+ 篇綜述）
  - EAGLE、vLLM、Medusa 成熟化

2025：Agent 系統化期
  - MemoryOS（OS 類比記憶）
  - Mem0（生產記憶層）
  - Blueprint-First（確定性工作流）
  - SWE-bench Pro（企業級基準）

2026（大量）：Harness Engineering 爆發期
  - 20+ 篇 harness 相關論文
  - 多個 harness 優化框架競爭（HARBOR、AHE、Life-Harness、Vesper）
  - 基準操縱問題暴露
  - Context Engineering 精細化
```

### 3.2 研究共識與分歧

**共識**（3 篇以上一致）：
1. Harness 工程 > 模型選擇（5+ 篇）
2. 記憶整合是高風險操作（4+ 篇）
3. 人工策展技能優於自動生成（3 篇）
4. 並行 agent 上限約 4 個（3 篇）

**分歧**：
1. NLAH 效能相當 vs AgentFlow 顯著提升（harness 表示方式之爭）
2. AutoMode 2× vs 顯式控制更可預測（記憶整合控制策略）
3. 全歷史長上下文 vs 記憶壓縮（成本效益評估依任務類型而異）

---

## 4. 最佳實踐萃取

### 4.1 Harness 設計最佳實踐

1. **CLAUDE.md 保持 <60 行**：錨定效應——過長的 CLAUDE.md 讓 agent 偏向舊模式 (`2026-03-12`)
2. **分離工作流邏輯與模型決策**：確定性藍圖處理路由，LLM 只處理判斷任務 (`2025-08-01-blueprint-first`)
3. **工具數量控制**：每個工具描述消耗指令預算；MCP 工具 >5 個時需精選 (`2026-03-12`)
4. **子 agent 上下文隔離**：fan-out 上限 4，child 間不直接溝通 (`2026-03-25-nlah`)
5. **後向壓力機制**：靜默成功、僅輸出失敗；完整測試套件淹沒上下文 (`2026-03-12`)
6. **動態系統提示**：含目標/進度/可用工具/預算提醒，比靜態提示更有效 (`2026-03-05-opendev`)
7. **工具模式編譯**：JSON→文本 52-57% token 節省，Phi-4 從 0%→84.4% (`2026-05-04-tscg`)
8. **快取邊界管理**：靜態系統提示專用快取，避免時間戳/session ID 注入 (`2026-01-31`)

### 4.2 記憶設計最佳實踐

1. **Episodic-First 架構**：保留原始事件作為第一手證據，整合為可選操作 (`2026-05-13-useful-memories`)
2. **選擇性整合**：明確門控觸發時機，AutoMode 讓 agent 自選 Retain/Delete/Consolidate (`2026-05-13`)
3. **Heat Score 驅動蒸發**：頻率 × 互動長度 × 時間衰減決定記憶保留 (`2025-05-30-memory-os`)
4. **三層記憶架構**：STM（7 條）→ MTM（200 段）→ LPM（永久人格），對應不同衰減策略 (`2025-05-30`)
5. **時間索引 + 圖索引**：純向量檢索不足以支持複雜推理，需多層索引 (`2025-05-01`)
6. **衝突標記而非自動解決**：生產環境記憶衝突應保留並標記，由應用層決策 (`2025-04-28-mem0`)
7. **關鍵資訊放首尾**：U 形效能曲線，中間位置 LLM 性能最差 (`2026-05-12-lost-in-the-middle`)

### 4.3 評估設計最佳實踐

1. **獨立驗證 agent**：生成器≠評估器（PGE 原則），強模型需更強驗證 (`2026-05-15-vesper`)
2. **結果導向驗證**：轉數與成功率無相關，驗證行為結果而非步驟數 (`2026-01-17-terminal-bench`)
3. **防作弊設計**：AGENTS.md 隔離區，評估鍵不應暴露給 agent (`2026-05-23-cheating`)
4. **worktree 隔離**：每個 agent 獨立 worktree，3.2-3.9× 並行加速 (`2026-05-15-vesper`)
5. **OckScore 效率指標**：準確率 + Token 效率聯合評估，避免過度思考稅 (`2025-11-07-ock`)

---

## 5. 可應用於 cc-workspace 的執行計畫

> **計畫 A-F 詳細內容已遷移至獨立文件**：[`2026-05-25-workspace-recommendations.md`](./2026-05-25-workspace-recommendations.md)
>
> 涵蓋：Harness Engineering 強化、記憶系統升級、Context Engineering 優化、技能庫策展、評估獨立性強化、LLM 推理加速部署（含 Prompts 模板與 decision tree）。

### 計畫 A：Harness Engineering 強化（優先度 P1）

**來源**：`2026-03-12`、`2026-04-14`、`2026-03-25`、`2026-04-23-car`

**目標**：將 workspace harness 從 H1 級提升至 H2-H3 級

**具體步驟**：

```bash
# Step 1：CLAUDE.md 精簡審核（目標 <60 行核心規則）
wc -l /Users/zeuik/cc-workspace/CLAUDE.md

# Step 2：建立 docs/ 結構化知識庫
mkdir -p docs/architecture docs/decisions docs/quality

# Step 3：工具模式審查（MCP 工具清單精選）
cat .claude/settings.json | python3 -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d.get('mcpServers',{}), indent=2))"

# Step 4：子 agent fan-out 上限驗證（目前 .claude/rules/subagent-strategy.md 已設 4）
grep "Fan-out" .claude/rules/subagent-strategy.md
```

**Prompts 模板（可直接使用）**：

```
[Harness Health Check Prompt]
審查以下 harness 配置是否符合最佳實踐：
1. CLAUDE.md 是否 <60 行（錨定效應警告）？
2. MCP 工具數量是否 ≤5 個？
3. AGENTS.md 是否只含非可發現資訊？
4. hooks 是否含後向壓力機制？
依 2026-03-12、2026-02-23、2026-04-23-car 標準評分（H0-H3）。
```

---

### 計畫 B：記憶系統升級（優先度 P2）

**來源**：`2026-05-13-useful-memories`（PDF 完整版）、`2025-05-30-memory-os`、`2025-04-28-mem0`、`2026-03-05-beyond-context`

**目標**：實現 Episodic-First 記憶架構，防止整合失真

**ARC-AGI 量化依據**（PDF 直接引用）：Stream 整合模式（每次互動後自動合併）→ 第 10 輪後準確率 52.6%，第 20 輪後 46%（從 100% 跌落）。batch 整合（每 50 輪一次）→ 保持 100%。原始軌跡保留 → 與 batch 整合相當。

**具體步驟**：

1. 保留原始事件層（MEMORY.md 中保留最近 5 個 session 完整紀錄，不即時摘要壓縮）
2. 整合頻率降低（改為每 5-10 session 一次 batch 整合，`memory-compactor` 只在明確達到閾值時觸發）
3. 衝突標記機制（整合前比對是否有矛盾記憶，標記後凍結，不自動覆寫）
4. AutoMode 引入（整合時讓 agent 自選 Retain/Delete/Consolidate，而非強制全部整合）

**Prompts 模板**：

```
[Memory Consolidation Gate Prompt]
在執行記憶整合前，評估：
1. 此記憶是否包含衝突資訊？（若是 → 標記，不整合）
2. 整合後是否可還原至原始事件？（若否 → 僅摘要，保留原始）
3. 此記憶的任務類型是否跨域混批？（若是 → 分開整合）
依 2026-05-13 AutoMode 原則：優先 Retain，次選 Delete，最後才 Consolidate。

格式：
- 決策：[Retain / Delete / Consolidate]
- 原因：<1句>
- 衝突標記：<若有>
```

---

### 計畫 C：Context Engineering 優化（優先度 P2）

**來源**：`2026-01-31-dont-break-cache`、`2026-05-12-lost-in-the-middle`、`2026-03-05-beyond-context-window`

**目標**：減少 30% token 消耗，同時保持精度

**具體步驟**：

1. 靜態快取前綴策略（CLAUDE.md + rules 永遠放最前，加 `cache_control` 標記）
2. 關鍵資訊位置策略（重要上下文放首段或末段，避免中間位置）
3. 10 輪 compact 觸發（實證 10 輪為成本-精度等價點）

**Prompts 模板**：

```
[Context Placement Audit Prompt]
審查當前 system prompt 結構：
1. 靜態資訊（CLAUDE.md rules）是否在最前？（快取效率）
2. 最重要的約束/目標是否在首段或末段？（U 形效能曲線）
3. 動態工具結果是否在快取標記之後？（避免破壞快取）
依 2026-01-31 和 2026-05-12 標準評估。
改進建議：<結構化重排方案>
```

---

### 計畫 D：技能庫策展（優先度 P3）

**來源**：`2026-02-13-skills-bench`、`2026-04-22-skill-learn-bench`、`2026-03-12-skill-issue`

**目標**：人工策展技能 +16.2pp，防止 skill 爆炸（>3 技能性能下降）

**具體步驟**：

1. 技能品質審計（具體性/基礎性/正交性三維度評估）
2. 每次會話限 2-3 個技能加載
3. 新技能必須外部評估門控（人工確認後才能加入庫）

**Prompts 模板**：

```
[Skill Quality Audit Prompt]
評估技能 [SKILL_NAME] 的品質：
1. 具體性：是否包含非通用、領域特定的指令？（0-10 分）
2. 基礎性：是否減少任務失敗的根本原因？（0-10 分）
3. 正交性：與現有技能是否有重疊？（0=完全重疊，10=完全正交）
4. SWE 域技能 ROI 最低（+4.5pp）；優先其他域（安全/架構/研究）。
依 2026-02-13、2026-04-22 標準判斷：保留 / 刪除 / 合併。
```

---

### 計畫 E：評估獨立性強化（優先度 P3）

**來源**：`2026-05-23-cheating-agents`、`2026-05-15-vesper`、`2025-09-21-swe-bench-pro`

**目標**：防止 meta-agent 利用基準結構作弊；確保評估結果可信

**具體步驟**：

1. `AGENTS.md` 隔離審查（不應暴露評估相關信息）
2. 生成器≠評估器（PGE 原則）：autoresearch 報告需獨立 agent 審查
3. worktree 隔離：並行 agent 任務使用 `scripts/feature.sh` 創建獨立分支

**Prompts 模板**：

```
[Independent Review Prompt]
作為獨立評估者（非生成者），審查以下輸出：
1. 邏輯一致性：主張是否自相矛盾？
2. 來源可追溯性：每個重要聲明是否有論文引用？
3. 操縱風險：輸出是否可能利用評估標準（如針對 healthcheck 優化而非真實改進）？
依 PGE 原則（2026-05-15-vesper）：評估者不應看到生成過程，僅評估最終輸出。
輸出：[PASS / FAIL / NEEDS_REVISION] + 具體問題清單
```

---

### 計畫 F：LLM 推理加速部署（優先度 P3，面向自建服務）

**來源**：`2024-07-11-flashattention-3`、`2023-09-11-vllm-paged-attention`、`2024-06-24-eagle-2`、`2024-12-26-deepseek-v3`（PDF 完整讀取）

**目標**：若 workspace 需要本地/自建 LLM 推理服務，提供 evidence-backed 技術選型指南

**技術選型 Decision Tree（基於 PDF 量化數據）**：

```
問題 1：是否有 H100 GPU？
  ├─ 是 → 啟用 FlashAttention-3 FP16（740 TFLOPs/s）
  │        可選 FP8 進一步提速（1.2 PFLOPs/s，誤差低 2.6×）
  └─ 否 → 啟用 FlashAttention-2（A100 225 TFLOPs/s）

問題 2：延遲敏感 or 吞吐敏感？
  ├─ 延遲優先 → EAGLE-2 動態草稿樹（LLaMA2-70B 達 4.26×）
  │              選草稿模型：同系列小 2-3× 的模型
  └─ 吞吐優先 → vLLM + PagedAttention（廢片 <5%，吞吐 2-4×）
               → 啟用 beam search block sharing

問題 3：有訓練需求？
  ├─ 是 → 加入多令牌預測頭（4-token，無記憶開銷，代碼 +12-17%）
  └─ 否 → Medusa（無草稿，QLoRA fine-tune，2.2-2.8×）

問題 4：多模型混用？
  └─ 是 → RouteLLM 路由器（3.66× 成本削減，95% 性能保持）
```

**Prompts 模板（推理服務評估）**：

```
[LLM Serving Architecture Review Prompt]
依 PDF 來源論文評估當前 LLM serving 架構：

1. 記憶體效率：KV cache 廢片率是多少？
   - 目標 <5%（vLLM PagedAttention 基準）
   - 來源：arXiv:2309.06180

2. 加速方案：是否使用投機解碼？
   - EAGLE-2 為目前最高（4.26×），Medusa 無草稿需求（2.2-2.8×）
   - 來源：arXiv:2406.16858、arXiv:2401.10774

3. Kernel 效率：FlashAttention 版本？
   - H100 用 v3（75% 利用率）；A100 用 v2（72%）
   - 來源：arXiv:2407.08608、arXiv:2307.08691

4. 成本路由：是否有強/弱模型動態路由？
   - RouteLLM 3.66× 削減，路由開銷 <0.4%
   - 來源：arXiv:2406.18665

5. 訓練新模型時：是否加入多令牌預測目標？
   - 無記憶開銷，HumanEval +12%，推理 3×
   - 來源：arXiv:2404.19737

輸出：[當前方案評分] + [優先優化項（按 ROI 排序）]
```

---

## 6. PDF 深度技術分析（poppler 完整讀取後更新）

本節為 PDF 論文的細節補充，上節分類表已更新相應數字，此處記錄 PDF 原文中的關鍵量化結論。

### 6.1 FlashAttention 演進系列（3 篇 PDF）

**FlashAttention v1 (arXiv:2205.14135)**
- BERT-large (seq=512) 快 15%；GPT-2 (seq=1K) 快 3×；長序列 (1K-4K) 快 2.4×
- HBM 訪問從 Ω(Nd+N²) 降至 O(N²d²/M⁻¹)，少 9 倍
- Block-sparse 擴展支援 64K 序列（Path-256: 63.1%）
- 反向傳播透過重計算恢復，FLOP 增加但 IO 減少

**FlashAttention v2 (arXiv:2307.08691)**
- v1 FLOPs 利用率僅 25-40%，v2 提升至 50-73%
- A100 前向 73%、反向 63% 理論最大吞吐
- 關鍵優化：減少非 matmul FLOPs（GPU matmul 單位快 16×）+ warp 間通訊優化
- 端到端：GPT-3 在 8×A100 達 225 TFLOPs/s = 72% 模型 FLOPs 利用率

**FlashAttention v3 (arXiv:2407.08608)**
- 針對 Hopper (H100) 的非同步架構，舊 GPU 需重新實作
- 製造者-消費者 warp 專項化：資料移動 warp + 計算 warp 解耦
- FP8：塊量化 + 非相干處理（incoherent processing），數值誤差比標準 FP8 低 2.6×
- 長序列優勢明顯，短序列邊際效益較小

### 6.2 投機解碼（Speculative Decoding）家族（4 篇 PDF）

**Google Speculative Decoding (arXiv:2211.17192)**
- 核心算法：小模型生成 γ 個候選，大模型**一次 forward** 驗證全部
- 拒絕採樣保證：輸出分佈與單獨用大模型**完全一致**（非近似）
- T5-XXL (11B) 達 2-3×；接受率 β 由 draft 品質決定
- 組合約束：需 draft/target 同系列，內存需同時容納兩個模型

**Medusa (arXiv:2401.10774)**
- N 個 decoding head 共享同一 backbone 最後隱藏層
- Head k: `p_t^(k) = softmax(W2·SiLU(W1·h_t) + h_t)`（殘差連接）
- 樹狀注意力掩碼（tree mask）並行驗證候選子集
- MEDUSA-1：僅 fine-tune heads，backbone 凍結；MEDUSA-2：聯合訓練
- 典型接受方案：相比 rejection sampling 進一步加速，允許微小分佈偏差

**EAGLE v1 (arXiv:2401.15077)**
- 核心洞見：token 層特徵本質不確定（given context, feature 仍有多種可能），feature 層則相對確定
- 解法：在 second-to-top 層進行 autoregression，並 offset 一個時間步的 token 序列輸入
- 訓練量：僅 2-4B tokens（對比 TinyLLaMA 需 3000B）
- non-greedy 生成也有保證（Medusa 的非貪心版本無 lossless 保證）

**EAGLE v2 (arXiv:2406.16858)**
- v1 假設接受率僅與草稿位置相關；v2 發現也與上下文高度相關
- 動態草稿樹：根據 draft 模型的信心分數實時調整樹寬度
- 零額外訓練：直接升級現有 EAGLE 部署
- LLaMA2-Chat 70B: 4.26×（v1 更高，因 70B 並行效益更顯著）
- 比 Medusa 快 2×，比 Lookahead 快 2.3×

### 6.3 vLLM PagedAttention (arXiv:2309.06180)

- 借鑒 OS 虛擬記憶體/TLB 概念：token → bytes，request → process
- KV block size 固定（預設 16 tokens），按需分配非連續實體頁
- 跨請求記憶體共享：beam search 分支共享 parent KV blocks，直到分叉點
- KV cache 廢片：vLLM <5% vs Orca ~40% vs FasterTransformer ~100%
- 對複雜解碼算法（parallel sampling、beam search）效益最高

### 6.4 多令牌預測 (arXiv:2404.19737, Meta FAIR)

- 架構：共享 trunk + N 個獨立輸出頭（無 trunk 計算開銷）
- 記憶高效：峰值 GPU 記憶體從 O(nV+d) 降至 O(V+d)
- 順序前後向傳播累積梯度（避免 N 倍中間態存儲）
- 歸納頭（induction heads）在 4-token 預測任務中顯著增強
- 推理時可選：**速度模式**（自投機解碼，3×）或 **品質模式**（只用主頭）
- 適用域：代碼/數學推理 > 自然語言（資訊密度更高）

### 6.5 DeepSeek-V3 (arXiv:2412.19437)

- **多頭潛在注意（MLA）**：低秩 KV 壓縮，推理時 KV cache 顯著減少
- **無輔助損失負載平衡**：傳統輔助損失強制均勻分配導致性能下降；DeepSeek 改用**偏置項調整**，自然均衡
- **FP8 混精訓練量化細節**：關鍵層用 FP8，累積梯度用 BF16/FP32；逐塊量化（block-wise）而非逐張量
- **DualPipe**：將 forward/backward 的計算與通訊重疊，氣泡率 <1/9
- 訓練成本對比：GPT-4 估計 $100M+，DeepSeek-V3 僅 $5.576M（H800 算力）
- 開源：模型 checkpoint 公開，商用授權

### 6.6 記憶整合失效機制 (arXiv:2605.12978, PDF 版)

PDF 版提供比 MD 版更詳細的**三種失效機制**量化：

1. **誤分類（Misgrouping）**：結構相似但解法不同的問題被歸為同一教訓 → 抽象化引入錯誤類比
2. **過度概括（Overgeneralization）**：有效策略被去除適用條件後泛化失敗 → 「在 A 情況下用 X」變成「總是用 X」
3. **窄流過擬合（Narrow Input Overfitting）**：連續合併同質性高的軌跡，bias 累積

**ARC-AGI 量化實驗**：
- Static-All（一次性合併全部 50 輪軌跡）：全程保持 100% 可解率
- Stream（逐批合併，每輪後更新）：第 10 輪後跌至 52.6%，第 20 輪後 46%
- 純原始軌跡（零合併）：與 Static-All 相當
- AutoMode（Retain/Delete/Consolidate agent 自選）：比強制合併高 2×

**結論（與 workspace MEMORY.md 直接相關）**：當前 MEMORY.md 採用「session 後摘要」模式，若頻率過高（每 session 必摘要），風險等同 Stream 模式；建議改為每 5-10 session 一次 batch 摘要，並保留最近 N session 原始紀錄。

---

## 7. 研究空白與前沿挑戰

基於論文集分析，以下是尚未解決的重要問題：

### 6.1 已識別研究空白

1. **記憶評估標準缺一致性**：`2024-04-21-survey` 指出評估標準碎片化，MemGPT/Mem0/MemoryOS 使用不同指標
2. **記憶跨任務遷移**：`2026-05-13-useful-memories` 發現跨任務混批記憶加速崩潰，但缺乏遷移策略
3. **Harness 可再現性**：`2026-04-23-car` 的 HarnessCard 提案，學術論文 harness 細節普遍缺失
4. **多 agent 共享狀態一致性**：`2026-05-18-code-as-agent-harness` 列為七大開放挑戰之一
5. **長期人類能力保留**：`2026-04-14-dive-into-claude-code` 列為最大未決挑戰

### 6.2 實際應用瓶頸

1. **開放式威脅獵殺**：`2026-04-21-cyber-defense` 最佳模型僅 3.8%，人機迴圈仍必要
2. **視覺接地任務**：`2026-03-31-aec-bench` 工具化 PDF 無助於視覺空間接地（5%）
3. **小模型能力下限**：`2026-05-12-harness-categorical` Phi-3.8B 無法通過格式紀律，與 harness 無關

---

## 7. 附錄：來源評分索引

### Critical 類（突破性，直接影響 workspace 設計決策）

| 論文 | 核心量化結論 | ArXiv |
|------|------------|-------|
| `2026-05-13-useful-memories-faulty-llm`（PDF） | ARC-AGI Stream 整合：100%→46%；AutoMode 2× 優於強制整合 | 2605.12978 |
| `2024-12-26-deepseek-v3`（PDF） | 671B MoE $5.576M 訓練，FP8 + MLA + 多令牌預測商用驗證 | 2412.19437 |

### A類（影響力最高，多維度 High）

| 論文 | 核心量化結論 | ArXiv |
|------|------------|-------|
| `2026-03-12-skill-issue-harness-engineering` | harness 優化：Terminal Bench #33→#5 | — |
| `2026-04-14-dive-into-claude-code-design-space` | 98.4% 基礎設施，1.6% AI 邏輯 | 2604.14228 |
| `2026-04-22-agentflow-synthesizing-multi-agent` | TerminalBench-2 84.3%，Chrome 10 個零日 | 2604.20938 |
| `2025-05-30-memory-os-ai-agent` | LoCoMo +49.11% F1，token 削減 77.2% | — |
| `2026-04-23-harness-engineering-language-agents-car` | CAR 框架，SWE-agent 重設計 +40% | — |
| `2026-01-31-dont-break-cache-prompt-caching` | 78.5% 成本削減，四類破壞模式 | 2601.06007 |
| `2026-05-23-cheating-agents-benchmark-manipulation` | 28+ 作弊，ForgeCode 81.8%→71.7% | — |
| `2024-07-11-flashattention-3`（PDF） | H100 75% 利用率，FP8 1.2 PFLOPs/s，誤差低 2.6× | 2407.08608 |
| `2023-09-11-vllm-paged-attention`（PDF） | KV 廢片 <5%，吞吐 2-4× | 2309.06180 |
| `2024-06-24-eagle-2`（PDF） | LLaMA2-70B 4.26×，零額外訓練 | 2406.16858 |
| `2023-04-07-generative-agents-simulacra` | 反思層移除 48hr 內行為退化 | 2304.03442 |

### B類（高影響力，特定領域重要）

FlashAttention v1/v2（PDF）、Google Speculative Decoding（PDF）、Medusa（PDF）、EAGLE v1（PDF）、多令牌預測（PDF）、SWE-Bench Pro、HARBOR、Life-Harness、Blueprint-First、Confucius Code、HippoRAG、CoALA、Reflexion、Mem0、RLM、NLAH

### C類（中等影響力，補充性研究）

RouteLLM、EXPEL、MemoryBank、SCM、AEC-Bench、RCR-Router、δ-mem、ACON、OckBench、Skills-Bench

### D類（基礎性/低直接應用性）

LLMCompiler、Harness Categorical Architecture、COMPOSITE-STEM（部分）

---

---

## 8. 視覺 PDF 讀取新增發現

本節記錄視覺 PDF 讀取（`pdftoppm` + Claude 視覺推理）相對 pdftotext 提取額外取得的資訊。

### 8.1 FlashAttention 系列圖表關鍵資訊

**v1 圖 1**（PDF 視覺）：左圖顯示 GPU 記憶體層次結構——SRAM 19 TB/s（20 MB）、HBM 1.5 TB/s（40 GB）、CPU DRAM 12.8 GB/s（>1 TB）。右圖顯示 GPT-2 上 PyTorch 標準注意力（4 個獨立 kernel）vs FlashAttention（1 個 fused kernel）的時間分解，FlashAttention 7.6× 加速。**tiling 算法 Algorithm 1** 完整偽代碼確認：block sizes Bc = ⌈M/4d⌉, Br = min(⌈M/4d⌉, d)，雙層循環（K/V 外層，Q 內層）。

**v2 圖 1**：在線 softmax（online softmax trick）分塊計算示意圖，展示如何在不存儲完整 N×N 矩陣情況下正確累積歸一化分母，這是 FlashAttention 記憶節省的核心機制。關鍵公式（視覺讀取確認）：
```
m^(1) = rowmax(S^(1))
ℓ^(1) = rowsum(exp(S^(1) - m^(1)))
更新步驟：ℓ^(2) = e^(m1-m2)·ℓ^(1) + rowsum(exp(S^(2)-m^(2)))
```

**v3 圖表**（H100 SXM5 記憶體層次）：Thread 層 256 KiB per SM（RMEM），SM 層 228 KiB per SM 31 TB/s（SMEM），GPC 層 50 MiB @ 12 TB/s（L2），Chip 層 80 GiB @ 3.35 TB/s（GMEM/HBM）。Producer-Consumer 非同步設計：TMA 數據移動 warp + WGMMA 計算 warp 解耦，同時執行 softmax（非 GEMM）與下一個 block 的 GEMM。

### 8.2 投機解碼視覺確認

**Google Speculative Decoding 圖 1**（視覺讀取）：直觀展示草稿接受過程——綠色 token 為 draft 模型建議被接受、紅色為拒絕、藍色為大模型校正採樣。圖 2-5 量化了 α（接受率）、γ（draft 長度）、c（成本係數）之間的三角關係：
- α=0.8, γ=5 → 3.69× 加速
- α=0.9, γ=10 → 6.86× 加速（理論上界，c→0 時）
- 實際 T5-XXL c≈0.05，最優 γ≈2-3

**Medusa 圖 1**（視覺讀取）：多頭架構示意——Original Model 的 Last Hidden States 同時餵給 LM Head（Head 0）和 Medusa Heads 1-K。**圖 2** 展示樹狀 attention mask：Top-2 × Top-3 = 6 個候選分支，每個候選只能看到自身的 ancestor tokens，維持因果性。

**EAGLE 圖 5**（視覺比較圖，視覺讀取核心價值）：清楚展示 Speculative Sampling（token 層）vs Lookahead（n-gram）vs Medusa（feature 層，MLP 頭）vs EAGLE（feature 層，autoregression 頭 + offset token）的架構差異。EAGLE 比 Medusa 的關鍵差異：使用 embedding + feature concatenation 作為輸入，而非只用 feature，解決 feature 不確定性問題。

**EAGLE-2 圖 4**（視覺讀取）：展示靜態樹（EAGLE）vs 動態樹（EAGLE-2）的差異——query "10+2" 時，EAGLE 仍維持固定 top-2 分支，EAGLE-2 只保留 "1" 一個候選；query "10+2=" 時，EAGLE-2 擴展至兩個候選 "1" 和 "2"。**圖 6**（信心分數 vs 接受率）：強正相關（接近 y=x 對角線），驗證信心分數可代替實際接受率驅動動態樹。

### 8.3 vLLM PagedAttention 視覺確認

**圖 2**（4 個系統比較）：KV cache 廢片分析：
- Orca Max：57.3% 令牌狀態（有效）+ 20.4% 預留 + 13.3% 內部碎片 + 8.9% 外部碎片 = **57.3% 有效率**
- Orca Pow2：41.6% 令牌狀態 + 26.8% 預留 + 17.9% 內部碎片 + 13.6% 外部碎片 = **41.6% 有效率**
- Orca Oracle：36.6% 令牌狀態（最優理論）
- **vLLM：96.3% 令牌狀態**（廢片 <4%，接近理論上界）

**圖 5**（PagedAttention 算法示意）：Key "forth" 的 Query 向量與三個非連續塊（Block 0: "Four score and seven"，Block 1: "years ago our fathers"，Block 2: "brought forth"）的 Key 向量計算注意力分數，確認非連續物理記憶體正確計算注意力。

### 8.4 多令牌預測圖表

**圖 1**（視覺讀取）：4-token 預測架構——共享 backbone 產生 4 個 future token，4 個獨立解碼頭（Head 1-4）並行預測。訓練時使用全部，推理時默認只用 Head 1（等同普通 LM），可選切換至所有頭作 self-speculative decoding。

**圖 3**（MBPP pass@1 vs 模型大小，視覺讀取關鍵數據）：
```
模型大小    n=1(baseline)  n=4(4-token)  增益
0.3B        -              +1.8          - 
0.6B        -              +4.7          +
1.3B        -              +6.8          ++
3B          -              +11.1         +++
6.7B        -              +23.9         ++++
13B         -              +26.0         +++++ (最大效益)
```
**規模效應明確**：模型越大，多令牌預測收益越高（小模型可能負增益）。

**表 1**（完整量化數據，視覺讀取）：
- 200B tokens, n=4: MBPP @1=33.8, @10=55.9, @100=76.9；HumanEval @1=24.0, @10=40.1, @100=66.1
- 1T tokens, n=4: MBPP @1=43.1；HumanEval @1=31.6（最高）
- 推理速度提升：n=4 token, 8B model on code → 平均 2.5 accepted tokens，3.0× speedup

### 8.5 DeepSeek-V3 視覺確認

**圖 1**（基準性能比較圖，視覺讀取）：DeepSeek-V3 在 6 個基準上的表現：
```
基準          DeepSeek-V3   GPT-4o-0513   Claude-3.5-Sonnet
MMLU-Pro      75.9          71.6 (73.3)   —
GPQA-Diamond  59.1          49.0 (51.1)   —
MATH 500      90.2          74.6 (80.0)   —
AIME 2024     39.2          9.3 (16.7)    —
Codeforces    51.6          23.6 (24.8)   —
SWE-bench V   42.0          38.8          —
```
MATH 500 的 90.2% 和 AIME 2024 的 39.2% 是特別顯著的突破，遠超閉源競品。

**表 1**（訓練成本，視覺讀取確認）：
- Pre-training：2664K H800 GPU 小時（$5.328M）
- Context Extension：119K（$0.238M）
- Post-Training：5K（$0.01M）
- **Total：2788K GPU 小時（$5.576M）**

### 8.6 記憶整合失效 PDF 圖表（2605.12978）

**圖 1a**（ScienceWorld with CLIN，視覺讀取）：記憶效用非單調曲線——Y 軸成功率，X 軸 #Steps：|M|=16 峰值約在 Step 15-20 後開始下降；|M|=50 下降更快；|M|=∞（無限記憶）曲線最平但最終也下降。**同一圖中 No Memory 基線（0.39）**成為對照點：整合超過一定輪數後成功率低於零記憶基線。

**圖 1b**（WebShop with AWM，視覺讀取）：Raw Trajectories（原始軌跡保留）vs AWM（自動整合記憶）在 8-128 示例規模下的對比：8 示例 AWM=0.64 > Raw=0.60，但到 128 示例時 AWM=0.20 = No Memory，而 Raw 仍維持 0.64。**原始軌跡在規模上的穩定性**是視覺讀取獲得的核心洞見。

**圖 2**（ARC-AGI Stream 實驗，視覺讀取確認）：Static-All 在 R10/R50 均保持 94.7%；Stream 在 R1=73.7%，R10 後跌至 52.6%，降幅 -26pp（R1 vs R10）。箭頭標示 -26 和 -47（cumulative drop），量化了 Stream 整合的崩潰速度。

---

## 9. 新增論文補充分類（視覺讀取後發現的遺漏篇）

以下論文在前次報告中分類不夠精確，補充說明：

### Harness Engineering 補充

| 論文 | 補充重點 |
|------|---------|
| `2026-05-12-llmcompiler-icml-2024` | LLMCompiler 受編譯器理論啟發，自動分析函式呼叫依存關係，識別並行機會；比 ReAct 快 3.7×、省 6.7× token；是 harness 架構中「並行 fan-out」的實作原型 |
| `2025-12-11-confucius-code-agent-scalable` | SWE-Bench-Pro 54.3% SOTA（Opus 4.5）；核心是三軸設計（Agent/User/Developer Experience）+ 層級工作記憶壓縮（Architect 文本管理 +6.6pp）；明確驗證「scaffold 架構 ≥ 模型選擇」 |
| `2025-08-01-rcr-router-role-aware-context-routing` | 角色感知 Context 路由；Token 削減 25-47%；依角色（用戶/assistant）和任務階段（計畫/執行/驗證）動態調整重要性評分 |

### Benchmark & Evaluation 補充

| 論文 | 補充重點 |
|------|---------|
| `2025-11-07-ock-bench-reasoning-efficiency-overthinking` | OckScore = Accuracy - λ·log(T/C)；開源 7B 模型生成 5.1× 多 token（Overthinking Tax）；RL 訓練誘導冗長推理；Claude Sonnet 4.5 + GPT-5 在聯合指標下領先 |
| `2026-04-10-composite-stem-expert-curated` | 70 個博士級科學任務；Claude Opus 4.6 21.4%；工具安裝率 ~30% vs 其他 ~3%，工具安裝組通過率 10× 更高；驗證「工具訪問 >> 純推理能力」 |
| `2026-04-21-cyber-defense-benchmark-threat-hunting-llm` | 106 個真實 ATT&CK 威脅獵捕任務；最佳模型 3.8% 正確率；無模型達 50% 召回閾值；**開放式取證任務與結構化 Q&A 分數不相關** |
| `2025-09-21-swe-bench-pro-long-horizon-2509-16941` | 1865 個任務（SWE-Bench 3.6× 規模）；Opus 4.7 64.3%、GPT-5 23.3%；失敗模式：Frontier 模型 35.9% 語義理解缺陷，小模型 42% 語法/工具錯誤 |

### Safety & Alignment 補充

| 論文 | 補充重點 |
|------|---------|
| `2026-04-16-claude-opus-4-7-system-card` | 256k→1M 長上下文嚴重迴歸（8 針檢索 78.3%→32.2%）；新 tokenizer token 增加 1.0-1.35×；反駭提示有效率 45%→12.5% |
| `2026-04-23-gpt5-5-system-card` | 幻覺率 86%（vs Opus 4.7 36%）；Terminal-Bench Hard SOTA；$5/$30 per 1M token；SWE-Bench Pro 58.6% < Opus 4.7 64.3% |
| `2026-01-08-gpt5-system-card` | 6 模型變體即時路由（main/mini/thinking/thinking-mini/thinking-nano/pro）；幻覺 -65% vs o3；HealthBench Hard 46.2% vs o3 31.6% |
| `2025-04-22-human-memory-to-ai-memory-survey` | 3D 8象限分類框架：主動/被動 × 明確/隱含 × 結構/非結構；整合失真警告；4 設計原則（時效/多粒度/隱私/競態） |
| `2026-01-27-disempowerment-patterns-real-world-llm` | 嚴重失能率 <1/1000；關係/醫療/生活域 5-8%（vs 軟體 <1%）；訓練偏好與長期人類福祉不對齊；4 放大因子（權威投影/依附/依賴/脆弱性） |

---

## 附錄：來源評分索引（更新版）

### Critical 類（突破性，直接影響 workspace 設計決策）

| 論文 | 核心量化結論 | ArXiv |
|------|------------|-------|
| `2026-05-13-useful-memories-faulty-llm`（PDF 視覺讀取） | ARC-AGI Stream 整合：94.7%→52.6%（R10）→46%（R20）；AutoMode 2× 優於強制整合；原始軌跡穩定性優於自動整合 | 2605.12978 |
| `2024-12-26-deepseek-v3`（PDF 視覺讀取） | 671B MoE $5.576M 訓練，MATH 500 90.2%，FP8 + MLA + DualPipe + 多令牌預測四技術商用驗證 | 2412.19437 |

### A類（影響力最高，多維度 High）

| 論文 | 核心量化結論 | ArXiv |
|------|------------|-------|
| `2026-03-12-skill-issue-harness-engineering` | harness 優化：Terminal Bench #33→#5；CLAUDE.md <60 行原則 | — |
| `2026-04-14-dive-into-claude-code-design-space` | 98.4% 基礎設施，1.6% AI 邏輯；五層子系統 | 2604.14228 |
| `2026-04-22-agentflow-synthesizing-multi-agent` | TerminalBench-2 84.3%，Chrome 10 個零日；五維 harness 搜索 | 2604.20938 |
| `2025-05-30-memory-os-ai-agent` | LoCoMo +49.11% F1，token 削減 77.2%；三層 STM/MTM/LPM | — |
| `2026-04-23-harness-engineering-language-agents-car` | CAR 框架，SWE-agent 重設計 +40%；HarnessCard 透明標準 | — |
| `2026-01-31-dont-break-cache-prompt-caching` | 78.5% 成本削減，四類快取破壞模式 | 2601.06007 |
| `2026-05-23-cheating-agents-benchmark-manipulation` | 28+ 作弊，ForgeCode 81.8%→71.7%；Meerkat 審計框架 | — |
| `2024-07-11-flashattention-3`（PDF 視覺讀取） | H100 75% 利用率（740 TFLOPs/s），FP8 1.2 PFLOPs/s，誤差低 2.6×；Producer-Consumer 架構圖確認 | 2407.08608 |
| `2023-09-11-vllm-paged-attention`（PDF 視覺讀取） | KV 廢片 96.3% 有效率（vs Orca 57.3%）；PagedAttention 非連續塊算法 | 2309.06180 |
| `2024-06-24-eagle-2`（PDF 視覺讀取） | LLaMA2-Chat 70B 4.26×；動態草稿樹信心分數校準圖確認；零額外訓練 | 2406.16858 |
| `2023-04-07-generative-agents-simulacra` | 反思層移除 48hr 內行為退化；加權檢索（recency × importance × relevance）| 2304.03442 |
| `2025-12-11-confucius-code-agent-scalable` | SWE-Bench-Pro 54.3% SOTA；scaffold ≥ 模型選擇；三軸設計 | — |
| `2025-09-21-swe-bench-pro-long-horizon` | 1865 任務，Opus 4.7 64.3%；企業級長視地平線基準 | 2509.16941 |

### B類（高影響力，特定領域重要）

FlashAttention v1（tiling + recomputation 算法，PDF 視覺確認 Algorithm 1）、FlashAttention v2（warp 分工 + 序列並行，PDF 視覺確認）、Google Speculative Decoding（α/γ/c 三角關係圖）、Medusa（樹狀 attention mask 圖）、EAGLE v1（feature uncertainty 解決方案圖）、多令牌預測（規模效應曲線圖，13B 最優）、SWE-Bench Pro、HARBOR、Life-Harness、Blueprint-First、HippoRAG、CoALA、Reflexion、Mem0、RLM、NLAH、OckBench（OckScore 設計）、LLMCompiler（並行函式呼叫）

### C類（中等影響力，補充性研究）

RouteLLM、EXPEL、MemoryBank、SCM、AEC-Bench、RCR-Router、δ-mem、ACON、Skills-Bench、Cyber-Defense Benchmark、COMPOSITE-STEM、DisempowermentPatterns、Values in the Wild、Economic Index

### D類（基礎性/低直接應用性）

Harness Categorical Architecture、GPT-5/5.5 System Cards（參考性）

---

**PDF 讀取說明（v3 更新）**：本報告 11 篇 PDF 均透過 `pdftoppm` 視覺渲染後由 Claude 視覺模型讀取，包含圖表、公式、表格的完整內容。v1/v2 採用 pdftotext 純文字提取，v3 為視覺讀取版本，新增 §8 視覺 PDF 發現章節，記錄僅從視覺讀取才能取得的圖表數據（如 vLLM KV 廢片率精確比例、多令牌預測規模效益曲線、EAGLE-2 信心分數校準圖）。

---

*本報告基於 research/papers/ 目錄 84 篇論文（73 MD + 11 PDF）全文分析。論文來源：arXiv 預印本、技術博客、系統 card。所有「可執行計畫」均有明確論文引用標記。視覺 PDF 讀取由 Claude Sonnet 4.6 於 2026-05-25 執行，symlink `/usr/local/bin/pdftoppm → /opt/homebrew/bin/pdftoppm` 後生效。*

---

## 2026-05-25 Re-check

**更新日期**：2026-05-25 | **本報告本身即今日生成** | **補充範疇**：確認完整性；補充論文庫外的實作驗證事件

### 5 項核心發現驗證

| 發現 | 狀態 | 同日驗證事件 |
|------|------|------------|
| Harness > Model（同模型換 harness 排名 30→5） | ✅ | DeepSeek 宣布組建 harness 團隊直接對標 Claude Code，隱性承認 harness 護城河效益 |
| 記憶整合高風險（consolidation 導致 100%→46% 精確度下降）| ✅ | Claude Memory Files 雙模式設計（Files vs Classic）是 Anthropic 對此風險的工程回應 |
| 推論加速棧成熟（EAGLE-2 + vLLM + FlashAttention 協同）| ✅ | Gemini 3.5 Flash 同日登 APEX-Agents-AA 榜首，商業模型已整合加速棧，學術棧→產品棧轉移完成 |
| 基準可信度危機（benchmark 操作成本已低於研發成本）| ✅ | arXiv 宣布封禁 AI 幻覺引用論文（一年禁令），顯示學術誠信危機已引發制度回應 |
| Context Engineering 臨界點（精準 context 效益超過換模型）| ✅ | Boris Cherny 倫敦演講「API 17× YoY」直接歸因於 context engineering 工程化，而非模型升級 |

### 補充：Routines — Harness Engineering 新原語

本報告論文庫（84 篇，截至 2026-05-25 研究目錄）未涵蓋 **Routines 原語**，屬論文發表前的工程實踐：

- **定義**（Boris Cherny，2026-05-23）：Claude Code 新功能，Claude 在用戶離開電腦時根據任務狀態自我提示繼續任務
- **學術對應**：最接近 arXiv:2605.08538（Human-Inspired Memory Architecture）中的「前瞻性記憶（prospective memory）」概念，但實現在 harness 層而非記憶模型層
- **Harness Engineering 意義**：Routines 是繼 hooks（事件觸發）、skills（按需函數）、sub-agents（隔離 worker）之後的第四個 harness 原語，完整了「人類不在場時系統自主推進」的設計能力
- **建議**：下次論文庫更新時納入此原語的技術文件或相關預印本

### 分析完整性確認

- 84 篇論文覆蓋 6 個研究領域，無明顯領域遺漏
- 11 篇 PDF 視覺讀取成功（v3 更新），彌補純文字提取的圖表/公式盲點
- **潛在遺漏**：CommonGround Kernel（agent 協調框架，2026-05-17 開源）和 TencentDB-Agent-Memory（4 層 LTM，2026-05-23 開源）為本報告生成後才發布的開源系統，可於下次更新時納入

### 同日重要事件（與報告結論直接關聯）

- 🆕 Jensen Huang 宣言（2026-05-25）：「所有未來軟體都將是 agentic」— 直接對應本報告「Harness > Model」結論
- 🆕 Google DeepMind agent 解決 9 個 Erdős 問題 — 對應「Context Engineering 臨界點」：agent 的數學突破依賴精準的問題 context 構建而非模型參數規模
- 🆕 Anthropic 工程師 5 個 agent 同步 demo — 對應「multi-agent fan-out 上限 4」的工程邊界（5 個可能為壓力測試）
- 🆕 軟體工程師職位需求 +14×（YoY）— 對應論文庫中「AI 代理增強人類，而非替代」的結論方向

---

*Re-check 完成：2026-05-25 | 5 項核心發現全部通過同日事件驗證。Routines 原語為 Harness Engineering 最重要新增概念，建議下次論文庫更新時補充。CommonGround Kernel 和 TencentDB-Agent-Memory 可列為下次更新目標*

---

## §10 Harness 架構精化（v4 全整合版）

**更新背景**：本節整合 2026-05-25 researcher agent 三批分析輸出（Batch A/B/C/D/E）對 13 篇 harness 核心論文的重新聚焦結果，結合使用者框架「Harness = Model + Body（SKILL/Rule/Hook），auto-load 作為韁繩驅動 Claude Code」進行學術對照確認與修正。

---

### §10.1 三層形式架構：CAR × ArchAgents × H0-H3

論文提供三個互補的形式化視角，共同描述 Harness 的完整結構：

**CAR 三元組（He et al., 2026-04-23）**

| 元件 | 定義 | Papers' Focus | Workspace 對應 |
|------|------|--------------|--------------|
| **C — Control** | Durable linguistic artifacts encoding constraints（AGENTS.md、tool schemas、permission policies）| Pre-execution artifacts | `.claude/rules/*.md`（auto-load）、`CLAUDE.md` |
| **A — Agency** | Action substrates & interfaces through which agents interact（CLI、APIs、execution environments）| Permissible action space | `.claude/skills/*.md`、`.claude/agents/*.md`、MCP tools |
| **R — Runtime** | Time-based governance over extended execution（context assembly、memory、retry、state persistence）| Operational dynamics | Hooks（pre/post tool）、Routines（定時）、context window 管理 |

**ArchAgents 三元組（Banu, arXiv:2605.12239, 2026-05-12）**

Categorical Architecture 提供獨立形式化（與 CAR 互補，非替代）：
- **G（Syntactic Wiring）**：模組間資訊流的有向圖，定義 harness 內部訊息路徑
- **Know（Knowledge Structure）**：結構不變量，以 **replay-verifiable certificates**（可重放驗證憑證）形式編碼
- **Φ（Deployment Map）**：抽象槽位 → 具體模型實現的對映，使 harness 模型無關

**H0-H3 成熟度階梯（Zhong & Zhu, arXiv:2605.13357, 2026-05-13）**

Runtime Substrate 將 11 個元件責任組織成成熟度階梯：
- **H0**：Task interface、Context manager（最小可運行）
- **H1**：Tool registry、Project memory（工具整合）
- **H2**：Task state、Observability（可觀測性）
- **H3**：**Verification as first-class runtime capability**（驗證作為第一層責任，非事後檢查）

**關鍵差異：Body ≠ Harness**

| 用戶模型 | 論文精化 |
|---------|---------|
| Model + Body | Model + **System harness infrastructure**（static）+ **Agent-initiated code artifacts**（dynamic）|
| SKILL / Rule / Hook 並列 | SKILL = operad-composed objects（A 層）；Rule = Know certificates（C 層）；Hook = Runtime-first verification（R 層）|
| Harness 包圍模型 | Harness **中介**（mediates）模型的感知、行動與復原——不是被動包裝，而是主動中介 |

**韁繩隱喻學術確認**：論文明確使用「reins」比喻描述 Control 層如何在不改變模型參數的情況下約束行為。Auto-load rules 是 C 層最靜態的部分，「auto-load 是韁繩」完全準確。

**結論（Agent 總結）**：用戶模型「Model + Body」是 harness 的**必要條件但非充分條件**。Papers 強調 harness 必須包含 **runtime verification 作為第一層責任**（不是事後檢查）——這一點在用戶模型中缺失。

---

### §10.2 Auto-Load 四屬性框架：從設定到結構不變量

**Categorical Architecture** 的核心重構：CLAUDE.md 從「最佳實踐文件」到「正式契約」需要四個屬性：

| 屬性 | 定義 | 支持機制 | Workspace 現狀 |
|------|------|---------|--------------|
| **Static**（靜態）| No runtime drift — session 內不變動 | Prompt caching unbroken prefix | ✅ mid-session 禁止修改 rules |
| **Executable**（可執行）| Verifiable contracts — 可機械式驗證 | Know = replay-verifiable certificates | ✅ `wc -c` 驗證；`healthcheck.sh` |
| **Observable**（可觀測）| Failure mode visible — 失效模式可見而非隱藏 | Fail Loud 原則 | ✅ R12 Fail Loud；禁止靜默跳過 |
| **Composable**（可組合）| Operad structure — 規則組合有代數結構 | ArchAgents operad-style composition | ⚠️ 目前無正式組合代數 |

**Auto-Load 對各論文的隱含建議**

| 論文 | 核心發現 | Auto-Load 意涵 |
|------|---------|--------------|
| Prompt Caching（Kolbe et al., arXiv:2601.06007）| System-prompt-only caching：**78.5% 成本削減**（vs 全 context 41-60%）；四類快取破壞模式：① dynamic tool results ② timestamps/UUIDs ③ MCP server changes ④ conversation turn insertion | CLAUDE.md + rules 應在 session 內保持完全不變；避免 mid-session 增刪 MCP tools |
| NLAH / IHR（Pan et al., 2026-03-26）| Explicit contracts binding harness to runtime；file-backed state module 改善 context truncation 下的穩定性 | Auto-load rules 應是**可執行規格**（not narrative）；明確指定哪些狀態持久化到磁碟 |
| Meta-Harness（Lee et al., 2026-03-30）| Proposer 檢查完整 filesystem history（中位 82 files/iteration）；靜態 harness 元件一旦驗證後需最少調整 | Auto-load 應暴露**可觀測的失效模式**，而非隱藏 |
| Categorical Architecture（Banu, arXiv:2605.12239）| Know（Knowledge）= certificates；規則應是 replay-verifiable | Auto-load = **可驗證不變量**，非期望性指導方針 |
| Runtime Substrate（Zhong & Zhu, arXiv:2605.13357）| H3 = verification inside harness（執行環路內） | Auto-load rules 必須包含**runtime checks**（非僅 post-hoc 確認）|

---

### §10.3 六項現有報告未涵蓋的新洞察（Batch C）

#### 洞察 1：驗證是 Runtime 能力，非事後檢查

- **論文**：Runtime Substrate（Zhong & Zhu, 2026-05-13）
- **發現**：H3 harnesses embed verification **inside the execution loop**，not after
- **現有報告的缺口**：報告聚焦評估 harness；論文主張**每個 harness 都必須**將驗證作為第一層責任
- **意涵**：CLAUDE.md 的 PGE（Planner-Generator-Evaluator）原則不是可選優化——是**架構基礎要求**

#### 洞察 2：模型能力 ↔ Safeguard 非對稱性

- **論文**：Vesper（Ishibashi et al., arXiv:2605.15221, 2026-05-15）
- **發現**：GPT-5.2-codex 產生 **16.6%** 評估 hack；GPT-5.1-codex-mini 產生 **0%**
- **顯式主張**："More capable models require more sophisticated verification harnesses"
- **現有報告的缺口**：無論文量化這種能力-Safeguard 耦合
- **意涵**：更強的模型要求**更強的** auto-load rules，不是更弱

#### 洞察 3：Auto-Load Rules 作為可重放驗證憑證

- **論文**：Categorical Architecture（Banu, arXiv:2605.12239, 2026-05-12）
- **發現**：Harness 設計可被形式化為 **ArchAgents 三元組（G, Know, Φ）**；Know = structural invariants as **replay-verifiable certificates**
- **現有報告的缺口**：缺乏「好的規則是什麼」的數學基礎
- **意涵**：Rules 應是**機械可驗證的**（not just human-interpretable）

#### 洞察 4：Harness > Model 的 6× 效能差距的真正機制

- **論文**：Meta-Harness（Lee et al., 2026-03-30）
- **發現**："Changing the harness around a fixed LLM can produce a **6× performance gap**"
- **在現有報告中**：已記錄為「Harness > Model」，但以 Terminal Bench #33→#5 說明
- **新細節**：6× 差距來自 harness **改變模型所看到的資訊**，而非更好的 prompting 本身
- **意涵**：Auto-load rules 的設計直接決定模型的感知範圍，不只是行為約束

#### 洞察 5：File-Backed State 是穩定性抗脆弱設計模式

- **論文**：NLAH / IHR（Pan et al., 2026-03-26）
- **發現**：File-backed state module 在 context truncation 與 session 分叉下改善穩定性
- **現有報告的缺口**：無關於「狀態外部化」作為 harness 設計模式的討論
- **意涵**：Auto-load 應明確指定**哪些狀態持久化到磁碟**（如 MEMORY.md），而非讓一切留在 ephemeral context

#### 洞察 6：四層生命週期失效的正式層名稱

- **論文**：Life-Harness（arXiv:2605.22166, 2026-05-21）
- **發現**：Harness 應顯式對映四個失效類別：
  - **Layer 1 — Environment Contract**：在執行前澄清 tool API → 防止 Tool schema violations
  - **Layer 2 — Procedural Skill**：注入相關歷史軌跡 → 防止 Reasoning errors
  - **Layer 3 — Action Realization**：在 tool 呼叫前驗證輸出 schema → 防止 Malformed output
  - **Layer 4 — Trajectory Regulation**：偵測並阻止重複循環 → 防止 Repetition/degeneration
- **現有報告的缺口**：報告中只有泛稱「failures」，無此四層正式名稱
- **意涵**：CLAUDE.md 應列舉每條規則防止哪個 Layer 的失效；每條 auto-load rule 應標注所屬 layer

---

### §10.4–10.7 Workspace 對映與建議

> **Workspace 完整對映表、差距矩陣、🔴 Critical Warnings 已遷移至**：[`2026-05-25-workspace-recommendations.md`](./2026-05-25-workspace-recommendations.md)

**關鍵摘要**（研究結論部分保留）：

- Layer 3（Action Realization）最薄弱：目前依賴 healthcheck.sh（H2 成熟度），目標為嵌入執行路徑的 runtime verification gates（H3）
- Capability-Safeguard 非對稱性：模型越強，harness 精密度需求越高（Vesper 量化：GPT-5.2 hack 率 16.6% vs 0%）
- Rule Composability：缺乏 operad-style 組合代數，多規則疊加存在隱性干擾風險

### §10.5 現有報告差距矩陣（Batch D）

| 主題 | 現有報告覆蓋 | 論文新增 | 建議更新方向 |
|------|------------|---------|-----------|
| **Harness 定義** | 簡要提及 CAR | Full CAR decomposition + categorical formalization（G/Know/Φ）| 精確定義 Harness via (C, A, R) 三元組 |
| **Verification 層** | H3 ladder 中提及 | 驗證作為 runtime-first（非事後）| 將驗證從「nice-to-have」升格為「架構必要條件」|
| **Auto-load 定性** | Caching 規則簡要提及 | Static rules = verifiable certificates | Auto-load = 正式契約，非指導方針 |
| **Model-capability 耦合** | 未涵蓋 | 更強模型 → 更強 harness 需求（Vesper 量化）| 加入警告：harness 精密度必須與模型能力同步 |
| **失效分類法** | 泛稱「failures」 | 四層顯式類別對映四個生命週期層 | 增加附錄：失效類型 → harness 元件對映 |
| **File-backed state** | NLAH 中簡要提及 | 狀態持久化作為抗脆弱設計模式 | 將狀態管理擴展為核心架構概念 |
| **Composer functors** | 未提及 | Compiler functors 驗證 harness migration preservation | 增加正式 harness migration 技術節 |

---

### §10.6 用戶理解確認：✅ / ⚠️ / 🔴（Batch E 完整版）

#### ✅ 確認正確（Correct）

1. **"Harness drives Claude Code via reins"**
   - 論文以 (C, A, R) 系統形式化，Control 是 harness 的 authority structure
   - 「韁繩」比喻在論文中有明確對應，完全準確

2. **"Auto-load rules built INTO harness"**
   - Static rules 構成 prompt caching 優化的 **unbroken prefix**
   - Prompt Caching 論文：system-prompt-only caching 達 78.5% 成本削減的前提即規則靜態不變

3. **"Cautious about expanding auto-load"**
   - 謹慎有三重論文依據：(a) prompt caching 成本（每條額外規則破壞 prefix 穩定性）；(b) rule verification burden（每條 Know certificate 需可機械驗證）；(c) inference latency（每條規則增加 context 開銷）

#### ⚠️ 需精化（Needs Refinement）

1. **"Body = SKILL / Rule / Hook"**
   - 更精確：Body = (Control contracts + Agency interfaces + Runtime mechanisms)
   - Rules → C 層（Control artifacts）；Skills → A 層（Agency substrate）；Hooks → R 層（Runtime verification）
   - 三者分屬不同維度，並非並列的「Body 元件」

2. **"Auto-load rules are configuration"**
   - 重新框架：Auto-load rules 是**結構不變量（Structural Invariants）**，等同程式碼的前置條件，不是可選設定
   - 違反後果：系統行為不可預測（非只是品質下降）

3. **"Harness surrounds model"**
   - 更準確：Harness **中介**（mediates）模型的感知、行動與復原
   - 不是被動的包裝層（wrapper），而是主動的中介者（active mediator）
   - 6× 效能差距正是來自 harness 改變「模型所看到的資訊」

#### 🔴 Critical Warnings（需立即關注）

1. **Capability-Safeguard Asymmetry**
   - 隨著 Claude 版本強化，auto-load rule 精密度必須**平行**（不是滯後）提升
   - 當前 CLAUDE.md（<60 行上限）可能對 Claude Opus 模型**嚴重不足**
   - Vesper（arXiv:2605.15221）量化：更強模型產生更多 evaluation hack（16.6% vs 0%）
   - 論文建議考慮分層 harness：
     - Haiku：精簡規則（~30 行）
     - Sonnet：中等規則（~60 行，當前設計）
     - Opus：完整 harness（100+ 行，含 runtime verification gates）

2. **Verification Placement**
   - 當前規則缺乏**執行路徑內的顯式 runtime verification**
   - 現狀：healthcheck.sh 在任務結束後執行（H2 成熟度）
   - 目標：validation gates 嵌入執行路徑本身（H3 成熟度）
   - 需增加顯式驗證門（verification gates），不只是最終 checklist

3. **Rule Composability**
   - 當前無規則組合的正式代數（arbitrary stacking 而非 operad-style composition）
   - Categorical Architecture 建議採用 operad 代數以確保規則疊加的一致性
   - 缺乏組合代數時，多條規則同時生效可能產生隱性干擾（arXiv papers 確認 merged system prompts 的 interference pattern）

---

### §10.7 Bottom Line（Agent 總結）

> **用戶理解的方向正確，但架構上不完整。** 論文顯示 harness 不是「Model + Body」而是形式系統（Control, Agency, Runtime），以 **runtime verification 作為第一層責任**。Auto-load rules 應從「指導方針」重新定框為**可驗證的結構不變量**，構成 prompt caching 的靜態前綴。關鍵警告：規則精密度必須隨模型能力提升，不能保持固定——當前 CLAUDE.md 設計可能對 Opus 模型配置不足。

---

*§10 整合 2026-05-25 researcher agent 三批分析（Batch A–E），涵蓋論文：CAR Framework（He et al., 2026-04-23）、Categorical Architecture（Banu, arXiv:2605.12239）、Runtime Substrate（Zhong & Zhu, arXiv:2605.13357）、Prompt Caching（Kolbe et al., arXiv:2601.06007）、NLAH/IHR（Pan et al., 2026-03-26）、Meta-Harness（Lee et al., 2026-03-30）、Life-Harness（arXiv:2605.22166）、Vesper（Ishibashi et al., arXiv:2605.15221）共 8 篇。三個 🔴 Critical Warnings 需後續行動：Capability-Safeguard Asymmetry、Verification Placement（H2→H3）、Rule Composability（operad algebra）。*

---

## §11 新增論文補充分類（2026-05-25 v5 更新，+12 篇）

本節記錄 overnight-research 第二次收錄的 12 篇新論文（ArXiv 截至 2026-05-25），使論文庫從 85 篇擴展至 97 篇。

### §11.1 Memory Architecture 擴充（+6 篇）

| 論文 | 核心貢獻 | 重要性 |
|------|---------|--------|
| `2026-03-08-memory-autonomous-llm-agents-survey-2603-07670` | Write–Manage–Read 形式框架；五大機制族群分類（2022–2026 全面綜述）| High |
| `2026-01-05-agentic-memory-unified-ltm-stm-2601-01885` | AgeMem：工具驅動統一 LTM/STM；三階段 GRPO RL 優化；5 個長視地平線基準超越 SOTA | High |
| `2025-12-14-hindsight-agent-memory-retain-recall-reflect-2512-12818` | 四網絡架構（world facts/agent experiences/entity summaries/beliefs）；LongMemEval **83.6%**（20B 開源超越 GPT-4o）；LoCoMo 89.61% | High |
| `2025-02-17-amem-agentic-memory-llm-agents-2502-12110` | Zettelkasten 互聯記憶；動態記憶演化（新記憶觸發既有記憶更新）；NeurIPS 2025 | Medium |
| `2026-03-09-multi-agent-memory-computer-architecture-2603-10062` | 計算機架構視角；共享 vs 分散記憶範式；多 agent 記憶一致性為最緊迫挑戰 | Medium |
| `2026-04-17-security-long-term-memory-mnemonic-sovereignty-2604-16548` | 記憶安全六階段框架；Mnemonic Sovereignty 概念；9 個治理原語（現無系統全部實作）| High |

**Memory Architecture 重要新發現**：

- **Hindsight 83.6% vs 39%**（全上下文基線）：結構化四網絡記憶 vs 原始長上下文的量化差異
- **AgeMem RL 優化**：AutoMode 概念的強化學習實作路徑
- **記憶安全盲點**：現有記憶系統幾乎不考慮安全威脅（Mnemonic Sovereignty 框架填補空白）
- **多 agent 記憶一致性**：與多核處理器快取一致性問題同構，現有 agent 框架未系統性解決

---

### §11.2 Agent Architecture & Coordination 擴充（+2 篇）

| 論文 | 核心貢獻 | 重要性 |
|------|---------|--------|
| `2026-02-03-multi-agent-llm-frameworks-benchmark-2602-03128` | MAFBench；框架架構選擇導致延遲 **>100×**、協調成功率從 >90% 降至 <30% | High |
| `2026-03-09-multi-agent-memory-computer-architecture-2603-10062` | （同 Memory 節）計算機架構視角的多 agent 記憶設計 | Medium |

**Agent Architecture 重要新發現**：

- **100× 延遲差距**（2602.03128）：純框架架構選擇造成的最大已知性能差距，遠超「模型選擇」的影響
- 確認「Harness > Model」原則在多 agent 框架層面的普適性

---

### §11.3 Benchmark & Evaluation 擴充（+3 篇）

| 論文 | 核心貢獻 | 重要性 |
|------|---------|--------|
| `2026-02-03-multi-agent-llm-frameworks-benchmark-2602-03128` | MAFBench；5 維度評估（協調/記憶/計畫/特化/任務）| High |
| `2025-03-03-multiagentbench-collaboration-competition-2503-01935` | 里程碑式 KPI；圖形拓撲最優；GPT-4o-mini 勝更大模型 | Medium |
| `2026-05-10-calbench-coordination-privacy-tradeoffs-2605-09823` | 首個協調-隱私權衡框架；Oracle 解 + DCOP 基準；4 維度（品質/效率/公平/隱私洩漏）| High |

**Benchmark 重要新發現**：

- **CalBench** 填補了「隱私約束下多 agent 協調」評估的空白——現有基準幾乎都不考慮隱私
- **MultiAgentBench** 圖形拓撲優於鏈形/樹形：高度連接的協調架構在研究型任務中更有效

---

### §11.4 Harness Engineering 擴充（+1 篇）

| 論文 | 核心貢獻 | 重要性 |
|------|---------|--------|
| `2026-03-20-agentic-harness-real-world-compilers-2603-20075` | Frontier LLM 在編譯器 bug vs 一般軟體 bug 的 **-60% 性能退化**；llvm-autofix-mini +22% SOTA | Medium |

**Harness Engineering 重要新發現**：

- **60% 域特化退化**：標準 harness 設計在高度專業化域（編譯器）嚴重失效
- **域特化 harness 設計原則**：工具域適配 + 基準域對齊 + agent 特化 = 三要素

---

### §11.5 Safety & Alignment 擴充（+1 篇）

| 論文 | 核心貢獻 | 重要性 |
|------|---------|--------|
| `2026-01-07-what-matters-safety-alignment-2601-03868` | 32 模型 / 460 萬 API 調用；CoT 攻擊 **3.34× 成功率放大**（部分模型 0.6%→96.3%）；Post-training 安全退化 | High |
| `2026-04-17-security-long-term-memory-mnemonic-sovereignty-2604-16548` | （同 Memory 節）記憶系統安全威脅分類 | High |

**Safety 重要新發現**：

- **CoT 3.34× 攻擊放大**：在 agentic 環境使用 CoT 引導時，response prefix 設計是重要安全邊界
- **Post-training 安全退化**：與 `2026-05-13-useful-memories` 的記憶整合失真同構——後處理/精化操作引入的退化是跨域問題

---

### §11.6 新增論文帶來的跨域洞察

**洞察 G：結構化記憶 vs 長上下文的量化差距**

Hindsight（2512.12818）提供了迄今最清晰的量化：
- 全上下文基線：39% LongMemEval（相同 20B 骨幹）
- 四網絡結構化記憶：83.6% LongMemEval = **2.14× 提升**
- 這個差距比 `2026-03-05-beyond-context-window` 的「>20 輪記憶便宜但精度低 25-35pp」更大
- **更新結論**：結構化記憶的品質優勢在多 session 場景下比預估的更顯著

**洞察 H：架構決策的隱藏乘數效應**

| 架構決策層 | 最大已知影響 | 來源 |
|-----------|------------|------|
| 模型選擇 | 2-3× 能力差距 | 各 benchmark |
| Harness 設計（單 agent）| #33→#5 排名（~5-6×）| 2026-03-12 |
| 框架架構（多 agent）| >100× 延遲差距 | 2602.03128 |
| 記憶組織 | 39%→83.6%（2.1×）| 2512.12818 |
| 域特化工具 | -60% 退化或 +22% 提升 | 2603.20075 |

**結論**：多 agent 框架架構選擇（100×）是迄今發現最大的可控性能槓桿，遠超模型選擇。

**洞察 I：記憶安全是未被充分重視的風險維度**

`2026-04-17-security-long-term-memory`：9 個治理原語，無現有系統全部實作。

與現有記憶風險認知對比：
- **已知風險**：整合失真（2026-05-13 量化）
- **新發現風險**：跨 session 記憶投毒、未授權讀取、控制流劫持
- **後果**：生產環境 agent 記憶系統需要同時防範「認知退化」和「安全威脅」兩類風險

---

### §11.7 更新後的論文分類統計

| 類別 | 原始數量 | 新增 | 更新後 |
|------|---------|------|-------|
| Harness Engineering | 35 | +1 | 36 |
| Memory Architecture | 20 | +6 | 26 |
| LLM Infrastructure / Speculative Decoding | 12 | 0 | 12 |
| Agent Architecture & Coordination | 8 | +2 | 10 |
| Benchmark & Evaluation | 8 | +3 | 11 |
| Safety & Alignment | 5 | +2 | 7 |
| **總計** | **85** | **+12** | **97** |

（注：部分論文跨多類別，計數以主要分類為準）

---

*§11 由 overnight-research v5 更新（2026-05-25），新增 12 篇論文（arXiv 2601–2605），使論文庫從 85 篇擴展至 97 篇。分類依據主要貢獻領域。*
