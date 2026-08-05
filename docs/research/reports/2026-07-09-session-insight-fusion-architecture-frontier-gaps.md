---
title: "Session Insight Report — Fusion 架構設計 + 前沿缺口研究 + 論文收錄"
date: 2026-07-09
collaborators: [GLM-5.2, Kimi-K2.7]
files_produced: 9
session_scope: Fusion 架構設計（Claude Code × Factory Droid × Devin Sidekick）+ 前沿模型缺口 + 邊緣推論/基礎設施缺口 + 論文收錄 + Token 節省策略
type: session-insight-report
---

# Session Insight Report 2026-07-09

> 本 Session 從 git pull 更新開始,歷經完整閱讀 workspace 全部研究產出（DAILY-TOPICS 22 檔 + DAILY-RESEARCH 23 檔 + NEW-DOMAINS 2 報告 + WEEKLY-REPORT 4 份 + Session Reports 22 份）、Fusion 架構設計、前沿缺口研究、論文收錄、Token 節省量化,最終產出 9 個檔案。

---

## 一、Session 產出總覽

| # | 檔案 | 產出者 | 類型 | 大小 |
|---|------|--------|------|------|
| 1 | `2026-07-09-fusion-architecture-design-plan.md` | GLM（主） | 架構設計計畫 | 21.9 KB |
| 2 | `2026-07-09-fusion-glm-architecture-validation.md` | GLM | Phase 1 可行性驗證 | 13.5 KB |
| 3 | `2026-07-09-fusion-glm-factory-phase2-config.md` | GLM | Factory Phase 2 配置指南 | 21.5 KB |
| 4 | `2026-07-09-fusion-kimi-token-simulation.md` | Kimi | Token 節省量化模擬 | 22.0 KB |
| 5 | `2026-07-09-fusion-kimi-agents-md-protocol-draft.md` | Kimi | AGENTS.md Fusion Protocol 草稿 | 1.1 KB |
| 6 | `2026-07-09-frontier-model-gaps-kimi-collab.md` | Kimi | 前沿模型缺口研究 | 24.5 KB |
| 7 | `2026-07-09-edge-infra-gaps-kimi-collab.md` | Kimi | 邊緣推論/基礎設施缺口 | 24.3 KB |
| 8 | `papers/2026-05-25-scaling-harness-system-scaling-agentic-ai-2605-26112.md` | GLM（主） | 論文歸檔 | — |
| 9 | `papers/pdfs/2605.26112.pdf` | GLM（主） | PDF 下載 | 419 KB |

---

## 二、核心洞見

### 2.1 Fusion 架構:模型選擇 → 路由策略的範式轉移

**關鍵發現**: Cognition Devin Fusion 的核心創新不是「用兩個模型」,而是「在 compaction 時切換模型 = 零 cache 懲罰」。這個洞見直接挑戰 workspace 既有鐵律「mid-session 禁止切換模型」。

**解法分歧**:
- **Claude Code 路徑**: 保持既有鐵律,用 sub-agent spawn（新 context）模擬 sidekick,用 checkpoint 模擬持久性 — Phase 1 可落地（GLM 驗證: 3/4 ✅, 1/4 ⚠️, 0 ❌）
- **Factory Droid 路徑**: Session API `PATCH /sessions/{id}` 原生支援 mid-session 切換 `model` + `compactionModel` — 可直接實現 Devin Fusion 的 compaction 時切換模式

**架構含義**: workspace 的「通用 Fusion」不是單一實現,而是**兩條平行路徑**:
1. Claude Code = sub-agent fan-out + checkpoint 模擬（保守,不破 cache）
2. Factory Droid = API 層 mid-session routing（激進,原生支援 compaction 切換）

### 2.2 Token 節省:成本加權 -35.2%,頻率加權 +2.8%

**Kimi 量化的關鍵發現**: Fusion 的節省高度依賴任務結構:

| 任務類型 | 節省 | 原因 |
|---------|------|------|
| 大規模遷移 | **53%** | 16 PR 機械執行 cost 檔 + 降級批次 |
| 深度研究 | **37%** | 子代理掃描階段 cost 檔 + 回報精簡 |
| 單檔小改 | **0%** | T0 例外,無 sidekick 介入 |
| 跨模組重構 | **-36%**（增加） | ceiling 升級 + sidekick 額外負擔,品質提升 |
| 安全審查 | **-18%**（增加） | ceiling 威脅判斷 + 對抗審查投資,品質提升 |

**洞察**: Fusion 不是「一律省 token」,而是「機械任務省、判斷任務花」。成本加權 -35.2%（因大規模遷移佔 56% 成本且省 53%）與 Devin Fusion 官方報告的 35-41% 區間一致,驗證了模擬規模。

