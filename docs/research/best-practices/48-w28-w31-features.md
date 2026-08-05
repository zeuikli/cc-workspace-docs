# Claude Code W28–W31 新功能（v2.1.202–v2.1.221）

> 來源：[anthropics/claude-code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)（v2.1.202 – v2.1.221）
> 期間：2026-07-05 ~ 2026-08-03
> 整理日期：2026-08-04

---

## 1. 模型

- **Claude Opus 5（`claude-opus-5`）上線，1M context window**（v2.1.219）。詳見 `44-claude-opus-5.md`。
- Auto mode 的分類器對外部 session 預設改用 **Sonnet 5**（v2.1.210）。
- Vertex AI 重新啟用 tool search（Claude 4.5 世代以後的模型，v2.1.213）。
- transcript 現在**逐則記錄該訊息的 reasoning effort**（v2.1.212）；`subagentStatusLine` payload 也帶 effort（v2.1.214）。

---

## 2. Subagent / 背景 session 的治理（本期最大變化）

> 主軸：**把「無界扇出」關掉，把背景 agent 的收尾語義補上。**

| 變更 | 版本 | 內容 |
|------|------|------|
| 每 session subagent 上限 | v2.1.212 | 預設 200，`CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION` 可調；`/clear` 重置 |
| 同時執行 subagent 上限 | v2.1.217 | 預設 20，`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` 可調 |
| **預設不再巢狀 spawn** | v2.1.217 | subagent 不再生 subagent；要更深需設 `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` |
| 預算真正止血 | v2.1.217 | `--max-budget-usd` 達標後拒絕新 spawn **並中止執行中的背景 agent**（先前無效）|
| WebSearch 上限 | v2.1.212 | 每 session 預設 200 次，`CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` 可調 |
| Task 工具 `mode` 參數**廢除** | v2.1.212 | 現已忽略；subagent 預設繼承 parent 的 permission mode |
| `/fork` 語義改變 | v2.1.212–213 | `/fork` = 把對話複製成**獨立背景 session**（自有 worktree）；原本的 in-session subagent 改名 `/subtask` |
| 背景 session 收尾 | v2.1.205 → v2.1.213 | commit + push 保存工作；**只在任務需要時才開 draft PR**；遵守你的 CLAUDE.md git 指示；結束時一定回報工作落在哪 |
| `context: fork` skill | v2.1.218 | 預設改為背景執行，可用 `background: false` 個別退出 |
| MCP 長工具呼叫 | v2.1.212 | 超過 2 分鐘自動轉背景，`CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS` 可調 |
| Worktree 隔離修正 | v2.1.203/210/216 | 修掉 worktree-isolated subagent 用 `git -C` / `--git-dir` / `GIT_DIR` 把 git 指回主 checkout 的三個路徑 |

**對本 workspace 的影響**：`fusion` / `multi-mode-skill` 的委派假設需重讀——巢狀委派預設關閉、`mode` 參數失效、背景 session 會自行 commit/push（`core.md` Git 鐵律的「使用者明示不 commit」須寫進 CLAUDE.md 才會被遵守）。

---

## 3. 自動觸發的收斂：驗證與研究改為手動

- **v2.1.215**：Claude 不再自行跑 `/verify` 與 `/code-review`，要用就自己打。
- **v2.1.218**：`/deep-research` 同樣改為只在手動呼叫時啟動。
- **v2.1.218**：`/code-review ultra` 在非互動 session 不再靜默降級成本地審查，改為啟動雲端審查。
- **v2.1.202**：`/review` 改為快速單趟審查。
- **`/ultrareview`（新指令，雲端深審）** 本期大量修正：接受 `#123` / `PR 123` / PR URL、會 fetch 遠端分支並在打錯時建議相近分支名、`/clear` 後仍要求計費確認、無 merge base 時改為提議審查全部 tracked 檔、diff 過大時顯示上限/實測大小/最大貢獻檔。

**判讀**：官方正在把「驗證什麼時候跑」的決定權從模型手上收回 harness。本 workspace 的 TEST 閘門本來就由規則與 hook 驅動，方向一致；但任何「靠模型自動 review」的假設要作廢。

---

## 4. 權限與沙箱（安全修正密集期）

**Bash / PowerShell 權限繞過修正**（v2.1.213/214/216）：

- zsh 在 `[[ ]]` 條件式中執行隱藏命令 → 現在會提示
- 檔案描述子重導向形式 → 改為 **fail closed**
- **超過 10,000 字元的命令一律提示**，不再自動執行
- `help` / `man` 的危險選項、`file` 的 `-m`/`-f`、`docker`（含 Podman shim）的 daemon 重導向旗標（`--url`/`--connection`/`--identity`）→ 改為需要授權
- Windows PowerShell 5.1 的權限檢查繞過、含引號路徑、隱形 Unicode 字元 → 修正
- 非 ASCII 字元的 shell 詞界解析 → 對齊真實 shell

**權限規則語義變更（會改變既有設定行為）**（v2.1.214）：

> 單段 `dir/**` 的 **allow** 規則（如 `Edit(src/**)`）與 hook `if:` 條件，現在只匹配 `<cwd>/dir`，不再匹配樹中任意深度的同名目錄。要任意深度請寫 `**/dir/**`。`deny`/`ask` 規則維持任意深度匹配。

**沙箱**：

