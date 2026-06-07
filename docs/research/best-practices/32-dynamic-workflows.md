# Dynamic Workflows 完整指南

> 來源：  
> - [Introducing dynamic workflows in Claude Code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)（2026-05-28）  
> - [A harness for every task: dynamic workflows in Claude Code](https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code)（2026-06-02）  
> 作者：Thariq Shihipar、Sid Bidasaria（Anthropic）  
> 整理日期：2026-06-05  
> 版本：W22（v2.1.150–v2.1.157）

---

## 什麼是 Dynamic Workflows

Claude 根據任務動態撰寫並執行 JavaScript 協調腳本，可在同一 session 中協調數十到數百個並行 subagent。

> "Claude can now write its own harness on the fly, custom-built for the task at hand."

**解決的三個失敗模式：**

| 失敗模式 | 說明 |
|---------|------|
| Agentic laziness | 複雜多步驟任務中提前停止 |
| Self-preferential bias | 需要驗證時偏向自己的結果 |
| Goal drift | 連續摘要導致目標漂移 |

---

## 啟動方式

**方法一**：直接請求

```text
> create a workflow that migrates every internal fetch() call to the new HttpClient wrapper
```

**方法二**：啟用 ultracode 設定（讓 Claude 自行決定何時使用 workflow）

```text
> /effort ultracode
```

管理執行中的 workflows：

```text
> /workflows
```

---

## 六大 Workflow 模式

| 模式 | 說明 | 適用場景 |
|------|------|---------|
| **Classify-and-act** | 依任務類型路由到不同 agent | Issue triage、文件分類 |
| **Fan-out-and-synthesize** | 並行分散 → 合併結果 | 大型 codebase 搜尋、研究報告 |
| **Adversarial verification** | 獨立 agent 驗證輸出 | 事實核查、安全審查 |
| **Generate-and-filter** | 生成候選 → 依品質篩選 | 程式碼生成、創意工作 |
| **Tournament** | 競爭 agent 解題 → 兩兩評判 | 排序、最佳解尋找 |
| **Loop until done** | 持續生成直到停止條件 | 遷移、批次處理 |

---

## 技術能力

- **模型選擇**：workflow 決定每個 subagent 使用哪個 Claude 模型
- **隔離**：subagent 可在獨立 worktree 執行，context 完全隔離
- **續接**：中斷的 workflow 可從最後 checkpoint 恢復
- **整合**：與 `/goal`、`/loop` 指令相容

---

## 實際應用案例

### 大型遷移

Bun 用 dynamic workflows 將 ~750,000 行從 Zig porting 到 Rust，11 天完成，通過 99.8% 既有測試：
- 一個 workflow 處理 lifetime mapping
- 並行 agents 完成各檔案 porting，每檔有雙重 reviewer

### 深度研究

`/deep-research` skill 內部使用 fan-out 並行 web 搜尋 + adversarial 驗證。

### 大型 Codebase 審查

全 codebase 安全 audit：並行搜尋 → 獨立驗證 → 整合報告。

---

## 何時使用 vs 何時不用

**使用情境：**
- 任務太大，單一 context window 無法協調
- 需要並行化或獨立驗證
- 高價值、複雜、反覆精煉

**不使用情境：**
- 標準編碼任務（不需多 agent 協調）
- Token 成本敏感任務（workflows 消耗明顯更多 token）

---

## 最佳化技巧

```text
# 設定 token 預算
> create a workflow to refactor auth module, use 10k tokens

# 結合 /goal 定義完成條件
> /goal all tests pass; create a workflow to fix failing tests

# 儲存 workflow 供重複使用
~/.claude/workflows/   # 個人
skills/                # 透過 skill 發布
```

---

## 方案可用性

| 方案 | 可用性 |
|------|------|
| Max、Team Premium、Enterprise PAYG、API | 預設可用（Research Preview） |
| Pro | 不支援 |
| 管理員 | 可關閉 |

平台：CLI、Desktop、VS Code extension、Claude API、Bedrock、Vertex AI、Microsoft Foundry。
