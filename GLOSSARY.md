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

## Linux for AI Engineers (Module 03)

| Term | Definition |
|---|---|
| **Kernel** | The core of the OS that manages hardware, processes, and memory (Linux is a kernel). |
| **Distribution (distro)** | A complete packaged OS built around the Linux kernel (Ubuntu, Fedora, Alpine). |
| **Shell** | A program (bash, zsh) that reads and runs your commands, composing tools via pipes. |
| **System call (syscall)** | A user-space program's request to the kernel for a privileged service (I/O, process, network). |
| **`strace`** | A tool that traces the system calls a program makes — for debugging what it tried to do. |
| **Pipe / redirection** | `\|` connects one program's stdout to another's stdin; `>`/`>>`/`2>&1` send streams to files. |
| **PATH** | The ordered list of directories the shell searches to find a command. |
| **Environment variable** | A named value available to the shell and its child processes (config/secrets). |
| **Symlink (symbolic link)** | A file that points to another path; used for atomic model/version swaps. |
| **Permissions / `chmod`** | Owner/group/other read-write-execute controls on files; `chmod` sets them. |
| **SUID** | A bit making an executable run with its owner's privileges (e.g., `passwd`) — security-critical. |
| **Process / daemon** | A running program; a daemon is a long-running background service process. |
| **`tmux`** | A terminal multiplexer whose sessions persist across disconnects — used for long training jobs. |
| **Signal (SIGTERM/SIGKILL)** | Messages to a process: SIGTERM = graceful shutdown, SIGKILL = force-kill. |
| **`nvidia-smi`** | The tool showing GPU utilization, memory, and processes — checked constantly in AI work. |
| **systemd** | The init system (PID 1) and service manager on most modern Linux distros. |
| **`journalctl`** | The command to read the systemd journal (service logs). |
| **SSH / SSH key** | Secure Shell for encrypted remote access; key-based auth uses a public/private key pair. |
| **`rsync`** | An efficient file-transfer/sync tool that copies only differences and can resume. |
| **Load average** | The average number of processes wanting to run (interpret relative to core count). |
| **Swap** | Disk-backed memory used when RAM is exhausted; heavy swap signals near-OOM. |
| **UFW / firewall** | A tool controlling which network ports accept connections (default-deny, allow needed). |
| **Fail2Ban** | A tool that auto-bans IPs after repeated failed logins (brute-force protection). |
| **Namespace** | A Linux kernel feature isolating a container's view (PIDs, network, filesystem, users). |
| **cgroup** | A Linux kernel feature limiting a process/container's resource use (CPU, memory, I/O). |
| **Container** | An isolated Linux process (namespaces + cgroups + union filesystem), not a virtual machine. |
| **OverlayFS / union filesystem** | Merges stacked, cached image layers into one filesystem view (Docker images). |

## Advanced Git & Collaboration (Module 04)

