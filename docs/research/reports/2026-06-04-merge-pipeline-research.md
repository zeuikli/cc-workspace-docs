# 自我驗證的自主 Merge Pipeline — 深度研究報告

> **日期**：2026-06-04
> **分支**：feature/insights-horizon-research
> **來源**：`/insights` On-the-Horizon 機會 #1
> **落點判定**：**新建 SKILL**（`.claude/skills/merge-guard/` 或 `.claude/commands/verified-merge`）——無既有覆蓋，是三主題中唯一真正 greenfield 的。
> **方法**：1 researcher sub-agent 深研 + 主對話機械 grep 重驗全部關鍵 verdict（subagent-strategy §Dynamic Workflow 鐵則）。

---

## 0. 問題陳述（接地一手證據）

把每次 git merge 當「有護欄的交易」：跑完整 test/healthcheck -> diff working tree 對照預期 -> grep removed-content manifest 防回歸 -> 才 `gh pr merge --squash`，失敗則 abort/stash/report，merge 後 re-fetch 驗證。

**真實痛點（MEMORY.md 一手記錄，非泛論）**：
- **背景搶分支已 5 次**（Lesson 5/31f-A / 6/03-B / 6/04-A），reflog 鐵證證明多 session 共用同一 working tree `/Users/zeuik/cc-workspace`。
- **PR #400 髒分支 checkout 誤 merge 錯內容**需 cleanup。
- **premature merge of failing tests**（insights friction「Self-Introduced Regressions」）。
- **18,000-token 版本倒退事件**：背景搶分支把整個 working tree 倒退回古老版本（insights fun_ending）。

---

## 1. 核心發現（8 點，全經機械重驗）

### F1 — 背景搶分支是 merge pipeline 的根因威脅
三次復發的共同根因：**多 session 共用同一 working tree**。git HEAD/index 是 repo 全域單例，非 per-process；任一 session `git checkout` 立刻改變所有人看到的分支。根因解已落地：`feature.sh wt-start <name>` 建獨立 worktree（git 物理拒絕同分支雙 checkout）。
**對 merge pipeline 的含義**：pipeline 必須在隔離 worktree 內執行，否則 `gh pr merge` 前的狀態斷言在中間 turn 可能被搶走而失效。
> 來源：MEMORY Lesson 5/31f-A / 6/03-B / 6/04-A / 6/04-B [HIGH，repo 一手 git reflog]

### F2 — PR #400 髒分支 merge = 未在 merge 前 assert 分支與 PR 目標一致
commit 期間背景 PR 自動 merge -> commit 直落 main（違 feature-branch 流程）。
**Gate 0 必須**：`git branch --show-current` 確認與 PR target 一致 + `git rev-parse HEAD` 與預期 sha 吻合，否則 abort。
> 來源：MEMORY Lesson 2026-05-31f-A [HIGH，repo 一手]

### F3 — healthcheck.sh 已是現成 merge gate，無需重寫
現有 `scripts/healthcheck.sh` 涵蓋：JSON 合法性、hooks `bash -n` 語法、frontmatter 完整性、CLAUDE.md 行數、@連結完整性、on-demand trigger 路徑驗證。結束碼 FAIL>0 -> exit 1。可直接作為 Gate 2 的機械性測試。
> 來源：親讀 `scripts/healthcheck.sh` L468-477 [HIGH]

### F4 — block-dangerous.sh 是 fail-loud 設計的對齊範本
block-dangerous 在危險時 exit 2（阻斷）、安全時 exit 0（放行）。merge pipeline 本身是**確定性腳本**（§R5），失敗 -> exit 1 + 完整錯誤輸出，不接受靜默通過（§R12 Fail Loud）。
> 來源：親讀 `.claude/hooks/block-dangerous.sh` L39-40 [HIGH]

### F5 — removed-content manifest 的真實案例 = R13 規則被刪後重被引入
insights friction 記載「reintroduced R13 rules」。trigger-index 4.0 精簡時 karpathy-principles（含 R13 Compounding 獨特內容）已刻意合併進 karpathy-mnilax-best-solution 後刪除。若未來 merge 重新引入該孤兒檔，等同 R13 回歸。
**防回歸**：維護「已刻意移除的 slug -> 移除日期 + 理由」manifest，merge 前 `grep` 驗證 diff 中無這些 slug。
**機械重驗**：`.claude/refs/removed-content-manifest.txt` 目前**不存在**（須隨 SKILL 新建）。
> 來源：insights friction + 主對話 grep 確認 manifest 不存在 [HIGH]

