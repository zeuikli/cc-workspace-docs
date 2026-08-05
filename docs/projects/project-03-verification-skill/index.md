# Project 03：把驗證編碼成 Skill

## 專案說明

Project 02 的 Evaluator 是一支 shell 腳本——它有效，但綁在一個專案裡、只有你知道怎麼用、而且需要你記得去跑。

本專案把它升級成 **Skill**：Claude 能自己在對的時機呼叫、能跨專案重用、能被團隊安裝。你也會實際跑一次評估驅動的迭代，而不是憑感覺調整措辭。

**完成後的成果**：

- 一個通過評估的驗證 Skill（含 Progressive Disclosure 結構）
- 3 個以上的評估場景與 baseline 對照
- 一份用 Claude A / Claude B 方法產出的迭代記錄
- 從 standalone 到 PR-wide 的部署路徑規劃

## 前置條件

- [Lecture 07：Skills 設計與 Progressive Disclosure](/lectures/lecture-07-skills/)
- [Lecture 10：驗證迴圈與 Code Review](/lectures/lecture-10-verification/)
- [Project 02：設計你的 Harness](/projects/project-02-harness-design/)（本專案改造它的 Evaluator）

## 任務清單

### 階段一：找出素材

判準是「**凡是你會反覆人工把關的事**」。不要憑空發明一個 Skill。

- [ ] **任務 1.1**：翻過去兩週的 PR review 意見與你對 Claude 的修正，列出**重複出現 ≥2 次**的把關項目
- [ ] **任務 1.2**：從中挑出**專案特定的確定性規則**——能寫成「符合／不符合」的那種。例：「拒絕會 drop column 但沒有 backfill 的 migration」、「新 API route 必須有 integration test」
- [ ] **任務 1.3**：用九大類別替它分類（Product Verification / Code Quality / CI-CD / Runbooks…）。**落不進任何一類就換一個題目**——那通常表示它該是 CLAUDE.md 的一行
- [ ] **任務 1.4**：確認它不是「Claude 預設就會做的事」。寫一句話說明：沒有這個 Skill 時，Claude 具體會漏掉什麼

### 階段二：先建評估，再寫文件

順序不能反。先寫 Skill 再補測試，會讓你只驗證自己想像中的問題。

- [ ] **任務 2.1**：建立 `evals/` 目錄與 3 個場景檔，**至少包含**：
  - 1 個**已知好**（應該通過）
  - 1 個**已知壞**（應該被抓到）
  - 1 個**邊界**（你自己也要想一下的那種）
- [ ] **任務 2.2**：每個場景寫明 `expected_behavior`——具體到「指出第幾行」「提出哪個替代方案」，不要寫「正確處理」
- [ ] **任務 2.3**：**建立 baseline**：在**沒有** Skill 的情況下跑這 3 個場景，記錄 Claude 的實際行為
- [ ] **任務 2.4**：確認 baseline 真的會失敗。如果沒有 Skill 也全過，這個 Skill 不需要存在——回到階段一

### 階段三：寫最少的文件通過測試

- [ ] **任務 3.1**：建立 `.claude/skills/<name>/SKILL.md`，frontmatter 至少含 `name` / `description` / `allowed-tools`
- [ ] **任務 3.2**：`description` 寫三件事：**做什麼 + 何時用 + 何時不用**（`Do NOT use for:`）。第三人稱，≤1,024 字元
- [ ] **任務 3.3**：名稱用動名詞形式（`verifying-api-changes`、`reviewing-migrations`），避免 `helper` / `utils`
- [ ] **任務 3.4**：依脆弱度校準自由度：
  - 窄橋（DB migration、破壞性操作）→ 精確步驟，明確禁止修改命令
  - 開闊平原（code review、分析）→ 給方向即可
- [ ] **任務 3.5**：規則寫**原因**不寫命令。「Use constructor injection. Field injection breaks testability because…」勝過「MUST use constructor injection」
- [ ] **任務 3.6**：加一個 checklist 區塊，讓 Claude 逐步勾選——明確步驟能防止它跳過關鍵驗證
- [ ] **任務 3.7**：寫回饋迴圈：**驗證失敗 → 修正 → 回到第一步重跑**，通過才繼續。不要只重跑失敗那一項

