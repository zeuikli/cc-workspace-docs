---
url: "https://warmwater.dev/blog/python-go-c"
title: "給 Python/Go 工程師的 C++ 語法地圖：推論篇"
date: 2026-04-16
category: Tutorial
source: warmwater.dev
---

[
← Tutorial ](/blog?tag=Tutorial)  Tutorial 
 
# 給 Python/Go 工程師的 C++ 語法地圖：推論篇
 
 2026-04-16 · — views  
  
  
> 
**系列：C++ AI 推論 10 天學習筆記 — Day 2**

> 
「C++ 有那麼多東西，我要學哪些才能寫 inference code？」

> 
答案：**7 件事。其他先跳過。**


---


## 為什麼是 7 件事？


ONNX Runtime 的 C++ API 不是從零開始設計的，它是給已經懂 C++ 的人用的。但是從 Python/Go 工程師的角度，讀懂它的 sample code 只需要掌握 7 個概念。


我刻意跳過的東西：template metaprogramming、繼承、operator overload、move semantics、虛函式、模板特化……這些學完才能寫優雅的 C++，但不是讀懂 ONNX Runtime 的必要條件。


本篇的目標：看到 ONNX Runtime 的 C++ code 時不會一頭霧水，能夠寫出第一個推論程式。


---


## 先說一件小事：`Ort::` 和 `std::` 是什麼


整份 code 裡到處是 `Ort::Session`、`std::vector`——`::` 就是 C++ 的 namespace 分隔符，等同 Python 的 `module.Class` 或 Go 的 `pkg.Type`。`std` 是標準函式庫，`Ort` 是 ONNX Runtime 的 namespace。看到 `Ort::` 開頭的東西就知道是 ONNX Runtime 提供的。


---


## 概念 1：指標與參考（`*` 和 `&`）


ONNX Runtime 的 API 到處是指標，這是逃不掉的第一關。


### 指標是什麼


指標儲存的是**記憶體位址**，不是值本身。


```
int x = 42;
int* p = &x; // & 取位址，p 存的是 x 的位址（例如 0x7ffee4b）

std::cout << x; // 42（值）
std::cout << p; // 0x7ffee4b（位址本身）
std::cout << *p; // 42（解引用：透過位址取值）

*p = 100; // 透過指標修改 x
std::cout << x; // 100

```


**Go 工程師的對照**：


```
x := 42
p := &x
*p = 100  // Go 和 C++ 的指標語法幾乎相同

```


主要差異：Go 指標不能做算術（`p++`），C++ 可以，也因此危險一些。


### 參考是什麼


參考是「別名」，必須在宣告時綁定，之後不能改指向。在函式參數常見：


```
// 傳值（複製）：修改 x 不影響外部
void by_value(int x) { x = 100; }

// 傳參考（別名）：直接修改外部的變數
void by_reference(int& x) { x = 100; }

// 傳 const 參考（唯讀、不複製）：效能最好的唯讀方式
void by_const_ref(const std::string& s) { std::cout << s; }

int a = 42;
by_value(a); // a 還是 42
by_reference(a); // a 變成 100

```


**為什麼 ONNX Runtime 程式碼到處是 `&`？**
因為傳大型物件（例如 `std::vector`、`std::string`）時，用 `const&` 可以避免複製，同時保持唯讀。


### 三種函式參數的選擇規則


```
傳的東西很小（int, float, bool）→ by value（直接複製）
傳的東西很大，需要修改 → by reference（int& x）
傳的東西很大，只需讀取 → by const reference（const std::vector<float>& v）

```


> 
**為什麼在推論程式碼裡這件事特別重要？**

> 
Day 1 的 latency breakdown 顯示推論本身只佔 30%，資料移動和處理佔了 70%。同樣的邏輯適用於 C++ 函式呼叫：每一次不必要的記憶體複製，都是真實的時間開銷。

