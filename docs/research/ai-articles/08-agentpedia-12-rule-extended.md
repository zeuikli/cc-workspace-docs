---
url: "https://agentpedia.codes/blog/karpathy-claude-md-rules-extended"
title: "Karpathy CLAUDE.md Rules + 8 More - The 12-Rule Template (2026)"
author: "Agentpedia Codes"
date: 2026-05-11
status: SUCCESS
---

# Karpathy CLAUDE.md Rules + 8 More: The 12-Rule Template (2026)

## 核心摘要

本文追溯了一個重要的軟體開發實踐的演進過程。2026年1月，Andrej Karpathy 發表了對 Claude 編碼能力的批評，指出三個關鍵失敗模式。開發者 Forrest Chang 將這些觀察轉化為四條明確的行為規則，編寫成 CLAUDE.md 檔案。隨後，開發者 Mnimiy 基於對 30 個代碼庫的六週測試，額外添加了 8 條規則，形成了完整的 12 規則體系。

**演進時間線**

- **2026年1月**：Karpathy 在 Twitter 上發布關於 Claude 編碼問題的觀察
- **2026年1月27日**：Forrest Chang 創建 andrej-karpathy-skills 倉庫，包含四條規則
- **首日反應**：5,828 顆星；兩週內 60,000 個書籤；年中突破 120,000 顆星
- **2026年5月**：Mnimiy 發布擴展研究，聲稱 12 條規則將 Claude 的錯誤率從 41% 降低到 3%

**原始四條規則**

四條規則對應四個核心失敗模式：

1. **編碼前思考**：防止無聲假設和盲目執行
2. **簡潔優先**：防止過度工程化和代碼膨脹
3. **精準修改**：防止無關修改和範圍蔓延
4. **目標驅動執行**：防止執行標準模糊和反覆迭代不足

實驗證明，應用這四條規則可將錯誤率從 41% 降低至 11%。

**擴展的八條規則**

**規則 5：禁止 LLM 執行確定性決策**

模型應只進行「判斷」（分類、摘要、提取、創意生成），不應進行「決定」（路由、重試邏輯、HTTP 狀態碼選擇、數學計算）。這區分了 LLM 的適用邊界。

**規則 6：硬性令牌預算**

設置 per-task 和 per-session 的令牌上限，防止上下文窗口濫用。規則規定 per-task ≤4,000 tokens，per-session ≤30,000 tokens。

**規則 7：衝突浮現**

當兩個互相矛盾的模式並存時，選擇更新或覆蓋率更高的一個，明確標註另一個待清理。禁止混用矛盾的模式。

**規則 8：讀前寫**

修改前必須閱讀目標代碼範圍的 exports、直接調用者、共享 utility。不清楚現有結構時先問再動。

**規則 9：測試檢驗意圖**

測試應能在業務邏輯改變時失敗。能通過任何實現的測試等同於沒有測試。

**規則 10：Checkpoint**

每完成重要步驟輸出一句摘要：「做了什麼/驗了什麼/剩什麼」。無法描述當前狀態時停下重述。

**規則 11：規範優先**

既有的 codebase 慣例優於個人偏好。遵循最近 3 個 commit 的模式。慣例本身有害時明說並另開議題，不「靜默 fork」。

**規則 12：大聲失敗**

完成後必須跑驗證並展示輸出前 5 行/後 5 行（中間省略）。略過步驟/跳過驗證必須明示，不得以「完成」「成功」掩蓋靜默跳過。

**實驗數據**

| 配置 | 錯誤率 | 合規性 |
|-----|--------|--------|
| 無指導 | ~41% | — |
| 四條規則 | ~11% | 78% |
| 12條規則 | ~3% | 76% |
| 14+條規則 | >15% | 52% |

**心態轉變**

重要洞察：「CLAUDE.md 不是願望清單。它是一份行為合約，關閉你觀察到的特定失敗模式。」

每條規則應回答：這條規則防止了什麼錯誤？

**實用建議**

- 一個六規則 CLAUDE.md 調整到真實失敗模式，勝過一個 12 規則的檔案
- 超過 14 條規則時合規性急劇下降至 52%，證實了 200 行的實用上限
- 針對項目特點定製，而非簡單複製標準集合

## 關鍵引述

> "5,828 stars on day one. 60,000 bookmarks in two weeks. 120,000 stars by mid-2026."
> — 項目成長的驚人速度

> "CLAUDE.md is not a wishlist. It's a behavioral contract, closing specific failure modes you observe."
> — 對該工具本質的關鍵理解

> "A six-rule CLAUDE.md tuned to your real failure modes beats a 12-rule file."
> — 實用性優於完整性的原則

> "Without CLAUDE.md: ~41% error rate. Four rules: ~11%. Twelve rules: ~3%."
> — 規則堆積的邊際效應
