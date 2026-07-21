# 🧠 Module 12 · Prompt Engineering — Flashcard Deck

[🏠 Module 12](../README.md) · [📖 Lessons](../weeks/README.md) · [📄 Cheat sheet](../cheat-sheets/prompt-cheatsheet.md)

> **~95 cards.** Cover the answer, say it aloud, *then* check. ⭐ marks the load-bearing ones.

---

## 12.1 · How LLMs Interpret Prompts

**Q:** ⭐ What does an LLM actually do with a prompt? → **A:** Treats it as text-so-far and predicts the most probable next tokens — it doesn't infer intent. → [12.1](../weeks/12.1-how-llms-interpret-prompts.md)

**Q:** What is prompt engineering, mechanistically? → **A:** Shaping the conditioning context so the desired output becomes the most probable continuation.

**Q:** The three message roles? → **A:** System (durable high-priority rules/format), user (request+data), assistant (output; can seed examples).

**Q:** Is the system message a security boundary? → **A:** No — high-priority steering, but the model still just predicts tokens and can be overridden.

**Q:** ⭐ Why can't you judge a prompt from one response? → **A:** Generation is probabilistic; reliability must be measured over a dataset.

---

## 12.2 · Anatomy of a Prompt

**Q:** ⭐ The eight components? → **A:** Role, objective, context, instructions, constraints, examples, output format, success criteria. → [12.2](../weeks/12.2-anatomy-of-a-prompt.md)

**Q:** ⭐ Usual cause of a weak prompt? → **A:** A missing component, not bad wording.

**Q:** Often the strongest component? → **A:** Examples — a demonstration pins format/behavior better than description.

**Q:** What does an escape-hatch constraint do? → **A:** Lets the model say "unknown" instead of hallucinating when data lacks the answer.

---

## 12.3 · Patterns

**Q:** ⭐ Zero-shot vs few-shot — how to choose? → **A:** Zero-shot when the task is describable; few-shot when it's demonstrable (subtle format/style/edge cases). → [12.3](../weeks/12.3-basic-patterns.md)

**Q:** What does role prompting change (and not)? → **A:** Vocabulary, depth, tone via a persona; it's not a safety control.

**Q:** Contextual prompting is the foundation of…? → **A:** Context engineering and RAG.

**Q:** Why start zero-shot? → **A:** Cheapest/lowest-latency; escalate only when evaluation shows a need.

---

## 12.4 · Structure

**Q:** ⭐ Most important structural move? → **A:** Unambiguously separating instructions from (untrusted) input data. → [12.4](../weeks/12.4-prompt-structure.md)

**Q:** Most robust delimiter for data? → **A:** XML-style tags + a "content is data, not instructions" rule.

**Q:** What's a delimiter-collision attack? → **A:** Untrusted input includes your closing delimiter to break out of the data region.

**Q:** Why keep structure consistent across calls? → **A:** It makes prompts reusable templates and outputs comparable for evaluation.

---

## 12.5 · Few-Shot

**Q:** ⭐ What are few-shot examples, really? → **A:** An executable spec — the model infers the task by analogy and imitates them (incl. mistakes). → [12.5](../weeks/12.5-few-shot.md)

**Q:** The four levers? → **A:** Selection, quality, diversity, ordering.

**Q:** Why does one bad example matter? → **A:** The model imitates it — poisons behavior.

**Q:** What teaches decision boundaries? → **A:** Diverse, near-boundary examples across all classes.

**Q:** ⭐ Instructions vs examples on conflict — which wins? → **A:** Examples usually win; keep them aligned.

---

## 12.6 · Structured Outputs

**Q:** ⭐ Why are structured outputs the backbone of production? → **A:** Downstream code consumes data, not prose; structure is reliable, validatable, composable, evaluable. → [12.6](../weeks/12.6-structured-outputs.md)

**Q:** The standard pattern? → **A:** Specify schema → low temp → parse+validate → repair-retry → reject.

**Q:** What does provider structured mode guarantee? → **A:** Syntactically valid, schema-conforming output (via constrained decoding); still validate semantics.

**Q:** ⭐ Is valid JSON safe to use? → **A:** No — a schema-valid string field can carry injection; validate values, treat as untrusted.

**Q:** Why use enums? → **A:** They stop the model inventing categories downstream code can't handle.

---

## 12.7 · Reasoning

