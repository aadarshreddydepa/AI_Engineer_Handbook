# 🧠 Module 09 · Deep Learning — Flashcard Deck

[🏠 Module 09](../README.md) · [📖 Lessons](../weeks/README.md) · [📄 Cheat sheet](../cheat-sheets/dl-cheatsheet.md)

> **~85 cards.** Cover the answer, say it out loud, *then* check. ⭐ marks the ones that will actually save you in production.

---

## 09.1 · Why Deep Learning?

**Q:** ⭐ What's the ONE thing deep learning changed? → **A:** **Who builds the features.** Classical ML: you hand-engineer them. Deep learning: the **network learns them, layer by layer**, from raw data. → [09.1](../weeks/09.1-why-deep-learning.md)

**Q:** What is representation learning? → **A:** Each layer transforms the data into a form where the next layer's job is easier — **edges → textures → parts → objects** — until a simple linear boundary suffices.

**Q:** ⭐ Why does transfer learning work? → **A:** **Early-layer features are generic** (edges/textures work for any vision task). You reuse a pretrained network's early layers and train on a **fraction of the data.**

**Q:** State the universal approximation theorem + its catches. → **A:** A big-enough net can approximate any function. **But: "enough" may be astronomical; existence ≠ learnability; fitting ≠ generalizing.** Depth (not width) makes it practical.

**Q:** ⭐ When does deep learning LOSE to classical ML? → **A:** **On tabular data.** Gradient boosting still wins — faster, cheaper, no GPU, interpretable. DL's home turf is **perception and language.**

**Q:** Why did DL explode in 2012? → **A:** **Data** (ImageNet) + **compute** (GPUs) + tricks (ReLU, dropout). The ideas were from the 1980s; the fuel was new.

---

## 09.2 · Neural Network Fundamentals

**Q:** What is an artificial neuron? → **A:** A **dot product + bias through a nonlinearity**: $\sigma(\mathbf{w}\cdot\mathbf{x}+b)$. Its **weights ARE the pattern it detects.** → [09.2](../weeks/09.2-neural-network-fundamentals.md)

**Q:** ⭐ What is a neural network layer, computationally? → **A:** **One matrix multiplication + a bias + an elementwise activation.** That's why >90% of a network's FLOPs are matmuls, and why networks run on GPUs.

**Q:** ⭐ Prove you need an activation function. → **A:** A stack of Linear layers with no nonlinearity **collapses to a single Linear layer** ($W_2(W_1x+b_1)+b_2 = W'x+b'$). Without activations, 100 layers = logistic regression. **The nonlinearity is the only reason depth helps.**

**Q:** Why did ReLU win over sigmoid for hidden layers? → **A:** Backprop multiplies per-layer derivatives. **Sigmoid's maxes at 0.25** (0.25¹⁰ ≈ 10⁻⁶ → vanishing); **ReLU's is exactly 1 when active** → nothing vanishes.

**Q:** What is the dying ReLU problem? → **A:** A neuron stuck negative outputs 0 with gradient **0 forever** — never recovers. Fix: Leaky ReLU/GELU.

**Q:** How do you choose the output layer? → **A:** Regression: 1, no activation, MSE. Binary: 1, sigmoid, BCE. Multi-class: k, softmax, cross-entropy.

---

## 09.3 · The Math

**Q:** What does "affine" mean? → **A:** Linear transformation **+ a shift** ($Wx+b$). The bias is the shift. "Linear"/"dense"/"fully-connected" all name it. → [09.3](../weeks/09.3-math-of-neural-networks.md)

**Q:** ⭐ Why does `CrossEntropyLoss` take logits, not probabilities? → **A:** It **fuses softmax+log+NLL** for **numerical stability** (log-sum-exp, no `log(0)`) and the clean `predicted − actual` gradient. **Applying softmax yourself applies it twice** and silently wrecks training.

**Q:** What's the binary equivalent? → **A:** **`BCEWithLogitsLoss`** (fuses sigmoid+BCE), not `BCELoss`. Rule: **model outputs logits; the loss applies the final activation.**

**Q:** ⭐ What should an untrained C-class classifier's loss be? → **A:** **≈ ln(C)** (uniform output). ln(10) ≈ 2.30. **If it isn't, you have a bug before training** — the cheapest sanity check in DL.

