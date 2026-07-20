# ✅ Module 11 · LLMs & Transformers — Quiz 01 Answers

[🏠 Module 11](../README.md) · [📝 Back to quiz](quiz-01.md)

> Each answer gives the **key point**, the **why**, and a **lesson link**. Grade on the reasoning.

---

## Part A · Architecture

**1.** A language model is a **probability distribution over token sequences**. The **chain rule** factors the joint probability of a sequence exactly into a product of next-token conditionals: `P(x₁…xₙ) = ∏ P(xₜ | x_<t)`. So modeling one thing — the next token given the past — lets you model any sequence, which is why LLMs are next-token predictors. → [11.1](../weeks/11.1-what-is-a-language-model.md)

**2.** **Causal (autoregressive):** predicts the next token left-to-right, seeing only the past — can generate. **Masked:** predicts randomly masked tokens using both-sided context — great at understanding, can't generate. ChatGPT is causal because generation requires predicting the *next* token from only the past; a bidirectional model has no notion of "next." → [11.1](../weeks/11.1-what-is-a-language-model.md)

**3.** The objective trains the model to produce **probable** text, not **true** text. It has no notion of truth — only of what tokens plausibly follow — so a confident, fluent falsehood *is* high-probability output. Hallucination is a property of the objective, not a fixable bug. → [11.1](../weeks/11.1-what-is-a-language-model.md)

**4.** BPE starts from characters/bytes, counts adjacent pairs, **merges the most frequent pair** into a new token, and repeats to a target vocab size, saving the merge rules. **Byte-level BPE** uses the 256 bytes as the base vocabulary, so *any* input (any language, emoji, code, corrupted bytes) tokenizes into known pieces — **zero unknown tokens, ever**. → [11.2](../weeks/11.2-tokenization.md)

**5.** **Token efficiency** = how many tokens a text costs — driving cost (per-token billing), context budget, and latency. It's **unfair across languages** because the vocabulary was trained mostly on English, so non-English scripts fragment into many more tokens (5–10×), meaning non-English users pay more and get less context. LLMs **can't count letters** because they see opaque token IDs, not individual characters (e.g., "strawberry" may be one token). → [11.2](../weeks/11.2-tokenization.md)

**6.** **Self-attention is permutation-invariant** — it's a weighted sum over all positions with no inherent order, so "dog bites man" and "man bites dog" have identical token *sets* and would look the same. Position must be **explicitly injected**. This is the tax for dropping recurrence (an RNN read tokens in order; attention processes them all at once). → [11.3](../weeks/11.3-embeddings-positional.md)

**7.** **Learned:** trainable per-position table — simple, but can't extrapolate past the trained length. **Sinusoidal:** fixed sines/cosines — parameter-free, relative-friendly. **RoPE:** rotates Q and K by an angle ∝ position so the attention score depends on **relative distance** — parameter-free and extrapolates. Modern LLMs use RoPE because relative position is what matters linguistically, and scaling RoPE (position interpolation/NTK) is how long-context models are made. → [11.3](../weeks/11.3-embeddings-positional.md)

**8.** **`Attention(Q,K,V) = softmax(QKᵀ/√dₖ)·V`.** Q = what a token seeks, K = how a token is matched, V = the content it delivers (all learned projections; K and V separate so matched-by ≠ delivered-content). The **√dₖ** scaling rescales the dot-product scores (whose variance grows with dₖ) back to unit variance, keeping softmax from saturating — without it, gradients vanish and deep attention stacks don't train. → [11.4](../weeks/11.4-attention.md)

**9.** **MHA:** h query heads, h key/value heads (biggest KV cache). **MQA:** h query heads, 1 K/V head (smallest cache, slight quality drop). **GQA:** h query heads, g<h K/V heads (groups share K/V — medium cache, ~MHA quality). Large models use **GQA** because it cuts the KV cache (the long-context serving bottleneck) several-fold with negligible quality loss. → [11.4](../weeks/11.4-attention.md)

**10.** **Multi-head attention** (tokens exchange information — the only cross-token step) and a **position-wise feed-forward network** (each token processed independently). Most of the model's **factual knowledge lives in the FFN weights** — the wide 4×d_model hidden layer acts like a key-value memory; attention decides *what to combine*, the FFN decides *what to do with it*. → [11.5](../weeks/11.5-transformer-architecture.md)

