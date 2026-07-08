# Reference & Citation Standards

[🏠 Standards](README.md) · [📚 Resources](../RESOURCES.md)

> How to cite external material so the handbook is trustworthy, verifiable, and respectful of sources.

---

## Source priority

Prefer sources in this order:

| Rank | Source type | Why |
|:--:|---|---|
| 1 | **Official documentation** | Authoritative and current |
| 2 | **Research papers** | Primary source for methods/claims |
| 3 | **Books** | Depth and durability |
| 4 | **Talks / lectures** | Expert framing and intuition |
| 5 | **High-quality tutorials / blogs** | Practical, but verify against primaries |

> [!WARNING]
> Never cite an AI model's output, an unattributed blog, or a forum answer as a primary source for a technical claim. Trace it to a primary source or mark it clearly as informal.

---

## Citation formats

**Paper**
```markdown
- Vaswani, A. et al. "Attention Is All You Need." NeurIPS, 2017. https://arxiv.org/abs/1706.03762
```

**Book**
```markdown
- Goodfellow, I., Bengio, Y., Courville, A. *Deep Learning*. MIT Press, 2016.
```

**Documentation**
```markdown
- PyTorch. "Autograd mechanics." Official docs. <url> (accessed 2026-07-08).
```

**Talk / video**
```markdown
- Karpathy, A. "Let's build GPT: from scratch." YouTube, 2023. <url>
```

**Blog / tutorial**
```markdown
- <Author>. "<Title>." <Site>, <year>. <url>
```

---

## In-lesson rules

- Every non-obvious factual or empirical claim gets a citation.
- Cite at the **point of use** or in the lesson's §25 References — link both ways where helpful.
- Include an **access date** for docs and web pages (they change).
- Papers: prefer the **arXiv** or DOI link.
- Reproduce numbers/quotes faithfully; paraphrase claims in your own words otherwise.

---

## Paper summaries

Deep engagement with a paper goes in `docs/<module>/references/` or `references/`, using the [research-paper-summary template](../templates/research-paper-summary-template.md). Each summary captures: problem, key idea, method, results, why-it-matters, limitations, and glossary terms.

---

## Attribution & licensing

- Third-party images/figures retain their original license — **do not** copy them in without permission and attribution. Prefer original Mermaid diagrams.
- Quotations must be short, attributed, and clearly marked.
- The handbook's own license is in [LICENSE.md](../LICENSE.md); respect others' equivalently.

---

## Where references aggregate

| Scope | Location |
|---|---|
| Lesson-level | Lesson §25 |
| Module-level deep dives | `docs/<module>/references/` |
| Repo-wide curated list | [RESOURCES.md](../RESOURCES.md) |

---

## Checklist

- [ ] Highest-quality source available is used
- [ ] Every non-obvious claim is cited
- [ ] Format matches the type (paper/book/docs/talk/blog)
- [ ] Access date included for web/docs
- [ ] Third-party media properly licensed & attributed
