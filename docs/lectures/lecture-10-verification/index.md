# Lecture 10：驗證迴圈與 Code Review

## 學習目標

完成本課後，你將能夠：

- 定義驗證迴圈，並把你反覆手動執行的檢查編碼成 Skill
- 選擇驗證 Skill 的四種部署形態（standalone / embedded / chained / PR-wide）
- 執行「Oracle 先驗」——在採信一個驗證器之前先確認它有區辨力
- 設計獨立 verifier，並說明它為什麼能把 false positive 砍半
- 設定 Code Review 與 `REVIEW.md`，控制 severity、nit 上限與 re-review 收斂

## 核心概念

### 定義

> **驗證迴圈** = agent 檢查自己的產出（跑測試、linter 或自訂檢查）並在往下走之前修好失敗項的**重複循環**。

重點在「自己閉環」。判準很簡單：**凡是你會反覆人工把關的事，都該編碼**。專案特定的確定性規則就是最好的素材——例如「拒絕會 drop column 但沒有 backfill 的 migration」。

### 2026-07 的重要轉向：觸發權回到 harness

兩件事同時發生，方向一致：

1. 官方推廣把驗證編碼成 Skill（《Building verification loops in Claude Code with skills》，2026-07-22）
2. 同時把自動觸發**關掉**：v2.1.215 起 Claude 不再自行跑 `/verify` 與 `/code-review`；v2.1.218 起 `/deep-research` 同樣改為手動

看似矛盾，其實是同一件事：**驗證什麼時候跑，是 harness 的決定，不是模型的判斷**。讓模型自己決定要不要驗證，正好落在它最有偏誤的地方。

**實務後果**：任何假設「模型會自己 review」的流程都已失效。驗證必須由**規則、hook 或 Skill 明確呼叫**。

### 內建驗證能力

| 機制 | 說明 |
|------|------|
| `/verify` skill | 內建驗證流程（**需手動呼叫**）|
| Toolchain 整合 | linter、type checker 直接由 agent 執行 |
| `/code-review` | PR 層級審查（**需手動呼叫**）|
| `/code-review ultra` | 雲端多 agent 深審；非互動 session 不再靜默降級 |
| GitHub Actions | CI 端自動化 |
| Spec validation / rubrics | Managed agents 的評分準則 |

### 四種部署形態

| 形態 | 時機 |
|------|------|
| **Standalone** | 跨切面檢查，刻意手動呼叫 |
| **Embedded** | 內嵌在產出型 Skill 裡，產完自動驗 |
| **Chained** | 一個 Skill 觸發另一個 |
| **PR-wide** | 團隊基礎建設，套用到所有變更 |

演進路徑是有方向的：**個人生產力工具（standalone）→ 鏈式自動化 → PR gate**，讓標準不再依賴個人自律。

### 為什麼 Generator 不能自評（再一次，這次有數字）

[Lecture 04](/lectures/lecture-04-harness-architecture/) 講過原則，這裡給量化證據。

《Using LLMs to secure source code》的六步驟漏洞掃描方法論：**Threat Modeling → Sandbox → Discovery → Verification → Triage → Patching**。關鍵設計是把 verification agent 與 discovery agent 分離，且 verifier 的 prompt 要求**反駁而非確認**：

| 做法 | 效果 |
|------|------|
| 驗證 agent 與 discovery agent 分離 | false positive 減少約 **50%** |
| 再要求提供 PoC 才算成立 | false positive **趨近於零** |

Anthropic 已用這套方法在開源軟體中揭露 **1,596 個漏洞**。

同一原則在別處反覆出現：

- **Anthropic 的 AI 原生 SDLC**：多個**窄焦點 agent 各持獨立 context 與偏誤**審同一個 PR，加上 SAST 與對自動核可的人工抽樣
- **Analytics agent**：加入 adversarial review sub-agent 準確率 +6%（代價 +32% 延遲）
- **Dynamic workflows**：六大模式中專門有一個叫 **Adversarial verification**
- **Human-agent teams**：Doer-Verifier harness（一個執行、一個驗證），信任建立後某工程團隊讓 agent 獨立處理 500 個 bug 修復

