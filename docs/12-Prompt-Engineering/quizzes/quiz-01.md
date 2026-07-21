# 📝 Module 12 · Prompt Engineering — Quiz 01

[🏠 Module 12](../README.md) · [📖 Lessons](../weeks/README.md) · [✅ Answers](answers-01.md)

> **40 questions across all 20 lessons.** Aim for an explanation, not just a phrase — the [answers](answers-01.md) grade reasoning. Target: **32/40** to consider the module solid.

---

## Part A · Foundations (12.1–12.5)

**1.** What is an LLM actually doing when it "follows" a prompt, and what does that imply for prompt design?

**2.** Why can't you judge a prompt's quality from a single output?

**3.** What are the three message roles, and how does the system message differ in practice from the user message?

**4.** List the eight components of a reliable prompt. Why is "a weak prompt is usually a missing component" a useful heuristic?

**5.** What's the "describable vs demonstrable" heuristic for choosing a prompting pattern?

**6.** Why is separating instructions from data the single most important structural move? How does it help security?

**7.** What is a delimiter-collision attack, and how do you prevent it?

**8.** Why are few-shot examples an "executable specification"? What happens if one is wrong?

**9.** When instructions and examples conflict, which tends to win, and what should you do about it?

## Part B · Controlling output & flow (12.6–12.10)

**10.** Why are structured outputs the backbone of production LLM systems?

**11.** Describe the specify→generate→validate→repair pattern for structured output.

**12.** Why is "valid JSON" not the same as "safe JSON"?

**13.** How should you design the *output* of a reasoning workflow, and why not expose raw chain-of-thought?

**14.** Why can more reasoning produce a confident wrong answer, and how do you defend against it?

**15.** Why does prompt chaining improve reliability — and what makes a chain fail to?

**16.** What glues chain steps together, and why?

**17.** Why should a reused prompt be a versioned template rather than an inline string?

**18.** Why should the model/temperature config be versioned with the prompt text?

**19.** What is the universal hallucination guard across tasks, and how does it look for extraction vs summarization?

## Part C · Interfaces (12.11–12.12)

**20.** Distinguish prompt engineering from context engineering. Give an example of each failing.

**21.** Why does adding more context often *reduce* answer quality?

**22.** Explain lost-in-the-middle and how you design around it.

**23.** How is RAG a scaled form of context engineering?

**24.** Walk through the tool-calling loop. What does the model do vs your code?

**25.** Why is a tool's schema effectively its prompt?

**26.** Why must tool arguments be validated, and what's the strongest defense if the model is hijacked?

**27.** How can tool results introduce prompt injection?

## Part D · Evaluate & operate (12.13–12.18)

**28.** Why is prompt evaluation fundamentally a dataset problem, and why track dimensions separately?

**29.** Name the six evaluation dimensions. Why include unanswerable cases?

**30.** What is a golden dataset, and how does regression testing use it?

**31.** Why must you pin and monitor the model version?

**32.** Describe the systematic prompt-debugging framework. Why is the cause rarely a "model flaw"?

**33.** Why is prompt injection structural rather than a fixable bug?

**34.** Why is least privilege the strongest defense against injection, and how do you apply it?

**35.** What does prompt optimization optimize, and why is evaluation essential?

**36.** Why is output length often the biggest latency/cost lever?

**37.** Why should a prompt edit be treated as a production deployment?

**38.** What is a prompt registry, and how do rollback and canary A/B make changes safe?

## Part E · Python & synthesis (12.19–12.20)

**39.** What five reusable Python components form a prompt-engineering toolkit, and what does each do?

**40.** Defend the claim "a prompt is a specification for a probabilistic machine," and give the five-part definition of prompt engineering.

---

## Navigation

| Direction | Link |
|---|---|
| 🏠 Module | [Module 12](../README.md) |
| ✅ Answers | [answers-01.md](answers-01.md) |
| 📖 Lessons | [Lesson index](../weeks/README.md) |
