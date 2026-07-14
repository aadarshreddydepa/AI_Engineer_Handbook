# 📄 Mathematics for AI Engineers — Cheat Sheet

[🏠 Module 06](../README.md) · [📖 Lessons](../weeks/README.md)

> Every formula, symbol, and NumPy translation from Module 06, on one page. **Intuition first, code second, formalism third.**

---

## 🔤 Notation → NumPy (the Rosetta Stone)

| Notation | Means | NumPy |
|---|---|---|
| $\sum_i x_i$ | loop and add | `x.sum()` |
| $\sum_j A_{ij}$ | sum j, **keep i** | `A.sum(axis=1)` |
| $\prod_i x_i$ | loop and multiply | **`np.log(x).sum()`** ← always |
| $x^\top y$, $\langle x,y\rangle$ | dot product | `x @ y` |
| $AB$ | matrix multiply | `A @ B` |
| $A \odot B$ | **element-wise** | `A * B` |
| $A^\top$ | transpose | `A.T` |
| $\|x\|$ | L2 norm | `np.linalg.norm(x)` |
| $\mathbb{E}[X]$ | expectation | `X.mean()` |
| $\nabla_\theta L$ | gradient w.r.t. θ | `loss.backward()` |
| $\arg\max_x f(x)$ | **the x** that maximizes | `np.argmax` |
| $\hat{y}$ / $\bar{x}$ / $\theta^*$ | predicted / mean / optimal | — |
| $x \in \mathbb{R}^{768}$ | **shape declaration** | `shape == (768,)` |
| $x \sim p$ | sampled from p | `rng.choice(..., p=p)` |

**Rule:** the **summed index is the axis that disappears.**
**Overloaded:** σ (sigmoid / std), α (LR / Dirichlet / significance), λ (regularization / eigenvalue), p (probability / p-value / top-p). **Context decides.**

---

## 📐 Linear Algebra

| Concept | Formula | NumPy | Meaning |
|---|---|---|---|
| Norm | $\sqrt{\sum x_i^2}$ | `np.linalg.norm(x)` | arrow length |
| **Dot product** | $\sum x_i y_i$ | `x @ y` | **ALIGNMENT** |
| **Cosine similarity** | $\frac{x\cdot y}{\|x\|\|y\|}$ | normalize, then `@` | alignment, magnitude-free |
| Matmul | $C_{ij}=\sum_p A_{ip}B_{pj}$ | `A @ B` | **function composition** |
| Transpose | $A^\top_{ij} = A_{ji}$ | `A.T` | free (a view) |
| Gram / covariance | $X^\top X$ | `X.T @ X` | how features relate |
| Solve | $Ax=b$ | **`np.linalg.solve`** | ✅ never `inv()` |
| Rank | # independent rows | `np.linalg.matrix_rank` | real information content |
| Determinant | $ad-bc$ | **`np.linalg.slogdet`** | volume scale factor |
| Eigen | $Av = \lambda v$ | **`np.linalg.eigh`** (symmetric) | unrotated directions |
| **SVD** | $A = U\Sigma V^\top$ | `np.linalg.svd` | **rotate → stretch → rotate** |
| Condition number | $\sigma_{\max}/\sigma_{\min}$ | `np.linalg.cond` | error amplification |
| PCA | SVD of **centered** X | — | top-k variance directions |
| **LoRA** | $W + BA$, rank ≤ r | — | **256× fewer trainable params** |

> **THE SHAPE RULE:** `(m,k) @ (k,n) → (m,n)`. Inner must match and vanish; outer survives.
> **THE BIG EQUIVALENCE:** det=0 ⟺ rank-deficient ⟺ λ=0 ⟺ σ=0 ⟺ not invertible ⟺ **space collapsed**.
> **Cost:** O(m·n·k). **>90% of a Transformer's FLOPs are matmuls.**

---

## ∂ Calculus

