---
url: "https://www.preprints.org/manuscript/202604.0428/v1"
title: "Agent Harness for Large Language Model Agents: A Survey"
date: 2026-04-07
type: article
---

# Agent Harness for Large Language Model Agents: A Survey

**原始來源**：https://www.preprints.org/manuscript/202604.0428/v1  
**作者**：Qianyu Meng 等 9 位  
**發表日期**：2026-04-07  
**評分日期**：2026-05-05

---

## 繁體中文全文摘要

### 核心論點

Agent 執行基礎設施——而非底層模型能力——決定了部署 LLM 系統的可靠性。

> 「harness 層級的改變單獨就能在編碼 benchmark 上產生高達 10× 的效益提升，而無需修改模型。」

從 OpenAI、Stripe 和 METR 的從業者報告中得到佐證：基礎設施投資帶來的效能改善**可媲美或超越**模型升級。

### 正式定義框架：H=(E,T,C,S,L,V)

#### E — Execution Loop（執行循環）
核心控制流，主導模型與工具的互動：
- Plan-act-observe 循環
- Verifier-operator-feedback 模式
- Agent-computer interface 流程
- 多 Agent 協調

#### T — Tool Integration（工具整合）
模型如何存取和使用外部能力：
- API/工具呼叫語義
- 錯誤處理和重試邏輯
- 工具抽象和組合

#### C — Context Management（Context 管理）
資訊如何在模型間流動：
- 輸入提示詞構建
- 歷史壓縮和 windowing
- Token 預算分配

#### S — State Persistence（狀態持久化）
系統狀態如何跨互動持久化：
- 長期記憶機制
- 基於文件的狀態儲存
- Session 管理

#### L — Lifecycle Governance（生命週期治理）
系統如何管理資源和執行政策：
- 預算追蹤（token、成本、時間）
- 核准流程和上升機制
- 檢查點和恢復

#### V — Evaluation Interfaces（評估介面）
系統效能如何被測量和優化：
- 結果評分
- Trace 分析
- 改進反饋循環

### 歷史脈絡

三條獨立的脈絡匯聚到共同模式：
1. **軟體測試 harness**：控制執行環境 + stimulus-response 觀察
2. **強化學習環境**（OpenAI Gym）：明確的狀態、動作、獎勵協議
3. **早期 LLM 框架**（LangChain、AutoGPT）：逐漸形式化的執行模式

### 22 個系統的實證分類

#### 執行循環模式
- 單 Agent 循環（基本 ReAct）
- 規劃者-驗證者結構（分層規劃）
- Agent-computer interface 循環
- 多 Agent 協調（平行/循序 Agent 團隊）

#### 工具整合方式
- 直接函式呼叫
- API 工具抽象（OpenAI Functions、Claude Tools）
- 可執行程式碼生成和沙箱化
- Web 自動化和 UI 互動

#### 狀態管理策略
- 暫態（對話歷史）
- 文件狀態（持久文件、日誌）
- 資料庫狀態（結構化記憶）
- 混合方法（多層狀態）

### 九大跨領域技術挑戰

| 挑戰 | 說明 |
|------|------|
| **沙箱和安全** | 隔離執行以防止資源耗盡、資料洩漏、意外系統修改 |
| **評估和評分** | 無確定性答案時的成功標準；exact-match + behavioral + LLM-jury 組合 |
| **協議標準化** | 缺乏通用 agent-harness 通訊協議；MCP vs. A2A 競爭 |
| **計算經濟學** | 在任務複雜度和推理深度增加時管理 token 消耗 |
| **長 Context 管理** | 處理延伸互動歷史和診斷 trace |
| **工具組合和依賴** | 協調複雜多工具工作流，並明確追蹤依賴 |
| **可重現性和追蹤** | 捕捉完整執行 trace 用於除錯和系統比較 |
| **失敗恢復和上升** | 當 agent 達到邊界（信心極限、資源限制）時的健壯恢復 |
| **遷移和泛化** | 讓發現的 harness 模式跨不同模型、領域和任務族群遷移 |

### 實證證據

- **HAL**：同樣模型在不同 harness 設計上產生 2-4× 效能差異
- **SWE-bench 分析**：harness 基礎設施佔效能差異的 >40%
- **AgencyBench**：多 Agent 協調模式（規劃者-驗證者、ensemble 投票）比單 Agent 基準一致高出 15-30%，即使使用相同基礎模型

### 對 Workspace 的啟示

1. **H=(E,T,C,S,L,V) 框架作為 harness 審計工具**：可用於系統性稽核 cc-workspace 的六個維度
2. **九大挑戰的對應機制**：cc-workspace 已有相應設計（L→生命週期 hooks、C→compact 觸發、V→/deep-review）
3. **2-4× 效能差異**：harness 改善 ≥ 模型升級的直接理論支撐
4. **標準化評估**：harness-eval skill 的設計應覆蓋 V（評估介面）維度

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 7/10 | H=(E,T,C,S,L,V) 框架可作為 harness-eval 的結構骨架；九大挑戰提供系統性審計清單 |
| B. 創新性 | 7/10 | 正式化六分量框架和 22 個系統分析是學術貢獻；但觀念本身並非全新 |
| C. 證據品質 | 8/10 | HAL、SWE-bench、AgencyBench 三個實驗支撐，量化數據（10×、>40%、15-30%）具體 |
| D. 技術深度 | 8/10 | 22 個系統的詳細分類、歷史脈絡分析、九大挑戰的系統性描述 |
| E. 泛化性 | 9/10 | 正式框架設計為跨系統、跨模型、跨任務通用 |
| **加權總分** | **7.65/10** | 7×0.3 + 7×0.2 + 8×0.2 + 8×0.15 + 9×0.15 = 2.1+1.4+1.6+1.2+1.35 |

**整合決策**：Rule  
**整合位置**：`.claude/refs/harness-design.md`（H=(E,T,C,S,L,V) 框架作為設計稽核工具）  
**整合狀態**：待實作

**TODO**：
- 在 harness-design.md 加入 H=(E,T,C,S,L,V) 六維框架作為稽核 checklist
- harness-eval skill 的 scorecard 可參考本 survey 的九大挑戰設計評估維度
