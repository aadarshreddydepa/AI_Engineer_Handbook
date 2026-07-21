# 🧠 Module 13 · RAG — Flashcard Deck

[🏠 Module 13](../README.md) · [📖 Lessons](../weeks/README.md) · [📄 Cheat sheet](../cheat-sheets/rag-cheatsheet.md)

> **~90 cards.** Cover the answer, say it aloud, *then* check. ⭐ marks the load-bearing ones.

---

## 13.1 · Why RAG Exists

**Q:** ⭐ Why does RAG exist? → **A:** LLM knowledge is cut off, private-blind, stale, and hallucination-prone; RAG injects fresh, private, citable facts at query time. → [13.1](../weeks/13.1-why-rag-exists.md)

**Q:** What is RAG in one sentence? → **A:** Retrieve relevant text for a query and generate an answer conditioned on it.

**Q:** ⭐ RAG vs fine-tuning vs prompting? → **A:** Facts/knowledge → RAG; behavior/style/skill → fine-tune; framing → prompt.

**Q:** Does RAG eliminate hallucination? → **A:** No — it strongly reduces it via grounding, but the model can still ignore or misread context.

**Q:** Does a bigger context window kill RAG? → **A:** No — you still must find and rank the right text; stuffing everything is slow, costly, and less accurate.

---

## 13.2 · RAG Architecture

**Q:** ⭐ What's wrong with "docs → embeddings → vector DB → LLM"? → **A:** It hides the stages that determine quality: cleaning, metadata, filtering, reranking, context construction, evaluation, monitoring. → [13.2](../weeks/13.2-rag-architecture.md)

**Q:** ⭐ Name the offline stages. → **A:** Ingest → parse → clean → chunk → metadata → embed → index.

**Q:** ⭐ Name the online stages. → **A:** Query → retrieve → filter → rerank → construct context → generate.

**Q:** Why is RAG hard to debug? → **A:** Quality bugs are baked in offline but surface online — cause and symptom are in different halves.

**Q:** Where do access controls live? → **A:** Metadata records ACLs (offline); filtering enforces them before generation (online).

---

## 13.3 · Ingestion & Parsing

**Q:** ⭐ Why does parsing quality cap retrieval quality? → **A:** A parse error (e.g., a mangled table) can't be fixed downstream — the fact is gone before embedding. → [13.3](../weeks/13.3-ingestion-parsing.md)

**Q:** Why are PDFs hard? → **A:** They store glyph positions, not paragraphs — no inherent reading order, columns, or table structure.

**Q:** ⭐ How should tables be extracted? → **A:** Structurally (preserve row/column relationships), row-serialized or as Markdown — never as flowed text.

**Q:** What is OCR and its risk? → **A:** Recovering text from pixels; imperfect, so garbled low-confidence output silently poisons the index — track confidence.

**Q:** Why capture metadata at parse time? → **A:** It powers filtering, access control, and citations, and can't be reconstructed from a bare chunk.

---

## 13.4 · Chunking

**Q:** ⭐ Why is the chunk "the atom of RAG"? → **A:** You embed, index, retrieve, rerank, and prompt with chunks — boundaries decide what can be retrieved together. → [13.4](../weeks/13.4-chunking.md)

**Q:** ⭐ What goes wrong with chunks too big? → **A:** The single embedding averages many ideas ("blurred"), matching everything weakly; the answer is diluted in noise.

**Q:** Chunks too small? → **A:** Facts get severed from context; an answer needing adjacent facts can't retrieve both.

**Q:** What is recursive chunking? → **A:** Split on the largest natural separator (paragraph), recursing to smaller ones until each chunk fits the size budget.

**Q:** Why is structure-aware chunking usually best? → **A:** It splits along the author's own organization (headings/sections), so chunks are coherent and citable.

**Q:** What does overlap buy you? → **A:** A fact straddling a boundary appears whole in at least one chunk.

**Q:** ⭐ Which dials to tune first when retrieval underperforms? → **A:** Chunk size and overlap, before changing embedding models or rerankers.

---

## 13.5 · Embeddings & Similarity