### Oracle 先驗：你的驗證器有區辨力嗎

這是最容易被跳過、但代價最高的一步。

> 用來判真偽的東西（test、checker、grep、baseline），**採信前先餵一組已知好 + 一組已知壞**，確認它能區辨。

一個永遠回傳「通過」的測試不會被發現，除非你餵它一個應該失敗的案例。這在 agent 場景特別危險，因為 agent 會**優先讓 gate 變綠**，而不是讓程式變對。

**Gate 選擇稽核**：gate 必須行使它宣稱涵蓋的實際執行路徑，不能是 proxy 子集：

```
type-check  ≠  build  ≠  跑得起來  ≠  行為正確
```

`mypy --strict` 通過不代表 import 得起來；build 成功不代表啟動得了；啟動得了不代表功能對。挑 gate 時要問：**這個 gate 真的走過我宣稱它保護的路徑嗎？**

### 裝完成的六種捷徑

Agent 在被 gate 卡住時會找出路。逐項審查這六種：

| 捷徑 | 長什麼樣 |
|------|---------|
| 放鬆測試 | 把 assert 改寬、把 strict 關掉 |
| 吞錯誤 | `try/except: pass`、`|| true` |
| Stub 回傳 | 函式直接 return 預期值 |
| 改測試檔配合實作 | 測試被改成符合現有錯誤行為 |
| 對給定輸入字面特判 | `if input == "test_case_1": return 42` |
| 縮小 gate 範圍 | 從跑全套改成只跑會過的那個檔案 |

**紅旗規則**：修復過程中**測試檔被修改**即為紅旗，需人工確認。修復的正確性要用**未見輸入**抽驗泛化，不能只看原本那個失敗案例變綠。

### 展示紀律：什麼時候該貼輸出

自報成功不算成功。但也不需要每一步都貼滿輸出：

| 階段 | 做法 |
|------|------|
| **中間輪** | 靜默——只給計數 / hash + 可重現的命令 |
| **終局** | 出示——貼出工具實際輸出的首尾節錄 |
| **失敗** | 大聲——完整貼出，不摘要、不美化 |

核心閘門是一句話：**宣告完成前親自跑確定性檢查，並展示工具的實際輸出**。口頭「已通過」不成立；subagent 回報「已完成」也不成立——child 的 verdict 不是證據，確定性 gate 由 parent 親跑。

### Code Review（多代理 PR 自動審查）

官方統計（Anthropic 內部驗證）：工程師程式碼產出成長 **200%**；獲得實質性 review comment 的 PR 比例 **16% → 54%**；誤報率 **< 1%**。

**運作流程**：

1. PR 開啟 / push / 手動觸發 → 啟動多個平行 agent
2. 每個 agent 分析 diff + 周邊程式碼，各負責不同類別的問題
3. **Verification pass**：對候選問題驗證實際程式碼行為，過濾誤報
4. 去重 + 按 severity 排序 → 發佈為 inline comments
5. 平均完成時間：**20 分鐘**

**Severity 三級**：

| 標記 | 等級 | 含義 |
|------|------|------|
| 🔴 | Important | merge 前應修復的 bug |
| 🟡 | Nit | 次要問題，值得修但不阻塞 |
| 🟣 | Pre-existing | 存在於 codebase 但非此 PR 引入 |

**三種觸發模式與成本**：`Once after PR creation`（每 PR 一次）、`After every push`（費用 × push 次數）、`Manual`（`@claude review` 才跑）。平均每次 review **$15–25**，按 token 計費、**不計入訂閱內含用量**。

### REVIEW.md：把 review 行為收斂到可用

`REVIEW.md` 放在 repo root，會被注入每個 review agent 的 system prompt **最高優先區塊**。它解決的是「review 太吵」這個實際問題：

