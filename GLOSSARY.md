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

---

## Machine Learning Foundations (Module 08)

### Foundations

| Term | Meaning |
|---|---|
| **Machine learning** | data + answers → **rules** (traditional programming is rules + data → answers). |
| **The test for ML** | **"Can you write the rule?"** If yes, write the rule. ML is for rules too complex/fuzzy/changeable to state. |
| **Supervised / unsupervised** | Learns from labeled `(X, y)` pairs / from the data's own structure. |
| **Self-supervised** | ⭐ **The data labels itself** ("predict the next word"). Removed the label bottleneck; made LLMs possible. |
| **The four boxes** | Every supervised algorithm = **model · loss · optimizer · predict**. "Learning" is just optimization. |
| **Inductive bias** | **Every algorithm is a bet about the shape of your data.** The one whose bet matches reality wins. |
| **Baseline** | "Predict the majority class / the mean." **A shocking number of production models don't beat it.** |
| **Bias–variance tradeoff** | Error = bias² (too simple) + variance (too sensitive) + irreducible noise. |
| **Underfit / overfit** | Train err high + val err high / train err low + val err high. **They need opposite fixes.** |
| **Learning curve** | Train/val error vs training-set size. **Answers "would more data help?"** — flat val curve = no. |
| **⭐ Error analysis** | **Look at 100 misclassified examples by hand.** Beats any amount of tuning; ~15% turn out to be mislabeled. |
| **Regularization** | `loss + λ·complexity` — the same shape as **Ridge**, **tree pruning**, the **SVM margin**, and **Laplace smoothing**. |
| **L1 vs L2** | L1's constraint diamond has **corners on the axes** → coefficients hit exactly **zero** → free feature selection. L2's circle doesn't. |

### Algorithms