**Q:** ⭐ What is a text embedding? → **A:** A dense vector positioned so semantically similar texts are geometrically close. → [13.5](../weeks/13.5-embeddings-similarity.md)

**Q:** Dense vs sparse vector? → **A:** Dense = few hundred rich learned dims; sparse = huge mostly-zero word-count vector.

**Q:** ⭐ Cosine vs dot vs L2 — which for text? → **A:** Cosine (angle, ignores length) is default; == dot product if normalized; L2 ranks the same when normalized.

**Q:** ⭐ The #1 similarity-search bug? → **A:** Metric mismatch / forgetting to normalize — or mixing models for corpus vs queries.

**Q:** How does search work once text is embedded? → **A:** Embed the query, compute similarity to all chunk vectors (a matmul), return the top-k.

**Q:** Why doesn't brute force scale? → **A:** It's O(N·d) per query — fine for thousands, far too slow for millions → need ANN.

**Q:** Does "similar" mean "relevant"? → **A:** No — similarity ≠ relevance ≠ truth ≠ authorization.

---

## 13.6 · Vector Databases

**Q:** ⭐ Why can't SQL do vector search? → **A:** B-trees do exact/range lookups, not nearest-in-high-dimensional-space; spatial trees break under the curse of dimensionality. → [13.6](../weeks/13.6-vector-databases.md)

**Q:** ⭐ What is ANN and its bet? → **A:** Approximate Nearest Neighbor — examine ~1% of vectors, return true neighbors ~99% of the time.

**Q:** How does HNSW search? → **A:** Greedily walks a multi-layer neighbor graph from sparse top layers to dense bottom, reaching the neighborhood in a few dozen hops.

**Q:** How does IVF prune? → **A:** Clusters vectors; searches only the `nprobe` nearest clusters at query time.

**Q:** What is Product Quantization? → **A:** Lossy compression of vectors into codebook byte-codes — huge memory savings, approximate distances, usually re-ranked exactly.

**Q:** ⭐ State the ANN trade-off. → **A:** Recall vs speed vs memory — every dial trades among them; tune to a measured recall target.

---

## 13.7 · Retrieval

**Q:** ⭐ Dense vs sparse retrieval? → **A:** Dense (embeddings) matches meaning/paraphrases but misses exact codes; sparse (BM25) matches exact terms but misses synonyms. → [13.7](../weeks/13.7-retrieval.md)

**Q:** What is BM25? → **A:** A refined TF-IDF: IDF weights rare terms, TF saturates (k₁), and long docs are length-normalized (b).

**Q:** ⭐ What is hybrid search and why? → **A:** Run dense + sparse and fuse rankings — semantic recall AND exact-term precision; most reliable upgrade after good chunking.

**Q:** What is RRF and why popular? → **A:** Reciprocal Rank Fusion combines retrievers by rank (`1/(k+rank)`), needing no score normalization.

**Q:** ⭐ Retrieval vs reranking objective? → **A:** Retrieval maximizes recall (get the right chunk into top-N); reranking maximizes precision (order it to the top).

**Q:** When use multi-query/HyDE? → **A:** When retrieval fails on short/mismatched queries — at the cost of latency, LLM calls, and noise.

**Q:** Where must ACL filtering happen? → **A:** At retrieval (pre-filter), before the LLM sees any text.

---

## 13.8 · Reranking

**Q:** ⭐ Why isn't first-stage retrieval enough? → **A:** It encodes query and chunk independently → measures similarity, not query-specific relevance; the best chunk is often retrieved but not ranked first. → [13.8](../weeks/13.8-reranking.md)

**Q:** ⭐ Bi-encoder vs cross-encoder? → **A:** Bi-encoder encodes query and chunk separately then compares vectors (fast); cross-encoder reads them together with attention (precise, one pass per candidate).

**Q:** Where does reranking sit? → **A:** Retrieve top-N → rerank → keep top-k.

**Q:** Why not rerank the whole corpus? → **A:** A cross-encoder needs a forward pass per candidate — feasible for dozens, impossible for millions.

**Q:** Can reranking fix bad chunks or missing recall? → **A:** No — it only reorders what retrieval surfaced.

---

## 13.9 · Context Construction

