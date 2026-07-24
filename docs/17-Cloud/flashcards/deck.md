# 🧠 Module 17 · Cloud for AI Engineers — Flashcard Deck

[🏠 Module 17](../README.md) · [📖 Lessons](../weeks/README.md) · [📄 Cheat sheet](../cheat-sheets/cloud-cheatsheet.md)

> **~80 cards.** Cover the answer, say it aloud, *then* check. ⭐ marks the load-bearing ones.

---

## 17.1–17.4 · Foundations

**Q:** ⭐ What is cloud computing, in one sentence? → **A:** Renting computing resources on demand over the internet, paying per use, with elastic capacity — a utility model for compute. → [17.1](../weeks/17.1-cloud-fundamentals.md)

**Q:** Scalability vs. elasticity? → **A:** Scalability is the *capability* to grow by adding resources; elasticity is doing so *automatically and reversibly* with demand. → [17.1](../weeks/17.1-cloud-fundamentals.md)

**Q:** Availability vs. fault tolerance? → **A:** Availability is measured uptime (outcome); fault tolerance is the redundant design that produces it. → [17.1](../weeks/17.1-cloud-fundamentals.md)

**Q:** ⭐ What separates IaaS/PaaS/SaaS/serverless? → **A:** How much of the stack you manage vs. the provider — control vs. operational burden; climb to the highest rung that meets control/cost/latency/GPU needs. → [17.1](../weeks/17.1-cloud-fundamentals.md)

**Q:** How do region, AZ, and datacenter nest? → **A:** Region ⊃ AZs ⊃ datacenters; an AZ is isolated-power/cooling/network datacenter(s) that fails independently. → [17.2](../weeks/17.2-regions-availability.md)

**Q:** ⭐ The core high-availability pattern? → **A:** Redundant instances across ≥2 AZs behind a load balancer that health-checks and reroutes around failures. → [17.2](../weeks/17.2-regions-availability.md)

**Q:** RTO vs. RPO? → **A:** Recovery Time Objective (max downtime) and Recovery Point Objective (max data loss) — they drive DR strategy and cost. → [17.2](../weeks/17.2-regions-availability.md)

**Q:** ⭐ CPU vs. GPU in one line? → **A:** Few fast cores for serial logic vs. thousands of cores for parallel matrix math; deep learning is matmul, so GPUs win. → [17.3](../weeks/17.3-compute.md)

**Q:** The hybrid AI compute pattern? → **A:** CPU app tier (logic, RAG glue, orchestration) calling a GPU model tier (embeddings, LLM inference), scaled and priced independently. → [17.3](../weeks/17.3-compute.md)

**Q:** ⭐ The binding GPU constraint? → **A:** VRAM — weights + activations (+ gradients & optimizer for training) must all fit, or it won't run. → [17.4](../weeks/17.4-gpu-infrastructure.md)

**Q:** Bytes per parameter by precision? → **A:** fp32=4, fp16/bf16=2, int8=1, int4=0.5. → [17.4](../weeks/17.4-gpu-infrastructure.md)

**Q:** ⭐ Why is full fine-tuning ≈16 bytes/param? → **A:** fp16 weights(2) + grads(2) + fp32 master(4) + Adam m,v(4+4), plus activations. → [17.4](../weeks/17.4-gpu-infrastructure.md)

**Q:** GPU scaling ladder? → **A:** Single → multi-GPU (NVLink) → distributed (network-bound) → cluster; climb only when memory/speed forces it. → [17.4](../weeks/17.4-gpu-infrastructure.md)

## 17.5–17.7 · Network, storage, data

**Q:** ⭐ Public vs. private subnet — what goes where? → **A:** Public (internet route) holds the load balancer only; private (no inbound internet) holds app servers, GPU model services, databases, vector DBs. → [17.5](../weeks/17.5-networking.md)

**Q:** What is a security group and best practice? → **A:** An instance-level firewall; default-deny, allow only the specific port from the specific source per tier. → [17.5](../weeks/17.5-networking.md)

**Q:** The standard AI request path? → **A:** User → DNS → Load Balancer → App → Model service → Database/vector DB. → [17.5](../weeks/17.5-networking.md)

**Q:** ⭐ Block vs. file vs. object storage? → **A:** Block = raw disk, one VM (fastest); file = shared filesystem, many VMs; object = key→blob over HTTP, unlimited/cheap/durable — the AI workhorse. → [17.6](../weeks/17.6-storage.md)

**Q:** What goes in object storage for AI? → **A:** Datasets, checkpoints, artifacts, logs, RAG source docs — large durable read-many blobs. → [17.6](../weeks/17.6-storage.md)

**Q:** Where do embeddings go and why not object storage? → **A:** A vector DB — they need similarity search, not key lookup. → [17.6](../weeks/17.6-storage.md)

