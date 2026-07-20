# 🧠 Module 11 · LLMs & Transformers — Flashcard Deck

[🏠 Module 11](../README.md) · [📖 Lessons](../weeks/README.md) · [📄 Cheat sheet](../cheat-sheets/llm-cheatsheet.md)

> **~110 cards.** Cover the answer, say it aloud, *then* check. ⭐ marks the load-bearing ones.

---

## 11.1 · What Is a Language Model?

**Q:** ⭐ What is a language model? → **A:** A probability distribution over token sequences; concretely, a next-token predictor `P(xₜ | x_<t)`. → [11.1](../weeks/11.1-what-is-a-language-model.md)

**Q:** State the chain rule for a sequence. → **A:** `P(x₁…xₙ) = ∏ P(xₜ | x₁…xₜ₋₁)` — model the next token, model any sequence.

**Q:** ⭐ Causal vs masked LM? → **A:** Left-to-right, generates (GPT) vs both-sided, understands but can't generate (BERT).

**Q:** Why are generative LLMs causal? → **A:** Generation needs to predict the *next* token from only the past; a bidirectional model has no notion of "next."

**Q:** What does "large" add? → **A:** Scale in params × data × compute → emergent abilities and in-context learning.

**Q:** ⭐ Why does an LLM hallucinate? → **A:** It's trained to produce *probable* text, not *true* text; a fluent falsehood is high-probability.

**Q:** What is in-context learning? → **A:** Performing new tasks from prompt examples with no weight updates — the "learning" happens in the forward pass.

---

## 11.2 · Tokenization

**Q:** ⭐ Why subwords over words/chars? → **A:** Fixed moderate vocabulary, no unknown words, manageable sequence length. → [11.2](../weeks/11.2-tokenization.md)

**Q:** ⭐ How does BPE train? → **A:** Start from chars/bytes; repeatedly merge the most frequent adjacent pair; stop at target vocab; save the merges.

**Q:** What is byte-level BPE and why use it? → **A:** Base = 256 bytes, so any input tokenizes with zero unknown tokens.

**Q:** BPE vs WordPiece vs Unigram? → **A:** Merge by frequency / by likelihood / start large and prune by likelihood.

**Q:** What does SentencePiece add? → **A:** Treats spaces as tokens (`▁`) → language-agnostic, losslessly reversible.

**Q:** ⭐ What is token efficiency? → **A:** Tokens per text — drives cost, context budget, latency; much worse for non-English scripts.

**Q:** Why can't LLMs count letters? → **A:** They see opaque token IDs, not individual characters (the strawberry problem).

**Q:** What turns next-token prediction into a chatbot? → **A:** Special/chat-role tokens (`<|user|>`, `<|assistant|>`, `<eos>`).

---

## 11.3 · Embeddings & Positional Encoding

**Q:** What is the token embedding table? → **A:** A trainable `(vocab, d_model)` matrix; a token ID indexes its row (lookup, not matmul). → [11.3](../weeks/11.3-embeddings-positional.md)

**Q:** ⭐ Why do Transformers need positional encoding? → **A:** Self-attention is permutation-invariant (a set op); without position, word order is lost.

**Q:** Why did dropping recurrence create the position problem? → **A:** RNNs read tokens in order (order for free); attention processes all at once, so order must be added.