**Q:** ⭐ What is lost-in-the-middle? → **A:** LLMs use info at the start and end reliably but often ignore the middle — a U-shaped accuracy curve. → [13.9](../weeks/13.9-context-construction.md)

**Q:** How do you counter it? → **A:** Keep k small; put the most relevant chunks at the edges (often strongest last).

**Q:** ⭐ Why is more context often worse? → **A:** Extra chunks add distractors, dilute attention, and push good chunks into the ignored middle.

**Q:** Why is dedup mandatory? → **A:** Overlap and multi-query surface the same passage repeatedly, wasting the window and biasing the model.

**Q:** What does source tagging enable? → **A:** Citation, tracing/debugging, and clearer separation of untrusted data from instructions.

---

## 13.10 · Generation

**Q:** ⭐ Why does generation quality depend on retrieval quality? → **A:** The model can only use given context; if the answer isn't retrieved, the best a good prompt yields is an honest "I don't know." → [13.10](../weeks/13.10-generation.md)

**Q:** ⭐ What is the escape hatch and why? → **A:** Instructing the model to say "I don't have that information" when sources lack the answer — the top anti-hallucination lever; it also surfaces retrieval failures.

**Q:** Is a cited source a verified source? → **A:** No — models can mis-attribute (citation hallucination); verify the cited chunk supports the claim.

**Q:** What temperature for RAG? → **A:** Low (0–0.3) — faithful extraction, not creative embellishment.

**Q:** Why treat sources as data, not instructions? → **A:** To defend against prompt injection through documents.

---

## 13.11 · Advanced RAG

**Q:** ⭐ What is parent-child / small-to-big? → **A:** Match on small chunks (precise) but return their larger parent for context. → [13.11](../weeks/13.11-advanced-rag.md)

**Q:** What does multi-hop solve? → **A:** Questions needing facts combined from different chunks/documents, via iterative retrieve→extract→retrieve.

**Q:** What is Graph RAG for? → **A:** Relationship and aggregation questions, via traversing an entity-relationship graph.

**Q:** ⭐ Corrective vs self-reflective RAG? → **A:** Corrective grades chunks and re-retrieves if poor; self-reflective also decides whether to retrieve and critiques its own answer's support/completeness.

**Q:** ⭐ When adopt an advanced pattern? → **A:** Only when evaluation shows a specific failure it fixes — complexity costs latency, money, and debuggability.

---

## 13.12 · Evaluation

**Q:** ⭐ Why does RAG need two evaluations? → **A:** An answer can fail from bad retrieval or bad generation; one score can't tell which, and they need different fixes. → [13.12](../weeks/13.12-evaluation.md)

**Q:** ⭐ Precision@K vs Recall@K — which matters most? → **A:** Recall@K — if the answer chunk isn't in top-K, the answer can't be correct; reranking fixes precision within a high-recall set.

**Q:** What is MRR? → **A:** Mean of 1/(rank of first relevant) — rewards ranking a correct chunk high.

**Q:** What does NDCG add? → **A:** Graded relevance and position discounting, normalized against the ideal ranking.

**Q:** ⭐ What is faithfulness? → **A:** Whether every claim in the answer is supported by the retrieved context — the anti-hallucination metric.

**Q:** RAG triad? → **A:** Context relevance (context↔question), faithfulness (answer↔context), answer relevance (answer↔question).

**Q:** Why include unanswerable questions? → **A:** To measure whether the system correctly declines instead of hallucinating.

---

## 13.13 · Debugging

**Q:** ⭐ Core RAG debugging method? → **A:** Trace one query through every stage; find the first stage where the answer's info disappears — that's the cause, not the final stage. → [13.13](../weeks/13.13-debugging.md)

**Q:** Why start at "is it in the corpus?" → **A:** Many "RAG bugs" are missing data; you can't retrieve what was never ingested.

**Q:** Right chunk in context but wrong answer — where's the bug? → **A:** Generation (weak grounding, no escape hatch, high temp) or injection — not retrieval.

**Q:** ⭐ Most valuable debugging investment? → **A:** Logging the full trace: candidates with scores, reranked order, and the exact context string sent to the model.

---

## 13.14 · Security

