# 🧠 Module 15 · Fine-Tuning & Alignment — Flashcard Deck

[🏠 Module 15](../README.md) · [📖 Lessons](../weeks/README.md) · [📄 Cheat sheet](../cheat-sheets/finetuning-cheatsheet.md)

> **~95 cards.** Cover the answer, say it aloud, *then* check. ⭐ marks the load-bearing ones.

---

## 15.1–15.3 · Decide

**Q:** ⭐ What does fine-tuning change — knowledge or behavior? → **A:** Behavior (style, format, skill, domain conventions); it's a poor, leaky way to inject knowledge. → [15.1](../weeks/15.1-why-fine-tuning.md)

**Q:** Facts → ? Framing → ? Behavior → ? → **A:** Facts → RAG; framing → prompt; behavior/style/skill → fine-tune.

**Q:** Why is fine-tuning facts a bad idea? → **A:** The model learns them fuzzily → confident hallucination, no citations, no way to update without retraining.

**Q:** ⭐ Base vs instruct vs chat model? → **A:** Base completes text; instruct follows single instructions (after SFT); chat is aligned for multi-turn with a chat template. → [15.2](../weeks/15.2-base-models.md)

**Q:** Why must training data use the model's chat template? → **A:** The model trains on the rendered template string; a mismatch means it sees an unfamiliar input at inference and behaves badly.

**Q:** ⭐ What's the default fine-tuning method and why? → **A:** LoRA (QLoRA when memory-bound): full-FT quality on most tasks at a fraction of memory/cost, swappable adapters. → [15.3](../weeks/15.3-strategy-selection.md)

**Q:** LoRA vs QLoRA — when each? → **A:** Both train adapters; QLoRA also 4-bit-quantizes the frozen base for limited GPUs; LoRA when you have the VRAM.

**Q:** What is continued pretraining, and when? → **A:** Next-token on unlabeled domain text (no instructions) to teach new domain language before SFT — for genuine domain gaps only.

---

## 15.4–15.5 · Data

**Q:** ⭐ Why is data the leverage in fine-tuning? → **A:** The model mirrors its training data (quirks and errors included); fine-tuning is ~80% data engineering. → [15.4](../weeks/15.4-dataset-preparation.md)

**Q:** ⭐ Quality vs quantity? → **A:** Quality dominates — a few thousand clean, diverse, correctly-formatted examples beat a hundred thousand noisy ones.

**Q:** What is data leakage and why is it fatal? → **A:** A test example (or paraphrase/same-source) also in training → the model saw the answer → inflated eval; dedup before splitting, split by group.

**Q:** Why remove PII before training? → **A:** The model memorizes training data and can leak PII in outputs.

**Q:** Two dominant instruction formats? → **A:** Alpaca `{instruction, input, output}` (single-turn source) and `messages` chat format (native multi-turn). → [15.5](../weeks/15.5-instruction-datasets.md)

**Q:** Why use `apply_chat_template`? → **A:** It inserts the model's exact special tokens/roles; hand-concatenation is a top format-bug source.

---

## 15.6–15.9 · Train

**Q:** ⭐ What is SFT, fundamentally? → **A:** The same next-token/cross-entropy objective as pretraining, applied to curated instruction→response examples. → [15.6](../weeks/15.6-sft.md)

**Q:** ⭐ What is loss masking and why? → **A:** Computing loss only on response tokens (prompt labels = -100) so the model learns to produce answers, not parrot prompts.

**Q:** Why keep EOS in the labels? → **A:** So the model learns when to stop generating.

**Q:** ⭐ Why is full fine-tuning so memory-hungry? → **A:** Per parameter you store weight + gradient + Adam's two moments (+ fp32 master) ≈ 16 bytes, on *every* parameter. → [15.7](../weeks/15.7-full-fine-tuning.md)

**Q:** How much to full-fine-tune a 7B? → **A:** ~112 GB (weights+grad+optimizer) — several high-end GPUs.

**Q:** ⭐ What is LoRA in one equation? → **A:** `W' = W + BA`: freeze pretrained `W`, train low-rank `B (d×r)` and `A (r×k)`. → [15.8](../weeks/15.8-lora.md)