### F6 — GitHub merge queue 與 bors-ng 的共同原則：test-then-promote
bors 哲學：「test it first, then promote it」——PR 先合入 staging branch、跑完整 CI、才 copy 到 main。GitHub merge queue 同理：在 temporary merge group branch 重跑所有 required check，通過才推進 base branch。
**對應 workspace**：`gh pr merge --squash` 之前必須完成所有 gate，merge 後驗等於不驗（revert 成本遠高於 abort）。
> 來源：[bors.tech](https://bors.tech/) [HIGH，一手文件]；[GitHub Docs — managing a merge queue](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue) [HIGH，官方]；[InfoQ — GitHub merge queues](https://www.infoq.com/news/2024/03/github-merge-queues/) [MEDIUM，二手報導]

### F7 — squash merge 後的 re-fetch 驗證是防「18,000-token 倒退」的唯一機械手段
squash 把整個 PR 壓成 single commit，不能靠「branch HEAD = PR HEAD」驗 content。需 merge 後：`git fetch origin main && git show origin/main:<file> | wc -c` 對照預期 byte range，或 `git show origin/main:.claude/rules/core.md | grep -c "^## §R"` 驗條數不變（= 11）。
> 來源：MEMORY 5/31f-A 細節 + 主對話 grep 確認 core.md §R = 11 [HIGH]

### F8 — SKILL（手動觸發）非 hook（全自動）
AGENTS.md §5：「不可逆後果 -> hook（確定性 gate）；偶發行為偏差 -> CLAUDE.md rule」。但 merge 是**高成本、低頻、需確認**的動作，且共用 hook 必 fail-open（見下限約束），不適合全自動。SKILL 允許逐 gate 確認，符合 §R1「不可逆例外必顯示摘要 + 等待確認」。
> 來源：AGENTS.md §5 + MEMORY Lesson 2026-06-04-B [HIGH]

---

## 2. SKILL 設計骨架（4 道 Gate + Re-fetch）

```bash
# ============ Gate 0：分支與狀態斷言（防 PR #400） ============
git branch --show-current        # == 預期 feature branch
git rev-parse HEAD               # 記錄起始 sha
git status --porcelain           # 必須 clean
# 失敗 -> ABORT，不進後續 gate

# ============ Gate 1：test / healthcheck（不改 healthcheck.sh） ============
bash scripts/healthcheck.sh      # exit 1 -> ABORT + 完整輸出（§R12）

# ============ Gate 2：diff working tree 對照預期 ============
gh pr diff <PR>                          # PR 變更清單
git diff origin/main...HEAD --name-only  # 實際 changed files
# assert 檔案清單 = 計劃書 pathspec -> 不符 STASH + REPORT

# ============ Gate 3：removed-content manifest grep ============
while IFS=$'\t' read -r slug date reason _; do
  gh pr diff <PR> | grep -qF "$slug" && {
    echo "[merge-gate] BLOCKED: '$slug' reintroduced (removed $date: $reason)"; exit 1; }
done < .claude/refs/removed-content-manifest.txt

# ============ Merge + Re-fetch 驗證 ============
gh pr merge <PR> --squash
git fetch origin main
git show origin/main:.claude/rules/core.md | grep -c "^## §R"  # == 11
git show origin/main:CLAUDE.md | wc -c                          # 預期 byte 範圍
git log origin/main -1 --format="%s"                            # 含 PR 號（非倒退舊 sha）
```

---

## 3. 關鍵風險與下限約束

- **fail-open 鐵則**：任何被「所有 session + 背景自動化」共用的 hook 必 exit 0（branch-isolation-guard.sh L13-15）。-> **解法：做 SKILL 不做 hook**。
- **merge 不可逆**：所有 gate 必在 merge 之前（bors test-then-promote + §R1 不可逆例外）。
- **manifest 維護成本**：只記「刻意 DEFER/DELETE 的規則 slug」，不記所有刪除（否則每次 refactor 都要更新）。格式：一行一條，tab 分隔，slug 為可 grep 唯一字串。
- **§R12 Fail Loud + 截斷標示**：每 gate 失敗輸出完整錯誤，輸出 `[Checkpoint] Gate N: PASS/FAIL + 原因`。
- **§R10 Checkpoint**：Gate 2 STASH 後不得自動續跑。

---

## 4. Falsifiable Prediction 候選（全機械可驗）

1. `bash scripts/healthcheck.sh | tail -1` -> 含 `FAIL: 0`
2. `git show origin/main:.claude/rules/core.md | grep -c "^## §R"` -> `11`
3. `git show origin/main:CLAUDE.md | wc -c` -> merge 前 byte ± 容差內
4. `git log origin/main -1 --format="%s"` -> 含 PR 號
5. removed-manifest 逐行 grep -> 0 個 slug 出現在 merge diff

任一不成立 -> SKILL 輸出 `NO-MERGE` + 具體失敗項，不輸出「完成」。

---

## 5. 信度分層彙整

| 來源 | 關鍵聲明 | 信度 | URL |
|------|---------|------|-----|
| bors.tech | test-then-promote 哲學 | HIGH | https://bors.tech/ |
| GitHub Docs | merge queue 在 temp branch 重跑 required check | HIGH | https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue |
| InfoQ | GitHub.com merge queue 管理 30k PR + 4.5M CI | MEDIUM | https://www.infoq.com/news/2024/03/github-merge-queues/ |
| MEMORY.md | 5 次分支互搶 / R13 回歸 / fail-open | HIGH | repo 一手 git log + MEMORY |
| healthcheck.sh | exit code 語義 | HIGH | 親讀 L468-477 |
| 主對話 grep | manifest 不存在 / core.md §R=11 / healthcheck 0 引用 measure.sh | HIGH | 機械重驗 |