**Q:** How do you read `RuntimeError: shapes cannot be multiplied (32x784 and 256x10)`? → **A:** **Inner dimensions don't match** (784 ≠ 256) — you skipped a layer or transposed something. Print `.shape`.

---

## 09.4 · Backpropagation

**Q:** ⭐ What is backpropagation? → **A:** The **chain rule applied right-to-left**, with forward activations **cached**. Not a new algorithm — the only clever part is the ordering (reverse mode gets all gradients in one pass). → [09.4](../weeks/09.4-backpropagation.md)

**Q:** Why right-to-left (reverse mode)? → **A:** One output (loss), millions of inputs (weights). Reverse mode = **one pass total**; forward mode = one pass **per parameter** (billions).

**Q:** ⭐ What are the four backward rules? → **A:** `Z=A@W` → `dW=A.T@dZ`, `dA=dZ@W.T`; `Z=A+b` → `db=dZ.sum(0)`; `A=f(Z)` → `dZ=dA*f'(Z)`; softmax+CE → `dZ=(p−y)/B`.

**Q:** How do you derive which term gets transposed? → **A:** **Shape-matching** — the gradient must have the same shape as the parameter; only one arrangement produces it.

**Q:** ⭐ What is gradient checking + its two gotchas? → **A:** Comparing the analytical gradient to a central finite difference — the unit test for backprop. **Gotchas: use float64** (float32 eps too coarse), and **never during training** (two forward passes per parameter).

**Q:** ⭐ Why does PyTorch accumulate gradients? → **A:** `backward()` **adds** to `.grad`. Without `zero_grad()`, they pile up → explode → NaN. The accumulation enables **gradient accumulation** (big effective batch).

**Q:** Why does training use ~3–4× the memory of inference? → **A:** Every forward **activation must be cached** until backprop consumes it. Inference throws them away.

---

## 09.5 · Optimization

**Q:** What are backprop's and the optimizer's separate jobs? → **A:** **Backprop computes the gradient; the optimizer decides what to do with it.** → [09.5](../weeks/09.5-optimization.md)

**Q:** ⭐ What is Adam? → **A:** **Momentum (1st moment) + RMSProp (2nd moment) + bias correction.** Twelve lines. It trained GPT.

**Q:** ⭐ Why AdamW over Adam? → **A:** Adam's L2 penalty gets divided by √v (heavily-updated params get less decay — backwards). **AdamW decouples the decay.** The default for every modern model.

**Q:** ⭐ How much memory does Adam add? → **A:** **Two extra copies of every parameter (m, v) → 3× total.** Why fine-tuning OOMs while inference fits, and a core reason for LoRA.

**Q:** ⭐ What's the #1 hyperparameter? → **A:** **The learning rate**, by a wide margin. A well-tuned SGD beats a badly-tuned Adam.

**Q:** Why do Transformers need LR warmup? → **A:** Adam's second-moment estimate is unreliable in the first steps; full-size adaptive steps can destabilize an untrained model.

---

## 09.6 · PyTorch Tensors

**Q:** ⭐ What does a tensor add to a NumPy array? → **A:** **A device** (GPU → ~100× faster matmul) and **an autograd tape** (`loss.backward()` is free). Everything else is NumPy. → [09.6](../weeks/09.6-pytorch-tensors.md)

**Q:** ⭐ The #1 PyTorch runtime error and its fix? → **A:** *"Expected all tensors on the same device."* Fix: move the **model once** at setup and **every batch inside the loop** (`X.to(device)`).

**Q:** ⭐ Why does `torch.from_numpy` cause silent bugs? → **A:** It **shares memory** (no copy) — mutating the array mutates the tensor. Use `torch.tensor(a)` for a copy.

**Q:** Why train in bfloat16, not float16? → **A:** float16 has a **tiny range** (overflows); **bfloat16 keeps float32's range** and drops precision. Why every LLM trains in bf16.

**Q:** ⭐ Why does timing GPU code need `torch.cuda.synchronize()`? → **A:** GPU ops are **asynchronous** — the Python line returns before the GPU finishes. Without a sync you time the *queuing*, not the *work*.

---

