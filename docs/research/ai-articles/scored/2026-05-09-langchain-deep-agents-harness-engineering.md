---
url: "https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering"
date: 2026-05-09
source: LangChain Official Blog
authors: LangChain Team
tags: [harness-engineering, reasoning-sandwich, middleware-hooks, Terminal-Bench, +13.7-points]
---

# LangChain: Improving Deep Agents with Harness Engineering

**原始來源**：https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering  
**作者**：LangChain Team  
**歸檔日期**：2026-05-09

---

## TL;DR

LangChain 在 Terminal-Bench 2.0 上達成 **13.7 百分點的改進**（52.8% → 66.5%）仅通過改變 harness，模型保持不變（GPT-5.2-Codex）。核心技術：「reasoning sandwich」（plan with xhigh、implement with high、verify with xhigh）、middleware hooks（LocalContextMiddleware、PreCompletionChecklistMiddleware、LoopDetectionMiddleware）。

---

## 核心主張

1. **Harness = System Prompts + Tools + Middleware**
   - 三個可獨立操作的 harness 層
   - 發現：Harness 對 benchmark 分數的影響力 = 或 > 模型升級

2. **Reasoning Sandwich：非線性 Reasoning 配置**
   - Naive xhigh everywhere = 53.9%（超時）
   - High only = 63.6%  
   - xhigh (plan) + high (implement) + xhigh (verify) = 66.5%
   - Insight：不同任務階段的 reasoning 需求不對稱

3. **Middleware 攔截點的力量**
   - `LocalContextMiddleware`：預先掃描 dir 結構、available tools、Python 版本 → inject
   - `PreCompletionChecklistMiddleware`：強制驗證通過後才退出
   - `LoopDetectionMiddleware`：追蹤重複編輯以避免「doom loop」
   - 這些都是「模型無法獨立完成」的假設編碼

4. **Trace-Driven 迭代而非猜測**
   - 分析失敗的 trace 找出真實瓶頸
   - 而非「覺得應該改這個」的投機優化
   - 每輪改動量化結果

---

## 直接意涵

### cc-workspace 可行動性

1. **Reasoning Sandwich 套用到 Opus Pilot Mode**
   - 當前 `.claude/refs/opus-pilot/SKILL.md` 使用「xhigh」作單純選項
   - LangChain 的發現表示：應該探索「plan 階段用 xhigh、refactor/implement 階段用 high」的混合策略
   - 適合補充進 `.claude/skills/opus-pilot/prompt.md` 作為推薦配置

2. **Middleware Hooks 架構在 cc-workspace 中的應用**
   - 推文 @nicbstme 提及 Codex 的 `Phase 2 consolidation prompt`、Claude Code 的 `<system-reminder>` 都是 middleware 的例子
   - cc-workspace 當前有 `PreCompletionChecklistMiddleware` 的等效物嗎？（TodoWrite + verification step）
   - `.claude/rules/core.md` 提到「驗證指令」（healthcheck），可視為 pre-exit middleware

3. **上下文準備的 ROI**
   - LocalContextMiddleware 減少模型理解工作環境的成本
   - cc-workspace 的 `~/.claude/projects/<cwd>/memory/` 是類似機制（預載入歷史脈絡）
   - Insight：harness 應主動「塞進」模型需要的環境信號，而非期待模型自行發現

---

## 評分

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 9/10 | Reasoning sandwich 可直接套用；middleware pattern 符合 cc-workspace hook 設計；量化數據強 |
| B. 創新性 | 7/10 | 推理預算分配不新奇，但「per-phase reasoning effort」系統化程度高 |
| C. 證據品質 | 9/10 | Terminal-Bench 排行驗證（Top 30→Top 5）；逐步改進的數據清晰（52.8→66.5） |
| D. 技術深度 | 8/10 | Middleware 架構清晰；缺乏 ablation study（各元件獨立貢獻多少） |
| E. 泛化性 | 8/10 | Reasoning sandwich 適用任何 reasoning-capable 模型；middleware pattern 跨 agent 框架通用 |
| **加權總分** | **8.2/10** | 9×0.3 + 7×0.2 + 9×0.2 + 8×0.15 + 8×0.15 = 2.7+1.4+1.8+1.2+1.2 = 8.3 |

**整合決策**：Skill（補充進 `.claude/skills/opus-pilot/prompt.md` 或新增 `.claude/skills/reasoning-sandwich/prompt.md`）

---

## 引用關聯

- 推文 @nicbstme 2026-05-04：「LangChain Opus 4.6 在不同 harness 分數差異」引用  
- `.claude/skills/opus-pilot/SKILL.md`：推理預算配置  
- `.claude/rules/core.md`：驗證指令與 pre-exit middleware  
- Terminal-Bench 2.0：排行驗證基準  

