# Session Insights — 評分機制統一 + 全局索引同步 + 工作流整合研究

> **日期**: 2026-06-15  
> **來源**: Session D/E（claude/research-article-scoring-dkv0rn branch；PRs #652–658）  
> **類型**: Session Learning Report  
> **Topic**: Scoring Unification · Index Sync · Quality Pipeline Design

---

## 1. 核心任務與結果

### 1.1 評分機制統一（SCORING.md §1）

**問題**：research/ 目錄存在兩套評分體系混用：
- `五維評分（X/5）`（舊格式，27 篇 tweets）
- `A-E /10 加權`（新 SCORING.md §1 格式）

**解法**：
- 27 篇 tweets 全量遷移至 A-E /10 加權（batch 並行執行，multi-mode-agent）
- 2 篇 ai-articles placeholder 補齊評分（agents-md-design 8.0/10、agents-md-haiku-opus-taiwan 6.3/10）
- SCORING.md 新增 §3（推文評分，與 §1 相同公式）

**關鍵規則確立**：
- tweets 評分 = SCORING.md §3（= §1 完全相同，統一入口）
- 加權公式：`A×0.3 + B×0.2 + C×0.2 + D×0.15 + E×0.15`（滿分 10）

### 1.2 舊 Skill 名稱清除

**遷移對應表**：

| 舊名稱 | 新名稱 | 涵蓋檔案 |
|--------|--------|---------|
| `score-article` | `research-hub:score` | hooks/user-prompt-submit.sh · ROUTINE-B · 24-plugins.md |
| `twitter-research` | `media-research` | twitter-FORMAT.md · twitter-PROTOCOL.md · deep-research-source-workflow.md |

**掃描方法論**：`grep -r "score-article\|twitter-research" .claude/ research/` 全域掃描後逐一確認（排除 ai-news/ 歸檔內容等 false positive）。

### 1.3 INDEX / README 全局同步

**修正項目**：

| 檔案 | 變更 |
|------|------|
| research/tweets/INDEX.md | 193 → 267 |
| research/tweets/README.md | 240 → 267；評分描述更新 |
| research/ai-articles/scored/INDEX.md | 52 → 50（排除 3 個特殊檔案）|
| research/ai-articles/scored/README.md | 48 → 50；日期範圍延至 2026-06 |
| research/ai-articles/INDEX.md | 移除不符 ≥8.5 閾值的 8.1/10 entry |
| research/articles/INDEX.md | 空表 → 11 篇實際文章 |
| BRAIN.md | tweets 178→267；scored 48→50；新增 DAILY-TOPICS；Updated→2026-06-15 |
| WORKSPACE-INDEX.md | tweets 183→267；substack 178→171；新增 DAILY-TOPICS；Current State 日期更新 |
| README.md | tweets 194→267 |

**教訓**：multi-mode agent 報告 scored=51（誤判，2 篇新文章已含在原 50 內）→ fable-pilot 機械重驗 `ls | wc -l` 確認為 50 並駁回。**subagent verdict 非證據，親跑確定性檢查才算數。**

---

## 2. 技術 Bug 分析

### 2.1 `$(cat <<'EOF'...)` 字面文字寫入 MEMORY.md

**症狀**：MEMORY.md 中 PR #651 記錄出現 `$(cat <<'EOF'...EOF)` 字面文字。

**根因**：
1. `gh pr create --body "$(cat <<'EOF'...EOF)"` 在某些執行環境下 heredoc 未被 bash 展開
2. PR body 帶著字面文字存入 GitHub
3. `memory-pr-record-gh.sh` hook 用 `gh pr view --json body` 抓 PR body 原封不動寫入 MEMORY.md

**根治方案**：改用 `mcp__github__create_pull_request`（直接傳字串，不走 bash heredoc）

**Lesson**：任何涉及 `gh pr create` 的 body 傳遞，優先用 MCP tool 避免 heredoc 展開問題。

### 2.2 Worktree Cherry-pick 計數誤差

**症狀**：Agent 在 worktree 執行後，帶回的 INDEX.md 計數（51）比真實值（50）多 1。

**根因**：Agent 在 worktree 計算時可能包含了 AGENTS-MD-RESEARCH-INDEX.md（特殊檔案），而正確排除邏輯是 `grep -v "INDEX\|README\|AGENTS-MD"。`

**防範**：計數驗算命令必須明確排除 INDEX/README/特殊檔案，並在 parent 主對話親跑確認。

---

## 3. Git 流程教訓

### 3.1 branch protection 阻擋直接 push main

