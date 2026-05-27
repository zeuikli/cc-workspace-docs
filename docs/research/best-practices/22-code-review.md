---
title: "Code Review — 多代理 PR 自動審查完整指南"
source: "https://code.claude.com/docs/en/code-review"
type: best-practices
---

# Code Review — 多代理 PR 自動審查完整指南

> 來源：https://code.claude.com/docs/en/code-review  
> 補充來源：https://claude.com/blog/code-review  
> 收錄日期：2026-05-01  
> 涵蓋：Code Review 運作原理、Setup 流程、Severity 等級、REVIEW.md 自訂、@claude review 指令、定價、troubleshooting

---

## 一、功能概述

**Code Review** 是 Claude Code 的多代理 PR 自動審查功能（research preview，Team / Enterprise 訂閱）。
一旦啟用，Claude 分析 GitHub PR 並以 inline comments 形式標出：邏輯錯誤、安全漏洞、邊界情況破壞、潛在回歸問題。

官方統計數字（Anthropic 內部驗證）：
- 工程師程式碼產出成長 **200%**
- 獲得實質性 review comment 的 PR 比例：**16% → 54%**
- 誤報率（false positive rate）：**< 1%**

Zero Data Retention 組織不可用。

---

## 二、運作原理

### 2.1 審查流程

1. PR 開啟 / push / 手動觸發 → 啟動多個平行 agent
2. 每個 agent 分析 diff + 周邊程式碼（各負責不同類別的問題）
3. Verification pass：對候選問題驗證對實際程式碼行為，過濾誤報
4. 去重 + 按 severity 排序 → 發佈為 PR inline comments
5. 若無問題：發佈簡短確認 comment
6. 平均完成時間：**20 分鐘**

### 2.2 Severity 等級

| 標記 | 等級 | 含義 |
|------|------|------|
| 🔴 | **Important** | merge 前應修復的 bug |
| 🟡 | **Nit** | 次要問題，值得修但不阻塞 |
| 🟣 | **Pre-existing** | 存在於 codebase 但非此 PR 引入的 bug |

每個 finding 含**可展開的 extended reasoning**，說明 Claude 為何標記此問題及驗證方式。

### 2.3 Check Run 輸出

GitHub Checks tab 出現「**Claude Code Review**」check run（結論永遠為 neutral，不阻擋 merge）。
Check run Details 含完整 finding 表格（按 severity 排序）：

```
| Severity     | File:Line                  | Issue                         |
|--------------|---------------------------|-------------------------------|
| 🔴 Important | src/auth/session.ts:142   | Token refresh races with logout |
| 🟡 Nit       | src/auth/session.ts:88    | parseExpiry returns 0 on malformed input |
```

用 CI 腳本讀取 severity 統計（machine-readable format）：

```bash
gh api repos/OWNER/REPO/check-runs/CHECK_RUN_ID \
  --jq '.output.text | split("bughunter-severity: ")[1] | split(" -->")[0] | fromjson'
# 回傳：{"normal": 2, "nit": 1, "pre_existing": 0}
# "normal" = Important findings 數量
```

### 2.4 Rating 機制

每則 review comment 附帶 👍 / 👎。
Anthropic 收集 PR merge 後的 reaction 統計 → 用於調整 reviewer 品質。
回覆 inline comment **不會**觸發 Claude 重新回應或更新 PR。

---

## 三、Setup 流程

> 前提：需要 Claude 組織 admin 權限 + GitHub 組織 GitHub App 安裝權限。

1. 前往 `claude.ai/admin-settings/claude-code` → Code Review 區塊 → **Setup**
2. 安裝 **Claude GitHub App** 到 GitHub 組織（需要 Contents read/write、Issues read/write、Pull requests read/write）
3. 選擇要啟用 Code Review 的 **repositories**
4. 為每個 repo 設定 **Review Behavior**：
   - **Once after PR creation**：PR 開啟或從 draft 轉 ready 時執行一次
   - **After every push**：每次 push 觸發（成本最高，自動解析已修復的 thread）
   - **Manual**：僅在 `@claude review` comment 時執行

驗證：開一個測試 PR → 數分鐘內出現「Claude Code Review」check run。

---

## 四、手動觸發指令

兩個 comment 指令，在任何 repo（任何模式下）均有效：

| 指令 | 效果 |
|------|------|
| `@claude review` | 執行一次 review，並訂閱此 PR 後續 push 觸發 |
| `@claude review once` | 執行一次 review，**不**訂閱後續 push |

使用條件：
- 必須是 PR **頂層 comment**（非 diff inline comment）
- 指令放在 comment 最前面
- 需有 repo owner / member / collaborator 存取權
- PR 必須是 open 狀態（manual 模式也支援 draft PR）

---

## 五、自訂 Review 行為

