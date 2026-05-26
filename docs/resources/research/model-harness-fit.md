# Model-Harness Fit（MHF）

> 來源：2026-05-16 深度研究報告（48 篇 scored articles + 本地研究材料交叉驗證）

**Harness Model Fit（HMF）** 描述 harness 設計與目標模型能力之間的對齊程度。這是 Harness Engineering 的核心子問題：harness 的每一個元件是否和「當前模型的能力邊界」正確對齊？

---

## 核心等式

```
Harness ⊇ Context ⊇ Prompt
```

Harness 是最外層，決定模型的整個執行環境。Context 是模型在單次 session 中能「看到」的內容。Prompt 是具體的指令輸入。**所有 prompt 工程技巧的效益上限，都被 harness 設計所封頂。**

---

## 三種 Harness-Model 失配狀態

| 失配類型 | 描述 | 症狀 |
|---------|------|------|
| **Over-scaffolding** | Harness 補足已不必要的缺口 | 冗餘提示詞、不必要的驗證步驟、token 浪費 |
| **Under-scaffolding** | Harness 沒有覆蓋模型實際能力邊界 | Agent 行為不可預測、錯誤恢復失敗 |
| **Model-drift** | 模型升級後 harness 未隨之更新 | 舊假設累積成死重，效能低於預期 |

> **Anthropic 的長期觀點**：每個 harness 元件都是一項假設——「模型無法自行完成 X，因此 harness 補足它」。模型能力提升時，需要年度 harness audit 系統性移除過時假設。

---

## 量化證據

同一模型在不同 harness 中的效能差距 **5.2–40 個百分點**：

| 案例 | 介入 | 效果 |
|------|------|------|
| Can.ac | Harness 重設計 | 6.7% → 68.3%（**10 倍**）|
| LangChain | 純 harness 改善 | 52.8% → 66.5%（**+13.7pp**，不換模型）|
| SWE-agent CLI 重設計 | 無模型改變 | ~40% 提升 |
| AgentFlow 同模型不同 harness | 效能差 4 倍 | 量化確認 |
| AgentOpt 最佳/最差模型組合 | 相同準確率 | 成本差 **13-32 倍** |
| Terminal-Bench 2.0（ForgeCode vs Crux）| 同 Opus 4.6 | 79.8% vs 66.9%（**13pp**）|

---

## 六維正式框架

**Agent Harness Survey（2026-04-07）** 提出：

```
H = (E, T, C, S, L, V)
```

| 維度 | 說明 |
|------|------|
| **E（Execution Loop）** | ReAct / Plan-Execute / Planner+Executor 分離 |
| **T（Tool Integration）** | 工具介面設計、lazy loading、授權邊界 |
| **C（Context Management）** | 壓縮策略、記憶分層、rot 防止 |
| **S（State Persistence）** | 跨 session 記憶、checkpoint、filesystem |
| **L（Lifecycle Governance）** | hooks、guardrails、safety gates |
| **V（Evaluation Interfaces）** | 驗證迴路、量化指標、regression 測試 |

---

## 七大架構決策軸

根據 Anatomy of Agent Harness（2026-04-01），任何 harness 設計必須在以下七個軸做出選擇：

| 軸 | 選項 | 建議 |
|----|------|------|
| 1. 單 Agent vs 多 Agent | Single / Multi | 單一 well-harnessed agent 在大多數任務優於多個弱協調的專業 agent |
| 2. 執行模式 | ReAct / Plan-Execute | ReAct 適探索性任務；Plan-Execute 適長序列確定性任務 |
| 3. Context 壓縮策略 | Rolling window / Summary / Hierarchical | 雙層方案（Confucius）效果最佳 |
| 4. 工具數量 | 單一 / 分割 | 超過 10 個工具應分割 sub-agent；lazy loading 減少 95% 平時 token |
| 5. 驗證機制深度 | 規則型 / 視覺 / LLM-as-judge | 三層組合達 2-3× 品質提升 |
| 6. 記憶持久化方式 | Filesystem / Context window / Episodic | 長期 filesystem，短期 context，跨 session episodic notes |
| 7. 錯誤恢復層次 | Retry / Rollback / Decompose / Escalate | 四層分級，從最廉價到最昂貴 |

---

## CAR 框架

**CAR（2026-04-23）** 將執行層分解為三維度：

| 維度 | 說明 | 範例 |
|------|------|------|
| **C（Control）** | 執行前編碼的約束 | CLAUDE.md、linter、pre-commit |
| **A（Agency）** | 模型的動作空間與工具介面 | Tool registry、allowed tools |
| **R（Runtime）** | 時間性治理 | hooks、PostToolUse、Stop hooks |

---

## Feedforward vs Feedback Controls

根據 Martin Fowler 的分析：

### Feedforward（引導型）— 預防問題

- CLAUDE.md 常駐規則
- ADR（架構決策記錄）
- Structural tests（架構合規測試）
- Conditional rules / globs

### Feedback（感知型）— 發現問題

| 機制 | 反饋速度 | 修正成本 |
|------|---------|---------|
| PostToolUse hooks | ms 級 | 趨近於零 |
| Pre-commit linters | seconds 級 | 低 |
| CI 測試 | minutes 級 | 中 |
| Human review | hours 級 | 高 |

**關鍵洞見**：Feedback 速度層次決定修正成本。PostToolUse 在 ms 內攔截問題，成本趨近於零；Human review 在數小時後才發現，修正成本倍增。

---

## Tool Format 的 Byte-Level 重要性

MHF 研究的一個關鍵發現：**工具介面格式是 byte-level 的後訓練習慣**。

- OpenAI 模型訓練時使用 V4A patch 格式
- Claude 模型訓練時使用 string-replace 格式
- **跨模型遷移工具格式 → 推理 token 增加 + 錯誤率上升**

這解釋了為什麼 Claude Code 的 `apply_patch` 工具比同等功能的其他工具更有效——模型和工具是協同訓練的。

---

## Model 升級後的 Harness Audit

**Anthropic April 23 Postmortem（2026-04-23）** 提供了一個反面教材：

Claude Code 的品質回歸不是模型退化，而是三項 harness 改動的累積效果：
1. 推理預算 default 值：`high` → `medium`（降低延遲，但智力下降）
2. KV cache bug：推理歷史每輪清除，而非每 session 清除
3. 系統提示字數限制：「≤25 words between tool calls」造成 3% 智力下降

**預防措施**：
- 每次 harness 改動都需要回歸測試
- Reasoning effort 改變 = harness 改動 = 需要測試
- System prompt 修改 = harness 改動 = 需要 regression suite
- 漸進式 rollout（5% → 25% → 100%）

---

## 年度 Harness Audit 清單

模型每次升級後應審查：

- [ ] **Context reset 機制**：模型是否已能自行管理 context？（消除 Over-scaffolding）
- [ ] **Retry logic**：模型是否已更可靠，retry 層可以簡化？
- [ ] **Validation prompts**：哪些驗證提示是模型現在原生具備的能力？
- [ ] **Tool descriptions**：措辭是否需要更新以配合新模型的理解方式？
- [ ] **Reasoning effort default**：新模型的預設 effort 是否適合你的工作負載？
- [ ] **Sub-agent boundary**：哪些任務現在可以由單一 agent 完成，不再需要委派？

---

## 延伸閱讀

- [Harness Engineering 研究全景](/resources/research/harness-engineering/)
- [跨源知識地圖](/resources/research/knowledge-map/)
- [Lecture 01：Claude Code 與 Harness 基礎](/lectures/lecture-01-foundations/)
- [Lecture 04：Harness 三層架構](/lectures/lecture-04-harness-architecture/)
