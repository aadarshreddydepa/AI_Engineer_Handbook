# 📄 Data Analysis for AI Engineers — Cheat Sheet

[🏠 Module 07](../README.md) · [📖 Lessons](../weeks/README.md)

> NumPy + Pandas + cleaning + EDA + features + plots + quality + pipelines, on one page.

---

## 🔄 The AI Data Lifecycle

```
Raw → Collection → VALIDATION → Cleaning → Transformation → FEATURES
    → Storage → Training → Evaluation → Deployment → MONITORING → (back to Raw)
```

**It's a LOOP.** Monitoring detects drift → recollect → retrain.

| The three killers | |
|---|---|
| **Leakage** | Looks like success. *"At prediction time, would I have this value?"* |
| **Training/serving skew** | Worked in the notebook. **One code path** |
| **Drift** | Used to work. **Monitor the inputs**, not just performance |

**Data bugs are SILENT.** No stack trace. No failing test. Confidently wrong for months.

---

## 🔢 NumPy

| Task | Code |
|---|---|
| Create | `np.zeros(n, dtype=np.float32)` · `np.arange` · `np.linspace` |
| Random | `rng = np.random.default_rng(42)` ← **not `np.random.seed`** |
| Inspect | `.shape` `.dtype` `.nbytes` `.strides` `.flags` |
| **Is it a view?** | `arr.base is other` |
| **View** (shares memory!) | `a[1:5]` · `a.T` · `.reshape()` · `.ravel()` |
| **Copy** | `a[[1,3]]` (fancy) · `a[a>5]` (boolean) · `.copy()` |
| Boolean mask | `a[(a>5) & (b<3)]` ← **`&` not `and`; parens REQUIRED** |
| Conditional | `np.where(cond, x, y)` |
| Reduce | `.sum(axis=0, keepdims=True)` ← **`keepdims`** |
| Standardize | `(X - X.mean(0, keepdims=True)) / X.std(0, keepdims=True)` |
| In-place | `a += 1` · `np.multiply(a, 2, out=a)` |

**Broadcasting:** compare shapes **from the right**; equal, or one is 1.
⚠️ **`(n,)` vs `(n,1)` silently gives an `(n,n)` outer op.** Use `keepdims=True`.
⚠️ `a[:,None] - b[None,:]` with 50k arrays = **20 GB**.
⚠️ **Never `np.append` in a loop** — O(n²).
⚠️ `np.load(allow_pickle=True)` = **RCE**.

---

## 🐼 Pandas

| Task | Code |
|---|---|
| **First command, always** | `df.info()` |
| **Read properly** | `pd.read_csv(f, dtype={...}, parse_dates=[...], na_values=[-1,'N/A'], usecols=[...])` |
| **Write properly** | `df.to_parquet('f.parquet')` |
| Select by label | `df.loc[rows, cols]` ← **slice is INCLUSIVE** |
| Select by position | `df.iloc[rows, cols]` ← exclusive |
| **Conditional assign** | `df.loc[mask, 'col'] = val` ← **ONE call. Never chain** |
| Independent subset | `sub = df[mask].copy()` |
| Memory | `df.memory_usage(deep=True).sum()` |
| **Shrink 10×** | `df['c'] = df['c'].astype('category')` |
| Nullable int | `.astype('Int64')` (capital I) |
| Strings | `df.col.str.lower().str.strip().str.contains(p, na=False)` |

### Combine · Group · Reshape · Window

| Task | Code |
|---|---|
| **Merge (safely)** | `pd.merge(a, b, on='k', how='left', validate='one_to_many', indicator=True)` |
| Check the grain | `df['k'].duplicated().any()` |
| Stack | `pd.concat([a,b], ignore_index=True)` |
| Aggregate | `df.groupby('k').agg(total=('x','sum'), n=('x','size'))` |
| **Group stat → every row** ⭐ | `df.groupby('k')['x'].transform('mean')` |
| Categorical groupby | `.groupby('c', observed=True)` ← **always** |
| Long→wide | `df.pivot_table(index=, columns=, values=, aggfunc=)` |
| Wide→long | `df.melt(id_vars=, var_name=, value_name=)` |
| **Rolling (SAFE)** ⭐ | `df.groupby('id')['x'].transform(lambda s: s.shift(1).rolling(7).mean())` |
| Lag / change | `.shift(1)` · `.diff()` · `.pct_change()` |
| Resample | `df.resample('D').sum()` (needs a DatetimeIndex) |
| Fill gaps | `.ffill()` ✅ · **`.bfill()` ⚠️ LEAKAGE** · `.interpolate(method='time')` |

**⛔ Never:** `.iterrows()` (10,000× slow) · `df[a][b] = x` (SettingWithCopy) · `pd.concat` in a loop (O(n²))

---

