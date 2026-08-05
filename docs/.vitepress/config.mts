import { defineConfig } from "vitepress";

const githubRepoLink = "https://github.com/zeuikli/cc-workspace-docs";

const lectureItems = [
  { text: "課程總覽", link: "/lectures/" },
  {
    text: "Part 1：基礎",
    collapsed: false,
    items: [
      { text: "Lecture 01：Claude Code 與 Harness 基礎", link: "/lectures/lecture-01-foundations/" },
      { text: "Lecture 02：CLAUDE.md 設計", link: "/lectures/lecture-02-claude-md/" },
      { text: "Lecture 03：Context Engineering", link: "/lectures/lecture-03-context-engineering/" },
    ],
  },
  {
    text: "Part 2：架構",
    collapsed: false,
    items: [
      { text: "Lecture 04：Harness 三層架構", link: "/lectures/lecture-04-harness-architecture/" },
      { text: "Lecture 05：記憶系統與工作區設計", link: "/lectures/lecture-05-memory-workspace/" },
      { text: "Lecture 06：安全沙箱與 Proxy", link: "/lectures/lecture-06-security/" },
    ],
  },
  {
    text: "Part 3：擴展",
    collapsed: false,
    items: [
      { text: "Lecture 07：Skills 設計與 Progressive Disclosure", link: "/lectures/lecture-07-skills/" },
      { text: "Lecture 08：Sub-agents 與 Dynamic Workflows", link: "/lectures/lecture-08-subagents-workflows/" },
      { text: "Lecture 09：模型選型與 Effort 經濟學", link: "/lectures/lecture-09-model-selection/" },
    ],
  },
  {
    text: "Part 4：工程化",
    collapsed: false,
    items: [
      { text: "Lecture 10：驗證迴圈與 Code Review", link: "/lectures/lecture-10-verification/" },
      { text: "Lecture 11：MCP 整合與外部系統", link: "/lectures/lecture-11-mcp/" },
      { text: "Lecture 12：Plugins、自動化與組織治理", link: "/lectures/lecture-12-governance/" },
    ],
  },
];

const projectItems = [
  { text: "專案總覽", link: "/projects/" },
  { text: "Project 01：從零建立你的第一個 Workspace", link: "/projects/project-01-init-workspace/" },
  { text: "Project 02：設計你的 Harness", link: "/projects/project-02-harness-design/" },
  { text: "Project 03：把驗證編碼成 Skill", link: "/projects/project-03-verification-skill/" },
  { text: "Project 04：Plugin 化與自動化治理", link: "/projects/project-04-plugin-automation/" },
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
      { text: "報告索引（全覽）", link: "/research/reports/" },
      {
        text: "⭐ Canonical 母報告",
        collapsed: false,
        items: [
          { text: "Agent 工程研究合成", link: "/research/reports/2026-05-31-consolidated-agent-engineering-research" },
          { text: "Auto-Load Token SSoT", link: "/research/reports/2026-06-05-autoload-token-best-practices-consensus" },
          { text: "12 條準則論文接地深化", link: "/research/reports/2026-06-05-12-rule-deepened-research" },
        ],
      },
      {
        text: "Harness Engineering",
        collapsed: true,
        items: [
          { text: "Harness 工程深度研究", link: "/research/reports/2026-05-31-harness-engineering-deep-research" },
          { text: "Harness 自演化合成", link: "/research/reports/2026-06-05-harness-memory-self-evolution-synthesis" },
          { text: "Harness 演化計劃", link: "/research/reports/2026-05-28-harness-evolution-plan" },
        ],
      },
      {
        text: "LLM Memory",
        collapsed: true,
        items: [
          { text: "LLM 記憶控制全調查", link: "/research/reports/2026-05-22-llm-memory-control-comprehensive-survey" },
        ],
      },
      {
        text: "Context Window / Caching",
        collapsed: true,
        items: [
          { text: "Context Window 深度研究", link: "/research/reports/2026-06-03-context-window-management-deep-research" },
          { text: "Prompt Caching 工程", link: "/research/reports/2026-06-03-prompt-caching-management-engineering" },
          { text: "冷啟動 Latency 研究", link: "/research/reports/2026-06-03-claude-code-cold-start-latency-deep-research" },
        ],
      },
      {
        text: "Auto-Load / Token",
        collapsed: true,
        items: [
          { text: "CJK Token 稅研究", link: "/research/reports/2026-06-06-cjk-token-tax-research" },
          { text: "Auto-Load Token 優化", link: "/research/reports/2026-06-06-autoload-token-optimization" },
        ],
      },
      {
        text: "12-Rule / Best Practices",
        collapsed: true,
        items: [
          { text: "12 條準則深化全文", link: "/research/reports/2026-06-05-12-rule-deepened-ruleset" },
          { text: "12 條準則 Universal 版", link: "/research/reports/2026-06-04-12-rule-universal-ruleset" },
        ],
      },
      {
        text: "Sub-Agent / Agent Team",
        collapsed: true,
        items: [
          { text: "研究艦隊", link: "/research/reports/2026-06-04-research-fleet-research" },
          { text: "Merge Pipeline", link: "/research/reports/2026-06-04-merge-pipeline-research" },
        ],
      },
      {
        text: "Skill / Workspace Canon",
        collapsed: true,
        items: [
          { text: "Skill 整併規格", link: "/research/reports/2026-06-07-skill-consolidation-spec" },
          { text: "Workspace Canon", link: "/research/reports/2026-06-06-zeuik-workspace-canon" },
          { text: "CLAUDE.md 最佳實踐", link: "/research/reports/2026-06-05-claudemd-best-practices" },
        ],
      },
      {
        text: "前沿 AI 領域研究（6/07）",
        collapsed: true,
        items: [
          { text: "AI Alignment / CAI", link: "/research/reports/2026-06-07-ai-alignment-constitutional-ai" },
          { text: "AI Safety Red-Teaming", link: "/research/reports/2026-06-07-ai-safety-red-teaming" },
          { text: "Diffusion Language Models", link: "/research/reports/2026-06-07-diffusion-language-models" },
          { text: "Mechanistic Interpretability", link: "/research/reports/2026-06-07-mechanistic-interpretability" },
          { text: "Multimodal VLM", link: "/research/reports/2026-06-07-multimodal-vision-language-models" },
          { text: "Test-Time Compute Scaling", link: "/research/reports/2026-06-07-test-time-compute-scaling" },
        ],
      },
      {
        text: "Claude Code 社群實踐",
        collapsed: true,
        items: [
          { text: "社群實踐基礎研究", link: "/research/reports/2026-06-07-claude-code-community-practices-report" },
          { text: "深度實踐 v2", link: "/research/reports/2026-06-07-claude-code-deep-practices-v2" },
        ],
      },
      {
        text: "Session Insights",
        collapsed: true,
        items: [
          { text: "對稱懷疑原則", link: "/research/reports/2026-06-07-session-insights-symmetric-skepticism" },
          { text: "六領域 Meta-Reflection", link: "/research/reports/2026-06-07-session-insights-multi-domain-ai-research" },
        ],
      },
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
      { text: "課程講義", link: "/lectures/", activeMatch: "^/lectures/" },
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
