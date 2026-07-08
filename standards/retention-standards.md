# Memory Retention Standards

[🏠 Standards](README.md) · [🧠 Learning strategy](../LEARNING_STRATEGY.md)

> Reading is not learning. Every lesson must actively engineer retention. These are the required retention artifacts and how to build them well.

---

## Required in every lesson

| Artifact | Purpose | Lesson section |
|---|---|---|
| **One-page summary** | Reconstruct the lesson at a glance | §20 Summary |
| **Cheat sheet** | Fast reference during work | §21 Cheat Sheet |
| **Flashcards** | Active recall via spaced repetition | §22 Flashcards |
| **Teach-back exercise** | Explain it to solidify it | §23 / revision checklist |
| **Common misconceptions** | Pre-empt predictable errors | §14 |
| **Revision checklist** | Confirm mastery | end of lesson |

A lesson missing any of these is **incomplete** and cannot be merged.

---

## One-page summary

- Fits on one screen.
- A **table of key ideas → one-line takeaways**, not prose.
- Written so a reader who forgot everything could re-derive the gist.

## Cheat sheet

- Scannable, not teachable — assume the reader already learned it.
- Prefer a compact code/command block plus a small "gotchas" table.
- Longer, module-wide cheat sheets live in `docs/<module>/cheat-sheets/` and repo-wide ones in `assets/cheatsheets/`.

## Flashcards

Format (in `docs/<module>/flashcards/deck.md`):

```markdown
**Q:** What problem does the KV cache solve?
**A:** It avoids recomputing keys/values for past tokens, making autoregressive decoding roughly linear instead of quadratic in sequence length.
```

**Rules:**
- One idea per card — recallable in a single breath.
- Prefer "why" and "when" questions over pure definitions.
- Split anything needing a paragraph into multiple cards.

## Teach-back exercise

Every lesson ends with a prompt like:
> *"Explain `<concept>` to a peer in under 3 minutes without notes."*

Teaching back exposes gaps that rereading hides.

## Common misconceptions

Use the myth → reality pattern:

> [!WARNING]
> **Myth:** More parameters always means a better model.
> **Reality:** Beyond a point, data quality, alignment, and inference cost dominate — see scaling laws.

---

## Spaced repetition — built into the content

> [!IMPORTANT]
> Lessons must **explicitly reference earlier lessons** to force retrieval of prior material. This interleaving is a feature, not a digression.

Every lesson includes a **spaced-repetition callback** block:
> *"Recall [`gradient descent`](#) from Module 06 — attention training reuses it directly."*

Cadence (see [LEARNING_STRATEGY.md](../LEARNING_STRATEGY.md)):

| Review | Interval after learning |
|:--:|---|
| 1 | Same day |
| 2 | +1 day |
| 3 | +3 days |
| 4 | +7 days |
| 5 | +16 days |
| 6 | +35 days |

Milestone audits (Roadmap checkpoints A–D) re-test whole phases from memory.

---

## Revision checklist (ends every lesson)

- [ ] I can explain this on a blank page
- [ ] I did the exercises without looking
- [ ] I can teach it back in under 3 minutes
- [ ] Flashcards created and first review scheduled
- [ ] I connected it to a prior lesson

---

## Authoring checklist

- [ ] Summary is a table, fits one screen
- [ ] Cheat sheet is scannable
- [ ] ≥ 5 flashcards, one idea each, "why/when" biased
- [ ] Teach-back prompt present
- [ ] Misconceptions section present
- [ ] At least one spaced-repetition callback to an earlier lesson
