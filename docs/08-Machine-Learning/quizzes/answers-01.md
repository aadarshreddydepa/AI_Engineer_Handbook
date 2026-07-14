# ✅ Answers · Module 08 Quiz 01

[🏠 Module 08](../README.md) · [❓ Questions](quiz-01.md)

---

## Part 1 — Foundations & Linear Models

**1.** **"Can you write the rule?"** If yes — **write the rule.** It's faster, cheaper, testable, auditable, deterministic, and won't drift. **ML is for when the rule exists but is too complex, fuzzy, or changeable for a human to state.** Using ML where an `if` would work is the most common failure in applied AI. → [08.1](../weeks/08.1-what-is-ml.md)

**2.** ⭐ **MODEL · LOSS · OPTIMIZER · PREDICT.**

| | Model | Loss | Optimizer |
|---|---|---|---|
| Linear reg | $Xw+b$ | MSE | Normal eq. or GD |
| Decision tree | Nested if/else | Gini/entropy | Greedy splitting |
| **KNN** | *(none — it memorizes)* | *(none)* | *(none — lazy!)* |

**KNN's is strange because it has none of them.** There's no model, no loss, no optimization — **the training data IS the model.** That's why it's called a *lazy* / instance-based learner, and it's why its cost structure is inverted (O(1) training, O(n) prediction). → [08.1](../weeks/08.1-what-is-ml.md)