| 可調整項 | 用途 |
|---------|------|
| Severity 重新定義 | 為你的 repo 定義什麼算 🔴 Important |
| **Nit 上限** | 每次 review 最多幾則 Nit |
| Skip 規則 | 排除 generated code、lockfile、vendored 依賴 |
| Repo 專屬檢查 | 「所有新 API route 必須有 integration test」 |
| **Verification bar** | 要求附 `file:line` 引用才能發佈某類 finding |
| **Re-review 收斂** | 「第一次 review 後只報 Important」防止 style 打 7 輪 |
| Summary 格式 | 「先寫 '2 factual, 4 style' 摘要行再展開」 |

**兩個硬限制**：內容是**逐字貼入**，`@` import 語法**不展開**；規則必須直接寫在檔案裡。

### 別把 CI 已經做的事再做一次

最常見的浪費是讓 review agent 報 lint / formatting / type error——CI 已經擋掉了，重報只是噪音。`REVIEW.md` 的 `Do not report` 段落就是為此存在。

## 程式碼範例

### 一個驗證 Skill

```markdown
---
name: verifying-api-changes
description: |
  驗證 API 層變更符合本專案的契約規則。
  Use after modifying anything under src/api/, or before opening a PR that touches routes.
  Do NOT use for: 前端元件、資料庫 migration（用 reviewing-migrations）、純文件變更。
allowed-tools: Read, Grep, Glob, Bash
---

# API 變更驗證

## 執行順序（失敗就修，修完回到步驟 1 重跑）

1. `pytest tests/api/ -q`
2. `python -m mypy src/api/ --strict`
3. `python scripts/check_openapi_sync.py` — 確認 route 與 OpenAPI spec 一致
4. 對每個**新增**的 route，確認存在對應的 integration test（`tests/integration/`）
5. `grep -rn "print(" src/api/` 應為空——log 一律走 `src/utils/log.py`

## 通過標準

上述 5 項**全部**通過才算完成。任一失敗 → 修正 → **從步驟 1 重跑**，不要只重跑失敗那項。

## Known Gotchas

- `check_openapi_sync.py` 對 `response_model=None` 的 route 會誤判為缺 schema。
  這是已知限制，遇到時在 PR 描述中註明，不要改腳本繞過。
```

注意最後一句——**明確禁止繞過**，而且給了替代做法。沒有這句，agent 遇到誤判時最可能的行為就是改腳本。

### 獨立 verifier subagent

```markdown
---
name: adversarial-verifier
description: |
  對一項聲稱已完成的工作做反駁性驗證。
  Use when a subagent or the main thread reports a task as done and the result matters.
  Do NOT use for: 產生程式碼、修復問題（你只驗證，不動手）。
model: opus
allowed-tools: Read, Grep, Glob, Bash
---

你的任務是**證明這項工作沒有完成**。預設立場是「它壞了，我還沒找到證據而已」。

## 規則

- 你**不修改任何檔案**。發現問題就回報，不要順手修。
- 你只回兩種結果：
  - `PASS`
  - `FAIL: <證據>`——證據必須是工具輸出、file:line 或可重現的命令，不能是推論。
- 不確定時回 `FAIL`。模糊的通過比明確的失敗傷害更大。

## 必查

1. 測試檔在這次變更中被修改了嗎？（`git diff --name-only` 找 `test_`）如果有，這是紅旗，先說明。
2. 有沒有 stub 回傳、寫死的特判、被吞掉的例外？
3. 拿一組**原任務沒提到**的輸入試一次，行為對嗎？
4. 宣稱跑過的命令，你自己跑一次，輸出一致嗎？
```

### Oracle 先驗：確認你的 gate 有區辨力

```bash
# 在採信這個 checker 之前，先確認它會對「已知壞」報錯
cp db/migrations/0042_ok.py /tmp/known_good.py
cp fixtures/bad_migration.py /tmp/known_bad.py

python scripts/check_backfill.py /tmp/known_good.py   # 預期 exit 0
python scripts/check_backfill.py /tmp/known_bad.py    # 預期 exit != 0
```

