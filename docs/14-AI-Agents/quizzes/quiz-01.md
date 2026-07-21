# 📝 Module 14 · AI Agents & MCP — Quiz 01

[🏠 Module 14](../README.md) · [📖 Lessons](../weeks/README.md) · [✅ Answers](answers-01.md)

> **40 questions across all 17 lessons.** Aim for an explanation, not just a phrase — the [answers](answers-01.md) grade reasoning. Target: **32/40** to consider the module solid.

---

## Part A · Build the agent (14.1–14.7)

**1.** Define an AI agent and contrast it with a chatbot, a workflow, and RAG.

**2.** "Who decides the control flow?" — how does this distinguish an agent from a workflow?

**3.** What can an agent do that a single LLM call cannot, and via which capability?

**4.** In an agent, what does the *code* own versus what the *model* owns?

**5.** Why must the loop and termination live in code, not the prompt?

**6.** Walk through decomposing a vague goal into executable actions. Where do you stop?

**7.** Compare sequential, dynamic, and hierarchical planning. What is the commitment-vs-adaptivity trade-off?

**8.** Why must every tool outcome become an observation rather than an exception?

**9.** How do you handle tool retries, and how do transient and permanent failures differ?

**10.** Why validate tool arguments, and what attacks does it prevent?

**11.** Why is an agent's memory necessarily external? Explain the RAM/disk analogy.

**12.** Walk through the memory lifecycle. Where does summarization fit, and why?

**13.** What is memory poisoning, and how do you defend against it?

**14.** What is reflection, and why does it improve reliability? When does it fail to?

**15.** Contrast self-check with grounded verification.

**16.** Compare fixed, adaptive, and event-driven loops. What termination conditions must an adaptive loop have?

**17.** How do you detect and break a degenerate (no-progress/oscillating) loop?

## Part B · Scale & connect (14.8–14.11)

**18.** When does a multi-agent system beat a single agent, and when is it the wrong choice?

**19.** What new failure modes and costs do multi-agent systems introduce? Where's the real performance win?

**20.** Why does MCP exist, and why is the "USB-C for AI" analogy apt?

**21.** Describe the MCP host/client/server architecture and the 1:1 client-server rule.

**22.** What are MCP resources, tools, and prompts, and who controls each?

**23.** Walk through the MCP connection lifecycle. What transports exist?

**24.** Why is MCP *not* a safety layer, and what must the host still enforce?

**25.** Why is context engineering harder for agents than for single prompts?

**26.** Why re-state the goal every step, and how do agents survive very long tasks?

**27.** Why should inter-agent communication be structured, and why is aggregation more than concatenation?

## Part C · Operate & deploy (14.12–14.16)

**28.** Where should a human be in the loop, and how do you avoid approval fatigue?

**29.** Why is human approval a critical defense against a hijacked agent?

**30.** Why does turning an LLM into an agent fundamentally raise the security stakes?

**31.** What is least privilege for an agent, and why is it the load-bearing control?

**32.** Explain the assume-breach mindset and how it shapes agent design.

**33.** How do you handle secrets so a hijacked agent can't leak them, and what does sandboxing protect against?

**34.** Why is task success the central agent metric? Distinguish outcome and trajectory evaluation.

**35.** How do component metrics help you localize an agent failure?

**36.** How does an agent change when it moves from notebook to production service?

**37.** Why is durable, resumable state critical, and why is trajectory tracing essential?

**38.** What do agent frameworks hide, and why build the loop by hand first?

## Part D · Synthesis (14.17)

**39.** Design an autonomous task-planner agent end-to-end (planning, tools, memory, safety, evaluation).

**40.** Defend the claim "an agent is a loop, not a prompt," and explain how you ship autonomy safely.

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 14](../README.md) |
| ✅ Answers | [answers-01.md](answers-01.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
