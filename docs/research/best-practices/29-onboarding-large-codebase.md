---
title: "Claude Code Onboarding 與大型 Codebase 最佳實踐"
source: Anthropic 官方
type: best-practices
---

# Claude Code Onboarding 與大型 Codebase 最佳實踐

> 來源 1：https://claude.com/blog/onboarding-claude-code-like-a-new-developer-lessons-from-17-years-of-development  
>   作者：Brendan MacLean（Claude Developer Ambassador，MacCoss Lab / Univ. of Washington）  
> 來源 2：https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start  
>   發布：2026-05-14，Anthropic 官方  
> 收錄日期：2026-05-16  
> 重要性：★★★（大型 codebase 導入 Claude Code 的基礎架構藍圖）

---

## 核心主張

「不要把 70 萬行程式碼丟給新人，然後期待立刻有成果。Claude 也一樣。」

成功導入 Claude Code 的組織，共同特徵是將 **context 視為需要維護的工件**——版本化、分層、持續更新。

---

## 一、Skyline 案例：17 年開發積累 vs. Claude 學習曲線

**背景**：MacCoss Lab 維護 Skyline（蛋白質分析軟體），70 萬行 C#，2008 年起開發，20 萬+ 自動化夜間測試，歷經數十位開發者 Onboarding。

**核心策略**：將人員 Onboarding 方法論直接套用到 Claude：
- 不期望 Claude 立刻理解整個 codebase
- 先從小型獨立模組開始建立理解
- 逐步擴大範圍，同時保持專屬 context

**成果**：
- 原本一年的 Files View 面板專案 → **兩週完成**
- 2,000+ 教程截圖自動更新
- 每日基礎設施摘要自動生成
- 原本抗拒的團隊成員也開始成功交付功能

---

## 二、三層 Context 架構

### 層 1：Context Repository（獨立 Git Repo）

```
pwiz-ai/                        # 獨立 context repository
├── CLAUDE.md                   # 根目錄：方向 + 文件索引
├── skills/
│   ├── skyline-development.md  # 領域知識 Skill
│   ├── version-control.md      # 版本控制流程
│   └── debugging.md            # 除錯流程
└── docs/
    └── architecture.md         # 架構概覽
```

**關鍵設計**：
- 適用所有 branch 和開發時間點
- 「參考不嵌入」原則：Skills 指向文件，而非複製內容
- 明確的觸發條件（什麼時候呼叫這個 Skill）

### 層 2：Skills Library（可重用領域知識）

- 將機構知識編碼為可跨 session 使用的 Skill
- 每個 Skill 有明確的觸發條件
- Critical skills 有顯式觸發條件（防止遺漏）

### 層 3：MCP 整合（實時資料接取）

MacCoss Lab 用 C# 和 Python 撰寫 MCP Server（由 Claude 自己撰寫），連接：
- 自動化測試結果
- 異常報告
- 技術支援帖（Historical Issues）

**原則**：「真實資訊勝過抽象知識」——MCP 讓 Claude 查到真實的測試失敗，而非猜測。

---

## 三、大型 Codebase 導入：官方建議

來源：Anthropic 官方（2026-05-14）

### Claude Code 的導覽方式

Claude Code 使用 **Agentic Search**（非 RAG/embedding）：
- 直接在本地 codebase traverse，使用類 grep 導覽
- 優勢：永遠是最新代碼（無過時 embedding index）
- 要求：codebase 組織良好，否則導覽效率低

**實際意涵**：好的 codebase 結構本身就是提升 Claude Code 效果的槓桿。

### 五元件 Harness 生態系統

成功的大型 codebase 導入依賴五元件組合：

| 元件 | 功能 | 設計原則 |
|------|------|---------|
| CLAUDE.md | 每 session 自動載入的 context | 精簡、分層（按目錄）、排除生成檔案 |
| Hooks | 事件觸發的自動化腳本 | 用於持續改進和自動化 |
| Skills | 按需載入的專業知識 | 特定任務類型的打包專業知識 |
| Plugins | 跨組織分發的設定包 | 統一組織內 Claude Code 設定 |
| MCP Servers | 連接內部工具和 API | 讓 Claude 存取真實的內部資料 |

**加分項**：LSP（Language Server Protocol）整合，提供符號級搜尋導覽。

### CLAUDE.md 三大設定原則

```
1. 保持精簡（lean）：大型 codebase 不等於長 CLAUDE.md
2. 子目錄初始化：每個子系統有自己的 CLAUDE.md，範疇化指令
3. 排除生成檔案：告訴 Claude 哪些目錄是自動生成的，避免誤讀
```

### 三個設定模式

**模式 A：讓 Codebase 可導覽**
- CLAUDE.md 保持精簡，按目錄初始化
- 子目錄 Commands 按範疇設定
- 排除生成檔案、執行 LSP server 做符號搜尋

**模式 B：主動維護設定**
- 每 3-6 個月審閱設定（模型進化，舊指令可能反而限制新模型）
- 隨模型能力提升逐步移除過時約束
- 建立設定版本追蹤

**模式 C：組織所有權**
- 指定 DRI（Directly Responsible Individual）管理 Claude Code 設定
- 建立跨職能工作組（工程 + 安全 + 治理）
- 防止設定碎片化，確保跨組織一致性

---

## 四、對 workspace 設計的啟示

### 現有 cc-workspace 的對應

| 本文建議 | workspace 現狀 |
|---------|---------------|
| 獨立 context repository | `.claude/` 目錄（Skill、rules、refs 分層） |
| CLAUDE.md 精簡分層 | CLAUDE.md ≤ 200 行 + @rules 載入 |
| Skills Library | `.claude/skills/` |
| MCP 整合 | settings.json MCP 設定 |
| 每 3-6 個月審閱 | 尚未設定定期審閱機制 ← 建議加入 |
| DRI 所有權 | 個人 workspace，單一 owner |

### 建議新增

1. **定期 Context 健康審閱**：每季執行 `research-hub:audit`，評估設定是否仍符合當前模型能力
2. **Skills 觸發條件文件化**：每個 Skill 加入明確的觸發/排除條件（現有 skills 大多已有，需持續維護）
3. **MCP 真實資料接入**：優先接入會頻繁查詢的內部資料（如 git log、test results）

---

## 快速 Checklist

### 初次設定
- [ ] 建立 context repository 或獨立 context 目錄
- [ ] 根目錄 CLAUDE.md：方向 + 文件索引（≤ 200 行）
- [ ] 子目錄各有各的 CLAUDE.md（範疇化指令）
- [ ] 排除生成檔案目錄（build/、dist/、*.generated.*)
- [ ] 核心領域知識編碼為 Skills

### 持續維護
- [ ] 每 3-6 個月審閱 CLAUDE.md 和 Skills（模型進化後重新評估）
- [ ] 新知識加入 Skills（不只是即時對話）
- [ ] MCP 接入高頻查詢的內部資料
- [ ] Cache hit rate 監控（ref: 28-thariq-prompt-caching-lessons.md）

> 一手來源（O 層）：Anthropic 官方 blog + Claude Developer Ambassador 案例
