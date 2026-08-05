---
url: "https://arxiv.org/abs/2607.04528"
title: "Measuring Harness-Induced Belief Divergence in Multi-Step LLM Agents"
archived_date: 2026-07-18
arxiv_id: 2607.04528
authors: ["Haiwen Yi", "Xinyuan Song"]
pdf_path: pdfs/2607.04528.pdf
published_date: 2026-07-05
---

# Measuring Harness-Induced Belief Divergence in Multi-Step LLM Agents

**Authors**: Haiwen Yi, Xinyuan Song
**Published**: July 2026
**Source**: https://arxiv.org/abs/2607.04528
**arXiv ID**: 2607.04528
**Categories**: Computer Science - Artificial Intelligence (cs.AI)
**PDF**: [research/papers/pdfs/2607.04528.pdf](https://arxiv.org/abs/2607.04528)

---

## Abstract

This research investigates how evaluation frameworks affect agent decision-making in language models. The authors observe that even when task specifications and underlying models remain constant, the testing infrastructure—including action restrictions, repair handling, and evidence logging—can meaningfully alter an agent's reasoning patterns. To measure this phenomenon, they developed a diagnostic tool that captures agent beliefs across nine dimensions including progress, risk, recoverability, constraints, failure mode, uncertainty, future success, repair cost, and next action under different testing setups. Their analysis on coding benchmarks reveals that blocking certain actions, limiting repair information, restricting verification checks, and filtering evidence often preserve task completion while shifting the underlying reasoning processes. They propose BIWM, a standardization protocol that reconciles observations across different evaluation frameworks by logging hidden branches, documenting repair history, recording verification outcomes, and executing risky actions in isolated simulation.

---

## Core Thesis

- 揭示一個容易被忽略的變因：即使任務規格與底層模型完全相同，**評測 harness 本身**（動作限制、修復處理、證據記錄方式）就會顯著改變 agent 的推理內容，即使最終任務完成率不變。
- 設計九維度信念探測工具（progress、risk、recoverability、constraints、failure mode、uncertainty、future success、repair cost、next action），量化不同 harness 設定下 agent「內在信念」的偏移程度。
- 在程式碼 benchmark 上發現：封鎖特定動作、限制修復資訊、限縮驗證檢查、過濾證據——這些 harness 層面的選擇常常「任務完成率不變、但推理過程已經改變」，是一種隱形的評測污染。
- 提出 BIWM 標準化協議（記錄隱藏分支、修復歷史、驗證結果，並在隔離模擬中執行風險動作）調和跨 harness 的觀測差異。
- **Workspace 關聯**：呼應本庫既有 Harness-Bench（2605.27922，同批次收錄）「agent capability 應以 model-harness 組態層級回報」的立場，並進一步指出即使任務完成率一致，harness 差異仍可能污染「推理過程」本身——對 `core.md §PROPOSE 委派`（原 subagent-strategy.md）的「verdict 非證據，需機械重驗」提供更細緻的失真來源分類。
