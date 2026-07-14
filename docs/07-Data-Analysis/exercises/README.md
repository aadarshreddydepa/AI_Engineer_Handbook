# 🏋️ Module 07 · Data Analysis — Exercises

[🏠 Module 07](../README.md) · [📖 Lessons](../weeks/README.md) · [📝 Quiz](../quizzes/quiz-01.md)

> Every lesson has its own exercise set. This page is the **index** plus the exercises that span the whole module — the ones where the lessons collide.

> [!IMPORTANT]
> **Do all of this on a dataset that fights back.** Not Iris. Not the pre-cleaned Titanic. **Find data with real problems** — a Kaggle competition, a government open-data CSV, an export from your own company. **Clean data teaches you nothing**, because the entire skill of this module is *what you do when the data is wrong*.

---

## Per-lesson exercises

| Lesson | Exercise types |
|---|---|
| [07.1 Data Lifecycle](../weeks/07.1-data-lifecycle.md#-exercises) | Conceptual · analysis · architecture design |
| [07.2 NumPy](../weeks/07.2-numpy.md#-exercises) | Conceptual · NumPy · performance |
| [07.3 Pandas I](../weeks/07.3-pandas-fundamentals.md#-exercises) | Conceptual · Pandas · cleaning |
| [07.4 Pandas II](../weeks/07.4-pandas-advanced.md#-exercises) | Merging · grouping · **windows & leakage** |
| [07.5 Data Cleaning](../weeks/07.5-data-cleaning.md#-exercises) | Missingness · outliers · encoding · **fairness** |
| [07.6 EDA](../weeks/07.6-eda.md#-exercises) | Dataset analysis · statistics · **the leakage hunt** |
| [07.7 Feature Engineering](../weeks/07.7-feature-engineering.md#-exercises) | Feature building · importance · **leakage tests** |
| [07.8 Visualization](../weeks/07.8-visualization.md#-exercises) | **Visualization challenges** |
| [07.9 Data Quality](../weeks/07.9-data-quality.md#-exercises) | Schema · checks · drift |
| [07.10 Performance](../weeks/07.10-performance.md#-exercises) | Benchmarking · memory · scale |
| [07.11 Pipelines](../weeks/07.11-pipelines.md#-exercises) | Design · reproducibility · **skew tests** |
| [07.12 Case Studies](../weeks/07.12-case-studies.md#-exercises) | **Five end-to-end assignments** |

---

## 🔗 Cross-lesson exercises

**These are the valuable ones.** Each forces two or more lessons to fuse.

### 1 · The Silent Bug Hunt ⭐⭐

The whole module in one exercise. **Do this first.**

1. Take a dataset you consider "clean." One you've used before.
2. Run `df.info()` and `df.describe()`. Note what looks fine.
3. **Plot a histogram of every numeric column.** ([07.8](../weeks/07.8-visualization.md))
4. Look for: a spike at `-1` / `0` / `999`; bimodality; a hard wall (truncation).
5. Compute the **mean and median** of every column. Where do they diverge? ([07.6](../weeks/07.6-eda.md))
6. Check for **duplicate rows** and **duplicate business keys**.
7. Compute the **correlation of every feature with the target**. **Anything above 0.9?**

> **You will find something.** Everyone does. **That's the exercise** — the bug was there the whole time, and `describe()` never mentioned it.

### 2 · The Leakage Gauntlet ⭐⭐

Build the **same model six times**, each with a different leak. Report the (fake) score each time.

| Version | The leak | Expected |
|---|---|---|
| 1 | Honest baseline | The truth |
| 2 | `StandardScaler` fit on **all** data | Slightly inflated |
| 3 | `.rolling(7)` **without** `.shift(1)` | Wildly inflated |
| 4 | **Naive** target encoding | Near-perfect |
| 5 | **Random split** on time-series data | Very inflated |
| 6 | A **post-event** column included | ~0.99 |

**Then write the test that catches each one.** ([07.7](../weeks/07.7-feature-engineering.md), [07.11](../weeks/07.11-pipelines.md))

> **The gap between version 1 and version 6 is the most persuasive number you will ever put in a portfolio**, because it proves you understand something most practitioners don't.

### 3 · From Notebook to Pipeline

1. Find a real Kaggle notebook (someone else's) that does EDA + cleaning + features.
2. **Restart the kernel and run all.** Does it work? (Often: no.) ([07.11](../weeks/07.11-pipelines.md))
3. Extract every transformation into a **pure function**.
4. Wrap them in a `fit`/`transform` pipeline.
5. **Find the leakage** the notebook contains. (It will contain some.)
6. Write the five CI tests: leakage, skew, idempotence, reproducibility, purity.

> This exercise converts you from someone who *writes analysis* into someone who *ships data systems*.

### 4 · The 10× Speedup

1. Take a slow Pandas script (or write a deliberately naive one).
2. **Profile it.** Where is the time actually going? (Not where you think.) ([07.10](../weeks/07.10-performance.md))
3. Apply the ladder in order and **measure after each rung**:
   vectorize → dtypes → Parquet → column pruning → chunk → DuckDB.
4. **Report the cumulative speedup and memory reduction at each step.**
5. Now do the same job in **DuckDB with 5 lines of SQL**. Compare.

### 5 · The Honest Report ⭐

Take any dataset and produce the artifact a senior engineer would trust:

1. Data quality report: nulls, sentinels, duplicates, ranges. ([07.9](../weeks/07.9-data-quality.md))
2. EDA report where **every finding maps to a decision**. ([07.6](../weeks/07.6-eda.md))
3. The **leakage hunt**, run before any modelling.
4. A recommended split, **justified by how the model will be used**. ([07.12](../weeks/07.12-case-studies.md))
5. Every metric reported with a **confidence interval and an `n`**. ([06.6](../../06-Mathematics/weeks/06.6-statistics.md))

**One page. No charts without a conclusion.**

### 6 · The Privacy Audit

Go through a real project of yours and answer:

1. Which columns are **PII**? Which are **proxies** for protected attributes? ([07.6](../weeks/07.6-eda.md))
2. Are any **notebook outputs** committed to git? ([07.1](../weeks/07.1-data-lifecycle.md))
3. Does any **grouped summary** contain a group of size 1? ([07.4](../weeks/07.4-pandas-advanced.md))
4. Do your **logs** ever print a field value? ([07.9](../weeks/07.9-data-quality.md))
5. Does any **Plotly HTML** you've shared embed PII in `hover_data`? ([07.8](../weeks/07.8-visualization.md))
6. If a user requested deletion, **how many places would you have to look?** ([07.11](../weeks/07.11-pipelines.md))

> **This is the exercise nobody wants to do, and it's the one most likely to find something real.**

---

## 🧩 Blank-page recall

Close every tab. On a blank page, from memory:

1. Draw the **eleven-stage lifecycle**. Mark where the loop closes.
2. Name the **three killers** (leakage, skew, drift) and how you'd detect each.
3. State the **six leakage rules**.
4. Write the **universal leakage test** in code.
5. Explain **MCAR / MAR / MNAR** and what you do for each.
6. State the **scaling leakage rule** and why it's structural, not disciplinary.
7. Write the correct **rolling-mean feature** for a forecasting model.
8. Name the **two highest-value data quality checks** and why.
9. State the **optimization ladder** in order.
10. Recite the **ten sentences** from the [cheat sheet](../cheat-sheets/data-cheatsheet.md).

> [!TIP]
> **Blank-page recall is brutal and it is the single most effective study technique there is.** Whatever you can't produce from an empty page, you don't know — regardless of how familiar it felt while reading.

---

## ✅ Solutions

Solutions are **deliberately not provided**. Verification is built in instead — and it's better than an answer key:

| Exercise type | How you know you're right |
|---|---|
| Vectorization | `np.allclose(loop_result, vectorized_result)` — **and time both** |
| Cleaning function | `clean(clean(df)).equals(clean(df))` — **idempotence** |
| Feature pipeline | **Perturb the future → assert nothing changed** |
| Scaler / encoder | Fit on train, snapshot the params, transform test, **assert the params are unchanged** |
| Skew | `transform(batch) == concat([transform(row) for row in batch])` |
| Data quality check | **Deliberately corrupt the data. Does the check fire?** |
| Performance | Measure. The number is the answer |
| Leakage | **Compare the honest score to the leaked score.** The gap is the proof |

> **Data work has a property most subjects lack: you can build the bug and watch your test catch it.** That's a stronger form of verification than any solutions manual, because it tells you not just *that* you're right but *that your defences work*.

---

[⬆ Module 07](../README.md) · [📖 Lessons](../weeks/README.md) · [🧠 Flashcards](../flashcards/deck.md) · [📝 Quiz](../quizzes/quiz-01.md)
