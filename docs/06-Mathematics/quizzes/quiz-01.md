# 📝 Module 06 Quiz · Mathematics for AI Engineers

[🏠 Module 06](../README.md) · [📖 Lessons](../weeks/README.md) · [✅ Answers](answers-01.md)

> **30 questions across all 12 lessons.** Answer from memory first. Then check. Anything you miss becomes a flashcard and a lesson to reread.
>
> **Scoring:** 25+ = solid · 20–24 = good, patch the gaps · <20 = reread, then retake in a week. **This is diagnostic, not a verdict.**

---

## Part 1 — Thinking & Linear Algebra (1–8)

**1.** What are the **7 steps** for decoding an unfamiliar equation? Which step produces the actual insight, and why?

**2.** Explain the **dot product** in one sentence, and name four places it appears in AI.

**3.** State the **matmul shape rule**. Then: `X` is `(32, 768)` and `W` is `(3072, 768)`. Write the expression that produces `(32, 3072)`, and say why PyTorch stores the weight that way.

**4.** Why is **cosine similarity** preferred over the raw dot product for text retrieval? And what is the production trick that makes cosine search a single matmul?

**5.** A matrix is described as "**singular**." Give **six equivalent statements** and the one geometric picture they all describe.

**6.** State the **SVD** in words. What does the **Eckart–Young theorem** guarantee, and which four AI techniques rest on it?

**7.** Explain **LoRA** using one equation and the word "rank." Why is `B` initialized to **zeros**? Why is `B @ (A @ x)` computed with those parentheses?

**8.** Your embedding matrix's singular values are `[50, 45, 40, 2, 1.8, 1.5, …]`. What does this tell you, and what would you do?

---

## Part 2 — Calculus & Optimization (9–15)

**9.** Which direction does the **gradient** point? What shape is `∇_W L` relative to `W`, and why does that fact let you derive the transposes in backprop?

**10.** What **is** backpropagation? Why **reverse** mode rather than forward mode — and what would forward mode cost for a 7B model?

**11.** Sigmoid's derivative maxes at **0.25**. Compute `0.25^10`. Now explain, in one sentence, why ReLU replaced sigmoid in hidden layers.

**12.** Why do **residual connections** (`x + f(x)`) make 100-layer networks trainable? Give the derivative.

**13.** In high dimensions, what is the *real* obstacle to optimization — local minima or saddle points? Justify with an eigenvalue argument.

**14.** **Adam** = ___ + ___ + ___. What problem does each component solve? How much memory does it cost, and what does that imply for fine-tuning a 7B model?

**15.** Why do Transformers need **learning-rate warmup**? What specifically is unreliable at step 0?

---

## Part 3 — Probability, Statistics, Information (16–23)

**16.** Write the equation for **what an LLM computes**. What is "prompt engineering," expressed in terms of that equation?

**17.** A test is **99% accurate**. The disease affects **1 in 10,000**. You test positive. What's the probability you have it — and what is the ML lesson?

**18.** What does **temperature** do mechanically? Why is **top-p** better than top-k?

**19.** Your API's mean latency is 180 ms and users are complaining. What's wrong with that number, and what should you report instead?

**20.** How does uncertainty scale with sample size? You want to halve your error bar — how much more data do you need? What does this mean for a 500-example eval set?

**21.** Model A scores 87.2%, Model B scores 87.9%, on 1000 test examples. **Do you ship B?** Name every check you'd run.

**22.** Derive **cross-entropy loss** for a one-hot target from `H(p,q) = −Σ p log q`. Then state *why* it's the correct loss (there's a theorem).

**23.** What is the gradient of **softmax + cross-entropy** w.r.t. the logits? Why does `nn.CrossEntropyLoss` take **logits** rather than probabilities — give both reasons.

---

## Part 4 — Numerical, Networks, Transformers (24–30)

**24.** Why do LLMs train in **bfloat16** rather than float16, despite bf16 having *less* precision? Answer using the exponent bits.

**25.** Name the **three numerical-stability tricks** that prevent most NaNs. For each, say what it prevents.

**26.** Prove in one line that a neural network **without activation functions** is equivalent to a single linear layer. What is the consequence?

**27.** Your 10-class classifier's initial loss is **6.9** instead of 2.303. What does that tell you? (Show the arithmetic.)

**28.** Write the **attention equation**. Then explain **why the √d_k is there** — and which three lessons of this module the explanation draws on.

**29.** What is the **only** architectural difference between BERT's and GPT's attention? Why must the mask be applied *before* the softmax?

**30.** Why is attention **O(n²)**? Name three distinct attacks on it — and say which one changed *nothing* mathematically and won anyway.

---

## 🏁 Bonus — the integration questions

**B1.** Trace **residual connections** back through three lessons: what calculus fact, what linear algebra fact, and what architectural consequence?

**B2.** You've been handed a paper you've never seen. Describe, step by step, exactly what you would do in the next 10 minutes, the next hour, and the next day.

**B3.** Recite the **ten sentences that carry modern AI**. (No peeking.)

---

[✅ Check your answers](answers-01.md) · [🧠 Flashcards](../flashcards/deck.md) · [📄 Cheat sheet](../cheat-sheets/math-cheatsheet.md)
