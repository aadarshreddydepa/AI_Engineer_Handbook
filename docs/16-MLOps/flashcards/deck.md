# 🧠 Module 16 · MLOps & LLMOps — Flashcard Deck

[🏠 Module 16](../README.md) · [📖 Lessons](../weeks/README.md) · [📄 Cheat sheet](../cheat-sheets/mlops-cheatsheet.md)

> **~80 cards.** Cover the answer, say it aloud, *then* check. ⭐ marks the load-bearing ones.

---

## 16.1–16.5 · Foundations

**Q:** ⭐ Why do AI systems "fail quietly"? → **A:** They can run fine (`200 OK`) while being *wrong* — a stale-RAG answer, a confidently wrong prediction, a broken agent plan. No exception is thrown, so only evaluation/observability/drift detection catches it. → [16.1](../weeks/16.1-what-is-mlops.md)

**Q:** ⭐ Why isn't MLOps just "train → deploy"? → **A:** It's a *closed loop* — reproduce, version, track, gate, serve, observe, detect drift, retrain, roll back — that keeps a system correct over time. → [16.1](../weeks/16.1-what-is-mlops.md)

**Q:** What three things must you version for reproducibility? → **A:** Code, data, and the model (+ prompts/config for LLMs) — plus environment and seed. → [16.2](../weeks/16.2-reproducibility.md)

**Q:** Why isn't pinning code enough? → **A:** Same code + different data or checkpoint = different system; reproducibility needs all inputs pinned. → [16.2](../weeks/16.2-reproducibility.md)

**Q:** Why is data a first-class versioned artifact? → **A:** A model is only reproducible from its exact data; version it by hash/snapshot (DVC/LakeFS), and diff *distributions*, not just lines. → [16.3](../weeks/16.3-data-versioning.md)

**Q:** What does experiment tracking capture? → **A:** Params, metrics, artifacts, and lineage per run — the basis for a defensible "this model is best." → [16.4](../weeks/16.4-experiment-tracking.md)

**Q:** ⭐ What is a model registry + gated promotion? → **A:** Versioned source of truth for models with lifecycle stages; promotion to prod only past an eval + approval, so prod is always known-good and traceable. → [16.5](../weeks/16.5-model-registry.md)

**Q:** Why must rollback be instant? → **A:** You often find a bad model *in prod*; the registry keeps prior versions so rollback is repointing, not retraining. → [16.5](../weeks/16.5-model-registry.md)

## 16.6–16.8, 16.13 · Build & ship

**Q:** Pipeline vs. training script? → **A:** Orchestration, retries, caching, scheduling, lineage — a failed stage resumes without rerunning everything. → [16.6](../weeks/16.6-ml-pipelines.md)

**Q:** Name three orchestrators. → **A:** Airflow, Prefect, Dagster (also Kubeflow). → [16.6](../weeks/16.6-ml-pipelines.md)

**Q:** ⭐ How does CI/CD for AI differ? → **A:** You test data, models, prompts, and RAG/agents — not just code; green = "quality didn't regress." → [16.7](../weeks/16.7-cicd.md)

**Q:** What is an eval gate? → **A:** An automated quality check that blocks promotion on regression; sits between "changed" and "promoted." → [16.7](../weeks/16.7-cicd.md)

**Q:** Batch vs. online vs. async serving? → **A:** Batch = high-throughput latency-tolerant; online = low-latency request/response; async = long/spiky via a queue. → [16.8](../weeks/16.8-model-serving.md)

**Q:** Serving stacks — classic vs. LLM? → **A:** Classic: FastAPI/BentoML/TorchServe. LLM: vLLM/TGI (KV cache, continuous batching, streaming). → [16.8](../weeks/16.8-model-serving.md)

**Q:** Blue-green vs. canary vs. rolling vs. shadow? → **A:** Two-env instant switch / small-% first / gradual replace / mirror traffic with no user impact. → [16.13](../weeks/16.13-deployment-strategies.md)

**Q:** When do you use shadow deployment? → **A:** To test a new model on real traffic *before* it serves any user. → [16.13](../weeks/16.13-deployment-strategies.md)

## 16.9, 16.12, 16.14 · LLMOps

**Q:** ⭐ What does LLMOps add over MLOps? → **A:** Versioning prompts/RAG/agents, pinning model versions, quality (not accuracy) evals, and token/cost/quality monitoring. → [16.9](../weeks/16.9-llmops.md)

**Q:** Why pin the LLM's model version? → **A:** A silent provider update changes outputs — evals and reproducibility break with no code change. → [16.9](../weeks/16.9-llmops.md)

**Q:** Why can't accuracy alone evaluate an LLM? → **A:** Outputs are open-ended; you need task success, generation quality, safety, and cost/latency axes. → [16.12](../weeks/16.12-llm-evaluation.md)

**Q:** What is LLM-as-judge, kept trustworthy how? → **A:** A strong model scoring outputs to a rubric; calibrate vs humans, fix the judge version, use for relative comparison. → [16.12](../weeks/16.12-llm-evaluation.md)

**Q:** Quantization / distillation / pruning? → **A:** Fewer bits/weight / small model mimics big / remove low-value weights — each trades quality for speed/cost. → [16.14](../weeks/16.14-model-optimization.md)

**Q:** ⭐ KV cache / continuous batching / speculative decoding? → **A:** Reuse past attention (per-request) / pack concurrent requests (throughput) / draft-then-verify (latency). → [16.14](../weeks/16.14-model-optimization.md)

## 16.10–16.11, 16.17–16.19 · Operate

