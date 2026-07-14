# 🧠 Module 08 · Machine Learning — Flashcard Deck

[🏠 Module 08](../README.md) · [📖 Lessons](../weeks/README.md) · [📄 Cheat sheet](../cheat-sheets/ml-cheatsheet.md)

> **~90 cards.** Cover the answer, say it out loud, *then* check. ⭐ marks the ones that will actually save you in production.

---

## 08.1 · What Is ML?

**Q:** ⭐ The one test for whether you need ML?
**A:** **"Can you write the rule?"** If yes — **write the rule.** It's faster, cheaper, testable, deterministic, and won't drift. → [08.1](../weeks/08.1-what-is-ml.md)

**Q:** ⭐ The key distinction between classical ML and deep learning?
**A:** **Who builds the features.** In ML *you* engineer them; in DL the **network learns them.** That's why DL won images/audio/text and **didn't win tabular data.**

**Q:** What still beats deep learning on tabular data?
**A:** **Gradient boosting.** Most revenue-generating ML in the world is **a GBM on 40 hand-built features.**

**Q:** ⭐ Why did self-supervised learning make LLMs possible?
**A:** **The data labels itself** — "predict the next word" needs **no human annotation.** It removes the label bottleneck entirely.

**Q:** The four boxes of every supervised algorithm?
**A:** **Model · Loss · Optimizer · Predict.** *"Learning" is just optimization.*

**Q:** ⭐ What is every algorithm, fundamentally?
**A:** **A bet about the shape of your data.** Linear = a straight line. KNN = near things are alike. NB = features are independent. **The one whose bet matches reality wins** — that's all of model selection.

**Q:** Why is a baseline mandatory?
**A:** *"Predict the majority class."* **A shocking number of production models don't beat it** — and nobody found out, because nobody measured.

---

## 08.2 · The ML Workflow

**Q:** ⭐ Why must the test set be touched exactly once?
**A:** Every look-and-change turns it into a **validation set.** Picking the best of 50 configs by test score = **selecting the max of 50 noisy samples**, which is guaranteed to be an overestimate. → [08.2](../weeks/08.2-ml-workflow.md)

**Q:** ⭐ The five-second overfit/underfit diagnostic?
**A:** **Both errors high → UNDERFIT** (bigger model, more features). **Train low, val high → OVERFIT** (more data, regularize, simplify). **They need OPPOSITE fixes** — check before touching anything.

**Q:** ⭐ How do you read a learning curve?
**A:** Both curves high & converged → **underfit; more data won't help.** Big gap, val still **falling** → **more data WILL help.** Big gap, val **flat** → **regularize instead.** *This plot answers "should we spend $50k on more data?"*

**Q:** ⭐ Why does L1 zero out coefficients but L2 doesn't?
**A:** **Geometry.** L1's constraint region is a **diamond with corners ON the axes**; the loss contours first touch at a corner, where a coefficient is exactly 0. L2's circle has no corners. **Feature selection as a geometric accident.**

**Q:** ⭐⭐ What is error analysis and why does it matter?
**A:** **Look at 100 misclassified examples BY HAND.** Categorize, count, fix the biggest bucket. **It routinely beats any amount of tuning** — and **~15% of your "errors" will turn out to be mislabeled data** (the model was right).

**Q:** In what order should you improve a model?
**A:** Baseline → simple model → **error analysis** → **features** → GBM → **tune LAST.** Tuning is +1–3%; features are +10–40%. **Everyone starts with tuning because it requires no thinking.**

**Q:** Why put everything in a `Pipeline`?
**A:** `cross_val_score` **refits it inside every fold**, so the scaler/imputer learn **only from that fold's training portion.** Scaling before CV leaks every fold's validation data. **It's a structural leakage guard, not tidiness.**

---

## 08.3 · Linear Regression

**Q:** ⭐ Write the MSE gradient and say what it means.
**A:** $\frac{2}{n}X^\top(\hat{y}-y)$ — **"the features, transposed, times the errors."** Each weight's gradient is the dot product of its column with the error vector: *does this feature correlate with our mistakes?* → [08.3](../weeks/08.3-linear-regression.md)

**Q:** Normal equations vs gradient descent?
**A:** Closed form: **exact, no hyperparameters, but O(d³)** and breaks on collinear features. GD: **O(nd)/step**, scales, and **generalizes to every non-convex model** (all of deep learning).

