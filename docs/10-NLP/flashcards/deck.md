# 🧠 Module 10 · NLP — Flashcard Deck

[🏠 Module 10](../README.md) · [📖 Lessons](../weeks/README.md) · [📄 Cheat sheet](../cheat-sheets/nlp-cheatsheet.md)

> **~90 cards.** Cover the answer, say it aloud, *then* check. ⭐ marks the ones that carry the module.

---

## 10.1 · Introduction

**Q:** ⭐ What is the one problem all of NLP solves? → **A:** Turning text into vectors **without losing meaning**. → [10.1](../weeks/10.1-introduction-to-nlp.md)

**Q:** State the distributional hypothesis. → **A:** A word's meaning is approximated by the distribution of contexts it appears in — "know a word by the company it keeps."

**Q:** ⭐ Why is language hard, in four words? → **A:** Ambiguity, context, compositionality, long-tail.

**Q:** Syntax vs semantics vs pragmatics? → **A:** Grammar / literal meaning / intended meaning in context.

**Q:** Why can't a lookup table do NLP? → **A:** Language is compositional — infinitely many valid sentences; you must generalize.

**Q:** Why does every NLP system need an unknown-word plan? → **A:** Zipf's law guarantees you meet unseen words at inference.

---

## 10.2 · Text processing

**Q:** Why normalize Unicode first? → **A:** The same visible string can have different byte forms ("café" ≠ "café"); NFC collapses them. → [10.2](../weeks/10.2-text-processing.md)

**Q:** Why is `str.split()` a bad tokenizer? → **A:** It glues punctuation to words and shreds URLs, contractions, numbers.

**Q:** ⭐ Stemming vs lemmatization? → **A:** Rule-based suffix chopping (fast, non-words) vs dictionary+POS lookup (real base forms).

**Q:** When is stop-word removal dangerous? → **A:** Sentiment ("not"), phrase search, and any sequence/Transformer model.

**Q:** ⭐ What problem does subword tokenization solve? → **A:** The long tail — any word decomposes into known subwords, so no unknown tokens.

**Q:** Why is lowercasing task-dependent? → **A:** Noise for topic classification; destroys the capitalization signal NER relies on.

---

## 10.3 · Text representation

**Q:** ⭐ Why are one-hot vectors "meaning-blind"? → **A:** Every distinct word is orthogonal (dot=0); can't encode that two words are related. → [10.3](../weeks/10.3-text-representation.md)

**Q:** What does bag-of-words throw away? → **A:** All word order — "dog bites man" = "man bites dog".

**Q:** ⭐ What is TF-IDF? → **A:** `count × log(N/df)` — frequent-and-informative words score high, ubiquitous words ~0.

**Q:** Why is IDF a logarithm? → **A:** Document frequency spans orders of magnitude; the log compresses it so one rare word doesn't dominate.

**Q:** ⭐ Why fit the vectorizer on train only? → **A:** IDF and vocab are learned parameters; fitting on test leaks corpus statistics.

**Q:** What do n-grams buy and cost? → **A:** Recover local order, but explode the feature space (V²,V³) into sparsity.

**Q:** Why still learn count-based methods? → **A:** TF-IDF + linear model is a fast, interpretable, hard-to-beat baseline.

---

## 10.4 · Word embeddings ⭐

**Q:** ⭐ What is a word embedding? → **A:** A dense vector per word, learned so similar-meaning words are geometrically close (direction = meaning). → [10.4](../weeks/10.4-word-embeddings.md)

**Q:** What's the "fake task" in Word2Vec? → **A:** Predict a word from context (CBOW) or context from a word (skip-gram); discard predictions, keep the weights.

**Q:** CBOW vs skip-gram? → **A:** context→target (faster) vs target→context (better on rare words; the default).

**Q:** ⭐ What does negative sampling do? → **A:** Replaces the intractable V-way softmax with a binary "real vs random pair" task — updates 1+k vectors, not V.

**Q:** How is GloVe different? → **A:** Factorizes a global co-occurrence count matrix instead of predicting from local windows; similar result.

**Q:** Why cosine, not Euclidean? → **A:** Meaning is direction; cosine ignores magnitude (≈ frequency).

**Q:** ⭐ The one thing embeddings can't do? → **A:** Give a word different vectors in different contexts — static embeddings blur polysemy ("bank").

**Q:** Where does embedding bias come from? → **A:** The distributional hypothesis — learning meaning from human co-occurrence encodes human prejudice as geometry.

---

## 10.5 · Sequence models

**Q:** What is a hidden state? → **A:** A fixed-size vector updated after each word; the running summary of the sequence so far. → [10.5](../weeks/10.5-sequence-models.md)

**Q:** Why can an LSTM handle negation when BoW can't? → **A:** It reads in order, so its state already contains "not" when it reaches "good."

**Q:** ⭐ How does the vanishing gradient show up in NLP? → **A:** Failed long-range dependencies — subject-verb agreement, coreference, long-distance negation.

**Q:** What does the LSTM cell state do? → **A:** A near-linear (gated, additive) memory path so gradients survive across hundreds of steps.

