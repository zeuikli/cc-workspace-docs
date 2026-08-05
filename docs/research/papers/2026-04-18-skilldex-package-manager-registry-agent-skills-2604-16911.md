---
url: "https://arxiv.org/abs/2604.16911"
title: "Skilldex: A Package Manager and Registry for Agent Skill Packages with Hierarchical Scope-Based Distribution"
archived_date: 2026-06-24
arxiv_id: 2604.16911
authors: ["Sampriti Saha", "Pranav Hemanth"]
domains: [cs.AI]
html: "https://arxiv.org/html/2604.16911v1"
pdf_path: pdfs/2604.16911.pdf
published_date: 2026-04-18
---

# Skilldex: A Package Manager and Registry for Agent Skill Packages with Hierarchical Scope-Based Distribution

**Authors**: Sampriti Saha, Pranav Hemanth
**Published**: April 18, 2026
**Source**: https://arxiv.org/abs/2604.16911 · [HTML](https://arxiv.org/html/2604.16911v1)
**arXiv ID**: 2604.16911
**Categories**: cs.AI
**PDF**: [research/papers/pdfs/2604.16911.pdf](https://arxiv.org/abs/2604.16911) (9 pp, full text archived)

---

## Abstract (quoted)

> Large Language Model (LLM) agents are increasingly extended at runtime via skill packages, structured natural-language instruction bundles loaded from a well-known directory. Community install tooling and registries exist, but two gaps persist: no public tool scores skill packages against Anthropic's published format specification, and no mechanism bundles related skills with the shared context they need to remain mutually coherent. We present Skilldex, a package manager and registry for agent skill packages addressing both gaps. The two novel contributions are: (1) compiler-style format conformance scoring against Anthropic's skill specification, producing line-level diagnostics on description specificity, frontmatter validity, and structural adherence; and (2) the skillset abstraction, a bundled collection of related skills with shared assets (vocabulary files, templates, reference documents) that enforce cross-skill behavioral coherence. Skilldex also provides supporting infrastructure: a three-tier hierarchical scope system, a human-in-the-loop agent suggestion loop, a metadata-only community registry, and a Model Context Protocol (MCP) server. The system is implemented as a TypeScript CLI (skillpm / spm) with a Hono/Supabase registry backend, and is open-source.

---

## 結構化摘要

### 核心貢獻
agent skill package 的 package manager + registry，補兩缺口：(a) 無工具對照 Anthropic skill 格式 spec 評分；(b) 無機制把相關 skill 連同共享 context 綁束。兩貢獻：

1. **Compiler-style format conformance scoring** — 對照 Anthropic skill 規範產 line-level 診斷（description 具體度、frontmatter 有效性、結構符合度）。
2. **skillset abstraction** — 相關 skill + 共享資產（vocabulary / templates / reference docs）綁束，強制跨 skill 行為一致。

附：三層 hierarchical scope、human-in-the-loop suggestion loop、metadata-only registry、MCP server。實作為 TypeScript CLI（skillpm/spm）+ Hono/Supabase，開源。

### 關鍵結果
- 無量化 benchmark（9 pp，工程/系統論文，1 圖 5 表）。

### 限制
- 偏工具/系統貢獻，無效能數字；conformance scoring 的 spec 隨 Anthropic 規範演進需維護。

---

## Workspace 關聯（評估，非既成結論）

- **直接對應 skill 審計建議**：compiler-style SKILL.md conformance scoring 可併入 `harness-meta` 的 schema-verify（本 session schema-lint 已偵測「INDEX no frontmatter」「1 agent schema issue」——正是此類 lint 的需求）。
- **skillset abstraction ↔ pilot 群 / review 群**：本 workspace 的 4 pilot（haiku/sonnet/opus/fable）+ review 三件（qp/`/pilot frontier` 稽核（原 pilot-review）/ship-review）即「相關 skill + 共享紀律」，可作 skillset 綁束的現成案例。
- **three-tier scope ↔ auto-load vs on-demand vs path-scoped**：本 workspace 規則已有三態（auto-load / on-demand / path-scoped），與 Skilldex scope 概念同構。
- ⚠️ 為外部開源工具（TypeScript/Supabase），非可直接套用；價值在「skill spec lint + skillset 綁束」設計理念，落地走 harness-meta schema-verify 擴充。
