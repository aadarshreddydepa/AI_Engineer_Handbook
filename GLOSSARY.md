# Glossary

> The master glossary for the handbook. Every term used in a lesson is defined here on first use and linked back. Terms are grouped by theme and sorted alphabetically within each group.

> [!NOTE]
> This is a seed glossary covering core vocabulary. Per-topic fragments live in [glossary/](glossary/) and are merged here as modules are authored. When you add a new term to a lesson, add it here too (see [CONTRIBUTING.md](CONTRIBUTING.md)).

---

## Foundations & ML

| Term | Definition |
|---|---|
| **AI Engineer** | An engineer who designs, builds, deploys, and maintains production systems powered by AI/ML models, especially foundation models. |
| **Model** | A parameterized function learned from data that maps inputs to outputs. |
| **Training** | The process of adjusting a model's parameters to reduce a loss on data. |
| **Inference** | Using a trained model to produce outputs for new inputs. |
| **Feature** | An input variable used by a model. |
| **Label** | The target output a supervised model learns to predict. |
| **Overfitting** | When a model memorizes training data and fails to generalize. |
| **Underfitting** | When a model is too simple to capture the underlying pattern. |
| **Bias–variance tradeoff** | The tension between error from wrong assumptions (bias) and error from sensitivity to data (variance). |
| **Generalization** | A model's performance on unseen data. |
| **Loss function** | A scalar measure of how wrong a model's predictions are. |
| **Gradient descent** | An optimization method that steps parameters opposite the gradient of the loss. |

## Deep Learning

| Term | Definition |
|---|---|
| **Neural network** | A model built from layers of interconnected units (neurons) applying weighted sums and nonlinearities. |
| **Activation function** | A nonlinear function (e.g. ReLU) applied to a neuron's output. |
| **Backpropagation** | The algorithm that computes gradients of the loss w.r.t. every parameter via the chain rule. |
| **Epoch** | One full pass over the training dataset. |
| **Batch** | A subset of data processed together in one optimization step. |
| **Regularization** | Techniques (e.g. dropout, weight decay) that reduce overfitting. |
| **Tensor** | A multi-dimensional array; the core data structure in DL frameworks. |
| **Autograd** | Automatic differentiation that builds and traverses a computation graph. |

## NLP & Transformers

| Term | Definition |
|---|---|
| **Token** | The unit of text a model processes (subword, word, or character). |
| **Tokenization** | Converting raw text into tokens (e.g. BPE, WordPiece). |
| **Embedding** | A dense vector representation of a token or piece of data. |
| **Attention** | A mechanism letting a model weigh the relevance of other tokens when representing one token. |
| **Self-attention** | Attention where queries, keys, and values come from the same sequence. |
| **Transformer** | A neural architecture built on attention, the backbone of modern LLMs. |
| **Positional encoding** | Information added to embeddings so the model knows token order. |

## Large Language Models

| Term | Definition |
|---|---|
| **LLM** | A large language model trained on vast text to predict and generate language. |
| **Pretraining** | Large-scale self-supervised training (typically next-token prediction). |
| **Next-token prediction** | The objective of predicting the following token given prior context. |
| **Scaling laws** | Empirical relationships between model/data/compute size and performance. |
| **Context window** | The maximum number of tokens a model can attend to at once. |
| **KV cache** | Cached key/value tensors that speed up autoregressive generation. |
| **Temperature** | A decoding parameter controlling randomness of generation. |
| **Top-k / Top-p (nucleus)** | Decoding strategies that restrict sampling to the most likely tokens. |
| **Hallucination** | Confident but false or unsupported model output. |

## Applied LLM Engineering

| Term | Definition |
|---|---|
| **Prompt** | The input text/instructions given to an LLM. |
| **System prompt** | Instructions that set an assistant's role and constraints. |
| **Few-shot prompting** | Providing examples in the prompt to guide behavior. |
| **Chain-of-thought** | Prompting a model to reason step by step. |
| **RAG** | Retrieval-Augmented Generation: grounding a model with retrieved external documents. |
| **Vector database** | A store optimized for similarity search over embeddings. |
| **Chunking** | Splitting documents into pieces for embedding and retrieval. |
| **Reranking** | Reordering retrieved candidates by relevance before generation. |
| **Fine-tuning** | Further training a pretrained model on task-specific data. |
| **LoRA** | Low-Rank Adaptation, a parameter-efficient fine-tuning method. |
| **PEFT** | Parameter-Efficient Fine-Tuning, a family of methods that train few parameters. |
| **RLHF** | Reinforcement Learning from Human Feedback, an alignment technique. |
| **DPO** | Direct Preference Optimization, an alignment method using preference pairs. |
| **Agent** | An LLM-driven system that reasons and takes actions via tools in a loop. |
| **Function calling / tool use** | A model producing structured calls to external tools. |

