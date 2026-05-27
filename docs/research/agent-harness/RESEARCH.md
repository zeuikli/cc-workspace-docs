---
title: "Agent Harness 深度研究"
type: documentation
---

# Agent Harness 深度研究

> 研究分支：`claude/agent-harness-research-eM6Vc`
> 完成日：2026-04-30
> 觸發：Zeuik 提供的 LinkedIn 長文（OpenClaw vs Claude Code 體感差異分析）

---

## 研究背景

同樣是 Opus 4.6，OpenClaw 寫 code 普通，Claude Code 寫 code 強。不是模型問題，是「身體」和「約束」被調去解不同問題。這個觀察引出了一個更深的問題：

**Agent 的能力上限到底是由什麼決定的？**

---

## 核心等式的演化

### 原始等式（LangChain / Viv Trivedy）

```
Agent = Model + Harness
```

> 「If you're not the model, you're the harness. A harness is every piece of code, configuration, and execution logic that isn't the model itself. A raw model is not an agent.」
> — Viv Trivedy, LangChain

### 精化等式（Zeuik 工作框架）

```
Agent = Model + Body + Harness
```

這不是術語修正，是**本質區分**：

| 層 | 定義 | 解的問題 | 典型組件 |
|----|------|---------|---------|
| **Model** | 大腦，intelligence 本身 | 推理、理解、生成 | GPT-5 / Claude Opus 4.7 |
| **Body** | 手腳，能力延伸 | 能不能做事 | bash、filesystem、MCP、browser、sandbox |
| **Harness** | 約束，行為校準 | 會不會做歪 | CLAUDE.md、hooks、planner-evaluator、sub-agent 結構 |

**關鍵區分**：body 解決「能力存在」，harness 解決「行為可預測」。沒有手腳的大腦只能空想；沒有約束的手腳會做歪。

---

## 實驗數據：Harness 的量化貢獻

### Terminal-Bench 2.0：同模型不同 Harness 的分數差距

Claude Opus 4.6 在相同 benchmark 上：

| Harness | 準確度 |
|---------|--------|
| ForgeCode | 79.8% ± 1.6 |
| Capy | 75.3% ± 2.4 |
| TongAgents | 71.9% ± 2.7 |
| Crux | 66.9% |

**結論：同一個 Opus 4.6，不同 harness 造成 13pp 分數差距。**

### Stanford Meta-Harness 研究

同模型，harness 變化範圍：59.6% → 76.4%（16.8pp 差距）

### Ewan Mak 實地案例（Claude Sonnet 4.6）

| 階段 | 準確度 | 方法 |
|------|--------|------|
| Baseline | 58% | 無優化 |
| After harness optimization | 81% | 提示優化 + subagent 委派 + 中介觀測 |

**結論：Harness 優化交付 15-25pp 提升，與模型升級效果相當。**

---

## Anthropic April 23 Postmortem：Harness 級變更如何出包

2026 年 3-4 月，Claude Code 品質下滑的三個根因：

| 事件 | 時間 | 變更內容 | 影響 |
|------|------|---------|------|
| Reasoning effort 降級 | 3/4 | default: high → medium | 「Claude 感覺不夠聰明」 |
| Caching loop bug | 3/26 | thinking history 每輪清空（應每小時） | 「forgetful and repetitive」 |
| Verbosity 限制 | 4/16 | 系統提示加 ≤25/≤100 words 限制 | Opus coding 品質下降 3% |

**官方承認**：「The models themselves were not to blame, but three separate issues in the Claude Code harness caused complex but material problems which directly affected users.」

**關鍵教訓**：Harness 改一行就能讓整個 output 分布跑掉，因為它直接校準分布。

---

## Context Rot：為什麼 Sub-Agent 是 Context Firewall

### Chroma 實驗數據

- 18 個模型在 NIAH（needle-in-a-haystack）任務上全部隨 context 增長而下降
- 即使是簡單任務（文字複製）在 2,500+ token 後也崩潰
- 加入語義相關但不正確的 distractor → 性能複合下降
- 悖論：隨機排列的 haystack 表現反而優於邏輯連貫文件（18 個模型一致）

### 實踐啟示

Context rot 不能靠「更大的 context window」解決，只能靠結構性切割：

```
Sub-Agent = Context Firewall

主 Agent 只看到：
  → 給 sub-agent 的 prompt
  → sub-agent 的最終結論

中間過程（grep 輸出、工具呼叫、中間檔案讀取）
  → 留在 child context
  → 不污染主 thread
```