**3.** ⭐ **Every time you look at the test set and change something, it becomes a validation set.** Try 50 configs and pick the best *test* score, and you have **selected the maximum of 50 noisy samples** — which is *guaranteed* to be an overestimate. **You no longer have an honest generalization estimate.** *(The whole field does this to ImageNet/MMLU, which is why published gains often don't replicate.)* → [08.2](../weeks/08.2-ml-workflow.md)

**4.** ⭐ **Both errors high → UNDERFIT** (bias). Fix: **bigger model, more features, less regularization.**
**Train low, val high → OVERFIT** (variance). Fix: **more data, regularization, simpler model, early stopping.**

**They need opposite fixes** — and **half of all ML debugging time is spent applying the overfitting fix to an underfitting problem.** Compare two numbers first. → [08.2](../weeks/08.2-ml-workflow.md)

**5.** ⭐ $J = \frac{1}{n}\|Xw - y\|^2$. Chain rule (outer $u^2$, inner $u = Xw - y$):

$$\nabla_w J = \frac{2}{n}X^\top(Xw - y) = \frac{2}{n}X^\top(\hat{y} - y)$$

**Shapes:** $X^\top$ is `(d,n)`, the error is `(n,)` → result is `(d,)` = **the same shape as w** ✓ *(That shape check is how you derive the transpose rather than memorizing it.)*

**In English: "the features, transposed, times the errors."** Each weight's gradient is the **dot product of its feature column with the error vector** — i.e. *"does this feature correlate with our mistakes?"* **That is the whole of gradient descent, in one sentence.** → [08.3](../weeks/08.3-linear-regression.md)

**6.** ⭐ Ridge's solution is $(X^\top X + \lambda I)^{-1}X^\top y$. **The $\lambda I$ adds λ to every diagonal entry — which adds λ to every eigenvalue.**

A matrix is **singular exactly when it has a zero eigenvalue.** So if $X^\top X$ is singular (perfectly collinear features), **$X^\top X + \lambda I$ has all eigenvalues ≥ λ > 0 — it is ALWAYS invertible.**

**Ridge doesn't just reduce overfitting. It makes an unsolvable problem solvable.** → [08.3](../weeks/08.3-linear-regression.md)

**7.** ⭐⭐ With MSE + sigmoid, the chain rule puts a factor of **σ′(z)** in the gradient. And **σ′(z) → 0 when |z| is large.**

**So: true label 1, model predicts p̂ = 0.001 (z ≈ −7). It is maximally, catastrophically wrong. But σ′(−7) ≈ 0.0009 — essentially zero. The gradient is essentially zero. The model barely updates.**

**MSE + sigmoid has a vanishing gradient exactly where you most need a large one.** The model sits there being confidently wrong and **learning nothing.**

**Log-loss fixes it:** $-\log(\hat{p}) \to \infty$ as $\hat{p} \to 0$ — **confident wrongness is punished nearly infinitely**, which is precisely the incentive you want. → [08.4](../weeks/08.4-logistic-regression.md)

**8.** ⭐ $$\nabla_w J = \frac{1}{n}X^\top(\hat{p} - y)$$

**It is IDENTICAL to linear regression's** (up to the constant). **The σ′ terms cancel exactly.**

**This isn't luck — it's a property of pairing an exponential-family model with its matching loss.** The ugly terms are *designed* to cancel. It's the same cancellation as softmax + cross-entropy ([06.8](../../06-Mathematics/weeks/06.8-information-theory.md)), and it's why frameworks **fuse** sigmoid+log-loss and softmax+CE into single operations.

**`predicted − actual`. Every time.** → [08.4](../weeks/08.4-logistic-regression.md)

---

## Part 2 — Trees, Ensembles, SVM

**9.** **Greedily.** Try **every feature × every threshold**, compute the **information gain** ($H_{\text{parent}} - \sum\frac{n_k}{n}H_{\text{child}}$), take the maximum, and **recurse.**

**It's greedy because finding the globally optimal tree is NP-complete.** The consequence: **a pair of splits that would be brilliant *together* may each look mediocre alone**, so the tree misses them. **That weakness is precisely what ensembles exist to paper over.** → [08.5](../weeks/08.5-decision-trees.md)

**10.** ⭐ It grows **until every leaf is pure** — so it can give **each training point its own leaf.** That means it achieves **100% training accuracy on ANY dataset, including pure random noise.** **Trees are variance machines**, and everything about using them well is about controlling that (`max_depth`, `min_samples_leaf`, `ccp_alpha`). → [08.5](../weeks/08.5-decision-trees.md)

**11.** ⭐ **No scaling needed:** splits are `feature <= threshold` — **scale-invariant.** `age <= 30` means the same thing in years or milliseconds.

**Two things trees cannot do:**
- **Diagonal boundaries.** They cut only **axis-aligned**, so `x₁ + x₂ = 5` — one parameter for a linear model — becomes a **staircase of 20 splits** that still generalizes badly.
- **Extrapolate.** A regression leaf predicts the **mean of its samples** — a constant. **Ask it about a house 2× bigger than any it saw, and it returns the same value as the biggest one it saw.** → [08.5](../weeks/08.5-decision-trees.md)

**12.** ⭐⭐ $$\text{Var}\!\left(\tfrac{1}{M}\sum f_m\right) = \underbrace{\rho\sigma^2}_{\text{the FLOOR}} + \underbrace{\tfrac{1-\rho}{M}\sigma^2}_{\text{vanishes as } M \to \infty}$$

**The second term disappears with more models. The first does not.**

**⭐ So the entire game is DECORRELATING the models (lowering ρ).** **If ρ = 1 — if your models are identical — averaging does absolutely nothing.** You've built the same model 500 times.

**The bias stays the same; the variance drops.** It is one of the few genuinely free lunches in machine learning. → [08.6](../weeks/08.6-ensembles.md)

**13.** ⭐ Two mechanisms: **bootstrap sampling** (each tree sees different data) and — the important one — **random feature subsets at every split** (`max_features='sqrt'`).

**Why it's counterintuitive: deliberately handicapping each individual tree makes the forest BETTER.** Without feature subsampling, if one feature is very predictive, **every tree splits on it first** and all your trees look nearly identical (ρ → 1), so averaging buys almost nothing. **Forbidding some trees from using the dominant feature forces them to find other signal — they become genuinely different, ρ drops, and the variance term collapses.** → [08.6](../weeks/08.6-ensembles.md)

**14.** ⭐ **Because the residual $y - F(x)$ IS the negative gradient of the squared-error loss:**

$$L = \tfrac{1}{2}(y-F)^2 \;\Rightarrow\; -\frac{\partial L}{\partial F} = y - F$$

**So gradient boosting is gradient descent in FUNCTION space** (rather than parameter space), where **each "step" is a whole decision tree** that approximates the negative gradient.

**That reframing is why it's a framework, not an algorithm: swap in ANY differentiable loss** — log-loss for classification, Huber for robust regression, a ranking loss for search — **and just fit the trees to that loss's negative gradient.** Everything else is unchanged. *(Friedman, 2001.)* → [08.6](../weeks/08.6-ensembles.md)

**15.** ⭐ **RF: more trees NEVER hurts** — the variance term $\frac{1-\rho}{M}\sigma^2$ just keeps shrinking toward the floor. So `n_estimators=500` is a safe default you barely need to tune.

**Boosting: more trees EVENTUALLY HURTS.** Each tree fits the **residuals** — and **once the real signal is exhausted, new trees start fitting the noise.** Validation loss makes a **U**.

**Consequence: set `n_estimators=5000` and let early stopping decide. NEVER grid-search it.** → [08.6](../weeks/08.6-ensembles.md)

**16.** ⭐⭐ **In the SVM's dual formulation, the data appears ONLY inside dot products** — both in the objective and in the prediction.

**So you never need φ(x). You only need $\phi(x_i)^\top\phi(x_j)$ — a single NUMBER.** And for many useful φ, **that number has a closed form computable directly in the original space, in O(d) time**, without ever constructing the high-dimensional vectors.

$$K(x_i, x_j) = \phi(x_i)^\top\phi(x_j)$$

**For the RBF kernel, φ maps into an INFINITE-dimensional space — and you compute the inner product with one exponential.** **You are working in infinite dimensions and it costs you a dot product.** → [08.7](../weeks/08.7-svm.md)

---

## Part 3 — NB, KNN, Clustering, PCA

**17.** ⭐⭐ **Because classification only needs the RANKING of the classes to be correct — not the probabilities themselves.**

Naive Bayes multiplies correlated word-probabilities as if they were independent, **double-counting the same evidence over and over.** So it produces **wildly miscalibrated** probabilities (0.99999999 is routine, and meaningless).

**But the correct class is still on top. And `argmax` doesn't care by how much.**

**What it DOES ruin: the probabilities.** Never use NB's `predict_proba` as a probability.

**⭐ The transferable lesson: a model can be badly wrong about the world and still be useful for the decision you actually need to make.** *(Domingos & Pazzani, 1997.)* → [08.8](../weeks/08.8-naive-bayes.md)

**18.** ⭐ **Without Laplace smoothing:** a word unseen in training gives $P(\text{word} \mid \text{class}) = 0$, which **zeroes the ENTIRE product.** *"free money viagra winner prize"* — **doesn't matter. One unseen word vetoes all the other evidence.** Add α to every count.

**Without log space:** multiplying 200 probabilities of ~0.001 gives $10^{-600}$, which **underflows to EXACTLY ZERO in float64.** Every class gets probability 0; **the argmax is meaningless.** `log(∏p) = Σ log(p)` — products become sums, and underflow becomes impossible. **Every NLP system does this.** → [08.8](../weeks/08.8-naive-bayes.md)

**19.** ⭐⭐ **As dimensionality grows, all pairwise distances converge to the same value:**

$$\frac{\text{dist}_{\max} - \text{dist}_{\min}}{\text{dist}_{\min}} \to 0$$

**At d = 10,000, the closest point is only ~9% closer than the farthest one.**

**"Nearest neighbor" stops meaning anything** — you're voting among points that aren't actually similar to your query in any useful sense. **And it breaks EVERY distance-based method**: KNN, K-Means, RBF-SVMs, and KD-trees (which is why they degrade to brute force above d ≈ 20). → [08.9](../weeks/08.9-knn.md)

**20.** ⭐⭐ **Because learned embeddings are NOT random points in 768-D.**

**They live on a low-dimensional MANIFOLD** inside that space — the model was **trained** to place semantically similar things close together and dissimilar things far apart. **The intrinsic dimensionality is far lower than 768.** *(Plot the explained-variance spectrum: 95% of the variance is often in ~40 of 768 components.)*

**The curse applies to random high-dimensional data, not to structured, learned representations.** **That is precisely what makes embeddings valuable** — and it's the curse being **defeated by learning the right space to measure distance in.** → [08.9](../weeks/08.9-knn.md), [08.11](../weeks/08.11-dimensionality-reduction.md)

**21.** ⭐⭐ **It ALWAYS returns an answer.** Ask K-Means for 5 clusters in **pure random noise** and you get **5 beautiful clusters, with centroids and everything.** **There is no ground truth, so nothing catches you.**

**How to actually validate:**
1. **⭐ EXTERNAL VALIDATION — do the clusters differ on something you did NOT cluster on?** (churn rate, revenue, support volume.) **If your "customer segments" have identical churn and revenue, you have partitioned your data and learned nothing.**
2. **⭐ THE NULL TEST — shuffle each feature column independently (destroying real structure, preserving marginals), re-cluster, and compare silhouettes.** If real data scores 0.42 and shuffled noise scores 0.38, **you found nothing.** *(Almost nobody runs this.)*
3. Stability: cluster two bootstrap resamples; are the assignments similar (ARI)? → [08.10](../weeks/08.10-clustering.md)

**22.** ⭐ **Variance is defined AROUND THE MEAN.** Without centering, the quantity you're maximizing is $\mathbb{E}[x^2]$ (the second moment about the *origin*), which is **dominated by the mean's magnitude.**

**So PC1 becomes a direction that points AT the mean — carrying no information about how the data VARIES.** You've burned your most important component on a constant.

**And nothing tells you.** The code runs, you get components, the plot looks plausible. **It's just wrong.** → [08.11](../weeks/08.11-dimensionality-reduction.md)

**23.** ⭐⭐
1. **🚨 Cluster SIZES are meaningless.** t-SNE expands dense clusters and contracts sparse ones. **A big blob is not a big cluster.**
2. **🚨 DISTANCES BETWEEN clusters are meaningless.** It preserves only *local* structure. Two clusters far apart on the plot are **not** necessarily far apart in reality.
3. **🚨 It manufactures clusters in PURE NOISE.** Run it on Gaussian noise at low perplexity and you will see beautiful, convincing clusters.

**t-SNE is for LOOKING at data, not MEASURING it.** Never cluster on it. Never feed it to a model. **And it cannot `transform()` new points** — which is why UMAP has largely superseded it. → [08.11](../weeks/08.11-dimensionality-reduction.md)

---

## Part 4 — Evaluation & Leakage

**24.** ⭐ With a **1% positive rate**, a model that predicts **"never positive" for everything** achieves:

```
accuracy = 9900/10000 = 99.0%  🎉
recall   = 0/100      =  0.0%  💀
```

**99% accuracy, and it caught nothing.** This is the [base-rate fallacy](../../06-Mathematics/weeks/06.5-probability.md) arriving in your production code. **When someone says "my model is 99% accurate," the only correct response is: "what's the class balance?"** → [08.12](../weeks/08.12-evaluation.md)

**25.** ⭐⭐ **Look at FPR's denominator: $FP + TN$.**

With 9,900 negatives and 100 positives, **TN is ENORMOUS.** So even if you produce **900 false positives**, FPR = 900/9900 = **0.09** — which *looks tiny*. **The ROC curve barely moves, and ROC-AUC reports 0.95.**

**But your precision is 100/(100+900) = 10%.** Nine out of ten of your alerts are false alarms. **The model is nearly useless.**

**⭐ PR-AUC contains NO TN at all** (precision = TP/(TP+FP), recall = TP/(TP+FN)). **It is blind to the huge, easy negative class — and therefore honest about the small, hard positive class you actually care about.**

**Rule: positive class < ~10% → report PR-AUC, and state its baseline (= the positive rate).** → [08.12](../weeks/08.12-evaluation.md)

**26.** ⭐⭐ **Because it's FREE, and it routinely beats every model improvement combined.**

Hyperparameter tuning buys **+1–3%** after six hours of compute. **Moving the threshold from 0.5 to the cost-optimal value can HALVE your business cost with no change to the model at all.**

```
COST_FP = $5     (an unnecessary retention call)
COST_FN = $2000  (a lost customer)

cost at t=0.50 : $128,000
cost at t=0.11 : $ 47,300     ← optimal
saving         : $ 80,700     ← from ONE LINE
```

**A false negative costs 400× a false positive**, so you should predict "churn" far more eagerly than 0.5 suggests.

**⭐ Tune it on the VALIDATION set — it's a hyperparameter like any other. Never on test.** **And almost nobody does this at all.** → [08.12](../weeks/08.12-evaluation.md)

**27.** ⭐⭐ **`cross_val_score` refits the entire pipeline INSIDE every fold** — so the scaler's μ/σ, the imputer's medians, the PCA's components, and the vectorizer's vocabulary are learned **only from that fold's training portion.**

**If you scale (or impute, or PCA, or vectorize) BEFORE cross-validating, every fold's validation data contributed to those parameters — and your CV score is a lie.**

**This is the most common leak in all of applied ML, and it is invisible.** **It is also why sklearn's `Pipeline` exists** — not as a convenience for tidy code, but as a **structural leakage guard.** **Everything with a `fit` method must be inside it.** → [08.13](../weeks/08.13-cross-validation.md)

**28.** ⭐ **You get ~90% cross-validated accuracy on PURE RANDOM NOISE.**

Take 200 samples × 10,000 random features with **random labels**. Select the 20 features that correlate best with `y` **using all the data**. Then cross-validate.

**The selection step already found the features that happened to fit the labels — including in the validation folds.** The CV is now measuring how well the model fits data the *selector* already peeked at.

*(This is the famous "wrong way to do cross-validation" from ESL Ch. 7.10.2. Run it once; you'll never forget it.)* → [08.13](../weeks/08.13-cross-validation.md)

**29.** ⭐⭐ **`GroupKFold`: whenever rows SHARE A SOURCE** — 30 X-rays from the same **patient**, 40 reviews of the same **product**, 100 photos from the same **camera**. A random split puts some in train and some in test, so **the model learns the patient's anatomy / the product's identity / the camera's sensor noise** — and reports fantastic accuracy that **evaporates on a new source.** *(This is the #1 cause of medical-imaging ML results that don't replicate.)*

**The time-series gap:** you're forecasting **7 days ahead**. If training ends March 7th and testing starts March 8th, a test row's `rolling_7d_mean` feature uses **March 1–7 — which is in your training set.** The model has effectively seen the recent past of its test period. **Insert a gap equal to your forecast horizon.**

```python
assert train.index.max() + pd.Timedelta(days=HORIZON) < test.index.min()
```
**One assertion. Catches the most common forecasting bug there is.** → [08.13](../weeks/08.13-cross-validation.md)

**30.** ⭐ **Target leakage in the features themselves** — `cancellation_reason`, `price_per_sqft` (which contains price), an un-shifted `rolling(7).mean()`.

**No CV strategy on Earth catches this.** The feature is **legitimately in the data**; it just **wouldn't exist at prediction time.**

**Only the availability question catches it:** *"At prediction time, would this value actually be available — with this value?"*

*(And in practice: SHAP. A feature carrying 80% of the model's importance is a bug report, not a discovery.)* → [08.13](../weeks/08.13-cross-validation.md), [08.16](../weeks/08.16-interpretability.md)

---

## Part 5 — Tuning, Interpretability, Production

**31.** ⭐⭐ **Because most hyperparameters don't matter.** In a typical problem, **1 or 2 drive nearly all the performance** and the rest are nearly irrelevant.

**Consider a 3×3 grid (9 points) over 2 parameters.** It tests only **3 distinct values** of the parameter that actually matters — the other 6 evaluations **re-test the same 3 values** with different settings of an irrelevant parameter. **You spent 9 fits to learn about 3 points.**

**Random search with 9 samples tests 9 DISTINCT values of the important parameter. Three times the resolution, identical compute.**

**And it gets exponentially better with more dimensions.** *(Bergstra & Bengio, 2012.)* → [08.15](../weeks/08.15-hyperparameter-tuning.md)

**32.** ⭐ **Two biases:**
1. **Biased toward HIGH-CARDINALITY features.** A continuous or high-cardinality feature has **far more candidate split points**, so **more chances to reduce impurity by luck.** **Add a random ID column and MDI will often rank it in your top 5.** It has zero signal.
2. **Correlated features SPLIT the credit.** Two nearly-identical features each get ~half, so **both look unimportant** — even though the pair is essential.

*(Plus: MDI is computed on **training** data, so it reflects what the model memorized.)*

**Use permutation importance, computed on VALIDATION.** → [08.16](../weeks/08.16-interpretability.md)

**33.** ⭐⭐ **SHAP is trustworthy because it has a THEOREM.**

Shapley values come from **cooperative game theory**: treat the features as **players** cooperating to produce the prediction, and **average each player's marginal contribution over all possible orderings.**

**The Shapley value is the UNIQUE attribution satisfying four axioms:** **efficiency** (contributions sum *exactly* to the prediction — no unexplained residual), **symmetry**, **dummy**, and **additivity**.

**It is not a heuristic. It is provably the only fair attribution.** No other method in the lesson has that.

**⭐ Its most valuable practical use: FINDING YOUR OWN LEAKS.** Every leak in this module shows up as a feature with **absurd importance** — `cancellation_reason` dominating a churn model, `price_per_sqft` dominating a price model. **A SHAP plot is the fastest leak detector you own.** → [08.16](../weeks/08.16-interpretability.md)

**34.** ⭐⭐ **Because performance monitoring requires LABELS, and labels arrive late.**

| Domain | Label delay |
|---|---|
| Churn | **90 days** |
| Loan default | **2 years** |
| Fraud chargeback | **60 days** |

**By the time your accuracy metric drops, you have been making bad decisions for a quarter.**

**Input drift is observable IMMEDIATELY.** PSI on the input features, and — **the cheapest, best canary — the distribution of the model's own predictions** (which needs **no labels at all**). **If your fraud model's mean predicted probability jumps from 0.02 to 0.11 overnight, you know TODAY.**

**Input drift is a LEADING indicator; performance decay is a LAGGING one. Alert on the leading indicator.** → [08.17](../weeks/08.17-production-ml.md)

**35.** ⭐⭐ **Two mechanisms:**

1. **⭐ Feedback loops.** Your model recommends items → users click those items → you train on that click data → **the model recommends them even harder.** **You've built a system that confirms its own beliefs**, and the diversity of your catalogue collapses.
2. **⭐ Bad data.** If an upstream pipeline breaks and you retrain automatically, **you have just deployed a model trained on corrupted data — automatically.**

**The fix: every automated retrain MUST pass a GATE that can REFUSE.**
```python
if new_model.cv_score < current.cv_score - TOLERANCE:  reject("worse")
if data_quality_checks_failed():                       reject("bad training data")
if prediction_distribution_shift() > THRESHOLD:        require_human_approval()
```
**Automated retraining without a gate is automated self-destruction.** → [08.17](../weeks/08.17-production-ml.md)

---

## 🏁 Bonus

**B1 — 0.94 offline, 0.71 in production. Five hypotheses, ranked:**

1. **⭐ LEAKAGE** (most likely). A target-derived feature, an un-shifted rolling window, naive target encoding, preprocessing outside the CV loop, or a random split on temporal/grouped data. **The offline number was fiction.**
   *Distinguish:* run the leakage hunt (ρ > 0.9 with target; single-feature AUC > 0.95); **run SHAP — the leak will dominate**; check whether a date or group column exists.
2. **Training/serving skew.** Features computed differently in production. *Distinguish:* **the skew test** (batch-transform must equal single-row transform — **a scaler refit on one row outputs all zeros**); compare feature distributions in training vs. production logs.
3. **Wrong CV strategy.** Random split on **grouped** data (the model learned the patient/product) or **temporal** data (it trained on the future). *Distinguish:* re-run with `GroupKFold` / `TimeSeriesSplit` and see whether the offline number collapses to ~0.71.
4. **Drift.** The world changed since training. *Distinguish:* **PSI per feature** and the prediction distribution.
5. **Data quality.** A stale or partially-loaded table upstream. *Distinguish:* **check freshness and volume first** — it's the cheapest check and a surprisingly common answer.

**B2 — One week:**

| Day | Do |
|---|---|
| **1** | ⭐ **ERROR ANALYSIS.** Look at 100 wrong predictions **by hand.** Categorize. Count. *(~15% will be mislabeled — the model was right.)* |
| **2–4** | ⭐ **FEATURES.** Fix the biggest error bucket. **+10–40%** |
| **5** | Better model (LR → LightGBM). **+3–8%** |
| **6** | ⭐ **Tune the THRESHOLD** on business cost *(free, often the biggest win)*. Then briefly tune hyperparameters. **+1–3%** |
| **7** | Honest evaluation: PR-AUC ± CI, sliced by segment. **Test set — once.** |

**⭐ NOT hyperparameter tuning on day 1.** That's where everyone starts, and it's the lowest-return activity in the workflow.

**B3 — The same regularization shape (`loss + λ·complexity`), four times:**
1. **Ridge:** $\|Xw-y\|^2 + \lambda\|w\|^2$ ([08.3](../weeks/08.3-linear-regression.md))
2. **Tree cost-complexity pruning:** $R(T) + \alpha\,|\text{leaves}|$ ([08.5](../weeks/08.5-decision-trees.md))
3. **SVM:** hinge loss $+ \lambda\|w\|^2$ — **maximizing the margin IS regularization** ([08.7](../weeks/08.7-svm.md))
4. **Laplace smoothing:** a Bayesian prior on the counts ([08.8](../weeks/08.8-naive-bayes.md))

**⭐ You did not learn ten algorithms. You learned about four ideas, wearing ten costumes.**

**B4 — The ten sentences:**
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

> [!TIP]
> **⭐ Turn every missed question into a flashcard. And for anything you fumbled: don't reread — BUILD IT.** Implement the algorithm and `np.allclose` it against sklearn. Construct the leak and watch your test catch it. **Machine learning is the one field where you can build the disaster and prove your defences hold** — and that beats any answer key.

---

[❓ Questions](quiz-01.md) · [🧠 Flashcards](../flashcards/deck.md) · [📄 Cheat sheet](../cheat-sheets/ml-cheatsheet.md) · [🏠 Module 08](../README.md)
