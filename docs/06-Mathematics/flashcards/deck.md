# 🧠 Module 06 · Mathematics — Flashcard Deck

[🏠 Module 06](../README.md) · [📖 Lessons](../weeks/README.md) · [📄 Cheat sheet](../cheat-sheets/math-cheatsheet.md)

> **~90 cards** for spaced repetition. Cover the answer, say it out loud, *then* check. If you can't explain the **why**, it's not learned — reread the linked lesson.

> [!TIP]
> **Mathematics rewards spaced repetition more than any other module in this handbook.** The material is dense, interlinked, and notation-heavy — exactly the profile where re-reading fails and active recall wins. Ten minutes a day beats two hours on Sunday. See [00.7 Learning Techniques](../../00-Orientation/weeks/00.7-learning-techniques.md).

---

## 06.1 · Mathematical Thinking

**Q:** In one sentence, why is mathematics the language of AI?
**A:** It's the most compressed, unambiguous, framework-independent way to specify what a model computes — the math is the source of truth; every framework is a compilation target. → [06.1](../weeks/06.1-mathematical-thinking.md)

**Q:** What are the 7 steps of decoding an equation?
**A:** Identify symbols → determine shapes → read aloud → shrink to a tiny case → implement in NumPy → **ask what breaks if a term is removed** → state it in plain English.

**Q:** Which 4 mathematical ideas carry most of practical AI?
**A:** Dot product, gradient, probability distribution, cross-entropy.

**Q:** Why can't you debug AI with a stack trace?
**A:** AI failures are **silent and numerical** — NaN, vanishing gradients, drift, miscalibration. The code "succeeds" while the numbers are wrong.

**Q:** Why did Transformers beat RNNs partly for *hardware* reasons?
**A:** Attention is expressible as large matmuls (GPU-friendly, parallel); RNNs are inherently sequential. **Hardware shapes which mathematics wins.**

**Q:** What single habit resolves most equation confusion?
**A:** Annotating the **shape** of every symbol.

---

## 06.2 · Linear Algebra I

**Q:** What does the dot product *measure*?
**A:** **Alignment** — how much two vectors point the same way. Positive = similar, 0 = orthogonal/unrelated, negative = opposite. → [06.2](../weeks/06.2-linear-algebra-vectors-matrices.md)

**Q:** Why normalize embeddings before storing them?
**A:** With unit-length vectors, cosine similarity **is** the dot product — so search becomes a single matmul with no divisions. Every vector DB does this.

**Q:** State the matmul shape rule.
**A:** `(m,k) @ (k,n) → (m,n)`. **Inner dimensions must match and disappear; outer dimensions survive.**

**Q:** What is a matrix, conceptually?
**A:** A **linear transformation** — a function that moves vectors. Its **columns are where the basis vectors land**.

**Q:** What does matrix multiplication represent?
**A:** **Function composition**: `AB` = "apply B, then A." Hence `AB ≠ BA` — order is the whole meaning.

**Q:** Difference between `A * B` and `A @ B` in NumPy?
**A:** `*` is element-wise (Hadamard); `@` is matrix multiplication. Broadcasting means `*` often *succeeds* when you meant `@` — silently wrong.

**Q:** Why doesn't AI use the cross product?
**A:** It's defined only in 3-D. AI works in 768–4096 dimensions, where "perpendicular to both" isn't a unique vector.

**Q:** Complexity of matmul, and why it dominates AI?
**A:** **O(m·n·k)**. Over **90% of a Transformer's FLOPs** are matmuls — it's why GPUs and tensor cores exist.

**Q:** Three ways to read `C = AB`?
**A:** (1) a grid of dot products; (2) columns of C are weighted sums of A's columns; (3) apply one transformation to a whole batch of points.

**Q:** Why is a Python triple-loop matmul unacceptable?
**A:** ~1000–5000× slower than BLAS, which does the identical math with cache blocking, SIMD, and multithreading.

