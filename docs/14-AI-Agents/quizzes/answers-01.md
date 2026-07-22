# ✅ Module 14 · AI Agents & MCP — Quiz 01 Answers

[🏠 Module 14](../README.md) · [📝 Quiz](quiz-01.md) · [📖 Lessons](../weeks/README.md)

> Model answers grade **reasoning**. Full credit = the key idea explained, not just a keyword.

---

## Part A · Build the agent

**1.** An **agent** is an LLM running in a loop that observes, decides an action (usually a tool call), executes it, observes the result, and repeats until a goal is met. Vs a **chatbot** (turn-based Q&A, no autonomous multi-step action), an **LLM call** (one shot, no actions), **RAG** (a fixed retrieve-then-generate step), and a **workflow** (developer-hardcoded steps). → [14.1](../weeks/14.1-what-are-agents.md)

**2.** In a workflow the **developer** writes the steps and the LLM fills in blanks; in an agent the **LLM decides at runtime** which tool to call, in what order, and when it's done. That runtime control-flow decision is the defining property (and the source of both power and risk). → [14.1](../weeks/14.1-what-are-agents.md)

**3.** Take **actions** (via tools), do **dependent multi-step** tasks (the loop), **recover from errors** (reflection), **remember across steps** (memory), and **choose its own path** (planning) — each capability maps to an agent component. → [14.1](../weeks/14.1-what-are-agents.md)

**4.** **Code owns:** the loop, `max_steps`/cost budget, argument validation, tool execution, error handling, memory, and permissions. **Model owns:** which tool to call, which arguments, and when to finish. *Model decides, code controls.* → [14.2](../weeks/14.2-agent-architecture.md)

**5.** A probabilistic model can loop forever, forget to stop, or oscillate between actions; a **code-owned budget and termination** guarantees the loop ends and can stop mid-task with a partial answer. Control logic in the prompt is unreliable. → [14.2](../weeks/14.2-agent-architecture.md)

**6.** Decompose **goal → sub-goals → tasks → actions → results**, stopping **at the tool level** — when each leaf maps to one available tool call. Finer is over-planning; a leaf with no tool is a capability gap. → [14.3](../weeks/14.3-planning.md)

**7.** **Sequential** plans all steps up front (fast, brittle to surprises); **dynamic** plans each step from observations (adaptive, can wander); **hierarchical** plans in layers (structure + local adaptivity). The **commitment-vs-adaptivity** trade-off: static commits early (efficient but stale-prone), dynamic adapts (flexible but costlier/driftier) — resolved by **plan-and-execute with re-planning**. → [14.3](../weeks/14.3-planning.md)

**8.** Because the agent's ability to **recover** depends on *seeing* what happened ([14.6](../weeks/14.6-reflection.md)); a crash ends the loop, while an error observation ("invalid args: …") lets the model read it and correct next step. Turn failures into feedback. → [14.4](../weeks/14.4-tool-calling.md)

**9.** **Bounded exponential-backoff retries for transient failures** (network, rate limit, timeout); **no retry for permanent failures** (bad args, 403, 404 — they never succeed and waste calls/loop). Cap retries; they multiply cost/latency. → [14.4](../weeks/14.4-tool-calling.md)

**10.** Tool arguments are **untrusted model output**; unvalidated args into SQL/shell/eval/file paths/URLs enable injection, crashes, and data loss. Validation (schema + business rules) is the first safety layer. → [14.4](../weeks/14.4-tool-calling.md)

**11.** The LLM is **stateless** — each call only sees the context window — so persistence across steps/sessions must be built externally. The window is **RAM** (small, fast, volatile: working memory); external stores are **disk** (large, durable, slow: long-term/semantic/episodic), shuffled via retrieval. → [14.5](../weeks/14.5-memory.md)

**12.** **Write → retrieve → summarize → prune → persist.** Summarization sits between retrieve and prune: when task history exceeds the window, compress old observations into a running summary so the agent can **survive long tasks** without overflowing. → [14.5](../weeks/14.5-memory.md)

**13.** An attacker writes **malicious content into long-term memory** so it influences **future** runs — a persistent injection. Defend by scoping/validating what gets written, partitioning by tenant, and treating recalled memory as **untrusted data**. → [14.5](../weeks/14.5-memory.md)

**14.** Reflection = self-evaluate → detect error → correct → verify. It adds an **error signal** to a single probabilistic attempt so the agent detects and recovers instead of propagating mistakes. It **fails** as pure self-critique with no grounded signal (it can rationalize a wrong answer). → [14.6](../weeks/14.6-reflection.md)

**15.** **Self-check** re-reads the agent's own output against the goal (cheap, catches obvious gaps, can rationalize); **verification** re-derives or tests against **external truth** (run the code, check the data, confirm the source) — more robust, costs more. → [14.6](../weeks/14.6-reflection.md)