### 2.3 前沿覆蓋盲區:competitor frontier 從未被選題

**從完整閱讀 22 份 DAILY-TOPICS 發現的系統性盲區**:

連續 22 天的選題聚焦 Claude/Anthropic 生態 + skill engineering,但以下 frontier 信號出現在 digests 中卻從未被深度研究:

| 缺口 | 信號 | workspace 影響 |
|------|------|--------------|
| Cognition SWE-1.7（Kimi K2.7, 1000 tok/s） | RL 小模型逼近 frontier | model-profiles「cost=弱」假設動搖 |
| xAI Grok 4.5（Terminal-Bench 擊敗 Opus 4.8） | 1/5 定價 | ceiling 獨佔假設鬆動 |
| OpenAI GPT-Live-1（全雙工語音） | 即時多模態 agent | 人因確認介面可能演進 |
| DeepSeek-V4-Flash + DGX Spark 1TB | $8K 本地 frontier | FinOps 雲端依賴策略改變 |

**Kimi 協作補完**: 3 個缺口已 filled（SWE-1.7 + Grok 4.5 + GPT-Live）,但結論是「不需立即更新 model-profiles.md」— 因為非 Anthropic 模型基準均未經第三方獨立驗證。

### 2.4 論文收錄:Scaling the Harness 學術 ground truth

收錄了 arXiv 2605.26112《From Model Scaling to System Scaling: Scaling the Harness in Agentic AI》— 這篇論文為 Fusion 架構提供了學術框架:

- **§4.3 Dynamic Skill Routing** = Devin Fusion sidekick 路由的學術對應
- **「harness = first-class object」** = workspace The Loop 設計的外部驗證
- **CheetahClaws 參考實現** = 跨 harness 比較的學術工具

PDF 已下載（419KB），pymupdf4llm 擷取 9 張圖表，歸檔含雙層格式（英文原文 + 中文說明），INDEX.md 已更新（Harness Engineering 46→47）。

### 2.5 Factory Droid 的 Fusion 原生能力

**最重大發現**: Factory Droid 的 Session API 已原生實現 Devin Fusion 的核心機制:

| Factory 功能 | Devin Fusion 對應 | 狀態 |
|-------------|-----------------|------|
| `compactionModel`（Session API） | compaction 時切換模型 | ✅ 已上線 |
| Factory Router | per-task 自動路由 | ✅ GA, 43% 節省 |
| Mixed Models | spec mode 強模型 + default 弱模型 | ✅ 已上線 |
| Custom Droids | sidekick agent | ✅ 已上線 |
| `childInclusiveTokenUsageBySessionId` | per-child token 追蹤 | ✅ API 回傳 |
| BYOK 開源模型 | sidekick 用 GLM/Kimi | ✅ 已上線 |

**GLM Phase 2 配置方案的關鍵修正**: 原設計報告的 `providerLock: anthropic` 在 Factory 文件中找不到對應 CLI 開關 — reasoning trace 相容性實際由 Mixed Models 相容性規則自動強制執行,非手動鎖定。

---

## 三、GLM×Kimi 協作模式驗證

本 Session 是 GLM×Kimi 交叉協作模式的第二次大規模驗證（首次為 07-08 Fable 5 終審）:

| 維度 | 07-08 終審 | 本 Session |
|------|-----------|-----------|
| 協作模式 | fresh-context 對抗審查 | 並行任務分工 + 交叉驗證 |
| GLM 角色 | 終審 reviewer | 架構驗證 + Factory 配置具體化 |
| Kimi 角色 | — | Token 量化 + Protocol 草稿 + 缺口研究 |
| 任務數 | 1 | 6（4 個 Fusion + 2 個缺口） |
| 產出 | 1 報告 | 9 檔案 |

**協作效果**: GLM 和 Kimi 的任務無衝突,各自產出互補（GLM 偏架構驗證/配置,Kimi 偏量化/撰寫）。Token 節省方面,用兩個開源模型（GLM-5.2 ceiling + Kimi K2.7 quality）取代 Opus 4.8 做這些任務,估算節省 ~85% 成本。

---

## 四、待行動項

### P0（立即）

| 項目 | 來源 | 驗證方法 |
|------|------|---------|
| 將 AGENTS.md Fusion Protocol 草稿提交人工審查 | KIMI-B 產出 | `wc -c` ≤1200 + grep 無模型名 |
| 將 tool-schema-degradation 提案升級為 Routine B 最高優先 | 07-09 DAILY-RESEARCH 積壓 4 天 | `grep -qE 'tool.schema' .claude/refs/model-profiles.md` |
| 將 China 偵測 v2.1.91 案例補入 security-hygiene.md | 07-09 DAILY-RESEARCH P0-2 | `grep -iq "2.1.91" .claude/rules/security-hygiene.md` |

