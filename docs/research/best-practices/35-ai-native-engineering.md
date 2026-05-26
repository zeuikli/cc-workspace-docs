# AI 原生工程組織管理指南

> 來源：[Running an AI-native engineering org](https://claude.com/blog/running-an-ai-native-engineering-org)（2026-06-03）  
> 作者：Fiona Fung（Claude Code & Claude Cowork Engineering Director）  
> 整理日期：2026-06-05

---

## 核心主張

當 Agentic coding 成為預設工作方式，工程組織必須根本性地重組流程。瓶頸從**撰寫程式碼**轉移到**驗證、審查、安全性**，需要在規劃、Context 蒐集、Code Review、團隊組成上建立新規範。

---

## 四大流程轉變

### 1. 規劃轉型：JIT Planning

傳統六個月 Roadmap 已過時。Claude Code 團隊採用「即時規劃（JIT Planning）」：

- 設計文件 -> 原型驅動開發
- 快速內部用戶回饋循環（而非長期前期規劃）
- 每次模型發布重新評估現有功能

### 2. Context 蒐集轉移

| 舊方式 | 新方式 |
|--------|--------|
| 找原始程式碼作者 | 先問 Claude contextual questions |
| 手動彙整客戶回饋 | 持續背景流程自動化 |

### 3. Code Review 重新定義

Claude 處理：style、linting、bug 偵測、test 生成

人工 Review 聚焦：
- 法律 review
- 安全敏感程式碼
- 產品感（Product sense）
- 設計品味

### 4. 角色模糊化

- PM 現在也寫程式
- 工程師承擔設計和內容工作
- 招聘優先「有產品感的創意建造者」和深度系統專家，而非純粹編碼產出

---

## 三大團隊原則

1. **無情地 Dogfood 自己的產品**：每位成員使用 Claude Code 和 Claude Cowork
2. **保持扁平結構**：Manager 從 IC 起步；扁平結構支援敏捷性
3. **消滅過時流程**：團隊成員有明確授權質疑並消除無效工作流

---

## 三個關鍵指標

| 指標 | 說明 | 目標 |
|------|------|------|
| **Onboarding ramp time** | 工程師第一週就 ship 真實程式碼 | ≤ 1 週 |
| **PR cycle time** | 識別 build system 和 CI 瓶頸 | 持續縮短 |
| **Claude-assisted commits** | 預設接近 100% | ≈ 100% |

Claude Code 團隊連續四個月沒有觀察到非 Claude 協助的 commit。

---

## 如何開始

找到你的「最吵工作流（Noisiest Workflow）」——最昂貴、最讓人頭痛、最低效的流程：

1. 問「這個流程現在還在發揮作用嗎？」
2. 判斷是否可以自動化或直接消除

**實例（Fung 的經驗）：**  
一個有眾多與會者的週例行狀態會議——除了報告自己狀態外，每個人都在滑電腦。問「我們為什麼要開這個會？」-> 取消會議，釋放大量團隊時間。

---

## AI 原生 vs 傳統工程文化對比

| 面向 | 傳統 | AI 原生 |
|------|------|---------|
| 規劃 | 季度/年度 Roadmap | JIT，原型驅動 |
| Context | 找人問 | 先問 Claude |
| Code Review | 覆蓋 style + logic | 人工聚焦高判斷領域 |
| 角色邊界 | 明確分工 | 模糊，PM/設計/工程互滲 |
| 招聘 | 編碼吞吐量 | 產品感 + 系統思維 |
| 流程 | 固化規範 | 主動質疑並消除 |

---

## 延伸閱讀

- `17-best-practices-overview.md` — 官方最佳實踐總綱
- `04-subagent-mcp-skill.md` — Sub-Agent 委派策略
- `29-onboarding-large-codebase.md` — 大型 Codebase 入職實踐
