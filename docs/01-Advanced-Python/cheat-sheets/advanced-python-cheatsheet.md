# Cheat Sheet · Module 01 — Advanced Python for AI Engineering

[🏠 Module](../README.md) · [📚 Lessons](../weeks/README.md)

> One-page reference for the whole module. Scan it; learn it in the [lessons](../weeks/README.md).

---

## Execution & memory (01.1–01.2)

```text
EXECUTION: source .py → (compile) bytecode → PVM interprets → output
  CPython default · dis.dis(fn) to inspect · __pycache__ = cached .pyc (not security)
IMPORT: sys.modules cache → find on sys.path → run top-level ONCE → bind
  circular import = A↔B at top level → move import into function / restructure
MODEL: variables are NAMES bound to OBJECTS; assignment never copies (aliasing)
IDENTITY: a is b (same obj, only for None/singletons) · a == b (value) · id(a)
MUTABLE: list/dict/set  IMMUTABLE: int/float/str/tuple/frozenset/bytes
DEFAULT-ARG BUG: def f(x, buf=None): buf = [] if buf is None else buf
COPY: b=a (alias) · a.copy() (shallow) · copy.deepcopy (full, costly)
MEMORY: refcount frees at 0 · cyclic GC frees cycles · leaks = unbounded refs (bound caches)
```

## OOP & functional (01.3–01.4)

```text
PILLARS: encapsulation · inheritance(is-a) · polymorphism(duck) · abstraction(ABC/Protocol)
PREFER COMPOSITION over deep inheritance · super().__init__() always
DATACLASS: @dataclass · field(default_factory=list) · frozen=True
PROPERTY: @property + @x.setter → attribute syntax + validation
DUNDERS: __init__ __repr__ __eq__ __len__ __getitem__ __iter__ __call__ __enter__/__exit__ __add__
__slots__ for many small objects (less memory)
FUNCTIONAL: functions are first-class · HOF (sorted key=, map/filter) · comprehensions > map/filter
CLOSURE: captures enclosing vars BY REFERENCE (loop bug → lambda i=i: i)
PARTIAL: functools.partial(f, fixed) · registry = {"name": fn}
```

## Lazy, wrapping, resource (01.5–01.7)

```text
ITERATOR: __iter__/__next__ (StopIteration) · for uses them
GENERATOR: yield → lazy, pausable · gen expr (x for x in it) · SINGLE-USE
  memory: gen ~constant vs list ∝ N · stream files: for line in f
  itertools: islice chain count groupby batched(3.12+)
DECORATOR: @dec == f = dec(f) ; wrapper closes over func
  def dec(f): @functools.wraps(f) def w(*a,**k): ...; return f(*a,**k); return w
  args → 3 layers · stack: @a\n@b\nf == a(b(f)) · uses: log/time/cache/retry/auth
CONTEXT MGR: with = guaranteed cleanup (even on error)
  __enter__/__exit__(et,ev,tb)→False (don't suppress) · @contextmanager: setup;try:yield;finally:cleanup
  ExitStack for dynamic N · torch.no_grad() is a context manager
```

## Types, errors, tests (01.8–01.10)

```text
TYPES: def f(x: int) -> list[str] · T|None (handle None) · Literal · Callable · Protocol · TypedDict
  hints = STATIC (mypy, no runtime effect) ; PYDANTIC = RUNTIME validation (validate LLM output!)
ERRORS: except SpecificError (never bare/BaseException) · custom hierarchy · raise New() from exc
  retry transient+idempotent only: exp backoff + jitter + cap + bounded
  assert = invariants only (stripped by -O) · validate at boundaries, fail fast
LOGGING: logging.getLogger(__name__) · configure ONCE at entry · levels DEBUG<INFO<WARNING<ERROR<CRITICAL
  logger.error(..., exc_info=True) · lazy %-args · STRUCTURED json + request_id + latency
  NEVER log secrets/PII
TESTS: pytest · AAA · pytest.raises · @fixture (yield teardown) · parametrize
  MOCK external deps (patch where USED; prefer dependency injection)
  coverage = gap-finder not goal · non-determinism → mock model, assert properties
```

## Perf, async, packaging (01.11–01.13)

```text
PERF: work→right→(MEASURE: timeit/cProfile)→fast where it matters
  complexity first: in list O(n) → set/dict O(1) · cache pure fns (lru_cache maxsize)
GIL: 1 thread runs Python bytecode at a time
  CPU-bound pure Python → multiprocessing · numeric → NumPy(releases GIL)
  I/O-bound → threading / asyncio
ASYNC: single-thread concurrency (overlap I/O waits, not parallelism)
  async def/await · asyncio.run(main) · gather(*coros)/TaskGroup · Semaphore(N) to bound
  NEVER block loop (no time.sleep/requests → asyncio.sleep / to_thread) · set timeouts
PACKAGING: src/ layout · pyproject.toml (deps/scripts/[tool.*]) · commit lockfile, ignore .venv/
  editable install: pip install -e . (fixes imports) · Ruff(format+lint) + mypy + pre-commit
```

## Reading open source (01.14)

```text
MAP: README · pyproject.toml · src/ · tests/ · docs/ · CI
METHOD: examples → public API (__init__) → pick ONE feature → trace inward → read its tests
TOOLS: go-to-definition · grep · git blame/log · breakpoints
RECOGNIZE: class(Base)+super · __call__/__len__/__getitem__ · @decorator · with ctx · yield · async def · Pydantic
RULE: trace one path; take notes in your own words
```

## The golden rules

```text
1. Measure before optimizing.               6. Validate data at trust boundaries (Pydantic).
2. Prefer composition over inheritance.      7. Never block the event loop.
3. Bound anything that grows (caches, concurrency). 8. Catch specific exceptions; log, don't swallow.
4. Type-hint everything; run mypy.           9. Commit the lockfile, not .venv/.
5. Stream large data (generators).           10. Reading code is a first-class skill.
```
