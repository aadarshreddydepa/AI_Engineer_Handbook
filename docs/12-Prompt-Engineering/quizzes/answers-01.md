# ✅ Module 12 · Prompt Engineering — Quiz 01 Answers

[🏠 Module 12](../README.md) · [📝 Quiz](quiz-01.md) · [📖 Lessons](../weeks/README.md)

> Model answers grade **reasoning**. Full credit = the key idea explained, not just a keyword.

---

## Part A · Foundations

**1.** It treats the prompt as text-so-far and predicts the **most probable next tokens** — it doesn't infer intent. Implication: prompt engineering means **removing ambiguity so the desired output is the most probable continuation** (precise instructions, structure, examples, format). → [12.1](../weeks/12.1-how-llms-interpret-prompts.md)

**2.** Generation is **probabilistic** — the same prompt can yield different outputs, and real inputs vary. One good output is a sample size of one; **reliability is a statistical property measured over a representative dataset**. → [12.1](../weeks/12.1-how-llms-interpret-prompts.md), [12.13](../weeks/12.13-evaluation.md)

**3.** **System** (durable, high-priority rules/role/format that persist across turns), **user** (the request + input data for this turn), **assistant** (model responses; can seed few-shot). The system message steers more reliably and persistently but is **high-priority, not a hard boundary**. → [12.1](../weeks/12.1-how-llms-interpret-prompts.md)

**4.** Role, objective, context, instructions, constraints, examples, output format, success criteria. The heuristic works because the model fills any unspecified component with a **plausible guess** — so a bad prompt is usually one you left the model to guess a component, not one that's badly phrased. → [12.2](../weeks/12.2-anatomy-of-a-prompt.md)

**5.** If the task is easy to **describe** in words, use a plain instruction (zero-shot); if it's easier to **demonstrate** (subtle format/style/edge cases), use examples (few-shot). Layer role for stance and context for grounding. → [12.3](../weeks/12.3-basic-patterns.md)

**6.** The model reads instructions and data as one token stream and can **misattribute** data as instructions. Separating them (delimiters/tags + "treat as data") prevents misreads (**reliability**) and resists **prompt injection** (**security**) — a sentence in the data won't be executed as a command. → [12.4](../weeks/12.4-prompt-structure.md)

**7.** Untrusted input includes your **closing delimiter** to "break out" of the data region and inject instructions. Prevent with fixed/hard-to-guess delimiters, input sanitization/escaping, and not letting input choose the fence. → [12.4](../weeks/12.4-prompt-structure.md)

**8.** Via **in-context learning**, the model infers the task/format/conventions by analogy and **imitates the examples** — so examples *are* the spec. One wrong example is imitated and **poisons** behavior. → [12.5](../weeks/12.5-few-shot.md)

**9.** **Examples usually win** — the model trusts the demonstrated pattern over the described one. Keep prose rules and examples **telling the same story**; if an instruction is ignored, an example that *shows* the rule often fixes it. → [12.5](../weeks/12.5-few-shot.md)

## Part B · Controlling output & flow

**10.** Because downstream systems **consume data, not prose** — structure makes output reliably parseable, validatable, composable (one step's output is the next's input), and evaluable. → [12.6](../weeks/12.6-structured-outputs.md)

**11.** Put the **schema** in the prompt → generate at **low temperature** → **parse + validate** against the schema (structure + semantics) → **repair-retry** on failure (feed back the error) → **reject** (fail closed) if still invalid. Never feed unvalidated output downstream. → [12.6](../weeks/12.6-structured-outputs.md)

**12.** A schema-valid string field can still contain **injection payloads or malicious content**. "Valid" checks shape, not safety — validate **values** and treat output as untrusted (never eval/SQL/exec it). → [12.6](../weeks/12.6-structured-outputs.md), [12.16](../weeks/12.16-security.md)

**13.** Return a **concise, structured result** — conclusion + assumptions + verification — not a raw monologue. Raw chain-of-thought is verbose, costly, and can **leak** system-prompt/sensitive content or expose exploitable rationalizations; you want the *benefit* of stepwise computation without displaying the transcript. → [12.7](../weeks/12.7-reasoning.md)

