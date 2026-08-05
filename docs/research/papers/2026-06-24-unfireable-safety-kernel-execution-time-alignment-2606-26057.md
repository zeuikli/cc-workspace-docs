---
url: "https://arxiv.org/abs/2606.26057"
title: "The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems"
arxiv_id: 2606.26057
collected_at: 2026-08-02
collected_by: routine-d
domain: Safety / Alignment
pdf_path: pdfs/2606.26057.pdf
year: 2026
---

# The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents

## 摘要 / 核心貢獻

核心論點：只要安全機制位於 agent 自己的位址空間（address space）內，就必然可被
「能影響該機制的輸入」觸及並繞過——訓練期對齊、prompt-level guardrail 皆屬此類。
本論文主張把安全機制徹底移出 agent 的執行期環境，提出四項架構要求：**行程隔離**
（process separation）、**動作前強制**（pre-action enforcement）、**多層 fail-closed
設計**、以及**外部可驗證證據**（externalized verifiable evidence）。

實作為一個以 Rust 撰寫的 safety kernel，搭配 Z3 定理證明與 Kani 有界模型檢查做形式化
驗證；Python 版本遷移至 Rust 後，用 1,000 個測試 fixture 與 17 類對抗手法驗證。實測：
面對一個「試圖逃逸」的對抗 agent 執行 1,000 次自我修改，其中 704 次針對安全關鍵系統
的攻擊全數被拒絕、零逃逸；另有 300 次在 operator kill switch 啟動狀態下的嘗試同樣
全被拒絕；6,240 次授權往返無一次被繞過；並在防止 agent 自發逃逸上優於三個既有的
agent 控制系統。

## 與 Harness 的關聯

core.md「能力悖論：能力提升不得換取更少驗證」與「不可逆操作永遠等確認」的深層假設，
是「模型自身會遵守寫在 context 裡的規則」——本論文直接挑戰這個假設的可靠邊界，
主張凡是能被輸入影響的機制都不可信任為終局防線。對本 workspace 而言，這是
「為何 unverified_success 閘門與確定性 hook 優先於模型自律」這條設計哲學的
外部理論佐證，也提示：真正高風險的不可逆操作，長期應朝向行程外（out-of-process）
強制執行演進，而非僅靠 CLAUDE.md 條文。
