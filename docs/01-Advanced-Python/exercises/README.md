# Exercises · Module 01 — Advanced Python for AI Engineering

[🏠 Module](../README.md) · [📚 Lessons](../weeks/README.md)

> A structured set spanning all 15 lessons — coding, debugging, refactoring, and design — with a deliberate difficulty ramp per the [exercise standards](../../../standards/exercise-standards.md). Do these in your study repo; commit your solutions.

**Difficulty:** ⭐ warm-up · ⭐⭐ practice · ⭐⭐⭐ challenge · ⭐⭐⭐⭐ stretch. **Types:** 💻 Coding · 🐞 Debug · ♻️ Refactor · 🏛️ Design.

---

## 01.1 · Architecture
- [ ] **⭐ 💻** Disassemble three functions with `dis.dis`; explain one's opcodes.
- [ ] **⭐⭐ 💻** Create a package, import it, find the `.pyc`; delete `__pycache__` and watch it regenerate.
- [ ] **⭐⭐⭐ 🐞** Create a circular import between two modules; fix it three ways.

## 01.2 · Memory
- [ ] **⭐ 💻** Demonstrate aliasing, then break it with a copy.
- [ ] **⭐⭐ 🐞** Reproduce and fix the mutable-default-argument bug; explain the fix.
- [ ] **⭐⭐⭐ 🐞** Write a function that leaks via a growing global cache; detect growth with `tracemalloc`; fix with a bounded cache.

## 01.3 · OOP
- [ ] **⭐ 💻** A `dataclass` config with a safe mutable default; show free `__repr__`/`__eq__`.
- [ ] **⭐⭐ 💻** A `Vector` class with `__add__`, `__len__`, `__getitem__`, `__repr__`.
- [ ] **⭐⭐⭐ ♻️** Refactor a deep inheritance hierarchy into composition; explain the improvement.

## 01.4 · Functional
- [ ] **⭐⭐ 💻** `make_counter()` using a closure + `nonlocal`.
- [ ] **⭐⭐ 🐞** Reproduce and fix the loop-closure bug.
- [ ] **⭐⭐⭐ 💻** A function registry via a registration decorator.

## 01.5 · Iterators & Generators
- [ ] **⭐ 💻** Implement `Fibonacci` as an iterator class, then as a generator.
- [ ] **⭐⭐ 💻** Benchmark list-comp vs generator-expr memory for 10M items.
- [ ] **⭐⭐⭐ 💻** Compose a 3+ stage lazy pipeline; prove nothing is fully materialized (works on an infinite source with `islice`).

## 01.6 · Decorators
- [ ] **⭐⭐ 💻** `@repeat(n)`; explain the three layers.
- [ ] **⭐⭐ 💻** Compare `fib` with/without `@lru_cache`; measure speedup.
- [ ] **⭐⭐⭐ 💻** `@retry` with exponential backoff catching only specified exceptions.
- [ ] **⭐⭐⭐ 🐞** Fix a decorator missing `wraps` and not returning results.

## 01.7 · Context Managers
- [ ] **⭐ 💻** A `Timer` context manager (class-based), then via `@contextmanager`.
- [ ] **⭐⭐ 💻** A set-and-restore context manager for an env var/global.
- [ ] **⭐⭐⭐ 💻** Open a runtime-determined list of files with `ExitStack`.

## 01.8 · Type Hinting
- [ ] **⭐ 💻** Fully type a function; fix mypy's findings.
- [ ] **⭐⭐ 💻** Define a `Protocol`; type-check a non-inheriting implementation.
- [ ] **⭐⭐⭐ 💻** Model an LLM structured response with Pydantic (field validation); handle `ValidationError` on bad JSON.

## 01.9 · Errors & Logging
- [ ] **⭐⭐ 💻** A subsystem exception hierarchy; chain low→high with `from`.
- [ ] **⭐⭐⭐ 💻** `call_with_retry` with backoff+jitter retrying only `TransientError`; test both paths.
- [ ] **⭐⭐ 💻** Configure `logging`; log each level; log an exception with `exc_info=True`; emit one structured (JSON) record.

## 01.10 · Testing
- [ ] **⭐ 💻** pytest tests for `top_k` (normal/empty/boundary).
- [ ] **⭐⭐ 💻** Test error paths with `pytest.raises(..., match=)`; write a fixture with `tmp_path`.
- [ ] **⭐⭐⭐ 💻** Test a function that calls a "model API" by mocking the client; verify return handling, call args, and the error path (`side_effect`).

## 01.11 · Performance
- [ ] **⭐ 💻** Benchmark `in list` vs `in set` with `timeit`.
- [ ] **⭐⭐ 💻** Profile a slow pipeline with `cProfile`; fix the top hotspot; re-measure.
- [ ] **⭐⭐⭐ 💻** Show threads don't speed CPU-bound work but do speed I/O-bound (simulate I/O with `sleep`).
- [ ] **⭐⭐⭐ 💻** Vectorize a numeric loop with NumPy; compare timings on 10M elements.

## 01.12 · Async
- [ ] **⭐ 💻** Two coroutines via `gather`; confirm total ≈ longest, not sum.
- [ ] **⭐⭐ 💻** 100 simulated API calls concurrently vs sequentially.
- [ ] **⭐⭐ 💻** Add a `Semaphore(10)`; observe timing/rate-limit effect.
- [ ] **⭐⭐⭐ 🐞** Introduce `time.sleep` in a coroutine (freeze the loop); fix with `asyncio.sleep`/`to_thread`.

## 01.13 · Packaging & Quality
- [ ] **⭐ 💻** `src/`-layout project + `pyproject.toml`; editable-install; import from elsewhere.
- [ ] **⭐⭐ 💻** Configure Ruff + mypy; clean a messy file.
- [ ] **⭐⭐⭐ 💻** Add `.pre-commit-config.yaml`; install hooks; watch a failing commit get blocked.

## 01.14 · Reading Open Source
- [ ] **⭐ 🏛️** Orient in a real library from README + `pyproject.toml` + `__init__.py` (15 min).
- [ ] **⭐⭐ 🏛️** Trace one public function to its implementation; diagram the call path.
- [ ] **⭐⭐⭐ 🏛️** Identify ≥5 Module 01 patterns in a small AI library.

## 01.15 · Projects
- [ ] Build **Project 3 (Async API Client)** at minimum — the flagship.
- [ ] Attempt **Project 6 (Plugin System)** as the module capstone.

---

## Completion criteria

- [ ] Every ⭐/⭐⭐ exercise attempted and committed
- [ ] At least three ⭐⭐⭐ challenges solved (incl. one debug + one async)
- [ ] The flagship **Async API Client** project builds, is packaged, and is tested
- [ ] You can tick the [01.15 mastery checklist](../weeks/01.15-projects-summary.md#module-01-mastery-checklist-from-memory) from memory

> [!TIP]
> The debugging (🐞) and refactoring (♻️) exercises build the most durable skill — fixing real, subtle problems is where deep understanding forms. Don't skip them for the easier coding tasks.
