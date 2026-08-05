---
url: "https://arxiv.org/abs/2605.29251"
title: "Provably Secure Agent Guardrail"
arxiv_id: 2605.29251
collected_at: 2026-08-01
collected_by: routine-d
domain: Safety / Alignment
pdf_path: pdfs/2605.29251.pdf
year: 2026
---

# Provably Secure Agent Guardrail

## 摘要 / 核心貢獻

隨著語言模型演化為具執行能力的自主 agent，安全漏洞隨之浮現。本文指出一個關鍵缺口：現有防禦仰賴「經驗式語意 guardrail 與機率式大模型仲裁者」，無法對複雜的語意操縱攻擊提供可證明的保護保證。

作者提出 **ePCA（Proof-Constrained Action）框架**，採用神經符號隔離架構。系統不信任自然語言指令本身，而是要求 agent 在執行前將其意圖行動形式化轉換為一階邏輯數學約束，強制執行無損的意圖形式化。

關鍵結果：在測試情境中達到零攻擊成功率與零誤判率；評測中計算延遲極低；驗證使用了宏觀與微觀兩種維度的動態對抗系統。研究意義在於從機率式語意防禦轉向以形式驗證為基礎的邏輯推理防線，是為未來自主系統建構基礎安全層的工程取徑，並明確揭露系統假設的適用範圍。

## 與 Harness 的關聯

呼應 core.md 公理「不可逆不變式必須落 hook 或程式層」——ePCA 把「agent 意圖是否安全」從 LLM 自陳（機率式）轉為形式化邏輯約束（確定性程序驗證），與本 workspace `core.md §APPLY 自主迴圈`（原 `loop.md L3`）「reward hacking 結構防線」同源：真正的防線是結構性的，而非「prompt 裡寫禁止」。可作為未來若要把 core.md「不可逆操作永遠等確認」規則從純文字指示升級為機械閘門時的形式化方法參考。
