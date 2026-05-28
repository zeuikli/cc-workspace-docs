import { defineConfig } from "vitepress";

const githubRepoLink = "https://github.com/zeuikli/cc-workspace-docs";

const lectureItems = [
  { text: "課程總覽", link: "/lectures/lecture-01-foundations/" },
  { text: "Lecture 01：Claude Code 與 Harness 基礎", link: "/lectures/lecture-01-foundations/" },
  { text: "Lecture 02：CLAUDE.md 設計", link: "/lectures/lecture-02-claude-md/" },
  { text: "Lecture 03：Context Engineering", link: "/lectures/lecture-03-context-engineering/" },
  { text: "Lecture 04：Harness 三層架構", link: "/lectures/lecture-04-harness-architecture/" },
  { text: "Lecture 05：記憶系統與工作區設計", link: "/lectures/lecture-05-memory-workspace/" },
  { text: "Lecture 06：安全沙箱與 Proxy", link: "/lectures/lecture-06-security/" },
];

const projectItems = [
  { text: "專案總覽", link: "/projects/" },
  { text: "Project 01：從零建立你的第一個 Workspace", link: "/projects/project-01-init-workspace/" },
  { text: "Project 02：設計你的 Harness", link: "/projects/project-02-harness-design/" },
];

const resourceItems = [
  { text: "資源總覽", link: "/resources/" },
  {
    text: "最佳實踐指南",
    collapsed: false,
    items: [
      { text: "最佳實踐總覽", link: "/resources/best-practices/" },
      { text: "工作流程與核心技巧", link: "/resources/best-practices/workflows" },
      { text: "Hooks 設計模式", link: "/resources/best-practices/hooks" },
      { text: "Permission 細粒度設定", link: "/resources/best-practices/permissions" },
      { text: "MCP Server 與 Skills", link: "/resources/best-practices/mcp-skills" },
      { text: "Prompt Caching 工程", link: "/resources/best-practices/prompt-caching" },
      { text: "Multi-Agent 架構模式", link: "/resources/best-practices/multi-agent" },
    ],
  },
  {
    text: "研究摘要（精選）",
    collapsed: false,
    items: [
      { text: "研究資料庫總覽", link: "/resources/research/" },
      { text: "Harness Engineering 研究全景", link: "/resources/research/harness-engineering" },
      { text: "跨源知識地圖", link: "/resources/research/knowledge-map" },
      { text: "Model-Harness Fit", link: "/resources/research/model-harness-fit" },
      { text: "Harness 驗證方法論", link: "/resources/research/verification-methods" },
    ],
  },
  { text: "延伸閱讀與參考資料", link: "/resources/reference/" },
];

