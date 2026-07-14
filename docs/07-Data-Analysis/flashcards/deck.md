# 🧠 Module 07 · Data Analysis — Flashcard Deck

[🏠 Module 07](../README.md) · [📖 Lessons](../weeks/README.md) · [📄 Cheat sheet](../cheat-sheets/data-cheatsheet.md)

> **~85 cards.** Cover the answer, say it out loud, *then* check. If you can't explain the **why**, it isn't learned.

> [!TIP]
> **The cards marked ⭐ are the ones that will save you in production.** If you only drill twenty, drill those.

---

## 07.1 · The AI Data Lifecycle

**Q:** ⭐ Why is a data bug more dangerous than a code bug?
**A:** Code bugs are **loud** (stack trace, failing test, pager). Data bugs are **silent** — the model trains fine, the loss drops, the dashboards stay green, and it's **confidently wrong for months**. → [07.1](../weeks/07.1-data-lifecycle.md)

**Q:** Name the eleven lifecycle stages.
**A:** Raw → Collection → **Validation** → Cleaning → Transformation → **Feature Engineering** → Storage → Training → Evaluation → Deployment → **Monitoring** → *(back to Raw)*. **It's a loop.**

**Q:** ⭐ What is data leakage, and why is it so dangerous?
**A:** Information available at training but **not at prediction time**. Dangerous because **it looks like success** — nobody investigates a model that's performing brilliantly.

**Q:** ⭐ The one-line diagnostic for leakage?
**A:** *"At prediction time, would this value actually be available — **with this value**?"*

**Q:** What is training/serving skew?
**A:** Features computed **differently** in training vs production (two code paths that diverge). Fix: **one definition, imported by both.**

**Q:** Data drift vs concept drift?
**A:** Data drift = **P(X)** changes (inputs look different). Concept drift = **P(y|X)** changes (the *relationship* itself — COVID is the canonical example).

**Q:** What is the medallion pattern?
**A:** **Bronze** (raw, **immutable**) → **Silver** (validated, cleaned) → **Gold** (features, ML-ready). Never modify raw data — fix the code and re-run.

**Q:** ⭐ Model-centric vs data-centric AI — why did the field move?
**A:** Architectures **commoditized** (download SOTA in one line). **Nobody can download your data.** Same task: better model = **+0.7pp**; better data = **+16.9pp**.

**Q:** Why must a quality gate *reject* bad data rather than clean it?
**A:** Silently cleaning corruption into plausibility **hides the incident** and leaves the upstream bug in place forever. **Fail loudly; quarantine.**

**Q:** Why is `df.head()` in a committed notebook a problem?
**A:** It publishes **real customer records into git history, permanently.** Strip outputs with `nbstripout` as a pre-commit hook.

---

## 07.2 · NumPy

**Q:** ⭐ Why is a NumPy array faster than a Python list? (Name all five.)
**A:** Contiguous raw bytes, not scattered 28-byte `PyFloat` objects → **(1)** no boxing, **(2)** no interpreter dispatch, **(3)** SIMD, **(4)** cache locality, **(5)** threaded BLAS. → [07.2](../weeks/07.2-numpy.md)

**Q:** What are strides?
**A:** The number of **bytes** to step to advance one index along each axis. They're why `a.T` moves **zero data** — it just swaps them.

**Q:** ⭐ Which operations return a **view**, and why does it matter?
**A:** **Basic slicing** (`a[1:5]`), `.T`, `.reshape()`, `.ravel()`. **Fancy and boolean indexing return copies.** Modifying a view **silently mutates the original** — no error. `.copy()` when you intend to mutate.

**Q:** Why `keepdims=True`?
**A:** Without it, a reduction collapses `(n,1)` → `(n,)`, and the next broadcast **silently produces an `(n,n)` outer operation** instead of elementwise — **with no error**.

**Q:** Why `&` and not `and` on arrays?
**A:** `and` calls `__bool__` on the whole array → *"truth value is ambiguous."* And **`&` binds tighter than `>`**, so **parentheses are mandatory**: `(a>5) & (b<3)`.