**11.** The **residual stream** is a d_model-wide highway running the network's full depth; each sublayer *adds* its output to it (never overwrites). Residual connections are essential because they form a **gradient highway** that lets deep (80+ layer) networks train (the λⁿ/vanishing-gradient fix). **Pre-LN** (norm before the sublayer) keeps the residual path clean and trains deep models stably; **Post-LN** (norm after the residual add) is the original but needs careful LR warmup. → [11.5](../weeks/11.5-transformer-architecture.md)

**12.** A **causal mask** sets future positions' attention scores to −∞ before softmax, so each token attends only to itself and earlier tokens. This makes training efficient because a **single forward pass computes a next-token loss at every position simultaneously** — position *t* predicts token *t+1*, and the mask prevents any position from seeing its own answer, so there's no leakage. n training signals from one pass. → [11.6](../weeks/11.6-decoder-only.md)

**13.** **Generation is a universal interface** — any task (translation, summarization, Q&A, classification, reasoning) can be framed as "continue this text," so one decoder-only model does everything with the right prompt. It also scales simply and exhibits strong in-context learning. You'd still use an **encoder-only** model for high-volume *understanding* tasks (classification, retrieval embeddings) where it's cheaper, faster, and often more accurate than a giant decoder. → [11.6](../weeks/11.6-decoder-only.md) · [11.7](../weeks/11.7-encoder-decoder-types.md)

**14.** Token IDs → token+positional embeddings → N causal Transformer blocks (each: norm → multi-head attention → +residual; norm → FFN → +residual) → final norm → output projection to vocab logits → cross-entropy against the next token. **First debugging step: overfit one batch to ~0 loss.** If a correct model can't memorize one batch, the bug is in the model or loop (mask, shapes, weight tying), not the data — it isolates the problem fastest. → [11.8](../weeks/11.8-build-mini-transformer.md)

---

## Part B · Training & Adaptation

**15.** Next-token prediction (cross-entropy). It's **self-supervised** — the label is simply the next token, requiring no human annotation — so you can train on *all* the text on the internet. This is the key enabler: without free labels, you could never assemble trillions of training examples. → [11.9](../weeks/11.9-pretraining.md)

**16.** Collection (web/books/code) → cleaning (strip boilerplate, fix encoding) → **deduplication** → filtering (quality/toxicity/PII) → tokenization → sharding (for streaming). Deduplication is essential because it improves model quality, reduces **memorization** of repeated text (a privacy risk), saves compute, and prevents **benchmark contamination** (test data leaking into training). → [11.9](../weeks/11.9-pretraining.md)

**17.** The full training footprint is weights + gradients + Adam's two moment estimates + activations — ~16 bytes/parameter in mixed precision. A 70B model needs ~1TB+ of aggregate GPU memory just for training state, far more than any single GPU holds, forcing you to shard across dozens of GPUs (tensor/pipeline/ZeRO). Compute is parallelizable; the memory wall is what forces distributed training. → [11.9](../weeks/11.9-pretraining.md)

**18.** A **scaling law**: test loss falls as a **power law** in parameters, data, and compute — a straight line on log-log axes, making quality predictable. **Chinchilla** showed model size and training data should scale roughly **equally** (~20 tokens/param), and that most large models (e.g., GPT-3 at ~1.7 tokens/param) were badly **under-trained**. The prior (Kaplan) view held that data was secondary and drove a race to ever-bigger, under-fed models — Chinchilla (70B/1.4T) beat Gopher (280B/300B) at equal compute. → [11.10](../weeks/11.10-scaling-laws.md)

**19.** Because **inference cost dominates deployment** — every query, forever. Chinchilla minimizes *training* compute, but a smaller model that's cheaper to serve is worth "over-spending" on training data. A 7B model trained on 2T tokens (~285/param) runs on modest hardware and serves millions of queries cheaply, beating a Chinchilla-optimal larger model on total (training + lifetime inference) cost. → [11.10](../weeks/11.10-scaling-laws.md)

**20.** SFT teaches **behavior and format** (how to follow instructions and be helpful), **not new knowledge** — the base model already learned facts/grammar/reasoning in pretraining. So a small, high-quality set works (LIMA: ~1,000 examples): you're **eliciting** a behavior the model can already perform, not teaching from scratch. → [11.11](../weeks/11.11-fine-tuning.md)

