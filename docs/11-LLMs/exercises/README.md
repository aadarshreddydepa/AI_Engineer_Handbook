# 🏋️ Module 11 · LLMs & Transformers — Exercises

[🏠 Module 11](../README.md) · [📖 Lessons](../weeks/README.md) · [🧩 Projects](../projects/)

> Build-it exercises, ordered along the module's spine: **build the architecture → train & adapt → serve & operate.** If you do only four, do ⭐ **E4, E8, E14, E16** — attention by hand, a working mini-GPT, LoRA, and a KV cache. Together they are the module.
>
> Each exercise lists a **goal**, **constraints**, and a **done-when** (an objective, checkable success criterion).

---

## Tier 1 · Build the architecture (11.1–11.8)

### E1 · Language model, three ways
**Goal:** build an n-gram, an LSTM, and (stub) a Transformer LM on one corpus; compare perplexity.
**Done-when:** the LSTM beats the n-gram on held-out perplexity; you can explain what next-token prediction each computes. → [11.1](../weeks/11.1-what-is-a-language-model.md)

### ⭐ E2 · BPE from scratch
**Goal:** implement BPE training (learn merges) + encode/decode. Byte-level base.
**Constraints:** no tokenizer library in the core.
**Done-when:** (1) `decode(encode(x)) == x` for arbitrary bytes (lossless); (2) merges match a reference on the same corpus; (3) a tokens-per-language report across 3 languages shows the efficiency gap. → [11.2](../weeks/11.2-tokenization.md)

### E3 · Positional encoding lab
**Goal:** implement learned, sinusoidal, and RoPE encodings; test extrapolation.
**Done-when:** without PE, a single attention layer is order-blind (outputs just permute); RoPE's relative-distance property holds numerically; train-short/test-long shows RoPE extrapolates and learned PE fails. → [11.3](../weeks/11.3-embeddings-positional.md)

### ⭐ E4 · Attention from scratch, verified
**Goal:** single-head, multi-head, causal, and **GQA** attention in NumPy.
**Constraints:** no framework in the forward pass.
**Done-when:** (1) `torch.allclose` vs PyTorch; (2) causal mask zeroes future weights; (3) a float64 gradient check passes; (4) the GQA KV-cache-size reduction vs MHA is quantified. **The most important exercise in the first half.** → [11.4](../weeks/11.4-attention.md)

### E5 · Transformer block
**Goal:** one Pre-LN block (attention + FFN + residuals + norm) in PyTorch.
**Done-when:** input/output shapes match; gradients flow to all params; param count ≈ 12·d²; overfits a tiny sequence. → [11.5](../weeks/11.5-transformer-architecture.md)

### E6 · Causal masking
**Goal:** show the causal mask yields n−1 next-token losses from one pass, and removing it causes trivial (leaky) overfitting.
**Done-when:** you demonstrate both, explaining the leakage the mask prevents. → [11.6](../weeks/11.6-decoder-only.md)

### E7 · Architecture selector
**Goal:** benchmark an encoder classifier vs a decoder generator on cost/latency/accuracy for a classification task.
**Done-when:** you show the small encoder is far cheaper for classification and can justify decoder-only for open-ended generation. → [11.7](../weeks/11.7-encoder-decoder-types.md)

### ⭐⭐ E8 · Build and train a mini-GPT
**Goal:** the complete decoder-only Transformer — tokenizer → embeddings → causal blocks → generation — trained until it produces coherent text.
**Constraints:** verify hand-built attention with `torch.allclose`; use the [09.10 loop](../../09-Deep-Learning/weeks/09.10-training-loop.md).
**Done-when:** (1) init loss ≈ ln(vocab); (2) overfit-one-batch → ~0; (3) trained model generates recognizable text; (4) an ablation (remove residuals / PE / norm) shows each breaks it. **The flagship of the first half.** → [11.8](../weeks/11.8-build-mini-transformer.md)

---

## Tier 2 · Train & adapt (11.9–11.13)

### E9 · Miniature pretraining pipeline
**Goal:** clean → dedup → filter → tokenize → shard → train your mini-GPT; ablate dedup/filter.
**Done-when:** dedup measurably improves validation perplexity and reduces verbatim memorization of a planted canary; resume-from-checkpoint (with optimizer state) continues smoothly. → [11.9](../weeks/11.9-pretraining.md)

### E10 · Scaling law
**Goal:** train mini-GPTs across sizes; fit loss vs params on log-log axes.
**Done-when:** the fit is approximately linear (a power law); you find a local compute-optimal N:D and demonstrate over-training keeps loss falling. → [11.10](../weeks/11.10-scaling-laws.md)

