---
url: "https://every.to/c/compounding-engineering"
title: "Compound Engineering — How Every Codes with Agents"
date: 2025-12-11 (Updated 2026-04-06)
status: RETRIEVED_FROM_ALTERNATIVE
alternative_url: "https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents"
authors: Dan Shipper, Kieran Klaassen
original_status: URL_NOT_FULLY_ACCESSIBLE
---

# Compound Engineering — How Every Codes with Agents

## 替代來源說明

原始 URL (`every.to/c/compounding-engineering`) 為 Every.to 付費訂閱內容。本文內容取自同一文章的可公開訪問版本：
https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents

---

## 核心摘要（繁體中文）

**Compound Engineering** 是 Every.to 提出的新型軟體開發方法論，針對 AI 代理承擔 100% 程式碼生成工作的團隊設計。其核心創新在於**反轉傳統工程的遞減回報規律**：每完成一項功能，都會為下一項功能的開發帶來便利，而非增加複雜性。

核心機制建立一個**反饋閉環**，其中每個 bug、失敗的測試，或問題解決的洞察都被記錄下來，供未來的代理使用。這形成累積知識系統，使得後續開發週期加速。

工作流程分為四個步驟：
1. **規劃（Plan）**：代理研究 codebase、分析提交歷史、學習網路最佳實踐，合成詳細實作計劃
2. **執行（Work）**：代理按計劃撰寫程式碼並建立測試
3. **審查（Review）**：工程師評估輸出並萃取經驗教訓
4. **複合（Compound）**：將洞察反饋回系統，改進未來代理的表現

根據作者經驗，每個環節的時間投入約為：規劃與審查占 80%，執行與複合占 20%。

**核心效能聲稱**：單一開發者可完成「數年前需要五名開發者的工作量」。Every 運營五個獨立產品，每個產品由單人工程團隊維護，服務數千名日活使用者。

這一方法論的本質在於改變開發思維：從「程式碼編寫困難、工程師稀缺」的假設，轉向「系統設計應協助代理從每次迭代學習」的新範式。Bug 修復、解決方案、設計模式——所有這些都轉化為文檔化知識，加速未來的開發週期。

---

## 關鍵引用

> "a single developer can do the work of five developers a few years ago" when properly leveraging AI

> "each feature makes the next feature easier to build" rather than harder

> "each bug, failed test, or problem-solving insight gets documented and used by future agents"

> Approximately 80% of effort goes to planning and review, while 20% covers work and compounding steps

---

## 與 Karpathy/Mnilax 規則的關聯

此文與 karpathy-principles.md 的**原則 5（Compound Engineering）** 直接對應。Both 強調：

1. **系統化學習反饋**：Karpathy 的「Tool Use as Compounding Knowledge」與 Every 的「每個 bug/test/洞察被記錄」機制相符
2. **代理自動化的邊界**：文章確認工程師角色轉向「編排與學習」而非「手動編碼」——與 Karpathy Rule 5 的角色分工一致
3. **文檔化即知識資產**：系統提示、斜杠指令、子代理、自動化鉤子作為「知識編碼位置」，體現 Mnilax Rule 11（Convention First）與 Rule 12（Fail Loud）的實踐

Every 的四步迴圈（Plan → Work → Review → Compound）可映射到本工作區 core.md 的「實作前假設顯露」（Rule 1）和「完成驗證心法」（Rule 4）的操作化形式。

---

## 相關資源

- GitHub: nibzard/awesome-agentic-patterns（複合工程模式實作參考）
- 本工作區相關檔案: `29-nibzard-compounding-engineering-pattern.md`、`karpathy-principles.md`、`mnilax-12rules.md`