> 
在追求低 latency 的推論程式碼裡，**「能少 copy 就少 copy」是核心原則**。`const&` 是讓函式「拿到資料但不複製」的標準做法；而 ONNX Runtime 要求傳 raw pointer（`.data()`）而不是接受整個 vector，也是同樣的設計哲學：**API 刻意拒絕幫你隱式複製資料**，讓你清楚知道「這裡沒有複製發生」。


---


## 概念 2：`std::vector<float>`


推論的 input 和 output 都是浮點數陣列。`std::vector` 就是 C++ 的動態陣列，等同 Python 的 `list`。


```
// Python
input_data = [0.5, 0.3, 0.7]
output = model.run(input_data)

// C++
std::vector<float> input_data = {0.5f, 0.3f, 0.7f};
auto output = session.Run(...);

```


常用操作：


```
std::vector<float> v = {1.0f, 2.0f, 3.0f};

v.size(); // 3（Python 的 len(v)）
v.push_back(4.0f);  // 尾端新增
v.data(); // 回傳 raw pointer（ONNX Runtime API 需要）
v[0]; // 存取（不做邊界檢查）
v.at(0); // 存取（有邊界檢查，會 throw）

// 預分配（inference 前的效能優化）
v.reserve(512); // 預留空間，不改變 size
v.resize(512); // 直接設定大小（並填 0）

// Range-based for（等同 Python for x in v）
for (const auto& x : v) {
 std::cout << x << "\n";
}

```


**在 ONNX Runtime 裡最重要的一行**：


```
// CreateTensor 需要 raw pointer，用 .data() 取得
Ort::Value::CreateTensor<float>(mem_info, v.data(), v.size(), shape.data(), shape.size())
// ^^^^^^^
// raw pointer，指向 vector 內部的陣列

```


---


## 概念 3：`auto` 和 Range-for


`auto` 讓編譯器自動推導型別，不是 Python 的 dynamic typing：


```
# Python：runtime 決定型別，可以隨時改
x = 42
x = "hello" # 完全合法

```


```
// C++：編譯期決定型別，之後固定
auto x = 42; // int，永遠是 int
auto pi = 3.14; // double
auto name = std::string("Alice");

// 用在 iterator（避免寫超長型別名稱）
auto it = my_map.find("key");  // 型別是 std::unordered_map<...>::iterator

```


Range-based for（讀 ONNX Runtime 時會一直看到）：


```
std::vector<std::string> names = {"input_ids", "attention_mask"};

// 舊式（繁瑣）
for (int i = 0; i < names.size(); ++i) {
 std::cout << names[i];
}

// 現代（推薦）
for (const auto& name : names) {
 std::cout << name;
}

```


---


## 概念 4：`std::unique_ptr`


ONNX Runtime 的物件（`Env`、`Session`）都用 `unique_ptr` 包裝，必須懂。


先說問題：C++ 有 `new` 和 `delete`，忘記 `delete` 就是 memory leak。


```
// ❌ 舊做法（容易忘記 delete）
OrtSession* session = new OrtSession(...);
// ... 用 ...
delete session;  // 如果中間 throw exception，這行永遠不會跑到

```


`unique_ptr` 是解法：物件離開 scope 時自動 delete。


```
// ✅ 現代做法
auto env = std::make_unique<Ort::Env>(ORT_LOGGING_LEVEL_WARNING, "test");
// 不需要 delete！env 離開 scope 時自動釋放

// 如果需要 raw pointer（傳給 C API 時）
Ort::Env* raw_ptr = env.get();

// unique_ptr 的「獨占」語義：不能複製，只能移動
auto env2 = env; // ❌ 編譯錯誤
auto env2 = std::move(env); // ✅ 移動所有權（env 變成 null）

```


**ONNX Runtime 的物件通常這樣管理**：