**Q:** Why is `np.append` in a loop O(n²)?
**A:** Arrays are **fixed-size** — every append allocates a new buffer and **copies everything**. Preallocate, or build a Python list and convert once.

**Q:** Why set dtype explicitly?
**A:** NumPy defaults to **float64**; `float32` is **half the memory** and roughly twice as fast through the memory hierarchy.

**Q:** Why is `A.sum(axis=0)` slower than `A.sum(axis=1)`?
**A:** C-order stores **rows** contiguously. Summing columns **strides through memory and thrashes the cache** — ~3× slower for identical arithmetic.

**Q:** What's the broadcasting memory bomb?
**A:** `a[:,None] - b[None,:]` with two 50k arrays allocates a **(50000, 50000)** result = **20 GB**. Broadcasting is free; the **result** is not.

**Q:** Why is `np.load(..., allow_pickle=True)` dangerous?
**A:** **Arbitrary code execution** from a malicious file.

---

## 07.3 · Pandas I

**Q:** ⭐ What is a DataFrame internally?
**A:** A **dict of columns**, each a NumPy array, sharing one **Index**. Hence **columns are fast and rows are slow** — and the entire Pandas idiom follows from that. → [07.3](../weeks/07.3-pandas-fundamentals.md)

**Q:** ⭐ Why is `df.iterrows()` so slow?
**A:** It **constructs a new Series object for every row** (and loses dtypes). **~10,000× slower** than vectorized.

**Q:** ⭐ What causes `SettingWithCopyWarning`?
**A:** **Chained indexing** — `df[mask]['col'] = x` assigns to a temporary that may be a copy, so the assignment **may silently do nothing**. Fix: **one** `df.loc[mask, 'col'] = x`.

**Q:** `.loc` vs `.iloc`?
**A:** `.loc` is by **label** and its slice is **INCLUSIVE**. `.iloc` is by **position** and exclusive.

**Q:** Why does an int column become float when a value goes missing?
**A:** NumPy's `int64` has **no NaN representation**. Use the nullable **`Int64`** (capital I).

**Q:** ⭐ Why is `category` such a big memory win?
**A:** An `object` column stores a **pointer to a separate string object per row**. A `category` stores each unique value **once** plus a compact int code array. **10–50× on low-cardinality strings** — and nobody uses it.

**Q:** When should you use `category`?
**A:** When a string column has **< ~50% unique values** (country, status, plan_tier).

**Q:** Why does Pandas arithmetic between two Series produce all-NaN?
**A:** **Index misalignment.** Pandas aligns on **labels**, not position — mismatched labels give NaN, **not an error**.

**Q:** ⭐ Why is Parquet better than CSV?
**A:** **Typed** (no guessing), **columnar** (read only the columns you need), **compressed** (~5× smaller), ~10× faster. **CSV has no schema.**

**Q:** ⭐ Why does `na_values` matter so much?
**A:** Real data encodes missing as **`-1`, `999`, `"N/A"`**. Undeclared, they become **legitimate values** and silently poison every statistic. `df['age'].mean()` returns 43.7 and it's a lie.

**Q:** Whitelist or blacklist on export?
**A:** **Whitelist.** A new PII column added upstream silently appears in a **blacklisted** export; it cannot appear in a whitelisted one.

---

## 07.4 · Pandas II

**Q:** ⭐ What is row explosion?
**A:** A **many-to-many merge** produces a **cartesian product** — 2 duplicate keys × 2 duplicate keys = 4 rows. Every metric is inflated, and **no error is raised**. → [07.4](../weeks/07.4-pandas-advanced.md)

**Q:** ⭐ What does `validate=` do?
**A:** It **raises** if the key-uniqueness assumption is violated (`'one_to_many'`, `'one_to_one'`, …). Turns a **silent row explosion** into a loud exception. **The most underused argument in Pandas.**

**Q:** ⭐ `.agg()` vs `.transform()` vs `.filter()`?
**A:** `agg` → **one row per group**. **`transform` → same shape as input** (broadcasts the group stat back onto every row — the feature-engineering workhorse). `filter` → keeps whole groups.

