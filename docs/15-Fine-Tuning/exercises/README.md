# 🏋️ Module 15 · Fine-Tuning & Alignment — Exercises

[🏠 Module 15](../README.md) · [📖 Lessons](../weeks/README.md) · [🧩 Projects](../projects/)

> Build-it exercises, ordered along the module's spine: **decide → data → train → align → evaluate → ship**. If you do only six, do ⭐ **E5, E8, E9, E13, E16, E19** — SFT from scratch, a LoRA layer, QLoRA on one GPU, a DPO objective, the evaluation framework, and the production pipeline. Together they are the module. The prompt asks for a mix of conceptual, mathematical, dataset-design, config, GPU-memory-estimation, evaluation, and debugging exercises — tagged below.

---

## Tier 1 · Decide & data (15.1–15.5)

### E1 · Adapt-or-not (conceptual)
**Goal:** classify 10 scenarios as prompt / RAG / fine-tune / pretrain and justify.
**Done-when:** each choice is defended by "knowledge vs behavior" and cost; you can name a case where fine-tuning facts fails. → [15.1](../weeks/15.1-why-fine-tuning.md)

### E2 · Checkpoint & template (conceptual)
**Goal:** contrast base vs instruct vs chat responses; print a chat template and format an example correctly/incorrectly.
**Done-when:** you show base "completes" vs instruct "answers", and a rendered example matches `apply_chat_template`. → [15.2](../weeks/15.2-base-models.md)

### E3 · Strategy + memory (GPU estimation)
**Goal:** for 8 constraint sets (data/GPU/privacy/latency), pick a strategy and estimate GPU memory for full FT vs LoRA vs QLoRA of a 7B.
**Done-when:** limited-GPU → QLoRA; private → self-host; memory estimates match the ~16 bytes/param and 4-bit rules. → [15.3](../weeks/15.3-strategy-selection.md)

### E4 · Leak-free data pipeline (dataset design)
**Goal:** build collect → clean → dedup (exact+near) → filter → PII-redact → group-split.
**Constraints:** no train/test overlap incl. near-dupes/same-source.
**Done-when:** (1) zero leakage proven; (2) PII removed; (3) a quality>quantity comparison (2k clean vs 20k noisy) shows the clean set wins. → [15.4](../weeks/15.4-dataset-preparation.md)

### E5 · Instruction formatting (dataset design)
**Goal:** convert tasks into alpaca + messages formats; render both with a real chat template; add edge/refusal examples.
**Done-when:** rendered training string == inference input (minus generation prompt); output format consistent. → [15.5](../weeks/15.5-instruction-datasets.md)

## Tier 2 · Train (15.6–15.13)

### ⭐ E6 · SFT from scratch (implementation)
**Goal:** implement the masked cross-entropy SFT loop with prompt masking + EOS.
**Done-when:** (1) masked vs unmasked → answering vs parroting; (2) omitting EOS → no stopping; (3) loss decreases and the model answers. → [15.6](../weeks/15.6-sft.md)

### E7 · Full-FT memory math (GPU estimation)
**Goal:** compute full-FT memory for 1B/7B/13B; split a 7B's ~112 GB into weights/grad/optimizer.
**Done-when:** you show the optimizer dominates and identify the minimum GPU setup for each. → [15.7](../weeks/15.7-full-fine-tuning.md)

### ⭐ E8 · LoRA layer (implementation + math)
**Goal:** implement `LoRALinear`; verify `ΔW=0` at init and only `A,B` trainable; sweep rank.
**Done-when:** (1) trainable params <1–2%; (2) merge preserves outputs with zero latency; (3) a rank sweep shows the quality/params knee. → [15.8](../weeks/15.8-lora.md)

### ⭐ E9 · QLoRA on one GPU (config + GPU)
**Goal:** load a model in 4-bit NF4 + double-quant, add LoRA, train with a paged optimizer.
**Done-when:** a model that didn't fit in fp16 trains within the target VRAM; NF4 in use; quality ≈ 16-bit LoRA. → [15.9](../weeks/15.9-qlora.md)

### E10 · Pipeline from the stack (config)
**Goal:** build the QLoRA SFT pipeline from Transformers + Datasets + PEFT + TRL + bitsandbytes.
**Done-when:** produces a saved adapter; base+adapter and merged give identical outputs; each line mapped to a concept. → [15.10](../weeks/15.10-practical-stack.md)

