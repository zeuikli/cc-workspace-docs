# CLAUDE.md 規則工程與 Hook 設計
> 來源：research/tweets/ Rule（40篇）+ Hook（1篇）分類
> 核心數據：200行上限（超過→compliance 76%→52%）；27% productive tokens（@Mnilax）

## 使用方式

**何時使用**：撰寫或稽核 CLAUDE.md 規則、設計 Hook 腳本、優化 token overhead 時。
**貼入哪裡**：`CLAUDE.md`、`.claude/rules/`、`.claude/settings.json`。

---

## 核心設計原則

### 1. 200 行硬上限（@vincemask + @Mnilax）
- 超過 14 條規則後 compliance 從 76% 跌至 52%
- CLAUDE.md bloat 是最大的 token overhead（占總浪費 14%）
- 精簡原則：每條規則回答「防止什麼具體失敗模式」，無法回答者刪除

### 2. 攻擊 Overhead，不是改進 Prompts（@Mnilax，8.8分）
9 個 token overhead 模式（90天/430小時/6M tokens 實測）：
- CLAUDE.md bloat：14% → 修復：4.8k→900 tokens，清理無觸發規則
- 對話歷史重讀：13% → 修復：每 60 messages compact 一次
- Hook injection：11% → 修復：mutex lock-file，停用重複插件
- Cache miss：10% → 修復：static-first 前綴排列
- Skill loading：7% → 修復：active skills ≤5-7 個，defer 未用的
- MCP tool schemas：6% → 修復：per-Skill tool scoping
- Extended thinking 濫用：5% → 修復：只在複雜推理時開啟
- Wrong-direction output：4% → 修復：Checkpoint 規則 + /rewind
- Plugin SessionStart：3% → 修復：停用不必要的 SessionStart hooks

### 3. 靜態前綴優先（@trq212，8.60分）
- CLAUDE.md 內容 = 最穩定的快取前綴（永遠放最前，不動）
- 動態資訊（日期、任務狀態）用 `<system-reminder>` messages 傳遞，不污染系統提示
- Mid-session 禁止：① 切換模型 ② 增刪 tool ③ 修改 CLAUDE.md（等 session 結束）
- Compaction 必須沿用完全相同的 system prompt + tools（forking 保留前綴）

### 4. 工具設計哲學：Progressive Disclosure（@trq212，8.6分）
- Claude Code ~20 個工具飽和閾值（超過模型選擇負擔加重）
- 按需載入取代工具增生：用 Skill 遞歸引用，而非無限加工具
- 工具應 fit 模型能力：AskUserQuestion 結構化輸出優於自由格式
- TodoWrite（引導模型思考）→ Task Tool（代理通訊）演化路徑

### 5. Harness 品質 > 模型版本（@akshay_pachaar + @nicbstme，8.05分）
- 同模型不同 harness = Terminal-Bench 排名 25+ 躍升
- Model-Harness-Fit：模型對特定 harness 有 byte-level 過擬合（wire format 是訓練一部分）
- Thin Harness 趨勢：Manus 5 次重建都在移除複雜度；LangChain 僅改 harness 排名 30→5

### 6. Hook 設計的 8 個黃金模式（@MinLiBuilds，7.90分）
```
PreToolUse 安全閘道：
- exit 2 → 阻斷 rm -rf / DROP TABLE / git push --force
- 偵測 .env* / *.pem / secrets/* 路徑 → 拒絕寫入

PostToolUse 品質保障：
- on Edit|Write → 自動執行 npm test（tail -5 防 context 爆）
- on Bash(git 相關) → 觸發 lint + format

Stop Hook 收尾：
- 觸發 git commit（附時間戳審計日誌）

PR 前強制門禁：
- PreToolUse on gh pr create → 先跑測試，失敗則 exit 2
```

### 7. Session 管理決策樹（@trq212，8.05分）
- Context rot 量化觸發點：300-400k tokens
- Bad compact 根因：忘記 save intermediate state 再 compact
- Rewind 優先於 compact（保留更多 context）
- Sub-agent mental test：「這個 task 需要隔離 context 嗎？」是 → sub-agent，否 → 繼續

### 8. 規則撰寫 5 條實戰準則（@vincemask，7.55分）
1. ≤200 行（分層：核心必讀 + on-demand）
2. 禁用清單（Do NOT introduce：speculative features、helper for one-off use）
3. 5 秒可驗證（每條規則可在 5 秒內判斷是否違反）
4. Router 指針模式（CLAUDE.md 指向 `.claude/rules/*.md`，主檔保持精簡）
5. Hook 強制執行層（可口頭描述的規則不需要 hook；會被忽視的才需要）

---

## Prompt 範本

### CLAUDE.md 規則撰寫模板

```markdown
# [規則名稱]（Rule N — [簡短描述，如 Surgical Changes / R3]）

> 對應失敗模式：[具體描述這條規則防止什麼問題]

## 核心指令
- **IMPORTANT**：[最重要的約束，用粗體標記]
- [其他約束條列]

## 判斷標準（5秒可驗證）
- 是：[符合規則的具體行為]
- 否：[違反規則的具體行為]

## 例外情況
- [明確可豁免的場景]
```

### CLAUDE.md 稽核 Prompt（每月執行）

```
分析以下 CLAUDE.md 內容，找出 token overhead：

[貼入當前 CLAUDE.md]

請回答：
1. 哪些規則超過 30 天未被觸發（根據行為推斷）？
2. 哪些規則相互矛盾？
3. 哪些規則可合併（≤3 句描述同一概念）？
4. 是否超過 200 行？若是，標出可移至 on-demand 的部分。

輸出：
- 刪除候選清單（附理由）
- 合併建議
- 最終精簡版本（保留核心，其餘 @ref 到 .claude/rules/）
```

### Hook 衝突診斷 Prompt

```
我的 Claude Code 有多個 hooks 和 plugins。診斷以下問題：

[描述症狀：例如「同一個檔案被 lint 7 次」「hooks 互相觸發形成迴圈」]

請分析：
1. 是哪種衝突類型？
   - PostToolUse cascade（格式化器互觸發）
   - Matcher overlap（多個 hook 匹配同一 pattern）
   - UserPromptSubmit 注入戰（多個插件都注入前置內容）
2. 需要哪種修復？
   - lock-file mutex（在 settings.json 設置）
   - 合併 formatter hooks
   - 停用重複注入的插件

輸出 settings.json 修改片段。
```

---

## 關鍵引用

> 「Attack overhead, not prompts. Productive tokens are the residual.」—— @Mnilax（2026-05-01）

> 「It's not a model problem, it's a configuration problem.」—— @addyosmani 引用（2026-05-09）

> 「Agent = Model + Harness. If you're not the model, you're the harness.」—— LangChain Vivek Trivedy via @nicbstme（2026-05-04）

> 「Cache hit rate 監控如同監控 uptime」—— @trq212（2026-02-19）
