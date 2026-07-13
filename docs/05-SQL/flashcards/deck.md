# Flashcards · Module 05 — Databases & Data Engineering

[🏠 Module](../README.md) · [📚 Lessons](../weeks/README.md)

> Active-recall deck for the whole module. Answer **out loud before flipping**. Review on the [spaced-repetition schedule](../../../LEARNING_STRATEGY.md): same day, +1d, +3d, +7d, +16d, +35d. A failed card resets to interval 1.

---

## 05.1 · Introduction
**Q:** Name five things a database gives you that a plain file doesn't.
**A:** Safe concurrency, fast indexed queries (not O(n) scans), durability (ACID), schema enforcement, and declarative queryability (plus access control).

**Q:** The standard AI storage pattern for documents?
**A:** Raw object in object storage, metadata in a relational DB, embedding in a vector DB — the backbone of RAG systems.

---

## 05.2 · Relational
**Q:** The organizing principle of relational design?
**A:** Each fact stored exactly once — duplication causes copies to drift out of sync.

**Q:** How do you model many-to-many?
**A:** A third "join table" holding FKs to both sides (usually with a composite primary key).

**Q:** State 3NF informally.
**A:** Every non-key column depends on "the key, the whole key, and nothing but the key."

---

## 05.3 · SQL Fundamentals
**Q:** `WHERE` vs `HAVING`?
**A:** `WHERE` filters rows *before* grouping; `HAVING` filters groups *after* aggregation (aggregates only work in HAVING).

**Q:** INNER vs LEFT JOIN?
**A:** INNER returns only rows matching in both tables (silently dropping unmatched rows); LEFT keeps all left rows with NULLs where there's no match.

**Q:** Why does `WHERE col = NULL` return nothing?
**A:** NULL means *unknown*; comparisons with NULL yield UNKNOWN, not TRUE — use `IS NULL`.

**Q:** How do you prevent SQL injection?
**A:** Always use parameterized queries (placeholders) — never string interpolation, especially with user or LLM-supplied values.

---

## 05.4 · Advanced SQL
**Q:** What do window functions do that GROUP BY doesn't?
**A:** Compute a value per row over a window of related rows *without collapsing the rows* — ranking, running totals, prev/next comparisons.

**Q:** How do you get the top 3 per group?
**A:** `ROW_NUMBER() OVER (PARTITION BY group ORDER BY score DESC)` in a CTE, then filter `WHERE rn <= 3`.

**Q:** View vs materialized view?
**A:** A view stores only the query (always fresh, no speedup); a materialized view stores the precomputed result (fast, but stale until refreshed) — a cache inside the DB.

---

## 05.5 · Query Optimization
**Q:** The red flag in an `EXPLAIN ANALYZE` output?
**A:** A `Seq Scan` on a large table (and/or a huge "Rows Removed by Filter") where you expected an index.

**Q:** State the leftmost-prefix rule.
**A:** A composite index on `(a,b,c)` serves filters on `a`, `(a,b)`, or `(a,b,c)` — not `b` or `c` alone; put the equality column first.

**Q:** What is a covering index?
**A:** One containing all columns the query needs, so it's answered entirely from the index (Index Only Scan) — which is why `SELECT *` hurts.

**Q:** What is the N+1 query problem?
**A:** App code issuing one query per row (101 queries for 100 users) instead of a single JOIN/`IN` query — no index fixes it.

---

