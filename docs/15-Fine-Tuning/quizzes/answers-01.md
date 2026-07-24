# ✅ Module 15 · Fine-Tuning & Alignment — Quiz 01 Answers

[🏠 Module 15](../README.md) · [📝 Quiz](quiz-01.md) · [📖 Lessons](../weeks/README.md)

> Model answers grade **reasoning**. Full credit = the key idea explained, not just a keyword.

---

## Part A · Decide

**1.** It changes **behavior, style, format, skill, and domain conventions** — *how* the model acts — by adjusting the weights. It does **not** reliably install **factual knowledge** (that comes out fuzzy/hallucinated) — facts belong in RAG. → [15.1](../weeks/15.1-why-fine-tuning.md)

**2.** **Missing knowledge (fresh/private/changing) → RAG; framing/one-off → prompt; behavior/style/skill prompting can't produce → fine-tune; broad new capability from scratch → pretraining.** Order of preference: prompt → RAG → fine-tune (last resort); they compose. → [15.1](../weeks/15.1-why-fine-tuning.md)

**3.** The model learns facts **fuzzily** — it paraphrases/misremembers/hallucinates them, can't cite sources, and can't be updated without retraining; and it risks **memorizing/leaking** them. RAG keeps facts fresh, citable, updatable, and access-controlled. → [15.1](../weeks/15.1-why-fine-tuning.md)

**4.** **Base** completes text (prompt it a question and it may continue with more questions); **instruct** follows single-turn instructions (after SFT); **chat** is aligned for multi-turn dialogue and ships with a **chat template**. → [15.2](../weeks/15.2-base-models.md)

**5.** **From base** for heavy domain/behavior changes with lots of data (full control, no inherited style); **from instruct/chat** for style/skill/format with limited data (instruction-following pre-installed). Data must use the model's **exact chat template** because the model trains on the rendered string — a mismatch means it sees unfamiliar input at inference. → [15.2](../weeks/15.2-base-models.md)

**6.** Prompt (nothing trained) < RAG (nothing) < **LoRA/QLoRA** (~0.1–1% params) < full FT (all) < continued pretraining (all, big corpus). **LoRA is the default** — full-FT quality on most tasks at a fraction of memory/cost, plus swappable adapters; QLoRA when memory-bound. → [15.3](../weeks/15.3-strategy-selection.md)

**7.** **Dataset size**: tiny → prompt/RAG/light-LoRA; huge unlabeled → continued pretraining. **GPU**: limited → QLoRA; ample → LoRA/full. **Privacy**: sensitive → self-hosted open model + LoRA/QLoRA (not a hosted FT API). → [15.3](../weeks/15.3-strategy-selection.md)

## Part B · Data

**8.** The model **mirrors its data** — errors, quirks, inconsistencies are all learned and amplified; a small, clean, diverse set outperforms a large noisy one (which teaches the model its own noise). Fine-tuning is ~80% data engineering. → [15.4](../weeks/15.4-dataset-preparation.md)

**9.** A **test example (or paraphrase/same-source item) also in training** → the model has effectively seen the answer → inflated eval, disappointing production. Prevent by **deduplicating (exact + near) before splitting**, **group-splitting** by document/user, and treating the **test set as sacred**. → [15.4](../weeks/15.4-dataset-preparation.md)

**10.** Because near-duplicates can otherwise land on both sides of the split (leakage); deduping first ensures splits are disjoint. A **group-aware split** keeps all items from the same source (document/user/entity) in the same split, preventing same-source leakage. → [15.4](../weeks/15.4-dataset-preparation.md)

**11.** **Alpaca** `{instruction, input, output}` is a convenient single-turn source; **messages** `{messages:[{role,content}]}` is native for chat models and multi-turn. Use messages for chat/multi-turn; alpaca as a source you convert into the template anyway. → [15.5](../weeks/15.5-instruction-datasets.md)

**12.** The model trains on the **rendered chat-template string** (special tokens, roles); if inference input differs, the model sees a shape it never trained on and behaves badly — use `apply_chat_template`, never hand-concatenation. → [15.5](../weeks/15.5-instruction-datasets.md)

## Part C · Train

**13.** SFT is the **same next-token cross-entropy objective as pretraining**, applied to curated **instruction→response** data — same math, narrower distribution, reshaping behavior toward answering as your data does. → [15.6](../weeks/15.6-sft.md)

**14.** Computing the loss **only on response tokens** (prompt-position labels = `-100`), so gradients reward predicting the *answer*, not reproducing the *prompt*. Without it the model wastes capacity parroting instructions. Keep **EOS** in labels so it learns to stop. → [15.6](../weeks/15.6-sft.md)

**15.** Per parameter you store, in mixed precision: **fp16 weight (2) + fp16 grad (2) + fp32 master weight (4) + Adam momentum (4) + Adam variance (4) ≈ 16 bytes** — not just the 2-byte weight. So a 7B needs ~112 GB for weights+grad+optimizer. → [15.7](../weeks/15.7-full-fine-tuning.md)

