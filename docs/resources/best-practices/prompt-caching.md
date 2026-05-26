# Prompt Caching 工程

整合自 Anthropic 官方技術文件與 Thariq Shihipar（Claude Code 核心工程師）的第一手生產經驗。

> **核心主張**（Thariq Shihipar）：「Cache rules everything」——長跑型 Agentic 產品應將 **Cache Hit Rate 視為關鍵指標**，下降時觸發 incident 處理。這不是優化項，是生產系統的基本健康指標。

---

## 費率結構

快取命中 = 基礎輸入費率的 **0.1×**（省 90%）：

| 模型 | 基礎輸入 | 5m 快取寫入 | 1h 快取寫入 | 快取命中 | 輸出 |
|------|---------|------------|------------|---------|------|
| Opus 4.7 | $5/MTok | $6.25 | $10 | **$0.50** | $25 |
| Sonnet 4.6 | $3/MTok | $3.75 | $6 | **$0.30** | $15 |
| Haiku 4.5 | $1/MTok | $1.25 | $2 | **$0.10** | $5 |

---

## 核心原理：前綴匹配

Prompt Caching 的工作方式：**逐 token 從頭比對前綴**，遇到第一個不同 token 即停止快取。

**最有效的分層結構（靜態 → 動態）**：

```
1. System prompt + Tools       ← 最穩定，全域快取
2. 專案特定檔案 / CLAUDE.md   ← 中度穩定，跨 session 快取
3. Session context             ← 僅當次 session
4. 對話訊息（最新輪次）        ← 每次請求不同
```

越靠前的內容變動越少，快取效益越高。

---

## 兩種實作方式

### 方式一：自動快取（多輪對話推薦）

在 request 頂層加 `cache_control` 欄位，系統自動將 breakpoint 套用到最後一個可快取的 block，並隨對話成長自動前移：

```python
response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    cache_control={"type": "ephemeral"},  # 頂層自動快取
    system="You are a helpful assistant...",
    messages=[
        {"role": "user", "content": "..."},
        {"role": "assistant", "content": "..."},
        {"role": "user", "content": "What did I say I work on?"},
    ],
)
```

| 請求 | 快取行為 |
|------|---------|
| Request 1 | 所有內容寫入快取 |
| Request 2 | System ~ User(2) 從快取讀取；Asst(2) + User(3) 寫入 |
| Request 3 | System ~ User(3) 從快取讀取；後續內容寫入 |

### 方式二：明確 Breakpoint（精細控制）

將 `cache_control` 放在特定 content block 上，可定義最多 4 個 breakpoint：

```python
response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    system=[
        {"type": "text", "text": "You are an AI assistant..."},
        {
            "type": "text",
            "text": "Here is the full text of a complex legal agreement: [50-page document]",
            "cache_control": {"type": "ephemeral"},  # 在長文件末尾設 breakpoint
        },
    ],
    messages=[{"role": "user", "content": "What are the key terms?"}],
)
```

工具列表末尾設 breakpoint（推薦模式）：

```json
{
  "tools": [
    {"name": "get_weather", "description": "..."},
    {
      "name": "get_time", "description": "...",
      "cache_control": {"type": "ephemeral"}
    }
  ],
  "messages": [{"role": "user", "content": "變動的查詢..."}]
}
```

---

## 最小快取長度

低於此值不快取，不報錯：

| 模型 | 最小 token 數 |
|------|-------------|
| Opus 4.7, 4.6, 4.5 / Haiku 4.5 | 4096 |
| Sonnet 4.6 / Haiku 3.5 | 2048 |
| Sonnet 4.5 / Opus 4.1, 4 / Sonnet 4 | 1024 |

確認快取是否生效：檢查 `cache_creation_input_tokens` 和 `cache_read_input_tokens`，兩者都是 0 表示沒有快取。

---

## Thariq 的六大生產教訓

### 教訓 1：靜態內容放最前，動態資訊用 messages 傳遞

**錯誤做法**：有新資訊（時間戳、檔案變更）時修改 system prompt → 無效化整個快取前綴。

**正確做法**：透過後續對話訊息傳遞更新資訊，使用 `<system-reminder>` 標籤標示動態注入內容：

```xml
<!-- 在後續訊息中注入，不修改 system prompt -->
<system-reminder>
  現在時間：2026-05-16 10:30
  最近修改的檔案：src/main.py
</system-reminder>
```

### 教訓 2：Mid-Session 禁止切換模型

