# ✅ Module 13 · RAG — Quiz 01 Answers

[🏠 Module 13](../README.md) · [📝 Quiz](quiz-01.md) · [📖 Lessons](../weeks/README.md)

> Model answers grade **reasoning**. Full credit = the key idea explained, not just a keyword.

---

## Part A · Why & Architecture

**1.** **Knowledge cutoff** (weights frozen at train time → no recent facts), **private data** (no public model saw your docs), **frequently changing data** (facts move faster than weights can), and **hallucination** (plausibility ≠ truth → confident invention). RAG addresses all four by putting fresh/private/citable text in the prompt at query time. → [13.1](../weeks/13.1-why-rag-exists.md)

**2.** Prompting changes the **instructions/framing** (no new knowledge); RAG changes the **knowledge** (injects fresh/private facts, updatable, citable); fine-tuning changes the **weights** (behavior/style/skill). Rule: **facts → RAG, behavior → fine-tune, framing → prompt.** They compose. → [13.1](../weeks/13.1-why-rag-exists.md)

**3.** A big window helps but doesn't replace retrieval: you still must **find and rank** the right text from a corpus larger than any window, and stuffing everything is slow, expensive, and *less* accurate (lost-in-the-middle). RAG selects and orders; the window just holds the selection. → [13.1](../weeks/13.1-why-rag-exists.md), [13.9](../weeks/13.9-context-construction.md)

**4.** It assumes docs parse cleanly, arbitrary splits make good chunks, cosine similarity = relevance, all retrieved chunks belong in the prompt, and the LLM uses them faithfully — all false in production. Omitted stages include **cleaning** (strip boilerplate), **metadata/ACL** (filter + cite + secure), **filtering**, **reranking** (precision), **context construction** (ordering/dedup), and **evaluation/monitoring**. → [13.2](../weeks/13.2-rag-architecture.md)

**5.** Offline (ingest→parse→clean→chunk→metadata→embed→index) runs **once per document** — can be slow/batched/expensive. Online (query→retrieve→filter→rerank→context→generate) runs **every query** — must be fast/cheap. The split means you can re-index without redeploying serving, scale halves independently, and it explains why bugs baked offline surface online. → [13.2](../weeks/13.2-rag-architecture.md)

## Part B · Index-time

**6.** A parse error is **permanent** — nothing downstream can recover it. E.g., a PDF table flattened to de-aligned text embeds as nonsense, can't be retrieved, and the answer is missing; reranking can't rerank text that was never extracted. → [13.3](../weeks/13.3-ingestion-parsing.md)

**7.** Extract **structurally** (preserve row/column relationships), then row-serialize with headers inline (`Region: EMEA | Q3: 4.2M`) or render as Markdown. A table's meaning is the cell *relationships*; flowing it to text destroys them and makes the fact untrievable. → [13.3](../weeks/13.3-ingestion-parsing.md)

