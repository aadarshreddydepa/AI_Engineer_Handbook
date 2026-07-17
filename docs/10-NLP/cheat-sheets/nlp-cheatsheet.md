# 📄 NLP — Cheat Sheet

[🏠 Module 10](../README.md) · [📖 Lessons](../weeks/README.md)

---

## 🧠 The core facts

| | |
|---|---|
| **The one problem** | text → vectors **without losing meaning** |
| **Distributional hypothesis** | ⭐ "know a word by the company it keeps" — the field's bedrock |
| **Why language is hard** | ambiguity · context · compositionality · long tail (Zipf) |
| **Syntax / semantics / pragmatics** | grammar / literal meaning / intended meaning |
| **⭐ The arc** | sparse → dense → **contextual** (one-hot → embeddings → attention) |

---

## 🔤 Text processing (10.2)

| | |
|---|---|
| **Normalize first** | `unicodedata.normalize("NFC", s)` — "café" ≠ "café" |
| **Case** | `casefold()`; ⚠️ destroys NER signal |
| **Tokenize** | regex/spaCy, **never `.split()`** |
| **Stemming vs lemmatization** | crude suffix-chop (non-words) vs dict+POS (real base) — both obsolete with neural |
| **⚠️ Stop words** | topic-classification only; **never** before sentiment/sequence models |
| **⭐ Subword (BPE/WordPiece)** | the modern default — **no unknown words**, language-agnostic |

---

## 📊 Text representation (10.3)

| Rep | What | Kills |
|---|---|---|
| **One-hot** | 1 at word index | huge, **orthogonal (dot=0)** |
| **Bag of Words** | word counts | **word order** |
| **N-grams** | short-phrase counts | sparsity explodes (V²,V³) |
| **⭐ TF-IDF** | `count × log(N/df)` | common words → 0 weight |

**IDF's log** compresses the huge df range. **Fit on train only** (it's a parameter). **The gap:** none capture **similarity**.

---

## 🧭 Embeddings (10.4) ⭐

| | |
|---|---|
| **Embedding** | dense vector per word; **direction = meaning** |
| **⭐ Word2Vec** | shallow net on a fake task (predict context); keep the weights |
| **CBOW / skip-gram** | context→word (fast) / word→context (better; default) |
| **⭐ Negative sampling** | V-way softmax → k+1 "real vs fake pair?" — 6 updates not a million |
| **GloVe** | count-based cousin: `wᵢ·wⱼ ≈ log(co-occurrence)` |
| **Similarity** | **cosine**, not Euclidean |
| **Analogy** | `king − man + woman ≈ queen` (real but oversold) |
| **⭐ Bias** | co-occurrence learning ⇒ inherited prejudice as geometry |
| **⭐ The limit** | one vector per word, context-free → **attention fixes it** |

---

## 🔁 Sequence models (10.5)

| | |
|---|---|
| **Hidden state** | fixed-size running summary of the sequence so far |
| **Why order matters** | "dog bites man" ≠ "man bites dog" |
| **⭐ Vanishing gradient (NLP)** | λⁿ kills long-range agreement/coreference after ~10 words |
| **LSTM / GRU** | gated **cell state** → memory over 100s of steps; GRU first |
| **Bidirectional** | sees whole sentence — **not for generation/streaming** |
| **⭐ Seq2seq bottleneck** | whole input crammed into one vector → **attention (10.7)** |
| **⭐ Fatal cost** | RNNs are **sequential** → can't parallelize → Transformers win |

---

## 🎯 NLP tasks — the 4 shapes (10.6)

| Shape | Tasks | Head | Metric |
|---|---|---|---|
| **Seq → label** | sentiment, spam, intent | pool → softmax | acc / **macro-F1** |
| **Seq → per-token** | NER, POS | per-token(+**CRF**) | **entity-F1** |
| **Seq → seq** | translation, summary, gen | decoder (10.8) | BLEU/ROUGE/ppl |
| **Pair → score** | similarity, QA, retrieval | compare encodings | cosine / recall@k |

**⭐ Every model = embed → encode → head.** NER needs a **CRF** (labels constrain each other). **Retrieval = bi-encoder retrieve + cross-encoder rerank.**

---

## 🔥 Attention (10.7) ⭐⭐

```
Attention(Q,K,V) = softmax(QKᵀ / √dₖ) · V
```

| | |
|---|---|
| **Q / K / V** | what I seek / how I'm matched / what I deliver (learned projections) |
| **QKᵀ** | (n×n) every token's relevance to every other |
| **⭐ √dₖ scale** | variance fix; without it softmax saturates → gradients vanish |
| **softmax rows → × V** | weights (sum 1) → weighted blend of values |
| **Self-attention** | Q,K,V same sequence → **contextual embeddings** ("bank" differs by sentence) |
| **Cross-attention** | Q one seq, K/V another (decoder→encoder) |
| **Multi-head** | h parallel attentions → many relationship types, ~same cost |
| **⭐ O(n²)** | quadratic in length — the central LLM problem |
| **vs RNN** | O(1) path length + parallel, at O(n²) cost |

