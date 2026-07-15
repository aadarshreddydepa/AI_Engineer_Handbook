# Module 09 · Deep Learning

[⬅ 08 · Machine Learning](../08-Machine-Learning/README.md) · [🏠 docs](../README.md) · [🗺 Roadmap](../../ROADMAP.md) · [10 · NLP ➡](../10-NLP/README.md)

> Neural networks from the ground up with PyTorch.

---

## Purpose

This module covers **Deep Learning**. Neural networks from the ground up with PyTorch. It fits into the overall program as described in the [Roadmap](../../ROADMAP.md) and [Curriculum](../../CURRICULUM.md).

## What you'll learn

- Neurons, layers, and backpropagation from scratch
- PyTorch: tensors, autograd, and training loops
- Regularization, normalization, and initialization
- Debugging and stabilizing neural networks

## 📖 Lessons (start here)

> ✅ **This module's content is written.** Work through the lessons in order via the [lesson index](weeks/README.md).

| # | Lesson | Torch yet? |
|---|---|---|
| 09.1 | [Why Deep Learning?](weeks/09.1-why-deep-learning.md) | — |
| 09.2 | [Neural Network Fundamentals](weeks/09.2-neural-network-fundamentals.md) | — |
| 09.3 | [The Math of Neural Networks](weeks/09.3-math-of-neural-networks.md) | — |
| 09.4 | [Backpropagation from Scratch](weeks/09.4-backpropagation.md) ⭐ | — |
| 09.5 | [Optimization](weeks/09.5-optimization.md) | — |
| 09.6 | [PyTorch Tensors](weeks/09.6-pytorch-tensors.md) | ✅ `import torch` |
| 09.7 | [Autograd](weeks/09.7-autograd.md) | ✅ |
| 09.8 | [Building Models with `nn.Module`](weeks/09.8-building-models.md) | ✅ |
| 09.9 | [Data Loading](weeks/09.9-data-loading.md) | ✅ |
| 09.10 | [The Training Loop](weeks/09.10-training-loop.md) ⭐ | ✅ |
| 09.11 | [Convolutional Neural Networks](weeks/09.11-cnns.md) | ✅ |
| 09.12 | [Sequence Models — RNN → LSTM → Transformer](weeks/09.12-sequence-models.md) | ✅ |
| 09.13 | [Regularization & Normalization](weeks/09.13-regularization.md) | ✅ |
| 09.14 | [Performance Optimization](weeks/09.14-performance.md) | ✅ |
| 09.15 | [Model Debugging](weeks/09.15-debugging.md) | ✅ |
| 09.16 | [Saving & Loading](weeks/09.16-saving-loading.md) | ✅ |
| 09.17 | [Production](weeks/09.17-production.md) | ✅ |
| 09.18 | [Projects & Summary](weeks/09.18-projects-summary.md) | ✅ |

**Companion artifacts:** [Exercises](exercises/README.md) · [Quiz](quizzes/quiz-01.md) · [Flashcards](flashcards/deck.md) · [Cheat sheet](cheat-sheets/dl-cheatsheet.md)

> [!IMPORTANT]
> **⭐ The rule of this module: derive it by hand *before* you import the library.**
>
> Lessons 09.1–09.5 use **only Python and NumPy** — no `import torch`. You will hand-write a neuron, a layer, a forward pass, and — the load-bearing moment — **backpropagation**, gradient-checked against finite differences. Only at **09.6** does torch appear. Then, in 09.7, you rebuild that *exact same network* in PyTorch and prove with **`torch.allclose`** that `loss.backward()` computes the identical gradients you derived by hand. That assertion is the instant autograd stops being magic.
>
> **And the sentence that carries the whole module: deep learning added a new model, not a new discipline.** The training loop is always `zero_grad → backward → step`. Backprop is always the chain rule, cached. And the evaluation and MLOps you learned in [Module 08](../08-Machine-Learning/README.md) carry over **unchanged** — the network got deeper; the engineering did not.

## How this module is organized

Content is delivered week by week. Each module uses the same subfolders:

| Folder | Contents |
|---|---|
| [`weeks/`](weeks/) | Weekly lesson content, one file per week (`week-01.md`, `week-02.md`, …). |
| [`diagrams/`](diagrams/) | Mermaid sources and exported diagram assets for this module. |
| [`exercises/`](exercises/) | Hands-on practice problems with solutions. |
| [`projects/`](projects/) | Buildable projects that apply this module's skills. |
| [`quizzes/`](quizzes/) | Self-assessment question banks with answer keys. |
| [`flashcards/`](flashcards/) | Spaced-repetition Q/A decks for active recall. |
| [`cheat-sheets/`](cheat-sheets/) | One-page quick references for this module. |
| [`references/`](references/) | Paper summaries and deep-dive notes. |

## Suggested study flow

```mermaid
flowchart LR
    R[Read the week] --> E[Do exercises]
    E --> P[Build project]
    P --> Q[Take quiz]
    Q --> F[Review flashcards]
    F --> N[Next week]
```

## File & naming conventions

| Item | Convention | Example |
|---|---|---|
| Weekly lesson | `week-NN.md` | `weeks/week-01.md` |
| Exercise | `exercise-NN.md` (+ `solution-NN.*`) | `exercises/exercise-01.md` |
| Project | `project-NN/` folder with `README.md` | `projects/project-01/` |
| Quiz | `quiz-NN.md` (+ `answers-NN.md`) | `quizzes/quiz-01.md` |
| Flashcards | `deck.md` | `flashcards/deck.md` |
| Diagram | `topic.mmd` / `topic.png` | `diagrams/attention.mmd` |

## Markdown conventions

This file follows the repository Markdown standards — see [CONTRIBUTING.md](../../CONTRIBUTING.md): one H1 per file, tables over prose, GitHub callouts (`> [!NOTE]`), fenced code blocks with a language, Mermaid for diagrams, and relative internal links.

## Related modules

- [Machine Learning](../08-Machine-Learning/README.md)
- [NLP](../10-NLP/README.md)

---

## Navigation

| Direction | Link |
|---|---|
| ⬆ Parent | [docs/](../README.md) |
| ⬅ Previous | [⬅ 08 · Machine Learning](../08-Machine-Learning/README.md) |
| ➡ Next | [10 · NLP ➡](../10-NLP/README.md) |
| 🗺 Roadmap | [ROADMAP.md](../../ROADMAP.md) |
| 📚 Curriculum | [CURRICULUM.md](../../CURRICULUM.md) |
| 🏠 Repo root | [README.md](../../README.md) |
