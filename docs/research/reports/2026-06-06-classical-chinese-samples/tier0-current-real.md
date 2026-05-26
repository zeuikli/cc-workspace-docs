# 規則（tier-0：現行 core.md 真實規則，公平 baseline）

> 從現行 auto-load core.md 直接抽出的對應 5 條。這是真實 baseline——
> 量測證明它已比「人造精練版」更精練（251 vs 302 o200k tok）。

- 改動前讀目標範圍的 exports（介面契約）+ 直接 caller（上游影響）+ 共用 utility（橫向依賴）；不清楚現有結構為何這樣設計，先問再動。
- 實作前先講：(1) 詮釋（≤2 句，非複述）；(2) 關鍵假設；(3) 多解釋時列選項讓使用者選，不靜默選。
- 寫最小能解決問題的代碼：不投機加 feature、不為單次使用抽 helper（Rule of 3：≥3 呼叫點才抽）、不為「未來可能」鋪設。
- 宣告「完成」前 YOU MUST 跑驗證並展示前 5 行/後 5 行輸出；subagent 自報「成功」記為中間態，直到主對話親跑確定性檢查才升 verified。
- Production（GCP/TF/K8s 含 prod）apply/deploy/delete -> 先 plan/diff，再二次確認。
