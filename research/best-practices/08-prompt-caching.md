# Prompt Caching — 完整技術指南

> 來源：https://platform.claude.com/docs/en/build-with-claude/prompt-caching  
> 收錄日期：2026-05-01  
> 涵蓋：兩種實作方式、快取機制、定價、失效條件、最佳實踐、各場景策略

---

## 核心概念

Prompt caching 讓你在 prompt 的特定前綴上繼續執行，顯著降低重複任務的處理時間和成本。

**費率（快取命中 = 基礎輸入的 0.1×）：**

| 模型 | 基礎輸入 | 5m 寫入 | 1h 寫入 | 快取命中 | 輸出 |
|------|---------|--------|--------|---------|------|
| Opus 4.7 | $5/MTok | $6.25 | $10 | **$0.50** | $25 |
| Sonnet 4.6 | $3/MTok | $3.75 | $6 | **$0.30** | $15 |
| Haiku 4.5 | $1/MTok | $1.25 | $2 | **$0.10** | $5 |

寫入費率：5m = 1.25× 基礎，1h = 2× 基礎

---

## 兩種實作方式

### 方式一：自動快取（多輪對話推薦）

在 request 頂層加 `cache_control` 欄位，系統自動將 breakpoint 套用到最後一個可快取的 block，並隨對話成長自動前移。

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

自動移動行為：

| 請求 | 快取行為 |
|------|---------|
| Request 1 | 所有內容寫入快取 |
| Request 2 | System ~ User(2) 從快取讀取；Asst(2) + User(3) 寫入 |
| Request 3 | System ~ User(3) 從快取讀取；後續內容寫入 |

### 方式二：明確 Breakpoint（精細控制）

將 `cache_control` 放在特定 content block 上，可定義最多 4 個 breakpoint。

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

---

## 最小快取長度（低於此值不快取，不報錯）

| 模型 | 最小 token 數 |
|------|-------------|
| Opus 4.7, 4.6, 4.5 / Haiku 4.5 / Mythos Preview | 4096 |
| Sonnet 4.6 / Haiku 3.5 | 2048 |
| Sonnet 4.5 / Opus 4.1, 4 / Sonnet 4 | 1024 |

確認快取是否生效：檢查 `cache_creation_input_tokens` 和 `cache_read_input_tokens`，兩者都是 0 表示沒有快取。

---

## 可快取的內容

| 可快取 ✓ | 不可快取 ✗ |
|---------|----------|
| Tool definitions | Thinking blocks（不能直接標記）|
| System messages | Sub-content blocks（如 citations）|
| Text messages | Empty text blocks |
| Images & Documents | |
| Tool use and tool results | |
| Thinking blocks（作為前一輪 assistant 的一部分）| |

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

## 1 小時快取

```json
{"cache_control": {"type": "ephemeral", "ttl": "1h"}}
```

適用情境：
- Prompt 使用頻率低於每 5 分鐘一次但高於每小時
- 延遲敏感且後續 prompt 可能超過 5 分鐘
- 需要改善 rate limit 利用率

---

## Breakpoint 位置最佳實踐

**原則：Breakpoint 放在跨請求不變的最後一個 block**

```json
{
  "tools": [
    {"name": "get_weather", "description": "..."},
    {
      "name": "get_time", "description": "...",
      "cache_control": {"type": "ephemeral"}  // 工具列表末尾
    }
  ],
  "messages": [{"role": "user", "content": "變動的查詢..."}]
}
```

**常見錯誤**：把 breakpoint 放在變動內容上（timestamp、per-request context）→ 每次都 cache miss。

**Lookback window**：系統從 breakpoint 往前最多查 20 個 block 找快取前綴。

---

## 監控快取效能

```python
usage = response.usage
# cache_creation_input_tokens：寫入快取的 token 數
# cache_read_input_tokens：從快取讀取的 token 數
# input_tokens：最後一個 breakpoint 後的 token 數

# 總輸入 token = cache_read + cache_creation + input_tokens
```

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

# 後續真實請求自動命中快取
```

---

## 各場景快取策略

| 場景 | 策略 |
|------|------|
| **對話型 Agent** | 快取長指令或上傳文件，降低延伸對話的成本 |
| **Coding Assistant** | 快取相關 codebase 段落或摘要 |
| **大型文件處理** | 嵌入完整長文（含圖片），不增加回應延遲 |
| **詳細指令集** | 快取 20+ 個高品質 few-shot examples |
| **Agentic Tool Use** | 優化多工具呼叫和迭代程式碼修改 |
| **知識庫應用** | 嵌入完整文件/轉錄文字供互動查詢 |

---

## Thinking Blocks 與快取

- Thinking blocks **不能**直接標記 `cache_control`
- 它們作為前一輪請求內容的一部分自動快取（當有 tool results 時）
- 從快取讀取的 thinking blocks 計為 input tokens
- Opus 4.5+ / Sonnet 4.6+：thinking blocks 預設保留（較舊模型加入非 tool-result user content 時會被清除）

---

## 常見問題排查

| 問題 | 原因 | 解法 |
|------|------|------|
| 沒有 cache hit | 快取段落不完全相同 / 超過 TTL / 未達最小 token | 確保 100% 相同、在 TTL 內、檢查 token 數 |
| Cache 失效 | tool_choice 或 image 使用不一致 | 確保 breakpoint 前的內容固定 |
| Breakpoint 位置錯誤 | 放在變動 block 上 | 移到最後一個固定 block |
| Tool JSON key 順序 | 部分語言隨機排序 | 確保穩定的 JSON key 順序 |

---

## Key Takeaways

- 多輪對話 → **自動快取**（頂層 cache_control）
- 不同頻率的段落 → **明確 breakpoint**（最多 4 個）
- Breakpoint 放在 **跨請求不變**的最後一個 block
- 監控 `cache_read_input_tokens` 評估命中率
- 延遲敏感 → **pre-warm** 消除冷啟動
- 快取命中 = 基礎輸入費率的 **0.1×**（省 90%）
