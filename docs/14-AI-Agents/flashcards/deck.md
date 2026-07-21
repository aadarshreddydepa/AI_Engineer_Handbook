# 🧠 Module 14 · AI Agents & MCP — Flashcard Deck

[🏠 Module 14](../README.md) · [📖 Lessons](../weeks/README.md) · [📄 Cheat sheet](../cheat-sheets/agents-cheatsheet.md)

> **~95 cards.** Cover the answer, say it aloud, *then* check. ⭐ marks the load-bearing ones.

---

## 14.1 · What Are Agents?

**Q:** ⭐ What is an AI agent? → **A:** An LLM running in a loop that observes, decides on an action (usually a tool call), executes it, observes the result, and repeats until a goal is met. → [14.1](../weeks/14.1-what-are-agents.md)

**Q:** ⭐ Agent vs workflow — the defining difference? → **A:** In a workflow the *developer* hardcodes the steps; in an agent the *LLM* decides them dynamically at runtime.

**Q:** Agent vs RAG? → **A:** RAG is a fixed retrieve-then-generate step; an agent may use retrieval as one of many tools, repeatedly, choosing when.

**Q:** The agent loop stages? → **A:** Perceive → reason → plan → act → observe → reflect (repeat).

**Q:** When should you NOT use an agent? → **A:** When the task path is fixed/known — a workflow is cheaper, faster, more reliable.

---

## 14.2 · Architecture

**Q:** ⭐ Where does the agent loop live? → **A:** In your code; the LLM is a stateless decision function called once per step, while the loop, budget, validation, and memory are code. → [14.2](../weeks/14.2-agent-architecture.md)

**Q:** What does the model own vs the code own? → **A:** Model: which tool, which args, when to finish. Code: the loop, budgets, validation, execution, error handling, memory.

**Q:** What is the ReAct loop? → **A:** Interleave reasoning, acting (tool call), and observing the result each iteration until done.

**Q:** ⭐ Why must the code own termination? → **A:** The model can loop forever or forget to stop; a code-owned max_steps/budget guarantees the loop ends.

**Q:** Why structured decisions, not free text? → **A:** Reliable, validatable tool selection and arguments.

---

## 14.3 · Planning

**Q:** What is agent planning? → **A:** Decomposing a goal into sub-goals, tasks, and finally tool-callable actions, then sequencing them. → [14.3](../weeks/14.3-planning.md)

**Q:** How far should you decompose? → **A:** To the tool level — until each leaf maps to one available tool call.

**Q:** ⭐ Sequential vs dynamic vs hierarchical? → **A:** Plan-all-up-front (fast, brittle) vs plan-each-step (adaptive, can wander) vs layered high-level+local.

**Q:** ⭐ The core planning trade-off? → **A:** Commitment vs adaptivity; the pragmatic middle is plan-and-execute with re-planning.

**Q:** When should an agent re-plan? → **A:** When a step fails, an assumption breaks, the goal changes, or it's looping without progress.

---

## 14.4 · Tool Calling

**Q:** ⭐ Why is the tool layer so important? → **A:** An agent can only *do* what its tools allow — capability, reliability, and safety all live there. → [14.4](../weeks/14.4-tool-calling.md)

**Q:** ⭐ What should happen when a tool call fails? → **A:** It becomes a structured error observation the agent can read and recover from — never a crash.

**Q:** How do you handle retries? → **A:** Bounded exponential backoff for transient failures only; don't retry permanent ones (bad args, 403).

**Q:** Why validate tool arguments? → **A:** They're untrusted model output; unvalidated args into SQL/shell/paths are an injection vector.

**Q:** Why return structured, trimmed results? → **A:** Raw/huge results flood the context, bury the signal, and balloon cost.

---

## 14.5 · Memory

**Q:** ⭐ Why does an agent need external memory? → **A:** The LLM is stateless — it only sees the context window — so persistence across steps/sessions is an external system. → [14.5](../weeks/14.5-memory.md)

**Q:** Working (RAM) vs long-term (disk)? → **A:** Working = current task's goal + recent observations in context; long-term = durable facts/episodes in a store, retrieved when relevant.

**Q:** Semantic vs episodic memory? → **A:** Semantic = general facts; episodic = records of specific past task runs. Both usually via a vector store.

**Q:** ⭐ Memory lifecycle stages? → **A:** Write → retrieve → summarize → prune → persist.

**Q:** How do agents survive long tasks in a finite window? → **A:** Summarize old history into a running summary and prune stale items.

