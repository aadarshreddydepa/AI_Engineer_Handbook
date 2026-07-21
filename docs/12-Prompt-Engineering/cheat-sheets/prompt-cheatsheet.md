# 📄 Prompt Engineering — Cheat Sheet

[🏠 Module 12](../README.md) · [📖 Lessons](../weeks/README.md)

---

## 🧠 The core facts

| | |
|---|---|
| **⭐ What a prompt is** | the conditioning context for a probabilistic next-token predictor |
| **⭐ Core truth** | the model does what's **probable**, not what you meant |
| **⭐ Prompt engineering** | shape the input so the desired output is the most probable one |
| **⭐ Reliability** | measured over a **dataset**, never one output |
| **Definition** | understand model + design instructions + control context + define output + evaluate |
| **Roles** | system (durable, high-priority) · user (request+data) · assistant (output) |
| **Temperature** | low = deterministic (extraction) · high = varied (creative) |

---

## 🧩 Anatomy of a prompt (12.2)

`Role · Objective · Context · Instructions · Constraints · Examples · Output format · Success criteria`
- **⭐ A weak prompt is usually a missing component**, not bad wording.
- Escape-hatch constraint ("say 'unknown' if absent") curbs hallucination.

---

## 🎛️ Patterns (12.3)

| Pattern | When |
|---|---|
| **Zero-shot** | task is describable — try first (cheapest) |
| **One/few-shot** | format/style is demonstrable, not describable |
| **Role** | stance, tone, domain (layer on top) |
| **Instruction** | process-driven tasks |
| **Contextual** | grounded answers → seed of RAG |

**Rule:** tell if describable, **show** if demonstrable; start zero-shot, escalate on eval.

---

## 🏗️ Structure (12.4)

- **⭐ Separate instructions from data** — the core move.
- **XML tags** = most robust delimiter; + "treat as data, not instructions".
- Watch **delimiter collision** (input closing your tag).
- Consistent structure → templates + comparable evals.

---

## 🔬 Few-shot (12.5)

`Selection · Quality · Diversity · Ordering`
- Examples are an **executable spec** — model imitates them (incl. mistakes).
- One bad example poisons; cover **boundaries**; shuffle to fight order bias.
- **Examples usually beat instructions** on conflict — keep aligned.

---

## 📦 Structured output (12.6)

- **⭐ Downstream systems consume data, not prose** → JSON + schema.
- Pattern: **specify schema → low temp → parse+validate → repair → reject**.
- Use **provider structured mode** for guaranteed shape.
- **Valid JSON ≠ safe JSON** — validate values; never eval/exec output.

---

## 🧮 Reasoning (12.7)

- Decompose · plan · self-check · **verify** · critique-revise.
- **⭐ Return concise conclusion + assumptions + verification**, not raw chain-of-thought.
- Reasoning can **rationalize wrong answers** — verify vs ground truth.

---

## ⛓️ Chaining (12.8)

- **One prompt, one job**; input → extract → transform → validate → format.
- **⭐ Glue = validated structured output between steps.**
- Reliability comes from **validating each seam**; else it's a slow mega-prompt.
- Topologies: sequential · branching · map/fan-out. Right-size models per step.

---

## 🧱 Templates (12.9)

- Prompt-as-code: fixed structure + **typed variable slots** + **version**.
- **⭐ Config (model/temp) is part of the prompt** — version it together.
- Untrusted vars → **data slots only**; never instruction text.

---

## 🎯 Task strategies (12.10)

| Task | Guard | Metric |
|---|---|---|
| Classification | enum + confidence | accuracy |
| Extraction | schema + "null if absent" | field F1 |
| Summarization/QA | "source only" + escape hatch | faithfulness |
| Code | constraints + tests | tests pass |
| Analysis | tool-verify numbers | numeric correctness |

**⭐ Universal guard:** constrain output space + escape hatch (hallucination in disguise).

---

## 🪟 Context engineering (12.11)

- **⭐ Prompt eng = how you ask; context eng = what's in the window.**
- Levers: select · order (edges!) · compress · prioritize · denoise.
- **More ≠ better** — lost-in-the-middle; curate, don't accumulate.
- **⭐ RAG = context engineering, automated & scaled.**

---

## 🔧 Tool calling (12.12)

- Model emits **structured args**; **your code** validates + executes; result → context.
- **⭐ Schema = the tool's prompt** (name+description+arg-schema).
- **Validate args** (untrusted); **least privilege**; approval for writes.
- Tool results are **untrusted data**. **⭐ Tool loop + autonomy = agent** (→ MCP).

---

## 📊 Evaluation (12.13)

`Accuracy · Consistency · Relevance · Completeness · Hallucination · Format`
- **⭐ Measure over a dataset; track dimensions separately.**
- Dataset must include **edge, adversarial, unanswerable** cases.
- Methods: deterministic > rubric > LLM-judge (calibrate).

---

## 🧪 Testing (12.14)

- **Prompts are code** → unit + **regression (golden set)** + A/B + versioning.
- **⭐ Pin the model version** — catch silent provider drift.
- Gate changes; roll back to last-good.

---

## 🐛 Debugging (12.15)

| Symptom | Fix |
|---|---|
| Hallucination | "source only" + escape hatch |
| Wrong format | schema + example + validate + low temp |
| Inconsistent | lower temperature; add examples |
| Constraint ignored | move to system + end; align examples; validate |

**⭐ First move:** inspect the exact assembled prompt. **Fix the missing component, don't reword.**

---

## 🔒 Security (12.16)

- **⭐ Injection is structural** (instructions & data share one channel) — can't fully patch.
- Direct (user msg) vs indirect (retrieved/tool content).
- **⭐ Least privilege > clever wording**; trust separation; validate output; output DLP; isolate tenants.
- **Defense-in-depth** — assume some injection succeeds.

---

## ⚙️ Optimization (12.17)

- Move on the **quality ↔ cost ↔ latency** surface via evaluation.
- **⭐ Output length** = often biggest latency/cost lever.
- **Change one thing → measure → keep/revert.** Never trim safety directives.

---

## 🚀 Production (12.18)

- Prompt = **deployed artifact**: registry · version · env-pin · log · **monitor** · rollback · A/B.
- **⭐ Monitor quality, not just uptime; pin/record model version.**
- Rollback = re-pin last-good (seconds).

---

## 🎯 The 10 through-lines

1. Model does what's probable, not meant. 2. Reliability is measured over a dataset. 3. Separate instructions from data. 4. Structure forces reliability. 5. Show, don't just tell. 6. Context engineering = prompt engineering (→ RAG). 7. Tool calling = prompt engineering (→ agents). 8. Prompts are code. 9. Least privilege > clever wording. 10. Optimize on the quality↔cost↔latency surface.

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 12](../README.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
| 🏋️ Exercises | [Exercises](../exercises/README.md) |
| 🎴 Flashcards | [Deck](../flashcards/deck.md) |