```
class TextEmbedder {
 Ort::Env env_;
 Ort::Session session_; // Session 包著 model
 Ort::SessionOptions opts_;

public:
 TextEmbedder(const std::string& model_path)
 : env_(ORT_LOGGING_LEVEL_WARNING, "Embedder"),
 session_(nullptr) // 先初始化為 null
 {
 opts_.SetIntraOpNumThreads(4);
 session_ = Ort::Session(env_, model_path.c_str(), opts_);
 }
 // 析構子自動清理，不需要手動 delete
};

```


---


## 概念 5：Lambda


`std::sort` 和其他 STL algorithm 要傳比較函式，這時候用 lambda。讀 ONNX Runtime 的 sample code 時也偶爾會看到。


```
# Python lambda
sorted_items = sorted(items, key=lambda x: x.score, reverse=True)

```


```
// C++ lambda：[捕獲列表](參數) { 函式本體 }
std::vector<int> v = {3, 1, 4, 1, 5, 9};

// 降序排列
std::sort(v.begin(), v.end(), [](int a, int b) { return a > b; });

// 捕獲外部變數
float threshold = 0.5f;
auto above_threshold = std::count_if(scores.begin(), scores.end(),
 [threshold](float s) { return s > threshold; });  // 捕獲 threshold（by value）

// 捕獲 reference（修改外部變數）
int count = 0;
std::for_each(v.begin(), v.end(), [&count](int x) {
 if (x > 3) ++count; // 修改外部的 count
});

```


**在 ONNX Runtime 裡最常見的 lambda 場景**：取推論結果的 Top-K


```
// 依信心度降序排序，取前 5 名
float* output_data = output_tensors[0].GetTensorMutableData<float>();
int num_classes = 1000;

std::vector<std::pair<float, int>> scores;
for (int i = 0; i < num_classes; ++i)
 scores.push_back({output_data[i], i});

std::sort(scores.begin(), scores.end(),
 [](const auto& a, const auto& b) { return a.first > b.first; });  // lambda 比較函式

// scores[0] 是最高信心度的 class

```


---


## 概念 6：try-catch


ONNX Runtime 遇到錯誤不是回傳 error code，而是直接 **throw exception**。model path 錯、input shape 不符、EP 初始化失敗——全都會 throw。沒有 try-catch 的話程式直接 crash，錯誤訊息幾乎看不懂。


```
# Python 對照
try:
 session = ort.InferenceSession("model.onnx")
except Exception as e:
 print(f"Error: {e}")

```


```
// C++：catch Ort::Exception（ONNX Runtime 專屬的例外型別）
try {
 Ort::Session session(env, "model.onnx", opts);
 // ... 執行推論 ...
} catch (const Ort::Exception& e) {
 std::cerr << "ONNX Runtime error: " << e.what() << "\n";
 return 1;
} catch (const std::exception& e) {
 // 其他 C++ 標準例外
 std::cerr << "Error: " << e.what() << "\n";
 return 1;
}

```


**兩層 catch 的原因**：`Ort::Exception` 繼承自 `std::exception`，第一層抓 ONNX Runtime 的錯誤，第二層兜底其他標準例外。`.what()` 回傳錯誤訊息字串，等同 Python 的 `str(e)`。


---


## 概念 7：Template 使用語法


ONNX Runtime code 裡這個語法到處出現：


```
Ort::Value::CreateTensor<float>(...)
output_tensors[0].GetTensorMutableData<float>()

```


`<float>` 是在告訴編譯器「我要 **float 版本** 的這個函式」。Template 是 C++ 的泛型機制，讓同一個函式可以處理不同型別。你**不需要會寫 template**，只需要知道：**`<T>` 的地方填你的資料型別**。


```
// float tensor（一般 embedding 輸出）
auto tensor_f = Ort::Value::CreateTensor<float>(mem_info, data_f.data(), ...);

// int64_t tensor（token ids、attention mask）
auto tensor_i = Ort::Value::CreateTensor<int64_t>(mem_info, data_i.data(), ...);

// 取出資料也一樣
float* output_f = tensor_f.GetTensorMutableData<float>();
int64_t* output_i = tensor_i.GetTensorMutableData<int64_t>();

```


