# 📝 Module 16 · MLOps & LLMOps — Quiz 01

[🏠 Module 16](../README.md) · [📖 Lessons](../weeks/README.md) · [✅ Answers](answers-01.md)

> **48 questions across all 24 lessons.** Aim for an explanation, not just a phrase — the [answers](answers-01.md) grade reasoning. Target: **38/48** to consider the module solid.

---

## Part A · Foundations (16.1–16.5)

**1.** What problem does MLOps solve that classic DevOps doesn't? Why do AI systems "fail quietly"?

**2.** Why is MLOps *not* just "train model → deploy model"? Name the stages the naive view omits.

**3.** What are the three things you must version for reproducibility, and why is code alone insufficient?

**4.** Why is data a first-class versioned artifact? How does data versioning differ from code versioning?

**5.** What does experiment tracking capture, and why is it the prerequisite for a defensible model choice?

**6.** What is a model registry, and what does *gated promotion* buy you over deploying from a training run?

**7.** Why must rollback be instant, and how does the registry make it so?

## Part B · Build & ship (16.6–16.8, 16.13)

**8.** What does an ML pipeline give you over a training script? Name three orchestrators.

**9.** How does CI/CD for AI differ from CI/CD for software? What do you test besides code?

**10.** What is an eval gate, and where does it sit in the pipeline?

**11.** Compare batch, online, and async serving. When is each correct?

**12.** Name the serving stacks for classic models vs. LLMs, and why LLMs need different ones.

**13.** Compare blue-green, canary, rolling, and shadow deployment. When do you use shadow?

## Part C · LLMOps (16.9, 16.12, 16.14)

**14.** What does LLMOps add on top of MLOps? Name the new artifacts it versions.

**15.** Why must you pin the LLM's model version, and what breaks if you don't?

**16.** How do you version a prompt, a RAG config, and an agent definition?

**17.** Why can't you evaluate an LLM with accuracy alone? What axes replace it?

**18.** What is an LLM-as-judge, and how do you keep it trustworthy?

**19.** Explain quantization, distillation, and pruning as optimization levers.

**20.** What are KV cache, continuous batching, and speculative decoding, and what does each speed up?

## Part D · Operate (16.10–16.11, 16.17–16.19)

**21.** What are the three pillars of observability? What must you additionally track for LLMs?

**22.** Why is tracing especially important for RAG and agent systems?

**23.** Distinguish data drift, concept drift, and model drift. Give an example of each.

**24.** What do the KS test and PSI measure, and how do they trigger action?

**25.** Describe the detect → evaluate → retrain loop. Why not retrain on every drift signal?

**26.** Name four reliability patterns and what failure each prevents.

**27.** What is graceful degradation for an AI system? Give a concrete example.

**28.** How do you attribute cost per request / user / model / workflow, and why bother?

**29.** What are the biggest LLM cost levers, and how do you cut cost without losing quality?

**30.** Why does AI security need *two* layers? Name a threat unique to the AI layer.

**31.** How do least privilege and defense-in-depth apply to an agent with tools?

## Part E · Infrastructure (16.15–16.16, 16.21–16.22)

**32.** How do you estimate the VRAM needed to serve (or train) a model?

**33.** What is the "fit ladder" for making a model fit on available GPUs?

**34.** Map pods, deployments, services, and jobs to what they do in a K8s ML system.

**35.** How does Kubernetes schedule GPUs and autoscale AI workloads?

**36.** Why version-control infrastructure? How do Docker, Terraform, Kubernetes, and Helm layer?

**37.** Why is IaC especially valuable for AI/GPU infrastructure?

**38.** What do the cloud MLOps platforms (SageMaker/Vertex/Azure ML) actually provide?

**39.** State the managed vs. self-hosted trade-off and how to avoid lock-in.

## Part F · Architecture & synthesis (16.20, 16.23–16.24)

**40.** What skeleton do ML, LLM, and agent production architectures share?

**41.** Where do the three architectures diverge, and why?

**42.** Walk through the traditional ML capstone as a closed loop, stage by stage.

**43.** Walk through the LLM application capstone, and say how it differs from the ML one.

**44.** How does each capstone *close its loop*, and why is the loop the whole point?

**45.** Why build mini projects before the capstones?

**46.** For "model suddenly inaccurate," what is your first diagnostic question and why?

**47.** For an unexpected LLM cost spike, how do you localize and stop it?

**48.** State the single most important idea of Module 16 in one sentence and defend it.

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 16](../README.md) |
| ✅ Answers | [answers-01.md](answers-01.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
