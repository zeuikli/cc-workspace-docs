# AI Agent 工程通用研究報告：Harness 工程、Context 最佳化、委派、記憶與自我進化

> **類型**：consolidated:deep-research — 整併 35 份前置研究報告（2026-05-12 → 2026-05-31）重寫成通用知識
> **日期**：2026-05-31 ｜ **語言**：繁體中文（技術術語保留英文）
> **定位**：去除工作區內部代號、可供任何讀者閱讀的 AI Agent 工程通用研究報告
> **引用原則**：所有數據與論文均源自前置報告語料；未經來源支持的主張一律標注 `[unverified]`

---

## 執行摘要

2025–2026 年 AI 工程的核心範式轉移，是從「調教模型」轉向「設計 Harness」。**Harness 指模型權重以外的一切執行環境**——指令系統、工具介面、驗證迴路、狀態管理、安全治理。多項實證顯示：同一個模型，僅靠 harness 設計差異，任務成功率可以從 20% 拉到接近 100%，準確率最高出現 10 倍落差。換言之，「選模型」實質上等於「選 harness 生態」，而遷移成本被市場嚴重低估。

本報告整併 35 份前置深度研究，收斂出五條主幹：

1. **Harness 工程**是新護城河——`Harness ⊇ Context Engineering ⊇ Prompt Engineering` 三層嵌套，框架貢獻往往 ≥ 模型選擇。
2. **Context 是稀缺資源**而非說明文件——「精確的少量 context > 大量 context」已獲論文級量化驗證（policy token 60.1K → 2.9K，-95%，效能相當）。
3. **Sub-agent 是資訊蒐集者，不是平行實作者**——錯置委派會因 context 隔離產生決策衝突；fan-out 有硬上限。
4. **記憶整合是高風險操作**——連續無節制整合會讓模型在 ARC-AGI 上從 100% 崩跌至 46%；顯式、可治理的記憶控制是關鍵。
5. **自我進化需要閉環**——失敗信號 → 記錄 → 提煉規則 → 修正架構 → 驗證 → 成為下次 baseline，且生成者不可自評（Generator ≠ Evaluator）。

以下逐節展開，附完整論文索引、量化數據總表與術語對照。

---

## 1. 背景：從 Prompt Engineering 到 Harness Engineering 的範式轉移

過去三年的主流敘事是「模型能力競賽」。但隨著前沿模型能力差距縮小，競爭軸線已明顯下移到 harness 層。一個被反覆引用的對照實驗最能說明問題：同一個 Claude Opus 4.5 模型，在「裸跑」狀態下執行 20 分鐘、花費約 9 美元，產出的是無法運行的程式碼；而在完整 harness（指令 + 工具 + 驗證 + 狀態管理）支撐下執行 6 小時、花費約 200 美元，產出的是生產品質程式碼。**差別不在模型，而在環境**。

Andrej Karpathy 在 2026 年初將這個轉變概念化為 **Context Engineering**：CLAUDE.md（或 AGENTS.md）這類指令文件中的每一個 token，都是「花掉的 context 預算」，而非「越詳細越好的說明書」。這個視角的反轉非常關鍵——它把指令文件從「文件」重新定義為「稀缺資源管理問題」。

三個層次的嵌套關係構成了整個領域的骨架：

```
Harness ⊇ Context Engineering ⊇ Prompt Engineering
```

- **Prompt Engineering**：單次互動的措辭最佳化。
- **Context Engineering**：跨整個 session 的 context 預算管理——填什麼、怎麼排序、何時壓縮。
- **Harness Engineering**：包含 context、工具、驗證、狀態、生命週期、安全的完整執行環境工程。

業界統計給這個轉變提供了急迫性的註腳：根據 Pinggy.io 的統計，**88% 的 AI agent 專案無法上線**，主因不是模型不夠強，而是 harness 太脆弱（2026-05-19 報告引用）。Augment Code 的研究則指出 **65% 的企業 AI 失敗源自 harness 缺陷**（2026-05-17 報告引用，`[unverified]` 未提供 URL）。

---

## 2. Harness Engineering 核心架構

### 2.1 五子系統模型

一個完整的 harness 可拆解為五個子系統（walkinglabs 課程框架）：

| 子系統 | 職責 | 典型載體 |
|--------|------|---------|
| 指令子系統 | 定義行為約束與規則 | AGENTS.md / CLAUDE.md |
| 工具子系統 | 提供與環境互動的能力 | Tool schema / MCP server |
| 環境子系統 | 提供執行的沙盒與資源 | 容器 / 檔案系統 / 網路策略 |
| 狀態子系統 | 跨步驟、跨 session 的記憶 | MEMORY 檔案 / 向量 DB / 日誌 |
| 反饋子系統 | 驗證與品質回授 | Hooks / 測試 / healthcheck |

一個 TypeScript + React 團隊的案例顯示：在模型完全不變的前提下，僅僅補齊這五個子系統，任務成功率就從 **20% 升到接近 100%**（2026-05-17 報告）。

### 2.2 CAR 三層分解（Control–Agency–Runtime）

學術界（He et al., CAR Framework, 2026-04-23）提出將 harness 形式化為三層：

- **Control（控制層）**：預先編碼的持久約束——規則、價值觀宣告、禁止事項。
- **Agency（能動層）**：模型可自主決定的行動空間——工具呼叫、規劃、推理。
- **Runtime（運行層）**：時間性治理——hooks、生命週期管理、阻斷機制。

CAR 並衍生出 **HarnessCard** 概念——類比 Model Card 的透明揭露標準，讓 harness 的設計假設可被審計與比較。

### 2.3 PEV 執行循環（Plan–Execute–Verify）

現代 harness 的核心執行架構是一個帶回授的循環：

```
PLAN（寫出可機械驗證的完成標準）
  → EXECUTE（在約束下執行）
  → VERIFY（執行所有驗證命令）
  → 失敗則回到 EXECUTE
```

