# 📝 Module 09 · Deep Learning — Quiz 01

[🏠 Module 09](../README.md) · [📖 Lessons](../weeks/README.md) · [✅ Answers](answers-01.md)

> **40 questions across all 18 lessons.** Mix of conceptual, diagnostic, and "spot the bug." Aim for a first-principles *explanation*, not just the letter — the [answers](answers-01.md) grade the reasoning. Target: **32/40** to consider the module solid.

---

## Part A · Foundations (09.1–09.5)

**1.** Classical ML and deep learning differ in exactly one fundamental way. What is it?

**2.** Explain, with a one-line algebraic argument, why a stack of `nn.Linear` layers with **no activation between them** is no more expressive than a single `nn.Linear`.

**3.** A colleague uses sigmoid activations in a 20-layer hidden network and training stalls. Name the phenomenon, give the number that causes it, and name the activation that fixes it.

**4.** You initialize a 10-class classifier and, before any training, print the loss. What value tells you the network is wired correctly, and why that specific number?

**5.** Backpropagation is often called "a new algorithm." Refute that in one sentence — what is it *actually*?

**6.** Why does backprop run **right-to-left** (reverse mode) rather than left-to-right? Frame your answer in terms of the number of inputs vs outputs.

**7.** For `Z = A @ W`, the gradient with respect to `W` is `dW = A.T @ dZ`. Without memorizing it, how would you *derive* that the `A` must be transposed and must come first?

**8.** State what each of these does and why both are needed every iteration: `optimizer.zero_grad()` and the fact that PyTorch **accumulates** gradients.

**9.** Adam is built from two older ideas plus one correction. Name all three and what each contributes.

**10.** Why is **AdamW** preferred over Adam for essentially every modern model? Be specific about what "decoupled" means.

**11.** Training a model works, but fine-tuning the *same* model OOMs at the same batch size. Give the memory-based explanation.

---

## Part B · PyTorch mechanics (09.6–09.10)

**12.** In one sentence each, what two capabilities does a `torch.Tensor` add on top of a NumPy array?

**13.** This code is subtly wrong. What's the bug and the one-word-ish fix?
```python
model = Net().to('cuda')
for X, y in loader:          # X, y come off the CPU DataLoader
    pred = model(X)
    loss = loss_fn(pred, y)
```

**14.** `a = np.arange(5); t = torch.from_numpy(a); a[0] = 99`. What is `t[0]` now, and what general rule does this illustrate?

**15.** Why must you call `torch.cuda.synchronize()` before reading a timer around GPU code?

**16.** Give the two-part distinction between `model.eval()` and `torch.no_grad()`. Why is running validation with only one of them a bug?

**17.** This training loop leaks memory until it OOMs after many epochs. Find the line.
```python
losses = []
for X, y in loader:
    loss = loss_fn(model(X), y)
    optimizer.zero_grad(); loss.backward(); optimizer.step()
    losses.append(loss)
```

**18.** PyTorch's computational graph is called **dynamic**. Explain what "dynamic" means mechanically, and name the practical benefit that made researchers adopt it.

**19.** A model defines its layers like this. It trains, but the loss barely moves and `sum(p.numel() for p in model.parameters())` is suspiciously small. What's wrong?
```python
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.blocks = [nn.Linear(64, 64) for _ in range(4)]
    def forward(self, x):
        for b in self.blocks: x = torch.relu(b(x))
        return x
```

**20.** Why do you shuffle the **training** DataLoader but not the **validation** one?

**21.** Your expensive GPU sits at 30% utilization the whole run. What is the most likely cause and the first knob to turn?

**22.** Write (from memory) the three lines at the heart of every training loop, in order.

**23.** After validating, the next epoch's training is unstable / the model seems to stop learning. Which single missing call most likely explains it?

**24.** What is the single most valuable "is my model broken?" test, and what does *passing* it rule out?

---

## Part C · Architectures (09.11–09.12)

**25.** Give the three reasons a fully-connected network is a poor choice for images, and say which of the three is the "killer."

**26.** Define **weight sharing** in a convolution and state the two properties it buys you.

**27.** Transfer learning turns a from-scratch 61% into 90%+ with a fraction of the data. What property of learned features makes this possible?

**28.** A vanilla RNN "forgets" information from more than ~10 steps ago. Name the mechanism and connect it to a formula you've seen elsewhere in this module.

**29.** LSTMs extend memory to hundreds of steps. What is the one architectural feature most responsible, and what does it protect?

**30.** Attention replaced RNNs for two reasons. State both, and identify which one was the *decisive* one for hardware.

**31.** You feed padded, variable-length sequences straight into an `nn.LSTM` and accuracy is mediocre. What did you forget to do, and what goes wrong without it?

---

## Part D · Regularization, performance, debugging, production (09.13–09.17)

**32.** Train accuracy 99%, validation 71%. Name the condition, and list two regularizers you'd reach for first.

**33.** Batch normalization behaves differently in training vs evaluation. Describe both behaviours and name the call that switches between them.

**34.** Why do Transformers use **LayerNorm** instead of **BatchNorm**?

**35.** What is **mixed-precision training**, why is it nearly free, and why is **bfloat16** preferred over float16 for it?

**36.** Explain **gradient accumulation** in one sentence and say what problem it solves.

**37.** Your loss goes to `NaN` on step 3,000 right after a sharp spike. Which failure mode is this, and what's the standard fix?

**38.** Why should you save a model's `state_dict` rather than the whole model object with `torch.save(model, ...)`?

**39.** `torch.load` on a file downloaded from the internet is a security risk. Why, and what's the safe alternative?

**40.** A teammate says: "Now that we're using deep learning, our whole MLOps and evaluation setup from the classical-ML project needs to be rebuilt." True or false — and defend your answer in one or two sentences.

---

## 🎁 Bonus (harder)

**B1.** You have the *exact* same 2-layer MLP implemented twice — once by hand in NumPy (09.4), once in PyTorch (09.7). You feed both the same weights and the same batch. What single line of code proves the PyTorch autograd gradients equal your hand-derived gradients, and why is that the whole point of the module?

**B2.** A model trains beautifully (loss → 0.02) but predicts nonsense in production. You confirm the weights loaded correctly. Name the two most likely one-line causes.

**B3.** Explain why training a 7B-parameter model needs ~80 GB but *serving* it needs ~14 GB, itemizing where the training memory goes.

---

[✅ Check your answers →](answers-01.md) · [🧠 Flashcards](../flashcards/deck.md) · [📄 Cheat sheet](../cheat-sheets/dl-cheatsheet.md)
