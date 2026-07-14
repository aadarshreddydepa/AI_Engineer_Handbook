# ✅ Answers · Module 07 Quiz 01

[🏠 Module 07](../README.md) · [❓ Questions](quiz-01.md)

> Model answers **with the reasoning**. If you got the gist but not the *why*, reread the linked lesson — and run the code.

---

## Part 1 — Lifecycle, NumPy, Pandas

**1.** **Code bugs are loud; data bugs are silent.** A code bug gives you a stack trace, a failing test, and a pager alert — you know in milliseconds. **A data bug gives you nothing**: the model trains fine, the loss drops, the dashboards stay green, and the model is **confidently and systematically wrong for months.** And AI *amplifies* it — a traditional program with bad data returns one wrong answer; a model **internalizes** the badness and applies it to every input forever, with high confidence. → [07.1](../weeks/07.1-data-lifecycle.md)

**2.** Raw → Collection → **Validation** → Cleaning → Transformation → **Feature Engineering** → Storage → Training → Evaluation → Deployment → **Monitoring**.
**The most important arrow is the one from Monitoring back to Raw.** The lifecycle is a **loop** — the world keeps changing, so a static model is a decaying model. Teams that draw it as a straight line ship once and then spend a year confused about why the numbers keep getting worse. → [07.1](../weeks/07.1-data-lifecycle.md)

**3.**
- **Leakage** — information available at training but not at prediction time. **Detect:** *"at prediction time, would I actually have this value?"* Plus: a suspiciously high correlation with the target, or one feature dominating importance.
- **Training/serving skew** — features computed differently in prod than in training. **Detect:** the skew test (batch-transform must equal single-row transform).
- **Drift** — the world changed. **Detect:** PSI/KS on the **input** distributions (not model performance, which needs labels that arrive months late). → [07.1](../weeks/07.1-data-lifecycle.md)

**4.** A list is a **box of pointers to scattered 28-byte `PyFloat` objects**; an array is **one contiguous block of raw bytes**. Five mechanisms: **(1)** no Python object boxing/unboxing, **(2)** no interpreter dispatch per element (one C call), **(3)** **SIMD** (8–16 elements per instruction), **(4)** cache locality (the prefetcher works), **(5)** threaded BLAS for linear algebra. → [07.2](../weeks/07.2-numpy.md)

**5.** **Views:** basic slicing (`a[1:5]`), `.T`, `.reshape()`, `.ravel()`. **Copies:** fancy indexing (`a[[1,3]]`), boolean indexing (`a[a>5]`), `.copy()`, arithmetic.
**It causes silent bugs because modifying a view mutates the original — with no error raised.** You slice a training set, normalize the slice in place, and silently corrupt the source array (including your test set). **`.copy()` when you intend to mutate.** → [07.2](../weeks/07.2-numpy.md)

**6.** A DataFrame is a **dict of columns**, each a NumPy array, sharing one **Index**. A column is one contiguous array; a **row cuts across every column** (different dtypes, different arrays).
**What follows:** `df.iterrows()` is ~10,000× slower than vectorized (it builds a **new Series object per row**), the entire Pandas idiom is column-oriented, and the Index is an **alignment key** — arithmetic aligns on labels, so a mismatched index gives you **NaN, not an error**. → [07.3](../weeks/07.3-pandas-fundamentals.md)

**7.** **Chained indexing.** `df[mask]['col'] = x` — `df[mask]` returns a new object that **may be a view or a copy** of the underlying buffer, and **Pandas cannot always tell which**. So the assignment goes to a temporary that may be immediately discarded. **Sometimes it works, sometimes it silently doesn't** — and that non-determinism is exactly why it warns.
**Fix:** one call — `df.loc[mask, 'col'] = x`. And for an independent subset, say so: `sub = df[mask].copy()`. → [07.3](../weeks/07.3-pandas-fundamentals.md)

