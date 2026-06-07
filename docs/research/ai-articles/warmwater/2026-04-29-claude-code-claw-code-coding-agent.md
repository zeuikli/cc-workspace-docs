---
url: "https://warmwater.dev/blog/claude-code-claw-code-coding-agent"
title: "Claude Code：從 claw-code 的分析看一個 Coding Agent 的設計關心"
date: 2026-04-29
category: Source Code
source: warmwater.dev
---

[
← Source Code ](/blog?tag=Source%20Code)  Source Code 
 
# Claude Code：從 claw-code 的分析看一個 Coding Agent 的設計關心
 
 2026-04-29 · — views  
  
  
claw-code 是 Claude Code 的 clean-room 重寫版。它本身是一個研究工具，不過有意思的地方不是重寫這件事，而是它帶出來的參考資料：29 個子系統 JSON 快照，描述了一個 1902 個 TypeScript 檔案、104 個 hook 模組、130 個 service 模組的系統。


讀這些快照，有件事讓我停下來：安全相關的基礎建設佔了多少份量。`BashTool` 子目錄有 9 個模組（主入口、權限層、安全檢查、命令語義分析、破壞性命令警告、sandbox 判斷……），`hooks/` 有 104 個模組，`permissions/` 貫穿整個架構。這些數字說的事情比任何功能清單都直接：**Claude Code 的核心問題，是怎麼讓一個有能力執行任意 shell command 的 Agent 在你的機器上安全地工作。**


**讀完精華版（2 分鐘），你會理解：**


- Claude Code 的 Hook 系統為什麼設計得這樣簡單，三個 exit code 決定一切
- PermissionMode 的有序 enum，以及為什麼 shell execution 的子系統要反覆分拆
- System Prompt Dynamic Boundary 是什麼，以及它解決的 prefix cache 問題
- Compaction 為什麼是本地確定性算法（不用 LLM），和 CrewAI 的對比
- Hooks / Skills / MCP 三個擴展層的設計分工


---


## 精華版


| 設計維度 | 設計選擇 | 核心用意 |
| --- | --- | --- |
| Hook 系統 | 3 個 exit code（0 / 2 / 其他非零） | 最小協議讓任意可執行檔都能成為攔截點 |
| PermissionMode | 有序 enum + 3 種 Prompter | 同一 runtime，不改核心 loop，在互動 / headless / 測試間切換 |
| System Prompt 結構 | __SYSTEM_PROMPT_DYNAMIC_BOUNDARY__ 切兩段 | 靜態段命中 prefix cache，動態段每輪刷新，兩件事不互相犧牲 |
| Compaction 策略 | 本地確定性 XML 算法，不呼叫 LLM | 保留的是「正在進行的工作狀態」，而非語意重要性 |
| 擴展機制 | Hooks / Skills / MCP 三層 | 執行介入、行為複用、外部能力整合，三個需求各走各的層 |


**各子系統一句話**


- **Hook 系統**：exit 2 是硬性阻擋，其他非零是帶資訊繼續跑，feedback 不論 allow 或 deny 都進入 model context，讓 Agent 知道上一步被攔截的原因。
- **PermissionMode**：`ReadOnly < WorkspaceWrite < DangerFullAccess < Prompt < Allow` 有序排列，`bash` 工具需要最高級，能力越強要求越高，runtime 比大小決定放行或升級。
- **System Prompt Dynamic Boundary**：sentinel string 把 system prompt 切成可快取的靜態前段與每輪刷新的動態後段，快取優化在架構設計時就決定，不是事後補丁。
- **Compaction 策略**：觸發門檻 200,000 input token，壓縮為結構化 XML，`<analysis>` 丟棄、`<summary>` 保留，不依賴 LLM 推斷，與 CrewAI 的 EncodingFlow 需要呼叫 LLM 評估重要性形成直接對比。
- **擴展層（Hooks / Skills / MCP）**：Hooks 用 shell exit code 介入工具執行、Skills 用 Markdown slash command 在對話層注入行為、MCP 用 JSON-RPC 整合外部能力，三層職責不互相污染。


**設計問題簡答**


**Q：為什麼 Hook 只用 3 個 exit code，不設計更豐富的回傳格式？**
因為 exit code 是所有可執行檔的最小公分母，shell script、Python、Go binary 都能用。豐富的回傳格式會把 hook 限制在「需要理解特定格式的程式」，exit code 讓任何工具都可以成為攔截點。


