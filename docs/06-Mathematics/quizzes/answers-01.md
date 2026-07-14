# ✅ Answers · Module 06 Quiz 01

[🏠 Module 06](../README.md) · [❓ Questions](quiz-01.md)

> Model answers **with the reasoning**. If you got the gist but not the *why*, reread the linked lesson — and run the code.

---

## Part 1 — Thinking & Linear Algebra

**1.** Symbols → **shapes** → read aloud → **shrink to a tiny case** → implement in NumPy → **ablate ("what breaks if I remove this term?")** → plain English. **The ablation is where the insight lives** — it tells you *why* a term exists, which is the only part you'll remember. (It's how you'd derive the √d_k yourself.) → [06.1](../weeks/06.1-mathematical-thinking.md)

**2.** The dot product measures **alignment** — how much two vectors point the same way. It appears in: **cosine similarity/RAG**, **attention scores** (QKᵀ), **a single neuron** (w·x + b), and **logits** (hidden state against each class vector). → [06.2](../weeks/06.2-linear-algebra-vectors-matrices.md)

**3.** `(m,k) @ (k,n) → (m,n)` — **inner dimensions must match and vanish; outer survive.** So: `X @ W.T` → `(32,768) @ (768,3072)` → `(32,3072)`. PyTorch stores `nn.Linear(in,out).weight` as `(out,in)` and computes `x @ W.T + b`; forgetting this causes half of all shape errors. → [06.2](../weeks/06.2-linear-algebra-vectors-matrices.md)

**4.** Cosine **divides out magnitude**, which in text tracks length/verbosity rather than meaning — a document that says the same thing twice as emphatically shouldn't win for being longer. **The production trick: pre-normalize every vector to unit length offline.** Then the denominator is 1, cosine *becomes* the plain dot product, and search is a single matmul with no divisions. Every vector DB does this. → [06.2](../weeks/06.2-linear-algebra-vectors-matrices.md)

**5.** det = 0 · not full rank · has a zero **eigenvalue** · has a zero **singular value** · not invertible · **collapses space to a lower dimension**. **The one picture: the plane got squashed onto a line, and you cannot un-squash it** — two different inputs now map to the same output, so no function can send them back. → [06.3](../weeks/06.3-linear-algebra-decomposition.md)

**6.** **Every matrix is rotate (Vᵀ) → stretch by singular values (Σ) → rotate (U).** Eckart–Young guarantees that truncating to the top-k singular values gives the **provably best possible rank-k approximation** — no other rank-k matrix gets closer. Resting on it: **PCA, data/model compression, LSA/recommenders, and the intuition behind LoRA**. → [06.3](../weeks/06.3-linear-algebra-decomposition.md)

**7.** $W_{\text{new}} = W + BA$ where B is `(d,r)`, A is `(r,d)`, r ≪ d (8–64) — so **ΔW has rank ≤ r**. The claim is that everything fine-tuning needs to change lives in an r-dimensional subspace, and empirically it does → **256× fewer trainable params**.
- **B = 0 at init** so that BA = 0 → **the adapted model starts identical to the base model** and is perturbed gently. Random init would inject noise into a working model before training began.
- **`B @ (A @ x)`**: `(A @ x)` is an 8-element vector — cheap. `(B @ A)` would materialize a full `(4096,4096)` matrix. **Same answer, wildly different cost** (matmul associativity doing real work). → [06.3](../weeks/06.3-linear-algebra-decomposition.md)

**8.** The spectrum **decays sharply after 3 components** → the data has **low intrinsic dimensionality**; most of those dimensions are noise or redundancy. **Do:** truncate to ~3–5 components (PCA), compress, or use a low-rank method. The fast decay *is* the reason compression works — random data has a flat spectrum. → [06.3](../weeks/06.3-linear-algebra-decomposition.md)

---

## Part 2 — Calculus & Optimization

**9.** The gradient points **uphill** (steepest ascent) — so to minimize you step **against** it. `∇_W L` has **exactly the same shape as W**. That's what lets you derive transposes by **shape-matching**: `∂L/∂W₂` must be `(h,c)`, and the only way to build that from `A₁ (B,h)` and `δ₂ (B,c)` is `A₁ᵀ δ₂`. → [06.4](../weeks/06.4-calculus.md)

**10.** Backprop is **the chain rule applied right-to-left**, with forward activations cached. **Reverse mode** because there is **one output (the loss) and billions of inputs (weights)** — reverse mode gets *all* gradients in **one** pass. Forward mode costs one pass **per parameter**: **7 billion forward passes per step** for a 7B model. **The key insight is computational, not mathematical.** → [06.4](../weeks/06.4-calculus.md)