| Concept | Formula | Meaning |
|---|---|---|
| Derivative | $f'(x)$ | **sensitivity** |
| **Gradient** | $\nabla f = [\partial f/\partial x_1, \dots]$ | **steepest ASCENT**; same shape as the parameter |
| **Chain rule** | $\frac{dz}{dx} = \frac{dz}{dy}\frac{dy}{dx}$ | **= BACKPROPAGATION** |
| Jacobian | $J_{ij} = \partial f_i/\partial x_j$ → `(m,n)` | vector-in, vector-out |
| Hessian | $H_{ij} = \partial^2 f/\partial x_i\partial x_j$ → `(n,n)` | **curvature** |
| **GD update** | $\theta \leftarrow \theta - \eta\nabla L$ | **all of deep learning** |
| Stability bound | $\eta < 2/\lambda_{\max}(H)$ | max safe learning rate |
| Condition number | $\kappa = \lambda_{\max}/\lambda_{\min}$ | how ravine-like the loss is |

### Derivatives to know

| $f$ | $f'$ | Consequence |
|---|---|---|
| $x^n$ | $nx^{n-1}$ | MSE |
| $e^x$ | $e^x$ | softmax/sigmoid |
| $\ln x$ | $1/x$ | cross-entropy |
| **ReLU** | **1** if x>0 else 0 | ✅ **gradients survive depth** |
| **Sigmoid** | $\sigma(1-\sigma) \le \mathbf{0.25}$ | ❌ $0.25^{10}=10^{-6}$ → **vanishes** |
| **Residual** | $\partial(x+f(x))/\partial x = \mathbf{1} + f'(x)$ | ✅ **the gradient highway** |

> **Vanishing/exploding = the chain rule multiplying.** $\lambda^n$: 0.9⁵⁰≈0.005, 1.5⁵⁰≈6×10⁸.
> **In high dimensions the enemy is SADDLE POINTS, not local minima.**

---

## 🎲 Probability

| Concept | Formula | Meaning |
|---|---|---|
| Expectation | $\mathbb{E}[X] = \sum x P(x)$ | `.mean()` |
| **Conditional** | $P(A\mid B) = \frac{P(A,B)}{P(B)}$ | **"given that"** |
| **Bayes** | $P(A\mid B) = \frac{P(B\mid A)P(A)}{P(B)}$ | posterior = likelihood × prior / evidence |
| Independence | $P(A,B)=P(A)P(B)$ | knowing one tells you nothing |
| Marginal | $P(A) = \sum_B P(A,B)$ | **`.sum(axis=...)`** |
| **Chain rule** | $P(w_{1:T}) = \prod_t P(w_t\mid w_{<t})$ | **= autoregressive LLM** |
| Softmax | $\frac{e^{z_i/T}}{\sum_j e^{z_j/T}}$ | logits → distribution |
| Normal | 68 / 95 / 99.7 within 1/2/3σ | the CLT's attractor |
| **He init** | $\mathcal{N}(0, \sqrt{2/n_{\text{in}}})$ | keeps activation variance ≈ 1 |

> **AN LLM COMPUTES:** $P(\text{next token} \mid \text{all previous tokens})$. **Prompting = choosing what goes after the bar.**
> **BASE-RATE TRAP:** a 99%-accurate test for a 1-in-10,000 disease → **P(disease \| positive) < 1%.** Accuracy is a lie on imbalanced data.
> **Temperature:** low = sharp/deterministic; high = flat/creative. **Top-p beats top-k** because it adapts to confidence.

---

## 📊 Statistics

| Concept | Formula | Use |
|---|---|---|
| **Median / p95 / p99** | — | ✅ **latency — NEVER the mean** |
| Std (sample) | `np.std(x, ddof=1)` | ⚠️ default `ddof=0` understates it |
| **Correlation** | $\rho = \frac{\text{Cov}}{\sigma_X\sigma_Y} \in [-1,1]$ | **LINEAR only** (ρ≈0 for y=x²) |
| **Standard error** | $\sigma/\sqrt{n}$ | **uncertainty shrinks as 1/√n** |
| **95% CI** | $\bar{x} \pm 1.96\,\text{SE}$ | put one on **every** metric |
| **Bootstrap** | resample → recompute → percentile | **CI for ANY metric.** Learn this |
| p-value | $P(\text{data}\mid H_0)$ | **NOT** P(hypothesis) |
| Paired test | `stats.ttest_rel` | ✅ same test set → **always pair** |
| Bias vs variance | train↑val↑ / train↓val↑ | underfit / overfit |

