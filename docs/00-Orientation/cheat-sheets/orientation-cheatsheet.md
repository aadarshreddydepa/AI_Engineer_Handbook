# Cheat Sheet · Module 00 — Orientation & Foundations

[🏠 Module](../README.md) · [📚 Lessons](../weeks/README.md)

> One-page quick reference for the whole module. Optimized for scanning, not learning — learn it in the [lessons](../weeks/README.md) first.

---

## Vocabulary

```text
AI ⊃ ML ⊃ DL ⊃ Generative AI ⊃ LLM
AI Engineering = design/build/deploy/scale/maintain SYSTEMS around foundation models
ML inverts programming:  data + answers → rules (the model)
AGI = hypothetical human-level general intelligence (NOT a product)
```

| Term | One line |
|---|---|
| ML | Learns patterns from data instead of hand-coded rules |
| DL | ML with deep neural networks; learns features |
| GenAI | DL that creates new content |
| LLM | Generative language model; predicts the next token |
| AI Engineer | Software engineer whose system has a model at its core |

## The stack & flow

```text
Foundations → Data&Math → ML → DL → NLP/LLMs → Applied LLMs → Production → Mastery
Python→Data→ML→DL→LLM→RAG→Agents→MLOps→Cloud→Production
The model is ONE box; engineering is everything around it.
```

## Roles (by function)

| Role | Core function |
|---|---|
| AI Engineer ⭐ | Products around foundation models |
| ML Engineer | Train & ship custom models |
| Data Scientist | Insight from data |
| Applied AI Eng | Ship AI product features fast |
| Research Engineer | Implement & scale new ideas |
| Prompt Engineer | Reliable LLM behavior (a *skill*) |
| MLOps Engineer | Run AI reliably at scale |

> Optimize for the **work** and **trajectory**, not the title.

## Four curriculum principles

1. Foundations before LLMs 2. Implement before import
3. Production is first-class 4. Learning science (recall + spacing + projects)

## Environment

```text
isolation + declaration + reproducibility
one venv per project · commit pyproject.toml + lockfile · IGNORE .venv/
ruff format (style) · ruff check (lint) · mypy (types) · pytest (works)
Python 3.11+ · never touch system Python · GPU not needed early
```

## Git workflow

```text
small daily commits: type(scope): why   (feat|fix|docs|refactor|test|chore)
main always works · branch for risky work · merge when done
SemVer: MAJOR.break . MINOR.add . PATCH.fix
maintain changelog (Added/Changed/Fixed/Removed) in the same commit
NEVER commit secrets → .env is git-ignored; commit .env.example
```

## Reading

```text
DOCS:   navigate by need · examples & tests > prose · match version · stop to act
        types: tutorial(start) how-to(task) reference(details) explanation(why)
PAPERS: 3 passes (10min gist → 1hr idea → hrs reimplement)
        order: abstract → contributions → conclusion → figures → method
        core: problem · key idea · why · evidence · cost
        intuition FIRST; skip derivations early
```

## Daily loop

```text
Study → Build → Revise → Quiz → Flashcards → Journal → Commit
short on time? cut NEW STUDY, never retrieval (revise/quiz/flashcards)
weekly: Mon–Thu lessons · Fri project · Sat interleaved review · Sun rest
NO zero days · behind? shrink scope, don't skip foundations
```

## The seven mindsets

```text
curiosity · debugging(hypothesis→test→fix) · systems thinking
continuous learning · experimentation · MEASURE results · maintainable code
→ be an ENGINEER, not a tool user. A confident wrong answer invites you to stop thinking — don't.
```

## Resources

```text
handbook is self-contained · one resource per topic → FINISH it
active/high-retention (books, docs, courses, papers) > passive (video, podcasts)
facts → official docs/papers, not blogs · model IDs/pricing → provider docs (latest models)
```