**Q:** Why do random high-dimensional vectors tend to be nearly orthogonal?
**A:** In high dimensions, random directions almost never align — which is *good news*: there's abundant room to place distinct meanings far apart.

---

## 06.3 · Linear Algebra II

**Q:** What does the determinant mean geometrically?
**A:** The factor by which the matrix **scales volume**. Zero means space was **collapsed** to a lower dimension → not invertible. → [06.3](../weeks/06.3-linear-algebra-decomposition.md)

**Q:** What is an eigenvector?
**A:** A direction the matrix **doesn't rotate** — it only scales it, by the eigenvalue: `Av = λv`.

**Q:** Why do gradients vanish or explode in deep networks?
**A:** Backprop multiplies by a Jacobian n times, raising its **eigenvalues to the n-th power**. λ<1 vanishes, λ>1 explodes; only λ≈1 survives depth.

**Q:** State the SVD in words.
**A:** Every matrix — any shape, any rank — is **rotate (Vᵀ) → stretch by singular values (Σ) → rotate (U)**.

**Q:** What does Eckart–Young guarantee?
**A:** Truncating the SVD to the top-k singular values gives the **provably best** rank-k approximation. The foundation of PCA, compression, LSA, and LoRA's intuition.

**Q:** What is PCA, in one sentence?
**A:** **Center** the data, take the SVD, keep the top-k right singular vectors as the new axes.

**Q:** Why must PCA center the data first?
**A:** PCA finds directions of maximum **variance**, measured around the mean. Without centering, the first "component" just points at the mean — carrying no information about variation. **Fails silently.**

**Q:** Why does LoRA work?
**A:** Fine-tuning updates are empirically **low-rank**, so ΔW can be parameterized as `BA` with r ≪ d (8–64) — **256× fewer trainable parameters** for the same effect.

**Q:** Why is LoRA's `B` initialized to zeros?
**A:** So `BA = 0` at step 0 — the adapted model **starts identical to the base model** and is perturbed gently. Random init would inject noise into a working model.

**Q:** Why never compute an explicit matrix inverse?
**A:** Slower and numerically unstable (amplifies error, catastrophically when ill-conditioned). Use `np.linalg.solve`.

**Q:** Six equivalent ways to say "singular"?
**A:** det = 0 · rank-deficient · has a zero eigenvalue · has a zero singular value · not invertible · **collapses space**. All one picture.

**Q:** What does a fast-decaying singular-value spectrum tell you?
**A:** The data has **low intrinsic dimensionality** — mostly redundant/noise. Compression, PCA, and low-rank methods will work well.

**Q:** Why does deep learning avoid matrix inversion entirely?
**A:** Inversion is O(n³) and fragile. Gradient descent replaces "solve exactly once" with "improve a little, many times" — that trade is *why it scales to billions of parameters*.

---

## 06.4 · Calculus

**Q:** What does a derivative *mean*, in one word?
**A:** **Sensitivity** — how much the output changes when you nudge the input. → [06.4](../weeks/06.4-calculus.md)

**Q:** Which direction does the gradient point?
**A:** Steepest **ascent**. To minimize, step in the **negative** gradient direction.

**Q:** What is backpropagation?
**A:** The **chain rule** applied right-to-left through the network, with forward activations cached. Reverse mode gets *all* gradients in **one** pass.

**Q:** Why reverse mode and not forward mode?
**A:** One output (the loss), billions of inputs (weights). Reverse mode costs one pass total; forward mode would cost one pass **per parameter**.

**Q:** Why do gradients vanish?
**A:** The chain rule **multiplies** per-layer factors. Sigmoid's derivative maxes at **0.25**, so 0.25ⁿ → 0 across depth.

**Q:** Why do residual connections fix that?
**A:** ∂(x + f(x))/∂x = **1** + f′(x). The leading 1 is a **gradient highway** that can never be multiplied away. Why ResNets go 152 layers and every Transformer block has `x + attn(x)`.

**Q:** Shapes: gradient vs Jacobian vs Hessian?
**A:** Gradient `(n,)` (scalar output); Jacobian `(m,n)` (vector output); Hessian `(n,n)` (second derivatives of a scalar).