**8.** You retrieve, embed, rerank, and prompt with **chunks**, not documents — boundaries decide what facts can be retrieved together. If a fact straddles a boundary (and there's no overlap), neither chunk contains it whole, so it becomes unretrievable. → [13.4](../weeks/13.4-chunking.md)

**9.** A chunk becomes **one vector** — the average-ish meaning of its content. Too big → the vector averages many ideas ("blurred"), matching everything weakly; too small → facts severed from context. Aim for one coherent idea per chunk. → [13.4](../weeks/13.4-chunking.md)

**10.** **Structure-aware > recursive > sentence/paragraph > fixed-size.** Structure-aware uses the author's own organization (best coherence); recursive respects natural separators *and* size (good default); sentence/paragraph respect some structure but vary in size; fixed-size is blind to meaning (baseline only). → [13.4](../weeks/13.4-chunking.md)

**11.** Overlap repeats ~10–20% of adjacent chunks so a boundary-straddling fact appears whole in at least one chunk. Cost: index bloat (~proportional to overlap) and duplicate retrieval (dedup later). → [13.4](../weeks/13.4-chunking.md)

**12.** Cosine = angle only `(q·d)/(‖q‖‖d‖)`; dot = alignment + magnitude `Σqᵢdᵢ`; Euclidean = straight-line distance `‖q−d‖`. On **normalized** vectors, dot == cosine, and L2 ranks the same as cosine. → [13.5](../weeks/13.5-embeddings-similarity.md)

**13.** **Metric mismatch / forgetting to normalize** — e.g., embedding for cosine but querying with L2, or mixing models for corpus vs queries. Avoid by normalizing, using the model's intended metric, and using the *same* model/metric everywhere. → [13.5](../weeks/13.5-embeddings-similarity.md)

**14.** Embed all chunks (normalized) into a matrix; embed the query; compute cosine = one matrix–vector product against every chunk; sort; take top-k. It's O(N·d) because it scores **all** N vectors — instant for thousands, far too slow for millions → need ANN. → [13.5](../weeks/13.5-embeddings-similarity.md)

**15.** B-tree/relational indexes do exact and range lookups on scalars, not "nearest point in high-dimensional space"; computing cosine to every row is the brute-force scan. Classic spatial trees (k-d, R-tree) break under the **curse of dimensionality**. → [13.6](../weeks/13.6-vector-databases.md)

**16.** **HNSW** walks a multi-layer neighbor graph (few dozen hops instead of N). **IVF** clusters vectors and searches only the nearest `nprobe` clusters. **PQ** compresses vectors to codebook bytes so approximate distances are cheap table lookups. All examine a small subset instead of all N. → [13.6](../weeks/13.6-vector-databases.md)

**17.** **Recall ↔ speed ↔ memory** — every dial trades among them. "Good enough" = measure ANN recall **against exact brute-force ground truth** and tune (`efSearch`/`nprobe`) until you hit a target (e.g., ≥95% Recall@10 at your latency budget), then stop. → [13.6](../weeks/13.6-vector-databases.md)

## Part C · Query-time

**18.** Dense fails on "error `E-4021`" (exact code) but handles "get my money back" ↔ "refund policy" (paraphrase); sparse/BM25 is the reverse. Dense matches **meaning** (blurs exact strings); sparse matches **exact terms** (misses synonyms). → [13.7](../weeks/13.7-retrieval.md)

**19.** IDF up-weights **rare** terms (informative); term frequency raises the score but **saturates** via k₁ (diminishing returns); length normalization (b·|d|/avgdl) prevents **long documents** from winning just by length. → [13.7](../weeks/13.7-retrieval.md)

**20.** Hybrid runs dense + sparse and **fuses** their rankings. RRF sums `1/(k+rank)` across retrievers — using **rank**, not raw score, so it needs no normalization between incomparable scales (cosine `[-1,1]` vs unbounded BM25). → [13.7](../weeks/13.7-retrieval.md)

**21.** Retrieval optimizes **recall** cheaply (get the right chunk into a generous top-N); reranking optimizes **precision** expensively (order the best to the top). Retrieving only the final few risks the right chunk never making the cut, and nothing downstream can recover a recall miss. → [13.7](../weeks/13.7-retrieval.md), [13.8](../weeks/13.8-reranking.md)

**22.** A bi-encoder encodes query and chunk **separately** into vectors, then compares (fast, scalable, but never reads them against each other). A cross-encoder feeds `(query, chunk)` **together** through a transformer with cross-attention (precise relevance) — but costs one forward pass **per candidate**, so it's slow. → [13.8](../weeks/13.8-reranking.md)

**23.** It needs a forward pass per `(query, chunk)` pair and can't precompute chunk scores (they depend on the query) — feasible for dozens of retrieved candidates, impossible for millions. → [13.8](../weeks/13.8-reranking.md)

**24.** LLMs use information at the **start and end** of the context reliably but often **ignore the middle** (U-shaped accuracy). Mitigate by keeping **k small** and putting the most relevant chunks at the **edges** (often strongest last, nearest the question). → [13.9](../weeks/13.9-context-construction.md)

**25.** Each extra chunk adds **distractors** the model must ignore, dilutes attention, and pushes good chunks toward the ignored middle. Precision beats volume — rerank to a small k. → [13.9](../weeks/13.9-context-construction.md)

**26.** Overlap and multi-query routinely surface the **same passage** multiple times; duplicates waste the window, bias the model toward the repeated claim, and crowd out other evidence. → [13.9](../weeks/13.9-context-construction.md)

**27.** The escape hatch instructs the model to say "I don't have that information" when sources lack the answer. It **reduces hallucination** (honest non-answer instead of confident fabrication) and **improves observability** (a decline signals a retrieval miss instead of masking it). → [13.10](../weeks/13.10-generation.md)

**28.** No — models can attach a citation to a claim the source doesn't support (citation hallucination). For citation-critical systems, **verify** each citation (the cited chunk must contain the claim); an unverified citation manufactures false confidence. → [13.10](../weeks/13.10-generation.md)

**29.** RAG wants **faithful extraction** from the given context, not creativity; low temperature (0–0.3) makes generation more deterministic and grounded, reducing embellishment/hallucination. → [13.10](../weeks/13.10-generation.md)

## Part D · Advanced & Evaluation

**30.** Precise chunk lacks context → **parent-child**; answer spans documents → **multi-hop**; entity relationships → **graph RAG**; needs planning/tools → **agentic**; silent retrieval failure → **corrective/self-reflective**. → [13.11](../weeks/13.11-advanced-rag.md)

**31.** Small chunks retrieve precisely but lack context; big chunks have context but blur embeddings. Parent-child **matches on small child chunks** but **returns their larger parent** as context — getting precision *and* context. → [13.11](../weeks/13.11-advanced-rag.md)

**32.** Only when **evaluation shows a specific failure** the pattern targets, and an A/B vs a well-tuned baseline shows the quality gain justifies the added latency, cost, and debugging complexity. Fix naive RAG (parsing/chunking/hybrid/rerank/context) first. → [13.11](../weeks/13.11-advanced-rag.md)

**33.** An answer fails for two different reasons — retrieval didn't fetch the right chunk, or generation misused a correct chunk — needing different fixes. A single end-to-end score can't distinguish them. → [13.12](../weeks/13.12-evaluation.md)

**34.** **Recall@K** — if the answer's chunk isn't in the top-K passed to the LLM, the answer *can't* be correct (a miss is unrecoverable). Precision matters (distractors) but reranking can fix precision within a high-recall set; nothing recovers a recall miss. → [13.12](../weeks/13.12-evaluation.md)

**35.** **Faithfulness** = answer supported by context (low → generation/grounding bug — hallucination). **Answer relevance** = answer addresses the question (low → evasive/off-topic). **Context relevance** = context relevant to question (low → retrieval bug). The triad localizes the failing stage. → [13.12](../weeks/13.12-evaluation.md)

**36.** To measure whether the system **correctly declines** (escape hatch) instead of hallucinating; testing only answerable questions hides confident fabrication on out-of-corpus queries. → [13.12](../weeks/13.12-evaluation.md)

## Part E · Operate

**37.** **Trace one query through every stage** (corpus → parse → chunk → retrieve → rerank → context → generate) and find the **first stage where the answer's information disappears**. The cause is rarely at generation because information lost at any earlier stage stays lost — the bad answer is a downstream symptom. → [13.13](../weeks/13.13-debugging.md)

**38.** Malicious instructions hidden in **retrieved documents** that the LLM may execute, because it can't reliably separate instructions from data. It's **structural** to how LLMs process text (not a patchable bug). Strongest defense: **least privilege** — ensure obeying an injected command can't do damage (no dangerous tools/exfiltration) — layered with sources-as-data prompting and output filtering. → [13.14](../weeks/13.14-security.md)

**39.** Mostly the **LLM generation call** (80–95%), then reranking; retrieval/embedding are small. Top optimizations: **semantic caching** (skip retrieval+LLM on similar past queries — biggest saver), **shrink context** (rerank small k, compress, dedup, cap output), and **right-size the model** (retrieval supplies knowledge). Risk: a **loose cache threshold** serves the wrong/stale answer, and caches must be ACL/tenant-scoped and invalidated on index updates. → [13.16](../weeks/13.16-performance.md)

**40.** Frameworks hide the **defaults for every quality-critical stage** (parser, chunk size, overlap, embedding model, metric, top-k, prompt). Building the core by hand ([13.5](../weeks/13.5-embeddings-similarity.md), [13.7](../weeks/13.7-retrieval.md)) lets you **see through the abstraction** and know which stage to fix when a framework's output is wrong — you can't debug or tune what you don't understand. → [13.17](../weeks/13.17-frameworks.md)

---

## Scoring

| Score | Verdict |
|---|---|
| 36–40 | Excellent — you can design, build, evaluate, secure, and deploy RAG. |
| 32–35 | Solid — review the missed lessons. |
| 24–31 | Partial — re-read 13.2, 13.5, 13.7, 13.12 (the load-bearing four). |
| < 24 | Re-study the module; redo ⭐ exercises E5, E9, E12, E14, E16. |

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 13](../README.md) |
| 📝 Quiz | [quiz-01.md](quiz-01.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
