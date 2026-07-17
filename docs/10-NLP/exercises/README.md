# 🏋️ Module 10 · NLP — Exercises

[🏠 Module 10](../README.md) · [📖 Lessons](../weeks/README.md) · [🧩 Projects](../projects/)

> Build-it exercises, ordered along the module's spine: **represent → sequence → attend → engineer.** If you do only three, do ⭐ **E3, E7, E9** — they are the module in miniature (sparse baseline → embeddings → attention by hand).
>
> Each exercise lists a **goal**, **constraints**, and a **done-when** (an objective, checkable success criterion).

---

## Tier 1 · Representation (10.1–10.4)

### E1 · The meaning-blindness demo
**Goal:** make BoW's two fatal flaws concrete. Take 20 sentence pairs where order or negation flips meaning; represent with bag-of-words; compute within-pair cosine similarity.
**Done-when:** you produce a table showing opposite-meaning pairs rated nearly identical, and you predict which later lesson fixes each failure. → [10.1](../weeks/10.1-introduction-to-nlp.md), [10.3](../weeks/10.3-text-representation.md)

### E2 · BPE by hand
**Goal:** run 5 iterations of Byte-Pair Encoding on the toy corpus `["low","lower","lowest","newer","newest"]`, starting from characters and merging the most frequent adjacent pair each round.
**Done-when:** you write out the vocabulary after each merge, then confirm a real `tokenizers` library reproduces your merges on the same corpus. → [10.2](../weeks/10.2-text-processing.md)

### ⭐ E3 · TF-IDF from scratch, beat it with nothing
**Goal:** implement `fit_tfidf`/`transform_tfidf` in NumPy; verify against `TfidfVectorizer` with `np.allclose`; train a logistic-regression sentiment/spam baseline.
**Constraints:** NumPy + sklearn's classifier only; **fit the vectorizer on train only**.
**Done-when:** (1) `np.allclose` passes vs sklearn; (2) "the" scores ≈ 0 and a rare word scores high; (3) you report the baseline F1 — **keep this number**, every later model must beat it. → [10.3](../weeks/10.3-text-representation.md)

