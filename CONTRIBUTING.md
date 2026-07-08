# Contributing & Style Guide

> This handbook should read like a **single-author published book**, even as it grows. This guide keeps every page consistent, professional, and maintainable.

---

## Golden rules

> [!IMPORTANT]
> 1. **First principles over shortcuts.** Explain *why* before *how*.
> 2. **Consistency over cleverness.** Follow the templates even when you could improvise.
> 3. **Never renumber published modules or lessons.** Append; don't reshuffle.
> 4. **Show, then generalize.** Concrete example first, abstraction second.
> 5. **Every claim is verifiable.** Prefer runnable code and cited sources.

---

## Voice & tone

| Do | Don't |
|---|---|
| Write clearly and directly | Pad with filler or hype |
| Assume a smart developer who knows Python | Re-teach basic syntax |
| Define jargon on first use (link to [GLOSSARY.md](GLOSSARY.md)) | Assume the reader knows ML acronyms |
| Use "we" and "you" naturally | Be stiff or overly academic |
| Prefer tables and diagrams | Write walls of text |

---

## Markdown standards

- **Headings**: one `#` H1 per file (the title); use `##`/`###` below it.
- **Tables** over long prose lists wherever data is comparable.
- **Callouts** using GitHub alert syntax:

```markdown
> [!NOTE]      general information
> [!TIP]       best practice / shortcut
> [!IMPORTANT] must-know
> [!WARNING]   easy-to-make mistake
> [!CAUTION]   dangerous / destructive
```

- **Mermaid** for diagrams whenever they aid understanding:

````markdown
```mermaid
flowchart LR
    A --> B
```
````

- **Code blocks** always specify a language for highlighting.
- **Image placeholders** use this exact pattern until the asset exists:

```markdown
![Descriptive Alt Text](assets/images/topic-name.png)

> **Illustration placeholder** — describe what the image should show.
```

- **Internal links** use relative paths so they work on GitHub.

---

## Lesson structure

Every lesson MUST follow the section order defined in [CURRICULUM.md](CURRICULUM.md#lesson-anatomy) and use [templates/lesson-template.md](templates/lesson-template.md). This is non-negotiable — it's what makes the book feel unified.

---

## File & naming conventions

| Item | Convention | Example |
|---|---|---|
| Module folder | `NN-slug` | `05-nlp-transformer` |
| Lesson file | `NN.M-slug.md` | `05.4-attention.md` |
| Image | `topic-descriptor.png` | `attention-heads.png` |
| Exercise set | `exercises/NN-slug/` | `exercises/05-nlp-transformer/` |
| Flashcard deck | `flashcards/NN-slug.md` | `flashcards/05-nlp-transformer.md` |

See [REPOSITORY_STRUCTURE.md](REPOSITORY_STRUCTURE.md) for the full map.

---

## Adding a new lesson — checklist

- [ ] Create the lesson from [templates/lesson-template.md](templates/lesson-template.md)
- [ ] Fill every required section (no empty headings)
- [ ] Add at least one diagram or a justified note that none is needed
- [ ] Add exercises, a quiz, and flashcards
- [ ] Add any new terms to the glossary
- [ ] Link prerequisites and further reading
- [ ] Update [CURRICULUM.md](CURRICULUM.md) if outcomes changed
- [ ] Add an entry to [CHANGELOG.md](CHANGELOG.md)
- [ ] Update [PROGRESS_TRACKER.md](PROGRESS_TRACKER.md) if the structure changed

---

## Code standards

- Python **3.11+**, type-hinted, formatted with a consistent formatter (e.g. `ruff`/`black`).
- Examples must be **minimal and runnable** — no hidden dependencies.
- Prefer clarity over cleverness; comment the *why*, not the *what*.
- Pin versions in project `requirements`/`pyproject` files.

---

## Commit & PR conventions

- Commit messages: imperative mood, scoped — e.g. `docs(m05): add attention lesson`.
- One logical change per PR where practical.
- CI (link checks / lint) should pass before merge — see `.github/workflows/`.
