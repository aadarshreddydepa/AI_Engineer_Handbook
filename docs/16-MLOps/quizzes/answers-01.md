# ✅ Module 16 · MLOps & LLMOps — Quiz 01 Answers

[🏠 Module 16](../README.md) · [📝 Quiz](quiz-01.md) · [📖 Lessons](../weeks/README.md)

> Model answers with reasoning. Grade on the *explanation*, not the phrase. ⭐ marks the load-bearing ideas.

---

## Part A · Foundations

**1. ⭐ What MLOps solves; why AI fails quietly.** DevOps ships code that either works or throws. AI systems have a third state: **running fine and being wrong** — a model returns `200 OK` with a confidently incorrect prediction, a RAG app answers fluently from stale documents, an agent completes a broken plan. There's no exception to catch. MLOps exists because correctness depends on *data* and a *learned model* that drift over time, so you need versioning, evaluation, observability, and drift detection to catch failures that raise no error. → [16.1](../weeks/16.1-what-is-mlops.md)

**2. Not train→deploy.** That view omits everything that keeps the system correct *over time*: reproducibility, data/model versioning, experiment tracking, a gated registry, pipelines, CI/CD with eval gates, progressive deployment, observability, drift detection, and the retraining loop. Train→deploy is a straight line; MLOps is a **closed loop**. → [16.1](../weeks/16.1-what-is-mlops.md)

**3. Three things to version.** Code, **data**, and the **model** (+ for LLMs, prompts/config). Code alone is insufficient because the same code on different data or with a different checkpoint produces a different system — reproducibility requires pinning all three plus environment and seed. → [16.2](../weeks/16.2-reproducibility.md)

**4. Data as first-class artifact.** A model is only reproducible from its *exact* training data, so data must be versioned like code — but it's large and often mutable, so you version it by content hash/snapshot (DVC/LakeFS) rather than storing copies in Git. Unlike code, you also need to *diff distributions*, not just lines. → [16.3](../weeks/16.3-data-versioning.md)

**5. Experiment tracking.** Captures params, metrics, artifacts, and lineage for every run. It's the prerequisite for a defensible choice because "this model is best" is only credible if you can compare runs on identical data and reproduce the winner. → [16.4](../weeks/16.4-experiment-tracking.md)

**6. ⭐ Registry + gated promotion.** A registry is the versioned source of truth for models with lifecycle stages (staging→prod) and lineage. Gated promotion means a model reaches prod only after passing an eval + approval — so prod always points at a **known-good, traceable** model, not whatever a training run happened to produce. → [16.5](../weeks/16.5-model-registry.md)

**7. Instant rollback.** Because AI fails quietly, you often discover a bad model *in production*; time-to-recover matters. The registry keeps prior prod versions as first-class, so rollback is repointing to the last-good version — one action, no retrain. → [16.5](../weeks/16.5-model-registry.md)

## Part B · Build & ship

**8. Pipeline vs script.** A pipeline gives orchestration, retries, caching, scheduling, and lineage — a failed stage resumes without rerunning everything, and the whole run is reproducible. Orchestrators: Airflow, Prefect, Dagster, Kubeflow. → [16.6](../weeks/16.6-ml-pipelines.md)

**9. ⭐ CI/CD for AI.** Beyond code, you test **data** (schema/quality/drift), **models** (eval metrics, no regression), **prompts** (for LLMs), and **RAG/agents** (end-to-end behavior). A green build means "quality didn't regress," not just "it compiles." → [16.7](../weeks/16.7-cicd.md)

**10. Eval gate.** An automated quality check in CI/CD that blocks promotion if a model/prompt regresses against a benchmark. It sits between "trained/changed" and "promoted," so regressions never reach prod. → [16.7](../weeks/16.7-cicd.md) · [16.12](../weeks/16.12-llm-evaluation.md)

**11. Serving modes.** **Batch** — high-throughput, latency-tolerant (nightly scoring). **Online** — low-latency request/response (real-time predictions). **Async** — long-running or spiky work via a queue (LLM generation, video). Choose by latency need and workload shape. → [16.8](../weeks/16.8-model-serving.md)

**12. Serving stacks.** Classic: FastAPI/BentoML/TorchServe. LLMs: vLLM/TGI — because LLMs need KV-cache management, continuous batching, and token streaming that generic servers don't provide. → [16.8](../weeks/16.8-model-serving.md) · [16.14](../weeks/16.14-model-optimization.md)

**13. Deployment strategies.** Blue-green (two full envs, instant switch), canary (small % first, promote on metrics), rolling (gradual replace), shadow (mirror traffic, no user impact). Use **shadow** to test a new model on real traffic *before* it serves anyone. → [16.13](../weeks/16.13-deployment-strategies.md)

