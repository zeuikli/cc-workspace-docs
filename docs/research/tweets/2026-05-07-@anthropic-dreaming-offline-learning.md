---
title: "Anthropic \"Dreaming\": Offline Agent Self-Improvement — @Anthropic"
author: "Anthropic（via VentureBeat coverage）"
date: 2026-05-07
source: "https://venturebeat.com/technology/anthropic-introduces-dreaming-a-system-that-lets-ai-agents-learn-from-their-own-mistakes/"
type: tweet
---

# Anthropic "Dreaming": Offline Agent Self-Improvement — @Anthropic

**來源**：https://venturebeat.com/technology/anthropic-introduces-dreaming-a-system-that-lets-ai-agents-learn-from-their-own-mistakes/
**作者**：Anthropic（via VentureBeat coverage）
**發布日期**：2026-05-07（近似）
**收錄日期**：2026-05-10
**類型**：Anthropic 官方功能公告 + 媒體報導
**分類**：harness-design / context-engineering

---

## 核心概念

> "Dreaming allows AI agents to learn from mistakes offline — separate from the main task flow. Rather than blocking on mistakes during execution, agents accumulate error patterns and improve asynchronously."

---

## 研究摘要

**TL;DR**：Anthropic 引入「dreaming」機制——讓 agent 在離線（不阻斷主任務）狀態下從錯誤中學習。解耦了「執行時的學習」和「任務流的進行」，避免 context 污染。

### Dreaming 的工作流程

```
Main Task Flow (不被阻斷)
      │
      ├── Error occurs → Error event 被記錄到 Dreaming buffer
      │
      └── Task continues...

Offline Dreaming Process (非同步)
      │
      ├── 分析 buffer 中的 error patterns
      ├── 生成 improved heuristics / rules
      └── 更新 agent 的工作記憶（不影響進行中的 session）
```

### Harness 架構意涵

| 傳統方式 | Dreaming 方式 |
|---------|-------------|
| 學習 = 同步，阻斷任務 | 學習 = 非同步，不阻斷 |
| 錯誤修正 = 中斷工作流 | 錯誤修正 = 下次 session 改善 |
| Auto Memory = 扁平累積 | Dreaming = 結構化反思 |
| Context rot risk 高 | Context 保持乾淨 |

---

## 對 ANTHROPIC-ALIGNMENT.md 的影響

此功能直接對應 §六 延伸議題 **議題 2：Post-task Reflection 機制**：

> "Memory Survey（2603.07670）實驗：移除反思 → 48 小時內行為退化。本 workspace 目前 Auto Memory 是扁平累積，沒有明確的「任務後反思」步驟。"

Dreaming 是 Anthropic 對此問題的官方解法。

---

## 評分

| 維度 | 分數 | 理由 |
|------|------|------|
| 相關性 | 9/10 | 直接對應 ANTHROPIC-ALIGNMENT.md 的開放議題 |
| 可行動性 | 7/10 | Dreaming API 是否開放給 cc-workspace 使用？待確認 |
| 新穎性 | 9/10 | 非同步離線學習是新 harness 範式 |
| **總評** | **8.3/10** | — |

---

## 與 cc-workspace 的連結

- `ANTHROPIC-ALIGNMENT.md` §六 議題 2 的進展追蹤
- 若 Dreaming 開放 API，考慮在 `session-stop.sh` 中觸發 dreaming reflection
- 關聯：`research/agent-harness/agent-memory-architecture-2026.md`