## 🧹 Cleaning

| Missingness | Meaning | Do |
|---|---|---|
| **MCAR** | No pattern | Impute or drop freely |
| **MAR** | Depends on *other observed* cols | Impute **conditionally** |
| **MNAR** ⚠️ | Depends on **the missing value itself** | ❌ **Never impute. FLAG IT — the missingness IS the signal** |

**The MNAR test:** compare `df[df.x.isna()].target.mean()` vs `df[df.x.notna()].target.mean()`.

| Task | Code |
|---|---|
| **The safe default** | `df['x_missing'] = df.x.isna(); df.x = df.x.fillna(df.x.median())` |
| Drop (carefully) | `df.dropna(subset=['x'])` ← **never bare `dropna()`** |
| **Hunt sentinels** | Look for a spike at `-1`, `0`, `999`, `"N/A"` in a smooth distribution |
| Invalid → NaN | `df.loc[~df.age.between(0,120), 'age'] = np.nan` |
| **Outliers (IQR)** ✅ | `q1,q3 = x.quantile([.25,.75]); iqr=q3-q1; lo,hi = q1-1.5*iqr, q3+1.5*iqr` |
| ⚠️ z-score | **Inflated by the very outliers it's hunting.** Use IQR or MAD |
| Cap | `df.x.clip(lo, hi)` |
| **Skew fix** ⭐ | `np.log1p(df.x)` |
| **Standardize** | `(x - μ_TRAIN) / σ_TRAIN` ← **train's params. Always.** |
| Robust scale | `(x - median) / IQR` |
| One-hot | nominal, low cardinality |
| Ordinal | **only when genuinely ordered** |
| **Target encode** | **Out-of-fold only.** Naive = leakage |

**Outliers: investigate, don't delete.** Error → remove. Real → cap/log. **Fraud/Black Friday → KEEP.**

---

## 🔍 EDA — the 7 steps

**shape → missing → univariate → bivariate (vs target) → multivariate → target → 🚨 LEAKAGE HUNT**

| Check | Code |
|---|---|
| Overview | `df.info()` · `df.describe(percentiles=[.01,.5,.99])` |
| **Median beside mean** | Divergence = skew |
| **Skew** | `df.x.skew()` — \|s\|>1 substantial → **`log1p`** |
| Kurtosis | `>0` = heavy tails = extremes are common |
| Correlation | `df.corr()` (**linear only!**) · `method='spearman'` (monotonic) |
| Non-linear | `mutual_info_regression` (ρ=0 for `y=x²`) |
| **🚨 Leakage** | Anything with \|ρ\| > 0.9 to the target |
| Multicollinearity | pairs with \|ρ\| > 0.95 **between features** |
| Category rate | `df.groupby('c').agg(rate=(t,'mean'), n=(t,'size'))` ← **always show `n`** |
| **Class balance** | `df[target].value_counts(normalize=True)` |
| **Date column?** | If yes → **you CANNOT random-split** |

---

## 🛠️ Feature Engineering (+10–40% — more than any model)

| Type | Code |
|---|---|
| **Ratio** ⭐ | `df.a / df.b.clip(lower=1)` ← **clip the denominator** |
| **Group comparison** ⭐ | `df.x / df.groupby('g')['x'].transform('mean')` |
| Group rank | `df.groupby('g')['x'].rank(pct=True)` |
| Date parts | `ts.dt.dayofweek` · `.hour` · `.month` · `.is_month_end` |
| **Cyclical** ⭐ | `np.sin(2*np.pi*h/24)` **AND** `np.cos(2*np.pi*h/24)` |
| Elapsed | `(as_of - df.signup).dt.days` |
| **Lag / rolling (safe)** | `.groupby('id')['x'].transform(lambda s: s.shift(1).rolling(7).mean())` |
| Text: cheap | `.str.len()` · `.str.count('!')` · caps ratio ← **often beat the words** |
| Text: TF-IDF | `TfidfVectorizer().fit(TRAIN_texts)` |
| **Selection** | `permutation_importance(model, X_VAL, y_val)` ← **val, not train** |

### 🚨 The 6 leakage rules
1. **Fit transformers on TRAIN only**
2. **`.shift(1)` before every rolling window**
3. **Out-of-fold target encoding**
4. **Respect the `as_of_date`** — filter `t < as_of` FIRST
5. **Never `bfill` a time series**
6. **Fit vectorizers on train**

**The test:** perturb a value in the **future** → rebuild → **assert nothing changed.**

---

## 📊 Visualization

| Question | Chart |
|---|---|
| Shape of one variable | **Histogram** (try several bin counts) |
| Distribution by group | **Box** (violin if shape matters) |
| Two numerics | **Scatter** + `alpha`; **hexbin** if > 10k |
| Which features correlate | **Heatmap**, `RdBu_r`, `vmin=-1, vmax=1` |
| Over time | **Line** + rolling-mean overlay |
| Compare categories | **Bar** (**start at zero**) |
| Parts of a whole | Stacked bar — ❌ **never a pie** |