**Q:** ⭐ Where does LoRA's memory saving come from? → **A:** Freezing `W` — no gradient/optimizer state on the base, so the ~16 bytes/param applies only to the tiny adapters.

**Q:** Why initialize `B` to zero? → **A:** So `BA=0` at start; training begins exactly at the pretrained model and adds to it (stable).

**Q:** What do rank and alpha control? → **A:** Rank = the update's capacity (subspace size); alpha scales `ΔW` (α/r ≈ effective adapter LR).

**Q:** ⭐ What is QLoRA? → **A:** LoRA on a 4-bit (NF4) quantized, frozen base — the base shrinks ~4× while full-precision adapters train through it. → [15.9](../weeks/15.9-qlora.md)

**Q:** What are NF4, double quantization, and paged optimizers? → **A:** 4-bit datatype optimal for normal-distributed weights; quantizing the quantization constants too; paging optimizer states GPU↔CPU to survive spikes.

**Q:** QLoRA's headline result? → **A:** Fine-tune a 65B on a single 48 GB GPU (7B on 24 GB) with ≈16-bit-LoRA quality.

---

## 15.10–15.13 · Stack, tuning, forgetting

**Q:** ⭐ What is QLoRA in code? → **A:** Transformers model + bitsandbytes 4-bit config + PEFT LoRA + TRL SFTTrainer. → [15.10](../weeks/15.10-practical-stack.md)

**Q:** Why use TRL's SFTTrainer over raw Trainer? → **A:** It handles chat-template rendering, completion-only loss masking, and sequence packing.

**Q:** ⭐ Which two hyperparameters most often ruin a fine-tune? → **A:** Learning rate (too high → forgetting/divergence) and epochs (too many → overfitting). → [15.11](../weeks/15.11-hyperparameters.md)

**Q:** What is effective batch size? → **A:** per-device batch × gradient accumulation × devices — what governs gradient stability.

**Q:** ⭐ Order to apply memory optimizations? → **A:** Mixed precision → LoRA/QLoRA → gradient checkpointing → accumulation → flash attention → distributed (last). → [15.12](../weeks/15.12-training-optimization.md)

**Q:** What does gradient checkpointing trade? → **A:** ~30% more compute (recomputing activations) for a large activation-memory reduction.

**Q:** ⭐ What is catastrophic forgetting? → **A:** Fine-tuning on a narrow task overwrites general capabilities the model learned in pretraining. → [15.13](../weeks/15.13-catastrophic-forgetting.md)

**Q:** ⭐ How do you detect it? → **A:** Evaluate on held-out *general* tasks (reasoning, instruction-following, safety), base vs tuned — not just your task.

**Q:** ⭐ Why does LoRA reduce forgetting? → **A:** The base weights are frozen, so general capability physically can't be overwritten; the adapter only adds behavior.

---

## 15.14–15.16 · Align

**Q:** ⭐ What are the four steps of RLHF? → **A:** Start from SFT → collect human preference comparisons → train a reward model → optimize the policy with RL (PPO). → [15.14](../weeks/15.14-rlhf.md)

**Q:** What does the reward model learn? → **A:** A scalar such that preferred (chosen) responses score higher than rejected (Bradley–Terry loss) — a differentiable preference proxy.

**Q:** ⭐ What does the KL penalty in PPO do? → **A:** Keeps the policy near the SFT model, preventing reward hacking (chasing the reward into degenerate nonsense).

**Q:** What is reward hacking? → **A:** The policy exploits a misspecified reward to get high scores with bad/degenerate/unsafe outputs.

**Q:** ⭐ What is DPO and why introduced? → **A:** Direct Preference Optimization: aligns to preferences with one supervised loss on (prompt, chosen, rejected) — no reward model, no RL — because RLHF is heavy and unstable. → [15.15](../weeks/15.15-dpo.md)

**Q:** ⭐ What role does the frozen reference play in DPO? → **A:** It's the anchor (RLHF's KL penalty baked into the loss); DPO measures log-prob shifts *relative to* the reference, keeping it stable.

**Q:** On which tokens are DPO log-probs computed? → **A:** Response tokens only (mask the prompt) — including the prompt is a common bug.

**Q:** ⭐ RLHF vs DPO? → **A:** Same data; DPO has no reward model/no RL, is stable and cheap (policy + frozen reference); RLHF is heavier with a potentially higher ceiling. Recipe: SFT → DPO.

