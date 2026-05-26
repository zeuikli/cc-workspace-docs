# Project 01：從零建立你的第一個 Workspace

## 專案說明

本專案帶你建立一個完整的 Claude Code Workspace——不是空白的 CLAUDE.md，而是一個能夠跨 session 記憶、自動初始化環境、有明確驗收定義的完整工作環境。

**完成後的成果**：
- 結構化的 `CLAUDE.md`（含 Ratchet 原則基礎）
- 跨 session 狀態追蹤（`claude-progress.md` + `feature_list.json`）
- SessionStart Hook（自動環境初始化）
- Stop Hook（session 結束提醒更新進度）
- 驗證你的設定是否有效（對照實驗）

## 前置條件

完成本專案前，請先完成：

- [Lecture 01：Claude Code 與 Harness 基礎](/lectures/lecture-01-foundations/)
- [Lecture 02：CLAUDE.md 設計](/lectures/lecture-02-claude-md/)
- [Lecture 05：記憶系統與工作區設計](/lectures/lecture-05-memory-workspace/)

## 任務清單

### 階段一：初始化 CLAUDE.md

- [ ] **任務 1.1**：在你的專案根目錄執行 `/init`，生成初始 CLAUDE.md
- [ ] **任務 1.2**：審查並精簡生成的 CLAUDE.md，確保在 200 行以內
- [ ] **任務 1.3**：加入「驗證命令」區塊（至少包含測試命令和 lint 命令）
- [ ] **任務 1.4**：加入「完成定義（Definition of Done）」區塊
- [ ] **任務 1.5**：加入「禁止事項」區塊（初始為空，後續從失敗中積累）

### 階段二：設定跨 Session 狀態追蹤

- [ ] **任務 2.1**：建立 `claude-progress.md`，使用本課程提供的模板
- [ ] **任務 2.2**：建立 `feature_list.json`，定義當前 sprint 的功能點
- [ ] **任務 2.3**：在 CLAUDE.md 中加入「每次 session 開始前讀取 claude-progress.md」的指令
- [ ] **任務 2.4**：在 CLAUDE.md 中加入「每次 session 結束前更新 claude-progress.md」的指令

### 階段三：設定 Hooks

- [ ] **任務 3.1**：建立 `.claude/settings.json`
- [ ] **任務 3.2**：建立 `.claude/hooks/session-init.sh`（SessionStart hook）
  - 內容：檢查 `node_modules` 或虛擬環境是否存在，必要時初始化
  - 內容：檢查 `.env` 是否存在，必要時從 `.env.example` 複製
- [ ] **任務 3.3**：建立 `.claude/hooks/session-end.sh`（Stop hook）
  - 內容：輸出「提醒：請確認 claude-progress.md 已更新」
- [ ] **任務 3.4**：在 `.claude/settings.json` 中設定兩個 hooks

### 階段四：對照實驗（驗證有效性）

- [ ] **任務 4.1**：選一個你常用的任務（例如：加一個新 API endpoint）
- [ ] **任務 4.2**：**第一次**：在沒有 CLAUDE.md 的空目錄執行這個任務，記錄：
  - Agent 犯了哪些錯誤（用了錯誤的框架版本？忘記加驗證？）
  - 需要幾輪對話才完成？
  - Agent 有沒有宣布完成但實際沒有？
- [ ] **任務 4.3**：**第二次**：在你建立的 workspace 中執行同樣的任務，記錄同樣的指標
- [ ] **任務 4.4**：對比兩次結果，把第一次出現的問題加入 CLAUDE.md 的「禁止事項」（Ratchet 原則）

### 階段五：優化與迭代

- [ ] **任務 5.1**：把你的 CLAUDE.md 給團隊成員（或朋友）看，詢問是否清晰易懂
- [ ] **任務 5.2**：如果 CLAUDE.md 超過 200 行，拆分出 path-scoped rules
- [ ] **任務 5.3**：建立 `CLAUDE.local.md`（個人偏好，加入 `.gitignore`）

## 參考實作

### 目錄結構