**Q:** Why never `np.linalg.inv`?
**A:** Slower **and** numerically worse than `solve` — it amplifies error, catastrophically when ill-conditioned.

**Q:** ⭐ Why does Ridge make $X^\top X$ always invertible?
**A:** $+\lambda I$ **adds λ to every eigenvalue.** Singular ⟺ a zero eigenvalue — so with λ>0 all eigenvalues are strictly positive. **Ridge makes an unsolvable problem solvable**, not just a less-overfit one.

**Q:** Ridge vs Lasso?
**A:** **Ridge (L2)** shrinks toward 0, handles correlated features. **Lasso (L1)** drives them to **exactly 0** → free feature selection, but arbitrarily picks one of a correlated pair.

**Q:** ⭐ Why must you scale before gradient descent?
**A:** Unscaled features (age 0–100 vs income 0–1e6) give $X^\top X$ a **condition number in the millions** — a ravine so narrow that any safe learning rate takes a million steps. **The #1 reason a from-scratch implementation "doesn't work."**

**Q:** Why never regularize the bias?
**A:** It's the model's **baseline prediction**, not a measure of complexity. Shrinking it just biases every prediction downward.

**Q:** ⭐ What does a residual plot tell you?
**A:** **Random cloud** → good. **A curve** → **non-linearity** (add polynomial features or use a tree). **A funnel** → **heteroscedasticity** (try log(y)). *One plot, three assumptions, ten seconds.*

**Q:** What does R² < 0 mean?
**A:** **Your model is worse than predicting the mean.**

---

## 08.4 · Logistic Regression

**Q:** ⭐⭐ Why is MSE catastrophic for logistic regression?
**A:** Its gradient contains a factor of **σ′(z)**, which **→ 0 for large |z|**. So a **confidently WRONG** prediction (p̂=0.001 when y=1) gets **almost no gradient** — the model sits there being confidently wrong and **learning nothing.** *Vanishing gradient exactly where you most need a big one.* → [08.4](../weeks/08.4-logistic-regression.md)

**Q:** ⭐ What's the log-loss gradient, and why is it remarkable?
**A:** $\frac{1}{n}X^\top(\hat{p}-y)$ — **IDENTICAL to linear regression's.** The σ′ terms **cancel exactly.** Not luck: it's a property of pairing an exponential-family model with its matching loss.

**Q:** ⭐ How do you interpret a logistic regression coefficient?
**A:** **$e^{w_j}$ is the ODDS RATIO.** If $w_{\text{smoker}}=0.7$, then $e^{0.7}\approx 2$ — **being a smoker doubles the odds.** *This is why medicine and credit scoring still use it.*

**Q:** What shape is the decision boundary?
**A:** A **hyperplane** — always **linear**, despite the sigmoid. **It cannot solve XOR.** Add polynomial features (→ the kernel trick).

**Q:** ⭐ What happens on perfectly separable data without regularization?
**A:** **Coefficients diverge to infinity** — scaling w up always makes the log-loss strictly smaller. **This is why sklearn regularizes by default.**

**Q:** What is sklearn's `C`?
**A:** **INVERSE** regularization. Small C = **strong** regularization. `C=1e10` ≈ none. **Everyone gets this backwards once.**

**Q:** ⭐⭐ Why is 0.5 almost never the right threshold?
**A:** **FP and FN rarely cost the same.** If FN costs $2000 and FP costs $5, the optimal threshold is ~0.1 — and using it can **halve your cost with no model change.** **The threshold is a business decision, and tuning it is free.**

---

## 08.5 · Decision Trees

**Q:** ⭐ How does a tree choose a split?
**A:** **Greedily** — try every feature × threshold, compute **information gain**, take the max, recurse. **Finding the optimal tree is NP-complete**, so greedy is what we can afford. → [08.5](../weeks/08.5-decision-trees.md)

**Q:** Entropy vs Gini?
**A:** $-\sum p\log p$ vs $1-\sum p^2$. **They pick the same splits ~98% of the time. Gini is faster (no logs).**

**Q:** ⭐ Why does an unpruned tree always overfit?
**A:** It grows until every leaf is pure — so it can hit **100% training accuracy on ANY data, including pure noise**, by giving each point its own leaf. **Trees are variance machines.**