**14.** The model can produce **fluent justification for a wrong conclusion** (rationalization). Defend by **verifying against source data/requirements** (independent re-derivation or a ground-truth check), not by judging whether the reasoning "sounds right." → [12.7](../weeks/12.7-reasoning.md)

**15.** Splitting into focused steps makes each simple and testable, and **validating between steps** catches errors at the seam instead of letting failure probabilities multiply in one overloaded prompt. It **fails to** improve reliability if you skip inter-step validation — then it's just a slower mega-prompt. → [12.8](../weeks/12.8-prompt-chaining.md)

**16.** **Validated structured output** — each step's typed, schema-checked output is the next step's input, so a bad intermediate is caught before it propagates. → [12.8](../weeks/12.8-prompt-chaining.md)

**17.** To make it **reusable, testable, versioned, safely parameterized, and deployable** (prompt-as-code) instead of an untestable, unversioned, injectable inline string. → [12.9](../weeks/12.9-templates.md)

**18.** The **same text behaves differently** across models and temperatures; bundling config with the text makes "the prompt" fully **reproducible** and **rollback-able**, essential for testing and production. → [12.9](../weeks/12.9-templates.md)

**19.** **Constrain the output space + provide an escape hatch.** Extraction: require a **schema** and "**null/unknown if absent; do not guess**." Summarization: "**use only the source; add nothing**" + a faithfulness check. → [12.10](../weeks/12.10-task-strategies.md)

## Part C · Interfaces

**20.** Prompt engineering = **how you ask** (instructions/format); context engineering = **what information you put in the finite window** (selection/ordering/compression). A perfect instruction over the wrong context fails; perfect context with a vague instruction fails. → [12.11](../weeks/12.11-context-engineering.md)

**21.** Extra content adds **distractors**, **dilutes attention**, raises cost, and pushes key facts into the **ignored middle** (lost-in-the-middle) — so quality rises then plateaus/drops. Curate, don't accumulate. → [12.11](../weeks/12.11-context-engineering.md)

**22.** Models attend to context **edges more than the middle** (U-curve). Design around it by keeping **k small** and placing the **most important content at the start/end** (often strongest last). → [12.11](../weeks/12.11-context-engineering.md)

**23.** RAG **automates and scales** context engineering: when relevant info is too large/dynamic to hand-pick, you **retrieve** it per query, **rerank** to the most relevant, and **construct** the context programmatically — exactly select/order/compress at system scale. → [12.11](../weeks/12.11-context-engineering.md), [13](../../13-RAG/README.md)

**24.** The model decides a tool is needed and emits a **structured call** (name + arguments); **your code** validates and executes it and returns the **result** into context; the model continues, possibly calling more tools, until it answers. The model **only requests** calls — it never executes anything. → [12.12](../weeks/12.12-tool-calling.md)

**25.** The model decides whether/how to call a tool almost entirely from its **name, description, and argument schema** — a vague description causes misuse; a precise, scoped one drives correct calls. → [12.12](../weeks/12.12-tool-calling.md)

**26.** Arguments are **untrusted model output** — unvalidated args into SQL/shell/API are an injection/damage vector. The strongest defense if the model is hijacked is **least privilege**: minimal, read-only tools and **human approval for high-impact actions**. → [12.12](../weeks/12.12-tool-calling.md)

**27.** Tool results **re-enter the context as untrusted data** — a tool returning web/user content can carry an injected instruction that targets the next model step; keep the data-as-data discipline. → [12.12](../weeks/12.12-tool-calling.md), [12.16](../weeks/12.16-security.md)

## Part D · Evaluate & operate

**28.** Because generation is **probabilistic** and inputs vary, quality is statistical — measured over a **representative dataset**. Dimensions are tracked **separately** because they move independently (accurate but misformatted, or well-formatted but hallucinating); a blended score hides real failures. → [12.13](../weeks/12.13-evaluation.md)

