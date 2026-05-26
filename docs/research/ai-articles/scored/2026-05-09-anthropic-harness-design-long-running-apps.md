---
url: "https://www.anthropic.com/engineering/harness-design-long-running-apps"
date: 2026-05-09
source: Anthropic Official Engineering Blog
authors: Anthropic Team
tags: [harness-design, agent-architecture, evaluator-agent, Model-Harness-Fit]
---

# Anthropic: Harness Design for Long-Running Application Development

**原始來源**：https://www.anthropic.com/engineering/harness-design-long-running-apps  
**作者**：Anthropic Team  
**歸檔日期**：2026-05-09

---

## TL;DR

Anthropic 官方展示三代理 harness（planner、generator、evaluator）設計，實現單一 Agent 難以達成的長時間自主開發任務。核心洞見：harness 各元件編碼「模型無法自行完成的假設」；當模型能力進化時，該假設需重新審視。

---

## 核心主張

1. **Agent + Harness 的共進化**（Co-evolution）
   - 每個 harness 元件編碼一項假設：「模型在這個能力上不足」
   - 當模型能力提升時，舊假設變成死重，應移除
   - 新模型解鎖新能力時，需要新的 harness scaffolding 才能達到天花板

2. **Playwright MCP 工具端設計**
   - Evaluator agent 直接與執行中的應用互動（screenshotting、navigation）
   - 工具表面形狀決定了模型能直觀執行的任務類型
   - 與推文 @nicbstme 「Tool Surface is Model's Vocabulary」呼應

3. **多代理分工的性能躍升**
   - Solo Agent 結果：20 分鐘、$9、核心功能破損
   - 三代理 Harness 結果：6 小時、$200、完整可玩遊戲 + 16 項功能規格
   - 品質大幅提升的代價是 context 和 token 消耗增加

---

## 直接意涵

### cc-workspace 可行動性

1. **CLAUDE.md 的 `<system-reminder>` 注入是 harness 過擬合的證據**  
   - 該機制明確編碼「Claude 會讀 system-reminder tag 並改變行為」  
   - 其他模型如未 post-train 認識此 tag，會無視它  
   - 跨模型移植 CLAUDE.md 時需警覺此耦合

2. **「harness 元件會隨模型成熟過時」適用於 subagent-strategy.md**  
   - 當前規則中 Haiku 4.5 的「context reset machinery」可能變成 dead weight（推文參考 Opus 4.6 已移除此機制）  
   - 年度 audit 必須檢查：這項 harness 元件還在補哪個模型的缺口？  
   - 與 research/agent-harness/eval-2026-05-08.md 的「harness obsolescence tracking」相連

3. **Multi-Agent 與 PGE 原則強化**  
   - `.claude/rules/subagent-strategy.md` 的 Planner-Generator-Evaluator 拓撲直接呼應此文，不是巧合  
   - Anthropic 本身採用三代理設計，驗證了 Opus 4.6/4.7 需要此分工才能達到長任務自主度

---

## 評分

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 8/10 | 明確論述 harness 過時機制、工具設計形狀的約束，直接支持 cc-workspace「harness audit」決策 |
| B. 創新性 | 7/10 | Co-evolution feedback loop 概念在推文 @nicbstme 已提出；此文貢獻是 Anthropic 官方確認 + 三代理具體實施 |
| C. 證據品質 | 8/10 | 具體數據：solo(20min/$9) vs harness(6hr/$200)；實際產品案例（retro game）；但未進行 ablation 對比 |
| D. 技術深度 | 7/10 | 架構清晰、Playwright MCP 工具細節充分；未深入 evaluation loop 內部設計 |
| E. 泛化性 | 8/10 | Agent harness 通用原則；但示例專注長時間開發任務，對短任務場景應用性未明確 |
| **加權總分** | **7.6/10** | 8×0.3 + 7×0.2 + 8×0.2 + 7×0.15 + 8×0.15 = 2.4+1.4+1.6+1.05+1.2 = 7.65 |

**整合決策**：Rule（補充進 `.claude/refs/harness-design.md` 的「harness obsolescence」段落）

---

## 引用關聯

- 推文 @nicbstme 2026-05-04：「Tool Surface is Model's Vocabulary」  
- `.claude/rules/subagent-strategy.md`：Planner-Generator-Evaluator 拓撲選擇  
- `research/agent-harness/eval-2026-05-08.md`：Harness health audit framework  
- `.claude/refs/model-selection-grid.md`：模型進化時 harness 需重新評估  

