# 📝 Module 13 · RAG — Quiz 01

[🏠 Module 13](../README.md) · [📖 Lessons](../weeks/README.md) · [✅ Answers](answers-01.md)

> **40 questions across all 18 lessons.** Aim for an explanation, not just a phrase — the [answers](answers-01.md) grade reasoning. Target: **32/40** to consider the module solid.

---

## Part A · Why & Architecture (13.1–13.2)

**1.** Name the four failure modes of a bare LLM that RAG addresses.

**2.** Compare prompting, RAG, and fine-tuning — what does each change, and when do you pick each?

**3.** Someone says "GPT has a huge context window now, so RAG is obsolete." Respond.

**4.** Why is "documents → embeddings → vector DB → LLM" a dangerous mental model? Name three stages it omits and what each does.

**5.** Distinguish index-time (offline) from query-time (online) stages. Why does this split drive engineering decisions?

## Part B · Index-time (13.3–13.6)

**6.** Explain why "parsing quality caps retrieval quality." Give a concrete failure.

**7.** How should tables be extracted so their meaning survives into a chunk, and why?

**8.** Why is the chunk called "the atom of RAG"? What happens if a fact straddles a chunk boundary?

**9.** Explain the chunk-size trade-off in terms of what a single embedding vector represents.

**10.** Rank fixed-size, recursive, semantic, and structure-aware chunking, and justify the ordering.

**11.** What is chunk overlap, what problem does it solve, and what does it cost?

**12.** Define cosine similarity, dot product, and Euclidean distance. When are they equivalent?

**13.** What is the most common bug in similarity search, and how do you avoid it?

**14.** Write (in words) how semantic search works from scratch. Why is it O(N·d), and why doesn't that scale?

**15.** Why can't a normal relational database do vector search well?

**16.** Contrast HNSW, IVF, and PQ — how does each avoid scanning all vectors?

**17.** State the ANN trade-off. How do you decide if your recall is "good enough"?

## Part C · Query-time (13.7–13.10)

**18.** Give a query dense retrieval fails and sparse handles, and vice-versa. Why?

**19.** Explain BM25 term by term (IDF, TF saturation, length normalization).

**20.** What is hybrid search? Explain RRF and why it avoids score normalization.

**21.** Why retrieve a large candidate set and then rerank, rather than retrieving the final few directly?

**22.** Explain the difference between a bi-encoder and a cross-encoder, and the resulting cost/accuracy trade-off.

**23.** Why can't you run a cross-encoder over the entire corpus?

**24.** What is lost-in-the-middle, and how do you mitigate it?

**25.** Why does adding more retrieved chunks often reduce answer quality?

**26.** Why is deduplication mandatory in context construction?

**27.** What is the escape hatch, and how does it affect both hallucination and observability?

**28.** Is a cited source a verified source? What follows for a citation-critical system?

**29.** Why is low temperature appropriate for most RAG generation?

## Part D · Advanced & Evaluation (13.11–13.12)

**30.** Name three naive-RAG failure modes and the advanced pattern that fixes each.

**31.** Explain parent-child (small-to-big) retrieval and the tension it resolves.

**32.** When is the added complexity of an advanced pattern justified?

**33.** Why must RAG evaluation separate retrieval from generation?

**34.** Which retrieval metric matters most for RAG, and why? Contrast it with precision.

**35.** Define faithfulness, answer relevance, and context relevance. What does a drop in each localize?

**36.** Why must an evaluation set include unanswerable questions?

## Part E · Operate (13.13–13.17)

**37.** Describe your systematic approach to debugging a wrong RAG answer. Why is the cause rarely at the generation stage?

**38.** Explain indirect prompt injection in RAG. Why is it structural, and what's the strongest defense?

**39.** Where do RAG latency and cost mostly go, and what are the top optimizations that follow? What's the risk with semantic caching?

**40.** What do RAG frameworks hide, and why did this module have you build the core by hand first?

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 13](../README.md) |
| ✅ Answers | [answers-01.md](answers-01.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