**Q:** What do the Hessian's eigenvalues tell you?
**A:** All positive = **minimum**; mixed signs = **saddle**. The condition number λmax/λmin predicts zig-zagging, and 2/λmax is your **max stable learning rate**.

**Q:** Why isn't Newton's method used in deep learning?
**A:** It needs the **inverse Hessian** — `(n,n)` for n=7B is ~5×10¹⁹ entries. Impossible. Adam approximates curvature cheaply instead.

**Q:** What is gradient checking?
**A:** Comparing an analytical gradient against a **central-difference** numerical one — the standard unit test for hand-written backprop. Do it in **float64**.

**Q:** In high dimensions, is the enemy local minima or saddle points?
**A:** **Saddles.** A local minimum needs *all* eigenvalues positive — vanishingly unlikely with billions of them.

---

## 06.5 · Probability

**Q:** What does an LLM actually compute?
**A:** **P(next token | all previous tokens)** — a categorical distribution over the vocabulary. → [06.5](../weeks/06.5-probability.md)

**Q:** State Bayes' theorem and name the four terms.
**A:** P(A|B) = P(B|A)P(A)/P(B). **Posterior = likelihood × prior / evidence.**

**Q:** A test is 99% accurate for a disease affecting 1 in 10,000. You test positive. Probability you have it?
**A:** **Under 1%.** False positives from the huge healthy population overwhelm the rare true positives. **Base rates dominate.**

**Q:** Why is accuracy a bad metric on imbalanced data?
**A:** Always predicting the majority class gives high accuracy while catching nothing. Use precision / recall / F1 / PR-AUC.

**Q:** What does temperature do, mechanically?
**A:** **Divides the logits before the softmax.** T<1 sharpens the distribution (deterministic); T>1 flattens it (creative, more errors).

**Q:** Why is top-p better than top-k?
**A:** It **adapts to confidence** — a narrow nucleus when the model is certain, wide when uncertain. Top-k always keeps exactly k regardless.

**Q:** What is marginalization?
**A:** Summing a joint distribution over the variable you don't care about — literally **`.sum(axis=k)`**.

**Q:** State the chain rule of probability and its significance.
**A:** P(A,B,C) = P(A)P(B|A)P(C|A,B). It's the **definition of an autoregressive model** — why LLMs generate one token at a time.

**Q:** Why does naive Bayes work despite a false independence assumption?
**A:** Classification only needs the correct **ranking**, not calibrated probabilities. **A model can be badly wrong about the world and still useful for the decision.**

**Q:** Why does He initialization use √(2/n_in)?
**A:** It keeps the **variance of activations ≈ 1** as signal propagates, so activations neither vanish nor explode with depth. Initialization is applied probability.

**Q:** What's the most consequential violated assumption in applied ML?
**A:** **i.i.d.** — random-splitting correlated (especially time-series) data leaks the future and inflates metrics. **Split by time.**

**Q:** Why can a PDF value exceed 1?
**A:** It's a **density**, not a probability. Only *areas under it* are probabilities. For continuous variables, P(X = 3.7) = exactly 0.

---

## 06.6 · Statistics

**Q:** Why never report **mean** latency?
**A:** Latency is right-skewed; the mean describes **no real user**. Report p50/p95/p99 — the tail is where the SLA breaks. → [06.6](../weeks/06.6-statistics.md)

**Q:** How does uncertainty scale with sample size?
**A:** As **1/√n**. To halve the error bar you need **4×** the data. To shrink it 10×, **100×**.

**Q:** What is a p-value?
**A:** **P(data this extreme | H₀ is true)**. **NOT** the probability the hypothesis is true.

**Q:** What is the bootstrap and why is it so useful?
**A:** Resample with replacement → recompute the metric → take percentiles. It gives a CI for **any** metric (F1, BLEU, win-rate) with **no distributional assumptions**. Fifteen lines.

