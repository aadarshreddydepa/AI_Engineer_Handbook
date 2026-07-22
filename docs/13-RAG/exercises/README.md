# 🏋️ Module 13 · RAG — Exercises

[🏠 Module 13](../README.md) · [📖 Lessons](../weeks/README.md) · [🧩 Projects](../projects/)

> Build-it exercises, ordered along the module's spine: **index the corpus → retrieve well → generate & evaluate → operate**. If you do only four, do ⭐ **E5, E9, E12, E15** — semantic search from scratch, hybrid + rerank, the two-family evaluation, and the secured production layer. Together they are the module.
>
> Each exercise lists a **goal**, **constraints**, and a **done-when** (an objective, checkable success criterion).

---

## Tier 1 · Index-time (13.3–13.6)

### E1 · Multi-format ingestion
**Goal:** parse PDF, HTML, DOCX, CSV, MD into a uniform `Document{text, metadata}` with structural table extraction and OCR fallback.
**Done-when:** a known table cell is retrievable as text; low-confidence OCR pages are flagged; every doc carries source/page/date/ACL metadata. → [13.3](../weeks/13.3-ingestion-parsing.md)

### E2 · Parsing autopsy
**Goal:** extract a multi-column PDF with two libraries; diff outputs.
**Done-when:** you can point to exactly where reading order and table structure break in the weaker parser. → [13.3](../weeks/13.3-ingestion-parsing.md)

### E3 · Chunking size/overlap sweep
**Goal:** chunk one corpus across {128,256,512,1024} tokens × {0,10,20}% overlap.
**Constraints:** measure size in **tokens**, not characters.
**Done-when:** a Recall@5 surface identifies the optimum; a boundary-straddling fact is unretrievable at 0% overlap and retrievable at 20%. → [13.4](../weeks/13.4-chunking.md)

### E4 · Structure-aware chunking
**Goal:** split Markdown on headings, carrying the heading path as metadata.
**Done-when:** a fact under a specific heading retrieves better than with fixed-size chunking, and each chunk is sensible read alone. → [13.4](../weeks/13.4-chunking.md)

### ⭐ E5 · Semantic search from scratch
**Goal:** NumPy-only semantic search — embed → normalize → matrix → cosine top-k. No vector DB, no framework.
**Constraints:** no ANN library in the core.
**Done-when:** (1) it retrieves paraphrases with zero lexical overlap; (2) normalized dot == cosine (assert close); (3) latency grows O(N), motivating ANN. **The most important exercise in the first half.** → [13.5](../weeks/13.5-embeddings-similarity.md)

### E6 · Metric-mismatch bug hunt
**Goal:** demonstrate the #1 similarity bug.
**Done-when:** you show that un-normalized dot ≠ cosine and that querying an index with the wrong metric silently returns garbage — then fix it. → [13.5](../weeks/13.5-embeddings-similarity.md)

### E7 · ANN vs FLAT
**Goal:** index 100k vectors with HNSW and brute force; sweep `efSearch`.
**Done-when:** a recall–latency curve (HNSW vs FLAT ground truth) shows the trade-off; you pick a config hitting ≥95% Recall@10 at minimum latency. → [13.6](../weeks/13.6-vector-databases.md)

---

## Tier 2 · Query-time (13.7–13.10)

### E8 · BM25 from scratch
**Goal:** implement BM25 scoring (IDF, TF saturation, length norm).
**Done-when:** IDF down-weights common terms; length normalization prevents long-doc bias; it beats dense retrieval on a code/ID query set. → [13.7](../weeks/13.7-retrieval.md)

### ⭐ E9 · Hybrid search with RRF
**Goal:** fuse dense + BM25 with Reciprocal Rank Fusion; add metadata + ACL filtering.
**Done-when:** (1) hybrid Recall@10 ≥ max(dense, sparse) on a mixed query set; (2) RRF needs no score normalization; (3) forbidden docs never appear regardless of similarity. → [13.7](../weeks/13.7-retrieval.md)

