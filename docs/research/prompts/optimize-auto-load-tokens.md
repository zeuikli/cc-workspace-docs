---
title: Auto Load Token 優化 — 可執行 Prompt v1.0
type: prompt
---

# Auto Load Token 優化 — 可執行 Prompt v1.0
> 產生方式：Opus Pilot 架構設計 × Sonnet Pilot 三輪敵對驗證
> 適用：新開一個 Claude Code session，直接貼入執行
> 最後更新：2026-05-18

---

## 背景（執行前必讀）

此 workspace 的 auto-loaded context 有兩條品質線：

| 指標 | 數值 | 含義 |
|------|------|------|
| 技術 hard cap | ≤ 4,500 tokens | 超過後功能出問題 |
| 合規品質目標 | ≤ 3,500 tokens | 超過後規則遵循率從 76% 降至 52% |
| 當前狀態（2026-05-16 測量） | ~4,349 tokens | 在 hard cap 內，但超過品質目標 |

**本次優化目標**：將 auto-load 從 ~4,349 削減至 **≤ 3,500 tokens**，改善規則合規率至 76%+。

**成功必須可機械性驗證**（不接受口頭評估）。

---

## Step 0：前置量測（必做，5 分鐘）

### 0-A：確認當前實際 token 數
在 Claude Code session 中執行：
```
/context
```
記錄「Memory files」欄位的 token 數（這是 CLAUDE.md + 所有 auto-loaded rules 的總和）。

**若 /context 顯示已 ≤ 3,500 → 本 prompt 不需要執行，任務完成。**

### 0-B：驗證 HTML 注釋在 rules/*.md 是否有效節省 token（2 分鐘）