### P1（本月）

| 項目 | 來源 | 說明 |
|------|------|------|
| Factory Phase 2 配置落地測試 | GLM-B 產出 | 依配置指南在 Factory CLI 實測 Router + compactionModel |
| Token 節省模擬用 cost-log.jsonl 精確化 | KIMI-A 產出 | 模擬權重為粗估,需實際任務頻率數據 |
| NEW-DOMAINS/INDEX.md 新增 3 個探勘項 | KIMI 缺口研究 | edge-frontier-inference, embodied-agent-rgb, agent-native-infrastructure |

### P2（觀察中）

| 項目 | 來源 | 說明 |
|------|------|------|
| Claude Code persistent sidekick 需求 | Fusion Phase 2 | 需 Claude Code 新功能（persistent background agent cache） |
| Factory Router 43% 節省獨立驗證 | Factory 官方自報 | 路由邏輯為黑箱,需 workspace 實測 |
| 開源模型 eval-hack 風險 | model-profiles §1 | sidekick 用開源模型需額外驗證 |

---

## 五、Session 統計

`<json-render>`{"root":"d","elements":{"d":{"type":"Box","props":`{"flexDirection":"column","padding":1}`,"children":["h","g1","g2","g3"]},"h":{"type":"Heading","props":`{"text":"Session 2026-07-09 統計","level":"h2"}`,"children":[]},"g1":{"type":"Box","props":`{"flexDirection":"row","gap":2}`,"children":["m1","m2","m3","m4"]},"m1":{"type":"Metric","props":`{"label":"產出檔案","value":"9","trend":"up"}`,"children":[]},"m2":{"type":"Metric","props":`{"label":"GLM 任務","value":"3","trend":"up"}`,"children":[]},"m3":{"type":"Metric","props":`{"label":"Kimi 任務","value":"4","trend":"up"}`,"children":[]},"m4":{"type":"Metric","props":`{"label":"論文 PDF","value":"1（419KB）","trend":"up"}`,"children":[]},"g2":{"type":"Box","props":`{"flexDirection":"row","gap":2}`,"children":["s1","s2","s3","s4"]},"s1":{"type":"StatusLine","props":`{"text":"Fusion 架構設計：完成 + Phase 1 驗證通過","status":"success"}`,"children":[]},"s2":{"type":"StatusLine","props":`{"text":"Token 節省量化：成本加權 -35.2%","status":"success"}`,"children":[]},"s3":{"type":"StatusLine":`{"text":"前沿缺口：3 filled + 3 NEW-DOMAINS 建議","status":"success"}`,"children":[]},"s4":{"type":"StatusLine":`{"text":"論文收錄：2605.26112 PDF + 圖表 + INDEX","status":"success"}`,"children":[]},"g3":{"type":"Card","props":`{"title":"關鍵洞察","padding":1}`,"children":["i1","i2","i3"]},"i1":{"type":"KeyValue","props":`{"label":"Fusion 本質","value":"compaction 時切換模型 = 零 cache 懲罰,非雙模型本身"}`,"children":[]},"i2":{"type":"KeyValue","props":`{"label":"Token 節省真相","value":"機械任務省 53%,判斷任務增加 36% — 非一律省"}`,"children":[]},"i3":{"type":"KeyValue","props":`{"label":"Factory 優勢","value":"Session API 原生支援 mid-session model 切換,Claude Code 不支援"}`,"children":[]}}}`</json-render>`

---

## 六、文件指針

| 欲查閱 | 路徑 |
|--------|------|
| Fusion 完整設計 | `research/reports/2026-07-09-fusion-architecture-design-plan.md` |
| Phase 1 可行性驗證 | `research/reports/2026-07-09-fusion-glm-architecture-validation.md` |
| Factory Phase 2 配置 | `research/reports/2026-07-09-fusion-glm-factory-phase2-config.md` |
| Token 節省模擬 | `research/reports/2026-07-09-fusion-kimi-token-simulation.md` |
| AGENTS.md Protocol 草稿 | `research/reports/2026-07-09-fusion-kimi-agents-md-protocol-draft.md` |
| 前沿模型缺口 | `research/reports/2026-07-09-frontier-model-gaps-kimi-collab.md` |
| 邊緣推論/基礎設施缺口 | `research/reports/2026-07-09-edge-infra-gaps-kimi-collab.md` |
| 論文歸檔 | `research/papers/2026-05-25-scaling-harness-system-scaling-agentic-ai-2605-26112.md` |
| 論文 PDF | `research/papers/pdfs/2605.26112.pdf` |
| 論文圖表 | `research/papers/pdfs/figures/2605.26112/` |
