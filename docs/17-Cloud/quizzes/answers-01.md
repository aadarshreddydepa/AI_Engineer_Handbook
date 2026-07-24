# ✅ Module 17 · Cloud for AI Engineers — Quiz 01 Answers

[🏠 Module 17](../README.md) · [📝 Quiz](quiz-01.md) · [📖 Lessons](../weeks/README.md)

> Model answers with reasoning. Grade on the *explanation*, not the phrase. ⭐ marks the load-bearing ideas.

---

## Part A · Foundations

**1. Cloud & elasticity.** Cloud computing is renting computing resources on demand over the internet, paying per use. It solves on-prem's over-/under-provisioning dilemma: instead of buying fixed hardware for a guessed peak, **elasticity** lets capacity grow and shrink with load — crucial for spiky, GPU-heavy AI (rent 8 GPUs for a run, release them after). → [17.1](../weeks/17.1-cloud-fundamentals.md)

**2. Four properties.** Scalability = the *capability* to grow by adding resources; elasticity = doing so *automatically and reversibly* with demand; availability = measured uptime (the outcome); fault tolerance = the redundant design that produces availability. → [17.1](../weeks/17.1-cloud-fundamentals.md)

**3. ⭐ IaaS/PaaS/SaaS/serverless.** They differ in how much of the stack you manage: IaaS (OS + up — GPU training/custom serving), PaaS (deploy code — model APIs), serverless (functions, scale-to-zero — event glue, *not* GPU/large models), SaaS (just consume — a hosted model API). Climb to the highest rung that still meets control/cost/latency/GPU needs. → [17.1](../weeks/17.1-cloud-fundamentals.md)

**4. Region/AZ/datacenter.** Region ⊃ AZs ⊃ datacenters. A datacenter is one building; an AZ is isolated-power/cooling/network datacenter(s) that fails independently; a region is several AZs in a geography. Independent failure domains are what let you build reliability by spreading across them. → [17.2](../weeks/17.2-regions-availability.md)

**5. HA pattern.** Redundant instances across ≥2 AZs behind a load balancer that health-checks and reroutes — surviving any AZ failure. Multi-region adds survival of a whole-region disaster plus low latency for distant users. → [17.2](../weeks/17.2-regions-availability.md)

**6. RTO/RPO.** Recovery Time Objective (max downtime) and Recovery Point Objective (max data loss). Tight objectives need warm/active standby (costly); loose ones allow backup-and-restore (cheap) — they drive the DR strategy and its cost. → [17.2](../weeks/17.2-regions-availability.md)

**7. ⭐ GPU vs. CPU.** GPUs have thousands of cores for massively parallel matrix math (deep learning is matmul → embarrassingly parallel); CPUs have few fast cores for serial branching logic. So GPUs crush training but not branchy business logic. → [17.3](../weeks/17.3-compute.md)

**8. ⭐ VRAM.** GPU on-board memory that must hold weights, activations, and (training) gradients + optimizer state simultaneously. If the model doesn't fit, it won't run regardless of core speed — so "which GPU?" is really "how much VRAM, does it fit?" → [17.3](../weeks/17.3-compute.md)

**9. ⭐ 7B VRAM.** Serving: 7B × 2 bytes (fp16) ≈ 14 GB weights + KV cache + ~15% overhead. Full fine-tuning: ~16 bytes/param (fp16 weights 2 + grads 2 + fp32 master 4 + Adam m,v 4+4) ≈ 112 GB + activations → needs multi-GPU or QLoRA. → [17.4](../weeks/17.4-gpu-infrastructure.md)

**10. Scaling ladder.** Single GPU (fits, simplest) → multi-GPU one node (model/data parallel, NVLink) → distributed across nodes (network-bound gradient sync) → GPU cluster (K8s-scheduled, shared, autoscaled). Climb only when memory/speed forces it. → [17.4](../weeks/17.4-gpu-infrastructure.md)

## Part B · Network, storage, data

**11. ⭐ VPC & subnets.** A VPC is your isolated private network. Public subnets (internet route) hold only the load balancer; private subnets (no inbound internet) hold app servers, GPU model services, databases, and vector DBs. → [17.5](../weeks/17.5-networking.md)

**12. Security groups.** Instance-level firewalls; default-deny then allow only the specific port from the specific source per tier — LB from internet, app from LB, model from app, DB from app/model. Each tier reaches only its neighbor. → [17.5](../weeks/17.5-networking.md)

**13. Load balancer.** Beyond distributing traffic: health-checks instances and routes only to healthy ones (HA), enabling horizontal scale and safe replica churn; terminates TLS; can route by path/host. → [17.5](../weeks/17.5-networking.md)

