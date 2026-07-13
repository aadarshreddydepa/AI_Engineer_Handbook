# Quiz · Module 05 — Databases & Data Engineering

[🏠 Module](../README.md) · [📚 Lessons](../weeks/README.md) · [✅ Answers](answers-01.md)

> 30 questions across all 15 concept lessons. Answer from memory first, then check [answers-01.md](answers-01.md). Scoring at the bottom.

---

### Part 1 — Foundations & SQL (05.1–05.4)
1. Name five things a database gives you that a plain file doesn't.
2. Where do structured, semi-structured, and unstructured data belong in an AI system?
3. State the organizing principle of relational design, and what 3NF means informally.
4. How do you model a many-to-many relationship?
5. `WHERE` vs `HAVING` — what does each filter, and when?
6. INNER vs LEFT JOIN — which silently drops rows, and how do you write an anti-join?
7. Why does `WHERE col = NULL` return nothing?
8. What is SQL's logical execution order?
9. What do window functions do that `GROUP BY` doesn't? How do you get top-3 per group?
10. View vs materialized view?

### Part 2 — Optimization & Transactions (05.5–05.6)
11. What's the red flag in an `EXPLAIN ANALYZE` plan, and what does an index give you?
12. State the leftmost-prefix rule for composite indexes.
13. What is a covering index, and why does `SELECT *` prevent it?
14. What is the N+1 query problem?
15. What does ACID guarantee?
16. What is the lost update, and what are two correct fixes?
17. What is MVCC, and how do you prevent deadlocks?
18. Why must you never call an LLM API inside an open transaction?

### Part 3 — NoSQL, Modeling, Warehouses (05.7–05.9)
19. What do you trade away with NoSQL? What's the pragmatic AI database stack?
20. What is the CAP theorem?
21. OLTP vs OLAP modeling; why are star-schema dimensions denormalized?
22. What is SCD Type 2 and point-in-time correctness?
23. Why is columnar storage fast for analytics?
24. Warehouse vs lake vs lakehouse — and what is a "data swamp"?

### Part 4 — Pipelines, AI Data, Security, Scaling, Vectors (05.10–05.15)
25. Why did ELT win over ETL? What is idempotency and why is it non-negotiable?
26. What is the defining danger of data pipelines, and what are the two highest-value alerts?
27. Explain data leakage (with the diagnostic question), training/serving skew, and drift.
28. Name the three controls that prevent most database breaches, and explain Row-Level Security.
29. State the scaling ladder in order. Why is sharding a last resort?
30. What is an embedding, what is ANN, and what's the #1 security bug in RAG retrieval?

---

### Scoring

| Score | Meaning |
|---|---|
| 26–30 | Excellent — proceed to Module 06 |
| 21–25 | Good — review the missed lessons' summaries/flashcards |
| 15–20 | Reread the weaker lessons before continuing |
| < 15 | Rework the module — data systems underpin all AI work |

> [!TIP]
> Every missed question maps to a lesson. For SQL and debugging questions, *run the query* against a real database — this module is learned by doing.
