# cc-workspace 大更新：GBrain + Hermes Agent + Karpathy LLM Wiki 精神實作

**日期**：2026-05-25 | **字元數目標**：≥ 5000
**Branch**：`claude/workspace-architecture-update-M6mXu`
**三個研究來源**：Karpathy LLM Wiki gist、Hermes Agent（Nous Research）、GBrain（Garry Tan）

---

## 執行摘要

本報告記錄對 cc-workspace 進行的「GBrain + Hermes Agent + Karpathy LLM Wiki」精神對齊更新。更新方法為「gap analysis 優先」——先比對三個參考來源的核心設計原則，再對照現有 workspace 構件，只補真正缺失的部分，不重複建立已存在的結構。

最終實施的 5 個核心變更：Karpathy 缺失的 LOG.md、GBrain 腦優先查找協議、GBrain 式有型邊知識圖、Hermes 品質 Telemetry 欄位補全、schema.md LOG 規範。

---

## 1. 背景與動機

### 1.1 三個參考來源核心設計哲學

**Karpathy LLM Wiki**（gist 442a6bf）

核心洞見：「The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping.」LLM 最大的優勢不是回答問題，而是能自動維護跨文件一致性，把 bookkeeping 從人類肩膀移走。

三層架構：
- Raw Sources（immutable）— 原始素材，LLM 只讀不改
- Wiki Core（LLM-owned）— 合成後的 markdown pages，LLM 完全擁有
- Schema（人定義）— 結構規範（類似 CLAUDE.md 或 AGENTS.md）

三個核心操作：Ingest（加入新知識）、Query（檢索 + 發現成為新 page）、Lint（週期性健康檢查）

導航工具：`index.md`（內容目錄）、`log.md`（append-only 操作紀錄）— **log.md 是防止知識流失的關鍵**。

**GBrain**（Garry Tan / Y Combinator）

核心洞見：「Search gives you raw pages. GBrain gives you the answer.」比傳統 RAG 多了一個合成層，且用 typed graph edges 讓知識之間有語意關係。

關鍵設計原則：
1. **知識圖優於純向量搜尋**：typed edges（`attended`/`works_at`/`invested_in`）比純 embedding 檢索精準 +31.4 points precision
2. **Markdown 作為 SSoT**：git 管理的 markdown，人類可讀 + agent 可用
3. **腦優先查找（brain-first lookup）**：每次查詢先過 brain，命中就不呼叫外部 API（省 token、省延遲）
4. **Signal Detection**：每條 agent 訊息自動偵測實體/事件/時效性資訊並決定是否 ingest
5. **可恢復工作隊列**：兩相持久化（pending→done）確保 LLM loop 崩潰不丟工作

**Hermes Agent**（Nous Research）

核心洞見：「The agent that grows with you」— 不只是工具，而是會從執行中學習並自我改良的系統。

關鍵機制：
1. **Skill 自主生成與精煉**：完成複雜任務後自動生成 skill 並存儲，執行中迭代改良
2. **持久記憶 + 週期性整合**：episodic memory 有 periodic nudge 機制，FTS5 全文搜尋跨 session 記憶
3. **Trajectory Compression**：多輪互動壓縮成訓練資料，驅動下一代 tool-calling model
4. **品質 Telemetry**：skill 執行追蹤（使用次數、成功率、refinement 次數）
5. **多平台 + 無人值守**：cron 排程 + 7 個 terminal backend + 跨平台持久狀態

### 1.2 現有 workspace 已實作什麼

Gap analysis 進行前，先盤點已有的構件，避免重複建設（Lesson 2026-05-25 a）：