**Q：PermissionMode 為什麼設計成有序 enum 而不是一組布林旗標？**
有序 enum 讓「A 的權限是否涵蓋 B 的需求」這個問題可以用一個比較運算回答。布林旗標需要管理所有組合的相容性，有序 enum 把這個問題收斂成線性順序。


**Q：System Prompt Dynamic Boundary 解決了什麼具體問題？**
Anthropic API 的 prefix cache 只在完全相同的前綴時命中。如果每輪都把動態的 git status、環境資訊混進 system prompt，cache 永遠失效。Dynamic Boundary 讓靜態規則享有快取，動態資訊每輪刷新，兩件事不互相犧牲。


**Q：Compaction 不用 LLM 的代價是什麼？**
代價是「語意判斷能力」。LLM-based compaction（如 CrewAI 的 EncodingFlow）可以推斷哪段對話對後續任務最重要。Claude Code 的確定性算法只能保留結構化事實：pending work、動過的檔案、最近的 request。這個設計假設是：coding agent 的長對話裡，工作狀態比語意重要性更需要確定性保留。


---


> 
以下是完整版，按需取用。


---


## Hook 系統：用 exit code 定義一條攔截線


Claude Code 的 Hook 系統設計讓我意外的，是它有多簡單。


協議是這樣的：每次 Agent 要呼叫工具，Claude Code 會先執行所有設定的 hook command。這些 command 收到的是一個 JSON payload（透過 stdin），裡面是「誰要做什麼」：


```
{
  "hook_event_name": "PreToolUse",
  "tool_name": "Bash",
  "tool_input": {"command": "rm -rf ./build"},
  "tool_result_is_error": false
}

```


然後 hook command 用 exit code 表達意見：


```
exit 0  = 允許，繼續執行
exit 2  = 拒絕，阻擋工具執行（stdout 作為拒絕訊息）
其他非零 = 警告，繼續執行，但 stdout 附加進工具結果

```


任何可執行檔都可以當 hook，shell script、Python script、Go binary，沒有限制。設定長這樣：


```
{
  "hooks": {
 "PreToolUse": [
 {
 "matcher": "Bash",
 "hooks": [{"type": "command", "command": ".claude/hooks/validate.sh"}]
 }
 ],
 "PostToolUse": [
 {
 "matcher": "Write|Edit",
 "hooks": [{"type": "command", "command": "eslint --fix $CLAUDE_FILE_PATHS"}]
 }
 ]
  }
}

```


這個設計有一個值得注意的地方：**hook feedback 不論是 allow 還是 deny，都會進入 model context**。exit 0 的情況下，hook 的 stdout 可以作為附加資訊送進對話；exit 2 拒絕時，拒絕原因也進入 context。這意味著 hook 不只是守門員，它還可以悄悄注入資訊，讓 Agent 在下一步知道上一個工具被攔截的原因。


對比 CrewAI 的 Guardrail：兩者都在攔截輸出，但層次不同。Guardrail 是「task 完成後，檢查結果是否符合規格」，是業務層的驗收。Claude Code 的 hook 是「工具執行前後，決定這個 shell command 能不能跑」，是執行層的安全閘。一個在意輸出的品質，一個在意執行的安全性。


---


## Permission 系統：有序的 Mode 層級


如果說 hook 是外部可設定的攔截層，Permission 系統就是內建的信任模型。


Claude Code 的 `PermissionMode` 是一個有序的 enum：


```
ReadOnly  <  WorkspaceWrite  <  DangerFullAccess  <  Prompt  <  Allow

```


每個工具有它需要的最低 permission mode。`bash` 工具的 `required_permission` 是 `DangerFullAccess`，是所有工具裡最高的，因為 shell execution 可以做任何事。`read_file` 只需要 `ReadOnly`，`write_file` 需要 `WorkspaceWrite`。


當 Agent 要呼叫一個工具，runtime 會比較 active mode 和 required mode：active mode 大於等於 required mode 就放行；否則拒絕，或是進入 Prompt mode，彈出一個 Y/N 讓使用者決定。


讓這個設計真正有彈性的，是 `PermissionPrompter` trait 的設計：


