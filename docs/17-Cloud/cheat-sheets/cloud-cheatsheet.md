# 📄 Module 17 · Cloud for AI Engineers — Cheat Sheet

[🏠 Module 17](../README.md) · [📖 Lessons](../weeks/README.md) · [🎴 Flashcards](../flashcards/deck.md)

> One-page reference. The whole module in one idea: **the cloud is a small set of transferable primitives — learn the concept once; the vendor name is a lookup.**

---

## ☁️ Foundations (17.1–17.2)

| Concept | Essence |
|---|---|
| **Cloud** | rent computing on demand, pay per use; a utility |
| **Elasticity** | capacity auto-grows/shrinks with load (reversible) |
| **IaaS→PaaS→serverless→SaaS** | how much of the stack *you* manage: most → least |
| **Region ⊃ AZ ⊃ datacenter** | nested independent failure domains |
| **⭐ HA pattern** | redundant replicas across ≥2 AZs behind a load balancer |
| **RTO / RPO** | max downtime / max data loss → drives DR |

## 🖥️ Compute & GPU (17.3–17.4)

| Concept | Essence |
|---|---|
| **CPU vs GPU vs TPU** | few fast cores (logic) · thousands of cores (matmul) · matmul ASIC |
| **⭐ VRAM** | the constraint — model must *fit* or it won't run |
| **Bytes/param** | fp32=4 · fp16=2 · int8=1 · int4=0.5 |
| **Full-FT VRAM** | ≈16 bytes/param + activations |
| **Fit ladder** | precision↓ → LoRA/QLoRA → bigger GPU → multi-GPU → distributed |
| **⭐ Rule** | matmul → GPU; plumbing → CPU; keep GPUs busy, never idle |

## 🌐 Network · storage · data (17.5–17.7)

| Concept | Essence |
|---|---|
| **VPC** | your isolated private network |
| **Public / private subnet** | LB only / app·model·DB·vector (no inbound internet) |
| **Security group** | instance firewall; default-deny, allow per port+source |
| **Path** | User → DNS → LB → App → Model → DB |
| **Block/file/object** | disk (one VM) / shared FS / **key→blob (AI workhorse)** |
| **Object storage** | datasets, checkpoints, artifacts, logs, RAG docs |
| **⭐ Vector DB** | embeddings — similarity search for RAG/agent memory |
| **Access pattern** | cache → DB → vector DB |

## 📦 Containers · orchestration · serverless (17.8–17.10)

| Concept | Essence |
|---|---|
| **Container** | app + deps, portable, OS-virtualized; kills "works on my machine" |
| **Flow** | Source → Dockerfile → Image → Registry → Container → Cloud |
| **⭐ AI rule** | CUDA base; pin deps; weights & secrets **not** baked in |
| **Kubernetes** | reconcile desired state; schedule/heal/scale containers |
| **Deployment / Job** | always-on replicas (serving) / run-to-completion (train, batch) |
| **⭐ GPU scheduling** | pod requests `nvidia.com/gpu`; scheduler places on GPU node |
| **Serverless** | functions per-event, scale-to-zero — glue, **not** GPU/large models |

## 🏛️ Architect · secure · cost · scale (17.11–17.16)

| Concept | Essence |
|---|---|
| **⭐ Skeleton** | gateway → app → **AI core** → data → observability+security |
| **Service categories** | model APIs · hosting · training · GPU · vector · data platforms |
| **⭐ Identity chain** | identity → authN → authZ (IAM) → resource |
| **⭐ Least privilege** | minimum permissions; deny-all default; shrinks blast radius |
| **Secrets / encryption** | vaulted, injected at runtime / at rest (KMS) + in transit (TLS) |
| **⭐ Cost buckets** | GPU + API dominate AI; compute/storage/network smaller |
| **Cost levers** | right-size · scale-to-zero · spot(train) · reserved(steady) · cache · batch |
| **Autoscaling** | horizontal (default, +LB) vs vertical; warm min for GPU |
| **⭐ Message queue** | decouple → burst-absorb · fault-tolerant · scale · async |
| **Distributed training** | data/model parallel; **network-bound** |

## 🚀 Ship & operate (17.17–17.21)

| Concept | Essence |
|---|---|
| **Deploy pipeline** | Code→Git→CI/CD→build→registry→staging→prod→monitor |
| **Build once, deploy many** | same image, per-env config/secrets |
| **⭐ IaC (Terraform)** | infra as versioned code; plan/apply/destroy; state = sensitive |
| **Environments** | same code, per-env variables (dev/staging/prod) |
| **Observability** | logs·metrics·traces·alerts + tokens/latency/throughput/retrieval |
| **⭐ Why AI obs** | AI fails quietly — AI signals catch what infra misses |
| **Reliability** | HA · fault tolerance · DR · backups · failover |
| **⭐ Graceful degradation** | cached / smaller model / retrieval-only, don't error |

## 🗺️ AWS · Azure · GCP mapping (17.21)

| Concept | AWS | Azure | GCP |
|---|---|---|---|
| VM | EC2 | Virtual Machines | Compute Engine |
| GPU | EC2 P/G | N-series | GPU on Compute Engine |
| Serverless | Lambda | Functions | Cloud Functions/Run |
| Object storage | S3 | Blob Storage | Cloud Storage |
| Block storage | EBS | Managed Disks | Persistent Disk |
| Relational DB | RDS/Aurora | Azure SQL | Cloud SQL/Spanner |
| NoSQL | DynamoDB | Cosmos DB | Firestore/Bigtable |
| Managed K8s | EKS | AKS | GKE |
| Private network | VPC | VNet | VPC |
| Firewall | Security Groups | NSG | Firewall rules |
| Load balancer | ELB/ALB/NLB | Load Balancer/App Gateway | Cloud Load Balancing |
| DNS | Route 53 | Azure DNS | Cloud DNS |
| Managed model API | Bedrock | Azure OpenAI | Vertex/Gemini |
| ML platform | SageMaker | Azure ML | Vertex AI |
| Registry | ECR | ACR | Artifact Registry |
| Secrets | Secrets Manager | Key Vault | Secret Manager |
| IAM | IAM | Entra ID/RBAC | Cloud IAM |

**⭐ Portable core (anti-lock-in):** Kubernetes · Terraform · Docker · MLflow · open formats (safetensors/ONNX/parquet).

## 🚨 Incident first-questions

| Symptom | First question |
|---|---|
| GPU instance unavailable | Another AZ/region/type? Fallback? |
| Costs suddenly increase | Which bucket — GPU/API/egress? |
| App becomes slow | Which hop? Autoscaling? Trace it |
| Database unreachable | Network first, then DB/failover |
| Pod crashes (CrashLoop) | Logs: config/secret/OOM/probe? |
| Deployment fails | Which stage? Staging vs prod diff? |
| Network access blocked | Security group/subnet/route? |
| Storage perms misconfigured | IAM/bucket policy; public? |

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 17](../README.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
| 🎴 Flashcards | [Deck](../flashcards/deck.md) |
| 🏋️ Exercises | [Exercises](../exercises/README.md) |