> **REPORT EVERY METRIC AS:** `87.9% ± 1.4% (95% CI, n=1000, 5 seeds)`.
> **To halve the error bar you need 4× the data.** A 500-example eval set cannot resolve a 2% difference.
> **p-hacking:** 40 configs at α=0.05 → ~2 "win" by pure chance.

---

## 🎯 Optimization

| Optimizer | Update | Key idea |
|---|---|---|
| SGD | $\theta \mathrel{-}= \eta g$ | step downhill |
| **Momentum** | $v = \beta v + g$; $\theta \mathrel{-}= \eta v$ | **remember past gradients** → kills ravine zig-zag |
| AdaGrad | $s \mathrel{+}= g^2$ | per-param LR — **but it decays to zero** |
| **RMSProp** | $s = \beta s + (1{-}\beta)g^2$ | **EMA** so it doesn't die |
| **Adam** | momentum + RMSProp + bias correction | ✅ robust default |
| **AdamW** | decay applied **outside** the scaling | ✅ **the LLM default** |

| Rule | |
|---|---|
| **LR is the #1 hyperparameter** | Tune it first |
| Linear scaling rule | batch ×k → LR ×k (+ warmup) |
| Schedule | **linear warmup + cosine decay** |
| **Warmup exists because** | Adam's `v` estimate is unreliable at step 0 |
| **Adam memory** | **3× params** (w + m + v) → why fine-tuning OOMs → **why LoRA exists** |
| Gradient noise | A **feature** — finds flat minima that generalize |
| Non-convexity | Works anyway: saddles ≫ minima; most minima are equally good |

**Losses:** MSE (clean regression) · **Huber** (outliers) · **Cross-entropy** (classification, LLMs) · InfoNCE (embeddings)

---

## 📡 Information Theory

| Concept | Formula | Meaning |
|---|---|---|
| **Information** | $-\log p$ | **surprise** |
| **Entropy** | $H(p) = -\sum p\log p$ | **average surprise** = uncertainty |
| **Cross-entropy** | $H(p,q) = -\sum p\log q$ | surprise using the **wrong** model |
| **CE loss (one-hot)** | $\boxed{-\log q_{\text{correct}}}$ | **the loss of every classifier & LLM** |
| **KL divergence** | $D(p\|q) = H(p,q) - H(p)$ | the **extra cost** of being wrong |
| **The identity** | CE = Entropy + KL | ∴ minimizing CE ≡ minimizing KL |
| **Perplexity** | $e^{H}$ | "effectively choosing among N tokens" |
| Mutual information | $I(X;Y) = H(X) - H(X\mid Y)$ | **ANY** dependence (not just linear) |
| **Softmax+CE gradient** | $\boxed{q - p}$ | **predicted − actual.** That's it |

> **WHY CROSS-ENTROPY:** $H(p,q) \ge H(p)$ with equality **iff q = p**. Minimizing it *is* matching reality. A theorem, not a heuristic.
> **KL is NOT a distance** (asymmetric). Forward = mean-seeking (covers modes); reverse = mode-seeking (collapses). **RLHF:** `reward − β·KL(policy‖ref)` — the leash against reward hacking.

---

## 🔢 Numerical Computing

| Problem | Fix |
|---|---|
| `exp()` overflow in softmax | **`z = z - z.max()`** ← in every production softmax on Earth |
| `log(0)` = −inf → NaN | `log_softmax` (fused), or clip with `eps` |
| Product of probabilities → 0 | **Work in log space:** $\log\prod = \sum\log$ |
| $\log\sum e^x$ overflows | **log-sum-exp:** $\max(x) + \log\sum e^{x-\max}$ |
| Division by ~0 | `eps = 1e-8` |
| Naive variance goes **negative** | Two-pass: `((x - x.mean())**2).mean()` |
| `==` on floats | `np.allclose` |
| `(n,)` vs `(n,1)` **silent outer op** | **`keepdims=True`** |
| Python loop | **Vectorize** — 100–1000× |

| dtype | Bits | **Range** | Use |
|---|---|---|---|
| float32 | 32 | 1e±38 | Safe DL default |
| **bfloat16** | 16 | **1e±38** ✅ | ✅ **Modern LLM training** |
| float16 | 16 | **6e−5 … 65,504** ⚠️ | Overflows constantly |