**29.** Accuracy, consistency, relevance, completeness, hallucination rate, format correctness. **Unanswerable cases** measure whether the model **correctly abstains** instead of hallucinating — invisible if you test only answerable inputs. → [12.13](../weeks/12.13-evaluation.md)

**30.** A **versioned set of representative (input, known-good) cases** the prompt must keep satisfying. Regression testing runs the prompt over it on **every change** and fails if a tracked metric drops below threshold — catching prompt- and model-driven regressions. → [12.14](../weeks/12.14-testing.md)

**31.** Because a **provider can update the model beneath you**, degrading quality with **no code change and no error**. Recording/pinning the model version lets your regression suite catch "nothing changed but quality dropped." → [12.14](../weeks/12.14-testing.md)

**32.** **Reproduce → categorize symptom → inspect the exact assembled prompt → map to cause → targeted fix → verify on eval set → add to golden set.** The cause is rarely a "model flaw" because most bad outputs come from **ambiguity, a missing component, bad/absent context, unspecified format, high temperature, or injection** — all in your control. → [12.15](../weeks/12.15-debugging.md)

**33.** Because **instructions and data share one token channel** and the model's job is to continue the most probable text — it can't inherently separate "your rules" from "attacker text," so no wording fully patches it. → [12.16](../weeks/12.16-security.md)

**34.** You **cannot instruct your way to immunity** (the model will sometimes obey injected text), so make **obeying harmless**: minimal tools, read-only defaults, no secrets/cross-tenant data in context, and **human approval for irreversible actions** — limiting the blast radius. → [12.16](../weeks/12.16-security.md)

**35.** It optimizes a **point on the quality↔cost↔latency surface** — you can only see that surface with **evaluation**. Blind shortening/lengthening ships silent regressions; you change one thing, measure, and keep what wins. → [12.17](../weeks/12.17-optimization.md)

**36.** **Output tokens usually cost more than input tokens and dominate latency** because decode is **sequential** (token-by-token). Constraining output length cuts both cost and time-to-completion. → [12.17](../weeks/12.17-optimization.md), [11.15](../../11-LLMs/weeks/11.15-kv-cache.md)

**37.** A prompt change **alters live behavior for real users** with no code change — so it needs the same discipline as a deploy: versioning, testing, staged rollout, monitoring, and rollback. → [12.18](../weeks/12.18-production.md)

**38.** A **registry** stores/serves prompts by `name@version` (decoupling prompt changes from app deploys). **Rollback** = re-pin the last-good version (seconds, no code deploy); **canary/A/B** validates a change on a fraction of live traffic before full promotion — together making frequent iteration safe. → [12.18](../weeks/12.18-production.md)

## Part E · Python & synthesis

**39.** **PromptTemplate** (versioned, safe render + config), **`call_validated`** (render→call→parse→validate→repair/reject), **`run_chain`** (steps with validated seams + trace), **`evaluate`** (multi-dimension scoring over a dataset), **`regression_gate`** (block changes that drop metrics). Together they're the transparent core of any LLM app. → [12.19](../weeks/12.19-python.md)

**40.** The model does what its input makes **probable, not what you meant** ([12.1](../weeks/12.1-how-llms-interpret-prompts.md)) — so the prompt is a **specification** you write precisely, and because generation is probabilistic, reliability is **measured over a dataset**, not felt. Definition: **understanding the model + designing instructions + controlling context + defining output structure + evaluating results.** → [12.20](../weeks/12.20-projects-summary.md)

---

## Scoring

| Score | Verdict |
|---|---|
| 36–40 | Excellent — you can design, evaluate, secure, and operate prompts. |
| 32–35 | Solid — review the missed lessons. |
| 24–31 | Partial — re-read 12.1, 12.6, 12.11, 12.13 (the load-bearing four). |
| < 24 | Re-study the module; redo ⭐ exercises E4, E6, E9, E12, E15. |

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 12](../README.md) |
| 📝 Quiz | [quiz-01.md](quiz-01.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
