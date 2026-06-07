---
url: "https://warmwater.dev/blog/autoresearch-c-33x"
title: "不靠直覺，靠實驗：用 AutoResearch 找到 C++ 的 33x 優化空間"
date: 2026-04-17
category: Implement
source: warmwater.dev
---

[
← Implement ](/blog?tag=Implement)  Implement 
 
# 不靠直覺，靠實驗：用 AutoResearch 找到 C++ 的 33x 優化空間
 
 2026-04-17 · — views  
  
  
> 
**系列：C++ AI 推論 10 天學習筆記 — Day 3**

> 
「沒有寫過 C++，怎麼做效能優化？」

> 
用你最擅長的方式：**設計實驗，讓數字說話。**


## 為什麼要先量測


C++ 給了你很多可以拉的槓桿——但不是每個槓桿在每個場景都有效，而且效果大小往往不直覺。


幾個常見的優化方向：


- **減少複製次數**：每一次資料在記憶體間搬移都是時間成本。用指標傳遞代替複製、用 I/O Binding 讓 ONNX Runtime 直接讀寫你指定的記憶體位址、避免 CPU ↔ GPU 之間不必要的來回——這類優化針對的是「推論以外的開銷」。
- **資料結構與記憶體佈局**：連續的記憶體（`std::vector`）比分散的結構 cache 友善；預先分配（`reserve`）避免 runtime 的動態擴張；Pinned Memory（鎖頁記憶體）加速 CPU→GPU 的資料傳輸。
- **精度與量化**：FP16 的計算量是 FP32 的一半，記憶體頻寬需求也減半；INT8 量化再壓一倍。在 GPU 上，記憶體頻寬往往才是瓶頸，降精度直接衝擊吞吐。
- **並行與硬體利用**：多個推論請求用 CUDA Stream 並行執行；CPU 端用多執行緒做前處理；換用 GPU / Neural Engine 等硬體加速後端。


每個方向帶來的提升幅度，完全取決於你的模型和硬體組合。如果沒有可信的數字，就不知道該優先拉哪個槓桿，也不知道拉了之後有沒有效。


### 突發奇想：用 Agent 系統化跑實驗


我過去沒有寫過 C++，所以沒辦法靠直覺判斷哪個優化方向有效。但我做得到另一件事：**設計實驗。**


想法來自 Karpathy 的 AutoResearch 框架——核心概念一句話說完：AI agent 讀你的代碼，想辦法改進它，跑一次實驗看結果，有效就留、沒效就丟，然後重來。把這個邏輯搬到 C++ 效能優化上，關鍵是把代碼切成兩個區域：


- **Fixed Harness（不能動）**：計時、正確性驗證、指標輸出——這是裁判
- **Editable Kernel（agent 負責改）**：實際的演算法實作——這是選手


Agent 的循環很簡單：改 kernel → compile → 跑實驗 → 看指標 → latency 降了就 commit，沒降就 `git reset --hard`，然後根據指標推測下一步。


這裡有個關鍵：**指標要能診斷瓶頸，不只是報告結果**。光看 latency 只知道有沒有變好；`GFLOPS` 低代表 compute 沒被充分利用，`bandwidth_gb_s` 接近硬體上限代表記憶體頻寬是瓶頸——兩者加在一起，agent 才能推理出下一步該改什麼，而不是瞎猜。


跑完之後有一個讓我印象深刻的 finding——


### 記憶體存取順序：只改三個字母，15.8x


先看問題在哪。這是最直覺的 naive matmul：


```
for (int i = 0; i < n; ++i)
 for (int j = 0; j < n; ++j)
 for (int k = 0; k < n; ++k)
 C[i*n + j] += A[i*n + k] * B[k*n + j];  // 最內層讀 B

```


最內層 `k` 每次加 1，`B[k*n + j]` 的記憶體位址就跳 512 個 float（2KB）。512×512 的矩陣總共 1MB，遠超 L1 cache（32KB）。每次讀 B 幾乎都是 cache miss，要去 RAM 等幾百個 CPU cycle——大半時間花在等記憶體，不是在算數學。


把 `j` 和 `k` 的 loop 對調，只改這一件事：


```
for (int i = 0; i < n; ++i)
 for (int k = 0; k < n; ++k)
 for (int j = 0; j < n; ++j)
 C[i*n + j] += A[i*n + k] * B[k*n + j];  // k 固定，j 遞增 → 連續記憶體

```


現在最內層 j 遞增，`B[k*n + j]` 變成連續位址，CPU 預取一次就能用整行。計算量完全沒變。


同一個 512×512 矩陣乘法，agent 第一步就找到了：


