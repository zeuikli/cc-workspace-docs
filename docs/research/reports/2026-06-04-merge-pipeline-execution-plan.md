# 自我驗證的自主 Merge Pipeline — 可執行計劃書

> **配套研究**：`2026-06-04-merge-pipeline-research.md`
> **落點**：**新建 SKILL** `verified-merge`（三主題中唯一 greenfield；無既有覆蓋）
> **狀態**：研究+計劃完成，**APPLY 待 gated session 核准**（新建 SKILL + manifest 新檔，破壞性度低但須使用者確認落點）
> **Harness Loop**：OBSERVE→IDENTIFY→PROPOSE→TEST→APPLY→RECORD

---

## extend vs build 判定

**BUILD（新建）**。merge pipeline 在 codebase 無既有覆蓋：`quick-pr` / `quick-commit` / `deploy` SKILL 皆無 merge gate；healthcheck.sh 是被整合的 gate 非 pipeline 本身。不違 R2（非重複）。

---

## OBSERVE（現況，全機械驗證）

| 觀察項 | 證據 | 驗證指令 |
|--------|------|---------|
| healthcheck 可作 Gate 1 | exit 1 on FAIL>0 | `bash scripts/healthcheck.sh; echo $?` |
| removed-manifest 不存在 | 須新建 | `ls .claude/refs/removed-content-manifest.txt`（No such file） |
| core.md §R = 11 | re-fetch 斷言基準 | `grep -c "^## §R" .claude/rules/core.md` → 11 |
| 背景搶分支 5 次 | 根因威脅 | MEMORY Lesson 5/31f-A/6/03-B/6/04-A |

---

## IDENTIFY（缺口）

1. 無「merge 前 4 道 gate」的單一觸發點（現散在 healthcheck + 人工記憶）。
2. 無 removed-content manifest（R13 回歸無機械防護）。
3. 無 squash-merge 後 re-fetch 斷言（18,000-token 倒退無偵測）。

---

## PROPOSE（交付物）

### 交付 A：SKILL `.claude/skills/verified-merge/SKILL.md`
4 道 gate + re-fetch，格式對齊既有 quick-pr / deploy SKILL frontmatter。參數：`PR`（PR 號）、`EXPECT_BRANCH`、`CRITICAL_FILES`（re-fetch 驗證清單）。

### 交付 B：`.claude/refs/removed-content-manifest.txt`（新檔）
```
# slug<TAB>YYYY-MM-DD<TAB>reason
karpathy-principles	2026-05-XX	R13 已合併進 karpathy-mnilax-best-solution，孤兒檔刪除
SYNC-STATUS.md	2026-06-04	machine-local 自動生成檔，untrack（Lesson 2026-06-04-B）
```
（初始種子，APPLY 時與使用者確認實際 slug。）

### 交付 C：SKILL.md 內含 4 道 gate 的 bash（見研究報告 §2）

---

## TEST（APPLY 後驗收，全 bash 可驗）

| # | 驗收條件 | 指令 |
|---|---------|------|
| T1 | SKILL frontmatter 合法 | `bash scripts/healthcheck.sh` FAIL=0 |
| T2 | manifest grep 機制可運作 | 注入含 `karpathy-principles` 的假 diff → SKILL 回 BLOCKED |
| T3 | Gate 0 抓錯分支 | 在非 EXPECT_BRANCH 跑 → ABORT |
| T4 | re-fetch §R 斷言 | `git show origin/main:.claude/rules/core.md \| grep -c "^## §R"` → 11 |
| T5 | fail-loud | 任一 gate 失敗 → 非零 exit + 完整錯誤（非靜默） |

---

## Falsifiable Prediction

**改動**：新建 verified-merge SKILL + removed-content-manifest.txt（2 新檔，0 動 §R 條文 / 0 動 healthcheck.sh）。
**預測**：
1. healthcheck FAIL=0；
2. manifest 注入測試 → BLOCKED（T2）；
3. Gate 0 錯分支 → ABORT（T3）；
4. SKILL 不增 auto-load byte（SKILL 非 auto-load，on-demand 觸發）；
5. 既有 26 SKILL + 1 = 27，RESOLVER.md 同步登錄。
**驗證指令**：
```bash
bash scripts/healthcheck.sh | tail -1
ls .claude/skills/ | grep -v RESOLVER | wc -l   # 27
wc -c CLAUDE.md .claude/rules/{core,context-management,output-discipline,subagent-strategy}.md | tail -1  # 不變 18,455
```
**失敗判定**：任一不成立 → 誠實回報 REFUTED，不漂移。

---

## APPLY 順序（gated）

1. AskUserQuestion 確認 manifest 初始 slug 清單（不可自決刪除候選 — Lesson 5/31b grep 驗證引用鏈）。
2. Write SKILL.md + manifest。
3. RESOLVER.md 登錄（防孤兒 — Lesson 2026-06-04-E）。
4. 跑 T1-T5。
5. 原子 commit 區塊（`checkout → branch-show-current 守衛 → git commit -- <pathspec> → push`，Lesson 2026-06-04-A）。

---

## RECORD

APPLY 後 MEMORY 留 ≤3 行 session + 任何 lesson（Lesson 2026-06-04-F：研究類 PR 即使產物落 repo 仍須沉澱 MEMORY）。

---

## 下限約束（不可違）

- fail-open 鐵則：若有任何 hook 成分必 exit 0。
- merge 不可逆：gate 全在 merge 前。
- §R1-R12 條文 / 驗證指令一字不動（本 SKILL 不碰 auto-load）。
