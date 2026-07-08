#!/usr/bin/env python3
"""
generate_structure.py
=====================================================================
Idempotently generates the AI Engineer Handbook repository skeleton:

  * All module folders under docs/ with standardized subfolders
  * A navigation-rich README.md for every module
  * READMEs for every top-level folder
  * All reusable templates
  * .gitkeep placeholders for empty folders

Root planning docs (README, ROADMAP, CURRICULUM, etc.) are authored by
hand and are NOT written by this script.

Run from the repository root:  python scripts/generate_structure.py
This script never deletes hand-written content; it only writes the
structural, templated files it owns.
"""
from __future__ import annotations
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# --------------------------------------------------------------------------
# Module catalogue — single source of truth for docs/ structure & navigation
# --------------------------------------------------------------------------
MODULES = [
    ("00", "Orientation", "How to use this handbook, the AI-engineer mindset, and setting up a reproducible environment.",
     ["What an AI Engineer does and the systems they own",
      "How to study this handbook for long-term retention",
      "Setting up a reproducible Python + GPU environment",
      "The experiment and reproducibility mindset"],
     ["01-Advanced-Python", "16-MLOps"]),
    ("01", "Advanced-Python", "Production-grade Python: typing, async, packaging, and performance.",
     ["Type hints and static checking at scale",
      "Dataclasses, Pydantic, and data validation",
      "Async, concurrency, and parallelism for AI workloads",
      "Packaging, dependency management, and profiling"],
     ["00-Orientation", "02-Computer-Science"]),
    ("02", "Computer-Science", "The core CS every engineer needs: data structures, algorithms, and complexity.",
     ["Complexity analysis (Big-O) in practice",
      "Core data structures and when to use them",
      "Algorithmic patterns and problem solving",
      "Memory, recursion, and computational thinking"],
     ["01-Advanced-Python", "20-Interview-Preparation"]),
    ("03", "Linux", "The command line and operating-system foundations AI systems run on.",
     ["Shell, filesystem, and text processing",
      "Processes, signals, and resource limits",
      "Permissions, users, and environment management",
      "Networking basics and remote servers"],
     ["04-Git", "17-Cloud"]),
    ("04", "Git", "Version control and collaboration workflows for real teams.",
     ["The Git object model and branching",
      "Collaboration workflows and pull requests",
      "Rebasing, resolving conflicts, and history hygiene",
      "Git for experiments, data, and large files"],
     ["03-Linux", "16-MLOps"]),
    ("05", "SQL", "Relational data modeling and querying for AI applications.",
     ["Relational modeling and normalization",
      "Querying: joins, aggregation, window functions",
      "Indexing and query optimization",
      "SQL in data and ML pipelines"],
     ["07-Data-Analysis", "13-RAG"]),
    ("06", "Mathematics", "The math that powers ML — built from intuition, not memorization.",
     ["Linear algebra for machine learning",
      "Calculus, gradients, and the chain rule",
      "Probability and statistics",
      "Optimization intuition"],
     ["08-Machine-Learning", "09-Deep-Learning"]),
    ("07", "Data-Analysis", "Turning raw data into insight with NumPy, pandas, and visualization.",
     ["NumPy vectorization and array thinking",
      "pandas for data wrangling",
      "Exploratory data analysis (EDA)",
      "Visualization and communicating findings"],
     ["05-SQL", "08-Machine-Learning"]),
    ("08", "Machine-Learning", "Classical ML from first principles: models, evaluation, and error analysis.",
     ["The end-to-end ML workflow and data leakage",
      "Regression, trees, and ensembles",
      "The bias–variance tradeoff",
      "Evaluation, metrics, and error analysis"],
     ["06-Mathematics", "09-Deep-Learning"]),
    ("09", "Deep-Learning", "Neural networks from the ground up with PyTorch.",
     ["Neurons, layers, and backpropagation from scratch",
      "PyTorch: tensors, autograd, and training loops",
      "Regularization, normalization, and initialization",
      "Debugging and stabilizing neural networks"],
     ["08-Machine-Learning", "10-NLP"]),
    ("10", "NLP", "Language modeling and the Transformer architecture.",
     ["Tokenization and text representation",
      "Embeddings and semantic similarity",
      "The attention mechanism from first principles",
      "Building a Transformer block"],
     ["09-Deep-Learning", "11-LLMs"]),
    ("11", "LLMs", "How large language models are trained, decode, and behave.",
     ["Pretraining objectives and scaling laws",
      "Decoding strategies (temperature, top-k/top-p)",
      "Context windows, positional encoding, KV cache",
      "Model selection: capability, cost, licensing"],
     ["10-NLP", "12-Prompt-Engineering"]),
    ("12", "Prompt-Engineering", "Reliably steering LLMs through structured prompting and reasoning techniques.",
     ["Anatomy of a prompt: roles and structured output",
      "Reasoning: few-shot, chain-of-thought, self-consistency",
      "Reliability: JSON schemas, guardrails, prompt testing",
      "Prompt evaluation and versioning"],
     ["11-LLMs", "13-RAG"]),
    ("13", "RAG", "Grounding LLMs with retrieval-augmented generation.",
     ["Why RAG: grounding and hallucination",
      "Embeddings, chunking, and vector databases",
      "Retrieval quality: hybrid search and reranking",
      "Building and evaluating production RAG"],
     ["12-Prompt-Engineering", "14-AI-Agents"]),
    ("14", "AI-Agents", "LLM-driven systems that reason and act through tools.",
     ["The reasoning–action loop",
      "Tools, function calling, and structured actions",
      "Planning, memory, and orchestration",
      "Failure recovery and multi-agent systems"],
     ["13-RAG", "15-Fine-Tuning"]),
    ("15", "Fine-Tuning", "Adapting foundation models with parameter-efficient fine-tuning and alignment.",
     ["When to fine-tune vs prompt vs RAG",
      "Parameter-efficient fine-tuning: LoRA / QLoRA / PEFT",
      "Data curation and instruction tuning",
      "Alignment: RLHF and DPO intuition"],
     ["14-AI-Agents", "16-MLOps"]),
    ("16", "MLOps", "Deploying, versioning, and maintaining ML/AI systems.",
     ["Serving models via APIs (batching, streaming)",
      "Containerization and reproducible deployments",
      "CI/CD, testing, and safe rollouts for AI",
      "Experiment tracking and model registries"],
     ["04-Git", "19-Production-AI"]),
    ("17", "Cloud", "Running AI workloads on cloud infrastructure.",
     ["Cloud primitives: compute, storage, networking",
      "Containers, orchestration, and serverless",
      "GPUs and accelerators in the cloud",
      "Cost management and infrastructure-as-code"],
     ["03-Linux", "18-System-Design"]),
    ("18", "System-Design", "Designing scalable, reliable systems — including AI systems.",
     ["System-design fundamentals and tradeoffs",
      "Scalability, caching, and data flow",
      "Designing LLM/RAG/agent systems",
      "Reliability, consistency, and bottlenecks"],
     ["17-Cloud", "19-Production-AI"]),
    ("19", "Production-AI", "Making AI systems reliable, observable, secure, and affordable.",
     ["Evaluation and LLM-as-judge in production",
      "Observability: tracing, logging, monitoring",
      "Security, guardrails, and red-teaming",
      "Latency, throughput, and cost engineering"],
     ["16-MLOps", "18-System-Design"]),
    ("20", "Interview-Preparation", "Getting job-ready: DSA, ML, system design, and behavioral.",
     ["Data structures and algorithms drills",
      "ML and LLM conceptual interviews",
      "AI system-design interviews",
      "Behavioral and portfolio storytelling"],
     ["02-Computer-Science", "18-System-Design"]),
    ("21", "Capstone-Projects", "End-to-end production systems that prove your capability.",
     ["Scoping and designing a full system",
      "Building RAG + agent + serving + eval",
      "Hardening, observing, and documenting it",
      "Publishing a portfolio-grade project"],
     ["14-AI-Agents", "19-Production-AI"]),
]

