# 📝 Module 08 Quiz · Machine Learning Foundations

[🏠 Module 08](../README.md) · [📖 Lessons](../weeks/README.md) · [✅ Answers](answers-01.md)

> **35 questions across all 17 lessons.** Answer from memory first.
>
> **Scoring:** 30+ = ready for Module 09 · 24–29 = good, patch the gaps · < 24 = reread, retake in a week.

---

## Part 1 — Foundations & Linear Models (1–8)

**1.** What is the **one test** for whether you should use ML at all?

**2.** ⭐ Name the **four boxes** of every supervised algorithm. Fill them in for linear regression, decision trees, and KNN. **What's strange about KNN's?**

**3.** ⭐ Why must the **test set** be touched exactly once? What happens if you tune on it?

**4.** ⭐ Give the **five-second overfit/underfit diagnostic.** Why do the two need **opposite** fixes?

**5.** ⭐ **Derive the MSE gradient.** State every shape. Say what it *means* in English.

**6.** ⭐ Why does **Ridge** make $X^\top X$ always invertible? *(Use the eigenvalue argument.)*

**7.** ⭐⭐ Why is **MSE catastrophic** as a loss for logistic regression? Be precise about **what vanishes and when.**

**8.** ⭐ What is the **log-loss gradient**, and why is it remarkable?

---

## Part 2 — Trees, Ensembles, SVM (9–16)

**9.** How does a decision tree **choose a split**? Why is the algorithm greedy?

**10.** ⭐ Why does an **unpruned tree always overfit**? What can it achieve on pure noise?

**11.** ⭐ Why do trees **not need scaling**? Name two things trees **cannot** do.

**12.** ⭐⭐ **Why do ensembles work?** Give the **formula**. What happens when ρ = 1?

**13.** ⭐ How does **Random Forest** decorrelate its trees? Why is `max_features` counterintuitive?

**14.** ⭐ Why is it called ***gradient*** boosting? Why does that make it a *framework* rather than an algorithm?

**15.** ⭐ Why is **early stopping mandatory** for boosting but **not** for Random Forest?

**16.** ⭐⭐ Explain the **kernel trick.** Why is φ(x) never needed?

---

## Part 3 — NB, KNN, Clustering, PCA (17–23)

**17.** ⭐⭐ Naive Bayes assumes independence, which is **obviously false**. **Why does it still work?** And what *does* it ruin?

**18.** ⭐ Why must Naive Bayes use **Laplace smoothing** and **log space**? What breaks without each?

**19.** ⭐⭐ Explain the **curse of dimensionality.** What does it do to the *meaning* of "nearest"?

**20.** ⭐⭐ Then **why does RAG work** with 768-dimensional embeddings?

**21.** ⭐⭐ What's the **most dangerous property of clustering**? How do you **actually** validate a clustering?

**22.** ⭐ Why is **centering mandatory** before PCA? What does PC1 become without it?

**23.** ⭐⭐ Name the **three ways people misread t-SNE plots.**

---

## Part 4 — Evaluation & Leakage (24–30)

**24.** ⭐ Why is **accuracy** dangerous? Give the arithmetic.

**25.** ⭐⭐ Why is **ROC-AUC misleadingly optimistic** under heavy imbalance? Use the FPR denominator.

**26.** ⭐⭐ Why is **tuning the threshold** the highest-return activity in evaluation? Where do you tune it?

**27.** ⭐⭐ **Why must preprocessing be inside the CV pipeline?** What exactly leaks?

**28.** ⭐ What happens if you do **feature selection before CV** — on pure random noise?

**29.** ⭐⭐ When do you need **`GroupKFold`**? Why does **time-series CV need a gap**?

**30.** ⭐ Which kind of leakage can **cross-validation NOT catch**? What *does* catch it?

---

## Part 5 — Tuning, Interpretability, Production (31–35)

**31.** ⭐⭐ Why does **random search beat grid search**? *(Give the argument, not just the claim.)*

**32.** ⭐ Why is **`feature_importances_` (MDI)** untrustworthy? Name both biases.

**33.** ⭐⭐ What makes **SHAP** trustworthy? And what is its **most valuable practical use**?

**34.** ⭐⭐ Why must you **monitor inputs** rather than performance? Give the label-delay argument.

**35.** ⭐⭐ Why can **automated retraining make things worse**? Name two mechanisms and the fix.

---

## 🏁 Bonus

**B1.** ⭐⭐ Your model scores **0.94 AUC offline** and **0.71 in production.** Give **five hypotheses**, ranked by likelihood, and say **how you'd distinguish them.**

**B2.** ⭐ You have **one week** to improve a model. **What do you do, day by day?**

**B3.** ⭐ Name the four algorithms where the **same regularization shape** (`loss + λ·complexity`) appears.

**B4.** Recite the **ten sentences.**

---

[✅ Answers](answers-01.md) · [🧠 Flashcards](../flashcards/deck.md) · [📄 Cheat sheet](../cheat-sheets/ml-cheatsheet.md)
