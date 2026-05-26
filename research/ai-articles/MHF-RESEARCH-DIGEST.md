# Model-Harness-Fit (MHF) Research Digest

**編製日期**：2026-05-09  
**來源數**：7 篇學術+業界  
**平均評分**：7.91/10  
**範圍**：Anthropic、Cursor、OpenAI/Codex、LangChain、Terminal-Bench、Arbiter cross-vendor analysis

---

## 概述

Model-Harness-Fit (MHF) 是 2026 年 agent 設計中最被低估的約束。核心論點：模型在 post-training 中已對特定 harness（系統提示結構、工具 schema、記憶儀式、引用規約）達成 byte-level 過擬合。跨 harness 移植模型 = 隱性效能崩塌，即使 logits 相同。

---

## 收集的來源（按評分排序）

| # | 標題 | 來源 | 評分 | 關鍵發現 |
|---|------|------|------|---------|
| 1 | LangChain: Deep Agents Harness Engineering | LangChain Blog | **8.2** | 13.7pt (+52.8→66.5%) on TB2.0 via reasoning sandwich + middleware；無模型改變 |
| 2 | Cursor: Continually Improving Agent Harness | Cursor Blog | **8.0** | Model-specific tool provisioning（patch vs string replace）；Keep Rate A/B 量化 |
| 3 | Anthropic: April-23 Postmortem (Claude Code) | Anthropic Eng Blog | **7.8** | Harness 變更累積致 3% 品質下滑；per-model eval suite 必須 |
| 4 | Anthropic: Harness Design Long-Running Apps | Anthropic Eng Blog | **7.65** | Co-evolution feedback loop；harness 元件隨模型成熟過時 |
| 5 | Arbiter: System Prompt Interference Analysis | arXiv 2603.08993 | **8.0** | 三種 harness 架構（monolithic/flat/modular）導致不同失敗模態；$0.27 cross-vendor audit |
| 6 | Terminal-Bench 2.0 | arXiv 2601.11868 | **7.6** | Harness impact ≥ model upgrade；ForgeCode (3rd-party) 在 top-6 佔 3 席 |
| 7 | V4A Diff Format (Codex) | Codex Blog | **7.5** | Tool format as post-training habit；Azure GPT-4.1 缺 V4A training → unreliable |

---

## 跨來源主題匯流

### 1. **Harness Impact 量化証證**

**獨立來源匯流**：LangChain、Cursor、Terminal-Bench、Anthropic postmortem

- **LangChain**：無模型改變，harness 改動 +13.7pt
- **Cursor**：Top 30 → Top 5（25 名躍升）via harness-only
- **Terminal-Bench 2.0**：同 Opus 4.6，ForgeCode 79.8% vs Capy 75.3%（4.5pt 差異）
- **Anthropic**：System prompt 改動 -3%（無模型版本改變）

**結論**：Harness 對分數的邊際貢獻 ≈ 或 > 模型世代升級。

### 2. **Tool Surface 為 Post-Training 的 Byte-Level 習慣**

**獨立來源**：Cursor、V4A format blog、推文 @nicbstme

- **Cursor**：OpenAI models trained on V4A patch → 給 `apply_patch` 工具；Claude trained on string-replace → 給 `Edit`
- **V4A 深度分析**：OpenAI 在 GPT-5.x 進行「significant training effort」專為 V4A。Azure GPT-4.1（未特化）移除 V4A prompt 後 → 無法可靠生成
- **Codex blog 結論**：「Format is part of the model's effective parameters」

**結論**：跨模型移植工具設計會增加 reasoning tokens 並提升錯誤率。

### 3. **System Prompt 架構決定失敗模式類型**

**來源**：Arbiter 論文、Anthropic postmortem

- **Arbiter**：Monolithic（Claude Code）vs Flat（Codex）vs Modular（Gemini）各有特異的矛盾類型
  - Monolithic：subsystem 矛盾累積（4 critical contradictions in Claude Code）
  - Modular：composition seams 設計漏洞（Gemini history compression data loss）
