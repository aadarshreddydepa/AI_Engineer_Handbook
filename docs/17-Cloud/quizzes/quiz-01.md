# 📝 Module 17 · Cloud for AI Engineers — Quiz 01

[🏠 Module 17](../README.md) · [📖 Lessons](../weeks/README.md) · [✅ Answers](answers-01.md)

> **48 questions across all 22 lessons.** Aim for an explanation, not just a phrase — the [answers](answers-01.md) grade reasoning. Target: **38/48** to consider the module solid.

---

## Part A · Foundations (17.1–17.4)

**1.** What is cloud computing, and what on-prem problem does elasticity solve?
**2.** Distinguish scalability, elasticity, availability, and fault tolerance.
**3.** Compare IaaS/PaaS/SaaS/serverless and when each fits an AI system.
**4.** How do regions, availability zones, and datacenters nest, and why does it matter?
**5.** What is the core high-availability pattern, and what does multi-region add over multi-AZ?
**6.** What are RTO and RPO, and how do they shape disaster recovery?
**7.** Why do GPUs beat CPUs on deep learning but not on business logic?
**8.** What is VRAM, and why is it the binding constraint on GPU workloads?
**9.** Estimate the VRAM to serve, and to full-fine-tune, a 7B model.
**10.** Walk through the single→multi→distributed→cluster GPU scaling ladder.

## Part B · Network, storage, data (17.5–17.7)

**11.** What is a VPC, and what belongs in public vs. private subnets?
**12.** How do security groups implement least privilege across tiers?
**13.** What does a load balancer provide beyond distributing traffic?
**14.** Compare block, file, and object storage; which is the AI workhorse and why?
**15.** Where do datasets, checkpoints, embeddings, and RAG documents belong?
**16.** How do you choose between relational, NoSQL, and vector databases?
**17.** Why do RAG and agent memory need a vector database?
**18.** What is the cache→DB→vector-DB access pattern, and why layer it?

## Part C · Containers & orchestration (17.8–17.10)

**19.** What is a container, how does it differ from a VM, and why does it matter for AI?
**20.** Explain image → registry → container → cloud, and why images are immutable.
**21.** How do you handle model weights and secrets in an AI container?
**22.** Explain Kubernetes as a reconciliation loop.
**23.** Deployment vs. Job vs. CronJob — which for serving, training, and batch?
**24.** How does Kubernetes schedule GPUs?
**25.** What is serverless, and why is it wrong for large models and GPU workloads?
**26.** Compare serverless, containers, and VMs.

## Part D · Architect, secure, cost, scale (17.11–17.16)

**27.** What five-layer skeleton do ML, LLM, and agent architectures share?
**28.** How do the three architectures diverge, and why?
**29.** What are the six cloud AI service categories, and why think in categories?
**30.** State the managed-vs-self-hosted trade-off and how to avoid lock-in.
**31.** Walk through the identity → authentication → authorization → resource chain.
**32.** What is least privilege, and how does it limit breach impact?
**33.** Where do secrets belong, and what must you never do with them?
**34.** What are the five cloud cost buckets, and which dominate AI?
**35.** What's the #1 AI cloud cost leak, and how do you defend against it?
**36.** When do you use spot, reserved, and on-demand pricing?
**37.** Compare horizontal and vertical scaling; why is horizontal the default?
**38.** Why is autoscaling GPU inference harder, and how do you mitigate the lag?
**39.** What does a message queue buy you over a synchronous call?
**40.** Explain data vs. model parallelism and why distributed training is network-bound.

## Part E · Ship & operate (17.17–17.21)

**41.** Walk through the CI/CD deployment pipeline; what is "build once, deploy many"?
**42.** Why version-control infrastructure, and what does Terraform state track?
**43.** How do modules and per-environment variables give dev/staging/prod parity?
**44.** What are the three pillars of observability, and what AI-specific signals do you add?
**45.** Why do AI systems need extra observability beyond infra metrics?
**46.** Distinguish high availability, fault tolerance, and disaster recovery.
**47.** What is graceful degradation, and how would you apply it to an LLM app?
**48.** What's the core insight about AWS vs. Azure vs. GCP, and when is multi-cloud justified?

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 17](../README.md) |
| ✅ Answers | [answers-01.md](answers-01.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
