# 🏋️ Module 12 · Prompt Engineering — Exercises

[🏠 Module 12](../README.md) · [📖 Lessons](../weeks/README.md) · [🧩 Projects](../projects/)

> Build-it exercises, ordered along the module's spine: **understand → structure → control output → interface → operate**. If you do only five, do ⭐ **E4, E6, E9, E12, E15** — structured output with validation, few-shot boundaries, tool calling, the evaluation harness, and the safer pipeline. Together they are the module.
>
> Each exercise lists a **goal**, **constraints**, and a **done-when** (an objective, checkable success criterion).

---

## Tier 1 · Foundations (12.1–12.5)

### E1 · Ambiguity → variance
**Goal:** show a vague prompt produces varied output and a precise one doesn't.
**Done-when:** running a vague prompt 10× at temp 1 yields many distinct outputs; tightening it collapses the variance — you can quantify the drop. → [12.1](../weeks/12.1-how-llms-interpret-prompts.md)

### E2 · Component audit
**Goal:** label three prompts by which of the eight components each has/misses; add the missing ones.
**Done-when:** each rewritten prompt has role/objective/context/instructions/constraints/examples/format/criteria as needed, and output quality improves. → [12.2](../weeks/12.2-anatomy-of-a-prompt.md)

### E3 · Escalation ladder
**Goal:** solve a subtle labeling task zero-shot → one-shot → few-shot; measure accuracy and tokens at each step.
**Done-when:** you can state the point where examples start paying off, with numbers. → [12.3](../weeks/12.3-basic-patterns.md)

### ⭐ E4 · Data-instruction separation (also security)
**Goal:** run a task with input data as a blob vs tagged/delimited with a "data only" rule; include an input containing an embedded instruction.
**Done-when:** the blob follows the injected instruction and the tagged version does not — measured over ≥10 inputs. → [12.4](../weeks/12.4-prompt-structure.md)

### E5 · Few-shot levers
**Goal:** poison one example, imbalance the classes, and fix ordering; measure each effect.
**Done-when:** you demonstrate that one bad example poisons output, boundary examples fix hard cases, and shuffling reduces order bias. → [12.5](../weeks/12.5-few-shot.md)

## Tier 2 · Controlling output & flow (12.6–12.10)

### ⭐ E6 · Structured output with validation
**Goal:** get JSON three ways (prompt-only, schema+example, provider structured mode); validate with Pydantic + a repair-retry.
**Constraints:** never use unvalidated output.
**Done-when:** (1) valid-JSON rate measured across methods; (2) semantic validators (enum/range) reject bad values; (3) a schema-valid-but-unsafe field is caught. **The most important exercise in the first half.** → [12.6](../weeks/12.6-structured-outputs.md)

### E7 · Verified reasoning
**Goal:** solve a multi-constraint task one-shot vs decomposed-with-verification; return a structured `{conclusion, assumptions, verification}`.
**Done-when:** decomposition + verification improves accuracy and the output is concise/structured (no raw chain-of-thought). → [12.7](../weeks/12.7-reasoning.md)

### E8 · Chain with validated seams
**Goal:** split a mega-prompt into a chain; validate between steps; inject a bad intermediate.
**Done-when:** the bad intermediate is caught at its seam, and end-to-end accuracy/debuggability beats the mega-prompt. → [12.8](../weeks/12.8-prompt-chaining.md)

### E9 · Template + injection
**Goal:** convert an inline prompt into a versioned template with typed slots; show the inline version is injectable and the template isn't.
**Done-when:** untrusted vars land only in delimited data slots; config travels with the template; version pinning works. → [12.9](../weeks/12.9-templates.md)

### E10 · Task guardrails
**Goal:** for extraction, summarization, and QA, induce the signature hallucination, then add the matching guard.
**Done-when:** "null if absent" (extraction), "source only" (summary/QA) each eliminate the induced hallucination, confirmed by the task metric. → [12.10](../weeks/12.10-task-strategies.md)

## Tier 3 · Interfaces (12.11–12.12)

### E11 · Context curation
**Goal:** answer a question with a full document vs a selected excerpt; reproduce lost-in-the-middle.
**Done-when:** the curated excerpt matches/beats full-dump accuracy at a fraction of tokens; answer accuracy follows the position U-curve. → [12.11](../weeks/12.11-context-engineering.md)

### ⭐ E12 · Safe tool-calling loop
**Goal:** build a tool loop with schema validation, least privilege, and an approval gate on writes.
**Done-when:** (1) invalid arguments rejected before execution; (2) a destructive action requires approval; (3) an injected tool result does not trigger an unsafe call. → [12.12](../weeks/12.12-tool-calling.md)

## Tier 4 · Operate (12.13–12.19)

### E13 · Evaluation harness
**Goal:** score a prompt on all six dimensions over a 30-case set (incl. edge + unanswerable).
**Done-when:** you find a case where accuracy is fine but format or hallucination fails — proving why dimensions are tracked separately. → [12.13](../weeks/12.13-evaluation.md)

### E14 · Regression gate
**Goal:** build a golden set + regression gate; make a bad edit and a model-version change.
**Done-when:** the bad edit is blocked; the model change triggers re-eval and flags the difference. → [12.14](../weeks/12.14-testing.md)

### ⭐ E15 · Safer prompt pipeline
**Goal:** wrap an LLM call with trust separation, output validation, least privilege, and output DLP; build an adversarial suite.
**Done-when:** injected instructions have no privileged effect, a planted secret is blocked from output, and the adversarial suite stays non-exploitable (gated in CI). → [12.16](../weeks/12.16-security.md)

### E16 · Systematic debugging
**Goal:** reproduce each of the seven symptoms; apply the mapped fix; verify on the eval set.
**Done-when:** every symptom is resolved by a structural fix (not rewording), confirmed by metrics, and one "constraint-ignored" bug turns out to be injection. → [12.15](../weeks/12.15-debugging.md)

### E17 · Optimize on the frontier
**Goal:** cut a prompt's cost/latency without dropping quality below a bar, changing one thing at a time.
**Done-when:** you produce a quality-vs-cost frontier and ship a cheaper-but-equal version; the security suite still passes after any downsizing. → [12.17](../weeks/12.17-optimization.md)

### E18 · Toolkit build
**Goal:** implement the five Python components (template, validated call, chain, evaluate, gate) and wire them end-to-end.
**Done-when:** an extraction task runs template→validated→evaluated→gated, with fencing and repair working. → [12.19](../weeks/12.19-python.md)

## Capstone · Production prompt management (Project 7)

### ⭐ E19 · End-to-end production system
**Goal:** ship the [12.18](../weeks/12.18-production.md) architecture: registry + env pins, promotion gate (tests+eval+security), per-call logging, monitoring, canary A/B, rollback.
**Done-when:** a deliberately-bad prompt version is blocked at the gate; a regression in prod is rolled back in seconds by re-pinning; an injected instruction has no privileged effect; quality/cost are attributable per version. → [12.20](../weeks/12.20-projects-summary.md)

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 12](../README.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
| 📝 Quiz | [Quiz 01](../quizzes/quiz-01.md) |
| 🎴 Flashcards | [Deck](../flashcards/deck.md) |
| 📄 Cheat sheet | [Prompt cheat sheet](../cheat-sheets/prompt-cheatsheet.md) |
