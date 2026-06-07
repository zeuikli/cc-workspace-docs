---
url: "https://arxiv.org/html/2603.08993v1"
date: 2026-05-09
source: Arbiter Research Paper / arXiv
tags: [system-prompt-analysis, cross-vendor, failure-modes, architectural-patterns, Model-Harness-Fit]
---

# Arbiter: Detecting Interference in LLM Agent System Prompts — Cross-Vendor Analysis

**原始來源**：https://arxiv.org/html/2603.08993v1  
**歸檔日期**：2026-05-09

---

## TL;DR

Arbiter 論文分析三大 agent harness（Claude Code、Codex CLI、Gemini CLI）的系統提示，發現各自特異的結構矛盾。例：Claude Code 的 TodoWrite mandate 與 workflow 禁止直接衝突（4 個 critical 矛盾）。論文產生跨廠商的 107 個獨特發現類別，成本僅 $0.27 USD，驗證了 harness 文本不同的架構選擇導致不同的失敗模態。

---

## 核心主張

1. **Harness 架構決定失敗模式類型**
   - **Monolithic**（Claude Code, 1,490 行）：增長型漏洞（subsystem 矛盾累積）
   - **Flat**（Codex CLI, 298 行）：簡潔但能力受限
   - **Modular**（Gemini CLI, 245 行）：composition seams 的設計級漏洞
   - 同一缺陷不會在三種架構上同時出現 → 架構本身決定脆弱模式

2. **跨模型互補性而非冗餘**
   - 十個模型針對 116 個發現生成 107 個獨特分類
   - Kimi K2.5 的「經濟/資源視角」在 Claude Opus 的分析中完全缺席
   - Implication：多模型審查不是浪費，而是發現型號特定的盲點

3. **文本層級的不可見性**
   - Claude Code 的 TodoWrite mandate 隱含在文本中，不可從 frontmatter 自動驗證
   - Codex 的 memory mutation 規則分散在 Phase 2 prompt 的 841 行深處
   - 人類 code review 無法發現這類結構矛盾

4. **System Prompt 作為 Wire Format 的一部分**
   - 「System prompt 矛盾」並非 bug 而是 harness 架構選擇的必然產物
   - 模型被 trained on 這個矛盾的 prompt，對此有適應（或損傷）
   - 跨 harness 移植 prompt 時會拉出新的矛盾

---

## 直接意涵

### cc-workspace 可行動性

1. **CLAUDE.md 的「自動載入」規則衝突檢測**
   - cc-workspace CLAUDE.md 已達 ~150 行（monolithic 傾向）
   - 建議建立「rule conflict audit」工具：scan `.claude/rules/` for implicit contradictions
   - 例：「避免 git add -A」vs「git commit 強制 pre-commit-review hook」—有沒有場景兩者衝突？

2. **Post-Training Harness Compatibility Matrix**
   - 此論文強調：Harness 文本結構在 model post-training 中被編碼
   - Claude 模型被 trained on 「CLAUDE.md monolithic format with specific rule sequences」
   - 移植至 Codex 時，Codex 被 trained on different rule ordering → behavioral shift
   - 推薦補充進 `.claude/refs/harness-design.md` 的新段：「Harness Text Structure Specifies Model Training Distribution」

3. **Gemini「History Compression Data Loss」的教訓**
   - 論文發現：Gemini CLI modular harness 設計在 context 壓縮時誤刪用戶偏好
   - cc-workspace 的 `/compact` 命令是否有類似風險？
   - 建議在 `.claude/rules/context-management.md` 添加「compact safety checklist」

---

## 評分

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 8/10 | 發現 harness 架構與失敗模式的對應；適合作為 audit framework 藍本 |
| B. 創新性 | 8/10 | Cross-vendor system prompt 分析前所未有；107 unique finding 分類新穎 |
| C. 證據品質 | 8/10 | 量化（$0.27 成本、10 模型）+ 獨立確認（Google's Gemini bug report）；但樣本量相對小 |
| D. 技術深度 | 9/10 | 深入每個 harness 的文本結構、rule ordering、架構選擇；分析精細 |
| E. 泛化性 | 7/10 | 原則（architecture→failure modes）通用；但具體發現 Claude/Codex/Gemini 特化 |
| **加權總分** | **7.9/10** | 8×0.3 + 8×0.2 + 8×0.2 + 9×0.15 + 7×0.15 = 2.4+1.6+1.6+1.35+1.05 = 8.0 |

**整合決策**：Rule + Reference（補充進 `.claude/rules/` 的新檔 `harness-audit.md`；同步更新 `.claude/refs/harness-design.md`）

---

## 引用關聯

- 推文 @nicbstme 2026-05-04：System prompt skeleton 與 identity file convention  
- `.claude/rules/core.md`：Current harness rule structure  
- `.claude/refs/harness-design.md`：Architecture patterns  

