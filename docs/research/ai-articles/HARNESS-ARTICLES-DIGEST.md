---
title: "Harness Engineering 文章收錄摘要"
type: documentation
---

# Harness Engineering 文章收錄摘要

> 收錄日期：2026-05-08  
> 收錄總數：14 篇（1 篇 Medium paywall 無法存取）  
> 評分標準：深度 × 原創性 × 實用性（★★★★★ 滿分）

---

## ★★★★★ 必讀（深度 × 實用性最高）

---

### 1. The Anatomy of an Agent Harness
**檔案：** `anatomy-of-agent-harness.md`  
**來源：** blog.dailydoseofds.com  
**評分：** ★★★★★

**核心觀點：**  
目前最完整的 harness 概覽文章。以「LLM = CPU、Context = RAM、Harness = OS」的類比為主軸，系統性拆解 11 個生產組件（Orchestration Loop、Tools、Memory、Context Management、Prompt Construction、Output Parsing、State Management、Error Handling、Guardrails、Verification Loops、Subagent Orchestration）。

**最有價值的部分：**
- 7 個架構決策矩陣（single vs multi-agent、ReAct vs plan-execute、context 策略等）
- TerminalBench 數據：僅換 harness，LangChain 從第 30 → 第 5；harness 移動 agent 20+ 排名
- ACON 研究：26–54% token 減少，保留 95%+ 精準度
- 「Harness Is the Product」核心論點，及 Manus 六個月五次重寫的個案

**適合誰：** 想一次掌握 harness 全貌的人

---

### 2. Agentic Harness Engineering: LLMs as the New OS
**檔案：** `agentic-harness-engineering-decodingai.md`  
**來源：** decodingai.com  
**評分：** ★★★★★

**核心觀點：**  
從 financial startup 實戰出發，拆掉 LlamaIndex/MCP 框架後用 plain Python 反而更好。強調「harness engineering = 用 LLM 作為 OS 建構真實軟體應用」。

**最有價值的部分：**
- Multi-surface architecture（OpenClaw 用 typed WebSocket 一份邏輯服務 CLI/Web/Desktop/Telegram）
- Lane-aware FIFO queue 解決多 client 並發問題
- 三層記憶體（Filesystem = 長期、RAM = 短期、Context Window = 當前）的讀寫路徑
- Ralph Loop 跨 context window 長任務模式的最清楚解釋
- 誠實的局限說明：記憶跨長 session 仍會斷、100 個平行 agent 共享 codebase 仍是開放問題

**適合誰：** 從零開始設計自訂 harness 的工程師

---

### 3. Agent Engineering: How the Harness Became the Product
**檔案：** `agent-engineering-morphllm.md`  
**來源：** morphllm.com  
**評分：** ★★★★★

**核心觀點：**  
Agent engineering 的全景地圖。介紹 swyx 的 IMPACT 框架（Intent、Memory、Planning、Authority、Control Flow、Tools），Manus $2B 收購故事，以及各工具 harness 的橫向比較表。

**最有價值的部分：**
- IMPACT 框架 — OpenAI TRIM 框架漏掉 Planning 和 Authority
- Manus 生產洞見：KV-cache 命中率是最關鍵指標（cached token 成本約未 cached 的 1/10）；用 logit masking 而非移除工具（避免 cache 失效）
- Cursor 發現：移除 GPT-5-Codex 的 reasoning trace 導致效能下降 30%
- The Apply Layer：edit 合併是所有 harness 的共同瓶頸，需要獨立的 apply model
- Test-first（Simon Willison）+ Spec-driven（Addy Osmani）工作流的實作範例

**適合誰：** 想深入理解 agent engineering 系統設計的架構師

---

### 4. Harness Engineering Best Practices for Claude Code / Codex Users
**檔案：** `harness-engineering-best-practices-2026-nyosegawa.md`  
**來源：** nyosegawa.com  
**評分：** ★★★★★

**核心觀點：**  
2026 最佳實踐集大成。7 個核心原則，從 repo 衛生到 E2E 測試策略全面覆蓋。