- `sandbox.credentials` 新增 `mode: "mask"`（Linux/WSL，v2.1.213）：沙箱內讀到哨兵副本，proxy 在對外時才換回真值；macOS 退回 `deny`
- `sandbox.network.strictAllowlist`（v2.1.219）
- `sandbox.filesystem.disabled`（v2.1.216）：只保留網路出口管制，跳過檔案系統隔離

**其他硬化**：

- `.claude` / `.claude/worktrees` 的 symlink 逃逸（workflow 儲存、排程任務寫入、worktree 建立）→ 修正（v2.1.212/216）
- `/rewind` 不再經 symlink/hard link 還原或刪檔，並回報跳過幾個路徑（v2.1.216）
- agent frontmatter hooks 需該 agent 檔所在資料夾已接受 workspace trust（v2.1.218）
- auto mode 新增「封鎖竄改 session transcript 檔」規則（v2.1.205）；對未解析變數的 `rm -rf` 會先問（v2.1.205）
- 啟動時對**過寬的 permission 規則**發出警告（v2.1.210）；permission 規則改存在 repo 根目錄，跨 worktree 持久（v2.1.211）
- 新增 **EndConversation 工具**：Claude 可終止極端濫用或越獄嘗試的 session（v2.1.214）
- 修正 permission preview 未中和特定 Unicode 字元導致核可訊息視覺被改寫（v2.1.211）

---

## 5. Context / cache / 記憶

- **prompt caching**：mid-conversation system block 現在在 LLM gateway 與自訂 base URL（Bedrock / Vertex / 1P）後方也生效（v2.1.212）
- auto-mode 權限檢查改為**重用已快取的對話前綴**，降低 cache 成本（v2.1.213）
- `/context` 超出視窗時顯示明確警告；`/compact` 失敗顯示為錯誤（v2.1.216）
- 修正 Opus 4.8 on Bedrock 從不觸發 auto-compact（v2.1.217）
- memory frontmatter 加 ISO `modified` 時戳（v2.1.214）；memory 值在行內 `#` 被截斷 → 修正（v2.1.214）
- 記憶索引警告改為只量測**實際載入**的內容（v2.1.211）
- `SendMessage` 內文不再重複灌進 replay 歷史與 tool result，降低 inter-agent 訊息 token（v2.1.212）
- 長 session 訊息正規化的二次方成本 → 修正（v2.1.216）
- Stats 面板納入 cache token，並分列 input / output / cache read / cache write（v2.1.213）

---

## 6. 工具鏈與企業治理

- **`claude-api` skill 新增 `prompt-audit` 子命令**（v2.1.213）：稽核 prompt 與 tool description 是否還帶著為舊世代模型寫的模式——與 `46-context-engineering-claude5.md` 同一問題意識
- `/doctor` 會提出 `CLAUDE.md` 精簡建議（v2.1.206）
- Dynamic workflow size 設定（控制 agent 數量）＋ `workflow.run_id` / `workflow.name` OTel 屬性（v2.1.202）
- OTel：`message.uuid` / `client_request_id` / `tool_source` 屬性（v2.1.214）、`CLAUDE_CODE_OTEL_CONTENT_MAX_LENGTH`（預設 60 KB 截斷）、managed settings 的 `OTEL_EXPORTER_OTLP_ENDPOINT` 現在統管所有 signal（v2.1.217）
- Enterprise `forceLoginMethod` 擴及 VS Code extension / SDK / `setup-token` / `install-github-app`（v2.1.212）
- Auto mode 在 Bedrock / Vertex / Foundry 免 opt-in（v2.1.207）
- 修正排程任務把自己設定的 prompt 當成不可信輸入而拒絕執行（v2.1.214）
- 修正 hook exit code 2 在 stdout JSON schema 驗證失敗時不阻斷（v2.1.214）；hook 逾時被誤報為使用者拒絕（v2.1.210）
- 修正 `continue:false` hook 的中止在工具失敗或中途完成時被丟棄（v2.1.212）

---

## 7. 介面

- Focus view 切換 `Ctrl+Alt+F`：把工具活動收進可展開的每輪摘要（v2.1.221）
- Screen reader mode（`--ax-screen-reader`）與刪字朗讀（v2.1.208/218）
- `/resume` 在 agent view 開啟過往 session 選單（含已從清單刪除者），選中即以背景 session 恢復（v2.1.212）
- `/status` 顯示 session 種類：`interactive` / 背景 `attached` / `unattended`（v2.1.213）
- emoji shortcode 自動補全（v2.1.217，`emojiCompletionEnabled` 可關）
- 左方向鍵誤丟對話 → 編輯後按下會先確認（v2.1.218）

---

## 8. 升級後建議重驗的本 workspace 假設

1. `Edit(src/**)` 類**單段 allow 規則**的匹配範圍已縮小 → 檢查 `settings.json` 與 hook `if:` 條件
2. 巢狀 subagent 預設關閉 → `fusion` / `multi-mode-skill` 的多層委派設計
3. Task 工具 `mode` 參數失效 → 依賴它切 permission mode 的地方改用 parent 模式繼承
4. 背景 session 會自動 commit/push → CLAUDE.md 的 git 指示成為唯一約束來源，須寫明
5. `/verify`、`/code-review`、`/deep-research` 不再自動觸發 → 驗證流程必須由規則、hook 或 SKILL 明確呼叫

---

## 延伸閱讀

- `42-w26-27-features.md` — 前一期（v2.1.185–201）
- `44-claude-opus-5.md` · `46-context-engineering-claude5.md` · `47-verification-loops-skills.md`
- `12-permissions.md` · `13-sandbox.md` — 權限與沙箱基礎（本期變更是其增量）