**Q:** What does ORPO change vs SFT→DPO? → **A:** It folds preference alignment into the SFT stage (one odds-ratio loss), needing no separate stage and no reference. → [15.16](../weeks/15.16-other-alignment.md)

**Q:** What does KTO uniquely enable? → **A:** Learning from *unpaired* binary 👍/👎 feedback — no matched chosen/rejected pairs.

**Q:** What are Constitutional AI / RLAIF? → **A:** Alignment using AI-generated feedback (against written principles / from an AI judge) instead of human labels — scalable, but the judge's biases propagate.

---

## 15.17–15.18 · Evaluate

**Q:** ⭐ What are the axes of fine-tuned evaluation? → **A:** Task performance (accuracy/F1), generation quality (relevance/fluency/coherence/instruction-following), and safety (toxicity/bias/harm/leakage). → [15.17](../weeks/15.17-evaluation.md)

**Q:** ⭐ Why is safety a first-class axis? → **A:** Fine-tuning and alignment can both degrade it; it must be measured every time and gate deployment.

**Q:** The four evaluation methods and their blind spots? → **A:** Reference-based (needs gold; penalizes valid variety), reference-free (subjective), LLM-judge (position/verbosity/self bias), human (slow/costly).

**Q:** ⭐ Why is a fine-tuned model's absolute score meaningless alone? → **A:** Improvement is the delta vs the base on the same eval — 92% is good if base was 80%, bad if base was 93%. → [15.18](../weeks/15.18-base-vs-finetuned.md)

**Q:** ⭐ When should you ship a fine-tune? → **A:** Only when the delta is statistically significant, net-positive across axes, and free of regressions on protected behaviors (safety, general capability, leakage).

**Q:** Why evaluate both models on the same prompts (paired)? → **A:** It removes prompt-difficulty variance, giving more power to detect the delta.

---

## 15.19–15.22 · Debug, secure, ship

**Q:** ⭐ Where do most fine-tuning bugs live? → **A:** In the data or the format (template/masking), not the optimizer — read your data and the rendered input first. → [15.19](../weeks/15.19-debugging.md)

**Q:** Loss NaN — fix? → **A:** Lower LR, clip gradients, use bf16, add warmup.

**Q:** Model repeats/never stops — cause? → **A:** Missing EOS token in the labels.

**Q:** ⭐ Three checks that catch most bugs? → **A:** Print the rendered training example, confirm loss is masked to the response with EOS, and read 50 random examples.

**Q:** ⭐ Core fine-tuning-specific risk? → **A:** Training data becomes part of the weights — irreversibly — so it can be memorized/leaked and can't be selectively deleted. → [15.20](../weeks/15.20-security.md)

**Q:** What is the memorization triad? → **A:** Redact PII + deduplicate + keep epochs low.

**Q:** Why prefer RAG for sensitive data (security)? → **A:** Weights can't be selectively deleted; RAG keeps knowledge access-controlled, updatable, and deletable.

**Q:** What is dataset poisoning? → **A:** Injecting malicious training examples to install backdoors/harmful behavior, invisible until triggered; defend with provenance control + validation.

**Q:** ⭐ What does a production pipeline add over a training run? → **A:** Versioning (data+model), validation, evaluation + safety gating, a registry, deployment with rollback, monitoring, and retraining. → [15.21](../weeks/15.21-production-pipeline.md)

**Q:** ⭐ The two invariants of a production pipeline? → **A:** Full lineage (reproduce any model) and safe change (gate before ship, roll back after).

**Q:** How does rollback work for fine-tunes? → **A:** Re-point serving to the last-good registered version — fast, no retraining.

**Q:** ⭐ The one thing to remember from the module? → **A:** Fine-tuning changes behavior not knowledge, it's a data problem, memory is the constraint, and it isn't done until you've proven it's better (base vs tuned) and not worse (safety/forgetting). → [15.22](../weeks/15.22-projects-summary.md)

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 15](../README.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
| 📄 Cheat sheet | [Fine-tuning cheat sheet](../cheat-sheets/finetuning-cheatsheet.md) |
| 📝 Quiz | [Quiz 01](../quizzes/quiz-01.md) |
