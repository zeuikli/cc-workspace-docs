---
url: "https://www.anthropic.com/engineering/april-23-postmortem"
date: 2026-05-09
source: Anthropic Official Engineering Blog
tags: [postmortem, Claude-Code, harness-regression, prompt-change-impact, model-stability]
---

# Anthropic: April 23 Postmortem — Claude Code Quality Incident

**原始來源**：https://www.anthropic.com/engineering/april-23-postmortem  
**作者**：Anthropic Team  
**歸檔日期**：2026-05-09

---

## TL;DR

2026 年 3-4 月，Anthropic 遇到 Claude Code 品質下滑；根本原因非模型退化，而是三項 harness 變更累積：(1) reasoning effort default 改為 medium、(2) prompt caching bug 導致 thinking history 反覆清除、(3) 系統提示加入字數限制。修復後，團隊引入「per-model evaluation suite」+ 「system prompt ablation」來防止類似回歸。

---

## 核心主張

1. **Harness 變更單獨可能不可見，累積則致命**
   - 單一改動：reasoning effort medium → 可能接受的速度-品質權衡
   - 但與 cache bug + prompt 字數限制一起，品質下降 3%
   - 用戶感知：「模型變蠢了」；實際：harness 三維退化

2. **Cache Bug 的隱形殺傷**
   - 原意：清除舊 thinking sections 避免 cache 膨脹
   - 實際：每次 turn 都清除 thinking history
   - 結果：模型「失去記憶為何選擇該路徑」→ cascading reasoning 失敗

3. **System Prompt 字數限制反直覺的影響**
   - 看似無害的「keep responses under word count」
   - 實際：reduce coding quality by 3% across both Opus versions
   - 未在內部測試中被捕捉（testing on development variant vs. production）

4. **Post-Training Harness Coupling 的脆性**
   - Opus 4.6/4.7 被 trained on 「specific reasoning effort levels, specific prompt structure, specific cache behavior」
   - Harness 改變後，模型在新環境下的有效能力下滑
   - Implication：模型和 harness 已共進化到難以解耦的程度

---

## 直接意涵

### cc-workspace 可行動性

1. **「Per-Model Evaluation Suite」對 cc-workspace 必要性**
   - 當前 `.claude/refs/quality.md` 提及 `bash scripts/healthcheck.sh`，但未區分 Haiku/Sonnet/Opus 的差異
   - Anthropic 的教訓：每個模型版本的 harness 假設不同
   - 建議擴展 healthcheck：為每個模型版本維持獨立的 test case 套組

2. **System Prompt Ablation 作為變更守門人**
   - 新增規則或改動 CLAUDE.md 時，應執行「this change × each model」的 ablation
   - 即：在 Haiku + current-harness、Sonnet + current-harness、Opus + current-harness 上各測一遍
   - `.claude/rules/core.md` 現有「git commit message 必含 session URL」，可補充「system prompt 變更需 ablation」

3. **Reasoning Effort 的模型特定性**
   - Postmortem 提及「revert to xhigh for Opus 4.7, high for others」
   - cc-workspace 當前 `.claude/refs/haiku-pilot/SKILL.md` + `.claude/refs/opus-pilot/SKILL.md` 各有 reasoning effort 推薦
   - 驗證點：Sonnet 4.6 的推薦 effort level 有無明確記錄？

---

## 評分

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 9/10 | 直接示教「harness 改變如何致使模型表現下滑」；per-model ablation 可直接套用 |
| B. 創新性 | 6/10 | 根本原因分析本身非創新；但「多個 harness 改動累積效應」值得論述 |
| C. 證據品質 | 8/10 | 時間線明確、三項根本原因清晰；無量化數據（僅「3%」一筆） |
| D. 技術深度 | 7/10 | Cache bug 機制清晰；缺乏對「為何字數限制影響編碼」的深入機制分析 |
| E. 泛化性 | 8/10 | Harness 改變風險適用任何 agent 系統；Anthropic-specific 的實施細節 |
| **加權總分** | **7.8/10** | 9×0.3 + 6×0.2 + 8×0.2 + 7×0.15 + 8×0.15 = 2.7+1.2+1.6+1.05+1.2 = 7.75 |

**整合決策**：Rule（補充進 `.claude/rules/core.md` 的新段 「System Prompt Changes: Per-Model Ablation Requirement」）

---

## 引用關聯

- Anthropic harness-design-long-running-apps：harness 元件隨模型成熟過時  
- `.claude/refs/opus-pilot/SKILL.md`：Reasoning effort 配置  
- `.claude/rules/core.md`：系統提示變更流程  

