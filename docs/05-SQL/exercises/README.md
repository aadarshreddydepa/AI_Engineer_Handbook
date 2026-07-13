# Exercises · Module 05 — Databases & Data Engineering

[🏠 Module](../README.md) · [📚 Lessons](../weeks/README.md)

> A structured set spanning all 15 concept lessons — SQL, database design, query optimization, data modeling, and debugging — with a deliberate difficulty ramp per the [exercise standards](../../../standards/exercise-standards.md). **Run a real PostgreSQL** and execute every query.

**Difficulty:** ⭐ warm-up · ⭐⭐ practice · ⭐⭐⭐ challenge · ⭐⭐⭐⭐ stretch. **Types:** 💾 SQL · 🏗️ Design · ⚡ Optimization · 📐 Modeling · 🐞 Debug.

---

## 05.1 · Introduction
- [ ] **⭐ 💾** Run PostgreSQL (Docker); connect with `psql`; create a database.
- [ ] **⭐⭐ 🏗️** For 10 AI artifacts (PDFs, embeddings, model weights, users, evals, logs…), decide the storage type and justify.

## 05.2 · Relational
- [ ] **⭐ 💾** Create tables with PKs, FKs, and constraints; try to violate each and observe the rejection.
- [ ] **⭐⭐ 🏗️** Model documents ↔ tags (many-to-many) with a join table.
- [ ] **⭐⭐⭐ 📐** Normalize a denormalized orders table to 3NF; name the anomalies you eliminated.

## 05.3 · SQL Fundamentals
- [ ] **⭐⭐ 💾** Write INNER and LEFT JOINs of users↔documents; explain the row-count difference.
- [ ] **⭐⭐ 💾** Anti-join: find users with zero documents; documents with no tags.
- [ ] **⭐⭐ 💾** Compute a label distribution (`GROUP BY` + `HAVING > 100`).
- [ ] **⭐⭐⭐ 🐞** Wrap a `DELETE` in a transaction, verify the affected count, and `ROLLBACK`.
- [ ] **⭐⭐ 🐞** Demonstrate `= NULL` failing and `IS NULL` working; show NULLs skewing `AVG`.

## 05.4 · Advanced SQL
- [ ] **⭐⭐ 💾** Rewrite a nested-subquery query using CTEs; compare readability.
- [ ] **⭐⭐⭐ 💾** Per user: rank documents by score, compute the user's average and a running total (window functions).
- [ ] **⭐⭐⭐ 💾** Top-3 per category via `ROW_NUMBER()`.
- [ ] **⭐⭐ 💾** Use `LAG()` for metric deltas between consecutive evaluations.
- [ ] **⭐⭐⭐ 💾** Build an org chart with a self-referencing FK; traverse with `WITH RECURSIVE`.
- [ ] **⭐⭐ 🐞** Reproduce the `NOT IN` + NULL bug; fix with `NOT EXISTS`.

## 05.5 · Query Optimization
- [ ] **⭐⭐ ⚡** Load 1M rows; `EXPLAIN ANALYZE` a filtered query (seq scan); add an index; compare.
- [ ] **⭐⭐ ⚡** Show a composite index serving `(a)` and `(a,b)` but not `(b)` alone.
- [ ] **⭐⭐⭐ ⚡** Achieve an *Index Only Scan*; break it with `SELECT *`.
- [ ] **⭐⭐ 🐞** Show an index ignored due to `lower(col)`; fix with an expression index.
- [ ] **⭐⭐⭐ 🐞** Write N+1 query code; rewrite as one JOIN; measure the difference.

## 05.6 · Transactions
- [ ] **⭐⭐⭐ 🐞** In two `psql` sessions, reproduce a **lost update**; fix with an atomic `UPDATE`, then with `FOR UPDATE`.
- [ ] **⭐⭐⭐ 🐞** Trigger a **deadlock** with opposite lock orders; fix with consistent ordering.
- [ ] **⭐⭐ 💾** Demonstrate a non-repeatable read under Read Committed vs Repeatable Read.
- [ ] **⭐⭐⭐ 💾** Implement a job queue with `FOR UPDATE SKIP LOCKED`; two workers, no double-claims.

## 05.7 · NoSQL
- [ ] **⭐ 💾** Cache a simulated "expensive LLM call" in Redis with a TTL; measure hit vs miss.
- [ ] **⭐⭐ 💾** Store and query a nested document in a Postgres `JSONB` column with a GIN index.
- [ ] **⭐⭐ 💾** Implement rate limiting with Redis atomic `INCR` + TTL; prove it's race-free.

## 05.8 · Data Modeling
- [ ] **⭐ 📐** Draw an ER diagram (Mermaid) for an AI document-QA app.
- [ ] **⭐⭐ 📐** Design a star schema for LLM usage (fact + user/model/date dims); write the DDL.
- [ ] **⭐⭐ 💾** Build `dim_date`; aggregate by week and quarter.
- [ ] **⭐⭐⭐ 📐** Implement SCD Type 2 on a user dimension; join a past fact to the then-current plan.

