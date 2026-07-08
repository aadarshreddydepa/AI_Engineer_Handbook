# Answers · Module 02 Quiz 01

[🏠 Module](../README.md) · [❓ Questions](quiz-01.md)

> Model answers with the *why*. If you got the gist but not the reasoning, reread the linked lesson.

---

### Part 1 — Hardware & Memory

**1.** Registers → L1 → L2 → L3 cache → RAM → SSD → HDD/network (each step ~10× slower and larger). The rule: **computation is cheap; moving data is expensive** — most optimization reduces data movement. → [02.1](../weeks/02.1-how-computers-work.md)

**2.** Each operation runs through the interpreter (bytecode + dynamic dispatch + heap objects + pointer chasing) = many instructions and cache misses per element. NumPy/PyTorch express bulk math as single C/CUDA operations over contiguous memory (releasing the GIL); GPUs run the parallel matrix math. → [02.1](../weeks/02.1-how-computers-work.md)

**3.** Stack: fast, automatic (freed on function return), LIFO, small, holds call frames/locals. Heap: dynamically allocated, larger, GC/manual lifetime, holds objects/tensors. → [02.2](../weeks/02.2-memory.md)

**4.** Fragmentation is free memory scattered in non-contiguous gaps. A large allocation (a tensor) can fail because no single contiguous block fits, even though total free memory is sufficient — the cause of CUDA OOM with "free" VRAM. → [02.2](../weeks/02.2-memory.md)

**5.** Cache locality: accessing contiguous data in order keeps cache lines (~64B) full. Arrays are contiguous (cache-friendly); linked lists pointer-chase, causing cache misses — so arrays often win despite equal/worse Big-O. → [02.2](../weeks/02.2-memory.md)

### Part 2 — Data Structures, Algorithms, Complexity

**6.** Hash table for O(1) unordered lookups; balanced BST when you also need sorted order or range queries (O(log n)). → [02.3](../weeks/02.3-data-structures.md)

**7.** A heap gives O(1) peek and O(log n) push/pop of the min/max — used for top-k retrieval and beam-search decoding. → [02.3](../weeks/02.3-data-structures.md)

**8.** A trie does prefix/string matching (autocomplete, tokenization) in O(k) where k is key length, independent of the number of keys. → [02.3](../weeks/02.3-data-structures.md)

**9.** DP solves problems with overlapping subproblems and optimal substructure by solving each subproblem once and caching the result (memoization/tabulation) — e.g., turning O(2ⁿ) fib into O(n). Memoization = top-down DP with a cache. → [02.4](../weeks/02.4-algorithms.md)

**10.** BFS uses a queue and explores level-by-level (finds shortest paths in unweighted graphs); DFS uses a stack/recursion and goes deep first (reachability, cycle detection, topological order). → [02.4](../weeks/02.4-algorithms.md)

**11.** Big-O describes how cost grows with input size n (dropping constants/lower terms). O = upper bound (worst case), Ω = lower bound (best case), Θ = tight bound (both match). → [02.5](../weeks/02.5-complexity.md)

**12.** A hidden O(n) operation inside a loop over n (e.g., `x in list`, `list.insert(0)`, slicing). It's dangerous because at n=1M, O(n²) is ~1 trillion operations vs ~20M for O(n log n) — the difference between instant and never-finishing. → [02.5](../weeks/02.5-complexity.md)

### Part 3 — OS, Networking, Concurrency

**13.** A process has isolated memory (heavy, true parallelism via separate GILs, communicates via IPC/serialization); threads share the process's memory (light, fast comms but need locks, GIL-limited for CPU work). → [02.6](../weeks/02.6-operating-systems.md)

**14.** A race condition is a bug where the result depends on unpredictable thread timing on shared mutable state (e.g., `count += 1` is read/add/write). Prevent it with synchronization (locks) or by avoiding shared mutable state (queues, isolation). → [02.6](../weeks/02.6-operating-systems.md)

**15.** Acquire multiple locks in a consistent global order (breaks the circular-wait condition) and use lock timeouts so a stuck acquire fails instead of hanging. → [02.6](../weeks/02.6-operating-systems.md)

**16.** Virtual memory gives each process a private virtual address space mapped to physical RAM (or disk via paging), providing isolation and the illusion of contiguous memory. An OOM kill is the OS terminating a process that exceeds its memory limit (Linux exit code 137). → [02.6](../weeks/02.6-operating-systems.md)

**17.** TCP = reliable, ordered, connection-based; UDP = fast, best-effort. AI APIs use TCP (via HTTP) because correctness matters — you can't tolerate a dropped chunk of a response. → [02.7](../weeks/02.7-networking.md)

**18.** Retry 429 (rate limited) and 5xx (server errors) as transient; do not retry other 4xx (permanent client errors like bad request/auth). → [02.7](../weeks/02.7-networking.md)

**19.** REST = request/response, usually JSON, universal (public APIs). WebSocket = persistent bidirectional connection (real-time/streaming). gRPC = HTTP/2 + Protobuf, fast and typed (high-performance internal services). → [02.7](../weeks/02.7-networking.md)

**20.** The GIL lets only one thread execute Python bytecode at a time in CPython. It's **held** during CPU-bound Python execution (so threads don't parallelize compute) and **released** during I/O waits and inside many C extensions (NumPy) — so threads/async help I/O and native math parallelizes. → [02.8](../weeks/02.8-concurrency.md)

### Part 4 — Serialization, Files, System Design, Debugging

**21.** Pickle can execute arbitrary code when loading (via `__reduce__`), so a malicious pickle = remote code execution — a real risk with untrusted model files. Use data-only formats (JSON/MessagePack/Protobuf) and `safetensors` for tensors; validate deserialized data. → [02.9](../weeks/02.9-serialization.md)

**22.** Use `yaml.safe_load()` (never `yaml.load()`). `safe_load` restricts to basic data types; plain `load` can construct arbitrary Python objects — a code-execution risk. → [02.9](../weeks/02.9-serialization.md)

**23.** Write to a temporary file, flush/`fsync` it, then **atomically rename** it into place (rename is atomic on most filesystems) — so a crash mid-write can't corrupt the existing checkpoint. → [02.10](../weeks/02.10-file-systems.md)

**24.** If a service holds no per-client state, any instance can serve any request — so a load balancer can distribute freely and you can add/remove/replace instances (scaling + fault tolerance). State is pushed to shared stores (DB/cache/object storage). → [02.11](../weeks/02.11-system-design-basics.md)

**25.** Cache identical prompts (deterministic at temperature 0), embeddings (deterministic, re-embedding is wasteful), and retrieval results — replacing paid, ~second-long model calls with free, instant cache hits. → [02.11](../weeks/02.11-system-design-basics.md)

**26.** Read the stack trace's **last line** for the error type/message, then find the deepest frame in your own code (the usual culprit). The systematic method: reproduce reliably → observe the actual behavior → hypothesize a cause → test the smallest experiment → fix and add a regression test. → [02.12](../weeks/02.12-debugging.md)

---

> [!TIP]
> Turn every missed question into a flashcard and schedule it for tomorrow — missed items are your highest-value study material.
