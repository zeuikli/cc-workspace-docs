# Lecture 03：Context Engineering

## 學習目標

完成本課後，你將能夠：

- 解釋 Context Rot 的機制及其量化數據
- 說明為什麼「更大的 context window」不是解法
- 設計使用 Sub-agent 作為 Context Firewall 的架構
- 套用 Claude 5 世代的六條 context engineering 新規則，並知道哪些東西**不可以**刪
- 正確配置 Prompt Caching，並說明五個會炸掉快取的操作

## 核心概念

### Context Rot：為什麼 Context 越長越危險

Context Rot 指的是：隨著 context window 中的 token 數增長，模型的輸出品質系統性下降的現象。

**Chroma NIAH 研究的量化數據**：

- 18 個模型在 NIAH（needle-in-a-haystack）任務上**全部**隨 context 增長而下降
- 即使是簡單任務（文字複製）在 2,500+ token 後也崩潰
- 加入語義相關但不正確的 distractor -> 性能**複合下降**

**最反直覺的發現**：隨機排列的 haystack 表現反而**優於**邏輯連貫文件（18 個模型一致）。為什麼？因為邏輯連貫的文件讓模型更難定位到正確的「針」——它會被大量相關但不精確的內容干擾。

**Context 焦慮（Context Anxiety）**：

Anthropic 觀察到一個特殊模式：當 agent 感覺 context 快滿了，它們會：
1. 匆忙結束當前工作
2. 跳過驗證步驟
3. 選一個簡單方案而不是最優方案

這直接導致任務品質下降和「宣布完成但實際未完成」的失敗。

### 為什麼 1M Context Window 是虛假安全感

很多人的誤解：「context window 越大，問題就越少」。

Chroma 研究的結論恰恰相反：**Context Rot 不能靠更大的 context window 解決**。更大的 context 意味著更多的潛在噪音，更多的干擾源，反而可能加劇 Context Rot。

| 常見誤解 | 實際情況 |
|---------|---------|
| 把所有文件都塞進 context | 大量不相關內容降低針對性 |
| 依賴更大的 context window | 噪音和干擾也等比例增加 |
| 長 session 保持完整歷史 | 越長的 session context 越脆弱 |

**唯一的結構性解法**：Context 切割（sub-agent + 獨立 context）。

### Sub-Agent 作為 Context Firewall

Sub-agent 的本質是 context 隔離。理解這個比知道怎麼建立 sub-agent 更重要：

```
Sub-Agent = Context Firewall

主 Agent 只看到：
  -> 給 sub-agent 的 prompt（輸入）
  -> sub-agent 的最終結論（輸出）

中間過程（grep 輸出、工具呼叫、中間檔案讀取）
  -> 留在 child context
  -> 不污染主 thread
```

**實踐意義**：一個複雜任務，如果讓同一個 agent 從頭到尾執行，它的 context 會不斷增長，最終 Context Rot 導致品質下降。如果把任務拆分給多個 sub-agent，每個 sub-agent 都在乾淨的 context 中工作，主 agent 只看到最終結論，context 保持緊湊。

**五來源一致共識（HumanLayer + RESEARCH.md + Daily Dose DS + Chroma + Weng）**：Sub-agent 是 Context Rot 的唯一結構性解決方案。

### Claude 5 世代的六條新規則

2026-07-24 官方公布了一個會改變寫作習慣的實證：

> Anthropic 為 Claude Opus 5 / Fable 5 **刪掉了 Claude Code system prompt 的 80% 以上**，在其 coding evals 上**無可量測退化**。

根因不是「模型變強所以不需要 context 工程」，而是**舊 prompt 對模型 over-constrain，且指令彼此打架**——同一次請求裡同時出現「leave documentation as appropriate」與「DO NOT add comments」。新世代模型會花推理預算去調解衝突訊息。

**「多加一條保險條文」不是零成本**——這是本節最重要的一句話。

| # | Then → Now | 內容 |
|---|-----------|------|
| 1 | **Judgment over rules** | 用「寫得像周遭程式碼」取代硬性條數禁令，讓模型判斷 |
| 2 | **Tool design over examples** | 與其給使用範例（會限縮探索），不如把參數設計得有表達力、enumeration 清楚（`status: pending/in_progress/completed`）|
| 3 | **Progressive disclosure over upfront info** | 驗證與 code review 指導從 system prompt 移出，改成需要時才呼叫的 Skill；部分工具改 **deferred loading**（先 `ToolSearch` 取 schema 才可呼叫）|
| 4 | **Simplified descriptions over repetition** | 同一指令不要在 system prompt 與 tool description 重覆；指令的正確歸宿是 tool description |
| 5 | **Auto-memory over manual saving** | 新世代自動保留相關記憶，不必事事用 `#` 熱鍵手寫進 CLAUDE.md |
| 6 | **Rich references over simple specs** | 除了 markdown 規格，也吃 HTML artifact / test suite / code sample / rubric |