PEV 的關鍵在於 **PLAN 階段必須先寫出可驗證條件**（例如「測試通過」「healthcheck 輸出 PASS」「特定指令輸出特定字串」），而非寫出「步驟清單」。目標導向（iterate to a target）勝過步驟導向（follow steps），因為後者容易卡在「下一步是什麼」而失去方向。

### 2.4 Harness–Model Fit（HMF）

HMF 指 harness 設計與目標模型能力邊界的對齊程度。三種典型失配：

- **Over-scaffolding（過度鷹架）**：為強模型寫了冗餘的補償性指令，浪費 context 預算。
- **Under-scaffolding（鷹架不足）**：對弱模型的支援覆蓋不足，導致失敗。
- **Model-drift（模型漂移）**：模型升級後，harness 仍沿用過時的能力假設。

設計良好的 harness 跨模型移植時，效能損失 **< 5%**；設計不良的則 **> 40%**（2026-05-16 報告）。這直接量化了「harness 可移植性」的價值。

### 2.5 五層失敗防禦模型

每一次 agent 失敗，都應對應到具體的某一層去修復，而不是反射性地「換個更強的模型」：

1. **任務規格層**：需求是否定義清楚、是否有可驗證標準？
2. **脈絡供給層**：是否給了正確的 context（而非更多 context）？
3. **執行環境層**：工具、沙盒、權限是否到位？
4. **驗證回饋層**：是否有獨立的驗證迴路捕捉錯誤？
5. **狀態管理層**：跨步驟的記憶是否正確傳遞？

---

## 3. Context Engineering 與 Token 最佳化

### 3.1 三層 Context Tiering

context 預算管理的核心架構是三層分級載入：

- **Layer 1 — 永遠自動載入**（建議 ≤ 3,500 tokens）：核心指令文件 + 全域規則。這是每個 session 的固定成本。
- **Layer 2 — 路徑觸發載入**：只在相關檔案被讀取時才計費（透過 frontmatter 的 `paths:` 宣告）。
- **Layer 3 — 顯式觸發載入**：技能（skills），完全按需載入。

把規則從「全域永遠載入」改為「路徑範圍按需載入」，效果驚人：某案例中 28 條全域規則改為「5 條全域 + 其餘路徑範圍」後，**session 啟動 token 降低 82%**（2026-05-18 報告）。

### 3.2 Auto-load 合規率的鐵律

指令文件不是越長越好，而是存在明確的「合規率懸崖」。KuCoin 對 30 個 repo、為期 6 週的研究給出了關鍵曲線（2026-05-18、2026-05-25 報告引用）：

| 規則情境 | 錯誤率 / 合規率 |
|----------|----------------|
| 無指令文件 | 錯誤率 41% |
| 4 條規則 | 錯誤率 11% |
| **12 條規則（甜蜜點）** | **錯誤率 3%** |
| 14–18 條規則 | 合規率跌至 52% |
| 文件 > 200 行 | 合規率從 76% 跌至 52% |
| 文件 > 4,000 tokens | 合規率降至約 30% |

**結論**：12 條左右的核心規則是甜蜜點；超過之後，多寫的每一條規則都在稀釋所有規則的遵從率。剪枝測試很簡單——「移除這行，模型會犯錯嗎？」答案是「不會」就立刻刪。

### 3.3 TYPE A/B/C/D 規則分類

在壓縮 auto-load 內容時，並非所有文字等價。一套經 50 輪優化驗證的分類框架（2026-05-18 報告）：

- **TYPE A — 強制行為動詞**（YOU MUST / 禁止 / IMPORTANT + 具體數字）→ **禁止移除**。
- **TYPE B — 規則 + 解釋** → 可移除「解釋」部分，保留規則本身。
- **TYPE C — 背景脈絡 meta** → 可安全移除。
- **TYPE D — 參考連結**（「詳見 X.md」）→ 可安全移除。

任何壓縮都應從 C/D 開始，最後才動 B 的解釋，絕不碰 A。

### 3.4 NLAH 原則：HEAD > TAIL >> MIDDLE

**NLAH（Natural Language Agent Harness）** 的核心是把 harness 控制邏輯從程式碼改寫為「可編輯的自然語言文件」，使 harness 可移植、可審計、可比較。NLAH 論文（arXiv:2603.25723）給出了一個論文級的量化結果：**policy token 從 60.1K 降到 2.9K（-95%），同時維持 SWE-bench 性能**。

這直接驗證了「right context > more context」不再只是經驗法則。其工程推論是 **HEAD > TAIL >> MIDDLE**：最強的 TYPE A 規則放在 context 的開頭（HEAD），次要規則放結尾（TAIL），避免落入「Lost-in-the-Middle」的中段注意力衰減區（200K window 下約在 147,000–152,000 tokens 處呈 U 型衰減）。

### 3.5 Token 最佳化具體手段

| 手段 | 效果 | 來源 |
|------|------|------|
| 工具延遲載入（Tool Search） | MCP token 51,000 → 8,500（-83.3%） | 2026-05-18 |
| 路徑範圍規則 | 規則 token 省 70–80% | 2026-05-18 |
| 記憶檔案重構 | 35.5KB → 3.5KB（-90%），每 session 省 ~8,000 tokens | 2026-05-18 |
| 輸出紀律（無開場白、精簡句式） | 英文輸出 -80.6%，繁中 -86.2%，品質無衰退 | 2026-05-12、2026-05-16 |
| 50 輪 framework-first 優化 | auto-load ~4,459 → ~3,392 tokens（-23.9%） | 2026-05-18 |

兩個系統性事實值得記住：(1) AI agent 的 token 消耗比純對話高約 **50 倍**（LeanOps 2026）；(2) Claude Code 的 auto-compact buffer 固定佔 **33,000 tokens**（200K window 的 16.5%，不可調整）——這意味著實際可用 context 比帳面少。