### E4 · Embedding geometry
**Goal:** load pretrained GloVe. Implement `cosine(a,b)` and `analogy(a,b,c)` = nearest word to `b − a + c` (excluding inputs).
**Done-when:** cosine ranks related pairs above unrelated ones; at least 3 of {capital-country, plural-singular, comparative} analogies return the right word; and you report one analogy that *fails* (they're fragile). → [10.4](../weeks/10.4-word-embeddings.md)

### E5 · Measure embedding bias
**Goal:** compute `cosine("he", profession)` vs `cosine("she", profession)` for 15 professions.
**Done-when:** you produce a ranked gender-skew table and write one paragraph on what a hiring system built on these embeddings would do. → [10.4](../weeks/10.4-word-embeddings.md), [10.14](../weeks/10.14-ethics-safety.md)

---

## Tier 2 · Sequence & attention (10.5–10.8)

### E6 · Order is signal
**Goal:** build a small dataset of sentence pairs with identical words / opposite meaning. Train the E3 TF-IDF baseline and a small LSTM.
**Done-when:** the LSTM separates the pairs and the baseline can't — quantified on a held-out "hard" subset. → [10.5](../weeks/10.5-sequence-models.md)

### ⭐ E7 · Attention from scratch, verified
**Goal:** implement `softmax`, `scaled_dot_product_attention`, `self_attention`, and `multi_head_attention` in **NumPy only**.
**Constraints:** no framework in the forward pass; include the `√dₖ` scaling and a causal-mask option.
**Done-when:** (1) `torch.allclose` vs PyTorch's attention on random inputs; (2) attention weights sum to 1 per row; (3) the causal mask zeroes all future weights; (4) a float64 gradient check passes. **The single most important exercise in the module.** → [10.7](../weeks/10.7-attention.md)

### E8 · The √dₖ ablation
**Goal:** run your attention with and without the `√dₖ` division for dₖ ∈ {4, 64, 512}. Print the max softmax weight each time.
**Done-when:** you show saturation (max weight → 1) growing with dₖ when unscaled, and explain the vanishing-gradient consequence. → [10.7](../weeks/10.7-attention.md)

### E9 · ⭐ Resolve polysemy with self-attention
**Goal:** build toy embeddings where "bank" is equidistant from "river" and "money." Run self-attention on "river bank" and "money bank."
**Done-when:** "bank"'s output vector **differs** between the two sentences — a contextual embedding — and you can point to the attention weights that caused it. This is [10.4](../weeks/10.4-word-embeddings.md)'s limitation, solved. → [10.7](../weeks/10.7-attention.md)

### E10 · Feel the bottleneck, then fix it
**Goal:** train an RNN seq2seq with and without attention on a reversal or date-normalization task. Plot accuracy/BLEU vs input length.
**Done-when:** the no-attention model falls off a cliff as length grows and the attention model doesn't; you extract and plot the cross-attention alignment heatmap. → [10.8](../weeks/10.8-seq2seq.md)

### E11 · Decoding bake-off
**Goal:** for one trained seq2seq model, generate with greedy, beam (k=1,3,5,10), and top-p sampling.
**Done-when:** you compare quality and diversity, and identify where beam gets repetitive vs where sampling wanders. → [10.8](../weeks/10.8-seq2seq.md)

---

## Tier 3 · Engineering & ethics (10.9–10.14)

### E12 · The metrics that lie
**Goal:** implement BLEU, ROUGE-1/2/L, and perplexity from scratch; verify vs `sacrebleu`/`rouge-score`.
**Done-when:** `np.allclose` vs the libraries; you find one translation with high BLEU but wrong meaning and one correct translation with low BLEU; and you verify `perplexity == exp(cross_entropy)` numerically. → [10.9](../weeks/10.9-evaluation.md)

### E13 · Agreement is the ceiling
**Goal:** have two people (or two labeling passes) annotate 50 texts for a subjective task; compute raw agreement and Cohen's κ.
**Done-when:** you report both, interpret the gap, and state the achievable accuracy ceiling your model faces. → [10.10](../weeks/10.10-nlp-data.md)

### E14 · Find the leak
**Goal:** take a public text-classification dataset; search for exact and near-duplicate documents across the train/test split.
**Done-when:** you report how many duplicates cross the split and estimate the score inflation; then dedup and re-measure. → [10.10](../weeks/10.10-nlp-data.md)

### ⭐ E15 · The full PyTorch pipeline
**Goal:** build vocab (train only, `<pad>`/`<unk>`), `nn.Embedding(padding_idx=0)`, a BiLSTM classifier with correct padding+packing, and the [09.10 loop](../../09-Deep-Learning/weeks/09.10-training-loop.md) with gradient clipping.
**Constraints:** overfit one batch to ~100% before full training ([09.15](../../09-Deep-Learning/weeks/09.15-debugging.md)).
**Done-when:** (1) overfit-one-batch passes; (2) removing `pack_padded_sequence` measurably hurts accuracy (prove the masking matters); (3) it beats the E3 TF-IDF baseline on the hard subset. → [10.11](../weeks/10.11-nlp-with-pytorch.md)

### E16 · Fine-tune and compare
**Goal:** fine-tune DistilBERT on the E3/E15 task using its own tokenizer.
**Done-when:** a head-to-head table (TF-IDF vs BiLSTM vs DistilBERT: F1, training time, params) and a **data-efficiency curve** (F1 vs #labels) showing the Transformer wins most when labels are scarce. → [10.12](../weeks/10.12-modern-libraries.md)

### E17 · Break it with skew
**Goal:** write a shared preprocessing function and a test asserting the training and serving paths produce identical token IDs on 100 texts. Then introduce a subtle difference (a stray `.lower()`).
**Done-when:** the skew test catches it, and you measure the accuracy hit the skew would have caused in production. → [10.13](../weeks/10.13-production.md)

### E18 · The safety audit
**Goal:** for a model you built, run a bias audit (WEAT or counterfactual), a PII scan of the training data, and (if generative) a hallucination spot-check; assemble a **model card**.
**Done-when:** the model card reports intended use, disaggregated metrics, known biases, and limitations — the artifact you'd ship with any real NLP system. → [10.14](../weeks/10.14-ethics-safety.md)

---

## 🎓 Capstone challenge

### E19 · The end-to-end proof
Combine E3 + E7 + E15 into one repo: a TF-IDF baseline, attention written from scratch and verified with `torch.allclose`, a full PyTorch classifier that beats the baseline, and a `pytest` suite with a TF-IDF-vs-sklearn test, an attention-equality test, and an overfit-one-batch test.
**Done-when:** `pytest` passes all three. This repo proves you understand NLP from counts to attention — not just that you can call `pipeline()`. → [10.15](../weeks/10.15-projects-summary.md)

---

> [!TIP]
> The gradient you check in E7 is the same `softmax(QKᵀ/√dₖ)·V` that runs every LLM. Do not skip the hand-build to get to Hugging Face faster — the library only makes sense *because* of the hand-build.

[🏠 Module 10](../README.md) · [📝 Quiz](../quizzes/quiz-01.md) · [🧠 Flashcards](../flashcards/deck.md) · [🧩 Projects](../projects/)
