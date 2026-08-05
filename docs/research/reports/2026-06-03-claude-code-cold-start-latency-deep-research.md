# Claude Code 冷啟動延遲與 Auto-Load 載入優化深度研究報告

**日期**：2026-06-03 | **分支**：`feature/autoload-coldstart-research`
**研究方法**：gap-map 去重 → latency 主軸 pivot → 本機實測 → arXiv 接地 → adversarial 校驗
**來源**：官方文件 5 處 · GitHub issues 9 個 · 社群/blog 5 處 · arXiv 全文 2 篇（另 2 篇摘要）· 本機 hook 實測 10+ 點

---

## 執行摘要

前作（2026-05-18 / 05-25 共 9+ 份報告）已徹底覆蓋 **token 重量**維度（auto-load ≤ 3,500 tokens、合規率 76%→52%、TYPE A/B/C/D 分類、defer_loading -85%）。本報告填補**未覆蓋的兩個 GAP**：

1. **冷啟動 wall-clock latency**（hook 執行時間、session init、MCP 連線）— 前作零覆蓋
2. **prompt cache 冷→暖機制**對 startup 的影響 — 前作僅覆蓋成本面，缺機制與 deferred-tool 交互

**核心結論**：Claude Code 的啟動與互動延遲，主要不在「載入多少 token」，而在「**每個 hook 各自 spawn 一個 Node.js/bash 進程的 cold-start 開銷**」。社群實測：11+ hooks 可使每 prompt 從 4.8s 暴增至 18–21s（+13–16s）。本機實測同樣指認 hook spawn 與同步 healthcheck 為延遲主因，而非 auto-load token 量。

**最高槓桿動作**（依社群 + 官方 + 本機交叉驗證）：
| 優先 | 動作 | 預期效果 | 來源 |
|------|------|---------|------|
| P0 | side-effect hook 加 `async: true`（v2.1.45+） | 不阻塞 model，回收阻塞延遲 | 官方 hooks doc |
| P0 | **security hook 不可 async** → 改 dispatcher / 內部優化 | 保留安全 + 降 spawn | Lane A #6/#8 + 安全紅線 |
| P1 | dispatcher 模式合併多 hook | V8 spawn 50–80ms → IPC ~2–5ms（-94~99%） | GitHub #26521 |
| P1 | prompt cache pre-warm（`max_tokens:0`） | 維持 cache 暖態，避免 resume cache miss | 官方 caching doc |
| P2 | MCP project-scoped + 待 `lazyConnect` | 減少 idle server spawn | GitHub #63251 |

---

## 1. 研究動機與去重定位

### 1.1 為何 pivot 到 latency

使用者首要訴求是「speed up cold start / 提升載入速度」。Gap-map 掃描 9+ 份既有報告 + 60+ 篇 papers，確認：

- **已覆蓋**：token-loaded-before-first-turn（auto-load 上限、合規率、cache 成本倍率、deferred token 數字）
- **零覆蓋**：startup 的真實 wall-clock 時間 — hook 執行 ms、session init 耗時、MCP 連線延遲、cache 冷→暖端到端時間

本報告 lead with latency（未服務的維度），token 維度僅引用前作數字接合，不重述。

### 1.2 概念框架（arXiv 接地）

兩篇 serverless cold-start 論文（雖屬 GPU/serverless 層，概念可遷移）建立本研究的分析框架：

- **HydraServe**（arXiv 2502.15524, PKU+Alibaba）：冷啟動延遲可由**架構重疊（overlap stages）與預備（proactive distribution）**消除，降 1.7–4.7×。對應：hook async 化 + cache pre-warm。
- **Cold-Start Anti-Patterns**（arXiv 2512.16066, UMich, IEEE SANER 2026）：把 cold-start 當 **developer-visible 設計問題**（非黑盒），從 81 issue reports 推導反模式（redundant imports / deferred one-time init / 大相依打包）。InitScope「loaded vs executed」框架 = 本研究 gap-map 同精神（auto-load 載入的有多少真被執行引用）。商業動機：**Amazon 每 +100ms 損失 1% 銷售**。

> 誠實標注：cold-start latency 屬系統工程，**Claude Code 專屬的學術文獻薄弱**。上述兩篇為概念類比，非直接研究 Claude Code；本報告主體證據來自官方文件 + GitHub issues + 本機實測。

---

## 2. 冷啟動延遲圖譜（本機實測 + 社群交叉驗證）

### 2.1 本機 hook 實測

> 方法學（誠實揭露）：**wall-clock，n=3，dummy `echo '{}'` stdin，cold interpreter 每次**。非生產負載 profiling，數量級可信、絕對值有 ±20% 噪音。