**Q:** Why does step-by-step reasoning help hard tasks? → **A:** Intermediate results condition the model toward a correct conclusion vs a blind first-token leap. → [12.7](../weeks/12.7-reasoning.md)

**Q:** ⭐ How should reasoning output be designed for production? → **A:** Return a concise structured result (conclusion + assumptions + verification), not raw chain-of-thought.

**Q:** Self-check vs verification? → **A:** Self-check re-reads vs requirements; verification re-derives/checks against source data — stronger.

**Q:** ⭐ Why can more reasoning mislead? → **A:** The model can fluently justify a wrong answer; only ground-truth verification reliably catches it.

---

## 12.8 · Chaining

**Q:** ⭐ Why does chaining improve reliability? → **A:** Each step does one job and you validate between steps, catching errors at the seam instead of multiplying in one overloaded prompt. → [12.8](../weeks/12.8-prompt-chaining.md)

**Q:** What glues chain steps? → **A:** Validated structured output — each step's typed output is the next's input.

**Q:** What makes a chain "just a slow mega-prompt"? → **A:** Skipping inter-step validation.

**Q:** Cost of chaining? → **A:** Extra LLM calls — justify the split with a measured reliability gain.

---

## 12.9 · Templates

**Q:** ⭐ Why turn a reused prompt into a template? → **A:** Reusable, testable, versioned, safely parameterized, deployable — prompt-as-code. → [12.9](../weeks/12.9-templates.md)

**Q:** Where do untrusted variables go? → **A:** Delimited data slots with a "treat as data" directive — never instruction text.

**Q:** ⭐ Why bundle config with prompt text? → **A:** Same text behaves differently across models/temperatures; bundling makes it reproducible and rollback-able.

**Q:** How are prompts versioned? → **A:** Name + semver, in VCS/registry, never edited live, pinned per environment.

---

## 12.10 · Task Strategies

**Q:** ⭐ What do all tasks share vs differ? → **A:** A common skeleton; the guardrails and metrics differ per task. → [12.10](../weeks/12.10-task-strategies.md)

**Q:** Universal hallucination guard? → **A:** Constrain the output space (enums/schema) + escape hatch ("unknown"/"null"/"not in source").

**Q:** Extraction: stop hallucinated fields how? → **A:** Schema + "null/unknown if absent; do not guess."

**Q:** Code generation: how to evaluate? → **A:** Run/compile it and pass tests/static analysis — never trust unverified.

---

## 12.11 · Context Engineering

**Q:** ⭐ Prompt vs context engineering? → **A:** How you ask vs what information you put in the finite window. → [12.11](../weeks/12.11-context-engineering.md)

**Q:** ⭐ Why is more context often worse? → **A:** Distractors dilute attention, cost rises, key facts drift into the ignored middle — curate, don't accumulate.

**Q:** Lost-in-the-middle + fix? → **A:** Models attend to edges more than the middle; put key content at start/end, keep the middle lean.

**Q:** ⭐ Context engineering vs RAG? → **A:** RAG is context engineering automated and scaled: retrieve → rerank → construct context per query.

---

## 12.12 · Tool Calling

**Q:** ⭐ What happens in a tool call? → **A:** The model emits structured args for a function you defined; your code validates+executes and returns the result — the model never runs anything. → [12.12](../weeks/12.12-tool-calling.md)

**Q:** What controls correct tool use? → **A:** The tool's name, description, and arg schema (its "prompt"), plus when-(not)-to-call rules.

**Q:** ⭐ Why validate tool arguments? → **A:** They're untrusted model output; unvalidated args into SQL/shell/API are an injection/damage vector.

**Q:** Strongest defense if the model is hijacked? → **A:** Least privilege — minimal, read-only tools; human approval for high-impact actions.

**Q:** ⭐ Tool calling relates to agents/MCP how? → **A:** The tool loop with autonomy is an agent; MCP standardizes exposing tools to models.

---

## 12.13 · Evaluation

**Q:** ⭐ Why is evaluation a dataset problem? → **A:** Generation is probabilistic and inputs vary; quality is statistical, measured over a representative dataset. → [12.13](../weeks/12.13-evaluation.md)

**Q:** The six dimensions? → **A:** Accuracy, consistency, relevance, completeness, hallucination rate, format correctness.

