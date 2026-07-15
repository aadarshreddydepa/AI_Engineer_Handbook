# 📄 Deep Learning with PyTorch — Cheat Sheet

[🏠 Module 09](../README.md) · [📖 Lessons](../weeks/README.md)

---

## 🧠 The core facts

| | |
|---|---|
| **A layer** | matmul + bias + **nonlinearity** ← the nonlinearity is why depth works |
| **Prove it** | no activation → 100 Linear layers collapse to 1 (linear ∘ linear = linear) |
| **Forward pass** | `affine → nonlinear → affine → … → loss` (one scalar) |
| **⭐ Backprop** | the **chain rule, cached, right-to-left** — reverse mode = all gradients in 1 pass |
| **⭐ The gradient of fused loss** | `predicted − actual` |
| **Loss takes** | **LOGITS**, not probabilities (CrossEntropyLoss fuses softmax+log+NLL) |
| **⭐ Sanity check** | initial loss ≈ **ln(C)** (2.30 for 10 classes) |
| **⭐ Vanishing/exploding** | chain rule multiplies → λⁿ. ReLU(1), **residuals**, norm, init |

---

## 🔥 PyTorch essentials

| | |
|---|---|
| **Tensor** | NumPy array **+ device + autograd** |
| **Device** | `device = 'cuda' if torch.cuda.is_available() else 'cpu'` |
| **⭐ #1 error** | "tensors on different devices" → **move model once, every batch in the loop** |
| **Ops** | same as NumPy, but **`dim`** not `axis` |
| **NumPy↔torch** | `torch.tensor(a)` copies; `torch.from_numpy(a)` ⚠️ **shares memory** |
| **Labels** | `.long()` for CrossEntropyLoss |
| **⭐ Training dtype** | **bfloat16** (range) — not float16 (overflows) |
| **⭐ Timing** | `torch.cuda.synchronize()` — GPU ops are **async** |

---

## 📼 Autograd

| | |
|---|---|
| **What** | records ops on `requires_grad` tensors; `backward()` walks the graph = **your 09.4 backward()** |
| **⭐ Dynamic graph** | built each forward pass → real Python `if`/`for`/`pdb` work |
| **`loss.backward()`** | fills `.grad` (loss must be a **scalar**) |
| **⭐ `model.eval()` ≠ `no_grad()`** | eval = dropout off + batchnorm stats; no_grad = no graph. **NEED BOTH at inference** |
| **⭐ Memory leak** | appending un-detached tensors → use **`.item()`** |
| **The ritual** | `zero_grad()` → `backward()` → `step()` |

---

## 🏗️ `nn.Module`

```python
class Net(nn.Module):
    def __init__(self):
        super().__init__()                # ⭐ first line
        self.fc = nn.Linear(784, 10)      # create layers
    def forward(self, x):
        return self.fc(x)                 # use them; output LOGITS

model = Net().to(device)                  # moves all params
model(x)                                  # ⭐ NOT model.forward(x)
```

| | |
|---|---|
| **Read a model** | `__init__` = parts · `forward` = wiring |
| **⭐ `.parameters()`** | auto-discovered → the optimizer's input |
| **⭐ Plain list = invisible** | use **`nn.ModuleList`** or params won't train |
| **`nn.Sequential`** | straight-line stacks; custom `forward` for branching/residuals |

---

## 🚚 Data & training loop

```python
loader = DataLoader(ds, batch_size=64, shuffle=True,     # ⭐ shuffle TRAIN only
                    num_workers=4, pin_memory=True)       # ⭐ num_workers or GPU starves

for epoch in range(N):
    model.train()                                          # ⭐ dropout on
    for X, y in train_loader:
        X, y = X.to(device), y.to(device)                  # ⭐ every batch
        optimizer.zero_grad()                              # 1
        loss = loss_fn(model(X), y)                        # forward + loss
        loss.backward()                                    # 2
        optimizer.step()                                   # 3
    model.eval()                                            # ⭐ + no_grad for val
    with torch.no_grad():
        ...validate...
```

| | |
|---|---|
| **⭐ Augment** | train only; val = deterministic |
| **Checkpoint** | save the **best-by-val** + **optimizer state** |
| **Early stop** | max epochs high; stop after `patience` stalls |
| **⭐ Idle GPU** | `nvidia-smi` low = data-bound → more `num_workers` |

