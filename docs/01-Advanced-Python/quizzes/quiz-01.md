# Quiz · Module 01 — Advanced Python for AI Engineering

[🏠 Module](../README.md) · [📚 Lessons](../weeks/README.md) · [✅ Answers](answers-01.md)

> 25 questions across all 15 lessons. Answer from memory first, then check [answers-01.md](answers-01.md). Scoring at the bottom.

---

### Part 1 — Internals (01.1–01.2)

1. Precisely: is Python compiled or interpreted? What runs the bytecode?
2. Why is a tight pure-Python numeric loop slow, and how do NumPy/PyTorch address it?
3. What's the difference between `==` and `is`? When may you use `is`?
4. Explain the mutable-default-argument bug and its fix.
5. Why does CPython need a cyclic garbage collector on top of reference counting?

### Part 2 — OOP & Functional (01.3–01.4)

6. Why prefer composition over inheritance? Give an example.
7. Which magic methods make an object behave like a dataset and be callable?
8. What is a closure, and how does it capture variables?
9. Explain the loop-variable closure bug and how to fix it.

### Part 3 — Lazy, Wrapping, Resources (01.5–01.7)

10. Compare the memory of a list comprehension vs a generator expression.
11. Why can't you iterate a generator twice?
12. What does `@decorator` desugar to, and why do we use `functools.wraps`?
13. When is caching a function unsafe?
14. What does the `with` statement guarantee, and what do `__enter__`/`__exit__` do?

### Part 4 — Types, Errors, Tests (01.8–01.10)

15. Do type hints run at runtime? How do hints and Pydantic differ in role?
16. What is a `Protocol`, and how does it relate to duck typing?
17. Why is a bare `except:` dangerous? What does `raise ... from` preserve?
18. What must be true to safely retry a failed call?
19. Why mock external APIs in tests, and what does "patch where it's used" mean?

### Part 5 — Performance, Async, Packaging (01.11–01.14)

20. What is the GIL, and how does it drive your choice of threading vs multiprocessing vs asyncio?
21. What's the single most common large Python speedup, and why (complexity)?
22. Concurrency vs parallelism — which does asyncio give, and why is that right for AI I/O?
23. Why must you never block the event loop, and how do you handle unavoidable blocking work?
24. Why commit the lockfile but not `.venv/`, and what's the right fix for inter-module import errors?
25. Describe the method for reading an unfamiliar codebase, and why tests are valuable.

---

### Scoring

| Score | Meaning |
|---|---|
| 22–25 | Excellent — proceed to Module 02 |
| 18–21 | Good — review the missed lessons' summaries/flashcards |
| 13–17 | Reread the weaker lessons before continuing |
| < 13 | Rework the module — these are load-bearing skills |

> [!TIP]
> Every missed question maps to a lesson. Turn misses into flashcards and schedule them for tomorrow.