```
myproject/
├── CLAUDE.md                        ← 主要專案指令（Project level）
├── CLAUDE.local.md                  ← 個人偏好（加入 .gitignore）
├── claude-progress.md               ← 任務進度追蹤
├── feature_list.json                ← 功能驗收清單
├── .claude/
│   ├── settings.json                ← Hooks 設定
│   ├── hooks/
│   │   ├── session-init.sh          ← SessionStart hook
│   │   └── session-end.sh           ← Stop hook
│   └── rules/
│       ├── frontend.md              ← 前端 path-scoped rules（可選）
│       └── api.md                   ← API path-scoped rules（可選）
└── .gitignore                       ← 包含 CLAUDE.local.md
```

### CLAUDE.md 模板

```markdown
# [專案名稱]

> CLAUDE.md 版本：1.0
> 最後更新：[日期]（更新原因：[說明]）

## 技術棧
- [列出所有技術和版本，越具體越好]
- 範例：Python 3.12, FastAPI 0.115, SQLAlchemy 2.0（注意：使用新版 async API）

## 驗證命令（每次變更後必須執行）
```bash
[測試命令]
[類型檢查命令]
[lint 命令]
```

## 架構約定
- [列出重要的架構決策]
- 範例：API handlers 放在 src/api/handlers/

## 完成定義（Definition of Done）
一項任務完成 = [具體的可驗證條件]

## 禁止事項（每條追蹤到具體失敗）
（初始為空，從失敗中積累）

## 跨 Session 規則
- 每次 session 開始時讀取 claude-progress.md 了解上次進度
- 每次 session 結束時更新 claude-progress.md 記錄進度和下一步
```

### claude-progress.md 模板

```markdown
# Claude Progress Log

## 當前 Sprint
**目標**：[描述當前正在做什麼]

## 完成狀態
- [ ] [功能 1]
- [ ] [功能 2]

## 遇到的問題
[記錄遇到的技術問題和解決方案]

## 下一步（下次 session 從這裡開始）
1. [具體的下一個步驟]

## 最後更新
[日期] by Claude (session [id])
```

### feature_list.json 模板

```json
{
  "sprint": "Sprint 1",
  "created": "2026-05-26",
  "features": [
    {
      "id": "feature-01",
      "description": "[功能描述]",
      "status": "pending",
      "completion_evidence": "[驗收命令或可觀察的證據]"
    }
  ]
}
```

### .claude/settings.json 模板

```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/session-init.sh"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/session-end.sh"
          }
        ]
      }
    ]
  }
}
```

### .claude/hooks/session-init.sh 模板

```bash
#!/bin/bash
set -euo pipefail

echo "=== Session Init ==="

# Python 專案
if [ -f "pyproject.toml" ] || [ -f "requirements.txt" ]; then
  if [ ! -d ".venv" ] && [ ! -d "venv" ]; then
    echo "Warning: Virtual environment not found"
    echo "Run: python -m venv .venv && source .venv/bin/activate && pip install -e ."
  fi
fi

# Node.js 專案
if [ -f "package.json" ]; then
  if [ ! -d "node_modules" ]; then
    echo "Installing dependencies..."
    npm install
  fi
fi

# .env 檔案
if [ -f ".env.example" ] && [ ! -f ".env" ]; then
  echo "Warning: .env not found, copying from .env.example"
  cp .env.example .env
  echo "IMPORTANT: Update .env with your actual values"
fi

echo "=== Session Init Complete ==="
exit 0
```

### .claude/hooks/session-end.sh 模板

```bash
#!/bin/bash
set -euo pipefail

echo ""
echo "=== Session End Reminder ==="
echo "Please ensure claude-progress.md is updated with:"
echo "  1. What was completed in this session"
echo "  2. Any issues encountered and their solutions"
echo "  3. Next steps for the next session"
echo "==========================="
exit 0
```

## 驗收標準

完成本專案後，你應該能夠：

- **驗收 1**：新開一個 session，Claude 會自動讀取 CLAUDE.md 並知道專案的技術棧和規則，**不需要**你重新說明
- **驗收 2**：執行 SessionStart hook 後，環境自動初始化（沒有「找不到 node_modules」等環境錯誤）
- **驗收 3**：完成一個任務後，claude-progress.md 有更新的進度記錄
- **驗收 4**：對照實驗中，有 CLAUDE.md 的版本比沒有的版本少犯至少一個曾經犯過的錯誤
- **驗收 5**：CLAUDE.md 在 200 行以內，且每條規則清晰可理解