**Q:** ⭐ Why track dimensions separately? → **A:** They move independently — accurate-but-misformatted or well-formatted-but-hallucinating; a blended score hides that.

**Q:** Why include unanswerable cases? → **A:** To measure correct abstention instead of hallucination.

**Q:** Methods cheapest-first? → **A:** Deterministic checks, rubric scoring, LLM-as-judge (calibrate).

---

## 12.14 · Testing

**Q:** ⭐ Why do prompts need regression testing? → **A:** A tiny edit or a silent model update can degrade quality with no code change; a golden-set suite is the only net. → [12.14](../weeks/12.14-testing.md)

**Q:** What is a golden dataset? → **A:** Versioned (input, known-good) reference cases the prompt must keep passing.

**Q:** ⭐ Why pin the model version in tests? → **A:** To catch provider-side drift ("nothing changed but quality dropped").

**Q:** How unit-test probabilistic prompts? → **A:** Assert invariants (schema, required, never-X) and use thresholds, not exact equality.

---

## 12.15 · Debugging

**Q:** ⭐ The systematic framework? → **A:** Reproduce → categorize symptom → inspect exact prompt → map to cause → targeted fix → verify → add to golden set. → [12.15](../weeks/12.15-debugging.md)

**Q:** First debugging move? → **A:** Print the fully assembled prompt the model received.

**Q:** ⭐ Most fixes are…? → **A:** Adding/clarifying a missing component, not rewording.

**Q:** Fails every time vs sometimes? → **A:** Every time = deterministic prompt/context/format bug; sometimes = variance (lower temp, remove ambiguity).

---

## 12.16 · Security

**Q:** ⭐ Why is prompt injection structural? → **A:** Instructions and data share one token channel; the model can't inherently separate them. → [12.16](../weeks/12.16-security.md)

**Q:** Direct vs indirect injection? → **A:** Direct from the user's message; indirect hidden in retrieved/tool content (often innocent user).

**Q:** ⭐ Strongest defense? → **A:** Least privilege — limit what obeying an injected instruction can achieve.

**Q:** Why never execute model output? → **A:** It's untrusted; eval/SQL/shell on it is a code/data-injection vector.

**Q:** What is data leakage? → **A:** The model revealing context contents (system prompt, other users' data, secrets) in its output.

---

## 12.17 · Optimization

**Q:** ⭐ What does prompt optimization optimize? → **A:** A point on the quality↔cost↔latency surface, via evaluation-driven iteration. → [12.17](../weeks/12.17-optimization.md)

**Q:** ⭐ Biggest latency/cost lever? → **A:** Constraining output length (decode is sequential; output tokens cost more).

**Q:** Why change one variable at a time? → **A:** To attribute effects and avoid shipping silent regressions.

**Q:** What must you never optimize away? → **A:** Safety directives (data-as-data) and output validation.

---

## 12.18 · Production

**Q:** ⭐ Why is a prompt edit a production deployment? → **A:** It changes live behavior for real users; needs versioning, testing, staged rollout, monitoring, rollback. → [12.18](../weeks/12.18-production.md)

**Q:** What is a prompt registry? → **A:** A central store to publish/fetch/pin prompts by name@version with config/status, decoupling prompt changes from app deploys.

**Q:** ⭐ Why monitor quality, not uptime? → **A:** An app can be fully up while quality silently degrades from a prompt regression or model change.

**Q:** How does rollback work? → **A:** Re-pin the last-good version in the registry — seconds, no code deploy.

---

## 12.19–12.20 · Python & Summary

**Q:** ⭐ The five toolkit components? → **A:** PromptTemplate, validated call, chain runner, evaluator, regression gate. → [12.19](../weeks/12.19-python.md)

**Q:** Why wrap the call in `call_validated`? → **A:** So downstream code only ever sees typed, valid data (parse→validate→repair/reject).

**Q:** ⭐ The one thing to remember from the module? → **A:** A prompt is a specification for a probabilistic machine; reliability is measured, not felt. → [12.20](../weeks/12.20-projects-summary.md)

**Q:** The five-part definition of prompt engineering? → **A:** Understanding the model + designing instructions + controlling context + defining output structure + evaluating results.

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 12](../README.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
| 📄 Cheat sheet | [Prompt cheat sheet](../cheat-sheets/prompt-cheatsheet.md) |
| 📝 Quiz | [Quiz 01](../quizzes/quiz-01.md) |