- **Anthropic postmortem**：System prompt 字數限制 → -3% 品質（看似無害實則傷害編碼能力）

**結論**：架構選擇 → 失敗模態分佈 → 模型被訓練去平衡該架構的內在矛盾。

### 4. **Harness 元件隨模型進化過時**

**來源**：Anthropic harness design + postmortem

- **設計原則**：「Every component encodes an assumption about what the model can't do on its own」
- **Opus 4.6 vs 4.5**：Context reset machinery 在 4.5 load-bearing，在 4.6 變成 dead weight
- **Postmortem**：Reasoning effort default 從 high → medium 的嘗試，在 Opus 4.7 需要回復為 xhigh
- **發現**：模型能力進化使舊假設失效；harness 年度審計必須檢查哪些元件仍需要

**結論**：Harness 不是「建一次就永遠用」，而是「追蹤模型進化重新評估」。

### 5. **多代理分工（PGE）的性能躍升**

**來源**：Anthropic 三代理設計、LangChain middleware hooks

- **Anthropic 實例**：Planner-Generator-Evaluator 在長時間任務實現「完全破損 → 完整可玩」的躍升
- **LangChain 實例**：Middleware（LocalContext、PreCompletionChecklist、LoopDetection）各自檢測不同失敗模式

**結論**：PGE 拓撲不是「nice-to-have」而是「必要」去達到前沿自主度。

### 6. **Reasoning Budget 分配的非線性效應**

**來源**：LangChain「reasoning sandwich」

- **Naive xhigh everywhere**：53.9%（超時）
- **High only**：63.6%
- **xhigh (plan) + high (implement) + xhigh (verify)**：66.5%

**發現**：不同任務階段的 reasoning 需求不對稱；靜態配置次優。

**結論**：動態 reasoning budget allocation 相較「maxout all」更有效且低成本。

### 7. **跨廠商互補分析的新發現**

**來源**：Arbiter 論文

- 10 個模型對 116 項發現生成 107 個獨特分類
- Kimi K2.5 的「經濟/資源視角」在 Claude Opus 的分析中完全缺席
- **成本**：$0.27 USD + 三小時評審
- **驗證**：Gemini history loss 獨立被 Google 確認為真實 bug

**結論**：多模型審查並非浪費，而是發現型號特定盲點的必要。

---

## 對立觀點（若存在）

### **反方 I：自然語言 Agent Harnesses (NLAH) 聲稱可實現跨模型可移植**

**主張**：透過外部化 harness 為自然語言制品（而非 code），可在不同執行環境間轉移。

**證據品質分析**：
- **實驗限制**：所有評估 exclusively on GPT-5.4（未測多模型）
- **Porting 效果**：47.2% (NLAH) vs 30.4% (native)，但這反映「行為重配置」而非「模式無關性」
- **機制局限**：自然語言無法捕捉「隱藏的服務端狀態、專有調度器、訓練導出行為」

**評估**：反方論文強度較弱，未驗證跨模型的真實可移植性，僅展示單一模型內的口述 harness。

### **反方 II：Model Context Protocol (MCP) 作為統一層**

**主張**：MCP 使任何宿主能連接任何 MCP 伺服器，regardless of 底層模型。

**現狀**：
- Google 2026 推出 managed MCP endpoints（IAM、audit logging）
- LangChain 引入「harness profiles」per-model

**評估**：MCP 解決了「工具發現」層，但不解決「tool schema shape」層的過擬合。Cursor 的實踐表明：即使透過 MCP，仍需 per-model tool inclusion（Codex 給 apply_patch、Claude 給 Edit）。

**結論**：MCP 是必要非充分條件；harness 仍需 model-specific 調整。

---

## CC-Workspace 直接行動建議

### A. **優先級高（立即可行）**

1. **Per-Model Evaluation Suite**  
   路徑：`.claude/refs/quality.md` § Benchmark Evaluation  
   行動：為 Haiku 4.5 / Sonnet 4.6 / Opus 4.7 維持獨立的 test case 套組  
   來源：Anthropic postmortem（per-model suite 防止回歸）