## 09.7 · Autograd

**Q:** ⭐ What is autograd? → **A:** A tape recorder: ops on `requires_grad` tensors are recorded; `backward()` walks the graph applying the chain rule. **It's the `backward()` you wrote in 09.4, automated.** → [09.7](../weeks/09.7-autograd.md)

**Q:** ⭐ Why is PyTorch's graph "dynamic," and why did that make it win? → **A:** Built **fresh each forward pass, as your Python runs.** So real Python `if`/`for`/`print`/`pdb` work — it's just code, no separate graph to compile. Researchers adopted it for the debuggability.

**Q:** ⭐ `model.eval()` vs `torch.no_grad()`? → **A:** **`no_grad()`** stops graph-building (memory); **`model.eval()`** switches dropout off + batchnorm to running stats (behaviour). **Need BOTH at inference** — forgetting `eval()` corrupts validation metrics.

**Q:** ⭐ The #1 way to leak memory in PyTorch? → **A:** **Appending un-detached tensors** (`losses.append(loss)`) — each keeps its whole graph alive. Fix: **`.item()`** or `.detach()`.

**Q:** The training-loop ritual? → **A:** **`zero_grad()` → `backward()` → `step()`.**

---

## 09.8 · Building Models

**Q:** How do you read any PyTorch model? → **A:** **`__init__` is the parts list**, **`forward` is the wiring.** Every model is these two methods. → [09.8](../weeks/09.8-building-models.md)

**Q:** ⭐ What's the silent `nn.Module` bug? → **A:** Layers in a **plain Python list** are **invisible to `.parameters()`** — not trained, not moved. **Use `nn.ModuleList`.**

**Q:** Why does `model.parameters()` find your weights? → **A:** Assigning `self.fc = nn.Linear(...)` **auto-registers** its parameters. So the optimizer sees every weight through arbitrary nesting.

**Q:** Why call `model(x)` not `model.forward(x)`? → **A:** `model(x)` runs hooks + `forward`; calling `forward` directly skips the hooks.

**Q:** When can't you use `nn.Sequential`? → **A:** Branching (residual `x + f(x)`), multiple inputs, or control flow — then write a custom `forward`.

---

## 09.9 · Data Loading

**Q:** What are `Dataset` and `DataLoader`? → **A:** **`Dataset`** = "one example, given an index." **`DataLoader`** = "batch, shuffle, load in parallel." → [09.9](../weeks/09.9-data-loading.md)

**Q:** ⭐ Why shuffle train but not validation? → **A:** **Train:** ordered data → class-clustered batches → wildly wrong gradients → unstable. **Val:** no training happens; shuffling just breaks reproducibility.

**Q:** ⭐ The most expensive mistake in deep learning? → **A:** **An idle GPU waiting for data.** Fix: **`num_workers > 0`** (parallel loading). Diagnose with `nvidia-smi`.

**Q:** ⭐ Why augment train but not validation? → **A:** Random augmentation at eval makes metrics **non-deterministic** and evaluates on **distorted** data. Val uses deterministic transforms.

---

## 09.10 · The Training Loop

**Q:** ⭐ The three-line heartbeat of every training loop? → **A:** `optimizer.zero_grad()` → `loss.backward()` → `optimizer.step()`. **Every model uses this exact loop.** → [09.10](../weeks/09.10-training-loop.md)

**Q:** ⭐ The three switches for train vs validation? → **A:** **`model.train()`** (dropout on) for training; **`model.eval()` + `torch.no_grad()`** for validation. Three different switches; need all.

**Q:** ⭐ The #1 correctness bug in training loops? → **A:** **Forgetting `model.eval()` at validation** — dropout stays on → noisy, pessimistic metrics. (And forgetting `model.train()` after → stuck in eval → silent overfitting.)

**Q:** ⭐ The single best "is my model broken?" test? → **A:** **Can it overfit a single batch to ~100%?** A correct model+loop memorizes 64 examples trivially. If not, the model or loop is broken (not the data). Karpathy's #1 recipe.

**Q:** Which checkpoint should you save? → **A:** The **best-by-validation**, not the last epoch (often overfit). Save the **optimizer state too**, to resume.

---

## 09.11 · CNNs