**Q:** When can't you use a bidirectional model? → **A:** Generation and streaming — no access to future tokens.

**Q:** ⭐ What is the seq2seq bottleneck? → **A:** The encoder compresses the whole input into one fixed vector; long inputs don't fit → attention fixes it.

**Q:** ⭐ Why did the field abandon RNNs? → **A:** They're inherently sequential — can't parallelize across time, wasting the GPU.

---

## 10.6 · NLP tasks

**Q:** ⭐ What are the four NLP I/O shapes? → **A:** Seq→label, seq→per-token-labels, seq→seq, pair→score. → [10.6](../weeks/10.6-nlp-tasks.md)

**Q:** What's shared across NLP tasks? → **A:** The front end (embeddings + encoder); only head, loss, and metric change.

**Q:** What is the BIO scheme? → **A:** Begin/Inside/Outside tags that turn span-finding (NER) into per-token classification.

**Q:** ⭐ Why does NER add a CRF? → **A:** Per-token softmax can emit illegal sequences (O I-PER); a CRF enforces globally consistent tags.

**Q:** Why entity-F1 over token accuracy for NER? → **A:** Token accuracy over-credits partial spans; you care about whole entities.

**Q:** ⭐ Bi-encoder vs cross-encoder? → **A:** Encode separately and compare (fast, pre-computable) vs encode together with cross-attention (accurate, slow) → retrieve then rerank.

**Q:** How is extractive QA framed? → **A:** Predict the start and end token positions of the answer span.

---

## 10.7 · Attention ⭐⭐

**Q:** ⭐ State the attention formula. → **A:** `softmax(QKᵀ/√dₖ)·V`. → [10.7](../weeks/10.7-attention.md)

**Q:** What are Q, K, V? → **A:** Learned projections: Query = what a token seeks, Key = how it's matched, Value = what it delivers.

**Q:** ⭐ Why divide by √dₖ? → **A:** Dot-product variance grows with dₖ; without scaling, softmax saturates and gradients vanish.

**Q:** What does QKᵀ compute? → **A:** An (n×n) matrix of every token's relevance to every other.

**Q:** ⭐ Why is attention better than an RNN for long range? → **A:** Direct O(1) access between any two tokens (no hop-by-hop decay) and full parallelism.

**Q:** What is a contextual embedding? → **A:** A token's representation that depends on its neighbors — self-attention gives "bank" different vectors in different sentences.

**Q:** Self- vs cross-attention? → **A:** Same sequence (context within) vs Q from one, K/V from another (attend across).

**Q:** ⭐ Why multi-head? → **A:** Different heads capture different relationship types (syntax, coreference) at ~the cost of one attention.

**Q:** ⭐ Attention's main cost? → **A:** O(n²) in sequence length — the central scaling problem of LLMs.

**Q:** Are attention weights faithful explanations? → **A:** No — suggestive, but manipulable and not reliable importance scores.

---

## 10.8 · Seq2seq

**Q:** What are the two halves of seq2seq? → **A:** Encoder (comprehends input) and decoder (autoregressively generates output). → [10.8](../weeks/10.8-seq2seq.md)

**Q:** ⭐ What does attention add to seq2seq? → **A:** The decoder attends over all encoder states each step instead of one fixed vector — killing the bottleneck.

**Q:** What is teacher forcing? → **A:** Feeding the decoder the ground-truth previous token during training (not its own prediction).

**Q:** ⭐ What is exposure bias? → **A:** Trained on perfect prefixes, but at inference runs on its own imperfect outputs.

**Q:** Why is generation slow? → **A:** Autoregressive — token t needs token t−1, so it can't be parallelized (unlike training).

**Q:** Greedy vs beam vs sampling? → **A:** Argmax (short-sighted) / keep k best (high-prob, bland) / random by distribution (diverse, LLM default).

**Q:** ⭐ Why sampling not beam for chatbots? → **A:** Beam maximizes probability → generic, repetitive text; open-ended generation wants diversity.

**Q:** ⭐ The Transformer's key move over seq2seq+attention? → **A:** Remove recurrence entirely; use only self-attention → full parallelism.

---

## 10.9 · Evaluation

**Q:** Which metrics carry over from Module 08? → **A:** Accuracy/precision/recall/F1 for classification and tagging. → [10.9](../weeks/10.9-evaluation.md)

**Q:** Macro vs micro F1? → **A:** Macro averages per-class (rare classes count equally); micro pools decisions. Prefer macro for imbalance.

**Q:** ⭐ What does BLEU measure? → **A:** N-gram precision vs reference(s) with a brevity penalty — for translation.

**Q:** ⭐ What does ROUGE measure? → **A:** N-gram recall vs reference — for summarization (coverage).

**Q:** ⭐ What is perplexity? → **A:** Exponentiated cross-entropy; the effective number of equally-likely choices per token; lower is better.

**Q:** Why is perplexity not comparable across tokenizers? → **A:** It depends on the vocabulary/units the probability is over.

**Q:** ⭐ Why do BLEU/ROUGE "lie"? → **A:** They measure surface n-gram overlap, not meaning.