const researchItems = [
  { text: "研究資料庫總覽", link: "/research/" },
  {
    text: "Agent Harness 核心",
    collapsed: true,
    items: [
      { text: "分類索引", link: "/research/agent-harness/" },
      { text: "SURVEY — 論文總覽", link: "/research/agent-harness/SURVEY" },
      { text: "KNOWLEDGE-MAP", link: "/research/agent-harness/KNOWLEDGE-MAP" },
      { text: "RESEARCH — 架構研究", link: "/research/agent-harness/RESEARCH" },
      { text: "References 索引（64 篇）", link: "/research/agent-harness/references/" },
    ],
  },
  {
    text: "社群文章",
    collapsed: true,
    items: [
      { text: "文章索引", link: "/research/ai-articles/" },
      { text: "Harness Articles Digest", link: "/research/ai-articles/HARNESS-ARTICLES-DIGEST" },
      { text: "MHF Research Digest", link: "/research/ai-articles/MHF-RESEARCH-DIGEST" },
      { text: "12 Harness Patterns", link: "/research/ai-articles/32-medium-12-agentic-harness-patterns" },
      { text: "Thin Harness Fat Skills", link: "/research/ai-articles/41-yageai-thin-harness-fat-skills" },
      { text: "Model-Harness Fit", link: "/research/ai-articles/2026-05-16-model-harness-fit" },
      { text: "Boris Verification Loops", link: "/research/ai-articles/2026-05-12-boris-cherny-verification-loops" },
      { text: "Stripe 1,300 PRs/Week", link: "/research/ai-articles/2026-05-12-ai-agent-harness-stripe-1300-prs" },
    ],
  },
  {
    text: "學術論文",
    collapsed: true,
    items: [
      { text: "論文索引", link: "/research/papers/" },
    ],
  },
  {
    text: "研究報告",
    collapsed: true,
    items: [
      { text: "報告索引", link: "/research/reports/" },
      { text: "Harness Engineering 深度研究", link: "/research/reports/2026-05-17-harness-engineering" },
      { text: "驗證方法論", link: "/research/reports/2026-05-19-harness-verification-methods" },
      { text: "Model-Harness Fit 分析", link: "/research/reports/2026-05-16-harness-engineering-model-fit" },
      { text: "Sub-Agent Delegation Gotchas", link: "/research/reports/2026-05-17-claude-code-subagent-delegation-gotchas" },
      { text: "Auto-Load Token 優化", link: "/research/reports/2026-05-18-auto-load-token-best-practices" },
      { text: "Karpathy×Mnilax 最佳解", link: "/research/reports/2026-05-18-karpathy-mnilax-best-solution" },
    ],
  },
  {
    text: "影片筆記",
    collapsed: true,
    items: [
      { text: "影片索引", link: "/research/videos/" },
      { text: "AI Engineer — Tejas Kumar (IBM)", link: "/research/videos/2026-05-17-AI-Engineer-C_GG5g38" },
      { text: "Sequoia Capital — AI Agents", link: "/research/videos/2026-04-29-Sequoia_Capital-96jN2OCO" },
      { text: "Nate Herk — 32 Claude Tricks", link: "/research/videos/2026-04-29-nateherk-32-claude-code-tricks" },
      { text: "No Priors Podcast", link: "/research/videos/2026-03-20-No_Priors-kwSVtQ7d" },
      { text: "Dwarkesh Patel Interview", link: "/research/videos/2025-10-17-Dwarkesh_Patel-lXUZvyaj" },
    ],
  },
  {
    text: "Claude Blog",
    collapsed: true,
    items: [
      { text: "Blog 索引", link: "/research/claude-blog/" },
    ],
  },
  {
    text: "推文筆記（Tweets）",
    collapsed: true,
    items: [
      { text: "推文索引", link: "/research/tweets/" },
    ],
  },
  {
    text: "AI 新聞摘要",
    collapsed: true,
    items: [
      { text: "新聞索引", link: "/research/ai-news/" },
      { text: "2026-04 月報", link: "/research/ai-news/2026-04-brief" },
      { text: "2026-04 Digest", link: "/research/ai-news/2026-04-digest" },
      { text: "2026-05 月報", link: "/research/ai-news/2026-05-brief" },
      { text: "2026-05 Digest", link: "/research/ai-news/2026-05-digest" },
      { text: "2026-Q1 季報", link: "/research/ai-news/2026-q1-brief" },
      { text: "2026-Q1 Digest", link: "/research/ai-news/2026-q1-digest" },
      { text: "主題索引", link: "/research/ai-news/TOPIC-INDEX" },
    ],
  },
  {
    text: "最佳實踐",
    collapsed: true,
    items: [
      { text: "索引", link: "/research/best-practices/" },
      {
        text: "入門概覽",
        collapsed: false,
        items: [
          { text: "Claude Code 如何運作", link: "/research/best-practices/18-how-claude-code-works" },
          { text: "最佳實踐總覽", link: "/research/best-practices/17-best-practices-overview" },
          { text: "功能總覽（Features Overview）", link: "/research/best-practices/19-features-overview" },
        ],
      },
      {
        text: "日常工作流",
        collapsed: false,
        items: [
          { text: "常見工作流（Common Workflows）", link: "/research/best-practices/20-common-workflows" },
          { text: "Memory 與 CLAUDE.md", link: "/research/best-practices/21-memory-claudemd" },
          { text: "Code Review 多代理審查", link: "/research/best-practices/22-code-review" },
          { text: "Onboarding 大型 Codebase", link: "/research/best-practices/29-onboarding-large-codebase" },
        ],
      },
      {
        text: "設定與權限",
        collapsed: false,
        items: [
          { text: "官方 Hooks、Memory、Settings", link: "/research/best-practices/01-official-hooks-memory-settings" },
          { text: "Permissions 細粒度設定", link: "/research/best-practices/12-permissions" },
        ],
      },
      {
        text: "Hooks 與自動化",
        collapsed: false,
        items: [
          { text: "Hooks 實戰設計模式", link: "/research/best-practices/03-hooks-patterns" },
          { text: "Routines 排程自動化", link: "/research/best-practices/11-routines" },
        ],
      },
      {
        text: "Agent、Skills 與 Prompting",
        collapsed: false,
        items: [
          { text: "社群 CLAUDE.md 與 Agent Skill", link: "/research/best-practices/02-community-claudemd-agent-skill" },
          { text: "Sub-agent、MCP、Skill 進階", link: "/research/best-practices/04-subagent-mcp-skill" },
          { text: "Claude Prompting 最佳實踐", link: "/research/best-practices/05-claude-prompting-best-practices" },
          { text: "Agent Skills 最佳實踐", link: "/research/best-practices/06-agent-skills-best-practices" },
          { text: "Advisor Tool 最佳實踐", link: "/research/best-practices/07-advisor-tool-best-practices" },
          { text: "Agent Skills 企業治理", link: "/research/best-practices/10-agent-skills-enterprise" },
        ],
      },
      {
        text: "Caching、MCP 與 Plugins",
        collapsed: false,
        items: [
          { text: "Prompt Caching 技術指南", link: "/research/best-practices/08-prompt-caching" },
          { text: "Prompt Caching 核心教訓（Thariq）", link: "/research/best-practices/28-thariq-prompt-caching-lessons" },
          { text: "MCP 整合完整指南", link: "/research/best-practices/14-mcp" },
          { text: "Plugin 系統完整指南", link: "/research/best-practices/24-plugins" },
        ],
      },
      {
        text: "安全與沙箱",
        collapsed: false,
        items: [
          { text: "安全部署完整指南", link: "/research/best-practices/09-secure-deployment" },
          { text: "Sandboxing OS 層隔離", link: "/research/best-practices/13-sandbox" },
        ],
      },
      {
        text: "社群技巧",
        collapsed: false,
        items: [
          { text: "Boris Cherny Tips", link: "/research/best-practices/15-boris-cherny-tips" },
          { text: "Boris Config & GitHub 設定", link: "/research/best-practices/25-bcherny-config-github" },
          { text: "Thariq Tips — Skill 與 Session", link: "/research/best-practices/16-thariq-tips" },
        ],
      },
      {
        text: "新功能追蹤",
        collapsed: true,
        items: [
          { text: "新工具與 Slash Commands（W13–W20）", link: "/research/best-practices/30-new-tools-commands" },
        ],
      },
    ],
  },
  {
    text: "Prompt 模板",
    collapsed: true,
    items: [
      { text: "索引", link: "/research/prompts/" },
      { text: "Agent Orchestration", link: "/research/prompts/agent-orchestration-prompt" },
      { text: "AI Agentic DevTools", link: "/research/prompts/ai-agentic-devtools-prompt" },
      { text: "AI Business FinOps", link: "/research/prompts/ai-business-finops-prompt" },
      { text: "AI Frontier Models", link: "/research/prompts/ai-frontier-models-prompt" },
      { text: "AI Safety Geopolitics", link: "/research/prompts/ai-safety-geopolitics-prompt" },
      { text: "Rule Engineering", link: "/research/prompts/rule-engineering-prompt" },
      { text: "Skill Design", link: "/research/prompts/skill-design-prompt" },
      { text: "Strategic Insights", link: "/research/prompts/strategic-insights-prompt" },
    ],
  },
  {
    text: "文件模板",
    collapsed: true,
    items: [
      { text: "索引", link: "/research/templates/" },
      { text: "AI 新聞研究 Prompt", link: "/research/templates/ai-news-research-prompt" },
      { text: "Overnight Research 模板", link: "/research/templates/overnight-research-template" },
      { text: "推文研究 Prompt", link: "/research/templates/tweets-research-prompt" },
    ],
  },
];