| Term | Definition |
|---|---|
| **Blob / tree / commit** | Git's core objects: a file's contents / a directory listing / a snapshot + parent(s) + metadata. |
| **Content addressing** | Storing objects keyed by the SHA hash of their content (gives deduplication and integrity). |
| **HEAD** | A pointer to the current branch (hence the current commit) — "where you are now." |
| **Reflog** | Git's record of every HEAD/branch-pointer move, used to recover "lost" commits. |
| **Detached HEAD** | HEAD pointing directly at a commit instead of a branch; commits there can be lost if you switch away without branching. |
| **Fast-forward / three-way merge** | Sliding a branch pointer forward (linear) / creating a merge commit with two parents when both branches diverged. |
| **Rebase** | Replaying commits onto a new base for linear history (creating new commit hashes). |
| **Interactive rebase** | `git rebase -i` — squash, reorder, reword, edit, or drop commits before sharing. |
| **Cherry-pick** | Copying a single commit onto the current branch. |
| **Reset (soft/mixed/hard)** | Moving a branch pointer, optionally unstaging and (hard) discarding uncommitted changes. |
| **Revert** | Creating a new commit that undoes a previous one — safe for shared history. |
| **Merge conflict** | When two branches change the same lines differently, requiring a human to resolve. |
| **Annotated tag** | A tag object (tagger, date, message, optional signature) used to mark releases. |
| **GitHub Flow / Git Flow / trunk-based** | Branching strategies: simple PR flow / structured release branches / frequent trunk integration. |
| **Pull request (PR)** | A request to merge a branch plus a space to review, discuss, and CI-check it. |
| **Protected branch** | A branch with enforced rules (require PR/review/CI, no force-push) protecting `main`. |
| **Squash merge** | Merging a PR as a single combined commit for a clean, linear history. |
| **CODEOWNERS** | A file mapping paths to owners so GitHub auto-requests their review. |
| **Git LFS** | Large File Storage — stores a pointer in Git and the actual large file in a separate store. |
| **`.gitignore`** | A file listing patterns Git should not track (data, caches, secrets). |
| **Git hook / pre-commit** | Scripts Git runs on events; the `pre-commit` framework runs shared checks before each commit. |
| **GitHub Actions / CI/CD** | GitHub's automation for running tests/lint on every push and deploying passing code. |
| **`git bisect`** | A binary search through history to find the commit that introduced a bug. |

## Databases & Data Engineering (Module 05)

| Term | Definition |
|---|---|
| **DBMS** | The software that stores, retrieves, and manages a database (e.g., PostgreSQL). |
| **Schema** | The structure and rules (tables, columns, types, constraints) data must follow. |
| **Primary / foreign key** | A row's unique identifier / a column referencing another table's PK, enforcing referential integrity. |
| **Normalization (3NF)** | Organizing tables so each fact is stored once, eliminating update/insert/delete anomalies. |
| **Denormalization** | Deliberately duplicating data to reduce JOINs and speed up reads (routine in analytics). |
| **JOIN (inner / left / anti)** | Combining tables: inner keeps only matches; left keeps all left rows; anti-join finds rows with no match. |
| **CTE** | A named subquery (`WITH`) making complex SQL readable and composable. |
| **Window function** | Computes a value per row over a window of related rows without collapsing them (ranking, running totals). |
| **Materialized view** | A stored, precomputed query result — a cache inside the database that must be refreshed. |
| **Execution plan** | The database's chosen strategy for a query, inspected with `EXPLAIN ANALYZE`. |
| **B-tree index** | The default balanced-tree index giving O(log n) lookups plus range and sort support. |
| **Composite / covering index** | An index on multiple columns (leftmost-prefix rule) / one containing all columns a query needs (index-only scan). |
| **ACID** | Atomicity, Consistency, Isolation, Durability — the transaction guarantees. |
| **Isolation level** | How much concurrent transactions may see of each other (Read Committed, Serializable, …). |
| **Lost update** | A race where two transactions read-modify-write and one overwrites the other. |
| **MVCC** | Multi-Version Concurrency Control — row versions so readers don't block writers. |
| **CAP theorem** | During a network partition, a distributed system must choose consistency or availability. |
| **OLTP / OLAP** | Transactional (application, normalized) vs analytical (warehouse, denormalized) workloads. |
| **Star schema** | An analytical model: a central fact table (measures + FKs) surrounded by denormalized dimensions. |
| **Fact / dimension table** | Events and measurements / descriptive context (who, what, when). |
| **SCD Type 2** | A slowly changing dimension that inserts a new row with valid_from/valid_to instead of overwriting. |
| **Data warehouse / lake / lakehouse** | Structured modeled analytics / raw cheap any-format storage / warehouse features on lake storage. |
| **Columnar storage** | Storing each column contiguously so analytical scans read only needed columns. |
| **ETL / ELT** | Transform-then-load vs load-raw-then-transform (the modern default). |
| **Idempotency** | Running an operation twice has the same effect as once — required for safe retries and backfills. |
| **Data lineage** | The record of where each table/column came from — used for debugging and blast-radius analysis. |
| **Data quality checks** | Assertions (nulls, uniqueness, ranges, freshness, volume) that block publication of bad data. |
| **Data leakage** | Information unavailable at prediction time entering training — inflates offline scores, fails in production. |
| **Training/serving skew** | Features computed differently at training vs serving, so the model sees unfamiliar inputs. |
| **Data drift** | The real-world input distribution changing over time, causing models to decay. |
| **Feature store** | A system providing one feature definition for both training (offline) and serving (online). |
| **Row-Level Security (RLS)** | Database policies that automatically filter every query (e.g., by tenant) — enforcing isolation. |
| **PITR** | Point-in-time recovery — restoring a database to any moment using backups plus the WAL. |
| **Connection pooling** | Reusing a bounded set of database connections (e.g., PgBouncer) instead of one per request. |
| **Read replica** | A read-only copy of the primary used to scale reads (with replication lag). |
| **Partitioning / sharding** | Splitting a table within one database / splitting data across machines (breaks cross-shard JOINs). |
| **Embedding** | A dense vector representing meaning, so semantically similar text lands nearby. |
| **ANN / HNSW** | Approximate nearest-neighbor search / the dominant graph-based ANN index. |
| **Vector database / pgvector** | A store for embeddings with similarity search / the Postgres extension providing it. |