### Context Assembly 四層

| 層 | 承載 |
|----|------|
| System prompt | 產品脈絡與核心目的（平台持有）|
| CLAUDE.md | 輕量 repo 描述 + critical gotchas |
| Skills | 編碼團隊意見的輕量指南 |
| References | code sample / spec / mockup / test suite |

工具面已經配合：`/doctor` 從 v2.1.206 起會主動提出 `CLAUDE.md` 精簡建議；`claude-api` skill 的 `prompt-audit` 子命令（v2.1.213）專門稽核「為舊世代寫的 prompt 與 tool description」。

### 哪些東西不在「可刪」之列

這一節是為了防止上一節被誤讀。

**可刪**：為補償模型弱點而堆的程序性鷹架——步驟拆解、重複提醒、防呆條文、對模型現在已經做得很好的事下的細節指令。

**不可刪**：

- 驗證閘門（測試、lint、type check 的強制執行）
- 不可逆操作的確認（`DROP`、prod deploy、金鑰輪替、`--force` push、`rm -rf`、`terraform destroy`）
- 安全邊界（sandbox 設定、permission deny 清單、hooks）

理由是**能力悖論**：能力提升不得換取更少驗證。越強的模型越有能力把 gate 弄綠——這是 [Lecture 10](/lectures/lecture-10-verification/) 的主題。

而且官方自己的動作是一致的：在刪 system prompt 的同一個季度，他們把 `/verify` 與 `/code-review` 的**自動觸發關掉**（v2.1.215），要求由 harness 明確呼叫。**刪鷹架，強化閘門**——這兩件事同時發生，不矛盾。

### Prompt Caching：Token 優化的正確姿勢

Prompt Caching 讓重複出現在 prompt 中的大塊 token（如 CLAUDE.md 內容、系統指令、大型程式碼庫上下文）只需計算一次。

**Thariq Shihipar（Claude Code 團隊）的核心教訓**：

1. **Caching 的前提是 prefix 穩定**：被 cache 的內容必須在每次請求中保持相同。如果你每次都稍微修改系統提示，cache 就會失效。
2. **Cache 鍵是 prefix**，不是 hash：完全匹配的 prefix 才能命中 cache。
3. **長靜態 context 最適合 caching**：CLAUDE.md、大型程式碼庫的內容摘要、API 文件——這些幾乎不會變，非常適合 cache。
4. **Dynamic content 放在後面**：把會變化的部分（當前任務、用戶輸入）放在 prompt 末尾，把靜態部分（指令、context）放在前面。

**April 23 Postmortem 的教訓**：Caching loop bug 讓 thinking history 每輪被清空（應每小時清空一次），導致用戶反映「forgetful and repetitive」。Caching 配置錯誤的代價可以是直接用戶體驗下降。

### 五個會炸掉快取的操作

Prompt Caching 的機制是**逐 token 從頭比對前綴，遇到第一個不同 token 即停止快取**。所以「前綴一動全斷」。

| # | 禁令 | 為什麼 | 正確做法 |
|---|------|--------|---------|
| 1 | **動態事實寫進穩定前綴** | 時間戳、檔案變更寫進 system prompt = 每次前綴都不同 | 用後續訊息注入，包在 `<system-reminder>` 標籤裡 |
| 2 | **Mid-session 換模型** | 快取是**模型專屬**的，換模型等於從頭付費 | 開 **subagent**（各有獨立 context 與快取）|
| 3 | **對話中增刪工具** | 工具定義是前綴的一部分 | 保留所有定義，不需要的用 stub + `defer_loading: true` |
| 4 | **Compact 時換 system prompt / tools** | 後續 session 失去快取匹配 | Compact 請求必須用**與父對話完全相同的** system prompt + tools |
| 5 | **改 CLAUDE.md（session 中）** | 它是穩定前綴的一部分 | 改完開新 session |

**分層結構（靜態 → 動態）**：

```
1. System prompt + Tools      ← 最穩定，全域快取
2. 專案檔案 / CLAUDE.md        ← 中度穩定，跨 session 快取
3. Session context            ← 僅當次 session
4. 對話訊息（最新輪次）        ← 每次請求不同
```