**8.** **`df['country'] = df['country'].astype('category')`**, plus downcasting `int64` → `int32` and `float64` → `float32`.
**The mechanism:** an `object` column stores a **pointer to a separate Python string object for every row** — a million rows of `"US"` stores a million pointers. A **`category`** stores the four unique values **once** plus a compact integer code array. **This is the single biggest memory win in Pandas (10–50× on low-cardinality strings) and almost nobody uses it.** → [07.3](../weeks/07.3-pandas-fundamentals.md), [07.10](../weeks/07.10-performance.md)

**9.** **(1) Typed** — CSV has no schema, so every read is a *guess* (is `007` a string or 7?), and the same code can behave differently on different files. **(2) Columnar** — read only the columns you need (3 of 200 = 1.5% of the I/O), and adjacent similar values **compress far better**. **(3) Predicate pushdown** — min/max statistics per row-group let a filter **skip whole blocks without decompressing them**. Net: ~5× smaller, ~10× faster. → [07.3](../weeks/07.3-pandas-fundamentals.md), [07.10](../weeks/07.10-performance.md)

---

## Part 2 — Combining, Cleaning, EDA

**10.** **Row explosion** = a many-to-many merge produces a **cartesian product**. Two duplicate keys × two duplicate keys = **four rows**. Every metric is inflated, and **no error is raised**.
**`validate=` raises if the key-uniqueness assumption is violated.** Pass **`'one_to_many'`** — it's what you almost always mean (the left key is unique). **It costs nothing and turns a silent catastrophe into a loud exception.** Also: know your **grain** ("one row per what?") before you merge. → [07.4](../weeks/07.4-pandas-advanced.md)

**11.** **`agg`** → one row per group (summaries). **`transform`** → **same shape as the input** — it broadcasts the group statistic back onto **every row**. **`filter`** → keeps whole groups meeting a condition.
**`transform` builds features**, and it's powerful because *"how does this row compare to its group?"* is one of the most predictive patterns in all of commercial ML: a customer's spend vs. their segment's average, a product's price vs. its category's median. **A $500 item is cheap for a laptop and outrageous for a phone case — the raw price doesn't know that; the ratio does.** → [07.4](../weeks/07.4-pandas-advanced.md)

**12.** ⭐ **`.rolling(7)` at row *t* averages rows *t−6 … t* — including row *t* itself.** If you're predicting the value at *t*, that feature **contains the answer**. Your model scores 0.99 offline, and in production the current value is **unknown by definition**, so the feature is garbage.
```python
df['avg_7d'] = df['sales'].shift(1).rolling(7).mean()   # ✅ window ends YESTERDAY
```
**This is the most common leakage bug in applied ML, and it hides in a single missing method call.** → [07.4](../weeks/07.4-pandas-advanced.md)

**13.** **`bfill()` fills a gap with a *future* value** — information that did not exist at that moment. It's the same sin as the un-shifted rolling window, wearing a different hat. **`ffill()` carries the *past* forward, which is information you actually had.** **In a time series, information may only flow forward.** → [07.4](../weeks/07.4-pandas-advanced.md)

**14.** ⭐
- **MCAR** (Missing Completely At Random) — no pattern (a dropped packet). ✅ Safe to impute or drop.
- **MAR** (Missing At Random) — depends on **other observed** columns (older users skip the income field). 🟡 Impute **conditionally** on those columns.
- **MNAR** (Missing Not At Random) — depends on **the missing value itself** (**high earners refuse to state their income**). ❌ **Never impute — the missingness IS the signal.**

**The MNAR test (and almost nobody runs it):** compare the **target rate** for rows where the column is missing vs. present.
```python
df.loc[df[col].isna(), 'target'].mean()  vs  df.loc[df[col].notna(), 'target'].mean()
```
**If they differ sharply, the missingness is predictive.** Imputing destroys it. **Add the flag** — it's often *more* predictive than the column it came from. → [07.5](../weeks/07.5-data-cleaning.md)

