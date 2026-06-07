---
url: "https://warmwater.dev/blog/agent-memory-06-k8s-sre"
title: "Memory 06：K8s SRE Agent 的記憶設計——真實場景的技術選型"
date: 2026-05-14
category: Source Code
source: warmwater.dev
---

「api-server OOMKilled 了，幫我看一下」

一個 K8s SRE Agent 收到這句話，要做的事情是：查 logs、看 describe pod、比對過去的 error pattern、找出上次是怎麼解的。

這個過程裡，有些資訊值得記下來，有些不值得，有些甚至記了反而有害。設計 K8s SRE Agent 的記憶，就是在解這個分類問題。

這篇用這個具體場景，把前五篇討論的 write design、search、storage、lifecycle 決策串起來。

* * *

## K8s 輸出有三種時效性，各自需要不同的記憶策略

K8s 環境裡的資訊，時效性差距極大：

| 時效性 | 資料類型 | 範例 |
|------|--------|------|
| 永久有效 | 架構決策、error pattern、操作手法 | "api-server OOMKilled 通常是 request limit 太低"、"rollout 用 restart 不用 delete" |
| 緩慢變化 | YAML manifest、cluster topology、service 名稱 | 已驗證可用的 deployment yaml、namespace 結構 |
| 瞬間過期 | pod status、logs、events | `kubectl get pods` 的輸出、10 分鐘前的 log |

這個分類直接決定記憶架構：**永久有效的要存，緩慢變化的按需存，瞬間過期的不存**。

一個常見錯誤是把「pod/api-server-xyz-abc123 是 Running」存進記憶。10 分鐘後這筆記憶就是錯的，但 agent 不知道，下次查詢還是會拿出來用。

**記憶存模式，不存狀態。**

```
❌  pod/api-server-xyz-abc123 是 Running（10 分鐘後就 wrong）
✅  api-server OOMKilled 通常是 request limit 太低（永遠有效）
✅  staging namespace rollout 用 kubectl rollout restart（可複用）
```

* * *

## 這個 Agent 需要兩種 Write Archetype

K8s SRE Agent 需要兩種不同的記憶寫入方式，因為它要記的東西性質不同。

**Pattern 和決策 → Agent Direct Write（Archetype C）**

當 agent 成功解決了一個問題，它應該把解法的「模式」直接寫進記憶：

```
mem_save(topic="oom_resolution", content="api-server OOMKilled 解法：memory limit 從 512Mi 調到 1Gi，通常就夠了")
```

這適合用 engram 的 latest-wins upsert：同一個問題的解法會演進，最新的比舊的更可信，直接覆蓋就好。

**可複用 YAML manifest → Verbatim Write**

已驗證可用的 YAML 必須原文儲存，不能讓 LLM 改寫：

```yaml
# 這份 deployment yaml 跑過 staging，驗證可用
# 存進 mempalace 的 verbatim chunk
apiVersion: apps/v1
kind: Deployment
spec:
  replicas: 3
  template:
    spec:
      containers:
        - name: api-server
          resources:
            limits:
              cpu: "500m"
              memory: "1Gi"
```

數字 `500m`、`1Gi`、`3` 必須原封不動。一旦讓 LLM 摘要，`1Gi` 可能變成「大概 1 GB」，`500m` 可能被省掉，`replicas: 3` 可能變成「幾個 replica」。這些誤差在 production 環境是真實的 incident。

* * *

## Search 需求：兩種不同的查詢

K8s SRE Agent 的搜尋需求也分兩類，對應不同的搜尋策略：

**keyword search 找 pattern**

「上次 api-server OOM 是怎麼解的？」——這是 keyword search，要找 `api-server` 和 `OOM` 這兩個詞同時出現的記憶。BM25 在這裡最直接。

**verbatim fetch 取 YAML**

「給我上次驗證過的 deployment yaml」——這是 verbatim retrieval，要找確切的 YAML，不是找「關於 deployment 的記憶」。語意搜尋在這裡反而干擾多。

這兩種需求對應到兩個不同的系統：

*   engram 的 FTS5 BM25 → 找 pattern 和決策
*   mempalace 的 verbatim chunk → 取 YAML 原文

不需要把兩個系統硬塞進一個 memory backend，根據查詢類型路由即可。

* * *

