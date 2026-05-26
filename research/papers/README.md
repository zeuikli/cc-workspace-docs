# Academic Paper Archive

> **Type:** raw:indexed — academic papers on LLM and AI agents (read-only source layer)

109 篇學術論文存檔：86 篇 .md 摘要 + 23 篇 .pdf 原文。涵蓋 2022–2026 年 LLM 與 AI agent 研究。

**2026-05-25 v5 更新**：新增 12 篇（記憶架構 +6、多 agent 協調 +2、評估基準 +3、Harness +1）。

檔名格式：`YYYY-MM-DD-slug-arxiv-id.md`（arxiv ID 內嵌於檔名）

## Agent Query Patterns

```
"有沒有關於 multi-agent 協作的論文？"
  → grep -l "multi-agent\|Multi-Agent" research/papers/*.md | head -10

"最新的 2026 年論文有哪些？"
  → ls research/papers/2026-*.md

"找 RAG 相關論文"
  → grep -l "RAG\|retrieval" research/papers/*.md
```

## 主題分類

| 主題 | 說明 |
|------|------|
| LLM Memory | 長期記憶、KV Cache、RAG 機制 |
| Speculative Decoding | 推理加速、draft model 策略 |
| Agent Architectures | ReAct / CoT / Tool-use / Planning |
| Multi-agent | 多 agent 協作框架、Fan-out 拓撲 |
| AI Values & Safety | 對齊、安全評估、Constitutional AI |
| Routing | LLM routing 策略、mixture-of-experts |