### 3.6 CJK 特殊警告

對繁體中文／日文／韓文內容，**禁止使用 token-pruning 類壓縮工具**（如 LLMLingua），實測會造成 25%+ 的品質衰退。中文場景本身還承擔約 1.71 倍的 token 稅（同一語意需要更多 token）。

---

## 4. Sub-Agent 委派模式與陷阱

### 4.1 核心心智模型：資訊蒐集者，不是平行實作者

官方文件作者 Adam Wolf 明確指出：sub-agent 的最佳定位是「information gathering（資訊蒐集）」，而不是「平行實作者」。這是最容易犯的根本性錯誤——把多個 sub-agent 派去各自實作不同模組，會因為彼此 context 隔離而產出互相衝突的設計決策。**實作任務應該交給單一、擁有完整 context 的 agent**；委派則用於研究、搜尋、審查這類「只需要結論」的工作。

### 4.2 委派觸發條件（任一成立即委派）

- 需讀取 **≥ 10 個檔案**（研究型任務，context 污染風險高）。
- 預期工具呼叫 **> 20 次**（大量工具雜訊會污染主對話）。
- 可拆成 **≥ 3 個獨立子任務**（適合平行 fan-out）。
- 任務類型屬於 {研究、安全審查、架構決策}（類型觸發，不計數量）。

### 4.3 拓撲規則

- **Fan-out 上限 4**：單一訊息最多同時啟動 4 個 sub-agent；第 5 個會被靜默忽略。
- **通訊限 parent ↔ child**：child 之間不直接溝通，失敗一律返回 parent 決策。
- **child 不 self-retry**：失敗就返回，由 parent 判斷重試或改策略。
- **child 不能再開 child**：sub-agent 不能再派 sub-agent。
- **child 輸出只含結果**：不加「完成」「Done」等確認句。

### 4.4 十大委派陷阱（Gotchas）

| # | 陷阱 | 修復方向 |
|---|------|---------|
| 1 | **過早宣告勝利**：agent 宣稱完成但只做一半 | 完成條件要求展示實際輸出（`wc -m`、test result） |
| 2 | **平行實作反模式**：多 agent 各自實作，產出衝突 | 實作改由單一有完整 context 的 agent 執行 |
| 3 | **Fan-out 超過 4**：第 5 個 agent 被靜默忽略 | 4 個以內或序列化 |
| 4 | **工具過度授權**：研究型 agent 被給了寫入工具 | 最小化 allowed-tools；研究只給 Read/Grep/Glob |
| 5 | **外部資料的 prompt injection** | 用 `<untrusted_objective>` 包裹外部輸入；研究型 agent 不給 Bash |
| 6 | **child 靜默失敗**：parent 誤以為成功 | prompt 明確要求失敗時輸出 `FAILED: <reason>` |
| 7 | **過大 context 破壞 cache**：fork 時繼承過大的 parent context | parent 先 compact 再 fork |
| 8 | **序列依賴陷阱**：平行執行有依賴的任務（B 需要 A 的輸出） | 識別依賴後改序列執行 |
| 9 | **AGENTS.md 品質差**：壞的指令文件效果 -30%，AI 自動生成 +20% 成本 / -2~3% 成功率 | 必含具體工作流程與「禁止+解法」配對 |
| 10 | **棄用工具未更新**：背景任務的讀取方式隨版本變更 | 跟隨最新版本慣例，用 Read 讀 output_file |

### 4.5 四層失敗恢復

`Retry（指數退避）→ Rollback（git revert）→ Decompose（拆更小子任務）→ Escalate（升模型或人工介入）`。重點是**逐層升級**，而不是一遇到失敗就跳到「換模型」。

---

## 5. 大道至簡與成本效率

### 5.1 加法思維是效率陷阱

整個領域反覆驗證的一條反直覺原則：**加法思維（一直加東西）是效率陷阱**。

- 更少但更精確的 context > 更多 context。
- 更強的 prompt > 更多的 agent。
- 更好的工具設計 > 更多的工具。

DeepMind 的多代理協調研究給出了警示性數字：在 Bag-of-Agents 模式下，錯誤會被放大 **17.2 倍**；而 agent 數量 ≥ 4 之後出現飽和效應，邊際效益遞減（2026-05-12 報告）。Vercel v0 的案例同樣顯示：移除 80% 的工具後，性能反而顯著提升。

### 5.2 Prompt Caching 五不原則

Prompt cache 命中可把輸入成本降到原本的約 10%（$0.30/MTok vs $3/MTok，節省約 90%）。但要維持高命中率，有五件事絕對不能做（Thariq Shihipar：「Cache rules everything. We treat it like uptime.」）：

1. 不動態修改 system prompt。
2. 不在 session 中途切換模型。
3. 不在對話中增刪工具定義。
4. 不在 compact 時改變 system prompt。
5. 不使用不一致的工具清單。

靜態內容（指令文件）永遠放最前面當快取前綴；動態資訊用 `<system-reminder>` 注入訊息流，而**不去修改 system prompt**（否則整個快取前綴失效）。

### 5.3 模型選擇準則

按「需要獨立認知的檔案數」分配模型：

- **0–1 個檔案** → 用最便宜的小模型（如 Haiku）。
- **2–9 個檔案** → 用中階模型（如 Sonnet）。
- **10+ 個檔案 / 架構決策** → 用旗艦模型（如 Opus）。

一個反直覺的研究發現（AgentOpt，`[C]` 未本地驗證）：**讓強模型當 Planner 反而最差**——強模型作 2-stage planner 僅 31.71%，而小模型作 planner + 強模型作 solver 達 74.27%；正確的模型組合比錯誤組合省 13–32 倍成本。教訓是：懂得委派的弱 planner，勝過什麼都自己扛的強 planner。

### 5.4 Advisor 模式（Generator + 外部評估）

