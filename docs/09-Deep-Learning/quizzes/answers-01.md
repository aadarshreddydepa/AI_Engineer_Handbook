# ✅ Module 09 · Deep Learning — Quiz 01 Answers

[🏠 Module 09](../README.md) · [📝 Back to quiz](quiz-01.md)

> Each answer gives the **key point**, the **why**, and a **lesson link**. Grade on the reasoning, not the wording.

---

## Part A · Foundations

**1.** **Who builds the features.** Classical ML: a human hand-engineers features and the algorithm fits a boundary. Deep learning: the network **learns the features itself**, layer by layer, from raw data (representation learning). Everything else about DL follows from this one shift. → [09.1](../weeks/09.1-why-deep-learning.md)

**2.** $W_2(W_1\mathbf{x}+b_1)+b_2 = (W_2W_1)\mathbf{x} + (W_2b_1+b_2) = W'\mathbf{x}+b'$. The composition of affine maps is **one affine map**. So without a nonlinearity between them, any depth collapses to a single layer — **the activation function is the only reason depth adds power.** → [09.2](../weeks/09.2-neural-network-fundamentals.md)

**3.** **Vanishing gradients.** Sigmoid's derivative maxes at **0.25**; backprop multiplies one such factor per layer, so 0.25²⁰ ≈ 10⁻¹² — the early layers get no signal. **ReLU** (derivative exactly 1 when active) fixes it. → [09.2](../weeks/09.2-neural-network-fundamentals.md)

**4.** **≈ ln(10) ≈ 2.30.** An untrained softmax should output roughly uniform probabilities (1/10 each); the cross-entropy of a uniform prediction over C classes is ln(C). If your initial loss is far from this, you have a bug (bad init, wrong loss, label mismatch) *before* training even starts — the cheapest sanity check in DL. → [09.3](../weeks/09.3-math-of-neural-networks.md)

**5.** It isn't new — **backpropagation is just the chain rule applied right-to-left with the forward activations cached.** The only "invention" is the efficient ordering (reverse-mode autodiff). → [09.4](../weeks/09.4-backpropagation.md)

**6.** There is **one output** (the scalar loss) and **millions of inputs** (the weights). Reverse mode computes the derivative of one output w.r.t. all inputs in a **single backward pass**; forward mode would need one pass **per parameter**. Right-to-left is the cheap direction. → [09.4](../weeks/09.4-backpropagation.md)

**7.** **Shape-matching.** `dW` must have the same shape as `W`, say `(in, out)`. `A` is `(B, in)` and `dZ` is `(B, out)`. The only product of these two (with one transposed) that yields `(in, out)` is `A.T @ dZ` — `A.T` is `(in, B)`, `dZ` is `(B, out)`, giving `(in, out)`. The shapes force the arrangement. → [09.4](../weeks/09.4-backpropagation.md)

**8.** PyTorch **adds** each `backward()`'s gradients into `.grad` (this is what enables gradient accumulation). If you don't `zero_grad()` first, this iteration's gradient is contaminated by all previous ones → the update is wrong → training diverges. So every iteration: clear, then compute. → [09.4](../weeks/09.4-backpropagation.md) · [09.7](../weeks/09.7-autograd.md)

