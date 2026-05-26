---
title: "32 Tricks to Level Up Claude Code in 16 Mins — @nateherk"
creator: Nate Herk
date: 2026-04-27
type: video
---

# 32 Tricks to Level Up Claude Code in 16 Mins — @nateherk

**影片來源**：https://www.youtube.com/watch?v=jqoFP9QapXI
**作者**：Nate Herk（@nateherk，YouTube 650K+ 訂閱）
**發布日期**：2026-04-27
**收錄日期**：2026-04-29
**研究方法**：透過 yt-dlp 取得英文自動字幕（VTT），全文解析後整理。字幕準確，涵蓋完整 32 個技巧。
**延伸分析**：@elliotchen100 推文（`research/tweets/2026-04-29-@elliotchen100-032393.md`）

---

## 完整 32 技巧（來自原始字幕）

### 入門層（Hacks 1–10）

1. **`/init` on every project** — 掃描整個 codebase，自動生成 CLAUDE.md（架構、慣例、關鍵檔案）；新專案也可對話式產生
2. **Status line** — `/status line` 設定 terminal 底部的 mini dashboard（model、context%、cost）
3. **Voice input** — `/voice` 原生語音輸入（仍在推廣中）；也可用第三方 dictation app
4. **Keep context small** — 不要把整個 codebase 倒進去，只給當前任務需要的內容
5. **`/context` for token bloat** — 查看各來源（system prompt、file、MCP）的 token 佔比
6. **Compact at 60% + clear between tasks** — context 達 60% 時 `/compact`（可指定保留哪些決策）；換任務用 `/clear`
7. **Always start in Plan Mode** — `Shift+Tab` 切換；規劃完才執行，大幅減少 revision
8. **Treat Claude like junior dev** — 給問題而非命令（「如何處理 X？」而非「寫一個做 X 的函式」），讓它推理後再行動
9. **Make Claude ask questions** — 告訴它「持續問我問題直到 95% 確信理解需求」
10. **Self-checking to-do lists** — 每個 to-do 後面接驗證步驟（截圖、DevTools 檢查），設定「達 95% 信心才進下一步」

### 進階層（Hacks 11–22）

11. **Sub-agents for parallel work** — 主 thread 派生獨立 sub-agents（各自有獨立 context window、可跑不同 model）；sub-agents 完成後回報結論
12. **Custom skills** — 可複用的 prompt 文件（對應 .claude/skills/）
13. **Cheaper models for simple tasks** — 讓 sub-agents 跑 Haiku，主 thread 跑 Opus
14. **Exit fast, re-prompt clean** — 走偏立刻 ESC，不要讓它自己掰回來（見原理三）
15. **`/memory` for cross-session recall** — 儲存跨 session 需要記憶的事
16. **Steer tight and steer early** — 走錯方向的每一步都是浪費的 context，越早修正越好
17. **Challenge outputs aggressively** — 輸出不夠好時說「Scrap that. Do a more elegant version.」，第二次往往明顯更好；然後讓它更新 skill 或 CLAUDE.md
18. **`/rewind` for quick undos** — 回滾到對話的前一個節點，無需重開
19. **Hooks for notifications** — `/hooks` 設定完成通知音效（可同時跑 15 個 session，聽到聲音才看）
20. **Screenshots for visual feedback** — Claude 可以看見，可截圖讓它自檢 layout 是否正確
21. **Chrome DevTools** — 可打開 browser、互動、檢查 app 功能
22. **Clone inspiration sites** — 餵截圖讓 Claude 重現設計模式

### 高階層（Hacks 23–32）

23. **Git worktrees for parallel sessions** — `claude --worktree <feature-name>`，每個 worktree 是獨立 branch，多個 session 並行不互相覆蓋
24. **API endpoints vs MCP servers** — ⚠️ **MCP server 會把所有工具定義載入 context**；若只需要單一功能，直接 hardcode API endpoint 省更多 token（例：只需讀 Notion 一個 database，就不要載入整個 Notion MCP）
25. **`/loop` for recurring tasks** — 「每 5 分鐘檢查部署狀態」，loop 在 background 跑，有事才打斷你；上限 3 天；也可設一次性提醒（「下午 3 點提醒我 check X」）
26. **VPS for always-on sessions** — SSH in 隨時互動，透過 Telegram 對話
27. **Remote control from phone** — Claude Code 新功能，本地執行、手機遙控；程式碼不離開本機
28. **No-SQL data analytics** — 連接 CLI 工具（如 BigQuery's `bq`），自然語言查詢
29. **`ultrathink`** — 輸入 `ultrathink` 分配最高 ~32,000 token 思考預算；架構決策、複雜 debug、大重構時使用
30. **Edit permissions for safe autonomy** — 明確 allow 安全命令，明確 deny 破壞性操作（delete/remove），不用 `--dangerously-skip-permissions` 也能達到同樣速度
31. **Agent teams** — 所有 agent 可互相通信、共享 task list、互相分配工作；比 sub-agents 更貴但產出更凝聚（適合大型專案）
32. **Context7 MCP** — 即時拉取最新函式庫文件（Next.js、React、MongoDB 等），解決訓練資料截止問題