| Term | Meaning |
|---|---|
| **Normal equations** | $w = (X^\top X)^{-1}X^\top y$. Exact but O(d³) and fragile. **Use `solve`, never `inv`.** |
| **⭐ Ridge** | L2 regularization. $+\lambda I$ **adds λ to every eigenvalue** → $X^\top X + \lambda I$ is **always invertible**. |
| **Lasso** | L1 — drives coefficients to exactly zero (feature selection), but arbitrarily picks one of a correlated pair. |
| **Sigmoid / logit** | $\sigma(z)=1/(1+e^{-z})$; its inverse is the **log-odds**. Logistic regression assumes the log-odds are linear. |
| **⭐ Odds ratio** | $e^{w_j}$ — *"smoking doubles your odds."* Why medicine and credit scoring still use logistic regression. |
| **⭐ Log-loss** | Binary cross-entropy. Its gradient is $\frac{1}{n}X^\top(\hat p - y)$ — **identical to linear regression's**; the σ′ cancels. |
| **Entropy / Gini** | $-\sum p\log p$ / $1-\sum p^2$ — measures of node impurity. **They pick the same splits ~98% of the time.** |
| **Information gain** | $H(\text{parent}) - \sum\frac{n_k}{n}H(\text{child}_k)$ — the tree's splitting criterion. |
| **Pruning** | Pre- (`max_depth`, `min_samples_leaf`) or post- (**cost-complexity**, $R(T)+\alpha|\text{leaves}|$). |
| **Bootstrap / bagging** | Sample n rows **with replacement** (~63.2% in-bag). Train deep trees in parallel and **average** → **reduces variance**. |
| **⭐ OOB score** | The ~36.8% left out of each bootstrap = **free cross-validation**, no extra fitting. |
| **⭐⭐ The ensemble variance formula** | $\rho\sigma^2 + \frac{1-\rho}{M}\sigma^2$ — **the entire game is decorrelating the models (lowering ρ)**. |
| **`max_features`** | ⭐ RF's key knob. **Deliberately handicapping each tree decorrelates the forest and makes it better.** |
| **⭐ Gradient boosting** | Sequential **shallow** trees fitting the **residuals** — which **are the negative gradient**. It's **gradient descent in function space**. |
| **Shrinkage** | The learning rate in boosting — the primary regularizer. **lr × n_estimators ≈ constant.** |
| **Support vector** | A point **on or inside the SVM margin** — **the only points that determine the hyperplane.** |
| **Hinge loss** | $\max(0, 1-y\cdot z)$ — **exactly zero past the margin** → zero gradient → **that's where the sparsity comes from**. |
| **⭐⭐ Kernel trick** | The data appears **only in dot products**, so swap $x^\top x'$ for $K(x,x')$ → **infinite-dimensional power at O(d) cost**. |
| **RBF kernel** | $\exp(-\gamma\|x-x'\|^2)$ — maps into an **infinite-dimensional** space. `gamma` = influence width. |
| **The naive assumption** | Features are conditionally independent given the class. **Obviously false — works anyway**, because classification needs only the correct **ranking**. |
| **Laplace smoothing** | Add α to every count — without it, **one unseen word gives P=0** and vetoes all other evidence. |
| **⭐ Lazy learner** | KNN: O(1) training, **O(n·d) per query**. The training data **IS** the model. |
| **⭐⭐ Curse of dimensionality** | As d grows, **all distances converge** — "nearest" stops meaning anything. Breaks KNN, K-Means, RBF-SVM, KD-trees. |
| **Why RAG escapes it** | ⭐ **Learned embeddings live on a low-dimensional manifold** — the curse applies to *random* high-d data, not structured representations. |
| **ANN / HNSW** | Approximate nearest neighbor — ~99% recall for a ~1000× speedup. **RAG = cosine-KNN + ANN.** |
| **K-Means / Lloyd's algorithm** | Assign → update → repeat. **Converges, but not to the global optimum** (non-convex) → `n_init` + **k-means++**. |
| **Silhouette / the elbow** | $(b-a)/\max(a,b)$ (has a real maximum) / inertia vs k (**always decreases — unreliable**). |
| **⭐⭐ The null test** | **Shuffle the data, re-cluster, compare silhouettes.** If noise scores as well, **you found nothing.** |
| **DBSCAN** | Density-based: **any shape, finds k itself, labels noise** (`-1`). **Fails with varying densities** → HDBSCAN. |
| **PCA** | SVD of the **centered** data. Right singular vectors = the principal components. **Centering is mandatory.** |
| **⭐ t-SNE's traps** | Cluster **sizes** meaningless · **distances between clusters** meaningless · **it invents clusters in noise** · **cannot `transform()` new points**. |

### Evaluation, leakage & production

| Term | Meaning |
|---|---|
| **Precision / recall** | *"When I say yes, am I right?"* / *"Did I find them all?"* **They trade off.** |
| **⭐ Why accuracy lies** | On imbalanced data, predicting the majority class gets **99% while catching nothing**. |
| **⭐⭐ ROC-AUC vs PR-AUC** | ROC's **FPR denominator (FP+TN)** is dominated by the huge negative class → **optimistic**. **PR-AUC has no TN** → honest. Use it when positives < ~10%. |
| **⭐⭐ Threshold tuning** | **0.5 is a default, not a decision.** Derive it from the **cost of FP vs FN**. **Free, and routinely beats every model improvement.** |
| **Calibration** | *"Is a 0.8 prediction right 80% of the time?"* LR ✅ · **Naive Bayes ❌ wildly overconfident** · NNs ❌. |
| **StratifiedKFold / GroupKFold / TimeSeriesSplit** | Preserve class ratios / **keep a group in one fold** / **train always precedes test, with a gap**. |
| **⭐⭐ The four leaks that survive CV** | **(1) preprocessing outside the loop** · (2) **feature selection before CV** (→ 90% accuracy on noise) · (3) duplicates across folds · (4) **target leakage — which CV cannot catch**. |
| **Nested CV** | Inner loop selects hyperparameters; outer loop estimates performance. **The naive best-CV score is optimistically biased.** |
| **⭐ MDI bias** | `feature_importances_` is **biased toward high-cardinality features** (a random ID column ranks top-5) and **splits credit among correlated ones**. |
| **⭐ Permutation importance** | Shuffle a feature, measure the damage — **on validation**. The one to trust. |
| **⭐⭐ SHAP** | Shapley values — the **unique** attribution satisfying **efficiency, symmetry, dummy, additivity**. **A theorem, not a heuristic.** |
| **⭐ SHAP's best use** | **Finding your own leaks.** A feature with 80% of the SHAP mass is a **bug report**. |
| **PDP / ICE / ALE** | Partial dependence (**lies when features are correlated** — "8-bedroom studios") / per-individual curves / **the correct version**. |
| **⭐ Fairness impossibility** | Demographic parity, equal opportunity, and equalized odds are **mathematically incompatible**. **Choose one deliberately.** |
| **Proxy** | ⭐ **Removing `race` doesn't remove race** — zip code reconstructs it. It only removes your ability to **measure**. |
| **⭐ Random > grid search** | **Most hyperparameters don't matter**, so a grid wastes its budget re-testing the same few values of the one that does. |
| **Successive halving / Hyperband** | Start many configs on a small budget, kill the worst, promote the survivors. 3–10× faster. |
| **⭐ Prefer the plateau** | A lone spike in CV score is luck; a **broad flat region** is a robust setting. |
| **⭐⭐ Monitor the inputs** | Performance needs **labels**, which arrive **months** late. **Input drift (PSI) and the prediction distribution are LEADING indicators.** |
| **The prediction-distribution canary** | ⭐ The cheapest, best drift signal — **no labels required**. |
| **⭐⭐ The retraining gate** | Reject a new model if it's worse, if the data failed validation, or if behaviour shifted. **Automated retraining without a gate is automated self-destruction.** |
| **Feedback loop** | The model's own recommendations become its training data → **it confirms its own beliefs**. |
| **Shadow mode** | ⭐ Run the new model on real traffic, log what it *would* have done, **don't act on it.** Real evidence, zero risk. |

---

## Deep Learning Systems with PyTorch (Module 09)

### Foundations & neurons

| Term | Meaning |
|---|---|
| **⭐ Representation learning** | The one thing deep learning changed: **the network learns the features itself**, layer by layer, instead of a human engineering them. |
| **Feature hierarchy** | Early layers → edges/textures; middle → parts; late → objects. **Each layer makes the next one's job easier.** |
| **Artificial neuron** | A **dot product + bias through a nonlinearity**: $\sigma(\mathbf{w}\cdot\mathbf{x}+b)$. **Its weights *are* the pattern it detects.** |
| **⭐ A layer** | One **matmul + bias + elementwise activation**. Why >90% of a net's FLOPs are matmuls and why nets run on GPUs. |
| **⭐ Why nonlinearity is mandatory** | Stacked Linear layers **collapse to one** ($W_2(W_1x+b_1)+b_2 = W'x+b'$). Without activations, 100 layers = logistic regression. |
| **Affine transformation** | Linear map **+ a shift** ($Wx+b$). "Linear" / "dense" / "fully-connected" all name the same layer; the bias is the shift. |
| **ReLU** | $\max(0,x)$. Derivative **exactly 1 when active** → nothing vanishes. Beat sigmoid for hidden layers for this reason. |
| **Dying ReLU** | A neuron stuck negative → outputs 0 with **gradient 0 forever**. Fix: Leaky ReLU / GELU. |
| **⭐ Universal approximation** | A big-enough net approximates any function — **but "enough" may be astronomical, and existence ≠ learnability ≠ generalization.** Depth (not width) makes it practical. |
| **Where DL loses** | ⭐ **Tabular data** — gradient boosting still wins (faster, cheaper, interpretable). DL's home turf is **perception and language.** |
| **Why 2012** | **Data (ImageNet) + compute (GPUs) + tricks (ReLU, dropout).** The ideas were from the 1980s; the fuel was new. |

### The math, loss & backprop

| Term | Meaning |
|---|---|
| **⭐ Loss takes logits** | `CrossEntropyLoss` fuses **softmax + log + NLL** for numerical stability. **Applying softmax yourself applies it twice** and wrecks training. |
| **`BCEWithLogitsLoss`** | The binary equivalent (fuses sigmoid + BCE). Rule: **model outputs logits; the loss applies the final activation.** |
| **⭐ The `ln(C)` sanity check** | An untrained C-class classifier's loss should be **≈ ln(C)** (2.30 for 10 classes). If not, there's a bug **before** training. |
| **⭐ Backpropagation** | The **chain rule applied right-to-left, with forward activations cached**. Not a new algorithm — just the efficient ordering (reverse-mode autodiff). |
| **Reverse mode** | One output (loss), millions of inputs (weights) → **all gradients in one backward pass.** Forward mode would need one pass per parameter. |
| **⭐ The gradient of the fused loss** | `predicted − actual` — the same clean form seen in linear and logistic regression. |
| **The four backward rules** | `Z=A@W` → `dW=A.T@dZ`, `dA=dZ@W.T`; `Z=A+b` → `db=dZ.sum(0)`; `A=f(Z)` → `dZ=dA*f'(Z)`; softmax+CE → `dZ=(p−y)/B`. |
| **Shape-matching** | You derive *which* term is transposed because **`dW` must match `W`'s shape** — only one arrangement produces it. |
| **⭐ Gradient checking** | Compare the analytical gradient to a **central finite difference** — the unit test for backprop. **Use float64; never during training.** |
| **⭐ Vanishing / exploding gradient** | Chain rule multiplies per-layer derivatives → $\lambda^n$. Fixes: **ReLU, residual connections, normalization, careful init.** |
| **Activation cache** | Every forward activation must be **kept until backprop consumes it** → training uses ~3–4× the memory of inference. |

### Optimization

| Term | Meaning |
|---|---|
| **Backprop vs optimizer** | **Backprop computes the gradient; the optimizer decides what to do with it.** Separate jobs. |
| **Momentum** | EMA of the gradient (1st moment) — smooths the path, powers through ravines. |
| **RMSProp** | EMA of the *squared* gradient (2nd moment) — gives **each parameter its own effective learning rate.** |
| **⭐ Adam** | **Momentum + RMSProp + bias correction.** Twelve lines. It trained GPT. |
| **⭐ AdamW** | Adam with **decoupled weight decay** (applied to the weights, not folded into the gradient). **The default for every modern model.** |
| **⭐ Adam's 3× memory** | Stores **m and v — two extra copies of every parameter.** Why fine-tuning OOMs while inference fits; a core motivation for **LoRA**. |
| **⭐ Learning rate** | **The #1 hyperparameter, by a wide margin.** A well-tuned SGD beats a badly-tuned Adam. |
| **Warmup + cosine** | Small LR at first (Adam's 2nd-moment estimate is unreliable early), then decay. Standard for Transformers. |

### PyTorch, autograd & models

| Term | Meaning |
|---|---|
| **⭐ Tensor** | A NumPy array **+ a device (GPU) + an autograd tape.** Strip those two away and it's NumPy. |
| **⭐ #1 runtime error** | *"Expected all tensors on the same device."* Fix: **move the model once at setup, every batch inside the loop** (`X.to(device)`). |
| **`from_numpy` gotcha** | ⭐ **Shares memory** (no copy) — mutating the array mutates the tensor. Use `torch.tensor(a)` to copy. |
| **bfloat16 vs float16** | bf16 keeps **float32's range** (won't overflow) and drops precision. **Why every LLM trains in bf16.** |
| **⭐ `cuda.synchronize()`** | GPU ops are **asynchronous** — you must sync before timing, or you measure the *launch*, not the *work*. |
| **⭐ Autograd** | Records ops on `requires_grad` tensors; `backward()` walks the graph applying the chain rule. **It's the `backward()` you hand-wrote, automated.** |
| **⭐ Dynamic graph** | Built **fresh each forward pass, as the Python runs** → real `if`/`for`/`print`/`pdb` work inside the model. Why researchers adopted PyTorch. |
| **⭐ `eval()` ≠ `no_grad()`** | `no_grad()` stops graph-building (memory); `model.eval()` switches dropout off + batchnorm to running stats (behaviour). **Need both at inference.** |
| **⭐ The `.item()` leak** | Appending un-detached tensors (`losses.append(loss)`) keeps each whole graph alive → OOM. Fix: **`.item()`** or `.detach()`. |
| **The ritual** | `optimizer.zero_grad()` → `loss.backward()` → `optimizer.step()`. |
| **`nn.Module`** | `__init__` = the **parts list**; `forward` = the **wiring.** Assigning `self.fc = nn.Linear(...)` **auto-registers** its parameters. |
| **⭐ `nn.ModuleList`** | Layers in a **plain Python list are invisible to `.parameters()`** — not trained, not moved. Use `ModuleList`. |
| **`nn.Sequential`** | Straight-line stacks only; write a custom `forward` for branching / residuals / multiple inputs. |

### Data & the training loop

| Term | Meaning |
|---|---|
| **`Dataset` / `DataLoader`** | "one example given an index" / "batch, shuffle, load in parallel." |
| **⭐ Shuffle train, not val** | Ordered train data → class-clustered batches → wrong gradients. Val does no updates, so shuffling only breaks reproducibility. |
| **⭐ `num_workers`** | Parallel data loading. The **most expensive DL mistake is an idle GPU waiting for data** — diagnose with `nvidia-smi`. |
| **Augment train, not val** | Random augmentation at eval makes metrics **non-deterministic** and evaluates on distorted data. |
| **⭐ The three-line heartbeat** | `zero_grad → backward → step`. **Every model uses this exact loop — it never changes.** |
| **⭐ `train()` / `eval()`** | Flip **both ways every epoch**: `train()` before training (dropout on), `eval()` + `no_grad()` before validation. Forgetting `eval()` = noisy metrics; forgetting `train()` after = silent overfitting. |
| **⭐ Overfit one batch** | **Can the model drive a single batch to ~0 loss?** If not, the bug is in the model/loop, not the data. Karpathy's #1 recipe. |
| **Best-by-validation checkpoint** | Save the best-val epoch (not the last, often overfit); **save the optimizer state too** to resume. |

### Architectures

| Term | Meaning |
|---|---|
| **⭐ Why FC fails on images** | Too many params (~150M/layer), ignores spatial structure, and — the killer — **no translation invariance** (relearns a pattern at every position). |
| **⭐ Weight sharing** | The **same filter applied at every position** → translation invariance + orders-of-magnitude fewer parameters. |
| **Convolution** | A **dot product between a learned filter and each image patch**, slid across the image → a feature map. |
| **Feature map / NCHW** | A conv layer's output; PyTorch image tensors are shaped `(N, C, H, W)`. |
| **⭐ Transfer learning** | Reuse a pretrained backbone's **generic early features**, train a new head → **thousands of images, not millions.** The default in vision. |
| **ResNet / residual connection** | `x + f(x)` — a gradient highway that made 152-layer nets trainable. **In every model since, including Transformers.** |
| **⭐ Why RNNs forget** | Vanishing gradient **across time** — BPTT multiplies the recurrent weights every step → dies after ~10 steps. The $\lambda^n$ problem, across time. |
| **LSTM / GRU** | Gates + a **protected cell state** (a near-linear conveyor belt) → memory of hundreds of steps. |
| **⭐ Why Transformers won** | RNNs are **sequential — can't parallelize** (waste the GPU) *and* struggle with long range. Attention fixes **both**: parallel + direct path between any two positions. |
| **`pack_padded_sequence`** | ⭐ Tells the LSTM where each real sequence ends; without it, **padding contaminates the hidden state.** |

### Regularization, performance & debugging

| Term | Meaning |
|---|---|
| **The overfit diagnostic** | Unchanged from [08.2](docs/08-Machine-Learning/weeks/08.2-ml-workflow.md): **train low + val high → regularize; both high → do the opposite.** |
| **⭐ Dropout** | Randomly zeroes neurons in training → prevents co-adaptation + implicit ensemble. **Off at inference** (`eval()`). |
| **⭐ Batch norm (train vs eval)** | Train: current-batch stats (+ updates a running average). Eval: the **stored running average.** `eval()` switches it. |
| **LayerNorm** | Normalizes **per example over features — batch-independent.** Why Transformers use it, not BatchNorm. |
| **⭐ The strongest regularizer** | **More data — and augmentation is "more data" for free.** It expands the problem instead of constraining the model. |
| **⭐ Mixed precision** | Half-precision matmuls on Tensor Cores + fp32 where it matters → **~2× faster, half the memory, ~free. Use by default.** |
| **Gradient clipping** | `clip_grad_norm_(params, 1.0)` — the seatbelt against exploding gradients / NaN. |
| **Gradient accumulation** | Sum gradients over several mini-batches, step once → **simulate a big batch that won't fit.** Why PyTorch accumulates. |
| **Gradient checkpointing** | Discard activations in the forward pass, **recompute them in the backward** — trades ~30% compute for a big memory saving. |
| **⭐ Data- vs compute-bound** | `nvidia-smi` GPU-Util: ~95% = compute-bound (optimize the model); low = **data-bound** (fix the DataLoader). **Check first.** |
| **⭐ The #1 debug test** | **Overfit one batch.** Passing it rules out model/loop bugs and isolates the problem to data/regularization/hyperparameters. |
| **Change one thing** | The cardinal debugging rule — and make the model prove it on something trivial before asking it to generalize. |
| **NaN by timing** | Step 0 → data/loss/init; after a spike → **exploding gradients (clip)**; mid-training → overflow. `set_detect_anomaly(True)` finds the op. |
| **Dead neuron** | ReLU stuck always-negative → outputs 0, gradient 0, never recovers. Fix: lower LR, Leaky ReLU/GELU. |

### Save / load & production

| Term | Meaning |
|---|---|
| **⭐ `state_dict`** | Save this, **not the whole model** — `torch.save(model, ...)` pickles the class path and breaks on refactor. `state_dict` is a portable dict of tensors. |
| **⭐ Resuming training** | Needs model + **optimizer state** (Adam's m, v) + scheduler + epoch. **Weights alone → Adam restarts cold → loss spike.** |
| **⭐ `torch.load` = RCE** | It's **pickle → arbitrary code execution.** Use **`weights_only=True`** or **safetensors** for untrusted files. |
| **GPU reproducibility** | Not easily perfect (some GPU ops are non-deterministic). Best practice: **report mean ± std across seeds.** |
| **⭐ Inference is lighter** | No gradients, no optimizer state, no activation cache → a 7B model trains in ~80 GB but **infers in ~14 GB.** |
| **⭐ Latency vs throughput** | Batching helps **throughput** (efficient GPU) but hurts **latency** (requests wait to fill). **Dynamic batching** is the tunable middle. |
| **TorchScript / ONNX** | Convert the model to a **static, Python-free graph** for deployment. **ONNX** = open, cross-framework. |
| **⭐ MLOps unchanged** | Monitoring, drift canaries, versioning, retraining gates all carry over **unchanged from [Module 08](docs/08-Machine-Learning/weeks/08.17-production-ml.md).** **Deep learning added a new model, not a new discipline.** |

---

## Natural Language Processing (Module 10)

### Foundations & representation

| Term | Meaning |
|---|---|
| **⭐ The one problem** | turn text into vectors **without losing meaning** — all of NLP is this. |
| **⭐ Distributional hypothesis** | "know a word by the company it keeps" — meaning ≈ the distribution of contexts a word appears in. The field's bedrock. |
| **Ambiguity** | one string, many meanings (lexical/syntactic/referential/scope) — the *default* in language. |
| **Syntax / semantics / pragmatics** | grammar / literal meaning / intended meaning in context. |
| **Zipf's law / long tail** | a few words dominate; the tail is near-infinite → you always meet unseen words at inference. |
| **NFC normalization** | ⭐ collapse Unicode so "café" == "café"; the first line of every pipeline. |
| **Tokenization** | split text into units; `.split()` is a trap (glues punctuation, shreds URLs). |
| **Stemming vs lemmatization** | rule-based suffix chop (fast, non-words) vs dict+POS lookup (real base forms); both obsolete with neural models. |
| **Stop words** | high-frequency low-info words; ⚠️ **never remove before sentiment or a sequence model** ("not"). |
| **⭐ Subword tokenization (BPE/WordPiece)** | vocabulary of frequent character sequences → **no unknown words**, language-agnostic. The modern default. |

### Sparse & dense representations

| Term | Meaning |
|---|---|
| **One-hot** | 1 at the word's index, else 0; huge and **orthogonal (dot=0)** → meaning-blind. |
| **Bag of Words** | word counts per document; **destroys word order** ("dog bites man" = "man bites dog"). |
| **N-grams** | counts of short phrases; recover local order but explode the feature space (V², V³). |
| **⭐ TF-IDF** | `count × log(N/df)`; ubiquitous words → ~0 weight, rare informative words → high. **Fit on train only.** |
| **Why IDF's log** | document frequency spans orders of magnitude; the log compresses it so one rare word doesn't dominate. |
| **⭐ Word embedding** | dense vector per word; **direction = meaning**; similar words are geometrically close. |
| **Distributed representation** | meaning spread across all dims (vs one-hot's single coordinate) → generalizes across similar words. |
| **⭐ Word2Vec** | shallow net on a fake task (predict context); keep the weight matrix, discard the predictions. |
| **CBOW / skip-gram** | context→word (faster) / word→context (better on rare words; the usual default). |
| **⭐ Negative sampling** | replace the V-way softmax with binary "real vs random pair?" → updates 1+k vectors, not V. |
| **GloVe** | count-based cousin: factorize the global co-occurrence matrix so `wᵢ·wⱼ ≈ log(count)`. |
| **Cosine similarity** | the embedding comparison — direction, not magnitude (which tracks frequency). |
| **Analogy arithmetic** | `king − man + woman ≈ queen`; real but oversold/fragile in the wild. |
| **⭐ Static-embedding limit** | one vector per word regardless of context ("bank" is one blur) → attention gives contextual ones. |

### Sequence models & attention

| Term | Meaning |
|---|---|
| **Hidden state** | a fixed-size running summary of the sequence read so far; how sequence models use word order. |
| **⭐ Vanishing gradient (in NLP)** | λⁿ decay across time breaks long-range agreement/coreference after ~10 words. |
| **LSTM / GRU** | gated **cell state** (near-linear memory path) → memory over hundreds of steps; GRU first. |
| **Bidirectional** | forward+backward pass; sees the whole sentence — **forbidden for generation/streaming**. |
| **⭐ Seq2seq bottleneck** | the encoder crushes the whole input into one fixed vector → fails on long inputs → attention fixes it. |
| **⭐ Attention** | `softmax(QKᵀ/√dₖ)·V` — a soft, differentiable dictionary lookup; every token blends the whole sequence by relevance. |
| **Query / Key / Value** | what a token seeks / how it's matched / what content it delivers (all learned projections). |
| **⭐ √dₖ scaling** | variance fix: without it, dot-product scores grow, softmax saturates, and gradients vanish. |
| **⭐ Self-attention** | Q,K,V from the same sequence → **contextual embeddings** ("bank" differs by sentence). |
| **Cross-attention** | Q from one sequence, K/V from another (decoder attends to encoder). |
| **Multi-head attention** | h parallel attentions → many relationship types (syntax, coreference) at ~the cost of one. |
| **⭐ O(n²) cost** | attention is quadratic in sequence length — the central engineering problem of LLMs. |
| **⭐ vs RNN** | attention has O(1) path length between tokens + full parallelism, at O(n²) compute. |

### Seq2seq, tasks & evaluation

| Term | Meaning |
|---|---|
| **Encoder–decoder** | understand the input → autoregressively generate the output one token at a time. |
| **Teacher forcing** | train the decoder on the ground-truth previous token (fast, clean loss). |
| **Exposure bias** | trained on perfect prefixes, tested on its own imperfect outputs → can derail. |
| **Greedy / beam / sampling** | argmax (short-sighted) / keep k best (high-prob, bland) / random by distribution (LLM default). |
| **⭐ The lineage** | seq2seq → +attention → **drop the RNN = Transformer**. |
| **⭐ The four I/O shapes** | seq→label, seq→per-token, seq→seq, pair→score — the shape dictates head, loss, and metric. |
| **BIO tagging** | Begin/Inside/Outside tags turning span-finding (NER) into per-token classification. |
| **CRF** | ⭐ enforces globally consistent tag sequences (no illegal `O I-PER`) on top of a tagger. |
| **Bi- vs cross-encoder** | encode separately & compare (fast, pre-computable) vs encode together (accurate, slow) → retrieve then rerank. |
| **Macro vs micro F1** | per-class balanced (use for imbalance) vs pooled (frequent-class dominated). |
| **BLEU** | n-gram **precision** vs reference + brevity penalty (translation); no semantics; relative only. |
| **ROUGE** | n-gram **recall** vs reference (summarization coverage); no semantics. |
| **⭐ Perplexity** | `exp(cross-entropy)` = effective choices per token; tokenizer-bound; measures fluency, not usefulness. |

### Data, engineering & ethics

| Term | Meaning |
|---|---|
| **⭐ The bottleneck** | labels, not the model — most NLP leverage is in the data. |
| **⭐ Inter-annotator agreement (Cohen's κ)** | chance-corrected labeling consistency; the **ceiling** on achievable model accuracy. |
| **Near-duplicate leakage** | the same/similar doc in train and test → score measures memorization; **dedup before splitting**. |
| **Author/temporal leakage** | random splits let a model learn the author/period; split by author/source/time. |
| **`<pad>` / `<unk>`** | fill short sequences / catch OOV words; both non-negotiable (long tail guarantees OOV). |
| **`padding_idx`** | pins the pad embedding to zeros and excludes it from gradients. |
| **⭐ Pad + pack/mask** | `pack_padded_sequence` (RNN), attention mask (attention), `ignore_index` (tagging) — else padding corrupts the model. |
| **⭐ The loop is unchanged** | NLP adds a text front end (numericalize/embed/mask); the [09.10](docs/09-Deep-Learning/weeks/09.10-training-loop.md) loop itself doesn't change. |
| **Hugging Face** | `tokenizers` + `transformers` + `datasets`; everything pretrained. |
| **BERT / GPT / T5** | encoder (understand) / decoder (generate) / encoder–decoder (text-to-text). |
| **⭐ Fine-tuning** | transfer learning for text: adapt a pretrained model with a small head on few labels. |
| **⭐ Tokenizer must match model** | mismatched tokenizer → wrong IDs → garbage output, with **no crash**. |
| **⭐ Train/serve skew** | the #1 NLP production bug: preprocessing must be byte-identical between training and serving. |
| **Distillation** | smaller model (DistilBERT) ~2× faster for ~3% accuracy — the top latency lever. |
| **NLP drift** | the **language itself** changes (slang/topics); monitor `<unk>`/vocabulary drift. |
| **⭐ Bias (structural)** | co-occurrence learning encodes human prejudice as geometry; measure (WEAT/disaggregate), can't just clean away. |
| **Proxy** | removing a protected attribute doesn't remove bias — name/style/school reconstruct it. |
| **⭐ Memorization/extraction** | models regurgitate rare training sequences verbatim (PII); the only robust defense is not training on it. |
| **⭐ Hallucination** | generation optimizes *probable*, not *true* — a fluent lie is high-probability; fight with RAG/citations/review. |
| **Model card / datasheet** | document intended use, disaggregated performance, and known risks — accountability, increasingly legal. |