**16.** `W' = W + BA`: freeze pretrained `W`; train `B (d×r)` and `A (r×k)` with small rank `r`; forward is `Wx + (α/r)BAx`. **`B` inits to zero** so `BA=0` at start (`W'=W`), meaning training begins exactly at the pretrained model and adds to it — stable. → [15.8](../weeks/15.8-lora.md)

**17.** From **freezing `W`**: it has no gradient or optimizer state, so the ~16 bytes/param cost applies only to the tiny `B,A` (<1% of params). Low rank suffices because the fine-tuning update `ΔW` has **low intrinsic rank** — a rank-`r` `BA` captures most of the behavior change. → [15.8](../weeks/15.8-lora.md)

**18.** **QLoRA** = LoRA on a **4-bit (NF4) quantized, frozen base**. **NF4**: a 4-bit datatype with levels placed by the quantiles of a normal distribution (optimal for pretrained weights). **Double quantization**: quantizing the quantization constants too (extra saving). **Paged optimizers**: paging optimizer states GPU↔CPU to survive memory spikes. → [15.9](../weeks/15.9-qlora.md)

**19.** The base is **frozen** (never receives gradient updates), so lower precision is fine — you de-quantize it on the fly to compute `Wx`; the **full-precision adapters** train through it and **compensate** for the fixed quantization error, recovering 16-bit performance. → [15.9](../weeks/15.9-qlora.md)

**20.** **Transformers** (model/tokenizer/Trainer), **Datasets** (data), **PEFT** (LoRA adapters), **TRL** (SFT/DPO trainers), **bitsandbytes** (4-bit + paged optimizers). QLoRA = Transformers model + **bitsandbytes 4-bit** + **PEFT LoRA** + TRL SFTTrainer. → [15.10](../weeks/15.10-practical-stack.md)

**21.** **Learning rate** (too high → forgetting/divergence/NaN) and **epochs** (too many on small data → overfitting/memorization). LoRA tolerates higher LR since only adapters move; set epochs by early-stopping on validation loss. → [15.11](../weeks/15.11-hyperparameters.md)

**22.** **Mixed precision (always) → LoRA/QLoRA (biggest win) → gradient checkpointing → gradient accumulation → flash attention → distributed (last).** Each attacks a specific memory term; add complexity only as needed. → [15.12](../weeks/15.12-training-optimization.md)

**23.** Fine-tuning on a narrow task **overwrites general capabilities** (shared weights; the objective only rewards your task). **Detect** by evaluating on held-out *general* tasks (reasoning, instruction-following, **safety**), base vs tuned. **LoRA reduces it** because the base weights are frozen — general capability physically can't be overwritten. → [15.13](../weeks/15.13-catastrophic-forgetting.md)

## Part D · Align

**24.** Start from an **SFT model** → collect **human preference comparisons** (chosen ≻ rejected) → train a **reward model** to predict them → optimize the policy with **RL (PPO)** to maximize reward while staying close to SFT (KL penalty) → aligned model. → [15.14](../weeks/15.14-rlhf.md)

**25.** The reward model (SFT backbone + scalar head) is trained with the **Bradley–Terry** loss `−log σ(r_chosen − r_rejected)` so preferred responses score higher. The **KL penalty** `β·KL(π‖π_SFT)` anchors the policy to the SFT model, **preventing reward hacking** (degenerate high-reward nonsense). → [15.14](../weeks/15.14-rlhf.md)

**26.** The policy **exploits a misspecified reward model** to get high scores with degenerate/wrong/unsafe outputs. Mitigate with a **KL penalty** (stay near SFT), a better/diverse reward model, and **red-teaming the aligned model** rather than trusting reward scores. → [15.14](../weeks/15.14-rlhf.md)

**27.** **Direct Preference Optimization** aligns to preferences using **one supervised loss** on (prompt, chosen, rejected) triples — **no reward model, no RL**. Introduced because RLHF's reward-model + PPO pipeline (four models, unstable, expensive) is impractical for most teams. → [15.15](../weeks/15.15-dpo.md)

