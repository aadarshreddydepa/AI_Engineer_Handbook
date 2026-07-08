# Curriculum

> The detailed, lesson-by-lesson breakdown of every module. Where [ROADMAP.md](ROADMAP.md) gives the schedule and dependencies, this document defines **what each lesson teaches, what you'll be able to do afterward, and how it's assessed**.

Every lesson follows the same anatomy so the handbook feels consistent from cover to cover.

---

## Lesson anatomy

Each lesson file (`docs/modules/<module>/<lesson>.md`) contains these sections in order:

| Section | Purpose |
|---|---|
| **Overview** | One paragraph: what and why |
| **Learning objectives** | Bullet list of measurable outcomes |
| **Prerequisites** | Links to lessons this depends on |
| **Intuition** | Plain-language mental model before any math |
| **First principles** | The concept derived from the ground up |
| **Mathematics** (where relevant) | Formal treatment, clearly notated |
| **Code** | Minimal, runnable implementations |
| **In production** | How this appears in real systems, with pitfalls |
| **Common mistakes & debugging** | What goes wrong and how to diagnose it |
| **Exercises** | Link to `exercises/` |
| **Quiz** | Link to `quizzes/` |
| **Flashcards** | Link to `flashcards/` |
| **Summary** | Key takeaways as a table |
| **Further reading** | Links into [RESOURCES.md](RESOURCES.md) |

---

## Module 00 · Foundations & Engineering Setup

| # | Lesson | You will be able to… |
|:--:|---|---|
| 0.1 | What is an AI Engineer? | Distinguish AI Engineer vs ML Engineer vs Data Scientist and map the role's responsibilities |
| 0.2 | The AI systems landscape | Draw the end-to-end anatomy of a production AI system |
| 0.3 | The engineering environment | Set up reproducible Python/GPU environments with `uv`/`poetry`, VS Code, and notebooks |
| 0.4 | The experiment mindset | Track experiments, seed randomness, and reason about reproducibility |

## Module 01 · Advanced Python for AI

| # | Lesson | You will be able to… |
|:--:|---|---|
| 1.1 | Typing discipline | Use type hints and static checking to keep large AI codebases sane |
| 1.2 | Dataclasses & Pydantic | Model and validate structured data and LLM I/O |
| 1.3 | Iterators & generators at scale | Stream large datasets without exhausting memory |
| 1.4 | Async & concurrency | Choose async vs threads vs processes for AI workloads |
| 1.5 | Packaging & performance | Package projects, profile hot paths, and vectorize with NumPy |

## Module 02 · Math & ML Intuition

| # | Lesson | You will be able to… |
|:--:|---|---|
| 2.1 | Linear algebra for ML | Reason about vectors, matrices, and why models are matrix multiplications |
| 2.2 | Calculus & gradients | Explain how the chain rule powers learning |
| 2.3 | Probability & statistics | Apply distributions, expectation, and Bayes to modeling |
| 2.4 | Optimization intuition | Visualize loss surfaces and how gradient descent navigates them |

## Module 03 · Classical Machine Learning

| # | Lesson | You will be able to… |
|:--:|---|---|
| 3.1 | The ML workflow | Build a leak-free train/val/test pipeline |
| 3.2 | Bias–variance tradeoff | Diagnose under- and over-fitting |
| 3.3 | Linear & logistic regression | Implement both from scratch and interpret them |
| 3.4 | Trees & ensembles | Use random forests and gradient boosting effectively |
| 3.5 | Evaluation & error analysis | Select correct metrics and analyze failure modes |

## Module 04 · Deep Learning Foundations

| # | Lesson | You will be able to… |
|:--:|---|---|
| 4.1 | Neurons & networks | Explain forward passes and activations |
| 4.2 | Backpropagation from scratch | Derive and implement backprop by hand |
| 4.3 | PyTorch deeply | Use tensors, autograd, and modules fluently |
| 4.4 | Training in practice | Apply regularization, normalization, and good initialization |
| 4.5 | Debugging neural networks | Diagnose vanishing gradients, overfitting, and non-convergence |

## Module 05 · NLP & the Transformer