**Q:** What is memory poisoning? → **A:** An attacker writes malicious content to long-term memory to influence future runs — a persistent injection; scope/validate writes, treat recall as data.

---

## 14.6 · Reflection

**Q:** What is agent reflection? → **A:** A self-evaluate → detect error → correct → verify loop where the agent checks its own work and fixes mistakes instead of carrying them forward. → [14.6](../weeks/14.6-reflection.md)

**Q:** ⭐ Why does reflection improve reliability? → **A:** It adds an error signal to a single probabilistic attempt, so the agent can detect and recover.

**Q:** ⭐ When does reflection help most/least? → **A:** Most with a grounded signal (test result, tool error, checkable constraint); least as pure self-critique (can rationalize).

**Q:** Why bound reflection? → **A:** It's extra LLM calls; unbounded correct/verify loops run away and may never terminate.

**Q:** Where is reflection also a safety control? → **A:** Before irreversible/high-impact actions — verify (and often get approval) first.

---

## 14.7 · Loops

**Q:** ⭐ Fixed vs adaptive vs event-driven loops? → **A:** Fixed runs N steps (predictable, inflexible); adaptive continues until goal/budget (flexible, needs guardrails); event-driven acts on events (reactive, idle-cheap). → [14.7](../weeks/14.7-agent-loops.md)

**Q:** ⭐ Most important loop-control decision? → **A:** The termination condition + budget — a probabilistic agent with no hard stop will run away.

**Q:** Termination conditions for an adaptive loop? → **A:** Goal achieved, step budget, cost/time budget, no-progress, oscillation, fatal error.

**Q:** What does graceful degradation mean? → **A:** Returning the best partial result at the budget rather than running forever or failing hard.

---

## 14.8 · Multi-Agent

**Q:** What is a multi-agent system? → **A:** Several specialized agents (each its own loop/prompt/tools) collaborating — like an org with a manager, specialists, and a reviewer. → [14.8](../weeks/14.8-multi-agent.md)

**Q:** ⭐ When should you use multi-agent over single? → **A:** Only for a concrete reason: too many tools, context overload, genuine parallelism, need for a reviewer, or conflicting expertise.

**Q:** Coordination patterns? → **A:** Hierarchical, sequential, parallel, debate/critique.

**Q:** ⭐ Main cost of multi-agent systems? → **A:** Multiplied LLM cost/latency plus new failure modes (miscommunication, coordination bugs, harder debugging).

**Q:** Where's the real performance win? → **A:** Parallelizing independent subtasks.

---

## 14.9 · MCP

**Q:** ⭐ Why does MCP exist? → **A:** To replace M×N bespoke app-tool integrations with M+N: each app implements a client once, each tool a server once. → [14.9](../weeks/14.9-mcp.md)

**Q:** ⭐ Host, client, server? → **A:** Host = the AI app (LLM + clients); client = in the host with a 1:1 link to a server; server = exposes capabilities wrapping a data source/service.

**Q:** ⭐ The three server primitives and who controls each? → **A:** Resources (application-controlled, read-only data by URI), tools (model-controlled actions), prompts (user-controlled templates).

**Q:** How does an MCP connection start? → **A:** An `initialize` handshake negotiating protocol version and capabilities, confirmed by an `initialized` notification.

**Q:** MCP transports? → **A:** stdio (local subprocess) and Streamable HTTP with SSE (remote); the JSON-RPC messages are identical.

**Q:** Is MCP a security layer? → **A:** No — it standardizes transport/discovery; the host still enforces validation, least privilege, sandboxing, and approvals.

---

## 14.10 · Context & 14.11 · Communication

**Q:** ⭐ Why is context engineering harder for agents? → **A:** You re-select the context every step while it grows with each action/observation; naive appending overflows the window. → [14.10](../weeks/14.10-context-engineering.md)

**Q:** What is dynamic context assembly? → **A:** Rebuilding context each step from structured state (goal + summary + recall + last observation) instead of appending.

**Q:** ⭐ Why re-state the goal each step? → **A:** Otherwise the agent drifts, optimizing the latest observation instead of the objective.

**Q:** ⭐ Why structured messages between agents? → **A:** One LLM's output becomes another's input; a schema turns a fuzzy chat into a reliable contract. → [14.11](../weeks/14.11-communication.md)

**Q:** Why is aggregation not concatenation? → **A:** Merging requires validating, de-duplicating, and reconciling contradictions.

