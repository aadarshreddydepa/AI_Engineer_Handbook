# 🏋️ Module 16 · MLOps & LLMOps — Exercises

[🏠 Module 16](../README.md) · [📖 Lessons](../weeks/README.md) · [🧩 Projects](../projects/)

> Build-it and break-it exercises, ordered along the module's spine: **reproduce → version → track → ship → serve → observe → operate**. If you do only seven, do ⭐ **E2, E4, E6, E8, E10, E12, E20** — a reproducible run, a gated registry, an eval-gated CI/CD, an optimized server, an observability stack, a drift→retrain loop, and the end-to-end capstone. Together they are the module. The final tier is **incident drills** — because production AI **fails quietly** ([16.1](../weeks/16.1-what-is-mlops.md)), the real skill is diagnosing and rolling back under a live failure.

---

## Tier 1 · Foundations (16.1–16.5)

### E1 · Fails-quietly audit (conceptual)
**Goal:** list 8 ways an AI system can return `200 OK` while being wrong; map each to the signal that would catch it.
**Done-when:** every quiet failure maps to a metric/trace/eval, not an error code. → [16.1](../weeks/16.1-what-is-mlops.md)

### ⭐ E2 · Reproducible run (implementation)
**Goal:** pin code, deps, data, and seed so two runs produce identical results.
**Done-when:** (1) byte-identical metrics twice; (2) unpinning any one of the four breaks it; (3) a colleague reproduces from the lineage alone. → [16.2](../weeks/16.2-reproducibility.md)

### E3 · Data versioning (implementation)
**Goal:** version a dataset; roll back to a prior version; diff two versions.
**Done-when:** a model is reproducible from its exact data version; the diff shows what changed. → [16.3](../weeks/16.3-data-versioning.md)

### E3b · Experiment tracker (implementation)
**Goal:** log 20 runs with params/metrics/artifacts; find the best by a metric; compare two.
**Done-when:** every run is reproducible from its logged config; the best model is traceable to its run. → [16.4](../weeks/16.4-experiment-tracking.md)

### ⭐ E4 · Gated registry (implementation)
**Goal:** promote a model staging→prod only past an eval gate + approval; wire instant rollback.
**Done-when:** (1) a failing model can't be promoted; (2) rollback to the previous prod version is one action; (3) prod always points at a known-good, lineage-traceable model. → [16.5](../weeks/16.5-model-registry.md)

## Tier 2 · Build & ship (16.6–16.8, 16.13)

### E5 · Retrain pipeline (implementation)
**Goal:** orchestrate data→train→eval→register as a DAG with retries and caching.
**Done-when:** a failed stage retries/resumes without rerunning the whole DAG; the run is reproducible. → [16.6](../weeks/16.6-ml-pipelines.md)

### ⭐ E6 · CI/CD eval gate (implementation)
**Goal:** block a PR that regresses model/prompt/RAG quality; test data, model, and prompts — not just code.
**Done-when:** a quality-regressing change is red in CI; a passing change auto-promotes to staging. → [16.7](../weeks/16.7-cicd.md) · [16.12](../weeks/16.12-llm-evaluation.md)

### E7 · Serving modes (implementation)
**Goal:** serve one model three ways — batch, online, async — and pick correctly per workload.
**Done-when:** each mode's latency/throughput/cost profile is measured; you can justify the choice per use case. → [16.8](../weeks/16.8-model-serving.md)

### E9b · Progressive deploy (implementation)
**Goal:** canary a new model to 5% of traffic; shadow it first; auto-abort on metric regression.
**Done-when:** a bad model is caught in canary before full rollout; shadow traffic never affects users. → [16.13](../weeks/16.13-deployment-strategies.md)

## Tier 3 · Serve efficiently (16.14–16.16)

### ⭐ E8 · Optimized LLM server (implementation + perf)
**Goal:** serve an LLM with continuous batching + KV cache; measure tokens/sec and cost/1k tokens.
**Done-when:** throughput rises multi-x vs naive serving with equal quality; the latency/throughput trade-off is quantified. → [16.14](../weeks/16.14-model-optimization.md) · [16.8](../weeks/16.8-model-serving.md)

### E9 · GPU fit ladder (GPU estimation)
**Goal:** take a model that OOMs on serving; apply quantization/batching/KV-cache tuning until it fits and hits an SLA.
**Done-when:** VRAM math predicts the fit; the model serves within the target latency. → [16.15](../weeks/16.15-gpu-infrastructure.md)

### E9c · Kubernetes deploy (config)
**Goal:** deploy the server on K8s with GPU requests, autoscaling, health checks, and a warm min replica.
**Done-when:** it scales under load, heals a killed pod, and cold-starts are bounded by the warm min. → [16.16](../weeks/16.16-kubernetes.md)

## Tier 4 · LLMOps & operate (16.9–16.12, 16.17–16.19)

### E11 · LLMOps versioning (implementation)
**Goal:** version prompts, RAG config, and agent definitions as first-class artifacts; pin the model version.
**Done-when:** any past output is reproducible from its pinned prompt+RAG+model version; a prompt change is diffable. → [16.9](../weeks/16.9-llmops.md)

### ⭐ E10 · Observability stack (implementation)
**Goal:** trace every request end-to-end; dashboard tokens, cost, latency, and a quality proxy.
**Done-when:** one request is traceable through every stage; a cost/latency spike is localizable to a stage. → [16.10](../weeks/16.10-observability.md)

