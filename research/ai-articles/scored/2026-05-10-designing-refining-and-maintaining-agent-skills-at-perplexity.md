---
url: https://research.perplexity.ai/articles/designing-refining-and-maintaining-agent-skills-at-perplexity
source_file: ../2026-05-10-designing-refining-and-maintaining-agent-skills-at-perplexity.md
date: 2026-05-10
scored: 2026-05-16
source: Perplexity Research Blog
source_tier: C
tags: [skill-design, progressive-loading, skill-index, gotchas-flywheel, eval-first]
---

# Designing, Refining, and Maintaining Agent Skills at Perplexity

**原始來源**：https://research.perplexity.ai/articles/designing-refining-and-maintaining-agent-skills-at-perplexity  
**字數**：約 3,948 字

---

## TL;DR

Perplexity 內部 Skill 設計指南。核心論點：「Skill 設計哲學與寫 code 完全相反」——好的 code 準則（Simple、Explicit、Sparse）在 Skill 中往往是反模式。三層 Progressive Loading 架構（Index 100t / Load 5k / Runtime 無上限）、eval-first 流程、gotchas flywheel，是生產品質 Skill 的核心。

---

## 核心主張

1. **Skill 是 Directory，不是 File**
   - Hub（`SKILL.md`）+ Spokes（`scripts/`、`references/`、`assets/`、`config.json`）
   - 多層 hierarchy 解決大規模知識路由：1,945 節稅法 → 20 類 × 15 條 > 單平鋪

2. **三層 Progressive Loading Token 預算**

   | Tier | 載入內容 | Token 預算 | 何時付費 |
   |------|---------|-----------|---------|
   | Index | name + description | ~100t/Skill | 每 session 必付 |
   | Load | 完整 SKILL.md body | ~5,000t | 呼叫後到 compaction |
   | Runtime | scripts/references/assets | 無上限 | 需要時才讀 |

3. **Description 是 Routing Trigger，不是文件**
   - 格式：「Load when...」（≤50 字）
   - 錯誤：描述 Skill 功能。正確：描述用戶意圖（real queries）
   - 描述改動需重跑 eval，否則不改

4. **Gotchas 是最高密度內容**
   - Agent 失敗 → append gotcha（負例）
   - off-target load → 收緊 description + 加負例 eval
   - Skill 是 append-mostly，description 改動才是例外

5. **arxiv 實證：LLM 無法自行寫好 Skill**
   - 論文 [2602.12670](https://arxiv.org/abs/2602.12670)：Self-generated Skills 平均無益
   - 結論：Skill 必須注入人類判斷與領域知識

---

## cc-workspace 可行動性

1. **Skill Index token 預算提醒**：每個 Skill 的 description ≤100 tokens，因為所有 session 都付費。當前 .claude/skills/ 下的 Skill description 是否過長？

2. **Reference 抽離原則**：條件性重內容（API 文件、特殊情況）應移至 `references/` 按需載入，不要塞進主 SKILL.md body。

3. **Eval-before-description**：新 Skill 先寫 eval case（包含負例），再寫 description；description 改動後重跑 eval。

4. **描述格式標準化**：統一 `Load when...` 格式；cc-workspace 現有 Skill 可審查是否符合。

---

## 評分

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 9/10 | 3-tier token budget、gotchas flywheel、directory structure 直接可套用至 cc-workspace Skill 設計審查 |
| B. 創新性 | 8/10 |「Zen of Python vs Zen of Skills」對比新穎；LLM 無法自寫 Skill 的 arxiv 實證未見於現有 rules |
| C. 證據品質 | 7/10 | 引用 arxiv 論文 + Perplexity 生產案例（稅法 1945 節）；缺量化 eval 數據 |
| D. 技術深度 | 9/10 | 具體 token budget 數字、目錄結構、5步驟建設流程、eval suite 分類（load precision/recall、progressive read、end-to-end） |
| E. 泛化性 | 9/10 | 原則適用任何 skill-based agent 系統，非 Perplexity 專屬 |
| **加權總分** | **8.4/10** | 9×0.3 + 8×0.2 + 7×0.2 + 9×0.15 + 9×0.15 = 2.70+1.60+1.40+1.35+1.35 |

**整合決策**：Rule（通用原則適用所有 Skill 設計任務）  
**整合位置**：`.claude/refs/skill-design-guide.md`（新建）或補充進 `.claude/rules/core.md` § Skill 設計原則  
**整合狀態**：待實作

---

## TODO

- [ ] 新建 `.claude/refs/skill-design-guide.md`，收錄：3-tier token budget、description 格式規範（Load when...）、gotchas flywheel、eval-first checklist
- [ ] 審查現有 `.claude/skills/*/SKILL.md` 的 description 是否符合 ≤50 字 / Load when... 格式
- [ ] 確認 references/ 抽離原則已反映在 skill-authoring-patterns
