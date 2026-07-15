# 🏋️ Module 09 · Deep Learning — Exercises

[🏠 Module 09](../README.md) · [📖 Lessons](../weeks/README.md) · [🧩 Projects](../projects/)

> These are **build-it** exercises, not multiple-choice. The ordering mirrors the module's spine: **derive it by hand → prove PyTorch agrees → then scale it.** If you do only three, do ⭐ **E4, E7, E10** — they are the module in miniature.
>
> Each exercise lists a **goal**, **constraints**, and a **done-when** (an objective, checkable success criterion). No solutions are provided on purpose — the [answers to the quiz](../quizzes/answers-01.md) and the lessons contain everything you need.

---

## Tier 1 · First principles, no torch (09.1–09.5)

> These use **only Python + NumPy.** Do not import torch. The point is to feel the mechanics before the abstraction hides them.

### E1 · A neuron is a dot product
**Goal:** Implement a single neuron `forward(x, w, b) -> sigmoid(w·x + b)` and, by hand, a `backward` that returns `dw, db, dx` for a scalar loss.
**Constraints:** NumPy only; no autograd of any kind.
**Done-when:** For random `w, x, b`, your analytical `dw` matches a central finite-difference estimate to within `1e-6` (use **float64**). → [09.2](../weeks/09.2-neural-network-fundamentals.md), [09.4](../weeks/09.4-backpropagation.md)

### E2 · Prove depth needs nonlinearity
**Goal:** Build a 3-layer linear network **without activations**, then find a single `(W, b)` that produces identical outputs for all inputs.
**Done-when:** You print the collapsed `W', b'` and show `max|net(x) − (W'x + b')| < 1e-10` over 1000 random inputs — demonstrating the network *is* one affine map. → [09.2](../weeks/09.2-neural-network-fundamentals.md)

### E3 · The vanishing-gradient table
**Goal:** For sigmoid, tanh, and ReLU, empirically measure the gradient magnitude reaching layer 1 in an `L`-layer network as `L` grows from 2 to 40.
**Done-when:** You produce a table/plot showing sigmoid's gradient collapsing toward 0 and ReLU's staying O(1), and you can state the per-layer multiplier that explains each curve. → [09.2](../weeks/09.2-neural-network-fundamentals.md)

### ⭐ E4 · Backprop a 2-layer MLP from scratch
**Goal:** Implement a full `[784 → 128 → 10]` MLP (ReLU + softmax-cross-entropy) with **hand-written forward and backward**, and train it on MNIST to **>95%** test accuracy.
**Constraints:** NumPy only. You write every gradient. No torch, no autograd.
**Done-when:** (1) Gradient check passes for **every** parameter tensor (float64, `<1e-5`). (2) Test accuracy **>95%**. Keep this code — E7 will resurrect it. → [09.4](../weeks/09.4-backpropagation.md)

### E5 · Implement Adam in twelve lines
**Goal:** Add an `Adam` optimizer class to your E4 network (m, v, bias correction) and compare its loss curve to plain SGD.
**Done-when:** Adam reaches your target loss in **fewer epochs** than SGD, and you can point to the exact lines implementing momentum, the second moment, and bias correction. → [09.5](../weeks/09.5-optimization.md)

---

## Tier 2 · Introducing PyTorch (09.6–09.10)

### E6 · Tensor & device drills
**Goal:** Write a small script that (a) creates the same computation in NumPy and torch, (b) moves it to GPU if available, (c) **times** a large matmul on CPU vs GPU **correctly**.
**Done-when:** Your GPU timing uses `torch.cuda.synchronize()` and reports a realistic speedup; you also demonstrate the `from_numpy` shared-memory gotcha with a two-line proof. → [09.6](../weeks/09.6-pytorch-tensors.md)

### ⭐ E7 · Prove autograd == your backward
**Goal:** Rebuild the **exact** E4 network in PyTorch, copy your NumPy weights into it, run one forward+backward on the same batch, and compare gradients.
**Constraints:** Same architecture, same weights, same batch as E4.
**Done-when:** `torch.allclose(numpy_grad, torch_param.grad, atol=1e-5)` is `True` for **every** layer. *This is the single most important exercise in the module* — it proves `loss.backward()` is your hand-derived chain rule. → [09.7](../weeks/09.7-autograd.md)

### E8 · Refactor into `nn.Module`
**Goal:** Re-express the network as a clean `nn.Module` with a `Dataset` + `DataLoader` feeding it.
**Constraints:** Use `nn.ModuleList`/`nn.Sequential` correctly; verify `sum(p.numel() for p in model.parameters())` equals the hand-count from E4.
**Done-when:** Param count matches E4 exactly (catches the "layers in a plain list" bug), and the model trains to the same accuracy. → [09.8](../weeks/09.8-building-models.md), [09.9](../weeks/09.9-data-loading.md)