| # | Lesson | You will be able to… |
|:--:|---|---|
| 5.1 | Text representation | Compare tokenization schemes (BPE, WordPiece) |
| 5.2 | Embeddings | Explain and use word/sentence embeddings |
| 5.3 | From sequences to attention | Motivate attention from the limits of RNNs |
| 5.4 | The attention mechanism | Derive scaled dot-product and multi-head attention |
| 5.5 | Building a Transformer | Implement a Transformer block from scratch |

## Module 06 · Large Language Models

| # | Lesson | You will be able to… |
|:--:|---|---|
| 6.1 | Pretraining | Explain next-token prediction and scaling laws |
| 6.2 | Decoding strategies | Control generation with temperature and top-k/top-p |
| 6.3 | Context & memory | Explain context windows, positional encodings, and the KV cache |
| 6.4 | The LLM landscape | Select models by capability, cost, and licensing |

## Module 07 · Prompt Engineering

| # | Lesson | You will be able to… |
|:--:|---|---|
| 7.1 | Anatomy of a prompt | Structure system/user roles and constrained output |
| 7.2 | Reasoning techniques | Apply few-shot, chain-of-thought, and self-consistency |
| 7.3 | Reliable prompting | Enforce JSON schemas and test prompts systematically |

## Module 08 · Retrieval-Augmented Generation

| # | Lesson | You will be able to… |
|:--:|---|---|
| 8.1 | Why RAG | Explain grounding, hallucination, and knowledge cutoffs |
| 8.2 | Embeddings & vector databases | Choose chunking and indexing strategies |
| 8.3 | Retrieval quality | Improve results with hybrid search and reranking |
| 8.4 | Production RAG | Build and evaluate an end-to-end RAG pipeline |

## Module 09 · Fine-tuning & Adaptation

| # | Lesson | You will be able to… |
|:--:|---|---|
| 9.1 | Prompt vs RAG vs fine-tune | Choose the right adaptation strategy |
| 9.2 | Parameter-efficient fine-tuning | Apply LoRA/QLoRA/PEFT |
| 9.3 | Data curation | Build high-quality instruction datasets |
| 9.4 | Alignment basics | Explain RLHF and DPO at an engineering level |

## Module 10 · AI Agents & Tool Use

| # | Lesson | You will be able to… |
|:--:|---|---|
| 10.1 | Agent foundations | Explain the reasoning–action loop |
| 10.2 | Tools & function calling | Give models reliable structured actions |
| 10.3 | Orchestration | Build multi-step, memory-aware agents that recover from failure |

## Module 11 · LLMOps & Deployment

| # | Lesson | You will be able to… |
|:--:|---|---|
| 11.1 | Serving | Expose models via APIs with batching and streaming |
| 11.2 | Containerization | Package AI services with Docker |
| 11.3 | CI/CD for AI | Test, version, and safely roll out AI systems |
| 11.4 | Cost & reliability | Add caching, rate limiting, and budget controls |

## Module 12 · Scaling & Infrastructure

| # | Lesson | You will be able to… |
|:--:|---|---|
| 12.1 | GPUs & quantization | Optimize inference memory and speed |
| 12.2 | Distributed systems | Apply parallelism for training and serving |
| 12.3 | Cost & latency engineering | Hit throughput and latency targets economically |

## Module 13 · Evaluation & Observability

| # | Lesson | You will be able to… |
|:--:|---|---|
| 13.1 | Evaluating LLM systems | Build offline evals and LLM-as-judge pipelines |
| 13.2 | Observability | Trace, log, and monitor AI systems in production |
| 13.3 | Feedback loops | Design data flywheels and detect regressions |

## Module 14 · Safety, Security & Ethics

| # | Lesson | You will be able to… |
|:--:|---|---|
| 14.1 | LLM security | Defend against prompt injection and data exfiltration |
| 14.2 | Guardrails & red-teaming | Add safety layers and test them adversarially |
| 14.3 | Ethics & governance | Reason about privacy, bias, and responsible deployment |

## Module 15 · Capstone Projects

| # | Capstone | Deliverable |
|:--:|---|---|
| 15.1 | Production RAG assistant | Deployed, observable, evaluated RAG service |
| 15.2 | Tool-using agent | Multi-step agent with guardrails and monitoring |
| 15.3 | Interview & portfolio | System-design writeups and a polished public portfolio |

---

> [!NOTE]
> This curriculum is intentionally stable. New lessons should slot into existing modules rather than reshuffle the numbering — see [CONTRIBUTING.md](CONTRIBUTING.md).