**最有價值的部分：**
- Linter 速度比較：Oxlint（50–100x faster than ESLint）、Ruff（900+ rules in Rust）
- 四種 Hook 模式：Safety Gates（PreToolUse）、Quality Loops（PostToolUse）、Completion Gates（Stop）、Observability
- 反饋速度層級：PostToolUse Hook (ms) > pre-commit (s) > CI (min) > 人工 review (h)
- AGENTS.md 大小目標：< 50 行（官方建議 200 行是上限，不是目標）；Claude Code 系統提示約 50 條指令，100 行 CLAUDE.md 會達到退化閾值
- Codex 架構差異：Hooks 僅支援 Bash（2026-03-26 實驗性），Claude Code 覆蓋所有工具
- Minimum Viable Harness 四週漸進 roadmap

**適合誰：** 需要具體實作清單的工程師

---

## ★★★★ 深度佳，值得細讀

---

### 5. Claude Code Harness: Runtime Architecture 2026 Guide
**檔案：** `claude-code-harness-runtime-architecture-pasqualepillitteri.md`  
**來源：** pasqualepillitteri.it  
**評分：** ★★★★

**核心觀點：**  
Claude Code runtime 的 8 個組件深度解析（Tool Executor、Permission Manager、Hook System、Context Manager、MCP Layer、Skill System、Subagent Framework、Session Storage）。

**最有價值的部分：**
- Auto mode 的背後機制：Sonnet 4.6 背景安全分類器，只評估 user requests 和 tool calls，不評估 model prose
- Session Storage：JSONL 格式、`--fork-session`、checkpoint 機制（Escape×2 rewind 只覆蓋 file edits，非遠端副作用）
- Harness token overhead：10K–50K tokens（系統提示、工具定義、CLAUDE.md、auto-memory 最多 25KB）
- `/context` 指令可看即時 token 分配明細

**適合誰：** 想了解 Claude Code 內部機制的開發者

---

### 6. Claude Code でハーネスエンジニアリングを実践する（5 層設計）
**檔案：** `claude-code-harness-engineering-zenn-sasadango.md`  
**來源：** zenn.dev/sasadango28  
**評分：** ★★★★（日文）

**核心觀點：**  
個人知識管理 repo 的 5 層設計實踐：CLAUDE.md（憲法）→ Rules（領域規則）→ Skills（可重用工作流）→ Agents（專業子 Agent）→ Settings（安全裝置）。

**最有價值的部分：**
- `globs` frontmatter 讓 Rules 延遲載入（條件式），節省 context
- LLM vs Script 責務分離：`tech-daily2` 用 Python 做 RSS 抓取，LLM 只做翻譯/分類 → token 降至 1/6、時間 1/3
- 「寫清楚不做什麼」是最高 CP 值的設計決策
- Hooks 的本質差別：CLAUDE.md 是「建議（advisory）」，Hooks 是「強制（deterministic）」

**適合誰：** Claude Code 個人工作區設計的參考

---

### 7. Codex vs Claude Code（2026）
**檔案：** `codex-vs-claude-code-morphllm.md`  
**來源：** morphllm.com  
**評分：** ★★★★

**核心觀點：**  
Claude Code 用 3.2–4.2x 更多 token 卻在多項 benchmark 領先。深入比較兩者架構、失敗模式、定價。

**最有價值的部分：**
- Token 差距數據：Figma Plugin 任務 Codex ~1.5M vs Claude ~6.2M（4.2x）
- Claude Agent Teams 有依賴追蹤 + 直接訊息；Codex 沒有 inter-agent 協調
- Codex 創新：diff-based memory（差分移除舊 context 而非摘要，保留結構理解）
- Rakuten 案例：12.5M 行 codebase，Claude 數值精準度 99.9%
- 混合工作流：Codex 快速 prototype → Claude 架構審查 → Claude Agent Teams 執行 → Codex 收尾

**適合誰：** 評估工具選擇或規劃混合工作流的團隊