## 05.9 · Warehouses & Lakes
- [ ] **⭐⭐ ⚡** Save a dataset as CSV and Parquet; compare size and single-column read time.
- [ ] **⭐⭐ 🏗️** For 5 scenarios, choose warehouse / lake / lakehouse / Postgres and justify.
- [ ] **⭐⭐ ⚡** Compute the cost of `SELECT *` vs 2 columns on a 5 TB table under a per-byte pricing model.

## 05.10 · ETL & ELT
- [ ] **⭐⭐ 🐞** Write a load that duplicates rows on re-run; fix it with an upsert; prove re-running is safe.
- [ ] **⭐⭐ 🏗️** Implement watermark-based incremental extraction; show the late-arriving-data bug and a lookback fix.
- [ ] **⭐⭐ 🏗️** Add schema/null/range/**volume** checks that quarantine a bad batch and alert.
- [ ] **⭐⭐⭐ 🏗️** Model a 5-task pipeline as a DAG; trigger a retry and a backfill.

## 05.11 · Data Pipelines
- [ ] **⭐⭐ 💾** Write SQL data tests (nulls, dupes, ranges, orphan FKs) that return zero rows when healthy.
- [ ] **⭐⭐ 🏗️** Implement freshness + volume monitoring; simulate a broken upstream feed and catch it.
- [ ] **⭐⭐⭐ 🏗️** Produce a lineage diagram; use it to answer "what's affected if source X was corrupt for 3 days?"
- [ ] **⭐⭐⭐ 🏗️** Build a content-hash-keyed embedding step; re-run it and show **zero** re-embedding cost.

## 05.12 · AI Data Workflows
- [ ] **⭐⭐⭐ 🐞** Deliberately create target and temporal **leakage**; show the inflated score; fix with point-in-time joins.
- [ ] **⭐⭐ 🐞** Implement a feature twice (SQL + Python), introduce a divergence, and detect the **skew**.
- [ ] **⭐⭐ 🐞** Show a random split with duplicates leaking; fix with entity/time-based splitting.
- [ ] **⭐⭐⭐ 🏗️** Simulate input **drift**; implement a distribution-comparison alert.

## 05.13 · Security
- [ ] **⭐ 💾** Create least-privilege roles; verify the app role cannot `DROP TABLE`.
- [ ] **⭐⭐⭐ 💾** Enable **RLS** for multi-tenancy; prove an unfiltered query can't see another tenant's rows.
- [ ] **⭐⭐ 🐞** Exploit a string-built query (sandbox); fix with parameterization.
- [ ] **⭐⭐ 🏗️** Back up, delete data, restore — then do a **PITR** to just before the deletion.
- [ ] **⭐⭐⭐ 🐞** Build a constrained text-to-SQL path (read-only role + allowlisted views + timeout); attempt a prompt injection and show it fails.

## 05.14 · Performance & Scaling
- [ ] **⭐ ⚡** Exhaust connections without pooling; add a pool and show stability.
- [ ] **⭐⭐ 🐞** Set up a read replica; reproduce the read-your-own-write bug; fix the routing.
- [ ] **⭐⭐⭐ ⚡** Partition a table by month; show pruning in `EXPLAIN`; drop an old partition vs a slow `DELETE`.
- [ ] **⭐⭐ ⚡** Add a tenant-scoped Redis cache; measure hit-rate and latency.

## 05.15 · Vector Databases
- [ ] **⭐⭐ 💾** Install `pgvector`; store embeddings; run a cosine-distance top-k query.
- [ ] **⭐⭐ 💾** Combine vector search with a SQL permission filter in one query.
- [ ] **⭐⭐ ⚡** Create an HNSW index; compare latency with/without it.
- [ ] **⭐⭐⭐ 🐞** Demonstrate the permission-bypass bug (global top-k leaking another tenant's chunk); fix with RLS/filtering.

## Projects
- [ ] Build **Project 6 (AI Dataset Pipeline)** — the flagship.
- [ ] Build at least two of Projects 1–5.

---

## Completion criteria

- [ ] Every ⭐/⭐⭐ exercise run against a real PostgreSQL
- [ ] At least five ⭐⭐⭐ challenges solved (incl. the lost update, leakage, and RLS)
- [ ] The AI Dataset Pipeline works and its tests prove idempotency + tenant isolation
- [ ] You can tick the [05.16 mastery checklist](../weeks/05.16-projects-summary.md#module-05-mastery-checklist-from-memory--on-a-real-database) from memory

> [!TIP]
> The 🐞 debugging exercises (lost update, leakage, deadlock, RLS bypass, N+1) build the most valuable instincts — these are the bugs that silently destroy real AI systems. Don't skip them for the easier SQL drills.
