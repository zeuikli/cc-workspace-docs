---
title: "Agent Engineering: A New Discipline"
authors: LangChain Team
source: "https://blog.langchain.com/agent-engineering-a-new-discipline/"
source_tier: P
---

# Agent Engineering: A New Discipline

- **作者**: LangChain Team
- **平台**: LangChain Blog
- **URL**: https://blog.langchain.com/agent-engineering-a-new-discipline/
- **收錄日期**: 2026-05-01
- **重要性**: Priority C — 定義 Agent Engineering 作為工程學科的宣言文章

---

## 核心定義

**Agent Engineering** = 「將非確定性 LLM 系統迭代精煉為可靠生產體驗的過程」

---

## 與傳統軟體工程的根本差異

| 維度 | 軟體工程 | Agent Engineering |
|------|---------|------------------|
| 輸入 | 大多數輸入已知且可預測 | 自然語言，任意輸入 |
| 測試 | 發布前完整測試 | 生產中學習，快速迭代 |
| 輸出 | 確定性輸出 | 非確定性，需統計視角 |
| 迭代周期 | 季度發行 | 快速 Build-Ship-Observe |

---

## 工程循環

```
Build → Test → Ship → Observe → Refine → Repeat
```

關鍵轉變：放棄「發布前完美」，改為快速發行 + 生產學習。

---

## 跨職能技能要求

Agent Engineering 需要三種能力的整合：

1. **Product Thinking**: 提示工程、workflow 設計、評估標準定義
2. **Engineering**: 工具整合、UI、durable runtime 建構
3. **Data Science**: 評估、A/B 測試、monitoring

---

## 實際案例

- **Clay**: prospect 研究 agent（B2B sales 自動化）
- **LinkedIn**: 招聘 agent（候選人匹配）
- **Cloudflare**: 候選人排名 agent（HR 自動化）

---

## 核心洞見

1. **非確定性是根本**: LLM 的不可預測性不是 bug，是 feature；harness 需要統計性管理
2. **自然語言的不可預測性**: 用戶可以輸入任何東西，打破傳統軟體的輸入/輸出假設
3. **系統化追蹤的必要性**: 每個決策要被記錄，大規模評估，快速迭代
4. **跨職能本質**: 沒有單一角色能獨立完成 agent 工程

---

## 與本 Workspace 的關聯

| Agent Engineering 要素 | Workspace 的對應 |
|---------------------|----------------|
| Build | implementer agent + core.md 實作習慣 |
| Test | test-writer agent + healthcheck.sh |
| Observe | Auto Memory + retro skill |
| Refine | Ratchet 原則 + FRAMEWORK.md 更新 |
| 跨職能協作 | 多 agent 分工（researcher/implementer/reviewer）|
