# 資源庫

本資源庫收錄課程相關的延伸閱讀、官方文件連結與參考資料。

課程講義本身已在每堂課末列出對應的官方一手來源；這裡收的是**跨課程通用**的入口與精選整理。

## 內容分類

### [最佳實踐指南](/resources/best-practices/)

五個面向的工程化整理：工作流程、Hooks 設計模式、Permission 細粒度設定、MCP 與 Skills、Prompt Caching。整理自官方文件與核心貢獻者（Boris Cherny、Thariq Shihipar）的公開分享。

### [研究摘要（精選）](/resources/research/)

Harness Engineering 的學術論文、工業案例與跨源知識地圖，含量化數據索引。

### [延伸閱讀與參考資料](/resources/reference/)

精選的官方文件、工程部落格與研究論文，按主題分類。篩選標準：只收錄「能**直接解釋 Harness 機制**」的內容——不是泛泛的 prompt engineering 或 agent 框架介紹。

## 快速連結

### Claude Code 官方文件

| 主題 | 連結 | 對應課程 |
|------|------|---------|
| 文件首頁 | <https://code.claude.com/docs> | — |
| Memory（CLAUDE.md + Auto Memory）| <https://code.claude.com/docs/en/memory> | [L02](/lectures/lecture-02-claude-md/) |
| Features Overview（機制選擇）| <https://code.claude.com/docs/en/features-overview> | [L07](/lectures/lecture-07-skills/) |
| Best Practices 總綱 | <https://code.claude.com/docs/en/best-practices> | [L01](/lectures/lecture-01-foundations/) |
| Common Workflows | <https://code.claude.com/docs/en/common-workflows> | [L05](/lectures/lecture-05-memory-workspace/) |
| Hooks | <https://code.claude.com/docs/en/hooks> | [L04](/lectures/lecture-04-harness-architecture/) |
| Sub-Agents | <https://code.claude.com/docs/en/sub-agents> | [L08](/lectures/lecture-08-subagents-workflows/) |
| Skills | <https://code.claude.com/docs/en/skills> | [L07](/lectures/lecture-07-skills/) |
| MCP | <https://code.claude.com/docs/en/mcp> | [L11](/lectures/lecture-11-mcp/) |
| Code Review | <https://code.claude.com/docs/en/code-review> | [L10](/lectures/lecture-10-verification/) |
| Permissions | <https://code.claude.com/docs/en/permissions> | [L06](/lectures/lecture-06-security/) |
| Sandboxing | <https://code.claude.com/docs/en/sandboxing> | [L06](/lectures/lecture-06-security/) |
| Plugins | <https://code.claude.com/docs/en/plugins> | [L12](/lectures/lecture-12-governance/) |
| Routines | <https://code.claude.com/docs/en/routines> | [L12](/lectures/lecture-12-governance/) |
| Advisor Tool | <https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool> | [L09](/lectures/lecture-09-model-selection/) |
| Agent Skills Best Practices | <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices> | [L07](/lectures/lecture-07-skills/) |

### 課程核心參考資料

**Harness 工程（理論基礎）**

| 文章 | 主題 |
|------|------|
| [Anthropic: Harness design for long-running apps](https://www.anthropic.com/engineering/harness-design-long-running-apps) | Planner / Generator / Evaluator |
| [Anthropic: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | 跨 session 狀態管理 |
| [OpenAI: Harness engineering](https://openai.com/index/harness-engineering/) | Agent-first 倉庫設計 |
| [LangChain: Improving Deep Agents](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering) | Harness 工程量化案例 |
| [Chroma: Context Rot Research](https://www.trychroma.com/research/context-rot) | 18 個模型的 context 衰退實證 |

**Claude 5 世代（2026 下半年的轉向）**

| 文章 | 主題 |
|------|------|
| [The new rules of context engineering for Claude 5](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) | system prompt −80% 無退化；六條 Then→Now |
| [Claude models explained](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case) | class × effort 選型框架；Advisor 90%/63% |
| [Building verification loops with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills) | 驗證迴圈四種部署形態 |
| [Steering Claude Code](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more) | 七種行為調整機制 |
| [Bringing MCP 2026-07-28 to Claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude) | Stateless core、Extensions、OAuth/OIDC |

**安全與治理**

| 文章 | 主題 |
|------|------|
| [Anthropic: How we contain Claude across products](https://www.anthropic.com/engineering/how-we-contain-claude) | 環境層優先於模型層 |
| [Zero Trust for AI agents](https://claude.com/blog/zero-trust-for-ai-agents) | 三層框架、六類 agentic 漏洞 |
| [Zero risk isn't the job: a CISO's guide](https://claude.com/blog/ciso-guide-to-agentic-ai) | 四個評估問題、七項控制 |
| [Using LLMs to secure source code](https://claude.com/blog/using-llms-to-secure-source-code) | 六步驟方法論；獨立 verifier −50% FP |
| [How Anthropic secures its AI-native SDLC](https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle) | AI 寫 80% 程式碼下的分層防線 |

## 全文歸檔

上述文章的重點摘錄與跨文合成收在研究資料庫：

- [claude-blog 官方部落格歸檔](/research/claude-blog/) — 153 個條目，2025-11 ~ 2026-07
- [跨主題合成分析](/research/claude-blog/docs/synthesis) — 九個主題，含 2026 下半年的三個轉向
- [發布時間軸](/research/claude-blog/docs/timeline)
- [最佳實踐 49 篇](/research/best-practices/)
