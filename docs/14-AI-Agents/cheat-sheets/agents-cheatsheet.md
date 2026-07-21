# 📄 AI Agents & MCP — Cheat Sheet

[🏠 Module 14](../README.md) · [📖 Lessons](../weeks/README.md)

---

## 🧠 The core facts

| | |
|---|---|
| **⭐ What an agent is** | an LLM in a **loop** with tools, memory, and a goal |
| **⭐ Core truth** | an agent is a **loop, not a prompt** — model decides, **code controls** |
| **Loop** | perceive → reason → plan → act → observe → reflect → repeat |
| **vs workflow** | **the LLM** decides the steps (not the developer) |
| **vs RAG** | RAG is one fixed step; an agent chooses tools dynamically |
| **Brain/hands/notebook/leash** | LLM / tools / memory / permissions |

---

## 🏗️ Architecture (14.2)

- **Code owns:** the loop, `max_steps`/budget, arg validation, execution, memory, permissions.
- **Model owns:** which tool, which args, when to finish.
- **Decisions are structured** (`{thought, tool, args}` / `{finish, answer}`).
- Architectures: **single-step < ReAct < plan-and-execute < reflection** (compose them).
- **Never** let the model own termination or execute unvalidated args.

---

## 🗺️ Planning (14.3)

- Decompose: **goal → sub-goals → tasks → actions (tool calls) → results**; stop at the tool level.
- **Sequential** (plan up front) · **dynamic/ReAct** (plan each step) · **hierarchical** (layered).
- ⭐ Trade-off: **commitment vs adaptivity** → default **plan-and-execute with re-planning**.

---

## 🔧 Tools (14.4)

- **Capabilities = tools, nothing more.**
- Pipeline: select → **validate args** → execute (sandbox/timeout) → **structured, trimmed result**.
- ⭐ **Failures → observations** (never crash the loop) → enables recovery.
- Retries: **transient only, bounded, backoff**; not permanent.
- Tag permissions (read/write/dangerous); results are **untrusted data**.

---

## 🧠 Memory (14.5)

- **LLM is stateless** → memory is external. Window = **RAM**, stores = **disk**.
- Types: working/short-term · long-term · **semantic** (facts) · **episodic** (past runs) · vector · conversation.
- ⭐ Lifecycle: **write → retrieve → summarize → prune → persist**.
- Long tasks survive via **summarization**; **prune** to keep recall sharp. Recall is **untrusted** (poisoning).

---

## 🔁 Reflection (14.6)

- self-evaluate → detect error → correct → **verify** → repeat.
- ⭐ **Grounded verification** (run tests/check data) > self-critique ("looks right").
- **Bound it** (capped retries); apply to risky/irreversible/finish steps.

---

## ⏱️ Loops (14.7)

- **Fixed** (N steps) · **adaptive** (until goal/budget, default) · **event-driven** (on events, idle-cheap).
- ⭐ **Termination** = goal · step budget · cost budget · **no-progress** · **oscillation**.
- Enforce hard limits in **code**; **degrade gracefully** (best partial result).

---

## 👥 Multi-agent (14.8)

- Roles: coordinator · planner · worker · researcher · **critic/reviewer** · executor.
- Patterns: hierarchical · sequential · parallel · debate.
- ⭐ **Default single-agent**; add agents for tools/context/parallelism/review/expertise.
- Perf win = **parallelize independent subtasks**. Least privilege per agent.

---

## 🔌 MCP (14.9)

| | |
|---|---|
| **⭐ MCP** | open protocol; app↔tool/data; **"USB-C for AI"**; M×N → M+N |
| **Host** | the AI app (LLM + clients) |
| **Client** | in the host; 1:1 link to a server |
| **Server** | exposes capabilities; wraps a service/data |
| **Resources** | app-controlled, read-only data (URI) |
| **Tools** | model-controlled actions (JSON-Schema) |
| **Prompts** | user-controlled templates |
| **Transport** | JSON-RPC over **stdio** (local) / **HTTP+SSE** (remote) |
| **Lifecycle** | initialize (capability negotiation) → operate → shutdown |
| **⚠️** | MCP = transport, **not** safety — scope, sandbox, validate, gate |

---

## 🪟 Context (14.10) & 💬 Communication (14.11)

- Agent context is **re-chosen every step and grows** → **dynamic assembly** + **rolling summarization** + externalized state; **re-state the goal** (anti-drift).
- Comms = **an API, not a chat**: structured, schema-validated messages; **aggregate ≠ concatenate**; messages are untrusted.

---

## 🧑‍⚖️ Human-in-the-loop (14.12)

- Pause for a human at **high-stakes / irreversible / low-confidence** moments.
- Approval · review checkpoint · override · escalation · feedback.
- ⭐ Calibrate by **impact & reversibility** (avoid approval fatigue); show action+rationale+impact; **last line of defense vs hijack**.

---

## 🔒 Safety (14.13)

| Control | One line |
|---|---|
| **⭐ Least privilege** | fewest/narrowest tools; read-only default — the top control |
| **Permission tiers** | read/write/dangerous; gate dangerous |
| **Sandboxing** | isolate code/file/shell; no network; limits |
| **Secret hygiene** | never in context; server-side |
| **Rate limiting** | bound blast radius; no cost-exhaustion |
| **Audit logging** | every decision/call — forensics |
| **⭐ Mindset** | **assume breach**; defense-in-depth; minimize blast radius |

---

## 📊 Evaluation (14.14)

- ⭐ Top-line = **task success rate** (did it accomplish the goal?).
- Component: tool/planning accuracy. Efficiency: steps/latency/cost. Reliability: consistency/hallucination/safety.
- Evaluate **outcome + trajectory**; sandboxed, repeatable, end-state checks; include adversarial/unachievable.

---

## 🚀 Production (14.15) & 🧰 Frameworks (14.16)

- Service-oriented: gateway → **orchestrator** (loop+budgets+**durable state**) → planner/memory/retriever → **tool manager** (security choke point) → MCP → observability.
- ⭐ **Trace the full trajectory**; monitor **success/cost/steps**, not uptime. Resumable state (checkpoint each step).
- Frameworks (LangGraph/CrewAI/AutoGen/OpenAI Agents SDK/Semantic Kernel/PydanticAI) package the primitives but **hide the guardrails** — build by hand first; **configure budgets/permissions explicitly**.

---

## 🎯 The 10 through-lines

1. Loop, not a prompt (model decides, code controls). 2. Tools = hands. 3. Memory = notebook (LLM stateless). 4. Autonomy is a liability — bound it. 5. Least privilege is load-bearing (assume breach). 6. Failures → observations. 7. Verify before irreversible actions. 8. MCP = USB-C of tools. 9. Evaluate task success (outcome + trajectory). 10. Frameworks hide the guardrails — build primitives first.

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 14](../README.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
| 🏋️ Exercises | [Exercises](../exercises/README.md) |
| 🎴 Flashcards | [Deck](../flashcards/deck.md) |