### ⭐ E9 · The canonical training loop
**Goal:** Write the full train/validate loop with `model.train()`/`model.eval()`, `no_grad()`, per-epoch metrics, best-by-validation checkpointing, and early stopping.
**Done-when:** (1) Removing `model.eval()` visibly changes validation numbers (prove you understand why). (2) The saved checkpoint reloads and reproduces the reported validation accuracy within noise. → [09.10](../weeks/09.10-training-loop.md)

### E10 · ⭐ Overfit one batch
**Goal:** Add a debug mode that trains on a **single fixed batch** of 32 examples until loss → ~0.
**Done-when:** Your model drives that batch to ~100% accuracy in a handful of iterations; then **deliberately break** the model (e.g., detach a layer, wrong loss) and show the test *fails* — proving the test discriminates. → [09.10](../weeks/09.10-training-loop.md), [09.15](../weeks/09.15-debugging.md)

---

## Tier 3 · Architectures & scale (09.11–09.17)

### E11 · CNN + the transfer-learning payoff
**Goal:** Train a small CNN on CIFAR-10 from scratch, record its accuracy, then fine-tune a **pretrained** ResNet on the same data.
**Done-when:** You report both numbers and the training-set size each needed; the pretrained model beats from-scratch by a wide margin with less data — and you can explain *why* in terms of generic early features. → [09.11](../weeks/09.11-cnns.md)

### E12 · Sequence model on variable-length data
**Goal:** Train an LSTM text classifier on a small dataset with **padded, packed** sequences.
**Done-when:** You show that **removing** `pack_padded_sequence` measurably hurts accuracy, and you can explain the hidden-state contamination that causes it. → [09.12](../weeks/09.12-sequence-models.md)

### E13 · Regularization ablation
**Goal:** Take a model that overfits (train ≫ val) and run a controlled ablation: baseline → +augmentation → +dropout → +weight decay.
**Constraints:** Change **one thing at a time**; hold everything else fixed.
**Done-when:** You produce a table of train/val accuracy for each variant and can rank the regularizers by effect on *your* data (augmentation usually wins). → [09.13](../weeks/09.13-regularization.md)

### E14 · Make it fast
**Goal:** Profile a training run, identify whether it's **data-bound or compute-bound** with `nvidia-smi`, and then apply the right fix (workers vs mixed precision).
**Done-when:** You report GPU-Util before/after and a wall-clock speedup, and you enabled **mixed precision** (`autocast` + `GradScaler` for fp16, or bf16) with **no accuracy regression**. → [09.14](../weeks/09.14-performance.md)

### E15 · Break it, then diagnose it
**Goal:** Deliberately induce, then diagnose and fix, three failure modes: (a) NaN from exploding gradients, (b) a dead-ReLU network that won't learn, (c) a device-mismatch error.
**Done-when:** For each, you name the symptom, the diagnostic that localized it, and the one-line fix. → [09.15](../weeks/09.15-debugging.md)

### E16 · Save, load, resume — bit-for-bit
**Goal:** Checkpoint mid-training (model + **optimizer** + scheduler + epoch), kill the process, and resume.
**Done-when:** The resumed loss curve continues smoothly with **no spike** — proving you saved the optimizer state; then show that resuming from **weights only** *does* produce a spike (Adam restarting cold). → [09.16](../weeks/09.16-saving-loading.md)

### E17 · Ship it
**Goal:** Export your trained model to **ONNX**, run inference through onnxruntime, and confirm outputs match PyTorch.
**Done-when:** `np.allclose(torch_out, onnx_out, atol=1e-4)`; you also write a 5-line "inference contract" listing the exact preprocessing the server must apply (the train/serve-skew guard). → [09.17](../weeks/09.17-production.md)

---

## 🎓 Capstone challenge

### E18 · The end-to-end proof
Combine E4 + E7 + E9 + E10 into a single well-structured repo: a from-scratch NumPy MLP, its PyTorch twin, a gradient-equality test (`torch.allclose`), a real training loop with checkpointing, and an overfit-one-batch smoke test in the test suite.
**Done-when:** `pytest` passes with at least: a gradient-check test, an autograd-equality test, and an overfit-one-batch test. This repo *is* your proof that you understand deep learning from the metal up — not just that you can call `.fit()`. → [09.18](../weeks/09.18-projects-summary.md)

---

> [!TIP]
> Struggling with an exercise is the point — the gradient you derive by hand in E4 is the gradient you'll trust `loss.backward()` to compute for the rest of your career. Don't skip the hand-derivation to get to the library faster; the library only makes sense *because* of the hand-derivation.

[🏠 Module 09](../README.md) · [📝 Quiz](../quizzes/quiz-01.md) · [🧠 Flashcards](../flashcards/deck.md) · [🧩 Projects](../projects/)
