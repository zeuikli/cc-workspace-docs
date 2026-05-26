# Overnight Research Template
# research-hub + autoresearch + /goal 通用全自動研究模板
# 版本：1.0 | 2026-05-15

---

## 使用方式

### 步驟 1：修改設定（填入 [TOPIC] 等變數後存檔）

```
TOPIC=        # 研究主題，例："Claude Code hooks 最佳實踐"
SCOPE=        # 搜尋範圍關鍵字，例："Claude Code hooks site:github.com OR site:anthropic.com"
REPORT_PATH=  # 輸出報告路徑，例：research/reports/2026-05-15-topic.md
MIN_CHARS=    # 報告最低字元數（中文用 wc -m），例：5000
ITERATIONS=   # autoresearch 迭代上限（整夜建議 20，快速測試用 5）
```

### 步驟 2：確認 bypassPermissions 已設定

> `.claude/settings.json` 已設定 `"defaultMode": "bypassPermissions"`，無需額外 flag。
> 若尚未設定，執行 `claude --dangerously-skip-permissions` 或手動加入設定。

### 步驟 3：貼入 /goal 條件（先貼，後貼工作 Prompt）

```
/goal 下列三個條件同時成立（評估依據是 transcript 中 Claude 執行命令的實際輸出）：
1. wc -m [REPORT_PATH] 的輸出數字 ≥ [MIN_CHARS]
2. git log --oneline -1 包含 "research:" 字樣
3. bash scripts/healthcheck.sh 的輸出包含 "PASS"
若以上輸出尚未在對話中出現，Claude 需執行驗證命令並展示結果，再由評估器判斷。
若超過 30 輪仍未達成，停止並輸出截至目前的完成狀態報告。
```

### 步驟 4：貼入工作 Prompt（見下方完整版）

---

## 完整工作 Prompt（複製全部貼入）

```
你是一個自主研究 Agent。執行以下研究任務，不需要任何人工確認，直接推進到完成。

---
## 研究設定

- **主題**：[TOPIC]
- **搜尋範圍**：[SCOPE]
- **報告輸出路徑**：[REPORT_PATH]
- **報告最低字元數**：[MIN_CHARS]（使用 wc -m 計算，支援中文）
- **autoresearch 迭代上限**：Iterations: [ITERATIONS]
- **Plateau-Patience**：off（永不因停滯而停止）

---
## Phase 1：網路搜尋與資料收集

執行以下工作（使用 WebSearch + WebFetch + research-hub skill）：

1. 用 WebSearch 搜尋主題相關的一手資料來源
   - 搜尋詞 A：[SCOPE]
   - 搜尋詞 B：[TOPIC] best practices 2024 OR 2025
   - 搜尋詞 C：[TOPIC] site:github.com OR site:arxiv.org

2. 選出最高品質的 10–15 個 URL（優先：官方文件、GitHub、學術論文、知名技術部落格）

3. 對每個 URL 執行 research-hub article-archive：
   - 主要方式：WebFetch
   - 備用方式：curl -sL [URL] | python3 -c "import sys; print(sys.stdin.read()[:5000])"
   - 提取：標題、作者、日期、核心論點、關鍵代碼/數據、可操作建議

4. 建立中間暫存摘要（不寫檔案，保留在 context）：
   每篇文章格式：
   ```
   ## [標題] — [URL]
   **評分**：A(影響力)/B(原創性)/C(可操作性)/D(可信度)/E(時效性) = 加權分
   **核心論點**：2-3 句
   **可操作建議**：條列
   **關鍵引用**：原文片段（≤100字）
   ```

---
## Phase 2：本地知識庫整合（若有）

若 research/tweets/ 目錄存在且含相關文章：
- 派遣最多 4 個平行 Sub Agent，每個負責一個子分類
- 每個 Sub Agent 回傳 ≤600 字結構化摘要
- 與 Phase 1 的網路資料交叉比對，找出共識與分歧

---
## Phase 3：synthesize — 生成初版報告

撰寫完整研究報告，儲存至 [REPORT_PATH]。

報告結構：
```markdown
# [TOPIC] — 深度研究報告
**日期**：[DATE] | **字元數目標**：≥ [MIN_CHARS]

