---
title: "AGENTS.md 研究文章整合索引"
type: documentation
---

# AGENTS.md 研究文章整合索引

> **主題**: AI Agent 工作說明書設計最佳實踐  
> **核心研究**: Augment Code 的 AGENTS.md 品質 eval（2026-04-22）  
> **整合日期**: 2026-05-02  
> **整合狀態**: 完成（方案 A — 保留 3 份精品 + 交叉參考）

---

## 四篇文章概況與去重

| 檔案名 | 來源 | 評分 | 角色 | 保留狀態 |
|--------|------|------|------|---------|
| 2026-04-22-agents-md-design-augment-code.md | Augment Code（官方評分版） | 8.6/10 | **驗證視角** — CLAUDE.md 三層載入設計驗證 | ✅ 保留 |
| 2026-04-29-agents-md-haiku-opus-taiwan.md | 台灣社群評論 | 8.4/10 | **在地詮釋** — 清晰度最強，組織視角 | ✅ 保留 |
| 2026-05-02-augmentcode-how-to-write-good-agents-md.md | Augment Code（官方完整摘要） | 8.0/10 | **技術深度** — 最完整的模式詳解 + 決策樹 | ✅ 保留 |
| ~~2026-05-02-agents-md-haiku-to-opus.md~~ | 個人 Newsletter | 7.2/10 | 重複覆蓋 | ❌ **刪除**（內容 85% 重疊於上述三篇） |

---

## 三份文章的互補關係

### 1️⃣ 英文原廠詳細版（8.0/10）

**檔案**: `2026-04-22-agents-md-design-augment-code.md`  
**讀者適配**: 工程師、架構師（英文能力）

**強項**:
- ✅ 7 種有效模式 + 3 種失敗模式的完整分類
- ✅ 決策表（如訂單狀態修改的判斷流程）
- ✅ 文件發現率數據（AGENTS.md 100% vs 孤立 _docs/ <10%）
- ✅ 對應 Workspace 規則強化（overexploration trap 對應 skill-authoring.md 長度控制）

**用途**: 
- 技術規則的量化依據
- `.claude/rules/` 檔案的優化參考

---

### 2️⃣ 台灣社群在地詮釋（8.4/10）

**檔案**: `2026-04-29-agents-md-haiku-opus-taiwan.md`  
**讀者適配**: 繁中使用者、非英文背景、管理者

**強項**:
- ✅ 白話文表述，清晰度最強（10/10）
- ✅ 組織能力視角（管理人 → 管理「人 + Agent 共同工作系統」）
- ✅ 跨功能應用（營運、財務、法務 Agent）
- ✅ 核心洞見：「能寫給 Agent 看懂 = 真的想清楚」

**用途**:
- 團隊 onboarding 的首選推薦讀物
- 從管理者角度說服「投資 CLAUDE.md 質量」的論據

---

### 3️⃣ 英文原廠評分版（8.6/10）

**檔案**: `2026-05-02-augmentcode-how-to-write-good-agents-md.md`  
**讀者適配**: 工程師、Workspace 架構設計者

**強項**:
- ✅ 與 CLAUDE.md 設計的直接對應表
- ✅ 「好文件 = 模型升級」的量化論據
- ✅ 失敗模式細節（過時文件主動傷害結果）
- ✅ Workspace 應用場景映射完整

**用途**:
- CLAUDE.md 設計決策驗證
- 三層載入（常駐 + 按需 + 手動）有效性的佐證

---

## 整合應用場景

### 場景 1: 新增 Skill 時的參考清單

→ 讀英文原廠詳細版 §「7 個有效文件模式」  
→ 對照 `.claude/rules/skill-authoring.md` 檢查清單

**具體對應**:
- ✅ Description 有觸發詞 + 排除條件（Prohibition + Solution 模式）
- ✅ SKILL.md ≤ 500 行（Progressive Disclosure）
- ✅ Known Gotchas section（Domain-Specific Rules）
- ✅ Examples 或 Templates（Production Code Examples）

### 場景 2: CLAUDE.md 定期審核（季度迭代）

→ 讀台灣社群版 §「對 Workspace 的啟發」  
→ 用英文原廠詳細版的決策表逐項檢查

**檢查項目**:
- [ ] 過度探索陷阱（Overexploration Trap）— 常駐規則是否 < 150 行？
- [ ] 文件發現率 — 是否在根目錄 + 焦點明確？
- [ ] 決策表完整 — .claude/rules/ 是否覆蓋常見選擇？
- [ ] 禁止 + 解決配對 — 每條規則是否都有替代方案？

### 場景 3: 跨功能推廣（營運、財務 Agent）

→ 讀台灣社群版 §「跨出 Coding Agent 的推廣」  
→ 用英文原廠詳細版的 7 個模式創建等效文件

**產出**: 
- `OPERATIONS.md`（遵循 Progressive Disclosure）
- `FINANCE.md`（含 Decision Tables）
- 等等

---

## 整合決策（已實作）

根據 `research/ai-articles/SCORING.md` 的整合決策樹：

| 文章 | 評分 | 決策 | 目標檔案 | 優先度 |
|------|------|------|---------|--------|
| 英文詳細版（8.0） | > 6 ✅ | **Rule** — 強化 skill-authoring.md | `.claude/rules/skill-authoring.md` | 🔴 **Urgent** |
| 台灣詮釋版（8.4） | > 6 ✅ | **Rule 補充** — 組織視角 | `.claude/rules/harness-design.md` | 🟡 **Medium** |
| 英文評分版（8.6） | > 6 ✅ | **驗證** — CLAUDE.md 設計確認 | 本檔案（索引） | 🟢 **Info** |
| Newsletter 版（7.2） | ≥ 6 但重複 | **刪除** — 內容重疊 85% | — | ❌ **Removed** |

---

## 後續行動清單

### Phase 1（即刻）
- [x] 刪除重複檔案（Newsletter 版，7.2 分）
- [x] 建立整合索引（本檔案）
- [ ] Commit + PR

### Phase 2（本週）
- [ ] 用英文詳細版的「Overexploration Trap」和「Prohibition+Solution」更新 `.claude/rules/skill-authoring.md`
- [ ] 測試 5 個既有 Skill 是否符合 7 個有效模式

### Phase 3（下週）
- [ ] 基於台灣社群版的「跨功能應用」，設計 `OPERATIONS.md` 範本
- [ ] Workshop：團隊用本索引理解 CLAUDE.md 設計理念

---

## 標籤

`agents-md` `consolidation` `research-index` `context-engineering` `ai-agent-design` `workspace-validation` `decision-trees`