---

## 核心心智模型（@elliotchen100 深度拆解）

> 把 Claude Code 當成「有限注意力、有限時間、有性格」的同事來管理，不是「無限算力的工具」來用。

### 六大原理

**原理一：Prompt 路徑決定推理深度**
- 命令式 → 淺層 pattern match
- 描述式（不帶預設答案）→ 觸發 chain-of-thought
- prompt 中預設的答案越少，激活的推理空間越大

**原理二：60% compact 是對抗 lost-in-the-middle，非省 token**
- 60% 是 Nate Herk 影片中的實踐建議（非 Stanford 論文數字）
- Stanford 2023「Lost in the Middle」（TACL 2024）確認 U 型注意力曲線，但**論文本身未提供百分比閾值**
- @elliotchen100 連結了論文機制來解釋 60% 背後的原理
- compact 判斷信號：模型開始問「你想做什麼」之類的迷失問題

**原理三：走偏立刻 exit（修正成本 ≈ 重開 2-3 倍）**
- 被污染 context 下，LLM confirmation bias 比人類更嚴重
- 修正 prompt 本身 + 道歉 + 受影響的輸出，三項加總超過重開成本

**原理四：Sub agents 核心是 context 隔離（樹形）**
- 父 agent 拿結論，不拿過程
- 最適任務：「需要大量探索但只需要少量結論」

**原理五：按「認知步驟數」選模型**

| 認知步驟數 | 推薦 | 原因 |
|-----------|------|------|
| 1-2 步 | Haiku | 大模型對簡單任務有過度設計副作用（30 行 vs 10 行） |
| 5 步以上 | Sonnet / Opus | 複雜推理 |
| 10 步以上 | ultrathink | 最高思考預算 |

**原理六：/loop 是把 Claude 變成異步值班同事**
- 輸入是狀態，輸出是「有事/沒事」判斷
- 適合：CI 監控、慢查詢掃描、PR queue 輪詢

---

## 官方來源驗證

| 主張 | 來源 | 狀態 |
|------|------|------|
| Lost in the Middle U 型注意力曲線 | Stanford / TACL 2024（arxiv 2307.03172） | ✅ 確認真實論文 |
| 60% compact 閾值 | Nate Herk 影片（字幕直接引用） | ✅ 為影片實踐建議，非論文數字 |
| MCP server 載入所有工具定義進 context | Nate Herk 影片（Hack #24） | ✅ 字幕直接陳述，符合 Claude Code 架構 |
| ultrathink ≈ 32,000 token 思考預算 | Nate Herk 影片（Hack #29） | ✅ 字幕直接陳述 |
| 走偏修正成本 2-3 倍 | @elliotchen100 個人估計 | ⚠️ 無第三方驗證 |
| 認知步驟分層（1-2/5/10）| @elliotchen100 個人實踐 | ⚠️ 合理啟發，需個人驗證 |

---

## Workspace 整合分析

### 新發現（影片獨有，workspace 未覆蓋）

1. **認知步驟數選模型判準** → 加入 `subagent-strategy.md`
2. **MCP vs API endpoint token 效率說明** → 現有 `defer_loading: true` 設計已覆蓋此原則，可補充引用來源
3. **Context7 MCP** → 可考慮加入 workspace MCP 設定（解決文件截止問題）
4. **`/status line` + `/context`** → 未在規則中明確提及，可加入 `context-management.md` 工具清單

### 已有對應（無需重複）

- Sub agent isolation > parallelism → `subagent-strategy.md` + `subagent-advanced.md`
- Fail fast / rewind → `session-management.md`
- /loop 異步同事 → `routines.md`
- Hooks for notifications → `auto-sync.md` + `opus47-best-practices.md`
- Git worktrees → `subagent-advanced.md`
- Descriptive prompts → `core.md` Think Before Coding
- Plan Mode → `quality.md`
- Permissions allow/deny → `settings.json` 已有完整配置

### 不需採納

- 60% threshold 取代現有 70%/30-35% — 現有規則更細緻（任務類型分層），60% 可作為輔助參考信號