**Q:** ⭐⭐ Why is `.rolling(7).mean()` leakage?
**A:** The window at row *t* **includes row t itself** — so a feature for predicting today **contains today's value**. Fix: **`.shift(1).rolling(7).mean()`**.

**Q:** ⭐ Why is `bfill()` leakage on a time series?
**A:** It fills a gap with a **future** value — information that didn't exist at that moment. **In a time series, information may only flow forward.**

**Q:** What happens if you `.rolling()` multi-entity data without `groupby`?
**A:** The window **bleeds across entities** — user B's first rows average in user A's last rows. **Silent and completely wrong.** (And you must `sort_values` first.)

**Q:** Why `observed=True` on a categorical groupby?
**A:** Without it, Pandas produces a row for **every combination** of categories, including ones that never occur — 1000×1000 categories = **1M rows from 500 real groups**.

**Q:** `.pivot()` vs `.pivot_table()`?
**A:** `pivot` **raises** on duplicate index/column pairs; `pivot_table` **aggregates** them.

**Q:** Why store datetimes in UTC?
**A:** DST means 2 a.m. happens **twice** in autumn and **never** in spring — local-time daily aggregates get 23- and 25-hour days, and the model learns a **clock artefact** as a seasonal signal.

**Q:** ⭐ Why is "we aggregated it, so it's anonymous" dangerous?
**A:** **A group of size 1 IS that person's record.** Enforce a minimum group size (k ≥ 5–10) before publishing any grouped summary.

---

## 07.5 · Data Cleaning

**Q:** ⭐⭐ MCAR vs MAR vs MNAR?
**A:** **MCAR** = no pattern (safe to impute). **MAR** = depends on *other observed* columns (impute conditionally). **MNAR** = depends on **the missing value itself** (high earners hide income) — **never impute; the missingness IS the signal**. → [07.5](../weeks/07.5-data-cleaning.md)

**Q:** ⭐ How do you test for MNAR?
**A:** Compare the **target rate** for rows where the column is missing vs present. If they differ sharply, **the missingness is predictive**. Almost nobody runs this check.

**Q:** What's wrong with `fillna(0)` on income?
**A:** It says **"missing means earns nothing"** — a lie the model will faithfully learn. Use median + a **missing flag**.

**Q:** Why is bare `df.dropna()` dangerous?
**A:** It drops every row with a null in **any** column — potentially 80% of a wide table — and the dropped rows are **not a random sample**. Always pass `subset=`.

**Q:** ⭐ What is disguised missingness, and how do you find it?
**A:** `-1`, `999`, `"N/A"`, `""` — missing values Pandas treats as real data. **Look for a frequency spike in an otherwise smooth distribution.** Invisible in `describe()`; **obvious in a histogram**.

**Q:** ⭐ Why is the z-score a bad outlier detector?
**A:** The outlier **inflates the σ it's compared against**, so extreme values **hide themselves**. Use **IQR or MAD** (median-based, robust).

**Q:** ⭐ Should you remove outliers?
**A:** **Investigate first.** Error → remove. Rare-but-real (a billionaire) → cap or `log1p`. **Fraud / Black Friday → they ARE the signal. KEEP THEM.**

**Q:** Why is outlier removal a fairness issue?
**A:** Members of an **underrepresented group** may look statistically "unusual," so a naive IQR filter **deletes them** — and the model then fails them in production.

**Q:** ⭐⭐ State the scaling leakage rule.
**A:** **Fit the scaler on TRAIN only**; apply those saved μ, σ to test **and to production**. Fitting on all data **leaks the test set**; refitting at inference causes **training/serving skew**.

**Q:** Why is label-encoding a nominal variable wrong?
**A:** It **invents an order**: `{red:0, green:1, blue:2}` tells a linear model green is *between* red and blue. Use **one-hot**.

**Q:** ⭐ Why is naive target encoding catastrophic?
**A:** `groupby.transform('mean')` gives each row **its own target** (exactly, for a category of size 1). Perfect training score, useless model. **Use out-of-fold.**