**28.** `−log σ(β·[(log π_θ/π_ref)_chosen − (log π_θ/π_ref)_rejected])`: it increases the **chosen** and decreases the **rejected** log-prob **relative to a frozen reference**, maximizing the margin. The **reference model is the anchor** (RLHF's KL penalty baked in), which makes DPO stable — measuring shifts relative to `π_ref` prevents collapse to degenerate text. → [15.15](../weeks/15.15-dpo.md)

**29.** The **response tokens only** (mask the prompt). Including prompt tokens is a common bug — you want the probability the model assigns to the *response*, not the prompt. → [15.15](../weeks/15.15-dpo.md)

**30.** RLHF: reward model + PPO (RL loop), **four models**, unstable (reward hacking, KL tuning), heavy infra — potentially higher ceiling. DPO: **no reward model, no RL**, just policy + frozen reference, **stable**, light (like SFT), **same data**. Recipe for most: **SFT → DPO**. → [15.15](../weeks/15.15-dpo.md)

**31.** **ORPO** folds preference alignment into the SFT stage as one odds-ratio loss — **no separate stage, no reference model**. **KTO** learns from **unpaired** binary 👍/👎 feedback — **no matched chosen/rejected pairs** required. → [15.16](../weeks/15.16-other-alignment.md)

## Part E · Evaluate & ship

**32.** **Task performance** (accuracy/precision/recall/F1), **generation quality** (relevance/fluency/coherence/instruction-following), and **safety** (toxicity/bias/harm/leakage). Separated because a model can ace one while failing another; a blended score hides it. → [15.17](../weeks/15.17-evaluation.md)

**33.** Because **fine-tuning and alignment can both degrade safety** — unsafe/insufficient data, catastrophic forgetting, or alignment to compliant-but-harmful preferences. It must be measured every run (base vs tuned) and **gate deployment**. → [15.17](../weeks/15.17-evaluation.md)

**34.** **Reference-based** (objective, cheap; needs gold, penalizes valid variety), **reference-free** (no gold; subjective), **LLM-judge** (scalable; position/verbosity/self bias — calibrate), **human** (gold standard; slow/costly/inconsistent). **Triangulate** — none is trustworthy alone. → [15.17](../weeks/15.17-evaluation.md)

**35.** Improvement is the **delta vs the base on the same eval**, not the absolute number — 92% is great if base was 80%, a regression if base was 93%. → [15.18](../weeks/15.18-base-vs-finetuned.md)

**36.** Ship only when the delta is **statistically significant**, **net-positive across all axes**, and **free of regressions on protected behaviors**. **Protected regressions** = safety, general capability (forgetting), and privacy leakage — a task win that regresses these is not shippable. → [15.18](../weeks/15.18-base-vs-finetuned.md)

**37.** **Identical eval set** prevents apples-to-oranges; **paired** (same prompts through both) removes prompt-difficulty variance for more statistical power; **significance testing** (paired test/bootstrap CI) distinguishes a real delta from noise (a small delta on few examples is likely noise). → [15.18](../weeks/15.18-base-vs-finetuned.md)

**38.** Most bugs live in the **data or format** (template/masking), not the optimizer. First three checks: **(1) print the rendered/tokenized training example**, **(2) confirm loss is masked to the response with EOS**, **(3) read 50 random data examples**. → [15.19](../weeks/15.19-debugging.md)

**39.** **Flat loss** → LR too low / broken masking / no trainable params → ↑LR, check masking, verify adapters train. **NaN** → LR too high/overflow → ↓LR, clip grads, bf16, warmup. **Repetition** → missing EOS in labels → add EOS (also fewer epochs). → [15.19](../weeks/15.19-debugging.md)

**40.** Fine-tuning **fuses training data into the weights** — the model can **memorize and leak** PII, the data **can't be selectively deleted** (retrain to remove), and it can be **poisoned**; a prompted/RAG model keeps data external, access-controlled, and deletable. → [15.20](../weeks/15.20-security.md)

**41.** The **memorization triad** = **redact PII + deduplicate + keep epochs low** (memorization scales with duplication × epochs). Prefer RAG for sensitive data because **weights can't be selectively deleted** (right-to-be-forgotten needs retraining), while RAG is access-controlled, updatable, and deletable. → [15.20](../weeks/15.20-security.md)

**42.** Injecting **malicious training examples** to install backdoors or biased/harmful behavior, invisible until triggered. Defend with **provenance control** (who can add data), **data validation + anomaly detection**, and retraining from clean data. → [15.20](../weeks/15.20-security.md)

## Part F · Synthesis

**43.** **Versioned data → validation (schema/PII/leakage/quality) → tracked training (config+code+data-hash) → evaluation (task+generation+safety) → safety gate → model registry (versioned artifact + lineage + stage) → deployment (canary/A-B) → monitoring (quality/drift/safety) → drift-triggered retraining.** The **two invariants**: **full lineage** (reproduce any model from data+config+code+base) and **safe change** (evaluate/gate before ship, roll back instantly after). → [15.21](../weeks/15.21-production-pipeline.md)

**44.** Fine-tuning continues gradient descent on a **small, task-specific distribution**, making a *short* move that reshapes **behavior** cheaply — but that same smallness can't reliably install large new **factual knowledge** (facts → RAG). A fine-tune is **"done"** only when you've proven it's **better** (significant, net-positive vs base on identical eval) **and not worse** (no safety/forgetting/leakage regression). → [15.22](../weeks/15.22-projects-summary.md)

---

## Scoring

| Score | Verdict |
|---|---|
| 40–44 | Excellent — you can decide, build, align, evaluate, secure, and deploy fine-tunes. |
| 35–39 | Solid — review the missed lessons. |
| 26–34 | Partial — re-read 15.1, 15.6, 15.8, 15.15, 15.17 (the load-bearing five). |
| < 26 | Re-study the module; redo ⭐ exercises E5/E6, E8, E9, E15, E16, E19. |

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 15](../README.md) |
| 📝 Quiz | [quiz-01.md](quiz-01.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
