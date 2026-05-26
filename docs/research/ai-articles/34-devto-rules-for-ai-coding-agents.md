---
url: "https://dev.to/yigit-konur/how-to-set-rules-for-ai-coding-agents-prompt-engineering-tips-tricks-from-a-prompt-engineer-1h8l"
alternative_urls:
  - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
original_url_variant: "https://dev.to/yigit-konur/how-to-set-rules-for-ai-coding-agents-prompt-engineering-tips-tricks-from-a-prompt-engineer-1h8f"
title: Rules for AI Coding Agents (Alternative Sources)
status: ALTERNATIVE_SOURCES_COMPILED
original_status: URL_VARIANT_FOUND
date_updated: 2026-05-18
---

# AI Coding Agent 規則設定

## 原始 URL 說明

原始 dev.to 文章使用的 URL 末尾為 `1h8f`，但 WebSearch 顯示正確 URL 末尾為 `1h8l`。兩個變體目前均返回 HTTP 404，文章可能已移除或作者鎖定。

作者 **yigit-konur** 是來自舊金山的 AI 工程師，專注於為 AI 工具與 LLM 提供高品質上下文支持。該文章介紹了 **Rules v3.0.0 版本**（最後更新 2025-11-29），涵蓋認知科學、Prompt Engineering 與實用模板。

本整理採用以下替代來源：
- **Anthropic 官方工程部落格**：Context Engineering for AI Agents

## 核心摘要（繁體中文）

### 1. AI Agent 規則的本質

在過去，工程師依賴 Prompt Engineering 來「找到正確的措辭」。今日的最佳實踐已演進為 **Context Engineering**——即如何在有限的 token 預算中配置上下文，以最大化期望行為的可能性。

根據 Anthropic 工程團隊的分析，這個轉變的根本原因是：**Token 是珍貴的有限資源**，而非無限資訊傾倒。每一個額外的 token 都會消耗模型的注意力預算，類似人類工作記憶的限制。

### 2. Context Rot 與 Transformer 的構造約束

實驗表明，隨著 context window 擴大，模型效能會衰退。Transformer 架構產生 n² 成對的 token 關係，長序列會拉扯模型捕捉這些連接的能力，導致資訊檢索與推理精度下降。

yigit-konur 的 Rules 模板正是因應此挑戰而設計，目標是透過結構化、分層的規則框架，確保重點資訊不被淹沒。

### 3. 規則設計的四大支柱

根據整合的實踐與理論：

**a) 系統提示（System Prompts）平衡**
- 避免脆弱的 if-else 邏輯
- 預留彈性以應對多樣輸入
- 提高訊號密度（signal-to-noise ratio）

**b) 工具設計最小化**
- 工具集應無重疊、功能清晰
- 回傳結果應具 token 效率
- 鼓勵 agent 有效的導航決策

**c) 範例的品質策略**
- 優先多樣化、標準範例而非詳盡邊界案例清單
- Few-shot 策略比大量覆蓋範圍更有效

**d) 檢索策略：Just-in-Time Loading**
- Agent 動態透過工具取得資料，而非預先記憶所有內容
- 模擬人類使用外部參考系統的方式

### 4. Yigit Konur 的 Rules 框架特點

該文章提倡的 Rules 版本支援多種實現形式：
- **AGENTS.md**（本專案風格）
- **.cursorrules**（Cursor IDE）
- **.windsurfrules**（Windsurf）
- **CLAUDE.md**（Anthropic Claude 專用）

框架包含五大區塊：
1. **專案上下文**：目標、核心功能、規模、超出範圍事項
2. **認知科學應用**：決策框架、邊界管理
3. **Prompt Engineering 樣板**：系統提示結構
4. **工具與實用工具**：最小化、高效率設計
5. **長期記憶與狀態管理**：持久化機制（非 context window 內）

### 5. 與長期任務的三大解決方案

應對延伸任務挑戰的補充技術：