Prompt Cache **是模型專屬的**。從 Opus 切換到 Haiku（或反之）：
- 快取前綴全部失效
- 下一輪請求必須重建整個快取（等同從頭支付計算費用）

**正確做法**：需要用不同模型 → 用 **Subagent**（每個 subagent 有獨立 context + 快取）。

### 教訓 3：對話中不增刪工具

工具定義（tool definitions）是快取前綴的一部分。增刪工具 = 前綴變動 = 快取失效。

**應對策略**：保留所有工具定義在前綴中，用輕量 stub + `defer_loading: true` 保持前綴穩定：

```json
{
  "name": "heavy_tool",
  "description": "...",
  "defer_loading": true
}
```

### 教訓 4：Compaction 不能破壞快取前綴

Context window 滿了進行 Compact 時，**Compact 請求必須使用與父對話完全相同的** system prompt + tools + user context：

```python
compaction_request = {
    "system": original_system_prompt,  # 完全相同
    "tools": original_tools,           # 完全相同
    "messages": [
        {"role": "user", "content": f"請摘要以下對話：{conversation_history}"}
    ]
}
```

### 教訓 5：監控快取命中率

將 Cache Hit Rate 加入核心監控指標，等同 uptime 指標：

```python
cache_hit_rate = response.usage.cache_read_input_tokens / response.usage.input_tokens
```

Claude Code 內部實踐：Cache hit rate 下降 → 觸發 incident 流程 → 找出導致快取失效的變更。

### 教訓 6：1 小時快取

```json
{"cache_control": {"type": "ephemeral", "ttl": "1h"}}
```

適用情境：
- Prompt 使用頻率低於每 5 分鐘一次但高於每小時
- 延遲敏感且後續 prompt 可能超過 5 分鐘
- 需要改善 rate limit 利用率

---

## 快取失效條件

| 改動類型 | 影響 |
|---------|------|
| Tool definitions | ✘ 整個快取失效 |
| Web search/Citations 切換 | ✘ system & message 快取失效 |
| Speed setting（fast mode）| ✘ system & message 快取失效 |
| Tool choice 改變 | ✘ message 快取失效（system 不影響）|
| Images 新增/移除 | ✘ message 快取失效 |
| Thinking 參數改變 | ✘ message 快取失效 |

> ⚠️ **2026-02-05 起**：快取隔離從 organization 層級改為 **workspace 層級**

---

## 快取預熱（Pre-Warming）

消除第一個請求的延遲：

```python
# 預熱請求（max_tokens=0，不產生輸出）
prewarm = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=0,
    system=[{"type": "text", "text": "...", "cache_control": {"type": "ephemeral"}}],
    messages=[{"role": "user", "content": "warmup"}],
)
# 產生 cache write 費用，但無 output 費用
```

---

## 各場景快取策略

| 場景 | 策略 |
|------|------|
| 對話型 Agent | 快取長指令或上傳文件，降低延伸對話的成本 |
| Coding Assistant | 快取相關 codebase 段落或摘要 |
| 大型文件處理 | 嵌入完整長文（含圖片），不增加回應延遲 |
| 詳細指令集 | 快取 20+ 個高品質 few-shot examples |
| Agentic Tool Use | 優化多工具呼叫和迭代程式碼修改 |
| 知識庫應用 | 嵌入完整文件/轉錄文字供互動查詢 |

---

## 常見問題排查

| 問題 | 原因 | 解法 |
|------|------|------|
| 沒有 cache hit | 快取段落不完全相同 / 超過 TTL / 未達最小 token | 確保 100% 相同、在 TTL 內、檢查 token 數 |
| Cache 失效 | tool_choice 或 image 使用不一致 | 確保 breakpoint 前的內容固定 |
| Breakpoint 位置錯誤 | 放在變動 block 上 | 移到最後一個固定 block |
| Tool JSON key 順序 | 部分語言隨機排序 | 確保穩定的 JSON key 順序 |

---

## 快速 Checklist

- [ ] System prompt 結構：靜態內容放最前，動態資訊用 messages 傳遞
- [ ] Session 內不切換模型（需換模型 → 開 subagent）
- [ ] 工具定義對話中不增刪（用 stub + defer_loading）
- [ ] Compact 操作保留原始 system prompt + tools
- [ ] Cache hit rate 加入 observability dashboard
- [ ] Breakpoint 放在跨請求不變的最後一個 block

---

## 延伸閱讀

- [官方 Prompt Caching 文件](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- [Thariq 的原文](https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything)
- [Lecture 03：Context Engineering](/lectures/lecture-03-context-engineering/)
