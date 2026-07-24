# 🏋️ Module 17 · Cloud for AI Engineers — Exercises

[🏠 Module 17](../README.md) · [📖 Lessons](../weeks/README.md) · [🧩 Projects](../projects/)

> Build-it and break-it exercises, ordered along the cloud stack: **fundamentals → compute/GPU → network/storage/data → containers/orchestration → architect/secure/cost/scale → ship/operate → multi-cloud**. If you do only seven, do ⭐ **E2, E4, E5, E9, E13, E14, E22** — VRAM sizing, a secure VPC, the right data stores, a K8s serving stack, least-privilege security, a cost audit, and the IaC platform capstone. The final tier is **incident drills** — because operating cloud AI is diagnosing failures (GPU unavailable, cost spike, pod crash, network blocked) under pressure. Exercises are tagged: **conceptual · architecture · deployment · GPU-selection · cost · security · troubleshooting.**

---

## Tier 1 · Foundations (17.1–17.4)

### E1 · Rung placement (conceptual)
For 6 AI workloads, choose IaaS/PaaS/serverless/SaaS and justify; distinguish scalability vs. elasticity and availability vs. fault tolerance. → [17.1](../weeks/17.1-cloud-fundamentals.md)

### E1b · HA & DR design (architecture)
Design a multi-AZ deployment for an LLM API that survives an AZ failure; add a DR plan for RTO=15min/RPO=5min. → [17.2](../weeks/17.2-regions-availability.md)

### ⭐ E2 · Compute + VRAM sizing (GPU-selection)
For 7B/13B/70B at fp16 and int4, compute inference *and* full-FT VRAM; pick a GPU class (or "needs N GPUs") for each; choose CPU/GPU/TPU for 6 workloads. → [17.3](../weeks/17.3-compute.md) · [17.4](../weeks/17.4-gpu-infrastructure.md)

### E3 · GPU scaling ladder (GPU-selection)
Take a 70B you must serve; decide single/multi-GPU with the arithmetic; explain single→multi→distributed→cluster. → [17.4](../weeks/17.4-gpu-infrastructure.md)

## Tier 2 · Network, storage, data (17.5–17.7)

### ⭐ E4 · Secure VPC (architecture + security)
Design a VPC (public LB + private app/model/DB) with least-privilege security-group rules so each tier talks only to its neighbor; map VPC/SG/LB/DNS to AWS/Azure/GCP. → [17.5](../weeks/17.5-networking.md)

### E4b · Storage matching (conceptual)
Place datasets, checkpoints, DB data, RAG docs, embeddings, and scratch on block/file/object/vector; design lifecycle rules for cost. → [17.6](../weeks/17.6-storage.md)

### ⭐ E5 · AI data layer (architecture)
For a multi-tenant RAG chat product, choose relational/document/KV/vector/object per data type; implement tenant isolation on vector search; show the cache→DB→vector access pattern. → [17.7](../weeks/17.7-databases.md)

## Tier 3 · Containers & orchestration (17.8–17.10)

### E6 · Containerize an AI service (deployment)
Write a Dockerfile with a CUDA base, pinned deps, non-root, no baked-in secrets/weights; describe commit→build→push→deploy. → [17.8](../weeks/17.8-containers.md)

### ⭐ E9 · Kubernetes serving stack (deployment)
Deploy a GPU model API: Deployment + Service + readiness probe + HPA + GPU-requested pods + a batch Job; explain Deployment vs. Job and GPU scheduling. → [17.9](../weeks/17.9-kubernetes.md)

### E7 · Serverless fit (conceptual)
For 6 tasks, decide serverless vs. container vs. VM; list the four serverless limits that block GPU/model workloads. → [17.10](../weeks/17.10-serverless.md)

## Tier 4 · Architect, secure, cost, scale (17.11–17.16)

### E8 · Three architectures (architecture)
Draw the five-layer skeleton for ML, LLM, and agent systems; mark where they diverge; place each component on a primitive. → [17.11](../weeks/17.11-ai-architectures.md)

### E8b · Service selection (conceptual)
Classify services into the six categories; make a build-vs-buy call for 5 scenarios with a portable-core/exit plan. → [17.12](../weeks/17.12-ai-services.md)

### ⭐ E13 · Least-privilege security (security)
Write least-privilege IAM roles for a serving pod, an ingestion function, and a training job; audit an architecture against the security checklist; show secret flow from vault to pod. → [17.13](../weeks/17.13-security.md)

### ⭐ E14 · Cost audit (cost)
Estimate monthly cost across the five buckets for a GPU serving stack; find the dominant driver; apply the levers (scale-to-zero, batching, spot/reserved, caching) and estimate savings. → [17.14](../weeks/17.14-cost-optimization.md)

### E15 · Autoscaling design (architecture)
Write an HPA for GPU serving with warm minimum, ceiling, target util, and anti-thrash; explain LB↔autoscaler cooperation and the GPU scale-up lag. → [17.15](../weeks/17.15-autoscaling.md)

