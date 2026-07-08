# Answers · Module 01 Quiz 01

[🏠 Module](../README.md) · [❓ Questions](quiz-01.md)

> Model answers with the *why*. If you got the gist but not the reasoning, reread the linked lesson.

---

### Part 1 — Internals

**1.** CPython **compiles** source to **bytecode**, which the **Python Virtual Machine (PVM)** — a bytecode interpreter — executes. It is not AOT-compiled to native machine code. → [01.1](../weeks/01.1-python-architecture.md)

**2.** Every operation goes through the interpreter's fetch-decode-execute loop with object boxing and dynamic dispatch (per-op overhead). NumPy/PyTorch express bulk math as single operations executed in optimized C/CUDA (releasing the GIL), avoiding per-element interpreter cost. → [01.1](../weeks/01.1-python-architecture.md), [01.11](../weeks/01.11-performance.md)

**3.** `==` compares **value**; `is` compares **identity** (same object). Use `is` only for singletons (`is None`, `is True/False`) — never for value equality (small-int/interning caching makes it *sometimes* work and then fail). → [01.2](../weeks/01.2-memory-management.md)

**4.** A mutable default (`def f(x, buf=[])`) is created **once** at definition and shared across all calls, so it accumulates state. Fix: default to `None` and create the object inside (`buf = [] if buf is None else buf`). → [01.2](../weeks/01.2-memory-management.md)

**5.** Reference counting frees an object when its count hits 0, but **reference cycles** (A↔B) keep each other's counts above 0 even when unreachable. A generational cyclic GC detects and collects those cycles. → [01.2](../weeks/01.2-memory-management.md)

### Part 2 — OOP & Functional

**6.** Deep inheritance is rigid and leads to class explosions for feature combinations; composition assembles behavior from swappable parts ("has-a"). Example: a RAG `Pipeline(retriever, ranker, generator)` composes interchangeable components. → [01.3](../weeks/01.3-object-oriented-python.md)

**7.** `__len__` + `__getitem__` (length/indexing, like a `Dataset`) and `__call__` (invoke like a function, e.g. `model(x)`). → [01.3](../weeks/01.3-object-oriented-python.md)

**8.** A closure is a function that captures variables from its enclosing scope — **by reference** — and remembers them after that scope returns. → [01.4](../weeks/01.4-functional-python.md)

**9.** Closures created in a loop all capture the *same* loop variable by reference, so they see its final value. Fix by binding per iteration with a default arg: `lambda i=i: i`. → [01.4](../weeks/01.4-functional-python.md)

### Part 3 — Lazy, Wrapping, Resources

**10.** A list comprehension materializes all items (memory ∝ N); a generator expression yields one at a time (~constant memory) — enabling processing of data larger than RAM. → [01.5](../weeks/01.5-iterators-generators.md)

**11.** A generator is single-use and stateful — once exhausted it raises `StopIteration` and yields nothing on a second pass. Recreate it or `list()` it if you need multiple passes. → [01.5](../weeks/01.5-iterators-generators.md)

**12.** `@dec` above `def f` means `f = dec(f)`. `functools.wraps` copies the wrapped function's metadata (`__name__`, `__doc__`) so introspection, tracebacks, and docs keep working. → [01.6](../weeks/01.6-decorators.md)

**13.** When the function isn't **pure** — has side effects, depends on changing external state, or is time-dependent — cached results become stale/incorrect. (Also: unbounded caches leak memory; args must be hashable.) → [01.6](../weeks/01.6-decorators.md)

**14.** `with` guarantees `__exit__` (cleanup) runs whether the block succeeds, returns, or raises. `__enter__` does setup and returns the `as` value; `__exit__(exc_type, exc, tb)` does teardown and returns falsy to let exceptions propagate. → [01.7](../weeks/01.7-context-managers.md)

### Part 4 — Types, Errors, Tests

**15.** No — hints don't run; Python ignores them (they're for mypy/editors). Pydantic uses the *same* annotations to **validate at runtime**. Hints = static safety; Pydantic = runtime enforcement (validate external/LLM data). → [01.8](../weeks/01.8-type-hinting.md)

**16.** A `Protocol` defines a structural interface — any object with the right methods satisfies it **without inheriting** it. It's duck typing made statically checkable. → [01.8](../weeks/01.8-type-hinting.md)

**17.** A bare `except:` catches everything, including `KeyboardInterrupt`/`SystemExit` (breaking Ctrl-C/shutdown) and hides bugs. `raise New(...) from exc` preserves the original exception's cause in the traceback. → [01.9](../weeks/01.9-error-handling-logging.md)

**18.** The failure is **transient** and the operation is **idempotent**; retries use bounded attempts with exponential backoff + jitter. Retrying permanent errors (bad input/auth) or non-idempotent calls is harmful. → [01.9](../weeks/01.9-error-handling-logging.md)

**19.** Mocking keeps tests fast, free, deterministic, and lets you control responses (incl. errors) instead of hitting a slow/costly/non-deterministic API. "Patch where it's used" = patch the name in the module that imported it (the namespace that looks it up), not where it's defined. → [01.10](../weeks/01.10-testing.md)

### Part 5 — Performance, Async, Packaging

**20.** The GIL (Global Interpreter Lock) lets only one thread run Python bytecode at a time. So: CPU-bound pure Python → **multiprocessing** (or NumPy, which releases the GIL); I/O-bound → **threading** or **asyncio** (the GIL is released while waiting). → [01.11](../weeks/01.11-performance.md)

**21.** Replacing an O(n) `in list` membership test with an O(1) `in set`/`dict`, which can turn an accidental O(n²) into O(n) — a massive win on large data. → [01.11](../weeks/01.11-performance.md)

**22.** asyncio gives **concurrency** (tasks interleave on one thread at `await` points), not CPU parallelism. AI workloads are I/O-bound (API/DB/HTTP waits), so overlapping the *waiting* is exactly what's needed. → [01.12](../weeks/01.12-async.md)

**23.** Scheduling is cooperative — a blocking call never yields, freezing the whole loop and all tasks. Use async libraries, or offload unavoidable blocking/CPU work with `asyncio.to_thread` (or a process pool). → [01.12](../weeks/01.12-async.md)

**24.** The lockfile pins exact versions so everyone/CI/prod builds the identical environment; `.venv/` is machine-specific and huge, so it's ignored. The correct fix for inter-module imports is an **editable install** (`pip install -e .`), not `sys.path` hacks. → [01.13](../weeks/01.13-packaging-code-quality.md)

**25.** Start at the README + examples, find the public API (top `__init__.py`), pick ONE feature, and trace it inward (go-to-definition), then read that feature's tests. Tests are executable, current usage examples showing real inputs/outputs and edge cases — the truest documentation. → [01.14](../weeks/01.14-reading-open-source.md)

---

> [!TIP]
> Turn every missed question into a flashcard and schedule it for tomorrow — missed items are your highest-value study material.