## Production & Ops

| Term | Definition |
|---|---|
| **LLMOps** | Practices for deploying, monitoring, and maintaining LLM systems. |
| **Serving** | Exposing a model for inference, typically behind an API. |
| **Batching** | Grouping requests to improve throughput. |
| **Streaming** | Returning output tokens incrementally as they are generated. |
| **Quantization** | Reducing numeric precision of weights to save memory and speed inference. |
| **Observability** | The ability to understand a system's behavior via logs, traces, and metrics. |
| **LLM-as-judge** | Using an LLM to evaluate outputs of another model. |
| **Prompt injection** | An attack that manipulates a model via crafted input to override instructions. |
| **Guardrails** | Controls that constrain model inputs/outputs for safety and reliability. |

## Foundations, Engineering & Learning (Module 00)

| Term | Definition |
|---|---|
| **AI Engineering** | The discipline of designing, building, deploying, scaling, and maintaining production systems built around AI/foundation models. |
| **AGI (Artificial General Intelligence)** | Hypothetical human-level, general-purpose intelligence across all domains; a research goal, not a shippable product. |
| **Generative AI** | Deep learning that produces new content (text, images, audio, video, code) rather than only classifying or predicting. |
| **Narrow AI** | AI competent at a specific task or domain (all AI that exists today), as opposed to AGI. |
| **Virtual environment** | An isolated, per-project Python interpreter plus that project's packages, preventing cross-project conflicts. |
| **Reproducibility** | The ability to rebuild an identical environment or result on any machine from declared files (e.g. `pyproject.toml` + lockfile). |
| **Package manager** | A tool (e.g. `uv`, `poetry`) that resolves, locks, and declares project dependencies. |
| **Lockfile** | A file pinning the exact versions of all (including transitive) dependencies for reproducible installs. |
| **Formatter** | A tool that standardizes how code looks (e.g. `ruff format`). |
| **Linter** | A tool that flags likely bugs and bad patterns (e.g. `ruff check`). |
| **Semantic Versioning (SemVer)** | A `MAJOR.MINOR.PATCH` versioning scheme: breaking / backward-compatible feature / backward-compatible fix. |
| **Conventional Commits** | A commit-message convention of the form `type(scope): summary` (e.g. `feat`, `fix`, `docs`). |
| **Changelog** | A human-readable, versioned list of notable project changes (Added/Changed/Fixed/Removed). |
| **Branch** | An isolated line of work in Git, keeping risky changes off the always-working main branch. |
| **Three-pass method** | Reading a research paper in three increasingly deep passes (gist → idea → reimplement). |
| **Active recall** | Learning by retrieving information from memory rather than rereading. |
| **Spaced repetition** | Reviewing material at expanding intervals to counteract forgetting. |
| **Interleaving** | Mixing multiple topics during review to strengthen retrieval and discrimination. |
| **Diátaxis** | A documentation framework distinguishing tutorials, how-to guides, reference, and explanation. |

## Advanced Python (Module 01)