「執行者用便宜模型 + 顧問用旗艦模型」的組合在實測中表現亮眼：

- Haiku 執行 + Opus 顧問：**每任務成本降低 85%**，效能相當。
- Sonnet 執行 + Opus 顧問：成本 -11.9%，效能 +2.7%。

### 5.5 Context 狀態決策梯階

依 context window 使用率調整行為：

`0–40% 無限制 → 40–70% 聚焦 → 70–85% 主動壓縮（compact）→ 85–95% 停止接新任務 → 95%+ 立即清空重開`。

---

## 6. LLM 記憶控制

### 6.1 記憶分類法（神經科學對照）

依 Tulving（1972）與 Wu et al.（arXiv:2504.15965）的框架，AI 記憶可對應人類記憶類型：

| 人類記憶 | AI 對應 | 工程實現 |
|---------|---------|---------|
| 感覺記憶 | Token 輸入緩衝 | 實時 token 流 |
| 工作記憶 | Context Window | 固定長度輸入序列 |
| 情節記憶（Episodic） | 對話歷史、軌跡 | 外部資料庫、日誌 |
| 語義記憶（Semantic） | 預訓練知識 + 知識庫 | 模型權重 + 向量 DB |
| 程序記憶（Procedural） | 技能庫、工具定義 | 程式碼庫、提示模板 |

Wu et al. 進一步提出 **三維八象限框架**：Object（個人 vs 世界）× Form（顯式 vs 隱式）× Time（短期 vs 長期）。記憶儲存則可四分（Zhang et al., arXiv:2404.13501）：文字記憶 / 向量記憶 / 結構化記憶（知識圖譜）/ 參數記憶（模型權重）。

### 6.2 六大記憶操作與控制旋鈕

Du et al.（arXiv:2505.00675）把記憶系統的操作收斂為六種：**整合（Consolidation）、更新（Updating）、索引（Indexing）、遺忘（Forgetting）、檢索（Retrieval）、壓縮（Condensation）**。其中一個關鍵主張：**整合應該是「顯式操作」而非自動觸發**——這正是下一節「記憶整合風險」的伏筆。

實務上的控制旋鈕清單：

- **寫入策略**：Always-write / Selective-write / Delayed-write。
- **整合頻率門控**：顯式觸發，預設不開。
- **遺忘策略**：Ebbinghaus 遺忘曲線（MemoryBank 的 `R = e^(-t/S)`）、Heat Score（MemoryOS）。
- **分層深度**：STM/MTM/LTM 三層是多篇論文一致的「黃金分割」。
- **檢索策略**：Dense + Sparse + Graph + Temporal 混合索引。
- **Context vs Memory 決策點**：≤ 10 輪用長上下文最划算；> 20 輪後外部記憶成本才有利。

### 6.3 關鍵記憶架構

- **MemGPT**（Packer et al., arXiv:2310.08560）：把 LLM 類比成作業系統——主記憶（Context Window）↔ 回憶儲存 ↔ 歸檔儲存，用 Interrupts 機制讓模型主動「換頁」。
- **MemoryOS**（arXiv:2506.06326）：STM → MTM → LTM 三層；Heat Score = 頻率 × 互動長度 × 時間衰減；LoCoMo 上 F1 +49.11%。
- **Mem0**（arXiv:2504.19413）：生產級記憶 API，ADD/UPDATE/DELETE/NONE 四動作增量寫入；LOCOMO 上比 OpenAI +26%，p95 延遲 -91%，token 成本 -90%。
- **HippoRAG**（Gutiérrez et al., arXiv:2405.14831, NeurIPS 2024）：用知識圖譜 + Personalized PageRank 模擬海馬體索引；多跳 QA +20%，比基線快 6–13 倍、便宜 10–30 倍。
- **A-MEM**（Xu et al., arXiv:2502.12110, NeurIPS 2025）：Zettelkasten 式互連記憶——新記憶會「觸發既有記憶的修訂」而非單純追加。
- **Chronos**（arXiv:2603.16862）：時序感知記憶，用 SVO 事件元組 + ISO 8601 時間戳建雙索引；LongMemEvalS 達 95.60%。
- **Hindsight**（arXiv:2512.12818）：四網絡架構（世界事實／agent 經驗／實體摘要／演化中的信念），讓 20B 開源模型在 LongMemEval 上超越 GPT-4o（83.6%）。

### 6.4 記憶整合的高風險本質（最重要的警告）

這是整個記憶領域最反直覺、也最重要的發現。**Useful Memories Become Faulty**（Zhang et al., arXiv:2605.12978）證明：連續、無節制的記憶整合會嚴重損害推理——GPT-5.4 在 ARC-AGI 上經過 20 輪整合後，準確率從 **100% 崩跌至 46%**。三個失效機制：

1. **Misgrouping（錯誤分組）**：把不該歸併的記憶硬塞進同一類。
2. **Interference（干擾）**：新舊記憶相互覆蓋污染。
3. **Overfitting（過擬合）**：記憶過度貼合歷史樣本，喪失泛化。

工程推論——**Episodic-First** 策略最穩健：優先保留原始 episode 作為一級證據，把「整合」當成顯式、可治理、可回滾的高風險操作，而不是預設背景行為。

---

## 7. Agent 自我進化

### 7.1 核心閉環

8 篇論文共同收斂出一個自我進化的閉環（harness-memory-self-evolution 合成報告）：

```
失敗信號 → [記憶層] 記錄 → [提煉] 可泛化規則 → [整合] 更新規則
  → [架構修正] 調整 harness / hooks → [驗證] healthcheck / eval
  → [記錄] 成為下次 baseline ↺
```

### 7.2 語言反思強化學習