**現象**：Claude Code auto-mode classifier 阻擋 `git push origin main`。

**標準流程**：
```bash
git checkout -b fix/<name>    # 從 main 建分支
git add <files>
git commit -m "..."
git push -u origin fix/<name>
# mcp__github__create_pull_request → mcp__github__merge_pull_request
```

**教訓**：即使是 MEMORY.md 這樣的非代碼檔案，也必須走 PR 流程。

### 3.2 `.memory-sync-seen.txt` 持續產生未提交變更

**現象**：每次 MEMORY.md 有新 commit，hook 就更新 `.memory-sync-seen.txt`，stop hook 就抱怨未提交。

**現況**：需要定期手動 commit 這個檔案（PR 流程）。

**潛在改善**：考慮在 `.gitignore` 加入此檔案，或讓 hook 自動 commit + push（目前已有類似機制但可能在 remote 環境不觸發）。

---

## 4. 工作流整合設計（`/qp` quality-pipeline）

### 4.1 問題陳述

現況：multi-mode（執行）+ fable-pilot（稽核）需分兩步手動呼叫，缺乏標準 gate 機制。

### 4.2 推薦架構（thin wrapper SKILL）

**新建 `quality-pipeline` SKILL**，觸發詞 `/qp`：

```
Phase 1 — ROUTE
  multi-mode-agent 依任務規模選 model（sonnet/opus/fable）
  取回 worker verdict（標記為 unverified）

Phase 2 — GATE（fable-pilot 精選 3 gate）
  G1: 確定性 grep 機械驗證（unverified → verified）
  G2: git diff 只含預期變更（worktree 落地檢查）
  G3: 四軸品質審查（security/reliability/maintainability/taste）
      ← sonnet 模式執行 G1+G2；opus/fable 模式加 G3

Phase 3 — DECIDE
  全 PASS → 回報 verified 結果
  任一 FAIL → 停，完整錯誤 + escalation 建議
  失敗 ≥3 → 回報 parent，不 self-retry
```

**設計原則**：
- 不修改 `multi-mode-skill` 或 `fable-pilot`（保持單一職責）
- 參照 `verified-merge` 的 gated pipeline 結構
- Gate 邏輯全為確定性 bash，無新 LLM 依賴

**實施複雜度：Low**（只需新增一個 SKILL.md + RESOLVER.md 一行登記）

---

## 5. 稽核方法論

### 5.1 四問框架（fable-pilot 模式 1 — 稽核）

稽核任務的固定問題集：
1. 哪裡互相矛盾？（雙方原文 + file:line）
2. 哪些規則在管理更弱的模型？
3. 哪些文件以壞示範教學？
4. 刪什麼？原樣留什麼？（report-only，裁決權在使用者）

### 5.2 計數稽核的確定性驗算步驟

```bash
# 1. 取真實計數
ls research/tweets/*.md | grep -v "INDEX\|README" | wc -l

# 2. 對照 INDEX 宣告
grep -m3 "[0-9]" research/tweets/INDEX.md

# 3. 掃描殘留過期值
grep -n "178\|183\|194\|48 scored" BRAIN.md WORKSPACE-INDEX.md README.md
```

### 5.3 False Positive 識別

本 session 識別的 false positive 類型：
- `research/ai-news/` 歸檔內容提到 "twitter research"（平文，非 skill 名稱）
- `research/articles/*.md` 內容中的歷史 skill 名稱（已歸檔文章）
- ROUTINE-B 的 `五維評分維度定義（A-E /10 加權）` 是描述性文字（非舊格式）

---

## 6. 關鍵數字（截至 2026-06-15）

| 指標 | 值 |
|------|---|
| research/tweets/ | 267 篇 |
| research/ai-articles/scored/ | 50 篇（53 總 .md - 3 特殊檔案）|
| research/DAILY-TOPICS/ | 1 篇（Routine A 首次執行）|
| healthcheck | PASS 125 / WARN 2 / FAIL 0 |
| PRs merged (本 session) | #652 · #654 · #655 · #656 · #657 · #658 |

---

## 待整合行動

| 行動 | 優先 | 說明 |
|------|------|------|
| 實作 `/qp` quality-pipeline SKILL | 🟡 | thin wrapper，複雜度 Low |
| `.memory-sync-seen.txt` 自動 commit | 🟡 | 避免 stop hook 持續抱怨 |
| sub-agent 計數驗算命令標準化 | 🟡 | 加入 GOTCHAS.md |
| scored/ 計數精確排除邏輯文件化 | 🟢 | 防止未來 agent 誤算 |
