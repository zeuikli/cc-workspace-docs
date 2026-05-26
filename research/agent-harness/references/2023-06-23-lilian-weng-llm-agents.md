# LLM Powered Autonomous Agents

- **作者**: Lilian Weng（OpenAI Research）
- **URL**: https://lilianweng.github.io/posts/2023-06-23-agent/
- **發表**: 2023-06-23
- **收錄日期**: 2026-05-01
- **重要性**: Priority B — 業界標準入門文章；Planning-Memory-Tools 三層框架的經典定義

---

## 核心框架：三層架構

### 1. Planning 層
- **Task Decomposition**: 複雜任務自動分解為可執行的子目標
  - Chain of Thought (CoT): 逐步推理
  - Tree of Thoughts (ToT): 樹狀探索多條推理路徑
- **Self-Reflection**: 讓 agent 從錯誤中學習
  - ReAct: Thought-Action-Observation 交錯
  - Reflexion: 語言形式的強化學習

### 2. Memory 層

| 記憶類型 | 對應概念 | 技術實現 |
|---------|---------|---------|
| Sensory Memory | 感知輸入 | 原始 input（圖像、文字） |
| Short-term Memory | 上下文學習 | Context Window（有限長度） |
| Long-term Memory | 外部存儲 | 向量資料庫（FAISS、ANNOY） |

**MIPS 快速近似向量搜尋算法**:
- LSH（Locality-Sensitive Hashing）
- ANNOY（Approximate Nearest Neighbors Oh Yeah）
- FAISS（Facebook AI Similarity Search）
- ScaNN（Scalable Nearest Neighbors）

### 3. Tools/Action 層
- 讓 agent 調用外部 API 超越訓練數據限制
- MRKL：Modular Reasoning, Knowledge, and Language
- 工具使用能力由 LLM 的理解力決定

---

## 核心洞見（對 Harness Engineering 最相關）

1. **Task Decomposition 是 Harness 分層的理論依據**: 複雜任務必須分解才能可靠執行，直接對應 Planner-Generator-Evaluator 三層

2. **三層記憶設計是現代 Agent 的基礎**: 短期（context）+ 長期（檢索）混合模式已成行業標準

3. **工具可靠性挑戰**: 自然語言界面與外部系統協調的脆性（parsing、錯誤處理）是 Harness 設計的核心考量

4. **ReAct 框架是 Agentic Loop 的原型**: Thought-Action-Observation 循環是所有 harness 設計的基礎

5. **Context 窗口的有限性驅動 Memory 架構設計**: 短期記憶的限制決定了 Long-term Memory 的必要性

---

## 歷史地位

這篇文章是 2023 年定義「LLM Agent」概念的分水嶺，是任何 agent harness 工程師必讀的基礎文獻。Planning-Memory-Tools 框架被後來幾乎所有 agent 框架（LangChain、AutoGPT、BabyAGI 等）採用為設計基礎。