**Q:** ⭐ How do you choose an AI database? → **A:** By data/query shape: structured/transactional → SQL; flexible/by-key → NoSQL; hot values → KV cache; embeddings/similarity → vector DB. → [17.7](../weeks/17.7-databases.md)

**Q:** ⭐ Why do RAG/agent memory need a vector DB? → **A:** They retrieve by similarity (meaning) — a nearest-neighbor query relational/object stores can't do efficiently at scale. → [17.7](../weeks/17.7-databases.md)

**Q:** Classic multi-tenant RAG bug? → **A:** Missing the tenant filter on vector search, leaking other users' docs into answers. → [17.7](../weeks/17.7-databases.md)

## 17.8–17.10 · Containers & orchestration

**Q:** ⭐ What is a container and what does it solve? → **A:** An app + its exact dependencies in a portable OS-virtualized box — kills "works on my machine"; the environment travels with the code. → [17.8](../weeks/17.8-containers.md)

**Q:** Image vs. container? → **A:** Image is the immutable layered snapshot; container is a running ephemeral instance of it. → [17.8](../weeks/17.8-containers.md)

**Q:** Weights & secrets in containers? → **A:** Pull large weights from object storage at startup; inject secrets at runtime from a manager — never bake either in. → [17.8](../weeks/17.8-containers.md)

**Q:** ⭐ What is Kubernetes in one sentence? → **A:** A control loop that continuously reconciles declared desired state with reality — scheduling, healing, and scaling containers across machines. → [17.9](../weeks/17.9-kubernetes.md)

**Q:** ⭐ Deployment vs. Job? → **A:** Deployment keeps N replicas always running (serving); Job runs to completion and stops (training, batch). → [17.9](../weeks/17.9-kubernetes.md)

**Q:** ⭐ How does K8s schedule GPUs? → **A:** A pod requests `nvidia.com/gpu: N`; the scheduler places it only on a node with free GPUs and reserves them. → [17.9](../weeks/17.9-kubernetes.md)

**Q:** ⭐ When is serverless wrong for AI? → **A:** Large models, GPU workloads, long training — it's CPU-only with time/memory caps; use it as glue that delegates heavy compute. → [17.10](../weeks/17.10-serverless.md)

**Q:** Serverless vs. containers vs. VMs? → **A:** Least-ops/most-limits (serverless) → portable/orchestrated (containers) → most-control (VMs); only containers/VMs get GPUs. → [17.10](../weeks/17.10-serverless.md)

## 17.11–17.16 · Architect, secure, cost, scale

**Q:** ⭐ Shared cloud-AI skeleton? → **A:** Gateway/API → app logic → AI core (model/RAG/agent) → data stores → observability + security. → [17.11](../weeks/17.11-ai-architectures.md)

**Q:** How do ML/LLM/agent architectures differ? → **A:** In the core and dominant data store, not the shape. → [17.11](../weeks/17.11-ai-architectures.md)

**Q:** ⭐ The six AI service categories? → **A:** Managed model APIs, model hosting, training infra, GPU compute, vector search, data platforms. → [17.12](../weeks/17.12-ai-services.md)

**Q:** Managed vs. self-hosted trade-off? → **A:** Managed = speed/integration at cost of lock-in/price; keep a portable core to avoid lock-in. → [17.12](../weeks/17.12-ai-services.md)

**Q:** ⭐ What question is all cloud security asking? → **A:** Is *this identity* allowed *this action* on *this resource*? — via authentication + authorization (IAM). → [17.13](../weeks/17.13-security.md)

**Q:** ⭐ What is least privilege? → **A:** Grant every identity the minimum permissions it needs — shrinking a compromised credential's blast radius to contained. → [17.13](../weeks/17.13-security.md)

**Q:** Where do secrets belong? → **A:** In a secrets manager, injected at runtime, rotated — never in code/images/git. → [17.13](../weeks/17.13-security.md)