- **Reflexion**（Shinn et al., arXiv:2303.11366, NeurIPS 2023）：用「語言反思」取代梯度更新——失敗後把錯誤語言化、存進 episodic buffer、帶記憶重試。GPT-3.5 在 HumanEval 上從 65.8% 拉到 91%（超越 GPT-4 基線），ALFWorld 從 53% 到 97%。**這是 agent 記憶式自我改進的學術先祖。**
- **ExpeL**（Zhao et al., arXiv:2308.10144, AAAI 2024）：批次離線提取跨任務洞見，用成功與失敗的對比學習，並用「受控整合」規避覆蓋式替換的風險。

### 7.3 推理策略蒸餾

- **ReasoningBank**（arXiv:2509.25140）：從成功/失敗經驗中提煉「可泛化的推理策略」（而非原始軌跡）；搭配 MaTTS（Memory-aware Test-Time Scaling）形成「更好記憶 → 更有效 scaling → 更好記憶」的正向循環。
- **ACE / Agentic Context Engineering**（arXiv:2510.04618, ICLR 2026）：Generator → Reflector → Curator 三模組，用增量 delta 更新對抗「brevity bias」和「context collapse」；讓小型開源模型在 AppWorld 上匹敵 GPT-4.1 級別的頂尖 agent。

### 7.4 技能即程序記憶

- **Voyager**（Wang et al., arXiv:2305.16291, NeurIPS 2023）：把「可執行程式碼」當成技能庫（程序記憶）——Minecraft 技術樹解鎖速度 15.3 倍。程式碼精確、可驗證，**完全規避了記憶整合失真的問題**，這是用程序記憶取代語義記憶的關鍵優勢。

### 7.5 Harness 自我進化

- **Continual Harness**（arXiv:2605.09998）：雙層迴圈——內層是 agent 行動，外層的 Refiner 每隔 F 步對 system prompt / sub-agents / skills / memory 執行 CRUD；reset-free 持續自適應。
- **The Last Harness You'll Ever Build**（arXiv:2604.21003）：兩層元進化——harness 進化層優化單任務 worker，元進化層跨領域優化「進化藍圖」本身。它對 harness 的定義非常乾淨：**harness = 提示 + 工具 + 編排 + hooks + 模型配置（除模型以外的一切）**。

### 7.6 技能品質：人工策展 vs 自動生成

一個對自動化抱有迷思的人需要記住的數字：在技能進化的實測中，**人工策展的技能帶來 +16.2pp 提升，而自動生成的技能反而 -1.3pp**（差距 17.5pp）。這與 AGENTS.md 的發現一致——AI 自動生成的指令文件通常降低性能且多耗 20%+ token。自我進化不等於「全自動」，人類的策展閘門仍是品質關鍵。

---

## 8. 驗證方法論與品質保證

### 8.1 Generator ≠ Evaluator（PGE 原則）

最核心的品質原則：**產生結果的模型不應評估自己的結果**。完成宣告前必須跑外部、機械性的驗證（測試 / lint / healthcheck），展示實際輸出（建議「前 5 行 + 後 5 行」），禁止口頭聲稱「測試通過」。LLM-as-Judge 時，**評估模型必須不同於生成模型**。

### 8.2 三層驗證

1. **確定性驗證**（毫秒級）：測試、lint、type check——這是 ground truth，不可妥協。
2. **語意驗證**（LLM-as-Judge）：評估模型 ≠ 生成模型。
3. **E2E 驗證**：Playwright / Puppeteer 等端到端測試。

驗證迴路被 Boris Cherny（Anthropic）稱為「**單一最高效的優化**」，可帶來 2–3 倍品質提升。

### 8.3 Hook 反饋速度層次（越早越便宜）

`PostToolUse（毫秒）→ PreToolUse（毫秒）→ pre-commit（秒）→ Stop（秒~分）→ CI/CD（分鐘）→ 人工審查（小時）`。一個關鍵數字：**PostToolUse hook 的成本比 PR review 低約 1000 倍**——盡量把錯誤攔在最早、最便宜的層次。Hook 的 exit code 語義：`0 = 繼續`、`1 = 警告但繼續`、`2 = 阻斷`。

### 8.4 Ratchet 升格機制

把「每次失敗」轉化為「永久防護」的六階段閉環：`OBSERVE → IDENTIFY → PROPOSE → TEST → APPLY → RECORD`。當某類失敗頻率 > 3 次/月，就把對應規則「升格」成 PreToolUse Hook（從靠模型自律變成機械強制），升格後再從指令文件移除該條規則以保持精簡——這呼應了 Mitchell Hashimoto 的原則：「一旦代理犯了錯，花時間設計解決方案，使代理永遠不再犯同樣的錯誤。」

### 8.5 冷啟動測試與知識可見性

- **Cold Start Test（冷啟動測試）**：用全新 agent session、僅依賴倉庫內容，測試能否回答五個基本問題——系統是什麼、如何運行、如何驗證、當前進度、下一步。
- **KVG（Knowledge Visibility Gap）**：倉庫外重要知識 / 全部重要知識，目標 < 10%。把「只在某人腦中」的知識降到最低。

---

## 9. 多代理共識與 Gap 分析方法論

當需要高可信度的判斷（例如「某個改進建議該不該採納」），單一 agent 容易自我強化偏誤。**多代理共識投票**提供了一個對抗機制：

- 三個「不同方法論」的 agent 各自獨立投票（例如：分層信度來源 / 無人值守綜合 / 對抗式精煉），決策規則為「**≥ 2/3 同意 → GO**」。
- **強制 Vote Matrix**：必須給出「每個 agent × 每個選項」的數字分數表，禁止只給敘述性自評。
- **證據門檻**：每個 agent 必須 `讀檔 ≥ 3` 且 `grep 命令 ≥ 2`；parent 必須親自抽驗至少一條 grep 命令重跑。

實務中發現的兩個關鍵陷阱：(1) **元穩定 / Split-Brain**——兩個分支可能在極短時間內各自宣稱「2/3 共識」但結論相反，需要第三輪打破；(2) **虛報驗證**——sub-agent 聲稱「已 grep 確認」但其工具呼叫紀錄中根本沒有 grep。教訓：**任何 agent 的「verdict」都不是證據，採信前必須機械性重驗**。

