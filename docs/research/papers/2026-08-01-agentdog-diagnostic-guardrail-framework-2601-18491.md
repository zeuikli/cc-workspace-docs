---
url: "https://arxiv.org/abs/2601.18491"
title: "AgentDoG: A Diagnostic Guardrail Framework for AI Agent Safety and Security"
arxiv_id: 2601.18491
collected_at: 2026-08-01
collected_by: routine-d
domain: Safety / Alignment
pdf_path: pdfs/2601.18491.pdf
year: 2026
---

# AgentDoG: A Diagnostic Guardrail Framework for AI Agent Safety and Security

## 摘要 / 核心貢獻

本文處理自主 AI agent 因工具使用與環境互動而產生的安全與安控挑戰。現有安全系統在風險診斷上缺乏透明度——多半只給出二元風險標籤而無法解釋成因。作者提出一套三維分類法，正交地依「來源（where）」、「失效模式（how）」、「後果（what）」對 agentic 風險分類。

研究貢獻分三部分：① **框架與分類法**——結構化分類系統；② **安全 benchmark ATBench**——涵蓋多樣情境的細粒度 agent 安全評測基準；③ **AgentDoG 系統**——核心貢獻是一套診斷式 guardrail，能對 agent 軌跡進行細粒度、具情境感知的監控，並提供超越簡單風險標籤的解釋，診斷不安全/不合理行動的根本原因，支援 agent 對齊。

關鍵結果：提供 4B/7B/8B 三種模型規模（基於 Qwen 與 Llama 架構）；在 agent 安全審核上達到 SOTA 效能；透過診斷式推理（而非二元分類）提供透明度；模型與資料集皆已開源。

## 與 Harness 的關聯

> 2026-08-02 深讀 PDF 原檔（40 頁）後重寫，對齊 v5.1。

三維正交分類法——**來源（where）／失效模式（how）／後果（what）**——可作為 core.md P0 安全二分（授權內即修 vs 授權外 blocking report）的診斷補充框架。

**v5.1 狀態更新**：本段原文指出「`security-reviewer` 與 `security-auditor` 兩個 agent 僅以觸發詞區分、缺乏結構化根因分類」。該落差的前半段已由 v5.1 消解——兩者已合併為單一 `security-reviewer`（prompt 註明「深掃」即升級為 OWASP Top 10 + STRIDE 模式）。**後半段仍然成立**：合併後的 agent 依舊以觸發詞與關鍵字路由，沒有結構化根因分類；AgentDoG 的三維法正好補這一格，且與現行 STRIDE 維度正交（STRIDE 分的是威脅類型，三維法分的是來源／機制／後果）。

**⚠️ 本篇最該注意的數字，是它自己的低分**：AgentDoG 在二元安全分類上達 SOTA（ATBench 92.80 / R-Judge 91.84），但在**細粒度**分類上全體模型都很低——failure-mode 維度最佳僅約 32.4%，risk-source 約 82%，real-world-harm 約 59%。也就是說「判斷有沒有風險」已相當可靠，「判斷風險為何發生」仍接近不可用。這對 workspace 的直接意涵是：**可以考慮引入其二元判定作為 advisory 訊號，但不可拿其根因標籤當作 oracle**——core.md §TEST「Oracle 先驗」要求採信前先驗鑑別力，本文自身的數據就已判定該用途不合格。

ATBench 作為 gate 選擇稽核（`core.md §PROPOSE 委派`「產出者不驗收自己的產出」，原 `graph.md §G2`「gate 不配模型」）的 oracle 資格驗證基準，僅在二元層級可用。

⚠️ 模型規模 4B/7B/8B，屬本地可跑量級；但引入即新增一個 LLM 判斷層，與 core.md「不可逆不變式落在 hook 或程式層」的原則相衝——只宜作 advisory，不得作阻斷閘。