---

## 07.6 · EDA

**Q:** ⭐ What are the 7 steps of systematic EDA?
**A:** Shape → Missing → Univariate → **Bivariate (vs target)** → Multivariate → **Target** → **🚨 Leakage hunt**. Most people do steps 1 and 3 and stop. → [07.6](../weeks/07.6-eda.md)

**Q:** Why always look at the median beside the mean?
**A:** Divergence signals **skew**. A mean of $2,400 with a median of $85 means **one whale**, not a typical customer.

**Q:** What's the most useful transform in applied data science?
**A:** **`np.log1p`** — right-skew is the default state of most real quantities (income, prices, counts, durations), and `log1p` handles zeros gracefully.

**Q:** What does high **kurtosis** warn you about?
**A:** **Heavy tails** — extreme events are far more common than a normal predicts. Normality-assuming models **underestimate exactly the events that matter most**.

**Q:** ⭐ Why can Pearson correlation be 0 for perfectly related variables?
**A:** It detects **linear** relationships only. `y = x²` gives ρ ≈ 0. Use **Spearman** (monotonic) or **mutual information** (any dependence).

**Q:** ⭐⭐ What does a 0.97 correlation with the target mean?
**A:** **Leakage**, almost certainly. Real signal is messy. **It's a bug report, not a discovery.**

**Q:** Why filter groups by `n >= 30` when ranking target rates?
**A:** A category with 3 rows and a 100% rate is **noise** (uncertainty ∝ 1/√n). Without the filter you've simply **ranked your smallest groups**.

**Q:** Why check class balance first?
**A:** It changes your **metric** (PR-AUC, never accuracy), your **split** (stratified), your **loss** (class weights), and your **threshold** (0.5 is wrong).

**Q:** ⭐⭐ What's the most consequential EDA finding?
**A:** **A date column.** Temporal structure means a **random split leaks the future** — violating i.i.d. and producing excellent, **fictional** offline metrics.

**Q:** What is multicollinearity and why does it matter?
**A:** Features correlated with **each other** (ρ > 0.95). Makes linear coefficients **unstable and uninterpretable**, and splits feature importances arbitrarily. Trees mostly don't care.

**Q:** Why is the proxy check a duty?
**A:** If `zip_code` correlates 0.8 with race, **your model uses race** — deleting the race column doesn't remove it, it only removes your ability to **measure** it.

---

## 07.7 · Feature Engineering

**Q:** ⭐ Why do features matter more than models?
**A:** A better model buys **+3–8%**; the right features buy **+10–40%**. Every Kaggle competition is won on features — the top 100 teams all use the same GBM. → [07.7](../weeks/07.7-feature-engineering.md)

**Q:** When does feature engineering stop mattering?
**A:** For **unstructured data** (images, audio, raw text), deep learning **learns the features**. For **tabular** — most business ML — it still dominates.

**Q:** Why can't a linear model learn `price/sqft`?
**A:** **Division isn't in its hypothesis space** — it can only take weighted sums. Hand it the ratio and the pattern becomes **trivially learnable**.

**Q:** ⭐ What's the most powerful generic feature pattern?
**A:** **"This row vs. its group"** — `df.x / df.groupby('g')['x'].transform('mean')`. A $500 item is cheap for a laptop and outrageous for a phone case.

**Q:** ⭐ Why does cyclical encoding need **both** sin and cos?
**A:** `sin` alone is **ambiguous** — 3 a.m. and 9 a.m. share a sine. The **(sin, cos) pair is a unique point on the unit circle**, so hour 23 and hour 0 land **adjacent**.

**Q:** Why `.clip(lower=1)` on denominators?
**A:** Division by zero produces **`inf`**, which propagates through every downstream computation and poisons the model.

**Q:** ⭐ Why is permutation importance more trustworthy than tree importance?
**A:** Tree importance is **biased toward high-cardinality features** and **splits credit between correlated features** (both look unimportant). Permutation asks the real question: *how much worse is the model without this?* **Compute it on VALIDATION, not train.**