**Q:** Bias vs variance — how do you diagnose in 5 seconds?
**A:** Train **and** val both high → **bias** (underfitting). Train low, val high → **variance** (overfitting).

**Q:** Why use a *paired* test to compare two models?
**A:** They see the same test examples, so pairing removes example-difficulty variance — **far more statistical power**.

**Q:** What is p-hacking, and why is ML full of it?
**A:** Trying many variants and reporting the winner. With **40 configs at α=0.05, ~2 "win" by pure chance.**

**Q:** Can correlation be 0 for perfectly related variables?
**A:** **Yes** — ρ detects only **linear** relationships. y = x² has ρ ≈ 0. **Always plot your data.**

**Q:** What's wrong with "significant at p<0.05"?
**A:** Significance ≠ importance. With huge n, a worthless 0.01% effect is significant. **Report the effect size.**

**Q:** How should you report every metric?
**A:** **"87.9% ± 1.4% (95% CI, n=1000, 5 seeds)"** — value, interval, sample size, seed count.

**Q:** `np.std()` default, and why it's wrong for you?
**A:** `ddof=0` (population). For a **sample** use `ddof=1` — otherwise you **understate your uncertainty**.

---

## 06.7 · Optimization

**Q:** What problem does momentum solve?
**A:** **Zig-zagging in ravines** and stalling on plateaus/saddles. It accumulates a velocity: consistent gradients build up, oscillating ones cancel. → [06.7](../weeks/06.7-optimization.md)

**Q:** What problem does RMSProp solve?
**A:** One global learning rate can't suit all parameters. It divides each step by an **EMA of that parameter's recent squared gradients**.

**Q:** What is Adam?
**A:** **Momentum (1st moment) + RMSProp (2nd moment) + bias correction.** Three ideas, twelve lines.

**Q:** Why AdamW over Adam?
**A:** Adam's L2 penalty gets divided by √v along with the gradient, so heavily-updated params get *less* decay — backwards. AdamW **decouples** it. Standard for all LLMs.

**Q:** How much memory does Adam add?
**A:** Two extra copies of the parameters (m and v) → **3× total**. It's why fine-tuning needs far more VRAM than inference, and a **core motivation for LoRA**.

**Q:** Why is mini-batch better than both full-batch and single-sample?
**A:** Full batch is too slow; single-sample wastes the GPU. Mini-batch gets a good gradient estimate, saturates the hardware, **and its noise acts as a regularizer**.

**Q:** Why does gradient noise *help*?
**A:** It escapes sharp minima and saddles, biasing training toward **flat minima**, which generalize better.

**Q:** Why do Transformers need LR warmup?
**A:** Adam's second-moment estimate `v` is unreliable in the first steps, so full-size adaptive steps can **destabilize an untrained model**.

**Q:** Deep nets are non-convex — why does GD work?
**A:** Saddles vastly outnumber local minima in high dimensions (momentum escapes them), most minima are of **similar quality**, and overparameterization smooths the landscape.

**Q:** What's the most important hyperparameter?
**A:** The **learning rate**, by a wide margin. A well-tuned SGD beats a badly-tuned Adam.

**Q:** Linear scaling rule?
**A:** batch ×k → **LR ×k** (with warmup). Larger batches give less noisy gradients (noise ∝ 1/√B), so bigger steps are safe.

**Q:** Why does MSE fail with outliers?
**A:** Errors are **squared** — one 10× outlier contributes 100× the loss and dominates training. Use **Huber**.

---

## 06.8 · Information Theory

**Q:** Why is information $-\log p$?
**A:** Independent events' information must **add** while their probabilities **multiply** — and only the **logarithm** turns products into sums. → [06.8](../weeks/06.8-information-theory.md)

**Q:** What is entropy, in one phrase?
**A:** **Average surprise** — how uncertain/spread-out a distribution is. Max for uniform, zero for a point mass.

**Q:** What is cross-entropy loss for a one-hot target?
**A:** **−log(probability assigned to the correct class).**

