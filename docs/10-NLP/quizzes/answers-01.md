# ✅ Module 10 · NLP — Quiz 01 Answers

[🏠 Module 10](../README.md) · [📝 Back to quiz](quiz-01.md)

> Each answer gives the **key point**, the **why**, and a **lesson link**. Grade on the reasoning.

---

## Part A · Representation

**1.** **Turning text into vectors without losing meaning.** It's hard because language is **ambiguous** (one string, many meanings), **context-dependent** (a word's meaning shifts with its neighbors), **compositional** (infinitely many valid sentences), and **long-tailed** (you always meet unseen words). A model only ever sees the vectors you produce, so every result is bounded by that representation. → [10.1](../weeks/10.1-introduction-to-nlp.md)

**2.** **The distributional hypothesis:** a word's meaning is approximated by the distribution of contexts it appears in ("know a word by the company it keeps"). It's foundational because it converts an unanswerable question ("what does 'dog' mean?") into a countable one ("what co-occurs with 'dog'?"). TF-IDF, Word2Vec, and attention are all different ways of cashing in co-occurrence statistics. → [10.1](../weeks/10.1-introduction-to-nlp.md)

**3.** "dog bites man" / "man bites dog" — identical BoW, opposite meaning. It exposes (1) **word-order blindness** (BoW is a multiset) and, more subtly, (2) that BoW captures no relationships between words. → [10.3](../weeks/10.3-text-representation.md)

**4.** TF-IDF = tf(t,d) × idf(t), where tf = count of *t* in *d* (often length-normalized) and idf = **log(N / df(t))**. The **log is essential**: without it, idf = N/df, so a word in 1 of 1,000,000 documents scores ~1,000,000 and swamps the whole vector. Document frequency spans many orders of magnitude; the log compresses that range so weights are comparable (and encodes diminishing returns). → [10.3](../weeks/10.3-text-representation.md)

**5.** IDF and the vocabulary are **learned parameters**; computing IDF over train+test leaks information about which words are rare *in the test set* into your features — a **preprocessing leak** ([08.13](../../08-Machine-Learning/weeks/08.13-cross-validation.md)). Fit on train, transform test. → [10.3](../weeks/10.3-text-representation.md)

**6.** Every distinct word is on its own orthogonal axis, so any two different words have a dot product of 0 — the representation literally **cannot encode that "cat" and "feline" are related**. Embeddings add **similarity**: dense vectors arranged so related words are geometrically close (direction = meaning). → [10.3](../weeks/10.3-text-representation.md) · [10.4](../weeks/10.4-word-embeddings.md)

