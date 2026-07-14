# 📄 Machine Learning Foundations — Cheat Sheet

[🏠 Module 08](../README.md) · [📖 Lessons](../weeks/README.md)

---

## ⭐ The four boxes (every supervised algorithm)

**MODEL** → **LOSS** → **GRADIENT** → **UPDATE** → repeat

| Algorithm | Model | Loss | Optimizer |
|---|---|---|---|
| Linear reg | $Xw + b$ | MSE | Normal eq. **or** GD |
| Logistic reg | $\sigma(Xw+b)$ | **Log-loss** | GD |
| Decision tree | Nested if/else | Gini/entropy | Greedy splitting |
| SVM | Max-margin hyperplane | **Hinge** + L2 | QP / SGD |
| KNN | *(none — memorizes)* | *(none)* | *(none — lazy)* |

**⭐ Every algorithm is a BET about the shape of your data. The one whose bet matches reality wins.**

---

## 📐 The key equations

| | |
|---|---|
| **⭐ Linear reg gradient** | $\frac{2}{n}X^\top(\hat{y}-y)$ — *"features ᵀ × errors"* |
| **⭐ Logistic reg gradient** | $\frac{1}{n}X^\top(\hat{p}-y)$ — **IDENTICAL. σ′ cancels** |
| **Normal equations** | $w = (X^\top X)^{-1}X^\top y$ — **use `solve`, never `inv`** |
| **⭐ Ridge** | $(X^\top X + \lambda I)^{-1}X^\top y$ — **always invertible** (λ added to every eigenvalue) |
| **Sigmoid** | $\sigma(z)=\frac{1}{1+e^{-z}}$; $\sigma'=\sigma(1-\sigma) \le 0.25$ |
| **Log-loss** | $-\frac{1}{n}\sum[y\log\hat p + (1-y)\log(1-\hat p)]$ |
| **Entropy** | $-\sum p\log_2 p$ · **Gini** $1-\sum p^2$ |
| **Information gain** | $H(\text{parent}) - \sum\frac{n_k}{n}H(\text{child}_k)$ |
| **⭐⭐ Ensemble variance** | $\rho\sigma^2 + \frac{1-\rho}{M}\sigma^2$ — **the game is lowering ρ** |
| **Gradient boosting** | $F_m = F_{m-1} + \eta h_m$, $h_m$ fits **the residuals = the negative gradient** |
| **SVM margin** | $2/\|w\|$ · **Hinge** $\max(0, 1-y\cdot z)$ — **exactly 0 past the margin** |
| **⭐ Kernel trick** | Data appears **only in dot products** → swap $x^\top x'$ for $K(x,x')$ |
| **Naive Bayes** | $\arg\max_y \log P(y) + \sum_j \log P(x_j\mid y)$ — **LOG SPACE** |
| **PCA** | SVD of the **centered** X. Right singular vectors = the PCs |

---

## ⭐⭐ THE SCALING TABLE

| Algorithm | Scale? | Why |
|---|---|---|
| Linear / Logistic / NN | ⭐ **YES** | GD conditioning + scale-dependent penalty |
| **SVM** | ⭐⭐ **MANDATORY** | The kernel is **Euclidean distance** |
| **KNN / K-Means / PCA** | ⭐⭐ **MANDATORY** | It **is** a distance / variance |
| **Trees / RF / GBM** | ❌ **NO** | Splits `x <= t` are **scale-invariant** |
| Naive Bayes | ❌ No | Counting |

| | Missing | Categorical | Outliers |
|---|---|---|---|
| Linear/Logistic/KNN | Impute | One-hot | ⚠️ Sensitive |
| SVM | Impute | One-hot | ✅ Robust |
| Trees/RF | Impute | Encode | ✅ Robust |
| **⭐ LightGBM/XGBoost** | ⭐ **NATIVE** | ⭐ **NATIVE** | ✅ Robust |

**⭐ "Just use LightGBM" removes 4 categories of preprocessing decision — each a chance for a bug.**

---

## 📊 Evaluation

| Metric | Use |
|---|---|
| **Accuracy** | ❌ **USELESS when imbalanced** (99% by predicting nothing) |
| **Precision** | *"When I say yes, am I right?"* |
| **Recall** | *"Did I find them all?"* |
| **F1** | ⚠️ **Assumes FP = FN in cost. They aren't** |
| **ROC-AUC** | ⚠️ **Optimistic when imbalanced** (the huge TN count hides FPs) |
| **⭐⭐ PR-AUC** | ⭐ **Imbalanced.** Baseline = the positive rate |
| **RMSE / MAE / R²** | Regression. **R² < 0 = worse than the mean** |

**⭐⭐ THE THREE RULES:**
1. **Imbalanced → PR-AUC**, never accuracy. State the baseline.
2. **⭐⭐ TUNE THE THRESHOLD on business cost.** FREE, and beats every model improvement.
3. **Report value ± CI, with n, SLICED by segment.**

**Calibration:** LR ✅ · **NB ❌ wildly overconfident** · SVM ❌ (a distance) · NN ❌ overconfident

---

## 🔒 Cross-validation & leakage

| Strategy | When |
|---|---|
| `KFold(shuffle=True)` | i.i.d. |
| **⭐ StratifiedKFold** | **Classification** — always |
| **⭐⭐ GroupKFold** | **Rows share a source** (patient, product, camera) |
| **⭐⭐ TimeSeriesSplit(gap=h)** | **Temporal** — **gap = the forecast horizon** |

