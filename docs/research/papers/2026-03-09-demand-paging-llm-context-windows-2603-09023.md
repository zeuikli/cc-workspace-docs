---
url: "https://arxiv.org/abs/2603.09023"
title: "The Missing Memory Hierarchy: Demand Paging for LLM Context Windows"
archived_date: 2026-06-24
arxiv_id: 2603.09023
authors: ["Tony Mason"]
domains: [cs.OS, "context management"]
html: "https://arxiv.org/html/2603.09023v1"
pdf_path: pdfs/2603.09023.pdf
published_date: 2026-03-09
---

# The Missing Memory Hierarchy: Demand Paging for LLM Context Windows

**Authors**: Tony Mason
**Published**: March 09, 2026
**Source**: https://arxiv.org/abs/2603.09023 · [HTML](https://arxiv.org/html/2603.09023v1)
**arXiv ID**: 2603.09023
**Categories**: cs.OS, context management
**PDF**: [research/papers/pdfs/2603.09023.pdf](https://arxiv.org/abs/2603.09023) (15 pp, full text archived)

---

## Abstract (quoted)

> The context window of a large language model is not memory. It is L1 cache: a small, fast, expensive resource that the field treats as the entire memory system. There is no L2, no virtual memory, no paging. Every tool definition, every system prompt, and every stale tool result occupies context for the lifetime of the session. The result is measurable: across 857 production sessions and 4.45 million effective input tokens, 21.8% is structural waste. We present Pichay, a demand paging system for LLM context windows. Implemented as a transparent proxy between client and inference API, Pichay interposes on the message stream to evict stale content, detect page faults when the model re-requests evicted material, and pin working-set pages identified by fault history. In offline replay across 1.4 million simulated evictions, the fault rate is 0.0254%. In live production deployment over 681 turns, the system reduces context consumption by up to 93% (5,038KB to 339KB); under extreme sustained pressure, the system remains operational but exhibits the expected thrashing pathology, with repeated fault-in of evicted content. The key observation is that the problems the field faces, such as context limits, attention degradation, cost scaling, lost state across sessions, are virtual memory problems wearing different clothes. The solutions exist: working set theory (Denning, 1968), demand paging, fault-driven replacement policies, and memory hierarchies with multiple eviction-managed levels. We describe the architecture of a full memory hierarchy for LLM systems (L1 through persistent storage), report on the first three levels deployed in production use (L1 eviction, L2 fault-driven pinning, L3 model-initiated conversation compaction), and identify cross-session memory as the remaining frontier.

---

## 結構化摘要

### 核心貢獻

- 提出 **Pichay**：一個 LLM context window 的 demand paging 系統，以透明 proxy 形式插入 client 與 inference API 之間，不需修改模型或客戶端
- 建立完整的 LLM memory hierarchy 框架（L1 eviction → L2 fault-driven pinning → L3 conversation compaction → persistent cross-session storage），類比傳統 OS 虛擬記憶體架構
- 量化 context 浪費：857 個生產 session、4.45M input tokens 中 21.8% 為 structural waste（tool definition、system prompt、過時 tool result 佔位）
- 引入 working set theory（Denning, 1968）為 LLM context 管理的理論基礎，重新詮釋 context limit / attention degradation / cost scaling 為虛擬記憶體問題

### 關鍵結果

- **Fault rate 極低**：1.4M 模擬 eviction 中 fault rate 為 0.0254%，說明模型鮮少重新請求已被 evict 的內容
- **Context 壓縮 93%**：681 turns 生產部署中，context 從 5,038KB 降至 339KB
- **Thrashing 可觀測**：極端持續壓力下系統仍可運作，但出現預期的 thrashing 病態（反覆 fault-in evicted content）
- L1–L3 三層已在生產環境部署，cross-session memory 標識為下一個待解前沿

### 限制

- **單作者、單系統實作**：Pichay 為作者自建生產系統，外部可重現性及泛化性未獲獨立驗證
- **Thrashing 未完全解決**：在高壓場景下仍發生 thrashing，replacement policy 的最佳化仍開放
- **L4（cross-session persistent memory）尚未實作**：論文識別此為 frontier 但未提供實驗數據
- 論文未列明確 limitation 章節；上述為讀者可推斷的弱點

---

## Workspace 關聯（評估，非既成結論）

- **直接對應 context-management 規則**：`context-management.md` 的 NLAH 原則（Right context > more context）與 token budget 管理正是 Pichay 所量化的問題——21.8% structural waste 為 LLM context 管理原則提供了實證依據；demand paging 機制可視為 NLAH 原則的自動化實作
- **對應 `/compact` 機制**：論文 L3 層（model-initiated conversation compaction）與 workspace 的 `/compact` 指令在概念上高度重合；Pichay 的 fault-driven pinning 可為 compact hint 保留哪些「working-set」提供設計參考
- **對應 memory-compactor 與 MEMORY.md 長期記憶回路**：論文將 cross-session memory 列為 remaining frontier，與 `core.md` §長期記憶回路（MEMORY.md、LESSONS.md 跨 session 保存）的實踐需求吻合；⚠️ workspace 目前無自動 eviction/paging 層，memory-compactor skill 的行數門檻為人工近似，非 fault-driven
- **⚠️ 落地門檻**：Pichay 為 proxy 架構，需插入 inference API 呼叫鏈；workspace 使用 Claude Code CLI 直接呼叫，無現成 proxy 層可掛載此機制，直接套用需額外工程投入