```
InteractivePrompter  →  終端 Y/N 提示，等人類確認
RecordingPrompter →  預設答案（測試用）
None →  自動拒絕所有需要升級的操作（headless 模式）

```


同一個 `ConversationRuntime`，透過注入不同的 prompter，可以在互動模式（人工確認每個危險操作）、自動化腳本（headless，遇到需要升級的操作直接停下）、測試環境（預設答案跑完整流程）之間切換，不需要修改核心 loop 邏輯。


`BashTool` 子系統的分拆也在說同一件事。9 個模組，`bashPermissions.ts`、`bashSecurity.ts`、`commandSemantics.ts`、`destructiveCommandWarning.ts`、`shouldUseSandbox.ts`、`readOnlyValidation.ts`、`sedValidation.ts`……這不是過度設計，而是在說 shell 執行的「安全」這個問題有多少個維度。什麼命令是破壞性的？`sed` 的哪些用法需要特別處理？什麼情況下要進 sandbox？每個問題都是一個模組在回答。


---


## System Prompt Dynamic Boundary


Claude Code 有一個設計細節很少被討論：system prompt 的組建方式。


大多數框架在每一輪對話前，會重新組建完整的 system prompt，把環境資訊、設定內容、CLAUDE.md 全部塞進去，送出去。問題是 Anthropic API 有 prefix cache：如果 prompt 前綴和上一輪完全一樣，API 就不需要重新處理那部分，可以省下大量 input token 費用。只要 system prompt 每輪都不一樣，cache 就完全沒用。


Claude Code 的解法是一個叫做 `__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__` 的 sentinel string，把 system prompt 切成兩段：


```
[靜態部分，可快取]
intro | system rules | task-doing guidelines | CLAUDE.md 固定內容

__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__

[動態部分，每次刷新]
environment info | git status | project context | 當前 session 變數

```


靜態部分每輪都一樣，享受 prefix cache；動態部分每次刷新，每次重新計算。快取優化不是事後加進去的補丁，而是在架構層就決定了哪些內容是穩定的、哪些是會變的。


這個解法和 hermes-agent 的做法形成有趣的對比。hermes 的選擇是：system prompt 在 session 開始時 build 一次，之後永遠不重建。兩個方案都在解 prefix cache 的問題，但方向不同：hermes 用「完全不改」換取 cache 命中，Claude Code 用「切成兩段」讓動態內容和快取策略共存。


---


## Compaction：確定性算法，不用 LLM


長對話的 context 管理，是這個系列每個框架都必須面對的問題。Claude Code 的答案，和前面所有框架都不一樣。


觸發條件：累積 input token 超過 200,000，自動壓縮。壓縮的格式是結構化的 XML：


```
<analysis>
推理過程（不保留）
</analysis>
<summary>
- scope count: N
- tool mentions: bash, read_file, edit_file
- 最近 3 個 user requests: ...
- pending work: TODO / next steps / remaining tasks
- key files: ./src/main.py, ./config.yaml
- timeline: [完整執行事件序列]
</summary>

```


`<analysis>` 裡的推理過程在壓縮後丟棄，`<summary>` 裡的結構化狀態保留。這個算法是本地確定性的，不額外呼叫 LLM，runtime 直接計算，沒有額外成本也沒有隨機性。


對比 CrewAI 的 memory 系統（EncodingFlow 會呼叫 LLM 推斷重要性和 scope）和 hermes-agent 的 compaction（用 LLM 對壓縮段落做摘要），兩者都依賴 LLM 的判斷來決定「什麼值得保留」。Claude Code 的判斷是結構化的：pending work、key files、最近的 request、tool mentions，這些不需要 LLM 來推斷。


這個選擇背後有一個假設：coding agent 在長對話裡，需要確定性保留的不是「語意上最重要的事情」，而是「正在進行的工作狀態」。pending work 是什麼？動過哪些檔案？這些是確定性的事實，不需要語意判斷。


---


## 三個擴展層：Hooks / Skills / MCP


Claude Code 有三個擴展機制，乍看都是「讓 Agent 能做更多事」，但設計上服務的是三個完全不同的需求。