MODULE_SUBFOLDERS = {
    "weeks": "Weekly lesson content, one file per week (`week-01.md`, `week-02.md`, …).",
    "diagrams": "Mermaid sources and exported diagram assets for this module.",
    "exercises": "Hands-on practice problems with solutions.",
    "projects": "Buildable projects that apply this module's skills.",
    "quizzes": "Self-assessment question banks with answer keys.",
    "flashcards": "Spaced-repetition Q/A decks for active recall.",
    "cheat-sheets": "One-page quick references for this module.",
    "references": "Paper summaries and deep-dive notes.",
}

TOP_FOLDERS = {
    "docs": "The handbook itself — one folder per module (`NN-Name/`).",
    "code": "Standalone, runnable code samples and small libraries referenced by lessons.",
    "notebooks": "Jupyter notebooks for interactive, exploratory lessons.",
    "exercises": "Cross-module exercise sets and challenges not tied to a single module.",
    "quizzes": "Cross-module and cumulative quizzes (per-module quizzes live inside each module).",
    "flashcards": "Global/cumulative flashcard decks (per-module decks live inside each module).",
    "interview-preparation": "Interview question banks, system-design prompts, and mock-interview rubrics.",
    "projects": "Large, multi-module and capstone projects.",
    "templates": "Reusable Markdown templates that keep every page consistent.",
    "references": "Cross-cutting references: papers, books, external docs, and reading notes.",
    "scripts": "Repository automation (structure generation, link checking, linting).",
    "archive": "Deprecated or superseded material kept for history — never linked from active content.",
}

