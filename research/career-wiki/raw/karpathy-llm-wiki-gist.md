# Karpathy LLM Wiki — 原文架構摘錄

> **來源**: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
> **Ingested**: 2026-04-23
> **Purpose**: workspace 的 career-wiki 與 knowledge management 哲學的原始根源

---

## 核心哲學：從檢索到累積（From Retrieval to Accumulation）

與 RAG（每次查詢從零開始）相對，LLM Wiki pattern 維護一個**持續增長的個人知識庫**：
- RAG = stateless 檢索（每次查詢起點相同）
- Wiki = stateful 知識庫（每次查詢在前人積累上建立）

核心洞見：「The wiki is a persistent, compounding artifact.」

---

## 三層架構（Raw → Wiki → Schema）

### Layer 1: Raw Sources（不可變）
- 你策劃的原始文件：文章、論文、圖片、資料
- **LLM 永遠不修改**——單一事實來源
- 作為稽核路徑和 ground truth

### Layer 2: The Wiki（LLM 生成和維護）
- 由 LLM 建立和維護的 Markdown 文件目錄
- 包含：摘要頁、實體頁、概念頁、比較頁、概覽/合成
- LLM 負責：建立新頁面、更新時更新、維護交叉引用、保持一致性

### Layer 3: The Schema（設定 + 工作流定義）
- 告訴 LLM「如何維護 wiki」的規範文件（如 CLAUDE.md 或 AGENTS.md）
- 包含：目錄佈局、命名慣例、頁面類型、工作流（ingest/query/lint）
- **關鍵洞見**：這是讓 LLM 成為「有紀律的 wiki 維護者」而非一般聊天機器人的差異
- 與人類共同演進：根據對特定領域的適用性持續精煉

**設計原則**：結構保持人類明確定義和範圍；推理保持機率性。

---

## 三大核心操作（Ingest → Query → Lint）

### INGEST（攝入）
**目標**：當新來源到達時，深度整合進 wiki。

**流程**：
1. LLM 讀取新來源
2. 與人類討論關鍵要點
3. 撰寫摘要頁
4. 更新索引（index.md）
5. 更新 wiki 中的相關實體和概念頁（可能觸及 10–15 頁）
6. 在日誌（log.md）中追加條目

### QUERY（查詢）
**目標**：對 wiki 回答問題。

**流程**：
1. 人類提問
2. LLM 搜索相關頁面（先看索引，再深入頁面）
3. LLM 讀取頁面
4. LLM 合成帶引用的答案
5. **重要**：有價值的答案被歸檔回 wiki 作為新頁面

### LINT（健康檢查）
**目標**：定期健康檢查 wiki 以發現偏差和機會。

**LLM 檢查**：
- 頁面間的矛盾
- 過時的主張（被更新來源取代）
- 孤兒頁面（無入站連結）
- 缺失頁面（提到了重要概念但沒有獨立頁面）
- 缺失交叉引用
- 資料缺口（可通過網絡搜索填補的地方）

---

## 為何此 Pattern 有效

**Karpathy 關鍵洞見**：
> 「維護知識庫的繁瑣部分不是閱讀或思考——而是記賬工作。」

**人類 vs LLM 的職責劃分**：
- **人類**：策劃來源、引導分析、提好問題、思考意義
- **LLM**：其他一切（摘要、交叉引用、歸檔、記賬）

---

## 索引與日誌（兩個特殊文件）

### index.md（內容導向）
- 目的：目錄 wiki 中的所有內容；LLM 的第一搜索步驟
- 結構：每頁列有連結、一行摘要、可選 metadata（日期、來源數）
- 搜索工作流：LLM 先讀索引 → 找相關頁 → 深入
- 規模：在適中規模（~100 來源，~百頁）無需嵌入式 RAG 就能良好運作

### log.md（時間順序）
- 目的：發生什麼和何時的只追加記錄
- 包含：攝入、查詢、帶時間戳的 lint 遍歷
- 每條條目使用一致前綴格式，可用 Unix 工具解析

---

## 設計原則（對 Skill/Agent 設計的直接應用）

1. **職責分離**：Raw = 不可變事實；Wiki = 可變知識；Schema = 操作規則
2. **LLM 作維護者，人類作策劃者**：別讓 LLM 決定什麼重要（人類策劃）；讓 LLM 做無聊的事（記賬）
3. **複利成效**：每次攝入、查詢、lint 都應讓 wiki 處於更好的狀態
4. **先確定性索引**：在使用嵌入前用簡單的可解析索引文件
5. **顯式 Schema 作紀律**：Schema（CLAUDE.md 等價物）是有組織的 wiki 和聊天機器人之間的差異
6. **Lint 作主動維護**：定期健康檢查防止偏差

---

## 本 Workspace 的實例化

career-wiki（`research/career-wiki/`）是此 Karpathy 模式的直接實例化：
- **Raw sources**: `research/career-wiki/raw/`（履歷、Medium blog index）
- **Wiki pages**: `research/career-wiki/pages/`（37+ 頁）
- **Schema**: `research/career-wiki/schema.md`
- **Index**: `research/career-wiki/INDEX.md`
- **Lint**: `bash scripts/wiki-lint.sh`（100/100 分）
- **Log/Audit**: `research/career-wiki/AUDIT-REPORT.md`

---

## 可選工具（模組化，非必需）

- **qmd**：本地搜索引擎（BM25/向量混合 + LLM 重排序，設備端）
- **Obsidian**：IDE 用於瀏覽 wiki（圖形視圖、Dataview 查詢等）
- **Obsidian Web Clipper**：將網頁快速轉換為 Markdown
- **Marp**：基於 Markdown 的幻燈片（從 wiki 內容生成演示文稿）

---

## 應用領域

1. **個人**：追蹤目標、健康、心理、自我改進
2. **研究**：在幾週/幾個月內深入主題
3. **閱讀書籍**：歸檔每章，為角色、主題、情節線建立頁面
4. **商業/團隊**：內部 wiki 由 Slack、會議記錄、項目文件提供支持
5. **競爭分析、盡職調查、旅行規劃、課程筆記、業餘深潛**