**Q:** ⭐ Why do fully-connected networks fail on images? → **A:** Too many params (150M/layer), no spatial structure, and — the killer — **no translation invariance** (learns "cat" separately at every position). → [09.11](../weeks/09.11-cnns.md)

**Q:** ⭐ What is weight sharing? → **A:** A convolution applies the **same filter at every position** → **translation invariance** (pattern detected anywhere by the same weights) + orders-of-magnitude fewer params.

**Q:** What does a convolution compute? → **A:** A **dot product** between a learned filter and each image patch, slid across the image → a **feature map.** The filter's weights ARE the learned pattern.

**Q:** ⭐ What is transfer learning and why is it the default? → **A:** Reuse an ImageNet-pretrained backbone's **generic early features**, train a new head. **Thousands of images instead of millions.** A from-scratch 61% becomes 90%+.

**Q:** ResNet's key idea? → **A:** **Residual connections** `x + f(x)` — a gradient highway that made 152-layer networks trainable. In every model since (including Transformers).

---

## 09.12 · Sequence Models

**Q:** ⭐ Why do vanilla RNNs forget? → **A:** **The vanishing gradient across time** — backprop-through-time multiplies the recurrent weights at every step → far-back gradient vanishes after ~10 steps. The $\lambda^n$ problem, across time. → [09.12](../weeks/09.12-sequence-models.md)

**Q:** How do LSTMs fix forgetting? → **A:** A **protected cell state** (information flows along nearly unchanged) + learned **gates** — a gradient highway extending memory to ~100s of steps.

**Q:** ⭐ The two limitations that killed RNNs? → **A:** **(1) Sequential — can't parallelize** (waste the GPU) — the killer. **(2) Even LSTMs struggle with very long range.** Attention fixes both: parallel + direct path between any two positions.

**Q:** Why can a Transformer parallelize but an RNN can't? → **A:** An RNN's step *t* needs step *t−1* first. A Transformer's attention processes **all positions at once** (one matmul), fully using the parallel GPU.

**Q:** ⭐ Why must you "pack" padded sequences? → **A:** Otherwise the LSTM **processes padding as real input**, contaminating the hidden state. `pack_padded_sequence` tells it where each sequence ends.

---

## 09.13 · Regularization

**Q:** ⭐ How do you diagnose whether to regularize? → **A:** [08.2](../../08-Machine-Learning/weeks/08.2-ml-workflow.md)'s diagnostic, unchanged: **train low + val high → overfit → regularize.** Both high → underfit → do the opposite. → [09.13](../weeks/09.13-regularization.md)

**Q:** ⭐ Why does dropout work? → **A:** **(1) Prevents co-adaptation** — neurons can't rely on specific others. **(2) Implicit ensemble.** **Off at inference** (`model.eval()`).

**Q:** ⭐ How does batch norm differ in train vs eval? → **A:** **Train:** current batch's stats (+ updates a running average). **Eval:** the **stored running average.** `model.eval()` switches it — forgetting it gives wrong predictions.

**Q:** Why do Transformers use LayerNorm not BatchNorm? → **A:** LayerNorm is **batch-independent** (normalizes per-example over features). Transformers have variable-length, small-batch inputs where BatchNorm's stats are unreliable.

**Q:** ⭐ The strongest regularizer? → **A:** **More data — and augmentation is "more data" for free.** It expands the problem rather than constraining the model. For images, often beats everything else combined.

---

## 09.14 · Performance

**Q:** ⭐ What is mixed precision and why use it by default? → **A:** Half-precision matmuls (Tensor Cores) + float32 where precision matters → **~2× faster, half memory, ~free.** Why LLMs train in bf16. → [09.14](../weeks/09.14-performance.md)

**Q:** ⭐ What is gradient accumulation? → **A:** Sum gradients over several mini-batches, step once → **simulate a big batch that won't fit.** Why PyTorch accumulates by default. Divide loss by accum_steps.

**Q:** What is gradient checkpointing? → **A:** **Throw away activations during forward, recompute during backward** — trades ~30% compute for a big memory saving.

**Q:** ⭐ Data-bound or compute-bound? → **A:** **`nvidia-smi` GPU-Util.** ~95% = compute-bound (optimize the model). Low = **data-bound** (fix the DataLoader). **Check FIRST** — optimizing the model won't help a starved GPU.

