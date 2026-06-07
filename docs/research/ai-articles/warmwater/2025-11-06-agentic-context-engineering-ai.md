---
url: "https://warmwater.dev/blog/agentic-context-engineering-ai"
title: "Agentic Context Engineering：讓 AI 代理人自我改進的關鍵技術"
date: 2025-11-06
category: Paper Notes
source: warmwater.dev
---

[
← Paper Notes ](/blog?tag=Paper%20Notes)  Paper Notes  
#  Agentic Context Engineering：讓 AI 代理人自我改進的關鍵技術 
  2025-11-06 · — views      


## 前言


在 AI 代理人（Agent）的開發過程中，我們經常遇到一個棘手的問題：如何讓代理人持續學習並改進，而不是在多次互動後逐漸「失憶」或產生錯誤？這就是「情境工程」（Context Engineering）要解決的核心挑戰。


今天要介紹的 **Agentic Context Engineering (ACE)** 框架，提供了一個創新的解決方案，讓 AI 系統能夠像人類一樣，透過經驗累積專業知識，並持續優化自己的表現。

## 情境工程面臨的五大痛點


在深入了解 ACE 之前,我們先來看看現有的情境工程方法遇到了哪些問題：

### 1. 情境污染 (Context Poisoning)


當錯誤資訊（例如 RAG 檢索錯誤）滲入情境後，會污染整個推理鏈。舉例來說，一個遊戲 AI 可能會產生「物品欄中有某個道具」的幻覺，然後浪費多個回合試圖使用這個根本不存在的物品。

### 2. 情境分心 (Context Distraction)


長情境視窗中充斥著無關資訊時，會壓倒模型的注意力機制。這就像在一堆雜訊中尋找訊號，模型容易忽略真正重要的核心任務。

### 3. 情境混淆 (Context Confusion)


結構不良的情境可能導致非預期的行為。例如，聊天機器人在處理圖片生成請求時，卻意外地從記憶中提取並注入了使用者的地理位置資訊。

### 4. 情境衝突 (Context Clash)


當情境中存在矛盾資訊時（如過時文件 vs. 最新文件），模型必須在沒有明確指導下做出選擇，導致不可預測的結果。

### 5. 迷失在中間 (Lost in the Middle)


LLM 處理長情境時呈現 U 型性能曲線——對開頭和結尾的資訊記憶最深刻，對中間部分容易忽略。這是 Transformer 架構注意力機制的根本限制。

## ACE 框架：動態備忘錄的創新設計


### 核心理念


ACE 框架的核心創新在於將情境視為「**動態備忘錄**」（Dynamic Cheatsheet）——一本可以持續演化的作業手冊。不同於傳統靜態提示，ACE 的情境會隨著代理人的經驗不斷優化與累積知識。

### 三大關鍵組件


#### 1. 動態備忘錄 (Dynamic Cheatsheet)


這是知識與情境的結構化存儲核心，支援：


- 細節保存與任務導向知識積累

- 結構化管理，避免知識流失

- 跨任務適應能力


#### 2. 反思器 (Reflector)


負責多輪自我反思與精煉：


- 根據執行回饋動態調整情境內容

- 防止知識流失與簡化偏誤

- 主動補充領域知識與細節


#### 3. 策展器 (Curator)


負責知識的策展、合併與去重：


- 利用非 LLM 技術確保內容完整性

- 高效管理情境內容

- 避免模型幻覺導致的知識崩解


### 運作流程


ACE 採用「**生成→反思→策展→更新**」的漸進式閉環流程：


- **生成階段**：初始情境由生成模組產生

- **執行階段**：代理人執行任務並獲得自然回饋

- **反思階段**：根據回饋進行內容精煉與細節補充

- **策展階段**：合併多輪結果並去除冗餘

- **更新階段**：更新動態備忘錄，準備下一輪疊代


這個流程支持多輪疊代，確保知識逐步積累且細節不流失。

## 技術創新亮點


### 1. 多輪精煉-策展閉環模式


將情境優化分為多個疊代輪次，每輪均包含反思與策展，形成可持續演化的閉環。這種模式可廣泛應用於：


- 知識管理系統

- 提示工程優化

- 代理人記憶管理


### 2. 非 LLM 基礎的合併與去重技術


避免依賴 LLM 進行知識合併，防止：


- 模型幻覺影響知識準確性

- 多次重寫導致的情境崩解（Context Collapse）

- 重要細節在簡化過程中流失


這張圖是呈現Context Collapse的實驗，研究顯示LLM會在第60步，突然將 Context 由原本的 18282 個 Token 縮減為 122 個 Token，導致知識細節流失

### 技術價值


ACE 框架為 AI 系統的自我改進與知識積累提供了：


- **可持續性**：知識能夠長期累積而不流失

- **可擴展性**：模組化設計易於適應新任務

- **高效率**：降低運算成本與適應延遲

- **可解釋性**：結構化的知識管理提升透明度


## 結語


Agentic Context Engineering 突破了傳統情境工程的侷限，為構建能夠自我改進的 AI 代理人提供了堅實的技術基礎。透過動態備忘錄、多輪反思與智能策展的創新組合，ACE 讓 AI 系統能夠像人類專家一樣，持續累積經驗、優化表現，並快速適應新挑戰。


隨著 AI 代理人在各領域的應用日益廣泛，ACE 這類能夠支撐持續學習與自我改進的技術框架，將成為打造下一代智能系統的關鍵基石。

---


## 參考資源


- [Agentic-Context-Engineering 論文解析](https://datasciocean.com/paper-intro/agentic-context-engineering/)

- [情境工程（Context Engineering）解析：打造實用 AI Agent 的關鍵技巧](https://ikala.ai/zh-tw/blog/ikala-ai-insight/introduction-to-context-engineering-ai-agent-vs-prompt-engineering/)


## 延伸閱讀


- [ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](/blog/reasoningbank-scaling-agent-self-evolving-with-reasoning-memory) — 同樣的 context 管理問題，從論文角度看推理記憶的結構化設計

- [Dynamic Cheatsheet Paper 筆記](/blog/dynamic-cheatsheet-paper) — 另一個 inference-time 自我改進方案：動態備忘錄的運作原理

- [Harness Engineering — AI 工程師的第三個維度](/blog/harness-engineering-ai) — Context Engineering 的上層框架：Harness 管的是讓 context 在系統中安全流動
     [ Paper Notes ](/blog?tag=Paper%20Notes)  
### 
相關文章

[Paper NotesDynamic Cheatsheet Paper 筆記2025-11-06](/blog/dynamic-cheatsheet-paper)[Paper NotesReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory2025-11-03](/blog/reasoningbank-scaling-agent-self-evolving-with-reasoning-memory)[Stock & FinanceTradingAgents: Multi-Agents LLM Financial TradingFramework2025-07-07](/blog/tradingagents-multi-agents-llm-financial-tradingframework)