**7.** The fake task: predict a word from its context (CBOW) or context from a word (skip-gram). You **keep the weight matrix** (each word's row is its embedding) and **throw away the predictions** — nobody cares about them. It encodes meaning because words appearing in similar contexts get pushed to similar vectors (the distributional hypothesis, optimized). → [10.4](../weeks/10.4-word-embeddings.md)

**8.** It replaces the intractable **V-way softmax** (predict which of a million words is the context — a million output updates per step) with a **binary "real vs random pair"** task, updating only **1 + k vectors** per step. That's the difference between six updates and a million, which is what made Word2Vec trainable on billions of words. → [10.4](../weeks/10.4-word-embeddings.md)

**9.** Meaning is encoded as **direction**, and cosine measures the angle between vectors while ignoring magnitude (which roughly tracks word frequency). Euclidean distance would let frequency contaminate similarity; cosine normalizes it out. → [10.4](../weeks/10.4-word-embeddings.md)

**10.** Static embeddings give each word **exactly one vector, regardless of context** — so "bank" is a single incoherent blend of riverbank and financial bank. **Self-attention** ([10.7](../weeks/10.7-attention.md)) resolves it by producing **contextual** embeddings that depend on the sentence. → [10.4](../weeks/10.4-word-embeddings.md)

**11.** Bias comes from the **distributional hypothesis doing its job**: embeddings learn meaning from human co-occurrence, so they faithfully encode human prejudice ("he" near "engineer," "she" near "nurse"). You can't clean it away because it's diffuse across billions of co-occurrences — it's structural, not a few bad rows. → [10.4](../weeks/10.4-word-embeddings.md) · [10.14](../weeks/10.14-ethics-safety.md)

---

## Part B · Sequence & attention

**12.** Word order changes meaning ("dog bites man" ≠ "man bites dog"; "not good" ≠ "good, not bad"). BoW represents both as the same multiset and *must* give them the same vector. A sequence model reads in order, so its **hidden state already contains "not" when it reaches "good,"** letting it flip the sentiment. → [10.5](../weeks/10.5-sequence-models.md)

**13.** Backprop-through-time multiplies the recurrent weight at every step, so the gradient to far-back words scales like **λⁿ** and dies after ~10 steps. Linguistically this breaks **long-range subject-verb agreement** ("the keys… are") and **coreference** ("the trophy… it…" across a long clause). → [10.5](../weeks/10.5-sequence-models.md)

**14.** The LSTM adds a **cell state** — a near-linear "conveyor belt" updated mostly by (gated) **addition**, not repeated multiplication — so the gradient can flow across hundreds of steps without vanishing. It's the same mechanism as a **residual connection**: an additive gradient highway. → [10.5](../weeks/10.5-sequence-models.md)

**15.** Appropriate for **understanding** tasks (NER, POS, classification) where the whole sentence is available and both-side context helps. **Forbidden** for **generation** (you'd peek at the token you're predicting) and **streaming** (the future isn't available yet). → [10.5](../weeks/10.5-sequence-models.md)

**16.** The encoder must compress the **entire input into one fixed-size vector**, and the decoder reconstructs everything from it alone. A single ~512-dim vector can't hold a 50-word sentence's detail, so quality collapses as input length grows — the bottleneck attention removes. → [10.5](../weeks/10.5-sequence-models.md)

**17.** **`Attention(Q,K,V) = softmax(QKᵀ/√dₖ)·V`.** **Q** (query) = what a token is looking for; **K** (key) = how a token should be matched/found; **V** (value) = the content a token delivers. Key and Value are separate so a token can be *found* by one property and *contribute* something different — matched-by ≠ delivered-content. → [10.7](../weeks/10.7-attention.md)

**18.** The dot product of two dₖ-dimensional vectors has variance ∝ dₖ, so for large dₖ the scores swing wide and **softmax saturates** — nearly all weight on one token, gradients ≈ 0 everywhere. Dividing by √dₖ rescales scores to unit variance, keeping softmax responsive and gradients alive. Without it, deep attention stacks don't train. → [10.7](../weeks/10.7-attention.md)

**19.** A contextual embedding is a token's vector that **depends on its neighbors**. Self-attention produces one by having each token attend to the others and take a weighted blend of their values — so "bank" in "river bank" attends to "river" and shifts toward the geographic sense. Word2Vec couldn't: it assigns one fixed vector per word, context-free. → [10.7](../weeks/10.7-attention.md)

**20.** Multi-head runs *h* attention operations in parallel, each with its own projections, then concatenates and projects. Different heads capture **different relationship types** (syntax, coreference, adjacency) that one head would blur together. Each head uses dₖ = d_model/h, so *h* heads cost ~the same as one full attention — diversity for free. → [10.7](../weeks/10.7-attention.md)

**21.** **(a) Path length:** RNN = O(n) hops between two tokens (signal decays); attention = **O(1)**, direct. **(b) Parallelizability:** RNN is sequential (step t needs t−1); attention is **one big matmul**, fully parallel. It pays with **O(n²)** compute/memory in sequence length. → [10.7](../weeks/10.7-attention.md)

**22.** Teacher forcing feeds the decoder the **ground-truth previous token** during training (not its own prediction), giving clean context and fast, parallelizable training. The problem it creates is **exposure bias**: the model is trained only on perfect prefixes but at inference runs on its own imperfect outputs — a distribution it never saw — so early errors can cascade. → [10.8](../weeks/10.8-seq2seq.md)

**23.** Beam search maximizes total sequence probability, which for open-ended text produces **bland, generic, repetitive** output ("I don't know. I don't know."). Open-ended generation wants **diversity**, so LLMs use **sampling** (temperature/top-k/top-p). Beam is right for translation (where there's a correct answer). → [10.8](../weeks/10.8-seq2seq.md)

**24.** **RNN seq2seq** (2014): the bottleneck. **+ attention** (2015): decoder attends over all encoder states → bottleneck gone, but the RNN remains, so it's still sequential. **Transformer** (2017): **removes recurrence entirely**, using only self-attention → full parallelism in encoding and training. Each step fixed the prior's specific failure. → [10.8](../weeks/10.8-seq2seq.md)

---

## Part C · Tasks, evaluation, data

**25.** **Seq→label** (sentiment; pool→softmax; macro-F1). **Seq→per-token** (NER; per-token+CRF; entity-F1). **Seq→seq** (translation; decoder; BLEU). **Pair→score** (retrieval; compare encodings; recall@k). All share the embed→encode front end; only head/loss/metric change. → [10.6](../weeks/10.6-nlp-tasks.md)

**26.** Independent per-token softmax can emit **illegal tag sequences** (e.g., `O I-PER` — an "inside-person" with no "begin"). A CRF models tag-to-tag transitions and finds the best **globally consistent** sequence, forbidding illegal transitions — because in tagging, labels constrain each other. → [10.6](../weeks/10.6-nlp-tasks.md)

**27.** A **bi-encoder** encodes each text separately and compares vectors — fast, and you can **pre-compute** all document embeddings (essential to search millions of docs). A **cross-encoder** feeds both texts together with cross-attention — more accurate but must run per pair (too slow to scan a corpus). Production **retrieves** with a bi-encoder, then **reranks** the top few with a cross-encoder. → [10.6](../weeks/10.6-nlp-tasks.md)

**28.** **BLEU = n-gram precision** vs reference(s) (of what I produced, how much matches) with a brevity penalty — for translation, where you shouldn't add junk. **ROUGE = n-gram recall** (of the reference, how much I covered) — for summarization, where the concern is missing key content. The orientation matches the task's failure mode. → [10.9](../weeks/10.9-evaluation.md)

**29.** **Perplexity = exp(cross-entropy)** — the exponentiated average negative log-likelihood of the true tokens. Intuitively it's the **effective number of equally-likely choices per token**; PPL = 20 means the model is as uncertain as if choosing among 20 options each step. It's your training loss on a readable scale; lower is better. → [10.9](../weeks/10.9-evaluation.md)

**30.** *Good translation, low BLEU:* "The film was excellent" vs reference "The movie was great" — correct, near-zero n-gram overlap. *Bad translation, high BLEU:* a scrambled version reusing the reference's words in wrong order can share many n-grams while being ungrammatical/wrong. BLEU measures surface overlap, not meaning. → [10.9](../weeks/10.9-evaluation.md)

**31.** IAA (e.g., Cohen's κ) measures how consistently annotators assign the same label, corrected for chance. It **bounds achievable accuracy** because if trained humans only agree X% of the time, the remaining disagreement is genuine ambiguity with no ground truth to learn. **Reaction to 90% acc on a κ=0.65 task:** red flag — you're likely overfitting label noise or there's hidden leakage; a model can't be meaningfully more consistent than the labels. → [10.10](../weeks/10.10-nlp-data.md)

**32.** (1) **Near-duplicate documents** across train/test (scraped reposts) → dedup before splitting. (2) **Author/source leakage** (same writer in both splits → learns the author, not the task) → split by author. (3) **Temporal leakage** (future text in training) → time-based split. (Also: fitting vocab/TF-IDF on all data.) → [10.10](../weeks/10.10-nlp-data.md)

---

## Part D · Engineering & ethics

**33.** It adds a **front end**: numericalization (strings→integer IDs via a vocab), an **embedding lookup**, and **variable-length handling** (pad/pack/mask). The training loop itself — `zero_grad → forward → loss → backward → step`, `train()`/`eval()`/`no_grad()` — is [09.10](../../09-Deep-Learning/weeks/09.10-training-loop.md) **unchanged**. → [10.11](../weeks/10.11-nlp-with-pytorch.md)

**34.** Building vocab on train+test **leaks which tokens exist in the test set** (a preprocessing leak). `<pad>` fills short sequences to a rectangular batch; `<unk>` catches out-of-vocabulary words — and the **long tail guarantees** you meet unseen words at inference, so without `<unk>` the code crashes on the first one. → [10.11](../weeks/10.11-nlp-with-pytorch.md)

**35.** **RNN:** `pack_padded_sequence` so the LSTM never processes pad tokens. **Attention:** an attention mask setting pad positions' scores to −∞ before softmax, so nothing attends to padding. **Tagging loss:** `ignore_index=<pad>` so pad positions don't contribute to the loss. Skip any and the model learns from meaningless padding. → [10.11](../weeks/10.11-nlp-with-pytorch.md)

**36.** Subword tokenization (BPE/WordPiece) builds a vocabulary of **frequent character sequences**, so any word — including unseen ones — decomposes into known pieces (worst case, individual characters). It solves the **out-of-vocabulary / long-tail** problem. You must use the model's **exact** tokenizer because token IDs index the pretrained embeddings; a mismatched tokenizer produces wrong IDs → garbage output, with **no error**. → [10.12](../weeks/10.12-modern-libraries.md)

**37.** Fine-tuning adapts a **pretrained** model (which already encodes grammar, meaning, and world knowledge from massive self-supervised pretraining) by adding/replacing a small task head and training on your labels. It beats from-scratch with limited labels because you're not re-learning language — it's **transfer learning** ([09.11](../../09-Deep-Learning/weeks/09.11-cnns.md)): a fine-tuned model can beat a from-scratch model with 100× fewer labeled examples. → [10.12](../weeks/10.12-modern-libraries.md)

**38.** Train/serve skew = the text is **preprocessed differently at inference than in training** (different tokenizer version, a stray lowercase, a normalization mismatch), so the model sees a distribution it never trained on. It's common because text preprocessing has many steps to get wrong, and it fails **silently** (no error, just worse accuracy). Prevent it with **one shared preprocessing function**, **shipping the exact tokenizer with the model**, and a **CI test asserting identical token IDs** across the training and serving paths. → [10.13](../weeks/10.13-production.md)

**39.** The biggest latency win is a **smaller (distilled) model** — ~2× faster for ~3% accuracy — because model size dominates cost more than serving infrastructure does. In **semantic search**, the highest-leverage optimization is **pre-computing the static-corpus embeddings offline** and storing them in a vector index, so at query time you embed only the query and do a nearest-neighbor lookup — never re-embed the corpus per request. → [10.13](../weeks/10.13-production.md)

**40.** Hallucination is structural because a language model is trained to produce **probable** text, not **true** text — it has no notion of truth, only of what tokens plausibly follow, so a confident, fluent falsehood *is* high-probability output. Mitigations: **RAG grounding** (retrieve real documents so the model quotes sources), **required citations + verification**, **confidence calibration/abstention** ("I don't know"), and human review for high-stakes output. → [10.14](../weeks/10.14-ethics-safety.md)

---

## 🎁 Bonus answers

**B1.** **`torch.allclose(numpy_attention_output, torch_attention_output)`** (returning `True`) — and, if you also check gradients, that the backward passes match. Building it by hand is the point because it makes `nn.MultiheadAttention` — and by extension every Transformer and LLM — **transparent**: when you later call a library's attention, you know it's the exact `softmax(QKᵀ/√dₖ)·V` you wrote, not magic. That is the whole thesis of the module. → [10.7](../weeks/10.7-attention.md)

**B2.** (1) **Train/serve skew** — the serving preprocessing/tokenizer differs from training, silently corrupting inputs ([10.13](../weeks/10.13-production.md)). (2) **Vocabulary/language drift** — the production text contains new slang/topics driving up the `<unk>` rate, so the model sees words it can't represent ([10.13](../weeks/10.13-production.md)). Both are one-liners; both look fine in offline eval on the old data. → [10.13](../weeks/10.13-production.md)

**B3.** A model is a **lossy, queryable compression of its training data**, not an abstraction that discards it. Two attacks make "just the model" unsafe: **membership inference** (determine whether a specific person's text was in training) and **extraction** (prompt the model to regurgitate memorized verbatim sequences — real PII has been recovered this way). So a model trained on sensitive text is itself a **sensitive artifact**; the only robust defense is not training on PII (redact at ingestion, dedup). → [10.14](../weeks/10.14-ethics-safety.md)

---

**Scoring:** 36–40 outstanding · 32–35 solid (module complete) · 26–31 review the linked lessons · <26 re-read **10.4, 10.7, and 10.8** — the load-bearing three.

[📝 Back to quiz](quiz-01.md) · [🧠 Flashcards](../flashcards/deck.md) · [📖 Lessons](../weeks/README.md)
