# 平行研究→報告 Agent 艦隊 — 深度研究報告

> **日期**：2026-06-04
> **分支**：feature/insights-horizon-research
> **來源**：`/insights` On-the-Horizon 機會 #2
> **落點判定**：**改進既有 `overnight-research` SKILL**（非新建 — 新建違 R2 + Lesson 2026-06-04-E 孤兒）。
> **方法**：1 researcher 深研 + 主對話機械重驗。

---

## 0. 問題陳述

每個 source 一個 subagent（限約 400 token inline 回傳、寫入各自 scratch 檔），完成後 reducer 讀 scratch 檔、重驗 citation、組裝 10k 字報告，checkpoint 可續跑。

**真實痛點**：
- **研究 session 因 API output-token-limit 在 synthesis 階段中斷**。
  > ⚠️ **CAVEAT（保留 advisor 要求的誠實邊界）**：「至少 5 個 session」此具體數字來自 `/insights` parent context，**repo 內多次 grep（MEMORY/reports/skills）未找到直接佐證**。採信為需求背景，非 repo 已證實事實。repo 實際佐證的相關 failure mode 是：overnight-research GOTCHAS 的 session 逾時終止、dynamic workflow 幻覺、citation 歸錯源（SELF-ROUTE 65%）——間接支持需求真實性。
- **subagent verdict 非證據**（Lesson 2026-06-04-C：委派建檔落 isolated worktree，主 tree 找不到 → 必 grep 主 tree）。
- **citation 歸錯源先例**（SELF-ROUTE 65% 歸錯源，靠手動對抗驗證修正）。

---

## 1. 核心發現（7 點）

### F1 — 兩側 failure mode 必須分開設計
- **output-token-limit（輸出側）**：synthesis 階段單一 response 試圖生成 10k 字撞 `max_tokens`。根本解 = **reducer 逐段寫盤**（section-by-section Write，每節獨立呼叫只生成該節）。
- **context-window-limit（輸入側）**：累積多輪 game of telephone 撞 200k。根本解 = **scratch-file per subagent**（subagent 發現寫檔、reducer 讀檔而非讀 context 歷史）。
- ⚠️ **關鍵**：scratch-file 本身**不**解 output-limit；reducer 逐段寫才解。兩者搭配才完整。
> 來源：Anthropic engineering blog [HIGH]；overnight-research SKILL.md Phase 3 [HIGH，repo]

### F2 — ≤400 token 是 inline reference，非 scratch 檔大小上限
scratch 檔可存完整發現 + verbatim 引文（數千字元）。「≤400 token per agent」指 subagent 回傳 parent 的 **lightweight reference**（「已寫 source-3.md，重要 claim：…」），與磁碟內容無關。
> 來源：Anthropic blog 實測 subagent 回傳 1,000–2,000 token distilled summary [MEDIUM，blog 無明確 400 數字]

### F3 — 既有 FS-Researcher 架構驗證此路徑可行
Context Builder agent 建超越 context length 的 hierarchical knowledge base（寫檔）；Report Writer agent 逐節讀寫。兩角色分離 + 逐段寫盤是解 output-limit 的 canonical 實作。
> 來源：arXiv 2602.01566 [MEDIUM，摘要層級]；per-agent budget 具體數字 [LOW，疑 PDF fetch 外推]

### F4 — checkpoint = scratch 檔本身，優於 workflow resumeFromRunId
`dynamic-workflows-harness-2026-06-03.md` §5 L128 明確：「退出 CC 則下個 session 重啟」——跨 session（正是 resume 需求）workflow runtime 無法保證。scratch 檔是天然 checkpoint：resume = 掃描哪些 `source-N.md` 已存在 → 只補缺的 → reducer 讀所有 scratch 生報告。比 resumeFromRunId 更簡、不依賴 session 存活。
> 來源：repo `dynamic-workflows-harness-2026-06-03.md` L128 [HIGH，一手]

### F5 — citation 重驗須機械化（§R5）
每個 scratch 檔存：source URL/path + verbatim 引文 + 位置（行號/段落）。reducer 把每個 claim 的引文 grep 回 scratch 檔，命中=VERIFIED、miss=⚠️。直接解 SELF-ROUTE 65% citation 歸錯源（「手動對抗驗證」→ 系統化）。非 LLM 自評，pure grep/read。
> 來源：repo + Anthropic CitationAgent blog [HIGH]

### F6 — dynamic workflow 是 orchestration 可選項，非必要
dynamic workflow JS 控制平面**不能碰 FS**（§3.1）——scratch 寫檔仍須 agent 工具。它不直接解 output-limit；屬研究預覽會幻覺（須 grep 重驗）。fan-out + scratch + reducer 可直接用 parallel sub-agent 委派實作，不依賴 workflow runtime。
> 來源：repo dynamic-workflows-harness §3.1 [HIGH]