2. **System Prompt Ablation Gate**  
   路徑：`.claude/rules/core.md` § System Prompt Changes  
   行動：CLAUDE.md 或 `.claude/rules/` 改動時，執行「change × each model」ablation  
   來源：Anthropic postmortem（字數限制無意中 -3%）+ Arbiter（架構矛盾檢測）

3. **Harness Obsolescence Audit Framework**  
   路徑：`.claude/refs/harness-design.md` § Component Lifecycle  
   行動：年度檢查「這項 harness 元件還在補哪個模型的缺口？還是 dead weight？」  
   來源：Anthropic 設計原則（context reset machinery 在 Opus 4.6 過時）

### B. **優先級中（設計階段）**

4. **Reasoning Sandwich 在 Opus Pilot Mode 中的應用**  
   路徑：`.claude/skills/opus-pilot/prompt.md`  
   建議：「plan: xhigh, implement: high, verify: xhigh」作推薦配置  
   來源：LangChain +13.7pt 驗證

5. **Tool Reliability 監測指標**  
   路徑：`.claude/refs/` 新檔 `tool-reliability.md`  
   建議：Read/Write/Edit/Bash/Monitor 的 error-rate 基準（Cursor 達成 2-3 9s）  
   來源：Cursor A/B test 文化

6. **Model-Specific Tool Provisioning 文件化**  
   路徑：`.claude/refs/model-selection-grid.md` § Tool Surface  
   確認：Haiku/Sonnet/Opus 各自的工具優選（Claude 系列都是 string-replace，所以目前無差異；但如未來支援 Codex，需此層）  
   來源：Cursor + V4A format 分析

### C. **優先級低（長期 Roadmap）**

7. **A/B Testing Infrastructure for Harness Changes**  
   前提：需要 session-level keep-rate 或代碼保留率統計  
   來源：Cursor 的線上評估法

8. **跨 Harness 相容性警告系統**  
   前提：若未來支援其他 harness（Cursor、Codex）  
   動作：動態檢測 tool schema mismatch 並警告可能的降級  
   來源：V4A format + Arbiter 架構分析

---

## 研究發現的可信度評估

| 維度 | 評價 |
|------|------|
| **證據強度** | **高**。Terminal-Bench 2.0、Cursor、LangChain、Anthropic 四個獨立來源量化相同現象 |
| **機制理解** | **高**。Codex V4A、Anthropic system-reminder、Claude Code memory 的具體實施細節已公開 |
| **反方論述** | **弱**。NLAH 論文未驗證跨模型；MCP 解決工具發現但未解決 schema overfitting |
| **可重現性** | **高**。Terminal-Bench 開源、Codex 開源碼、公開數據足以複現 |
| **適用範圍** | **廣**。發現適用任何 multi-model agent 平台；不限 Claude Code 用戶 |

---

## 總結

Model-Harness-Fit 是 2026 年 agent 設計的隱藏杠桿。與其追求跨 harness 通用性，不如承認「each model + harness = different product」並據此優化。

cc-workspace 已內化此觀點（CLAUDE.md、Skills、subagent-strategy 都對齐 Claude Code 特定設計），現階段重點應轉向：
1. **驗證當前 harness 對 Opus 4.7 仍最優**
2. **建立 per-model evaluation 防止回歸**  
3. **審計哪些元件已過時需清除**

跨 harness 支援（如 Cursor、Codex）應視為「不同產品」而非「參數調整」，成本遠高於單一 harness 最優化。

---

## 引用索引

**關鍵推文**：@nicbstme 2026-05-04（Model-Harness-Fit 命名與綜合論述）

**相關 cc-workspace 檔案**：
- `.claude/rules/core.md` § 實作前假設  
- `.claude/rules/subagent-strategy.md` § PGE 拓撲  
- `.claude/refs/harness-design.md` § 反模式  
- `.claude/refs/model-selection-grid.md` § 模型選擇  
- `.claude/skills/opus-pilot/SKILL.md` § 推理配置  

---

**Last updated**: 2026-05-09  
**Next review suggested**: 2026-11-09（harness evolution 年度檢查）