> **WHY bf16 WON:** it keeps float32's **8-bit exponent** (range) and sacrifices mantissa (precision). **Deep learning needs RANGE, not precision.** One insight; reshaped the hardware industry.
> **NaN is CONTAGIOUS** — one bad value poisons every weight in one step. `assert not np.isnan(X).any()`.

---

## 🧠 Neural Networks

| Forward | Backward |
|---|---|
| `Z = A @ W + b` | `dW = A.T @ dZ` · `db = dZ.sum(0)` · `dA = dZ @ W.T` |
| `A = relu(Z)` | `dZ = dA * (Z > 0)` ← **`*` not `@`** |
| `P = softmax(Z)`, `L = CE(P,y)` | `dZ = (P − Y) / B` |

| Rule | |
|---|---|
| **No nonlinearity → no depth** | linear ∘ linear = linear. 100 layers collapse to 1 |
| **Broadcast forward = sum backward** | the bias gradient |
| **Gradient shape = parameter shape** | use it to *derive* the transposes |
| **Initial loss should be ln(C)** | **2.303** (10 classes) · **10.82** (50k vocab). Print it! |
| Zero-init | ❌ symmetry never breaks |
| Gradient-check in **float64** | float32 eps is too coarse |

**Activations:** ReLU (default, derivative = 1) · **GELU/SiLU** (Transformers — smooth, no dead neurons) · Sigmoid (❌ hidden layers)

---

## 🤖 Transformers

$$\boxed{\text{Attention}(Q,K,V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V}$$

| Term | Shape | Role |
|---|---|---|
| Q, K, V | `(n,d_k)`, `(n,d_k)`, `(n,d_v)` | all `= XW` |
| $QK^\top$ | **`(n,n)`** | every query · every key ← **the O(n²)** |
| softmax | `(n,n)` | rows sum to 1 |
| output | `(n,d_v)` | weighted average of values |

| Concept | |
|---|---|
| **Attention =** | a **soft, differentiable dictionary lookup** |
| **Why √d_k** | Var(q·k) = d_k → softmax saturates → gradients vanish. **Variance fix** |
| **Causal mask** | `np.tril`, scores → −1e9 **before** softmax. **The ONLY difference between GPT and BERT** |
| Multi-head | h heads at `d_k = d/h` → **same total FLOPs.** Free |
| **Positional encoding** | Mandatory — attention is **permutation-invariant** |
| **RoPE** | Rotate q,k by position → scores depend on **(m−n)**. LLaMA/Mistral/Qwen |
| **Block** | `x + MHA(LN(x))`; `x + FFN(LN(x))`. Repeat 80× |
| Division of labour | **Attention mixes across tokens; FFN thinks about each one** (FFN ≈ 2/3 of params) |
| Complexity | **O(n²·d)** — why long context is a research field |
| FlashAttention | **Same math**, better memory access. The bottleneck was never FLOPs |

---

## 📖 Reading Papers

**3 passes:** triage (10 min: abstract + figures + conclusion) → method (1 h: decode the core equation, **skip proofs**) → reimplement (½ day)

**7-step decode:** symbols → **shapes** → read aloud → **shrink to n=2** → implement → **ABLATE ("what breaks if I remove this?")** → plain English

> **The ablation step is where the understanding is.** It's how you'd discover the √d_k argument yourself.
> **Skip the proofs. Read the ablation table.**
> **Confusion is the process, not a verdict.**

---

## 🎯 The ten sentences that carry modern AI

1. **The dot product measures alignment** → similarity, attention, neurons, logits.
2. **A matrix is a function**; matmul is composition — hence depth needs nonlinearity.
3. **The gradient points uphill**; step against it. That's training.
4. **The chain rule multiplies** → backprop, and vanishing/exploding gradients.
5. **Eigenvalues to the n-th power** → why residual connections exist.
6. **Real matrices are low-rank** → PCA, compression, **LoRA**.
7. **Variance must be controlled** → He init, layer norm, **√d_k**.
8. **Cross-entropy is surprise**; its gradient is **predicted − actual**.
9. **Products underflow — take the log.** Every language model does.
10. **Uncertainty shrinks as 1/√n** — your eval set is smaller than you think.

---

[⬆ Back to Module 06](../README.md) · [📖 Lessons](../weeks/README.md) · [🧠 Flashcards](../flashcards/deck.md)