**16.** **Fixed** runs N steps (predictable, inflexible); **adaptive** continues until goal/budget (flexible, needs guardrails — the default); **event-driven** acts on external events (reactive, idle-cheap). Adaptive termination: **goal achieved, step budget, cost/time budget, no-progress, oscillation, fatal error**. → [14.7](../weeks/14.7-agent-loops.md)

**17.** Track recent actions/observations: **same action repeated**, an **A→B→A→B oscillation**, or **observations adding no new information** → declare stuck and **stop or re-plan** ([14.3](../weeks/14.3-planning.md)). Enforce in code. → [14.7](../weeks/14.7-agent-loops.md)

## Part B · Scale & connect

**18.** Use multi-agent only for a **concrete reason**: too many tools for one agent to select well, context overload, genuine parallelism, a needed independent reviewer, or conflicting expertise. Otherwise a single agent is cheaper, faster, and less buggy. → [14.8](../weeks/14.8-multi-agent.md)

**19.** New costs/failures: **multiplied LLM cost/latency**, miscommunication between agents, coordination deadlocks, and harder debugging (which agent failed?). The real performance win is **parallelizing independent subtasks** — a sequential multi-agent chain is just slower. → [14.8](../weeks/14.8-multi-agent.md)

**20.** MCP replaces **M×N** bespoke integrations (M apps × N tools) with **M+N**: each app implements a client once, each tool a server once, and any client talks to any server through one protocol — exactly like USB-C: one standard port, universal interoperability. → [14.9](../weeks/14.9-mcp.md)

**21.** **Host** = the AI app (holds the LLM and manages clients); **client** = lives in the host with a **1:1 stateful connection** to one server; **server** = a lightweight program exposing capabilities, wrapping a data source/service. The host composes many clients (one per server), keeping servers isolated. → [14.9](../weeks/14.9-mcp.md)

**22.** **Resources** (application-controlled) — read-only, file-like data by **URI**; **tools** (model-controlled) — functions with a JSON-Schema the LLM calls; **prompts** (user-controlled) — reusable templates/workflows the user triggers. → [14.9](../weeks/14.9-mcp.md)

**23.** **Initialize** (client sends protocol version + capabilities → server replies with its capabilities → client confirms with `initialized`) → **operate** (`tools/list`, `tools/call`, `resources/read`, etc.) → **shutdown**. Transports: **stdio** (local subprocess) and **Streamable HTTP with SSE** (remote); same JSON-RPC messages. → [14.9](../weeks/14.9-mcp.md)

**24.** MCP standardizes **transport and discovery**, not safety — a malicious server can expose dangerous tools or return injected content. The **host** still validates arguments, scopes servers to least privilege, sandboxes untrusted servers, and gates high-impact actions. → [14.9](../weeks/14.9-mcp.md)

**25.** In a single prompt you choose context **once**; in an agent you re-choose it **every step** while it **grows** (each iteration adds a decision, action, and observation), so naive appending overflows the window and buries the signal in the ignored middle. → [14.10](../weeks/14.10-context-engineering.md)

**26.** Re-state the goal each step because as history compresses/scrolls the agent **drifts** — optimizing the latest observation instead of the objective. Long tasks survive via **rolling summarization** of old steps, **externalizing** findings to memory, and giving sub-agents **focused contexts**. → [14.10](../weeks/14.10-context-engineering.md)

**27.** One LLM's output becomes another's input, so **ambiguity compounds** — a schema (task/inputs/expected output) makes each hand-off a reliable **contract**. **Aggregation** must validate, de-duplicate, and **reconcile contradictions** between workers, not glue outputs together (which yields incoherent results). → [14.11](../weeks/14.11-communication.md)

## Part C · Operate & deploy

**28.** Put the human at **high-stakes, irreversible, or low-confidence** moments (approve before send/delete/pay/deploy). Avoid **approval fatigue** by calibrating on **impact and reversibility** — gate irreversible/high-cost actions, let reversible low-stakes ones run free; too many prompts cause blind approval. → [14.12](../weeks/14.12-human-in-the-loop.md)

**29.** If injection hijacks the agent toward a destructive action, the **approval gate** is the last line of defense — a human sees the action (with args, rationale, impact) and blocks it. That's why high-impact actions must be **gated, not merely logged**. → [14.12](../weeks/14.12-human-in-the-loop.md)

**30.** A hijacked chatbot writes a bad message; a hijacked **agent takes a bad action** (deletes data, sends money, leaks secrets). Agents read untrusted content (web/files/tool results) that can carry injection, so the consequences are **real-world side effects**. → [14.13](../weeks/14.13-safety.md)