`ijk` 和 `ikj` 的計算量完全相同，差在 B 矩陣的存取方式：`ijk` 逐欄讀取，每次都 cache miss；`ikj` 改成逐行，大量命中 cache。**15.8x，零演算法改動。** tiling 再把工作區塊縮到 32×32（約 12KB，剛好塞進 L1 cache），又多了一倍。


指標在這裡不只是報告結果，而是告訴 agent 下一步往哪看：


- **naive ijk → ikj**：1.71 GFLOPS 遠低於這顆 CPU 的理論算力——compute 明顯沒被充分利用，瓶頸在記憶體存取，不在演算法本身。agent 推測：改成連續存取。
- **ikj → tiling**：26.98 GFLOPS 進步明顯，方向對了；但 working set 縮到 L1 cache 還有空間。32×32 塊約 12KB，剛好塞進 L1 cache（32KB），理論上應該再推一步。agent 推測：加 tiling。
- **tiling 之後**：56.83 GFLOPS，接近 peak throughput，邊際回報開始遞減。實驗結束。


GFLOPS 低，往記憶體存取看；GFLOPS 接近硬體上限，才往演算法看。有了這兩個數字，agent 每一步都在推理，而不是瞎猜。這也是 benchmark 不能只報 latency 的原因——latency 只告訴你有沒有變好，GFLOPS 和 bandwidth 告訴你為什麼。


這就是 Day 2 「能少 copy 就少 copy」的下一層：不只是少 copy，還要讓存取是連續的、可以被 cache 預取的。C++ 讓你能精確控制這件事；Python 和 Go 基本上做不到。


這也帶出量測的第一個設計要求：**一定要 warmup**，因為第一次執行的 cache 是冷的，數字完全不代表穩定性能。


---


概念清楚了。來看計時怎麼實作：分段找瓶頸，或批量跑統計量測。


## 分段計時：RAII Timer


最簡單的計時方式，用 C++ 的 RAII 語意（離開 scope 自動執行析構函式）：


```
#include <chrono>
#include <string>
#include <cstdio>

class Timer {
 std::string name_;
 std::chrono::time_point<std::chrono::high_resolution_clock> start_;
public:
 Timer(const std::string& name) : name_(name) {
 start_ = std::chrono::high_resolution_clock::now();
 }
 ~Timer() {
 auto end = std::chrono::high_resolution_clock::now();
 auto ms = std::chrono::duration<double, std::milli>(end - start_).count();
 std::printf("[%s] %.3f ms\n", name_.c_str(), ms);
 }
};

```


使用方式：


```
{
 Timer t("preprocessing");
 preprocess();
}
// 離開 scope，Timer 析構，自動印出：[preprocessing] 2.341 ms

{
 Timer t("inference");
 run_model();
}
// [inference] 4.872 ms

```


這個 pattern 在 Go 裡沒有直接對應物（Go 的 defer 接近，但沒有 scope 析構）。Python 可以用 `with` 加上 `__exit__`。C++ 的 RAII 讓你不用手動記得結束計時。


---


## 為什麼要 Warmup


第一次執行發生的事：


- **Memory allocation**：第一次要向 OS 申請記憶體，之後 reuse
- **CPU cache miss**：資料第一次讀入時，cache 是冷的；之後留在 L2/L3 cache，速度差距可以到 10 倍以上
- **延遲初始化**：部分函式庫在第一次呼叫時才完成某些內部初始化


這不是哪個框架特有的問題，而是任何 C++ 系統的通性。**第 1 次的數字不代表穩定性能，只代表冷啟動成本。**


建議：**warmup 20 次，measure 100 次**，取 median 與 P99。


---


## 統計量測：Benchmark 函式


```
#include <chrono>
#include <vector>
#include <functional>
#include <numeric>
#include <algorithm>
#include <cstdio>

struct BenchmarkResult {
 double median_ms; // 中位數延遲（比平均更穩健，排除偶發的 spike）
 double min_ms; // 最佳情況（代表 cache 全熱、無干擾時的極限）
 double p99_ms; // P99 延遲（tail latency，線上服務的 SLA 依據）
 double qps; // 每秒請求數
};

BenchmarkResult run_benchmark(
 std::function<void()> fn,
 int warmup_runs = 20,
 int measure_runs = 100
) {
 // --- Warmup ---
 // 讓 memory allocation、CPU cache 都進入穩定狀態
 for (int i = 0; i < warmup_runs; ++i) fn();

 // --- Measure ---
 std::vector<double> latencies;
 latencies.reserve(measure_runs);

 for (int i = 0; i < measure_runs; ++i) {
 auto start = std::chrono::high_resolution_clock::now();
 fn();
 auto end = std::chrono::high_resolution_clock::now();
 latencies.push_back(
 std::chrono::duration<double, std::milli>(end - start).count()
 );
 }

 // --- 統計 ---
 std::sort(latencies.begin(), latencies.end());
 double median = latencies[latencies.size() / 2];
 double min = latencies[0];
 double p99 = latencies[static_cast<size_t>(latencies.size() * 0.99)];

 return {median, min, p99, 1000.0 / median};
}

```