**Q:** Learned vs sinusoidal PE? → **A:** Trainable per-position table (can't extrapolate) vs fixed sinusoids (parameter-free, relative-friendly).

**Q:** ⭐ What is RoPE and why is it the default? → **A:** Rotates Q and K by an angle ∝ position so the attention score depends on *relative* distance; parameter-free and extrapolates.

**Q:** How are long-context models made? → **A:** By scaling RoPE (position interpolation / NTK) beyond the trained length.

**Q:** What is weight tying? → **A:** Sharing the input embedding matrix with the output projection to save parameters.

---

## 11.4 · Attention

**Q:** ⭐ State the attention formula. → **A:** `softmax(QKᵀ/√dₖ)·V`. → [11.4](../weeks/11.4-attention.md)

**Q:** Where do tokens exchange information in an LLM? → **A:** Only in attention; the FFN processes each token independently.

**Q:** ⭐ Why divide by √dₖ? → **A:** Dot-product variance grows with dₖ; without scaling, softmax saturates and gradients vanish.

**Q:** What is multi-head attention? → **A:** h parallel attention ops (d_k=d_model/h) capturing different relationship types at ~the cost of one.

**Q:** ⭐ MHA vs GQA vs MQA? → **A:** Number of key/value heads: h / g (grouped) / 1 — shrinking the KV cache.

**Q:** ⭐ Why does every large model use GQA? → **A:** It cuts KV-cache memory (the long-context bottleneck) several-fold with almost no quality loss.

**Q:** What is FlashAttention? → **A:** Exact attention that never materializes the (n×n) matrix — same math, minimal memory traffic, much faster.

**Q:** ⭐ Attention's fundamental cost? → **A:** O(n²) in time and memory — the central scaling constraint.

---

## 11.5 · Transformer Architecture

**Q:** ⭐ What are the two sublayers of a block? → **A:** Multi-head attention (tokens mix) and a position-wise feed-forward network (per-token processing). → [11.5](../weeks/11.5-transformer-architecture.md)

**Q:** ⭐ Where does most LLM "knowledge" live? → **A:** In the feed-forward weights (the wide 4×d_model hidden layer acts like key-value memory).

**Q:** What is the residual stream? → **A:** A d_model-wide highway through the network that each sublayer *adds* to (never overwrites) — enabling trainable depth.

**Q:** ⭐ Pre-LN vs Post-LN? → **A:** Norm before the sublayer (clean residual, stable, modern) vs after the residual add (original, needs warmup).

**Q:** What is RMSNorm? → **A:** LayerNorm without mean-centering — cheaper, equal quality (Llama).

**Q:** How do you estimate parameter count? → **A:** ≈ 12·N·d_model² plus embeddings.

**Q:** What makes deep Transformers trainable? → **A:** Residual connections (gradient highway) + Pre-LN normalization.

---

## 11.6–11.7 · Decoder-only & architecture types

**Q:** ⭐ What makes a Transformer decoder-only? → **A:** A causal mask: each token attends only to itself and earlier tokens. → [11.6](../weeks/11.6-decoder-only.md)

**Q:** ⭐ Why does the causal mask make training efficient? → **A:** One forward pass yields a next-token loss at every position, with no answer leakage.

**Q:** How does a decoder-only model generate? → **A:** Autoregressively: forward → sample → append → repeat until `<eos>`.

**Q:** ⭐ Why did general LLMs converge on decoder-only? → **A:** Generation is a universal interface — any task is text-in/text-out.

**Q:** The three architecture families? → **A:** Encoder-only (understand), decoder-only (generate), encoder-decoder (seq2seq). → [11.7](../weeks/11.7-encoder-decoder-types.md)

**Q:** ⭐ Why haven't encoders disappeared? → **A:** For high-volume understanding (classification, RAG embeddings), a small encoder is cheaper, faster, often more accurate than a giant decoder.

---

## 11.8 · Build a Mini Transformer

**Q:** ⭐ What is a mini-GPT made of? → **A:** Token+positional embeddings → N causal blocks (attention+FFN, Pre-LN, residuals) → output projection → next-token cross-entropy. → [11.8](../weeks/11.8-build-mini-transformer.md)

**Q:** How do you prepare LM training data? → **A:** Chunk a token stream into (x, y) where y is x shifted by one; every position's target is the next token.

**Q:** ⭐ First debugging step for a mini-GPT? → **A:** Overfit one batch to ~0 loss; if it can't, the bug is in the model/loop.

**Q:** What should the initial loss be? → **A:** ≈ ln(vocab_size).

**Q:** ⭐ What does building a working mini-GPT prove? → **A:** An LLM is not magic — it's these components stacked and trained; scale changes magnitude, not mechanism.

---

## 11.9–11.10 · Pretraining & Scaling

**Q:** What is the pretraining objective? → **A:** Next-token prediction (cross-entropy) — self-supervised, so labels are free. → [11.9](../weeks/11.9-pretraining.md)

**Q:** ⭐ Why can LLMs train on trillions of tokens? → **A:** Self-supervision needs no human labels; the whole web becomes training data.

**Q:** ⭐ Why is deduplication essential? → **A:** Improves quality, cuts memorization, saves compute, prevents benchmark contamination.

**Q:** The three axes of distributed training? → **A:** Data parallel (split batch), tensor parallel (split each layer's matmuls), pipeline parallel (split layers).

**Q:** ⭐ The binding constraint in pretraining? → **A:** Memory — weights + gradients + optimizer states + activations exceed a single GPU.

**Q:** ⭐ What is a scaling law? → **A:** Test loss falls as a power law in size, data, compute — a straight line on log-log, so quality is predictable. → [11.10](../weeks/11.10-scaling-laws.md)

**Q:** ⭐ What did Chinchilla show? → **A:** Scale params and data roughly equally (~20 tokens/param); most big models were under-trained.

**Q:** ⭐ Why over-train small models? → **A:** Inference cost dominates deployment; a smaller, over-trained model is cheaper to serve for life.

---

## 11.11–11.13 · Fine-tuning & Alignment

**Q:** ⭐ What does instruction tuning (SFT) teach? → **A:** Behavior/format (how to be helpful), not new knowledge — the base model already knows the facts. → [11.11](../weeks/11.11-fine-tuning.md)

**Q:** ⭐ What is loss masking in SFT? → **A:** Setting prompt-token labels to -100 so loss is computed only on the response tokens.

**Q:** What is catastrophic forgetting? → **A:** Losing general ability by over-fine-tuning; mitigate with low LR, few epochs, diverse data, or PEFT.

**Q:** Should you fine-tune to add facts? → **A:** No — use RAG; fine-tuning teaches behavior, not reliable factual recall.

**Q:** ⭐ What is LoRA? → **A:** Freeze W, train a low-rank update ΔW=B·A (rank r≪d) → ~0.1% of params. → [11.12](../weeks/11.12-peft-lora.md)

**Q:** Why does low-rank fine-tuning work? → **A:** Fine-tuning makes a small, structured change whose intrinsic rank is low ([06.3](../../06-Mathematics/weeks/06.3-linear-algebra-2.md)).

**Q:** ⭐ What memory problem does LoRA solve? → **A:** Adam's optimizer state (3× per trained param) — training 0.1% of params pays the tax on only 0.1%.

**Q:** ⭐ What is QLoRA? → **A:** LoRA on a 4-bit-quantized frozen base — fine-tune a 65B model on a single 48GB GPU at ~full quality.

**Q:** Why keep LoRA adapters separate? → **A:** One frozen base + many tiny (~10MB) adapters, hot-swappable — serve dozens of fine-tunes from shared weights.

**Q:** ⭐ What are the three stages of building an assistant? → **A:** Pretrain (knowledge) → SFT (instruction-following) → alignment (preferences). → [11.13](../weeks/11.13-alignment.md)

**Q:** What is RLHF? → **A:** Train a reward model from human preference comparisons → RL-fine-tune (PPO) to maximize reward, with a KL penalty.

**Q:** What is reward hacking? → **A:** The policy exploits the imperfect reward model (sycophancy, verbosity) to score high without being better.

**Q:** ⭐ What is DPO and why is it popular? → **A:** Direct Preference Optimization — aligns with a single classification-style loss, no reward model or RL; stable, cheap, dominant.

---

## 11.14–11.16 · Inference

**Q:** ⭐ What does temperature do? → **A:** Reshapes the distribution: low sharpens (focused), high flattens (diverse/creative). → [11.14](../weeks/11.14-inference-decoding.md)

**Q:** Top-k vs top-p? → **A:** Fixed number of top tokens vs smallest set with cumulative probability ≥ p (adaptive to confidence — the default).

**Q:** Why avoid beam search for chat? → **A:** It maximizes sequence probability → bland, repetitive, generic text.

**Q:** ⭐ How does temperature relate to safety? → **A:** Higher temperature samples lower-probability tokens, increasing hallucination/unsafe output.

**Q:** ⭐ What is the KV cache? → **A:** A store of past tokens' keys/values so each new token attends to cached K/V instead of recomputing them. → [11.15](../weeks/11.15-kv-cache.md)

**Q:** Why is naive generation O(n²)? → **A:** Each step re-runs attention over the whole growing sequence, recomputing unchanged past K/V.

**Q:** ⭐ Prefill vs decode? → **A:** Prefill processes the prompt in one parallel pass (compute-bound); decode generates token by token from the cache (memory-bound).

**Q:** ⭐ What often limits concurrency, weights or cache? → **A:** The KV cache — it grows with batch × context and can exceed the fixed weight memory.

**Q:** ⭐ Highest-leverage inference optimization? → **A:** Quantization (int8/int4) — decode is memory-bound, so fewer bytes/weight cuts the dominant cost ~4× for ~1% quality. → [11.16](../weeks/11.16-inference-optimization.md)

**Q:** ⭐ What is continuous batching? → **A:** Add/remove requests from the running batch per token so the GPU never idles; works because decode is memory-bound (shared weight reads).

**Q:** What is speculative decoding? → **A:** A small draft model guesses several tokens; the big model verifies them in one parallel pass — 2–3× faster, identical output.

---

## 11.17–11.20 · Evaluation, Safety, Deployment, Production

**Q:** ⭐ Why can't one number tell you an LLM is good? → **A:** Low perplexity can be unhelpful; high benchmarks can hallucinate; fluent can be wrong — capability is multi-dimensional. → [11.17](../weeks/11.17-evaluation.md)

**Q:** What is benchmark contamination? → **A:** Test questions appearing in training data → memorized answers inflate scores without real capability.

**Q:** What biases does LLM-as-judge have? → **A:** Position (favors first), verbosity (prefers longer), self-preference, and being fooled by confident-but-wrong answers.

**Q:** ⭐ Root cause of most LLM security problems? → **A:** Instructions and data share one channel — the model can't separate trusted instructions from untrusted content. → [11.18](../weeks/11.18-safety.md)

**Q:** ⭐ Why is prompt injection not fully fixable? → **A:** It's a consequence of the architecture; mitigations reduce but don't eliminate it.

**Q:** ⭐ The most important LLM defense? → **A:** Least privilege — assume the model will be hijacked and limit what it can *do*, so a compromise is contained.

**Q:** ⭐ The two decisive factors in API vs open? → **A:** Privacy (can data leave?) and cost-at-scale (the cost curves cross at high volume). → [11.19](../weeks/11.19-apis-vs-open-models.md)

**Q:** What is a model cascade? → **A:** Route easy queries to a cheap small model, escalate hard ones to a frontier model.

**Q:** ⭐ In production, what's the main engineering? → **A:** The system *around* the model — gateway, guardrails, caching, monitoring, rate limiting, fallbacks. → [11.20](../weeks/11.20-production-architecture.md)

**Q:** ⭐ Why is semantic caching high-leverage? → **A:** Generation is slow and per-token-billed; returning a cached answer for a similar query serves much of FAQ traffic for free.

**Q:** The recurring production lesson? → **A:** LLM production is the [08.17](../../08-Machine-Learning/weeks/08.17-production-ml.md)/[10.13](../../10-NLP/weeks/10.13-production.md) MLOps discipline, unchanged, plus LLM specifics.

---

## 🎯 The twelve sentences (recall all twelve cold)

1. **Everything an LLM does is next-token prediction.**
2. **The chain rule lets one next-token model represent any sequence.**
3. **Attention = softmax(QKᵀ/√d)·V — the only place tokens exchange info.**
4. **A Transformer block is attention + FFN, residual + norm, repeated N times.**
5. **Causal masking makes a Transformer a generator; decoder-only won because generation is universal.**
6. **A mini-GPT is pure assembly — build it and the black box opens.**
7. **Pretraining is the training loop at scale; memory, not compute, is the constraint.**
8. **Scaling laws are predictable; Chinchilla says ~20 tokens/param.**
9. **SFT teaches behavior (loss-masked); LoRA/QLoRA make it cheap; DPO aligns it simply.**
10. **The KV cache turns generation O(n²)→O(n); prefill is compute-bound, decode is memory-bound.**
11. **Quantize first, batch continuously — inference optimization is a memory game.**
12. **Prompt injection has no complete fix — least privilege; the system around the model is the product.**

---

[⬆ Module 11](../README.md) · [📖 Lessons](../weeks/README.md) · [📄 Cheat sheet](../cheat-sheets/llm-cheatsheet.md) · [📝 Quiz](../quizzes/quiz-01.md)