**Q:** ⭐ What is indirect prompt injection? → **A:** Malicious instructions hidden in retrieved documents that the LLM may follow, because it can't reliably separate instructions from data. → [13.14](../weeks/13.14-security.md)

**Q:** ⭐ Why can't you fully patch injection? → **A:** It's structural to how LLMs process text; best defense is least privilege — limit what obeying an injected command can achieve.

**Q:** ⭐ Where must access control be enforced? → **A:** At retrieval (metadata pre-filter), before the LLM sees anything.

**Q:** How isolate multi-tenant RAG? → **A:** Separate index/namespace per tenant, or an un-omittable tenant filter; test isolation continuously.

**Q:** What is document poisoning? → **A:** Injecting false/malicious content into the corpus so RAG serves it authoritatively; defend with provenance, write controls, citations.

**Q:** Are embeddings safe to expose? → **A:** No — they can leak source text via inversion; treat the vector store as sensitive.

---

## 13.15 · Production

**Q:** ⭐ Why decompose RAG into services? → **A:** Stages have different scaling/latency/failure profiles; decoupling lets you scale, deploy, and fix each independently. → [13.15](../weeks/13.15-production-architecture.md)

**Q:** ⭐ Two planes and what they share? → **A:** Offline indexing (async, batched) and online serving (sync, latency-bound); they share only the state (vector DB, sparse index, cache).

**Q:** Why version the index? → **A:** Changing the embedding model requires re-embedding the whole corpus; versioning enables blue/green swaps and rollback.

**Q:** ⭐ Why monitor quality, not just uptime? → **A:** A "healthy" system can return wrong answers from a stale index or degraded retrieval; track freshness, refusal rate, faithfulness.

---

## 13.16 · Performance

**Q:** ⭐ Where does RAG latency/cost go? → **A:** The LLM generation call (80–95%), then reranking; retrieval and embedding are small. → [13.16](../weeks/13.16-performance.md)

**Q:** ⭐ What is semantic caching? → **A:** Returning a stored answer when a new query is embedding-similar to a past one — skipping retrieval and the LLM; the biggest latency/cost saver.

**Q:** Risk of a loose cache threshold? → **A:** Serving the wrong cached answer — a correctness bug.

**Q:** ⭐ Why does RAG let you use a smaller model? → **A:** Retrieval supplies the facts, so the model only reads/synthesizes rather than knows.

**Q:** Why must caches be ACL/tenant-scoped? → **A:** A query-only-keyed cache can serve one user's answer to another; and it must invalidate on index updates.

---

## 13.17 · Frameworks

**Q:** ⭐ What do RAG frameworks hide? → **A:** Every stage's defaults (parser, chunk size, overlap, embed model, metric, top-k, prompt) — the quality knobs. → [13.17](../weeks/13.17-frameworks.md)

**Q:** When do frameworks help most? → **A:** Prototyping, data-source connectors, swapping vector stores/models, standard patterns.

**Q:** ⭐ Pragmatic strategy? → **A:** Prototype with a framework, understand every stage, then own the parts that determine your quality.

**Q:** What to always verify in a framework? → **A:** ACL enforcement at retrieval, the actual defaults chosen, and hidden LLM calls/loops that add cost.

---

## 13.18 · Projects & Summary

**Q:** ⭐ The one thing to remember from RAG? → **A:** Retrieval quality is the ceiling on generation quality — the pipeline before the LLM decides whether the answer can be correct. → [13.18](../weeks/13.18-projects-summary.md)

**Q:** The minimal RAG project? → **A:** A semantic search engine — retrieval only, no LLM.

**Q:** What makes a "production" RAG API? → **A:** Two-plane service architecture, evaluation gates, ACL/PII security, caching, monitoring, safe re-indexing.

**Q:** Defend "RAG is a retrieval problem with a language model attached." → **A:** The LLM is the last, least-controllable stage; parsing, chunking, retrieval, filtering, reranking, and context decide whether it can be right.

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 13](../README.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
| 📄 Cheat sheet | [RAG cheat sheet](../cheat-sheets/rag-cheatsheet.md) |
| 📝 Quiz | [Quiz 01](../quizzes/quiz-01.md) |
