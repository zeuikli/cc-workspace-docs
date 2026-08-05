---
url: "https://arxiv.org/abs/2606.10209"
title: "Less Context, Better Agents: Efficient Context Engineering for Long-Horizon Tool-Using LLM Agents"
archived_date: 2026-06-24
arxiv_id: 2606.10209
authors: ["Abhilasha Lodha", "Mahsa Pahlavikhah Varnosfaderani", "Abir Chakraborty", "Abhinav Mithal"]
domains: [cs.AI]
html: "https://arxiv.org/html/2606.10209v1"
pdf_path: pdfs/2606.10209.pdf
published_date: 2026-06-08
---

# Less Context, Better Agents: Efficient Context Engineering for Long-Horizon Tool-Using LLM Agents

**Authors**: Abhilasha Lodha, Mahsa Pahlavikhah Varnosfaderani, Abir Chakraborty, Abhinav Mithal
**Published**: June 08, 2026
**Source**: https://arxiv.org/abs/2606.10209 · [HTML](https://arxiv.org/html/2606.10209v1)
**arXiv ID**: 2606.10209
**Categories**: cs.AI
**PDF**: [research/papers/pdfs/2606.10209.pdf](https://arxiv.org/abs/2606.10209) (17 pp, full text archived)

---

## Abstract (quoted)

> Large language models deployed as autonomous agents for enterprise workflows face a key challenge: verbose tool responses from enterprise systems can cause context overflow, stale-state errors, and high inference cost. We study this problem in automated expense itemization in Microsoft Dynamics 365 Finance and Operations using Model Context Protocol tools. We evaluate four GPT-5 configurations on a 50-task hotel expense benchmark: no user model, full conversation history, context pruned to the last 5 tool call/response pairs, and pruning with automated summarization. Results are averaged across 5 independent runs, with the user model held constant for the context-engineering comparison. The no-user-model baseline achieves only 8.0% complete itemization. Full-context retention improves completion to 71.0%, but consumes 1,480,996 tokens and 14.56 hours per benchmark. Pruning to the last 5 tool calls improves completion to 79.0% while reducing token use to 535,274 and runtime to 5.39 hours. Adding summarization achieves the best result: 91.6% complete itemization and 99.64% average amount itemized, with 553,374 tokens and 5.79 hours. We further report confidence intervals, effect-size analysis, sensitivity over pruning and summary windows, failure analysis, results across five expense types grouped into three categories, and cross-model evidence with Claude Sonnet 4.5. These results show that, for this class of enterprise tool-use workflow, selective retention of recent tool interactions plus compact summarization can improve both reliability and efficiency compared with full-history retention.

---

## 結構化摘要

### 核心貢獻

- 在真實 enterprise ERP（Microsoft Dynamics 365）上以 MCP tools 做 long-horizon agentic 任務，建立 50-task hotel expense benchmark
- 系統評估四種 context 策略：no user model / full history / pruning-only（last 5 tool pairs）/ pruning + summarization
- 量化證明 context overflow 是 LLM agent 可靠性與成本的核心瓶頸，不是 model 能力問題
- 提供跨模型驗證（Claude Sonnet 4.5），增強結論泛化性

### 關鍵結果

- **無 user model**：8.0% 完成率（baseline）
- **Full history**：71.0% 完成率，耗 1,480,996 tokens，14.56 小時/benchmark
- **Pruning（last 5 pairs）**：79.0% 完成率，535,274 tokens，5.39 小時（↓64% tokens，↓63% 時間）
- **Pruning + summarization**：91.6% 完成率，99.64% 金額正確率，553,374 tokens，5.79 小時 — **最佳**
- Summarization 比 full history 多用 ~3% tokens 但完成率提升 20.6pp

### 限制

- 領域特定：benchmark 限於 hotel expense itemization，泛化到其他 enterprise workflow 需另行驗證
- 小規模 benchmark（50 tasks），統計置信區間較寬
- Pruning window 固定為 last 5 pairs，動態調整策略未探索
- User model 作為固定常數控制，實際部署中 user model 本身亦可能需要 context 管理

---

## Workspace 關聯（評估，非既成結論）

- **NLAH 原則直接對應**：論文的 pruning + summarization 策略實驗性地佐證了 `context-management.md` 的 NLAH 原則（Right context > more context）——保留最近 tool 互動而非全部 history，在 reliability 與 token 效率上同時勝出
- **context-management token budget**：論文的 token 數字（full history 1.48M vs pruning 0.55M）量化了 token overflow 的真實代價，與 workspace token budget 軟性上限的設計動機吻合；`context-management.md` 的 compact hint 機制在概念上與論文的 summarization window 同源
- **unverified_success 閘門**：論文指出 agent 在 full-history 條件下會產生 stale-state errors（以為任務已完成實則未完成），這與 `core.md` TEST 階段的 `unverified_success` 閘門所防範的失敗模式一致——LLM 自報「成功」不等於真正完成
- ⚠️ **落地門檻**：論文場景為單一確定性 ERP 任務（expense itemization），workspace 的 subagent fan-out 涉及多層協作與非確定性任務；pruning window 大小需按具體 tool response verbosity 校準，不可直接套用 last-5 數字

