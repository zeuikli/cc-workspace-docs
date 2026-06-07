---
url: "https://warmwater.dev/blog/prompt-copilot"
title: "用 Copilot Instructions 讓 AI 更懂你的專案：prompt-copilot 實戰指南"
date: 2025-06-28
category: Viewpoint
source: warmwater.dev
---

[
← Viewpoint ](/blog?tag=Viewpoint)  Viewpoint  
#  ✨ 如何用一段 Prompt 讓 Copilot 更了解你的專案？ 
  2025-06-28 · — views      

GitHub Copilot 是許多開發者不可或缺的 AI 助手，但你是否也曾遇過這種情況：

> 


「咦？它怎麼還用舊版的 Pydantic 語法？」

「為什麼補的程式碼不符合我們團隊的風格？」


這些看似小問題，背後的主因是 —— **Copilot 對你的專案背景「一無所知」**。

幸好，GitHub 推出了新的機制：

你可以透過 `.github/copilot-instructions.md` 這個檔案，**教 Copilot 如何更聰明地協作。**

## 🧩 `.github/copilot-instructions.md` 是什麼？


這是一個由 GitHub 官方支援的特殊設定檔，放在你專案的 `.github/` 資料夾下。


透過這份 Markdown 文件，你可以告訴 Copilot：


- 


專案是做什麼的


- 


主要用哪些技術與框架（例如 FastAPI, Pydantic v2, LangChain）


- 


喜歡什麼樣的寫法與風格（像是 async/await, type hint, logging 工具）


- 


有哪些過時或不該使用的語法（像是舊版 `@validator`）


一旦這份檔案存在，Copilot Chat 與自動補全功能都會**優先參考裡面的指引**，大幅提升建議的品質與一致性。

## 🧠 用一段 Prompt 自動產生指引


手動撰寫 `.copilot-instructions.md` 雖然可以，但何不讓 AI 來幫我們生成呢？


以下是我實際使用的 prompt，讓 Copilot 自動分析整個專案並產出這份指引：


(基本款)

```
You are an expert GitHub Copilot agent.

Please analyze the **entire codebase** in this repository and generate a comprehensive `.github/copilot-instructions.md` file that Copilot Chat and autocomplete can use to follow correct, consistent, and modern code practices.

...

Output the final result as a valid markdown file, ready to be saved as `.github/copilot-instructions.md`.

```


(進階款)

```
You are an expert GitHub Copilot agent.

Please analyze the **entire codebase** in this repository and generate a comprehensive `.github/copilot-instructions.md` file that Copilot Chat and autocomplete can use to follow correct, consistent, and modern code practices.

### Your tasks:

1. **Generate** a detailed `.github/copilot-instructions.md` file with the following sections:
   - Project Context
   - Used Technologies
   - Coding Style Guidelines
   - Preferred Patterns
   - LLM Integration Rules (if applicable)
   - Development Practices
   - Things to Avoid

2. **Infer the package versions** and major dependencies based on the `pyproject.toml` file.  
   All syntax and code style should align with the actual versions used in this project.  
   (For example, if `pydantic = "^2.0"` is found, ensure all validation follows Pydantic v2 style.)

3. Ensure alignment with:
   - Python 3.12+
   - FastAPI >= 0.115
   - Pydantic v2
   - Modern async/await practices
   - LangChain (if found), Langfuse, Prometheus, and any other dependencies

4. ⚠️ **Important Behavior Rule for Copilot Chat**:  
   Every time you respond to a user query in Copilot Chat:
   - Begin by stating that you have read and understood the `.github/copilot-instructions.md`.
   - Use a phrase like:  
     _"I've reviewed and understood the project's Copilot instructions. Based on your codebase's style and declared dependencies, here's the best solution..."_
   - Do **not answer any question** until this declaration is made and all suggestions follow the documented style.

5. Do not make assumptions. Only infer patterns and usage based on actual project code and dependencies.

Output the final result as a valid markdown file, ready to be saved as `.github/copilot-instructions.md`.
```


這段 prompt 的工作內容包含：


- 


掃描整個程式碼庫，總結出專案使用的技術與慣例


- 


根據 `pyproject.toml` 推斷出使用的套件與版本（例如 Pydantic v2）


- 


建立包含「開發風格」、「架構慣例」、「避免事項」的標準化說明


- 


要求 Copilot Chat 每次回答前，都需明確聲明自己遵守了這份指引


## 🚀 小結：讓 Copilot 更像你的隊友


GitHub Copilot 很強，但**它不懂你的專案，就只能亂猜**。

透過 `.copilot-instructions.md` + 一段精心設計的 Prompt，你可以：


✅ 建立開發共識

✅ 自動生成程式風格指南

✅ 提升程式碼品質與可維護性

✅ 讓 Copilot 成為一位真正懂你專案的 AI 工程師


我整理了一些prompts for copilot agent放在**[useful-prompt-for-copilot-agent](https://github.com/jason8745/useful-prompt-for-copilot-agent)**裡, 歡迎contribute或是拿去使用

## Update (2025/12/05)


我覺得可以直接參考保哥的Repo, 他有整理了更多好用的prompt -> [https://github.com/doggy8088/github-copilot-configs](https://github.com/doggy8088/github-copilot-configs)

## 延伸閱讀


- [Harness Engineering — AI 工程師的第三個維度](/blog/harness-engineering-ai) — context 注入是 Harness 的一個面向：把專案背景放進 context 讓 AI 更懂你

- [Agentic Context Engineering：讓 AI 代理人自我改進的關鍵技術](/blog/agentic-context-engineering-ai) — 系統性地思考 context window 的內容設計，不只是 prompt 措辭

- [Plan Mode 之後：你的 AI Agent 還缺什麼](/blog/superpowers-plan-mode-ai-agent) — Copilot 之後：AI coding agent 四個失敗模式與行為約束設計
     [ Viewpoint ](/blog?tag=Viewpoint)  
### 
相關文章

[ViewpointAI 時代的 PM / HR / Sales：你才是讓 AI 落地的那個人2026-05-26](/blog/ai-for-non-engineer-workplace)[ViewpointAI 時代的非工程師：從今天開始，不需要準備好2026-05-26](/blog/ai-mindset-non-engineer)[ViewpointAI 時代的 Backend Engineer：從會用到能建的完整路線2026-05-26](/blog/backend-to-ai-engineer-roadmap)