| Hook | 觸發時機 | 頻率 | 實測 avg | 性質 |
|------|---------|------|---------:|------|
| **pre-commit-review.sh** | PreToolUse `git commit` | 低（2 次/7天） | **2,965ms** | 低頻高延遲 — 96% 來自同步 `healthcheck.sh`（單獨 2,854ms） |
| **session-init.sh** | SessionStart | 每 session 1 次 | **592ms** | warm-cache 下 fetch=0ms（cache hit），592ms 主要是 shell init + 26 skill 掃描 + echo；**僅冷 clone 才含 fetch** |
| **user-prompt-submit.sh** | UserPromptSubmit | **每 prompt（阻塞）** | **146ms** | 高頻中延遲 — 每次互動前阻塞 model |
| **block-dangerous.sh** | PreToolUse `Bash` | **每次 Bash** | **53ms** | 高頻低延遲 — 安全 gate，**不可 async** |
| protect-sensitive-files.sh | PreToolUse `Edit\|Write` | 每次寫檔 | 56ms | 安全 gate，**不可 async** |
| pre-compact.sh | PreCompact | 偶發 | 73ms | side-effect |
| memory-sync.sh | (依設定) | 偶發 | 26ms | side-effect |
| ~~sdd-cache-pre.sh~~ | PreToolUse `WebFetch` | （已於 PR #743 刪除）| 33ms | cache |

**關鍵洞察**：
- 延遲不來自 auto-load token（16,927 bytes ≈ 4.2K tokens，cache 命中後 0.1× 成本，且不重複載入）
- 延遲來自**進程 spawn × 觸發頻率**。block-dangerous 53ms × 每次 Bash = 一個 50-tool-call 的 session 累積 ~2.6s 純 hook 開銷
- pre-commit 的 2,965ms 是低頻但體感最強的「卡住」點

### 2.2 社群實測交叉驗證（Lane A）

| 發現 | 數字 | 來源 | 類型 |
|------|------|------|------|
| `showSetupScreens()` 佔啟動 | **3,112ms**（總啟動 3,460ms） | GitHub #21261 | 定量實測 |
| 11+ hooks（9 lifecycle）每 prompt | **18–21s**（無 hook 4.8s，+13–16s） | ruflo #1530 | 定量實測 |
| 每 Node.js process spawn V8 cold-start | **50–80ms** | GitHub #26521 | 定量實測 |
| 63 hooks blocking overhead/tool call | **375–525ms** | GitHub #26521 | 定量實測 |
| → `type:"server"` IPC hook | **~2–5ms/call（-94~99%）** | GitHub #26521 提案 | 原型實測 |
| 95 hooks dispatcher 模式總開銷 | **~200ms/event** | blakecrosley.com | 實測 |
| static-analysis RAG hook wall-clock | **-35.3%（11.80s→7.64s）** | GitHub #53224 / MIT context-os | 定量實測 |
| Windows `tasklist\|findstr` | **599,879ms（~10min）→ 336ms** | GitHub #16257（已修） | 定量實測 |
| Claude Desktop eager loading 重啟 | **30–60s**（清 git-worktrees.json 可解） | GitHub #38346 | 定量實測 |
| MCP server 全部 eager connect | 無 wall-clock 數字（提案 `lazyConnect`） | GitHub #63251 | 定性 |
| HTTP MCP transport/call | +30–200ms（vs stdio 本地） | TrueFoundry | 估算 |

**社群與本機一致結論**：hook 進程 spawn 是 Claude Code 互動延遲的首要可控來源。

---

## 3. Prompt Cache 冷→暖機制（官方明文，Lane B）

前作覆蓋 TTL 5min + 90% discount。本報告補機制：

### 3.1 成本倍率與回本點
| 狀態 | 成本倍率 | 說明 |
|------|---------|------|
| Cache write（冷，5min TTL） | **1.25×** base input | 首次寫入 |
| Cache write（1hr TTL） | **2.0×** base input | `ttl:"1h"` |
| Cache read（暖） | **0.1×** base input | 兩種 TTL 皆同 |

- **回本點**：1.25 / (1−0.1) ≈ **1.4 次命中即打平**；≥2 次命中淨賺
- **無背景刷新**：cache 僅在被使用時刷新；TTL 過期 → 下次請求整個前綴重新 write（1.25×，非 read）
- 最低 cacheable：Opus 4.8 / Sonnet 4.6 = **1,024 tokens**；Haiku 4.5 = 4,096

### 3.2 Cache pre-warming（降冷啟動體感）
官方提供 `max_tokens:0` 觸發 cache write 而不產 output：
```python
client.messages.create(model="claude-opus-4-8", max_tokens=0,
  system=[{"type":"text","text":"...","cache_control":{"type":"ephemeral"}}],
  messages=[{"role":"user","content":"warmup"}])
```
不相容：`stream=true` / extended thinking / structured outputs / `tool_choice:any|tool` / batch。

### 3.3 20-block lookback
cache read 時從 breakpoint 往回最多掃 **20 個 block** 找最長匹配前綴；超出視為 miss → 需在舊 breakpoint 加 `cache_control`。每 request 最多 **4 breakpoints**。

### 3.4 cache-breaking 反模式（接合前作 dont-break-cache 論文）
timestamps / UUID / MCP server restart / mid-session 改 CLAUDE.md / 增刪 tool → 破壞靜態前綴 → cache miss → 成本 +30–60%。對應 CLAUDE.md context-management.md「mid-session 禁止切模型/增刪 tool/改 CLAUDE.md」。

---