### E11 · Instruction-tune with loss masking
**Goal:** SFT a small base model on prompt→response pairs, with and without prompt-loss-masking.
**Done-when:** the masked model *answers* while the unmasked one drifts toward *generating questions*; you quantify a forgetting delta on a general task. → [11.11](../weeks/11.11-fine-tuning.md)

### ⭐ E12 · LoRA from scratch
**Goal:** implement `LoRALinear`; wrap attention projections of your mini-GPT.
**Constraints:** zero-init B; tune alpha/r.
**Done-when:** (1) trainable params ≈ 0.1–1% of total; (2) a merged adapter's outputs equal the unmerged (base + adapter); (3) two adapters both work from one frozen base (multi-task). → [11.12](../weeks/11.12-peft-lora.md)

### E13 · DPO in miniature
**Goal:** apply a DPO-style loss on preference pairs to a small SFT model, with a frozen reference.
**Done-when:** the aligned model raises chosen-response likelihood and lowers rejected; a reward-hacking demo (optimize "longer = better") visibly degenerates. → [11.13](../weeks/11.13-alignment.md)

---

## Tier 3 · Serve & operate (11.14–11.20)

### E14 · Decoding playground
**Goal:** implement greedy, temperature, top-k, top-p, and a repetition penalty; visualize the next-token distribution.
**Done-when:** temperature sweep shows the coherence/diversity trade-off; top-p adapts its nucleus to confidence while top-k doesn't; greedy is reproducible and sampling isn't (until seeded). → [11.14](../weeks/11.14-inference-decoding.md)

### ⭐ E15 · KV cache from scratch
**Goal:** add a KV cache to your mini-GPT `generate`; benchmark vs naive.
**Constraints:** cached output must equal naive output.
**Done-when:** (1) outputs are bit-identical; (2) naive is O(n²) and cached is O(n) on a length sweep; (3) prefill vs decode timing is separated; (4) a capacity calculator predicts max concurrent requests (MHA vs GQA). → [11.15](../weeks/11.15-kv-cache.md)

### E16 · Optimized serving stack
**Goal:** take an open model from naive to efficient: +KV cache → +int4 quant → +continuous batching → +speculative decoding.
**Done-when:** each stage's latency (TTFT, per-token) and throughput are measured, quality is preserved within tolerance, and you report the cumulative speedup. → [11.16](../weeks/11.16-inference-optimization.md)

### E17 · Evaluation harness
**Goal:** perplexity + a benchmark + a (debiased) LLM-as-judge + a risk eval (factuality/toxicity) + a contamination check.
**Done-when:** judge debiasing reduces position bias; the contamination checker catches planted overlap; a regression run detects an injected quality drop. → [11.17](../weeks/11.17-evaluation.md)

### E18 · Guardrail layer
**Goal:** wrap a model in input/output guardrails + least-privilege tools + monitoring; red-team it.
**Done-when:** guards catch known injection/PII patterns, consequential tools require confirmation, and you report a catch-rate vs false-positive-rate on an adversarial set (no exploit details — just categories). → [11.18](../weeks/11.18-safety.md)

### E19 · Model router
**Goal:** a provider-agnostic layer routing by privacy/complexity + a cascade + fallback + cost tracking.
**Done-when:** private-tagged requests never hit an external API; the cascade escalates only hard cases; a cost report compares API-only vs self-hosted vs routed. → [11.19](../weeks/11.19-apis-vs-open-models.md)

### E20 · Production LLM service
**Goal:** gateway (rate limit) + guardrails + versioned prompts + **semantic cache** + streaming + monitoring (cost/latency/quality/drift).
**Done-when:** guardrails block injection/PII; a cache hit returns instantly; rate limits enforce; cost is tracked per request; fallback triggers on model failure. → [11.20](../weeks/11.20-production-architecture.md)

---

## 🎓 Capstone challenge

### E21 · The end-to-end LLM
Combine E2 + E4 + E8 + E12 + E15 + E20 into one repo: your tokenizer, your attention (verified), a trained mini-GPT, a LoRA fine-tune, a KV cache, and a production serving wrapper — with a `pytest` suite covering the round-trip tokenizer, attention `torch.allclose`, overfit-one-batch, LoRA param-count, and cached==naive generation.
**Done-when:** `pytest` passes all five. This repo *is* your proof that you understand LLMs from the token up to the served endpoint — not just that you can call an API. → [11.21](../weeks/11.21-projects-summary.md)

---

> [!TIP]
> The `softmax(QKᵀ/√dₖ)·V` you verify in E4 is the exact operation running in every frontier model. Don't skip the hand-builds (E2, E4, E8, E12, E15) to get to the API faster — the libraries only make sense *because* of the hand-builds.

[🏠 Module 11](../README.md) · [📝 Quiz](../quizzes/quiz-01.md) · [🧠 Flashcards](../flashcards/deck.md) · [🧩 Projects](../projects/)