---

## 🔀 Seq2seq (10.8)

| | |
|---|---|
| **Encoder → decoder** | understand → generate one token at a time (autoregressive) |
| **⭐ Attention in seq2seq** | decoder attends over ALL encoder states → no bottleneck |
| **Teacher forcing** | train on ground-truth previous token |
| **Exposure bias** | trained on perfect prefixes, tested on own outputs |
| **Greedy / beam / sampling** | argmax / k-best (bland) / random (LLM default) |
| **⭐ Lineage** | seq2seq → +attention → **drop the RNN = Transformer** |

---

## 📏 Evaluation (10.9)

| Metric | Task | Watch out |
|---|---|---|
| **Macro-F1** | classification | use for imbalance |
| **Entity-F1** | NER | not token accuracy |
| **BLEU** | translation | n-gram **precision**; no semantics; relative only |
| **ROUGE** | summarization | n-gram **recall**; no semantics |
| **⭐ Perplexity** | language modeling | `exp(cross-entropy)`; tokenizer-bound; ≠ usefulness |
| **Human / LLM-judge** | generation | the real truth |

**⭐ Generation has no single answer → every auto metric is a proxy → pair with human eval.**

---

## 🗂️ Data (10.10)

| | |
|---|---|
| **⭐ The bottleneck** | labels, not the model |
| **⭐ Inter-annotator agreement (κ)** | chance-corrected; the **ceiling** on model accuracy |
| **Near-duplicate leakage** | dedup **before** splitting |
| **Author/temporal leakage** | split by author/source/time |
| **⭐ PII in free text** | redact at ingestion; the highest-stakes risk |
| **Bias** | the default; measure (disaggregate), document, mitigate |

---

## 🔧 PyTorch pipeline (10.11)

| Stage | Do |
|---|---|
| **Vocab** | specials first (`<pad>`=0,`<unk>`=1); **train only**; `min_freq` |
| **Embedding** | `nn.Embedding(V, d, padding_idx=0)`; init from GloVe if scarce |
| **⭐ Padding** | `pack_padded_sequence` (RNN) or **attention mask** |
| **Head** | pool→Linear (classify) · per-token + `ignore_index` (tag) |
| **Loss** | `CrossEntropyLoss` on **logits** (09.3) |
| **Loop** | ⭐ **09.10, unchanged** + `clip_grad_norm_` |

---

## 🤗 Hugging Face (10.12)

| Pillar | Key point |
|---|---|
| **`tokenizers`** | subword (BPE/WordPiece); **must match the model** |
| **`transformers`** | pretrained BERT (understand) / GPT (generate) / T5 (text-to-text) |
| **`datasets`** | memory-mapped, streaming |
| **⭐ Fine-tuning** | transfer learning: few labels, minutes, beats from-scratch |
| **⭐ #1 bug** | tokenizer ≠ model → garbage output, **no crash** |

---

## 🚀 Production (10.13)

| | |
|---|---|
| **⭐ #1 bug** | **train/serve skew** — preprocessing must be byte-identical |
| **Ship the tokenizer** | with the model; never reconstruct |
| **⭐ Latency** | tokenization + **O(n²) attention** + autoregressive gen |
| **⭐ Distill first** | ~2× faster for ~3% accuracy |
| **⭐ Cache** | pre-compute static embeddings **offline** |
| **Monitor** | input drift + prediction canary + **`<unk>`/vocab drift** |

---

## ⚖️ Ethics & safety (10.14)

| Harm | Fix |
|---|---|
| **Bias** | measure (WEAT, disaggregate, counterfactual); balance; review |
| **Toxicity** | audited filters; **check dialect fairness** |
| **⭐ Privacy** | **redact at ingestion**, dedup, DP, output filter |
| **⭐ Hallucination** | RAG grounding, citations, calibration, review |
| **⭐ Docs** | datasheet + **model card** |

**⭐ An NLP model is a queryable compression of human text — bias, secrets, falsehood included.**

---

## 🎯 The ten sentences

1. **All of NLP is one problem: text → vectors without losing meaning.**
2. **One-hot/BoW are meaning-blind (orthogonal); TF-IDF is a strong baseline anyway.**
3. **Embeddings make meaning geometry — similar words point the same way.**
4. **Word order is signal; sequence models keep it, attention preserves it via position.**
5. **Attention = softmax(QKᵀ/√dₖ)·V — a soft dictionary lookup you can write by hand.**
6. **Self-attention gives contextual embeddings — "bank" finally differs by sentence.**
7. **Attention beats RNNs on path length and parallelism, at O(n²) cost — hence the Transformer.**
8. **Generation metrics (BLEU/ROUGE/perplexity) measure overlap/fluency, not truth.**
9. **The training loop, evaluation, and MLOps are Modules 08–09, unchanged.**
10. **Bias, PII, and hallucination are structural in language — measure, mitigate, document.**

---

[⬆ Module 10](../README.md) · [📖 Lessons](../weeks/README.md) · [🧠 Flashcards](../flashcards/deck.md) · [📝 Quiz](../quizzes/quiz-01.md)