ONNX Runtime 推論常用的型別：


| 型別 | 用途 |
| --- | --- |
| float | 一般推論輸入 / embedding 輸出 |
| int64_t | token ids、attention mask、position ids |
| uint8_t | INT8 量化模型的 tensor |


---


## 7 個概念的對照表


| C++ 概念 | Python 等效 | 在推論 code 裡的用途 |
| --- | --- | --- |
| int*（指標） | id() + 手動 deref | ONNX API 到處要 raw pointer |
| const std::string& s（參考） | 傳 string（Python 自動 ref） | 避免複製大型物件 |
| std::vector`<float>` | list[float] | 存 input/output tensor 資料 |
| auto + range-for | 變數型別自動、for x in v | 讓 code 可讀 |
| unique_ptr | — （Python GC 自動管） | RAII：物件生命週期管理 |
| Lambda [&](x){ ... } | lambda x: ... | sort、filter、callback |
| try-catch | try/except | 攔截 ONNX Runtime throw 的錯誤 |
| CreateTensor`<float>` | — （Python 無需指定） | 告訴編譯器要哪種型別的版本 |


---


## 一個完整的最小範例


把這 7 個概念組合起來，下面是一個能跑的最小 C++ 推論骨架：


```
#include <onnxruntime/core/session/onnxruntime_cxx_api.h>
#include <vector>
#include <string>
#include <memory>

int main() {
 // 概念 4：RAII，不需要手動 delete
 Ort::Env env(ORT_LOGGING_LEVEL_WARNING, "minimal");
 Ort::SessionOptions opts;
 opts.SetGraphOptimizationLevel(GraphOptimizationLevel::ORT_ENABLE_ALL);

 // 概念 6：try-catch 攔截 ONNX Runtime 的錯誤
 try {
 Ort::Session session(env, "model.onnx", opts);

 // 概念 2：vector 存 input 資料
 std::vector<float> input_data(128, 0.5f);  // 128 個值，全填 0.5
 std::vector<int64_t> shape = {1, 128}; // batch=1, seq_len=128

 Ort::MemoryInfo mem_info = Ort::MemoryInfo::CreateCpu(OrtArenaAllocator, OrtMemTypeDefault);

 // 概念 1 + 7：.data() 取得 raw pointer；<float> 指定 tensor 型別
 Ort::Value input_tensor = Ort::Value::CreateTensor<float>(
 mem_info,
 input_data.data(), // raw pointer
 input_data.size(),
 shape.data(),
 shape.size()
 );

 // 概念 3：auto 推導回傳型別
 const char* input_names[]  = {"input"};
 const char* output_names[] = {"output"};

 auto output_tensors = session.Run(
 Ort::RunOptions{nullptr},
 input_names,  &input_tensor, 1,
 output_names, 1
 );

 // 概念 3 + 7：range-for 遍歷結果；<float> 指定取出型別
 float* output = output_tensors[0].GetTensorMutableData<float>();
 auto out_shape = output_tensors[0].GetTensorTypeAndShapeInfo().GetShape();

 for (int64_t i = 0; i < out_shape[1]; ++i) {
 if (i < 5) std::printf("output[%ld] = %.4f\n", i, output[i]);
 }

 } catch (const Ort::Exception& e) {
 std::cerr << "ONNX Runtime error: " << e.what() << "\n";
 return 1;
 } catch (const std::exception& e) {
 std::cerr << "Error: " << e.what() << "\n";
 return 1;
 }

 return 0;
}

```


---


## Takeaway：C++ 為什麼快？


學完這 7 個概念之後，有一個問題值得想清楚：**C++ 到底是因為什麼比 Python 快？**


答案不是單一因素，而是三層疊加的優勢：


