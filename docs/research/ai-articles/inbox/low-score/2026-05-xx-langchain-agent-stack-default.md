---
url: "https://medium.com/@sehaj23chawla/langsmith-and-langgraph-in-2026-how-langchains-agent-stack-quietly-became-the-default-f1609af5d658"
date: 2026-05
authors: SC (Sehaj Chawla)
reason: Low score — competitive analysis; LangGraph/Claude different harness philosophies
score: 5.85
source: Medium
tags: [langchain, langgraph, langsmith, agent-orchestration, competitive-analysis]
---

# LangSmith and LangGraph in 2026: How LangChain's Agent Stack Quietly Became the Default

**歸檔日期**：2026-05-10  
**分數**：5.85/10（低於有效整合閾值 6.0）  
**原因**：觀察性報導，LangGraph 生態系分析對 Claude Code / cc-workspace 直接可行動性低

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 4/10 | LangGraph 是競爭生態，不直接適用 Claude Code |
| B. 創新性 | 3/10 | 觀察報導，無新方法論 |
| C. 證據品質 | 6/10 | 行業觀察，anecdotal |
| D. 技術深度 | 5/10 | High-level，無 internals |
| E. 泛化性 | 8/10 | 行業趨勢有參考價值 |
| **加權總分** | **5.1/10** | 計算後 5.10（低分原因：A 和 B 低）|

---

## 核心觀察（參考用）

1. LangGraph v1.0 stable（2025 Q4）成為 multi-agent 協調的社群標準
2. 核心價值主張：state persistence（survive restart, resume exactly）
3. 生態三層：LangChain（構建）+ LangGraph（協調）+ LangSmith（觀測）
4. 行業問題從「哪個模型」轉為「如何生產化」

**關聯**：Claude Code 的競爭對比參考。Claude Code 選擇 Agent SDK（不是 graph-based）反映不同哲學：  
- LangGraph：顯式 state machine graph
- Claude Code：implicit context + explicit hooks