ASSET_FOLDERS = {
    "assets/diagrams": "Editable diagram sources (`.mmd`, `.excalidraw`) and their exports.",
    "assets/images": "Illustrations, screenshots, and figures referenced by lessons.",
    "assets/icons": "Small reusable icons and badges used across the handbook.",
    "assets/cheatsheets": "Printable, repository-wide cheat sheets spanning multiple modules.",
}

MD_CONVENTIONS = (
    "This file follows the repository Markdown standards — see "
    "[CONTRIBUTING.md](%s/CONTRIBUTING.md): one H1 per file, tables over prose, "
    "GitHub callouts (`> [!NOTE]`), fenced code blocks with a language, Mermaid for "
    "diagrams, and relative internal links."
)


def rel(depth: int) -> str:
    """Relative path back to repo root from a given nesting depth."""
    return "../" * depth if depth else "./"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")
    print(f"  wrote {path.relative_to(ROOT)}")


def gitkeep(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)
    (path / ".gitkeep").write_text("", encoding="utf-8")


def title_of(slug: str) -> str:
    return slug.split("-", 1)[1].replace("-", " ")


# --------------------------------------------------------------------------
# Module READMEs
# --------------------------------------------------------------------------
def module_readme(i: int) -> str:
    num, name, purpose, learn, related = MODULES[i]
    slug = f"{num}-{name}"
    title = name.replace("-", " ")
    prev = MODULES[i - 1] if i > 0 else None
    nxt = MODULES[i + 1] if i < len(MODULES) - 1 else None
    prev_link = f"[⬅ {prev[0]} · {prev[1].replace('-', ' ')}](../{prev[0]}-{prev[1]}/README.md)" if prev else "[⬅ docs](../README.md)"
    next_link = f"[{nxt[0]} · {nxt[1].replace('-', ' ')} ➡](../{nxt[0]}-{nxt[1]}/README.md)" if nxt else "[Roadmap ➡](../../ROADMAP.md)"

    learn_md = "\n".join(f"- {x}" for x in learn)
    sub_rows = "\n".join(
        f"| [`{f}/`]({f}/) | {d} |" for f, d in MODULE_SUBFOLDERS.items()
    )
    related_md = "\n".join(
        f"- [{title_of(r)}](../{r}/README.md)" for r in related
    )

    return f"""# Module {num} · {title}

{prev_link} · [🏠 docs](../README.md) · [🗺 Roadmap](../../ROADMAP.md) · {next_link}

> {purpose}

---

## Purpose

This module covers **{title}**. {purpose} It fits into the overall program as described in the [Roadmap](../../ROADMAP.md) and [Curriculum](../../CURRICULUM.md).

## What you'll learn

{learn_md}

## How this module is organized

Content is delivered week by week. Each module uses the same subfolders:

| Folder | Contents |
|---|---|
{sub_rows}

## Suggested study flow

```mermaid
flowchart LR
    R[Read the week] --> E[Do exercises]
    E --> P[Build project]
    P --> Q[Take quiz]
    Q --> F[Review flashcards]
    F --> N[Next week]
```

## File & naming conventions

| Item | Convention | Example |
|---|---|---|
| Weekly lesson | `week-NN.md` | `weeks/week-01.md` |
| Exercise | `exercise-NN.md` (+ `solution-NN.*`) | `exercises/exercise-01.md` |
| Project | `project-NN/` folder with `README.md` | `projects/project-01/` |
| Quiz | `quiz-NN.md` (+ `answers-NN.md`) | `quizzes/quiz-01.md` |
| Flashcards | `deck.md` | `flashcards/deck.md` |
| Diagram | `topic.mmd` / `topic.png` | `diagrams/attention.mmd` |

## Markdown conventions

{MD_CONVENTIONS % "../.."}

## Related modules

{related_md}

---

## Navigation

| Direction | Link |
|---|---|
| ⬆ Parent | [docs/](../README.md) |
| ⬅ Previous | {prev_link} |
| ➡ Next | {next_link} |
| 🗺 Roadmap | [ROADMAP.md](../../ROADMAP.md) |
| 📚 Curriculum | [CURRICULUM.md](../../CURRICULUM.md) |
| 🏠 Repo root | [README.md](../../README.md) |
"""


