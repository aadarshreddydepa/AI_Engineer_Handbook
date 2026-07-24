# 📄 Fine-Tuning & Alignment — Cheat Sheet

[🏠 Module 15](../README.md) · [📖 Lessons](../weeks/README.md)

---

## 🧠 The core facts

| | |
|---|---|
| **⭐ What FT changes** | behavior / style / format / skill — **not knowledge** |
| **Facts → RAG** | fresh/private/changing knowledge, citable, updatable |
| **Framing → prompt** · **Behavior → fine-tune** | |
| **⭐ FT is a data problem** | the model mirrors its data; quality > quantity |
| **⭐ Memory is the constraint** | LoRA/QLoRA exist because full FT is huge |
| **⭐ Always** | compare base vs tuned (significant, net-positive, safe) |

---

## 🧭 Decide (15.1–15.3)

- **Order:** prompt → RAG → LoRA → QLoRA → full FT → continued pretraining (climb only as needed).
- **Base / instruct / chat:** completes text / follows instructions / multi-turn + chat template.
- **From base** = max control, more data; **from instruct/chat** = less data (common).
- **⭐ Match the chat template** (`apply_chat_template`) — top "trained-but-wrong" cause.
- **Privacy** often decides: sensitive → self-host open model + LoRA/QLoRA.

---

## 🗂️ Data (15.4–15.5)

- **Pipeline:** collect → clean → **dedup (exact+near)** → filter → **PII-redact** → validate → **split (no leakage)**.
- **⭐ Leakage:** dedup before splitting; group-split; test set sacred.
- **Formats:** alpaca `{instruction,input,output}` · `messages` (chat/multi-turn).
- Diversity + edge/refusal examples; consistent output format.

---

## 🎓 SFT (15.6)

- Same **next-token cross-entropy** as pretraining, on instruction→response data.
- **⭐ Loss masking:** loss on **response tokens only** (prompt labels = `-100`) → answer, don't parrot.
- Keep **EOS** in labels (learns to stop); small **LR** (1e-5–2e-4); **1–3 epochs**.

---

## 💾 Full FT vs LoRA vs QLoRA (15.7–15.9)

| | Full FT | LoRA | QLoRA |
|---|---|---|---|
| Trains | 100% | ~0.1–1% | ~0.1–1% |
| Base | 16-bit | 16-bit | **4-bit NF4** |
| 7B memory | ~112 GB | ~15–20 GB | **~6–10 GB** |
| Hardware | multi-GPU | 1 big GPU | **1 consumer GPU** |

- **Full-FT memory ≈ 16 bytes/param** (fp16 weight 2 + grad 2 + fp32 master 4 + Adam m 4 + v 4).
- **⭐ LoRA:** freeze `W`, learn `ΔW = BA`; forward `Wx + (α/r)BAx`; `B=0` init; rank 8–16, α≈2r; targets = attention (+MLP).
- **⭐ QLoRA:** LoRA on a **4-bit NF4 + double-quant** frozen base + **paged optimizer** → 65B on one 48 GB GPU.

---

## 🛠️ Stack, HParams, Optimization (15.10–15.12)

- **Stack:** Transformers (model) · Datasets (data) · **PEFT** (LoRA) · **TRL** (SFT/DPO trainers) · **bitsandbytes** (4-bit). QLoRA = all four.
- **Dangerous knobs:** **LR** (too high → forget/NaN) · **epochs** (too many → overfit). Effective batch = batch × accum × devices.
- **Fit-it order:** mixed precision → LoRA/QLoRA → gradient checkpointing → accumulation → flash attention → distributed (last).

---

## 🧟 Catastrophic forgetting (15.13)

- FT can **overwrite general capability** (shared weights; objective only rewards your task).
- **⭐ Detect** on a **retention set** (general + **safety**), base vs tuned.
- **Reduce:** lower LR/epochs · diversity/replay · **LoRA (frozen base can't be overwritten)**.

---

## 🎯 Alignment (15.14–15.16)

- **RLHF:** SFT → preference data → **reward model** (Bradley–Terry) → **PPO** (`E[r] − β·KL(π‖SFT)`). KL prevents **reward hacking**. Heavy (4 models).
- **⭐ DPO:** same data, **no reward model, no RL** — loss `−log σ(β·[(logπ/π_ref)_chosen − (logπ/π_ref)_rejected])`, response-only log-probs, **frozen reference** = the anchor. **SFT → DPO** is the default.
- **Others:** Constitutional AI / RLAIF (AI feedback) · ORPO (align in SFT, no reference) · KTO (unpaired 👍/👎) · reward-model reranking (no training).

---

## 📊 Evaluate & compare (15.17–15.18)

- **Axes:** task (F1) · generation (relevance/fluency/IF) · **safety** (toxicity/bias/**leakage**).
- **Methods:** reference-based · reference-free · **LLM-judge (calibrate)** · human. **Triangulate.**
- **⭐ Ship if:** delta is **significant** (paired test/bootstrap) **AND net-positive AND** no regression on **protected** behaviors (safety, general capability, leakage).

---

## 🐛 Debug (15.19)

| Symptom | Fix |
|---|---|
| Loss flat | ↑ LR · check masking · trainable params · data |
| Loss NaN | ↓ LR · clip grads · bf16 · warmup |
| Repeats | add EOS · fewer epochs |
| Less capable | forgetting → LoRA · ↓ LR · replay |
| Ignores instructions | fix chat template · right checkpoint |

**⭐ First 3 checks:** render the input · confirm masking+EOS · read 50 examples.

---

## 🔒 Security (15.20)

- Weights **fuse the data** → **memorization/leakage** (redact + **dedup** + low epochs), **can't delete** (prefer RAG), **poisoning** (provenance + validation), **extraction/membership** (rate-limit + DP).

---

## 🚀 Production (15.21)

- **Pipeline:** version data → validate → train (tracked) → eval → **safety gate** → registry (lineage) → deploy (canary) → monitor → retrain.
- **⭐ Two invariants:** full **lineage** (reproduce any model) + **safe change** (gate + **rollback**). LoRA adapters = cheap versioned artifacts.

---

## 🎯 The 10 through-lines

1. Behavior not knowledge (facts → RAG). 2. Last resort — prompt → RAG → FT. 3. Data quality > quantity. 4. Memory is the constraint. 5. LoRA is the default (`W'=W+BA`). 6. DPO ≈ RLHF, far simpler (SFT→DPO). 7. FT can make it worse (forgetting). 8. Always compare base vs tuned. 9. Weights fuse the data (leakage/poisoning). 10. Production = lineage + safe change.

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 15](../README.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
| 🏋️ Exercises | [Exercises](../exercises/README.md) |
| 🎴 Flashcards | [Deck](../flashcards/deck.md) |