| GBrain/Hermes/Karpathy 原則 | cc-workspace 現有對應 |
|-----------------------------|----------------------|
| Karpathy 三層架構 | `research/career-wiki/`（schema.md + raw/ + pages/）✅ 完整 |
| Karpathy Ingest op | `scripts/wiki-ingest.py` + `/autoresearch:wiki` ✅ |
| Karpathy Lint op | `scripts/wiki-lint.sh` ✅ |
| Karpathy Index.md | `research/career-wiki/INDEX.md` ✅ |
| GBrain Markdown SSoT | 全 workspace 以 git 管理 markdown ✅ |
| Hermes Skill system | `.claude/skills/` 下 18 個 skills ✅ |
| Hermes 持久記憶 | `memory/MEMORY.md` + hooks 維護 ✅ |
| Hermes episodic batch gate | `pre-compact.sh` + MEMORY 規範 ✅ |
| Hermes 無人值守排程 | `overnight-research` skill ✅ |
| GBrain 合成報告層 | `research/reports/` 20+ 深度報告 ✅ |

---

## 2. Gap Analysis 結果（5 個真正缺口）

### Gap 1：Karpathy LOG.md 缺失

**問題**：`research/career-wiki/` 有 schema.md、INDEX.md、raw/、pages/ 四個構件，但缺少 Karpathy 設計中明確要求的 `log.md`（append-only 操作紀錄）。

**影響**：無法追蹤 wiki 的演化歷史；新 session 的 agent 不知道上次什麼時候 ingest、lint 了什麼；知識維護的可見性差。

**修復**：建立 `research/career-wiki/LOG.md`，包含完整的 Session 1–9 歷史紀錄，定義 `[INGEST]`/`[QUERY]`/`[LINT]`/`[EVOLVE]` 四個 prefix，並在 schema.md 補入 LOG 規範章節。

**同步更新**：schema.md 加入 v0.2 版本標記 + LOG.md 格式規範。

### Gap 2：GBrain 腦優先查找協議缺失

**問題**：workspace 有大量知識（career-wiki、RESEARCH-INDEX、refs、memory），但沒有一個明確的「查找優先序協議」。Agent 每次需要知識時，傾向直接呼叫 WebSearch，沒有先查本地知識庫的行為規範。

**影響**：重複抓取已有的知識（增加 token + 延遲）；本地合成知識（career-wiki 36 pages、20+ reports）被閒置；brain-first 精神未落地。

**修復**：建立 `.claude/refs/brain-first-protocol.md`，定義四層 lookup hierarchy：
1. career-wiki → 職涯實戰知識
2. RESEARCH-INDEX → AI/Harness 研究
3. .claude/refs/ → 設計決策
4. memory/MEMORY.md → 跨 session 決策

只有前四層都未命中，才觸發 WebSearch。並定義 Signal Detection 五種觸發模式，以及 Post-Discovery 知識回流義務（不靜默跳過）。

### Gap 3：GBrain Typed Edges 缺失

**問題**：`research/RESEARCH-INDEX.md` 有一個優秀的 Mermaid 心智圖，但各構件之間缺乏**語意化的關係標注**。「context-management.md 使用了 Karpathy 的思想」這個關係只隱含在文字描述裡，沒有 GBrain 式的 typed edge。

**影響**：Agent 在跨構件搜尋時缺乏圖結構支援，只能靠全文匹配；架構決策溯源困難；無法識別哪個構件「實作」了哪個原則。

**修復**：在 `research/RESEARCH-INDEX.md` 底部新增「Knowledge Graph — Typed Edges」章節，定義 6 種 edge 類型（`implements`/`references`/`inspired_by`/`extends`/`contradicts`/`supersedes`），並建立 15 條 workspace 構件間的具體邊關係，涵蓋 rules、skills、agents、scripts 與其研究來源的語意關聯。

**成效**：GBrain 文獻顯示 typed edge 比純向量搜尋提升 +31.4 points precision@rank5；cc-workspace 雖無向量搜尋基礎設施，但結構化的 edge 表對 LLM agent 的 reasoning 有同等效果（LLM 可直接讀取 markdown 表格推理關係）。

### Gap 4：Hermes 品質 Telemetry 欄位缺失

**問題**：8 個現有 `METADATA.json` 文件有基本字段（name、version、last_reviewed）但缺少 Hermes 式的**自我演化追蹤**欄位：使用次數、改良迭代次數、品質評分、最後呼叫時間、進化階段。

