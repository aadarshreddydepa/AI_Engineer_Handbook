# Curriculum

> The detailed learning outcomes for every module. Where [ROADMAP.md](ROADMAP.md) gives the schedule and dependencies, this document defines **what each module teaches and what you'll be able to do afterward**.

Every weekly lesson follows the same anatomy so the handbook reads like a single book.

---

## Lesson anatomy

Each lesson (`docs/<module>/weeks/week-NN.md`, built from [templates/lesson-template.md](templates/lesson-template.md)) contains these sections in order:

| Section | Purpose |
|---|---|
| **Overview** | What and why, in one paragraph |
| **Learning objectives** | Measurable outcomes |
| **Prerequisites** | Links to lessons this depends on |
| **Intuition** | Plain-language mental model before math |
| **First principles** | The concept from the ground up |
| **Mathematics** (where relevant) | Formal treatment, clearly notated |
| **Code** | Minimal, runnable implementations |
| **In production** | Real-world usage and pitfalls |
| **Common mistakes & debugging** | What breaks and how to diagnose it |
| **Exercises / Quiz / Flashcards** | Links to practice & retention |
| **Summary** | Key takeaways as a table |
| **Further reading** | Links into [RESOURCES.md](RESOURCES.md) |

---

## Module outcomes

### 00 · Orientation
Distinguish AI Engineer from adjacent roles; map an end-to-end AI system; set up a reproducible environment; adopt an experiment-tracking mindset.

### 01 · Advanced Python
Use typing and validation at scale; choose async vs threads vs processes; package, profile, and vectorize AI workloads.

### 02 · Computer Science
Analyze complexity; choose the right data structure; apply core algorithmic patterns; reason about memory and recursion.

### 03 · Linux
Work fluently in the shell; manage processes, permissions, and environments; operate remote servers.

### 04 · Git
Explain the object model; run team workflows; keep clean history; version experiments and large files.

### 05 · SQL
Model relational data; write joins, aggregations, and window functions; index and optimize; embed SQL in pipelines.

### 06 · Mathematics
Reason about vectors and matrices; explain gradients and the chain rule; apply probability and statistics; visualize optimization.

### 07 · Data Analysis
Vectorize with NumPy; wrangle data with pandas; run EDA; communicate findings visually.

### 08 · Machine Learning
Build leak-free ML pipelines; implement core models; diagnose bias/variance; choose metrics and analyze errors.

### 09 · Deep Learning
Derive and implement backprop; use PyTorch fluently; apply regularization/normalization; debug neural nets.

### 10 · NLP
Compare tokenizers; use embeddings; derive attention; build a Transformer block from scratch.

### 11 · LLMs
Explain pretraining and scaling laws; control decoding; reason about context/KV-cache; select models by cost and capability.

### 12 · Prompt Engineering
Structure prompts and roles; apply few-shot, chain-of-thought, and self-consistency; enforce structured output with schemas and guardrails; test, evaluate, and version prompts.

### 13 · RAG
Explain grounding and hallucination; design chunking and vector indexing; improve retrieval with hybrid search and reranking; evaluate RAG.

### 14 · AI Agents
Explain the reasoning–action loop; implement reliable tool use; orchestrate multi-step, memory-aware agents that recover from failure.

### 15 · Fine-tuning
Decide when to fine-tune vs prompt vs RAG; apply parameter-efficient fine-tuning (LoRA/QLoRA/PEFT); curate instruction data; explain alignment (RLHF/DPO) at an engineering level.

### 16 · MLOps
Serve models via APIs; containerize deployments; build CI/CD and safe rollouts; track experiments and models.

### 17 · Cloud
Use cloud compute/storage/networking; run containers and serverless; provision GPUs; manage cost and infrastructure-as-code.

### 18 · System Design
Apply system-design fundamentals and tradeoffs; design scalable LLM/RAG/agent systems; reason about reliability and bottlenecks.

### 19 · Production AI
Build production evals and LLM-as-judge; add observability; defend against prompt injection with guardrails; engineer latency and cost.

### 20 · Interview Preparation
Solve DSA under pressure; handle ML/LLM conceptual interviews; run AI system-design interviews; tell strong behavioral and portfolio stories.

### 21 · Capstone Projects
Scope, build, harden, observe, and document end-to-end production AI systems worthy of a public portfolio.

---

> [!NOTE]
> This curriculum is intentionally stable. New lessons slot into existing modules rather than reshuffle numbering — see [CONTRIBUTING.md](CONTRIBUTING.md). Full per-module lesson lists are authored alongside each module.
