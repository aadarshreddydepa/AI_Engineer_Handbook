# Resources

> A curated, opinionated list of the best external material to complement the handbook. Quality over quantity — every entry here is worth your time.

> [!NOTE]
> The handbook is self-contained; these are for going deeper. Links are added as modules are authored. Prefer primary sources (papers, official docs) over secondary summaries.

---

## Foundational books

| Topic | Resource | Why |
|---|---|---|
| ML | *Hands-On Machine Learning* — A. Géron | Practical, code-first classical ML & DL |
| Deep Learning | *Deep Learning* — Goodfellow, Bengio, Courville | The rigorous reference |
| Math | *Mathematics for Machine Learning* — Deisenroth et al. (free PDF) | Exactly the math you need, no more |
| DL intuition | *The Little Book of Deep Learning* — F. Fleuret (free) | Compact and clear |

---

## Courses

| Topic | Resource |
|---|---|
| Neural nets from scratch | Andrej Karpathy — *Neural Networks: Zero to Hero* |
| Deep learning | fast.ai — *Practical Deep Learning for Coders* |
| ML foundations | Stanford CS229 |
| NLP / Transformers | Stanford CS224N |

---

## Key papers (read as you reach the relevant module)

| Module | Paper |
|---|---|
| 05 | *Attention Is All You Need* (Transformer) |
| 05 | *BERT: Pre-training of Deep Bidirectional Transformers* |
| 06 | *Language Models are Few-Shot Learners* (GPT-3) |
| 06 | *Training Compute-Optimal LLMs* (Chinchilla scaling laws) |
| 07 | *Chain-of-Thought Prompting Elicits Reasoning* |
| 08 | *Retrieval-Augmented Generation for Knowledge-Intensive Tasks* |
| 09 | *LoRA: Low-Rank Adaptation of Large Language Models* |
| 09 | *Direct Preference Optimization (DPO)* |
| 10 | *ReAct: Synergizing Reasoning and Acting in Language Models* |

---

## Tools & libraries

| Category | Tools |
|---|---|
| Core DL | PyTorch, NumPy |
| LLM APIs / SDKs | Anthropic SDK (Claude), and other provider SDKs |
| Serving | FastAPI, vLLM, Docker |
| Vector DBs | FAISS, and hosted vector stores |
| Fine-tuning | Hugging Face `transformers`, `peft`, `trl` |
| Eval & observability | Tracing/eval frameworks (added per module) |
| Environment | `uv` / `poetry`, `ruff`, Jupyter |

> [!TIP]
> When building AI applications, default to the latest and most capable models available. See [claude-api](https://docs.anthropic.com/) references for model IDs and pricing before choosing one.

---

## Staying current

| Type | Where |
|---|---|
| Papers | arXiv `cs.CL` / `cs.LG`, Papers with Code |
| Engineering blogs | Provider engineering blogs, practitioners' writeups |
| Communities | Reputable ML/AI engineering forums and newsletters |

> [!WARNING]
> The field moves fast, but **fundamentals don't**. Spend most of your time on the first-principles material in this handbook; use news to contextualize, not to chase.