**Q:** Why is cross-entropy the *right* loss?
**A:** **H(p,q) ≥ H(p), with equality iff q = p.** So minimizing it *is* making your model match reality. **A theorem, not a heuristic.**

**Q:** Why does cross-entropy punish confident wrongness so hard?
**A:** −log q → **∞** as q → 0. Being certain of a falsehood is infinitely bad — exactly the incentive you want. (And why `log(0)` = the classic NaN.)

**Q:** What is the gradient of softmax + cross-entropy w.r.t. the logits?
**A:** **`probs − onehot`.** Predicted minus actual. The softmax derivative **cancels exactly**.

**Q:** Why does `nn.CrossEntropyLoss` take logits, not probabilities?
**A:** It **fuses** softmax+CE for the simplified gradient **and** numerical stability (log-sum-exp). Applying softmax yourself applies it **twice** — a silent, common bug.

**Q:** Relationship between cross-entropy, entropy, and KL?
**A:** **CE(p,q) = H(p) + KL(p‖q).** Since H(p) is constant w.r.t. the model, minimizing CE ≡ minimizing KL — we just optimize the cheaper one.

**Q:** Is KL divergence a distance?
**A:** **No** — it's asymmetric. Forward KL is **mean-seeking** (covers all modes → blurry outputs); reverse KL is **mode-seeking** (collapses onto one → less diverse). The direction changes model behaviour.

**Q:** What is perplexity?
**A:** **e^(cross-entropy)** — "the model is effectively choosing among this many tokens." Only comparable across **identical tokenizers**.

**Q:** What role does KL play in RLHF?
**A:** A **leash**: `reward − β·KL(policy‖reference)` stops the model **reward-hacking** into gibberish. β is the leash length.

**Q:** Why use mutual information over correlation?
**A:** MI detects **any** dependence, not just linear. Correlation is ≈0 for y = x²; MI sees it perfectly.

**Q:** What do CLIP and SimCLR maximize?
**A:** A lower bound on the **mutual information** between two views (image/text, or two augmentations). **InfoNCE** — the basis of modern representation learning.

---

## 06.9 · Numerical Computing

**Q:** Why does `0.1 + 0.2 != 0.3`?
**A:** They aren't exactly representable in binary; the stored values are approximations. **Never compare floats with `==`** — use `np.allclose`. → [06.9](../weeks/06.9-numerical-computing.md)

**Q:** Why is **bfloat16** better than float16 for training?
**A:** It keeps float32's **8-bit exponent** (range up to 1e38) and sacrifices mantissa bits. **Deep learning needs RANGE far more than precision** — float16 maxes at 65,504 and overflows constantly.

**Q:** What is the softmax max-subtraction trick?
**A:** `z = z - z.max()` before `exp`. **Mathematically identical** (the factor cancels), but the largest exponent becomes e⁰=1 → **overflow impossible**. In every production softmax on Earth.

**Q:** Why do language models work in log space?
**A:** Multiplying 100 probabilities < 1 **underflows to exactly 0**. `log(∏p) = Σlog(p)` turns products into sums.

**Q:** What is log-sum-exp?
**A:** `max(x) + log(Σ exp(x − max(x)))` — a numerically stable way to compute `log(Σ exp(x))`.

**Q:** What is catastrophic cancellation?
**A:** Subtracting nearly-equal numbers destroys the significant digits. The naive variance formula `E[X²]−E[X]²` can return a **negative** number.

**Q:** Why is `keepdims=True` important?
**A:** Without it, a reduction collapses `(n,1)` → `(n,)`, and the next broadcast **silently produces an (n,n) outer operation** instead of an elementwise one — **with no error raised.**

**Q:** How much faster is vectorized NumPy than a Python loop?
**A:** **100–1000×.** Contiguous memory, no per-element boxing, SIMD, multithreaded BLAS.

**Q:** Broadcasting rules?
**A:** Compare shapes **from the right**; dimensions must be **equal, or one must be 1**.

**Q:** Loss is NaN — what do you check first?
**A:** Was it NaN **from step 0** (data/model bug: NaN input, log(0), div by 0) or **appeared later** (exploding gradients / overflow)? Then bisect by hooking layers.