---

## ⚙️ Optimizers (09.5)

| Optimizer | Fixes |
|---|---|
| SGD | (baseline; zig-zags) |
| Momentum | ravine zig-zag |
| RMSProp | one-LR-fits-nobody |
| Adam | both + bias correction |
| **⭐ AdamW** | **the default** — decoupled weight decay |

**⭐ Adam = 3× param memory** (weights + m + v) → why fine-tuning OOMs, why LoRA.
**⭐ LR is the #1 hyperparameter.** Schedule: warmup + cosine.

---

## 🖼️ CNNs (09.11) & sequences (09.12)

| CNN | |
|---|---|
| **Why not FC** | 150M params, **no translation invariance** |
| **⭐ Weight sharing** | same filter everywhere → invariance + few params |
| **Recipe** | `Conv2d(c, c', 3, stride=1, padding=1)` → same size |
| **Shape** | `(N, C, H, W)` |
| **⭐ Transfer learning** | pretrained backbone → 1000s not millions of images |
| **ResNet** | residual `x + f(x)` → 152 layers |

| RNN/LSTM | |
|---|---|
| **RNN forgets** | vanishing gradient across time (~10 steps) |
| **LSTM/GRU** | gates + protected cell state → 100s of steps |
| **⭐ Why Transformers won** | **sequential (can't parallelize)** + long-range → attention fixes both |

---

## 🛡️ Regularization (09.13) & performance (09.14)

| Regularizer | Note |
|---|---|
| **⭐ Data/augmentation** | the strongest — try first |
| Early stopping · weight decay (AdamW) | free / default |
| Dropout | ⭐ **off at inference** |
| BatchNorm / LayerNorm | ⭐ train/eval differ · **LayerNorm for Transformers** |

| Performance | |
|---|---|
| **⭐ Mixed precision** | 2× faster, half memory, ~free. **Use by default** |
| Gradient clipping | `clip_grad_norm_(params, 1.0)` — seatbelt vs NaN |
| Gradient accumulation | big effective batch, less memory |
| Gradient checkpointing | recompute activations, less memory |
| **⭐ Diagnose first** | `nvidia-smi`: data-bound vs compute-bound |

---

## 🐛 Debugging (09.15)

**The workflow, in order:**
1. Initial loss ≈ **ln(C)**?
2. ⭐ **Can it overfit ONE batch?** (→0 or it's broken)
3. Gradients flowing? (None/~0/huge)
4. LR sane? (10× each way)

| Symptom | Fix |
|---|---|
| NaN from step 0 | check data · stable loss · init |
| NaN after spike | **clip gradients** · lower LR · warmup |
| NaN mid-training | `set_detect_anomaly(True)` finds the op |
| Vanishing gradients | ReLU · **residuals** · norm · init |
| Dead neurons | lower LR · Leaky ReLU/GELU |
| Shape error | print `.shape` in `forward`; check NCHW |

**⭐ Change ONE thing at a time. Overfit one batch FIRST.**

---

## 💾 Save/load (09.16) & production (09.17)

| | |
|---|---|
| **⭐ Save** | `state_dict` — **not the whole model** |
| **⭐ Resume** | model + **optimizer state** + scheduler + epoch |
| **Transfer** | `load_state_dict(..., strict=False)` |
| **⭐ Security** | `torch.load` = pickle = **RCE**. `weights_only=True` / safetensors |
| **After loading** | `model.eval()` |

| Production | |
|---|---|
| **⭐ Inference path** | `model.eval()` + `torch.no_grad()` |
| **⭐ Inference is lighter** | no gradients/optimizer state → 7B trains 80GB, infers 14GB |
| **⭐ Latency vs throughput** | batching helps throughput, hurts latency |
| **Batch vs online** | start with **batch** |
| **Export** | TorchScript (C++) · **ONNX** (open, cross-framework) |
| **⭐ MLOps** | **unchanged from Module 08** — monitor inputs, version, gate retraining |

---

## 🎯 The ten sentences

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

[⬆ Module 09](../README.md) · [📖 Lessons](../weeks/README.md) · [🧠 Flashcards](../flashcards/deck.md)