**Q:** ⭐ Why don't trees need scaling?
**A:** Splits are `feature <= threshold` — **scale-invariant.** `age <= 30` means the same in years or milliseconds.

**Q:** ⭐ What can't trees do?
**A:** **Diagonal boundaries** (axis-aligned cuts → a staircase of 20 splits where a line needs 1 parameter) and **extrapolation** (a regression leaf predicts a **constant** — it's flat outside the training range).

**Q:** ⭐ Why is `feature_importances_` (MDI) untrustworthy?
**A:** **Biased toward high-cardinality features** (more split points = more chances to look useful by luck) and **splits credit among correlated features.**

**Q:** Why is a single tree rarely a production model?
**A:** **Instability** — retrain on a slightly different sample and you get a **completely different tree**, which destroys the interpretability that was its whole selling point.

---

## 08.6 · Ensembles

**Q:** ⭐⭐ Why do ensembles work?
**A:** $\text{Var}(\bar{f}) = \rho\sigma^2 + \frac{1-\rho}{M}\sigma^2$. **The second term vanishes as M grows; the first doesn't.** **So the entire game is DECORRELATING the models (lowering ρ).** If ρ=1, averaging does nothing. → [08.6](../weeks/08.6-ensembles.md)

**Q:** ⭐ How does Random Forest decorrelate its trees?
**A:** **Bootstrap sampling** (different data) and — the big one — **random feature subsets at every split** (`max_features='sqrt'`), which **forbids** some trees from using the dominant feature.

**Q:** ⭐ What's counterintuitive about `max_features`?
**A:** **Deliberately handicapping each individual tree makes the forest BETTER** — because it decorrelates them, and ρ is what limits the variance reduction.

**Q:** What is OOB scoring?
**A:** Each bootstrap leaves out **~36.8%** of rows. Evaluate each tree on the rows it never saw. **Free cross-validation, no extra fitting.** `oob_score=True`.

**Q:** ⭐ Why is it called *gradient* boosting?
**A:** **The residual $y-F(x)$ IS the negative gradient of $\frac{1}{2}(y-F)^2$.** So it's **gradient descent in FUNCTION space** — each "step" is a whole tree. **Swap the loss and it still works** — that's why it's a *framework*.

**Q:** ⭐ Bagging vs boosting, fundamentally?
**A:** **Bagging:** parallel, independent, **DEEP** trees, **averaged** → reduces **variance**. **Boosting:** sequential, **SHALLOW** trees fitting the **residuals**, **summed** → reduces **bias**.

**Q:** ⭐⭐ Why is early stopping mandatory for boosting but not RF?
**A:** **More trees never hurts RF** (the variance term keeps shrinking). **Boosting eventually fits noise** — once the signal is exhausted, each new tree fits residual *noise*, and validation loss makes a **U**.

**Q:** How do you tune `n_estimators` for a GBM?
**A:** **Don't grid-search it.** Set it absurdly high (5000), use a small learning rate, and **let early stopping decide.**

**Q:** Why does hand-rolled stacking leak?
**A:** The meta-model sees **predictions the base models made on data they memorized.** Use **out-of-fold** predictions (`cv=5`).

---

## 08.7 · SVM

**Q:** ⭐ What does an SVM optimize?
**A:** The **maximum margin** — the widest buffer between classes. Minimize $\frac{1}{2}\|w\|^2$ s.t. $y_i(w^\top x_i+b)\ge1$. **Maximizing the margin IS regularization.** → [08.7](../weeks/08.7-svm.md)

**Q:** ⭐ What is a support vector?
**A:** A point **on or inside the margin.** **They are the ONLY points that determine the hyperplane** — delete the other 99% and you get the identical model.

**Q:** ⭐ Where does the sparsity come from?
**A:** **The hinge loss is EXACTLY ZERO** for points correctly classified beyond the margin → zero gradient → they don't move `w`. **Log-loss is NEVER exactly zero, so every point tugs.** *That one difference is the whole distinction between SVM and logistic regression.*

**Q:** ⭐⭐ Explain the kernel trick.
**A:** In the dual, **the data appears only inside DOT PRODUCTS.** So replace $x_i^\top x_j$ with $K(x_i,x_j)=\phi(x_i)^\top\phi(x_j)$ — **a single number computable in O(d) without ever constructing φ(x).** For **RBF, φ maps into INFINITE dimensions** and you compute the inner product with one exponential.

**Q:** What do `C` and `gamma` control?
**A:** **C: INVERSE regularization** (small = wide margin). **Gamma: influence width** (large = the boundary wraps around individual points = memorization). **Tune them JOINTLY, on a log scale.**

**Q:** ⭐ Why is scaling mandatory for SVMs?
**A:** The RBF kernel is $\exp(-\gamma\|x-x'\|^2)$ — **built on Euclidean distance.** An unscaled feature with a 1000× range **dominates completely.** *The #1 reason people think "SVMs don't work."*

**Q:** Why can't kernel SVMs scale?
**A:** The **kernel matrix is n×n** — O(n²)–O(n³). At n=100k that's **80 GB.** **Unusable above ~50k samples.**

**Q:** Do SVMs give probabilities?
**A:** **No** — a **signed distance.** `probability=True` costs **5× training time** and is poorly calibrated.

---

## 08.8 · Naive Bayes

**Q:** ⭐ The naive assumption, and what it buys?
**A:** Features are **conditionally independent given the class** → $2^{1000}$ parameters become $2\times1000$, **estimable by just counting.** → [08.8](../weeks/08.8-naive-bayes.md)

**Q:** ⭐⭐ The assumption is obviously false. Why does it still work?
**A:** **Classification only needs the correct RANKING, not calibrated probabilities.** NB's probabilities are garbage (it double-counts correlated evidence), but **the right class is still on top, and argmax doesn't care by how much.** *A model can be badly wrong about the world and still useful for the decision you need.*

**Q:** ⭐ Why is Laplace smoothing essential?
**A:** Without it, **a single unseen word gives P=0**, which **zeroes the ENTIRE product** — vetoing all other evidence. *(It's a Bayesian prior in disguise.)*

**Q:** ⭐ Why must NB work in log space?
**A:** Multiplying 200 probabilities of ~0.001 gives $10^{-600}$ — which **underflows to exactly zero.** **`log(∏p) = Σ log(p)`.**

**Q:** What kind of classifier is NB, structurally?
**A:** **A linear classifier in log space.** Prediction = `X @ log_likelihood.T + log_prior` — **one matmul.**

**Q:** How fast is training?
**A:** ⭐ **ONE PASS, O(nd), no optimization at all.** No gradients, no iterations. **Just count.**

**Q:** ⭐ When does NB beat sophisticated models?
**A:** **In the LOW-DATA regime.** Its strong assumption = **high bias, LOW variance** — and when data is scarce, that beats a flexible model that overfits. As data grows, they overtake it — because their variance falls and **NB's bias doesn't go anywhere.**

---

## 08.9 · KNN

**Q:** Why is KNN "lazy"?
**A:** **Training is O(1)** (just store), but **prediction is O(n·d) PER QUERY.** It **inverts the normal cost structure** — catastrophic in production. → [08.9](../weeks/08.9-knn.md)

**Q:** ⭐ Why is scaling mandatory?
**A:** `age` differing by 5 vs `income` by 5,000 → **income contributes 99.9999% of the distance.** The model is **blind to age.** *(Wine dataset: 0.72 → 0.96 from one line.)*

**Q:** ⭐⭐ What is the curse of dimensionality?
**A:** As d grows, **all pairwise distances converge to the same value.** At d=10,000 the closest point is only **9% closer** than the farthest. **"Nearest neighbor" becomes meaningless** — and it breaks **every** distance-based method.

**Q:** ⭐⭐ Then why does RAG work with 768-d embeddings?
**A:** **Learned embeddings aren't random points in 768-D** — they live on a **low-dimensional MANIFOLD**, because the model was *trained* to put similar things close. **The curse applies to random high-d data, not structured representations.**

**Q:** ⭐ Connection between KNN and RAG?
**A:** **They are the same algorithm.** RAG = **cosine-KNN over learned embeddings with an ANN index.** Fix KNN's two flaws (the curse → embeddings; O(n) queries → HNSW) and **the laziest algorithm in ML becomes the retrieval layer of the AI industry.**

**Q:** Why do KD-trees fail in high dimensions?
**A:** They prune by proving *"nothing in this box can be closer."* **In high d that proof almost always fails** — so the tree visits nearly every node. **Slower than brute force above d≈20.**

**Q:** KNN's unique privacy problem?
**A:** **The model IS the training data.** Shipping it ships every example.

---

## 08.10 · Clustering

**Q:** ⭐⭐ The most dangerous property of clustering?
**A:** **It ALWAYS returns an answer.** Ask K-Means for 5 clusters in **pure noise** and you get 5 beautiful clusters. **No ground truth, so nothing catches you.** → [08.10](../weeks/08.10-clustering.md)

**Q:** ⭐⭐ How do you actually validate a clustering?
**A:** **Do the clusters differ on something you did NOT cluster on?** (churn, revenue) **Plus THE NULL TEST: shuffle the data, re-cluster, compare silhouettes.** If noise scores nearly as well, **you found nothing.**

**Q:** Is K-Means guaranteed to find the best clustering?
**A:** It **converges** but **NOT to the global optimum** (non-convex). Hence `n_init=10` and **k-means++**.

**Q:** ⭐ What does K-Means assume, and how does it break?
**A:** **Spherical, equal-size, equal-density clusters, no noise.** It draws straight-line **Voronoi boundaries** — so it **cannot find a ring or a crescent** — and **outliers drag its centroids.**

**Q:** ⭐ Why is the elbow method unreliable?
**A:** **Inertia ALWAYS decreases with k** (at k=n it's 0), so **there's no minimum to find.** Use **silhouette** (has a real max) or **GMM's BIC** (principled).

**Q:** When do you use DBSCAN?
**A:** **Arbitrary shapes**, **you don't know k**, and **you want outliers labelled** (`-1` = noise → a free outlier detector). **Flaw: one global `eps` fails with varying densities** → **HDBSCAN.**

**Q:** Why can't you compare cluster labels directly?
**A:** **Labels are arbitrary.** Use the **Adjusted Rand Index (ARI)**.

---

## 08.11 · Dimensionality Reduction

**Q:** ⭐ How do you compute PCA properly?
**A:** **Center, then take the SVD.** The **right singular vectors are the PCs.** **Never form $X^\top X$** — it **squares the condition number.** → [08.11](../weeks/08.11-dimensionality-reduction.md)

**Q:** ⭐⭐ Why is centering mandatory?
**A:** Variance is defined **around the mean.** Without centering, **PC1 points AT the mean** — a direction carrying **no information about how the data varies.** **And it fails silently.**

**Q:** ⭐ Why does PCA cure multicollinearity?
**A:** **The components are ORTHOGONAL by construction.** **The price is interpretability** — a PC is a meaningless blend.

**Q:** ⭐⭐ Three ways people misread t-SNE plots?
**A:** **(1) Cluster SIZES are meaningless.** **(2) DISTANCES between clusters are meaningless.** **(3) It invents clusters in PURE NOISE.** **t-SNE is for looking, not measuring.**

**Q:** ⭐ The killer difference between t-SNE and UMAP?
**A:** **t-SNE cannot `transform()` new points** — there is no such method. **It cannot live in a pipeline.** UMAP can.

**Q:** ⭐ Why does dimensionality reduction work at all?
**A:** **Real data is almost never full-rank.** Its singular-value spectrum **decays fast** (random data's is flat). **That decay is why PCA, compression, and LoRA all work.**

---

## 08.12 · Evaluation

**Q:** ⭐ Why is accuracy dangerous?
**A:** On imbalanced data, **predicting the majority class gets 99% while catching nothing.** *"99% accurate"* should always be met with **"what's the class balance?"** → [08.12](../weeks/08.12-evaluation.md)

**Q:** ⭐⭐ Why is ROC-AUC misleading under imbalance?
**A:** **FPR's denominator is FP+TN, and TN is ENORMOUS.** 900 false positives out of 9,900 negatives → FPR = 0.09, which **looks tiny** — while **precision is 10%.** **PR-AUC has NO TN**, so it can't hide them.

**Q:** ⭐⭐ Why is tuning the threshold so valuable?
**A:** **It's FREE and routinely beats every model improvement combined.** Tuning buys +1–3%; moving the threshold to the cost-optimal point can **halve your business cost with no model change.** **Almost nobody does it.**

**Q:** Why is F1 often wrong?
**A:** It **assumes FP and FN cost the same.** They almost never do.

**Q:** Which models are well-calibrated?
**A:** **Logistic regression** ✅ (log-loss *is* a calibration objective). **Naive Bayes** ❌ (wildly overconfident). **SVM** ❌ (a distance). **Neural nets** ❌ (notoriously overconfident).

**Q:** ⭐ How should every metric be reported?
**A:** **Value ± CI, with n, SLICED by segment.** A bare number is an opinion.

---

## 08.13 · Cross-Validation & Leakage

**Q:** ⭐⭐ Why must preprocessing be inside the CV loop?
**A:** `cross_val_score` **refits the pipeline inside every fold**, so the scaler learns **only from that fold's training portion.** **Scaling before CV means every fold's validation data contributed to μ and σ.** **The most common leak in applied ML, and it's invisible.** → [08.13](../weeks/08.13-cross-validation.md)

**Q:** ⭐ What if you do feature selection before CV?
**A:** **~90% CV accuracy on PURE RANDOM NOISE** — the selector already found the features fitting the labels, *including in the validation folds*.

**Q:** ⭐⭐ When do you need `GroupKFold`?
**A:** Whenever rows **share a source** — 30 X-rays from one **patient**, 40 reviews of one **product**. A random split makes the model learn *the patient*, not the disease. **This has invalidated an alarming number of medical imaging papers.**

**Q:** ⭐⭐ Why does time-series CV need a gap?
**A:** A test row's `rolling_7d` feature uses the **previous 7 days — which are in your training set.** **Gap = the forecast horizon.**

**Q:** Why is the best CV score after tuning biased?
**A:** **You selected the maximum of N noisy samples.** **Nested CV, or a held-out test set touched once.**

**Q:** ⭐ Which leak can CV NOT catch?
**A:** **Target leakage in the features themselves.** The feature is legitimately in the data — **it just wouldn't exist at prediction time.** **Only the availability question catches it.**

---

## 08.14 · Feature Engineering

**Q:** ⭐ Which algorithms need scaling, and why?
**A:** **Distance-based** (KNN, SVM, K-Means, PCA — **mandatory**) and **gradient-based** (linear, logistic, NN). **Trees DON'T** — splits are **scale-invariant.** → [08.14](../weeks/08.14-feature-engineering.md)

**Q:** ⭐ Why is "just use LightGBM" good advice?
**A:** **No scaling, native missing values, native categoricals, outlier-robust.** It removes **four whole categories of preprocessing decision** — each a chance for a bug or a leak.

**Q:** ⭐ Why does naive target encoding leak catastrophically?
**A:** `groupby.transform('mean')` gives each row **its own target** — literally, for a category of size 1. **Use out-of-fold + smoothing.**

**Q:** ⭐ What's wrong with SMOTE?
**A:** It **interpolates**, which in high dimensions can create **implausible points** and **cross the class boundary.** **It must be inside the CV loop** or it's a catastrophic leak. **`class_weight` frequently matches or beats it.**

**Q:** ⭐ Best first moves for imbalanced data?
**A:** **`class_weight='balanced'` + tune the threshold + report PR-AUC.** Two lines.

---

## 08.15 · Hyperparameter Tuning

**Q:** ⭐⭐ Why does random search beat grid search?
**A:** **Most hyperparameters don't matter.** A 3×3 grid tests only **3 distinct values** of the one that does. **Random search with 9 samples tests 9 distinct values — 3× the resolution, same compute** — and it gets exponentially better with more dimensions. → [08.15](../weeks/08.15-hyperparameter-tuning.md)

**Q:** ⭐ Why sample learning rates on a **log** scale?
**A:** 0.001 vs 0.01 is **enormous**; 0.21 vs 0.22 is **nothing.** A uniform draw wastes 97% of its samples.

**Q:** What is Bayesian optimization?
**A:** A **surrogate model** + an **acquisition function** balancing **exploit** (high predicted score) and **explore** (high uncertainty). 10–50 evaluations instead of hundreds. **Worth it only when each fit is expensive.**

**Q:** ⭐ Why prefer a plateau over a peak?
**A:** **A lone spike is almost always luck.** A broad flat region is a **robust** setting that generalizes.

**Q:** ⭐ Where does tuning belong, and why?
**A:** **LAST.** It buys **+1–3%.** Error analysis and features buy **+10–40%.** **Everyone starts with tuning because it's the part you can do without thinking.**

---

## 08.16 · Interpretability

**Q:** ⭐ Why is MDI untrustworthy?
**A:** **Biased toward high-cardinality features** — **a random ID column often ranks top-5** — and it **splits credit among correlated features.** → [08.16](../weeks/08.16-interpretability.md)

**Q:** ⭐⭐ What makes SHAP special?
**A:** **Shapley values** — the **UNIQUE** attribution satisfying **efficiency, symmetry, dummy, additivity.** **A theorem, not a heuristic.** No other method here has one.

**Q:** ⭐⭐ SHAP's most valuable use?
**A:** **FINDING YOUR OWN LEAKS.** A feature carrying 80% of the SHAP mass is a **bug report.**

**Q:** SHAP vs LIME?
**A:** SHAP has a **uniqueness theorem and is consistent**; LIME is a heuristic that **can give different explanations on different runs** — disqualifying when you must defend a decision.

**Q:** ⭐ Why do PDPs lie when features are correlated?
**A:** They evaluate the model at **unrealistic combinations** — an **8-bedroom, 500 sq ft studio.** Use **ALE**.

**Q:** ⭐⭐ Can you satisfy all fairness definitions?
**A:** **No — they are mathematically INCOMPATIBLE** (the impossibility theorem). **Choose one deliberately** — an ethical/legal decision, not a technical one.

**Q:** ⭐ Does removing the protected attribute make a model fair?
**A:** **No.** **Proxies reconstruct it** (zip → race). **It only removes your ability to MEASURE the disparity.**

---

## 08.17 · Production

**Q:** ⭐⭐ Why monitor inputs rather than performance?
**A:** **Performance needs LABELS, which arrive late** — churn 90 days, default 2 years. **By the time accuracy drops, you've made bad decisions for a quarter.** **Input drift is observable immediately — a LEADING indicator.** → [08.17](../weeks/08.17-production-ml.md)

**Q:** ⭐ The cheapest, best drift signal?
**A:** **The PREDICTION DISTRIBUTION.** No labels, no ground truth. **If the mean predicted probability jumps overnight, you know TODAY.**

**Q:** ⭐ What five things go in the model artifact?
**A:** **(1)** The pipeline (preprocessing **+** model). **(2)** The **tuned threshold**. **(3)** The feature list/order. **(4)** The manifest (git SHA + **dirty flag**, data hash, versions). **(5)** ⭐ **The training feature distributions — your drift baseline, which you CANNOT get retroactively.**

**Q:** ⭐⭐ Why can automated retraining make things worse?
**A:** **(1) Feedback loops** — the model confirms its own beliefs. **(2) Bad data** — a broken upstream means you **automatically deploy a model trained on corruption.** **Every retrain needs a GATE that can REFUSE.**

**Q:** What is shadow mode?
**A:** **Run the new model on real traffic, log what it WOULD have done, don't act on it.** **Real evidence, zero risk.** Nearly free, almost nobody does it.

**Q:** ⭐ The #1 regret of ML teams?
**A:** **Not logging inference inputs from day one.** You cannot detect drift on data you didn't keep, and **you cannot get it retroactively.**

---

## 🎯 The ten sentences (recall all ten cold)

1. **"Can you write the rule?"** If yes — **write the rule.**
2. **Every algorithm is a bet about the shape of your data.**
3. **model · loss · gradient · update** — and `predicted − actual` is the gradient, three times.
4. **Ensembles work by DECORRELATION.** ρσ² is the floor.
5. **Accuracy is a lie. ROC-AUC is optimistic. TUNE THE THRESHOLD.**
6. **Everything with a `fit` goes inside the Pipeline — or you leak.**
7. **CV cannot catch target leakage.** Only *"would I have this value at prediction time?"*
8. **Error analysis (+10–40%) beats tuning (+1–3%).** Everyone does it backwards.
9. **`feature_importances_` will rank a random ID column in your top 5.**
10. **Monitor inputs, not performance — labels arrive months too late.**

---

[⬆ Module 08](../README.md) · [📖 Lessons](../weeks/README.md) · [📄 Cheat sheet](../cheat-sheets/ml-cheatsheet.md) · [📝 Quiz](../quizzes/quiz-01.md)
