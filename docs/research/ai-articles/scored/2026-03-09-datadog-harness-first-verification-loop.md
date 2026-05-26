---
url: "https://www.datadoghq.com/blog/ai/harness-first-agents/"
date: 2026-03-09
source: Datadog AI Blog
authors: Datadog Engineering
tags: [harness-first, verification, formal-methods, observability, DST]
---

# Closing the Verification Loop: Observability-Driven Harnesses for Building with Agents

**原始來源**：https://www.datadoghq.com/blog/ai/harness-first-agents/  
**作者**：Datadog Engineering  
**歸檔日期**：2026-05-10

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 9/10 | 具體 verification pyramid 可直接套用 |
| B. 創新性 | 8/10 | Harness-first 反轉傳統 code review 是新思維 |
| C. 證據品質 | 9/10 | 生產案例含具體數字（87% memory reduction, 10M simulations）|
| D. 技術深度 | 9/10 | TLA+ specs + DST + model checking + telemetry 四層詳解 |
| E. 泛化性 | 8/10 | 適用任何有 simulated 環境的系統 |
| **加權總分** | **8.6/10** | 9×0.3 + 8×0.2 + 9×0.2 + 9×0.15 + 8×0.15 = 8.60 |

**整合決策**：RULE — 核心原則（Verification Loop 作為 harness 設計要求）  
**整合位置**：`research/agent-harness/FRAMEWORK.md` §驗證策略  
**整合狀態**：待實作

---

## TL;DR

Harness-first 方法論：automated verification 取代 line-by-line code review。實作 Verification Pyramid（TLA+ → DST → model checking → production telemetry）。人類角色從「審查程式碼」轉為「定義不變量」。生產案例：redis-rust 優化（87% memory reduction）、Helix Kafka 語意（93% throughput across 10M simulations）。

---

## 核心主張

### 1. Harness-First 思維反轉

**舊模式**：寫程式碼 → code review → 測試 → 部署  
**新模式**：定義不變量（invariants）→ 建 harness → 讓 agent 在 harness 約束下工作

> "We don't review AI-generated code line by line; we verify it against formally specified invariants."

### 2. Verification Pyramid（四層）

```
TLA+ Specifications（最高層）
         ↓
Deterministic Simulation Testing（DST）
         ↓  
Model Checking
         ↓
Production Telemetry（最低層）
```

### 3. 生產案例數據

**redis-rust 優化**：
- AI 生成優化建議 → DST 驗證 → 87% memory reduction
- 等效生產延遲：通過 DST 確認
- Code review 時間：0 小時（replaced by DST）

**Helix Kafka 語意**：
- 10M simulations across 5 failure modes
- 93% throughput maintain across all scenarios
- 人工測試等效工時：~120 天 → DST：3 小時

---

## 對 cc-workspace 的直接意涵

### 1. `/deep-review` 升級方向

目前 `/deep-review` 以 LLM 審查為主（Generator ≠ Evaluator 原則）。  
Datadog 的 harness-first 建議加入**確定性驗證**：
- 現有 `bash scripts/healthcheck.sh` = 初級 invariant check
- 可擴充：在 `/deep-review` 的 Execution Checklist 加入 deterministic test 步驟

### 2. Known Gotchas 從「事後記錄」到「事前 invariant」

Ratchet 原則的進化：
- **現有**：踩坑 → 記入 Known Gotchas → rule 升格
- **目標**：預先定義不變量 → harness 防止踩坑 → 無需事後記錄

### 3. Observability 作為 harness 設計要求

AHE (2604.25850) 研究同樣強調 observability。Datadog 從工業界確認：
- 無可觀測性的 harness = 黑箱（無法改善）
- telemetry 是 verification loop 的最後防線

---

## 升級路徑建議

1. **短期**：在 `healthcheck.sh` 加入一個 invariant check（例：`.claude/rules/` 中的所有 @import 均存在）
2. **中期**：在 `/deep-review` 加入 deterministic test phase（lint + type check + unit test 作為 hard gate）
3. **長期**：研究 DST 是否適用於 CLAUDE.md rule 變更的回歸驗證
