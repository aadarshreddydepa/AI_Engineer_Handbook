# Module 07 · Data Analysis

[⬅ 06 · Mathematics](../06-Mathematics/README.md) · [🏠 docs](../README.md) · [🗺 Roadmap](../../ROADMAP.md) · [08 · Machine Learning ➡](../08-Machine-Learning/README.md)

> Turning raw data into insight with NumPy, pandas, and visualization.

---

## Purpose

This module covers **Data Analysis**. Turning raw data into insight with NumPy, pandas, and visualization. It fits into the overall program as described in the [Roadmap](../../ROADMAP.md) and [Curriculum](../../CURRICULUM.md).

## What you'll learn

- NumPy vectorization and array thinking
- pandas for data wrangling
- Exploratory data analysis (EDA)
- Visualization and communicating findings

## 📖 Lessons (start here)

> ✅ **This module's content is written.** Work through the lessons in order via the [lesson index](weeks/README.md). **Do it against a dataset that fights back** — not Iris, not the cleaned Titanic. The entire skill is what you do when the data is wrong.

| # | Lesson |
|---|---|
| 07.1 | [The AI Data Lifecycle](weeks/07.1-data-lifecycle.md) |
| 07.2 | [NumPy — Internals & Performance](weeks/07.2-numpy.md) |
| 07.3 | [Pandas I — Series, DataFrames & Indexing](weeks/07.3-pandas-fundamentals.md) |
| 07.4 | [Pandas II — Combining, Grouping & Time](weeks/07.4-pandas-advanced.md) |
| 07.5 | [Data Cleaning](weeks/07.5-data-cleaning.md) |
| 07.6 | [Exploratory Data Analysis](weeks/07.6-eda.md) |
| 07.7 | [Feature Engineering](weeks/07.7-feature-engineering.md) |
| 07.8 | [Visualization](weeks/07.8-visualization.md) |
| 07.9 | [Data Quality](weeks/07.9-data-quality.md) |
| 07.10 | [Performance & Scale](weeks/07.10-performance.md) |
| 07.11 | [Reusable Data Pipelines](weeks/07.11-pipelines.md) |
| 07.12 | [Real AI Case Studies](weeks/07.12-case-studies.md) |
| 07.13 | [Projects & Summary](weeks/07.13-projects-summary.md) |

**Companion artifacts:** [Exercises](exercises/README.md) · [Quiz](quizzes/quiz-01.md) · [Flashcards](flashcards/deck.md) · [Cheat sheet](cheat-sheets/data-cheatsheet.md)

> [!IMPORTANT]
> **You will spend 60–80% of your career as an AI Engineer on the work in this module, and roughly 0% of the glory.** Model architecture is what gets talked about; **data quality is what determines whether the model works.** A mediocre model on excellent data beats a state-of-the-art model on garbage, every time, and it isn't close.
>
> The single idea running through all thirteen lessons: **the thing that will destroy your model does not raise an exception.** Leakage, skew, drift, a `-1` sentinel, a silent row explosion, a stale table — none of them crash, all of them produce a model that looks excellent and is worthless. **Everything here is a technique for making the silent things loud.**

## How this module is organized

Content is delivered week by week. Each module uses the same subfolders:

| Folder | Contents |
|---|---|
| [`weeks/`](weeks/) | Weekly lesson content, one file per week (`week-01.md`, `week-02.md`, …). |
| [`diagrams/`](diagrams/) | Mermaid sources and exported diagram assets for this module. |
| [`exercises/`](exercises/) | Hands-on practice problems with solutions. |
| [`projects/`](projects/) | Buildable projects that apply this module's skills. |
| [`quizzes/`](quizzes/) | Self-assessment question banks with answer keys. |
| [`flashcards/`](flashcards/) | Spaced-repetition Q/A decks for active recall. |
| [`cheat-sheets/`](cheat-sheets/) | One-page quick references for this module. |
| [`references/`](references/) | Paper summaries and deep-dive notes. |

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

This file follows the repository Markdown standards — see [CONTRIBUTING.md](../../CONTRIBUTING.md): one H1 per file, tables over prose, GitHub callouts (`> [!NOTE]`), fenced code blocks with a language, Mermaid for diagrams, and relative internal links.

## Related modules

- [SQL](../05-SQL/README.md)
- [Machine Learning](../08-Machine-Learning/README.md)

---

## Navigation

| Direction | Link |
|---|---|
| ⬆ Parent | [docs/](../README.md) |
| ⬅ Previous | [⬅ 06 · Mathematics](../06-Mathematics/README.md) |
| ➡ Next | [08 · Machine Learning ➡](../08-Machine-Learning/README.md) |
| 🗺 Roadmap | [ROADMAP.md](../../ROADMAP.md) |
| 📚 Curriculum | [CURRICULUM.md](../../CURRICULUM.md) |
| 🏠 Repo root | [README.md](../../README.md) |