**⭐⭐ THE FOUR LEAKS THAT SURVIVE A "CORRECT" CV:**
1. **Preprocessing outside the loop** ← **the most common leak in ML.** *Everything with a `fit` goes in the Pipeline*
2. **Feature selection before CV** ← **90% accuracy on pure noise**
3. **Duplicate rows across folds**
4. **Target leakage in the features** ← ⚠️ **CV CANNOT catch this.** Only: *"would I have this value at prediction time?"*

**Inside the pipeline:** scaler · imputer · encoder · **PCA** · **TF-IDF** · selector · target encoder · SMOTE

---

## 🎯 The workflow

**baseline → simple model → ⭐ ERROR ANALYSIS → ⭐ FEATURES → GBM → tune (LAST)**

| Activity | Gain |
|---|---|
| ⭐ **Fixing bad labels / data** | Can be **+∞** |
| ⭐ **Error analysis + features** | **+10–40%** |
| Better model (LR → GBM) | +3–8% |
| **Hyperparameter tuning** | **+1–3%** ← everyone starts here |

| Train err | Val err | Diagnosis | Lever |
|---|---|---|---|
| **High** | **High** | **UNDERFIT** | Bigger model, more features |
| **Low** | **High** | **OVERFIT** | More data, regularize, simplify |

**⭐ Learning curve:** gap + val **falling** → **more data helps**. Gap + val **flat** → **regularize instead**.
**⭐ Error analysis: look at 100 errors BY HAND.** ~15% will be **mislabeled** — the model was right.

---

## 🌲 Ensembles

| | **Bagging / RF** | **Boosting / GBM** |
|---|---|---|
| Trees | **Parallel, DEEP** | **Sequential, SHALLOW** |
| Fits | Bootstrap samples | **The residuals** |
| Reduces | **Variance** | **Bias** |
| More trees | ✅ **Never hurts** | ⚠️ **Eventually overfits** |
| **Early stopping** | Unnecessary | ⭐⭐ **MANDATORY** |
| Free validation | ⭐ **OOB (36.8%)** | — |

**⭐ RF's key knob: `max_features='sqrt'`** — **handicapping each tree DECORRELATES the forest and makes it better.**
**⭐ GBM: `n_estimators=5000` + early stopping.** Never grid-search it. **lr × n_estimators ≈ constant.**

---

## 🔍 Interpretability

| Method | Trust |
|---|---|
| **MDI** (`feature_importances_`) | ❌ **BIASED** — ranks a random ID column top-5 |
| **⭐ Permutation importance** | ✅ **On VALIDATION** |
| **⭐⭐ SHAP** | ⭐ **Best — a uniqueness theorem** (Shapley) |
| LIME | 🟡 Heuristic; **inconsistent between runs** |
| PDP | ⚠️ **Lies if features are correlated** → use **ALE** |

**⭐⭐ SHAP's best use: FINDING YOUR LEAKS.** A feature with 80% of the SHAP mass is a **bug report**.
**⭐ Removing the protected attribute does NOT make a model fair** — proxies reconstruct it. **Measure.**
**⭐⭐ Fairness definitions are mathematically INCOMPATIBLE.** Choose one, deliberately.

---

## 🚀 Production

**The artifact = pipeline + ⭐ tuned threshold + feature list + manifest + ⭐⭐ drift baseline**

| Monitor | Lag |
|---|---|
| System, data quality | Instant |
| **⭐⭐ Drift (PSI) + the PREDICTION DISTRIBUTION** | ⭐ **Instant — LEADING** |
| Performance | 🐌 **Months (needs labels) — LAGGING** |

**⭐⭐ MONITOR THE INPUTS.** Labels arrive months late (churn 90d, default 2y).
**⭐ The prediction distribution is the cheapest, best canary — NO labels required.**
**⭐ PSI:** <0.1 ✅ · 0.1–0.25 ⚠️ · **>0.25 🚨 retrain**
**⭐⭐ Retraining MUST have a GATE that can REFUSE** (worse model? bad data? → reject).
**⭐ Deploy: shadow → canary → ramp.** **LOG YOUR INFERENCE INPUTS FROM DAY ONE.**

---

## 🎯 The ten sentences

1. **"Can you write the rule?"** If yes — **write the rule.**
2. **Every algorithm is a bet about the shape of your data.**
3. **model · loss · gradient · update** — and `predicted − actual` is the gradient, three times over.
4. **Ensembles work by DECORRELATION.** ρσ² is the floor.
5. **⭐ Accuracy is a lie. ROC-AUC is optimistic. TUNE THE THRESHOLD.**
6. **⭐ Everything with a `fit` goes inside the Pipeline** — or you leak.
7. **CV cannot catch target leakage.** Only *"would I have this value at prediction time?"* can.
8. **⭐ Error analysis (+10–40%) beats tuning (+1–3%).** Everyone does it backwards.
9. **`feature_importances_` will rank a random ID column in your top 5.**
10. **⭐ Monitor inputs, not performance — labels arrive months too late.**

---

[⬆ Module 08](../README.md) · [📖 Lessons](../weeks/README.md) · [🧠 Flashcards](../flashcards/deck.md)
