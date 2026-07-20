# 📝 Module 11 · LLMs & Transformers — Quiz 01

[🏠 Module 11](../README.md) · [📖 Lessons](../weeks/README.md) · [✅ Answers](answers-01.md)

> **45 questions across all 21 lessons.** Aim for an explanation, not just the letter — the [answers](answers-01.md) grade reasoning. Target: **36/45** to consider the module solid.

---

## Part A · Architecture (11.1–11.8)

**1.** Define a language model mathematically. What does the chain rule of probability have to do with it?

**2.** What's the difference between a causal and a masked language model? Why is ChatGPT causal?

**3.** Why is hallucination intrinsic to the language-modeling objective?

**4.** Walk through BPE training. Why do modern LLMs use *byte-level* BPE?

**5.** What is token efficiency, and why is tokenization considered unfair across languages? Why can't LLMs reliably count letters?

**6.** Why must a Transformer add positional information? What property of attention makes it necessary?

**7.** Compare learned, sinusoidal, and rotary (RoPE) positional encodings. Why do modern LLMs use RoPE, and how does it enable long-context extension?

**8.** ⭐ Write the scaled dot-product attention formula. Explain each of Q, K, V and why the √dₖ scaling exists.

**9.** Explain MHA vs GQA vs MQA. Why do modern large models use GQA?

**10.** What are the two sublayers of a Transformer block? What does each do, and where does most of the model's "knowledge" live?

**11.** What is the residual stream, and why are residual connections essential? Explain Pre-LN vs Post-LN.

**12.** What makes a Transformer "decoder-only," and why does the causal mask make training efficient?

**13.** Why did general-purpose LLMs converge on decoder-only architectures? When would you still use an encoder-only model?

**14.** ⭐ Walk through a mini-GPT forward pass from token IDs to loss. What's your first debugging step if it won't learn, and why?

---

## Part B · Training & Adaptation (11.9–11.13)

**15.** What is the pretraining objective, and why is self-supervision the key enabler of LLMs?

**16.** Walk through the pretraining data pipeline. Why is deduplication so important?

**17.** Why is memory (not compute) usually the binding constraint in large-scale training?

**18.** ⭐ What is a scaling law? Explain the Chinchilla result and what was wrong with the prior view.

**19.** Why do modern 7B models train on far more than 20 tokens per parameter?

**20.** What does instruction tuning (SFT) actually teach the model? Why does a small, high-quality dataset often suffice?

**21.** ⭐ Explain loss masking in SFT. What breaks without it?

**22.** What is catastrophic forgetting, and how do you mitigate it? When should you use RAG instead of fine-tuning?

**23.** ⭐ Explain LoRA. Why is the low-rank assumption reasonable, and what memory problem does it solve?

**24.** What is QLoRA, and how does it fit a 65B fine-tune on one GPU? Why keep adapters separate from the base weights?

**25.** Walk through the RLHF pipeline. What are the roles of the reward model and the KL penalty?

**26.** What is reward hacking, and how does it relate to Goodhart's law?

**27.** ⭐ What is DPO, and why has it largely replaced RLHF for open-source alignment?

---

## Part C · Inference & Serving (11.14–11.16)

**28.** Explain the difference between the model and the decoding strategy in generation.

**29.** What does temperature do, and how do you choose it per task? How does it relate to safety?

**30.** Compare top-k and top-p sampling. Why is top-p usually preferred?

**31.** ⭐ What is the KV cache, and what problem does it solve? Why is caching keys and values valid?

**32.** ⭐ Explain prefill vs decode. Why is one compute-bound and the other memory-bound?

**33.** Why does the KV cache often limit concurrency more than the model weights? How does GQA help?

**34.** ⭐ Why is quantization the highest-leverage LLM inference optimization?

**35.** Explain continuous batching. Why does it work so well for LLM decode?

**36.** What is speculative decoding, and why doesn't it hurt output quality?

---

## Part D · Evaluation, Safety, Production (11.17–11.20)

**37.** Why is evaluating LLMs so much harder than classification models? Walk through the evaluation ladder.

**38.** What is benchmark contamination, and how does it corrupt reported scores?

**39.** What biases does LLM-as-judge have, and how do you mitigate them?

**40.** ⭐ Why is prompt injection considered the signature LLM vulnerability, and why can't it be fully fixed?

**41.** ⭐ What is the most important defensive principle for LLM systems, and why?

**42.** Compare hosted APIs, open-weight self-hosting, and managed hosting. What are the two decisive factors in choosing?

**43.** What is a model cascade, and why is it cost-effective?

**44.** ⭐ Draw the reference architecture for a production LLM application. Why is caching (especially semantic) so important?

**45.** How much of production LLM engineering is genuinely new vs inherited MLOps discipline?

---

## 🎁 Bonus (harder)

**B1.** Trace a single idea — "memory is the constraint" — through pretraining, LoRA, the KV cache, and quantization. How does each relate to it?

**B2.** You build a mini-GPT, and it generates coherent text. Explain precisely what this proves (and doesn't prove) about a 175B-parameter model.

**B3.** Explain why the same fact — "instructions and data share one channel" — is simultaneously why decoder-only models are so general (11.6) *and* why prompt injection can't be fully fixed (11.18).

---

[✅ Check your answers →](answers-01.md) · [🧠 Flashcards](../flashcards/deck.md) · [📄 Cheat sheet](../cheat-sheets/llm-cheatsheet.md)
