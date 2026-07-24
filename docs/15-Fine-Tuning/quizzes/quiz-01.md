# 📝 Module 15 · Fine-Tuning & Alignment — Quiz 01

[🏠 Module 15](../README.md) · [📖 Lessons](../weeks/README.md) · [✅ Answers](answers-01.md)

> **44 questions across all 22 lessons.** Aim for an explanation, not just a phrase — the [answers](answers-01.md) grade reasoning. Target: **35/44** to consider the module solid.

---

## Part A · Decide (15.1–15.3)

**1.** What does fine-tuning change, and what does it *not* change well?

**2.** Give the decision framework for prompt vs RAG vs fine-tune vs pretrain.

**3.** Why is injecting factual knowledge via fine-tuning a mistake?

**4.** Distinguish base, instruct, and chat models. How does each respond to a question?

**5.** When do you fine-tune from a base model vs an instruct model, and why must data match the chat template?

**6.** Compare the six adaptation options (prompt/RAG/LoRA/QLoRA/full/continued-pretrain). What's the default and why?

**7.** How do dataset size, GPU memory, and privacy drive the strategy choice?

## Part B · Data (15.4–15.5)

**8.** Why is data quality more important than quantity in fine-tuning?

**9.** What is data leakage, how does it happen, and how do you prevent it?

**10.** Why must deduplication happen before splitting, and what's a group-aware split?

**11.** Compare the alpaca and messages instruction formats. When do you use each?

**12.** Why must the training format match the model's chat template exactly?

## Part C · Train (15.6–15.13)

**13.** What is SFT, and how does it relate to pretraining?

**14.** Explain loss masking and why it's essential for instruction tuning.

**15.** Break down full-FT memory per parameter. Why is it ~16 bytes, not 2?

**16.** Explain LoRA: the equation, what's frozen, what's trained, and why `B` inits to zero.

**17.** Where does LoRA's memory saving come from, and why does low rank usually suffice?

**18.** What is QLoRA? Explain NF4, double quantization, and paged optimizers.

**19.** Why can the base be 4-bit while adapters stay full precision?

**20.** Name the five core libraries and how PEFT + bitsandbytes form QLoRA.

**21.** Which two hyperparameters most often ruin a fine-tune, and how?

**22.** In what order do you apply memory optimizations to fit a run?

**23.** What is catastrophic forgetting, how do you detect it, and why does LoRA reduce it?

## Part D · Align (15.14–15.16)

**24.** Walk through the RLHF pipeline end to end.

**25.** How is a reward model trained, and what does the KL penalty in PPO do?

**26.** What is reward hacking, and how do you mitigate it?

**27.** What is DPO, and why was it introduced?

**28.** Explain the DPO loss and the role of the frozen reference model.

**29.** On which tokens are DPO log-probabilities computed, and why?

**30.** Compare RLHF and DPO on complexity, stability, and infrastructure.

**31.** What do ORPO and KTO each change relative to DPO?

## Part E · Evaluate & ship (15.17–15.21)

**32.** What are the axes of evaluating a fine-tuned model, and why separate them?

**33.** Why is safety a first-class evaluation axis after fine-tuning/alignment?

**34.** Compare reference-based, reference-free, LLM-judge, and human evaluation.

**35.** Why is a fine-tuned model's absolute score meaningless in isolation?

**36.** When should you ship a fine-tune? What are protected regressions?

**37.** Why must base and tuned be evaluated on identical, paired data with significance testing?

**38.** Where do most fine-tuning bugs live, and what are your first three checks?

**39.** Map three symptoms (flat loss, NaN, repetition) to causes and fixes.

**40.** Why does fine-tuning create privacy risks that prompting/RAG don't?

**41.** What is the memorization triad, and why prefer RAG for sensitive data?

**42.** What is dataset poisoning, and how do you defend against it?

## Part F · Synthesis (15.22)

**43.** Design an end-to-end production fine-tuning pipeline (Project 8). What two invariants must it guarantee?

**44.** Defend "fine-tuning changes behavior, not knowledge," and state when a fine-tune is "done."

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 15](../README.md) |
| ✅ Answers | [answers-01.md](answers-01.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