### ⭐ E12 · Drift → retrain loop (implementation)
**Goal:** detect data/quality drift (KS/PSI); trigger evaluate→retrain→gated-promote automatically.
**Done-when:** injected drift fires an alert; the loop retrains and only promotes past the eval gate; false alarms are tuned out. → [16.11](../weeks/16.11-monitoring-drift.md)

### E13 · LLM eval suite (evaluation)
**Goal:** build an eval suite (task + generation + safety, LLM-judge calibrated) that gates CI/CD.
**Done-when:** a prompt/model regression is caught by the suite before ship; the judge is calibrated vs humans. → [16.12](../weeks/16.12-llm-evaluation.md)

### E14 · Reliable client (implementation)
**Goal:** wrap an external model call with timeout, retry+backoff, circuit breaker, and graceful degradation.
**Done-when:** a dependency outage degrades gracefully instead of cascading; retries don't stampede. → [16.17](../weeks/16.17-reliability.md)

### E15 · Cost attribution (analysis)
**Goal:** compute cost per request / per user / per model / per workflow; find the top driver and cut it.
**Done-when:** the dominant cost driver is identified; an optimization (caching/routing/batching) measurably lowers cost with no quality loss. → [16.18](../weeks/16.18-cost-optimization.md)

### E16 · Defense-in-depth (security)
**Goal:** secure both layers — infra (IAM/network/secrets) and AI (prompt-injection defense, output validation, least privilege for tools).
**Done-when:** a prompt-injection attempt is blocked; no secret is in code/IaC; tool access is least-privilege. → [16.19](../weeks/16.19-security.md)

## Tier 5 · Infra & architecture (16.20–16.22)

### E17 · Architecture map (conceptual)
**Goal:** draw the shared skeleton (gateway → core → observability + registry/CI-CD backbone) for an ML, an LLM, and an agent system.
**Done-when:** the three share a skeleton and differ only where MLOps vs LLMOps demands. → [16.20](../weeks/16.20-production-architecture.md)

### E18 · Deployment as code (config + security)
**Goal:** declare the serving stack as IaC — Docker (pinned) + Terraform (GPU pool) + Helm (per-env); no secrets in files.
**Done-when:** the stack reproduces on a fresh environment from IaC alone; `destroy` tears it down; secrets are external. → [16.21](../weeks/16.21-iac.md)

### E19 · Portable cloud core (architecture)
**Goal:** run the lifecycle on managed cloud compute with a portable core (MLflow, std formats, Docker/K8s) and a documented exit plan.
**Done-when:** core artifacts reproduce off-platform; managed vs self-hosted cost is compared; migration effort is estimated. → [16.22](../weeks/16.22-cloud.md)

## Tier 6 · Incident drills (operate — AI fails quietly)

> Plant each failure, then **diagnose with observability and roll back** — first question in bold. These are the on-call reality of [16.1](../weeks/16.1-what-is-mlops.md).

### I1 · Model suddenly inaccurate
**First question: drift or bad deploy?** Correlate input distribution vs. the last model/prompt change; roll back if it's a deploy, retrain if it's drift. → [16.11](../weeks/16.11-monitoring-drift.md) · [16.13](../weeks/16.13-deployment-strategies.md)

### I2 · GPU memory exhausted (OOM)
**First question: what changed in batch/sequence/model size?** Localize the VRAM driver; apply the fit ladder; add an OOM guardrail. → [16.15](../weeks/16.15-gpu-infrastructure.md)

### I3 · LLM cost spikes unexpectedly
**First question: which token driver moved?** Attribute cost per request/user/workflow; find the runaway prompt/retry/context growth; cap it. → [16.18](../weeks/16.18-cost-optimization.md)

### I4 · Latency climbs
**First question: queue, batch, or dependency?** Read traces to localize; check backpressure and a slow downstream call. → [16.10](../weeks/16.10-observability.md) · [16.17](../weeks/16.17-reliability.md)

### I5 · Data distribution shifts
**First question: detect → evaluate → retrain?** Confirm drift statistically (KS/PSI), evaluate impact, trigger the gated retrain loop. → [16.11](../weeks/16.11-monitoring-drift.md)

### I6 · Deployment fails
**First question: roll back first, diagnose second?** Restore last-good from the registry immediately, then investigate with the failed run's lineage. → [16.13](../weeks/16.13-deployment-strategies.md) · [16.5](../weeks/16.5-model-registry.md)

### I7 · Model rollback required
**First question: is the previous version one click away?** Prove the registry makes rollback instant and lineage-traceable; measure time-to-recover. → [16.5](../weeks/16.5-model-registry.md)

## Capstone

### ⭐ E20 · End-to-end platform, closed loop (Projects 16.23)
**Goal:** the flagship — build **both** capstones: (A) an ML platform (versioned data → tracked train → gated registry → served → observed → drift-triggered retrain) and (B) an LLM platform (versioned prompt/RAG/agent → eval-gated CI/CD → optimized serving → tokens/cost/quality observability → regression→rollback).
**Done-when:** each system **closes its loop** — a planted failure is detected, evaluated, and auto-fixed or rolled back; every artifact is reproducible from lineage; rollback is demonstrated in both. → [16.23](../weeks/16.23-end-to-end-projects.md)

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 16](../README.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
| 📝 Quiz | [Quiz 01](../quizzes/quiz-01.md) |
| 🎴 Flashcards | [Deck](../flashcards/deck.md) |
| 📄 Cheat sheet | [MLOps & LLMOps cheat sheet](../cheat-sheets/mlops-cheatsheet.md) |
