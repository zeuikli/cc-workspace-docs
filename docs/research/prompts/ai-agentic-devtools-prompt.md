---
title: Agentic 架構 + 開發工具 — 分析 Prompt
type: prompt
---

# Agentic 架構 + 開發工具 — 分析 Prompt
> 資料來源：research/ai-news/ Q1-2026 ~ 2026-05-16 | 涵蓋 17 個 newsletter | 主題 2 + 主題 7

---

## 使用方式

**適用場景：**
- 設計 Agentic 系統架構（Harness 層、記憶堆疊、多代理編排）
- 評估 Claude Code / Cursor / Codex for Work 等工具選型
- 規劃工程組織轉型（Two-Slice Team、Compound Engineering）
- 評估 Model-Harness-Fit 與遷移成本

---

## 核心洞察（Q1 2026 ~ 2026-05-16）

### Agentic 架構成熟：6 大工程瓶頸

根據 Harness Engineering 研究（TheSequence 2026-04-16、TLDR AI 2026-04-20），Agentic 系統的真正瓶頸不在模型，在 Harness 層：

| 瓶頸 | 說明 | 解決方向 |
|------|------|---------|
| 記憶管理 | Episodic vs Abstract 記憶失衡 | 優先 Episodic；無記憶 > 低質記憶 |
| 可見性 | 代理執行中間狀態難追蹤 | 結構化 checkpoint 輸出 |
| 驗證框架 | Claude 9 秒刪除 DB 事件 | 四層防禦（worktree+Docker+deny-list+auto）|
| 架構隔離 | 子代理間無隔離，失敗傳播 | parent↔child 單向通訊；child 不自重試 |
| 持久執行 | 長任務中斷無法恢復 | Cloudflare Project Think / LangChain DeepAgents |
| 工具介面選擇 | CLI vs MCP 使用場景混淆 | 短時程 CLI；長時程/跨代理 MCP |

### 工具市場競爭格局（2026-05 現況）

| 工具 | 最新動態 | 市場訊號 |
|------|---------|---------|
| Claude Code | 記憶三層架構、LSP 工具、Context 熵優化 | 週活 520 萬（Q1）；Microsoft 撤回企業授權 |
| OpenAI Codex for Work | CUA 速度 +42%、/goal 持久目標、Chrome 原生整合 | 快速追上 Claude Code |
| Cursor | 被 xAI 收購（$60B）；NRR 300%，正向毛利 | 編碼工具市場整合加速 |
| GitHub Copilot | 改為 token 計費（終止月費制）| 計費模式革命訊號 |
| Microsoft MDASH | 100+ 專門代理；CyberGym benchmark 超越 Mythos | 企業代理平台潛在勝者 |

### 組織革命：Two-Slice Team 與 Cognitive Surrender

**Two-Slice Team 模型**（Chain of Thought 2026-04-25）：
- 2 名工程師 + AI 達成傳統 8-10 人的輸出
- Compound Engineering：單人維護 5 個產品

**Cognitive Surrender 風險**（Wisely Chen AI 2026-05-12）：
- 73% 工程師使用 AI 後技術理解力下降
- 「AI 讓我寫代碼但我不再理解它」
- 防範：保留核心架構決策的人工審核

**Model-Harness-Fit 研究**（Digest 2026-05-05）：
- 後訓練已綁定特定工具生態
- 通用模型時代結束；選模型 = 選 Harness 生態
- 遷移成本被嚴重低估

### 重要安全事件（代理架構必讀）

| 事件 | 影響 | 防禦措施 |
|------|------|---------|
| Claude 代理 9 秒刪 prod DB（含備份）| 不可逆生產事故 | deny-list + Docker 沙箱 + auto 模式 |
| Claude Code npm Mini Shai-Hulud 供應鏈攻擊 | 後門植入風險 | 固定版本鎖定；SCA 掃描 |
| Mercor 洩露 4TB 語音樣本 | 代理訓練資料汙染 | 零信任工具鏈審計 |

---

## 分析 Prompt 範本

```
你是 Agentic 系統架構師。基於以下 2026 Q1-Q2 工程實踐背景：

【Harness 層 6 大瓶頸】
記憶管理（Episodic 優先）、可見性（結構化 checkpoint）、驗證框架（四層防禦）、
架構隔離（parent↔child 單向）、持久執行（MCP 長時程）、工具介面（CLI vs MCP）

【工具格局】
- Claude Code（520 萬週活）vs Codex for Work（CUA +42%，Chrome 整合）
- Cursor $60B 被 xAI 收購；GitHub Copilot 轉 token 計費
- Model-Harness-Fit：選模型 = 選生態，遷移成本被低估

【組織影響】
- Two-Slice Team：2 工程師 + AI = 8-10 人產出
- Cognitive Surrender：73% 工程師技術理解力下降
- Compound Engineering：單人維護 5 產品

請分析以下 Agentic 系統設計問題：[插入具體場景]

評估維度：
1. Harness 架構選型（記憶策略、持久化方案、工具介面）
2. 工具鏈選擇（Claude Code / Codex / Cursor 的 Fit 分析）
3. 安全防禦設計（沙箱層級、deny-list、驗證框架）
4. 組織影響評估（Two-Slice Team 適用性、Cognitive Surrender 風險）
5. 遷移成本（從現有架構切換的實際代價）

輸出格式：
- 架構圖（文字版）
- 工具選型矩陣
- 安全防禦清單（4 層）
- 組織轉型路徑（12 個月計畫）
```

---

## 追蹤指標（持續監測）

| 指標 | 當前基線 | 更新頻率 |
|------|---------|---------|
| Claude Code 週活用戶 | 520 萬（Q1）→ 持續增長中 | 月度 |
| Harness 瓶頸研究論文 | 6 大瓶頸（TheSequence 4/16）| 季度 |
| Cognitive Surrender 研究 | 73% 工程師受影響 | 半年 |
| 工具計費模式 | GitHub Copilot 已轉 token 計費 | 隨發布 |
| MCP 協定普及率 | Q1 開始成多代理編排基礎 | 月度 |

---

*最後更新：2026-05-16 | 下次建議更新：2026-06-01（05 月月報完成後）*