---

### 8. ハーネスエンジニアリング、全員が違うことを言っている（5 社解釈比較）
**檔案：** `harness-engineering-interpretations-zenn-kenimo.md`  
**來源：** zenn.dev/kenimo49  
**評分：** ★★★★（日文）

**核心觀點：**  
比較 OpenAI、Anthropic、LangChain、Birgitta Böckeler（martinfowler.com）、arXiv 論文對 harness 的不同定義。

**最有價值的部分：**
- OpenAI 角度：宣告式約束，人類 steering + 大規模並行
- Anthropic 角度：context anxiety 概念，長時間穩定性優先，盡量 single agent
- LangChain 數據：harness 設計改善讓 benchmark 從 52.8% → 66.5%
- Böckeler 最獨特觀點：TypeScript strict mode / Rust Borrow Checker 本身就是 harness，不需另外建
- 三步驟實用起點：寫 AGENTS.md → 自動化品質閘道 → 錯誤回饋循環

**適合誰：** 想理清 harness 概念發展脈絡的研究者

---

### 9. The importance of Agent Harness in 2026
**檔案：** `agent-harness-2026-philschmid.md`  
**來源：** philschmid.de（Hugging Face）  
**評分：** ★★★★

**核心觀點：**  
Phil Schmid 從「Bitter Lesson」視角論證 harness 為何必須保持輕量。模型的每次改版都可能讓你的「智慧控制邏輯」過時。

**最有價值的部分：**
- Benchmark 問題：1% leaderboard 差距無法偵測 50+ tool call 後的指令跟隨穩定性
- Harness 三大作用：驗證真實世界進步、提升使用者體驗上限、提供 hill-climbing 反饋迴路
- Manus 五次重寫、LangChain 三次重構、Vercel 移除 80% 工具的教訓
- **「Harness is the Dataset」**：agent 失敗的軌跡是下一代訓練數據的競爭優勢
- 訓練與推理環境收斂的預測：harness 將成偵測 model drift 的主要工具

**適合誰：** 想了解 harness 未來發展方向的技術領袖

---

### 10. What Is Harness Engineering（SmartScope 四象限）
**檔案：** `harness-engineering-overview-smartscope.md`  
**來源：** smartscope.blog  
**評分：** ★★★★

**核心觀點：**  
harness ⊇ context ⊇ prompt 的嵌套關係，以及四象限設計框架（Architecture constraints、Feedback loops、Workflow control、Improvement cycles）。

**最有價值的部分：**
- Can.ac 實驗：僅改工具格式，同一模型從 6.7% → 68.3%（約 10x 改善）
- OpenAI 百萬行案例五大原則：設計環境、機械強制架構、倉庫為單一事實來源、可觀測性、抗熵
- 診斷啟發法：「個別輸出偏差」是 context 問題；「重複使用後架構一致性下降」是 harness 問題
- 多 agent 並行時 harness 更重要：人覺得麻煩的細粒度邊界，正是 agent 最適合的工作方式

**適合誰：** 快速定位 context vs harness 問題根因

---

## ★★★ 實用參考，不需深讀

---

### 11. SWE-Bench Pro Leaderboard（2026）
**檔案：** `swe-bench-pro-morphllm.md`  
**來源：** morphllm.com  
**評分：** ★★★

**核心觀點：**  
解釋為何 SWE-bench Verified 80.9% 而 SWE-bench Pro 只有 45.9%。Verified 已被訓練資料污染，Pro 是更可靠的基準。

**關鍵數據：**
- Scaffolding gap：同一個 Opus 4.5，三個 agent system 跑出 50.2%–55.4%（5.2pp 差距完全來自 harness）
- Pro vs Verified：平均修改行數 107 vs 11，平均修改檔案數 4.1 vs ~1
- 失敗模式分析：semantic understanding 35.9%、context overflow 35.6%、tool-use inefficiency 42%（小模型）

**適合誰：** 需要評估 agent 效能基準的研究者

---