**Q:** Ground truth for generation quality? → **A:** Human evaluation (or LLM-as-judge as a proxy).

---

## 10.10 · Data

**Q:** ⭐ The real bottleneck in NLP? → **A:** Label quality, not the model. → [10.10](../weeks/10.10-nlp-data.md)

**Q:** What is inter-annotator agreement and why Cohen's κ? → **A:** How consistently annotators label; κ corrects for chance agreement.

**Q:** ⭐ Why is IAA a ceiling on model accuracy? → **A:** If trained humans only agree X%, the rest is genuine ambiguity with no ground truth.

**Q:** What is near-duplicate leakage? → **A:** The same/similar document in train and test → score partly measures memorization; dedup before splitting.

**Q:** Why split by author or time? → **A:** Random splits let the model learn the author/period instead of the task.

**Q:** ⭐ Why is text a PII minefield? → **A:** PII hides in unstructured free-text fields no schema flags; redact at ingestion.

---

## 10.11 · PyTorch

**Q:** What does the NLP front end add to the 09.10 loop? → **A:** Numericalization, an embedding lookup, and variable-length handling (pad/pack/mask). The loop is unchanged. → [10.11](../weeks/10.11-nlp-with-pytorch.md)

**Q:** Why two special tokens? → **A:** `<pad>` fills short sequences; `<unk>` catches OOV words.

**Q:** ⭐ What does `padding_idx` do? → **A:** Pins the pad embedding to zeros and excludes it from gradients.

**Q:** ⭐ How do you stop padding from corrupting the model? → **A:** `pack_padded_sequence` (RNN), attention mask (attention), `ignore_index` (tagging loss).

**Q:** Is `nn.Embedding` a matmul? → **A:** No — a row-lookup by integer ID.

**Q:** ⭐ Which loop do NLP models use? → **A:** The exact 09.10 loop; text changes the front end, not the discipline.

---

## 10.12 · Hugging Face

**Q:** The three pillars? → **A:** `tokenizers` (subword), `transformers` (pretrained models), `datasets` (efficient loading). → [10.12](../weeks/10.12-modern-libraries.md)

**Q:** ⭐ What is subword tokenization? → **A:** BPE/WordPiece build a vocabulary of frequent character sequences, so any word decomposes into known pieces.

**Q:** ⭐ Why must the tokenizer match the model? → **A:** Token IDs index the pretrained embeddings; a mismatch → garbage output, no error.

**Q:** BERT vs GPT vs T5? → **A:** Encoder (understanding) / decoder (generation) / encoder–decoder (text-to-text).

**Q:** ⭐ What is fine-tuning? → **A:** Transfer learning for text — adapt a pretrained model with a new head on few labels.

**Q:** What's inside `AutoModel`? → **A:** The self-attention stack you built in 10.7 — pretrained and scaled.

---

## 10.13 · Production

**Q:** ⭐ The #1 NLP production bug? → **A:** Train/serve skew — preprocessing/tokenization differs between training and serving. → [10.13](../weeks/10.13-production.md)

**Q:** How do you prevent skew? → **A:** One shared preprocessing function, ship the exact tokenizer, CI test on token IDs.

**Q:** ⭐ What dominates NLP inference latency? → **A:** Tokenization, O(n²) attention, and autoregressive generation.

**Q:** ⭐ The biggest latency win? → **A:** A smaller (distilled) model, before fancier serving.

**Q:** The highest-leverage NLP optimization? → **A:** Pre-compute static-corpus embeddings offline; embed only the query at request time.

**Q:** ⭐ What's special about NLP drift? → **A:** The language itself changes (new slang/topics); monitor `<unk>`/vocabulary drift.

---

## 10.14 · Ethics & safety

**Q:** ⭐ Why is NLP bias structural? → **A:** Models learn meaning from human co-occurrence, so they encode human prejudice; you can only measure and reduce it. → [10.14](../weeks/10.14-ethics-safety.md)

**Q:** How do you measure bias? → **A:** WEAT (embedding associations), disaggregated metrics per group, counterfactual swaps.

**Q:** Why doesn't removing the protected attribute fix bias? → **A:** Proxies (name, style, school) reconstruct it — in text, everything correlates with demographics.

**Q:** ⭐ The two privacy risks? → **A:** PII in the corpus, and memorization → extraction (models regurgitate rare training sequences).

**Q:** The only robust privacy defense? → **A:** Don't train on PII — redact at ingestion; dedup reduces memorization.

**Q:** ⭐ Why is hallucination structural? → **A:** Generation optimizes *probable* text, not *true* — a fluent lie is high-probability.

**Q:** How do you fight hallucination? → **A:** RAG grounding, required citations, calibration/abstention, human review.

**Q:** What documents make NLP risk accountable? → **A:** Datasheets (data) and model cards (model).

---

## 🎯 The ten sentences (recall all ten cold)

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

[⬆ Module 10](../README.md) · [📖 Lessons](../weeks/README.md) · [📄 Cheat sheet](../cheat-sheets/nlp-cheatsheet.md) · [📝 Quiz](../quizzes/quiz-01.md)
