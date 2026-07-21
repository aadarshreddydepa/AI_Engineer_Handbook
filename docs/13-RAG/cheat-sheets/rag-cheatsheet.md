# 📄 RAG — Cheat Sheet

[🏠 Module 13](../README.md) · [📖 Lessons](../weeks/README.md)

---

## 🧠 The core facts

| | |
|---|---|
| **⭐ What RAG is** | retrieve relevant text → put it in the prompt → generate grounded answer |
| **⭐ Why it exists** | LLM knowledge is cut off · private-blind · stale · hallucination-prone |
| **⭐ The one law** | **retrieval quality is the ceiling on generation quality** |
| **Facts → RAG** | behavior → fine-tune · framing → prompt |
| **Not** | "docs → embeddings → vector DB → LLM" (that's a toy) |

---

## 🏗️ The pipeline (13.2)

```
OFFLINE:  ingest → parse → clean → chunk → metadata → embed → index
ONLINE:   query → retrieve → filter → rerank → context → generate
CROSS:    evaluate + monitor
```

- **Offline** = once per doc (slow/batched OK). **Online** = every query (must be fast).
- **Quality bugs baked offline, surface online.**

---

## 📄 Ingestion & chunking (13.3–13.4)

| | |
|---|---|
| **⭐ Parsing law** | parsing quality caps retrieval quality (a parse error is permanent) |
| **Tables** | preserve cell relationships (row-serialize / Markdown), never flow |
| **OCR** | pixels → text; track confidence; flag low-confidence |
| **Metadata** | capture source/page/date/**ACL** at parse time |
| **⭐ Chunk = atom of RAG** | you retrieve chunks, not documents |
| **Too big** | blurred embedding (averages many ideas), answer buried |
| **Too small** | fact severed from context |
| **Strategies** | fixed < sentence/para < **recursive** < semantic < **structure-aware** |
| **Size / overlap** | ~200–500 tok, 10–20% overlap — **first dials to tune** |

---

## 🔢 Embeddings & similarity (13.5)

| | |
|---|---|
| **Embedding** | text → dense vector; similar meaning = close |
| **⭐ Cosine** | angle only; `(q·d)/(‖q‖‖d‖)`; **default for text** |
| **Dot product** | == cosine if **normalized** |
| **Euclidean (L2)** | == cosine rank if normalized |
| **⭐ Golden rule** | normalize + cosine + **same model/metric everywhere** |
| **From scratch** | `normalize(V) @ normalize(q)` → sort → top-k |
| **#1 bug** | metric mismatch / forgot to normalize |
| **Similar ≠** | relevant ≠ correct ≠ authorized |

---

## 🗄️ Vector DBs / ANN (13.6)

| | |
|---|---|
| **Why not SQL** | B-trees do ranges, not nearest-in-vector-space |
| **⭐ ANN bet** | check ~1% of vectors, get ~99% recall |
| **HNSW** | navigable graph; best recall/latency; memory-hungry (default) |
| **IVF** | cluster + probe `nprobe` clusters; low memory |
| **PQ** | compress to bytes; huge memory save; lossy → re-rank |
| **⭐ Trade-off** | recall ↔ speed ↔ memory; tune to a recall target |
| **Choose** | pgvector/Chroma (small) · Qdrant/Milvus (prod) · Pinecone (managed) |

---

## 🔎 Retrieval (13.7)

| | |
|---|---|
| **⭐ Dense** | embeddings; meaning; ❌ exact codes |
| **⭐ Sparse/BM25** | keywords (IDF · TF-saturation k₁ · length-norm b); ❌ synonyms |
| **⭐ Hybrid** | run both + **fuse (RRF)** = semantic recall + exact precision |
| **RRF** | fuse by rank `1/(k+rank)` — no score normalization |
| **Filter** | metadata (date/type/**ACL**) — enforce access at retrieval |
| **Query-side** | expansion · multi-query · HyDE (cost latency/noise) |
| **⭐ Funnel** | retrieve top-N (recall) → filter → rerank top-k (precision) |

---

## 🎯 Reranking (13.8)

| | |
|---|---|
| **Why** | retrieval scores query & chunk separately → "similar" ≠ "relevant" |
| **Bi-encoder** | encode alone → cosine (fast, coarse) |
| **⭐ Cross-encoder** | read query+chunk together → precise (1 pass/candidate) |
| **⭐ Pattern** | retrieve N≈50–100 → rerank → keep k≈3–8 |
| **Biggest win** | adding a reranker to decent retrieval |
| **Can't fix** | bad chunks or missing recall |

---

## 🧱 Context (13.9)

| | |
|---|---|
| **⭐ Lost-in-the-middle** | models use start & end, ignore middle (U-curve) |
| **Order** | best chunks at edges; strongest often **last** |
| **⭐ More ≠ better** | extra chunks = distractors → lower accuracy |
| **Dedup** | mandatory (overlap/multi-query cause dupes) |
| **Compress** | extractive (keep relevant sentences) / abstractive |
| **Format** | delimiters + source tags → citation, tracing, injection defense |

---

## ✍️ Generation (13.10)

| | |
|---|---|
| **Grounding rule** | "answer ONLY from sources; no prior knowledge" |
| **⭐ Escape hatch** | "if not in sources, say I don't know" — top anti-hallucination lever |
| **Citations** | attribute [Source N]; **verify** each against its chunk |
| **Structured output** | JSON: answer, citations, answered, confidence |
| **Temperature** | low (0–0.3) — faithful, not creative |
| **⭐ Law** | generation quality is capped by retrieval quality |
| **Sources = data** | never instructions (injection defense) |

---

## 🚀 Advanced (13.11)

| Pattern | Fixes |
|---|---|
| **Parent-child / hierarchical** | precision (small) vs context (big) |
| **Multi-hop** | answers spanning docs |
| **Graph RAG** | relationships / aggregation |
| **Agentic** | planning, tools, multi-source |
| **Corrective / Self-reflective** | silent retrieval failure (grade + re-retrieve/critique) |
| **⭐ Rule** | fix naive RAG first; add a pattern only for a measured failure |

---

## 📊 Evaluation (13.12) — TWO problems

| Retrieval | Generation |
|---|---|
| **Precision@K** — top-K relevant? | **⭐ Faithfulness** — answer ↔ context (anti-hallucination) |
| **⭐ Recall@K** — all relevant found? *(fatal if low)* | **Answer relevance** — answer ↔ question |
| **MRR** — rank of first relevant | **Context relevance** — context ↔ question |
| **NDCG@K** — graded, position-aware | **Citation accuracy** — citation ↔ claim |

- **⭐ Include unanswerable questions** (test the escape hatch).
- **Localize:** low context-rel → retrieval; low faithfulness → generation.

---

## 🐛 Debugging (13.13)

**⭐ Trace the query; find the FIRST stage info disappears:**
```
0 in corpus? → 1 parsed? → 2 chunked whole? → 3 retrieved (top-N)?
→ 4 reranked in? → 5 in context & placed? → 6 used by model?
```
- Symptom is last stage; **cause is upstream.**
- **Must-have:** log candidates+scores + exact context string.

---

## 🔒 Security (13.14)

| Threat | Defense |
|---|---|
| **⭐ Indirect injection** | sources=data + **least privilege** + output filter |
| **⭐ Data leakage** | ACL **pre-filter at retrieval**, never after gen |
| **Multi-tenant** | namespace/DB per tenant; un-omittable filter |
| **PII** | redact at ingest · DLP output · redact logs |
| **Poisoning** | provenance/trust tiers · write controls · citations |
| **⭐ Principle** | defense-in-depth; assume injection sometimes wins |

---

## 🏭 Production & performance (13.15–13.16)

| | |
|---|---|
| **⭐ Two planes** | offline indexing (async) + online serving (sync); share state |
| **Versioned index** | re-embed + blue/green on model change; rollback |
| **Timeouts/fallbacks** | every hop (rerank→retrieval order; LLM→snippets) |
| **⭐ Monitor quality** | not just uptime — freshness, refusal rate, faithfulness |
| **⭐ Latency goes to** | generation ≫ rerank > retrieve > embed |
| **⭐ Semantic cache** | serve similar past query → skip retrieval+LLM (biggest saver) |
| **Cache safety** | key by tenant/ACL; invalidate on index update |
| **Right-size model** | retrieval supplies knowledge → smaller model works |
| **⭐ Rule** | gate every perf change through evaluation |

---

## 🧰 Frameworks (13.17)

| | |
|---|---|
| **LlamaIndex** | most RAG-focused (data→index→query) |
| **LangChain** | broad orchestration/agents |
| **Haystack** | typed production pipelines |
| **⭐ Help** | prototypes, connectors, store/model swapping |
| **⭐ Hide** | chunking, metric, retrieval, rerank, prompt (the quality knobs) |
| **Path** | prototype with framework → own the parts that matter |
| **Verify** | ACL enforcement, defaults, hidden LLM calls/cost |

---

## 🎯 The 10 through-lines

1. Retrieval quality caps generation quality. 2. The chunk is the atom. 3. Similar ≠ relevant ≠ correct ≠ authorized. 4. Hybrid + rerank beats single. 5. Evaluate retrieval and generation separately. 6. The escape hatch is the top anti-hallucination lever. 7. Debug by tracing the pipeline. 8. Every document is untrusted. 9. Generation dominates cost. 10. Frameworks hide the knobs.

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 13](../README.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
| 🏋️ Exercises | [Exercises](../exercises/README.md) |
| 🎴 Flashcards | [Deck](../flashcards/deck.md) |