**Hooks** 是執行層的介入。操作對象是工具呼叫本身，用來在 Agent 呼叫 Bash 之前驗證命令、在它寫完檔案之後跑 linter、在任何工具結果裡注入額外資訊。Hook 用 shell 協議（exit code）定義，不需要理解 Claude Code 的內部結構，任何能寫 shell script 的人都可以用。


**Skills** 是 context 層的擴展。每個 skill 是一個 Markdown 文件，定義一個可複用的「slash command 巨集」，不介入工具執行，而是在對話層注入行為。`/commit`、`/review-pr`、`/loop` 這類 skill，本質上是在告訴 Agent「遇到這個 trigger，按照這份說明做事」。claw-code 的參考資料顯示，Claude Code 有 20 個 bundled skill（`batch`、`loop`、`skillify`、`scheduleRemoteAgents`……），而且 skill 可以從 MCP server 動態提供。


**MCP** 是協議層的整合。JSON-RPC 2.0，讓外部 server 提供工具和 skill。5 種 transport（stdio subprocess、HTTP/SSE、WebSocket、OAuth gate……），支援整個 server 的生命週期管理。MCP 解決的問題不是「怎麼介入執行」或「怎麼複用行為」，而是「怎麼把外部能力接進來」。


三層的分工很清楚：有什麼事情需要在工具執行前後介入，用 Hook；有什麼行為需要複用，定義成 Skill；有什麼外部能力需要整合，走 MCP。三個需求不互相污染，各自走各自的層。


---


## 這些設計在問什麼問題


把這幾個機制放在一起，Claude Code 的問題比「怎麼做一個 coding assistant」更具體：**怎麼讓一個有能力在你的機器上執行任意命令的 Agent，安全地、可控地工作。**


這個問題的難度在於它有兩個互相拉扯的面向。讓 Agent 真的有用，它需要能執行 shell command、能改你的檔案、能接入外部工具。但讓這件事安全，你需要一個地方能攔截、能分級授權、能審計。Claude Code 的設計，是把這兩件事分別交給不同的層：MCP 和 Skills 負責「能做什麼」，Hooks 和 Permission 系統負責「能不能做、由誰決定」。


在這個系列裡，每個框架問的問題都不同。hermes 問「怎麼讓 Agent 越用越好」，OpenClaw 問「怎麼讓 Agent 永遠在線」，CrewAI 問「怎麼讓一組 AI 像組織一樣工作」，Claude Code 問的是「怎麼讓 Agent 安全地在你的環境裡執行」。這個問題決定了它為什麼在 bash 工具上花了 9 個模組，為什麼 hook 系統有 104 個模組，為什麼 permission mode 是有序的 enum 而不是一個布林值。


---


> 
**結語**：分析 claw-code 帶出來的參考資料，最讓我印象深刻的不是某個機制有多聰明，而是安全基礎建設佔的份量：104 個 hook 模組、bash 子系統的 9 層分拆、貫穿整個架構的 permission 系統。這些不是功能，是對「在你的機器上執行」這件事有多謹慎的一種量化。


## 延伸閱讀


- [四個 Agent 框架，四種對「穩定性」的理解](/blog/agent-20260430) — 系列總結：Claude Code 和 hermes、OpenClaw、CrewAI 並排比較，看四種不同的問題意識如何決定設計
- [hermes-agent：從原始碼看一個為 Production 設計的 Agent 系統](/blog/hermes-agent-production-agent) — 對照：hermes 用「完全不改 system prompt」解決 prefix cache，和 Claude Code 的 Dynamic Boundary 形成有趣對比
- [Superpowers Plan Mode：用 Claude Code Skill 打造 AI Agent 規劃流程](/blog/superpowers-plan-mode-ai-agent) — 實作面：Skills 擴展層的具體應用，從 slash command 到可複用的 Agent 行為

  
  
 [ Source Code ](/blog?tag=Source%20Code)[ Agentic System ](/blog?tag=Agentic%20System) 
 

### 相關文章
[System Design

Agent 要怎麼進化？六個系統的 Self-Improvement 機制比較

2026-05-22
](/blog/agent-self-improvement-design-comparison)[
System Design

SOUL 設計決定了 Agent 是什麼：六個 Agentic System 的 system prompt 比較

2026-05-22
](/blog/agent-soul-design-comparison)[
Source Code

不預裝能力，只定義生長方式：GenericAgent 原始碼解析

2026-05-22
](/blog/generic-agent-source-code)
