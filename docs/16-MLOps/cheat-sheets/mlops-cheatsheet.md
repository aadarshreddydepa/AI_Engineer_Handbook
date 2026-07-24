# 📄 Module 16 · MLOps & LLMOps — Cheat Sheet

[🏠 Module 16](../README.md) · [📖 Lessons](../weeks/README.md) · [🎴 Flashcards](../flashcards/deck.md)

> One-page reference. The whole module in one idea: **production AI is a closed loop, not train→deploy — because AI fails quietly.**

---

## 🔁 The closed loop (the whole module)

```
reproduce → version (data/model/prompt) → track → gate (registry) →
pipeline → CI/CD (eval gate) → serve → deploy (canary/shadow) →
observe → detect drift → evaluate → retrain / roll back → ↺
```
- **Train→deploy is a line. MLOps is a loop.** Only a loop catches a failure that raises no error.
- AI **fails quietly**: `200 OK` + wrong answer. Catch it with **evals, observability, drift detection** — not exceptions.

## 🧱 Foundations (16.1–16.5)

| Concept | Essence |
|---|---|
| Reproducibility | Pin **code + data + model + env + seed** — all inputs, not just code |
| Data versioning | Version by hash/snapshot (DVC/LakeFS); diff *distributions* |
| Experiment tracking | Params/metrics/artifacts/lineage per run → defensible "best model" |
| **Registry** | Versioned source of truth; **gated promotion** (eval+approval); **instant rollback** |

## 🚢 Build & ship (16.6–16.8, 16.13)

| Concept | Essence |
|---|---|
| Pipelines | Orchestration + retries + caching + lineage (Airflow/Prefect/Dagster/Kubeflow) |
| CI/CD for AI | Test **data, models, prompts, RAG/agents** — not just code |
| Eval gate | Blocks promotion on quality regression |
| Serving | **batch** (throughput) · **online** (low-latency) · **async** (queue) |
| Stacks | classic: FastAPI/BentoML/TorchServe · LLM: **vLLM/TGI** |
| Deploy | blue-green · canary · rolling · **shadow** (test on real traffic, no impact) |

## 🤖 LLMOps (16.9, 16.12, 16.14)

| Concept | Essence |
|---|---|
| LLMOps adds | version **prompts/RAG/agents**, **pin model version**, quality evals, token/cost/quality monitoring |
| LLM eval | axes: task · generation quality · safety · cost/latency — **not accuracy alone** |
| LLM-as-judge | rubric-scored by a strong model; **calibrate vs humans**, fix judge version |
| Optimization | quantization · distillation · pruning |
| Speed levers | **KV cache** (per-req) · **continuous batching** (throughput) · **speculative decoding** (latency) |

## 🛠️ Operate (16.10–16.11, 16.17–16.19)

| Concept | Essence |
|---|---|
| Observability | logs · metrics · **traces** + LLM: tokens/cost/latency/quality |
| Drift | **data** (input shifts) · **concept** (relationship shifts) · **model** (perf decays) |
| Drift tests | KS / PSI → **detect → evaluate → retrain** (drift ≠ degradation) |
| Reliability | timeout · retry+backoff · circuit breaker · rate limit/backpressure · **graceful degradation** |
| Cost | attribute per request/user/model/workflow; cut via routing/caching/trimming/batching |
| Security | **two layers** — infra (IAM/net/secrets) + AI (prompt injection, exfiltration, tool misuse); least privilege + defense-in-depth |

## 🖥️ Infrastructure (16.15–16.16, 16.21–16.22)

| Concept | Essence |
|---|---|
| GPU VRAM | model bytes + KV cache (batch×seq) + activations; full-FT ≈ **16 bytes/param** |
| Fit ladder | precision ↓ → batch/seq ↓ → KV cache tune → offload/shard → bigger/more GPUs |
| Kubernetes | pod · deployment · service · job; GPU via `nvidia.com/gpu`; autoscale + warm min |
| IaC | **Docker** (runtime) · **Terraform** (cloud) · **K8s** (orchestrate) · **Helm** (parameterize); no secrets in files |
| Cloud | SageMaker/Vertex/Azure ML = managed lifecycle; managed vs self-hosted = speed vs lock-in; keep a **portable core** |

## 🏛️ Architecture & capstones (16.20, 16.23–16.24)

- **Shared skeleton:** gateway → core → observability, on a registry + CI/CD backbone.
- **Capstone A (ML):** data+version → train+track → registry(gated) → serve → observe → **drift→retrain**.
- **Capstone B (LLM):** prompt/RAG/agent version → CI/CD **eval gate** → serve → observe tokens/cost → **regression→rollback**.
- **A vs. B = MLOps vs. LLMOps** — same loop, different failure modes.

## 🚨 Incident first-questions

| Symptom | First question |
|---|---|
| Model suddenly inaccurate | Drift or bad deploy? |
| GPU OOM | What changed in batch/seq/model size? |
| LLM cost spike | Which token driver moved? |
| Latency climbs | Queue, batch, or dependency? |
| Data shifts | Detect → evaluate → retrain? |
| Deployment fails | Roll back first, diagnose second |
| Rollback needed | Is the previous version one click away? |

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 16](../README.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
| 🎴 Flashcards | [Deck](../flashcards/deck.md) |
| 🏋️ Exercises | [Exercises](../exercises/README.md) |
