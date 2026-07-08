# Exercise Standards

[🏠 Standards](README.md)

> Exercises are where understanding is forged. Every lesson ships graded, progressively harder exercises across five types.

---

## The five exercise types

| Type | Trains | Typical prompt |
|---|---|---|
| **Coding** | Implementation from spec | "Implement `<thing>` that passes these tests." |
| **Debugging** | Reading & fixing broken code | "This code produces `<wrong output>`. Find and fix the bug." |
| **Refactoring** | Improving working code | "Make this correct code faster / cleaner / safer." |
| **Architecture design** | System-level thinking | "Design a system that `<requirement>`." |
| **Scenario-based** | Judgment & tradeoffs | "Given `<constraints>`, which approach and why?" |

Every lesson should include a **mix**, not only coding.

---

## Difficulty must progress gradually

Use a 4-level scale and order exercises from easy to hard:

| Level | Label | Description |
|:--:|---|---|
| ⭐ | Warm-up | Direct application of one idea from the lesson |
| ⭐⭐ | Practice | Combines 2–3 ideas; light problem-solving |
| ⭐⭐⭐ | Challenge | Multi-step; requires real design decisions |
| ⭐⭐⭐⭐ | Stretch | Open-ended; connects to earlier modules |

> [!WARNING]
> Never jump from ⭐ to ⭐⭐⭐⭐. A visible difficulty ramp keeps learners in the productive-struggle zone instead of frustration or boredom.

---

## Required structure (per exercise)

Built from [templates/exercise-template.md](../templates/exercise-template.md):

| Field | Required |
|---|---|
| Title & type | ✅ |
| Difficulty (⭐ scale) | ✅ |
| Goal | ✅ |
| Instructions | ✅ |
| Constraints | ✅ |
| Progressive hints (collapsed) | ✅ |
| Solution (separate file) | ✅ |
| Self-check criteria | ✅ |

---

## Rules

- **Every exercise has a solution** in `solution-NN.*`, but hints come first so learners struggle productively before revealing it.
- **Hints are staged** — use collapsible `<details>` so they don't spoil the problem.
- **Coding exercises are testable** — provide expected inputs/outputs or a small test.
- **Debugging exercises embed a realistic bug**, not a typo — the kind engineers actually hit.
- **Solutions are exemplary** — they follow [code standards](code-standards.md); learners will imitate them.
- **Reference earlier modules** in stretch exercises to reinforce spaced repetition.

---

## File layout

```text
docs/<module>/exercises/
├── exercise-01.md        # ⭐ warm-up
├── exercise-02.md        # ⭐⭐ practice
├── exercise-03.md        # ⭐⭐⭐ challenge (debugging)
├── exercise-04.md        # ⭐⭐⭐⭐ stretch
├── solution-01.py
├── solution-02.py
└── ...
```

---

## Debugging-exercise pattern

```markdown
## Goal
The function below should return the mean of a list but crashes on empty input
and returns the wrong value for negatives. Diagnose both issues and fix them.

## Provided (buggy) code
`<broken snippet>`

## Expected behavior
| Input | Expected |
|---|---|
| [1, 2, 3] | 2.0 |
| [] | raises ValueError |
```

---

## Checklist

- [ ] Mix of types (not only coding)
- [ ] Difficulty ramps ⭐ → ⭐⭐⭐⭐
- [ ] Staged hints before the solution
- [ ] Coding exercises are testable
- [ ] Solutions follow code standards
- [ ] At least one exercise links back to a prior module