## 4. Deferred-Tool / ToolSearch 機制（前作 GAP，官方明文）

本 session 即為實例：~30 個 deferred tools 經 ToolSearch 按需載入。

### 4.1 觸發閾值
- tool definitions > **10K tokens**，或 **10+ tools** → 自動 `defer_loading: true`
- Token 節省：50+ MCP 工具 77K → 8.7K tokens（**-85%**）；ToolSearch overhead 僅 ~500 tokens

### 4.2 與 cache 的交互（關鍵 — 前作未答）
官方明文：
> "Deferred tools are not included in the system-prompt prefix... the API appends a `tool_reference` block inline in the conversation... **The prefix is untouched, so prompt caching is preserved.**"

- deferred tool 的 schema **不計入 cache prefix**，被搜尋時注入 **messages 層**而非 system/tools 層 → **不破壞 cache**
- 兩種搜尋：`regex`（≤200 字元 pattern）/ `bm25`（自然語言）；每次返回 3–5 個工具
- 約束：**不可全部 deferred**（至少一個非 deferred，否則 400）；strict mode 相容

### 4.3 已知副作用（社群）
首輪不可用（#42148）、compact 後 reference 消失（#42835）、hook 衝突（#33073）、`--print` deadlock（#35262）。SkillSearch（skill 層 lazy-load）尚為 feature request。

---

## 5. 業界最佳實踐彙整（可執行，依優先序）

### 5.1 啟動層（SessionStart）
1. 升級至最新版（修 showSetupScreens async、Windows tasklist bug）
2. **SessionStart hook 維持 < 1s**（官方建議）；本機 session-init 592ms 可接受但 skill 掃描可快取
3. 清 stale `git-worktrees.json`（Desktop 30–60s → 大幅改善）

### 5.2 互動層（每 prompt / 每 tool call）
4. **side-effect hook 加 `async:true`**（logging/audit/notification）— v2.1.45+
5. **security/validation/context hook 維持同步**，改用 dispatcher 模式降 spawn（V8 50–80ms → IPC 2–5ms）
6. UserPromptSubmit hook 預設 timeout 30s（其他 600s）— 保持輕量
7. 同一 event 多 hook → 單一 dispatcher（cached stdin），避免各自讀 stdin 造成 JSON corruption

### 5.3 Cache 層
8. 靜態前綴（CLAUDE.md/rules/tools）放最前不動 → 最大化 cache 命中
9. resume 間隔 > 5min（TTL）→ 接受 cache miss 或 pre-warm；長閒置考慮 1hr TTL
10. 不在 mid-session 改 CLAUDE.md / 切模型 / 增刪 tool

### 5.4 MCP / Tool 層
11. ToolSearch（v2.1.7+ 預設開）已處理 token；wall-clock 連線待官方 `lazyConnect`
12. project-scoped settings 限制 MCP server 清單
13. local agent 用 stdio transport（非 HTTP）

---

## 6. 安全紅線（不可優化掉）

> ⚠️ **security hook 不可 async**：`block-dangerous.sh`（阻擋危險命令）、`protect-sensitive-files.sh`（保護憑證）、`user-prompt-submit.sh`（context 注入）若改 async，會失去阻擋/保護/即時注入能力 — 違反 CLAUDE.md 安全紅線（§生產環境安全紅線 + R12 Fail Loud）。

對這些 hook，正確路徑是**內部優化（dispatcher / 減 spawn / 加速 script）**而非 async。partition「async-safe vs must-stay-sync」是任何 hook 優化計劃的核心安全前提。

---

## 7. 附錄：arXiv 全文收錄

| arXiv | 標題 | 收錄 | 相關性 |
|-------|------|------|--------|
| 2502.15524 | HydraServe: Cold Start Latency for Serverless LLM | **全文 PDF + 摘要** | 間接（架構類比） |
| 2512.16066 | Cold-Start Anti-Patterns in Serverless（SANER 2026） | **全文 PDF + 摘要** | 間接但概念強相關 |
| 2604.06664 | Foundry: CUDA Graph Cold Start | 摘要連結 | 間接（CUDA 層） |
| 2512.01357 | Tangram: Serverless LLM Loading | 摘要連結 | 間接（GPU memory） |
| 2601.06007 | Don't Break the Cache（前作已收） | 既有 | cache 直接 |
| 2510.04618 | Agentic Context Engineering（前作已收） | 既有 | context 直接 |

---

## 來源清單

**官方**：[memory](https://code.claude.com/docs/en/memory) · [prompt-caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) · [tool-search-tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool) · [hooks](https://code.claude.com/docs/en/hooks) · [advanced-tool-use](https://www.anthropic.com/engineering/advanced-tool-use)

**GitHub issues**：#21261 #16257 #38346 #5186 #26521 #63251 #44536 #53224 #62327 · ruflo #1530

**社群/blog**：blakecrosley.com（95 hooks）· softwarethug.com（ToolSearch lazy load）· implicator.ai（cache miss as incident）· claudecodecamp.com · TrueFoundry

**本機實測**：8 hooks wall-clock + healthcheck 隔離計時 + auto-load byte（`wc -c`）+ live session-init elapsed
