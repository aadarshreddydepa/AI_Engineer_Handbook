# 📝 Module 07 Quiz · Data Analysis for AI Engineers

[🏠 Module 07](../README.md) · [📖 Lessons](../weeks/README.md) · [✅ Answers](answers-01.md)

> **30 questions across all 12 lessons.** Answer from memory first. Then check.
>
> **Scoring:** 25+ = ready for Module 08 · 20–24 = good, patch the gaps · < 20 = reread, retake in a week. **Diagnostic, not a verdict.**

---

## Part 1 — Lifecycle, NumPy, Pandas (1–9)

**1.** Why is a data bug more dangerous than a code bug? Answer with the specific asymmetry.

**2.** Name the eleven lifecycle stages. **Which arrow is the most important, and why?**

**3.** Name the **three failures** that cause most broken ML systems, and give the one-line detection for each.

**4.** Why is a NumPy array faster than a Python list? **Name all five mechanisms.**

**5.** Which NumPy operations return a **view** and which return a **copy**? Why does the distinction cause silent bugs?

**6.** What is a DataFrame, internally? Why are columns fast and rows slow — and what follows from that?

**7.** Explain `SettingWithCopyWarning`. Why does Pandas warn rather than just working? Write the fix.

**8.** You have a 70 MB DataFrame with a `country` column (4 unique values in 1M rows). **How do you get it to 8 MB?** What's the mechanism?

**9.** Give three reasons Parquet is a better default than CSV.

---

## Part 2 — Combining, Cleaning, EDA (10–18)

**10.** What is **row explosion**? How does `validate=` prevent it, and what's the value you should almost always pass?

**11.** Explain `.agg()` vs `.transform()` vs `.filter()` on a groupby. **Which one builds features, and why is it so powerful?**

**12.** ⭐ Why is `df['sales'].rolling(7).mean()` **leakage** in a forecasting model? Write the correct version.

**13.** Why is `.bfill()` leakage on a time series but `.ffill()` isn't?

**14.** ⭐ Explain **MCAR / MAR / MNAR**. Which must you never impute, and **how do you test for it**?

**15.** What is **disguised missingness**? Why does it make `df['age'].mean()` a lie, and **what's the fastest way to find it**?

**16.** Why is the **z-score** a poor outlier detector? What do you use instead?

**17.** ⭐ Should you remove outliers? Answer for: a $10M mansion, a corrupt JPEG, and Black Friday.

**18.** ⭐ State the **scaling leakage rule**. What breaks if you violate it — in evaluation, *and* in production?

---

## Part 3 — Features, Visualization, Quality (19–25)

**19.** Why do features matter more than models? **Quantify it. And say when it stops being true.**

**20.** How would you encode the **hour of the day**? Why do you need **two** columns?

**21.** Why is **permutation importance** more trustworthy than tree feature importance? Name the two biases. **And on which dataset must you compute it?**

**22.** ⭐ State the **six leakage rules** for feature engineering, and **the one universal test**.

**23.** What does a histogram reveal that `describe()` cannot? Name four things.

**24.** Why must a correlation heatmap use a **diverging** colormap centered at zero?

**25.** ⭐ If you could build only **two** data quality checks, which two — and why?

---

## Part 4 — Performance, Pipelines, Case Studies (26–30)

**26.** State the **optimization ladder** in order. Where does distributed computing sit, and why?

**27.** Which operations **chunk** cleanly and which don't? **Why is that — not file size — the real signal to change tools?**

**28.** ⭐ Why is a notebook not a pipeline? Name the specific mechanism that makes results irreproducible.

**29.** ⭐ What is the **skew test**, and what specific production disaster does it catch?

**30.** ⭐ Why does a **time-series validation split need a gap**? How big should it be?

---

## 🏁 Bonus — the integration questions

**B1.** Your model scores **0.94 AUC offline** and **0.71 in production**. Give five hypotheses, ranked by likelihood, and say how you'd distinguish them.

**B2.** For each of the five case studies (churn, houses, sentiment, images, forecasting), name the **signature leakage trap**.

**B3.** You're handed a new dataset and a target column. **Describe exactly what you do in the first hour** — before writing any modelling code.

**B4.** Recite the **ten sentences**.

---

[✅ Check your answers](answers-01.md) · [🧠 Flashcards](../flashcards/deck.md) · [📄 Cheat sheet](../cheat-sheets/data-cheatsheet.md)