兩個都通過才代表這個 checker 能用。只跑 known_good 通過，等於什麼都沒驗。

### PreToolUse hook：阻止改測試檔

```bash
#!/bin/bash
# .claude/hooks/protect-tests.sh
# 修復期間動測試檔是最常見的作弊路徑，這裡改成需要明確意圖
set -euo pipefail

INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name')
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // .tool_input.path // empty')

if [[ "$TOOL_NAME" =~ ^(Write|Edit)$ ]] && [[ "$FILE_PATH" =~ (^|/)tests?/ ]]; then
  echo "BLOCKED: 修改測試檔需要明確意圖。" >&2
  echo "若這次任務本來就是「補測試」，請在 prompt 中說明，並改用 /subtask 由 test-writer 執行。" >&2
  echo "若你是為了讓失敗的測試變綠而修改它——那是紅旗，請改修實作。" >&2
  exit 2
fi
exit 0
```

### REVIEW.md 範例

```markdown
# Review instructions

## What Important means here

Reserve Important for findings that would break behavior, leak data, or block a
rollback: incorrect logic, unscoped database queries, PII in logs or error
messages, and migrations that aren't backward compatible. Style, naming, and
refactoring suggestions are Nit at most.

## Cap the nits

Report at most five Nits per review. If you found more, say "plus N similar
items" in the summary instead of posting them inline. If everything you found is
a Nit, lead the summary with "No blocking issues."

## Do not report

- Anything CI already enforces: lint, formatting, type errors
- Generated files under `src/gen/` and any `*.lock` file
- Test-only code that intentionally violates production rules

## Always check

- New API routes have an integration test
- Log lines don't include email addresses, user IDs, or request bodies
- Database queries are scoped to the caller's tenant

## Re-review

After the first review on a PR, report only Important findings. Do not re-post
Nits that were already raised.
```

### 用 check run 自建 merge gate

Code Review 的 check run 結論**永遠是 neutral**，不會擋 merge。要當成 branch protection 用，得自己解析：

```bash
gh api repos/OWNER/REPO/check-runs/CHECK_RUN_ID \
  --jq '.output.text | split("bughunter-severity: ")[1] | split(" -->")[0] | fromjson'
# → {"normal": 2, "nit": 1, "pre_existing": 0}
#   "normal" = Important findings 數量

# 在 CI 裡當 gate
[ "$(... | jq '.normal')" -eq 0 ] || { echo "有未解決的 Important finding"; exit 1; }
```

### 非互動式深審（CI 用）

```bash
claude ultrareview            # 結構化輸出
claude ultrareview --json     # 原始 JSON
# exit 0 成功，exit 1 失敗
```

## 常見問題與注意事項

**Q：`/verify` 不會自己跑了，那我要在哪裡呼叫它？**

A：三個位置擇一或並用：① 在你的產出型 Skill 結尾嵌一步「呼叫驗證 Skill」（embedded）；② `Stop` 或 `PostToolUse` hook 觸發確定性檢查；③ CLAUDE.md 的完成定義裡寫明「宣告完成前必須跑 `<逐字命令>` 並貼出輸出」。**不要**留給模型自己想起來。

**Q：`@claude review` 在 draft PR 不觸發？**

A：對，除非該 repo 設為 Manual 模式並手動指定。另外 GitHub Checks tab 的 **Re-run 按鈕無效**，重觸必須用 comment 指令。

**Q：REVIEW.md 可以 `@import` 拆檔嗎？**

A：不行。內容逐字貼入，`@` 語法不展開。規則必須直接寫在 `REVIEW.md` 裡。

**Q：review 明明說有 finding，但看不到 inline comment？**

A：三個地方找：Check run 的 Details（完整 finding 表格，即使 inline comment 被 GitHub 拒絕也在）、Files changed tab 的 annotations、review body 的「Additional findings」（review 進行中 push 導致行號失效的那些）。