### 5.1 CLAUDE.md

Code Review 讀取 repo 中所有層級的 `CLAUDE.md`，將新引入的違規標為 🟡 Nit。
支援雙向：若 PR 讓某 `CLAUDE.md` 說明過時，Claude 也會標記需更新文件。

### 5.2 REVIEW.md（Review 專屬，最高優先）

放在 repo root 的 `REVIEW.md` 被注入到每個 review agent 的 system prompt 最高優先區塊。

**注意**：
- 內容逐字貼入，`@` import 語法**不展開**
- 規則直接寫在檔案中，不要引用其他檔案

#### 可調整的項目

| 項目 | 說明 |
|------|------|
| **Severity 重新定義** | 為你的 repo 重定義什麼算 🔴 Important |
| **Nit 上限** | 設定每次 review 最多幾則 Nit comment |
| **Skip 規則** | 排除 generated code、lockfile、vendored 依賴、特定分支 |
| **Repo 專屬檢查** | 「所有新 API route 必須有 integration test」等規則 |
| **Verification bar** | 要求附 `file:line` 引用才能發佈某類 finding |
| **Re-review 收斂** | 「第一次 review 後，只報 Important」防止 style 打 7 輪 |
| **Summary 格式** | 「先寫 '2 factual, 4 style' 摘要行再展開細節」 |

#### REVIEW.md 完整範例

```markdown
# Review instructions

## What Important means here

Reserve Important for findings that would break behavior, leak data,
or block a rollback: incorrect logic, unscoped database queries, PII
in logs or error messages, and migrations that aren't backward
compatible. Style, naming, and refactoring suggestions are Nit at most.

## Cap the nits

Report at most five Nits per review. If you found more, say "plus N
similar items" in the summary instead of posting them inline. If
everything you found is a Nit, lead the summary with "No blocking issues."

## Do not report

- Anything CI already enforces: lint, formatting, type errors
- Generated files under `src/gen/` and any `*.lock` file
- Test-only code that intentionally violates production rules

## Always check

- New API routes have an integration test
- Log lines don't include email addresses, user IDs, or request bodies
- Database queries are scoped to the caller's tenant
```

---

## 六、用量分析

前往 `claude.ai/analytics/code-review` 查看：

| 區塊 | 內容 |
|------|------|
| PRs reviewed | 每日審查 PR 數量 |
| Cost weekly | 每週 Code Review 費用 |
| Feedback | 開發者因修復而被自動解析的 comment 數 |
| Repository breakdown | 每個 repo 的 PR 審查數 + comment 解析數 |

---

## 七、定價

- 按 token 用量計費，**不計入**訂閱內含用量（extra usage 計費）
- 平均每次 review：**$15–25**（依 PR 大小、codebase 複雜度、需驗證的問題數而異）
- 設定月費上限：`claude.ai/admin-settings/usage` → Claude Code Review service 的 limit

| 觸發模式 | 費用影響 |
|---------|---------|
| Once after PR creation | 每 PR 一次費用 |
| After every push | 費用 × push 次數 |
| Manual | 無 review = 無費用；@claude review 後轉為 per-push |

---

## 八、Troubleshooting

### 8.1 review 失敗 / 超時

Check run 標題顯示「Code review encountered an error」或「Code review timed out」：
- Comment `@claude review once` 重新觸發
- GitHub Checks tab 的 **Re-run** 按鈕**無效**（不會重觸 Code Review）

### 8.2 超過月費上限

PR 上出現 spend-cap message → 下個計費週期自動恢復，或 admin 在 `claude.ai/admin-settings/usage` 調高上限。

### 8.3 找不到 inline comments

若 check run 顯示有 finding 但看不到 inline comments，找這些位置：
- **Check run Details**：完整 finding 表格（即使 inline comment 被 GitHub 拒絕也存在）
- **Files changed tab annotations**：直接標在 diff 行上
- **Review body「Additional findings」**：review 進行中 push 導致舊行號失效的 finding

---

## 九、與本 Workspace 的整合

- **REVIEW.md** 可搭配本 workspace 的 `/deep-review` skill（本地 commit 前）使用，形成雙層 review 防線
- Code Review (managed) 適合 PR 開啟後的**雲端平行審查**；`/deep-review` 適合 commit 前的**本地三維度審查**
- `CLAUDE.md` 在兩者中共享，規則統一維護

---

## Known Gotchas

- `@claude review` 在 **draft PR** 不觸發（除非在 Manual 模式下手動指定）
- `REVIEW.md` 的 `@import` 語法無效，規則必須直接寫入
- check run 結論永遠 neutral，無法直接用作 branch protection rule → 需用 `gh` + jq 解析 severity JSON 自建 gate
- Re-run 按鈕無法重觸 Code Review，務必用 comment 指令