# --------------------------------------------------------------------------
# Folder READMEs
# --------------------------------------------------------------------------
def folder_readme(name: str, purpose: str, depth: int, extra: str = "") -> str:
    root = rel(depth).rstrip("/") or "."
    display = name if name != "docs" else "docs"
    return f"""# `{name}/`

[🏠 Repo root]({root}/README.md) · [🗺 Roadmap]({root}/ROADMAP.md) · [📁 Structure]({root}/REPOSITORY_STRUCTURE.md)

> {purpose}

---

## Purpose

{purpose}

{extra}

## How to organize files here

- Follow the naming and Markdown conventions in [CONTRIBUTING.md]({root}/CONTRIBUTING.md).
- Keep folder and file names `kebab-case`; module-scoped items are numbered to match `docs/`.
- Every non-trivial subfolder gets its own `README.md`.
- Placeholder `.gitkeep` files hold empty folders until real content lands.

## Navigation

| | |
|---|---|
| ⬆ Parent | [Repo root]({root}/README.md) |
| 🗺 Roadmap | [ROADMAP.md]({root}/ROADMAP.md) |
| 📁 Structure | [REPOSITORY_STRUCTURE.md]({root}/REPOSITORY_STRUCTURE.md) |
"""


def docs_index() -> str:
    rows = "\n".join(
        f"| {num} | [{name.replace('-', ' ')}]({num}-{name}/README.md) | {purpose} |"
        for num, name, purpose, _, _ in MODULES
    )
    return f"""# Documentation — Handbook Modules

[🏠 Repo root](../README.md) · [🗺 Roadmap](../ROADMAP.md) · [📚 Curriculum](../CURRICULUM.md) · [📁 Structure](../REPOSITORY_STRUCTURE.md)

> The handbook itself. Each module is a self-contained folder with weekly lessons, exercises, projects, quizzes, flashcards, cheat-sheets, and references.

---

## Modules

| # | Module | Focus |
|---|---|---|
{rows}

---

## How modules are structured

Every `NN-Name/` module contains the same subfolders — `weeks/`, `diagrams/`, `exercises/`, `projects/`, `quizzes/`, `flashcards/`, `cheat-sheets/`, `references/` — and a `README.md` with navigation. See [REPOSITORY_STRUCTURE.md](../REPOSITORY_STRUCTURE.md).

> [!NOTE]
> Module content is authored one module at a time. Only structure and navigation exist so far — see [CHANGELOG.md](../CHANGELOG.md).
"""