**Q:** Why is one NaN in your dataset catastrophic?
**A:** NaN is **contagious** — it propagates through the gradient to **every weight in one step**, killing the whole model. `assert not np.isnan(X).any()`.

---

## 06.10 · Neural Networks

**Q:** Why is a nonlinearity mandatory?
**A:** Composition of linear maps **is linear** — 100 linear layers collapse to **one**. Without activations, depth buys you *nothing*. → [06.10](../weeks/06.10-neural-network-math.md)

**Q:** What are the four backward rules?
**A:** `Z=A@W` → `dW=A.T@dZ`, `dA=dZ@W.T`; `Z=A+b` → `db=dZ.sum(0)`; `A=f(Z)` → `dZ=dA*f'(Z)`; softmax+CE → `dZ=(P−Y)/B`. **Every backward pass is these four, composed.**

**Q:** Why is the bias gradient a **sum** over the batch?
**A:** The bias was **broadcast** across the batch in the forward pass. **Broadcast forward = sum backward.**

**Q:** Why can't you initialize all weights to zero?
**A:** Every neuron computes the same thing and gets the same gradient — **symmetry never breaks**. The network is effectively one neuron wide, forever.

**Q:** Why does training need 3–4× the memory of inference?
**A:** Every **forward activation must be cached** for the backward pass — plus gradients and optimizer state.

**Q:** What should an untrained 10-class classifier's loss be?
**A:** **ln(10) ≈ 2.303** (uniform output). For a 50,257-token LLM: **10.82**. **If it isn't, you have a bug before training a single step.**

**Q:** What is the dying ReLU problem?
**A:** A neuron stuck with negative pre-activation has gradient **exactly 0 forever** — it can never recover. Fix with Leaky ReLU or GELU.

**Q:** Why do Transformers use GELU instead of ReLU?
**A:** GELU is **smooth** with nonzero gradient everywhere — no hard kill switch, no dead neurons.

**Q:** How do you derive which term gets transposed in a gradient?
**A:** **Shape-matching.** The gradient must have the **same shape as the parameter** — only one arrangement of transposes produces it.

**Q:** Why gradient-check in float64?
**A:** float32's machine epsilon (~1e-7) is too coarse for a central difference with eps=1e-4 — cancellation gives **false failures**.

---

## 06.11 · Transformers

**Q:** Explain attention in one phrase.
**A:** A **soft, differentiable dictionary lookup** — score the query against every key, softmax, take a weighted average of the values. → [06.11](../weeks/06.11-transformer-math.md)

**Q:** What are Q, K, V?
**A:** Query ("what I want"), Key ("what I offer"), Value ("what I contribute") — all learned **linear projections of the same input** in self-attention.

**Q:** Why divide by **√d_k**?
**A:** The dot product of random d_k-dim vectors has **std √d_k**. Unscaled, large scores **saturate the softmax**, whose gradient then vanishes. Scaling restores unit variance. **A variance fix (probability), protecting a gradient (calculus), from a numerical saturation.**

**Q:** Shape of the attention score matrix, and why it matters?
**A:** **`(n, n)`** — this is the **O(n²)** term that makes long context expensive. Doubling context **quadruples** cost.

**Q:** The only difference between BERT's and GPT's attention?
**A:** The **causal mask**. GPT masks the future (autoregressive → can generate); BERT doesn't (bidirectional → understanding). **One triangular boolean matrix.**

**Q:** Why must masking happen *before* the softmax?
**A:** So masked weights become exactly 0 **and** the remaining weights still sum to 1. Masking after softmax **breaks normalization**.

**Q:** Why do Transformers need positional encoding?
**A:** Attention is **permutation-invariant** — without position, "the cat sat" and "sat cat the" are identical. **It's the price of trading RNN sequentiality for GPU parallelism.**