**Skill Gap 評估**也採類似的量化評分（使用頻率 30% + 不可替代性 25% + 維護成本 20% + 簡潔度 15% + 實戰驗證 10%），設定明確門檻（例如 ≥ 2.0 才加入），避免「為了功能而功能」的膨脹。

---

## 10. 生態系統趨勢與外部框架

### 10.1 競爭軸線下移

前沿模型能力差距縮小後，定價戰成為新競爭軸，而「選模型 = 選 harness 生態」的遷移成本被嚴重低估。業界開始談「**Two-Slice Team**」——2 名工程師搭配 AI 達成傳統 8–10 人的產出；某些團隊每月合併 1,000+ PR。但也有反面警告：一份研究指 **73% 的工程師在使用 AI 後技術理解力下降**（「Cognitive Surrender」——可以外包思考，但無法外包理解）。

### 10.2 代表性外部框架（通用化）

- **多角色技能框架（如 gstack）**：把完整開發生命週期（Think → Plan → Build → Review → Test → Ship → Reflect）封裝成 40+ 個 slash-command 技能，核心模式是「**Thin Harness + Fat Skills**」——框架本身輕量，業務邏輯全在技能裡。GitHub 星數約 101,000 `[unverified — 來源報告自身標注該數字無法即時驗證；正文另記 ~20,000，同步更新節修正為 ~101,000]`。
- **個人持久知識圖（如 gbrain）**：用 hybrid scoring（vector + BM25 + RRF + reranker）搭配 typed graph edges（`works_at` / `invested_in` 等），比純向量搜尋在 rank@5 上 +31.4pp 精準度。一句話總結它的價值主張：「搜尋給你原始頁面，知識圖給你答案。」
- **背景記憶整合引擎（如未發布的 autoDream）**：四階段（Orient → Gather → Consolidate → Prune），在使用者長時間閒置時由 forked subagent 執行，輸出上限 25KB——這正是第 6.4 節「記憶整合須顯式、有上限」原則的產品化體現。
- **持久背景 daemon（如未發布的 KAIROS）**：always-on，週期性 tick，單次工具執行設 15 秒 blocking budget，並有推送通知 / 檔案投遞 / PR 訂閱三種主動能力。
- **自我演化 agent 框架（如 Hermes）**：三階段——Experience Capture（複雜任務後自動生成技能）→ Active Learning（使用中迭代改良）→ Persistence（跨 session 全文搜尋記憶），並以 `usage_count` / `quality_score` / `evolution_stage`（draft/tested/stable/mature）做品質 telemetry。

### 10.3 供應鏈安全成為生產事故

agent 生態的開放性帶來了新的攻擊面，已從理論變成實際生產事故：

- 公開技能倉庫的**惡意率達 12%**（實測）。某次大規模篩選中，247 個社群技能只有 23 個通過品質門檻（9.3% pass rate）。
- npm 套件投毒（針對 agent 工具用戶植入後門）、GitHub 大規模惡意 commit 注入（6 小時內數千個）等事件已發生。
- 模型本身的洩漏也暴露了未發布功能——某次 source map 洩漏暴露了 51 萬行程式碼、1,906 個檔案，間接揭示了上述 autoDream / KAIROS 等內部元件。

防禦面的對應：研究型 agent **不給 Bash 與寫入工具**、外部輸入一律 `<untrusted_objective>` 包裹、PreToolUse hook 阻斷危險命令、不可逆操作（DELETE / DROP TABLE / `terraform destroy` / `git push --force`）一律先顯示摘要再二次確認。

### 10.4 成本現實衝擊

「能力可行」不等於「成本可行」。已被報導的成本事故包括：某大型企業因帳單爆炸而要求工程師停用某 agent；某公司在 4 月就燒完全年 AI 預算；訂閱制正逐步讓位給 token 計費。這使得第 5 節的成本工程（caching、模型分級、advisor 模式、輸出紀律）從「優化項」變成「生存項」。

---

## 11. 前沿趨勢與預測

1. **Harness 標準化與透明化**：HarnessCard / HarnessCard 類的揭露標準會像 Model Card 一樣普及，讓 harness 設計可比較、可審計。
2. **自動 Harness 進化（AHE）走向實用**：透過觀測 agent 行為自動調整 harness 組件的機制（如 HARBOR 的貝葉斯最佳化，Terminal-Bench 10 輪迭代 69.7% → 77.0%，跨模型轉移 +5.1–10.1pp）會逐步落地——但人類策展閘門仍不可或缺（見 §7.6）。
3. **記憶治理（Mnemonic Sovereignty）成為一級議題**：對「寫入 / 讀取 / 更新 / 遺忘」的可驗證治理，會與安全合規綁定（記憶安全調查 arXiv:2604.16548）。
4. **Agent teams 取代 single-agent**：「Single-agent workflows are dead」的宣言指向多 agent 編排，但要避免 §5.1 的協調錯誤放大陷阱——數量不是答案，編排才是。
5. **精簡 harness 勝出**：實證顯示精簡 harness（~11.4K tokens）可超越冗長 harness（~50.8K tokens）——「少即是多」會持續被數據驗證。

---

## 12. 可立即實作的行動建議