**11.** `0.25^10 ≈ 1e-6`. **The chain rule multiplies per-layer derivatives**, so ten sigmoid layers annihilate the gradient and the early layers never learn. **ReLU's derivative is exactly 1 when active** — multiply by 1 as often as you like and nothing shrinks. **ReLU won because of its derivative.** → [06.4](../weeks/06.4-calculus.md)

**12.** $\frac{\partial}{\partial x}(x + f(x)) = \mathbf{1} + f'(x)$. **That leading 1 is a gradient highway**: no matter how many layers you stack, the gradient always has an unmultiplied path back to every earlier layer, so it can never be fully annihilated. This is why ResNets reached 152 layers and why every Transformer block is `x + attn(x)`, `x + mlp(x)`. → [06.4](../weeks/06.4-calculus.md)

**13.** **Saddle points.** For a critical point to be a local **minimum**, *all* n Hessian eigenvalues must be positive — astronomically unlikely when n is 7 billion. Overwhelmingly, random critical points have **mixed-sign eigenvalues** = saddles. This overturned decades of folk wisdom, and it's why **momentum** (which carries velocity through flat regions) matters so much. → [06.4](../weeks/06.4-calculus.md)

**14.** **Adam = Momentum + RMSProp + bias correction.**
- **Momentum** (1st moment): fixes **ravine zig-zag** and stalling on plateaus/saddles — consistent gradients accumulate, oscillating ones cancel.
- **RMSProp** (2nd moment): fixes "**one LR can't suit every parameter**" — per-parameter scaling by an EMA of squared gradients.
- **Bias correction**: both moments start at 0, biasing early estimates toward zero. Dividing by (1−βᵗ) undoes it — matters most in the fragile first ~100 steps.

**Memory: 3× the parameters** (w + m + v). For 7B in fp32: 28 GB weights + **56 GB optimizer state**, while *inference* needs only ~14 GB. **The optimizer state, not the model, is what doesn't fit — and that is the core motivation for LoRA.** → [06.7](../weeks/06.7-optimization.md)

**15.** Adam's **second-moment estimate `v` is built from almost no data at step 0** and is therefore unreliable — so the adaptive per-parameter step sizes are erratic and can destroy an untrained model instantly. Warmup (linearly ramping the LR over ~2000 steps) gives `v` time to become a sensible estimate. **It's a statistics fix for an optimizer's cold-start problem**, and it is not optional for Transformers. → [06.7](../weeks/06.7-optimization.md)

---

## Part 3 — Probability, Statistics, Information

**16.** $$P(w_1,\dots,w_T) = \prod_{t=1}^{T} P(w_t \mid w_{<t})$$ An LLM estimates **P(next token | all previous tokens)** — a categorical distribution over the vocabulary. **Prompt engineering is choosing the conditioning variables — literally, choosing what goes after the `|`.** RAG, few-shot examples, system prompts, and chain-of-thought are all conditioning strategies. → [06.5](../weeks/06.5-probability.md)

**17.** **Under 1%** (≈0.98%). Of 10,000 people, ~1 has the disease and tests positive — but ~100 *healthy* people also test positive (1% false-positive rate on 9,999). So of ~101 positives, only 1 is real.
**The ML lesson: accuracy is a lie on imbalanced data.** Your "99% accurate" fraud detector on a 0.1% fraud rate produces overwhelmingly false alarms. **This is why you report precision and recall, not accuracy** — and why "my model is 99% accurate" should always be met with "what's the class balance?" → [06.5](../weeks/06.5-probability.md)

**18.** **Temperature divides the logits before the softmax.** Low T amplifies the gaps between logits → the distribution **sharpens** toward argmax (deterministic, safe, repetitive). High T shrinks the gaps → **flattens** (creative, diverse, more errors).
**Top-p beats top-k because it adapts to the *shape* of the distribution**: when the model is certain ("capital of France is ___"), the nucleus contains one token and sampling is effectively greedy; when it's uncertain ("Once upon a ___"), the nucleus is wide. Top-k always keeps exactly k — cutting off good options when the model is unsure, and admitting garbage when it's sure. → [06.5](../weeks/06.5-probability.md)

**19.** **Latency is right-skewed** — a tall cluster of fast requests and a long tail of slow ones. **The mean sits in the empty space between them and describes no actual user.** Report **p50 / p95 / p99**. Your p99 is where your SLA lives and dies, and LLM serving is *brutally* skewed (long prompts, long generations, cold starts). → [06.6](../weeks/06.6-statistics.md)

