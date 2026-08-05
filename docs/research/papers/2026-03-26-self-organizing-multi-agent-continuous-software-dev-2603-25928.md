---
url: "https://arxiv.org/abs/2603.25928"
title: "Self-Organizing Multi-Agent Systems for Continuous Software Development"
archived_date: 2026-06-24
arxiv_id: 2603.25928
authors: ["Wenhan Lyu", "Yue Xiao", "Yixuan Zhang", "Yifan Sun"]
domains: [cs.SE]
html: "https://arxiv.org/html/2603.25928v1"
pdf_path: pdfs/2603.25928.pdf
published_date: 2026-03-26
---

# Self-Organizing Multi-Agent Systems for Continuous Software Development

**Authors**: Wenhan Lyu, Yue Xiao, Yixuan Zhang, Yifan Sun
**Published**: March 26, 2026
**Source**: https://arxiv.org/abs/2603.25928 · [HTML](https://arxiv.org/html/2603.25928v1)
**arXiv ID**: 2603.25928
**Categories**: cs.SE
**PDF**: [research/papers/pdfs/2603.25928.pdf](https://arxiv.org/abs/2603.25928) (12 pp, full text archived)

---

## Abstract (quoted)

> Large Language Model-based multi-agent systems have shown promise in automating software development tasks. However, most vibe code systems focus on completing small tasks and incremental code changes, leaving persistent, continuous software development largely unexplored. We present TheBotCompany, an open-source orchestration framework for continuous multi-agent software development. TheBotCompany introduces three key innovations: (1) a three-phase state machine (Strategy to Execution to Verification) for milestone-driven development, (2) self-organizing agent teams where manager agents dynamically hire, assign, and fire worker agents based on project needs, and (3) asynchronous human oversight. We evaluate TheBotCompany on real-world software projects over multiple days of continuous development, measuring team adaptation patterns, milestone completion rates, cost efficiency, and code quality. Our results demonstrate that the self-organizing approach enables effective long-term software development with measurable progress, while the verification phase catches defects that would otherwise persist.

---

## 結構化摘要

### 核心貢獻
- 提出 **TheBotCompany**：open-source orchestration framework，專注於 *continuous*（跨日、持續性）multi-agent software development，補足現有 vibe code 系統只做小任務 / incremental change 的空缺。
- **Three-phase state machine**：Strategy → Execution → Verification，以 milestone-driven 方式驅動長期開發流程。
- **Self-organizing agent teams**：manager agent 依專案需求動態 *hire / assign / fire* worker agent（團隊規模與分工隨需求自我調節）。
- **Asynchronous human oversight**：人類非同步介入監督，不阻塞 agent 持續推進。

### 關鍵結果
- 於 real-world software projects 進行 multiple days 連續開發評估，量測四維：team adaptation patterns、milestone completion rates、cost efficiency、code quality。
- Self-organizing 方式可達成有 measurable progress 的長期開發。
- Verification phase 能攔截「否則會持續存在」的 defects（驗證階段對缺陷攔截有實際作用）。
- ⚠️ Abstract 未給出具體數字（completion rate %、cost、defect 數）；精確量化需查 PDF 全文。

### 限制
文件 abstract 未列明確 limitation 章節。依方法判斷的潛在弱點：
- 評估規模僅「multiple days / real-world projects」，未說明專案數量與多樣性 → 外推性存疑。
- Manager agent 的 hire/fire 決策品質高度依賴底層 LLM 能力，cost efficiency 可能對 model 選擇敏感。
- Asynchronous human oversight 的介入頻率 / 成本未量化，「自主程度」邊界不清。
- Verification phase 攔截 defect 的 recall（漏網缺陷）未必有 ground-truth 對照。

---

## Workspace 關聯（評估，非既成結論）

- **Self-organizing manager→worker 模型 vs. 本 workspace fan-out 紀律**：論文的 dynamic hire/assign/fire 與 `core.md §PROPOSE 委派`（原 `subagent-strategy.md`）的 Fan-out ≤4、parent↔child 通訊限制方向相反（動態擴張 vs. 靜態上限）。可作為「放寬 fan-out 上限」的對照案例，⚠️ 但本 workspace 無 manager-agent 自治生命週期機制，落地需新增 orchestration 層。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
- **Strategy→Execution→Verification 三相 vs. The Loop 六階段**：其 Verification phase ≈ core.md 的 TEST + `unverified_success` 閘門（fresh-context verifier 攔缺陷）。論文「verification catches persistent defects」與本 workspace「確定性 gate 不經 sub-agent 中介」可互相印證。
- **Continuous / milestone-driven 開發 vs. overnight 任務**：對應 `claude-progress.json` + `research-hub:deep` + `autoresearch`（原 overnight-research，v5.1 刪除） pipeline 的跨 session 持續性概念，⚠️ 但論文以 days 為尺度的 team adaptation 目前 workspace 無對應自動化載體。
- ⚠️ 落地門檻：論文為框架層 proposal（TheBotCompany），引入需整套 manager-agent runtime；本 workspace 現以 skill/rule advisory + hook enforcement 為主，非 agent 自治系統，無法直接移植，僅供架構參考。