### Cache Hit Rate 是健康指標，不是優化項

Claude Code 團隊的內部實踐值得直接抄：

> Cache hit rate 下降 → **觸發 incident 流程**，找出導致失效的變更（通常是 system prompt 動態注入、工具增刪、模型切換）。

```python
cache_hit_rate = response.usage.cache_read_input_tokens / response.usage.input_tokens
```

Claude Code 端從 v2.1.213 起，Stats 面板會分列 input / output / **cache read / cache write**——不必自己算。

一個容易忽略的失效來源：**Fable 5 的安全分類器**會把 cyber / bio-chem / distillation 相關請求路由到 Opus 4.8（< 5% sessions），**路由過去的 session 不共享快取**。這是你控制不了但需要知道的。

### Token Budget Management

長任務消耗大量 token 的根源往往不是「做了太多事」，而是「做了太多重複的事」：

| 常見 Token 浪費 | 解法 |
|--------------|------|
| 每輪都重新探索專案結構 | CLAUDE.md 提供結構摘要 |
| 重複讀取相同的大型檔案 | Prompt Caching |
| 冗長的中間結果污染 context | Sub-agent 做 context 切割 |
| 驗證過程佔用主 context | 獨立 evaluator agent |

**Addy Osmani 的建議**：用 Sub-agent 委派大量 token 消耗的工作（探索、搜尋、分析），主 agent 只保留 task-level 的 context。

### Context Compaction

Claude Code 的 `/compact` 指令可以壓縮當前 session 的 context，用摘要取代詳細歷史。

使用時機：
- Session 已經很長，但任務還沒完成
- 你知道前面大部分的工作已經完成，只需要保留摘要

限制：壓縮後某些細節可能遺失。建議在 compaction 之前讓 Claude 把重要發現寫入 MEMORY.md。

Pre-compact hook 範例：

```json
{
  "hooks": {
    "PreCompact": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "echo 'About to compact — ensure MEMORY.md is updated'"
          }
        ]
      }
    ]
  }
}
```

## 程式碼範例

### Sub-agent 架構的基本模式

```python
# 主 agent 的邏輯（偽碼）
def main_agent_task(large_codebase_dir):
    # 不讓主 agent 直接掃描整個 codebase（會污染 context）
    # 而是啟動一個 sub-agent 來做這件事
    
    search_result = spawn_sub_agent(
        task="在 {dir} 裡找到所有 API endpoint 定義，回傳一個清單".format(dir=large_codebase_dir),
        context_limit=8192  # sub-agent 只有有限的 context
    )
    
    # 主 agent 只看到 search_result（一個清單）
    # 不看到 sub-agent 掃描過程中讀取的所有檔案內容
    
    implement_changes(search_result)
```

在 Claude Code 中，使用 `/agent` 或 `Task()` tool 建立 sub-agent：

```
# 在主 agent 中
Task: 掃描 src/ 目錄，找出所有使用了 deprecated v1 API 的位置，返回檔案路徑和行號清單。
不需要修改任何檔案，只需要返回清單。
```

### 設計良好的 Prompt（利用 Caching）

```
[SYSTEM - 靜態部分，適合 cache]
你是一個 Python API 專家。

專案規則：
- 使用 FastAPI + SQLAlchemy 2.0
- 所有 endpoint 需要 OAuth 2.0
- 測試框架：pytest
- 驗證命令：pytest tests/ && mypy src/ --strict

[USER - 動態部分，每次不同]
現在的任務：在 /api/v2/users 下新增一個用戶偏好設定 endpoint。
```

### 利用 path-scoped rules 減少不必要的 context 載入

```markdown
<!-- CLAUDE.md 根檔案 -->
# My Project

## 全域規則（每次 session 都載入）
- 使用 Python 3.12
- 驗證命令：pytest && mypy --strict

## 路徑規則（按需載入）
- 前端：@.claude/rules/frontend.md
- 後端：@.claude/rules/backend.md
```

這樣只有 Claude 在處理前端檔案時，才會載入前端規則；不處理前端時，這些 token 不會佔用 context。

### 監控 Context 使用狀況

```bash
# 查看當前 session 的 token 使用情況
/status

# 查看 cache 命中率（在 verbose 模式下）
claude --verbose

# 手動壓縮 context
/compact
```

## 常見問題與注意事項

**Q：多大的 context 算「太大」？**

