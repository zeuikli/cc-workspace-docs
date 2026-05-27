---
url: "https://cobusgreyling.medium.com/auto-agentic-harness-engineering-b27a962fad9a"
date: 2026-05-02
authors: Cobus Greyling
source: Medium (Cobus Greyling)
tags: [auto-harness, falsifiable-prediction, harness-portability, control-plane]
---

# Auto Agentic Harness Engineering

**原始來源**：https://cobusgreyling.medium.com/auto-agentic-harness-engineering-b27a962fad9a  
**作者**：Cobus Greyling  
**歸檔日期**：2026-05-10

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 8/10 | Falsifiable prediction 方法論可立即採用 |
| B. 創新性 | 7/10 | Harness 優化作為假設測試，新的思維框架 |
| C. 證據品質 | 7/10 | 具體不對稱數字（33.7% vs 11.8%），但統計基礎不詳 |
| D. 技術深度 | 6/10 | 概念清楚，實作細節有限 |
| E. 泛化性 | 8/10 | 跨模型可移植 |
| **加權總分** | **7.3/10** | 8×0.3 + 7×0.2 + 7×0.2 + 6×0.15 + 8×0.15 = 7.30 |

**整合決策**：RULE — Falsifiable prediction 方法論整合進 Ratchet 決策流程  
**整合位置**：`research/agent-harness/RATCHET.md` + `.claude/refs/harness-design.md`  
**整合狀態**：待實作

---

## TL;DR

Harness（tools + middleware + memory）比 prompts 更決定 agent 效能；進化的 system prompts 在脫離配套 infrastructure 後回退。引入「falsifiable prediction」框架：每次 harness 改動前先寫預測（「我預期這會改善 X by Y%」），改動後驗證。揭示 agent 不對稱性：33.7% 準確預測修復、11.8% 準確預測回歸。展示跨模型 harness 移植。

---

## 核心主張

### 1. Harness vs Prompts 的不對稱性

> "We evolved system prompts for 6 weeks and improved accuracy by 23%. Then we stripped the harness and re-ran — accuracy dropped back to baseline. The prompt improvements were harness-dependent artifacts."

Prompt 改善是 harness 依賴的工件（artifact），不是可遷移的能力。

### 2. Falsifiable Prediction 框架

**改動前**：
```
預測：移除 step-back prompting 會讓推理任務準確率下降 15%
驗證方式：在 50 個推理任務上對比 A/B
```

**改動後**：
```
實際結果：下降 8%（預測 15%）
學習：對推理的影響比預期小；對事實召回的影響更大（未預測到）
```

### 3. Agent 不對稱性（重要數據）

| 預測類型 | 準確率 | 含義 |
|---------|------|------|
| 預測改善效果 | 33.7% | 我們通常知道「哪裡可以改善」|
| 預測回歸效果 | 11.8% | 我們幾乎不知道「哪裡會被破壞」|

**結論**：比「改善 harness」更重要的是「不要破壞 harness」。回歸是三倍難以預測的問題。

### 4. Harness 跨模型可移植性

設計良好的 harness 在 Claude Sonnet → Claude Opus → GPT-5 之間的移植損失 < 5%。  
設計不良的 harness（依賴特定模型行為）移植損失 > 40%。

**移植測試清單**：
1. 移除所有模型特定的 workaround（「Claude 有時會...」的 hack）
2. 對比在 3 個模型上的性能
3. 損失 > 10% = harness 過擬合特定模型行為

---

## 對 cc-workspace 的映射

| 概念 | cc-workspace 應用 | 現狀 |
|-----|----------------|------|
| Falsifiable prediction | 每次改動 rules/hooks 前寫預測 | ❌ 未實作 |
| 11.8% 回歸預測準確率 | 解釋為何 `/deep-review` 如此重要 | ✅ 驗證現有實踐 |
| Harness 移植測試 | 跨模型測試 (Haiku/Sonnet/Opus) | ⚠️ 偶發性，非系統化 |

**行動建議**：
- 在 `RATCHET.md` 加入 falsifiable prediction 步驟（改前寫預測）
- 建立 regression test checklist（參考 11.8% 不對稱性）
