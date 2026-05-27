---
title: "Generative Agents: Interactive Simulacra of Human Behavior"
authors: "Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein"
published: 2023-04-07
source: "https://arxiv.org/abs/2304.03442"
venue: UIST 2023
---

# Generative Agents: Interactive Simulacra of Human Behavior

**Authors**: Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein  
**Affiliations**: Stanford University, Google Research  
**Published**: April 7, 2023 (v1); revised August 6, 2023 (v2)  
**Venue**: UIST 2023  
**Source**: https://arxiv.org/abs/2304.03442  
**arXiv ID**: 2304.03442  
**Categories**: cs.AI, cs.HC

---

## Abstract

We introduce generative agents — computational software agents that simulate believable human behavior. Generative agents wake up, cook breakfast, and head to work; artists create, writers write; they form opinions, notice each other, and initiate conversations; they remember and reflect on days past as they plan the next day. To enable generative agents, we describe an architecture that extends a large language model to store a complete record of the agent's experiences using natural language, synthesize those memories into higher-level reflections, and retrieve them dynamically to plan behavior. We instantiate generative agents to populate an interactive sandbox environment inspired by The Sims, in which end users can interact with a small town of twenty-five agents using natural language. In an evaluation, these generative agents produce believable individual and emergent social behaviors: for example, starting with the single user-generated notion that one agent wants to throw a Valentine's Day party, by the day of the party, agents autonomously spread invitations to the party over the course of two days, make new acquaintances, ask each other out on dates to the party, and coordinate to show up for the party together at the right time.

---

## 核心貢獻

### 問題
現有 AI 代理人缺乏可信賴的人類行為模擬能力——無法維持長期記憶、反思過去，或基於累積經驗規劃未來行動。

### 架構三要素

**1. 記憶流（Memory Stream）**
- 外部資料庫：以自然語言儲存代理人的所有體驗
- 每個記憶條目記錄：事件描述、時間戳記、重要性分數
- 儲存粒度：從「早餐吃了什麼」到「有人讓我失望了」

**2. 記憶檢索（Retrieval）**
三因子加權得分決定哪些記憶被喚起：

```
relevance = α₁·recency + α₂·importance + α₃·relevance_to_query
```

- **Recency**：時間衰減（指數衰減，沙盒世界小時為單位）
- **Importance**：記憶被存入時由 LLM 打分（1–10）
- **Relevance**：與當前情境的語義相似度

**3. 反思（Reflection）**
- 觸發條件：最近記憶的重要性總和超過閾值（100 分）
- LLM 從記憶流中提問「什麼問題值得深思？」
- 生成高層次洞見（如「Isabella 是一個關心他人的人」）
- 反思本身也存入記憶流，可被再次反思（遞迴反思）

**4. 規劃（Planning）**
- 每日計畫：起床時生成粗粒度一天計畫
- 動態更新：遇到意外事件時重新規劃

---

## 消融實驗（Ablation Studies）

測試移除各組件的影響：

| 條件 | 現象 |
|------|------|
| 無記憶（no memory） | 代理人忘記過去交互，行為不連貫 |
| 無反思（no reflection） | 48 小時後退化為重複性無狀態回應 |
| 無規劃（no planning） | 無法維持跨對話的目標一致性 |
| 完整架構 | 產生可信的個體與社會湧現行為 |

**關鍵發現**：反思移除後效果最顯著——**48 小時內行為從多日規劃退化為重複無狀態回應**。這表明反思不是優化，而是維持複雜行為的必要條件。

---

## 評估方法

### 可信度評估
- **自我評估訪談**：詢問代理人過去行動，評估答案一致性
- **知識評估**：測試代理人對環境的認知是否符合實際
- **社會評估**：觀察代理人之間的互動是否符合人際關係邏輯

### 湧現行為觀察
- 情人節派對：從單一種子意圖（一個代理人想辦派對），2 天內自主傳播邀請、相約同行
- 謠言傳播：一條信息在社交網絡中自然擴散
- 求職競爭：多個代理人競爭同一職位的社交動態

---

## 記憶架構的局限

1. **成本**：每個 agent 每步推理需多次 LLM 調用（記憶、反思、規劃各一次）
2. **記憶噪聲**：LLM 可能在反思時引入幻覺
3. **長期漂移**：極長時間後，早期記憶在衰減中消失，影響身份連貫性
4. **評估困難**：「可信的人類行為」無量化標準

---

## 與本論文的直接關聯（2605.12978）

Generative Agents 是第一個展示反思式記憶整合的代理人系統。然而，**2605.12978（Useful Memories Become Faulty）**正是指出這種整合的危險性：

- Generative Agents 的反思層相當於 **consolidation**
- 2605.12978 發現：即使從正確的原始記憶整合，LLM 重寫記憶的過程本身就引入失真
- 消融實驗顯示反思不可缺少 ≠ 反思不會出錯
- **啟示**：Generative Agents 的成功可能部分依賴任務的短時間尺度；長期運行的整合退化問題需要後續研究

---

## 引用

```bibtex
@inproceedings{park2023generative,
  title={Generative Agents: Interactive Simulacra of Human Behavior},
  author={Park, Joon Sung and O'Brien, Joseph C and Cai, Carrie J and Morris, Meredith Ringel and Liang, Percy and Bernstein, Michael S},
  booktitle={Proceedings of UIST 2023},
  year={2023}
}
```

---

**關鍵詞**: 生成式代理人, 記憶流, 反思機制, 可信行為模擬, 社會湧現行為, 記憶整合
