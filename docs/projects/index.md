# 實作專案

本課程的實作專案讓你從「看懂理論」進入「動手建立」。每個專案都有具體的任務清單、參考實作和驗收標準。

## 專案清單

### [Project 01：從零建立你的第一個 Workspace](/projects/project-01-init-workspace/)

建立一個完整的 Claude Code Workspace，包含 CLAUDE.md、MEMORY.md 和基本的 Hooks 設定。完成後你的 workspace 應該能夠：跨 session 記憶專案規則、自動初始化環境、有明確的驗收定義。

**前置課程**：Lecture 01, 02, 05

### [Project 02：設計你的 Harness](/projects/project-02-harness-design/)

設計並實作一個有 Planner / Generator / Evaluator 三層架構的 Harness。完成後你應該能夠：把模糊需求轉換成可執行 spec、阻斷危險指令、讓 Evaluator 用外部工具驗證 Generator 的輸出。

**前置課程**：Lecture 03, 04, 06

## 學習建議

1. 按順序完成：每個專案都建立在前一個的基礎上
2. 使用你自己的實際專案：比用範例專案學得更快
3. 記錄失敗：每個失敗都是 Ratchet 原則的素材
4. 從小開始：先建立最小可用 Harness，再逐步迭代
