# 🏋️ Module 14 · AI Agents & MCP — Exercises

[🏠 Module 14](../README.md) · [📖 Lessons](../weeks/README.md) · [🧩 Projects](../projects/)

> Build-it exercises, ordered along the module's spine: **build the agent → scale & connect → operate & deploy**. If you do only five, do ⭐ **E2, E4, E9, E13, E15** — the loop from scratch, the tool pipeline, an MCP server/client, the safety harness, and the evaluation pipeline. Together they are the module.
>
> Each exercise lists a **goal**, **constraints**, and a **done-when** (an objective, checkable success criterion). The prompt asks for a mix of conceptual, architecture, MCP, tool-calling, planning, memory, multi-agent, and debugging exercises — they're tagged below.

---

## Tier 1 · Build the agent (14.1–14.7)

### E1 · Agent-or-not (conceptual)
**Goal:** classify 8 tasks as single-call / RAG / workflow / agent and justify.
**Done-when:** each choice is defended by "who decides the control flow?" and the capabilities needed. → [14.1](../weeks/14.1-what-are-agents.md)

### ⭐ E2 · Agent loop from scratch (architecture)
**Goal:** implement the ReAct loop (~40 lines) with two tools, structured decisions, `max_steps`, and error-as-observation. No framework.
**Constraints:** the loop, budget, and validation live in *code*, not the prompt.
**Done-when:** (1) solves a 3-step task and stops; (2) an impossible goal terminates at the budget with a partial answer; (3) a tool error is read and recovered from. **The most important exercise in the module.** → [14.2](../weeks/14.2-agent-architecture.md)

### E3 · Planning strategies (planning challenge)
**Goal:** solve one task with sequential, dynamic, and hierarchical planning; add re-planning on failure.
**Done-when:** re-planning recovers where a static plan fails; you can state the commitment-vs-adaptivity trade-off with numbers (steps/cost). → [14.3](../weeks/14.3-planning.md)

### ⭐ E4 · Tool execution pipeline (tool-calling)
**Goal:** select → validate → execute (sandbox+timeout) → structured result, with transient/permanent retry logic.
**Done-when:** (1) bad args become recoverable observations; (2) transient failures retry with backoff, permanent don't; (3) a malicious argument (path/SQL) is blocked pre-execution. → [14.4](../weeks/14.4-tool-calling.md)

### E5 · Memory system (memory design)
**Goal:** working + vector-backed long-term memory with the full lifecycle (write/retrieve/summarize/prune/persist).
**Done-when:** recall works across sessions; summarization prevents overflow on a long task; no cross-tenant recall. → [14.5](../weeks/14.5-memory.md)

### E6 · Reflective step
**Goal:** add self-evaluate → correct → verify (grounded) with bounded retries.
**Done-when:** the agent recovers from a seeded error; grounded verification (run tests/check data) catches a wrong-but-plausible output; retries are capped. → [14.6](../weeks/14.6-reflection.md)

### E7 · Loop control
**Goal:** implement fixed/adaptive/event-driven modes with termination on goal/budget/no-progress/oscillation.
**Done-when:** an oscillation (A→B→A→B) is detected and broken; budget enforced; event mode idles at zero cost. → [14.7](../weeks/14.7-agent-loops.md)

## Tier 2 · Scale & connect (14.8–14.11)

### E8 · Coordinator–worker–critic (multi-agent coordination)
**Goal:** build a hierarchical multi-agent system with parallel workers and a critic; structured hand-offs.
**Done-when:** parallel workers speed up vs sequential; the critic catches seeded errors; a global budget bounds the whole system. → [14.8](../weeks/14.8-multi-agent.md)

