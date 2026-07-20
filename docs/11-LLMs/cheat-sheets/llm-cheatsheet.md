# 📄 LLMs & Transformers — Cheat Sheet

[🏠 Module 11](../README.md) · [📖 Lessons](../weeks/README.md)

---

## 🧠 The core facts

| | |
|---|---|
| **⭐ What an LLM is** | a next-token predictor: `P(xₜ \| x_<t)` |
| **Chain rule** | `P(seq) = ∏ P(xₜ \| x_<t)` — models any sequence via the next token |
| **Training objective** | cross-entropy = log(perplexity) — nothing new |
| **Causal vs masked** | GPT (left-to-right, generates) vs BERT (both sides, understands) |
| **"Large"** | params × data × compute scaled together → **emergence** |
| **⭐ Probable ≠ true** | hallucination is built into the objective |

---

## 🔤 Tokenization (11.2)

| | |
|---|---|
| **Token** | the atom — read, predicted, and billed |
| **Granularity** | char (long) · word (OOV) · **subword (sweet spot)** |
| **⭐ BPE** | start from chars/bytes, merge most frequent pair repeatedly |
| **Byte-level BPE** | base = 256 bytes → **no unknown token, ever** |
| **WordPiece / Unigram / SentencePiece** | likelihood merge / prune-down / space-as-`▁` (multilingual) |
| **⭐ Context length** | max tokens; hard limit (O(n²)) |
| **⭐ Token efficiency** | cost/context/latency; unfair across languages; "strawberry" problem |

---

## 🧭 Embeddings + position (11.3)

| | |
|---|---|
| **Token embedding** | trainable `(vocab × d_model)` lookup; often **tied** with output |
| **⭐ Why position** | attention is **permutation-invariant** — order must be added |
| **Learned PE** | per-position table; can't extrapolate |
| **Sinusoidal** | fixed; relative-friendly |
| **⭐ RoPE** | rotate Q,K by position → **relative** distance; extrapolates (→ long context) |
| **d_model** | model width; residual-stream bandwidth |

---

## 🔥 Attention (11.4) ⭐

```
Attention(Q,K,V) = softmax(QKᵀ / √dₖ) · V
```

| | |
|---|---|
| **Q/K/V** | seek / matched-by / delivered-content (learned) |
| **√dₖ** | variance fix; else softmax saturates → vanishing gradients |
| **Multi-head** | h parallel heads, d_k=d_model/h → many relationship types |
| **Causal mask** | future → −∞ → decoder/GPT |
| **⭐ MHA/GQA/MQA** | h / g / 1 KV-heads → shrinking **KV cache** |
| **FlashAttention** | exact attention without the (n×n) matrix — memory rewrite |
| **⭐ O(n²)** | the central scaling wall |

---

## 🏗️ Transformer block (11.5)

| Component | Role |
|---|---|
| **⭐ Block** | attention + FFN, each with **residual + norm**, × N |
| **Attention** | the only cross-token step |
| **FFN (4×d)** | per-token; holds ~⅔ params & **knowledge** |
| **⭐ Residual stream** | info highway; sublayers *add* → trainable depth |
| **LayerNorm/RMSNorm** | per-token scale; RMSNorm skips centering |
| **⭐ Pre-LN** | norm before sublayer → stable deep training |
| **Params** | ≈ **12·N·d²** + embeddings |

---

## 🤖 Architecture families (11.6–11.7)

| Family | Attention | Generates? | For |
|---|---|---|---|
| Encoder (BERT) | bidirectional | ❌ | understanding |
| **⭐ Decoder (GPT)** | causal | ✅ | generation (general) |
| Enc-Dec (T5) | both + cross-attn | ✅ | seq2seq |

**⭐ Decoder-only won:** generation is a universal interface (any task = text-in/out). **Mini-GPT (11.8)** = embed → N causal blocks → proj → next-token loss → [09.10 loop](../../09-Deep-Learning/weeks/09.10-training-loop.md).

---

## 🏭 Pretraining & scaling (11.9–11.10)

| | |
|---|---|
| **Objective** | next-token (self-supervised → free labels) |
| **Pipeline** | clean → **dedup** → filter → tokenize → shard → train → checkpoint |
| **⭐ Constraint** | **memory** (weights+grads+Adam+activations), not compute |
| **Distributed** | data / tensor / pipeline parallel + ZeRO/FSDP |
| **⭐ Scaling laws** | loss = power law in params/data/compute (log-log line) |
| **⭐ Chinchilla** | scale params & data equally; **~20 tokens/param** |
| **Over-training** | small model + more data → cheap inference (deployment win) |