### E16 · Distributed pipeline (architecture)
Convert a synchronous "upload→embed→index" flow into a queued, event-driven pipeline with idempotent workers, retries, and a dead-letter queue; explain data vs. model parallelism. → [17.16](../weeks/17.16-distributed-systems.md)

## Tier 5 · Ship & operate (17.17–17.21)

### E17 · CI/CD pipeline (deployment)
Design a git→test(+evals)→build→staging→canary-prod pipeline with per-env config/secrets and rollback. → [17.17](../weeks/17.17-deployment.md)

### ⭐ E22 · IaC platform (deployment + capstone)
Define a full AI platform in Terraform — network, K8s+GPU, storage, DB — with modules, per-env tfvars, remote encrypted state, no secrets in files, least-privilege IAM, and `destroy` for ephemeral envs. → [17.18](../weeks/17.18-iac.md)

### E18 · Observability stack (troubleshooting)
Instrument an LLM+RAG service with logs/metrics/traces + AI signals (tokens, model latency, retrieval quality); define 5 alerts without alert fatigue. → [17.19](../weeks/17.19-observability.md)

### E19 · Resilient architecture (architecture)
Add HA (multi-AZ), fault tolerance (timeout/retry/circuit-breaker), graceful-degradation tiers, and a DR plan; run a game-day thought experiment. → [17.20](../weeks/17.20-reliability.md)

### E20 · Provider mapping (conceptual)
From memory, fill the concept→AWS/Azure/GCP table for 10 primitives; instantiate one architecture on each provider; decide single vs. multi-cloud. → [17.21](../weeks/17.21-multi-cloud.md)

## Tier 6 · Incident drills (operate — diagnose under pressure)

> Plant each failure, then diagnose and recover — **first question in bold**. These are the on-call reality of cloud AI.

### I1 · GPU instance becomes unavailable
**First question: another AZ/region/instance type, or a fallback?** GPU capacity is scarce and regional; build retry + region/type fallback into provisioning; degrade gracefully. → [17.4](../weeks/17.4-gpu-infrastructure.md) · [17.2](../weeks/17.2-regions-availability.md)

### I2 · Cloud costs suddenly increase
**First question: which bucket moved — GPU, API/tokens, or egress?** Attribute via tags/metrics; find the idle GPU, runaway agent, or cross-region traffic; cap it; add a budget alert. → [17.14](../weeks/17.14-cost-optimization.md)

### I3 · Application becomes slow
**First question: which hop, and did it autoscale?** Trace the request (retrieval/model/DB/tool); check the autoscaler metric and GPU provisioning lag; look for a downstream bottleneck. → [17.19](../weeks/17.19-observability.md) · [17.15](../weeks/17.15-autoscaling.md)

### I4 · Database becomes unreachable
**First question: network or the database?** Check security group/subnet/route first, then DB health/failover and connection-pool exhaustion. → [17.7](../weeks/17.7-databases.md) · [17.5](../weeks/17.5-networking.md)

### I5 · Kubernetes pod crashes (CrashLoopBackOff)
**First question: what do the logs say — config, secret, OOM, or probe?** `kubectl logs`/`describe`; also check Pending-on-GPU (no free GPU / autoscaler). → [17.9](../weeks/17.9-kubernetes.md)

### I6 · Model deployment fails
**First question: which stage, and does staging differ from prod?** Build vs. deploy vs. runtime; identical image → it's config/secret/resource wiring; roll back to last-good tag. → [17.17](../weeks/17.17-deployment.md)

### I7 · Network access is blocked
**First question: security group, subnet, or route?** Is the port open from the right source? Is the resource in a private subnet with no route? Check LB health checks. → [17.5](../weeks/17.5-networking.md)

### I8 · Storage permissions misconfigured
**First question: IAM/bucket policy — too little, or public?** Grant exactly what's needed; if public, lock down + enable account-level public-access block + audit access. → [17.6](../weeks/17.6-storage.md) · [17.13](../weeks/17.13-security.md)

## Capstone

### ⭐ E23 · Full cloud AI platform (Projects 17.22)
Build **Project 8** end-to-end: an IaC-defined AI platform (network, K8s+GPU, storage, DB, vector) with CI/CD serving + autoscaling + canary, least-privilege security, infra + AI observability, multi-AZ reliability with backups/rollback, and spot/reserved/scale-to-zero cost control — reproducible across dev/staging/prod. → [17.22](../weeks/17.22-projects-summary.md)

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 17](../README.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
| 📝 Quiz | [Quiz 01](../quizzes/quiz-01.md) |
| 🎴 Flashcards | [Deck](../flashcards/deck.md) |
| 📄 Cheat sheet | [Cloud cheat sheet](../cheat-sheets/cloud-cheatsheet.md) |