1. **把指令文件砍到 12 條核心規則以內**，總量 < 200 行、< 4,000 tokens。對每一行做剪枝測試（「移除它，模型會犯錯嗎？」）。
2. **建立三層 context tiering**：核心規則全域載入、領域規則路徑觸發、技能顯式觸發。優先把全域規則改成路徑範圍（可省 70–82% 啟動 token）。
3. **導入 PEV 循環**：每個任務先寫「可機械驗證的完成標準」（測試 / healthcheck / 特定輸出），再執行、再驗證。
4. **建立獨立驗證迴路**：至少一個確定性驗證（測試/lint），並確保 LLM 評估者 ≠ 生成者。把錯誤攔在 PostToolUse / PreToolUse hook（比 PR review 便宜 1000 倍）。
5. **委派只用於資訊蒐集**：研究/搜尋/審查才 fan-out（上限 4，只給 Read/Grep/Glob）；實作交給單一 agent。
6. **記憶採 Episodic-First**：原始 episode 為一級證據，把整合設成顯式、有上限、可回滾的操作，定期（14–30 天）做壓縮而非連續整合。
7. **成本工程常駐**：開啟 prompt caching（守五不原則）、工具延遲載入、按檔案數選模型、用 advisor 模式（便宜執行 + 旗艦顧問）。
8. **安全紅線機械化**：外部輸入包裹隔離、研究 agent 不給 Bash、不可逆操作強制二次確認、PreToolUse hook 阻斷危險命令。
9. **建立 Ratchet 閉環**：每次失敗都記錄並評估是否升格成 hook；高頻失敗從「靠自律」升級成「機械強制」。
10. **高風險判斷用多代理共識**：≥ 2/3 投票 + 強制 vote matrix + 證據門檻（讀檔 ≥ 3 / grep ≥ 2），且 parent 親自抽驗——任何 verdict 都不是證據。

---

## 附錄 A：核心論文索引

> 以下 arXiv ID 與發表場所均源自前置報告語料；標題以報告中出現的形式為準。

**記憶架構**
- Generative Agents — Park et al., arXiv:2304.03442, UIST 2023
- Reflexion — Shinn et al., arXiv:2303.11366, NeurIPS 2023
- MemGPT — Packer et al., arXiv:2310.08560
- Voyager — Wang et al., arXiv:2305.16291, NeurIPS 2023
- MemoryBank — Zhong et al., arXiv:2305.10250, AAAI 2024
- HippoRAG — Gutiérrez et al., arXiv:2405.14831, NeurIPS 2024
- Useful Memories Become Faulty — Zhang et al., arXiv:2605.12978
- Rethinking Memory（六大操作） — Du et al., arXiv:2505.00675
- MemoryOS — arXiv:2506.06326
- Mem0 — arXiv:2504.19413
- A-MEM — Xu et al., arXiv:2502.12110, NeurIPS 2025
- Chronos — arXiv:2603.16862
- Hindsight — arXiv:2512.12818
- Beyond Context Window — arXiv:2603.04814
- ACE（Agentic Context Engineering） — arXiv:2510.04618, ICLR 2026
- 記憶分類三維框架 — Wu et al., arXiv:2504.15965
- 記憶儲存四分類 — Zhang et al., arXiv:2404.13501
- CoALA（認知架構） — Sumers et al., arXiv:2309.02427
- AgeMem（統一記憶模型 + GRPO） — arXiv:2601.01885

**Harness 工程**
- NLAH（Natural Language Agent Harnesses） — arXiv:2603.25723
- AgentOpt（pipeline 模型分配） — 2026-04 `[C]`
- CAR Framework（Control-Agency-Runtime） — He et al., 2026-04-23
- Continual Harness — arXiv:2605.09998
- The Last Harness You'll Ever Build — arXiv:2604.21003
- Meta-Harness Optimization — arXiv:2603.28052
- ReasoningBank — arXiv:2509.25140
- Agent Harness Survey（六維 H=(E,T,C,S,L,V)） — 2026-04
- 記憶安全調查（Mnemonic Sovereignty） — arXiv:2604.16548
- Skill-Issue Harness Engineering（Terminal-Bench #33→#5） — 2026-03-12
- SWE-agent（ACI 概念） — 2024
- ReasoningBank / HARBOR / AHE / Vesper 等 — 詳見前置深度研究

**學術根據標注**：少數論文（如 NLAH 的 TACL 根據、CAR 的最終 arXiv 編號）在前置報告中標為 `[unverified]` 或編號待確認，本報告沿用該標注。

---

## 附錄 B：量化數據總表

| 主題 | 數據 | 來源 |
|------|------|------|
| 工具格式調整對準確率 | 6.7% → 68.3%（10×） | 2026-05-16/19 |
| 純 harness 改善（Terminal-Bench 2.0） | 52.8% → 66.5%（+13.7pp） | 2026-05-16 |
| 五子系統補齊（模型不變） | 成功率 20% → ~100% | 2026-05-17 |
| Harness 巡檢 | 成功率 75% → 95%+ | 2026-05-28 |
| AI agent 專案無法上線 | 88% | 2026-05-19 |
| 指令文件 > 200 行合規率 | 76% → 52% | 2026-05-16/18 |
| 12 條規則錯誤率（甜蜜點） | 3% | 2026-05-18/25 |
| 路徑範圍規則 session token | -82% | 2026-05-18 |
| 工具延遲載入 MCP token | 51,000 → 8,500（-83.3%） | 2026-05-18 |
| 記憶檔案重構 | 35.5KB → 3.5KB（-90%） | 2026-05-18 |
| 輸出紀律 token 節省（英/繁中） | -80.6% / -86.2% | 2026-05-12/16 |
| NLAH policy token | 60.1K → 2.9K（-95%） | 2026-05-25 |
| 跨模型移植損失（好/壞 harness） | < 5% / > 40% | 2026-05-16 |
| 強 Planner vs 弱 Planner（AgentOpt） | 31.71% vs 74.27% `[C]` | 2026-05-16 |
| Advisor 模式（Haiku+Opus）成本 | -85% | 2026-05-16 |
| 多代理錯誤放大（Bag-of-Agents） | 17.2× | 2026-05-12 |
| Prompt cache 命中費率 | $0.30/MTok（一般 $3） | 2026-05-16 |
| 記憶整合崩潰（GPT-5.4 ARC-AGI） | 100% → 46% | 2026-05-22 |
| MemoryOS（LoCoMo F1） | +49.11% | llm-memory-deep-research |
| Mem0 vs OpenAI（LOCOMO） | +26%，成本 -90% | llm-memory-deep-research |
| Reflexion（HumanEval GPT-3.5） | 65.8% → 91% | 2026-05-22 |
| Voyager 技術樹加速 | 15.3× | 2026-05-22 |
| Chronos（LongMemEvalS） | 95.60% | llm-memory-deep-research |
| 人工 vs 自動技能 | +16.2pp vs -1.3pp | 2026-05-25 |
| PostToolUse hook vs PR review 成本 | 1/1000 | 2026-05-19 |
| 公開技能倉庫惡意率 | 12% | tweets-synthesis |
| 社群技能篩選通過率 | 247 → 23（9.3%） | tweets-synthesis |
| 論文分析總數 | 84–97 篇 / 6 領域 | 2026-05-25 |

