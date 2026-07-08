# Flashcards · Module 00 — Orientation & Foundations

[🏠 Module](../README.md) · [📚 Lessons](../weeks/README.md)

> Active-recall deck for the whole module. Answer **out loud before flipping**. Review on the [spaced-repetition schedule](../../../LEARNING_STRATEGY.md): same day, +1d, +3d, +7d, +16d, +35d. Failing a card resets it to interval 1 — that's normal.

---

## 00.1 · Introduction

**Q:** How do AI, ML, DL, Generative AI, and LLMs relate?
**A:** They nest: AI ⊃ ML ⊃ DL ⊃ Generative AI ⊃ LLMs.

---

**Q:** What inversion defines ML vs traditional programming?
**A:** Traditional: rules + data → answers. ML: data + answers → rules (the model).

---

**Q:** What is an LLM's core training objective?
**A:** Next-token prediction over large text corpora.

---

**Q:** In one sentence, what is AI Engineering?
**A:** Designing, building, deploying, and maintaining production systems built around AI/foundation models.

---

**Q:** ML Engineer vs AI Engineer?
**A:** MLE builds/trains models (the engine); AI Engineer builds products around (often pre-trained) models (the car).

---

**Q:** Why avoid "AGI" in engineering design discussions?
**A:** It's hypothetical and undefined operationally; it hides real, shippable requirements.

---

## 00.2 · Landscape

**Q:** Name the layers of the AI Engineering stack, bottom to top.
**A:** Foundations → Data & Math → ML → DL → NLP & LLMs → Applied LLMs → Production → Mastery.

---

**Q:** In a production AI system, what surrounds the model?
**A:** API/auth, orchestration, cache, retrieval, prompt building, guardrails, logging, evaluation.

---

**Q:** Why learn concepts over tools?
**A:** Tools become obsolete; conceptual understanding transfers to their replacements.

---

**Q:** What is the "skip-ahead trap"?
**A:** Rushing to LLMs/agents while skipping foundations, producing demos that can't be deployed or maintained.

---

## 00.3 · Careers

**Q:** Which role does this handbook primarily target?
**A:** AI Engineer — building production products around foundation models.

---

**Q:** Is "Prompt Engineer" a durable standalone career?
**A:** Increasingly no — it's becoming a core *skill* of the AI Engineer.

---

**Q:** Name three durable drivers of AI compensation.
**A:** Skill scarcity, production impact, and the ability to ship reliably (plus scope/seniority).

---

**Q:** Why read job descriptions over titles?
**A:** The same title means different work at different companies; descriptions reveal the real role.

---

## 00.4 · Learning Strategy

**Q:** Why foundations before LLMs?
**A:** LLM systems are software; you debug and design them with foundational skills. Without them the model is an unfixable black box.

---

**Q:** What does "implement before import" mean and why?
**A:** Build a naive version of a concept before using the library — to understand it, debug it, and transfer to future tools.

---

**Q:** Why is production engineering a core phase?
**A:** A model in a notebook has no value; value comes from reliable, affordable systems reaching users.

---

**Q:** What is the "illusion of competence"?
**A:** Rereading/highlighting feels like learning but doesn't build recall; if you can't reproduce it blank-page, you don't know it.

---

## 00.5 · Development Environment

**Q:** What three properties should every project environment have?
**A:** Isolation, declaration, reproducibility.

---

**Q:** What do you commit vs ignore for environments?
**A:** Commit `pyproject.toml` + lockfile; ignore `.venv/`.

---

**Q:** Formatter vs linter?
**A:** Formatter fixes how code *looks*; linter flags likely *bugs*/smells.

---

**Q:** Most common beginner environment bug?
**A:** VS Code interpreter ≠ the terminal's active `.venv`, causing mysterious import errors.

---

**Q:** Do you need a GPU to start?
**A:** No — CPU and free cloud GPUs cover everything until deep learning/fine-tuning.

---

## 00.6 · Repository Workflow

**Q:** What makes a good commit?
**A:** One logical change, a clear "why" message, repo left working, small enough to review.

---

**Q:** Explain SemVer parts.
**A:** MAJOR = breaking change, MINOR = backward-compatible feature, PATCH = backward-compatible fix.

---

**Q:** Why branch instead of working on main?
**A:** To isolate risky/large work so `main` always stays in a working state.

---

**Q:** What must you never commit, and how do you avoid it?
**A:** Secrets, `.venv/`, large data — use `.gitignore` and a git-ignored `.env` (+ committed `.env.example`).

---

## 00.7 · Reading Documentation

**Q:** What are the four documentation content types?
**A:** Tutorial (learning), how-to (task), reference (details), explanation (understanding).

---

**Q:** Where do you look when docs are incomplete?
**A:** The test suite — it shows the true, current intended usage.

---

**Q:** When should you stop reading docs?
**A:** When you have enough to take the next concrete action; return later as new questions arise.

---

## 00.8 · Reading Papers

**Q:** What are the three passes?
**A:** (1) ~10 min gist, (2) ~1 hr idea (method + figures), (3) hours to reimplement/critique.

---

**Q:** Where is a paper's core contribution usually stated?
**A:** The last paragraph of the introduction ("we propose…/our contributions are…").

---

**Q:** How do you handle unfamiliar math in a paper?
**A:** Get the plain-English intuition first; skip full derivations early; return after the math/DL modules.

---

**Q:** What five things capture a paper's essence?
**A:** Problem, key idea, why it works, evidence, cost/tradeoffs.

---

## 00.9 · Daily Workflow

**Q:** Name the seven steps of the daily loop.
**A:** Study, Build, Revise, Quiz, Flashcards, Journal, Commit.

---

**Q:** When short on time, what do you cut first?
**A:** New study (step 1) — never the retrieval steps (revise/quiz/flashcards).

---

**Q:** What is a "zero day" and why avoid it?
**A:** A day with no work; even 15 min of flashcards preserves the habit and the chain.

---

## 00.10 · Mindset

**Q:** What distinguishes an engineer from a tool user when output is wrong?
**A:** The engineer methodically investigates *why* and fixes it; the tool user retries or gives up.

---

**Q:** What is debugging, properly done?
**A:** A methodical loop: observe → hypothesize → test the smallest thing → fix → verify → prevent recurrence.

---

**Q:** Why measure instead of trusting vibes?
**A:** AI output is probabilistic; cherry-picked good results easily fool you. Metrics make quality claims real.

---

**Q:** The subtle AI-era trap?
**A:** A model's confident fluency tempting you to stop thinking; stay curious and skeptical.

---

## 00.11 · Resources

**Q:** What's the resource-hoarding trap?
**A:** Collecting resources you never finish; it feels productive but is procrastination. Finish one before adding another.

---

**Q:** Where do you get authoritative model capabilities/pricing?
**A:** The model provider's official docs — never a blog or memory; default to the latest models.

---

**Q:** Is external material required to finish this handbook?
**A:** No — it's self-contained; resources are optional depth and currency.

---

> [!TIP]
> When you can answer every card correctly across two spaced reviews, Module 00 is locked in. Any card you keep failing points to a lesson worth rereading.