### E10 · Reranking lift
**Goal:** add a cross-encoder over the retrieved top-50.
**Done-when:** reranked NDCG@5 > retrieval-only; you show a case where cosine's top-1 is wrong and the reranker fixes it. → [13.8](../weeks/13.8-reranking.md)

### E11 · Context construction
**Goal:** dedup + order + budget-fit reranked chunks; reproduce lost-in-the-middle.
**Done-when:** answer accuracy follows the U-curve by chunk position; dedup improves quality; the exact prompt string is inspectable. → [13.9](../weeks/13.9-context-construction.md)

### ⭐ E12 · Grounded generation with escape hatch + citations
**Goal:** a RAG prompt that answers only from sources, cites [Source N], and declines when unsupported.
**Done-when:** (1) fabrication rate on unanswerable questions drops sharply with the escape hatch; (2) every citation's quote is verified present in its chunk; (3) low temperature beats high on faithfulness. → [13.10](../weeks/13.10-generation.md)

---

## Tier 3 · Operate & improve (13.11–13.17)

### E13 · Corrective / multi-hop RAG
**Goal:** decompose a multi-part question, retrieve per sub-question, grade relevance, and re-retrieve on poor results.
**Done-when:** a 2-hop question answered correctly where single-shot fails; the corrective loop is bounded by a max-iterations cap. → [13.11](../weeks/13.11-advanced-rag.md)

### ⭐ E14 · Two-family evaluation harness
**Goal:** score retrieval (P@K, Recall@K, MRR, NDCG) and generation (faithfulness, answer/context relevance, citation accuracy) separately.
**Constraints:** include unanswerable and adversarial cases.
**Done-when:** metrics match hand-computed values; the harness localizes each failure as retrieval-vs-generation; unanswerable questions are scored on correct declines. → [13.12](../weeks/13.12-evaluation.md)

### E15 · Trace-based debugging
**Goal:** instrument the full per-query trace (candidates+scores → reranked → exact context → answer); plant a bug at each stage.
**Done-when:** the trace localizes every planted bug to the correct stage; the gold chunk's drop-out point is detected. → [13.13](../weeks/13.13-debugging.md)

### ⭐ E16 · Secure RAG layer
**Goal:** ACL/tenant pre-filter (un-omittable), PII redaction + output DLP, sources-as-data prompting, provenance tiers, audit logging.
**Done-when:** (1) a cross-tenant isolation test asserts zero cross-tenant hits (and fails when the filter is removed); (2) planted PII is redacted before embedding and blocked in output; (3) an injected instruction has no privileged effect. → [13.14](../weeks/13.14-security.md)

### E17 · Semantic cache (safe)
**Goal:** add an embedding-similarity answer cache, tenant/ACL-scoped, invalidated on index update.
**Done-when:** measurable hit rate + latency/cost reduction on a repetitive query stream; a query-only-keyed cache is shown to leak across users, then fixed by ACL-scoping. → [13.16](../weeks/13.16-performance.md)

### E18 · Framework vs from-scratch
**Goal:** build the same RAG with a framework and hand-rolled; expose the framework's hidden defaults.
**Done-when:** both reach the same eval bar after tuning; you can name the chunk size, overlap, embedding model, metric, and top-k the framework chose; ACL enforcement is verified in both. → [13.17](../weeks/13.17-frameworks.md)

---

## Capstone · Production RAG API (Project 7)

### ⭐ E19 · End-to-end production RAG
**Goal:** ship the two-plane service ([13.15](../weeks/13.15-production-architecture.md)) with incremental indexing, hybrid+rerank+ACL retrieval, grounded cited generation, semantic caching, a golden-set eval gate, and a monitoring dashboard.
**Done-when:** measurable Recall@k + faithfulness on the golden set; zero cross-tenant leakage; injected instructions have no privileged effect; a blue/green embedding-model upgrade completes with no downtime. → [13.18](../weeks/13.18-projects-summary.md)

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 13](../README.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
| 📝 Quiz | [Quiz 01](../quizzes/quiz-01.md) |
| 🎴 Flashcards | [Deck](../flashcards/deck.md) |
| 📄 Cheat sheet | [RAG cheat sheet](../cheat-sheets/rag-cheatsheet.md) |