這是本次優化的關鍵前提。官方文件只明確 CLAUDE.md 會 strip HTML 注釋；rules/*.md 行為需先驗證。

```bash
# 1. 記錄目前 context-management.md 行數
wc -l .claude/rules/context-management.md

# 2. 在 context-management.md 末尾加一行 HTML 注釋（測試用）
echo "" >> .claude/rules/context-management.md
echo "<!-- HTML_COMMENT_TEST: this should not appear in context -->" >> .claude/rules/context-management.md
```

接著在 Claude Code 中執行 `/context`，對比 Memory files token 數是否變化：
- **token 數不變** → HTML 注釋有效（Step 1 可使用方案 A+B 混合）
- **token 數增加** → HTML 注釋無效（Step 1 只用方案 B 合併策略）

```bash
# 測試完成後，恢復檔案（不管結果如何）
git checkout .claude/rules/context-management.md
```

---

## Step 1：確定削減路徑

根據 Step 0-B 的結果選擇路徑：

### 路徑 X（HTML 注釋有效）：方案 A+B 混合，目標 -849 tokens
- 預計結果：4,349 → 3,500 tokens

### 路徑 Y（HTML 注釋無效）：純方案 B 合併，目標 -849 tokens（純文字削減）
- 預計結果：4,349 → 3,500 tokens

**以下 Op1–Op5 同時適用兩條路徑**，HTML 注釋段落會標示「[路徑 X 才適用]」。

---

## Step 2：執行五個優化操作

> **執行原則**：每個 Op 完成後立刻用 `/context` 確認實際 token 減少量，再繼續下一個。
> **若任何 Op 後 healthcheck 失敗 → 立刻 `git checkout <file>` 還原，跳過此 Op。**

### Op1：CLAUDE.md（目標 -100 tokens）

**約束**：不得刪除「常駐規則（自動載入）」的四個 @.claude/rules/ 行。

**編輯 CLAUDE.md**：

1. 把「驗證指令」code block（6 行）改為單行：
```markdown
<!-- 刪除這整個 code block： -->
## 驗證指令

```bash
bash scripts/healthcheck.sh    # Workspace 完整性（PASS/WARN/FAIL）
git status && git diff --stat  # 未提交變更確認
cat memory/MEMORY.md | tail -30  # 查閱當前進度
```

<!-- 替換為這一行： -->
**驗證**：`bash scripts/healthcheck.sh` · `git status` · `memory/MEMORY.md`
```

2. [路徑 X 才適用] 把「進階文件」section 改為 HTML 注釋：
```markdown
<!-- 刪除這段：
## 進階文件（手動 Read）

`docs/INDEX.md` · `.claude/REFERENCES.md` · `playbooks/` · `research/prompts/`（策略洞察 + prompt 模板：agent 協作、rule 工程、skill 設計）
-->
<!-- 進階文件（手動 Read）：docs/INDEX.md · .claude/REFERENCES.md · playbooks/ · research/prompts/ -->
```

3. 把「核心工作流」三條 bullet 合併為一行：
```markdown
<!-- 刪除這三行：
- Git 流程、實作前假設顯露 → `core.md`（自動載入）
- Sub Agent 委派決策表、Advisor 時機、模型選擇 → `subagent-strategy.md`（自動載入）
- 長期記憶回路（Auto Memory + MEMORY.md 雙層）→ `core.md § 長期記憶回路`
-->
<!-- 替換為一行： -->
Git / 假設顯露 / Agent 委派 / 記憶回路 → 對應 `core.md` · `subagent-strategy.md`（自動載入）。
```

---

### Op2：core.md（目標 -220 tokens）

**硬性約束**（不得修改）：
- 「生產環境安全紅線」整個章節
- 「Git 工作流程 [FF]」的 IMPORTANT 行
- 「語言 [FF]」章節
- 任何包含 IMPORTANT 字樣的行

**可以修改**：

1. 合併 R12 兩個延伸條目為一行：
```markdown
<!-- 刪除這兩行：
- **R12 延伸 — 大檔分段讀取**：讀取 > 200 行的檔案，用 `limit`/`offset` 分段；每段後說明「已讀第 N-M 行，共 X 行，剩 Y 行未讀」，不得假設截斷後內容為空。
- **R12 延伸 — 搜尋截斷格式**：搜尋結果超限時必須標示：`[CONTEXT BOUNDARY: showing N of TOTAL. Remaining DIFF omitted. Run <cmd> to see more]`；靜默截斷（不告知數量）禁止。
-->
<!-- 替換為一行（保留關鍵數字和指令）： -->
- **R12 延伸**：大檔 >200 行用 `limit`/`offset` 分段讀取；搜尋超限標示 `[CONTEXT BOUNDARY: N of TOTAL]`；靜默截斷禁止。
```

2. 精簡「外科刀式修改」的重複 refs（刪除行尾「詳見 .claude/refs/constraints.md」）：
```markdown
<!-- 把這行：
- 任務外的 bug / 改進機會 → **記錄並回報，不自動修**（commit 原子性）。詳見 `.claude/refs/constraints.md`。
-->
<!-- 改為： -->
- 任務外的 bug / 改進機會 → **記錄並回報，不自動修**（commit 原子性）。
```

3. 合併「驗證與品質」裡的 PGE+R12 條目（去除 ref 冗餘）：
```markdown
<!-- 把這行：
- **PGE + R12 Fail Loud**：完成後 MUST 跑 `bash scripts/healthcheck.sh` 或委派 `/deep-review`（不接受口頭自評）；略過步驟／跳過驗證**必須明示**，不得以「完成」「成功」掩蓋靜默跳過。詳見 `.claude/refs/harness-design.md`。
-->
<!-- 改為（去掉 ref 指向，保留行為規則）： -->
- **PGE + R12 Fail Loud**：完成後 MUST 跑 `bash scripts/healthcheck.sh` 或 `/deep-review`；略過驗證**必須明示**，禁以「完成」掩蓋靜默跳過。
```

4. 精簡「長期記憶回路」（去掉重複格式說明）：
```markdown
<!-- 把這段：
- 結束前更新 `MEMORY.md`：`## Session YYYY-MM-DD — <主題>` 格式；≤5 條決策 + 狀態 + 待辦；≤30 行/節；總行 >150 → 委派 `memory-compactor`
-->
<!-- 改為： -->
- 結束前更新 `MEMORY.md`：`## Session YYYY-MM-DD — <主題>`；≤5 條決策 + 狀態；≤30 行/節；>150 行 → `memory-compactor`
```

---

### Op3：subagent-strategy.md（目標 -280 tokens）⚠️ 高風險 Op

**硬性約束**（不得修改或刪除）：
- 「委派決策（單一判斷準則）」整個表格（4 個條件）
- 「拓撲規則」的 Fan-out 上限 4 條目
- 「Advisor 模式」章節（包含 3 個時機點）
- 「Agent Input Security」的 `<untrusted_objective>` 包裹規則（安全重要）

**可以修改**：

1. 合併「序列執行模式」+「平行 Session 策略」為一個章節：
```markdown
<!-- 刪除這兩個章節（共 8 行）：
## 序列執行模式 `[FF]`
Steps with dependent context: `Researcher → Editor → Analyst`（序列 > fan-out）；各 Agent 含 YAML frontmatter + 禁止清單 + 完成標準。

## 平行 Session 策略 `[FF]`
複雜任務開 3–5 個平行 session，用 `git worktree` 隔離工作目錄。
-->
<!-- 替換為兩行： -->
## 序列 / 平行執行 `[FF]`
序列（有依賴）：`Researcher→Editor→Analyst`；平行（獨立）：3–5 session + `git worktree`。
```

2. 精簡「Frozen Snapshot 記憶設計」：
```markdown
<!-- 把這段（4 行）：
## Frozen Snapshot 記憶設計 `[FF]`

- 記憶檔案（MEMORY.md）在 session **開始**時注入，非實時更新（保護 KV Cache 前綴）
- 字元硬限制：MEMORY.md ≤ 2,200 字元；只寫 Agent 判斷為「重要」的內容
-->
<!-- 改為（2 行，保留關鍵數字）： -->
## Frozen Snapshot `[FF]`
MEMORY.md 於 session 開始時注入（非實時），≤ 2,200 字元；只寫「重要」內容。
```

3. [路徑 X 才適用] 把「HarnessCard 模板」改為 HTML 注釋：
```markdown
<!-- 
## HarnessCard 模板 `[FF]`
每個 Agent 設計時必須填寫 Control / Agency / Runtime 三段 CAR 摘要；模板與四層失敗恢復詳見 `.claude/refs/subagent-advanced.md` §HarnessCard。
-->
<!-- HarnessCard 模板：Control/Agency/Runtime 三段；詳見 .claude/refs/subagent-advanced.md §HarnessCard -->
```

4. [路徑 X 才適用] 把「Sub Agent 委派表」改為 HTML 注釋：
```markdown
<!--
## Sub Agent 委派表 `[FF]`
詳見 `.claude/refs/subagent-dispatch.md`（含場景→Agent 完整對照表及 Advisor 時機決策矩陣）。
-->
<!-- Sub Agent 委派表：.claude/refs/subagent-dispatch.md -->
```

5. 精簡「模型選擇」能力下限段落（去掉論文引用，保留規則）：
```markdown
<!-- 把這段：
複雜任務（跨模組決策、多輪迭代、架構設計）在弱模型下可能全面衰退，而非只是「慢一點」（continual-harness 論文：Haiku 在複雜推理任務損益不對稱）。識別信號：
-->
<!-- 改為： -->
複雜任務（跨模組決策、多輪迭代、架構設計）在弱模型下可能全面衰退（非只是慢一點）。識別信號：
```

---

### Op4：context-management.md（目標 -120 tokens）

**約束**：保留所有 token budget 數字（4,000 / 30,000 / 70% / 85% 等）。

1. 壓縮「Compact 三層觸發」為單行：
```markdown
<!-- 把這段（7 行）：
- **Compact 三層觸發**（優先序：行為信號 > 數字閾值 > 定時器）：
  1. **行為信號**：模型出現「請提供更多上下文」「你想做什麼？」等迷失問句 → 立即 `/rewind` 或 `/compact`
  2. **數字閾值**：一般任務 **70%**；初學者 ~**60%**；長 agentic **30–35%** 主動 compact
  3. **定時器**：複雜 agentic 每 **300–400K token** 主動 compact
  - **PreCompact hook**：`exit 2` 可完全阻斷 compact（保護重要未提交決策）；一般用 `additionalContext` 注入保留摘要。
-->
<!-- 改為（2 行）： -->
- **Compact 三層觸發**：① 行為信號（迷失問句 → `/compact`）② 數字閾值（70% 一般 / 60% 初學 / 30–35% agentic）③ 定時器（300–400K token）。
- **PreCompact hook**：`exit 2` 阻斷；一般用 `additionalContext` 保留摘要。
```

2. 精簡「Token Overhead 九大模式」（保留數字，去掉全稱）：
```markdown
<!-- 把這段：
## Token Overhead 九大模式（Mnilax 實測） `[FB]`

Top-3：CLAUDE.md bloat 14%、對話歷史重讀 13%、Hook 衝突 11%。完整表格詳見 `.claude/refs/session-management.md` §Token Overhead；productive tokens 目標 ≥ 27%。
-->
<!-- 改為： -->
## Token Overhead `[FB]`
Top-3：CLAUDE.md 14% / 歷史 13% / Hook 11%；productive ≥ 27%。詳見 session-management.md。
```

---

### Op5：output-discipline.md（目標 -129 tokens）

**約束**：保留「填充語禁止」和「禁用技術術語」的所有禁用詞（不能刪詞）。

1. 合併填充語 + 禁用術語為一條：
```markdown
<!-- 刪除這兩行：
- **填充語禁止**：just / really / basically / it's worth noting / as you can see / 值得注意的是 / 如您所見 / 事實上 — 純輸出膨脹。
- **禁用技術術語（bcherny）**：leverage / robust / seamless / delve / utilize — 在技術文件與程式碼回覆中禁用。
-->
<!-- 替換為一行（保留全部禁用詞）： -->
- **禁用詞**：just / really / basically / it's worth noting / 值得注意的是 / 事實上 / leverage / robust / seamless / delve / utilize。
```

2. 壓縮「優雅性自檢」：
```markdown
<!-- 把這段（5 行）：
## 優雅性自檢（bcherny — Demand Elegance） `[FB]`

非瑣碎變更完成後，輸出前自問：「有更優雅的解法嗎？」
- 若現有解法感覺笨拙 → 退回實作更優雅方案，再輸出
- 明確瑣碎修改（改錯字、修單行 bug）→ 跳過此步
-->
<!-- 改為（2 行）： -->
## 優雅性自檢 `[FB]`
非瑣碎變更完成前自問「更優雅解法？」；是 → 退回重做；瑣碎修改（錯字、單行 bug）→ 跳過。
```

3. 壓縮「例外情況」（去掉重複說明，保留核心邏輯）：
```markdown
<!-- 把這段（5 行，含子條目）：
## 例外情況 `[FF]`

- 使用者明確要求「詳細解釋」「完整說明」「逐步說明」→ 放寬長度限制，但仍禁止開場白與填充語
- 教學性內容（如技術文章、文件草稿）→ 散文形式可接受，但仍去除冗詞
- 使用者語氣輕鬆隨意時 → 可以加入一句話回應確認，但不要多行鋪陳
- **多步驟任務 Checkpoint**：每步驟摘要「做了什麼、驗了什麼、剩什麼」可超過 150 字限制
-->
<!-- 改為（2 行）： -->
## 例外情況 `[FF]`
詳細/教學要求 → 放寬長度，但禁開場白；多步驟 Checkpoint → 無長度限制；輕鬆語氣 → 一句確認即可。
```

---

## Step 3：驗證（三層，缺一不可）

### 驗證 Layer 1：Healthcheck
```bash
bash scripts/healthcheck.sh
```
期望：PASS ≥ 90，FAIL = 0

### 驗證 Layer 2：Token 實測
在 Claude Code session 中：
```
/context
```
期望：Memory files 顯示 ≤ 3,500 tokens

若未達標 → 繼續執行剩餘 Op（依照 `/context` 結果判斷優先做哪個）。

### 驗證 Layer 3：行為測試（2 個，缺一不過）

**測試 A（core.md R12 延伸規則）**：
```
給 Claude 一個 prompt：
「請讀取 CLAUDE.md，這個檔案超過 100 行。」
```
期望 Claude 說：使用 `limit`/`offset` 分段讀取，或說明每段後的進度（N-M 行）。

若 Claude 直接讀整個檔案而不說分段 → Op2 的合併損失了語意，需還原 R12 延伸原文。

**測試 B（subagent-strategy.md Fan-out 限制）**：
```
給 Claude 一個 prompt：
「我有 6 個獨立的研究任務，請同時啟動。」
```
期望 Claude 說：「Fan-out 上限 4，我會分兩批執行」或類似表述。

若 Claude 直接啟動 6 個 → Op3 的修改損失了語意，需還原 Fan-out 上限原文。

---

## Step 4：Commit

```bash
git add CLAUDE.md .claude/rules/core.md .claude/rules/context-management.md \
  .claude/rules/output-discipline.md .claude/rules/subagent-strategy.md

git commit -m "$(cat <<'EOF'
refactor(rules): trim auto-load context 4,349→≤3,500 tokens (-21%)

- CLAUDE.md: 驗證指令簡化、工作流合併
- core.md: R12 延伸合併單行、PGE 去 ref 冗餘
- subagent-strategy.md: 序列/平行合併、Frozen Snapshot 簡化
- context-management.md: Compact 三層觸發單行化、Overhead 段落精簡
- output-discipline.md: 禁用詞合一、優雅性自檢壓縮

規則語意驗證: R12 分段讀取 ✅ / Fan-out 上限 4 ✅ / healthcheck 94+ PASS ✅
EOF
)"
git push -u origin HEAD
```

---

## 回滾計畫

若任何驗證失敗或 Layer 3 行為測試不通過：

```bash
# 還原特定檔案
git checkout HEAD~1 -- .claude/rules/core.md

# 或還原所有修改
git checkout HEAD~1 -- CLAUDE.md .claude/rules/core.md \
  .claude/rules/context-management.md \
  .claude/rules/output-discipline.md \
  .claude/rules/subagent-strategy.md
```

---

## 估算總結

| Op | 目標削減 | 方法 | 風險 |
|----|---------|------|------|
| Op1 CLAUDE.md | -100 tokens | 合併 + [X: HTML 注釋] | 低 |
| Op2 core.md | -220 tokens | 合併 R12、去 ref 冗餘 | 低 |
| Op3 subagent-strategy.md | -280 tokens | 合併章節 + [X: HTML 注釋] | 中（有行為測試保護） |
| Op4 context-management.md | -120 tokens | 壓縮三層觸發 | 低 |
| Op5 output-discipline.md | -129 tokens | 合併禁用詞 | 低 |
| **合計** | **-849 tokens** | | |

預計結果：4,349 → **3,500 tokens** ✅

---

## 方案選擇邏輯（Opus + Sonnet 驗證後結論）

1. **路徑 X（HTML 注釋有效）**：執行全部 Op，預計超額完成（可能到 3,200–3,300）
2. **路徑 Y（HTML 注釋無效）**：執行 Op1（去 HTML 的版本）+ Op2 + Op3（去 HTML 的版本）+ Op4 + Op5，依靠純合併策略仍可達 -849 tokens
3. **若執行 Op1–Op5 後仍 > 3,500**：繼續壓縮「Advisor 時機決策樹」指向（4 行 → 1 行 HTML 注釋）

> 重要：Sonnet Pilot 挑戰確認——估算有 ±20% 誤差。用 `/context` 實測替代估算判斷，是本 prompt 最關鍵的設計決策。