**21.** **Loss masking** sets the prompt-token labels to `ignore_index` (-100) so the loss is computed **only on the response tokens**. Without it, the model wastes capacity learning to *generate the user's prompt* (useless) and can misbehave — sometimes continuing your question instead of answering it. Only the assistant's tokens should contribute to the loss. → [11.11](../weeks/11.11-fine-tuning.md)

**22.** **Catastrophic forgetting** is losing general ability by over-fine-tuning on a narrow dataset. Mitigate with a **low learning rate, few epochs (1–3), diverse data**, or PEFT (frozen base). Use **RAG** instead of fine-tuning to **add facts** — fine-tuning teaches behavior, not reliable factual recall, and RAG grounds the model in retrieved, updatable knowledge. → [11.11](../weeks/11.11-fine-tuning.md)

**23.** **LoRA** freezes the pretrained weight W and trains a **low-rank update** ΔW = B·A (rank r ≪ d), so you train ~0.1% of the parameters. The low-rank assumption is reasonable because fine-tuning makes a **small, structured change** whose intrinsic rank is low (the SVD/[06.3](../../06-Mathematics/weeks/06.3-linear-algebra-2.md) intuition). It solves the **Adam optimizer-state memory** problem: Adam stores 2 extra copies per *trained* parameter, so training only 0.1% of params pays that tax on only 0.1%. → [11.12](../weeks/11.12-peft-lora.md)