## Part C · LLMOps

**14. ⭐ LLMOps adds.** On top of MLOps: versioning **prompts, RAG configs, and agent definitions**; pinning model versions; evaluating *quality* (not accuracy); and monitoring *tokens, cost, latency, and quality drift*. → [16.9](../weeks/16.9-llmops.md)

**15. Pin the model version.** A provider silently updating the model changes outputs under you — reproducibility and evals break, and quality can regress with no code change. Pinning makes the model a versioned dependency. → [16.9](../weeks/16.9-llmops.md)

**16. Versioning prompts/RAG/agents.** Store them as files in Git (diffable, reviewable), tie each to an eval run, and pin the model + retrieval config so any past output is reproducible. → [16.9](../weeks/16.9-llmops.md)

**17. Beyond accuracy.** LLM outputs are open-ended, so you evaluate axes: task success, generation quality (relevance/faithfulness), safety, and cost/latency — accuracy on a fixed label set doesn't capture any of them. → [16.12](../weeks/16.12-llm-evaluation.md)

**18. LLM-as-judge.** Using a strong model to score outputs against a rubric. Keep it trustworthy by **calibrating against human labels**, fixing the judge model/version, and using it for relative comparison, not absolute truth. → [16.12](../weeks/16.12-llm-evaluation.md)

**19. Optimization levers.** Quantization (fewer bits/weight → smaller, faster), distillation (train a small model to mimic a big one), pruning (remove low-value weights). Each trades some quality for latency/cost. → [16.14](../weeks/16.14-model-optimization.md)

**20. KV cache / continuous batching / speculative decoding.** KV cache avoids recomputing attention over past tokens (per-request speed). Continuous batching packs concurrent requests to keep the GPU busy (throughput). Speculative decoding drafts tokens with a small model and verifies with the big one (latency). → [16.14](../weeks/16.14-model-optimization.md)

## Part D · Operate

**21. ⭐ Three pillars.** Logs, metrics, traces. For LLMs, additionally track **tokens, cost, latency, and quality** per call — the observables that reveal quiet failures. → [16.10](../weeks/16.10-observability.md)

**22. Tracing RAG/agents.** They're multi-step (retrieve → generate; plan → tool → observe). A single latency/quality number hides *which step* failed; a trace localizes it. → [16.10](../weeks/16.10-observability.md)

**23. Drift types.** Data drift (input distribution changes — new user vocabulary). Concept drift (the input→output relationship changes — fraud patterns evolve). Model drift (performance decays over time as a result). → [16.11](../weeks/16.11-monitoring-drift.md)

**24. KS / PSI.** Both measure how far a current distribution has moved from a reference (KS = max CDF gap; PSI = binned population shift). Crossing a threshold triggers evaluate→retrain. → [16.11](../weeks/16.11-monitoring-drift.md)

**25. ⭐ Detect→evaluate→retrain.** Detect drift, *then evaluate whether it actually hurt quality*, then retrain only if it did. You don't retrain on every signal because drift ≠ degradation — blind retraining wastes compute and can chase noise. → [16.11](../weeks/16.11-monitoring-drift.md)

**26. Reliability patterns.** Timeout (prevents hanging on a slow dependency), retry+backoff (transient failures), circuit breaker (stops hammering a down service), rate limit/backpressure (prevents overload). → [16.17](../weeks/16.17-reliability.md)

**27. Graceful degradation.** Serve a reduced-but-working response when a component fails — e.g., fall back to a cached answer, a smaller model, or retrieval-only when the LLM is down, instead of erroring. → [16.17](../weeks/16.17-reliability.md)

**28. Cost attribution.** Tag every request with model, tokens, user, and workflow so you can compute cost per each dimension. You bother because a single blended bill hides the runaway driver; attribution finds it. → [16.18](../weeks/16.18-cost-optimization.md)

**29. Cost levers.** Model routing (cheap model for easy queries), caching, prompt/context trimming, batching, and quantized self-hosting. Cut cost without quality loss by routing/caching where the eval shows no regression. → [16.18](../weeks/16.18-cost-optimization.md)

**30. ⭐ Two security layers.** Infra layer (IAM, network, secrets — same as any service) **and** the AI layer (prompt injection, data exfiltration via outputs, tool misuse). Unique AI threat: **prompt injection** turning untrusted input into instructions. → [16.19](../weeks/16.19-security.md)

**31. Least privilege + defense-in-depth for agents.** Give each tool the minimum permission it needs, validate/authorize tool calls, sandbox execution, and layer defenses (input filtering + output validation + scoped credentials) so one bypass isn't catastrophic. → [16.19](../weeks/16.19-security.md)

## Part E · Infrastructure

