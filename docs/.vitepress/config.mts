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
    ],
  },
  {
    text: "研究資料庫",
    collapsed: false,
    items: [
      { text: "研究資料庫總覽", link: "/resources/research/" },
      { text: "Harness Engineering 研究全景", link: "/resources/research/harness-engineering" },
      { text: "跨源知識地圖", link: "/resources/research/knowledge-map" },
    ],
  },
  { text: "延伸閱讀與參考資料", link: "/resources/reference/" },
];

export default defineConfig({
  title: "CC Workspace Docs",
  description: "Zeuik 的 Claude Code Workspace 課程文件站。涵蓋 CLAUDE.md 設計、Context Engineering、Harness 工程架構與最佳實踐。",
  base: "/cc-workspace-docs/",
  cleanUrls: true,
  ignoreDeadLinks: true,
  themeConfig: {
    logo: "/logo.svg",
    nav: [
      { text: "首頁", link: "/" },
      { text: "課程講義", link: "/lectures/lecture-01-foundations/", activeMatch: "^/lectures/" },
      { text: "實作專案", link: "/projects/", activeMatch: "^/projects/" },
      { text: "資源庫", link: "/resources/", activeMatch: "^/resources/" },
      {
        text: "GitHub ↗",
        link: githubRepoLink,
        target: "_blank",
        rel: "noopener noreferrer",
      },
    ],
    sidebar: {
      "/lectures/": [
        {
          text: "課程講義",
          items: lectureItems,
        },
      ],
      "/projects/": [
        {
          text: "實作專案",
          items: projectItems,
        },
      ],
      "/resources/": [
        {
          text: "資源庫",
          items: resourceItems,
        },
      ],
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