**15.** Real data doesn't use `NaN` — it uses **`-1`, `999`, `"N/A"`, `""`, `"unknown"`**. Pandas treats them as **legitimate values** and happily includes them in `.mean()`, `.std()`, and every model you train.
**So `df['age'].mean()` returns 43.7 and it's a lie, and nothing anywhere will tell you.** This is the concrete form of "data bugs are silent."
**The fastest way to find it: plot a histogram.** A spike at exactly `-1` in an otherwise smooth distribution is **instantly obvious in a plot and completely invisible in `describe()`**. → [07.5](../weeks/07.5-data-cleaning.md), [07.8](../weeks/07.8-visualization.md)

**16.** **The z-score is self-defeating on data that has outliers — which is exactly when you'd use it.** The outlier **inflates the standard deviation it's being compared against**, so extreme values **hide themselves**. One value of 1,000,000 in a column of ~50s can have |z| < 3, because it single-handedly dragged σ up to 300,000.
**Use IQR (1.5×) or MAD** — both built on **medians**, which don't move. → [07.5](../weeks/07.5-data-cleaning.md)

**17.** ⭐ **There is no universal rule — and that's the answer.**
- **$10M mansion** → **Cap / winsorize.** It's a real house, but MSE squares the error, so one outlier can contribute 900× the loss and dominate training.
- **Corrupt JPEG** → **Remove.** It's an error, and it will crash training at epoch 3.
- **Black Friday** → **KEEP IT.** It is not an error — **it's the day the business most needs predicted.** An IQR filter would helpfully delete it, and your model would be accurate on boring Tuesdays and blind on the days that matter. **Add a holiday/promotion feature that explains the spike; never erase it.**

**The question is never "how do I remove outliers?" It is "is this an error, a rare event, or the entire point?"** And in fraud detection, **the outliers are the positive class.** → [07.5](../weeks/07.5-data-cleaning.md), [07.12](../weeks/07.12-case-studies.md)

