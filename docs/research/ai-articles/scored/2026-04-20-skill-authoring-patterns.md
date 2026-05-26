---
url: "https://generativeprogrammer.com/p/skill-authoring-patterns-from-anthropics"
title: "Skill Authoring Patterns from Anthropic's Best Practices"
date: 2026-04-20
type: article
---

# Skill Authoring Patterns from Anthropic's Best Practices

**來源**：https://generativeprogrammer.com/p/skill-authoring-patterns-from-anthropics  
**作者**：Generative Programmer  
**日期**：2026-04-19  
**收錄日期**：2026-04-20  
**原始資料**：Anthropic 官方 [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)、[skill-creator SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)、[33-page Complete Guide](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)

---

## 文章概覽

14 個 Skill 設計模式，5 大類別，每個模式包含：問題描述、解法、適用時機、取捨。
這是對 Anthropic 官方 Skill 設計最佳實踐的系統化整理。

---

## 14 個模式速查

### 類別 A：Discovery & Selection（技能能否被選中）

| # | 模式 | 核心問題 | 解法 |
|---|------|---------|------|
| 1 | **Activation Metadata** | description 太模糊導致 Claude 選錯或不選 | description 要「主動觸發」：寫明什麼情境必用此 Skill，用第三人稱，略帶 pushy |
| 2 | **Exclusion Clause** | 邊界模糊導致 Skill 在不適合時觸發 | description 結尾加明確排除條件："Do NOT use for blog articles, newsletters, emails" |

> **重要數字**：description + when_to_use 總 token 上限 **1,536 字元**（Claude Code）；每句話都是競爭預算。

### 類別 B：Context Economy（節省 context window）

| # | 模式 | 核心問題 | 解法 |
|---|------|---------|------|
| 3 | **Context Budget** | Skill 重複解釋 Claude 已知的事 | 每段落都要「justify token cost」；移除廢話；統一術語（選一個詞，不用同義詞） |
| 4 | **Progressive Disclosure** | SKILL.md 800 行全部載入，但大多數呼叫不需要 | SKILL.md 控制在 **500 行以內**，只做 TOC；細節放 FORMS.md / REFERENCE.md 等子檔，按需讀取 |

> **500 行閾值**：超過就應該用 Progressive Disclosure 拆分。子檔要加 TOC（長檔案截斷時 Claude 只能看到前面）。

### 類別 C：Instruction Calibration（指令精確度）

| # | 模式 | 核心問題 | 解法 |
|---|------|---------|------|
| 5 | **Control Tuning** | 過度限制扼殺彈性；過度鬆散導致關鍵步驟出錯 | 依任務脆弱度調整自由度：低危 = 文字指令；中危 = pseudocode；高危（DB 遷移）= 精確腳本，不允許修改 |
| 6 | **Explain-the-Why** | ALWAYS/NEVER/MUST 規則沒有 context，邊界情況失效 | 規則後面附上原因：「用 constructor injection，因為 field injection 讓 Spring mock 困難」 |
| 7 | **Template Scaffold** | 每次呼叫輸出結構不一致 | SKILL.md 中放有 placeholder 的模板；嚴格（機器解析）或彈性（人閱讀）兩種等級 |
| 8 | **In-Skill Examples** | 結構對但風格不對（commit msg 格式正確但語氣不對） | 放 2-3 個 Input/Output 範例對；Templates 定骨架，Examples 校正風格 |
| 9 | **Known Gotchas** | 只有 happy path，遇到真實邊界情況 Claude 自行亂猜 | 加獨立 Gotchas section：「Scanned PDF 會靜默回傳 []，先 check page type」 |

> **Gotchas section** 被稱為「成熟 Skill 最有價值的內容」。

### 類別 D：Workflow Control（多步驟流程控制）

