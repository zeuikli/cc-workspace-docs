---
url: "https://warmwater.dev/blog/karpathy-autoresearch-design"
title: "你去睡覺，它在做研究：讀 Karpathy 的 AutoResearch"
date: 2026-05-12
category: Source Code
source: warmwater.dev
---

## Karpathy AutoResearch 的三個檔案各自做什麼？

autoresearch 只有三個真正重要的檔案，每個角色截然不同：`prepare.py` 是固定不動的裁判、`train.py` 是 agent 的實驗場、`program.md` 是人類寫給 agent 的工作協議。

```
prepare.py   — 固定，不能改。資料載入、tokenizer、評估函式、計時器。
train.py     — 唯一可以改的檔案。模型架構、optimizer、training loop。
program.md   — 人類寫給 agent 的指令文件。
```

這個分法第一眼看起來像是一般的「乾淨設計」——把評估邏輯和業務邏輯分開。但它真正要解決的問題比那深一層：

**Agent 需要有不可以動的裁判，才能產生可信的實驗結果。**

`prepare.py` 裡的 `evaluate_bpb()` 是唯一的評估函式，val_bpb（validation bits per byte）是唯一的指標。這個函式不能被 agent 修改。如果 agent 可以改評估邏輯，它可以在不提升真實能力的情況下讓數字好看——這不是研究，是作弊。

相對地，`train.py` 是完全開放的：模型架構、optimizer 選擇、超參數、batch size、甚至 attention 機制，全部都是 fair game。邊界很清楚：裁判固定，選手自由。

program.md 是第三種東西，後面會仔細說。

---

## 為什麼固定 5 分鐘的時間預算能讓不同實驗直接比較？

固定時間預算讓所有實驗在同一個計算約束下競爭，不需要做任何 normalization。每個實驗的計算量上限是你的 GPU 能在 5 分鐘內跑完的量，不管 agent 改了什麼——deeper model、更大的 batch size、不同的 attention window——都在相同的時間預算下評估。

ML 實驗通常有一個比較問題：一個更大的模型可能 val_loss 更低，但訓練時間也更長。你怎麼知道效益是否值得代價？傳統做法是固定 epoch 數或 token 數，但這在架構改變時又不公平（不同模型一個 epoch 的計算量可能差很多）。

固定時間預算帶來兩個好處。第一，所有實驗直接可比——val_bpb 就是 val_bpb，不需要換算。第二，它自然鼓勵 agent 找「在這個時間預算下最有效率的設計」，而不只是「最大的模型」。

副作用是不同平台的結果不能互相比較：在 H100 跑 5 分鐘 vs 在 MacBook 跑 5 分鐘，是完全不同的實驗。Karpathy 在 README 裡明白說了這一點。但這是可以接受的取捨——autoresearch 的目標不是找到普世最優解，是在你的平台上找到最佳解。每小時約 12 個實驗，睡一覺能跑約 100 個。

---

## AutoResearch 怎麼用 Git 管理實驗狀態？

autoresearch 把 git commit 當成「保留這個實驗」，git reset —hard 當成「丟棄這個實驗」。Git 本身成為實驗狀態機，agent 只需要兩個指令就能管理整個實驗歷程。

實驗循環很直接：

```
1. 改 train.py
2. git commit
3. uv run train.py > run.log 2>&1
4. grep "^val_bpb:" run.log
5. 有進步 → 留在這個 commit，繼續
   沒進步 → git reset --hard，回到上一個好的狀態
6. 把結果寫進 results.tsv
7. 回到 1
```

keep 的決策表現為「不 reset」，discard 的決策表現為 `git reset --hard`。Git log 就是研究歷程。

results.tsv 是 TSV 格式（不是 CSV，因為描述欄位可能有逗號），記錄每個實驗的 commit hash、val_bpb、記憶體使用、狀態（keep/discard/crash）和簡短描述。它不被 git 追蹤（列在 .gitignore），因為它是跨 commit 的元數據，不屬於任何一個 code state。

這個設計的精妙在於：**agent 不需要自己管理「哪個版本最好」的狀態**。Git 本身就是一個可靠的狀態機。Agent 只需要會這兩個 git 指令，就有了完整的實驗管理能力。

---

## program.md 是什麼？它和一般 prompt 有什麼不同？

program.md 不是一次性的 prompt，而是定義了 agent 整個工作協議的文件——包括循環邏輯、判斷標準、邊界案例處理，以及需要 override agent 預設行為的明確指令。Karpathy 自己在 README 裡說它是 "a super lightweight skill"。

看三個 program.md 裡的具體設計選擇：

**「NEVER STOP」的明確指令**：

```
Once the experiment loop has begun, do NOT pause to ask the human 
if you should continue. The human might be asleep, or gone from a computer.
You are autonomous. If you run out of ideas, think harder.
The loop runs until the human interrupts you, period.
```