**9.** **Momentum** (exponential moving average of the gradient — the 1st moment — smooths the path), **RMSProp** (EMA of the squared gradient — the 2nd moment — gives each parameter its own effective learning rate), and **bias correction** (rescales both EMAs so they aren't biased toward zero in the first few steps). → [09.5](../weeks/09.5-optimization.md)

**10.** Adam folds L2 weight decay into the gradient, so it gets divided by √v — parameters with large gradients get *less* decay, which is backwards. **AdamW decouples** the decay: it applies the weight shrinkage **directly to the weights**, separately from the adaptive gradient step. This is why AdamW is the default for modern models. → [09.5](../weeks/09.5-optimization.md)

**11.** **Adam stores two extra copies of every parameter** (the first- and second-moment estimates m and v), roughly **3× the parameter memory** of inference, plus the activation cache for backprop. Inference has none of that. This is why the same model that serves fine OOMs when you fine-tune it — and a core motivation for LoRA. → [09.5](../weeks/09.5-optimization.md)

---

## Part B · PyTorch mechanics

**12.** (1) **A device** — it can live on a GPU, making matmuls ~100× faster. (2) **An autograd tape** — operations are recorded so `loss.backward()` computes all gradients automatically. Strip those two away and it's a NumPy array. → [09.6](../weeks/09.6-pytorch-tensors.md)

**13.** `X` and `y` come off the CPU DataLoader but the model is on `cuda` → **"Expected all tensors to be on the same device."** Fix: move **every batch** inside the loop: `X, y = X.to(device), y.to(device)`. (Move the model once at setup; move the data every iteration.) → [09.6](../weeks/09.6-pytorch-tensors.md)

**14.** `t[0]` is **99**. `torch.from_numpy` **shares the underlying memory** — no copy — so mutating the array mutates the tensor and vice versa. Use `torch.tensor(a)` when you want an independent copy. → [09.6](../weeks/09.6-pytorch-tensors.md)

**15.** GPU kernels are **asynchronous** — the Python line launches the work and returns immediately, before the GPU finishes. Without `synchronize()` you measure the *launch/queue* time, not the compute, and get absurdly fast (wrong) numbers. → [09.6](../weeks/09.6-pytorch-tensors.md)

**16.** **`torch.no_grad()`** stops the autograd graph from being built (saves memory/time, no gradients). **`model.eval()`** changes *layer behaviour* — turns dropout off and switches batchnorm to its stored running statistics. They're orthogonal: at inference you need **both** — `no_grad()` for efficiency and `eval()` for correct outputs. Running validation without `eval()` leaves dropout on and batchnorm using batch stats → noisy, wrong metrics. → [09.7](../weeks/09.7-autograd.md)

**17.** `losses.append(loss)` — `loss` is a tensor still attached to its **computational graph**, so each append keeps an entire forward graph alive; memory grows every iteration. Fix: `losses.append(loss.item())` (or `.detach()`). → [09.7](../weeks/09.7-autograd.md)

**18.** "Dynamic" means the graph is **built fresh on every forward pass, as the Python executes** — there's no separate compiled graph. The practical benefit: ordinary Python control flow (`if`, `for`, `print`, `pdb`) works inside the model, so it's trivially debuggable. That debuggability is why researchers adopted PyTorch. → [09.7](../weeks/09.7-autograd.md)

**19.** The layers are stored in a **plain Python list** (`self.blocks = [...]`), which `nn.Module` **cannot see**, so their parameters are missing from `.parameters()` — they're never handed to the optimizer, never trained, never moved to the GPU. Fix: **`self.blocks = nn.ModuleList([...])`**. → [09.8](../weeks/09.8-building-models.md)

**20.** **Training** on ordered data (e.g., all class-0 examples, then all class-1) produces batches that aren't representative → wildly biased gradients → unstable training; shuffling decorrelates them. **Validation** does no gradient updates, so order doesn't affect the metric; shuffling there only hurts reproducibility. → [09.9](../weeks/09.9-data-loading.md)

**21.** The GPU is **data-starved** — the DataLoader can't feed batches fast enough (single-process loading, heavy per-item transforms). First knob: **increase `num_workers`** (parallel loading), plus `pin_memory=True`. Confirm with `nvidia-smi` showing low GPU-Util. → [09.9](../weeks/09.9-data-loading.md) · [09.14](../weeks/09.14-performance.md)

**22.**
```python
optimizer.zero_grad()
loss.backward()
optimizer.step()
```
Clear old gradients, compute new ones, take the step. Every model on earth uses this exact trio. → [09.10](../weeks/09.10-training-loop.md)

**23.** You forgot **`model.train()`** at the top of the training phase, so the model is stuck in the `eval()` state from validation (dropout off, batchnorm frozen). The switches must be flipped **both** ways each epoch: `model.train()` before training, `model.eval()` before validation. → [09.10](../weeks/09.10-training-loop.md)

**24.** **Can the model overfit a single batch to ~100% accuracy / near-zero loss?** A correctly wired model+loop can memorize 64 examples trivially. Passing it rules out bugs in the **model architecture and the training loop** — it isolates the problem to data, regularization, or hyperparameters. → [09.10](../weeks/09.10-training-loop.md) · [09.15](../weeks/09.15-debugging.md)

---

## Part C · Architectures

**25.** (1) **Parameter explosion** — a single FC layer on a modest image is ~150M weights. (2) **No use of spatial structure** — flattening throws away which pixels are adjacent. (3) **The killer: no translation invariance** — the network must relearn "cat" separately for every position it could appear. Convolutions fix all three. → [09.11](../weeks/09.11-cnns.md)

**26.** **Weight sharing** = the *same* small filter is applied at **every spatial position**. It buys (1) **translation invariance** — a pattern is detected wherever it appears, by the same weights — and (2) a massive **parameter reduction** vs a fully-connected layer. → [09.11](../weeks/09.11-cnns.md)

**27.** **Early-layer features are generic.** The first layers learn edges, textures, and simple shapes that are useful for *any* vision task, so a network pretrained on ImageNet already "knows how to see." You reuse that and only train a small task-specific head — needing thousands, not millions, of labelled images. → [09.11](../weeks/09.11-cnns.md)

**28.** **Vanishing gradient across time.** Backpropagation-through-time multiplies the recurrent weight matrix at every timestep; the gradient to far-back steps scales like **λⁿ** — the same λⁿ that causes vanishing/exploding gradients across *depth*, here across *time*. If λ < 1 the signal dies within ~10 steps. → [09.12](../weeks/09.12-sequence-models.md)

**29.** **The protected cell state** — a nearly-linear "conveyor belt" along which information flows with minimal multiplication, guarded by learned gates that decide what to add or remove. It protects the long-range gradient from the λⁿ decay, extending usable memory to hundreds of steps. → [09.12](../weeks/09.12-sequence-models.md)

**30.** (1) **Attention gives a direct path between any two positions**, so it handles arbitrarily long-range dependencies. (2) **Attention is parallelizable** — all positions are processed in one matmul, whereas an RNN must process step *t* only after *t−1*. The **parallelism** was the decisive one: it let Transformers fully use the GPU and scale to enormous datasets. → [09.12](../weeks/09.12-sequence-models.md)

**31.** You forgot to **pack** the sequences (`pack_padded_sequence`). Without it the LSTM treats the padding tokens as real input, updating and contaminating the hidden state with meaningless steps. Packing tells the LSTM exactly where each real sequence ends. → [09.12](../weeks/09.12-sequence-models.md)

---

## Part D · Regularization, performance, debugging, production

**32.** **Overfitting** (large train–val gap). First reaches: **more data / data augmentation** (the strongest regularizer), then **dropout** and/or **weight decay** (AdamW), plus **early stopping**. The diagnostic itself is unchanged from [08.2](../../08-Machine-Learning/weeks/08.2-ml-workflow.md). → [09.13](../weeks/09.13-regularization.md)

**33.** **Training:** batchnorm normalizes using the **current batch's** mean/variance and updates a running estimate. **Evaluation:** it uses the **stored running statistics** (so a single test example gets a consistent, batch-independent result). The call that switches them is **`model.eval()` / `model.train()`** — forgetting `eval()` makes predictions depend on whatever else is in the batch. → [09.13](../weeks/09.13-regularization.md)

**34.** **LayerNorm normalizes per-example across features and is independent of batch size**, whereas BatchNorm's statistics come from the batch. Transformers process variable-length sequences with small/uneven batches where batch statistics are unreliable, so LayerNorm is the natural fit. → [09.13](../weeks/09.13-regularization.md)

**35.** **Mixed precision** runs the heavy matmuls in half precision (float16/bfloat16) on Tensor Cores while keeping a float32 master copy where precision matters. It's ~free because GPUs do half-precision matmul roughly 2× faster and at half the memory with negligible accuracy loss. **bfloat16** is preferred because it keeps float32's **exponent range** (float16 overflows/underflows easily); it trades mantissa bits, not range. → [09.14](../weeks/09.14-performance.md)

**36.** **Sum gradients over several mini-batches and call `optimizer.step()` once**, simulating a large batch that wouldn't fit in memory (divide the loss by the number of accumulation steps). It solves the "I need a big batch size but the GPU can't hold it" problem. → [09.14](../weeks/09.14-performance.md)

**37.** **Exploding gradients.** A NaN appearing right after a loss spike means a gradient blew up and overflowed. Standard fixes: **gradient clipping** (`clip_grad_norm_(params, 1.0)`), lower the learning rate, and/or add warmup. → [09.15](../weeks/09.15-debugging.md)

**38.** `torch.save(model, ...)` pickles the **class definition and its import path**, so the checkpoint breaks if you rename or move the model class. The **`state_dict`** is just a portable dictionary of tensors that loads into any compatible architecture — the robust, recommended format. → [09.16](../weeks/09.16-saving-loading.md)

**39.** `torch.load` uses **pickle**, which can execute **arbitrary code** during unpickling — a malicious `.pt` file can run anything on your machine (RCE). Safe alternative: load with **`weights_only=True`**, or use the **safetensors** format for anything you didn't produce yourself. → [09.16](../weeks/09.16-saving-loading.md)

**40.** **False.** Deep learning **added a new kind of model, not a new discipline.** Input monitoring, prediction-distribution canaries, versioning data/models/code, retraining gates, and evaluation methodology all carry over **unchanged** from [Module 08](../../08-Machine-Learning/weeks/08.17-production-ml.md). The network got deeper; the operational scaffolding did not. → [09.17](../weeks/09.17-production.md)

---

## 🎁 Bonus answers

**B1.** **`torch.allclose(my_numpy_grad, torch_param.grad)`** (returning `True`). That single assertion is the whole thesis of the module made concrete: PyTorch's `loss.backward()` is computing **exactly the same chain-rule gradients you derived by hand in 09.4** — autograd is your hand-written `backward()`, automated, and the equality proves you understand what the abstraction is doing. → [09.7](../weeks/09.7-autograd.md)

**B2.** (1) **You forgot `model.eval()`** — dropout is still active and/or batchnorm is using batch statistics at inference, so predictions are noisy/wrong. (2) **A preprocessing mismatch** — the production input isn't normalized/resized/tokenized the same way as training (train/serve skew). Both are one-liners; both are classic "trained fine, serves garbage" causes. → [09.10](../weeks/09.10-training-loop.md) · [09.17](../weeks/09.17-production.md)

**B3.** Training memory (~80 GB) holds, for a 7B model: the **weights** (~14 GB in fp16), the **Adam optimizer state** — m and v, two more copies (~28 GB, often in fp32), the **gradients** (~14 GB), and the **cached activations** for backprop (batch- and sequence-length-dependent, often the largest single term). **Serving** keeps only the **weights** (~14 GB) — no optimizer state, no gradients, no activation cache — which is why inference fits on far smaller hardware than training. → [09.5](../weeks/09.5-optimization.md) · [09.17](../weeks/09.17-production.md)

---

**Scoring:** 36–40 outstanding · 32–35 solid (module complete) · 26–31 review the linked lessons · <26 re-read 09.4, 09.7, and 09.10 — the load-bearing three.

[📝 Back to quiz](quiz-01.md) · [🧠 Flashcards](../flashcards/deck.md) · [📖 Lessons](../weeks/README.md)