---

## Anthropic 三層架構：Planner / Generator / Evaluator

來自 Anthropic engineering blog《Harness Design for Long-Running Apps》：

```
User Brief
  │
  ▼
PLANNER AGENT
  └─ 轉成細粒度 spec（防止 scope 爆炸）
  │
  ▼
GENERATOR AGENT
  └─ 逐項實作
  └─ 遇到 context limit → 完整 reset（不靠摘要）
  │
  ▼
EVALUATOR AGENT
  └─ Playwright / 外部工具（非模型自評）
  └─ Hard threshold：任一失敗 → sprint 失敗
  │
  ▼
(Feedback Loop)
```

**為什麼不能讓同一個 agent 自評**：Generator 「自信地稱讚自己的工作，即使品質明顯平庸」——self-evaluation 永遠偏正向。

---

## Harness 的 11 大構件（Stanford 分類）

1. Orchestration loop
2. Tools
3. Filesystem
4. Bash / Code execution
5. Sandbox
6. Memory
7. Context management
8. **Context rot defense** ← 最容易被忽略
9. Long-horizon execution
10. Error handling / Guardrails
11. Serving layer

---

## Ratchet 原則（Mitchell Hashimoto）

> 「Anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that mistake again.」

每一條 CLAUDE.md 規則、每一個 hook，都應該追得回某次具體的失敗。

Addy Osmani 的延伸：「Every line in a good AGENTS.md should be traceable back to a specific thing that went wrong.」

---

## Model 變強之後，Body 和 Harness 各自的走向

| 層 | Model 變強後的走向 | 原因 |
|----|----------------|------|
| **Body** | 長新器官：Computer Use → 多 agent 並行 → 跨 device | Model 能力提升，body 用得更好、能長更多東西 |
| **Harness** | 搬家但不消失：舊 scaffolding 退場，新 scaffolding 長出來 | Harness 解的是 non-determinism 這個結構問題，不是 model 弱的問題 |

**真正會被 model 進步解掉的 harness**：補弱點用的（subagent for context isolation、early-stop 機制）

**永遠不會消失的 harness**：校準 non-deterministic 系統用的（hooks、verification、planner-evaluator）

---

## 參考資料

| 來源 | 核心貢獻 |
|------|---------|
| Viv Trivedy / LangChain | Agent = Model + Harness 原始等式 |
| HumanLayer《Skill Issue》 | CLAUDE.md + hooks 的具體 harness 工程實踐 |
| Anthropic 4/23 Postmortem | 三個 harness 級變更的失敗解剖 |
| Anthropic 《Effective Harnesses》 | 跨 session 狀態管理（Initializer + Progress + Git） |
| Anthropic 《Harness Design》 | Planner/Generator/Evaluator 三層架構 |
| Anthropic 《Building Effective Agents》 | 六種設計模式；從簡單 prompt 開始 |
| Chroma 《Context Rot》 | 18 個模型的量化衰退數據；NIAH benchmark |
| Ewan Mak《70% Rule》| 58%→81% harness 優化實地案例 |
| Terminal-Bench 2.0 | 同模型不同 harness 的 13pp 分數差距 |
| Simon Willison | Agentic loop 設計原則；測試套件是 loop 基礎 |
| Mitchell Hashimoto | Ratchet 原則：mistake → permanent rule |
| Addy Osmani | AGENTS.md 每行可追蹤到具體失敗 |

---

## 2026-05 新論文待閱讀隊列

- [ ] Continual Harness (2605.09998) — Online adaptation; runtime modification without retraining
- [ ] Harness Engineering as Categorical Architecture (2605.12239) — Category theory framework for tool composition
- [ ] AI Harness Engineering: Runtime Substrate (2605.13357) — Execution layer taxonomy
- [ ] Effective Harness Engineering for Algorithm Discovery (2605.15221) — Vesper framework with empirical benchmarks
- [ ] Code as Agent Harness (2605.18747) — Tool schema compilation from code structure
- [ ] Adapting the Interface, Not the Model (2605.22166) — Interface-level runtime adaptation
- [ ] Cheating Agents: Benchmark Manipulation (DebugML 2026-05-23) — Evaluation validity implications
- [ ] Coordination Architectural Layer (2605.03310) — Multi-agent coordination layer
- [ ] HeavySkill (2605.02396) — Extended reasoning within skill invocations
