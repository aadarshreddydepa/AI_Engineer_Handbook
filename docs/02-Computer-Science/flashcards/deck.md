# Flashcards · Module 02 — Computer Science Foundations

[🏠 Module](../README.md) · [📚 Lessons](../weeks/README.md)

> Active-recall deck for the whole module. Answer **out loud before flipping**. Review on the [spaced-repetition schedule](../../../LEARNING_STRATEGY.md): same day, +1d, +3d, +7d, +16d, +35d. A failed card resets to interval 1.

---

## 02.1 · Hardware

**Q:** What's the single most important hardware fact for performance?
**A:** Computation is cheap; moving data is expensive — most optimization reduces data movement.

**Q:** Why are pure-Python numeric loops slow (hardware view)?
**A:** Interpretation + heap objects + dynamic dispatch + pointer chasing mean many instructions and cache misses per operation.

**Q:** Why do neural networks use GPUs?
**A:** They're huge parallel matrix multiplications, matching GPUs' thousands of throughput-oriented cores.

---

## 02.2 · Memory

**Q:** Stack vs heap?
**A:** Stack: fast, automatic (freed on return), LIFO, small, for call frames/locals. Heap: dynamic, larger, GC/manual, for objects/tensors.

**Q:** Why can you get CUDA OOM with "free" memory?
**A:** GPU memory fragmentation — no single contiguous block large enough for the tensor.

**Q:** What is cache locality and why does it matter?
**A:** Accessing contiguous data in order keeps cache lines full, making arrays/tensors far faster than pointer-chasing structures.

---

## 02.3 · Data Structures

**Q:** Hash table vs balanced BST — when each?
**A:** Hash table for O(1) unordered lookups; balanced BST when you also need sorted order or range queries (O(log n)).

**Q:** What does a heap give you, and a key AI use?
**A:** O(1) peek and O(log n) push/pop of the min/max; used for top-k retrieval and beam-search decoding.

**Q:** Why do arrays often beat linked lists in practice?
**A:** Contiguous layout gives cache locality; linked lists pointer-chase and cause cache misses, outweighing Big-O advantages.

---

## 02.4 · Algorithms

**Q:** What is dynamic programming?
**A:** Solving problems with overlapping subproblems by solving each once and caching (memoization) — e.g., turns O(2ⁿ) fib into O(n).

**Q:** BFS vs DFS — structures and uses?
**A:** BFS uses a queue and finds shortest paths (unweighted); DFS uses a stack/recursion for reachability, cycles, and topological order.

**Q:** Greedy decoding vs beam search?
**A:** Greedy picks the top token each step (myopic); beam search keeps top-k partial sequences (heap) to reduce greediness.

---

## 02.5 · Complexity

**Q:** O vs Ω vs Θ?
**A:** O = upper bound (worst case), Ω = lower bound (best case), Θ = tight bound (both match).

**Q:** What silently creates O(n²) in Python?
**A:** A hidden O(n) operation inside a loop over n (e.g., `x in list`, `insert(0)`, slicing).

**Q:** Why is self-attention's complexity significant?
**A:** It's O(n²) in sequence length, making long context expensive — driving efficient-attention research and LLM cost/latency.

---

## 02.6 · Operating Systems

**Q:** Process vs thread?
**A:** A process has isolated memory (parallel via separate GILs); threads share the process's memory (GIL-limited for CPU, need locks).

**Q:** How do you prevent deadlock in practice?
**A:** Acquire multiple locks in a consistent global order (breaks circular wait) and use lock timeouts.

**Q:** What does virtual memory provide, and what's an OOM kill?
**A:** Each process gets a private virtual address space mapped to RAM/disk; exceeding a memory limit triggers the OS killing the process (exit 137).

---

## 02.7 · Networking

**Q:** TCP vs UDP, and which do AI APIs use?
**A:** TCP = reliable, ordered, connection-based (used by HTTP/APIs); UDP = fast, best-effort. APIs use TCP because correctness matters.

**Q:** Which HTTP status codes should you retry?
**A:** 429 (rate limited) and 5xx (server errors) as transient; not other 4xx (permanent client errors).

**Q:** REST vs WebSocket vs gRPC?
**A:** REST = request/response (JSON); WebSocket = persistent bidirectional (real-time/streaming); gRPC = HTTP/2 + Protobuf for fast internal services.

---

## 02.8 · Concurrency

**Q:** Which model for CPU-bound vs I/O-bound?
**A:** CPU-bound → multiprocessing (or NumPy/GPU); I/O-bound → async (high scale) or threading (moderate).

**Q:** When is the GIL released?
**A:** During I/O waits and inside many C extensions (NumPy) — which is why threads/async help I/O and native math parallelizes.

**Q:** Why does `count += 1` race despite the GIL?
**A:** It's three bytecode steps (read/add/write) the scheduler can interrupt between; the GIL only guards a single op.

---

## 02.9 · Serialization

**Q:** Why is unpickling untrusted data dangerous?
**A:** Pickle can execute arbitrary code on load (via `__reduce__`) — a remote-code-execution vulnerability; use JSON/safetensors instead.

**Q:** How do you safely load YAML?
**A:** `yaml.safe_load()` (never `yaml.load()`), which restricts to basic data types and can't construct arbitrary objects.

**Q:** Protobuf vs JSON — key trade-off?
**A:** Protobuf is smaller/faster/typed (schema required, great for internal gRPC); JSON is readable/universal for public APIs.

---

## 02.10 · File Systems

**Q:** Why open a model file with `"rb"`?
**A:** It's binary — text mode would corrupt it via encoding/line-ending translation.

**Q:** How do you write a crash-safe checkpoint?
**A:** Write to a temp file, flush/fsync, then atomically rename it into place.

**Q:** What is path traversal and its fix?
**A:** Untrusted input like `../../secret` escaping the intended directory; validate/normalize paths and confine them to an allowed base.

---

## 02.11 · System Design

**Q:** Horizontal vs vertical scaling?
**A:** Vertical = bigger machine (ceiling + single point of failure); horizontal = more machines behind a load balancer (unlimited, fault-tolerant, needs statelessness).

**Q:** Why is statelessness key to scaling?
**A:** If instances hold no per-client state, any instance can serve any request — so you can add/remove/replace instances freely.

**Q:** Top AI caching wins?
**A:** Cache identical prompts (temp 0), embeddings, and retrieval results — replacing paid, slow model calls with free, instant hits.

---

## 02.12 · Debugging

**Q:** Where is the cause in a Python stack trace?
**A:** The last line gives the error type/message; the deepest frame in your own code is usually the culprit.

**Q:** What is the systematic debugging method?
**A:** Reproduce reliably → observe the actual behavior → hypothesize → test the smallest experiment → fix and add a regression test.

**Q:** Key move for debugging wrong AI output?
**A:** Isolate the layer — data, code, model, or integration — because each has a completely different fix.

---

> [!TIP]
> When you can answer every card across two spaced reviews, Module 02 is locked in. Persistent misses point to a lesson worth rereading.
