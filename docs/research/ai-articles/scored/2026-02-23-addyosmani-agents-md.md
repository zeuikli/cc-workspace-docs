---
url: "https://addyosmani.com/blog/agents-md/"
title: "Stop Using /init for AGENTS.md"
date: 2026-02-23
type: article
---

# Stop Using /init for AGENTS.md

**原始來源**：https://addyosmani.com/blog/agents-md/  
**作者**：Addy Osmani  
**發表日期**：2026-02-23  
**評分日期**：2026-05-05

---

## 繁體中文全文摘要

### TL;DR

自動生成的 AGENTS.md 傷害 Agent 效能，增加成本 20% 以上。原因是 Agent 本來就能自己發現這些資訊，你只是讓它讀了兩遍。**只有 Agent 無法自行推斷的資訊才值得一行。**

### 研究發現：AGENTS.md 有沒有用？

兩項研究，結論看似矛盾，但實際揭示了更深的真相：

#### Lulla et al.（ICSE JAWs 2026）
- 124 個真實 GitHub PR，有無 AGENTS.md 對比
- **結果**：有 AGENTS.md → median 執行時間 -28.64%，輸出 token -16.58%
- **但**：這些是人類精心維護的文件，包含真實的項目特有知識

#### ETH Zurich 研究
- 測試 LLM 自動生成 vs. 開發者撰寫的 context 文件
- **LLM 生成文件**：task 成功率 -2~3%，成本 +20% 以上
- **開發者撰寫文件**：成功率 +4%，但成本也 +19%
- **最關鍵發現**：移除 repo 的所有文件後再測試，LLM 生成的 context 文件改善了 2.7%

**統一解釋**：自動生成的內容不是沒用，而是**冗餘**。Agent 能自己找到這些資訊。給它同樣的資訊兩次 = 噪音。

### 粉象問題（Anchoring Effect）

AGENTS.md 中提到的任何技術/模式都會在每個提示詞中影響模型。若你提到已廢棄的框架，模型會傾向於使用它。**「Lost in the Middle」效應（Liu et al. 2024）**：放在 context 中間的資訊更容易被忽略，但放在 AGENTS.md 的資訊卻會無差別地影響每個任務。

### /init 的核心問題

100% 的 Sonnet 4.5 自動生成文件都包含 codebase 概覽。99% 的 GPT-5.2 也是如此。這些正好是 Agent 通過 `ls` 和讀取 README 就能自己找到的東西。

**實際效果**：Agent 讀取 AGENTS.md → 去讀真實代碼確認 → 需要協調兩個資訊來源 → 更多 token，更慢，同樣結果。

### 什麼真正值得寫入 AGENTS.md

ETH Zurich 研究的具體發現：
- 當 context 文件提到 `uv`（套件管理器）→ Agent 使用頻率：1.6 次/任務
- 不提及 → 使用頻率：< 0.01 次/任務

**判斷標準**：`uv` vs `pip` 的區別符合三條件：
1. 代碼庫中無法直接發現
2. 操作上有重大影響（改變執行的命令）
3. Agent 無法透過慣例推斷

對比「專案使用 monorepo 結構，packages 在 /packages 下」—— 第一個 `ls` 就能找到。

**理想 AGENTS.md 範例**：
```
- 使用 uv 進行套件管理

- 永遠用 --no-cache 跑測試，否則 fixture 設定會有假陽性

- auth 模組使用自定義 middleware，勿重構為標準 Express middleware

- legacy/ 目錄已棄用但被三個生產模組引用，不要刪除其中任何東西
```

### 靜態文件問題

一個扁平的指令集無法針對任務類型做條件判斷：
- Agent 做 CSS 重構時不需要看資料庫遷移警告
- Agent 實作安全修復時可能應該跳過效能優化提示

**ACE 框架（ICLR 2026）** 透過 generator/reflector/curator pipeline 把 context 當成動態演進的 playbook，超越靜態文件 **12.3%**。

### 正確架構

**Layer 1（Protocol File）**：AGENTS.md 的本質 — routing 文件，不是概覽
- 可用角色與何時調用
- 可用 skills 與任務類別
- Agent 真正無法發現的最小必要 repo 事實

**Layer 2（Focused persona/skill files）**：依任務類型選擇性載入

**Layer 3（維護 Sub-agent）**：唯一職責是保持 protocol file 準確

### 正確心態

把 AGENTS.md 當成「**你還沒修好的磨擦點列表**」：
- Agent 一直把工具放錯目錄 → 目錄結構有問題，應重組
- Agent 一直用廢棄 dependency → import 結構讓錯誤的那個太容易被抓到
- Agent 忘記跑 type check → build pipeline 應該自動捕捉

每一行 AGENTS.md 都是你尚未修好的技術債的信號，而非永久配置。

### 對 Workspace 的啟示

1. **CLAUDE.md 應是目錄，不是百科全書**：與 OpenAI Codex 文章的發現一致
2. **`@-import` 按需載入策略是正確的**：不同任務載入不同 rules，已在 cc-workspace 實踐
3. **60 行以下的 CLAUDE.md 是目標**：過長的 CLAUDE.md = 警示信號，應提取到 refs/
4. **Agent 反覆犯同樣的錯 → 先改代碼，再改 AGENTS.md**：這條原則應納入 haiku-pilot 的 Known Gotchas

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 9/10 | 直接影響 CLAUDE.md 設計策略，「靜態 vs 動態載入」是 cc-workspace 的核心架構決策 |
| B. 創新性 | 7/10 | 反直覺結論（/init 有害）和粉象問題是新穎洞見；但整合現有研究而非原創 |
| C. 證據品質 | 7/10 | 引用兩篇有量化數據的獨立研究；本文本身是 blog，非原始研究 |
| D. 技術深度 | 7/10 | 三層架構方案具體，`uv` 案例有說服力，但 ACE 框架只是提及未深入 |
| E. 泛化性 | 8/10 | 適用所有使用 agent 配置文件的項目，不限 Claude Code |
| **加權總分** | **7.75/10** | 9×0.3 + 7×0.2 + 7×0.2 + 7×0.15 + 8×0.15 = 2.7+1.4+1.4+1.05+1.2 |

**整合決策**：Rule  
**整合位置**：`.claude/refs/anthropic-insights.md` 或 `.claude/rules/core.md`  
**整合狀態**：待實作

**TODO**：
- 在 CLAUDE.md 加入「每行 CLAUDE.md 都是尚未修好的摩擦點」的指導原則
- haiku-pilot Known Gotchas 補充：「Agent 反覆同一錯誤時，先看代碼結構，再加 context」
