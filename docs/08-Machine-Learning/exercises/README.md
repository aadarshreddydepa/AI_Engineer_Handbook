# 🏋️ Module 08 · Machine Learning — Exercises

[🏠 Module 08](../README.md) · [📖 Lessons](../weeks/README.md) · [📝 Quiz](../quizzes/quiz-01.md)

> Every lesson has its own exercise set. This page is the **index** plus the cross-lesson exercises — the ones where the algorithms collide.

> [!IMPORTANT]
> **⭐ The rule of this module: implement it from scratch, then `np.allclose(mine, sklearn)`.** That single assertion is the moment the library stops being magic. **Do it for every algorithm.**

---

## Per-lesson exercises

| Lesson | Types |
|---|---|
| [08.1 What is ML](../weeks/08.1-what-is-ml.md#-exercises) | Conceptual · **problem framing** · comparison |
| [08.2 Workflow](../weeks/08.2-ml-workflow.md#-exercises) | Debugging · **error analysis** · math |
| [08.3 Linear Regression](../weeks/08.3-linear-regression.md#-exercises) | **Math (derive the gradient)** · NumPy · debugging |
| [08.4 Logistic Regression](../weeks/08.4-logistic-regression.md#-exercises) | Math · NumPy · **threshold tuning** |
| [08.5 Decision Trees](../weeks/08.5-decision-trees.md#-exercises) | Math (entropy/IG) · NumPy · **the depth sweep** |
| [08.6 Ensembles](../weeks/08.6-ensembles.md#-exercises) | **Math (the ρ term)** · NumPy · comparison |
| [08.7 SVM](../weeks/08.7-svm.md#-exercises) | Math (the kernel trick) · NumPy · **visualization** |
| [08.8 Naive Bayes](../weeks/08.8-naive-bayes.md#-exercises) | Math · NumPy · **breaking it deliberately** |
| [08.9 KNN](../weeks/08.9-knn.md#-exercises) | **The curse** · NumPy · **the RAG connection** |
| [08.10 Clustering](../weeks/08.10-clustering.md#-exercises) | NumPy · **the null test** |
| [08.11 Dim. Reduction](../weeks/08.11-dimensionality-reduction.md#-exercises) | Math (SVD) · NumPy · **t-SNE on noise** |
| [08.12 Evaluation](../weeks/08.12-evaluation.md#-exercises) | Math · **cost-optimal threshold** |
| [08.13 Cross-Validation](../weeks/08.13-cross-validation.md#-exercises) | **The noise experiment** · leakage |
| [08.14 Feature Engineering](../weeks/08.14-feature-engineering.md#-exercises) | Scaling · encoding · imbalance |
| [08.15 Tuning](../weeks/08.15-hyperparameter-tuning.md#-exercises) | Grid vs random · overfitting validation |
| [08.16 Interpretability](../weeks/08.16-interpretability.md#-exercises) | **MDI bias** · SHAP · fairness |
| [08.17 Production](../weeks/08.17-production-ml.md#-exercises) | Serving · **drift** · retraining gates |

---

## 🔗 Cross-lesson exercises

### 1 · The From-Scratch Gauntlet ⭐⭐

**The spine of the module. Do this and you own machine learning.**

Implement **all nine** from scratch, and **verify every one against sklearn:**

| # | Algorithm | Verify with |
|---|---|---|
| 1 | Linear regression (GD + closed form) | `np.allclose(w, sklearn.coef_)` |
| 2 | Logistic regression | `np.allclose(w, LogisticRegression(C=1e10).coef_)` |
| 3 | Decision tree | `np.array_equal(predictions)` |
| 4 | Random Forest | Beats a single tree by a clear margin |
| 5 | Gradient boosting | `np.allclose(rmse, GradientBoostingRegressor)` |
| 6 | Linear SVM (hinge + SGD) | `np.allclose(accuracy, LinearSVC)` |
| 7 | Naive Bayes | `np.array_equal(predictions, MultinomialNB)` |
| 8 | KNN | `np.array_equal(predictions, KNeighborsClassifier)` |
| 9 | K-Means + PCA | ARI ≈ 1.0 / `explained_variance_ratio_` matches |

**Plus: gradient-check the two gradient-based ones.**

> **⭐ When all nine assertions pass, scikit-learn is transparent to you — permanently.**

### 2 · The Leakage Gauntlet ⭐⭐

Build the **same model seven times**, each with a different leak. Report the (fake) score each time, then **write the test that catches it.**

| # | The leak | Lesson |
|---|---|---|
| 1 | Honest baseline | — |
| 2 | Scaler fit on **all** data | [08.13](../weeks/08.13-cross-validation.md) |
| 3 | **Feature selection before CV** *(on random noise!)* | [08.13](../weeks/08.13-cross-validation.md) |
| 4 | **Naive target encoding** | [08.14](../weeks/08.14-feature-engineering.md) |
| 5 | **Random split on grouped data** | [08.13](../weeks/08.13-cross-validation.md) |
| 6 | **Random split on temporal data** (no gap) | [08.13](../weeks/08.13-cross-validation.md) |
| 7 | A **post-event feature** included | [08.16](../weeks/08.16-interpretability.md) |

**⭐ Then run SHAP on #7 and watch the leak scream.**

> **The gap between #1 and #7 is the most persuasive number you will ever put in a portfolio.**

### 3 · The Algorithm Bake-Off

One dataset. **All nine algorithms.** Report:
- Accuracy / PR-AUC **± bootstrap CI**
- **Training time** and **inference latency**
- **Model size** (MB)
- **Interpretable?** (yes/no)
- **Would you ship it?**

**⭐ Then answer honestly: does the best model beat logistic regression by enough to justify its complexity?** *(Often it doesn't — and knowing that is [08.3](../weeks/08.3-linear-regression.md)'s lesson.)*

### 4 · The Threshold Gold Mine ⭐⭐

**The most commercially valuable exercise in this module.**

1. Train any classifier on imbalanced data.
2. Report F1 at threshold 0.5.
3. **Now define `COST_FP` and `COST_FN` in real currency.**
4. **Sweep thresholds on validation. Find the cost-optimal one.**
5. **Report the dollar saving vs 0.5.**
6. Compare that saving against the gain from a **six-hour hyperparameter search.**

> **⭐ The threshold will win. It cost you ten minutes.** ([08.12](../weeks/08.12-evaluation.md))

### 5 · The Bias–Variance Tour

Produce the **same U-curve** with four different dials:

| Dial | Lesson |
|---|---|
| Tree `max_depth` (1→20) | [08.5](../weeks/08.5-decision-trees.md) |
| KNN `k` (1→200) | [08.9](../weeks/08.9-knn.md) |
| Polynomial degree (1→15) | [08.4](../weeks/08.4-logistic-regression.md) |
| Regularization `C` (1e-4→1e4) | [08.3](../weeks/08.3-linear-regression.md) |

**⭐ Plot all four. They're the same picture.** *(Because they're the same idea.)*

### 6 · The Regularization Rhyme

**Show that these four are the same shape — `loss + λ·complexity`:**

1. **Ridge:** $\|Xw-y\|^2 + \lambda\|w\|^2$ ([08.3](../weeks/08.3-linear-regression.md))
2. **Tree pruning:** $R(T) + \alpha|\text{leaves}|$ ([08.5](../weeks/08.5-decision-trees.md))
3. **SVM:** hinge $+ \lambda\|w\|^2$ ([08.7](../weeks/08.7-svm.md))
4. **Laplace smoothing:** a prior on the counts ([08.8](../weeks/08.8-naive-bayes.md))

**Write one paragraph explaining why they're the same idea.**

### 7 · From KNN to RAG ⭐

1. Implement cosine-KNN from scratch (normalize → matmul → argpartition). ([08.9](../weeks/08.9-knn.md))
2. Get 10,000 real sentence embeddings.
3. **Reproduce the curse of dimensionality table.** Then plot the **explained-variance spectrum** of the embeddings. ([08.11](../weeks/08.11-dimensionality-reduction.md))
4. **Explain why the curse doesn't kill RAG.**
5. Compare brute-force vs **FAISS HNSW**: recall@5 and latency.

> **⭐ You have just built a RAG retriever and explained why it works.**

---

## 🧩 Blank-page recall

Close every tab. From memory:

1. Write the **four boxes** and fill them in for three algorithms.
2. Derive the **MSE gradient**. Then the **log-loss gradient**. **Why are they the same?**
3. Write the **ensemble variance formula.** Explain both terms.
4. Explain the **kernel trick** in three sentences.
5. State **which algorithms need scaling, and why.**
6. Name the **four leaks that survive a correct CV.**
7. Explain why **ROC-AUC is optimistic** under imbalance.
8. Write the **threshold-tuning loop.**
9. Explain **why MDI is biased.**
10. Recite the **ten sentences** from the [cheat sheet](../cheat-sheets/ml-cheatsheet.md).

---

## ✅ Solutions

**Deliberately not provided.** Verification is built in — and it's better:

| Exercise | How you know you're right |
|---|---|
| **From-scratch algorithm** | ⭐ **`np.allclose(mine, sklearn)`** |
| **Gradient** | **Central-difference gradient check**, float64 |
| **Leakage** | **Build the leak, watch the score inflate, write the test that catches it** |
| Ensemble | It must beat a single tree |
| Clustering | ⭐ **The null test** (shuffle → re-cluster → compare) |
| Threshold | **Compute the dollar cost.** The number is the answer |
| Drift | **Simulate the incident. Does the monitor fire?** |

> **⭐ Machine learning has a property most subjects lack: you can construct the disaster and prove your defences work.** That beats any answer key — it tells you not just *that* you're right, but *that your guards hold.*

---

[⬆ Module 08](../README.md) · [📖 Lessons](../weeks/README.md) · [🧠 Flashcards](../flashcards/deck.md) · [📝 Quiz](../quizzes/quiz-01.md)
