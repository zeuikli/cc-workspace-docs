---
url: "https://warmwater.dev/blog/llm-eval-metrics-decision"
title: "選對指標，不要選多：LLM 評估的決策框架"
date: 2026-05-12
category: LLMOps
source: warmwater.dev
---

第一次認真跑 LLM 評估的時候，作者做了一個很蠢的事：全選。DeepEval 有 40 幾個指標，全部開起來，跑完拿到一張報表，上面有 40 幾個分數。然後完全不知道哪個重要。

那次經驗讓作者意識到一件事：指標是工具，不是成績單。你不是要拿高分，你是要回答「這個系統哪裡有問題」。選太多指標的結果，和完全不評估差不多——都是沒有可行動的資訊。

**讀完這篇，你會知道：**

*   不同系統架構對應哪些指標，以及為什麼
*   幾個看起來相似但實際量不同東西的指標，怎麼區分
*   什麼時候用 G-Eval，什麼時候應該換做法
*   指標全過了但系統還是爛的幾個典型情況

這篇是決策框架，不是指標字典。你的系統是什麼架構，就看對應的段落。

---

## 選指標之前，先確認系統架構是什麼

選指標之前，先想清楚你在評估什麼。不同架構的失敗模式不一樣，需要量的東西也不一樣：

| 架構 | 主要失敗點 | 核心指標方向 |
|------|----------|-----------|
| RAG（檢索增強生成） | Retrieval 召回了錯的東西；生成時沒用好 context | Faithfulness、Contextual 系列 |
| Tool-use Agent | 工具選錯；參數填錯；多步驟順序錯 | Tool Correctness、Argument Correctness |
| 多輪 Chatbot | 忘記前幾輪說的；角色飄移 | Knowledge Retention、Role Adherence |
| 純 LLM 推理服務 | Prompt 改版後輸出品質變化 | G-Eval（自訂準則）、ArenaEval（版本比較） |

架構確定了，才知道要量什麼。從這張表找到你的位置，然後去看對應的段落。

---

## 做 RAG：先搞清楚是 retrieval 爛還是生成爛

RAG 系統的問題通常發生在兩個地方：召回的東西不對，或者召回的東西是對的但沒有被正確使用。這兩個問題要用不同的指標去找。

### Faithfulness vs. Hallucination——兩個都在看「事實性」，但量的不是同一件事

Faithfulness 問的是："這個回答有沒有被 retrieval context 支撐？" 它是 RAG pipeline 的核心指標——就算世界上沒有這個知識，只要 context 支持，Faithfulness 就高。

Hallucination 問的是："這個回答有沒有和提供的 context 相矛盾？" 更像是一個安全檢查，防止模型「腦補」出 context 裡沒有的東西。

簡單說：Faithfulness 是 RAG 的品質指標；Hallucination 是事實一致性的防護指標。兩個都量，但不要把它們當成同一件事。

### Retrieval 品質的三個指標怎麼分工

| 指標 | 在問什麼 | 如果低代表什麼 |
|------|--------|--------------|
| Contextual Precision | 相關的 chunk 有沒有排在前面？ | Ranking 邏輯有問題，模型看到最前面的 chunk 都是雜訊 |
| Contextual Recall | Retrieval 有沒有涵蓋回答所需的資訊？ | 重要資訊根本沒被召回，巧婦難為無米之炊 |
| Contextual Relevancy | 整批召回的 chunks 和問題有多相關？ | 召回太雜，context window 被填滿了無用資訊 |

如果你只能選一個 retrieval 指標，Contextual Recall 通常最有診斷價值：它告訴你「你需要的資訊，有沒有在 context 裡」。

---

## 做 Agent：工具對了不代表答案對了

Agent 的失敗往往不在最後的輸出，而在中間的某一步。這就是為什麼 Agent 評估需要 trace，不是只看最終輸出就夠。

### Tool Correctness vs. Argument Correctness

兩個指標分開量不同的東西：

*   **Tool Correctness**：選對工具了嗎？（呼叫 `search_flights` 而不是 `book_hotel`）
*   **Argument Correctness**：參數填對了嗎？（`origin: "NYC"` 而不是 `origin: "New York City"`）

兩個都要量。工具選對但參數格式不對，一樣 fail。實務上，Argument Correctness 的問題更常見，尤其在 tool schema 描述模糊的時候，模型容易用錯參數格式。

### Task Completion 為什麼需要 trace

Task Completion 要評估「agent 有沒有完成任務」，但只看最終輸出不夠——agent 說「已幫您完成訂位」，但中間的工具呼叫其實失敗了，你不看 trace 根本不知道。

這個指標需要完整的執行記錄（用 `@observe` decorator 追蹤），讓 judge 能看到 agent 每一步做了什麼，而不是只看它說了什麼。

### Step Efficiency——怎麼設閾值

Step Efficiency 量的是「有沒有走不必要的步驟」。這個指標比較特殊，因為什麼叫「不必要」本身就是業務判斷，不同任務有不同的合理步驟數。

實務做法：先建立 baseline（現有系統跑 50 個 case，記錄平均步驟數），然後用這個 baseline 設閾值，而不是從零定義一個絕對標準。

---

## 做多輪 Chatbot：記憶和角色是兩個不同的問題

