---
title: Cat Wu 面試了幾百個 PM 候選人，幾乎沒人答對一個問題：AI 產品經理到底應該干什麼？
date: 2026-04-24
type: article
---

# Cat Wu 面試了幾百個 PM 候選人，幾乎沒人答對一個問題：AI 產品經理到底應該干什麼？

**來源（X Article）**：https://x.com/dotey/status/2047537778959778209  
**作者**：宝玉 (@dotey)，提示工程師  
**發佈日期**：2026-04-24  
**收錄日期**：2026-04-27  
**原始 Podcast**：[How Anthropic's product team moves faster than anyone else | Cat Wu](https://www.lennysnewsletter.com/p/how-anthropics-product-team-moves)（Lenny's Newsletter，2026-04-23）  
**延伸閱讀**：[Product management on the AI exponential](https://claude.com/blog/product-management-on-the-ai-exponential)（Cat Wu，claude.com，2026-03-19）

---

## 文章背景

Cat Wu 是 Anthropic Claude Code 和 Cowork 的產品負責人，與工程負責人 Boris Cherny 搭檔，帶領團隊把產品功能交付週期從半年壓縮到一天。本文整理自 Lenny's Podcast 最新一期訪談，涵蓋 Anthropic 內部速度文化、PM 角色的劇變、源代碼洩漏善後，以及 OpenClaw 封堵決策等話題。

---

## 核心觀點（20 個段落摘要）

### 1. 與 Boris Cherny 的搭檔模式

與工程負責人 Boris Cherny 維持「80% 心智同步、20% 各自專注」的工作方式——大多數決策兩人方向一致，不需要反覆對齊。

### 2. PM 面試最常見的錯誤

面試幾百個 PM 候選人，幾乎沒人答對的問題：**AI 產品經理到底應該干什麼？**  
大多數候選人仍停留在「6-12 個月 roadmap」的舊思維，未能理解 AI 時代節奏根本不同。

> 最優秀的 AI PM，是那些能夠想清楚：「從有這個想法，到把產品交到用戶手中，我怎麼縮短這段時間？」的人。

### 3. 快速交付的三個機制

- **目標清晰**：方向明確讓團隊不需反覆對齊
- **Research Preview 機制**：降低發布門檻——以「研究預覽」名義早期發布，獲取真實反饋
- **長青啟動室（Evergreen Launch Room）**：跨職能協調室，常設化而非一次性 sprint

### 4. PRD 已死，週期複盤取而代之

傳統 PRD 被替換為：
- **每週 metrics readout**（關注真實數據而非計劃書）
- **團隊原則文件（Team Principles Doc）**：讓每個人在沒有 PM 盯著的情況下仍能做出對齊的決策

### 5. 速度文化早於 Mythos 模型

交付速度的提升**早於**強力 AI 模型的出現——根本驅動力是文化與流程，而非工具。

### 6. 源代碼洩漏的處置

源代碼洩漏被定性為**流程失敗**而非個人失誤——相關人員被留任，防範措施強化。強調「不怪人，修系統」的文化。

### 7. 封堵 OpenClaw 訂閱的原因

以「容量管理」為由封堵第三方工具 OpenClaw——原因是第三方工具對系統造成不成比例的負擔，屬於資源保護措施而非競爭封鎖。

### 8. PM 團隊結構

30-40 名 PM，分佈於五個部門：
- 研究（Research）
- 開發者平台（Developer Platform）
- Claude Code
- 企業（Enterprise）
- 成長（Growth）

大多數 PM 來自工程師或工程師轉型背景。

> Product taste 是極稀缺的技能，我們幾乎會錄取任何能展現這個能力的人。

### 9. 角色邊界的消融

- 工程師在寫程式的同時也在做產品決策
- 設計師在寫程式
- PM、工程、設計的邊界正在消融

### 10. AGI 校準感——最難培養的 PM 技能

最難的技能：在**當前模型能力限制**內判斷產品方向——既不過度悲觀（認為模型做不到），也不過度樂觀（忽略當前限制）。

這被稱為「剛好適量的 AGI 信念」（right amount of AGI belief）。

### 11. 人類仍然不可被替代的領域

- 常識判斷
- 人際關係理解

這兩個領域仍然是人類的護城河。

### 12. 高壓環境的日常管理

面對 P0000 級別問題的連環爆發，靠以下三點維持：
- 睡眠（不省略）
- 優先排序（不什麼都做）
- 接受不完美（接受有些事做不好）

### 13. 速度的代價

高速交付的副作用：
- 功能同時上線導致**重疊與用戶混淆**
- **一致性被犧牲**換取速度

### 14. 統一使命降低組織摩擦

Anthropic 的統一使命讓各團隊能夠放棄個人 KR，優先服務公司整體目標，消除大多數組織政治的根源。

### 15. 產品組合使用模式

| 產品 | 主要用途 |
|------|---------|
| CLI | 開發者，深度整合 |
| Desktop | 主力日常開發 |
| Web/Mobile | 輕量存取 |
| Cowork | 知識工作（Todo、Slides） |

### 16. 客製化應用程式

Anthropic 內部大量使用客製化 AI 工具——「每個人都有自己的個人化 Claude」。

### 17. Token 經濟學

Token 成本持續上升，但仍低於工程師薪資成本——ROI 仍然正向。

### 18. Claude 的個性差異化

Claude 的**低自我（low ego）和正向能量**是核心差異化因素，超越純粹能力指標。

### 19. 產品願景路線圖

演進路徑：
```
單一任務 → 多任務 → Agent 矩陣（多 Agent 協同）
```

### 20. 個人興趣

閱讀推薦、Waymo、攀岩，以及「退休計畫」（玩笑性質）。

---

## Cat Wu 自述：AI 時代 PM 的四個工作法轉變

（來源：claude.com 博文，2026-03-19）

| 舊工作法 | 新工作法 | 說明 |
|---------|---------|------|
| 長期 Roadmap | **Side Quest 文化** | 自主實驗，午後原型就是功能起點 |
| PRD 文件 | **Demo 取代 PRD** | 讓 Claude Code 做出 prototype，原型錨定決策 |
| 固定功能設計 | **模型更新時重訪功能** | 每個新模型版本都是重新設計的機會 |
| 防禦性複雜設計 | **擁抱簡單** | Workaround 會隨模型進步消失，越簡單的設計越持久 |

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 7/10 | Demo 取代 PRD、research preview 機制、週期 metrics readout 可直接套用於 cc-workspace 的任務規劃流程；side quest 文化呼應 karpathy-principles |
| B. 創新性 | 8/10 | AGI 校準感作為核心 PM 技能、Evergreen Launch Room 機制、「模型更新時重訪功能」設計原則——均為現有 Skills 未涵蓋的洞見 |
| C. 證據品質 | 8/10 | 直接訪談 Anthropic 現任 Claude Code 產品負責人，一手陳述；並有 claude.com 官方博文佐證 |
| D. 技術深度 | 7/10 | 有具體流程（metrics readout 取代 PRD、Research Preview 機制）但缺乏實作細節（例如 Principles Doc 的具體格式） |
| E. 泛化性 | 8/10 | 適用於所有 AI-native 產品團隊，不限 Anthropic 情境；「重訪功能 with 新模型」對任何使用 Claude 的開發者均成立 |
| **加權總分** | **7.6/10** | 7×0.3 + 8×0.2 + 8×0.2 + 7×0.15 + 8×0.15 = 2.1 + 1.6 + 1.6 + 1.05 + 1.2 = **7.55 ≈ 7.6** |

**整合決策**：Rule（更新既有規則）  
**整合位置**：`.claude/rules/karpathy-principles.md` — 補充「模型更新時重訪功能」和「Demo 取代 PRD」作為 Simplicity First + Surgical Changes 的具體 AI 時代變體  
**整合狀態**：待實作
