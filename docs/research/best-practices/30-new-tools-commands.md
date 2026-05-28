# Claude Code 新工具與 Slash Commands（2026）

> 來源：23-whats-new-w13-w17.md / 26-new-features-2026-q1.md / 27-whats-new-w18-w19.md / 2026-w20 整合  
> 整理日期：2026-05-28  
> 涵蓋版本：v2.1.83 → v2.1.142（W13–W20）

補充各主題章節未收錄的使用者介面、終端體驗、及新增 slash commands。

---

## 一、Computer Use — 桌面與 CLI 控制

### Desktop App（W13, research preview）

在 Desktop app 中直接控制真實桌面（原生 app、iOS simulator、硬體 control panel）。預設關閉，每次操作前詢問確認。

適用場景：
- 沒有 API 的 app
- 專有工具或純 GUI 工具
- iOS simulator 互動測試

```text
> Open the iOS simulator, tap through onboarding, and screenshot each step
```

### CLI 擴展（W14, research preview）

CLI 也可使用 Computer Use：

```text
/mcp → 找到 computer-use → 開啟
```

---

## 二、Terminal UI 功能

### Flicker-free Rendering（W14, v2.1.89）

Alt-screen renderer，prompt input 釘在底部，支援跨長對話的滑鼠選取，消除重繪 flicker。

```bash
export CLAUDE_CODE_NO_FLICKER=1
claude
```

取消：`unset CLAUDE_CODE_NO_FLICKER`

### `/tui` — 即時切換 Renderer（W16）

在 session 中隨時切換 classic / flicker-free renderer，不需重啟：

```text
> /tui
```

### Custom Themes — 自訂配色（W17, v2.1.118）

```text
> /theme    # 開啟 theme picker
```

手動編輯 `~/.claude/themes/` 中的 JSON（選擇 base preset 並覆蓋特定 token）。Plugin 也可打包 theme 一起發布。

### Vim Visual Mode（W17）

在 prompt input 中使用 vim 選取：

| 按鍵 | 功能 |
|------|------|
| `v` | 字元選取模式 |
| `V` | 行選取模式 |

支援完整 vim operator（d、y、c 等）。

---

## 三、Session 管理新指令

### Session Recap（W16 Other wins → W17 正式功能）

切換 focus 後回到 session 時顯示一行摘要，適合同時跑多個 Claude session：

```text
> /recap    # 手動觸發
# 輸出範例：* recap: Fixing the post-submit transcript shift bug. PR #29869. Next: ...
```

在 `/config` 關閉自動 recap。

### PR URL 恢復 Session（W18, v2.1.122）

在 `/resume` picker 中貼入 PR URL（輸入第一個字元進入搜尋模式），列表自動過濾到建立該 PR 的 session：

```bash
claude --from-pr 1234         # CLI 直接指定 PR 號
claude --from-pr <github_url> # 或直接貼 PR URL
```

支援 GitHub、GitHub Enterprise、GitLab、Bitbucket 的 PR/MR URL。

---

## 四、/insights — 工作流自我診斷（2026-02-04）

來源：Thariq（@trq212，Anthropic Claude Code 核心成員）

```text
> /insights
```

讀取過去一個月的 message history，輸出三份分析：

1. **專案摘要**：這個月在做什麼（專案類型、主要任務）
2. **使用模式分析**：哪些功能用得多、哪些沒用到
3. **工作流改進建議**：基於使用模式提出具體改進

**使用時機：**
- Session 初期診斷：了解上個月工作模式，確認方向
- 定期複查（每週或每月）：檢視工作流是否退步或可改進
- 學習新功能前：先看建議，確認哪些對你特別有價值

**注意：**
- 一個月 history 的 token 量可能相當大，初次執行前確認 context 用量
- 若常用 `/clear`，history 可能不連貫，建議品質會下降

---

## 五、/powerup — 互動式功能教學（W14）

```text
> /powerup
```

內建動畫 demo 的互動式課程，直接在 terminal 中教學 Claude Code 功能，適合新成員或想探索未用過功能的用戶。

---

## 六、/terminal-setup（W18）

```text
> /terminal-setup
```

啟用 iTerm2 clipboard access，讓 `/copy` 指令在 tmux 中也能正常運作。

---

## 七、/feedback — 跨 Session 回報（W20）

```text
> /feedback
```

W20 更新：可附加最近 24 小時或 7 天的 sessions，用於回報跨多個 session 的問題。

---

## 速查表

| 指令 / 功能 | 版本 | 主要用途 |
|------------|------|---------|
| Computer Use（Desktop）| W13 | 控制真實桌面 / iOS sim |
| Computer Use（CLI）| W14 | CLI 版本（research preview）|
| Flicker-free Rendering | W14 | 無閃爍 terminal UI |
| `/tui` | W16 | 即時切換 renderer |
| Custom Themes | W17 | 自訂配色方案 |
| Vim visual mode | W17 | v/V 選取 operator |
| Session Recap / `/recap` | W17 | 多 session 工作流摘要 |
| PR URL Session Resume | W18 | 從 PR URL 恢復 session |
| `/insights` | 2026-02 | 工作流自我診斷 |
| `/powerup` | W14 | 互動式功能教學 |
| `/terminal-setup` | W18 | iTerm2 tmux clipboard |
| `/feedback` 跨 session | W20 | 附加歷史 sessions 回報 |