**Q：verifier 用同一個模型可以嗎？**

A：可以，但要是**異 instance**（不同 session / subagent），且 prompt 要求反駁而非確認。同一個 session 裡叫它「批判性地檢查一下」是最不可靠的形態——它已經有「這樣是對的」的 prior。

**Q：驗證的成本會不會太高？**

A：會，而且要正視。Analytics agent 加 adversarial review 是 +6% 準確率 / +32% 延遲。做法是**按風險分配**：不可逆操作、安全相關、跨模組變更值得付；改個 typo 不值得。但**廉價的確定性檢查（lint、type check、跑測試）任何檔位都不該跳過**。

**Q：Datadog 的做法值得學嗎？**

A：值得知道它存在。Temper 的思路是 agent **不產出應用程式碼，只產出精確規格**，由確定性 kernel 用符號推理、窮舉狀態探索與 property testing 驗證後才執行。這是「判斷交給模型、決定交給程序」推到極致的形態。多數專案不需要走這麼遠，但它示範了驗證可以往哪個方向強化。

## 本課小結

- **驗證迴圈 = agent 自己閉環**：跑檢查 → 修失敗 → 重跑 → 通過才往下。素材是你反覆手動把關的專案特定確定性規則。
- **觸發權在 harness，不在模型**。`/verify`、`/code-review`、`/deep-research` 都已改為手動呼叫——驗證必須由規則、hook 或 Skill 明確發動。
- **獨立 verifier 把 false positive 砍半**，要求 PoC 後趨近於零。verifier 不動手修、只回 PASS / `FAIL: 證據`。
- **Oracle 先驗**：採信一個 gate 之前，先餵已知好 + 已知壞確認它有區辨力。type-check ≠ build ≠ 跑得起來。
- **六種裝完成捷徑**要逐項審查；**測試檔被改即紅旗**；修復要用未見輸入抽驗泛化。
- **展示紀律**：中間輪靜默、終局出示、失敗大聲。child 的 verdict 不是證據，確定性 gate parent 親跑。
- **REVIEW.md 是讓 Code Review 可用的關鍵**：定義 severity、限制 nit 數量、排除 CI 已擋的項目、收斂 re-review。

## 延伸閱讀

- [Lecture 04：Harness 三層架構](/lectures/lecture-04-harness-architecture/) — Evaluator 獨立性的原理與 Hooks
- [Lecture 07：Skills 設計](/lectures/lecture-07-skills/) — 把驗證寫成 Skill 的格式
- [Lecture 08：Sub-agents 與 Dynamic Workflows](/lectures/lecture-08-subagents-workflows/) — Adversarial verification 模式
- [Lecture 12：組織治理與 AI 原生工程](/lectures/lecture-12-governance/) — 把驗證推到 PR-wide

**官方一手來源**

- [Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills)（2026-07-22）
- [Using LLMs to secure source code](https://claude.com/blog/using-llms-to-secure-source-code)（2026-05-27）— 六步驟方法論、false positive −50%
- [Bringing Code Review to Claude Code](https://claude.com/blog/code-review)（2026-03-09）
- [How Anthropic secures its AI-native software development lifecycle](https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle)（2026-07-21）
- [How Datadog built a "universal machine tool" for Claude Code](https://claude.com/blog/how-datadog-built-a-universal-machine-tool-for-claude-code)（2026-07-21）
- [Building effective human-agent teams](https://claude.com/blog/building-effective-human-agent-teams)（2026-06-24）— Doer-Verifier harness
- [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)（2026-03-24）
- [官方文件：Code Review](https://code.claude.com/docs/en/code-review)

**站內研究歸檔**

- [用 Skill 建構驗證迴圈](/research/best-practices/47-verification-loops-skills)
- [Code Review 多代理 PR 自動審查完整指南](/research/best-practices/22-code-review)
- [Claude Code 最佳實踐官方總綱](/research/best-practices/17-best-practices-overview)