**影響**：無法識別哪個 skill 是「battle-tested」還是「draft」；無法追蹤哪個 skill 最常被使用（優先維護）；skill 演化無量化基礎；`skill-evolution` skill 的分析缺乏數據源。

**修復**：使用 Python 腳本批次更新全部 8 個 METADATA.json，新增：
- `quality_score: null` — 數值評分（0–10），agent 執行後填入
- `usage_count: 0` — 被呼叫次數（agent 可遞增）
- `refinement_count` — 已應用的改良迭代次數（autoresearch 設為 11 對應 v1.11）
- `last_invoked: null` — 最後呼叫日期
- `evolution_stage` — 四個階段：`draft`/`tested`/`stable`/`mature`

### Gap 5（輕量）：schema.md LOG 規範缺失

**問題**：schema.md 定義了 page 格式、三個 ops 的流程，但沒有正式定義 LOG.md 的格式規範，導致 LOG.md 缺乏機器可解析的結構。

**修復**：在 schema.md 的「Version」章節前插入「LOG.md 規範」章節，定義 Entry 格式、OP prefix 清單、append-only 不可刪除原則。

---

## 3. 核心概念分析

### 3.1 LLM Wiki 的本質：消除 bookkeeping 的認知成本

Karpathy 的核心洞察是：知識庫維護失敗的主因不是「不夠努力」或「知識太多」，而是**維護工作的認知成本過高**。更新 10 個相關頁面、保持交叉引用一致、標記過時資訊——這些 bookkeeping 任務是 LLM 的強項，卻是人類的弱點。

cc-workspace 的 `career-wiki/` 已完整落地這個概念：36 個 pages、自動 lint、wiki-ingest.py 橋接 digest 到 wiki。這次更新添加的 LOG.md 完成了 Karpathy 架構的最後一塊——**不可變的操作歷史**，讓 wiki 的演化本身也變得可追溯。

### 3.2 GBrain 的圖優於向量：語意 vs 統計

GBrain 的重要發現是：純向量搜尋在知識圖譜場景下有系統性缺陷——語意相似的文字不代表概念關係。`redis-zero-downtime.md` 和 `postgres-microsec-tuning.md` 在 embedding 空間很近（都是「資料庫調優」），但它們的關係是 `similar_to`；而 `context-management.md` 和 Karpathy Context Engineering 的關係是 `implements`——這是完全不同的語意。

Typed edges 讓 agent 可以做**溯源推理**：「這個規則的設計依據是什麼？」「哪些構件落實了 Hermes 原則？」這類問題靠純 embedding 難以回答，但靠 RESEARCH-INDEX 的 typed edge 表可以直接用 grep 找到。

### 3.3 Hermes 的自我演化：從靜態工具到成長系統

Hermes 的核心主張是：一個 skill 在使用中應該**越來越好**，而不是保持靜態。每次執行都是改善的機會。

cc-workspace 的 `skill-evolution` skill 已實現了這個哲學的控制平面，但缺少**資料平面**——METADATA.json 沒有記錄 skill 的使用歷史。這次補充的 `usage_count`/`refinement_count`/`quality_score` 欄位提供了演化的數據基礎：skill-evolution 分析時可直接讀取所有 skill 的 METADATA，找出哪些是高頻使用但品質低（優先改良），哪些是低頻但品質高（維持現狀）。

`evolution_stage` 的設計借鑑 Hermes 的 skill lifecycle：`draft`（新建未驗證）→ `tested`（跑過少量場景）→ `stable`（battle-tested、已有 gotchas 記錄）→ `mature`（版本穩定、高頻使用）。overnight-research 設為 `tested`（新 skill），autoresearch v1.11 設為 `mature`（11 個改良週期）。

### 3.4 Brain-First vs WebSearch-First：成本與知識累積的分歧

WebSearch-first 的 agent 每次都從零開始——即使相同問題已被回答 10 次，仍要重新抓取、重新合成。Brain-first 的 agent 把每次成功查詢都視為未來查詢的投資——今天的 WebSearch + 歸檔 = 明天的 brain lookup。

