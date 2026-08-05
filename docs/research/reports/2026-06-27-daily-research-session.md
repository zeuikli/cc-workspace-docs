---
date: 2026-06-27
source: DAILY-RESEARCH/2026-06-27.md
topics: [tokenizer-covert-channel-multiagent-security, omnigent-meta-harness-agent-portability, agent-memory-sleep-time-infrastructure, fable5-comeback-claude-code-v2191-strings, ai-legal-liability-enterprise-deployment]
type: session-report
---

# Session Report 2026-06-27 — Daily Research

## 執行概要

- **研究主題**：5 個（DAILY-TOPICS/2026-06-27.md 全覆蓋）
- **搜尋查詢**：7 次 WebSearch（5 次並行主搜尋 + 2 次補充搜尋）
- **頁面 Fetch**：7 次深度抓取（5 次並行主 Fetch + 2 次補充 Fetch）
- **識別 GAP**：3 個 gap（首次建立）+ 1 個 partial（更新）+ 1 個補充

---

## 本日研究成果摘要

### 最高價值發現（Top 3）

**1. Tokenizer Covert Channel — Claude-as-Monitor 架構假設被推翻**（影響等級：**Critical**）

Wisely Chen「Lingua Ex Machina」實驗：Anthropic Claude 系列（Opus 4.8 + Haiku 4.5）刪除 10 類 Unicode，是 12 家 frontier 廠商中最盲者。針對 Tag Character 隱寫通道，接收方還原率 100%、Claude monitor 偵測率 0%、Youden's J = 0.00。

整個「多廠商 LLM 互監」安全架構的根本假設已被實驗性推翻。49/66 model pairs 存在可利用通道，共 250 個實例。GPT↔Claude 跨廠商組合攻擊面最豐富。

防禦路徑唯一解：deterministic Unicode sanitization 於 harness 層，而非依賴 LLM 判斷。

**2. Omnigent — Meta-Harness 成為 Harness 競爭新標準**（影響等級：**High**）

Databricks 開源 Omnigent（Apache-2.0，2026-06-16），以 YAML 一行切換 Claude Code / Codex / Cursor / Pi，統一 session、tool-call、stream、spend-control API。這是「harness = 護城河」論述的業界主流化信號，與本 workspace .claude/skills/ 哲學高度共鳴。

spend-control policy（per-session 動態預算追蹤）直接對應本 workspace context-management.md 的 Token Budget 設計需求。

**3. Weaviate Engram GA + Sleep-Time Compute — Agent Memory 升格為基礎設施**（影響等級：**High**）

Engram GA（2026-06-24）確認 Extract-Transform-Commit 異步管線為 production-grade agent memory 的業界標準。fire-and-forget API + Temporal durable execution 解決了本 workspace RECORD 階段手動更新 MEMORY.md 的根本侷限。sleep-time compute（離線 trace 分析 → memory 寫回）外部驗證了本 workspace dreaming-consolidator skill 的設計哲學。

---

## 可實作 / 可測試內容

### P0 — 立即可執行（今日或明日，< 2 小時）

**P0-1：EVOLUTION-QUEUE.md 登記 tokenizer blind spot 提案**
- 背景：DAILY-TOPICS 已草擬 security-hygiene.md 修改方向
- 步驟：在 `.claude/EVOLUTION-QUEUE.md` 追加提案條目（多模型互監 → 必加 Unicode sanitization 警示）
- 驗證：`grep -q "tokenizer\|blind.spot" .claude/EVOLUTION-QUEUE.md && echo OK`
- 安全邊界：僅登記提案，不修改 security-hygiene.md（DAILY-TOPICS 明確標注待人工審核）

**P0-2：MEMORY.md 本日 session 記錄**
- 步驟：追加 `## Session 2026-06-27 — Tokenizer Blind Spot + Omnigent + Fable5 週配額` 段落
- 驗證：`grep -q "2026-06-27" memory/MEMORY.md && echo OK`

### P1 — 本月優先（需輕量設計，2–8 小時）

**P1-1：Unicode Sanitization Hook 設計與實作**
- 目標：在 agent pipeline 邊界（PreToolUse 或 PostToolUse hook）加入確定性字元過濾
- 實作：NFC 正規化 + PUA（U+E000–U+F8FF）+ Tag Characters（U+E0000–U+E01FF）黑名單
- 驗收：含 U+E0001 payload 通過 hook 後字元被清除；`grep -c "E000" <(echo $'')` = 0
- 參考：GLOSSOPETRAE 工具的字元類別清單（elder-plinius/GLOSSOPETRAE）

**P1-2：Omnigent YAML Spec 對照分析**
- 目標：讀取 omnigent-ai/omnigent GitHub repo YAML schema，對照 .claude/skills/ 結構
- 驗收：完成對照表（omnigent spec field → workspace 對應位置或 gap），存入 `.claude/refs/`
- 價值：識別 spend-control policy 語法可否直接借鏡 context-management.md hook 設計

### P2 — 觀察中（需更多信號再決定）

**P2-1：Fable 5 週配額方案**
- 觀察條件：Anthropic 官方公告回歸時間表 + 確認每週內含用量數值（目前 zero traffic 狀態）
- 行動觸發：一旦確認 → 更新 pilot-shared-preflights.md §E 定價矩陣

**P2-2：EU AI 法律責任框架化**
- 觀察條件：德國判決上訴結果 / EU 層級採納類似推理
- 行動觸發：評估 research-hub / media-research 輸出格式來源追溯性需求

---

## GAP 狀態更新

| GAP | 研究前狀態 | 研究後狀態 | 行動 |
|-----|-----------|-----------|------|
| tokenizer-covert-channel-multiagent-security | gap (0篇) | **filled** — Wisely Chen + arXiv 2605.22001 + SLEIGHT-Bench | P0-1 EVOLUTION-QUEUE 登記 |
| omnigent-databricks-agent-portability | gap (0篇) | **filled** — Databricks blog + GitHub + Latent Space | P1-2 YAML spec 對照 |
| agent-memory-sleep-time-compute | gap (0篇) | **filled** — Engram deep dive + Latent Space AINews | dreaming-consolidator reference 更新 |
| fable5-comeback-code-strings | partial (舊) | **updated** — v2.1.190 週配額字串驗證 | P2-1 觀察中 |
| ai-legal-liability-court-ruling | gap (0篇) | **filled** — 德國判決 + Schneier + Simon Willison | P2-2 觀察中 |

---

## 下一次循環優先事項

1. **P0-1 執行**：EVOLUTION-QUEUE.md 登記 tokenizer blind spot 提案（< 30 分鐘）
2. **P1-1 啟動**：設計 Unicode Sanitization PreToolUse hook 的 spec，提交 implementer agent
3. **Fable 5 監控**：下次 Routine A 若發現 Anthropic 官方聲明，立即觸發 pilot-shared-preflights.md §E 更新