### 階段四：Claude A / Claude B 迭代

- [ ] **任務 4.1**：**Claude A**（有完整脈絡的當前 session）：請它把你剛才自然提供的脈絡打包進 Skill
- [ ] **任務 4.2**：請 Claude A **刪掉「Claude 本來就知道」的部分**。這一步通常能砍掉三分之一
- [ ] **任務 4.3**：**Claude B**（全新 session + 該 Skill）：跑 3 個評估場景的真實版本
- [ ] **任務 4.4**：觀察 Claude B 如何導航 Skill，記錄四個訊號：
  | 觀察到 | 意義 |
  |--------|------|
  | 意外的探索路徑 | 結構不直覺 |
  | 遺漏某個 reference 連結 | 連結不夠明顯 |
  | 反覆讀同一個檔案 | 該內容應移進主 SKILL.md |
  | 某檔案從未被讀取 | 可能不必要 |
- [ ] **任務 4.5**：帶著觀察回到 Claude A 迭代，重跑評估。**記錄每一輪的通過數**
- [ ] **任務 4.6**：至少跨兩個檔位測一次（例如 Sonnet 與 Opus）——同一份 Skill 對不同檔位的指引需求不同

### 階段五：Progressive Disclosure

- [ ] **任務 5.1**：量 SKILL.md 行數。< 300 行維持單檔；300–500 開始識別可拆的 reference；**> 500 必須拆**
- [ ] **任務 5.2**：拆分時 SKILL.md 只留 TOC + 核心流程，細節進獨立檔案
- [ ] **任務 5.3**：**確認參考鏈只有一層深**。`SKILL.md → advanced.md（直接有資訊）` 可以；再往下一層不行
- [ ] **任務 5.4**：超過 100 行的 reference 檔案頂部加 TOC
- [ ] **任務 5.5**：把重複邏輯移進 `scripts/`——腳本**只有輸出進 context**，內容不進，這是最省 context 的做法
- [ ] **任務 5.6**：腳本要**解決問題而不是推回給 Claude**：明確處理錯誤、不留魔法數字、錯誤訊息具體到可以直接修

### 階段六：選定部署形態

- [ ] **任務 6.1**：從四種形態中選一個起點：
  | 形態 | 時機 |
  |------|------|
  | Standalone | 跨切面檢查，刻意手動呼叫 |
  | Embedded | 內嵌在產出型 Skill 裡，產完自動驗 |
  | Chained | 一個 Skill 觸發另一個 |
  | PR-wide | 團隊基礎建設，套用到所有變更 |
- [ ] **任務 6.2**：**確保它真的會被觸發**。v2.1.215 起 Claude 不再自行跑 `/verify` 與 `/code-review`——三個掛載點擇一或並用：
  - 在產出型 Skill 結尾嵌一步呼叫
  - `Stop` 或 `PostToolUse` hook
  - CLAUDE.md 的完成定義寫明「宣告完成前必須跑 `<逐字命令>` 並貼出輸出」
- [ ] **任務 6.3**：規劃演進路徑：個人工具 → 鏈式自動化 → PR gate。寫下你打算什麼時候推進到下一階
- [ ] **任務 6.4**：（選）建立 `REVIEW.md`，定義 severity、nit 上限、排除 CI 已擋的項目、re-review 收斂規則
- [ ] **任務 6.5**：用 `PreToolUse` hook 記錄這個 Skill 的呼叫次數——三個月後你會需要知道它有沒有人用

## 參考實作

### 目錄結構

```
.claude/skills/verifying-api-changes/
├── SKILL.md              ← 入口，≤500 行
├── CONTRACTS.md          ← 完整契約規則（需要時才讀）
├── scripts/
│   ├── check_openapi_sync.py
│   └── check_route_tests.py
└── ../../../evals/
    ├── case-01-known-good.json
    ├── case-02-known-bad.json
    └── case-03-boundary.json
```