# --------------------------------------------------------------------------
# Templates
# --------------------------------------------------------------------------
TEMPLATES = {
"lesson-template.md": """# <Lesson Title>

[⬅ Prev](#) · [🏠 Module](../README.md) · [Next ➡](#)

| | |
|---|---|
| **Module** | <NN · Name> |
| **Week** | <NN> |
| **Difficulty** | ⭐–⭐⭐⭐⭐⭐ |
| **Est. time** | <minutes> |
| **Prerequisites** | [<lesson>](#) |

## Overview
<What and why, in one paragraph.>

## Learning objectives
- <measurable outcome>

## Intuition
<Plain-language mental model. No math yet.>

> **Illustration placeholder** — `assets/images/<topic>.png`: describe the figure.

## First principles
<Derive the concept from the ground up.>

## Mathematics
<Formal treatment where relevant; define all notation.>

## Code
```python
# Minimal, runnable example
```

## In production
<Real-world usage and pitfalls.>

> [!WARNING]
> <A common, costly mistake.>

## Common mistakes & debugging
| Symptom | Likely cause | Fix |
|---|---|---|
| | | |

## Exercises · Quiz · Flashcards
- Exercises: [`../exercises/`](../exercises/)
- Quiz: [`../quizzes/`](../quizzes/)
- Flashcards: [`../flashcards/`](../flashcards/)

## Summary
| Key idea | Takeaway |
|---|---|
| | |

## Further reading
- <link into RESOURCES.md>
""",

"weekly-summary-template.md": """# Week <NN> Summary · <Module>

[🏠 Module](../README.md) · [🗺 Roadmap](../../../ROADMAP.md)

## What this week covered
- <topic>

## Key takeaways
| Concept | One-line summary |
|---|---|
| | |

## What I built
- <exercise / project>

## Where I struggled
- <weak spot → follow-up plan>

## Flashcards added
- <count / link>

## Next week
- <preview>
""",

"project-template.md": """# Project · <Title>

[🏠 Module](../README.md) · [🗺 Roadmap](../../../ROADMAP.md)

| | |
|---|---|
| **Module** | <NN · Name> |
| **Est. time** | 🛠️ <hours> |
| **Difficulty** | ⭐–⭐⭐⭐⭐⭐ |

## What you'll build
<One paragraph: the deliverable and why it's realistic.>

## Skills exercised
- <skill>

## Requirements
| # | Requirement | Done |
|--:|---|:--:|
| 1 | | ☐ |

## Starter
<Point to `starter/` or describe the blank slate.>

## Stretch goals
- <optional extension>

## Rubric
| Criterion | Weight |
|---|:--:|
| Correctness | 40% |
| Code quality | 20% |
| Production-readiness | 25% |
| Documentation | 15% |

## Reflection
<3–5 sentences after finishing — see the retrospective template.>
""",

"exercise-template.md": """# Exercise · <Title>

[🏠 Module](../README.md)

| | |
|---|---|
| **Lesson** | <NN.M> |
| **Type** | ☐ Implement ☐ Debug ☐ Analyze ☐ Design |
| **Est. time** | <minutes> |

## Goal
<What to produce or figure out.>

## Instructions
1. <step>

## Constraints
- <e.g. no external libraries>

## Hints
<details><summary>Hint 1</summary>
<hint>
</details>

## Solution
See `solution.*`. Try fully before looking.

## Self-check
- [ ] It runs
- [ ] I can explain why it works without looking
""",

"quiz-template.md": """# Quiz · <Module / Week>

[🏠 Module](../README.md)

> <N> questions. Answer from memory first; answers are in `answers.md`.

1. <question>
2. <question>
3. <question>

---

### Scoring
| Score | Meaning |
|---|---|
| 90–100% | Move on |
| 70–89% | Review weak spots |
| < 70% | Redo the week |
""",

"flashcards-template.md": """# Flashcards · <Module / Topic>

[🏠 Module](../README.md)

> Review on the schedule in [LEARNING_STRATEGY.md](../../../LEARNING_STRATEGY.md).

---

**Q:** <question>
**A:** <concise answer>

---

**Q:** <question>
**A:** <concise answer>

---

> [!TIP]
> Keep answers recallable in one breath. Split anything longer into multiple cards.
""",

"architecture-notes-template.md": """# Architecture Notes · <System>

[🏠 Repo root](../README.md)

## Context
<What problem this system solves and for whom.>

## Requirements
| Type | Requirement |
|---|---|
| Functional | |
| Non-functional | |

## High-level design
```mermaid
flowchart LR
    Client --> API --> Service --> Store
```

## Components
| Component | Responsibility | Notes |
|---|---|---|
| | | |

## Data flow
<Describe the request/response and data lifecycle.>

## Tradeoffs & alternatives
| Decision | Chosen | Rejected | Why |
|---|---|---|---|
| | | | |

## Failure modes & mitigations
| Failure | Impact | Mitigation |
|---|---|---|
| | | |

## Open questions
- <question>
""",

"research-paper-summary-template.md": """# Paper Summary · <Title>

[🏠 References](../README.md)

| | |
|---|---|
| **Authors** | |
| **Year / Venue** | |
| **Link** | |
| **Related module** | <NN> |

## Problem
<What gap does this address?>

## Key idea (in one paragraph)
<The core contribution.>

## Method
<How it works — enough to reimplement mentally.>

## Results
| Metric | Result | Baseline |
|---|---|---|
| | | |

## Why it matters for engineers
<Practical implications.>

## Limitations & critiques
- <limitation>

## Terms to add to the glossary
- <term>
""",

"cheat-sheet-template.md": """# Cheat Sheet · <Topic>

[🏠 Module](../README.md)

> One-page quick reference. Optimized for scanning, not learning.

## At a glance
| Thing | Use it for | Gotcha |
|---|---|---|
| | | |

## Common commands / snippets
```text
# key snippets
```

## Decision guide
```mermaid
flowchart TD
    A{Question?} -->|yes| B[Do X]
    A -->|no| C[Do Y]
```

## Remember
- <key point>
""",

"interview-notes-template.md": """# Interview Notes · <Topic / Question>

[🏠 Interview Prep](../README.md)

| | |
|---|---|
| **Category** | ☐ DSA ☐ ML ☐ LLM ☐ System Design ☐ Behavioral |
| **Difficulty** | ⭐–⭐⭐⭐⭐⭐ |

## Question
<Prompt.>

## My approach
<Structured thinking / steps.>

## Ideal answer
<Model answer and why.>

## Follow-ups
- <likely follow-up>

## Mistakes to avoid
- <trap>

## Related
- <topic / module link>
""",

"debugging-session-template.md": """# Debugging Session · <Short Title>

[🏠 Repo root](../README.md)

| | |
|---|---|
| **Date** | <YYYY-MM-DD> |
| **System / lesson** | |
| **Severity** | ☐ blocker ☐ major ☐ minor |

## Symptom
<What went wrong, observed behavior, error messages.>

## Hypotheses
| # | Hypothesis | Test | Result |
|--:|---|---|---|
| 1 | | | |

## Root cause
<What actually caused it.>

## Fix
<What changed, with a code/diff reference.>

## Verification
<How you confirmed it's fixed.>

## Lesson learned
<The durable takeaway — this is the point.>
""",

"project-retrospective-template.md": """# Retrospective · <Project>

[🏠 Module](../README.md)

| | |
|---|---|
| **Project** | |
| **Time spent** | |
| **Outcome** | ☐ shipped ☐ partial ☐ abandoned |

## What went well
- <thing>

## What went badly
- <thing>

## What I learned
- <insight>

## What I'd do differently
- <change>

## Skills to reinforce next
- <topic → link to module>
""",
}