---

## 14.12 · Human-in-the-Loop

**Q:** ⭐ Where do you put the human in the loop? → **A:** At high-stakes, irreversible, or low-confidence moments where judgment is worth the delay — not every step. → [14.12](../weeks/14.12-human-in-the-loop.md)

**Q:** The intervention patterns? → **A:** Approval workflows, review checkpoints, manual override, escalation, feedback collection.

**Q:** ⭐ How do you calibrate approval frequency? → **A:** By impact and reversibility; too many prompts cause approval fatigue (blind approval).

**Q:** Why is human approval a security control? → **A:** It's the last line of defense if injection hijacks the agent toward a destructive action.

---

## 14.13 · Safety

**Q:** ⭐ Why is agent safety more critical than chatbot safety? → **A:** An agent takes actions, so a hijack causes real damage, not just a bad message. → [14.13](../weeks/14.13-safety.md)

**Q:** ⭐ The single most important agent-safety control, and why? → **A:** Least privilege — it contains the agent regardless of how it's compromised; no capability means no injection can invoke it.

**Q:** The assume-breach mindset? → **A:** Design so even a fully hijacked agent does little damage — ask "what's the blast radius?"

**Q:** Why never put secrets in the context? → **A:** They can leak via injection or logging; keep them server-side.

**Q:** What does sandboxing contain? → **A:** Both bugs and hijacks — isolated execution stops code/file/shell tools escaping or reaching sensitive data.

**Q:** Why is one safety control never enough? → **A:** Each can fail; defense-in-depth forces defeating several layers, with least privilege underlying all.

---

## 14.14 · Evaluation

**Q:** ⭐ The top-line agent metric? → **A:** Task success rate — did it accomplish the goal — because agents are judged by outcomes. → [14.14](../weeks/14.14-evaluation.md)

**Q:** ⭐ Outcome vs trajectory evaluation? → **A:** Outcome = did the final state meet the goal; trajectory = was the path efficient/correct.

**Q:** What makes a good agent test case? → **A:** A goal, a sandboxed initial environment, and a programmatic end-state success check.

**Q:** Why run each task multiple times? → **A:** Agents are probabilistic; reliability/consistency need repeated runs.

**Q:** What must an agent eval suite include beyond happy paths? → **A:** Edge cases, adversarial/injection tasks (safety), and unachievable goals (graceful give-up).

---

## 14.15 · Production & 14.16 · Frameworks

**Q:** ⭐ Why is a production agent a distributed system? → **A:** It's stateful, long-running, action-taking, and cost-unpredictable — needing durable state, resumability, per-component scaling, security, and deep observability. → [14.15](../weeks/14.15-production-architecture.md)

**Q:** ⭐ Why is durable, resumable state essential? → **A:** Tasks span many steps and may pause for approval; per-step checkpoints let the agent survive restarts and resume.

**Q:** ⭐ Why is observability deeper for agents? → **A:** You must trace the full reasoning trajectory (decisions, tool calls, observations) to debug misbehavior — also the safety audit trail.

**Q:** Where do agent security controls concentrate? → **A:** The tool manager — validation, sandboxing, rate limits, permission gates, audit.

**Q:** ⭐ What do agent frameworks hide? → **A:** The loop, budgets, validation, memory assembly, and guardrails — the parts that determine reliability and safety. → [14.16](../weeks/14.16-frameworks.md)

**Q:** Do frameworks make agents safe by default? → **A:** No — you must explicitly configure least privilege, sandboxing, approvals, and budgets.

**Q:** ⭐ Why build the loop by hand before a framework? → **A:** So you can see through the abstraction — tune what matters and debug/secure it when it breaks.

---

## 14.17 · Summary

**Q:** ⭐ The one thing to remember from agents? → **A:** An agent is a loop, not a prompt — the LLM decides, and your code controls the loop, tools, memory, budget, and gates. → [14.17](../weeks/14.17-projects-summary.md)

**Q:** Where does each agent capability come from? → **A:** Capability from tools, continuity from memory, connectivity from MCP, reliability from reflection/evaluation, safety from least privilege/containment.

**Q:** How do you ship autonomy safely? → **A:** By bounding it — budgets, least privilege, human gates, and evaluation.

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 14](../README.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
| 📄 Cheat sheet | [Agents cheat sheet](../cheat-sheets/agents-cheatsheet.md) |
| 📝 Quiz | [Quiz 01](../quizzes/quiz-01.md) |
