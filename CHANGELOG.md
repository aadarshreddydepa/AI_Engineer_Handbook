# Changelog

All notable changes to this handbook are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/), and this project aims to follow it loosely. Dates are in `YYYY-MM-DD`.

---

## [Unreleased]

### Planned
- Module 10 · NLP — lesson content
- Weekly lessons authored module by module

---

## [0.14.0] — 2026-07-15

### Added
- **Module 09 · Deep Learning Systems with PyTorch — complete.** (Authored in `docs/09-Deep-Learning/`. **Deep learning is taught from first principles before any reliance on PyTorch abstractions** — per the module brief. Lessons 09.1–09.5 use **only Python and NumPy** — no `import torch`; the reader hand-writes a neuron, a layer, a forward pass, backpropagation, and Adam, gradient-checked against finite differences. Torch is introduced only at 09.6, and 09.7 proves with `torch.allclose` that `loss.backward()` computes the *identical* gradients derived by hand in 09.4.)
  - 18 lessons (`docs/09-Deep-Learning/weeks/09.1`–`09.18`): why deep learning (**representation learning as the one thing that changed**; the feature hierarchy; universal approximation and its catches; **where DL loses — tabular data**; why 2012), neural network fundamentals (**the neuron as a dot product**; **a layer as matmul + bias + nonlinearity**; **the one-line proof that stacked Linear layers collapse without a nonlinearity**; ReLU vs sigmoid and the dying-ReLU problem; choosing the output layer), the math of neural networks (affine transformations; **why `CrossEntropyLoss` takes logits, not probabilities**; `BCEWithLogitsLoss`; **the `ln(C)` initial-loss sanity check**; reading shape errors), **backpropagation from scratch** (**the chain rule, cached, run right-to-left**; reverse-mode and why it's the cheap direction; **the four backward rules**; shape-matching to derive transposes; **gradient checking in float64**; why PyTorch accumulates gradients; the activation-cache memory story), optimization (backprop-vs-optimizer; momentum; RMSProp; **Adam in twelve lines**; **AdamW and decoupled weight decay**; **Adam's 3× parameter memory and its link to LoRA**; the learning rate as the #1 hyperparameter; warmup + cosine), PyTorch tensors (**tensor = NumPy array + device + autograd tape**; the "tensors on different devices" error; the `from_numpy` shared-memory gotcha; **bfloat16 vs float16**; **why timing GPU code needs `cuda.synchronize()`**), autograd (**the dynamic graph and why it made PyTorch win**; `loss.backward()`; **`model.eval()` ≠ `torch.no_grad()`**; the `.item()` memory leak; the zero_grad→backward→step ritual), building models (`nn.Module` as `__init__`-parts + `forward`-wiring; auto-registered parameters; **`nn.ModuleList` vs the invisible-plain-list bug**; `nn.Sequential`'s limits), data loading (`Dataset`/`DataLoader`; **shuffle train not val**; **`num_workers` and the idle-GPU mistake**; augment train only), **the training loop** (**the three-line heartbeat**; **the `train()`/`eval()`/`no_grad()` dance and the bugs from getting it wrong**; **overfit-one-batch**; best-by-validation checkpointing), CNNs (**why FC fails on images — no translation invariance**; **weight sharing**; convolution as a patch dot product; **transfer learning**; ResNet's residual connection), sequence models (**why RNNs forget — the vanishing gradient across time**; LSTM/GRU and the protected cell state; **why Transformers won — parallelism + long range**; `pack_padded_sequence`), regularization & normalization (the overfit diagnostic unchanged from 08.2; **dropout**; **batch norm's train-vs-eval behaviour**; **LayerNorm for Transformers**; **data/augmentation as the strongest regularizer**), performance (**mixed precision by default**; gradient clipping; gradient accumulation; gradient checkpointing; **diagnosing data- vs compute-bound with `nvidia-smi`**), model debugging (**overfit-one-batch as the #1 test**; change one thing at a time; **NaN diagnosis by timing**; vanishing/exploding gradients; dead neurons), saving & loading (**`state_dict` not the whole model**; **the optimizer state is what lets you resume without a loss spike**; **`torch.load` as an RCE risk — `weights_only=True`/safetensors**; GPU reproducibility), production (**inference is lighter — no gradients/optimizer/activation cache**; **latency vs throughput and dynamic batching**; TorchScript/ONNX; **MLOps unchanged from Module 08**), and a projects + module-summary consolidation lesson.
  - Companion artifacts: consolidated [exercises](docs/09-Deep-Learning/exercises/README.md) (three tiers — **first-principles NumPy** with gradient checks, **introducing PyTorch** culminating in the `torch.allclose` autograd-equality proof, and **architectures & scale** — plus an end-to-end capstone with a `pytest` suite), a 40-question [quiz](docs/09-Deep-Learning/quizzes/quiz-01.md) with model [answers](docs/09-Deep-Learning/quizzes/answers-01.md), an ~85-card [flashcard deck](docs/09-Deep-Learning/flashcards/deck.md), and a [master cheat sheet](docs/09-Deep-Learning/cheat-sheets/dl-cheatsheet.md).
  - Seven mini-projects: a **neural network from scratch in NumPy** (the flagship of the first half — backprop by hand, gradient-checked), a **PyTorch training framework** (the reusable `Trainer` every later project uses), an MNIST classifier (rebuilt in NumPy and confirmed to match), a **CIFAR-10 classifier** (CNN-from-scratch vs fine-tuned ResNet, with the transfer-learning gap *widening* on small data), a **sentiment LSTM** (with the stopwatch reading that shows a Transformer trains faster because it parallelizes), a **tabular regression model** (deliberately built to **lose to LightGBM** — teaching when *not* to use deep learning), and a **model server** (FastAPI, dynamic batching, ONNX parity, and the drift monitor from 08.17 unchanged) — each with requirements, folder structure, architecture diagram, evaluation strategy, testing plan, and future improvements.
  - Module [lesson index](docs/09-Deep-Learning/weeks/README.md) (with a "Torch yet?" column marking where `import torch` first appears); linked from the module README.
- Glossary: added a "Deep Learning Systems with PyTorch (Module 09)" section (~85 terms across foundations/neurons, math/loss/backprop, optimization, PyTorch/autograd/models, data/training loop, architectures, regularization/performance/debugging, and save-load/production).

### Notes
- **The module's spine is a promise kept: derive it by hand, then prove PyTorch agrees.** The same MNIST network is hand-built in NumPy (09.2–09.4), then rebuilt in PyTorch (09.6–09.8), and the capstone assertion `torch.allclose(numpy_grad, torch_param.grad)` proves `loss.backward()` *is* the hand-written `backward()` from 09.4. Autograd stops being magic at exactly that line.
- **The recurring thesis — deep learning added a new model, not a new discipline.** The training loop (`zero_grad → backward → step`) never changes across the CNN, the LSTM, and the regression model. The overfitting diagnostic, honest evaluation, and deployment discipline transfer **unchanged** from Module 08; the drift monitor in the model-server project is 08.17's, verbatim.
- Builds directly on Modules 06 and 08, made concrete: the chain rule (06.4) becomes a `backward()` method; cross-entropy (06.8) becomes the loss; Adam (06.7) becomes `torch.optim.AdamW`; the √d_k and residual-connection arguments (06.11, 06.3) reappear as LayerNorm and the gradient highway; the overfit/underfit diagnostic (08.2), evaluation (08.12), and production discipline (08.17) carry over intact.
- Cross-module through-lines are threaded explicitly: the **vanishing/exploding $\lambda^n$ problem** appears in 09.4 (depth), 09.12 (across time in RNNs), and 09.15 (diagnosed empirically); **residual connections** are traced from 09.4 through ResNet (09.11), the LSTM cell (09.12), and normalization (09.13); the **train/eval/no_grad dance** recurs in 09.7, 09.10, 09.13, and 09.17.
- A senior instinct the module deliberately instills: **deep learning did not win tabular data** — project 6 has the reader build a careful deep MLP and watch it lose to LightGBM, inoculating against reaching for the fancy tool on spreadsheet-shaped problems.
- Image placeholders are described in-place (the feature hierarchy, computational graphs, the loss landscape and optimizer trajectories, convolution/weight-sharing, the RNN-vs-Transformer parallelism picture, learned CNN filters, gradient-norm-by-layer diagnostics) — no images are generated.

---

## [0.13.0] — 2026-07-14

### Added
- **Module 08 · Machine Learning Foundations for AI Engineers — complete.** (Authored in `docs/08-Machine-Learning/`. **Every important algorithm is implemented from scratch in NumPy and verified against scikit-learn with `np.allclose` BEFORE the library is introduced** — per the module brief. The objective is to deeply understand ML, not merely use libraries.)
  - 18 lessons (`docs/08-Machine-Learning/weeks/08.1`–`08.18`): what machine learning is (AI vs ML vs DL; supervised/unsupervised/semi-/**self-supervised**/RL; problem framing and baselines), the ML workflow (the nine stages; the three-way split; bias–variance; learning curves; **error analysis**), **linear regression** (deriving the MSE gradient; normal equations vs gradient descent; **Ridge, Lasso, and why $+\lambda I$ makes $X^\top X$ always invertible**; residual diagnostics), **logistic regression** (the sigmoid; **why MSE is catastrophic — σ′ vanishes when confidently wrong**; log-loss and its `predicted − actual` gradient; the linear decision boundary; **threshold tuning on business cost**), **decision trees** (entropy, Gini, information gain; recursive CART from scratch; pruning; why they always overfit; **MDI bias**), **ensembles** (**the variance-of-the-average formula and why decorrelation is the whole game**; bagging; Random Forest with OOB scoring; **gradient boosting as gradient descent in function space**; XGBoost/LightGBM/CatBoost), **SVMs** (maximum margin; **support vectors and how the hinge loss produces sparsity**; soft margins; **the kernel trick**; RBF; why they don't scale past ~50k), **Naive Bayes** (Bayes' theorem; **why an obviously false independence assumption still works**; Laplace smoothing; **why log space is mandatory**), **KNN** (distance metrics; **the curse of dimensionality**; KD-trees; **ANN and the identity between KNN and RAG**), **clustering** (K-Means from scratch with k-means++; **the null test**; DBSCAN; hierarchical; GMM), **dimensionality reduction** (**PCA from scratch via SVD**; why centering is mandatory; **t-SNE's three traps**; UMAP), **model evaluation** (confusion matrix; precision/recall; **why accuracy lies and ROC-AUC is optimistic under imbalance**; PR-AUC; **cost-optimal threshold tuning**; calibration), **cross-validation and leakage** (stratified/grouped/time-series with a **gap**; nested CV; **the four leaks that survive a "correct" CV**), **feature engineering for ML** (the algorithm→preprocessing table; encoding; selection; **imbalanced data and skepticism of SMOTE**), **hyperparameter tuning** (**why random beats grid**; Bayesian optimization; successive halving; **overfitting the validation set**), **interpretability** (**MDI's biases**; permutation importance; **SHAP and its uniqueness theorem**; LIME; PDP/ALE; **fairness impossibility**), **production ML** (artifacts; serialization; versioning; serving; **monitoring inputs, not performance**; **retraining gates**; shadow mode), and a projects + module-summary consolidation lesson.
  - Companion artifacts: consolidated [exercises](docs/08-Machine-Learning/exercises/README.md) (mathematical, NumPy implementation, debugging, evaluation, algorithm comparison — plus **cross-lesson exercises** including *The From-Scratch Gauntlet* and *The Leakage Gauntlet*), a 35-question [quiz](docs/08-Machine-Learning/quizzes/quiz-01.md) with model [answers](docs/08-Machine-Learning/quizzes/answers-01.md), a ~90-card [flashcard deck](docs/08-Machine-Learning/flashcards/deck.md), and a [master cheat sheet](docs/08-Machine-Learning/cheat-sheets/ml-cheatsheet.md).
  - Seven mini-projects: Iris classifier from scratch, house price prediction, Titanic survival, spam detection, customer churn, credit risk (with a **fairness audit that fails the build**), and movie recommendation — each with requirements, folder structure, architecture diagram, evaluation strategy, testing plan, and future improvements.
  - Module [lesson index](docs/08-Machine-Learning/weeks/README.md); linked from the module README.
- Glossary: added a "Machine Learning Foundations (Module 08)" section (~70 terms across foundations, algorithms, and evaluation/leakage/production).

### Notes
- **The module's spine is the four-box template** (model · loss · gradient · update) established in 08.3 and reused by every algorithm after it — so the reader recognizes variations rather than learning from zero each time. The `predicted − actual` gradient recurs in linear regression, logistic regression, and softmax+cross-entropy; the `loss + λ·complexity` regularization shape recurs as Ridge, tree pruning, the SVM margin, and Laplace smoothing.
- **Every algorithm lesson carries a `test_vs_sklearn.py`** in its mini project. That `np.allclose` assertion is the module's central discipline: it converts scikit-learn from magic into a faster version of code the reader understands.
- Builds directly on Modules 06 and 07: gradients and optimizers from 06.4/06.7, cross-entropy from 06.8, SVD/eigenvalues from 06.3 (Ridge, PCA), the bootstrap from 06.6 (bagging, CIs), numerical stability from 06.9 (the stable sigmoid, log-space Naive Bayes), and the leakage/pipeline groundwork from 07.7/07.11/07.12.
- Recurring practical emphases that distinguish this from a textbook treatment: **error analysis beats hyperparameter tuning** (+10–40% vs +1–3%), **threshold tuning is free and beats every model improvement**, **`feature_importances_` will rank a random ID column in your top 5**, **CV cannot catch target leakage**, and **monitor inputs rather than performance because labels arrive months late**.
- Image placeholders are described in-place (bias–variance curves, L1-vs-L2 geometry, residual plots, sigmoid derivative, decision boundaries, SVM margins and kernels, hinge-vs-log-loss, clustering comparisons, grid-vs-random search, ROC-vs-PR, SHAP beeswarm) — no images are generated.

---

## [0.12.0] — 2026-07-14

### Added
- **Module 07 · Data Analysis, Scientific Computing & Visualization for AI Engineers — complete.** (Authored in `docs/07-Data-Analysis/`. Teaches the **complete data workflow**, not libraries in isolation — everything builds toward Machine Learning.)
  - 13 lessons (`docs/07-Data-Analysis/weeks/07.1`–`07.13`): the AI data lifecycle (11 stages as a **loop**; why data bugs are silent; leakage/skew/drift; the medallion pattern; model-centric vs data-centric AI), NumPy (ndarray internals, **strides**, memory layout, vectorization, broadcasting, ufuncs, **views vs copies**, structured arrays, performance), Pandas I (Series/DataFrame/Index internals, `.loc`/`.iloc`, **SettingWithCopyWarning**, dtypes and the **`category` 10× memory win**, I/O, MultiIndex), Pandas II (merge with **`validate=`** and row explosion, split-apply-combine, **`transform`**, pivot/melt, **window operations and the `.shift(1)` leakage guard**, time series, timezones), data cleaning (**MCAR/MAR/MNAR** and the MNAR target-rate test, **disguised missingness/sentinels**, duplicates, invalid values, **outliers as error-vs-rare-event-vs-target**, normalization vs standardization and **the fit-on-train-only rule**, categorical encoding and **out-of-fold target encoding**), EDA (a **7-step systematic procedure ending in the leakage hunt**, descriptive statistics, distributions, skew/kurtosis, correlation vs mutual information, class imbalance, **how EDA determines model selection**), feature engineering (**why features beat models: +10–40% vs +3–8%**, domain/aggregate/ratio/interaction features, **cyclical sin+cos encoding**, date/time, introductory text features/TF-IDF, **permutation importance**, and **the six leakage rules + the universal leakage test**), visualization (chart-selection flowchart, Matplotlib's OO API, the six plots that matter for ML, Plotly, **how charts lie**, accessibility), data quality (the **six dimensions**, schema contracts with pandera, **freshness + volume as the two highest-value checks**, quarantine-never-fix, **PSI drift detection**, lineage, alert fatigue), performance & scale (**the optimization ladder**, memory optimization, **columnar storage and why Parquet beats CSV 5–100×**, chunking and what doesn't decompose, **Pandas vs Polars vs DuckDB vs Dask vs Spark**, profiling), reusable pipelines (**why a notebook is not a pipeline**, pure composable steps, the **`fit`/`transform` contract as a structural leakage guard**, reproducibility's five pins, **dataset versioning**, killing training/serving skew, orchestration), real AI case studies (**churn, house prices, sentiment, image metadata, time-series forecasting** — each with every preprocessing decision justified and its signature leakage trap identified), and a projects + module-summary consolidation lesson.
  - Companion artifacts: consolidated [exercises](docs/07-Data-Analysis/exercises/README.md) (conceptual, NumPy, Pandas, cleaning, visualization, dataset analysis, plus **cross-lesson exercises** including "The Silent Bug Hunt" and "The Leakage Gauntlet"), a 30-question [quiz](docs/07-Data-Analysis/quizzes/quiz-01.md) with model [answers](docs/07-Data-Analysis/quizzes/answers-01.md), an ~85-card [flashcard deck](docs/07-Data-Analysis/flashcards/deck.md), and a [master cheat sheet](docs/07-Data-Analysis/cheat-sheets/data-cheatsheet.md).
  - Seven mini-projects: CSV profiler, data cleaning toolkit, automated EDA report, feature engineering library, sales dashboard, automated data quality system, and the flagship **production pipeline** — with **five CI tests** (no-leakage, no-skew, idempotent, reproducible, purity) that block merges. Plus bonus projects: array profiler, customer analytics engine, big-data processor, and a case-study portfolio.
  - Module [lesson index](docs/07-Data-Analysis/weeks/README.md); linked from the module README.
- Glossary: added a "Data Analysis, Scientific Computing & Visualization (Module 07)" section (~75 terms across the lifecycle, NumPy, Pandas, cleaning/EDA, features/visualization, and quality/scale/pipelines).

### Notes
- **Every lesson carries a "Security & privacy considerations" section** per the module brief — and it does real work rather than being a checkbox: aggregation-is-not-anonymization (a group of size 1 *is* that person), the Netflix de-anonymization join, `df.head()` in a committed notebook as a permanent breach, outlier removal as a fairness problem, EXIF GPS as a home address, Plotly HTML embedding the underlying dataset, logs as the least-protected data store, and pseudonymization-at-ingestion as the only design that survives a GDPR deletion request.
- **The spine of the module is one idea: the thing that will destroy your model does not raise an exception.** Leakage is introduced in 07.1, *born* in 07.4's windows, *hunted* in 07.6, *guarded against* in 07.7, made **structurally impossible** in 07.11, and shown to have five different faces in 07.12. The `-1` sentinel that makes `df['age'].mean()` a lie recurs from 07.1 through 07.5 and is finally *made visible* by a histogram in 07.8.
- Builds directly on Module 06: broadcasting/`keepdims` from 06.9, the 1/√n rule from 06.6 (why 100k rows is enough for EDA), cyclical sin/cos as the same geometry as Transformer positional encoding (06.11), and PSI as a KL divergence (06.8) turned into a production alert.
- Image placeholders are described in-place (ndarray strides, cyclical encoding on a circle) — no images are generated.

---

## [0.11.0] — 2026-07-14

### Added
- **Module 06 · Mathematics for AI Engineers — complete.** (Authored in `docs/06-Mathematics/`. Taught from the perspective of *building AI systems*, not as a university course: every concept must answer why it exists, why an AI Engineer should care, where it's used, how it's implemented, and how it relates to ML, deep learning, and Transformers.)
  - 13 lessons (`docs/06-Mathematics/weeks/06.1`–`06.13`): mathematical thinking (a 7-step equation-decoding procedure; the four ideas that carry most of AI), linear algebra I (scalars/vectors/matrices/tensors, the dot product as **alignment**, cosine similarity, matmul as **function composition**, the cross product and why AI ignores it), linear algebra II (transpose, inverse, rank, determinant, eigenvalues, **SVD**, PCA, and **LoRA as a rank argument**), calculus (limits, derivatives, partials, gradients, the **chain rule = backpropagation**, Jacobian, Hessian, a 50-line micro-autograd), probability (random variables, distributions, conditional probability, **Bayes and the base-rate fallacy**, independence, the chain rule of probability as the definition of an autoregressive LLM, temperature/top-k/top-p), statistics (mean vs median vs percentiles, variance, correlation, **bootstrap confidence intervals**, hypothesis testing, p-hacking), optimization (loss functions, convexity, batch/SGD/mini-batch, momentum, AdaGrad/RMSProp, **Adam and AdamW**, LR schedules and warmup), information theory (information as surprise, entropy, the **derivation of cross-entropy**, KL divergence, mutual information, perplexity), numerical computing (floats, **bfloat16 vs float16**, overflow/underflow, the three stability tricks, vectorization, broadcasting, systematic NaN debugging), the mathematics of neural networks (forward pass, activations, a full **backpropagation derivation**, weight updates, a complete NumPy network with gradient checking), the mathematics of Transformers (embeddings, attention decoded symbol by symbol, **the √d_k variance argument**, multi-head attention, causal masking, sinusoidal PE and **RoPE**, the O(n²) bottleneck), reading mathematical notation (sigma/product notation, typography as a type system, the ML symbol table, the three-pass paper-reading method, a live decoding of the LoRA paper), and a projects + module-summary consolidation lesson.
  - Companion artifacts: consolidated [exercises](docs/06-Mathematics/exercises/README.md) (conceptual, intuition, NumPy, visualization, equation-interpretation, plus **cross-lesson exercises** that force topics to fuse), a 30-question [quiz](docs/06-Mathematics/quizzes/quiz-01.md) with model [answers](docs/06-Mathematics/quizzes/answers-01.md), a ~90-card [flashcard deck](docs/06-Mathematics/flashcards/deck.md), and a [master cheat sheet](docs/06-Mathematics/cheat-sheets/math-cheatsheet.md).
  - Five mini-projects: matrix calculator & transformation visualizer, linear regression from scratch, gradient descent visualizer (optimizer zoo), PCA & compression lab, and the flagship **neural network mathematics simulator** — culminating in a from-scratch multi-head causal attention and a generating tiny Transformer, with **no frameworks at any step**.
  - Module [lesson index](docs/06-Mathematics/weeks/README.md); linked from the module README.
- Glossary: added a "Mathematics for AI Engineers (Module 06)" section (~90 terms across linear algebra, calculus/optimization, probability/statistics/information theory, numerical computing, and neural networks/Transformers).

### Notes
- **Intuition first, implementation second, formal mathematics third** — per the module brief. Proofs are omitted unless they carry intuition; every concept has a geometric picture, a NumPy implementation, and a named place where it appears in production AI.
- Concepts deliberately recur across lessons so they fuse: the ravine `x² + 10y²` appears in 06.4 (gradient descent zig-zags), 06.3 (its Hessian's condition number *predicts* that zig-zag), and 06.7 (momentum fixes it); the `√d_k` in attention is shown to be a *variance* fix (06.5) protecting a *gradient* (06.4) from a *numerical* saturation (06.9); residual connections are traced from a derivative through eigenvalue compounding to the Transformer block.
- Image placeholders are described in-place (vector geometry, matrix transformations, rank collapse, SVD geometry, the loss landscape, distributions, entropy, broadcasting, activations and their derivatives, attention heatmaps, positional encoding) — no images are generated.

---

## [0.10.0] — 2026-07-09

### Added
- **Module 05 · Databases & Data Engineering for AI Engineers — complete.** (Authored in `docs/05-SQL/`; scope expanded well beyond SQL syntax to full data engineering, per the module brief.)
  - 16 lessons (`docs/05-SQL/weeks/05.1`–`05.16`): introduction to databases (files vs DBs, the five guarantees), relational databases (keys, relationships, normalization/denormalization), SQL fundamentals (JOINs, aggregation, NULL logic, injection), advanced SQL (CTEs, window functions, views, triggers), query optimization (`EXPLAIN ANALYZE`, B-trees, composite/covering indexes, N+1), transactions (ACID, isolation levels, the lost update, deadlocks, MVCC), NoSQL (document/key-value/wide-column/graph, CAP), data modeling (ER diagrams, star/snowflake, facts/dimensions, SCD Type 2), warehouses & lakes (columnar storage, lakehouse, platform comparison), ETL & ELT (ingestion, validation, idempotency, Airflow), data pipelines (medallion layers, monitoring, lineage, data quality), AI data workflows (leakage, training/serving skew, drift, reproducibility), database security (RLS, encryption, PITR, LLM-generated SQL), performance & scaling (the scaling ladder), a vector-database preview (embeddings, ANN/HNSW, pgvector), and a projects+summary consolidation lesson.
  - Companion artifacts: consolidated [exercises](docs/05-SQL/exercises/README.md) (SQL/design/optimization/modeling/debugging, difficulty-ramped), a 30-question [quiz](docs/05-SQL/quizzes/quiz-01.md) with model [answers](docs/05-SQL/quizzes/answers-01.md), a full [flashcard deck](docs/05-SQL/flashcards/deck.md), and a [master cheat sheet](docs/05-SQL/cheat-sheets/databases-cheatsheet.md).
  - Six mini-projects: inventory database, employee management system, analytics dashboard backend, ETL/ELT pipeline, data warehouse design, and the flagship **AI dataset pipeline** (idempotent content-hash embedding → pgvector with tenant-aware retrieval).
  - Module [lesson index](docs/05-SQL/weeks/README.md); linked from the module README.
- Glossary: added a "Databases & Data Engineering (Module 05)" section (~40 terms: normalization, window function, execution plan, ACID, MVCC, CAP, star schema, SCD Type 2, lakehouse, ETL/ELT, idempotency, lineage, data leakage, drift, RLS, PITR, sharding, embedding, ANN/HNSW, pgvector, and more).

### Notes
- PostgreSQL-first throughout; taught from first principles at production depth with a continuous AI thread (credit-deduction races, label-distribution queries, idempotent/paid embedding pipelines, point-in-time correctness, LLM-generated SQL as untrusted input, permission-aware RAG retrieval). Ends by previewing vector databases as the bridge to Module 13 · RAG.
- **Milestone:** completes the engineering-foundations phase (Modules 00–05). The handbook now pivots to the ML journey from Module 06.

---

## [0.9.0] — 2026-07-09

### Added
- **Module 04 · Advanced Git & Collaboration for AI Engineers — complete.**
  - 13 lessons (`docs/04-Git/weeks/04.1`–`04.13`): Git internals (objects, refs, reflog), commit history (the DAG, merges, detached HEAD), branching strategies (GitHub Flow/Git Flow/trunk-based), advanced branch management (rebase, interactive rebase, cherry-pick, reset, revert, reflog recovery), merge conflict resolution, tags & releases (SemVer, GitHub Releases), GitHub collaboration (PRs, reviews, protected branches, merge strategies), repository management (README/CONTRIBUTING/CODEOWNERS/templates), large files (Git LFS, `.gitignore`), automation (Git hooks, pre-commit), GitHub Actions (CI/CD), debugging Git (recovery walkthroughs), and a complete AI-project-workflow + projects + summary lesson.
  - Companion artifacts: consolidated [exercises](docs/04-Git/exercises/README.md) (branching, conflict labs, rebase, recovery drills, collaboration, CI — difficulty-ramped), a 26-question [quiz](docs/04-Git/quizzes/quiz-01.md) with model [answers](docs/04-Git/quizzes/answers-01.md), a full [flashcard deck](docs/04-Git/flashcards/deck.md), and a [master cheat sheet](docs/04-Git/cheat-sheets/git-cheatsheet.md).
  - Five mini-projects (professional OSS repo, CI pipeline, release automation, AI project with Git LFS, branching-strategy design) plus a Git recovery playbook, and an end-to-end "feature branch → PR → review → merge → tag → release" workflow.
  - Module [lesson index](docs/04-Git/weeks/README.md); linked from the module README.
- Glossary: added an "Advanced Git & Collaboration (Module 04)" section (objects/refs/reflog, rebase, reset/revert, merge conflict, protected branch, CODEOWNERS, Git LFS, pre-commit, GitHub Actions, `git bisect`, and more).

### Notes
- Assumes Git fundamentals (no `init`/`add`/`commit` reteaching); focuses on internals, recovery, collaboration, releases, automation, and AI-project specifics (notebooks, LFS, model/data versioning, secret handling). Heavily cross-referenced to Modules 00–03; the object model builds on Module 02 data structures, and CI runs on Module 03 Linux runners.

---

## [0.8.0] — 2026-07-09

### Added
- **Module 03 · Linux for AI Engineers — complete.**
  - 17 lessons (`docs/03-Linux/weeks/03.1`–`03.17`): introduction (kernel vs OS vs distro, why AI/cloud/Docker/K8s use Linux), architecture (kernel/user space/syscalls/scheduler), filesystem (hierarchy, inodes, symlinks, `/proc`, `/dev`), terminal mastery (pipes, redirection, PATH, env vars, globs), essential commands (grep/find/awk/sed/xargs/…), permissions (chmod/chown, SUID/SGID/sticky, least privilege), processes (states, tmux, nvidia-smi, signals), systemd services, networking (SSH keys, rsync, diagnostics), storage (df/du, ext4/xfs, fstab), logs (journalctl, dmesg, rotation), bash scripting (`set -euo pipefail`, functions, traps, exit codes), package & environment management (apt vs uv/conda), performance monitoring (free/vmstat/iostat/sar, bottleneck analysis), security (SSH hardening, UFW, Fail2Ban, secrets), Docker preparation (namespaces/cgroups/OverlayFS), and a workflow + projects + summary lesson.
  - Companion artifacts: consolidated [exercises](docs/03-Linux/exercises/README.md) (terminal/debug/log/permission/bash, difficulty-ramped), a 28-question [quiz](docs/03-Linux/quizzes/quiz-01.md) with model [answers](docs/03-Linux/quizzes/answers-01.md), a full [flashcard deck](docs/03-Linux/flashcards/deck.md), and a [master cheat sheet](docs/03-Linux/cheat-sheets/linux-cheatsheet.md).
  - Six mini-projects threaded through their host lessons: log analyzer, file backup utility, dataset organizer, monitoring dashboard, deployment automation, and server health & security checker — plus a "day in the life of an AI Engineer" end-to-end workflow.
  - Module [lesson index](docs/03-Linux/weeks/README.md); linked from the module README.
- Glossary: added a "Linux for AI Engineers (Module 03)" section (kernel, distro, shell, syscall, systemd, `journalctl`, SSH keys, `rsync`, `tmux`, `nvidia-smi`, load average, swap, UFW, Fail2Ban, namespaces, cgroups, containers, and more).

### Notes
- Teaches Linux **as an operating system** (not a command list), with every topic tied to real AI-Engineer usage (SSH into GPU servers, tmux training jobs, nvidia-smi, systemd model services, rsync datasets, hardening) and cross-referenced to Modules 00–02. The Docker-preparation lesson reveals containers as namespaces + cgroups + union filesystems, priming Module 16.

---

## [0.7.0] — 2026-07-08

### Added
- **Module 02 · Computer Science Foundations for AI Engineers — complete.**
  - 13 lessons (`docs/02-Computer-Science/weeks/02.1`–`02.13`): how computers work (CPU/cache/instruction cycle/compilers), memory (stack/heap/fragmentation/GC/cache locality), data structures (arrays→graphs), algorithms (search/sort/DP/greedy/graph/backtracking), time & space complexity (Big-O/Ω/Θ), operating systems (processes/threads/scheduling/virtual memory), networking (TCP/IP, HTTP(S), REST/WebSocket/gRPC, load balancers), concurrency (threading/multiprocessing/async, the GIL, races/locks), serialization (JSON/YAML/Pickle/MessagePack/Protobuf + security), file systems (permissions/symlinks/compression/durable writes), system-design basics (scaling/availability/fault tolerance/caching), debugging (stack traces/profiling/observability), and a projects+summary consolidation lesson.
  - Companion artifacts: consolidated [exercises](docs/02-Computer-Science/exercises/README.md) (conceptual/coding/debug/architecture, difficulty-ramped), a 26-question [quiz](docs/02-Computer-Science/quizzes/quiz-01.md) with model [answers](docs/02-Computer-Science/quizzes/answers-01.md), a full [flashcard deck](docs/02-Computer-Science/flashcards/deck.md), and a [master cheat sheet](docs/02-Computer-Science/cheat-sheets/cs-foundations-cheatsheet.md).
  - Seven mini-projects threaded through their host lessons: trie autocomplete, graph traversal visualizer, thread-safe queue, LRU cache, in-memory cache, URL shortener (core), and a simple HTTP server.
  - Module [lesson index](docs/02-Computer-Science/weeks/README.md); linked from the module README.
- Glossary: added a "Computer Science Foundations (Module 02)" section (memory hierarchy, cache locality, Big-O, process/thread, deadlock, virtual memory, TCP/HTTP, load balancer, serialization, statelessness, observability, and more).

### Notes
- Taught from first principles (no prior CS assumed) but at professional depth, with every concept tied to AI-system relevance (GPUs, tensors, model serving, distributed training) and cross-referenced to Modules 00–01.

---

## [0.6.0] — 2026-07-08

### Added
- **Module 01 · Advanced Python for AI Engineering — complete.**
  - 15 lessons (`docs/01-Advanced-Python/weeks/01.1`–`01.15`): Python architecture/bytecode/import system, memory & the data model, OOP, functional programming, iterators & generators, decorators, context managers, type hinting (+ Pydantic), error handling & logging, testing, performance & the GIL, async programming, packaging & code quality, reading open-source code, and a projects+summary consolidation lesson.
  - Companion artifacts: consolidated [exercises](docs/01-Advanced-Python/exercises/README.md) (coding/debug/refactor/design, difficulty-ramped), a 25-question [quiz](docs/01-Advanced-Python/quizzes/quiz-01.md) with model [answers](docs/01-Advanced-Python/quizzes/answers-01.md), a full [flashcard deck](docs/01-Advanced-Python/flashcards/deck.md), and a [master cheat sheet](docs/01-Advanced-Python/cheat-sheets/advanced-python-cheatsheet.md).
  - Six progressively harder mini-projects (file indexer → log analyzer → async API client → CLI → config manager → plugin system), with the async API client as the flagship.
  - Module [lesson index](docs/01-Advanced-Python/weeks/README.md); linked from the module README.
- Glossary: added an "Advanced Python (Module 01)" section (CPython, bytecode, PVM, GIL, closures, decorators, generators, context managers, Protocol, Pydantic, coroutine/event loop, vectorization, lockfile, and more).

### Notes
- Lessons assume Python fundamentals (no beginner reteaching) and target production AI-engineering depth; §9 (Error Handling) and §10 (Logging) from the module spec are combined into lesson 01.9.

---

## [0.5.0] — 2026-07-08

### Added
- **Module 00 · Orientation & Foundations — complete.** First authored module of the handbook.
  - 12 lessons (`docs/00-Orientation/weeks/00.1`–`00.12`): vocabulary of the field, the AI Engineering landscape, careers & roles, learning strategy, development environment, GitHub workflow, reading documentation, reading research papers, the daily learning workflow, the AI Engineer mindset, recommended resources, and a consolidation/summary lesson.
  - Companion artifacts: consolidated [exercises](docs/00-Orientation/exercises/README.md), a 20-question [quiz](docs/00-Orientation/quizzes/quiz-01.md) with model [answers](docs/00-Orientation/quizzes/answers-01.md), a full [flashcard deck](docs/00-Orientation/flashcards/deck.md), and a [master cheat sheet](docs/00-Orientation/cheat-sheets/orientation-cheatsheet.md).
  - Module [lesson index](docs/00-Orientation/weeks/README.md); linked from the module README.
- Glossary: added a "Foundations, Engineering & Learning (Module 00)" section (AI Engineering, AGI, reproducibility, SemVer, Conventional Commits, active recall, spaced repetition, and more).

### Notes
- Lessons follow the standards library and the 26-section master template, adapted for conceptual/orientation content (template sections not applicable to non-technical material — e.g. Security/Performance Considerations — are intentionally omitted with a note).

---

## [0.4.0] — 2026-07-08

### Changed
- **Adopted Curriculum Review Option A — expanded to 22 modules.** Inserted `12-Prompt-Engineering` (after LLMs) and `15-Fine-Tuning` (after AI-Agents); renumbered former modules `12–19` → `13–21`.
- Regenerated all `docs/` module folders, READMEs, and navigation from the updated [scripts/generate_structure.py](scripts/generate_structure.py) (single source of truth).
- Realigned `README.md`, `ROADMAP.md` (now ~57 weeks, updated dependency graph & phases), `CURRICULUM.md`, and `PROGRESS_TRACKER.md` to the 22-module taxonomy.
- Marked the structural decision as applied in [CURRICULUM_REVIEW.md](CURRICULUM_REVIEW.md).

---

## [0.3.0] — 2026-07-08

### Added
- **Standards library** in [standards/](standards/): documentation philosophy, visual, code, retention, exercise, project, interview, and reference standards, plus an index.
- **Master lesson template** — canonical 26-section structure in [templates/lesson-template.md](templates/lesson-template.md).
- **Curriculum validation** in [CURRICULUM_REVIEW.md](CURRICULUM_REVIEW.md): gap analysis (fine-tuning, prompt engineering, data engineering, evaluation), ordering check, and a structural decision proposal.

### Changed
- Upgraded [templates/project-template.md](templates/project-template.md) to the required 9-section project standard.
- Linked the standards library from [CONTRIBUTING.md](CONTRIBUTING.md) and [README.md](README.md); aligned naming conventions to the `NN-Title-Case` scheme.

---

## [0.2.0] — 2026-07-08

### Changed
- **Expanded to a 20-module taxonomy** (`00-Orientation` … `19-Capstone-Projects`), superseding the earlier 16-module ML-only structure. Added Computer Science, Linux, Git, SQL, Data Analysis, Cloud, System Design, and Interview Preparation as first-class modules.
- Restructured `docs/` so each module is a top-level folder (removed the `docs/modules/` nesting).
- Realigned `README.md`, `ROADMAP.md`, `CURRICULUM.md`, `REPOSITORY_STRUCTURE.md`, and `PROGRESS_TRACKER.md` to the new taxonomy.

### Added
- Full repository skeleton: every module folder with eight standardized subfolders (`weeks/`, `diagrams/`, `exercises/`, `projects/`, `quizzes/`, `flashcards/`, `cheat-sheets/`, `references/`).
- Navigation-rich `README.md` for every module and top-level folder (parent / prev / next / roadmap / related).
- New top-level folders: `code/`, `notebooks/`, `interview-preparation/`, `scripts/`, `archive/`, and `assets/{icons,cheatsheets}`.
- Twelve reusable templates (lesson, weekly summary, project, exercise, quiz, flashcards, architecture notes, research-paper summary, cheat sheet, interview notes, debugging session, project retrospective).
- `LICENSE.md` (CC BY 4.0 content + MIT code) and `.gitignore`.
- `scripts/generate_structure.py` — idempotent generator that owns the structural/templated files.

### Removed
- Superseded top-level `cheatsheets/`, `interview-prep/`, and `glossary/` folders (replaced by `assets/cheatsheets/`, `interview-preparation/`, and per-module `references/`).

---

## [0.1.0] — 2026-07-08

### Added
- Initial repository structure (docs, assets, exercises, quizzes, flashcards, projects, notebooks, references, cheatsheets, interview-prep, glossary, templates).
- Planning documents:
  - `README.md` — entry point and overview
  - `ROADMAP.md` — full modules → weeks → lessons plan with estimates, difficulty, and dependency graph
  - `CURRICULUM.md` — lesson-by-lesson learning outcomes
  - `REPOSITORY_STRUCTURE.md` — folder map and conventions
  - `LEARNING_STRATEGY.md` — retention system (active recall, spaced repetition, project-based learning)
  - `CONTRIBUTING.md` — style guide and standards
  - `PROGRESS_TRACKER.md` — personal progress checklist
  - `RESOURCES.md` — curated external resources
  - `GLOSSARY.md` — master glossary index
  - `FAQ.md` — frequently asked questions
  - `CHANGELOG.md` — this file

### Notes
- Planning phase complete. Module content authoring begins next, one module at a time.