多輪對話有兩類常見失敗：記不住說過的事，以及人格飄移。

*   **Knowledge Retention**："你之前說你叫 Alice，下一輪我問你名字，你答對了嗎？" 量的是 chatbot 有沒有正確記住對話中的事實。
*   **Role Adherence**："system prompt 說你是一個只回答財經問題的助理，用戶問你做菜，你有沒有拒絕？" 量的是有沒有維持設定的角色邊界。
*   **Conversation Completeness**：整個對話下來，用戶提出的需求有沒有被全部滿足？

這三個各自獨立，不要用 Conversation Completeness 代替前兩個——它只告訴你結果，不告訴你哪裡出了問題。

---

## 純 LLM 推理服務：G-Eval 和 ArenaEval 是主力

如果你的系統沒有 retrieval，沒有 tools，就是 prompt 進去、LLM 輸出來，那 RAG 五指標和 Agentic 指標大半都用不上。你需要的是能評估「輸出品質」的通用工具。

### G-Eval：用自然語言描述你的評估準則

G-Eval 讓你用自己的語言定義什麼叫「好的輸出」：

```python
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCaseParams

metric = GEval(
    name="Reasoning Quality",
    evaluation_params=[
        LLMTestCaseParams.INPUT,
        LLMTestCaseParams.ACTUAL_OUTPUT,
    ],
    criteria="評估推理過程是否邏輯清晰、結論是否有根據支撐",
    threshold=0.7,
)
```

這讓你不需要把評估準則硬編碼成規則，LLM judge 會根據你的 criteria 給出 score + reason。

**G-Eval 適合用在：**

*   評估準則是模糊的語意標準（清晰、有幫助、邏輯一致）
*   你需要知道為什麼分數低（reason 可以告訴你哪裡有問題）
*   快速驗證一個新版 prompt 的整體輸出品質

**什麼時候不適合用 G-Eval**

如果你的評估準則是明確的業務規則——「輸出一定要包含 X 欄位」「如果 input 含有 Y，output 必須拒絕」——那用 G-Eval 讓 LLM 自由裁量反而容易出現不一致。這種情況更適合用 DAG（Directed Acyclic Graph），把評估邏輯顯式地建成決策流，讓每一步都是確定性的。

### ArenaEval：不問分數，問誰更好

當你想知道「這個 prompt 改版有沒有進步」，最直觀的問題不是「新版分數是多少」，而是「新版和舊版對打，誰贏？」

這就是 ArenaEval 的設計邏輯：把新版和舊版的輸出丟進去做 pairwise 比較，拿到勝場數。

```python
from deepeval import compare
from deepeval.test_case import ArenaTestCase, Contestant, LLMTestCase
from deepeval.metrics import ArenaGEval, LLMTestCaseParams

metric = ArenaGEval(
    name="Reasoning Quality",
    evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT, LLMTestCaseParams.INPUT],
    criteria="哪個回答的推理過程更清晰、結論更有依據？",
)

win_counts = compare(test_cases=arena_cases, metric=metric)
# {"prompt_v1": 17, "prompt_v2": 33}
```

相對比較不需要定義絕對門檻，對 prompt iteration 的場景特別實用——你不需要說「0.75 算好」，只需要說「新版要贏過舊版超過 60% 的 case」。

---

## 指標全過了，為什麼系統還是爛？

### Test set 不代表真實分佈

你的 golden dataset 是你自己建的，你怎麼建，就會測什麼。如果所有 test case 都是「標準問法」，那評估通過了，遇到真實用戶的奇怪提問還是會壞。

解法是讓 Observability 工具餵回 Evaluation。在 Langfuse 或 AgentOps 裡，對生產環境中行為異常或值得關注的 trace 打標籤（例如 `add_to_eval`），再定期透過 SDK 把這些 trace 拉出來轉成 Golden 補進 test set。這樣 test set 就會跟著真實用戶行為一起進化，而不是永遠只測你一開始想到的 case。

**Observability → Evaluation 閉環**

```
Online

⬡ Production LLM 呼叫

↓

◈ Langfuse / AgentOps  
收 trace，打標籤 `add_to_eval`

↓

⇄ SDK 定期匯出標籤 traces  
轉換為 DeepEval Golden

↓

CI / Dev

◉ Golden dataset 更新  
edge case 持續補入

↓

▷ CI Eval 跑一遍  
G-Eval / ArenaEval 回歸測試

↓

✦ 修 prompt / 換模型  
部署新版本

閉環

↑
```

### 分數高但 reason 告訴你問題在哪

G-Eval 除了 score，還會給 reason。很多人只看分數，但 reason 往往更有價值——"雖然通過了，但推理步驟三跳過了關鍵假設"。養成看 reason 的習慣，特別是分數在閾值附近的 case。

### Agent decay：評估不是做一次就好

系統的指標今天通過，不代表三個月後還 OK。模型版本更新、tool API 悄悄改了 schema、用戶行為模式漂移，這些都可能讓評估結果悄悄下滑。把評估接進 CI，讓每次變更都跑一遍，而不是靠人記得「去測一下」。

---

## 結語

> "指標選得少但選得對，比全選更有診斷價值。知道自己系統的架構，找到對應的失敗點，只量那幾個——這樣拿到的數字才有地方可以接。"
