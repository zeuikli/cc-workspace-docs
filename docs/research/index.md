# research/ INDEX

> Type: raw→wiki（TPKI Layer1–2）
> Harness-Layer: L4-knowledge

研究知識庫總索引。跨 20 個子目錄，覆蓋論文、新聞、合成文件、參考資料、harness 規範等。

> **計數 SSoT**：檔案數/目錄數以 [`RESEARCH-INDEX.md`](RESEARCH-INDEX.md) 「目錄總覽」表為唯一維護點；本檔只描述各目錄職責，不維護計數（2026-07-10 起，消除雙表漂移）。

## 子目錄索引

| 目錄 | Type | 說明 |
|------|------|------|
| papers | raw:corpus | 315 篇論文歸檔（.md + .pdf），跨 Memory、Harness、Agent 等域；2020–2026 |
| tweets | raw:corpus | 273 條 Claude Code / AI Engineering 技術 thread 歸檔 |
| articles | raw:corpus | 非 AI 主題文章歸檔（research-hub Article Archive 輸出） |
| ai-articles | raw:corpus | 50 篇評分 AI 文章；統一評分框架（A-E /10 加權） |
| ai-news | raw:corpus | 每日 AI Newsletter 機器自動抓取；外部來源 |
| videos | raw:corpus | 7 個影片逐字稿/摘要；Podcast 與 YouTube |
| claude-blog | raw:corpus | Anthropic 官方 blog / docs 外部歸檔；~155 篇 |
| DAILY-RESEARCH | raw:digest | 每日研究輸出（Routine C）；格式 `YYYY-MM-DD.md` |
| DAILY-TOPICS | raw:digest | 每日選題輸出（Routine A）；供 DAILY-RESEARCH 消費 |
| reports | wiki:synthesis | autoresearch / overnight-research 輸出；合成報告 |
| best-practices | wiki:synthesis | 46 篇最佳實踐；涵蓋 hooks、agents、skills、permissions、MCP、模型選型等 |
| agent-harness | wiki:synthesis | Harness 評估框架 + 深度研究；consumer: `harness-meta` skill |
| evals | wiki:synthesis | Harness eval runs + baseline；PGE 評分（Generator ≠ Evaluator） |
| NEW-DOMAINS | wiki:synthesis | 每次 Routine E 新領域探勘紀錄；供下次去重 |
| career-wiki | wiki:knowledge-base | Karpathy LLM Wiki pattern；36 頁；consumer: `zeuik-senior-architect` agent |
| archive | schema:archived | **唯讀封存**：the-loop-harness-v2/v3/v4 三代（含各自的 fixtures 與 baseline）。**不得作為 canonical 引用**，只供歷史對照 |
| the-loop-harness-v5 | schema:spec | **現行世代**：v5.1 單人 baseline、六題 fixture、三模型結果與限制。**條文本身不在此**——canonical = `.claude/rules/` |
| unknowns-workspace-refine | wiki:project | Know Your Unknowns 框架導入 + workspace refine 全案（PLAN + 盲點報告） |
| workspace-agent-architecture | spec:living | 智能體化全案：SPEC + 製作過程留存（MCP 轉換/KYU OS 層/SIA 接線/client 路線） |

**行為契約 canonical**：`.claude/rules/{core,context-management,output-discipline}.md`——v5 裁決條文**單一 owner**，不再有 `HARNESS-CORE-vN.md` 全文層。（v5.1 起 `loop.md`／`graph.md` 已刪，精要壓入 `core.md` §APPLY 與 §PROPOSE；path-scoped 另有 `security-hygiene.md`／`prompt-lifecycle.md`。）
**Routine 執行契約**：`ROUTINE-AUTONOMY-CONTRACT.md`（無人值守自主執行：終止條件／blast radius／verifier／展示紀律／oracle／測試檔紅旗／終局狀態）＋ `ROUTINE-MERGE-GATE.md`（merge 前置閘與失敗語義）——A–G 七個 Routine 共用，各 `ROUTINE-*.md` 只放指針。
**v5.1 目錄**：`research/the-loop-harness-v5/`（INDEX、SPEC、FIXTURES、結果、評估、限制與交接；執行入口 = `scripts/run-v51-baseline.py`）。
**封存**：`research/archive/the-loop-harness-{v2,v3,v4}/` 唯讀。歷史內容只供參考，不是 v5.1 的輸入或回歸證據。

---

## Agent Quick Navigation

| Looking for... | Go to |
|---------------|-------|
| Career experience / past decisions | `career-wiki/INDEX.md` → `zeuik-senior-architect` agent |
| Agent harness evaluation | `agent-harness/HARNESS-CARD.md` |
| Latest AI news (7-day dashboard) | `ai-news/README.md` |
| Claude Code official guidance | `claude-blog/README.md` |
| Academic papers | `papers/README.md` |
| Per-model eval results | `evals/INDEX.md` |
| Deep research reports | `reports/README.md` |
| Workspace 智能體化全案（SPEC/MCP/client） | `workspace-agent-architecture/SPEC.md` |
| Claude Code best practices | `best-practices/INDEX.md` |
| Tweet / article archive | `tweets/README.md` |

## Query Patterns

```
"Zeuik 在 KKStream 怎麼做 FinOps？"
  → zeuik-senior-architect agent → career-wiki/pages/finops-*.md

"最新的 LLM agent 論文有哪些？"
  → papers/README.md → browse by topic

"今天的 AI 新聞"
  → ai-news/README.md (7-day dashboard)

"Harness 目前評分多少？"
  → agent-harness/HARNESS-CARD.md

"最近有哪些深度研究報告？"
  → reports/README.md → sort by date
```

---

**最後更新**: 2026-08-04