def main() -> None:
    print("Generating repository skeleton...")

    # Module folders + subfolders + READMEs
    docs = ROOT / "docs"
    for i, (num, name, *_ ) in enumerate(MODULES):
        mod = docs / f"{num}-{name}"
        for sub in MODULE_SUBFOLDERS:
            gitkeep(mod / sub)
        write(mod / "README.md", module_readme(i))

    # docs index
    write(docs / "README.md", docs_index())

    # Top-level folder READMEs
    for name, purpose in TOP_FOLDERS.items():
        (ROOT / name).mkdir(parents=True, exist_ok=True)
        if name == "docs":
            continue  # handled above
        write(ROOT / name / "README.md", folder_readme(name, purpose, depth=1))

    # Assets + subfolders
    (ROOT / "assets").mkdir(exist_ok=True)
    write(ROOT / "assets" / "README.md",
          folder_readme("assets", "Static assets: diagrams, images, icons, and printable cheat sheets.", depth=1))
    for name, purpose in ASSET_FOLDERS.items():
        gitkeep(ROOT / name)
        write(ROOT / name / "README.md", folder_readme(name, purpose, depth=2))

    # Templates
    tdir = ROOT / "templates"
    tdir.mkdir(exist_ok=True)
    for fname, body in TEMPLATES.items():
        write(tdir / fname, body)

    print("Done.")


if __name__ == "__main__":
    main()
