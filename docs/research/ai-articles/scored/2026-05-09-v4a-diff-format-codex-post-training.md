---
url: "https://codex.danielvaughan.com/2026/03/31/codex-cli-apply-patch-v4a-diff-format/"
date: 2026-05-09
source: Codex Blog / Daniel Vaughan
tags: [tool-format, wire-format, post-training-investment, interoperability, Model-Harness-Fit]
---

# The V4A Diff Format: How Codex CLI's apply_patch Actually Edits Your Code

**原始來源**：https://codex.danielvaughan.com/2026/03/31/codex-cli-apply-patch-v4a-diff-format/  
**作者**：Daniel Vaughan（Codex Team）  
**歸檔日期**：2026-05-09

---

## TL;DR

V4A 是 Codex 的專有 diff 格式（context-anchored，以周圍代碼匹配而非絕對行號定位）。OpenAI 在 GPT-5.x 的 post-training 中投入「significant training effort」讓模型流暢生成 V4A。該格式現已成為 Codex models 的 byte-level 習慣；其他模型即使理論上可以採用 V4A，但缺乏訓練導致不可靠生成。Azure GPT-4.1 部署的失敗案例印證：移除 V4A 提示後，模型無法可靠產出。

---

## 核心主張

1. **Context-Anchored Diff 設計**
   - 解決問題：模型不可靠預測行號；全檔重寫浪費 tokens
   - V4A 方案：`@@` anchor 包含周圍代碼，harness 掃描匹配後 apply
   - Resilient to intervening edits and formatting variations

2. **Post-Training 是實現的核心**
   - GPT-5.x 專為 V4A 進行 post-training
   - 模型不是簡單「理解 V4A 語法」，而是「習慣性自動生成 V4A」
   - Prompt cookbook 明確記錄「significant training effort」

3. **格式鎖定帶來的不可移植性**
   - 理論：任何模型可採用 V4A（format-agnostic）
   - 實際：Codex models 的 V4A 生成可靠；其他廠商模型在無 post-training 下表現不佳
   - Azure GPT-4.1（非 Codex CLI 特化部署）的故事：移除 V4A prompt → model can't reliably generate it

4. **Harness 作為 Model 的隱形 Vocab**
   - 推文 @nicbstme 的「Tool Surface is Model's Vocabulary」的具體證據
   - V4A 不只是一個「工具」，而是模型 latent space 中的一個習慣固著點（attractor）

---

## 直接意涵

### cc-workspace 可行動性

1. **Claude 的 String Replacement vs GPT 的 Patch：不可混淆**
   - Claude Code 內建 `Edit` tool（search old_string → replace new_string）
   - 即使有人提出「讓 Claude 用 V4A」的想法，缺乏 post-training 會導致品質下降
   - `.claude/refs/harness-design.md` 應明確標記：「Edit tool shape is baked into Claude post-training；不應嘗試於 Claude Code 環境中強制 Codex 的 V4A 格式」

2. **Multi-Harness Portability 的硬限制**
   - 此案例是 Model-Harness-Fit 最明確的 prove-by-contradiction
   - 若要實現 multi-harness agent（如 Copilot CLI），無法「共用一套工具 schema」
   - Copilot 的解方：per-model tool inclusion（Codex 時代給 `apply_patch`，Claude 時代給 `Edit`）

3. **新工具引入的 Post-Training 成本**
   - 若 cc-workspace 想引入新工具（如 SQL query tool），假設該工具需要 post-training 才能被模型可靠利用
   - 工具可通過 prompt 介紹，但「byte-level 習慣」只能透過 post-training 來建立
   - 實務建議：新工具應先在小 POC 驗證 Opus 4.7 的自然採用度，再廣泛部署

---

## 評分

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 8/10 | 清晰論述 tool-format 的不可移植性；直接影響 multi-harness 決策 |
| B. 創新性 | 6/10 | V4A 設計本身不新（已在 Codex 中部署多年）；此文的新意在「格式鎖定」論述 |
| C. 證據品質 | 8/10 | Azure 故事作為失敗案例；OpenAI 官方「significant training effort」的文件引用 |
| D. 技術深度 | 8/10 | V4A context-anchored 機制、anchor 匹配演算法清晰；缺乏對 post-training 內部機制的深入 |
| E. 泛化性 | 7/10 | 原則（format specificity leads to overfitting）通用；V4A 本身 Codex 特化 |
| **加權總分** | **7.5/10** | 8×0.3 + 6×0.2 + 8×0.2 + 8×0.15 + 7×0.15 = 2.4+1.2+1.6+1.2+1.05 = 7.45 |

**整合決策**：Reference（納入 `.claude/refs/harness-design.md` 的「Tool Format Specificity」段落）

---

## 引用關聯

- 推文 @nicbstme 2026-05-04：Tool Surface 和 wire format 為 post-training 的 byte-level 習慣  
- `.claude/refs/harness-design.md`：Harness 架構模式  
- Cursor harness blog：per-model tool provisioning（apply_patch vs Edit）  