---

## 09.15 · Debugging

**Q:** ⭐ The single most valuable debugging test? → **A:** **Can the model overfit ONE batch to ~100%?** If not, the bug is in the model/loop (not data/hyperparameters). Do it **first**. → [09.15](../weeks/09.15-debugging.md)

**Q:** The cardinal rule of DL debugging? → **A:** **Change ONE thing at a time**, and make the model prove it on something trivial (overfit one batch) before asking it to generalize.

**Q:** How do you diagnose a NaN loss? → **A:** By **when**: step 0 → data/loss/init; after a spike → **exploding gradients** (clip); mid-training → overflow. `set_detect_anomaly(True)` finds the exact op.

**Q:** ⭐ Vanishing vs exploding gradients? → **A:** **Watch per-layer gradient norms.** Early ≈ 0 → vanishing (ReLU/residuals/norm/init). Exploding + spike → clip. The $\lambda^n$ table diagnosed empirically.

**Q:** What is a dead neuron? → **A:** A **ReLU stuck always-negative → outputs 0 → gradient 0 → never recovers.** Fix: lower LR, Leaky ReLU/GELU.

---

## 09.16 · Save/Load

**Q:** ⭐ Why save the `state_dict` not the whole model? → **A:** Whole-model save **pickles the class path** → breaks on refactor. `state_dict` is a **portable dict of tensors.** → [09.16](../weeks/09.16-saving-loading.md)

**Q:** ⭐ What's needed to resume training? → **A:** Model + **optimizer state** (Adam's m, v — built over hundreds of steps) + scheduler + epoch. **Resume from weights alone → Adam restarts cold → loss spike.**

**Q:** ⭐ Why is `torch.load` a security risk? → **A:** It's **pickle → arbitrary code execution.** A malicious `.pt` runs anything. Use **`weights_only=True`** or **safetensors** for untrusted files.

**Q:** Can you get perfect GPU reproducibility? → **A:** **Not easily** — some GPU ops are non-deterministic by design. `cudnn.deterministic` forces it (slower). Best practice: report **mean ± std across seeds.**

---

## 09.17 · Production

**Q:** ⭐ Why is inference lighter than training? → **A:** **No gradients, no optimizer state, no activation cache.** A 7B model trains in ~80 GB but infers in ~14 GB. → [09.17](../weeks/09.17-production.md)

**Q:** ⭐ The central trade-off in ML serving? → **A:** **Latency vs throughput.** Batching improves throughput (efficient GPU) but **hurts latency** (requests wait to fill). **Dynamic batching** is the tunable middle.

**Q:** ⭐ What are TorchScript and ONNX for? → **A:** Convert a PyTorch model to a **static, Python-free graph** for deployment. **ONNX** = open, cross-framework (the one to know). The dynamic graph is a research asset, a production liability.

**Q:** ⭐ How much of Module 08's production lesson applies to deep learning? → **A:** **All of it, unchanged** — monitor inputs, prediction-distribution canary, version everything, retraining gates, log inputs. **The model got fancier; deployment did not.**

---

## 🎯 The ten sentences (recall all ten cold)

1. **A layer is matmul + bias + nonlinearity; the nonlinearity is the only reason depth works.**
2. **Backprop is the chain rule, cached, run right-to-left.**
3. **PyTorch autograd is the `backward()` you wrote in 09.4, automated.**
4. **The training loop is `zero_grad → backward → step`, and it never changes.**
5. **`model.eval()` + `no_grad()` at inference — always.**
6. **Mixed precision by default: 2× faster, half the memory, ~free.**
7. **Overfit one batch first — it isolates model/loop bugs from data/hyperparameters.**
8. **CNNs win images via weight sharing; Transformers won sequences via parallelism.**
9. **Transfer learning: reuse pretrained features, train on 1000s not millions.**
10. **Deep learning added a new model, not a new discipline — MLOps and evaluation don't change.**

---

[⬆ Module 09](../README.md) · [📖 Lessons](../weeks/README.md) · [📄 Cheat sheet](../cheat-sheets/dl-cheatsheet.md) · [📝 Quiz](../quizzes/quiz-01.md)
