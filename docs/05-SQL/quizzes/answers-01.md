# Answers · Module 05 Quiz 01

[🏠 Module](../README.md) · [❓ Questions](quiz-01.md)

> Model answers with the *why*. If you got the gist but not the reasoning, reread the linked lesson — and run the query.

---

### Part 1 — Foundations & SQL

**1.** Safe **concurrency** (many readers/writers), **indexed speed** (O(log n), not O(n) scans), **durability** (ACID, survives crashes), **structure** (schema + constraints), and **queryability** (declarative SQL) — plus access control. → [05.1](../weeks/05.1-introduction.md)

**2.** Structured → relational DB; semi-structured (JSON/logs) → document DB or Postgres `JSONB`; unstructured (text/images/audio) → object storage, with metadata in a DB and embeddings in a vector DB. → [05.1](../weeks/05.1-introduction.md)

**3.** **Each fact is stored exactly once, in exactly one place** (duplication causes copies to drift). 3NF informally: every non-key column depends on "the key, the whole key, and nothing but the key." → [05.2](../weeks/05.2-relational-databases.md)

**4.** With a third **join table** holding foreign keys to both sides (typically with a composite primary key preventing duplicate links). → [05.2](../weeks/05.2-relational-databases.md)

**5.** `WHERE` filters individual **rows** *before* grouping; `HAVING` filters **groups** *after* aggregation (aggregates like `COUNT(*)` can only be used in HAVING). → [05.3](../weeks/05.3-sql-fundamentals.md)

**6.** **INNER** silently drops rows without a match (e.g., users with zero documents disappear). Anti-join: `LEFT JOIN b ON ... WHERE b.id IS NULL`. → [05.3](../weeks/05.3-sql-fundamentals.md)

**7.** NULL means *unknown*; any comparison with NULL yields UNKNOWN (three-valued logic), which `WHERE` treats as not-matching — use `IS NULL`. → [05.3](../weeks/05.3-sql-fundamentals.md)

**8.** FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT. → [05.3](../weeks/05.3-sql-fundamentals.md)

**9.** Window functions compute a value **per row** over a window of related rows *without collapsing rows* (ranking, running totals, LAG/LEAD). Top-3 per group: `ROW_NUMBER() OVER (PARTITION BY g ORDER BY score DESC)` in a CTE, then `WHERE rn <= 3`. → [05.4](../weeks/05.4-advanced-sql.md)

**10.** A **view** stores only the query (always fresh, no speedup — good for abstraction/security); a **materialized view** stores the precomputed *result* (fast reads, stale until refreshed — a cache inside the DB). → [05.4](../weeks/05.4-advanced-sql.md)

### Part 2 — Optimization & Transactions

**11.** Red flag: a **`Seq Scan` on a large table** (and/or a huge "Rows Removed by Filter") where you expected an index. An index (B-tree) turns an O(n) full scan into an O(log n) lookup. → [05.5](../weeks/05.5-query-optimization.md)