**14. ⭐ Storage types.** Block (raw disk, one VM, fastest — DB/OS volumes), file (shared filesystem, many VMs — distributed scratch), object (key→blob over HTTP, unlimited/cheap/durable). Object is the AI workhorse — datasets, checkpoints, artifacts, docs. → [17.6](../weeks/17.6-storage.md)

**15. Artifact placement.** Datasets, checkpoints, artifacts, logs, RAG source docs → object storage; embeddings → vector DB (similarity search); DB data → block. → [17.6](../weeks/17.6-storage.md) · [17.7](../weeks/17.7-databases.md)

**16. DB choice.** By data shape and query: structured/transactional → relational (SQL, joins/ACID); flexible/by-key → NoSQL (conversations, profiles); hot values → KV cache; embeddings/similarity → vector DB. → [17.7](../weeks/17.7-databases.md)

**17. ⭐ Vector DB for RAG.** RAG and agent memory retrieve by *similarity* (meaning) — a nearest-neighbor query that relational/object stores can't do efficiently at scale; vector DBs index vectors (HNSW/IVF) for millisecond similarity + metadata filtering. → [17.7](../weeks/17.7-databases.md)

**18. Layered access.** App → cache (µs, avoid recompute) → on miss DB (structured) → vector DB (retrieval), write results back to cache. Each store does what it's best at; caching is a major latency/cost saver. → [17.7](../weeks/17.7-databases.md)

## Part C · Containers & orchestration

**19. ⭐ Container vs. VM.** A container packages an app + exact dependencies in a portable, OS-virtualized box (shares host kernel, ms boot, dense); a VM virtualizes hardware (full OS each, heavy). It kills "works on my machine" — vital for fragile CUDA/PyTorch AI stacks. → [17.8](../weeks/17.8-containers.md)

**20. Image flow.** Source → Dockerfile → image (immutable, layered, reproducible) → registry → container (ephemeral instance) → cloud. Immutability means the same versioned artifact runs identically everywhere; containers are disposable. → [17.8](../weeks/17.8-containers.md)

**21. Weights & secrets.** Don't bake large weights into the image (slow pulls) — pull from object storage at startup. Never bake secrets in (shared via registries) — inject at runtime from a secrets manager. → [17.8](../weeks/17.8-containers.md)

**22. ⭐ K8s reconciliation.** You declare desired state (replicas, GPUs, endpoints); the control plane continuously reconciles reality to match — scheduling pods, restarting failures, rescheduling off dead nodes, scaling. You manage outcomes, not containers. → [17.9](../weeks/17.9-kubernetes.md)

**23. Deployment vs. Job.** Deployment keeps N replicas always running and self-healing (serving); Job runs a pod to completion and stops (training, batch inference); CronJob schedules Jobs (nightly scoring). → [17.9](../weeks/17.9-kubernetes.md)

**24. ⭐ GPU scheduling.** A pod requests `nvidia.com/gpu: N`; via a device plugin the scheduler places it only on a node with that many free GPUs and reserves them — enabling shared, bin-packed, autoscaled GPU clusters. → [17.9](../weeks/17.9-kubernetes.md)

**25. Serverless limits.** Deploy functions run per-event, scale to zero, no servers — great for glue. Wrong for large models/GPU/long training because it's CPU-only with time/memory caps and cold starts; the AI pattern is a function that *delegates* heavy compute. → [17.10](../weeks/17.10-serverless.md)

**26. Three compute forms.** VM (most control/ops) → container (portable, orchestrated) → serverless (least ops, most limits, scale-to-zero, no GPU). A control-vs-convenience spectrum. → [17.10](../weeks/17.10-serverless.md)

## Part D · Architect, secure, cost, scale

**27. ⭐ Shared skeleton.** Gateway/API → app logic → AI core (model/RAG/agent) → data stores → observability + security, riding the cloud primitives. → [17.11](../weeks/17.11-ai-architectures.md)

**28. Divergence.** They differ in the *core* (trained model vs. LLM+RAG vs. agent loop) and dominant data store (object/relational vs. vector/cache vs. vector/state) — not the overall shape. → [17.11](../weeks/17.11-ai-architectures.md)

**29. Service categories.** Managed model APIs, model hosting, training infrastructure, GPU compute, vector search, data platforms. Think in categories because product names change yearly and differ per cloud but categories are stable. → [17.12](../weeks/17.12-ai-services.md)

**30. ⭐ Managed vs. self-hosted.** Managed buys speed/integration at the cost of lock-in and price; avoid lock-in with a portable core (MLflow, open formats, Docker/K8s) on managed compute — buy the undifferentiated heavy lifting, own your edge. → [17.12](../weeks/17.12-ai-services.md)