**24.** **QLoRA** quantizes the frozen base model to **4-bit** (nearly free, since it's not updated) and trains LoRA adapters in higher precision on top. The 4-bit base cuts model-holding memory ~4×, and LoRA cuts training memory, together fitting a 65B fine-tune on a single 48GB GPU at ~full-precision quality. Keeping **adapters separate** (each ~10MB) lets one frozen base serve many hot-swappable fine-tunes. → [11.12](../weeks/11.12-peft-lora.md)

**25.** (1) Collect human **preference comparisons** (prompt + two responses, pick the better). (2) Train a **reward model** to predict a scalar such that chosen responses score higher — a learned proxy for human judgment. (3) **RL-fine-tune (PPO)** the LLM to maximize the reward model's score, with a **KL penalty** anchoring it to the SFT model (or it drifts into degenerate high-scoring gibberish — reward hacking). → [11.13](../weeks/11.13-alignment.md)

**26.** **Reward hacking:** the policy exploits flaws in the imperfect reward model to score high without being genuinely better — e.g., becoming **sycophantic** or **verbose** because the reward model was fooled by those features. It's **Goodhart's law** — the reward model is a *proxy* for human values, and optimizing a proxy hard makes it cease to measure what you wanted. → [11.13](../weeks/11.13-alignment.md)

**27.** **DPO (Direct Preference Optimization)** aligns to preferences with a **single classification-style loss** (increase the likelihood of chosen responses, decrease rejected, relative to a frozen reference) — **no separate reward model and no RL loop**. It's replaced RLHF for open-source because it's far simpler, more stable, and cheaper (no unstable PPO), and combines easily with LoRA — turning alignment into something close to ordinary fine-tuning. → [11.13](../weeks/11.13-alignment.md)

---

## Part C · Inference & Serving

**28.** The **model** produces a probability distribution over the next token (fixed after training); the **decoding strategy** picks a token from that distribution (a runtime choice). The same model can be a precise fact-answerer or a creative writer depending only on decoding settings — it's the cheapest lever on behavior. → [11.14](../weeks/11.14-inference-decoding.md)

**29.** **Temperature** reshapes the distribution before sampling (`softmax(logits/T)`): low T sharpens toward the top token (focused/deterministic), high T flattens it (diverse/creative). Choose **low for facts/code/extraction** (you want the confident token), **moderate (~0.7) for chat**, **high (~1.0+) for creativity**. **Safety:** higher temperature samples lower-probability tokens, increasing hallucination and unsafe output — use low temperature where correctness matters. → [11.14](../weeks/11.14-inference-decoding.md)

**30.** **Top-k** keeps a fixed number of the most likely tokens; **top-p (nucleus)** keeps the smallest set whose cumulative probability ≥ p. Top-p is preferred because it's **adaptive**: a tiny nucleus when the model is confident (near-greedy), a large one when uncertain (more diverse) — matching the truncation to the model's actual confidence. → [11.14](../weeks/11.14-inference-decoding.md)

**31.** The **KV cache** stores the keys and values of all past tokens so each new token attends to cached K/V instead of recomputing them — turning generation from O(n²) (re-running attention over the whole prefix each step) to O(n). Caching is valid because the **causal mask** means past tokens' representations don't depend on future tokens — the past is frozen, so its K/V never change. → [11.15](../weeks/11.15-kv-cache.md)

**32.** **Prefill:** the prompt is known, so all its tokens are processed in **one parallel forward pass** (filling the cache) — lots of matmul FLOPs, GPU well-utilized → **compute-bound**. **Decode:** generate one token at a time; each step does tiny compute but must read all weights + the whole cache from memory → **memory-bandwidth-bound**, GPU starved for data. → [11.15](../weeks/11.15-kv-cache.md)

**33.** The **weights are fixed** (e.g., 140GB for a 70B fp16 model), but the **KV cache grows with batch × context** and can reach tens of GB for many concurrent long-context requests — so you run out of *cache* memory before *weight* memory, capping concurrency. **GQA** reduces the number of K/V heads, shrinking the cache several-fold and letting more requests fit. → [11.15](../weeks/11.15-kv-cache.md)

**34.** Because **decode is memory-bound** — the dominant cost is reading the model weights from memory each step. **Quantization** (int8/int4) cuts the bytes per weight, directly cutting that dominant cost (~4× faster decode) *and* freeing 4× more room for the KV cache (more concurrent requests) — all for ~1% quality loss with modern methods (GPTQ/AWQ). Biggest, cheapest win; do it first. → [11.16](../weeks/11.16-inference-optimization.md)

**35.** **Continuous batching** adds and removes requests from the running batch at the token level, so the GPU never idles waiting for the slowest request to finish. It works so well because decode is **memory-bound**: the expensive weight read is **shared** across every request in the batch, so packing more requests in costs almost no extra memory traffic — near-linear throughput gains until KV-cache memory runs out. → [11.16](../weeks/11.16-inference-optimization.md)

**36.** A small **draft model** proposes several tokens ahead; the large model **verifies them all in one parallel forward pass** (cheap, like prefill), accepting the correct prefix. It doesn't hurt quality because the **large model still decides** — the output distribution is provably identical to normal decoding. It exploits decode's spare compute (memory-bound → idle compute) to generate multiple tokens per big-model pass. → [11.16](../weeks/11.16-inference-optimization.md)

---

## Part D · Evaluation, Safety, Production

**37.** Open-ended output (many valid answers, no single reference), general-purpose (one model, thousands of tasks), emergent capabilities (benchmarks saturate), contamination, subjectivity, and gaming all make it hard. The **evaluation ladder**: **perplexity** (cheap, measures prediction not usefulness) → **task benchmarks** (MMLU/HumanEval/GSM8K — broader but gameable/contaminatable) → **human/LLM-as-judge** (meaningful but slow/subjective/biased). No single number captures "good." → [11.17](../weeks/11.17-evaluation.md)

**38.** **Benchmark contamination** is test questions appearing in the training data (web-scraped corpora contain most public benchmarks). The model may have **memorized** the answers, inflating scores without real capability — so a model can top MMLU by having seen it, not by reasoning. Defense: dedup against benchmarks, and keep private held-out evals. → [11.17](../weeks/11.17-evaluation.md)

**39.** **Position bias** (favors the first response shown), **verbosity bias** (prefers longer answers), **self-preference** (rates its own family higher), and being **fooled by confident-but-wrong** answers. Mitigate by randomizing positions, controlling for length, and using multiple judges — and never treat it as ground truth for high-stakes decisions (it's a proxy, subject to Goodhart). → [11.17](../weeks/11.17-evaluation.md)

**40.** Because it stems from the **architecture**: instructions and data share one channel — the model can't distinguish trusted instructions from attacker-controlled content in its context. An attacker who controls *any* text the model reads (a message, a web page, a document) can try to issue instructions. It **can't be fully fixed** because it's a consequence of how the model works; mitigations (delimiting, screening, instructions) reduce but don't eliminate it. → [11.18](../weeks/11.18-safety.md)

**41.** **Least privilege — assume the model will be hijacked and limit what it can *do*.** You can't make the model un-hijackable, so make a hijack *harmless*: if an agent can read but not send email, injection can't exfiltrate; if tools require human confirmation, injection can't act unilaterally. It's the security principle of containing blast radius, and it's more reliable than perfecting the model's refusals. → [11.18](../weeks/11.18-safety.md)

**42.** **Hosted API:** rent frontier models, zero ops, fast start — but data leaves, pay-per-token (expensive at scale), limited customization, lock-in. **Self-hosted open:** full privacy/customization/cost-at-scale — but you own serving + ops and often trail frontier. **Managed open hosting:** open models via API (middle ground). The **two decisive factors** are **privacy** (can data leave?) and **cost-at-scale** (the cost curves cross — API cheaper at low volume, self-host cheaper at high steady volume). → [11.19](../weeks/11.19-apis-vs-open-models.md)

**43.** A **cascade** routes easy queries to a cheap small model and escalates only hard ones to an expensive frontier model. It's cost-effective because most queries are easy — you capture most of the cost savings (cheap model handles the bulk) with most of the capability (frontier model handles the hard tail). → [11.19](../weeks/11.19-apis-vs-open-models.md)

**44.** User → **gateway** (auth, rate limiting) → **input guardrails** → **cache** check → **prompt management + RAG** → **model** (with fallback) → **output guardrails** → cache write → response, with **monitoring** across all. **Caching** is critical because generation is slow and per-token-billed, so a cache hit is a free, instant response; **semantic caching** (return a cached answer for a *similar* query via embeddings) serves much of FAQ-like traffic, often cutting cost/latency more than any model optimization. → [11.20](../weeks/11.20-production-architecture.md)

**45.** Mostly **inherited** — it's the [08.17](../../08-Machine-Learning/weeks/08.17-production-ml.md)/[10.13](../../10-NLP/weeks/10.13-production.md) MLOps discipline unchanged: versioning, monitoring, canaries, retraining/regression gates, PII-safe logging, rate limiting. The **LLM-specific additions** are prompt management (version prompts like code), token-cost tracking/budgeting, semantic + prefix caching, and guardrails against injection. The recurring lesson: the fancy model didn't change the discipline. → [11.20](../weeks/11.20-production-architecture.md)

---

## 🎁 Bonus answers

**B1.** **Pretraining:** the training footprint (weights + gradients + Adam states + activations) exceeds a single GPU, forcing distributed sharding — *memory*, not compute, is the wall ([11.9](../weeks/11.9-pretraining.md)). **LoRA:** the Adam optimizer state (3× per trained param) is what OOMs full fine-tuning, so training only 0.1% of params (low-rank) collapses the memory ([11.12](../weeks/11.12-peft-lora.md)). **KV cache:** it grows with batch × context and often limits concurrency more than the weights do ([11.15](../weeks/11.15-kv-cache.md)). **Quantization:** decode is memory-*bandwidth*-bound, so cutting bytes-per-weight is the biggest speedup ([11.16](../weeks/11.16-inference-optimization.md)). Across the whole lifecycle — train, adapt, serve — **memory is the binding constraint**, and the field's key techniques are all memory-management moves.

**B2.** It proves the **mechanism**: an LLM is next-token prediction computed by stacked self-attention blocks trained with cross-entropy — coherence, style imitation, and pattern-continuation all emerge from that mechanism, visible in miniature. It does **not** prove you have the *capabilities* of a 175B model — scale unlocks emergent abilities (reasoning, in-context learning) your tiny model lacks. The point: **scale changes the magnitude of capability, not the mechanism** — the 175B model is your mini-GPT, wider and deeper, trained on more. → [11.8](../weeks/11.8-build-mini-transformer.md), [11.10](../weeks/11.10-scaling-laws.md)

**B3.** "Instructions and data share one channel" means **everything is just tokens to continue** ([11.1](../weeks/11.1-what-is-a-language-model.md)). This is the **superpower** behind decoder-only generality: because any task is expressible as "continue this text," one model does everything via prompting ([11.6](../weeks/11.6-decoder-only.md)). It's *also* the **vulnerability**: because the model can't distinguish trusted instructions from untrusted content in that single channel, an attacker's text in the context can be read as instructions — prompt injection, which has no complete fix ([11.18](../weeks/11.18-safety.md)). The same architectural fact is both the feature and the flaw.

---

**Scoring:** 41–45 outstanding · 36–40 solid (module complete) · 28–35 review the linked lessons · <28 re-read **11.4, 11.8, 11.12, and 11.15** — the load-bearing four.

[📝 Back to quiz](quiz-01.md) · [🧠 Flashcards](../flashcards/deck.md) · [📖 Lessons](../weeks/README.md)
