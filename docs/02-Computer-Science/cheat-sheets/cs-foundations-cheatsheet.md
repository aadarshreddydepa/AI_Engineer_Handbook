# Cheat Sheet · Module 02 — Computer Science Foundations

[🏠 Module](../README.md) · [📚 Lessons](../weeks/README.md)

> One-page reference for the whole module. Scan it; learn it in the [lessons](../weeks/README.md).

---

## Hardware & memory (02.1–02.2)

```text
HIERARCHY (fast→slow, small→big): registers→L1→L2→L3→RAM→SSD→HDD/network (each ~10×)
RULE: computation cheap · MOVING DATA expensive → cache locality, batching, keep data on GPU
CYCLE: fetch→decode→execute(ALU)→write-back · cache line ~64B → contiguous access fast
WHY PYTHON SLOW: interpret bytecode + dynamic objects + pointer-chasing → NumPy/PyTorch (C/CUDA)
GPU: 1000s parallel cores → matrix math = neural nets · LLM inference often MEMORY-BANDWIDTH bound
MEMORY: STACK(calls/locals, LIFO, fast, small→overflow) vs HEAP(dynamic objects/tensors, GC)
  fragmentation → CUDA OOM despite "free" · leak = unbounded refs → bound caches
  GC: refcount + cyclic + generational · cache locality: contiguous > pointer-chasing
```

## Data structures & algorithms & complexity (02.3–02.5)

```text
ARRAY/TENSOR: a[i] O(1), contiguous, cache-friendly · HASH(dict/set): O(1) lookup, unordered
BST(balanced): O(log n) sorted+range · HEAP: peek O(1)/push-pop O(log n) → TOP-K, beam search
TRIE: O(k) prefix → autocomplete/tokenization · GRAPH: adjacency list(sparse)/matrix(dense)
  → comp graphs, GNN, HNSW, agents · STACK(DFS/calls) QUEUE(BFS/pipelines, use deque)
SEARCH: linear O(n) / binary O(log n) SORTED · SORT: Timsort (stable, n log n)
DIVIDE&CONQUER → parallelism · DP: overlapping subproblems→memoize (Viterbi, edit dist)
GREEDY: local choice (greedy decoding) vs beam(heap) · BFS(queue,shortest) DFS(stack) · BACKTRACK: try/prune
BIG-O: growth vs n (drop constants) · O(1)<log<n<n log n<n²<2ⁿ · CLIFF: n log n→n²
  HIDDEN O(n) in loop (in list, insert(0), slice) = O(n²)! · attention = O(n²) in seq len
  O(upper/worst) Ω(lower/best) Θ(tight) · amortized (dyn array append O(1))
```

## OS, networking, concurrency (02.6–02.8)

```text
PROCESS(isolated mem, parallel, IPC=pickle) vs THREAD(shared mem, GIL-limited, needs locks)
SCHEDULER: time slices + context switch (thrashes cache) · async avoids OS switches
RACE: count+=1 NOT atomic → Lock(with lock:)/Queue/avoid shared state · DEADLOCK: fixed lock order + timeouts
VIRTUAL MEMORY: per-process space → page table → RAM/disk · page cache(fast re-read) · OOM kill(137) · mmap
NETWORK LAYERS: App(HTTP/gRPC)→Transport(TCP reliable/UDP fast, ports)→IP→Link
  DNS(name→IP) · HTTP methods+status(429=rate limit,5xx=server→retry;4xx=don't) · HTTPS=TLS(always)
  REST(json)·WebSocket(realtime)·gRPC(HTTP2+protobuf internal) · LOAD BALANCER + reverse proxy
CONCURRENCY: CPU-bound→multiprocessing/NumPy · I/O-bound→async(scale)/threads
  GIL(CPython): 1 thread runs bytecode; RELEASED on I/O & in C ext · "GIL=thread-safe" is a MYTH
```

## Serialization, files, system design, debugging (02.9–02.12)

```text
SERIALIZE: JSON(universal, safe, API default+validate w/ Pydantic) · YAML(config, safe_load ONLY)
  PICKLE(any Python obj — ⚠️ RCE on untrusted! → use safetensors/JSON) · MessagePack/Protobuf(binary, safe)
  GOLDEN RULE: never deserialize untrusted data with code-executing formats
FILES: tree of named bytes · perms(7=rwx..600 secrets) · symlink(atomic version swap) vs hard link
  binary "rb" (model/parquet) vs text encoding="utf-8" · compression(lossless data/models)
  storage: Parquet/sharded(sequential) · CHECKPOINTS: temp→fsync→atomic rename · path traversal
SYSTEM DESIGN: scalability/availability/reliability/fault-tolerance
  scale OUT(horizontal+LB) > up · STATELESS enables scaling(push state to DB/cache)
  design FOR failure(redundancy, health checks, graceful degradation) · CACHE everywhere
  AI cache wins: identical prompts, embeddings, retrieval → huge cost/latency savings
DEBUG: reproduce→observe→hypothesize→test ONE thing→fix+regression test
  stack trace: LAST line=cause, deepest YOUR frame=culprit · PROFILE don't guess (cProfile/tracemalloc)
  observability: logs+metrics(p95/p99!)+traces · AI: isolate layer(data/code/model/integration)
```

## The golden rules

```text
1. Moving data > computing it (optimize data movement).   6. Never deserialize untrusted data (pickle=RCE).
2. Match data structure to access pattern.                 7. Design stateless for horizontal scaling.
3. Avoid the O(n log n)→O(n²) cliff (no hidden O(n) loops). 8. Design FOR failure; cache aggressively.
4. CPU→parallel(processes), I/O→concurrent(async).         9. Debug systematically; profile, don't guess.
5. Shared mutable state needs locks (GIL ≠ safe).          10. Trust boundaries: validate all external input.
```
