---
url: "https://arxiv.org/abs/2606.21005"
title: "Building Agent Harnesses for Scientific Curation from Multimodal Sources"
archived_date: 2026-06-24
arxiv_id: 2606.21005
authors: ["Sheng Zhang", "Qin Liu", "Renqian Luo", "Shufang Xie", "Reuben Tan", "Sean Hayes", "Gregory Bryman", "Wendong Ge", "Roxy Zhang", "Oluwaseun Egbelowo", "Kelly Yee", "Hoifung Poon"]
domains: [cs.AI, cs.CL]
html: "https://arxiv.org/html/2606.21005v1"
pdf_path: pdfs/2606.21005.pdf
published_date: 2026-06-19
---

# Building Agent Harnesses for Scientific Curation from Multimodal Sources

**Authors**: Sheng Zhang, Qin Liu, Renqian Luo, Shufang Xie, Reuben Tan, Sean Hayes, Gregory Bryman, Wendong Ge, Roxy Zhang, Oluwaseun Egbelowo, Kelly Yee, Hoifung Poon
**Published**: June 19, 2026
**Source**: https://arxiv.org/abs/2606.21005 · [HTML](https://arxiv.org/html/2606.21005v1)
**arXiv ID**: 2606.21005
**Categories**: cs.AI, cs.CL
**PDF**: [research/papers/pdfs/2606.21005.pdf](https://arxiv.org/abs/2606.21005) (20 pp, full text archived)

---

## Abstract (quoted)

> Scientific discovery workflows often depend on structured curation from the literature. This is difficult for current agents because the key evidence is scattered across long text, dense tables, and figures, and the final records often require reasoning across multiple evidence fragments rather than copying a single span. We study scientific curation from multimodal sources and introduce Beaver, an agent harness that extracts structured information from scientific papers while preserving provenance to the supporting evidence. Beaver combines a frontier agent with multimodal evidence tooling, task scaffolding, and artifact-grounded autoresearch. These components turn curation into a staged, auditable workflow and enable an iterative evaluate–diagnose–revise loop, where persistent run artifacts expose stage-localized failures and guide harness updates. Experiments show that Beaver reaches 81.0 on Gold-Referenced Attribute Score (GRAS), an attribute-level measure of agreement with gold curated records, outperforming frontier agents by over 23 absolute points. Ablations show that task scaffolding, multimodal evidence tooling, and provenance traces each contribute meaningfully to performance, while attribute-level analysis shows the largest gains on high-value attributes that require cross-modal reasoning and normalization. These results show that, for scientific curation from papers with multimodal evidence, harness design is a central determinant of agent performance.

---

## 結構化摘要

### 核心貢獻
**Beaver** = 從多模態科學文獻做結構化 curation 的 agent harness，核心主張「harness 設計是 agent 表現的中心決定因素」。組成：

1. **Frontier agent + multimodal evidence tooling** — 跨長文 / 密集表格 / 圖的證據抽取。
2. **Task scaffolding** — 把 curation 變成 staged、可稽核 workflow。
3. **Artifact-grounded autoresearch** — persistent run artifact 暴露 **stage-localized failure**，驅動 **evaluate→diagnose→revise** 迭代與 harness 更新。
4. **Provenance preservation** — 最終記錄保留到支撐證據的溯源（非單 span 複製，而需跨片段推理）。

### 關鍵結果
- **GRAS 81.0**（attribute-level 與 gold 記錄一致度），超 frontier agent **+23 絕對分**。
- Ablation：task scaffolding / multimodal tooling / provenance trace 各自顯著貢獻。
- 最大增益落在「需跨模態推理 + 正規化」的高價值屬性。

### 限制
- 文件未列明確 limitation；依賴 frontier agent + 多模態工具，成本與領域泛化待驗。

---

## Workspace 關聯（評估，非既成結論）

- **The Loop 同構（最直接者之一）**：`evaluate→diagnose→revise` + persistent artifact 暴露 stage-localized failure = `OBSERVE→IDENTIFY→...→RECORD` 的 trace 化；artifact-grounded 對應本 workspace 的 `claude-progress.json` / RECORD checkpoint。
- **autoresearch skill 直接呼應**：「artifact-grounded autoresearch」+ modify→verify→keep/discard，幾乎是 autoresearch:learn / research-hub 的學術版；可作該 skill 設計參考。
- **provenance / 溯源**：對應 research-hub 歸檔的引用紀律與 deep-research 的 cited synthesis。
- ⚠️ 「harness design 為中心決定因素」+ ablation 證據，是支持 harness-engineering 投資的有力外部佐證；列入 KNOWLEDGE-MAP 證據池。
