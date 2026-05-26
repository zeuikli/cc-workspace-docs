---
url: https://cursor.com/blog/continually-improving-agent-harness
date: 2026-05-09
source: Cursor Official Blog
authors: Cursor Research Team
tags: [harness-engineering, Terminal-Bench, model-specific-tools, optimization-loop, Model-Harness-Fit]
---

# Cursor: Continually Improving Our Agent Harness

**原始來源**：https://cursor.com/blog/continually-improving-agent-harness  
**作者**：Cursor Research Team  
**歸檔日期**：2026-05-09

---

## TL;DR

Cursor 團隊量化了 harness 對模型效能的影響：相同模型配置不同 harness 可造成數個百分點的差異。核心實踐是「model-specific tool tuning」—OpenAI 模型用 patch-based 編輯、Claude 用 string replacement，並透過 A/B testing + 異常檢測系統化改進。

---

## 核心主張

1. **Model-Harness-Fit 量化證據**
   - 「Harness 和模型共同決定 agent 品質」（the harness and the model together determine how good the agent is）
   - 給模型陌生的工具格式會增加 reasoning tokens 並提升錯誤率
   - Cursor 的量化：修改一項 harness 參數可移動整個 benchmark 排名（從 Top 30 跳至 Top 5）

2. **Model-Specific Tool Provisioning**
   - OpenAI 模型被 trained on patch-based diffs（V4A 格式）→ Cursor 給 `apply_patch` 工具
   - Anthropic Claude 被 trained on string replacement → Cursor 給 `Edit` 工具 + Read 
   - 「Different frontiers trained on different tool shapes」=  post-training 的直接結果

3. **模型行為差異深於表面風格**
   - OpenAI 模型：「more literal and precise in instruction following」
   - Claude：「more intuitive and more tolerant to imprecise instructions」
   - 「Context Anxiety」的差異：一個模型因 context 填滿而拒工作，另一個則健壯運行
   - Harness 設計必須 account for 這些細微差異

4. **Harness Engineering 如同可量測迴圈**
   - Offline：CursorBench 標準化品質檢測
   - Online：A/B testing + Keep Rate 測量（代碼最終留在 codebase 的比率）
   - 自動異常檢測 + 週報：修復工具呼叫的 reliability 到「2 個 9s 或 3 個 9s」

---

## 直接意涵

### cc-workspace 可行動性

1. **Haiku/Sonnet/Opus 三層模型的 harness 調整需求**
   - cc-workspace 跨三個 Anthropic 模型（Haiku 4.5, Sonnet 4.6, Opus 4.7）
   - 推薦在 `.claude/refs/model-selection-grid.md` 中標記「each model generation may require harness tuning」
   - 現狀：subagent-strategy.md 選擇模型，但未記錄「選定後需驗證該模型對現有 harness 是否仍最優」

2. **Tool Reliability 量化指標**
   - Cursor 達成「2-3 個 9s of reliability」為基準
   - cc-workspace 缺乏對 Read/Write/Edit/Bash/Monitor 這些工具的 error rate 監測
   - 建議補充進 `.claude/rules/output-discipline.md` 或新增 `.claude/refs/tool-reliability.md`

3. **A/B Testing 文化**
   - Cursor 的每項 harness 改動都透過 Keep Rate + 語言模型分析驗證
   - cc-workspace 當前依賴人工 session feedback，無系統化的 harness 變更前後對比
   - 適合納入 long-term roadmap（非立即可行，但教科書級實踐）

---

## 評分

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 8/10 | 具體論述 model-specific tool provisioning，直接影響 Haiku/Sonnet/Opus 選擇決策 |
| B. 創新性 | 7/10 | Model-specific tuning 不新奇，但「3-model reliability framework」體系化程度高 |
| C. 證據品質 | 9/10 | 量化 harness impact（Top 30→5 的躍升），A/B test 數據充分 |
| D. 技術深度 | 8/10 | 工具差異（patch vs string replace）、模型行為特徵（literal vs intuitive）都有細節 |
| E. 泛化性 | 8/10 | 原則適用所有多模型 agent 平台；Cursor 特定的 Keep Rate 指標未必可直接轉移 |
| **加權總分** | **8.0/10** | 8×0.3 + 7×0.2 + 9×0.2 + 8×0.15 + 8×0.15 = 2.4+1.4+1.8+1.2+1.2 = 8.0 |

**整合決策**：Rule（補充進 `.claude/refs/model-selection-grid.md` 的 harness-tuning requirements）

---

## 引用關聯

- 推文 @nicbstme 2026-05-04：Cursor「Top 30→Top 5 harness-only」  
- `.claude/refs/model-selection-grid.md`：模型選擇決策樹  
- `.claude/rules/subagent-strategy.md`：三層模型委派規則  
- Terminal-Bench 2.0：Harness impact 量化基準  