### F7 — 「5 session 中斷」repo 未找到直接佐證（見 §0 CAVEAT）
採信為 parent context。repo 佐證的是相同根本問題（長 synthesis 單點失敗），間接支持需求。

---

## 2. 與既有 SKILL 的關係：改進 overnight-research，非新建

**overnight-research 已有**：fan-out（Phase 2 ≤4 sub-agent）、寫盤報告（Phase 3 + REPORT_PATH）、autoresearch 迭代（Phase 4）、keepalive heartbeat（機械重驗確認 L118-121）、per-phase checkpoint。

**缺少的 4 個 gap（精確 diff）**：
1. Phase 2 subagent 目前 **inline 回傳**（機械重驗：SKILL.md L36 inline 模式屬實）→ 改 Write `research/scratch/source-N.md`
2. Phase 3 整份報告一次生成 → 改 reducer 逐節串流 Write
3. citation 無機械 re-verify pass → Phase 3/5 加 grep-back
4. 無 disk-resume → Phase 0 加 scratch 掃描，已存在 source 跳過

新建 SKILL 違 R2（骨架已覆蓋）+ Lesson 2026-06-04-E（孤兒）。**改進是唯一 R2 合規選擇**。

---

## 3. Pipeline 設計骨架

```
Phase 0 — Resume 偵測
  mkdir -p research/scratch/
  EXISTING=$(ls research/scratch/source-*.md 2>/dev/null | wc -l)
  [已存在 M 個 → 從第 M+1 個繼續]

Phase 1 — 網搜（現有保留）

Phase 2 — Fan-out（每來源一 subagent，≤4 並行）
  per subagent: WebFetch → 分析 → Write research/scratch/source-N.md
    格式: url / claims[claim+verbatim引文+位置] / key_facts / source層級(P/O/C/E)
  inline 回傳: ≤200 token reference
  [checkpoint: ls research/scratch/source-N.md 機械確認存在（subagent verdict 非證據）]

Phase 3 — Reducer 逐節串流
  for SECTION in [摘要,背景,核心,最佳實踐,工具比較,陷阱,趨勢,建議,附錄]:
    grep 篩相關 scratch → 生成該節 → Append Write
    [checkpoint: wc -m 報告字數]

Phase 4 — Citation 機械重驗
  for claim in 報告 [citation]:
    grep verbatim 回 scratch/source-N.md → HIT/MISS
    MISS → 標 ⚠️（非刪，research-hub:deep 規範）

Phase 5 — 現有驗證（wc -m ≥ MIN_CHARS + healthcheck）
Phase 6 — 現有提交（保留）
```

---

## 4. 關鍵風險與下限約束

- **subagent verdict 非證據**：Phase 2 每 subagent 聲稱「已寫 source-N.md」→ parent 必 `ls` 機械確認（Lesson 2026-06-04-C）。
- **信度分層**：scratch 記 source 層級，reducer 標 HIGH/MEDIUM/LOW。
- **幻覺防護**：reducer 不得從 memory/context 推斷 citation，只讀 scratch verbatim 欄。
- **下限**：Anthropic 的「1,000–2,000 token distilled」是實測值非 scratch 上限，設計不能倒推。

---

## 5. Falsifiable Prediction 候選

「overnight-research 加 Phase 2 scratch-write + Phase 3 section-wise reducer 後，10k 字報告可不撞 output-token-limit 生成；kill session 後重跑，已有 scratch 檔數 = resume 點，最終 source 覆蓋率與首次一致。」

```bash
ls research/scratch/source-*.md | wc -l        # scratch 檔數
wc -m [REPORT_PATH]                            # ≥ 10000
diff <(first_run scratch list) <(after_resume scratch list)  # 相同
```

---

## 6. 信度分層彙整

| 來源 | 關鍵聲明 | 信度 | URL |
|------|---------|------|-----|
| Anthropic engineering blog | filesystem output / CitationAgent / 1k-2k distilled | HIGH | https://www.anthropic.com/engineering/multi-agent-research-system |
| repo dynamic-workflows-harness | workflow 不跨 session resume | HIGH | research/agent-harness/dynamic-workflows-harness-2026-06-03.md L128 |
| repo overnight-research SKILL.md | Phase 2 inline / Phase 3 配額 / keepalive | HIGH | 親讀 + 主對話 grep L36/L102/L118 |
| FS-Researcher arXiv 2602.01566 | Context Builder + Report Writer 逐節 | MEDIUM | https://arxiv.org/abs/2602.01566 |
| FS-Researcher 細節 | per-agent budget 數字 | LOW（疑外推） | 同上 |
| MEMORY「5 session 中斷」 | 此具體數字 | **未驗證**（parent context，非 repo） | — |
