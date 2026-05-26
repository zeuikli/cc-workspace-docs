---
status: SUCCESS
url: https://github.com/ciembor/agent-rules-books
repository: ciembor/agent-rules-books
date_fetched: 2026-05-18
---

# 37. GitHub: Agent Rules Books

## 核心摘要（繁體中文）

該儲存庫提供從經典軟體工程著作中提取的規則集合，專門設計用於 AI 編碼工具（Codex、Cursor、Claude Code）。提供三個版本（完整、精簡、迷你），並以驗證實驗證明規則有效性提升。

### 涵蓋的 13 本軟體工程書籍

1. **A Philosophy of Software Design**：深層模組、簡單介面和資訊隱藏
2. **Clean Architecture**：穩定邊界和依賴規則
3. **Clean Code**：可讀性、命名和小型函數
4. **Code Complete**：構造實踐、防禦性編程和測試
5. **Designing Data-Intensive Applications**：可靠性、可擴展性和一致性
6. **Domain-Driven Design**：領域建模和無所不在的語言
7. **Domain-Driven Design Distilled**：實用的 DDD 入門
8. **Implementing Domain-Driven Design**：聚合體和領域事件
9. **Patterns of Enterprise Application Architecture**：企業應用設計模式
10. **Refactoring**：安全改進程式碼結構的方法
11. **Refactoring.Guru**：實用的重構過程和代碼異味
12. **Release It!**：生產環境的系統可靠性
13. **The Pragmatic Programmer**：實用的軟體開發方法
14. **Working Effectively with Legacy Code**：安全修改困難程式碼

### 規則版本選項

**完整版（Full）**
- 詳細的參考資料
- 包含完整解釋和背景
- 適合學習和深度理解

**精簡版（Mini）**
- 推薦用於大多數實踐應用
- 平衡詳細度和簡潔性
- 在驗證實驗中表現最佳

**迷你版（Nano）**
- 針對內容預算有限的情況
- 極簡規則集合
- 適合快速參考

### 規則涵蓋的關鍵主題

**代碼品質**
- 命名約定和慣例
- 函數設計和責任單一性
- 簡單性和複雜度管理

**架構設計**
- 邊界清晰性
- 依賴注入和反轉
- 關注點分離（Separation of Concerns）

**領域建模**
- 無所不在的語言（Ubiquitous Language）
- 有限上下文（Bounded Contexts）
- 聚合體（Aggregates）和領域事件

**重構與改進**
- 安全的重構技術
- 代碼異味識別
- 行為保護（Behavioral Preservation）

**生產系統**
- 可靠性原則
- 故障處理和恢復
- 可觀測性和監控
- 電路斷路器（Circuit Breakers）

**遺留代碼**
- 特徵測試（Characterization Tests）
- 接縫模型（Seam Model）
- 漸進式改進

### 驗證與效果評估

儲存庫包含驗證實驗結果：

- **應用規則的版本**：重構 A Philosophy of Software Design 時達到約 74/100 評分
- **對照組（無規則）**：僅得 46/100 評分
- **改進幅度**：約 61% 的質量提升

**結論**：使用具體規則列表比僅提及書籍名稱更有效。

### 使用方式

規則可用於多種場景：
- 集成至 `AGENTS.md` 或 `.claude/` 配置
- 作為 Claude Code 的技能和提示
- 作為 Cursor 或 GitHub Copilot 的指導
- 專案級別的編碼標準

---

## 關鍵數據/引用

### 驗證實驗成果

> 應用具體規則列表的版本在重構任務中獲得約 74/100 的評分，而對照組僅得 46/100。

**關鍵發現**：
- 規則版本 vs 對照：+61% 品質提升
- Mini 版本與完整版性能相近
- 具體規則優於一般建議

### 核心原則

儲存庫強調的統一主題：
- **簡單性優先**：複雜系統難以維護和演進
- **邊界清晰**：明確的責任分離和依賴流向
- **可測試性**：代碼應設計成可測試的
- **可觀測性**：生產系統需要明確的可見性
- **漸進改進**：安全的重構而非大規模重寫

### 推薦應用流程

1. **選擇合適版本**：大多數情況選 Mini 版本
2. **集成至工作流程**：納入代理提示或 `.claude/` 規則
3. **組織成類別**：按書籍或主題分組
4. **定期審視**：隨著專案演進更新和補充

---

## MIT 授權

該儲存庫採用 MIT 授權，允許自由使用和修改。

---

## 重要說明

這些規則是「受啟發於」而非官方再現；它們補充但不替代閱讀實際書籍。建議將規則作為快速參考，配合原著進行深度學習。