**Q:** What does a feature with 95% of the importance mean?
**A:** **Leakage**, almost certainly. Feature importance is one of your best **leak detectors**.

**Q:** ⭐⭐ Name the 6 leakage rules.
**A:** **(1)** Fit transformers on train only · **(2)** `.shift(1)` before rolling · **(3)** out-of-fold target encoding · **(4)** respect the `as_of_date` · **(5)** never `bfill` a time series · **(6)** fit vectorizers on train.

**Q:** ⭐⭐ What is the universal leakage test?
**A:** **Perturb a value in the future, rebuild the features, assert nothing changed.** Worth more than every other test in your pipeline. **Almost nobody writes it.**

**Q:** ⭐ What makes a feature a "fantasy"?
**A:** If you **can't compute it at inference time, within your latency budget, from data that exists at request time** — it isn't a feature, no matter how predictive.

---

## 07.8 · Visualization

**Q:** ⭐ What does a histogram reveal that `describe()` cannot?
**A:** **Bimodality** (two populations mixed / mixed units), **sentinel spikes** (a bar at exactly −1), **truncation** (a hard wall), and skew shape. **All invisible in summary statistics.** → [07.8](../weeks/07.8-visualization.md)

**Q:** Why is a truncated y-axis a lie on a bar chart?
**A:** The bar's **length** encodes the value — truncating multiplies the apparent difference. (On a line chart, *position* is the encoding, so zooming is more defensible — but label it.)

**Q:** Why never a pie chart?
**A:** **Humans cannot compare angles accurately.** They can compare lengths. Use a sorted horizontal bar chart.

**Q:** ⭐ Why must a correlation heatmap use a **diverging** colormap centered at 0?
**A:** Correlation has a meaningful midpoint. With a **sequential** map, **−0.9 (a strong relationship) looks as "low" as 0.0** — hiding half your findings.

**Q:** Why are dual y-axes dangerous?
**A:** You can **manufacture any apparent correlation** by choosing the two scales.

**Q:** How do you fix an overplotted scatter?
**A:** In order: `alpha`, smaller `s`, **sample**, then **hexbin / 2-D histogram** (which shows **density** — usually what you actually wanted).

**Q:** Why `fig, ax = plt.subplots()` over `plt.plot()`?
**A:** The **OO API** is explicit about which axes you're drawing on. The `plt.` state machine breaks with subplots, functions, and loops.

**Q:** ⭐ Why is `fig.write_html()` a privacy risk?
**A:** Plotly **embeds the underlying data arrays in the HTML** — including everything in `hover_data`. **A shared Plotly HTML is a shared dataset.**

**Q:** What's the standard for **exploratory** plots?
**A:** **Quantity over polish.** 200 ugly plots beat 10 beautiful ones. Polish only the two that survived.

---

## 07.9 · Data Quality

**Q:** ⭐ Name the six dimensions of data quality.
**A:** Completeness, Validity, **Accuracy**, Consistency, Timeliness, Uniqueness. → [07.9](../weeks/07.9-data-quality.md)

**Q:** ⭐ Why is **accuracy** the hardest dimension?
**A:** It requires an **external reference**. Data can be complete, valid, consistent, fresh, and unique — **and completely wrong** (prices switched from dollars to cents). **Only reconciliation catches it.**

**Q:** ⭐⭐ If you build only two data quality checks, which?
**A:** **Freshness** (a stale table looks perfectly healthy) and **volume** (a partial load is silent). They catch **most real incidents** and take twenty lines.

**Q:** Why `strict=True` on a schema?
**A:** It **rejects unexpected columns** — catching upstream **renames** and additions. Without it, a schema will happily validate a DataFrame **missing half your features**.

**Q:** What should a quality gate do on failure?
**A:** **Quarantine + alert.** Never silently fix — a silent fix **hides the incident** and leaves the upstream bug in place forever. **The bad rows are the most valuable data you have that day.**