---

## Mathematics for AI Engineers (Module 06)

### Linear algebra

| Term | Meaning |
|---|---|
| **Scalar / vector / matrix / tensor** | Rank 0/1/2/n arrays. In deep learning, "tensor" simply means an n-dimensional array. |
| **Dot product** | `Σ xᵢyᵢ` — measures **alignment** between two vectors. The atomic operation of AI. |
| **Cosine similarity** | The dot product with magnitude divided out — pure direction. The basis of semantic search. |
| **Matrix multiplication** | `(m,k)@(k,n)→(m,n)`. Represents **function composition**; >90% of a Transformer's FLOPs. |
| **Hadamard product (⊙)** | Element-wise multiplication (`*` in NumPy) — **not** matmul. |
| **Transpose** | Flipping rows and columns. `XᵀX` is the (unscaled) feature covariance matrix. |
| **Rank** | The number of dimensions a matrix's output actually uses — its real information content. |
| **Low-rank hypothesis** | Real matrices (and fine-tuning updates) use far fewer dimensions than their shape suggests. |
| **Determinant** | The factor by which a matrix scales volume. Zero ⟹ space collapsed ⟹ not invertible. |
| **Singular matrix** | det=0 / rank-deficient / zero eigenvalue / zero singular value / not invertible — all one picture. |
| **Eigenvector / eigenvalue** | A direction a matrix doesn't rotate (`Av = λv`) and its stretch factor. |
| **SVD** | `A = UΣVᵀ` — every matrix is rotate → stretch → rotate. The master decomposition. |
| **Eckart–Young theorem** | Truncating the SVD gives the *provably best* rank-k approximation. Underpins PCA and compression. |
| **PCA** | Center the data, take the SVD, keep the top-k directions of variance. |
| **Condition number** | σmax/σmin — how much a matrix amplifies numerical error. |
| **LoRA** | `W + BA` with rank r ≪ d — fine-tune with ~256× fewer trainable parameters. |

### Calculus & optimization