**第一層：編譯成機器碼（最大的差距）**


Python 是直譯語言，每行 code 執行前都要經過 CPython interpreter 翻譯。C++ 直接編譯成 CPU 可以執行的機器碼，中間沒有翻譯層。這是純計算速度差距最大的來源。Go 也是編譯語言，所以 Go 和 C++ 在這點上差距不大。


**第二層：物件沒有記憶體開銷**


Python 的每個物件——哪怕是一個 `int`——都帶著 reference count、型別指標等 metadata，大約 28 bytes。一個裝了 100 萬個 float 的 Python list，實際上存的是 100 萬個「指向 float 物件的指標」，每個 float 物件還各自帶 header。


C++ 的 `std::vector<float>` 就是 100 萬個連續的 4-byte float，沒有任何 metadata 開銷。這不只是記憶體省了，更重要的是 **cache 友善**——CPU 可以一次預取一大塊連續記憶體，比追指標快很多。


值得一提的是，**NumPy 其實已經解決了這一層的問題**：NumPy array 的記憶體佈局和 `std::vector<float>` 幾乎相同，都是連續的 raw float，這也是 NumPy 比 Python list 快的核心原因。（以前只知道「做數值計算要用 NumPy」，放在這裡一起看，突然覺得以前用 NumPy 其實是在往 C++ 的方向靠近，只是沒意識到。）但從 Python 把 NumPy array 傳給 ONNX Runtime，仍然存在 Python/C++ 的邊界成本（boundary crossing 與潛在的記憶體複製）。C++ 直接在同一個 process 裡操作，完全消除這個邊界。


**第三層：直接控制硬體（Go 也做不到）**


這是 C++ 真正的獨門優勢：


- **SIMD 指令**（AVX2、NEON）：一個 CPU 指令同時處理 8 個 float
- **直接寫 CUDA kernel**：從 GPU 的 warp 層級控制執行邏輯
- **Zero-copy**：傳指標而不是複製資料——這正是 ONNX Runtime 要你傳 `.data()` 的原因


```
Python 慢的原因 誰解決了它
├── interpreter 翻譯層 →  C++ 和 Go 都解決
├── 物件 metadata 開銷 →  C++ 解決；Go 部分解決
├── GIL：只能單執行緒跑 →  C++ 和 Go 都沒有 GIL
└── 無法控制硬體 →  只有 C++ 可以（SIMD、CUDA kernel）

```


Go 和 C++ 的真正差距在最後一點。在 AI 推論的 hot path（矩陣乘法、attention），精細控制硬體的能力是決定性的——這也是為什麼 llama.cpp、Flash Attention、TensorRT 的核心全是 C++，而不是 Go。


## 延伸閱讀


- [在 Claude Code 的年代，我為什麼還要學 C++？](/blog/claude-code-c) — 系列 Day 1：為什麼選 C++，以及學習目標的設定
- [不靠直覺，靠實驗：用 AutoResearch 找到 C++ 的 33x 優化空間](/blog/autoresearch-c-33x) — 系列 Day 3：語法學完，用 AutoResearch 實際跑出優化結果
- [Python 資料結構深度解析：不只是背複雜度，而是知道什麼時候該用哪一個](/blog/python) — 跨語言視角：Python 的資料結構選型邏輯，對比 C++ 的記憶體控制思維

  
  
 [ Tutorial ](/blog?tag=Tutorial) 
 

### 相關文章
[Tutorial

第一個 Claude Skill：用 skill-creator 打包可重用工作流程

2026-05-25
](/blog/create-your-own-claude-skill)[
Tutorial

Claude Code 五個組件的觸發邏輯，以及為什麼 Hooks 是最被低估的那一個

2026-05-21
](/blog/claude-code-hooks-guide)[
Tutorial

為什麼你的 Claude Code 用起來跟別人不一樣？

2026-05-14
](/blog/claude-code-commands-beginner)