| Term | Definition |
|---|---|
| **CPython** | The reference C implementation of Python that virtually everyone (and every AI framework) uses. |
| **Bytecode** | Compact, stack-machine instructions Python compiles source into, executed by the PVM. |
| **PVM (Python Virtual Machine)** | The bytecode-interpreting evaluation loop inside CPython. |
| **GIL (Global Interpreter Lock)** | CPython's lock allowing only one thread to run Python bytecode at a time. |
| **Reference counting** | CPython's primary memory management: an object is freed when its reference count hits zero. |
| **Garbage collection (cyclic)** | The generational collector that reclaims unreachable reference cycles refcounting can't. |
| **Aliasing** | Two or more names bound to the same object, so changes via one are visible via the others. |
| **Closure** | A function that captures (by reference) variables from its enclosing scope. |
| **Higher-order function** | A function that takes and/or returns other functions. |
| **Decorator** | A callable that takes a function/class and returns an enhanced one (`@dec` == `f = dec(f)`). |
| **Iterator / iterable** | An iterable has `__iter__`; an iterator (from `iter()`) has `__next__` and raises `StopIteration`. |
| **Generator** | A pausable function using `yield` that produces values lazily, one at a time. |
| **Lazy evaluation** | Computing values only when needed, enabling constant-memory processing of large data. |
| **Context manager** | An object with `__enter__`/`__exit__` used with `with` to guarantee setup/cleanup. |
| **Type hint** | An optional annotation of expected types, checked statically (e.g. by mypy), ignored at runtime. |
| **Protocol** | A structural (duck-typed) interface: any object with the right methods conforms, without inheritance. |
| **Pydantic** | A library that uses type annotations to validate and parse data at runtime (e.g. LLM output). |
| **Coroutine** | An `async def` function that can suspend at `await`, scheduled by the asyncio event loop. |
| **Event loop** | The asyncio scheduler that runs, suspends, and resumes coroutines cooperatively. |
| **Memoization** | Caching a pure function's results by input (e.g. `functools.lru_cache`). |
| **Vectorization** | Expressing numeric loops as array operations executed in optimized C (e.g. NumPy). |
| **Editable install** | Installing a package (`pip install -e .`) so it's importable and reflects live edits. |
| **Lockfile** | A file pinning exact versions of all dependencies for reproducible installs. |
| **Pre-commit hook** | A Git hook running quality checks (lint/format/type) automatically before each commit. |

## Computer Science Foundations (Module 02)

| Term | Definition |
|---|---|
| **Memory hierarchy** | The tiered speed/size layers: registers → L1/L2/L3 cache → RAM → SSD → HDD/network. |
| **Cache line** | The fixed chunk (~64 bytes) memory is moved in; the reason contiguous access is fast. |
| **Cache locality** | Fast access from reusing recently/nearby data that stays in cache. |
| **Stack (memory)** | The region holding call frames and locals; fast, automatic, LIFO, size-limited. |
| **Heap (memory)** | The region for dynamically allocated objects; larger, GC/manually managed. |
| **Fragmentation** | Free memory scattered in non-contiguous gaps so large allocations fail (e.g., CUDA OOM). |
| **Hash table** | A structure mapping keys to values via a hash function; O(1) average lookup. |
| **Heap (data structure)** | A tree giving O(1) access to the min/max and O(log n) insert/pop; used for top-k. |
| **Trie** | A prefix tree storing strings by shared prefixes; O(k) lookup by key length. |
| **Graph** | Vertices connected by edges; models relationships (computation graphs, HNSW, agents). |
| **Big-O / Big-Omega / Big-Theta** | Upper / lower / tight bounds on how an algorithm's cost grows with input size. |
| **Process** | A running program with its own isolated memory space. |
| **Thread** | A unit of execution within a process, sharing the process's memory. |
| **Context switch** | Saving one thread/process's state and loading another's; disrupts the CPU cache. |
| **Race condition** | A bug whose outcome depends on unpredictable thread timing on shared state. |
| **Deadlock** | Threads waiting forever for each other's resources (circular wait). |
| **Virtual memory** | Per-process private address space mapped to physical RAM/disk via paging. |
| **Page cache** | RAM caching of recently-read file data, making repeat reads fast. |
| **TCP / UDP** | Reliable ordered / fast best-effort transport protocols. |
| **DNS** | The system translating domain names to IP addresses. |
| **HTTP / HTTPS** | The request/response web protocol / its TLS-encrypted form. |
| **REST / gRPC / WebSocket** | Request-response APIs / HTTP-2+Protobuf RPC / persistent bidirectional connections. |
| **Load balancer** | Distributes requests across multiple server instances for scale and availability. |
| **Reverse proxy** | A server fronting backends for TLS, routing, auth, and rate limiting. |
| **Serialization / deserialization** | Converting objects to bytes for storage/transport, and back. |
| **Horizontal / vertical scaling** | Adding more machines / making one machine bigger. |
| **Statelessness** | Keeping no per-client state so any instance can serve any request (enables scaling). |
| **Fault tolerance** | A system's ability to keep working when components fail. |
| **Stack trace (traceback)** | The chain of function calls at the moment of an error. |
| **Observability** | Understanding a system's behavior via logs, metrics, and traces. |