### ⭐ E9 · MCP server + client (MCP implementation)
**Goal:** build an MCP server exposing one tool, one resource, one prompt (stdio); a client that initializes, lists, and calls; wire it into your E2 agent.
**Constraints:** scope the server (least privilege).
**Done-when:** (1) the agent calls an MCP tool in its loop; (2) the JSON-RPC lifecycle (initialize→list→call→close) is traceable; (3) the server can't act outside its scope. → [14.9](../weeks/14.9-mcp.md)

### E10 · Context management
**Goal:** dynamic context assembly with rolling summarization and externalized state; re-state the goal each step.
**Done-when:** a long task fits the window and completes; removing the goal causes drift, re-pinning fixes it. → [14.10](../weeks/14.10-context-engineering.md)

### E11 · Structured communication
**Goal:** Task/Result schemas + validated message passing + a real aggregation step (validate/merge/reconcile).
**Done-when:** prose delegation misunderstanding rate > structured; aggregation reconciles conflicting worker outputs (not concatenation). → [14.11](../weeks/14.11-communication.md)

## Tier 3 · Operate & deploy (14.12–14.16)

### E12 · Approval & escalation (human-in-the-loop)
**Goal:** gate dangerous actions with event-driven approval showing action+rationale+impact; escalate on low confidence.
**Done-when:** irreversible actions are gated; only high-stakes prompts fire (no approval fatigue); a hijack attempt is blocked at the gate. → [14.12](../weeks/14.12-human-in-the-loop.md)

### ⭐ E13 · Safety harness
**Goal:** wrap tool execution with least privilege, sandbox, secret hygiene, rate limits, approval gates, and audit log.
**Constraints:** assume-breach.
**Done-when:** (1) removing a dangerous tool makes an injection harmless (blast-radius test); (2) secrets never appear in context/logs; (3) sandbox contains a code tool; (4) a full run is reconstructable from the audit log. → [14.13](../weeks/14.13-safety.md)

### E14 · Failure localization (debugging)
**Goal:** instrument full trajectory tracing; plant bugs in planning, tools, and memory; localize each.
**Done-when:** each planted failure is attributed to the right component from the trace; a high-tool-accuracy-but-task-failure case is diagnosed as a planning problem. → [14.14](../weeks/14.14-evaluation.md)

### ⭐ E15 · Agent evaluation pipeline
**Goal:** a task suite with sandboxed environments and programmatic end-state checks; score success/tool-accuracy/steps/cost + an adversarial safety sub-suite.
**Done-when:** success rate + cost/steps reported; reliability via repeated runs; injection tasks scored on unsafe-action rate and gated. → [14.14](../weeks/14.14-evaluation.md)

### E16 · Production decomposition (architecture)
**Goal:** split your agent into orchestrator + tool manager + memory + observability with durable, resumable state.
**Done-when:** the agent resumes after a mid-task restart; budgets enforced centrally; a failed run is reconstructed from the trajectory trace. → [14.15](../weeks/14.15-production-architecture.md)

### E17 · Framework bake-off
**Goal:** build the same agent from scratch and in a framework; expose the framework's hidden defaults.
**Done-when:** both meet the eval bar; you can name the framework's default max-steps/budget/permissions and confirm guardrails are enforced (not defaulted). → [14.16](../weeks/14.16-frameworks.md)

## Capstone

### ⭐ E18 · Autonomous task planner (Project 10)
**Goal:** the flagship — hierarchical planning + re-planning, full memory stack, reflection before irreversible actions, human gates, safety harness, budgets, audit, and an eval suite (incl. adversarial).
**Done-when:** completes multi-step goals with a measured success rate, stays within budget, gates every high-impact action, blocks an injected instruction from causing an unsafe action, and produces a full trajectory trace. → [14.17](../weeks/14.17-projects-summary.md)

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 14](../README.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
| 📝 Quiz | [Quiz 01](../quizzes/quiz-01.md) |
| 🎴 Flashcards | [Deck](../flashcards/deck.md) |
| 📄 Cheat sheet | [Agents cheat sheet](../cheat-sheets/agents-cheatsheet.md) |
