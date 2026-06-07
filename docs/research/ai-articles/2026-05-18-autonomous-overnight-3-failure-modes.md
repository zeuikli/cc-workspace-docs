---
title: "Running Claude Code Autonomously Overnight — What Breaks and How to Fix It"
author: "Eva Khmelinskaya"
date: 2026-05-18
source: "https://medium.com/@evekhm/running-claude-code-autonomously-overnight-what-breaks-and-how-to-fix-it-3bee3bd958b5"
tags: [claude-code, autonomous, overnight, orchestration, context-window, STATUS.md, fail-modes]
topic: orchestration
---

# Running Claude Code Autonomously Overnight — What Breaks and How to Fix It

Eva Khmelinskaya 嘗試讓 Claude Code 無人值守跑 12 小時後發現 session 靜默停止——Claude 工作了很久但未意識到已失敗。根本原因是 context window 耗盡，觸發三個連鎖失敗模式。

## 三個失敗模式

**1. Context Overflow & Thrashing**
工具輸出（API logs、file reads、script results）累積速度超過 compaction 機制的處理能力。當 summary 仍超過可用空間，session 進入持續 compact → 立即重填的循環，工作停頓但不報錯。

**2. Instruction Dilution（指令稀釋）**
多輪 compaction 後，CLAUDE.md 的關鍵規則被壓縮進 summary，模型逐漸忽略已建立的規範。「即使是 CLAUDE.md 的關鍵指令，在多次 compaction 後也會失去效力」。

**3. No Self-Awareness（無自我感知）**
Claude 無法查詢剩餘 context budget。無法偵測低記憶體，持續工作直到突然觸及上限，沒有優雅的交接機制，12 小時的工作靜默停止。

## 三層修復方案

**Layer 1：CLAUDE.md 輸出重導規則**
注入 context 管理指令：
- 冗長輸出導向至檔案，只以 `tail` 摘要
- 禁止 HTTP/API raw logs 進入對話
- 避免重複讀取已快取的檔案
- 每個里程碑後更新 `STATUS.md`（記錄結果，非原始資料）

效果：context 效率提升 ~10x。

**Layer 2：STATUS.md Handoff 文件**
跨 session 繼承文件，記錄：
- 完成狀態
- 下一步驟
- 關鍵指標

讓每個新 session 在不需完整 context 轉移的情況下接續工作。

**Layer 3：Phase Orchestrator Shell Script**
將 12+ 小時工作切分為 30-60 分鐘的 phase，shell script 依序啟動 `claude --print` sessions：
- 每個 phase 有獨立 context budget
- Phase-specific prompts
- `--max-budget-usd` 成本護欄
- 透過共享檔案通訊（不依賴對話 context）

## 關鍵實作細節

```bash
claude --print \
    --model opus \
    "$PROMPT" \
    < /dev/null \
    > phase.log 2>&1
```

**`< /dev/null` 是必須的**：沒有它，背景 process 會等待 stdin，然後提前退出並留下空 log。

## /goal 自我修復指令

```bash
claude -p "/goal Run analyze.py. Goal: results.txt has valid JSON"
```

Claude 內部重試直到條件達成，不需外部 watchdog script。

## 核心 Meta-Pattern

把自主 Claude session 當成 CI pipeline，而非對話：
- Jobs 透過 artifacts（檔案、STATUS 文件）通訊，不依賴對話 context
- 用 `nohup` 啟動一次後離開
- Claude 先在互動 session 建立可靠性基礎設施，再用這些工具執行自主工作

**結果**：5 個測試 phase 全部成功完成，產生 MB 級實驗資料，同時遵守 context budget。

## Key Insights
- 三個失敗模式：context window 耗盡（冗長工具輸出靜默累積）、instruction dilution（CLAUDE.md 規則在 90+ 分鐘 session 的多次 compaction 後被壓縮消失）、silent stalling（Claude 無感知工作了 12 小時才停止）
- 三層修復：CLAUDE.md 輸出重導規則（context 效率 10x）、STATUS.md handoff artifact、帶 30-60 分鐘 `claude --print` 的 phased orchestrator shell script
- Meta-pattern：Claude 在互動 session 中建立自己的可靠性基礎設施，再用這些工具執行自主工作

## Code Examples / Commands

```bash
#!/bin/bash
# phased-orchestrator.sh

PHASES=("research" "analyze" "synthesize" "validate" "report")
BUDGET="5.00"

for PHASE in "${PHASES[@]}"; do
  PROMPT="Continue from STATUS.md. Execute phase: $PHASE. Update STATUS.md when complete."
  
  echo "[$(date)] Starting phase: $PHASE"
  
  claude --print \
      --model opus \
      --max-budget-usd "$BUDGET" \
      "$PROMPT" \
      < /dev/null \
      > "phase-${PHASE}.log" 2>&1
  
  EXIT_CODE=$?
  echo "[$(date)] Phase $PHASE completed with exit code: $EXIT_CODE"
  
  # Check STATUS.md for phase completion signal
  if ! grep -q "phase: $PHASE: DONE" STATUS.md; then
    echo "Phase $PHASE did not complete successfully"
    exit 1
  fi
done
```

```markdown
# CLAUDE.md 輸出重導規則（插入）
## Context Management Rules
- Never print raw API responses; save to file and use `tail -20 <file>` to summarize
- After every milestone, write summary to STATUS.md (results only, not raw data)
- Do not re-read files you have already processed in this session
- If a command output exceeds 100 lines, redirect to file: `command > output.log 2>&1`
```