**Q:** What is PSI, and what are its thresholds?
**A:** Population Stability Index — a **symmetrized KL divergence** measuring distribution shift. **< 0.1 stable · 0.1–0.25 investigate · > 0.25 retrain.**

**Q:** ⭐ Why monitor **input drift** rather than model performance?
**A:** Performance needs **labels**, which arrive late (churn: 90 days; default: 2 years). **Input drift is observable immediately** — a leading indicator, not a lagging one.

**Q:** Why is **alert fatigue** a failure mode?
**A:** A check that fires daily gets **muted within a week** — and then the **real** incident is invisible in the noise. **A wrong check is worse than no check.**

**Q:** ⭐ Why must you never log the offending **value**?
**A:** **Logs are the least-protected data store you have** — shipped to third parties, retained for years, readable by all of engineering. **Log the rule and the row ID.**

**Q:** How do you avoid hand-writing 60 validation rules?
**A:** **Auto-generate the schema** from a trusted baseline profile, then have a human review it once. Version it in git. **This is the difference between having data tests and not.**

---

## 07.10 · Performance

**Q:** ⭐ What's the real bottleneck in data processing?
**A:** **Memory bandwidth and I/O**, not CPU. Wins come from **moving less data**, not computing faster. → [07.10](../weeks/07.10-performance.md)

**Q:** ⭐ State the optimization ladder in order.
**A:** **Profile** → **vectorize** → **dtypes** → **Parquet** → column pruning → chunk → change tool → **distribute (last resort)**. **Stop as soon as it's fast enough.**

**Q:** ⭐ Why is Parquet 5–100× faster than CSV?
**A:** **Columnar**: (1) read only the columns you need, (2) adjacent similar values **compress far better**, (3) **predicate pushdown** skips whole row-groups using min/max statistics. Plus it's **typed**.

**Q:** What's the biggest memory win in Pandas?
**A:** **`category`** on low-cardinality strings — **10–50×**.

**Q:** ⭐ Which operations chunk cleanly, and which don't?
**A:** ✅ sum, count, min, max, mean. ❌ **median, exact nunique, quantiles, joins, sort** — they need all the data at once. **That's the real signal to change tools** — not file size.

**Q:** ⭐ Why is DuckDB underrated?
**A:** **SQL directly on Parquet files** — no server, no setup, **out-of-core**, multi-threaded. Handles **100 GB on a laptop**. **Most "we need Spark" is actually "we need DuckDB."**

**Q:** What makes Polars fast?
**A:** Not just Rust — its **lazy API builds a query plan** that's optimized end-to-end (filter pushdown, column pruning, fusion) before executing. **It does less work.**

**Q:** Why measure **peak** memory rather than result size?
**A:** **Peak is what OOM-kills you.** `(a+b)*c-d` allocates several full-size temporaries **simultaneously** — the result is 800 MB, the peak was 3.2 GB.

**Q:** Why does distributing computation widen your privacy risk?
**A:** Spark/Dask ship your data (and PII) to **every executor's memory, shuffle spills, and logs**. **The cheapest way to secure data is not to move it.**

---

## 07.11 · Pipelines

**Q:** ⭐ Why is a notebook not a pipeline?
**A:** **Hidden state.** You can delete the cell that created a variable and it still works — so the notebook produces a result **its own code cannot reproduce**. Restart-and-run-all breaks it. → [07.11](../weeks/07.11-pipelines.md)

**Q:** ⭐⭐ Why does `fit`/`transform` make leakage **structurally impossible**?
**A:** `transform()` **has no code path that learns anything** — it physically cannot compute a statistic from the test set. **Always prefer a structural guarantee to a promise of discipline.**

**Q:** What five things must be pinned for reproducibility?
**A:** **Code** (git SHA) · **data** (hash/version) · **config** · **environment** (locked deps) · **seed**. Miss any one and it fails.

**Q:** Why is `np.random.seed(42)` worse than `default_rng(42)`?
**A:** It sets **global** state — any library can consume from and perturb the same stream. **Seed locally, pass explicitly.**

