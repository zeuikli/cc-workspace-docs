# Lecture 03：Context Engineering

## 學習目標

完成本課後，你將能夠：

- 解釋 Context Rot 的機制及其量化數據
- 說明為什麼「更大的 context window」不是解法
- 設計使用 Sub-agent 作為 Context Firewall 的架構
- 正確配置 Prompt Caching 減少 token 使用

## 核心概念

### Context Rot：為什麼 Context 越長越危險

Context Rot 指的是：隨著 context window 中的 token 數增長，模型的輸出品質系統性下降的現象。

**Chroma NIAH 研究的量化數據**：

- 18 個模型在 NIAH（needle-in-a-haystack）任務上**全部**隨 context 增長而下降
- 即使是簡單任務（文字複製）在 2,500+ token 後也崩潰
- 加入語義相關但不正確的 distractor → 性能**複合下降**

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
  → 給 sub-agent 的 prompt（輸入）
  → sub-agent 的最終結論（輸出）

中間過程（grep 輸出、工具呼叫、中間檔案讀取）
  → 留在 child context
  → 不污染主 thread
```

**實踐意義**：一個複雜任務，如果讓同一個 agent 從頭到尾執行，它的 context 會不斷增長，最終 Context Rot 導致品質下降。如果把任務拆分給多個 sub-agent，每個 sub-agent 都在乾淨的 context 中工作，主 agent 只看到最終結論，context 保持緊湊。

**五來源一致共識（HumanLayer + RESEARCH.md + Daily Dose DS + Chroma + Weng）**：Sub-agent 是 Context Rot 的唯一結構性解決方案。

### Prompt Caching：Token 優化的正確姿勢

Prompt Caching 讓重複出現在 prompt 中的大塊 token（如 CLAUDE.md 內容、系統指令、大型程式碼庫上下文）只需計算一次。

**Thariq Shihipar（Claude Code 團隊）的核心教訓**：

1. **Caching 的前提是 prefix 穩定**：被 cache 的內容必須在每次請求中保持相同。如果你每次都稍微修改系統提示，cache 就會失效。
2. **Cache 鍵是 prefix**，不是 hash：完全匹配的 prefix 才能命中 cache。
3. **長靜態 context 最適合 caching**：CLAUDE.md、大型程式碼庫的內容摘要、API 文件——這些幾乎不會變，非常適合 cache。
4. **Dynamic content 放在後面**：把會變化的部分（當前任務、用戶輸入）放在 prompt 末尾，把靜態部分（指令、context）放在前面。

**April 23 Postmortem 的教訓**：Caching loop bug 讓 thinking history 每輪被清空（應每小時清空一次），導致用戶反映「forgetful and repetitive」。Caching 配置錯誤的代價可以是直接用戶體驗下降。

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

## 延伸閱讀

- [Lecture 01：Claude Code 與 Harness 基礎](/lectures/lecture-01-foundations/) — Context Rot 的五層防禦框架
- [Lecture 04：Harness 三層架構](/lectures/lecture-04-harness-architecture/) — Evaluator 作為獨立 context 的設計
- [LangChain: Context Management for Deep Agents](https://www.langchain.com/blog/context-management-for-deepagents)
- [Chroma: Context Rot Research](https://www.trychroma.com/blog/context-rot)