---

## 🎯 Fine-tuning & alignment (11.11–11.13)

| | |
|---|---|
| **Base model** | autocomplete; not an assistant |
| **⭐ SFT** | prompt→response pairs → follows instructions; teaches **behavior** not knowledge |
| **⭐ Loss masking** | prompt tokens = `-100`; train only on the response |
| **Forgetting** | narrow FT erodes general ability → low LR, few epochs |
| **⭐ LoRA** | freeze W, train low-rank `B·A` (~0.1% params) — the [06.3](../../06-Mathematics/weeks/06.3-linear-algebra-2.md) rank argument |
| **⭐ QLoRA** | 4-bit frozen base + LoRA → **fine-tune 65B on one GPU** |
| **Alignment** | pretrain → SFT → **align** (HHH) |
| **RLHF** | reward model (imitates preferences) + PPO + KL penalty; reward hacking |
| **⭐ DPO** | RL-free: one classification loss, ↑chosen ↓rejected — **stable, dominant** |

---

## ⚡ Inference (11.14–11.16)

| | |
|---|---|
| **Decoding** | greedy (facts) · **temperature** (creativity dial) · **top-p** (adaptive default) · beam (translation, not chat) |
| **⭐ KV cache** | store past K/V → generation O(n) not O(n²) |
| **⭐ Prefill** | process prompt in one parallel pass — **compute-bound** |
| **⭐ Decode** | one token at a time from cache — **memory-bound** |
| **KV cache memory** | grows with batch × context; often the real limit → GQA |
| **⭐ Quantize first** | int4 ≈ 4× memory/speed for ~1% quality |
| **Continuous batching** | add requests per token → GPU never idle (biggest throughput win) |
| **Speculative decoding** | draft guesses, big model verifies in parallel; same output |

---

## 📏 Evaluation & safety (11.17–11.18)

| | |
|---|---|
| **⭐ Ladder** | perplexity → benchmarks → human/LLM-judge |
| **Perplexity** | prediction, not usefulness; tokenizer-bound |
| **⭐ Contamination** | test in training → inflated scores |
| **LLM-as-judge** | position/verbosity/self-preference bias |
| **Risks** | factuality, toxicity, bias — eval each on your data |
| **⭐ Prompt injection** | instructions & data share one channel → **no complete fix** |
| **Jailbreaks / leakage** | alignment is shallow; models memorize |
| **⭐ Best defense** | **least privilege — assume hijack, contain blast radius** |

---

## 🚀 Deployment & production (11.19–11.20)

| | |
|---|---|
| **API vs open vs self-hosted** | rent / own / own-infra |
| **⭐ Deciders** | **privacy** & **cost-at-scale** (curves cross at high volume) |
| **Cascade** | small model → escalate to frontier |
| **⭐ The system** | gateway · guardrails · **cache** · monitor · rate-limit · fallback |
| **⭐ Caching** | exact + **semantic** + prefix → biggest cost/latency win |
| **Monitor** | token cost · latency (TTFT/per-token) · quality proxies · drift |
| **⭐ The discipline** | [08.17](../../08-Machine-Learning/weeks/08.17-production-ml.md)/[10.13](../../10-NLP/weeks/10.13-production.md) MLOps, **unchanged** + LLM specifics |

---

## 🎯 The twelve sentences

1. **Everything an LLM does is next-token prediction.**
2. **The chain rule lets one next-token model represent any sequence.**
3. **Attention = softmax(QKᵀ/√d)·V — the only place tokens exchange info.**
4. **A Transformer block is attention + FFN, residual + norm, repeated N times.**
5. **Causal masking makes a Transformer a generator (GPT); decoder-only won because generation is universal.**
6. **A mini-GPT is pure assembly — build it and the black box opens.**
7. **Pretraining is the training loop at scale; memory, not compute, is the constraint.**
8. **Scaling laws are predictable; Chinchilla says ~20 tokens/param.**
9. **SFT teaches behavior (loss-masked); LoRA/QLoRA make it cheap; DPO aligns it simply.**
10. **The KV cache turns generation from O(n²) to O(n); prefill is compute-bound, decode is memory-bound.**
11. **Quantize first, batch continuously — inference optimization is a memory game.**
12. **Prompt injection has no complete fix — least privilege and defense in depth; the system around the model is the product.**

---

[⬆ Module 11](../README.md) · [📖 Lessons](../weeks/README.md) · [🧠 Flashcards](../flashcards/deck.md) · [📝 Quiz](../quizzes/quiz-01.md)