**Q:** ⭐⭐ What is the **skew test**, and what does it catch?
**A:** Batch-transforming N rows must equal transforming them **one at a time**. It catches any step that computes **across rows** — e.g. **a scaler that refits on a single row outputs exactly zero for every feature**, and your model silently receives all-zeros in production.

**Q:** ⭐ Why must you never overwrite a dataset?
**A:** Storage is **cheap**; an **unreproducible model is worthless**. And without data versioning, *"did the code change or the data change?"* is **unanswerable**.

**Q:** What's the `git_dirty` flag for?
**A:** A result from **uncommitted code cannot be reproduced** — that code exists nowhere but your laptop. **Flag it loudly; refuse it in CI.**

**Q:** ⭐ How do you kill training/serving skew?
**A:** **One code path.** Serialize the pipeline **with** the model; serving **imports and calls `transform()`** rather than reimplementing. **Nothing can diverge because there's only one implementation.**

**Q:** Why must steps be **pure**?
**A:** Testable, **cacheable**, parallelizable, debuggable. **You cannot safely cache an impure function** — the design property and the performance property are the **same property**.

**Q:** ⭐ Why do dataset versioning and GDPR conflict, and what resolves it?
**A:** A deleted user still exists in **every historical snapshot**. **Pseudonymize at ingestion** with a separate mapping table — **deleting the mapping row severs the link**. A decision you can only make at the start.

---

## 07.12 · Case Studies

**Q:** ⭐ What determines your preprocessing choices?
**A:** **How the model will be used.** It determines the **grain**, the **split**, and the **metric** — and everything else follows. → [07.12](../weeks/07.12-case-studies.md)

**Q:** Why must churn use a **time-based** split?
**A:** Churn is temporal — a random split trains on July and tests on April. **Also beware survivorship bias** (`SELECT * FROM active_customers` excludes everyone who already churned).

**Q:** ⭐ Why is `pool_quality = NaN` different from `lot_frontage = NaN`?
**A:** `pool_quality` NaN means **there is no pool** (structurally absent → fill with `"None"`). `lot_frontage` NaN means **unknown** (impute). **Both look identical in `isna()`** — only the **data dictionary** tells you.

**Q:** Why is `price_per_sqft` a fatal feature in a price model?
**A:** It **contains `sale_price` — the target.** Brilliant for EDA, catastrophic as a feature.

**Q:** ⭐ What's the leakage trap in text datasets?
**A:** **Duplicate reviews** (5–15% is typical). A random split puts identical text in train *and* test; the model **memorizes** it. **Deduplicate on normalized text before splitting.**

**Q:** Why shouldn't you strip punctuation and caps for sentiment?
**A:** `!!!`, `ALL CAPS`, and 😡 are among the **strongest sentiment signals that exist**. The classic NLP cleaning pipeline was built for 2005 bag-of-words and **destroys signal**.

**Q:** ⭐⭐ What's the #1 failure in medical imaging ML?
**A:** **Group leakage** — images from the **same patient** in both train and test. The model learns the patient, not the disease. **Split by patient.**

**Q:** ⭐ What is metadata leakage, and how do you test for it?
**A:** Image size/format/EXIF correlating with the class because different classes came from different sources (**the portable X-ray marker → pneumonia**). **Test: train on metadata alone. If it works, you have leakage.**

**Q:** ⭐⭐ Why does time-series validation need a **gap**?
**A:** If you forecast 7 days ahead, a test row's rolling features use the previous 7 days — **which are in your training set**. **Insert a gap equal to your forecast horizon.**

**Q:** ⭐ Should you remove outliers from a sales time series?
**A:** **NO.** **Black Friday is not an error** — it's the day the business most needs predicted. **Add a feature that explains the spike; never erase it.**

---

## 🎯 The ten sentences (recall all ten cold)

**Q:** Name the ten sentences that carry this module.
**A:**
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

[⬆ Module 07](../README.md) · [📖 Lessons](../weeks/README.md) · [📄 Cheat sheet](../cheat-sheets/data-cheatsheet.md) · [📝 Quiz](../quizzes/quiz-01.md)
