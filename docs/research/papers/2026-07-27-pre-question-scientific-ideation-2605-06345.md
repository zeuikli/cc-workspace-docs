---
url: "https://arxiv.org/abs/2605.06345"
title: "More Than Can Be Said: A Benchmark and Framework for Pre-Question Scientific Ideation"
archived_date: 2026-07-27
arxiv_id: 2605.06345
authors: ["Jie Yu", "Song Qiu"]
domain: hypothesis-generation-infrastructure
published_date: 2026-05-07
source_routine: routine-e
---

# More Than Can Be Said: A Benchmark and Framework for Pre-Question Scientific Ideation

## 摘要 / 核心貢獻
提出 InciteResearch 多 agent 框架，處理研究者在能明確表述問題前的「內隱摩擦」（tacit friction）——一種尚無法言明的錯位直覺。三階段：①以五維研究者側寫錨定具體摩擦點 ②挑戰隱藏假設（優化 feasibility×novelty 乘積 + 七階段因果推導鏈）③驗證方法是否為重新框架後洞見的必然結果。並提出 TF-Bench 評測基準，涵蓋四種科學模式、區分領域相關/不相關的靈感來源。相較 prompt-based baseline，novelty 分數由 3.671 升至 4.250，impact 由 3.806 升至 4.397，且產出從「單純重組」轉向「更深的架構性洞見」。

## 為何屬「新領域」
「問題形成前的內隱摩擦處理」與 workspace 既有覆蓋無語意重疊；核心關鍵詞 hypothesis 於既有覆蓋集合反向 grep 命中為 0，且概念上與 know-your-unknowns SKILL 的 Unknown Knowns 象限相近但非既有收錄領域。
