# Code Standards

[🏠 Standards](README.md)

> Every code example in this handbook is a teaching artifact **and** a model of production quality. Readers will copy it — so it must be worth copying.

---

## Principles

| Principle | In practice |
|---|---|
| **Production-quality** | Handle errors, validate inputs, no silent failures |
| **Readable over clever** | Obvious beats terse; no code golf |
| **Minimal & runnable** | Smallest complete example that actually runs |
| **Comment the *why*** | Explain intent and non-obvious decisions, not syntax |
| **Clear naming** | Descriptive, consistent, no single letters except math/indices |
| **Typed** | Type hints on public functions and data models |

---

## Baseline conventions

| Item | Standard |
|---|---|
| Python version | **3.11+** |
| Formatting | `ruff format` / `black`, 88-char lines |
| Linting | `ruff` clean |
| Typing | `mypy`-friendly type hints |
| Imports | stdlib → third-party → local, grouped |
| Docstrings | One-line summary for public functions; expand where non-obvious |

---

## Comment discipline

> [!TIP]
> A comment should explain something the code cannot. If the code already says it, delete the comment.

```python
# ❌ Redundant — the code already says this
i = i + 1  # increment i

# ✅ Explains a non-obvious decision
# Retry with backoff: the embedding API rate-limits bursts above ~50 rps.
```

---

## Error handling

Examples labeled production-ready **must** handle failure explicitly:

```python
import logging
from typing import Any

logger = logging.getLogger(__name__)


def embed(text: str, client: Any) -> list[float]:
    """Return the embedding vector for `text`.

    Raises:
        ValueError: if `text` is empty.
        EmbeddingError: if the provider call fails after retries.
    """
    if not text.strip():
        raise ValueError("text must be non-empty")

    try:
        response = client.embeddings.create(input=text)
    except Exception as exc:  # narrow this to the SDK's error in real code
        logger.exception("embedding request failed")
        raise EmbeddingError("failed to embed text") from exc

    return response.data[0].embedding
```

> [!NOTE]
> Teaching snippets that are *deliberately* simplified must say so: `# simplified for clarity — see the production version in code/`.

---

## Reproducibility

- **Seed randomness** in any example that involves it (`random`, `numpy`, framework seeds).
- **Pin versions** in each project's `pyproject.toml` / `requirements.txt`.
- **No hidden state** — an example should run top-to-bottom in a fresh environment.

---

## Performance notes

Where performance matters, annotate it inline or in a short note:

| Note when… | Example |
|---|---|
| A naive approach is O(n²) | "This is O(n²); vectorize with NumPy for large n." |
| Memory scales with input | "Loads the full file into memory — stream for large inputs." |
| A cheaper alternative exists | "Batching cuts API calls ~10×." |

---

## AI / LLM code specifics

- **Never hard-code secrets.** Read keys from environment variables; document `.env.example`.
- **Default to the latest, most capable models** when building AI apps; keep model IDs in config, not scattered in code.
- **Validate model output** (e.g. parse/validate JSON) before trusting it.
- **Make calls resilient** — timeouts, retries with backoff, and graceful degradation.
- **Log inputs/outputs** at a level that supports debugging without leaking sensitive data.

---

## Where code lives

| Context | Location |
|---|---|
| Inline teaching snippet | Inside the lesson `.md` |
| Full runnable sample | `code/NN-topic/` |
| Interactive exploration | `notebooks/NN.M-topic.ipynb` |
| Exercise solution | `docs/<module>/exercises/solution-NN.*` |

---

## Checklist

- [ ] Runs top-to-bottom in a clean env
- [ ] Type-hinted, formatted, lint-clean
- [ ] Errors handled (or explicitly marked "simplified")
- [ ] No secrets; config externalized
- [ ] Randomness seeded; versions pinned
- [ ] Comments explain *why*, not *what*
- [ ] Performance caveats noted where relevant