Agent 的預設行為是遇到不確定就問人。autoresearch 需要的是相反的行為：不確定的時候繼續往前，不是停下來等確認。這個指令是在 override agent 的 default behavior。

**Simplicity criterion**：

```
All else being equal, simpler is better. A 0.001 val_bpb improvement 
that adds 20 lines of hacky code? Probably not worth it. 
An improvement of ~0 but much simpler code? Keep.
```

這在告訴 agent 一個 value judgment——不只優化 val_bpb，還要優化 code quality。這是研究員的判斷，不是算法可以自動得出的結論。

**Crash handling 的分類**：

```
If it's something dumb and easy to fix (typo, missing import), fix it and re-run.
If the idea itself is fundamentally broken, skip it, log "crash", and move on.
```

這是在告訴 agent 什麼時候值得 debug、什麼時候直接放棄。

這三個指令有個共同點：它們都在編碼「研究員在場時會做的判斷」。哪些判斷可以提前寫進 program.md、哪些不行，是下表的整理：

| 可以提前編碼進 program.md | 需要人在場 |
|---|---|
| 停止條件（NEVER STOP） | 判斷新研究方向是否有意義 |
| 品質 tradeoff（simplicity criterion） | 解讀異常結果 |
| 錯誤分類處理（crash handling） | 決定何時結束整個研究 |
| 結果格式與記錄規範 | 添加新的 evaluation 角度 |

program.md 在做的事情是：**把原本需要人類研究員在場才能做的判斷，提前編碼進指令文件**。不是所有判斷都能提前編碼（所以這個系統仍有邊界），但很多可以。能提前編碼的，寫進 program.md；不能的，才需要人在場。

---

## AutoResearch 能自主運作，需要什麼前提條件？

autoresearch 能讓 agent 獨立工作，有一個根本前提：**評估函式是可信的、可量化的、自動運行的**。沒有這個前提，agent 跑完實驗不知道結果好不好，自主循環就無從建立。

val_bpb 可以被 agent 自動計算，不需要人類判斷「這個 loss 好不好」。實驗結束後 5 秒就有結果。這是讓 agent 可以獨立工作的基礎。

如果你在做的研究沒有這樣的評估函式——例如「這份報告寫得好不好」、「這個 UI 是否好用」——autoresearch 的這個設計就不適用。Agent 可以跑實驗，但它不知道結果是否有意義，它需要你告訴它。

另一個假設是：**agent 的探索是序列式的，每次只走一個方向**。program.md 裡的循環讓 agent 每次都在 `train.py` 的當前版本上做一個改動，評估，然後 keep 或 discard。好處是簡單可靠——不需要管理多個實驗分支、不需要 orchestrator、不需要多 agent 協調。缺點是搜尋效率有限，陷入局部最優的風險較高。

Karpathy 在 repo 裡說得很清楚這是一個「bare bones baseline」。你可以在 program.md 裡加入「每 10 個實驗做一次 from-scratch 重置」的指令，或者開多個 agent 實例跑不同的 branch。autoresearch 提供的是最小可運作的骨架，進化空間是設計的一部分。

---

## AutoResearch 這個設計帶來的三個洞見

讀這個 repo 有幾個收穫對我的印象最深。

**限制是設計，不是偷懶**。三個檔案的結構不是「因為簡單所以這樣寫」，而是因為「這個邊界讓系統的每個部分都清楚自己能做什麼、不能做什麼」。`prepare.py` 不可改，所以評估是可信的。`train.py` 完全開放，所以 agent 可以大膽嘗試。這兩個限制一起工作，形成了一個 agent 可以安全自主運作的空間。

**program.md 是這個系統真正的原始碼**。`train.py` 是 agent 寫的程式，不是你寫的。你寫的是 program.md——那個定義了研究流程、判斷標準、邊界條件的指令文件。「怎麼寫好的 program.md」才是工程師在 autoresearch 設計下真正需要掌握的技能。這是一個視角的轉換：不是「怎麼寫好 ML 訓練代碼」，而是「怎麼把你的研究直覺編碼成 agent 能遵循的工作協議」。

**overnight researcher 的概念需要先決條件**。每小時 12 個實驗、睡一覺得到 100 個實驗的結果——這個畫面很吸引人，但背後需要：一個可自動評分的 evaluation function、一個清楚定義邊界的系統、以及一份把關鍵判斷都提前想清楚的 program.md。沒有這三樣，你得到的不是 overnight researcher，而是 overnight chaos。

---

## 結語

autoresearch 的精妙不在於 AI 會跑 ML 實驗，而在於它展示了如何把「需要人在場才能進行的判斷」提前編寫進 program.md，讓 agent 在你睡覺的時候也能做出合理的決策。這個問題——什麼判斷可以提前編碼、什麼不能——比任何具體的模型架構問題都更值得想清楚。