A：沒有絕對標準，但 Chroma 研究顯示 2,500+ token 後即使是簡單任務也開始出現問題。在實踐中，建議把超過 1 萬 token 的長任務切分給多個 sub-agent 處理。

**Q：Sub-agent 的額外開銷值得嗎？**

A：是的，因為 Context Rot 導致的品質下降遠比 sub-agent 的額外延遲代價更高。而且 Prompt Caching 可以大幅降低 sub-agent 的 token 成本（sub-agent 的系統提示如果是靜態的，可以被 cache）。

**Q：Prompt Caching 需要特別配置嗎？**

A：Claude Code 在 API 層面自動處理 prompt caching，你不需要手動標記哪些部分要 cache。但你需要確保靜態內容（CLAUDE.md、系統指令）在 prompt 中的位置固定（前面），動態內容（任務描述）放在後面，這樣 prefix 才能穩定命中 cache。

**Q：Context Compaction 和 Sub-agent 有什麼區別？**

A：Compaction 是壓縮當前 agent 的歷史（有損，用摘要替代細節）。Sub-agent 是新建一個獨立 context 來執行子任務（無損，原始 context 不受影響）。兩者解決的是不同的問題。

**Q：NIAH 研究裡說「邏輯連貫的 haystack 比隨機排列更差」，這意味著什麼？**

A：這說明模型在面對大量相關但不完全準確的內容時，更容易被「近似正確」的答案干擾。這對 RAG（Retrieval-Augmented Generation）系統設計有重要影響：寧可多次精確查詢，不要一次返回大量相關文件。

## 本課小結

- **Context Rot 是量化的**：18 個模型全部隨 context 增長而下降；2,500+ token 後即使簡單任務也崩潰。
- **1M context window 是虛假安全感**：更大的 context 帶來更多噪音，Context Rot 沒有消失。
- **Sub-agent 是唯一結構性解法**：隔離中間過程，主 agent 只看最終結論。Context Firewall。
- **Prompt Caching 的前提是 prefix 穩定**：靜態指令放前面，動態任務放後面。
- **Context 焦慮要提前預防**：在 CLAUDE.md 裡說清楚「context 不夠時應該停下來等待，而不是跳過驗證」。
- **Claude 5 世代六條新規則**：judgment over rules、tool design over examples、progressive disclosure、去重、auto-memory、rich references。system prompt −80% 無退化是實證。
- **可刪的是鷹架，不是閘門**：驗證、不可逆操作確認、安全邊界不在精簡範圍內。
- **五個炸快取的操作**：動態事實入前綴、mid-session 換模型、增刪工具、compact 換 prompt、session 中改 CLAUDE.md。

## 延伸閱讀

- [Lecture 01：Claude Code 與 Harness 基礎](/lectures/lecture-01-foundations/) — Context Rot 的五層防禦框架
- [Lecture 04：Harness 三層架構](/lectures/lecture-04-harness-architecture/) — Evaluator 作為獨立 context 的設計
- [Lecture 08：Sub-agents 與 Dynamic Workflows](/lectures/lecture-08-subagents-workflows/) — Context Firewall 的實作與扇出治理
- [Lecture 09：模型選型與 Effort 經濟學](/lectures/lecture-09-model-selection/) — 換模型對快取的破壞
- [Lecture 11：MCP 整合](/lectures/lecture-11-mcp/) — deferred loading 與 Tool Search

**官方一手來源**

- [The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)（2026-07-24）
- [Lessons from building Claude Code: Prompt caching is everything](https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything)（2026-04-30）
- [Using Claude Code: session management and 1M context](https://claude.com/blog/using-claude-code-session-management-and-1m-context)（2026-04-15）— rewind / clear / compact 決策框架
- [Seeing like an agent: how we design tools in Claude Code](https://claude.com/blog/seeing-like-an-agent)（2026-04-10）— Progressive Disclosure 與約 20 個工具上限
- [Building agents that reach production systems with MCP](https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp)（2026-04-22）— Tool Search 降 85%+ token
- [Chroma: Context Rot Research](https://www.trychroma.com/research/context-rot)
- [LangChain: Context Management for Deep Agents](https://www.langchain.com/blog/context-management-for-deepagents)

**站內研究歸檔**

- [Claude 5 世代 Context Engineering 新規則](/research/best-practices/46-context-engineering-claude5)
- [Prompt Caching 核心教訓（Thariq）](/research/best-practices/28-thariq-prompt-caching-lessons) · [官方 Prompt Caching 技術指南](/research/best-practices/08-prompt-caching)