| Term | Meaning |
|---|---|
| **Derivative** | A **sensitivity**: how much the output changes when you nudge the input. |
| **Gradient (∇)** | The vector of partial derivatives — points in the direction of **steepest ascent**. |
| **Chain rule** | Sensitivities multiply along a chain. **This is backpropagation.** |
| **Backpropagation** | The chain rule applied right-to-left with cached activations — all gradients in one pass. |
| **Reverse-mode autodiff** | Why training is feasible: one backward pass for *all* parameters, not one per parameter. |
| **Jacobian / Hessian** | First derivatives of a vector function `(m,n)` / second derivatives of a scalar `(n,n)` (curvature). |
| **Vanishing / exploding gradients** | Per-layer factors compounding: 0.25ⁿ → 0, or 1.5ⁿ → ∞. |
| **Residual connection** | `x + f(x)` — its derivative is `1 + f′(x)`, a gradient highway that makes depth trainable. |
| **Saddle point** | A critical point that's up in some directions, down in others. The real obstacle in high dimensions. |
| **Gradient descent** | `θ ← θ − η∇L`. All of deep learning is this line. |
| **Learning rate (η)** | The step size — **the single most important hyperparameter**. Stability needs η < 2/λmax(H). |
| **Mini-batch SGD** | Estimate the gradient from a batch. Its **noise is a regularizer** that finds flat minima. |
| **Momentum** | Accumulate a velocity — kills ravine zig-zag, powers through plateaus and saddles. |
| **RMSProp / AdaGrad** | Per-parameter learning rates from an EMA (or sum) of squared gradients. |
| **Adam / AdamW** | Momentum + RMSProp + bias correction. AdamW decouples weight decay. **3× parameter memory.** |
| **Warmup + cosine decay** | The standard LR schedule. Warmup exists because Adam's variance estimate is unreliable at step 0. |
| **Convexity** | One global minimum, guaranteed convergence. **Neural networks are not convex** — and work anyway. |
| **Bias–variance tradeoff** | Underfitting (train↑ val↑) vs overfitting (train↓ val↑). |

### Probability, statistics & information

| Term | Meaning |
|---|---|
| **PMF / PDF** | Probability mass (discrete) / density (continuous). A PDF can exceed 1 — only *areas* are probabilities. |
| **Expectation 𝔼[·]** | The average, weighted by probability. In code: `.mean()`. |
| **Conditional probability** | `P(A|B)` — "A given B." **An LLM computes P(next token \| previous tokens).** |
| **Bayes' theorem** | `P(A|B) = P(B|A)P(A)/P(B)` — posterior = likelihood × prior / evidence. |
| **Base-rate fallacy** | A 99%-accurate test for a rare event yields mostly false positives. Why accuracy lies on imbalanced data. |
| **Marginalization** | Summing a joint distribution over a variable you don't care about — `.sum(axis=k)`. |
| **Chain rule of probability** | `P(w₁..wT) = ∏ P(wt | w<t)` — **the definition of an autoregressive language model**. |
| **i.i.d. assumption** | Independent and identically distributed. Violated by time series — random splits leak the future. |
| **He / Xavier initialization** | Weight init variance chosen to keep activations alive through depth (He: `√(2/n_in)`). |
| **Softmax / temperature** | Logits → probability distribution. Temperature sharpens (T<1) or flattens (T>1) it. |
| **Top-k / top-p (nucleus)** | Truncate the distribution before sampling. Top-p **adapts to model confidence**; top-k doesn't. |
| **Standard error** | `σ/√n` — **uncertainty shrinks as 1/√n**, so 4× the data halves your error bar. |
| **Confidence interval** | `x̄ ± 1.96·SE`. Report one on every metric. |
| **Bootstrap** | Resample → recompute → percentile. A CI for **any** metric, with no assumptions. |
| **p-value** | `P(data | H₀)` — **not** the probability the hypothesis is true. |
| **p-hacking** | Trying many variants and reporting the winner. 40 configs at α=0.05 → ~2 false wins by chance. |
| **Entropy** | Average surprise: `−Σ p log p`. A free per-token confidence signal from any model. |
| **Cross-entropy** | `−Σ p log q` — surprise using the wrong model. **The loss function of every classifier and LLM.** |
| **KL divergence** | `CE − entropy` — the *extra* cost of being wrong. Asymmetric. RLHF's leash; VAEs' regularizer. |
| **Perplexity** | `e^(cross-entropy)` — "effectively choosing among N tokens." Only comparable across identical tokenizers. |
| **Mutual information** | How much one variable tells you about another — captures **any** dependence, not just linear. InfoNCE/CLIP maximize it. |

### Numerical computing