**12.** A composite index on `(a,b,c)` serves filters on `a`, `(a,b)`, or `(a,b,c)` — **not** `b` or `c` alone (it's sorted by `a` first). Put the **equality** column first, the range/sort column second. → [05.5](../weeks/05.5-query-optimization.md)

**13.** A covering index contains all columns the query needs, so it's answered entirely from the index (**Index Only Scan**) without touching the table. `SELECT *` requires columns not in the index, forcing a table lookup. → [05.5](../weeks/05.5-query-optimization.md)

**14.** Application code issuing one query per row (fetch 100 users, then 100 more queries for their documents = 101 round-trips) instead of a single JOIN/`IN` query. No index fixes it — it's an app-side bug (often from ORM lazy loading). → [05.5](../weeks/05.5-query-optimization.md)

**15.** **Atomicity** (all-or-nothing), **Consistency** (constraints hold), **Isolation** (concurrent transactions don't corrupt each other), **Durability** (committed data survives crashes, via the WAL). → [05.6](../weeks/05.6-transactions.md)

**16.** Two transactions read the same value, both modify it, and one overwrites the other (permitted under Read Committed, Postgres's default). Fixes: **(a)** do the arithmetic atomically in the DB (`UPDATE ... SET credits = credits - 10 WHERE credits >= 10`), or **(b)** lock the row (`SELECT ... FOR UPDATE`) / use SERIALIZABLE and retry. → [05.6](../weeks/05.6-transactions.md)

**17.** **MVCC** keeps multiple row versions so each transaction reads a consistent snapshot — readers don't block writers (needs VACUUM to clean dead versions). **Deadlocks**: prevent by acquiring locks in a consistent order (e.g., ascending id), keeping transactions short, and retrying when the DB aborts one. → [05.6](../weeks/05.6-transactions.md)

**18.** The transaction holds its locks for the *entire duration* of the slow, unpredictable network call — blocking other writers, exhausting the connection pool, and inviting timeouts. Do the external work first, then open a short transaction to write the result. → [05.6](../weeks/05.6-transactions.md)

### Part 3 — NoSQL, Modeling, Warehouses

**19.** You typically trade away JOINs, full ACID, ad-hoc query flexibility, and schema enforcement — for scale, speed, or flexibility. The pragmatic AI stack: **Postgres** (source of truth) + **Redis** (cache/queue) + **object storage** (files/models) + **pgvector/vector DB** (embeddings). → [05.7](../weeks/05.7-nosql.md)

**20.** In a distributed system, during a **network partition** you must choose **consistency** (reject requests) or **availability** (serve possibly-stale data) — you can't have both. "Eventual consistency" means reads may be stale. → [05.7](../weeks/05.7-nosql.md)

**21.** OLTP is **normalized** (integrity, fast small writes) for applications; OLAP is **denormalized** (star schema, fast aggregations) for analytics. Star dimensions are denormalized because they're tiny compared to fact tables — the redundancy costs little and saves a JOIN on every query. → [05.8](../weeks/05.8-data-modeling.md)

**22.** **SCD Type 2**: instead of overwriting a changed dimension attribute, insert a new row with `valid_from`/`valid_to`, preserving history. **Point-in-time correctness**: join features as they were *at event time* — joining *current* values to historical facts leaks future information (data leakage). → [05.8](../weeks/05.8-data-modeling.md)

**23.** It stores each **column** contiguously, so an aggregation reads only the needed column (skipping all other fields) — often 10–100× less I/O — and similar adjacent values compress far better. → [05.9](../weeks/05.9-warehouses-lakes.md)

**24.** **Warehouse** = structured, modeled, governed, fast SQL (schema-on-write). **Lake** = raw data in any format in cheap object storage (schema-on-read) — ideal for AI's unstructured data. **Lakehouse** = warehouse features (ACID, schema, time travel via Delta/Iceberg) on lake storage. A **data swamp** is a lake without governance — nobody knows what the data is or whether it's trustworthy. → [05.9](../weeks/05.9-warehouses-lakes.md)

### Part 4 — Pipelines, AI Data, Security, Scaling, Vectors

**25.** ELT won because cloud-warehouse compute is cheap and elastic, and **keeping the raw data** means a transform bug is fixed by re-running SQL (no re-extraction). **Idempotency** = running an operation twice has the same effect as once; it's non-negotiable because retries and backfills inevitably re-run tasks, and a non-idempotent pipeline duplicates data (silently biasing models — and in AI, re-embedding costs real money). → [05.10](../weeks/05.10-etl-elt.md)

**26.** **Silent failure** — corrupt data doesn't crash anything; it produces plausible but wrong numbers and quietly degrades models. The two highest-value alerts: **freshness** (table not updated within its SLA) and **volume** (row count far off the recent average). → [05.11](../weeks/05.11-data-pipelines.md)

**27.** **Leakage**: information unavailable at prediction time entering training — dangerous because it *looks like success*. Diagnostic: *"at prediction time, would this value actually be available, with this value?"* (Usually a time-unaware JOIN.) **Skew**: features computed differently at training vs serving (two diverging code paths) — fix with one definition used by both. **Drift**: the real-world distribution changes, so models decay with no code change — monitor input distributions and retrain. → [05.12](../weeks/05.12-ai-data-workflows.md)

**28.** (1) Never expose the DB to the internet (private network + firewall), (2) least-privilege credentials (the app can't `DROP TABLE`), (3) parameterized queries (no injection). **RLS** applies a policy that automatically filters every query (e.g., `tenant_id = current_setting(...)`), eliminating the catastrophic "forgot the `WHERE tenant_id`" cross-tenant leak. → [05.13](../weeks/05.13-database-security.md)

**29.** Indexes/query optimization → caching → connection pooling → scale up → read replicas → partitioning → **sharding**. Sharding is last because it fragments the data model: no cross-shard JOINs or transactions, the app must route every query, rebalancing is risky, and a bad shard key is nearly irreversible. Most teams that shard should have added an index. → [05.14](../weeks/05.14-performance-scaling.md)

**30.** An **embedding** is a dense vector positioned so semantically similar text lands nearby (meaning as geometry). **ANN** (Approximate Nearest Neighbor, e.g. HNSW — a graph traversed greedily) accepts ~99% recall for roughly a 1000× speedup over exhaustive O(N·d) comparison. The **#1 RAG security bug**: retrieval that ignores the user's permissions, returning another tenant's confidential chunks into the LLM's context. → [05.15](../weeks/05.15-vector-databases.md)

---

> [!TIP]
> Turn every missed question into a flashcard. For the debugging ones (lost update, leakage, RLS bypass), *reproduce the bug and fix it* on a real database — those instincts are what protect production AI systems.