**20.** **Uncertainty ∝ σ/√n — it shrinks as 1/√n, not 1/n.** To **halve** the error bar you need **4× the data**; to shrink it 10×, **100×**. **A 500-example eval set has an error bar of roughly ±4 percentage points** — it cannot resolve a 2% difference between models, no matter how carefully you run it. **The square root is the tax on all empirical knowledge.** → [06.6](../weeks/06.6-statistics.md)

**21.** **Almost certainly not, on this evidence.** Run:
1. **Bootstrap 95% CI** on each → B's interval is roughly [85.9%, 89.9%], which **contains A's 87.2%**.
2. **Paired** significance test (same test set → always pair; it's far more powerful).
3. **Permutation test** for an assumption-free check.
4. **How many seeds?** Seed variation alone often spans ±1%.
5. **How many configs did you try?** 40 configs at α=0.05 → ~2 false winners by chance.
6. **Effect size vs. cost:** is 0.7% worth the added complexity/latency even if real?

**A 0.7pp difference on 1000 examples is consistent with noise.** You'd need ~10,000+ examples to resolve it. → [06.6](../weeks/06.6-statistics.md)

**22.** For a one-hot target, $p_c = 1$ for the correct class and 0 elsewhere, so the sum collapses:
$$H(p,q) = -\sum_c p_c \log q_c = \boxed{-\log q_{\text{correct}}}$$
**Why it's the right loss (the theorem): $H(p,q) \ge H(p)$, with equality *if and only if* q = p.** So **"minimize cross-entropy" and "make your model match reality" are the same instruction.** It's not a heuristic — it's provable. It also explains the behaviour: −log q → ∞ as q → 0, so **being confidently wrong is punished nearly infinitely**, which is exactly the incentive you want (and why `log(0)` is the classic NaN). → [06.8](../weeks/06.8-information-theory.md)

**23.** $$\frac{\partial L}{\partial z} = \boxed{q - p} \quad\text{— predicted minus actual. One subtraction.}$$
The softmax's derivative **cancels exactly**. `nn.CrossEntropyLoss` takes **logits** for **two** reasons:
1. **Mathematical:** it fuses softmax+CE to use this simplified gradient.
2. **Numerical:** it computes `log_softmax` in one stable kernel (max-subtraction + log-sum-exp), never materializing a probability that could be exactly 0.

**Applying softmax yourself and then calling `CrossEntropyLoss` applies softmax twice** — silently flattening your distribution, wrecking training, and raising no error. → [06.8](../weeks/06.8-information-theory.md) + [06.9](../weeks/06.9-numerical-computing.md)

---

## Part 4 — Numerical, Networks, Transformers

**24.** **The exponent bits.** Both are 16 bits, but they spend them differently:
- **float16**: 5 exponent bits, 10 mantissa → max value **65,504**. Gradients and activations routinely exceed it → **constant overflow**, requiring loss-scaling hacks.
- **bfloat16**: **8 exponent bits** (same as float32) → range **1e±38**, with only ~7 mantissa bits.

**Deep learning needs RANGE far more than PRECISION** — gradients span many orders of magnitude, and nobody cares whether a weight is 0.13 or 0.131. **That single insight is why bf16 is in every TPU and modern GPU, and why nearly every LLM trains in it.** → [06.9](../weeks/06.9-numerical-computing.md)

**25.**
1. **Subtract the max before softmax** (`z = z - z.max()`) → prevents **`exp` overflow**. Mathematically a no-op (the factor cancels); numerically essential. In every production softmax on Earth.
2. **Log-sum-exp** (`max(x) + log Σ exp(x − max(x))`) → prevents overflow when computing `log Σ exp(x)`.
3. **Work in log space** (`log ∏ p = Σ log p`) → prevents **underflow** when multiplying many probabilities. **Every language model, HMM, and likelihood computation does this.**

(Honourable mention: `eps` in every denominator, preventing division by ~0.) → [06.9](../weeks/06.9-numerical-computing.md)

**26.** $$Z_2 = (XW_1 + b_1)W_2 + b_2 = X\underbrace{(W_1W_2)}_{W'} + \underbrace{(b_1W_2 + b_2)}_{b'} = XW' + b'$$
**A stack of 100 linear layers collapses into ONE linear layer** — the composition of linear maps is linear. **Consequence: without a nonlinearity, a 100-layer network has exactly the expressive power of logistic regression.** The activation is not a detail — **it is the entire reason depth buys you anything.** → [06.10](../weeks/06.10-neural-network-math.md)

**27.** An untrained C-class classifier should output a **uniform** distribution → loss = **−log(1/C) = ln(C)**. For 10 classes: **ln(10) = 2.303**. You got **6.9 ≈ ln(1000)** — so **the model is effectively distributing over ~1000 classes, not 10.** Likely causes: wrong `num_classes` in the output layer, a label/logit mismatch, or a bug in the loss.
**The `ln(C)` check is the cheapest bug-catcher in deep learning — print it every single time.** → [06.10](../weeks/06.10-neural-network-math.md)

**28.** $$\text{Attention}(Q,K,V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$$
**Why √d_k:** the dot product of two random d_k-dimensional vectors has **variance d_k**, hence **std √d_k** ([06.5](../weeks/06.5-probability.md) probability). Unscaled, scores reach ±8 at d_k=64 — which **saturates the softmax**, driving one weight to ~1 and the rest to ~0 ([06.9](../weeks/06.9-numerical-computing.md) numerical). **A saturated softmax has near-zero gradient** ([06.4](../weeks/06.4-calculus.md) calculus), so **training stalls.** Dividing by √d_k restores unit variance.

**Three lessons converging on one square root.** That's what it looks like when mathematics is load-bearing — the code shows you `/ math.sqrt(d_k)` but never tells you that removing it kills your model. → [06.11](../weeks/06.11-transformer-math.md)

**29.** **The causal mask.** GPT masks the future (lower-triangular → autoregressive → *can generate*); BERT doesn't (bidirectional → *understanding*, useless for generation). **One triangular boolean matrix is the entire architectural difference.**

**The mask must be applied to the *scores*, before the softmax** (setting them to −1e9): that way the masked weights become **exactly 0** *and* **the remaining weights still sum to 1**. Masking *after* the softmax leaves the weights unnormalized. The mask is also what makes $P(w_t \mid w_{<t})$ well-defined — without it, the model would trivially "predict" the next token by looking at it. → [06.11](../weeks/06.11-transformer-math.md)

**30.** $QK^\top$ is `(n,d) @ (d,n) → (n,n)` — **the attention matrix is n × n**, so compute and memory scale as **O(n²·d)**. **Doubling the context quadruples the cost** (32k context ≈ 1 billion score entries).

Three attacks:
1. **FlashAttention** — ✅ **changed NOTHING mathematically.** Identical result, computed by tiling in SRAM so the n×n matrix is never materialized. 2–4× faster and far more memory-efficient. **The bottleneck was memory traffic, not FLOPs** — a pure memory-hierarchy win.
2. **Sparse / sliding-window attention** — don't attend to everything (Mistral).
3. **Linear attention / state-space models (Mamba)** — reorder the matmuls or abandon attention for an O(n) recurrence.

(Also: **MQA/GQA** shrink the *KV cache*, the real bottleneck at inference.) → [06.11](../weeks/06.11-transformer-math.md)

---

## 🏁 Bonus

**B1 — Residual connections through three lessons:**
- **Calculus** ([06.4](../weeks/06.4-calculus.md)): $\partial(x + f(x))/\partial x = \mathbf{1} + f'(x)$ — a gradient path with factor 1.
- **Linear algebra** ([06.3](../weeks/06.3-linear-algebra-decomposition.md)): backprop through n layers raises the Jacobian's **eigenvalues to the n-th power**; only λ≈1 survives depth. The identity term pushes eigenvalues toward 1.
- **Architecture** ([06.11](../weeks/06.11-transformer-math.md)): this is why ResNets reached 152 layers and why **every Transformer block** is `x + attn(x)`, `x + mlp(x)`. **Without residuals, a deep Transformer will not train at all.**

**B2 — Reading a new paper:**
- **Next 10 min (triage):** title, abstract, **all figures and captions**, conclusion. Answer: what problem, what claim, is it relevant to me? **Most papers stop here — that's triage, not failure.**
- **Next hour (method):** find **the core equation** (there's almost always one). Run all 7 decoding steps: symbols → shapes (the paper often *gives* them: $W \in \mathbb{R}^{d\times k}$) → read aloud → shrink to n=2 → implement in NumPy → **ablate each term** → plain English. **Skip the proofs; read the ablation table instead.**
- **Next day (reimplement):** build the core idea. **Reading creates a reliable illusion of understanding; implementation destroys it.** Ask, for every design choice: *why this and not the obvious alternative?* → [06.12](../weeks/06.12-reading-notation.md)

**B3 — The ten sentences:**
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

> [!TIP]
> **Turn every missed question into a flashcard.** And for anything in Parts 2–4 that you fumbled: **don't reread — reimplement.** Write the gradient, gradient-check it, plot the failure mode. Mathematics is the one subject where you can verify your own understanding, and a gradient check is worth more than any answer key.

---

[❓ Questions](quiz-01.md) · [🧠 Flashcards](../flashcards/deck.md) · [📄 Cheat sheet](../cheat-sheets/math-cheatsheet.md) · [🏠 Module 06](../README.md)