export default defineConfig({
  title: "Zeuik's Claude Code Docs",
  description: "Zeuik 的 Claude Code Workspace 課程文件站。涵蓋 CLAUDE.md 設計、Context Engineering、Harness 工程架構與最佳實踐。",
  base: "/cc-workspace-docs/",
  cleanUrls: true,
  ignoreDeadLinks: true,
  srcExclude: [],
  themeConfig: {
    logo: "/logo.svg",
    nav: [
      { text: "首頁", link: "/" },
      { text: "課程講義", link: "/lectures/lecture-01-foundations/", activeMatch: "^/lectures/" },
      { text: "實作專案", link: "/projects/", activeMatch: "^/projects/" },
      { text: "資源庫", link: "/resources/", activeMatch: "^/resources/" },
      { text: "研究資料庫", link: "/research/", activeMatch: "^/research/" },
      {
        text: "GitHub ↗",
        link: githubRepoLink,
        target: "_blank",
        rel: "noopener noreferrer",
      },
    ],
    sidebar: {
      "/lectures/": [{ text: "課程講義", items: lectureItems }],
      "/projects/": [{ text: "實作專案", items: projectItems }],
      "/resources/": [{ text: "資源庫", items: resourceItems }],
      "/research/": [{ text: "研究資料庫", items: researchItems }],
    },
    outline: {
      level: [2, 3],
      label: "本頁目錄",
    },
    docFooter: {
      prev: "上一篇",
      next: "下一篇",
    },
    lastUpdated: {
      text: "最後更新於",
    },
    returnToTopLabel: "回到頂部",
    sidebarMenuLabel: "選單",
    darkModeSwitchLabel: "主題",
    lightModeSwitchTitle: "切換到淺色模式",
    darkModeSwitchTitle: "切換到深色模式",
    socialLinks: [{ icon: "github", link: githubRepoLink }],
    search: {
      provider: "local",
    },
  },
  markdown: {
    theme: {
      light: "github-light",
      dark: "github-dark",
    },
  },
});