| # | 模式 | 核心問題 | 解法 |
|---|------|---------|------|
| 10 | **Execution Checklist** | 長流程 Claude 跳過驗證步驟或提前宣告完成 | 在 Skill 中提供可貼入對話的 checklist；未勾選的步驟對用戶可見 |
| 11 | **Self-Correcting Loop** | 單次 forward pass 輸出有錯，沒有驗證機制 | 明確指示：產出 → 跑 validator → 失敗就修 → 直到通過；必須設 retry 上限防無限迴圈 |
| 12 | **Plan-Validate-Execute** | 批量/破壞性操作直接執行，錯誤已落地才發現 | 先產出 JSON plan → 腳本驗證 plan → **通過才執行**；與 Self-Correcting Loop 的差異：Plan 在副作用前驗證 |

### 類別 E：Executable Code（腳本化）

| # | 模式 | 核心問題 | 解法 |
|---|------|---------|------|
| 13 | **Utility Bundle** | 每次呼叫重新生成同樣的腳本，浪費 token | 把重複邏輯寫成 `scripts/` 下的腳本；Claude 呼叫 bash 執行，只有輸出進 context |
| 14 | **Autonomy Calibration** | 預設工具集過寬（有 Write 的 security-audit Skill 是安全風險） | YAML frontmatter 宣告 `allowed-tools`：security-audit 只給 Read/Grep/Glob；deploy 只給 Bash（窄 matcher） |

---

## 對 cc-workspace 現有 Skills 的差距分析

### 立即可改善的問題（基於現有 `.claude/skills/`）

| 模式 | 現況 | 建議 |
|------|------|------|
| **Exclusion Clause** | 多數 Skill description 只有正向觸發，缺乏排除條件 | 在 `bugfix`、`web-fetch`、`deep-review` 等 description 加 "Do NOT use for..." |
| **Known Gotchas** | 幾乎所有 Skill 都沒有 Gotchas section | 從 `web-fetch` 開始補（已知：Next.js SPA、Cloudflare 防護等） |
| **Progressive Disclosure** | `gh-fetch` 已達 200+ 行，內聯太多細節 | 考慮把 curl 範例移到 `scripts/` 子目錄 |
| **Autonomy Calibration** | 所有 Skill 都未設定 `allowed-tools` | security-reviewer、deep-review 優先加 Read/Grep/Glob 限制 |
| **Explain-the-Why** | `bugfix` Skill 已有此模式（GEPA 背後的原因），其他 Skill 多為命令式 | 在 `web-fetch` fallback 步驟後加解釋（為何 WebFetch 對 Next.js 失效） |

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 9/10 | 直接對應 20+ 個 workspace Skills，每個模式都有具體改善機會 |
| B. 創新性 | 9/10 | Progressive Disclosure、Plan-Validate-Execute、Known Gotchas、Autonomy Calibration 都是 workspace 現有 Skills 未實作的模式 |
| C. 證據品質 | 8/10 | 基於 Anthropic 官方文件，非實驗數據，但有具體來源可追溯 |
| D. 技術深度 | 8/10 | 每個模式有問題 + 解法 + 適用時機 + 取捨；500 行/1536 字元等具體數字 |
| E. 泛化性 | 9/10 | 適用於所有 `.claude/skills/` 下的 Skill，不分功能類別 |
| **加權總分** | **8.65/10** | |

**整合決策**：Rule（新增 `.claude/rules/skill-authoring.md`）  
**理由**：這是「設計/更新 Skill 時」的參考規則，不是單一任務的執行 Skill。最適合做成按需載入的 Rule，在任何建立或修改 Skill 的場景自動提供指引。  
**整合位置**：`.claude/rules/skill-authoring.md`  
**整合狀態**：✅ 已完成  

**後續建議（可選）**：
- 委派 `implementer` 對 `deep-review`、`web-fetch`、`bugfix` 三個 Skill 加入 Exclusion Clause + Known Gotchas
- 對 `deep-review` 加入 `allowed-tools: Read, Grep, Glob` 的 Autonomy Calibration