### SKILL.md 骨架

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

當前分支：`!git branch --show-current`
變更的檔案：`!git diff --name-only main -- src/api/`

## 執行順序（失敗就修，修完回到步驟 1 重跑）

複製此 checklist 並逐步勾選：

- [ ] Step 1：`pytest tests/api/ -q`
- [ ] Step 2：`python -m mypy src/api/ --strict`
- [ ] Step 3：`python scripts/check_openapi_sync.py`
- [ ] Step 4：每個新增 route 都有 `tests/integration/` 下的對應測試
- [ ] Step 5：`grep -rn "print(" src/api/` 應為空

## 通過標準

5 項全過才算完成。任一失敗 → 修正 → **從 Step 1 重跑**。

## Rules

- 新欄位一律 nullable 或有 default。
  原因：非同步部署期間舊版程式碼仍在寫入，NOT NULL 會讓舊版寫入全部失敗。
- log 一律走 `src/utils/log.py`。
  原因：`print()` 不會經過 PII 過濾，2026-04 曾把 email 寫進 stdout。

## Known Gotchas

- `check_openapi_sync.py` 對 `response_model=None` 的 route 會誤判為缺 schema。
  這是已知限制——遇到時在 PR 描述中註明，**不要改腳本繞過**。
- 契約規則全文見 [CONTRACTS.md](CONTRACTS.md)。
```

### 評估場景檔

```json
{
  "skills": ["verifying-api-changes"],
  "query": "I added POST /api/v2/exports. Verify the change.",
  "files": ["src/api/handlers/exports.py"],
  "expected_behavior": [
    "Runs pytest tests/api/ and reports the actual output",
    "Flags the missing integration test under tests/integration/ by name",
    "Does NOT claim the change is fine without running check_openapi_sync.py"
  ]
}
```

`expected_behavior` 的第三條特別重要——它檢查的是**沒有發生**的事。只驗證正向行為的 eval 抓不到「跳過驗證但宣稱通過」。

### 迭代記錄模板

```markdown
# verifying-api-changes 迭代記錄

## Baseline（無 Skill，2026-08-05）
- case-01 known-good：通過（但沒跑任何檢查就說 OK）
- case-02 known-bad：**未抓到**缺少 integration test
- case-03 boundary：誤報
→ 2/3 失敗。Skill 有存在價值。

## v1（Claude A 初版，142 行）
- 3/3 通過，但 Claude B 從未讀取 CONTRACTS.md
→ 連結不夠明顯，把最關鍵的兩條規則搬進 SKILL.md 主體

## v2（96 行）
- 3/3 通過；Claude B 導航路徑符合預期
- Sonnet 檔位：3/3；Opus 檔位：3/3（無過度解釋問題）
→ 定版，部署為 embedded 形態
```

## 驗收標準

- **驗收 1**：baseline（無 Skill）在至少一個評估場景上失敗——證明這個 Skill 解決真實問題
- **驗收 2**：有 Skill 後 3 個評估場景全通過，且**跨兩個檔位**都通過
- **驗收 3**：SKILL.md ≤ 500 行，參考鏈只有一層深
- **驗收 4**：`description` 同時含「何時用」與「何時不用」
- **驗收 5**：Skill 會被**確實觸發**——你能指出它掛在哪裡（hook / embedded / CLAUDE.md 完成定義），而不是「Claude 應該會想起來」
- **驗收 6**：至少一條規則寫的是**原因**而非命令
- **驗收 7**：你能說出這個 Skill 的迭代記錄——每一版改了什麼、為什麼、評估分數怎麼變

## 下一步

- 把這個 Skill 打包給第二個 repo 用 → [Project 04：Plugin 化與自動化治理](/projects/project-04-plugin-automation/)

## 延伸閱讀

- [Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills)（2026-07-22）
- [Lessons from building Claude Code: How we use skills](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills)（2026-06-03）
- [Improving skill-creator: Test, measure, and refine Agent Skills](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills)（2026-03-03）
- [Agent Skills Authoring Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