## 05.6 · Transactions
**Q:** What does ACID guarantee?
**A:** Atomicity (all-or-nothing), Consistency (constraints hold), Isolation (concurrent txns don't corrupt each other), Durability (committed data survives crashes).

**Q:** What is a lost update, and how do you prevent it?
**A:** Two transactions read-modify-write the same value and one overwrites the other; prevent with an atomic DB update (`SET x = x - n`), `SELECT ... FOR UPDATE`, or SERIALIZABLE + retry.

**Q:** What is MVCC's key benefit?
**A:** Multiple row versions mean readers don't block writers (each transaction reads a consistent snapshot) — but dead versions need VACUUM.

**Q:** Why never call an LLM API inside a transaction?
**A:** The transaction holds locks for the entire slow call, blocking writers and exhausting the connection pool.

---

## 05.7 · NoSQL
**Q:** What do you trade away when adopting NoSQL?
**A:** Typically JOINs, full ACID, ad-hoc query flexibility, and schema enforcement — in exchange for scale, speed, or flexibility.

**Q:** What is Redis used for in AI systems?
**A:** Caching (prompts, embeddings, retrieval results), rate limiting (atomic INCR), and job queues — a complement to Postgres, not a source of truth.

**Q:** What is the CAP theorem?
**A:** During a network partition you must choose consistency (reject requests) or availability (serve possibly-stale data).

---

## 05.8 · Data Modeling
**Q:** OLTP vs OLAP modeling?
**A:** OLTP is normalized (integrity, small writes) for apps; OLAP is denormalized (star schema, fast aggregations) for analytics.

**Q:** Why are star-schema dimensions denormalized?
**A:** Dimensions are tiny vs fact tables, so redundancy costs little — and it saves a JOIN on every analytical query.

**Q:** What is point-in-time correctness?
**A:** Features must reflect what was known *at event time*; joining current values to historical facts leaks future information (data leakage).

---

## 05.9 · Warehouses & Lakes
**Q:** Why is columnar storage fast for analytics?
**A:** It stores each column together, so an aggregation reads only the needed column (10–100× less I/O) and compresses far better.

**Q:** What is a data swamp?
**A:** A lake without governance (no catalog/schema/ownership) — nobody knows what the data is or whether it's trustworthy.

**Q:** What is a lakehouse?
**A:** Warehouse features (ACID, schema, time travel via Delta/Iceberg) on cheap lake storage — the ML default.

---

## 05.10 · ETL & ELT
**Q:** Why did ELT win over ETL?
**A:** Cloud-warehouse compute is cheap/elastic, and keeping raw data lets you fix a transform bug and re-run without re-extracting.

**Q:** What is idempotency and why is it non-negotiable?
**A:** Running an operation twice has the same effect as once — retries/backfills inevitably re-run tasks, and a non-idempotent pipeline duplicates data.

**Q:** Two workhorse idempotency patterns?
**A:** Upsert on a stable key (`ON CONFLICT DO UPDATE`), or delete-then-insert the whole partition being rebuilt.

---

## 05.11 · Data Pipelines
**Q:** The defining danger of data pipelines?
**A:** Silent failure — corrupt data doesn't crash anything; it produces plausible but wrong numbers and quietly degrades models.

**Q:** Why is the bronze/raw layer immutable?
**A:** So you can re-derive downstream layers after fixing a transform bug, without re-extracting from a source that may have changed.

**Q:** The two highest-value pipeline alerts?
**A:** Freshness (table not updated within SLA) and volume (row count far off the recent average).

**Q:** What is data lineage used for?
**A:** Debugging backwards (where did this number come from?) and blast radius forwards (which models used this corrupt table?), plus GDPR.

---

## 05.12 · AI Data Workflows
**Q:** What is data leakage and why is it so dangerous?
**A:** Information unavailable at prediction time entering training — dangerous because it *looks like success* (great offline scores) then fails in production.

**Q:** The diagnostic question for leakage?
**A:** "At prediction time, would this value actually be available, with this value?" (Leakage is usually a time-unaware JOIN.)

**Q:** What is training/serving skew and its fix?
**A:** Features computed differently at training vs serving (two diverging code paths); fix with one feature definition used by both (a feature store).

**Q:** Why do models decay with no code change?
**A:** Data/concept drift — the real-world distribution or input→output relationship changes, so the training distribution no longer matches reality.

---

## 05.13 · Security
**Q:** The three controls preventing most database breaches?
**A:** Never expose the DB to the internet, least-privilege credentials (app can't DROP TABLE), and parameterized queries.

**Q:** What is Row-Level Security, and what bug class does it eliminate?
**A:** Policies that auto-filter every query (e.g., by tenant_id) — eliminating the catastrophic "forgot the WHERE tenant_id" cross-tenant leak.

**Q:** Why is an untested backup not a backup?
**A:** Teams routinely discover backups are broken only when they need them — schedule regular restore drills.

**Q:** How do you safely let an LLM agent query your database?
**A:** Read-only role on restricted views, allowlist/validate the SQL (no DDL/DML), statement timeouts and row limits, and RLS so retrieval respects the end user's permissions.

---

## 05.14 · Performance & Scaling
**Q:** State the scaling ladder in order.
**A:** Indexes → caching → connection pooling → scale up → read replicas → partitioning → sharding (last resort).

**Q:** Why is connection pooling mandatory?
**A:** Postgres forks a process per connection; without a pool, an async/serverless app exhausts `max_connections` and takes the DB down.

**Q:** What bug does replication lag cause?
**A:** "Read-your-own-write" — a user writes to the primary, reads from a lagging replica, and sees stale data.

**Q:** Partitioning vs sharding?
**A:** Partitioning splits a table within one DB (keeps JOINs/transactions, enables pruning and instant retention); sharding splits across machines (scales writes but breaks cross-shard JOINs/transactions).

---

## 05.15 · Vector Databases
**Q:** What is an embedding?
**A:** A dense vector positioned so semantically similar text lands nearby — turning meaning into geometry.

**Q:** Why can't SQL do semantic search?
**A:** SQL matches exact values/patterns, so `LIKE '%refund%'` misses "money-back guarantee" — meaning isn't a string match.

**Q:** What is ANN and its trade-off?
**A:** Approximate Nearest Neighbor — accepts ~99% recall for roughly a 1000× speedup over exhaustive O(N·d) comparison. HNSW (the dominant index) is a graph traversed greedily.

**Q:** The #1 security bug in RAG retrieval?
**A:** Retrieval that ignores the user's permissions — returning another tenant's confidential chunks into the LLM's context.

---

> [!TIP]
> When you can answer every card AND design the full data architecture for a RAG product, Module 05 is locked in.