**31.** Give the agent the **minimum tools/access** its task needs (read-only by default). It's load-bearing because it works **regardless of how** the agent is compromised — you can't enumerate every injection, but you *can* ensure the agent simply **lacks the capability** to do catastrophic things. → [14.13](../weeks/14.13-safety.md)

**32.** **Assume the agent will be hijacked** and design so that even a fully compromised agent **can't do much damage** — the question is "what's the blast radius?" not "will it be tricked?" This drives least privilege, sandboxing, rate limits, gates, and audit. → [14.13](../weeks/14.13-safety.md)

**33.** Keep secrets in a **secrets manager**; tools use them **server-side** so they never enter the context (where injection/logging could leak them). **Sandboxing** isolates code/file/shell execution (containers, no network, resource/time limits) so even malicious code can't escape or reach sensitive data — containing both bugs and hijacks. → [14.13](../weeks/14.13-safety.md)

**34.** An agent is judged by **outcomes** — did it accomplish the goal — so **task success rate** is the headline. **Outcome** evaluation checks whether the final state meets the goal; **trajectory** evaluation checks whether the *path* was efficient/correct (an agent can reach a right answer via a slow, expensive, or lucky path). → [14.14](../weeks/14.14-evaluation.md)

**35.** Success rate is the "what"; **component metrics** (tool accuracy, planning accuracy, memory recall) are the "why." E.g., high per-tool accuracy but low task success localizes the failure to **planning** (uses tools correctly but sequences them poorly), pointing the fix precisely. → [14.14](../weeks/14.14-evaluation.md)

**36.** It becomes a **distributed, service-oriented system**: **durable, resumable state** (checkpoint each step), **per-component scaling** (stateless orchestrator + state store), **deep observability** (trajectory tracing), **centralized budgets and tool security** (the tool manager), **human-in-the-loop pauses**, and **tenant isolation** — because agents are stateful, long-running, action-taking, and cost-unpredictable. → [14.15](../weeks/14.15-production-architecture.md)

**37.** Tasks span many steps and may **pause for approval**, so persisting state per step lets the agent **survive restarts and resume**. **Trajectory tracing** (every decision, tool call, observation) is essential because agent misbehavior's *why* is buried in the step sequence — it's both the debugging tool and the safety audit trail; you can't operate an agent you can't see. → [14.15](../weeks/14.15-production-architecture.md)

**38.** Frameworks hide the **loop, budgets, validation, memory assembly, and guardrails** — the parts that determine reliability and safety. Building the loop by hand first lets you **see through the abstraction**: know what it does, tune the knobs that matter (budgets, permissions), and debug/secure it when it breaks. Frameworks aren't safe by default. → [14.16](../weeks/14.16-frameworks.md)

## Part D · Synthesis

**39.** A strong answer: define the **goal + programmatic success check**; **hierarchical planning with re-planning** ([14.3](../weeks/14.3-planning.md)); a **least-privilege toolset** (some via MCP, [14.9](../weeks/14.9-mcp.md)); the **full memory stack** with summarization ([14.5](../weeks/14.5-memory.md), [14.10](../weeks/14.10-context-engineering.md)); **reflection/verification before irreversible actions** ([14.6](../weeks/14.6-reflection.md)); **human approval gates** on high-impact actions ([14.12](../weeks/14.12-human-in-the-loop.md)); a **step/cost budget** and termination ([14.7](../weeks/14.7-agent-loops.md)); a **safety harness** (sandbox, secrets, rate limits, audit, [14.13](../weeks/14.13-safety.md)); and **evaluation on task success + cost + an adversarial safety sub-suite** ([14.14](../weeks/14.14-evaluation.md)), all as a **service** with durable state and trajectory tracing ([14.15](../weeks/14.15-production-architecture.md)). → [14.17](../weeks/14.17-projects-summary.md)

**40.** The LLM only **decides**; the **loop, tools, memory, budget, validation, and gates are code** — so the agent's behavior, reliability, and safety live in the engineering *around* the model, not the model itself. You **ship autonomy by bounding it**: step/cost budgets and termination, least-privilege tools and sandboxing, human approval on irreversible actions, and task-success evaluation — autonomy is powerful and dangerous in equal measure, and the discipline is containment. → [14.17](../weeks/14.17-projects-summary.md)

---

## Scoring

| Score | Verdict |
|---|---|
| 36–40 | Excellent — you can design, build, secure, evaluate, and deploy agents. |
| 32–35 | Solid — review the missed lessons. |
| 24–31 | Partial — re-read 14.2, 14.4, 14.9, 14.13 (the load-bearing four). |
| < 24 | Re-study the module; redo ⭐ exercises E2, E4, E9, E13, E15. |

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 14](../README.md) |
| 📝 Quiz | [quiz-01.md](quiz-01.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
