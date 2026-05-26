---
title: "Patterns for Building LLM-based Systems & Products"
authors: Eugene Yan
source: "https://eugeneyan.com/writing/llm-patterns/"
source_tier: P
---

# Patterns for Building LLM-based Systems & Products

- **作者**: Eugene Yan
- **URL**: https://eugeneyan.com/writing/llm-patterns/
- **發表**: 2023（約）
- **收錄日期**: 2026-05-01
- **重要性**: Priority B — 生產級 LLM 系統的 7 大設計模式

---

## 7 大 Patterns

| Pattern | 核心目的 | Harness 相關度 |
|---------|---------|--------------|
| **Evals** | 評估與品質保證 | ⭐⭐⭐⭐⭐ 必需 |
| **RAG** | 檢索增強生成 | ⭐⭐⭐⭐ Memory 層的實現 |
| **Fine-tuning** | 模型專化 | ⭐⭐ 模型層，非 harness |
| **Caching** | 重複交互優化 | ⭐⭐⭐⭐ Context 效率 |
| **Guardrails** | 輸出控制與安全 | ⭐⭐⭐⭐⭐ 必需 |
| **Defensive UX** | 防禦性交互設計 | ⭐⭐⭐ 使用者界面層 |
| **Collect User Feedback** | 持續改進迴路 | ⭐⭐⭐⭐ Ratchet 的外部信號 |

---

## 核心洞見（對 Harness Engineering 最相關）

### 1. 專化模型組隊優於單一通才
多個小型專化模型的組合（用提示鏈式串接）在許多任務上優於單一大型通才模型。
- **Harness 意義**: 子任務路由到最合適的 agent/skill，而非全部交給同一個 agent

### 2. Hybrid 方法優於單一最優策略
Hybrid Retrieval（傳統搜尋 + embedding 搜尋）的組合效果優於任一單一方法。
- **Harness 意義**: 多層次決策機制（tools + context + memory）比單一路徑更可靠

### 3. Guardrails 和 Evals 是生產環境的必需品
系統化的評估框架和輸出守衛，不是可選的優化。
- **Harness 意義**: verification loop 和 error handling 必須內建，而非事後添加

### 4. 數據與反饋是競爭護城河
用戶反饋收集機制是長期持續改進的關鍵。
- **Harness 意義**: 每次 agent 失敗都是 Ratchet 改進的原料；需要系統性收集

### 5. 實施細節影響巨大
提示措辭、tokenization 策略等細節會導致模型排名大幅波動。
- **Harness 意義**: Harness 的每一行配置都可能影響整體性能分布

---

## 與 Harness 設計的對應

| Eugene Yan 的 Pattern | 本 Workspace 的實現 |
|----------------------|-------------------|
| Evals | /deep-review skill + healthcheck.sh |
| RAG | WebFetch + researcher agent |
| Caching | prompt caching 架構規則（context-management.md） |
| Guardrails | security-hygiene.md + PreToolUse hook |
| Collect Feedback | Ratchet + Known Gotchas 更新 |