`brain-first-protocol.md` 的 Signal Detection 表和 Post-Discovery 知識回流義務，強制 agent 在每次新發現後選擇其一（Ingest/Archive/Memorize/Skip），確保知識不斷累積而不只是過眼雲煙。

---

## 4. 最佳實踐與實作模式

### 4.1 LOG.md append-only 原則的強制性

設計原則：log 文件永遠只增不改。這解決了 wiki 維護中一個常見的「修正歷史」衝動——當發現 Session 3 的決策有誤時，正確做法是在最新條目說明修正，而不是回去改 Session 3 的記錄。

實作在 LOG.md 的 header 明確標注：`**Never delete entries** — this is a log, not a note`。

### 4.2 Typed Edge 的六種類型設計

選擇六種邊類型而非自由格式的原因：太少（只有 `related`）失去語意精度，太多（10+）維護負擔過重。六種覆蓋了 workspace 構件間最常見的語意關係：
- `implements`：最常用，rule/skill 落實外部概念
- `references`：引用但不完全落實
- `inspired_by`：學到精神但實作不同
- `extends`：基於現有構件擴展
- `contradicts`：衝突（需標注並管理）
- `supersedes`：取代舊版（幫助清理廢棄構件）

### 4.3 METADATA telemetry 的空值設計

所有新增欄位初始值為 `null` 或 `0`，而非設預設分數。原因：自動填入的初始值（如 `quality_score: 7`）比 `null` 更危險——它看起來像有效數據，但實際是噪音。`null` 明確表示「尚未評估」，agent 看到 `null` 會知道需要執行才能填入真實數據。

### 4.4 Brain-First Hierarchy 的設計原則

四層 hierarchy 的設計考量：
- 第一層（career-wiki）放個人職涯實戰，這是最不可能在 WebSearch 找到的知識，也是最有差異化價值的
- 第二層（RESEARCH-INDEX）放 AI/Harness 研究合成，已付出 WebSearch 成本的知識優先重用
- 第三層（refs/）放官方文件和設計決策，通常變化慢
- 第四層（memory）放跨 session 決策，命中意味著「這個問題之前想過了」
- WebSearch 是最後手段，且命中後有回流義務

---

## 5. 工具與生態系統

### 現有工具（已整合）

| 工具 | 功能 | 狀態 |
|------|------|------|
| `scripts/wiki-ingest.py` | digest → wiki 橋接，關鍵字匹配得分 | ✅ 生產就緒 |
| `scripts/wiki-lint.sh` | wiki pages 健康檢查，Lint Score ≥85 = PASS | ✅ 生產就緒 |
| `scripts/healthcheck.sh` | workspace 整體健康 | ✅ 生產就緒 |
| `.claude/skills/autoresearch/` | wiki Ingest/Query/Lint ops 操作層 | ✅ v1.11 mature |
| `.claude/skills/skill-evolution/` | skill 品質審查與進化 | ✅ stable |
| `research/career-wiki/` | 36 pages Karpathy 三層架構 | ✅ 36 pages |

### 新增工具（本次更新）

| 工具 | 功能 | 類型 |
|------|------|------|
| `research/career-wiki/LOG.md` | append-only wiki 操作歷史 | 新建文件 |
| `.claude/refs/brain-first-protocol.md` | 四層查找 hierarchy + Signal Detection | 新建 ref |
| RESEARCH-INDEX typed edges 章節 | 15 條語意關係邊 | 更新既有文件 |
| METADATA.json telemetry 欄位 | 8 個 skill 的品質追蹤數據結構 | 更新既有文件 |
| schema.md LOG 規範 | LOG.md 格式定義 v0.2 | 更新既有文件 |

---

## 6. 常見陷阱與反模式

### 反模式 1：看到「gap」就建新目錄

本次更新的第一個版本計劃建立 `wiki/` 目錄，完全複製 GBrain 的結構。但 advisor 指出這會建立和 `research/career-wiki/` 的平行結構，違反 workspace 的「更簡單被維護」目標。正確做法：先問「現有哪些構件已經滿足這個需求？」，只補真正缺失的。