### 12. Claude Code vs Codex vs Aider vs OpenCode vs Pi（2026）
**檔案：** `ai-coding-harness-agents-2026-jock.md`  
**來源：** thoughts.jock.pl  
**評分：** ★★★

**核心觀點：**  
六個工具的快速比較：Claude Code（長任務自主）、Codex CLI（app 開發）、Aider（預算/稽核）、OpenCode（多模型）、Pi（自訂 harness）、Cursor（監督式 IDE）。

**關鍵數據：**
- Terminal-Bench 2.0：Claude Code harness 92.1% vs Codex CLI 77.3%
- Aider：4.2x token 效率優勢
- 選擇框架：自主隔夜執行 → Claude Code；App 開發 → Codex；預算限制 → Aider

**適合誰：** 快速選工具的工程師

---

### 13. What Is an Agent Harness?（Firecrawl）
**檔案：** `what-is-agent-harness-firecrawl.md`  
**來源：** firecrawl.dev  
**評分：** ★★★

**核心觀點：**  
入門概念文，結合 Firecrawl 服務介紹 harness 的 4 個核心組件。有輕微產品推廣成分。

**值得記錄：**
- ICML 2025 遊戲研究：啟用 harness vs 停用 harness，同模型所有遊戲 win-rate 均提升
- harness engineering 定義：「把每次 agent 失敗當成工程問題永久修復，而非重試的 prompt」

**適合誰：** 第一次接觸 harness 概念的入門讀者

---

### 14. ハーネスエンジニアリングは枠組みから始めよう（CADDi）
**檔案：** `start-harness-engineering-caddi.md`  
**來源：** caddi.tech  
**評分：** ★★★（日文）

**核心觀點：**  
降低 harness 整備心理障礙的實踐文章。核心洞見：**框架的存在比內容充實更重要**。空的 Rules 檔案只要放對位置，團隊就會自然填充。

**值得記錄：**
- `/update-coding-rule` skill 概念：實作中遇到問題 → 一個指令轉化成品質規則
- Rules index file 設計：`.claude/rules/` 只放路徑指引，本體另存，minimizes 條件式載入 token
- 「開發與 harness 整備不分離」的工作方式：同一個任務完成時順手完善 harness

**適合誰：** 想在既有團隊低阻力導入 harness 的工程師

---

## 無法收錄

| 文章 | 原因 |
|------|------|
| Building Claude Code with Harness Engineering (levelup.gitconnected.com) | Medium paywall，只能存取標題/摘要 |

---

## 閱讀路徑建議

**完全新手（30 分鐘入門）：**  
firecrawl → smartscope → philschmid

**工程師（想動手）：**  
anatomy-of-agent-harness → nyosegawa best practices → pasqualepillitteri runtime

**架構師（系統設計）：**  
agent-engineering-morphllm → agentic-harness-engineering-decodingai → interpretations-zenn-kenimo

**工具評估：**  
swe-bench-pro → codex-vs-claude-code → ai-coding-harness-agents-jock

**Claude Code 深度使用者：**  
zenn-sasadango（5 層設計）→ pasqualepillitteri（runtime）→ nyosegawa（best practices）

---

## 跨文章共識（5 篇以上提及）

1. **Harness ⊇ Context ⊇ Prompt** — 嵌套層級，harness 涵蓋一切
2. **「文件說要跑 linter」≠「Hook 強制跑 linter」** — advisory vs deterministic 的本質差異
3. **Manus 六個月五次重寫** — harness 需要持續精簡，不是一次建好
4. **同模型換 harness 效能差 5–22 個百分點** — harness 比模型選擇更影響結果
5. **Thin harness 趨勢** — 隨模型進步，harness 應該越來越薄；越複雜的控制邏輯越容易被下一個模型版本淘汰
6. **驗證循環是生產與 Demo 的分水嶺** — 沒有自我驗證能力的 agent 不是生產就緒
7. **Filesystem 是最基礎的 harness primitive** — 不需要 vector DB，git log + progress.json 已足夠