**31. Identity chain.** Identity (who) → authentication (prove it) → authorization/IAM (what's allowed) → resource. Every cloud access is gated by this chain. → [17.13](../weeks/17.13-security.md)

**32. ⭐ Least privilege.** Grant every identity the minimum permissions it needs; it shrinks the blast radius of a compromised credential from catastrophe to contained. Over-broad IAM is the most common damaging misconfiguration. → [17.13](../weeks/17.13-security.md)

**33. Secrets.** In a secrets manager, injected at runtime, rotated — never in code, images, env files committed to git, or CI logs. → [17.13](../weeks/17.13-security.md)

**34. ⭐ Cost buckets.** Compute (CPU), GPU, storage, network (egress/cross-region), API (per-token). GPU and per-token API dominate AI; the rest is usually rounding error. → [17.14](../weeks/17.14-cost-optimization.md)

**35. ⭐ #1 leak.** Idle/oversized/under-utilized GPUs billing at full rate. Defend with scale-to-zero/warm-minimum, batching for utilization, spot for training, right-sizing, and budget alerts. → [17.14](../weeks/17.14-cost-optimization.md)

**36. Pricing models.** Spot/preemptible (deep discount, interruptible — training/batch with checkpointing); reserved/committed (discount for a steady baseline — always-on serving floor); on-demand (full rate, no commitment — the unpredictable middle). → [17.14](../weeks/17.14-cost-optimization.md)

**37. Horizontal vs. vertical.** Horizontal adds/removes identical instances (unlimited, needs an LB) — the default for stateless serving; vertical resizes one instance (capped, disruptive) — a fallback for a single big unit. → [17.15](../weeks/17.15-autoscaling.md)

**38. ⭐ GPU autoscaling.** Harder because new GPU replicas need node scheduling, large image pulls, and weight loading into VRAM (seconds–minutes). Mitigate with warm minimums, lean images/fast weight loading, predictive/scheduled scaling, and queue backpressure. → [17.15](../weeks/17.15-autoscaling.md)

**39. ⭐ Message queue.** Decoupling: burst absorption (queue buffers spikes), fault tolerance (messages wait if a worker dies), independent scaling (scale workers on queue depth), and async responsiveness (caller returns immediately). → [17.16](../weeks/17.16-distributed-systems.md)

**40. Distributed training.** Data parallelism (each GPU a full model copy on different batches, syncing gradients) vs. model parallelism (model split across GPUs because it doesn't fit). Network-bound because gradient sync every step moves huge data between nodes. → [17.16](../weeks/17.16-distributed-systems.md)

## Part E · Ship & operate

**41. ⭐ Pipeline.** Code → Git → CI/CD (test + evals) → build → registry → staging → production → monitoring. "Build once, deploy many" = promote the same immutable image across environments, injecting per-env config/secrets, so the artifact never changes. → [17.17](../weeks/17.17-deployment.md)

**42. IaC & state.** Version-control infrastructure for reproducibility/review/rollback. Terraform state records what actually exists (mapping config to real resources); it can contain secrets, so store it remotely, encrypted, locked, never in git. → [17.18](../weeks/17.18-iac.md)

**43. Environments.** The same Terraform code with per-environment variable files (sizes, replica counts) and separate state produces dev/staging/prod — guaranteeing parity and avoiding drift; enables `destroy`-able ephemeral envs. → [17.18](../weeks/17.18-iac.md)

**44. Observability pillars.** Logs (events), metrics (time-series), traces (one request's path) + alerts. AI adds tokens, model latency, inference throughput, retrieval quality, and agent tool calls. → [17.19](../weeks/17.19-observability.md)

**45. ⭐ Why AI needs more.** AI fails quietly (`200 OK` but wrong) — infra signals look healthy while quality or cost degrades with no error; AI-specific signals and quality metrics catch it. → [17.19](../weeks/17.19-observability.md)

**46. HA/FT/DR.** High availability = redundancy so no single failure = outage; fault tolerance = graceful handling of component failures (timeout/retry/circuit-breaker); disaster recovery = recovering from large failures via backups + failover (sized by RTO/RPO). → [17.20](../weeks/17.20-reliability.md)

**47. ⭐ Graceful degradation.** Serving a reduced-but-working response instead of erroring — for an LLM app, fall back to a cached answer, a smaller model, or retrieval-only when the primary is down, so a dependency outage degrades quality rather than failing. → [17.20](../weeks/17.20-reliability.md)

**48. ⭐ Multi-cloud.** AWS/Azure/GCP implement the same primitives under different names — learn the concept once, the vendor name is a lookup. Multi-cloud is justified by lock-in avoidance, GPU availability, resilience, or residency — at the cost of complexity, egress, and doubled ops; otherwise one primary cloud + a portable core. → [17.21](../weeks/17.21-multi-cloud.md)

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 17](../README.md) |
| 📝 Quiz | [quiz-01.md](quiz-01.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
