# 🏋️ Module 06 · Mathematics — Exercises

[🏠 Module 06](../README.md) · [📖 Lessons](../weeks/README.md) · [📝 Quiz](../quizzes/quiz-01.md)

> Every lesson has its own exercise set. This page is the **index** plus the exercises that span the whole module — the ones that force different lessons to collide.

> [!IMPORTANT]
> **Run the code. All of it.** Mathematics becomes real when you *see* a matrix rotate a vector, watch gradient descent roll downhill, or print an attention matrix. Reading these lessons without executing the NumPy is the most efficient way to acquire an illusion of understanding.

---

## Per-lesson exercises

| Lesson | Exercise types |
|---|---|
| [06.1 Mathematical Thinking](../weeks/06.1-mathematical-thinking.md#-exercises) | Conceptual · intuition · NumPy · equation interpretation |
| [06.2 Vectors & Matrices](../weeks/06.2-linear-algebra-vectors-matrices.md#-exercises) | + visualization (matrix transformations) |
| [06.3 Decomposition](../weeks/06.3-linear-algebra-decomposition.md#-exercises) | + PCA, SVD image compression, LoRA |
| [06.4 Calculus](../weeks/06.4-calculus.md#-exercises) | + gradient checking, micro-autograd |
| [06.5 Probability](../weeks/06.5-probability.md#-exercises) | + sampling, temperature, probability trees |
| [06.6 Statistics](../weeks/06.6-statistics.md#-exercises) | + bootstrap, permutation tests, p-hacking sim |
| [06.7 Optimization](../weeks/06.7-optimization.md#-exercises) | + optimizer race, LR finder |
| [06.8 Information Theory](../weeks/06.8-information-theory.md#-exercises) | + entropy monitoring, KL, distillation |
| [06.9 Numerical Computing](../weeks/06.9-numerical-computing.md#-exercises) | + deliberate NaN production and repair |
| [06.10 Neural Networks](../weeks/06.10-neural-network-math.md#-exercises) | + full network from scratch |
| [06.11 Transformers](../weeks/06.11-transformer-math.md#-exercises) | + attention from scratch, heatmaps |
| [06.12 Reading Notation](../weeks/06.12-reading-notation.md#-exercises) | + notation drills, paper decoding |

---

## 🔗 Cross-lesson exercises

**These are the valuable ones.** Each forces two or more lessons to fuse — which is where understanding actually lives.

### 1 · The ravine, three ways ⭐

The function $f(x,y) = x^2 + 10y^2$ appears in three lessons. Unify them.

1. Compute its **Hessian** and its eigenvalues by hand. ([06.4](../weeks/06.4-calculus.md))
2. From the eigenvalues, compute the **condition number** and the **maximum stable learning rate** $2/\lambda_{\max}$. ([06.3](../weeks/06.3-linear-algebra-decomposition.md))
3. Run gradient descent at lr = 0.05, 0.09, **0.11**. **Predict which one diverges before you run it.** ([06.7](../weeks/06.7-optimization.md))
4. Add momentum. Measure the **path length** reduction.
5. Plot all trajectories on one contour map.

> **You should be able to predict your own divergence from an eigenvalue.** When that works, linear algebra, calculus, and optimization have become one subject rather than three.

### 2 · The √d_k, derived from scratch ⭐

The scaling factor in attention is a variance argument. Rediscover it.

1. For d_k ∈ {4, 16, 64, 256, 1024}, generate random q, k and measure `std(q·k)`. Confirm it equals **√d_k**. ([06.5](../weeks/06.5-probability.md))
2. Feed those raw scores into a softmax. Measure the output **entropy**. ([06.8](../weeks/06.8-information-theory.md))
3. Plot entropy vs d_k **with and without** the √d_k scaling. **Watch the unscaled version saturate to near-zero entropy.**
4. Explain, in terms of the softmax's derivative, why near-zero entropy means near-zero gradient. ([06.4](../weeks/06.4-calculus.md))

> **You have now independently derived a design decision from a landmark paper.** That's what this module is for.

### 3 · Why LoRA exists — the memory argument

1. For a 7B-parameter model in fp32: compute weights, gradients, and **Adam's optimizer state**. Total? ([06.7](../weeks/06.7-optimization.md))
2. Compare against inference memory (weights only).
3. Now apply LoRA with r=8 to every attention projection. Recompute the trainable parameters and optimizer state. ([06.3](../weeks/06.3-linear-algebra-decomposition.md))
4. **What fits on a 24 GB consumer GPU, and what doesn't?**

> LoRA is not a clever trick — it's the intersection of a **rank** fact and a **memory** fact. Do the arithmetic and it becomes obvious.

### 4 · Build the NaN, then kill it

1. Write a softmax without max-subtraction. Feed it `[1000, 1001, 1002]`. Get `nan`. ([06.9](../weeks/06.9-numerical-computing.md))
2. Compute `log(0)` from a cross-entropy where the model assigned probability 0 to the truth. ([06.8](../weeks/06.8-information-theory.md))
3. Train a deep sigmoid network and watch the layer-1 gradient norm decay to ~1e-30. ([06.4](../weeks/06.4-calculus.md))
4. Blow up the same network with lr=10. Get `inf`.
5. **Fix all four.** Document which fix addresses which failure mode.

### 5 · The honest evaluation ⭐

You've trained two models. A: 87.2%. B: 87.9%. Test set: 1000 examples.

1. Compute a **bootstrap 95% CI** for each. ([06.6](../weeks/06.6-statistics.md))
2. Run a **paired** significance test.
3. Run a **permutation** test (no assumptions).
4. Compute how many test examples you'd need to detect a 0.7% difference reliably.
5. **Write the one-sentence honest conclusion**, including the interval and n.

> This is the most professionally useful exercise in the module. Most engineers cannot do it, and it's why the field ships so much noise.

### 6 · From micrograd to a Transformer

The capstone chain. Build each on the last.

1. `Value` class with `+`, `*`, `relu`, and `backward()`. ([06.4](../weeks/06.4-calculus.md))
2. Gradient-check every op.
3. Train a 2-layer MLP on XOR using only `Value` objects.
4. Rewrite it with NumPy arrays and layer classes. Train MNIST to >95%. ([06.10](../weeks/06.10-neural-network-math.md))
5. Add multi-head causal attention. ([06.11](../weeks/06.11-transformer-math.md))
6. Train it on Shakespeare. **Generate text.**

> **No frameworks at any step.** This is a weekend, and it will change how you see every model you ever touch again.

---

## 🧩 Blank-page recall

Close every tab. On a blank page, from memory:

1. Write the **matmul shape rule** and explain why it works.
2. Write the **gradient descent update rule** and say which direction the gradient points.
3. Write **cross-entropy loss** for a one-hot target, and its gradient w.r.t. the logits.
4. Write the **attention equation** and explain why the √d_k is there.
5. Write the **four backward rules** (matmul, bias, elementwise, softmax+CE).
6. Explain **why residual connections work**, using a derivative.
7. Explain **why LoRA works**, using the word "rank."
8. List the **three numerical-stability tricks**.
9. State how **uncertainty scales with n**, and what that means for your eval set.
10. Recite the **ten sentences that carry modern AI**.

> [!TIP]
> **Blank-page recall is brutal and it is the single most effective study technique there is.** Whatever you can't produce from an empty page, you don't know — regardless of how familiar it felt while reading. Do this once a week. ([00.7 Learning Techniques](../../00-Orientation/weeks/00.7-learning-techniques.md))

---

## ✅ Solutions

Solutions are **deliberately not provided** for most exercises. Verification is built in instead — and it's better than an answer key:

| Exercise type | How you know you're right |
|---|---|
| From-scratch NumPy op | `np.allclose(mine, np.<builtin>)` |
| Hand-derived gradient | **Gradient check** against central differences |
| PCA | Compare against `sklearn` (allowing sign flips) |
| Optimizer | It must converge on the convex bowl |
| Attention | Rows of the weight matrix sum to 1; the causal mask blocks the future |
| Statistics | Bootstrap CI ≈ analytic CI on normal data |
| Stability | The unstable version must NaN; the stable one must not |

> **Mathematics has a property most subjects lack: you can check your own work.** Use it. A gradient check is worth more than any solutions manual, because it tells you *that* you're wrong — and then you have to find out *why*, which is where the learning happens.

---

[⬆ Module 06](../README.md) · [📖 Lessons](../weeks/README.md) · [🧠 Flashcards](../flashcards/deck.md) · [📝 Quiz](../quizzes/quiz-01.md)