使用範例：


```
// 把任何你想量的邏輯包成 lambda
auto result = run_benchmark([&]() {
 do_some_work();
}, 20, 100);

std::printf("median: %.2f ms | min: %.2f ms | P99: %.2f ms | QPS: %.1f\n",
 result.median_ms, result.min_ms, result.p99_ms, result.qps);

```


**如何解讀這四個數字：**


- **median**：穩定狀態的代表值，比 mean 更不受偶發 spike 干擾
- **min**：cache 全熱、OS 無干擾時的理論下限，代表這段 code 的物理極限
- **P99**：每 100 次有 1 次會超過這個值——線上服務的 tail latency 是這個，不是 median
- **median vs P99 差距大**：執行時間不穩定，可能有鎖競爭或 OS scheduling 干擾


---


## 幾個想像場景：工具怎麼幫你找到方向


有了 Timer 和 benchmark 函式，接下來要知道量什麼、怎麼解讀。幾個具體場景：


**場景 1：pipeline 分段計時，找出真正的瓶頸**


一個 embedding 請求從文字進來到向量出去，中間有多個階段。在沒有數字之前，你可能以為推論本身是瓶頸；量過才知道真相：


```
{ Timer t("tokenize"); tokenize(text, &input_ids);  }
{ Timer t("h2d"); copy_to_device(input_ids); }
{ Timer t("inference"); run_model(); }
{ Timer t("d2h"); copy_from_device(output); }
{ Timer t("normalize"); normalize(output); }

```


輸出可能是：


```
[tokenize]  2.1 ms
[h2d] 0.8 ms
[inference] 1.3 ms ← 以為最重要的，反而不是最大
[d2h] 0.2 ms
[normalize] 0.1 ms

```


瓶頸在 tokenize，不在 inference——這決定了接下來應該優化哪一段。


**場景 2：預分配 vs 動態分配**


高頻推論場景（每秒 500 次請求），每次請求都建一個新的 `std::vector` 接收結果：


```
// ❌ 每次 inference 都動態分配
auto result = run_benchmark([&]() {
 std::vector<float> output(384);  // 每次都 malloc + free
 run_model(output);
}, 20, 100);

// ✅ 預分配，每次 reuse
std::vector<float> output(384);
auto result = run_benchmark([&]() {
 run_model(output);  // 直接寫入，不分配
}, 20, 100);

```


P99 的差距通常比 median 更明顯——動態分配在 OS 記憶體壓力高時會偶發性地慢很多，這正是 tail latency 的來源。


**場景 3：GFLOPS 和 bandwidth 告訴你瓶頸在哪**


回到 matmul 的例子：naive ijk 只有 1.71 GFLOPS，CPU 的理論算力遠不止於此——這個數字代表 compute 完全沒被充分利用，原因在記憶體存取，不在演算法本身。如果看到 GFLOPS 低，先想記憶體；如果 GFLOPS 已經接近硬體上限，才去想演算法。


---


## 小結


工具備好了，概念也清楚了：


- **RAII Timer** 做分段計時，找到真正的瓶頸階段
- **run_benchmark** 做穩定量測，median 比較優化效果，P99 評估線上表現
- **GFLOPS + bandwidth** 診斷瓶頸是 compute 還是記憶體存取
- **一定要 warmup**，冷啟動數字不代表穩定性能


## 延伸閱讀


- [在 Claude Code 的年代，我為什麼還要學 C++？](/blog/claude-code-c) — 系列 Day 1：為什麼學 C++，學習路徑的設定
- [給 Python/Go 工程師的 C++ 語法地圖：推論篇](/blog/python-go-c) — 系列 Day 2：7 個需要懂的 C++ 語法概念
- [AI 自主研究實驗：讓 Agent 在你睡覺時跑 100 個實驗](/blog/ai-agent-100) — autoresearch 的另一個應用：ML 領域的自主實驗設計

  
  
 [ Implement ](/blog?tag=Implement) 
 

### 相關文章
[Implement

用 RPG 架構評估 SRE Agent：Kube Arena 設計紀錄

2026-05-28
](/blog/kube-arena)[
Harness Engineering

Self Escalate Agent：刻意設計成不完整的 AI

2026-05-09
](/blog/self-escalate-agent)[
Implement

把 ML 工程師的直覺，打包進 Agent

2026-04-04
](/blog/ml-agent)
