# prompts/INDEX.md

> **Type:** schema:prompts — 9 個研究專用 system prompt 範本  
> **Updated**: 2026-06-02  
> **Query pattern**: BRAIN.md → 本表（用途欄）→ `<name>.md`

---

## 完整清單

| 檔案 | 用途 | 適用 Skill |
|------|------|-----------|
| [agent-orchestration-prompt.md](agent-orchestration-prompt.md) | Sub-Agent 協作與記憶架構研究 | `autoresearch` · `overnight-research` |
| [ai-agentic-devtools-prompt.md](ai-agentic-devtools-prompt.md) | Agentic 架構 + 開發工具分析 | `research-hub:deep` |
| [ai-business-finops-prompt.md](ai-business-finops-prompt.md) | AI 產品經濟學 + 物理 AI 研究 | `finops` · `research-hub` |
| [ai-frontier-models-prompt.md](ai-frontier-models-prompt.md) | 前沿模型競逐 + 開源生態研究 | `overnight-research` |
| [ai-safety-geopolitics-prompt.md](ai-safety-geopolitics-prompt.md) | AI 地緣政治 + 對齊安全研究 | `research-hub:deep` |
| [optimize-auto-load-tokens.md](optimize-auto-load-tokens.md) | Auto-load token 優化可執行 prompt | `harness-meta:token` |
| [rule-engineering-prompt.md](rule-engineering-prompt.md) | CLAUDE.md 規則工程與 Hook 設計 | `harness-meta:audit` · `autoload-evolution` |
| [skill-design-prompt.md](skill-design-prompt.md) | Claude Code SKILL 設計最佳實踐 | `skill-evolution` · `harness-meta:add` |
| [strategic-insights-prompt.md](strategic-insights-prompt.md) | 策略洞察：Karpathy × Mnilax × bcherny | `autoresearch:reason` |

## 模型遷移注意

> 這些 prompt 跨模型 generation 復用前須注意（接地：prompt-caching-management-engineering C.1/B.4，見 `research/reports/INDEX.md`；完整規則 `.claude/rules/prompt-lifecycle.md`）：

- **re-express ≠ translate**：換模型 generation 時重寫表達保留意圖，不逐字沿用舊 prompt 的 workaround。
- **Claude 偏 XML**：結構用 `<context>`/`<task>`/`<output_format>` 標籤，非 markdown heading。
- **hardest-cases-first**：先用最難案例迭代，通過後簡單案例自然涵蓋。
- **不可跨 generation 直接移植**：舊 prompt 的 workaround 在新模型可能反成噪音。