**Q:** ⭐ Three pillars of observability (+ LLM extras)? → **A:** Logs, metrics, traces — plus tokens, cost, latency, quality per call. → [16.10](../weeks/16.10-observability.md)

**Q:** Why is tracing vital for RAG/agents? → **A:** They're multi-step; a single number hides *which step* failed — a trace localizes it. → [16.10](../weeks/16.10-observability.md)

**Q:** Data vs. concept vs. model drift? → **A:** Input distribution shifts / input→output relationship shifts / performance decays as a result. → [16.11](../weeks/16.11-monitoring-drift.md)

**Q:** What do KS and PSI measure? → **A:** How far a current distribution moved from a reference; crossing a threshold triggers evaluate→retrain. → [16.11](../weeks/16.11-monitoring-drift.md)

**Q:** ⭐ Why not retrain on every drift signal? → **A:** Drift ≠ degradation — detect, then *evaluate impact*, then retrain only if quality actually dropped. → [16.11](../weeks/16.11-monitoring-drift.md)

**Q:** Four reliability patterns? → **A:** Timeout, retry+backoff, circuit breaker, rate limit/backpressure (+ graceful degradation). → [16.17](../weeks/16.17-reliability.md)

**Q:** Graceful degradation example? → **A:** LLM down → serve a cached answer / smaller model / retrieval-only instead of erroring. → [16.17](../weeks/16.17-reliability.md)

**Q:** ⭐ Attribute cost along which dimensions, and why? → **A:** Per request / user / model / workflow — a blended bill hides the runaway driver. → [16.18](../weeks/16.18-cost-optimization.md)

**Q:** Cut LLM cost without losing quality — how? → **A:** Model routing, caching, context trimming, batching, quantized self-host — where evals show no regression. → [16.18](../weeks/16.18-cost-optimization.md)

**Q:** ⭐ Why two security layers? → **A:** Infra (IAM/network/secrets) *and* AI (prompt injection, exfiltration, tool misuse); unique threat = prompt injection. → [16.19](../weeks/16.19-security.md)

**Q:** Least privilege for an agent's tools? → **A:** Each tool gets minimum permission; validate/authorize calls; sandbox; layer defenses. → [16.19](../weeks/16.19-security.md)

## 16.15–16.16, 16.21–16.22 · Infrastructure

**Q:** How to estimate serving VRAM? → **A:** Model bytes (params × bytes/precision) + KV cache (batch × seq) + activation overhead. → [16.15](../weeks/16.15-gpu-infrastructure.md)

**Q:** The GPU "fit ladder"? → **A:** Lower precision → smaller batch/seq → tune KV cache → offload/shard → bigger/more GPUs. → [16.15](../weeks/16.15-gpu-infrastructure.md)

**Q:** K8s pod / deployment / service / job? → **A:** Running container(s) / declarative replicas+rollout / stable endpoint+LB / run-to-completion work. → [16.16](../weeks/16.16-kubernetes.md)

**Q:** How does K8s handle GPUs? → **A:** Request `nvidia.com/gpu`, schedule onto GPU nodes, autoscale under load, keep a warm min replica. → [16.16](../weeks/16.16-kubernetes.md)

**Q:** ⭐ How do Docker/Terraform/K8s/Helm layer? → **A:** Docker = runtime, Terraform = cloud resources, K8s = orchestration, Helm = parameterized manifests. → [16.21](../weeks/16.21-iac.md)

**Q:** Why is IaC especially valuable for AI? → **A:** Makes GPU infra repeatable — `apply` a Terraform pool + Helm chart, not a day of clicking. → [16.21](../weeks/16.21-iac.md)

**Q:** What do cloud MLOps platforms provide? → **A:** A managed packaging of the same lifecycle — tracking/registry/pipelines/serving/monitoring; only the console changes. → [16.22](../weeks/16.22-cloud.md)

**Q:** ⭐ Managed vs. self-hosted, and avoiding lock-in? → **A:** Managed = speed+integration at lock-in+price cost; keep a portable core (MLflow, std formats, Docker/K8s) on managed compute. → [16.22](../weeks/16.22-cloud.md)

## 16.20, 16.23–16.24 · Architecture & synthesis

**Q:** Shared production skeleton? → **A:** Gateway → core → observability, on a registry + CI/CD backbone. → [16.20](../weeks/16.20-production-architecture.md)

**Q:** ⭐ How does the ML capstone close its loop? → **A:** Drift detected → evaluate → retrain → gated promote — back to serving. → [16.23](../weeks/16.23-end-to-end-projects.md)

**Q:** ⭐ How does the LLM capstone differ + close its loop? → **A:** Versions prompt/RAG/agent, gates on evals, monitors quality/cost; regression → re-eval/rollback. → [16.23](../weeks/16.23-end-to-end-projects.md)

**Q:** Why build mini projects before the capstones? → **A:** Each drills one muscle in isolation, so the capstone is integration, not ten new bugs at once. → [16.24](../weeks/16.24-projects-summary.md)

**Q:** "Model suddenly inaccurate" — first question? → **A:** Drift or bad deploy? Correlate input distribution vs. last change; roll back or retrain. → [16.24](../weeks/16.24-projects-summary.md)

**Q:** ⭐ The single idea of Module 16? → **A:** Production AI is a *closed loop*, not train→deploy — because AI fails quietly and only a loop catches quiet failure. → [16.1](../weeks/16.1-what-is-mlops.md)

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 16](../README.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
| 📄 Cheat sheet | [MLOps & LLMOps cheat sheet](../cheat-sheets/mlops-cheatsheet.md) |
