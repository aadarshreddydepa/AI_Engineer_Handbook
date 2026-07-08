# Flashcards · Module 01 — Advanced Python for AI Engineering

[🏠 Module](../README.md) · [📚 Lessons](../weeks/README.md)

> Active-recall deck for the whole module. Answer **out loud before flipping**. Review on the [spaced-repetition schedule](../../../LEARNING_STRATEGY.md): same day, +1d, +3d, +7d, +16d, +35d. A failed card resets to interval 1.

---

## 01.1 · Architecture

**Q:** Precisely, is Python compiled or interpreted?
**A:** CPython compiles source to bytecode, then the PVM interprets that bytecode; it is not AOT-compiled to native machine code.

---

**Q:** Why is pure-Python numeric code slow?
**A:** Per-operation interpreter overhead (boxing, dynamic dispatch) — which is why frameworks push math into C/CUDA (NumPy/PyTorch).

---

**Q:** What are `sys.path` and `sys.modules`?
**A:** `sys.path` = ordered search locations for modules; `sys.modules` = cache giving import-once semantics.

---

## 01.2 · Memory

**Q:** What does `b = a` do?
**A:** Binds `b` to the same object as `a` — no copy. Mutating via one is visible via the other (aliasing).

---

**Q:** When may you use `is`?
**A:** Only for identity against singletons (`is None`, `is True/False`), never for value equality.

---

**Q:** Why avoid mutable default arguments?
**A:** The default is created once at definition and shared across calls, accumulating state; use a `None` sentinel.

---

**Q:** How does CPython free memory, and why isn't refcounting enough?
**A:** Reference counting frees at count 0; a cyclic GC is needed because reference cycles keep counts above 0 even when unreachable.

---

## 01.3 · OOP

**Q:** Why prefer composition over inheritance?
**A:** Deep inheritance is rigid; composition assembles swappable behavior ("has-a"), avoiding class explosions.

---

**Q:** How do you avoid the mutable-default bug in a dataclass?
**A:** `field(default_factory=list)` instead of `= []`.

---

**Q:** Which dunders make an object dataset-like and callable?
**A:** `__len__` + `__getitem__` (length/indexing) and `__call__` (invoke like a function, e.g. `model(x)`).

---

## 01.4 · Functional

**Q:** What is a closure, and how does it capture?
**A:** A function capturing enclosing-scope variables **by reference**, remembered after that scope returns.

---

**Q:** Why do loop-created closures often all return the last value?
**A:** They capture the loop variable by reference; fix with a per-iteration default arg (`lambda i=i: i`).

---

**Q:** What does `functools.partial` do?
**A:** Returns a new function with some arguments pre-filled, specializing a general function.

---

## 01.5 · Iterators & Generators

**Q:** What does `yield` do?
**A:** Pauses a generator function, returns a value, and preserves local state to resume on the next `next()`.

---

**Q:** Memory: list comprehension vs generator expression?
**A:** List holds all items (memory ∝ N); generator holds one at a time (~constant memory).

---

**Q:** Why can't you iterate a generator twice?
**A:** It's single-use/stateful — once exhausted it yields nothing; recreate or `list()` it.

---

## 01.6 · Decorators

**Q:** What is `@dec` equivalent to?
**A:** `f = dec(f)` — rebinding the name to the decorator's returned function.

---

**Q:** Why use `functools.wraps`?
**A:** To copy the wrapped function's metadata (`__name__`, `__doc__`) so introspection, tracebacks, and docs still work.

---

**Q:** When is caching a function unsafe?
**A:** When it isn't pure — side effects, changing external state, or time-dependence make cached results stale/wrong.

---

## 01.7 · Context Managers

**Q:** What does `with` guarantee?
**A:** That `__exit__` (cleanup) runs whether the block succeeds, returns, or raises.

---

**Q:** In `@contextmanager`, where does teardown go and why?
**A:** In a `finally` after `yield`, so cleanup runs even if the block raises.

---

**Q:** Why is `torch.no_grad()` a context manager?
**A:** It temporarily disables gradient tracking and guarantees restoration on block exit.

---

## 01.8 · Type Hinting

**Q:** Do type hints run at runtime?
**A:** No — Python ignores them; they're for static checkers (mypy) and editors. Pydantic adds opt-in runtime validation.

---

**Q:** Protocol vs ABC?
**A:** Protocol matches by structure (methods present, no inheritance); ABC requires explicit inheritance.

---

**Q:** How do you safely consume LLM JSON output?
**A:** Parse it through a strict Pydantic model — get a typed object or a clear ValidationError to retry on.

---

## 01.9 · Errors & Logging

**Q:** Why never use a bare `except:`?
**A:** It catches everything (incl. `KeyboardInterrupt`/`SystemExit`), breaking Ctrl-C/shutdown and hiding bugs.

---

**Q:** What does `raise New(...) from exc` do?
**A:** Chains exceptions, preserving the original cause in the traceback.

---

**Q:** What must hold to safely retry a failed call?
**A:** The failure is transient and the operation idempotent; retries are backed-off, jittered, and bounded.

---

**Q:** Why not `assert` for input validation?
**A:** `python -O` strips asserts, so the check silently disappears; use `if ...: raise`.

---

## 01.10 · Testing

**Q:** Why mock external model APIs in tests?
**A:** To keep tests fast, free, and deterministic, and to control responses (including errors).

---

**Q:** "Patch where it's used" means?
**A:** Patch the name in the namespace that looks it up (where imported), not where it's defined.

---

**Q:** How do you unit-test non-deterministic model output?
**A:** Mock the model and assert invariants/properties; measure real quality separately via evaluation.

---

## 01.11 · Performance

**Q:** What is the GIL and its consequence?
**A:** CPython's lock lets only one thread run Python bytecode at a time, so threads don't parallelize CPU-bound Python.

---

**Q:** CPU-bound pure Python — which concurrency?
**A:** multiprocessing (separate processes/GILs) or push math into NumPy (C, releases GIL).

---

**Q:** Biggest common Python speedup?
**A:** Replacing O(n) `in list` with O(1) `in set/dict`, turning O(n²) into O(n).

---

## 01.12 · Async

**Q:** Concurrency vs parallelism — which is asyncio?
**A:** Concurrency (tasks take turns on one thread at `await` points), not CPU parallelism.

---

**Q:** Why is a blocking call in a coroutine so bad?
**A:** Scheduling is cooperative — a blocking call never yields, freezing the whole loop and all tasks.

---

**Q:** How do you bound concurrency for external calls?
**A:** An `asyncio.Semaphore(N)` via `async with sem:` to cap in-flight requests.

---

## 01.13 · Packaging & Quality

**Q:** Commit vs ignore for reproducibility?
**A:** Commit `pyproject.toml` + lockfile; ignore `.venv/`.

---

**Q:** Correct fix for inter-module import errors?
**A:** An editable install (`pip install -e .`), not `sys.path` hacks.

---

**Q:** What do pre-commit hooks do?
**A:** Run quality checks (Ruff/mypy) automatically on every commit, blocking commits that fail.

---

## 01.14 · Reading Open Source

**Q:** Core method for reading an unfamiliar repo?
**A:** Top-down from the public API, then trace ONE feature inward; read that feature's tests.

---

**Q:** Why read tests when learning a library?
**A:** They're executable, current usage examples with real inputs/outputs and edge cases — the truest documentation.

---

> [!TIP]
> When you can answer every card across two spaced reviews, Module 01 is locked in. Persistent misses point to a lesson worth rereading.
