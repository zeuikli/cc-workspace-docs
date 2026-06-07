---
title: "Cognitive Architectures for Language Agents"
authors: "Theodore R. Sumers, Shunyu Yao, Karthik Narasimhan, Thomas L. Griffiths"
published: 2023-09-05
source: "https://arxiv.org/abs/2309.02427"
venue: TMLR 2024
---

# Cognitive Architectures for Language Agents (CoALA)

**Authors**: Theodore R. Sumers, Shunyu Yao, Karthik Narasimhan, Thomas L. Griffiths  
**Affiliations**: Princeton University; Google DeepMind  
**Published**: September 5, 2023 (v1); revised March 15, 2024 (v3)  
**Venue**: Transactions on Machine Learning Research (TMLR 2024)  
**Source**: https://arxiv.org/abs/2309.02427  
**arXiv ID**: 2309.02427  
**DOI**: 10.48550/arXiv.2309.02427  
**Categories**: cs.AI, cs.CL

---

## Abstract

Language models (LMs) are increasingly being used as the backbone of sophisticated AI agents. While the cognitive science literature has long studied how humans and animals make decisions, the analogous work on LM-based agents remains fragmented. To address this, we propose CoALA (Cognitive Architectures for Language Agents), a conceptual framework that organizes agents with modular memory components, a structured action space to interact with internal memory and external environments, and a generalized decision-making process. We use CoALA to retrospectively survey and catalog a large body of recent agent work, revealing key trends and gaps in the literature. We then use it to prospectively identify directions for future research. Our framework contextualizes language agents within the broader history of AI and cognitive science, outlining a path towards language-based general intelligence.

---

## 框架核心：CoALA 的四維度組織

### 1. 記憶組件（Memory Components）

CoALA 將記憶分為四類：

| 記憶類型 | 內容 | 更新機制 | 示例 |
|---------|------|---------|------|
| **Working Memory** | 當前上下文（輸入、行動歷史、觀察） | 每步更新 | Context window |
| **Episodic Memory** | 過去 episode 的具體記錄 | 寫入、提取 | 對話歷史、任務軌跡 |
| **Semantic Memory** | 一般知識、事實 | 寫入、提取 | 知識庫、維基百科片段 |
| **Procedural Memory** | 行動序列、技能 | 學習、編寫 | 代碼庫、工具文檔 |

**關鍵洞見**：LM 的預訓練知識本身是一種**隱式語義記憶**，而 RAG、MemGPT 等系統提供的是**顯式外部記憶**。二者的整合是當前研究核心問題。

### 2. 行動空間（Action Space）

```
行動空間（Agent Actions）
├── 記憶操作（Memory Ops）
│   ├── 讀取（Read）：從記憶中提取資訊
│   └── 寫入（Write）：向記憶中添加/更新資訊
├── 內部行動（Internal Actions）
│   ├── 推理（Reasoning）：CoT、ToT
│   └── 反思（Reflection）：評估過去行動
└── 外部行動（External Actions）
    ├── 工具使用（Tool Use）：搜索、計算器
    └── 環境互動（Environment Interaction）：代碼執行、API 調用
```

### 3. 決策過程（Decision-Making Process）

```
當前觀察 → Working Memory 更新
          → 記憶提取（從 Episodic/Semantic/Procedural）
          → LM 推理（選擇行動）
          → 行動執行
          → 觀察 → 記憶更新
                 → 反思（若觸發條件滿足）
```

### 4. 學習機制（Learning Mechanism）

| 層次 | 方法 | 記憶更新 |
|------|------|---------|
| 上下文學習（in-context） | Few-shot examples | Working Memory |
| 記憶更新（memory update） | 寫入外部記憶 | Episodic/Semantic |
| 參數更新（param update） | 微調 | Procedural（隱式）|

---

## 文獻回顧框架

### 記憶操作分類
| 操作 | 系統示例 |
|------|---------|
| 讀取（Retrieval） | RAG, MemGPT (Load from Recall) |
| 寫入（Write） | MemGPT (Push to Archival), Generative Agents |
| 整合（Consolidation） | Generative Agents 反思層 |
| 遺忘（Forgetting） | MemoryBank (Ebbinghaus曲線) |

### 代表性系統的 CoALA 分類

| 系統 | 記憶類型 | 核心行動 | 學習方式 |
|------|---------|---------|---------|
| ReAct | Working | 推理+行動 | In-context |
| Reflexion | Episodic | 反思 | In-context |
| MemGPT | Episodic+Semantic | 記憶讀寫 | In-context |
| Voyager | Procedural | 技能生成 | 記憶更新 |
| Generative Agents | 全四種 | 規劃+反思 | In-context |

---

## 研究缺口與未來方向

CoALA 識別的關鍵未解問題：

1. **記憶一致性**：如何在多種記憶形式之間保持一致性？（Working → Episodic → Semantic 更新的同步問題）

2. **遺忘機制**：何時刪除舊記憶？主動遺忘（learned forgetting）vs 被動衰減

3. **記憶壓縮**：如何在壓縮記憶時保留關鍵資訊？（與 2605.12978 的 consolidation 退化問題直接相關）

4. **跨 session 持久化**：多 session 代理人的狀態保持問題

5. **記憶評估標準**：缺乏統一的基準來評估不同記憶機制

---

## 對 LLM 記憶控制研究的定位作用

CoALA 是 LLM 記憶研究的**統一分類框架**。當解讀以下研究時，CoALA 提供了對應的術語：

- **MemGPT** = 顯式管理 Episodic + Semantic Memory 的讀寫
- **Reflexion** = Episodic Memory 的反思更新
- **Generative Agents** = 全類型記憶 + 整合（consolidation = Episodic → Semantic）
- **2605.12978** = 發現 Episodic → Semantic 整合的失真問題（consolidation failure）
- **δ-mem** = 在 Procedural Memory 層面引入參數記憶（不同於上層管理）

---

## 引用

```bibtex
@article{sumers2023cognitive,
  title={Cognitive Architectures for Language Agents},
  author={Sumers, Theodore R and Yao, Shunyu and Narasimhan, Karthik and Griffiths, Thomas L},
  journal={Transactions on Machine Learning Research},
  year={2024}
}
```

---

**關鍵詞**: 認知架構, 語言代理人, 記憶分類, 工作記憶, 情節記憶, 語義記憶, 程序記憶, 行動空間
