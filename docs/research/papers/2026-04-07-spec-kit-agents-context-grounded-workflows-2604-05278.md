---
url: "https://arxiv.org/abs/2604.05278"
title: "Spec Kit Agents: Context-Grounded Agentic Workflows"
archived_date: 2026-07-31
arxiv_id: 2604.05278
authors: ["Pardis Taghavi", "Santosh Bhavani"]
collected_at: 2026-07-31
collected_by: routine-d
domain: loop-workflow-engineering
pdf_path: pdfs/2604.05278.pdf
published_date: 2026-04-07
---

# Spec Kit Agents: Context-Grounded Agentic Workflows

## 摘要 / 核心貢獻
針對大型程式庫中 AI 代理常因缺乏足夠 repository context 而產生虛構 API 或設計不一致的問題，提出 Spec Kit Agents 框架：以產品經理與開發者兩種角色的多代理協作，並在開發各階段插入「context 驗證檢查點」，對照實際 repository 環境驗證輸出。在 5 個 repository、128 個功能實作的測試中，複合 1–5 分品質量表提升 +0.15，測試相容性幾近完美，並在 SWE-bench Lite 上取得增益。

## 與 Harness 的關聯
「context 驗證檢查點」與本 repo `core.md`「References > 散文 spec：說不清但認得出 → 指向原始碼」高度一致——把驗證錨點釘在實際 repo 內容而非模型記憶或籠統敘述，是防止虛構的具體工程實作，可作為 Done Contract 設計的參考案例。
