# Exercises · Module 02 — Computer Science Foundations

[🏠 Module](../README.md) · [📚 Lessons](../weeks/README.md)

> A structured set spanning all 12 concept lessons — conceptual, coding, debugging, and architecture — with a deliberate difficulty ramp per the [exercise standards](../../../standards/exercise-standards.md). Do these in your study repo; commit your solutions.

**Difficulty:** ⭐ warm-up · ⭐⭐ practice · ⭐⭐⭐ challenge · ⭐⭐⭐⭐ stretch. **Types:** 💭 Conceptual · 💻 Coding · 🐞 Debug · 🏛️ Architecture.

---

## 02.1 · Hardware
- [ ] **⭐ 💭** Draw the memory hierarchy with approximate latencies; explain a cache miss.
- [ ] **⭐⭐ 💻** Benchmark summing a Python list vs a NumPy array (10M floats); explain the gap.
- [ ] **⭐⭐ 💻** Time sequential vs random array access on a large array; relate to cache locality.

## 02.2 · Memory
- [ ] **⭐ 💭** Diagram a call chain's stack frames; identify what's on the heap.
- [ ] **⭐⭐ 💻** Trigger a `RecursionError`; rewrite the recursion iteratively with an explicit stack.
- [ ] **⭐⭐ 🐞** Simulate a leak (growing global cache); find it with `tracemalloc`; fix with a bounded cache.

## 02.3 · Data Structures
- [ ] **⭐ 💭** For 6 scenarios, pick the best structure and justify via access pattern.
- [ ] **⭐⭐ 💻** Use `heapq` for top-k of a stream in O(n log k); compare to sorting.
- [ ] **⭐⭐⭐ 💻** Implement a hash map from scratch (buckets + chaining + resize).
- [ ] **⭐⭐⭐ 💻** Build a trie with insert + prefix query (→ Project 1).

## 02.4 · Algorithms
- [ ] **⭐ 💻** Implement binary search; find/fix an off-by-one bug in a given version.
- [ ] **⭐⭐ 💻** Solve a DP problem (edit distance / coin change) with memoization; time vs naive.
- [ ] **⭐⭐ 💻** Implement iterative BFS and DFS on an adjacency list; find a shortest path (→ Project 2).
- [ ] **⭐⭐⭐ 💻** Solve N-queens (or permutations) with backtracking + pruning.

## 02.5 · Complexity
- [ ] **⭐ 💭** Give time & space complexity of 6 short functions; justify.
- [ ] **⭐⭐ 🐞** Find a hidden O(n²) and fix it to O(n); measure at n=100k.
- [ ] **⭐⭐ 💻** Empirically confirm complexity: time a function at n=1k/10k/100k; match the growth to its Big-O.

## 02.6 · Operating Systems
- [ ] **⭐ 💭** For three workloads, choose threads/processes/async and justify.
- [ ] **⭐⭐ 💻** Reproduce a race condition (two threads, shared counter); fix with a lock.
- [ ] **⭐⭐⭐ 💻** Construct a deadlock (opposite lock orders); fix by ordering locks (→ Project 3).
- [ ] **⭐⭐ 🐞** Simulate an OOM under a low limit; observe the kill; explain exit code 137.

## 02.7 · Networking
- [ ] **⭐ 💭** Trace an API call end-to-end (DNS→TCP→TLS→HTTP); label latency/failure points.
- [ ] **⭐⭐ 💻** Use `curl -v` + Python to inspect headers/status/timing of a public API.
- [ ] **⭐⭐ 💻** Build a client that retries 429/5xx with backoff and reuses a connection.

## 02.8 · Concurrency
- [ ] **⭐ 💭** For six workloads, pick threading/multiprocessing/async and justify.
- [ ] **⭐⭐ 💻** Compare timing: 50 API calls sequential vs async `gather`; a CPU task threads vs processes.
- [ ] **⭐⭐⭐ 💻** Build a producer/consumer with `queue.Queue` and multiple workers; prove no lost items.

## 02.9 · Serialization
- [ ] **⭐ 💻** Serialize an object with JSON and MessagePack; compare sizes.
- [ ] **⭐⭐ 💻** Validate LLM-style JSON with a Pydantic model; handle a malformed case.
- [ ] **⭐⭐⭐ 🐞** (Sandbox) Demonstrate the untrusted-pickle code-execution risk; write a note on safe alternatives.

## 02.10 · File Systems
- [ ] **⭐ 💭** Decode 5 permission strings/octals; state who can do what.
- [ ] **⭐⭐ 💻** Trigger a `UnicodeDecodeError`; fix with UTF-8. Read a binary file in text mode and observe corruption.
- [ ] **⭐⭐ 💻** Implement an atomic write (temp→rename); prove a simulated crash leaves the original intact.
- [ ] **⭐⭐⭐ 🐞** Write a "safe open" rejecting path traversal outside a base directory.

## 02.11 · System Design
- [ ] **⭐ 💭** Classify five failures as availability/reliability/scalability/fault-tolerance.
- [ ] **⭐⭐ 🏛️** Make a given stateful service stateless; identify where state moves.
- [ ] **⭐⭐ 💻** Add a caching layer (TTL) before a simulated "model call"; measure hit-rate & latency savings.
- [ ] **⭐⭐⭐ 🏛️** Draw a fault-tolerant, horizontally-scaled AI service; annotate the four properties.

## 02.12 · Debugging
- [ ] **⭐ 💭** For three stack traces, identify the error, culprit line, and likely cause.
- [ ] **⭐⭐ 🐞** Reproduce, hypothesize, and fix a buggy function; document each step.
- [ ] **⭐⭐ 💻** Profile a slow script; fix the hotspot; report before/after numbers.
- [ ] **⭐⭐⭐ 🐞** Given an AI pipeline with wrong output, isolate whether it's data/code/model.

## Projects
- [ ] Build **Project 4 (LRU Cache)** at minimum — the classic interview + real infra.
- [ ] Build one system project (**P5 In-memory Cache**, **P6 URL Shortener**, or **P7 HTTP Server**).

---

## Completion criteria

- [ ] Every ⭐/⭐⭐ exercise attempted and committed
- [ ] At least four ⭐⭐⭐ challenges solved (incl. one debug + one concurrency)
- [ ] The **LRU cache** project builds and is tested
- [ ] You can tick the [02.13 mastery checklist](../weeks/02.13-projects-summary.md#module-02-mastery-checklist-from-memory) from memory

> [!TIP]
> The debugging (🐞) exercises are the highest-value — systematic debugging across these layers is the skill you'll use most. Don't skip them for the easier coding tasks.