| Term | Meaning |
|---|---|
| **float32 / bfloat16 / float16** | bf16 keeps float32's 8-bit **exponent** (range) and sacrifices precision — **deep learning needs range**. |
| **Machine epsilon** | The granularity of a float type (~1e-7 for float32). Why `0.1+0.2 != 0.3`. |
| **Overflow / underflow** | `exp(1000)` → inf / a product of 100 probabilities → 0. The two roads to NaN. |
| **Max-subtraction trick** | `z - z.max()` before softmax — mathematically a no-op, numerically essential. |
| **Log-sum-exp** | `max(x) + log Σ exp(x − max(x))` — a stable way to compute `log Σ exp(x)`. |
| **Log space** | `log ∏ p = Σ log p`. Every language model works here to avoid underflow. |
| **Catastrophic cancellation** | Subtracting near-equal numbers destroys precision — the naive variance formula can go *negative*. |
| **Vectorization** | Replacing Python loops with array ops. 100–1000× faster (SIMD, contiguity, threaded BLAS). |
| **Broadcasting** | Virtually stretching arrays to matching shapes. Compare from the right; `(n,)` vs `(n,1)` is a silent bug. |
| **keepdims** | Preserves the reduced axis so broadcasting aligns — prevents accidental outer operations. |

### Neural networks & Transformers

| Term | Meaning |
|---|---|
| **Forward / backward pass** | Compute the prediction and cache activations / compute all gradients via the chain rule. |
| **Activation function** | The nonlinearity. **Without it, any depth of linear layers collapses to one layer.** |
| **ReLU / GELU / SiLU** | ReLU's derivative is 1 (gradients survive depth). GELU/SiLU are smooth — no dead neurons. Used by Transformers. |
| **Dying ReLU** | A neuron stuck negative has gradient exactly 0 forever — it can never recover. |
| **Universal approximation** | An MLP can approximate any continuous function — true, and says nothing about *learnability*. |
| **Attention** | A **soft, differentiable dictionary lookup**: `softmax(QKᵀ/√dk)V`. |
| **Q / K / V** | Query ("what I want"), Key ("what I offer"), Value ("what I contribute") — all projections of the same input. |
| **√dk scaling** | Var(q·k) = dk; unscaled scores saturate the softmax and kill its gradient. A **variance fix**. |
| **Causal mask** | Lower-triangular masking of future tokens. **The only architectural difference between GPT and BERT.** |
| **Multi-head attention** | h heads at `dk = d/h` — many relationship-detectors for the FLOPs of one. Free. |
| **Positional encoding** | Mandatory, because attention is **permutation-invariant** — the price of trading sequentiality for parallelism. |
| **RoPE** | Rotate q,k by position so scores depend only on **relative** distance. Used by LLaMA/Mistral/Qwen. |
| **Layer normalization** | Normalize each token's features to mean 0, std 1 — keeps activations (and gradients) in a sane range. |
| **FFN** | The per-token MLP in a Transformer block (`d → 4d → d`). ~2/3 of all parameters; likely where facts are stored. |
| **O(n²) attention** | The score matrix is n×n — doubling context quadruples cost. The reason "long context" is a research field. |
| **FlashAttention** | **Identical math**, better memory access (tiling in SRAM). The bottleneck was memory traffic, not FLOPs. |
| **KV cache** | Caching past keys/values at generation time — the dominant memory cost of LLM inference. |

---

## Data Analysis, Scientific Computing & Visualization (Module 07)

### The lifecycle & its failures

| Term | Meaning |
|---|---|
| **AI data lifecycle** | Raw → collection → validation → cleaning → transformation → features → storage → training → evaluation → deployment → monitoring → *(loop back)*. **It is a loop, not a line.** |
| **Silent data bug** | A data failure that raises no exception — the model trains fine and is confidently wrong for months. The central problem of this module. |
| **Data leakage** | Information available at training but **not at prediction time**. Dangerous because **it looks like success**. |
| **Training/serving skew** | Features computed differently in production than in training (two diverging code paths). |
| **Data / concept / label drift** | P(X) changes / P(y\|X) changes (the *relationship*) / P(y) changes. |
| **Medallion (bronze/silver/gold)** | Raw-immutable → validated → ML-ready. **Never modify raw data.** |
| **Data-centric AI** | Holding the model fixed and improving the data. Architectures commoditized; **nobody can download your data.** |
| **Survivorship bias** | Building a training set from *current* entities, silently excluding everyone who already churned/failed/left. |