**Q:** What is RoPE and why did it win?
**A:** **Rotate** q and k by an angle proportional to position, so the score depends only on the **relative** distance (m−n). No extra params; extrapolates well. LLaMA/Mistral/Qwen. (Context-extension tricks = adjusting RoPE frequencies.)

**Q:** Why is multi-head attention **free**?
**A:** Each head uses `d_k = d_model/h` dimensions — h heads cost the **same total FLOPs** as one full-width head. Many relationship-detectors for the price of one.

**Q:** What are the two operations in a Transformer block?
**A:** `x + MHA(LN(x))`, then `x + FFN(LN(x))`. **Attention mixes information *across* tokens; the FFN processes each token *individually*.** (FFN ≈ 2/3 of all parameters.)

**Q:** Why are residual connections essential in a Transformer?
**A:** ∂(x+f(x))/∂x = **1** + f′(x) — a **gradient highway**. Without it, a deep Transformer simply will not train.

**Q:** What does FlashAttention change mathematically?
**A:** **Nothing.** Identical result, better memory access (tiling in SRAM, never materializing the n×n matrix). **The bottleneck was memory traffic, not FLOPs.**

---

## 06.12 · Reading Notation

**Q:** How do you read $\sum_j A_{ij}$?
**A:** "Sum over j, keeping i" → the **j axis disappears** → `A.sum(axis=1)`. **The summed index is the axis that vanishes.** → [06.12](../weeks/06.12-reading-notation.md)

**Q:** What should you think when you see **Π** in a paper?
**A:** **"Take the log."** Products of probabilities underflow; every Π becomes a **Σ of logs** in the implementation.

**Q:** What does typography tell you?
**A:** The **type**. Lowercase italic = scalar; **bold** lowercase = vector; capital = matrix; script = set; 𝔼 = expectation; **hat** = predicted; **bar** = mean.

**Q:** What does $x \in \mathbb{R}^{768}$ tell you?
**A:** The **shape** — `(768,)`. Papers hand you shapes for free and almost nobody reads them.

**Q:** Name four overloaded symbols.
**A:** **σ** (sigmoid *or* std dev), **α** (LR / Dirichlet / significance / LoRA scale), **λ** (regularization / eigenvalue / rate), **p** (probability / p-value / top-p).

**Q:** The three passes for reading a paper?
**A:** **Triage** (10 min: abstract, figures, conclusion) → **Method** (1 h: decode the core equation, skip proofs) → **Reimplement** (½ day).

**Q:** Which decoding step produces the real insight?
**A:** **The ablation** — "what breaks if I remove this term?" It tells you *why the term exists*, which is the only thing you'll actually remember.

**Q:** What's $\arg\max_x f(x)$?
**A:** The **x** that maximizes f — **not** the maximum value. (`np.argmax`, not `np.max`.)

**Q:** What should you do when stuck on a derivation?
**A:** **Skip it.** You need the result, not the proof. Come back only if the result surprises you.

**Q:** What does it mean if you're confused by a paper?
**A:** **That you're reading a paper.** Confusion is the process, not a verdict. A paper is a cleaned-up account of a messy process, *designed* to look inevitable.

---

## 🎯 The ten sentences (recall all ten cold)

**Q:** Name the ten sentences that carry modern AI.
**A:**
1. The **dot product measures alignment**.
2. A **matrix is a function**; matmul is composition → depth needs nonlinearity.
3. The **gradient points uphill**; step against it.
4. The **chain rule multiplies** → backprop, and vanishing/exploding gradients.
5. **Eigenvalues to the n-th power** → why residual connections exist.
6. **Real matrices are low-rank** → PCA, compression, LoRA.
7. **Variance must be controlled** → He init, layer norm, √d_k.
8. **Cross-entropy is surprise**; its gradient is predicted − actual.
9. **Products underflow — take the log.**
10. **Uncertainty shrinks as 1/√n.**

---

[⬆ Module 06](../README.md) · [📖 Lessons](../weeks/README.md) · [📄 Cheat sheet](../cheat-sheets/math-cheatsheet.md) · [📝 Quiz](../quizzes/quiz-01.md)