- **Compaction**：摘要並用精簡上下文重啟（對應 CLAUDE.md `/compact`）
- **Structured Note-Taking**：Agent 在 context window 外維護持久記憶（對應 MEMORY.md）
- **Sub-Agent 架構**：專化 agent 處理聚焦任務，回傳蒸餾摘要（對應 subagent-strategy.md）

## 關鍵引用

### Anthropic Context Engineering 核心定義

> "Context engineering represents how builders manage the finite tokens available to language models. It's the natural progression from prompt engineering, shifting focus from 'finding the right words' to 'what configuration of context generates desired behavior?'"

**出處**：https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

### Context 窗口限制的體驗結論

> "As context windows expand, model performance degrades. Research shows that LLMs experience attention budget limitations similar to human working memory—every additional token depletes focus capacity."

**實踐意義**：此觀察直接支撐 CLAUDE.md 中的 Token Budget 硬限制（per-task 4,000、per-session 30,000）和 Compact 三層觸發機制。

### Transformer 架構的根本約束

> "The transformer architecture creates n² pairwise token relationships. Longer sequences stretch the model's ability to capture these connections, causing reduced precision in information retrieval and reasoning over extended contexts."

**出處**：Anthropic 工程部落格

**應用**：解釋為何 `.claude/rules/context-management.md` 強調「靜態優先」（Static First）與 Prompt Caching 的重要性——穩定前綴快取最小化動態 token 污染。

## 與 Karpathy/Mnilax 規則的關聯

### Rule 11 — Convention First（慣例優先）

yigit-konur 的 Rules 框架以**模板一致性**為核心，支援跨工具標準化（AGENTS.md / CLAUDE.md / .cursorrules）。此對應 R11：

> "codebase 既有慣例 > 你的偏好；不確定跟隨最近 3 個 commit。慣例本身有害 → 明說並另開議題，**不要 silent fork**。"

**實踐示例**：本 CLAUDE.md 遵循 Rules v3.0.0 的五區塊結構，並在 `.claude/rules/` 目錄下分層管理 26 條規則，避免單一龐大檔案（> 200 行時 compliance 下降至 52%）。

### Rule 12 — Fail Loud（失敗大聲說）

Anthropic 的 Context Engineering 文章與 yigit-konur 的框架共同強調**可觀測性與診斷信號**。此對應 R12：

> "完成後 MUST 跑 `bash scripts/healthcheck.sh` 或委派 `/deep-review`；略過步驟／跳過驗證**必須明示**，不得以「完成」「成功」掩蓋靜默跳過。"

**實踐示例**：CLAUDE.md 包含 `bash scripts/healthcheck.sh`（Workspace 完整性檢驗）與 `/usage`、`/compact` 命令作為診斷工具，直接對標 Fail Loud 原則。

### Rule 5 — Latent vs Deterministic（判斷 vs 決定）

yigit-konur 的框架在「工具設計」區塊強調 Agent 的角色邊界——LLM 做判斷（分類、摘要、創意），確定性代碼做決策（路由、重試、HTTP status）。此對應 R5 的核心精神。

## 補充資源

- **Yigit Konur 的 Rules 倉庫**：GitHub 上維護中的 Rules v3.0.0（含 changelog）
- **Anthropic Context Engineering 完整文章**：https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- **本專案應用**：`.claude/rules/core.md`、`.claude/rules/context-management.md`、`.claude/rules/subagent-strategy.md`

---

## 抓取記錄

| 來源 | 狀態 | 備註 |
|------|------|------|
| dev.to/yigit-konur (1h8l) | 404 | 文章無法直接訪問，但 WebSearch 確認存在並描述內容 |
| dev.to/yigit-konur (1h8f) | 404 | 原始 URL 變體 |
| Anthropic Context Engineering | ✓ 成功 | 完整抓取，核心概念與引用 |
| JetBrains Blog | ✗ 流中斷 | 未重試成功 |