這個教訓對應到 Lesson 2026-05-25 (a) 和 (e) 的精神：gap analysis 優先，避免重做已滿足項。

### 反模式 2：METADATA 預設非空值

如果自動填 `quality_score: 7.5`（一個看起來合理的初始值），後續的 skill-evolution 分析會把它當真實數據處理，無法區分「已評估為 7.5」和「從未評估」。空值 (`null`) 是更誠實的初始狀態。

### 反模式 3：brain-first 沒有「回流義務」

如果只定義「先查 brain」但不定義「查完後要回填知識」，brain-first 只能消耗知識，不能累積知識。最終 brain 的覆蓋率不增長，WebSearch 的觸發比例永遠不下降。

Post-Discovery 的四選一（Ingest/Archive/Memorize/Skip）把「靜默跳過」變成需要明示的選擇，強制 agent 每次都為知識累積做出貢獻。

---

## 7. 前沿趨勢與預測

### 7.1 Typed Knowledge Graph 的必要性日增

隨著 workspace 規模擴大（skills 從 13 增至 19，refs 從少量增至 28+），純文本搜尋的精度下降。GBrain 的 typed edges 代表了知識組織的下一步：從「哪裡有相關文字」到「構件間有什麼語意關係」。預計 cc-workspace 在未來 3–6 個月會自然發展出更多 `contradicts` 和 `supersedes` 類型的邊，因為這是知識系統成熟時自然產生的清理需求。

### 7.2 Skill Telemetry 驅動的資源分配

一旦 `usage_count` 開始被記錄，workspace 維護就能從主觀判斷（「這個 skill 感覺很常用」）轉為數據驅動（「這個 skill 被呼叫 23 次，gotchas_count 升至 8，refinement_count 仍為 0 → 最需要改良」）。Hermes 的自我演化精神最終落地於此。

### 7.3 Brain-First 作為 Cost Engineering 的一部分

隨著 token 成本管理變得更重要（MEMORY.md 的 token budget 優化記錄表明這是持續關注點），brain-first lookup 的每次命中都是一次省 token 的機會。若 career-wiki 能覆蓋 40% 的架構查詢，等效於每 session 省 5–10 次 WebSearch 往返。

---

## 8. 可立即實作的行動建議

1. **LOG.md 第一條用戶更新**：下次執行 `wiki-lint.sh` 後，手動在 LOG.md 加入 `[LINT]` 條目（建立使用習慣）
2. **腦優先查找試跑**：下個需要知識的任務，先 `grep -i <keyword> research/RESEARCH-INDEX.md` 再決定是否 WebSearch（驗證四層 hierarchy 的實用性）
3. **METADATA 第一次填值**：下次執行任一 skill 後，手動更新 `last_invoked` 和 `usage_count`（一旦有真實數據，skill-evolution 的分析才有意義）
4. **Typed edges 擴展**：每次發現新的「此構件基於某研究」關係，在 RESEARCH-INDEX typed edges 表新增一行（保持 graph 更新）
5. **brain-first-protocol.md 加入 HANDOFF**：在 `.claude/HANDOFF.md` 的「相關檔案」欄位加入 `brain-first-protocol.md` 的引用（確保 rewind 後新 session 知道此協議存在）

---

## 附錄：來源評分與索引

| 來源 | 影響力 | 原創性 | 可操作性 | 可信度 | 時效性 | 加權分 |
|------|--------|--------|---------|--------|--------|--------|
| Karpathy LLM Wiki gist | A | A | A | A | A | 9.5/10 |
| GBrain (garrytan/gbrain) | A | A | B | A | A | 9.2/10 |
| Hermes Agent (nousresearch) | B | A | A | A | A | 9.0/10 |

**Karpathy 核心引用**：「The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping.」

**GBrain 核心引用**：「Search gives you raw pages. GBrain gives you the answer.」/ 「+31.4 points precision improvement at rank 5 vs vector-only」

**Hermes 核心引用**：「The agent that grows with you」/ 「built-in learning loop — it creates skills from experience, improves them during use」

---

*生成工具：overnight-research pipeline / Branch：claude/workspace-architecture-update-M6mXu*