## 執行摘要（≤300字）
## 1. 背景與動機
## 2. 核心概念分析
## 3. 最佳實踐與實作模式
## 4. 工具與生態系統比較
## 5. 常見陷阱與反模式
## 6. 前沿趨勢與預測
## 7. 可立即實作的行動建議
## 附錄：來源評分與索引
```

每節目標字元數：執行摘要 300、背景 500、核心分析 1000、最佳實踐 1000、工具比較 800、陷阱 600、趨勢 500、行動建議 500、附錄 300。

---
## Phase 4：autoresearch 迭代改進

啟動 autoresearch 迭代（Iterations: [ITERATIONS]，Plateau-Patience: off）：

**Metric（主指標）**：`wc -m [REPORT_PATH]`（字元數，higher is better）
**Guard（守衛）**：`bash scripts/healthcheck.sh`（必須 PASS）
**Verify command**：`wc -m [REPORT_PATH] && bash scripts/healthcheck.sh | tail -3`

迭代策略（按優先序輪換）：
1. 擴展字元數最少的章節（補充來源、範例、數據）
2. 追加 WebSearch 搜尋新角度（競品、反例、學術論文）
3. 加入具體代碼示例或案例研究
4. 強化「可行動建議」的具體度（加入工具名稱、指令、參數）
5. 補充「附錄：來源評分」的完整性

每次迭代：
- 執行 ONE focused change
- git commit -m "experiment: [描述改動]"
- 執行 verify command 並展示輸出
- 若 wc -m 增加 → Keep；相同或減少 → git revert

---
## Phase 5：最終驗證（必須執行並展示輸出）

```bash
wc -m [REPORT_PATH]
bash scripts/healthcheck.sh
git log --oneline -3
ls -la [REPORT_PATH]
head -30 [REPORT_PATH]
```

將以上所有命令的輸出完整顯示在 transcript 中（供 /goal 評估器讀取）。

---
## Phase 6：提交

```bash
git add [REPORT_PATH]
git commit -m "research: [TOPIC] — 完整研究報告 $(wc -m [REPORT_PATH] | awk '{print $1}') 字元"
git push -u origin HEAD
```

---
## 執行規則

- 不詢問任何授權、不等待確認、直接推進
- 所有驗證指令必須執行並展示實際輸出（不得口頭聲稱「已完成」）
- 遇到單一來源抓取失敗 → 跳過並記錄，繼續下一個
- 遇到 healthcheck FAIL → **立即停止**，修復後才能繼續（blocking，不得跳過）；修復失敗 ≥ 3 次 → 停止並回報用戶
- 每完成一個 Phase → 輸出 checkpoint：「Phase N 完成：[做了什麼 / 驗了什麼 / 剩什麼]」
```

---

## 快速填表（複製後替換）

| 變數 | 說明 | 範例 |
|------|------|------|
| `[TOPIC]` | 研究主題 | Claude Code hooks 最佳實踐 |
| `[SCOPE]` | 搜尋關鍵字 | "Claude Code hooks" site:github.com |
| `[REPORT_PATH]` | 報告儲存路徑 | research/reports/2026-05-15-claude-hooks.md |
| `[MIN_CHARS]` | 最低字元數 | 5000 |
| `[ITERATIONS]` | autoresearch 上限 | 20（整夜）/ 5（快速測試） |
| `[DATE]` | 今天日期 | 2026-05-15 |

---

## /goal 評估條件（替換後貼入）

```
/goal 下列三個條件同時成立（評估依據是 transcript 中 Claude 執行命令的實際輸出）：
1. wc -m [REPORT_PATH] 的輸出數字 ≥ [MIN_CHARS]
2. git log --oneline -1 包含 "research:" 字樣
3. bash scripts/healthcheck.sh 的輸出包含 "PASS"
若以上輸出尚未在對話中出現，Claude 需執行 Phase 5 驗證命令並展示結果，再由評估器判斷。
若超過 30 輪仍未達成，停止並輸出截至目前的完成狀態報告。
```

---

## 設計原理

| 設計決策 | 原因 |
|----------|------|
| `wc -m` 非 `wc -w` | `wc -w` 對中文回傳近零（whitespace 分詞），`wc -m` 計算 Unicode 字元 |
| `/goal` 條件用命令輸出 | Haiku 評估器只讀 transcript，命令輸出必須顯示在對話中 |
| Plateau-Patience: off | 整夜執行，不因 15 輪無改善而停止 |
| guard = healthcheck.sh | 防止 autoresearch 優化虛假指標（Echo Chamber 陷阱） |
| 每迭代一個 change | 原子性；失敗時精確定位原因 |
| Sub-agent fan-out ≤ 4 | CLAUDE.md 規定，超過 4 個並發子代理上限 |
| Phase 5 必須展示輸出 | `/goal` 評估器依賴 transcript 中的實際輸出，不能只說「已完成」 |
| `--dangerously-skip-permissions` | 整夜無人值守必須，避免授權提示阻斷執行流 |
