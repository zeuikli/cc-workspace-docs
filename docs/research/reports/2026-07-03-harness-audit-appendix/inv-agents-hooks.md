# 稽核：.claude/agents · .claude/hooks · settings.json · .claude/commands

## 1. Agents frontmatter 一致性（13 檔，非題述 14；INDEX.md 明寫「共 13 個」與實檔一致）

- 全部 13 檔 `model:` 欄位一律用 alias（`haiku`/`sonnet`/`opus`），**無任何寫死版本 id**（如 `claude-3-5-sonnet-20241022`）— 乾淨。
  - 對照：`.claude/settings.json:4` `"model": "claude-sonnet-4-6"` 是**具體版本 id**（非 alias），與 agents 慣例不同調——非錯誤但值得注意：settings.json 頂層 model 綁死版本號，模型世代升級時需手動改此檔（agents 用 alias 則由 harness 自動解析新版本）。
- description 內 "Do NOT use for" 交叉引用檢查：`researcher.md` ↔ `quick-code-reviewer.md` ↔ `reviewer.md` ↔ `security-reviewer.md` ↔ `security-auditor.md` ↔ `test-writer.md` ↔ `doc-writer.md` ↔ `implementer.md` ↔ `haiku-implementer.md` ↔ `multi-mode-agent.md` 全部形成雙向排斥描述，一致。
- `.claude/agents/INDEX.md` 速查表 13 列與實際 13 檔一一對應，用途/model/禁止欄位與各檔 frontmatter description 相符，未見過時或矛盾條目。

### Agent × Skill 職責重疊（同觸發詞兩邊搶）
- **無明顯字面重疊**：agents 觸發詞多為中文動詞句（「幫我實作」「做安全審查」），skills 觸發詞為 `/slash-command` 或英文 keyword（`harness-meta:audit` 等），命名空間分離。
- 唯一交界案例：`memory-compactor`——`.claude/agents/memory-compactor.md`（實際壓縮執行者）+ `.claude/commands/memory-compactor.md`（orchestration wrapper，呼叫 agent）。**非重複，是設計上的 command→agent 轉發**（command 負責行數檢查+驗證+commit，agent 負責純壓縮邏輯）。
- `dreaming-consolidator` skill、`pilot-review` skill、`handoff` skill、`harness-meta` skill 皆在文件中「提及」memory-compactor（作為委派對象），非各自重複實作同功能——屬正常交叉引用。

## 2. Hooks 佈線驗證（settings.json ↔ .claude/hooks/*.sh）

- **21 個 `.sh` 腳本（不含 `lib/common.sh`）全數在 settings.json 中被引用，且 `test -x` 全部 PASS**（無孤兒、無死佈線）。
- `diff` 结果为空（wired set == actual file set 完全相等）。
- `.claude/hooks/INDEX.md` 宣稱「共 22 個 hook 腳本」= 21 個事件腳本 + `lib/common.sh`，數字正確。
- README 宣稱「18 個 settings.json 設定群組」— **實測為 17 個 matcher 群組**（SessionStart 1 + UserPromptSubmit 1 + PreToolUse 4 + PostToolUseFailure 1 + PostToolUse 5 + PreCompact 1 + PostCompact 1 + Stop 1 + SessionEnd 1 + PermissionRequest 1 = 17）。**輕微計數漂移（18 vs 17），非阻斷性但建議下次同步時修正**（`.claude/hooks/INDEX.md` 開頭 summary 行）。

## 3. Hook scripts 快速健檢

- **無寫死模型名版本**（`grep -nE "claude-(3|opus|sonnet|haiku)-[0-9]"` 全部 hooks 無命中）。
- **無寫死絕對路徑**（`/Users/xxx` 硬編碼）；全用 `$CLAUDE_PROJECT_DIR` / `$HOME` / `git rev-parse --show-toplevel` fallback。乾淨。
- **重型 hook（每次 UserPromptSubmit / 每次 Bash 都跑）**：
  - `user-prompt-submit.sh`（192 行，UserPromptSubmit matcher `""` = 每個 prompt 都跑，timeout 30s）：內含 **3 次 `python3` subprocess spawn** + 2 次 `git log`/`git rev-list` 呼叫（讀 MEMORY.md commit 距離）+ 1 次讀 cost-log。單次開銷估 100–300ms（3× python cold start + 2× git subprocess），**session 長跑時累積成本最高的 hook**。
  - `tool-log.sh`（每次 Bash PostToolUse + PostToolUseFailure 都跑，async + timeout 5s）：async 執行不阻塞主線程，但仍 fork python3；因為每次 Bash 呼叫觸發，次數最多。
  - `monitor-reminder.sh`（每次 Bash 都跑，PostToolUse，timeout 5s，非 async）：**3 次 python3 subprocess**（`echo | python3 -c` × 3）在同步路徑上，是目前**唯一每次 Bash 都同步阻塞執行且含多重 python spawn 的 hook**——若 Bash 呼叫頻繁（agentic session 常見），此 hook 為主要延遲來源候選。
  - `memory-pr-record-gh.sh`（每次 Bash 都掛，async，timeout 90s）：async 不阻塞，但每次 Bash（非僅 `gh pr create`）都觸發一次 script 啟動判斷，屬佈線寬鬆（matcher 是 `Bash` 而非 `Bash(gh pr create*)`），建議未來收斂 matcher 範圍以減少無謂 fork。

## 4. Commands vs Skills 重複 + README 同步

- `.claude/commands/` 實際：`autoresearch/`（子目錄，10 個子命令）+ 5 個 `.md`（`grill` `memory-compactor` `plan` `quick-commit` `quick-pr`）+ `README.md`。README 表列 6 行（`autoresearch/` 算 1 項）= 與題述「7 項」（含 README 自身或算法不同）**基本同步**，內容與實際檔案一致，無缺漏無多餘。
- `memory-compactor`：commands 版是 orchestration wrapper（呼叫 agent 執行壓縮），agents 版是實際執行者——**非重複，職責分工正確**（見上方 §1）。
- `.claude/skills/` 中無獨立 `memory-compactor` skill 目錄；`RESOLVER.md`／`pilot-review`／`handoff`／`harness-meta`／`dreaming-consolidator` 僅「引用」memory-compactor 作委派對象，非重複實作。

## 5. INDEX.md 同步性

- `.claude/agents/INDEX.md`：宣稱「共 13 個 specialist agents」，實際 `ls .claude/agents/*.md`（扣除 INDEX.md 自身）= 13 檔，**完全同步**，速查表逐列核對用途/model/禁止欄位皆與各 agent frontmatter 一致。
- `scripts/INDEX.md`：宣稱「51 個自動化腳本」，`find scripts -type f \( -name "*.sh" -o -name "*.py" \)` 實測 = **51，完全同步**（`Updated: 2026-07-01`，且 `scripts/sync-workspace.sh` §13b 有自動同步機制維護此計數）。

## 綜合建議（僅供 record，非本次委派修改範圍）
1. `.claude/hooks/INDEX.md` 開頭「18 個 settings.json 設定群組」→ 應更正為 17（1 行數字漂移）。
2. `memory-pr-record-gh.sh` 的 PostToolUse matcher 目前綁 `Bash`（全量），可收斂為更精確 pattern 降低無謂 fork 次數。
3. `monitor-reminder.sh` 同步執行 3 次 python3 spawn，為目前每次 Bash 呼叫的主要延遲熱點，若後續要做 hook 效能優化可從此下手（非本次任務範圍，僅記錄觀察）。