## Storage：為什麼是混搭而不是單一系統

儲存選擇根據記憶類型來決定：

| 記憶類型 | 儲存選擇 | 理由 |
|--------|--------|------|
| Pattern、決策、error 解法 | SQLite + FTS5（engram） | keyword 精確搜尋、single-user 夠用、零 server 依賴 |
| 驗證過的 YAML manifest | ChromaDB verbatim（mempalace） | 原文不被 LLM 改寫、可直接貼回用 |
| pod status、logs、events | 不存，on-demand `kubectl` fetch | 永遠落後真實狀態，存了有害 |

這個場景是 single-user（一個 SRE 工程師用一個 agent），不需要 PostgreSQL 或遠端 Vector DB。SQLite + 本機 ChromaDB 就夠，而且搬遷和 ops 都簡單。

需要注意的是：**不要把這個架構掛上 NFS 或 S3**。SQLite WAL 不支援 NFS，s3fs 的 atomic rename 不保證。single-user agent 用 EBS（ReadWriteOnce PVC）就好。

* * *

## Lifecycle：模式不過期，狀態不入庫

K8s SRE Agent 的 lifecycle 設計很清楚：

**Pattern 記憶不需要 time-based decay**

「api-server OOMKilled 通常是 request limit 太低」——這個知識三年後還是對的，不應該因為久沒用就衰退。engram 的 latest-wins upsert 剛好合適：有更好的解法就覆蓋，沒有就保留。

**YAML manifest 需要版本意識**

已驗證的 YAML 不會「過期」，但會因為 K8s API 版本更新而失效。這不是 time-based decay 能解的問題，需要 agent 在使用 YAML 前先確認版本相容性，或手動標記為 deprecated。

**當下狀態永遠不入庫**

任何 `kubectl get` 的輸出都不值得存進記憶。agent 在需要當下狀態時，應該直接呼叫 kubectl，不應該從記憶裡拿。記憶只存「下次遇到同樣情況，該怎麼做」的知識。

* * *

## 數字精度：SRE 場景的紅線

LLM extraction 對數字特別不可靠。在 K8s SRE 場景，這不只是品質問題，是安全問題。

```
原文 YAML：cpu: 500m, memory: 1Gi, replicas: 3, port: 8443
LLM extraction 可能變成：
  "CPU 大概半核"、"記憶體 1G 左右"、replicas 被省掉、port 沒有記錄
```

把錯誤的 resource limit 套回 deployment，輕則 pod 一直 OOMKilled，重則影響生產流量。

規則只有一條：**YAML 不走 LLM extraction pipeline，verbatim 進、verbatim 出。**

數字型的 fact（resource limit、replica count、port）如果需要結構化存，用 typed field：

```json
{
  "service": "api-server",
  "cpu_limit": "500m",
  "memory_limit": "1Gi",
  "replicas": 3
}
```

不是 `{ "fact": "api-server 用半核 CPU 和約 1G 記憶體" }`。

* * *

## 最終架構：三層記憶，各選最合適的工具

K8s SRE Agent — 三層記憶架構

| 記憶層 | 存什麼 | Write | Search | Storage | Lifecycle |
|------|------|-------|--------|---------|-----------|
| 長期知識 | error pattern 解法、操作決策 | Agent Direct Write latest-wins upsert | FTS5 BM25 keyword 精確搜尋 | SQLite + engram | 不 decay，有更好的 解法直接覆蓋 |
| 可複用物件 | 驗證過的 YAML manifest | Verbatim Write 原文不被 LLM 改寫 | Verbatim Fetch 不走語意搜尋 | 本機 ChromaDB | 版本棄用時 手動清理 |
| 當下狀態 | pod status、logs | 不存 | on-demand 直接 kubectl | — | — |

**這個架構沒有用任何一個「完整的 memory 系統」，而是針對不同記憶類型選了最合適的工具。**

沒有一個框架能完美解決所有記憶問題。write design、search、storage、lifecycle 的每一個決策，都是根據場景來的。K8s SRE Agent 需要的，不是最強的記憶系統，是最匹配這個場景的記憶設計。

* * *

> **結語**：設計 agent memory 的起點，是先搞清楚你的 agent 在什麼場景、記什麼、多久用一次——架構自然就從這裡長出來。