### E11 · Hyperparameter sweeps (config)
**Goal:** sweep LR and epochs with early stopping; achieve a target effective batch via accumulation.
**Done-when:** you locate LR divergence/under-stepping and the overfitting epoch; effective-batch math verified. → [15.11](../weeks/15.11-hyperparameters.md)

### E12 · Fit-it ladder (GPU estimation)
**Goal:** take a model that OOMs and apply optimizations in order until it fits; attribute each reduction.
**Done-when:** the run fits after mixed-precision → LoRA/QLoRA → checkpointing → accumulation; each lever's effect measured. → [15.12](../weeks/15.12-training-optimization.md)

### E13 · Forgetting detector (evaluation)
**Goal:** induce catastrophic forgetting; build a retention set (general + safety); compare LoRA vs full FT.
**Done-when:** forgetting is quantified on the retention set; LoRA forgets less; a safety regression is flagged. → [15.13](../weeks/15.13-catastrophic-forgetting.md)

## Tier 3 · Align (15.14–15.16)

### E14 · Reward model (implementation + math)
**Goal:** train a reward model with the Bradley–Terry loss on preference triples.
**Done-when:** preference accuracy > chance on held-out pairs; you can explain the KL penalty's role in PPO. → [15.14](../weeks/15.14-rlhf.md)

### ⭐ E15 · DPO objective (implementation + math)
**Goal:** implement `dpo_loss` + response-masked `sequence_logprob`; train with a frozen reference.
**Done-when:** (1) chosen implicit reward rises above rejected; (2) whole-sequence (unmasked) log-probs fail; (3) win-rate > 50% vs the SFT start. → [15.15](../weeks/15.15-dpo.md)

### E16b · Alignment selector (conceptual)
**Goal:** map 5 data situations (pairs / thumbs / no-human-labels / principles / no-train) to the right method.
**Done-when:** each choice (DPO/ORPO/KTO/RLAIF/CAI/rerank) is justified by data shape + infra. → [15.16](../weeks/15.16-other-alignment.md)

## Tier 4 · Evaluate & ship (15.17–15.21)

### ⭐ E16 · Evaluation framework (evaluation)
**Goal:** score a model on task/generation/safety with calibrated LLM-judge; include leakage + edge cases.
**Done-when:** a model strong on one axis but weak on another is found; judge calibrated vs humans; safety gate present. → [15.17](../weeks/15.17-evaluation.md)

### E17 · Base-vs-tuned significance (evaluation + math)
**Goal:** paired base-vs-candidate comparison with bootstrap CIs; a regression golden set.
**Done-when:** an insignificant delta is not shipped; a safety regression blocks the ship; paired design beats unpaired power. → [15.18](../weeks/15.18-base-vs-finetuned.md)

### E18 · Debugging drills (debugging)
**Goal:** plant each failure (no masking, no EOS, high LR→NaN, over-epoch, wrong template) and apply the mapped fix.
**Done-when:** every symptom is diagnosed and resolved; the first three checks (render input, masking+EOS, read data) catch most. → [15.19](../weeks/15.19-debugging.md)

### E19b · Secure fine-tune (debugging + security)
**Goal:** demonstrate memorization leakage then reduce it; detect a planted poisoned example.
**Done-when:** a duplicated string leaks verbatim, then dedup+low-epochs+redaction stops it; poisoning flagged via provenance. → [15.20](../weeks/15.20-security.md)

### ⭐ E19 · Production pipeline (architecture)
**Goal:** build versioned-data → validate → tracked-train → eval+safety-gate → registry → deploy → rollback.
**Done-when:** any model reproducible from lineage; a regressing/unsafe candidate blocked; rollback restores last-good. → [15.21](../weeks/15.21-production-pipeline.md)

## Capstone

### ⭐ E20 · Base vs SFT vs LoRA vs DPO, productionized (Project 8)
**Goal:** the flagship — versioned data, tracked QLoRA SFT, a DPO stage, base-vs-all evaluation with safety gating + significance, registry with lineage, canary deploy with rollback, drift-triggered retrain.
**Done-when:** a defensible verdict that the shipped model is significantly better than base with no safety/forgetting regression; reproducible lineage; demonstrated rollback. → [15.22](../weeks/15.22-projects-summary.md)

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 15](../README.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
| 📝 Quiz | [Quiz 01](../quizzes/quiz-01.md) |
| 🎴 Flashcards | [Deck](../flashcards/deck.md) |
| 📄 Cheat sheet | [Fine-tuning cheat sheet](../cheat-sheets/finetuning-cheatsheet.md) |