### NumPy

| Term | Meaning |
|---|---|
| **ndarray** | A header (dtype, shape, **strides**) over one contiguous C buffer. |
| **Strides** | Bytes to step to advance one index along an axis. Why `a.T` copies zero data. |
| **View vs copy** | Basic slicing/`.T`/`.reshape` return **views** (share memory — mutation propagates!); fancy and boolean indexing return **copies**. |
| **Vectorization** | Replacing Python loops with array ops. 100–10,000× (no boxing, no dispatch, SIMD, cache locality, threaded BLAS). |
| **Broadcasting** | Virtually stretching arrays to matching shapes. Compare from the right; equal or one is 1. |
| **`keepdims=True`** | Preserves the reduced axis so broadcasting aligns — prevents a silent `(n,)` vs `(n,1)` outer operation. |
| **Ufunc** | An element-wise compiled function with broadcasting built in. Use `out=` to avoid temporaries. |
| **Structured array** | A NumPy array with named heterogeneous fields (a C struct). Rarely the right choice — use Pandas. |

### Pandas

| Term | Meaning |
|---|---|
| **DataFrame** | A **dict of columns** (each a NumPy array) sharing one **Index**. Columns are fast; rows are slow. |
| **Index alignment** | Pandas aligns operations on **labels**, not position. A mismatched index yields **NaN, not an error**. |
| **`SettingWithCopyWarning`** | Chained indexing (`df[mask]['c'] = x`) assigns to an ambiguous view-or-copy — **the assignment may silently do nothing**. Use one `.loc[rows, cols] = v`. |
| **`category` dtype** | Stores unique values once + an integer code array. **10–50× memory reduction** on low-cardinality strings — the biggest win in Pandas. |
| **Nullable `Int64`** | Integer dtype that supports missing values (NumPy's `int64` has no NaN, so a null upcasts the column to float). |
| **Row explosion** | A many-to-many merge producing a **cartesian product** — every metric inflated, no error raised. |
| **`validate=`** | Merge argument that **raises** if key-uniqueness is violated. Turns a silent row explosion into a loud exception. |
| **Grain** | "One row per *what*?" — the question that prevents most join bugs. |
| **`transform`** | GroupBy mode returning the **same shape as the input** — broadcasts a group statistic onto every row. **The feature-engineering workhorse.** |
| **Long (tidy) vs wide** | One row per observation (for models and plots) vs one row per entity (for humans). |
| **Window operations** | `.rolling()`, `.expanding()`, `.ewm()`, `.shift()` — where time-aware features are born, and where leakage sneaks in. |

### Cleaning & EDA

| Term | Meaning |
|---|---|
| **MCAR / MAR / MNAR** | Missing completely at random (impute freely) / depends on *other observed* columns (impute conditionally) / **depends on the missing value itself — never impute; the missingness IS the signal**. |
| **The MNAR test** | Compare the **target rate** for rows where a column is missing vs present. If they differ, the missingness is predictive. |
| **Missing-indicator flag** | A boolean `x_missing` column — often *more* predictive than the column it came from. |
| **Disguised missingness / sentinel** | `-1`, `999`, `"N/A"` treated as real data — silently poisoning every statistic. Visible as a **spike in a histogram**, invisible in `describe()`. |
| **IQR / MAD outlier detection** | Median-based and robust. Preferred over the **z-score**, which is inflated by the very outliers it hunts. |
| **Winsorize / clip** | Capping extreme values instead of deleting the row. |
| **`log1p`** | `log(1+x)` — fixes right-skew (income, prices, counts) and handles zeros. **The most useful transform in applied data science.** |
| **Standardization / normalization / robust scaling** | `(x−μ)/σ` / `(x−min)/(max−min)` / `(x−median)/IQR`. **Fit on TRAIN only.** |
| **Target encoding** | Replacing a category with its mean target. **Must be out-of-fold** — the naive version leaks the label. |
| **Skewness / kurtosis** | Asymmetry / tail-heaviness. High kurtosis = extreme events are far more common than a normal predicts. |
| **Multicollinearity** | Features correlated with **each other** (ρ > 0.95) — makes linear coefficients unstable and splits feature importances. |
| **The leakage hunt** | Run *before* training: correlation > 0.9 with the target, single-feature AUC > 0.95, suspicious column names. |

### Features & visualization

| Term | Meaning |
|---|---|
| **Cyclical encoding** | `sin` **and** `cos` of a periodic feature, so hour 23 and hour 0 are adjacent. Both are needed — sine alone is ambiguous. |
| **Interaction feature** | `a × b`. Trees find these automatically; **linear models cannot** — a key reason GBMs win on tabular data. |
| **TF-IDF** | Term frequency × inverse document frequency — a word frequent *here* and rare *everywhere* is distinctive. A shockingly strong text baseline. |
| **Permutation importance** | Shuffle a feature, measure the damage **on validation**. Trustworthy, unlike tree importances (biased to high cardinality; split credit among correlated features). |
| **Overplotting** | A scatter with too many points becomes a blob. Fix with `alpha`, sampling, or **hexbin** (which shows density). |
| **Diverging colormap** | `RdBu_r` centered at 0 — **required** for correlation, or −0.9 looks as "low" as 0.0. |
| **k-anonymity** | Suppressing groups smaller than k (5–10) before publishing. **A group of size 1 IS that person's record.** |

### Quality, scale & pipelines

| Term | Meaning |
|---|---|
| **Six quality dimensions** | Completeness · Validity · **Accuracy** · Consistency · Timeliness · Uniqueness. |
| **Accuracy (the hard one)** | Requires an **external reference** — data can pass every internal check and be completely wrong (prices in cents). Only **reconciliation** catches it. |
| **Freshness / volume checks** | The two highest-value data tests. **A stale table looks perfectly healthy.** |
| **Quarantine** | Isolating failing rows + alerting — **never silently "fixing" them**, which hides the incident. |
| **PSI (Population Stability Index)** | A symmetrized KL divergence measuring drift. < 0.1 stable · 0.1–0.25 investigate · **> 0.25 retrain**. |
| **Data lineage** | Where did this come from? What breaks if I change it (**blast radius**)? Who owns it? |
| **Alert fatigue** | A check that fires daily gets muted — and then real incidents are invisible. **A wrong check is worse than no check.** |
| **Columnar storage (Parquet)** | Column pruning + better compression + **predicate pushdown** → 5–100× faster than CSV. |
| **Predicate pushdown** | Skipping whole row-groups using min/max statistics, without decompressing them. |
| **Chunking** | Processing data larger than RAM in pieces. Works only for **decomposable** operations (not median, joins, or sort). |
| **DuckDB** | SQL directly on Parquet files — no server, out-of-core, multi-threaded. **Most "we need Spark" is actually "we need DuckDB."** |
| **`fit` / `transform` contract** | `fit` learns from train; `transform` only applies. Makes leakage **structurally impossible**, not merely inadvisable. |
| **Manifest** | Per-run record: git SHA (+ **dirty flag**), input hash, config hash, seed, library versions. |
| **Dataset versioning** | **Never overwrite.** Without it, *"did the code change or the data change?"* is unanswerable. |
| **Pseudonymization at ingestion** | A separate `user_id → pseudonym` mapping table. **The only design that survives a GDPR deletion request** across immutable snapshots. |
| **The skew test** | Batch-transform must equal single-row transform. Catches the **all-zeros scaler** disaster in production. |
| **Group split** | Splitting by patient/photographer/product rather than randomly. **The #1 fix for medical-imaging leakage.** |
| **The validation gap** | A hole between train and test equal to the forecast horizon — without it, test rows' rolling features use training data. |