**Always:** `fig, ax = plt.subplots()` · `plt.close(fig)` in loops · label axes with units · **show `n`**

**The lies:** truncated bar axis · dual y-axes · pie charts · `jet` · sequential colormap on correlation

---

## 🛡️ Data Quality

| Dimension | Check |
|---|---|
| Completeness | `df[c].isna().mean() < t` |
| Validity | ranges · regex · `isin` |
| **Accuracy** ⚠️ | **Reconcile against an external source.** The only way |
| Consistency | `order_date <= ship_date` |
| **Timeliness** ⭐ | `now() - df.updated_at.max() < SLA` |
| Uniqueness | `df[key].duplicated().any()` |

**Build FRESHNESS + VOLUME first.** They catch most real incidents and take 20 lines.
**On failure: QUARANTINE + ALERT. Never silently fix.**
**Log the rule and row_id — NEVER the value.**

| PSI (drift) | Action |
|---|---|
| < 0.10 | ✅ stable |
| 0.10–0.25 | ⚠️ investigate |
| **> 0.25** | 🚨 **retrain** |

---

## ⚡ Performance — the ladder

| Rung | Action | Gain |
|---|---|---|
| **0** | **Profile** (`%lprun`, `%memit`) | — |
| **1** | **Vectorize** | **100–10,000×** |
| **2** | **Dtypes** (`category`, downcast) | **2–50× memory** |
| **3** | **Parquet** not CSV | **5–100×** |
| **4** | Read fewer columns | 10–100× |
| **5** | Chunk | Beats RAM |
| **6** | **DuckDB** / Polars | 5–30× |
| **7** | Dask / Spark | ⚠️ Last resort |

| Tool | Sweet spot |
|---|---|
| Pandas | < 5 GB |
| **Polars** | 1–100 GB (lazy, multi-threaded) |
| **DuckDB** ⭐ | 1–500 GB — **SQL on Parquet, no setup, out-of-core** |
| Spark | > 1 TB only |

**Chunkable:** ✅ sum, count, min, max, mean · ❌ **median, nunique, joins, sort**
**Peak memory is what OOMs you**, not result size.

---

## 🏭 Pipelines

| Principle | |
|---|---|
| **Notebook ≠ pipeline** | Hidden state. Explore in one; **ship functions** |
| **Pure steps** | No globals, no mutation. `df.copy()` |
| **`fit` on train; `transform` everywhere** | **Structural** leakage prevention |
| **One code path** | Serialize the pipeline **with** the model |
| **Pin five** | code (git SHA) · data (hash) · config · env · seed |
| **`rng = default_rng(seed)`** | Never global `np.random.seed()` |
| **Never overwrite** | New version. Always |
| **Manifest every run** | git SHA + **dirty flag** + hashes + versions |
| Idempotent + atomic | Retries are guaranteed |

**The 5 CI tests:** `no_leakage` · `no_skew` (batch == single row) · `idempotent` · `reproducible` · `purity`

---

## 🎓 Case studies — the same technique, five different answers

| | Churn | Houses | Sentiment | Images | Forecast |
|---|---|---|---|---|---|
| **Split** | **time** | random/time | stratified + group | **GROUP** ⭐ | **time + GAP** ⭐ |
| **Outliers** | investigate | **cap** | keep | drop corrupt | **KEEP** ⭐ |
| **Missing** | flag (MNAR) | **"None" ≠ NaN** | drop | flag | **`ffill`** |
| **Trap** | post-event cols | `price_per_sqft` | **duplicates** | **group + metadata** | **un-shifted window** |

---

## 🎯 The ten sentences

1. **Data bugs are silent.** No stack trace, no failing test, confidently wrong for months.
2. **Leakage looks like success.** A suspiciously good result is a **bug report**.
3. **"At prediction time, would I actually have this value?"** — the question that catches most of it.
4. **`.shift(1)` before every rolling window.** One missing call = a useless model.
5. **Fit on train only** — and make it **structural** (`fit`/`transform`), not disciplinary.
6. **Every `fillna` is a claim about the world.** Usually a false one.
7. **A `-1` in an age column** makes every statistic a lie. **Plot it.**
8. **Understand the outlier before you delete it.** It might be Black Friday.
9. **A stale table looks perfectly healthy.** Check freshness and volume.
10. **Features beat models** (+10–40% vs +3–8%) — and **nobody can download your data**.

---

[⬆ Module 07](../README.md) · [📖 Lessons](../weeks/README.md) · [🧠 Flashcards](../flashcards/deck.md)
