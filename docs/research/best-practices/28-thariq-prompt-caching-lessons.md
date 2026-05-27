---
title: "Prompt Caching 核心教訓 — Thariq Shihipar（Claude Code 團隊）"
source: "https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything"
type: best-practices
---

# Prompt Caching 核心教訓 — Thariq Shihipar（Claude Code 團隊）

> 來源：https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything  
> 作者：Thariq Shihipar（MTS, Claude Code Team）  
> 收錄日期：2026-05-16  
> 重要性：★★★（直接影響 Claude Code 架構設計與 Session 管理）

---

## 核心主張

「Cache rules everything」——長跑型 Agentic 產品應將 **Cache Hit Rate 視為關鍵指標**，下降時觸發 incident 處理。這不是優化項，是生產系統的基本健康指標。

---

## 一、前綴匹配是快取的根本

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

## 二、用 Messages 代替更新 System Prompt

**錯誤做法**：有新資訊（時間戳、檔案變更）時修改 system prompt → 無效化整個快取前綴。

**正確做法**：透過後續對話訊息傳遞更新資訊，使用 `<system-reminder>` 標籤標示動態注入內容：

```xml
<!-- 在後續訊息中注入，不修改 system prompt -->
<system-reminder>
  現在時間：2026-05-16 10:30
  最近修改的檔案：src/main.py
</system-reminder>
```

---

## 三、Mid-Session 禁止切換模型

Prompt Cache **是模型專屬的**。從 Opus 切換到 Haiku（或反之）：
- 快取前綴全部失效
- 下一輪請求必須重建整個快取（等同從頭支付計算費用）

**正確做法**：需要用不同模型 → 用 **Subagent**（每個 subagent 有獨立 context + 快取）。

---

## 四、工具管理：對話中不增刪工具

工具定義（tool definitions）是快取前綴的一部分。增刪工具 = 前綴變動 = 快取失效。

**應對策略**：
- 保留所有工具定義在前綴中（不需要的用 stub 佔位）
- 用輕量 stub + `defer_loading: true` 保持前綴穩定，同時支援按需載入：

```json
{
  "name": "heavy_tool",
  "description": "...",
  "defer_loading": true
}
```

EnterPlanMode 等行為控制工具也用此模式——工具定義永遠在，用工具本身的呼叫來控制模式。

---

## 五、Compaction 不能破壞快取前綴

Context window 滿了進行 Compact 時：

**錯誤做法**：用不同的 system prompt 或 tools 建立 compaction 請求 → 後續 session 失去快取匹配。

**正確做法**：Compact 請求必須使用**與父對話完全相同的** system prompt + tools + user context，確保前綴匹配：

```
compaction_request = {
    "system": original_system_prompt,  # 完全相同
    "tools": original_tools,           # 完全相同
    "messages": [
        {"role": "user", "content": f"請摘要以下對話：{conversation_history}"}
    ]
}
```

---

## 六、監控快取命中率

將 Cache Hit Rate 加入核心監控指標，等同 uptime 指標：

```python
cache_hit_rate = response.usage.cache_read_input_tokens / response.usage.input_tokens
```

Claude Code 內部實踐：
- Cache hit rate 下降 → 觸發 incident 流程
- 找出導致快取失效的變更（通常是 system prompt 動態注入、工具增刪、模型切換）

---

## 快速 Checklist

- [ ] System prompt 結構：靜態內容放最前，動態資訊用 messages 傳遞
- [ ] Session 內不切換模型（需換模型 → 開 subagent）
- [ ] 工具定義對話中不增刪（用 stub + defer_loading）
- [ ] Compact 操作保留原始 system prompt + tools
- [ ] Cache hit rate 加入 observability dashboard

---

## 與現有 workspace 規則的對應

本文主張與 workspace 已有規則高度一致，並補充細節：

| 本文新增細節 | 對應現有規則 |
|------------|------------|
| `<system-reminder>` 注入動態資訊 | `context-management.md` § Prompt Caching 核心原則 |
| 工具 stub + defer_loading | `best-practices/08-prompt-caching.md` |
| Compact 保留相同 system prompt | `context-management.md` § Compact hint 格式 |
| Mid-session 禁止切換模型 | `context-management.md` § 禁止 mid-session |

> 一手來源（O 層）：claude.com blog，作者為 Thariq Shihipar（Claude Code MTS）