**32. VRAM estimate.** Serving ≈ model bytes (params × bytes/param for the precision) + KV cache (grows with batch × sequence length) + activation overhead. Training adds gradients + optimizer state (~16 bytes/param full-precision). → [16.15](../weeks/16.15-gpu-infrastructure.md)

**33. Fit ladder.** Apply in order until it fits: lower precision/quantization → smaller batch/sequence → tuned KV cache → offloading/sharding → bigger/multiple GPUs. Each step trades some speed for memory. → [16.15](../weeks/16.15-gpu-infrastructure.md)

**34. K8s objects.** Pod (a running container group), Deployment (declarative replicas + rollout/heal), Service (stable network endpoint + load balancing), Job (run-to-completion batch/training work). → [16.16](../weeks/16.16-kubernetes.md)

**35. K8s + GPUs.** GPUs are requested as a resource (`nvidia.com/gpu`) and scheduled onto GPU nodes; autoscaling adds pods/nodes under load. Keep a warm min replica to bound cold starts. → [16.16](../weeks/16.16-kubernetes.md)

**36. ⭐ IaC layers.** Version-control infra for reproducibility/review/rollback. Docker packages the runtime, Terraform declares cloud resources (GPU pools, storage, network), Kubernetes orchestrates containers, Helm parameterizes K8s manifests into charts. → [16.21](../weeks/16.21-iac.md)

**37. IaC for AI.** It makes GPU infrastructure repeatable — a Terraform GPU node pool + Helm serving chart turns "stand up a training/serving environment" into `apply`, not a day of console clicking. → [16.21](../weeks/16.21-iac.md)

**38. Cloud platforms.** SageMaker/Vertex/Azure ML package the *same lifecycle you learned* — tracking, registry, pipelines, serving, monitoring — into one managed console. Concepts transfer; only the console changes. → [16.22](../weeks/16.22-cloud.md)

**39. ⭐ Managed vs. self-hosted.** Managed buys speed + integration at the cost of lock-in + price. Avoid lock-in with a **portable core** (MLflow, standard formats, Docker/K8s) on managed compute, plus a documented exit plan. → [16.22](../weeks/16.22-cloud.md)

## Part F · Architecture & synthesis

**40. Shared skeleton.** Gateway (auth, rate limit, routing) → core (the model/RAG/agent logic) → observability, all sitting on a registry + CI/CD backbone. → [16.20](../weeks/16.20-production-architecture.md)

**41. Divergence.** ML systems center a served model + feature/data pipeline; LLM apps add prompt/RAG layers and token/cost concerns; agent systems add tool orchestration, planning loops, and tighter security/observability. Same skeleton, different core. → [16.20](../weeks/16.20-production-architecture.md)

**42. ML capstone loop.** Versioned data → tracked training → gated registry → served (canary/shadow) → observed → drift detected → auto-retrain → back through the gate. A loop, not a line. → [16.23](../weeks/16.23-end-to-end-projects.md)

**43. LLM capstone.** Versioned prompt/RAG/agent → eval-gated CI/CD → optimized serving → observability of tokens/cost/quality → quality/cost regression → re-eval/rollback. Differs from ML by versioning prompts (not just data), gating on evals (not just metrics), and monitoring quality/cost drift (not just data drift). → [16.23](../weeks/16.23-end-to-end-projects.md)

**44. ⭐ Closing the loop.** ML closes via drift→retrain→gated-promote; LLM closes via regression→re-eval/rollback. The loop is the point because AI **fails quietly** — only a feedback loop catches and fixes a failure that raises no error. → [16.23](../weeks/16.23-end-to-end-projects.md)

**45. Mini projects first.** Each drills one muscle (versioning, registry, serving, drift…) in isolation, so assembling the capstone is integration, not debugging ten unfamiliar pieces at once. → [16.24](../weeks/16.24-projects-summary.md)

**46. Model suddenly inaccurate.** First question: **drift or bad deploy?** Correlate input distribution against the last model/prompt change — roll back if it's a deploy, retrain if it's drift. → [16.11](../weeks/16.11-monitoring-drift.md) · [16.13](../weeks/16.13-deployment-strategies.md)

**47. Cost spike.** Attribute cost per request/user/workflow to find which token driver moved (runaway prompt, retry storm, growing context), then cap/cache/route it. → [16.18](../weeks/16.18-cost-optimization.md)

**48. ⭐ The one idea.** Production AI is a **closed loop** — reproduce → ship through gates → observe → detect drift → evaluate → retrain → roll back — not train→deploy, because AI systems fail quietly and only a loop catches quiet failure. → [16.1](../weeks/16.1-what-is-mlops.md)

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 16](../README.md) |
| 📝 Quiz | [quiz-01.md](quiz-01.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
