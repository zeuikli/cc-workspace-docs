# 用 Skill 建構驗證迴圈（Verification Loops）

> 來源：[Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills)（2026-07-22）
> 整理日期：2026-08-04

---

## 定義

> 驗證迴圈 = agent 檢查自己的產出（跑測試、linter 或自訂檢查）並在往下走之前修好失敗項的**重複循環**。

重點在「自己閉環」：把你**反覆手動執行**的品質檢查編碼成 Skill，Claude 就能在無人介入下迭代。

---

## 內建驗證能力

| 機制 | 說明 |
|------|------|
| `/verify` skill | 內建驗證流程（v2.1.215 起**不再由 Claude 自行觸發**，需手動呼叫）|
| Toolchain 整合 | linter、type checker 直接由 agent 執行 |
| Code Review | PR 層級審查（`/code-review`，v2.1.215 起同樣改為手動呼叫）|
| GitHub Actions | CI 端自動化 |
| Spec validation / rubrics | Managed agents 的評分準則 |

---

## 自訂驗證 Skill 的寫法

1. 最快路徑：用 `skill-creator` plugin 產生骨架。
2. 手寫：在 `.claude/skills/` 放 markdown，frontmatter 給 `name` / `description` / `allowed-tools`，正文用**白話的程序描述**（不是程式碼）。
3. 判準：**專案特定的確定性規則**就是驗證迴圈的素材——例如「拒絕會 drop column 但沒有 backfill 的 migration」。凡是你會反覆人工把關的事，都該編碼。

---

## 四種部署形態

| 形態 | 時機 |
|------|------|
| **Standalone** | 跨切面檢查，刻意手動呼叫 |
| **Embedded** | 內嵌在產出型 Skill 裡，產完自動驗 |
| **Chained** | 一個 Skill 觸發另一個 |
| **PR-wide** | 團隊基礎建設，套用到所有變更 |

演進路徑：個人生產力工具（standalone）→ 鏈式自動化 → PR gate，讓標準不再依賴個人自律。

---

## 與本 workspace 的關係

- `core.md` §TEST 的 `unverified_success` 閘門與「Oracle 先驗」是同一件事的更嚴格版本：官方講「自己檢查自己」，本 workspace 額外要求 **verifier 為異 instance、只回 PASS/FAIL、不得動手修**，且**確定性 gate 由 parent 親跑**。
- `review-hub` / `security-reviewer` / `.githooks/pre-commit` 即本 workspace 的 standalone 與 PR-wide 形態。
- 官方新增的「Claude 不再自行呼叫 `/verify`、`/code-review`」（v2.1.215）意味著**驗證的觸發責任回到 harness**——本 workspace 的 SKILL 與 hook 需明確呼叫，不能假設模型自動跑。

---

## 延伸閱讀

- `06-agent-skills-best-practices.md` — Skill 撰寫原則
- `22-code-review.md` — 多代理 PR 審查
- `48-w28-w31-features.md` — v2.1.215 / v2.1.218 對 `/verify`、`/code-review`、`/deep-research` 自動觸發的收斂
