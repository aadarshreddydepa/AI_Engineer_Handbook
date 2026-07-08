# Answers · Module 00 Quiz 01

[🏠 Module](../README.md) · [❓ Questions](quiz-01.md)

> Model answers with the *why*. If you got the gist but not the reasoning, reread the linked lesson.

---

### Part 1 — Vocabulary & Landscape

**1.** AI ⊃ Machine Learning ⊃ Deep Learning ⊃ Generative AI ⊃ LLMs. *(They nest — each is a subset of the one before.)* → [00.1](../weeks/00.1-introduction.md)

**2.** Traditional programming: you supply **rules + data → answers**. Machine learning: you supply **data + answers → rules** (the learned model). ML is worth it when the rules are too complex to hand-write. → [00.1](../weeks/00.1-introduction.md)

**3.** AI Engineering is designing, building, deploying, scaling, and maintaining production software systems that use AI/foundation models — usually models you consume rather than train from scratch. → [00.1](../weeks/00.1-introduction.md)

**4.** Any four of: API gateway/auth, orchestration/prompting, cache, retriever + vector DB, prompt builder, guardrails/validation, logging/tracing, evaluation. *(The model is one box; these surround it.)* → [00.2](../weeks/00.2-ai-engineering-landscape.md)

**5.** Tools become obsolete quickly; the underlying concepts endure and transfer. Understanding *why* a tool exists lets you learn its replacement in an afternoon. → [00.2](../weeks/00.2-ai-engineering-landscape.md)

### Part 2 — Careers & Strategy

**6.** An **ML Engineer** builds/trains models (the engine); an **AI Engineer** builds products *around* (often pre-trained) foundation models (the car). → [00.3](../weeks/00.3-career-roadmap.md)

**7.** Any three of: skill scarcity, production impact, ability to ship reliably (not just prototype), depth+breadth ("T-shaped"), scope/seniority. → [00.3](../weeks/00.3-career-roadmap.md)

**8.** (1) Foundations before LLMs, (2) implement before import, (3) production is first-class, (4) learning science built in (active recall + spaced repetition + project-based learning). → [00.4](../weeks/00.4-learning-strategy.md)

**9.** The illusion that rereading/highlighting means you've learned — it builds recognition, not recall. The cure is **active recall** (retrieving from memory: blank-page recall, quizzing, flashcards). → [00.4](../weeks/00.4-learning-strategy.md)

**10.** Because a model in a notebook has ~zero value; value is created only when a reliable, affordable system reaches real users. Most jobs and impact live in that deploy-and-operate gap. → [00.4](../weeks/00.4-learning-strategy.md)

### Part 3 — Environment & Git

**11.** Isolation (one env per project), declaration (deps written in a file), reproducibility (rebuild anywhere from that file). → [00.5](../weeks/00.5-development-environment.md)

**12.** Commit `pyproject.toml` + the lockfile; `.gitignore` the `.venv/` directory. The declaration + lock *is* the environment. → [00.5](../weeks/00.5-development-environment.md)

**13.** Formatter = how code *looks* (style, e.g. `ruff format`); linter = likely *bugs*/smells (e.g. `ruff check`); test runner = does it *work* (e.g. `pytest`). *(Bonus: type checker = do the types line up, e.g. mypy.)* → [00.5](../weeks/00.5-development-environment.md)

**14.** e.g. `fix(loader): handle empty CSV without crashing`. *(type(scope): why.)* → [00.6](../weeks/00.6-github-repository-workflow.md)

**15.** MAJOR for incompatible/breaking changes; MINOR for backward-compatible new features; PATCH for backward-compatible bug fixes. → [00.6](../weeks/00.6-github-repository-workflow.md)

### Part 4 — Reading, Workflow & Mindset

**16.** Tutorial (learning-oriented — when new), how-to (task-oriented — specific goal), reference (information-oriented — exact details), explanation (understanding-oriented — the why). → [00.7](../weeks/00.7-reading-technical-documentation.md)

**17.** Read in three increasingly deep passes: (1) ~10 min gist (abstract, intro, headings, conclusion) to triage; (2) ~1 hr for the idea (method + figures, skip heavy proofs); (3) hours to reimplement/critique. Most papers deserve only Pass 1. → [00.8](../weeks/00.8-reading-research-papers.md)

**18.** Study, Build, Revise, Quiz, Flashcards, Journal, Commit. Never cut the **retrieval** steps (Revise, Quiz, Flashcards) — cut *new study* first. → [00.9](../weeks/00.9-learning-workflow.md)

**19.** The engineer methodically investigates *why* the output is wrong (observe → hypothesize → test → fix → prevent); the tool user shrugs and retries. Debugging is a trainable, systematic skill. → [00.10](../weeks/00.10-ai-engineer-mindset.md)

**20.** Books/docs/courses/papers are **active, high-retention** sources you engage with (and pair with recall); YouTube/podcasts are **passive** — good for first-pass intuition and awareness but weak for retention because you can't retrieve while consuming. → [00.11](../weeks/00.11-recommended-resources.md)

---

> [!TIP]
> Turn every question you missed into a flashcard and schedule it for tomorrow. Missed questions are the highest-value study material you have right now.