**Q:** Encryption at rest vs. in transit? → **A:** At rest (stolen disk/bucket unreadable) + in transit (TLS so traffic can't be sniffed) — both, everywhere. → [17.13](../weeks/17.13-security.md)

**Q:** ⭐ Five cost buckets, which dominate AI? → **A:** Compute, GPU, storage, network, API — GPU and per-token API dominate. → [17.14](../weeks/17.14-cost-optimization.md)

**Q:** ⭐ #1 AI cloud cost leak? → **A:** Idle/oversized/under-utilized GPUs billing at full rate. → [17.14](../weeks/17.14-cost-optimization.md)

**Q:** Spot vs. reserved vs. on-demand? → **A:** Spot for interruptible training/batch (with checkpointing); reserved for the steady always-on floor; on-demand for the unpredictable middle. → [17.14](../weeks/17.14-cost-optimization.md)

**Q:** How to cut per-token API cost? → **A:** Cache repeats, route easy queries to cheaper models, trim prompts, cap agent budgets. → [17.14](../weeks/17.14-cost-optimization.md)

**Q:** ⭐ Horizontal vs. vertical scaling? → **A:** Horizontal adds identical instances (default, needs LB); vertical resizes one instance (capped, disruptive, fallback). → [17.15](../weeks/17.15-autoscaling.md)

**Q:** ⭐ Why is GPU serving harder to autoscale? → **A:** New replicas need node scheduling, big image pulls, and weight loading — slow/costly; use warm minimums + predictive scaling. → [17.15](../weeks/17.15-autoscaling.md)

**Q:** Load balancer + autoscaler relationship? → **A:** The autoscaler resizes the pool; the LB spreads traffic across the current healthy pool — neither works alone. → [17.15](../weeks/17.15-autoscaling.md)

**Q:** ⭐ What does a message queue buy you? → **A:** Decoupling: burst absorption, fault tolerance, independent scaling, async responsiveness. → [17.16](../weeks/17.16-distributed-systems.md)

**Q:** Sync vs. async — when? → **A:** Sync for fast must-answer-now inference; async for slow/heavy/bursty work (embedding, batch, agents). → [17.16](../weeks/17.16-distributed-systems.md)

**Q:** Why is queue depth the ideal worker autoscaling metric? → **A:** It directly measures backlog — rising depth means scale workers out (and to zero when empty). → [17.16](../weeks/17.16-distributed-systems.md)

**Q:** ⭐ Why is distributed training network-bound? → **A:** Gradient sync every step moves huge data between nodes, so interconnect bandwidth (not FLOPs) often limits it. → [17.16](../weeks/17.16-distributed-systems.md)

## 17.17–17.22 · Ship, operate, synthesize

**Q:** ⭐ The cloud deployment pipeline? → **A:** Code → Git → CI/CD (test + evals) → build → registry → staging → production → monitoring. → [17.17](../weeks/17.17-deployment.md)

**Q:** "Build once, deploy many"? → **A:** Promote the same immutable image across environments, injecting per-env config/secrets — the artifact never changes. → [17.17](../weeks/17.17-deployment.md)

**Q:** ⭐ Why use Infrastructure as Code? → **A:** So infrastructure is version-controlled — reproducible, reviewable, recoverable — instead of console clicking. → [17.18](../weeks/17.18-iac.md)

**Q:** ⭐ What is Terraform state and why is it sensitive? → **A:** Its record of what exists; can contain secrets — store remotely, encrypted, locked, never in git. → [17.18](../weeks/17.18-iac.md)

**Q:** How do you get dev/staging/prod parity with IaC? → **A:** Same code, per-environment variable files and separate state. → [17.18](../weeks/17.18-iac.md)

**Q:** ⭐ Three observability pillars + AI signals? → **A:** Logs, metrics, traces (+ alerts); AI adds tokens, model latency, throughput, retrieval quality, tool calls. → [17.19](../weeks/17.19-observability.md)

**Q:** ⭐ Why do AI systems need extra observability? → **A:** They fail quietly (200 OK but wrong) — infra looks healthy while quality/cost degrade; AI signals catch it. → [17.19](../weeks/17.19-observability.md)

**Q:** Why are traces vital for RAG/agents? → **A:** They're multi-step; a single latency number hides which hop failed — a trace localizes it. → [17.19](../weeks/17.19-observability.md)

**Q:** HA vs. fault tolerance vs. DR? → **A:** Redundancy so no single failure = outage; graceful handling of failures; recovering from large failures via backups + failover. → [17.20](../weeks/17.20-reliability.md)

**Q:** ⭐ Graceful degradation for AI? → **A:** Fall back to a cached answer / smaller model / retrieval-only when the primary is down — degrade quality, don't fail. → [17.20](../weeks/17.20-reliability.md)

**Q:** ⭐ Core insight about AWS vs. Azure vs. GCP? → **A:** They implement the same primitives under different names — learn the concept once; the vendor name is a lookup. → [17.21](../weeks/17.21-multi-cloud.md)

**Q:** When is multi-cloud justified? → **A:** Lock-in avoidance, GPU availability, provider-outage resilience, data residency — at the cost of complexity/egress/ops; else one cloud + portable core. → [17.21](../weeks/17.21-multi-cloud.md)

**Q:** ⭐ The single takeaway of Module 17? → **A:** The cloud is a small set of transferable primitives; production AI engineering is composing them into secure, cost-controlled, scalable, observable, reliable systems. → [17.22](../weeks/17.22-projects-summary.md)

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 17](../README.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
| 📄 Cheat sheet | [Cloud cheat sheet](../cheat-sheets/cloud-cheatsheet.md) |