---

## 附錄 C：術語對照表（內部代號 → 通用意義）

| 術語 | 通用意義 |
|------|---------|
| **Harness Engineering** | 圍繞 AI 模型建立的完整執行環境工程（指令/工具/驗證/狀態/安全） |
| **Context Engineering** | 把 context 當稀缺資源管理：填什麼、怎麼排序、何時壓縮 |
| **HMF（Harness–Model Fit）** | harness 設計與模型能力邊界的對齊程度 |
| **NLAH** | 把 harness 控制邏輯寫成可編輯的自然語言文件（可移植/可審計/可比較） |
| **CAR** | Harness 三層分解：Control（約束）/ Agency（行動空間）/ Runtime（時間性治理） |
| **PEV** | Plan-Execute-Verify 執行循環 |
| **PGE / Generator≠Evaluator** | 生成結果的模型不可自評，須獨立評估者 |
| **TYPE A/B/C/D** | 規則分類：A 強制（不可移除）/ B 規則+解釋 / C 背景 / D 連結 |
| **Context Rot / Lost-in-the-Middle** | context 變長後中段注意力衰減，長任務退化 |
| **Ratchet 機制** | 把每次失敗轉成永久防護的升格閉環 |
| **Cold Start Test** | 全新 session 僅靠倉庫內容能否回答五個基本問題 |
| **KVG** | 倉庫外重要知識 / 全部重要知識，目標 < 10% |
| **Episodic-First** | 優先保留原始 episode 作一級證據，整合設為顯式高風險操作 |
| **STM/MTM/LTM** | 短期/中期/長期記憶三層架構 |
| **Mnemonic Sovereignty** | 記憶主權：對寫入/讀取/更新/遺忘的可驗證治理 |
| **Thin Harness + Fat Skills** | 框架輕量、業務邏輯全在技能層的設計模式 |
| **Two-Slice Team** | 少數工程師 + AI 達成傳統大團隊產出的協作模式 |
| **Advisor 模式** | 便宜模型執行 + 旗艦模型顧問的成本優化組合 |
| **Fan-out** | 單一訊息同時啟動多個 sub-agent 的並行模式（上限 4） |

---

## 附錄 D：本報告整併的前置報告清單

本報告整併並重寫自 `research/reports/` 下前置研究（2026-05-12 → 2026-05-31），原檔多數保留作為一級證據（Episodic-First）。**2026-06-05 清理**：其中 8 份已執行過的過程產物（cross-validation / auto-load-50round / nlah-audit / gap-analysis-consensus / third-round-consensus / harness-full-audit / memory-control-architecture / refs-genericization）已移除，其結論已內化進 workspace 規則或本整併報告。主要來源分群（已移除者標 ~~刪除線~~）：

- **Harness 工程 / Auto-load**：`2026-05-17-harness-engineering`、`2026-05-16-harness-engineering-model-fit`、`2026-05-19-harness-verification-methods`、~~`2026-05-18-auto-load-50round-optimization`~~、`2026-05-18-auto-load-token-best-practices`、`2026-05-25-reduce-auto-load-token`、`harness-engineering-deep-research`、`2026-05-28-harness-evolution-plan`、~~`2026-05-26-nlah-audit-review`~~
- **Claude Code 最佳實踐 / 委派**：`2026-05-16-claude-code-best-practices`、`2026-05-17-claude-code-subagent-delegation-gotchas`、`2026-05-18-karpathy-mnilax-best-solution`、`2026-05-12-best-practices-simplicity`、~~`2026-05-15-cross-validation-report`~~、`2026-05-23-implementation-research-garry-tan-claude-code`
- **LLM 記憶 / 自我進化 / 論文**：`2026-05-22-llm-memory-control-comprehensive-survey`、`2026-05-25-papers-analysis`、`2026-06-05-harness-memory-self-evolution-synthesis`、~~`2026-05-31-memory-control-architecture`~~、`llm-memory-deep-research`、`2026-06-05-skill-evolution-report`
- **生態趨勢 / 框架 / 共識方法論**：`2026-05-16-ai-news-synthesis-report`、`2026-05-15-tweets-synthesis-report`、`2026-05-23-gstack-deep-research`、`2026-05-23-autodream-kairos-deep-research`、`2026-05-25-workspace-gbrain-hermes-update`、`2026-05-25-workspace-recommendations`、`2026-05-25-github-hermes-evolution`、`2026-05-26-skill-gap-analysis`、~~`2026-05-28-gap-analysis-consensus-results`~~、~~`2026-05-28-third-round-consensus`~~、`2026-05-31-claude-dir-inventory`、~~`2026-05-31-harness-full-audit`~~、~~`2026-05-31-refs-genericization-audit`~~、`ORCHESTRATION-harness-memory-deep-research`

---

*本報告為前置語料的通用化整併與重寫。所有量化數據與論文引用均可回溯至上述前置報告；標注 `[unverified]` / `[C]` 者表示前置報告中即未經本地完全驗證，沿用其保守標注。*