**18.** ⭐ **Fit the scaler on the TRAINING set. Only. Ever.** Then apply those saved μ and σ to the test set and to production.
- **Violate it in evaluation:** the test set's values influenced the mean, so **information from your test set entered your training data**. Your evaluation is optimistic and **you no longer know how good your model is.**
- **Violate it in production:** at inference you have *one row* — **you cannot compute a mean.** If serving recomputes the scaling on live data, you have **training/serving skew**. (And a `StandardScaler` refit on a single row outputs **exactly zero for every feature** — a single value's deviation from its own mean is 0. **Your model silently receives all-zeros.**)

**The fitted μ and σ are model artifacts — version them alongside the weights.** This is exactly what sklearn's `fit`/`transform` split exists to enforce. → [07.5](../weeks/07.5-data-cleaning.md), [07.11](../weeks/07.11-pipelines.md)

---

## Part 3 — Features, Visualization, Quality

**19.** A better model buys **+3–8%**. Hyperparameter tuning buys **+1–3%**. **The right domain features buy +10–40%.** Every Kaggle competition is won on features — the top 100 teams all use gradient boosting with near-identical hyperparameters; **the difference between rank 1 and rank 500 is what they fed it.**
**When it stops being true:** for **unstructured data** (images, audio, raw text), **deep learning learns the features for you** — that's literally what the deep learning revolution *was* (CNNs replaced hand-crafted SIFT/HOG). **But for tabular data — most business ML — feature engineering still dominates, and gradient boosting on good features still beats deep learning.** → [07.7](../weeks/07.7-feature-engineering.md)

**20.** **Not as an integer.** Hour 23 and hour 0 are **one hour apart**, but numerically they're 23 apart — the model learns a **discontinuity that doesn't exist**.
```python
df['hour_sin'] = np.sin(2*np.pi*df.hour/24)
df['hour_cos'] = np.cos(2*np.pi*df.hour/24)
```
**Why two columns?** Because **`sin` alone is ambiguous** — `sin(2π·3/24) == sin(2π·9/24)`, so 3 a.m. and 9 a.m. would map to the same value. **The (sin, cos) pair is a unique point on the unit circle**, so 23:00 and 00:00 land adjacent — exactly as they should. (Same geometry as Transformer positional encoding.) → [07.7](../weeks/07.7-feature-engineering.md)

**21.** ⭐ **Tree feature importance lies in two specific ways:** it's **biased toward high-cardinality features** (more possible splits = more chances to look useful), and when two features are **correlated it splits the credit**, so both look unimportant even though the pair is essential.
**Permutation importance asks the question you actually care about:** *"if I destroyed this feature, how much worse would the model get?"*
**Compute it on the VALIDATION set, not train** — on train, an overfit model will happily insist that its memorized noise features are critical.
**And: a feature with 95% of the importance is a leak.** Feature importance is one of the best leak detectors you have. → [07.7](../weeks/07.7-feature-engineering.md)

**22.** ⭐ **The six rules:**
1. **Fit transformers (scalers, encoders, imputers, vectorizers) on TRAIN only.**
2. **`.shift(1)` before every rolling window.**
3. **Out-of-fold target encoding** (naive `groupby.transform('mean')` hands each row its own label).
4. **Respect the `as_of_date`** — filter `t < as_of` **first**, structurally.
5. **Never `bfill` a time series.**
6. **Fit vectorizers on train** (TF-IDF vocabulary from train texts only).

**The universal test:**
```python
def test_no_leakage(df, as_of):
    baseline = build_features(df, as_of)
    poisoned = df.copy()
    poisoned.loc[poisoned.date > as_of, 'amount'] *= 1000    # absurd FUTURE value
    assert baseline.equals(build_features(poisoned, as_of)), "🚨 LEAKAGE"
```
**Perturb the future. Rebuild. Assert nothing changed.** This single test is worth more than every other test in your pipeline, and almost nobody writes it. **Put it in CI.** → [07.7](../weeks/07.7-feature-engineering.md), [07.11](../weeks/07.11-pipelines.md)

**23.** **(1) Bimodality** — two populations mixed together (often **two units** or two data sources — a weight column that's 30% pounds and 70% kilograms contains **no individually invalid value** and will pass every range check). **(2) A sentinel spike** at exactly `-1` / `0` / `999`. **(3) Truncation** — a hard wall at 100 means the data was capped upstream. **(4) Skew shape** — which tells you whether to `log1p`.
**None of these appear in `describe()`.** And Anscombe's quartet / the Datasaurus Dozen prove the point: **identical mean, variance, and correlation; wildly different data, one of which is a dinosaur.** → [07.8](../weeks/07.8-visualization.md)

**24.** **Correlation has a meaningful midpoint — zero.** With a **sequential** colormap (`viridis`, `Blues`), **−0.9 and 0.0 look similarly "low"** — which is exactly backwards, because **−0.9 is a strong relationship**. A diverging map (`RdBu_r`, `vmin=-1, vmax=1`) makes strong-negative and strong-positive both visually loud, and zero the quiet middle. **This is the single most common mistake in correlation heatmaps, and it hides half your findings.** → [07.8](../weeks/07.8-visualization.md)

**25.** ⭐ **FRESHNESS and VOLUME.**
- **Freshness** (`now() - max(updated_at) < SLA`) catches: the pipeline silently stopped, the upstream job failed, the API key expired, a cron didn't fire. **A stale table looks completely healthy** — every value in it is perfectly valid; it's just from last Tuesday. **Your model has been making decisions on week-old data and nothing will tell you.**
- **Volume** (row count within a band of the baseline) catches: partial loads, broken filters, exploded joins, a source returning empty pages. **Half the expected rows is a silent catastrophe.**

**These two catch the majority of real production data incidents, and they take about twenty lines to write.** Everything else in data quality is refinement. → [07.9](../weeks/07.9-data-quality.md)

---

## Part 4 — Performance, Pipelines, Case Studies

**26.** **0 · Profile** (the bottleneck is never where you think) → **1 · Vectorize** (100–10,000×) → **2 · Dtypes** (`category`, downcast — 2–50× memory) → **3 · Parquet** (5–100×) → **4 · Read fewer columns** → **5 · Chunk** → **6 · Change tool** (Polars, **DuckDB**) → **7 · Distribute** (Dask, Spark).
**Distributed computing is LAST because it adds a cluster, a scheduler, a serialization boundary, a debugging nightmare, a bill — and a much wider privacy blast radius** (your PII now lives in every executor's memory, shuffle spills, and logs).
**Climb in order and stop the moment the job is fast enough.** The overwhelming majority of "we need Spark" conversations are actually "we're reading a 40 GB CSV with `object` dtypes inside a `for` loop." → [07.10](../weeks/07.10-performance.md)

**27.** **Chunkable:** sum, count, min, max (combine the partials); mean (track sum and count separately). **Not chunkable:** **median, exact `nunique`, quantiles, joins, sort** — they need **all the data at once**.
**Why that's the real signal:** **big files chunk fine.** A 500 GB file of sums is trivial. **It's the *operation* that forces your hand** — the moment you need a median or a join across the whole dataset, chunking stops being an option and you need an out-of-core engine (**DuckDB**) or a distributed one. **"The file is big" is not a reason to reach for Spark. "The operation doesn't decompose" is.** → [07.10](../weeks/07.10-performance.md)

**28.** ⭐ **Hidden state.** You define `df` in cell 3, modify it in cell 8, **delete cell 8** — and cell 12 still works, because `df` is still in memory. **The notebook now produces a result that its own code cannot reproduce.** Restart the kernel, run all, and it breaks.
This is not hypothetical; **it is the single most common way analysis results become irreproducible.** Plus: no tests, unreviewable JSON diffs, no error handling, no idempotency.
**Notebooks are excellent for exploration and disqualifying for production.** The failure isn't using them — it's **shipping** them. **Explore in a notebook; extract the logic into functions the notebook imports.** → [07.11](../weeks/07.11-pipelines.md)

**29.** ⭐ **The skew test:** batch-transforming N rows must **equal** transforming them one at a time.
```python
batch  = pipeline.transform(sample_df)
single = pd.concat([pipeline.transform(sample_df.iloc[[i]]) for i in range(len(sample_df))])
pd.testing.assert_frame_equal(batch.reset_index(drop=True), single.reset_index(drop=True))
```
**What it catches:** any step that computes **across rows** — a mean, a rank, a frequency count, a groupby, **or a scaler that refits on the incoming batch.**
**The disaster:** in training you have 100,000 rows; in production you have **one**. A `StandardScaler` that refits will, on a single row, produce **exactly zero for every feature** (a value's deviation from its own mean is 0). **Your model receives all-zeros in production, returns garbage, and raises no error.** This test finds it in ten seconds. → [07.11](../weeks/07.11-pipelines.md)

**30.** ⭐ **You're forecasting *h* days ahead.** If training ends March 7th and testing starts March 8th, then a feature like `roll_7_mean` for the March 8th test row uses data from **March 1–7 — which is in your training set.** The model has effectively seen the recent past of its test period, and your validation is **optimistic**.
**Insert a gap equal to your forecast horizon.** Train through March 1st, **gap March 2–7**, test from March 8th.
```python
assert train.index.max() + pd.Timedelta(days=HORIZON) < test.index.min()
```
**One assertion. Catches the most common forecasting bug there is. Almost nobody writes it.** → [07.12](../weeks/07.12-case-studies.md)

---

## 🏁 Bonus

**B1 — 0.94 offline, 0.71 in production. Five hypotheses, ranked:**

1. **Leakage** (most likely) — a feature the model won't have at prediction time, an un-shifted rolling window, naive target encoding, a target-derived feature, or a random split on temporal data. **The offline number was fiction.**
   *Distinguish:* run the leakage hunt (correlation > 0.9 with target; one feature dominating importance); run the perturb-the-future test; check whether a date column exists and whether you random-split.
2. **Training/serving skew** — features computed differently in prod. *Distinguish:* run the **skew test** (batch vs single-row); compare the feature distributions in training vs. production logs. **A scaler refit at inference outputs all-zeros.**
3. **Drift** — the world changed since training. *Distinguish:* **PSI per feature** between the training and production distributions. PSI > 0.25 → retrain.
4. **A broken train/test split** — duplicates straddling it (text/images), or **group leakage** (same patient/product/photographer in both).
5. **Data quality** — a stale or partially-loaded table upstream. *Distinguish:* **check freshness and volume first** — it's the cheapest check and it's a surprisingly common answer.

→ [07.1](../weeks/07.1-data-lifecycle.md), [07.9](../weeks/07.9-data-quality.md), [07.12](../weeks/07.12-case-studies.md)

**B2 — The signature leakage trap per case study:**

| Case study | The trap |
|---|---|
| **Churn** | **Post-event columns** (`cancellation_reason` only exists *because* they churned) — plus **survivorship bias** (`SELECT * FROM active_customers` excludes everyone who already left) |
| **House prices** | **Target-derived features** (`price_per_sqft` contains `sale_price`) — and **imputing structurally-absent values** (`pool_quality = NaN` means *there is no pool*, not "unknown") |
| **Sentiment** | **Duplicate reviews** (5–15% is typical) straddling a random split — the model **memorizes** them |
| **Images** | **Group leakage** (same patient/photographer in both splits — *the #1 failure in medical imaging ML*) and **metadata leakage** (the portable X-ray marker → pneumonia; the model never looked at the lungs) |
| **Forecasting** | The **un-shifted rolling window**, and **no gap** in the validation split |

→ [07.12](../weeks/07.12-case-studies.md)

**B3 — The first hour with a new dataset:**

1. **`df.info()`** — rows, dtypes, nulls, memory. Four bugs in one command.
2. **`df.describe(percentiles=[.01,.5,.99])`** — and read the **median beside the mean**.
3. **Plot a histogram of every numeric column.** Hunt for **sentinel spikes**, bimodality, truncation.
4. **Missingness report** — count, %, and the **MNAR test** (target rate for missing vs. present).
5. **Duplicates** — exact rows, and business keys.
6. **Check the target**: class balance (imbalanced → PR-AUC, stratify, tune the threshold) or skew (→ `log1p`).
7. **🚨 Run the leakage hunt** — correlation with target > 0.9? Single-feature AUC > 0.95? Suspicious column names (`cancel`, `final`, `reason`, `_after`)?
8. **Look for a date column.** **If one exists, you cannot random-split.**
9. **Ask: "how will this model actually be used?"** — that determines the grain, the split, and the metric.

**Only then do you write a line of modelling code.** → [07.6](../weeks/07.6-eda.md), [07.12](../weeks/07.12-case-studies.md)

**B4 — The ten sentences:**
1. **Data bugs are silent.** No stack trace, no failing test, confidently wrong for months.
2. **Leakage looks like success.** A suspiciously good result is a **bug report**.
3. **"At prediction time, would I actually have this value?"**
4. **`.shift(1)` before every rolling window.**
5. **Fit on train only** — and make it **structural**, not disciplinary.
6. **Every `fillna` is a claim about the world.**
7. **A `-1` in an age column** makes every statistic a lie. **Plot it.**
8. **Understand the outlier before you delete it.** It might be Black Friday.
9. **A stale table looks perfectly healthy.**
10. **Features beat models** — and **nobody can download your data**.

---

> [!TIP]
> **Turn every missed question into a flashcard.** And for anything in Parts 2–4 you fumbled: **don't reread — build the bug.** Create the leak, watch the score inflate, then write the test that catches it. **Data work is the one field where you can construct the disaster and prove your defences work** — and that beats any answer key.

---

[❓ Questions](quiz-01.md) · [🧠 Flashcards](../flashcards/deck.md) · [📄 Cheat sheet](../cheat-sheets/data-cheatsheet.md) · [🏠 Module 07](../README.md)
