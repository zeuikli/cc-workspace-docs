---
title: "Dive into Claude Code — 系統架構深度分析"
author: "VILA-Lab (arXiv 2604.14228)"
date: 2026-06-07
source: "https://github.com/VILA-Lab/Dive-into-Claude-Code"
tags: [claude-code, architecture, security, context-management, subagents, cve, infrastructure]
topic: "Claude Code 架構系統分析，98.4% 確定性基礎設施，5 層壓縮，pre-trust window 漏洞"
---

# Dive into Claude Code — 系統架構深度分析

VILA-Lab 對 Claude Code v2.1.88（~1,900 TypeScript 檔案，~512K 行程式碼）進行 source-level 架構分析，並發表於 arXiv（2604.14228）。1,481 stars。

**核心結論**：Claude Code 只有 **1.6% 是 AI 決策邏輯**，其餘 **98.4% 是確定性基礎設施**——permission gate、context management、tool routing、recovery logic。Agent loop 本身是簡單的 while-loop；真正的工程複雜度在其周圍的系統。

## 架構數字

| 維度 | 數值 |
|------|------|
| TypeScript 檔案 | 1,884 |
| 程式碼行數 | ~512K |
| 工具數量 | 54 |
| Hook 事件 | 27 |
| 安全層次 | 7 |
| Context 壓縮層 | 5 |
| Permission 模式 | 7 |
| 擴充機制 | 4 |
| Agent loop 核心 | 1 個 while-loop |

## 四大設計問題的答案

| 問題 | Claude Code 的回答 |
|------|--------------------|
| 推理在哪裡？ | Model 推理；harness 執行。~1.6% AI，98.4% 基礎設施 |
| 幾個執行引擎？ | 一個 `queryLoop` 供所有介面（CLI/SDK/IDE）使用 |
| 預設安全姿態？ | Deny-first：deny > ask > allow，最嚴格規則勝出 |
| 綁定資源限制？ | ~200K（舊模型）/ 1M（Claude 4.6 系列）context window，每次 model call 前執行 5 層壓縮 |

## 5 值 → 13 原則 → 實作

**5 個核心價值**：人類決策權威、安全隱私、可靠執行、能力放大、情境適應

**關鍵設計選擇**：當 93% prompt 核准率揭露「核准疲勞」時，反應是重構邊界而非增加警告。

## Agent Loop 技術細節

**每次 model call 前**，5 層壓縮依序執行（最便宜優先）：Budget Reduction → Snip → Microcompact → Context Collapse → Auto-Compact

**每輪 9 步 pipeline**：Settings resolution → State init → Context assembly → 5 pre-model shapers → Model call → Tool dispatch → Permission gate → Tool execution → Stop condition

**兩條執行路徑**：
- `StreamingToolExecutor`：工具在 streaming 中即開始執行（延遲優化）
- 備用 `runTools`：分類工具為 concurrent-safe 或 exclusive

**5 個停止條件**：無工具使用、達最大輪數、context overflow、hook 介入、明確中止

## 安全架構

**7 種 permission 模式**（由嚴到寬）：`plan` → `default` → `acceptEdits` → `auto`（ML 分類器）→ `dontAsk` → `bypassPermissions`

**Deny-first 鐵律**：廣泛 deny 永遠覆蓋窄 allow

**Auto-mode 分類器**（`yoloClassifier.ts`）：獨立 LLM call，含 internal/external permission template，兩階段：fast-filter + chain-of-thought

**重要：Resume 時 permission 不恢復**——信任每 session 重新建立

## Pre-Trust Window 漏洞（CVE）

4 個已修復 CVE 共享同一根因：hooks 與 MCP server 在**信任 dialog 出現前**的初始化期間即執行，創造出在 deny-first pipeline 之外的結構性特權攻擊窗口。

**另一共享失效模式**：per-subcommand 解析造成 event-loop 飢餓——超過 50 個 subcommand 的指令會為避免 REPL 凍結而**完全繞過安全分析**。

## 擴充機制（4 種，依 context 成本排列）

Hooks（零成本）→ Skills（低）→ Plugins（中）→ MCP（高）

**27 個 hook 事件**，4 種執行類型：shell、LLM-evaluated、webhook、subagent verifier

**Skills 關鍵區別**：SkillTool 注入當前 context（便宜）；AgentTool 生成隔離 context（昂貴，但防 context 爆炸）

## Subagent 架構

**6 種內建類型**：Explore、Plan、General-purpose、Guide、Verification、Statusline，加上 `.claude/agents/*.md` 自訂

**Sidechain transcript**：只有摘要回傳給 parent（parent context 受保護，不受 subagent verbosity 污染）

**三種隔離模式**：worktree、remote、in-process；協調透過 POSIX `flock()`

## Context 管理

**9 個有序來源**建構 context window。CLAUDE.md 以 **user context** 傳遞（機率性 compliance），非 system prompt（確定性）。

**4 層 CLAUDE.md 層級**：Managed（`/etc/`）→ User（`~/.claude/`）→ Project（`CLAUDE.md`、`.claude/rules/`）→ Local（`CLAUDE.local.md`，gitignored）

**記憶體**：LLM 掃描記憶檔案 header，選最多 5 個相關檔案。無 embedding，無 vector DB。

## Key Insights
- **98.4% 確定性基礎設施是核心洞見**：agent 能力不是 model 屬性，而是 runtime、context 層、execution boundary、tool 供應鏈共同決定——複製 while-loop 很容易，hooks/classifier/compaction/isolation 才是護城河
- **Pre-trust window 是結構性問題**：初始化期間的特權執行窗口不能用「更嚴格的 hook」修補，因為 hook 本身就在窗口內執行——這是架構設計的根本矛盾
- **CLAUDE.md 是 user context 而非 system prompt**：這意味著 CLAUDE.md 指示是機率性遵從，不是確定性執行，過度依賴 CLAUDE.md 做安全執法是設計錯誤

## Code Examples / Commands

```typescript
// queryLoop 核心結構（簡化）
async function* queryLoop(options: QueryOptions): AsyncGenerator<StreamEvent> {
  while (true) {
    // 1. Context assembly（9 個來源）
    const context = await assembleContext();

    // 2. 5 層壓縮（最便宜優先）
    await runPreModelShapers(context);

    // 3. Model call
    const response = await callModel(context);

    // 4. Tool dispatch + permission gate
    for (const tool of response.tools) {
      if (await checkPermission(tool)) {
        await executeTool(tool);
      }
    }

    // 5. Stop conditions
    if (shouldStop(response)) break;
  }
}
```

```yaml
# Custom agent frontmatter（完整欄位）
# .claude/agents/my-agent.md
---
name: my-agent
description: "專屬任務描述"
tools: Read, Write, Bash
disallowedTools: []
model: sonnet
effort: high
permissionMode: default
mcpServers: []
hooks: {}
maxTurns: 20
skills: []
memoryScope: isolated
background: false
isolation: worktree
---
```
